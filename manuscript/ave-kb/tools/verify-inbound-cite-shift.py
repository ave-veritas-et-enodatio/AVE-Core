#!/usr/bin/env python3
"""Inbound cite-shift checker.

The corpus pins by `path:NNN`. Any edit that moves a line silently re-points some
OTHER file's cite at different content. Nothing catches it: verify-md-links gates
only out-of-RANGE, verify-anchor-content is advisory and needs an adjacent excerpt.

The one question that matters: for every corpus cite targeting a file this branch
CHANGED, does the cited line still hold what it held at the merge-base?
base[N] != tip[N]  =>  the cite moved under its citer, silently.
"""
import re, subprocess, sys, collections

def sh(*a):
    r = subprocess.run(a, capture_output=True)
    return r.stdout.decode('utf-8', 'replace')

def blob(rev, path):
    r = subprocess.run(['git','show',f'{rev}:{path}'], capture_output=True)
    return r.stdout.decode('utf-8','replace').split('\n') if r.returncode == 0 else None

def main(base, tip, verbose=False):
    changed = [l for l in sh('git','diff','--name-only',base,tip).split('\n') if l.strip()]
    by_leaf = collections.defaultdict(list)
    for c in changed:
        by_leaf[c.rsplit('/',1)[-1]].append(c)
    if not by_leaf:
        print('no changed files'); return 0

    # candidate citers: any tracked line at TIP mentioning a changed file's leaf
    # name followed (within a few punctuation chars) by :NNN. git grep -I skips
    # binaries. Deliberately over-broad; resolved targets are validated after.
    # NOTE: candidate collection uses git grep with a FIXED STRING (-F), never a
    # regex. An earlier version passed an ERE to git grep and a near-identical
    # pattern to Python's re: inside a POSIX bracket expression a backslash is
    # LITERAL, so `[...\]]` demanded a literal ']' before the colon and the stage
    # silently under-collected -- it missed a citer I had already proved by hand.
    # One engine does the finding, one does the precision. Never two.
    cand = collections.defaultdict(list)
    for leaf in by_leaf:
        out = sh('git','grep','-nIF', leaf, tip, '--')
        for line in out.split('\n'):
            if not line.strip(): continue
            parts = line.split(':', 3)
            if len(parts) < 4: continue
            _, src, lno, text = parts[0], parts[1], parts[2], parts[3]
            cand[src].append((int(lno), text, leaf))

    pat_tmpl = r'([A-Za-z0-9_./\\-]*%s)[^A-Za-z0-9\s]{0,3}:(\d+)'
    findings, cache, checked = [], {}, 0
    for src, rows in cand.items():
        for lno, text, leaf in rows:
            for m in re.finditer(pat_tmpl % re.escape(leaf), text):
                n = int(m.group(2))
                for target in by_leaf[leaf]:
                    if src == target and abs(lno - n) < 3: continue
                    if target not in cache:
                        cache[target] = (blob(base,target), blob(tip,target))
                    b, t = cache[target]
                    if b is None or t is None: continue
                    checked += 1
                    bl = b[n-1] if 0 < n <= len(b) else None
                    tl = t[n-1] if 0 < n <= len(t) else None
                    if bl is None: continue          # never a valid address at base
                    if tl is None:
                        findings.append((src,lno,target,n,'OUT-OF-RANGE',bl,'',0))
                    elif bl.strip() != tl.strip():
                        # THE REACH TEST. Two very different things look identical
                        # at the cited address:
                        #   SHIFTED  - the base content still exists in the file,
                        #              at a DIFFERENT line. The address now returns
                        #              someone else's subject, silently. Real rot.
                        #   EDITED   - the base content is gone; the line was
                        #              rewritten in place. The cite still points at
                        #              the right row, with updated text. Usually the
                        #              intended edit, not a defect.
                        # Without this split the checker is the S4a scan again: a
                        # marker with no reach test, 1.3% true-positive.
                        b_ = bl.strip()
                        moved_to = [j+1 for j,l in enumerate(t) if l.strip() == b_] if b_ else []
                        kind = 'SHIFTED' if moved_to else 'EDITED-IN-PLACE'
                        findings.append((src,lno,target,n,kind,bl,tl,moved_to[0] if moved_to else 0))

    # LIVENESS CONTROL, same shape as verify-fired-riders.py's. A checker that
    # resolves nothing reports a clean it did not earn. If this branch changed
    # files and NOT ONE corpus cite into them could be resolved, the finder is
    # broken (a bad pattern, a bad rev, an empty grep) -- abort rather than
    # print a zero. Measured precedent: an earlier build of this very script
    # passed an ERE to `git grep` and a near-identical pattern to Python's `re`.
    # Inside a POSIX bracket expression a backslash is LITERAL, so the git-grep
    # arm silently under-collected and the script reported 3 moved cites where
    # there were 79. One engine finds, one engine decides -- never two.
    if changed and checked == 0:
        print('[inbound-cites] ABORT: %d changed file(s) but ZERO cites resolved. '
              'The FINDER is broken -- a clean report here would be false.' % len(changed))
        return 2

    findings = sorted(set(findings))
    shifted = [f for f in findings if f[4] in ('SHIFTED','OUT-OF-RANGE')]
    edited  = [f for f in findings if f[4] == 'EDITED-IN-PLACE']
    print(f'[inbound-cites] {base[:8]}..{tip[:8]}  changed-files={len(changed)}  cites-resolved={checked}'
          f'  SHIFTED={len(shifted)} (real rot)  EDITED-IN-PLACE={len(edited)} (advisory)')
    findings = shifted if not verbose else findings
    if not findings:
        print('  clean — every corpus cite into a changed file still holds its content')
        return 0
    print()
    for src,lno,target,n,kind,bl,tl,to in findings:
        if kind == 'EDITED-IN-PLACE' and not verbose: continue
        arrow = f' -- base content is now at :{to}' if to else ''
        print(f'  {src}:{lno}  ->  {target}:{n}   [{kind}]{arrow}')
        b_, t_ = bl.strip(), tl.strip()
        mark = '  [differs beyond col 105]' if b_[:105] == t_[:105] else ''
        print(f'     was: {b_[:105]}{mark}')
        print(f'     now: {t_[:105]}{mark}')
        print()
    return 1

if __name__ == '__main__':
    sys.exit(main(sys.argv[1], sys.argv[2], '-v' in sys.argv))
