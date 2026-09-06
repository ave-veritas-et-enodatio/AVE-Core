#!/usr/bin/env python3
r"""Audit staleness of manuscript .tex against the KB truth-source.

The KB is the truth source (standing G-ruling). A .tex is STALE when it cites KB
content that has since moved, been demoted, or been rewritten. This tool measures
five mechanical signals; it adjudicates nothing and edits nothing.

  S1 DEAD-PATH    a \kbleaf{...} / inline ave-kb path that does not resolve
  S2 DEAD-ID      a clm-/def-/ilk-/exp-/sup- id in .tex that is not in claims.jsonl
  S3 GRADE-DRIFT  .tex cites an id whose KB record is do-not-build / refuted /
                  ambiguous / proposed -- i.e. printed text leaning on a claim the
                  KB does not license building on
  S4 TIME-LAG     the cited KB leaf's last commit is NEWER than the citing .tex's
                  last commit: the print cannot reflect the leaf's current content
  S5 LINE-DRIFT   a :NNN line anchor that is now out of range, or whose leaf changed
                  after the .tex (the anchor may point at different bytes)

Exit 0 always: this is a measurement, not a gate.
"""
import json, os, re, subprocess, sys, collections

ROOT = subprocess.run(['git','rev-parse','--show-toplevel'],capture_output=True,text=True).stdout.strip()
os.chdir(ROOT)

KB_PREFIX = 'manuscript/ave-kb/'
CLAIMS = KB_PREFIX + '.index/claims.jsonl'

ID_RE   = re.compile(r'\b((?:clm|def|ilk|exp|sup)-[a-z0-9]{6})\b')
# an ave-kb path, with or without a manuscript/ prefix, inside \kbleaf{} or bare
PATH_RE = re.compile(r'(?:manuscript/)?(ave-kb/[A-Za-z0-9_./-]+\.md)')
# a :NNN anchor appearing within ~200 chars after a path on the same line
ANCH_RE = re.compile(r':(\d{1,5})\b')

def sh(args):
    return subprocess.run(args,capture_output=True,text=True).stdout.strip()

def last_commit_epoch(path, cache={}):
    if path in cache: return cache[path]
    out = sh(['git','log','-1','--format=%ct','--',path])
    cache[path] = int(out) if out else 0
    return cache[path]


# Markers that make a KB change MATERIAL to printed text: a walk-back, a
# demotion, a retraction, a scope fence, or a changed grade. A leaf that only
# gained a typo fix or a link repair after the .tex is not staleness.
MATERIAL_RE = re.compile(
    r'RETRACT|DEMOT|WALK-?BACK|SUPERSED|STRUCK|STRIKE|CORRECTED|REFUTED|'
    r'do-not-build|NOT\s+RE-?RATIFIED|scope-correct|VACATED|DEPRECAT|'
    r'\U0001F534|solidity|build_band|build-band',
    re.IGNORECASE)

def leaf_delta_kind(leaf, tex, cache={}):
    """Classify what changed in `leaf` since `tex` was last committed.

    Returns a short reason string when the diff carries a walk-back/grade marker,
    else '' (cosmetic). Only ADDED lines are inspected: what the leaf says now.
    """
    key = (leaf, tex)
    if key in cache: return cache[key]
    since = sh(['git','log','-1','--format=%H','--',tex])
    if not since:
        cache[key] = ''; return ''
    diff = sh(['git','diff','--unified=0',since+'..HEAD','--',leaf])
    hits = []
    for ln in diff.splitlines():
        if not ln.startswith('+') or ln.startswith('+++'):
            continue
        m = MATERIAL_RE.search(ln)
        if m:
            tok = m.group(0)
            if tok not in hits: hits.append(tok)
        if len(hits) >= 4: break
    cache[key] = ('added: ' + ', '.join(hits)) if hits else ''
    return cache[key]


# A .tex site is DISCLOSED when a demotion / scope / walk-back banner sits near
# the cite. Rule 12 keeps the demoted body and adds a dated banner, so a cite to
# a do-not-build claim under such a banner is HONEST, not a violation.
DISCLOSE_RE = re.compile(
    r'DEMOT|RETRACT|WALK-?BACK|SUPERSED|Scope demotion|scope-correct|STRUCK|'
    r'do not build|do-not-build|not an independent|NOT a prediction|preserved per Rule 12|'
    r'\U0001F534|caveat|UNVALIDATED|OPEN PROBLEM|illustrative|coarse-correctness|not an? (?:atomic-precision|independent|prediction)|truth-source card|solidity|not a validation|single-case|indicative only',
    re.IGNORECASE)

def disclosed_near(lines, n, window=15):
    lo = max(0, n-1-window); hi = min(len(lines), n-1+window+1)
    for ln in lines[lo:hi]:
        if DISCLOSE_RE.search(ln):
            return True
    return False

def main():
    claims = {}
    with open(CLAIMS) as fh:
        for line in fh:
            if not line.strip(): continue
            d = json.loads(line)
            claims[d['id']] = d

    tex_files = sh(['git','ls-files','manuscript/*.tex','manuscript/**/*.tex']).splitlines()
    # tool test fixtures are deliberate negative cases, not corpus staleness
    tex_files = [t for t in tex_files
                 if t.endswith('.tex') and '/tools/tests/' not in t]

    findings = collections.defaultdict(list)
    per_file = collections.Counter()

    for tex in tex_files:
        tex_epoch = last_commit_epoch(tex)
        try:
            lines = open(tex, encoding='utf-8', errors='replace').read().splitlines()
        except OSError:
            continue
        for n, line in enumerate(lines, 1):
            if line.lstrip().startswith('%'):
                continue  # LaTeX comment: not printed
            for m in PATH_RE.finditer(line):
                rel = m.group(1)
                full = 'manuscript/' + rel
                if not os.path.exists(full):
                    findings['S1_DEAD_PATH'].append((tex,n,rel,'path does not resolve'))
                    per_file[tex]+=1
                    continue
                leaf_epoch = last_commit_epoch(full)
                if leaf_epoch > tex_epoch:
                    days = (leaf_epoch - tex_epoch)/86400.0
                    kind = leaf_delta_kind(full, tex)
                    bucket = 'S4a_TIME_LAG_MATERIAL' if kind else 'S4b_TIME_LAG_COSMETIC'
                    why = 'leaf newer by %.0f d%s' % (days, (' -- ' + kind) if kind else '')
                    findings[bucket].append((tex,n,rel,why))
                    per_file[tex]+=1
                tail = line[m.end():m.end()+200]
                for a in ANCH_RE.finditer(tail):
                    ln = int(a.group(1))
                    try:
                        total = sum(1 for _ in open(full,encoding='utf-8',errors='replace'))
                    except OSError:
                        continue
                    if ln > total:
                        findings['S5_LINE_DRIFT'].append(
                            (tex,n,'%s:%d'%(rel,ln),'out of range (leaf has %d lines)'%total))
                        per_file[tex]+=1
                    elif leaf_epoch > tex_epoch:
                        findings['S5_LINE_DRIFT'].append(
                            (tex,n,'%s:%d'%(rel,ln),'anchor unverified: leaf changed after this .tex'))
                        per_file[tex]+=1
                    break  # first anchor after the path only
            for m in ID_RE.finditer(line):
                cid = m.group(1)
                rec = claims.get(cid)
                if rec is None:
                    if cid.endswith('xxxxxx'):
                        continue  # documented placeholder token, not a cite
                    findings['S2_DEAD_ID'].append((tex,n,cid,'not in claims.jsonl'))
                    per_file[tex]+=1
                    continue
                band = rec.get('build_band'); status = rec.get('status')
                sol  = rec.get('solidity')
                # S3a is the real signal: printed text leaning on a claim the KB
                # says not to build on. S3b is informational only -- every ilk-
                # node is 'proposed' and 'ambiguous' is a legitimate
                # disambiguation-node status, so neither is drift by itself.
                if band in ('do-not-build','refuted'):
                    why = 'build_band=%s' % band
                    if sol is not None: why += ', solidity=%s' % sol
                    is_table_row = lines[n-1].count('&') >= 2 and lines[n-1].rstrip().endswith('\\\\')
                    if is_table_row:
                        findings['S3d_BUILD_BAND_INDEX_ROW'].append(
                            (tex,n,cid,why+' -- lookup-table provenance row, not an assertion'))
                    elif disclosed_near(lines, n):
                        findings['S3c_BUILD_BAND_DISCLOSED'].append(
                            (tex,n,cid,why+' -- banner present nearby (honest)'))
                    else:
                        findings['S3a_BUILD_BAND_UNDISCLOSED'].append((tex,n,cid,why))
                        per_file[tex]+=1
                elif status in ('proposed','ambiguous','pending'):
                    findings['S3b_NODE_STATUS_INFO'].append(
                        (tex,n,cid,'status=%s (convention for this node class)'%status))

    order = ['S1_DEAD_PATH','S2_DEAD_ID','S3a_BUILD_BAND_UNDISCLOSED','S4a_TIME_LAG_MATERIAL','S5_LINE_DRIFT','S4b_TIME_LAG_COSMETIC','S3b_NODE_STATUS_INFO','S3c_BUILD_BAND_DISCLOSED','S3d_BUILD_BAND_INDEX_ROW']
    print('# manuscript .tex vs KB staleness audit')
    print('# repo HEAD: %s' % sh(['git','rev-parse','--short','HEAD']))
    print('# .tex scanned: %d   KB records: %d' % (len(tex_files), len(claims)))
    print()
    for k in order:
        print('## %s  --  %d' % (k, len(findings[k])))
    print()
    for k in order:
        rows = findings[k]
        if not rows: continue
        print('=== %s (%d) ===' % (k, len(rows)))
        for tex,n,what,why in sorted(rows):
            print('%s:%d\t%s\t%s' % (tex,n,what,why))
        print()
    print('=== FILES BY FINDING COUNT ===')
    for f,c in per_file.most_common(30):
        print('%4d  %s' % (c,f))
    return 0

if __name__ == '__main__':
    sys.exit(main())
