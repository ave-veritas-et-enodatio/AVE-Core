#!/usr/bin/env python3
"""Solidity ratchet.

Solidity is `min` over a claim's declared dependencies, so deleting the weakest
`depends-on` bullet lifts the claim and everything downstream of it. Every other
gate reads that edit as routine: refresh regenerates the index, the verifier finds
it fresh, and `make verify` stays green. Measured at cbc668e7: of 408 claim-to-claim
`depends` edges, removing any one of 53 moves the citing claim up a build band.

The one question: for every `depends` edge the merge-base has and the tip does not,
put the edge back and re-solve the tip. If that lowers any claim's band, the deletion
is holding the band up and the branch owes a receipt. The test is against the
restored solve and not the base band, because the same cut also stops a claim
falling when its dependency was downgraded, and there the band never rises at all.

THE RECEIPT
-----------
A line ADDED by this branch, in a file under research/ or
_orchestration/docket-entries/, that names BOTH ids of the removed edge. The cost is
one sentence in a reviewed document. The gate reads none of its meaning: it forces
the deletion into the open and leaves judging the reason to review. A register
cannot serve, because claim-quality.md names every id and would match anything.

WHAT IT DOES NOT GATE
---------------------
Raised confidence, raised support quality or on-point fraction, and run experiments
all lift bands too. Those are authored judgments, visible where they are written, and
are printed as `not gated`. A claim re-minted under a new id starts with no removed
edges of its own, so only the claims that depended on the old id see the deletion.

THE SOLVE
---------
The graph is rebuilt from the committed `.index/` of each rev and solved by
kb_index_lib.compute_solidity_full, the one computation behind the published values.
Before any verdict both revs must reproduce every recorded solidity exactly. A rev
that does not is either stale or this reconstruction has drifted; either way a clean
report would be false, so the run aborts.

Exit codes: 0 no unexplained lift, 1 at least one, 2 the gate itself could not run.

    verify-solidity-ratchet.py <base> <tip>
    verify-solidity-ratchet.py --selftest           can-it-fire + negative controls
    verify-solidity-ratchet.py --mutation-receipt   each rule, removed, must trip
"""
import json, os, re, shutil, subprocess, sys, tempfile
from pathlib import Path
from types import SimpleNamespace

sys.path.insert(0, str(Path(__file__).resolve().parent))
import kb_index_lib as lib

CLAIMS = 'manuscript/ave-kb/.index/claims.jsonl'
EDGES = 'manuscript/ave-kb/.index/depends-on.jsonl'
RECEIPT_ROOTS = ('research/', '_orchestration/docket-entries/')

#: Band names, lowest first, read off the library so a renamed band needs no edit here.
BANDS = list(dict.fromkeys(
    [lib.derive_build_band(None)] + [lib.derive_build_band(n / 100) for n in range(101)]))

#: Rules switched OFF by --mutation-receipt. Empty in every real run.
MUTATE = set()

HUNK = re.compile(r'^@@ -\d+(?:,(\d+))? \+\d+(?:,(\d+))? @@')


class GateError(Exception):
    """The machinery failed. A clean report past this point would be false."""


class Repo:
    """A git repo handle. Fixtures scrub GIT_* so a hook's GIT_DIR cannot reach the real repo."""

    def __init__(self, cwd=None, scrub_env=False):
        self.cwd, self.env = cwd, None
        if scrub_env:
            self.env = {k: v for k, v in os.environ.items() if not k.startswith('GIT_')}

    def git(self, *args):
        p = subprocess.run(('git',) + args, cwd=self.cwd, env=self.env, capture_output=True,
                           text=True, encoding='utf-8', errors='replace')
        if p.returncode:
            raise GateError('git %s exited %d: %s' % (' '.join(args), p.returncode, p.stderr.strip()))
        return p.stdout


class Graph:
    """One rev's claim graph, as its committed index records it."""

    def __init__(self, nodes, edges):
        self.claims = {r['id']: r for r in nodes if r['node_type'] == 'claim'}
        self.supports = {r['id']: r for r in nodes if r['node_type'] == 'support'}
        self.experiments = {r['id']: r for r in nodes if r['node_type'] == 'experiment'}
        self.edges = edges


def records(repo, rev, path):
    out = []
    for n, line in enumerate(repo.git('show', '%s:%s' % (rev, path)).split('\n'), 1):
        if not line:
            continue
        try:
            out.append(json.loads(line))
        except ValueError as e:
            raise GateError('%s:%s line %d is not JSON: %s' % (rev, path, n, e))
    return out


def solve(graph, restored=(), retired=None):
    """Claim finals and support solidities for `graph` plus any restored edges.

    `retired` maps a claim gone from this graph to its final at the base, so an edge
    restored to it binds at the value it had.
    """
    deps, gives, confers = {}, {}, {}
    for e in list(graph.edges) + list(restored):
        if e['relation'] == 'depends':
            deps.setdefault(e['source'], []).append(SimpleNamespace(
                relation='depends', target=e['target'], target_kind=e['target_kind']))
        elif e['relation'] == 'supports':
            f = lib.PENDING_FRACTION if e['fraction'] == '*pending*' else e['fraction']
            gives.setdefault(e['source'], []).append((e['target'], f))
        elif e['relation'] == 'strengthens':
            confers.setdefault(e['source'], []).append((e['target'], e['strength']))
    entries = [SimpleNamespace(id=c, confidence=r['confidence'], depends_on=tuple(deps.get(c, ())))
               for c, r in graph.claims.items()]
    entries += [SimpleNamespace(id=c, confidence=v, depends_on=()) for c, v in (retired or {}).items()]
    sups = [SimpleNamespace(id=s, quality=r['quality'], depends_on=tuple(deps.get(s, ())),
                            supports=tuple(gives.get(s, ()))) for s, r in graph.supports.items()]
    exps = [SimpleNamespace(id=x, status=r['status'], strengthens=tuple(confers.get(x, ())))
            for x, r in graph.experiments.items()]
    full = lib.compute_solidity_full(entries, exps, sups)
    return {c: r.final for c, r in full.items()}, dict(full.sup_solidity)


def reconcile(graph, label):
    """Fail unless this reconstruction reproduces every value the index records."""
    if 'no-reconcile' in MUTATE:
        return
    finals, sups = solve(graph)
    wrong = ['%s computes %r, records %r' % (i, have.get(i), r['solidity'])
             for have, nodes in ((finals, graph.claims), (sups, graph.supports))
             for i, r in sorted(nodes.items()) if have.get(i) != r['solidity']]
    if wrong:
        raise GateError('%s: %d recorded solidities do not reproduce, so either the index is '
                        'stale (run make refresh-kb-metadata) or this reconstruction no longer '
                        'matches kb_index_lib. First: %s' % (label, len(wrong), wrong[0]))


def load(repo, rev):
    try:
        graph = Graph(records(repo, rev, CLAIMS), records(repo, rev, EDGES))
        reconcile(graph, rev)
    except (KeyError, TypeError) as e:
        raise GateError('%s: malformed index record: %r' % (rev, e))
    return graph


def rank(value):
    return BANDS.index(lib.derive_build_band(value))


def removed_edges(base, tip):
    """Claim-to-claim `depends` edges at the base and not the tip, one per (source, target).

    A source gone from the tip needs no restoring: the claims that depended on it
    carry removed edges of their own, and those are what get tested.
    """
    if 'no-restore' in MUTATE:
        return []
    kept = {(e['source'], e['target']) for e in tip.edges if e['relation'] == 'depends'}
    nodes = set(tip.claims) | set(tip.supports)
    gone = {}
    for e in base.edges:
        key = (e['source'], e['target'])
        if (e['relation'] == 'depends' and e['target_kind'] == 'claim'
                and key not in kept and e['source'] in nodes):
            gone.setdefault(key, e)
    return list(gone.values())


def held_up(tip, restored):
    """Claims whose band the restored solve takes away, with what they would read."""
    if 'any-rise' in MUTATE:
        return {c: restored.get(c) for c, v in tip.items() if v != restored.get(c)}
    return {c: restored.get(c) for c, v in tip.items() if rank(v) > rank(restored.get(c))}


def added_lines(repo, base, tip):
    """(path, text) for every line this range adds under RECEIPT_ROOTS.

    Hunk headers are counted, not matched: a Markdown line beginning `++ ` reads as a
    `+++` file header to anything that only looks at the leading characters.
    """
    roots = () if 'any-root' in MUTATE else ('--',) + RECEIPT_ROOTS
    if 'any-line' in MUTATE:
        names = repo.git('ls-tree', '-r', '--name-only', tip).split('\n')
        return [(n, line) for n in names if n
                for line in repo.git('show', '%s:%s' % (tip, n)).split('\n')]
    diff = repo.git('-c', 'core.quotePath=false', 'diff', '--unified=0', '--no-color',
                    '--no-ext-diff', '--find-renames', base, tip, *roots)
    out, path, old, new = [], None, 0, 0
    for line in diff.split('\n'):
        if old or new:
            if line.startswith('-'):
                old -= 1
            elif line.startswith('+'):
                new -= 1
                out.append((path, line[1:]))
            continue
        hunk = HUNK.match(line)
        if hunk:
            old = 1 if hunk.group(1) is None else int(hunk.group(1))
            new = 1 if hunk.group(2) is None else int(hunk.group(2))
        elif line.startswith('+++ '):
            path = line[4:][2:] if line[4:].startswith('b/') else line[4:]
    return out


def find_receipt(edge, lines):
    for path, text in lines:
        if edge['source'] in text and (edge['target'] in text or 'one-id' in MUTATE):
            return path
    return None


def scan(repo, base_rev, tip_rev):
    base, tip = load(repo, base_rev), load(repo, tip_rev)
    base_f, tip_f = solve(base)[0], solve(tip)[0]
    gone = removed_edges(base, tip)
    retired = {} if 'no-stub' in MUTATE else {
        e['target']: base_f.get(e['target']) for e in gone if e['target'] not in tip.claims}

    def against(edges):
        """Claims the given edges hold down, or None if restoring them closes a cycle."""
        try:
            held = held_up(tip_f, solve(tip, edges, retired)[0])
        except lib.SolidityCycleError:
            return {} if 'cycle-passes' in MUTATE else None
        if 'rise-only' in MUTATE:
            return {c: v for c, v in held.items() if rank(tip_f[c]) > rank(base_f.get(c))}
        return held

    effects = {}
    for e in gone:
        got = against([e])
        if got is None or got:
            effects[(e['source'], e['target'])] = got
    # Two supports can each hold a claim up alone: neither restoration moves it, and
    # together they do. Solidity has max branches, so singles do not bound the joint.
    solvable = [e for e in gone if effects.get((e['source'], e['target']), {}) is not None]
    joint = {} if 'no-joint' in MUTATE else against(solvable)
    named = {c for got in effects.values() if got for c in got}
    if joint is None or set(joint) - named:
        residual = joint and {c: v for c, v in joint.items() if c not in named}
        for e in solvable:
            effects.setdefault((e['source'], e['target']), residual)

    lines = added_lines(repo, base_rev, tip_rev) if effects else []
    findings = []
    for e in gone:
        key = (e['source'], e['target'])
        if key in effects:
            findings.append({'edge': e, 'holds': effects[key], 'receipt': find_receipt(e, lines)})
    claimed = {c for f in findings if f['holds'] for c in f['holds']}
    others = [c for c in sorted(tip_f) if c in base_f and c not in claimed
              and rank(tip_f[c]) > rank(base_f[c])]
    return {'gone': gone, 'findings': findings, 'others': others, 'base': base_f, 'tip': tip_f}


def show(value):
    return '*pending*' if value is None else '%g' % value


def report(res, base, tip):
    open_ = [f for f in res['findings'] if not f['receipt']]
    print('[solidity-ratchet] %s..%s  removed-edges=%d  band-holding=%d  receipted=%d  '
          'UNEXPLAINED=%d  other-band-rises=%d (not gated)'
          % (base[:8], tip[:8], len(res['gone']), len(res['findings']),
             len(res['findings']) - len(open_), len(open_), len(res['others'])))
    for f in res['findings']:
        e = f['edge']
        print('\n  %s -x-> %s  %s' % (e['source'], e['target'],
                                      'receipt: ' + f['receipt'] if f['receipt'] else 'UNEXPLAINED'))
        if f['holds'] is None:
            print('     restoring it closes a cycle, so its effect cannot be computed')
        for c, restored in sorted((f['holds'] or {}).items()):
            print('     holds %s at %s (%s); restored it reads %s (%s)' % (
                c, lib.derive_build_band(res['tip'][c]), show(res['tip'][c]),
                lib.derive_build_band(restored), show(restored)))
        if e.get('context'):
            print('     dropped: %s' % e['context'])
    for c in res['others']:
        print('\n  not gated: %s  %s -> %s  (%s -> %s)' % (
            c, lib.derive_build_band(res['base'][c]), lib.derive_build_band(res['tip'][c]),
            show(res['base'][c]), show(res['tip'][c])))
    if open_:
        print('\nRestore the edge, or add a line to a document under %s on this branch that names '
              'both ids and says why the dependency is gone.' % ' or '.join(RECEIPT_ROOTS))
        return 1
    return 0


def main(base, tip, repo=None):
    repo = repo or Repo()
    dead = run_gate(out=lambda line: None)
    if dead:
        print('[solidity-ratchet] ABORT: self-gate failed -- a clean report here would be false.')
        for why in dead:
            print('  ' + why)
        return 2
    try:
        for rev in (base, tip):
            repo.git('rev-parse', '--verify', '%s^{tree}' % rev)
        res = scan(repo, base, tip)
    except (GateError, lib.SolidityCycleError) as e:
        print('[solidity-ratchet] ABORT: %s' % e)
        return 2
    print('[solidity-ratchet] liveness OK -- both revs resolve and reproduce their recorded '
          'solidities, self-gate %d/%d.' % (len(CASES), len(CASES)))
    return report(res, base, tip)


# ------------------------------------------------------------------- fixtures
#
# One throwaway repo. Trees are built with `git write-tree`: no commit, so no
# identity, no hooks, no signing.
#
#   WEAK 0.30 <- CITE 0.85 -> SOLID 0.90        DOWN 0.85 -> CITE
#   WEAK <- SUP1, SUP2 (quality 0.90) both supporting LIFT 0.10 in full
#   NEAR 0.80 -> NEAR2 0.70                     same band either way

WEAK, SOLID, CITE, DOWN, LIFT = 'clm-weak00', 'clm-solid0', 'clm-cite00', 'clm-down00', 'clm-lift00'
NEAR, NEAR2, SUP1, SUP2 = 'clm-near00', 'clm-near02', 'sup-one000', 'sup-two000'
NOTE = 'research/2026-01-01_fixture_result.md'


def spec(**changes):
    s = {'claims': {WEAK: .30, SOLID: .90, CITE: .85, DOWN: .85, LIFT: .10, NEAR: .80, NEAR2: .70},
         'sups': {SUP1: .90, SUP2: .90},
         'deps': [(CITE, WEAK), (CITE, SOLID), (DOWN, CITE), (NEAR, NEAR2), (SUP1, WEAK), (SUP2, WEAK)],
         'gives': [(SUP1, LIFT), (SUP2, LIFT)]}
    s.update(changes)
    return s


def without(*pairs):
    return [d for d in spec()['deps'] if d not in pairs]


def tree(repo, root, s, files=(), tamper=False):
    edges = [{'source': a, 'target': b, 'relation': 'depends', 'target_kind': 'claim', 'context': None}
             for a, b in s['deps']]
    edges += [{'source': a, 'target': b, 'relation': 'supports', 'target_kind': 'claim', 'fraction': 1.0}
              for a, b in s['gives']]
    nodes = [{'node_type': 'claim', 'id': c, 'confidence': v, 'solidity': None} for c, v in s['claims'].items()]
    nodes += [{'node_type': 'support', 'id': c, 'quality': v, 'solidity': None} for c, v in s['sups'].items()]
    finals, sups = solve(Graph(nodes, edges))
    for r in nodes:
        r['solidity'] = (finals if r['node_type'] == 'claim' else sups).get(r['id'])
    if tamper:
        nodes[0]['solidity'] = 0.99
    shutil.rmtree(root + '/manuscript', ignore_errors=True)
    shutil.rmtree(root + '/research', ignore_errors=True)
    wanted = [(CLAIMS, '\n'.join(map(json.dumps, nodes)) + '\n'),
              (EDGES, '\n'.join(map(json.dumps, edges)) + '\n')] + list(files)
    for path, text in wanted:
        Path(root, path).parent.mkdir(parents=True, exist_ok=True)
        Path(root, path).write_text(text, encoding='utf-8')
    repo.git('add', '-A')
    return repo.git('write-tree').strip()


CUT = (CITE, WEAK)
BOTH_IDS = 'dropped %s from %s: the bound no longer applies' % (WEAK, CITE)

#: name -> (base files, tip spec, tip files, expected exit, expected removed edges flagged)
CASES = {
    'unchanged':          ((), spec(), (), 0, set()),
    'cut-binding':        ((), spec(deps=without(CUT)), (), 1, {CUT}),
    'cut-slack':          ((), spec(deps=without((CITE, SOLID))), (), 0, set()),
    'cut-within-band':    ((), spec(deps=without((NEAR, NEAR2))), (), 0, set()),
    'add-edge':           ((), spec(deps=spec()['deps'] + [(DOWN, SOLID)]), (), 0, set()),
    'receipt':            ((), spec(deps=without(CUT)), ((NOTE, BOTH_IDS + '\n'),), 0, {CUT}),
    'receipt-one-id':     ((), spec(deps=without(CUT)), ((NOTE, 'dropped a dep from %s\n' % CITE),), 1, {CUT}),
    'receipt-wrong-root': ((), spec(deps=without(CUT)),
                           (('manuscript/ave-kb/vol1/claim-quality.md', BOTH_IDS + '\n'),), 1, {CUT}),
    'receipt-old-line':   (((NOTE, BOTH_IDS + '\n'),), spec(deps=without(CUT)),
                           ((NOTE, BOTH_IDS + '\n'),), 1, {CUT}),
    'raised-confidence':  ((), spec(claims={**spec()['claims'], WEAK: .90}), (), 0, set()),
    'no-longer-binding':  ((), spec(deps=without(CUT), claims={**spec()['claims'], CITE: .25}), (), 0, set()),
    'held-against-fall':  ((), spec(deps=without(CUT), claims={**spec()['claims'], WEAK: .10, CITE: .40}),
                           (), 1, {CUT}),
    'retired-binding':    ((), spec(deps=without(CUT, (SUP1, WEAK), (SUP2, WEAK)),
                                    claims={k: v for k, v in spec()['claims'].items() if k != WEAK}),
                           (), 1, {CUT, (SUP1, WEAK), (SUP2, WEAK)}),
    'retired-slack':      ((), spec(deps=without((CITE, SOLID)),
                                    claims={**{k: v for k, v in spec()['claims'].items() if k != SOLID},
                                            WEAK: .90}), (), 0, set()),
    'reversed-edge':      ((), spec(deps=without(CUT) + [(WEAK, CITE)]), (), 1, {CUT}),
    'joint-only':         ((), spec(deps=without((SUP1, WEAK), (SUP2, WEAK))), (), 1,
                           {(SUP1, WEAK), (SUP2, WEAK)}),
}


def run_case(repo, root, name):
    base_files, tip_spec, tip_files, want_rc, want = CASES[name]
    base = tree(repo, root, spec(), base_files)
    tip = tree(repo, root, tip_spec, tip_files)
    res = scan(repo, base, tip)
    got = {(f['edge']['source'], f['edge']['target']) for f in res['findings']}
    rc = 1 if any(not f['receipt'] for f in res['findings']) else 0
    return rc == want_rc and got == want


def run_gate(out=print):
    """Every fixture verdict, plus the abort a stale index owes. Returns what failed."""
    root = tempfile.mkdtemp(prefix='solidity-ratchet-selftest-')
    failed = []
    try:
        repo = Repo(cwd=root, scrub_env=True)
        repo.git('init', '-q')
        for name in CASES:
            try:
                ok = run_case(repo, root, name)
            except (GateError, lib.SolidityCycleError) as e:
                ok, name = False, '%s (%s)' % (name, e)
            out('  [%s] %s' % ('OK' if ok else 'BROKEN', name))
            if not ok:
                failed.append('fixture verdict wrong: %s' % name)
        base = tree(repo, root, spec())
        stale = tree(repo, root, spec(), tamper=True)
        try:
            scan(repo, base, stale)
            failed.append('a tip whose recorded solidity does not reproduce was accepted')
            out('  [BROKEN] stale-index')
        except GateError:
            out('  [OK] stale-index')
    finally:
        shutil.rmtree(root, ignore_errors=True)
    return failed


def selftest():
    print('[solidity-ratchet] SELF-GATE')
    failed = run_gate()
    if failed:
        print('[solidity-ratchet] SELF-GATE FAILED: %s' % '; '.join(failed))
        return 1
    print('[solidity-ratchet] SELF-GATE OK: %d fixtures and the stale-index abort.' % len(CASES))
    return 0


#: mutation -> the one fixture verdict switching it off must break.
MUTATIONS = {
    'no-restore':    ('cut-binding', 'stop finding removed edges'),
    'any-rise':      ('cut-within-band', 'gate on any solidity rise instead of a band rise'),
    'rise-only':     ('held-against-fall', 'exempt a cut that only stops a claim falling'),
    'one-id':        ('receipt-one-id', 'accept a receipt naming only the source'),
    'any-root':      ('receipt-wrong-root', 'accept a receipt outside the reviewed roots'),
    'any-line':      ('receipt-old-line', 'accept a line this branch did not add'),
    'no-stub':       ('retired-slack', 'restore edges to retired claims as pending'),
    'cycle-passes':  ('reversed-edge', 'treat an edge that cannot be restored as harmless'),
    'no-joint':      ('joint-only', 'test edges only one at a time'),
}


def mutation_receipt():
    print('[solidity-ratchet] MUTATION RECEIPT -- each rule, switched off, must change a verdict')
    allgood = True
    for mutation, (case, label) in MUTATIONS.items():
        MUTATE.add(mutation)
        try:
            failed = run_gate(out=lambda line: None)
        finally:
            MUTATE.discard(mutation)
        tripped = 'fixture verdict wrong: %s' % case in failed
        print('  [%s] %s -> %s' % ('OK' if tripped else 'BROKEN', label, case))
        allgood = allgood and tripped
    MUTATE.add('no-reconcile')
    try:
        failed = run_gate(out=lambda line: None)
    finally:
        MUTATE.discard('no-reconcile')
    tripped = any('does not reproduce' in why for why in failed)
    print('  [%s] skip the reconcile -> stale-index' % ('OK' if tripped else 'BROKEN'))
    allgood = allgood and tripped
    if not allgood:
        print('[solidity-ratchet] MUTATION RECEIPT FAILED')
        return 1
    print('[solidity-ratchet] MUTATION RECEIPT OK: every rule is load-bearing.')
    return 0


if __name__ == '__main__':
    if '--selftest' in sys.argv:
        sys.exit(selftest())
    if '--mutation-receipt' in sys.argv:
        sys.exit(mutation_receipt())
    if len(sys.argv) != 3:
        print('usage: verify-solidity-ratchet.py <base> <tip> | --selftest | --mutation-receipt')
        sys.exit(2)
    sys.exit(main(sys.argv[1], sys.argv[2]))
