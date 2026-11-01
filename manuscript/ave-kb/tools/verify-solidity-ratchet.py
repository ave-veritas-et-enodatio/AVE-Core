#!/usr/bin/env python3
"""Solidity ratchet.

Solidity is `min` over a claim's declared dependencies, so deleting the weakest
`depends-on` bullet lifts the claim and everything downstream of it. No other gate reads
solidity: refresh regenerates the index, the verifier finds it fresh, and `make verify`
stays green, while the cite-shift gate fires only if the deletion moves a cited line.
Measured at cbc668e7: of 408 claim-to-claim `depends` edges, removing any one of 53
moves the citing claim up a build band.

The one question: for every claim-to-claim `depends` edge the merge-base has and the tip
does not, put the edge back and re-solve the tip. If that lowers any claim's band, the
deletion is holding the band up and the branch owes a receipt. The test is against the
restored solve and not the base band, because the same cut also stops a claim falling
when its dependency was downgraded, and there the band never rises at all. Pending
ranks lowest, because None is the bottom of the solve's min and max.

A claim that left the index is tested as if it had stayed and lost those edges, so a
re-mint under a new id, or a split, owes the same receipt as a cut. Ids are stable
(INVARIANT-S8) and none left the index across the 113 index changes measured.

THE RECEIPT
-----------
A line at the tip, in a Markdown file under research/ or
_orchestration/docket-entries/, reading

    dep-removed: <source> -> <target>: <why>

One edge per line. Only indentation or a list marker may precede `dep-removed:`, and the
base tree must not already hold that edge and reason anywhere, whitespace aside. So a
regenerated dump, a grep echo, or an old line that was moved or re-indented does not
count. The gate reads none of the reason: it forces the deletion into the open and
leaves judging it to review. A register cannot serve, because refresh rewrites it and the
deletion is the edit under test.

WHAT IT DOES NOT GATE
---------------------
Raised confidence, raised support quality or on-point fraction, run experiments, and a
support added or re-minted under a new id all lift bands too. Those are authored
judgments, visible where they are written. A rise that survives restoring the removed
edges is printed as `not gated`, so a claim that rose both ways shows both.

THE SOLVE
---------
The graph is rebuilt from the committed `.index/` of each rev and solved by
kb_index_lib.compute_solidity_full, the one computation behind the published values.
Before any verdict both revs must hold at least one claim, every `depends` edge must name
nodes the rev holds, and every recorded solidity must reproduce exactly. A rev that fails
is empty, truncated or stale, or this reconstruction has drifted; either way a clean
report would be false, so the run aborts.

Exit codes: 0 no unexplained lift, 1 at least one, 2 the gate itself could not run. A
crash is a 2: an uncaught traceback exits 1, which would read as a verdict.

    verify-solidity-ratchet.py <base> <tip>
    verify-solidity-ratchet.py --selftest           can-it-fire + negative controls
    verify-solidity-ratchet.py --mutation-receipt   each listed rule, removed, must trip
"""
import json, os, re, shutil, subprocess, sys, tempfile, traceback
from pathlib import Path
from types import SimpleNamespace

sys.path.insert(0, str(Path(__file__).resolve().parent))
try:
    import kb_index_lib as lib
except Exception as e:
    print('[solidity-ratchet] ABORT: cannot import kb_index_lib: %s' % e)
    sys.exit(2)

CLAIMS = 'manuscript/ave-kb/.index/claims.jsonl'
EDGES = 'manuscript/ave-kb/.index/depends-on.jsonl'
RECEIPT_ROOTS = ('research/', '_orchestration/docket-entries/')
TOKEN = 'dep-removed:'

_ID = r'[a-z]{3}-[a-z0-9]+'
RECEIPT = re.compile(r'\s*(?:[-*]\s+)?%s\s*(%s)\s*->\s*(%s)\s*:(.*)' % (TOKEN, _ID, _ID))

#: Band names, lowest first, read off the library so a renamed band needs no edit here.
BANDS = list(dict.fromkeys(
    [lib.derive_build_band(None)] + [lib.derive_build_band(n / 100) for n in range(101)]))

#: Rules switched OFF by --mutation-receipt. Empty in every real run.
MUTATE = set()


class GateError(Exception):
    """The machinery failed. A clean report past this point would be false."""


class Repo:
    """A git repo handle. Fixtures scrub GIT_* so a hook's GIT_DIR cannot reach the real repo."""

    def __init__(self, cwd=None, scrub_env=False):
        self.cwd, self.env = cwd, None
        if scrub_env:
            self.env = {k: v for k, v in os.environ.items() if not k.startswith('GIT_')}

    def git(self, *args, ok=(0,)):
        p = subprocess.run(('git',) + args, cwd=self.cwd, env=self.env, capture_output=True,
                           text=True, encoding='utf-8', errors='replace')
        if p.returncode not in ok:
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
            if 'skip-bad-json' in MUTATE:
                continue
            raise GateError('%s:%s line %d is not JSON: %s' % (rev, path, n, e))
    return out


def solve(graph, restored=()):
    """Claim finals and support solidities for `graph` plus any restored edges."""
    deps, gives, confers = {}, {}, {}
    for e in list(graph.edges) + list(restored):
        if e['relation'] == 'depends':
            deps.setdefault(e['source'], []).append(SimpleNamespace(
                relation='depends', target=e['target'], target_kind=e['target_kind']))
        elif e['relation'] == 'supports':
            pending = e['fraction'] == '*pending*'
            f = 1.0 if pending and 'fraction-one' in MUTATE else lib.PENDING_FRACTION if pending else e['fraction']
            gives.setdefault(e['source'], []).append((e['target'], f))
        elif e['relation'] == 'strengthens':
            confers.setdefault(e['source'], []).append((e['target'], e['strength']))
    entries = [SimpleNamespace(id=c, confidence=r['confidence'], depends_on=tuple(deps.get(c, ())))
               for c, r in graph.claims.items()]
    sups = [SimpleNamespace(id=s, quality=r['quality'], depends_on=tuple(deps.get(s, ())),
                            supports=tuple(gives.get(s, ()))) for s, r in graph.supports.items()]
    exps = [SimpleNamespace(id=x, status=r['status'], strengthens=tuple(confers.get(x, ())))
            for x, r in graph.experiments.items()]
    if 'no-experiments' in MUTATE:
        exps = []
    full = lib.compute_solidity_full(entries, exps, sups)
    return {c: r.final for c, r in full.items()}, dict(full.sup_solidity)


def check_whole(graph, label):
    """Fail on an index a reconcile would pass by comparing nothing."""
    if not graph.claims and 'allow-empty' not in MUTATE:
        raise GateError('%s: the index holds no claims, so it is empty or its node_type values '
                        'changed' % label)
    holders = set(graph.claims) | set(graph.supports)
    orphans = [e for e in graph.edges if e['relation'] == 'depends'
               and (e['source'] not in holders
                    or e['target_kind'] == 'claim' and e['target'] not in graph.claims)]
    if orphans and 'allow-orphans' not in MUTATE:
        raise GateError('%s: %d depends edges name a node the index does not hold, so it is '
                        'truncated or stale. First: %s -> %s'
                        % (label, len(orphans), orphans[0]['source'], orphans[0]['target']))


def reconcile(graph, label):
    """Fail unless this reconstruction reproduces every value the index records."""
    if 'no-reconcile' in MUTATE:
        return
    finals, sups = solve(graph)
    kinds = ((finals, graph.claims),) if 'claims-only' in MUTATE else (
        (finals, graph.claims), (sups, graph.supports))
    wrong = ['%s computes %r, records %r' % (i, have.get(i), r['solidity'])
             for have, nodes in kinds
             for i, r in sorted(nodes.items()) if have.get(i) != r['solidity']]
    if wrong:
        raise GateError('%s: %d recorded solidities do not reproduce, so either the index is '
                        'stale (run make refresh-kb-metadata) or this reconstruction no longer '
                        'matches kb_index_lib. First: %s' % (label, len(wrong), wrong[0]))


def load(repo, rev, trusted=False):
    try:
        graph = Graph(records(repo, rev, CLAIMS), records(repo, rev, EDGES))
        check_whole(graph, rev)
        if not trusted:
            reconcile(graph, rev)
    except (KeyError, TypeError) as e:
        raise GateError('%s: malformed index record: %r' % (rev, e))
    return graph


def rank(value):
    return BANDS.index(lib.derive_build_band(value))


def pair(edge):
    return edge['source'], edge['target']


def rest(edges, edge):
    return [e for e in edges if e is not edge]


def claim_deps(graph):
    return [e for e in graph.edges if e['relation'] == 'depends' and e['target_kind'] == 'claim']


def removed_edges(base, tip):
    """Claim-to-claim `depends` edges at the base and not the tip, one per (source, target)."""
    if 'no-restore' in MUTATE:
        return []
    kept = {pair(e) for e in (tip.edges if 'kept-any-relation' in MUTATE else claim_deps(tip))}
    gone = {}
    for e in claim_deps(base):
        if pair(e) not in kept:
            gone.setdefault(pair(e), e)
    if 'skip-retired' in MUTATE:
        return [e for k, e in gone.items() if k[0] in tip.claims or k[0] in tip.supports]
    return list(gone.values())


def with_retired(base, tip, gone):
    """The tip plus each claim `gone` touches that it no longer has, as the base had it.

    The removed edges stay off, so a claim that left reads what it would without them and
    restoring one binds it, the same as a kept claim. The authored lifts into it come back
    too. Base supports and experiments are in the node table for those lifts alone: with
    no edge into a tip claim they move nothing.
    """
    back = {n for e in gone for n in pair(e)} & (set(base.claims) - set(tip.claims))
    if 'no-stub' in MUTATE:
        back = set()
    world = Graph([], tip.edges + [e for e in base.edges if e['target'] in back
                                   and e['relation'] in ('supports', 'strengthens')])
    world.claims = {**{c: base.claims[c] for c in back}, **tip.claims}
    world.supports = {**base.supports, **tip.supports}
    world.experiments = {**base.experiments, **tip.experiments}
    return world


def held_up(tip, restored):
    """Claims whose band the restored solve takes away, with what they would read."""
    if 'any-rise' in MUTATE:
        return {c: restored.get(c) for c, v in tip.items() if v != restored.get(c)}
    return {c: restored.get(c) for c, v in tip.items() if rank(v) > rank(restored.get(c))}


def blame_jointly(singles, whole, edges, read):
    """Edge -> {claim: reading} for each claim `whole` takes below every single restore.

    Singles do not bound the joint: two supports can each hold a claim up alone, and two
    edges in series bind only together. Restoring only ever lowers a claim, so an edge
    whose omission leaves the claim higher is in every set that reaches that band. If
    those edges reach it by themselves they are the one such set. If they do not, several
    sets reach it and every edge is blamed.
    """
    lowest = {}
    for got in singles.values():
        for c, v in (got or {}).items():
            lowest[c] = min(lowest.get(c, rank(v)), rank(v))
    extra = {c: v for c, v in whole.items()
             if c not in lowest or (rank(v) < lowest[c] and 'membership' not in MUTATE)}
    blamed = {}
    if extra:
        omitted = {pair(e): read(rest(edges, e)) for e in edges}
        for c, v in extra.items():
            need = [e for e in edges if rank(omitted[pair(e)].get(c)) > rank(v)]
            if 'blame-all' in MUTATE or (rank(read(need).get(c)) != rank(v) and 'no-sufficiency' not in MUTATE):
                need = edges
            for e in need:
                blamed.setdefault(pair(e), {})[c] = v
    return blamed


def receipt_lines(repo, rev, paths):
    """(path, (source, target, reason)) for each receipt line at `rev` under `paths`."""
    pins = () if 'no-grep-pin' in MUTATE else ('--no-color', '--no-line-number', '--no-column')
    out = repo.git('grep', '-I', '-z', *pins, '-F', '-e', TOKEN, rev, '--', *paths, ok=(0, 1))
    found = []
    for row in out.split('\n'):
        where, _, text = row.partition('\0')
        line = (RECEIPT.search if 'token-anywhere' in MUTATE else RECEIPT.match)(text)
        if line and (line[3].strip() or 'no-reason' in MUTATE):
            found.append((where.split(':', 1)[1], (line[1], line[2], ' '.join(line[3].split()))))
    return found


def receipts(repo, base, tip):
    """{(source, target): path} for each receipt the tip has and the base tree does not."""
    paths = tuple(root + '*.md' for root in RECEIPT_ROOTS)
    if 'any-root' in MUTATE:
        paths = ('*.md',)
    if 'any-file' in MUTATE:
        paths = RECEIPT_ROOTS
    old = set() if 'old-text' in MUTATE else {line for _, line in receipt_lines(repo, base, ())}
    return {line[:2]: path for path, line in reversed(receipt_lines(repo, tip, paths)) if line not in old}


def find_receipt(edge, found):
    for (source, target), path in found.items():
        if ((source == edge['source'] or 'target-only' in MUTATE)
                and (target == edge['target'] or 'source-only' in MUTATE)):
            return path
    return None


def scan(repo, base_rev, tip_rev):
    base, tip = load(repo, base_rev, trusted='tip-only' in MUTATE), load(repo, tip_rev)
    base_f = solve(base)[0]
    gone = removed_edges(base, tip)
    world = with_retired(base, tip, gone)
    live = solve(world)[0]

    def against(edges):
        """Claims the given edges hold up, or None if restoring them closes a cycle."""
        try:
            held = held_up(live, solve(world, edges)[0])
        except lib.SolidityCycleError:
            return {} if 'cycle-passes' in MUTATE else None
        if 'rise-only' in MUTATE:
            return {c: v for c, v in held.items() if rank(live[c]) > rank(base_f.get(c))}
        return held

    singles = {pair(e): against([e]) for e in gone}
    cycle = {key for key, got in singles.items() if got is None}
    solvable = [e for e in gone if pair(e) not in cycle]
    while against(solvable) is None:
        # Edges no single restore catches can close a cycle together. Those whose omission
        # opens it are the cycle; if none does, more than one cycle is closed.
        stuck = [] if 'cycle-blames-all' in MUTATE else [
            e for e in solvable if against(rest(solvable, e)) is not None]
        stuck = stuck or solvable
        if 'joint-cycle-passes' not in MUTATE:
            cycle |= {pair(e) for e in stuck}
        solvable = [e for e in solvable if not any(e is s for s in stuck)]
    whole = {} if 'no-joint' in MUTATE else against(solvable)
    jointly = blame_jointly(singles, whole, solvable, lambda edges: solve(world, edges)[0])

    open_edges = [e for e in gone if pair(e) in cycle or singles[pair(e)] or pair(e) in jointly]
    found = receipts(repo, base_rev, tip_rev) if open_edges else {}
    findings = [{'edge': e, 'cycle': pair(e) in cycle, 'holds': singles[pair(e)] or {},
                 'jointly': jointly.get(pair(e), {}), 'receipt': find_receipt(e, found)}
                for e in open_edges]
    after = live if 'others-tip' in MUTATE else solve(world, solvable)[0]
    named = {c for f in findings for c in {**f['holds'], **f['jointly']}}
    others = [c for c in sorted(tip.claims) if c in base_f and rank(after[c]) > rank(base_f[c])
              and not ('others-skip-named' in MUTATE and c in named)]
    return {'gone': gone, 'findings': findings, 'others': others, 'base': base_f, 'tip': live,
            'after': after, 'retired': sorted(set(base.claims) - set(tip.claims))}


def show(value):
    return '*pending*' if value is None else '%g' % value


def reading(value):
    return '%s (%s)' % (lib.derive_build_band(value), show(value))


def report(res, base, tip):
    open_ = [f for f in res['findings'] if not f['receipt']]
    print('[solidity-ratchet] %s..%s  removed-edges=%d  band-holding=%d  receipted=%d  '
          'UNEXPLAINED=%d  retired-claims=%d  other-band-rises=%d (not gated)'
          % (base[:8], tip[:8], len(res['gone']), len(res['findings']),
             len(res['findings']) - len(open_), len(open_), len(res['retired']), len(res['others'])))
    for f in res['findings']:
        e = f['edge']
        print('\n  %s -x-> %s  %s' % (e['source'], e['target'],
                                      'receipt: ' + f['receipt'] if f['receipt'] else 'UNEXPLAINED'))
        if f['cycle']:
            print('     restoring it, alone or with the other removed edges, closes a cycle, so '
                  'its effect cannot be computed')
        name = lambda c: c + (' (gone from the tip)' if c in res['retired'] else '')
        for c, restored in sorted(f['holds'].items()):
            print('     holds %s at %s; restored it reads %s' % (
                name(c), reading(res['tip'][c]), reading(restored)))
        for c, restored in sorted(f['jointly'].items()):
            print('     with other removed edges, holds %s at %s; restored together they read %s' % (
                name(c), reading(res['tip'][c]), reading(restored)))
        if e.get('context'):
            print('     dropped: %s' % e['context'])
    for c in res['others']:
        print('\n  not gated: %s  %s -> %s  (%s -> %s)' % (
            c, lib.derive_build_band(res['base'][c]), lib.derive_build_band(res['after'][c]),
            show(res['base'][c]), show(res['after'][c])))
    for c in res['retired']:
        print('\n  gone from the tip: %s  %s' % (c, reading(res['base'][c])))
    if open_:
        print('\nFor each UNEXPLAINED edge: if the input still bears load, restore the edge, because '
              'a prose cap in the rationale is no alternative (PR #549). If the dependency is really '
              'gone, add this line to a Markdown file under %s on this branch:\n\n    %s <source> -> '
              '<target>: <why>' % (' or '.join(RECEIPT_ROOTS), TOKEN))
        return 1
    return 0


def main(base, tip, repo=None):
    try:
        dead = run_gate(out=lambda line: None)
        if dead:
            print('[solidity-ratchet] ABORT: self-gate failed -- a clean report here would be false.')
            for why in dead:
                print('  ' + why)
            return 2
        repo = repo or Repo(cwd=Repo().git('rev-parse', '--show-toplevel').strip())
        for rev in (base, tip):
            repo.git('rev-parse', '--verify', '%s^{tree}' % rev)
        res = scan(repo, base, tip)
        print('[solidity-ratchet] liveness OK -- both revs resolve and reproduce their recorded '
              'solidities, self-gate %d/%d.' % (len(CASES) + len(ABORTS), len(CASES) + len(ABORTS)))
        return report(res, base, tip)
    except Exception as e:
        traceback.print_exc()
        print('[solidity-ratchet] ABORT: %s: %s' % (type(e).__name__, e))
        return 2


# ------------------------------------------------------------------- fixtures
#
# One throwaway repo with hostile diff, grep and colour config. Trees are built with
# `git write-tree`: no commit, so no identity, no hooks, no signing.
#
#   WEAK 0.30 <- CITE 0.85 -> SOLID 0.90        DOWN 0.85 -> CITE
#   WEAK <- SUP1, SUP2 (quality 0.90) both supporting LIFT 0.10 in full
#   NEAR 0.80 -> NEAR2 0.70                     same band either way

WEAK, SOLID, CITE, DOWN, LIFT = 'clm-weak00', 'clm-solid0', 'clm-cite00', 'clm-down00', 'clm-lift00'
NEAR, NEAR2, SUP1, SUP2 = 'clm-near00', 'clm-near02', 'sup-one000', 'sup-two000'
X, Y, Z, M, M2, W = 'clm-xxxxxx', 'clm-yyyyyy', 'clm-zzzzzz', 'clm-mmmmmm', 'clm-nnnnnn', 'clm-wwwwww'
EXP = 'exp-one000'
NOTE = 'research/2026-01-01_fixture_result.md'
HOSTILE = (('diff.interHunkContext', '2'), ('grep.lineNumber', 'true'), ('grep.column', 'true'),
           ('color.ui', 'always'))


def graph_spec(claims, deps=(), sups=None, gives=(), exps=None, fraction=1.0):
    return {'claims': claims, 'sups': sups or {}, 'deps': list(deps), 'gives': list(gives),
            'exps': exps or {}, 'fraction': fraction}


def spec(**changes):
    s = graph_spec({WEAK: .30, SOLID: .90, CITE: .85, DOWN: .85, LIFT: .10, NEAR: .80, NEAR2: .70},
                   [(CITE, WEAK), (CITE, SOLID), (DOWN, CITE), (NEAR, NEAR2), (SUP1, WEAK), (SUP2, WEAK)],
                   {SUP1: .90, SUP2: .90}, [(SUP1, LIFT), (SUP2, LIFT)])
    s.update(changes)
    return s


def without(*pairs):
    return [d for d in spec()['deps'] if d not in pairs]


def tree(repo, root, s, files=(), stale=None, drop=(), blank=(), garble=None):
    def edge(a, b, relation, **extra):
        return {'source': a, 'target': b, 'relation': relation, 'target_kind': 'claim', **extra}
    edges = [edge(a, b, 'depends', context=None) for a, b in s['deps']]
    edges += [edge(a, b, 'supports', fraction=s['fraction']) for a, b in s['gives']]
    edges += [edge(x, c, 'strengthens', strength=v) for x, (_, gives) in s['exps'].items() for c, v in gives]
    nodes = [{'node_type': 'claim', 'id': c, 'confidence': v, 'solidity': None} for c, v in s['claims'].items()]
    nodes += [{'node_type': 'support', 'id': c, 'quality': v, 'solidity': None} for c, v in s['sups'].items()]
    nodes += [{'node_type': 'experiment', 'id': x, 'status': v[0]} for x, v in s['exps'].items()]
    finals, sups = solve(Graph(nodes, edges))
    for r in nodes:
        if r['node_type'] != 'experiment':
            r['solidity'] = (finals if r['node_type'] == 'claim' else sups).get(r['id'])
        if r['id'] == stale:
            r['solidity'] = 0.99
    nodes = [r for r in nodes if r['id'] not in drop]
    texts = {CLAIMS: '\n'.join(map(json.dumps, nodes)) + '\n',
             EDGES: '\n'.join(map(json.dumps, edges)) + '\n'}
    texts.update({path: '' for path in blank})
    if garble:
        texts[garble] += '{"truncated\n'
    for p in Path(root).iterdir():
        if p.name != '.git':
            shutil.rmtree(p) if p.is_dir() else p.unlink()
    for path, text in list(texts.items()) + list(files):
        Path(root, path).parent.mkdir(parents=True, exist_ok=True)
        Path(root, path).write_text(text, encoding='utf-8')
    repo.git('add', '-A')
    return repo.git('write-tree').strip()


CUT = (CITE, WEAK)
SUPS = ((SUP1, WEAK), (SUP2, WEAK))
CUTTING = spec(deps=without(CUT))
LINE = '%s %s -> %s: the bound no longer applies' % (TOKEN, CITE, WEAK)
NEARBY = 'l1\nl2\nl3\nl4\nl5\nl6\n'


def case(tip=None, files=(), base=None, base_files=(), rc=0, flagged=(), others=()):
    return {'tip': spec() if tip is None else tip, 'files': files, 'rc': rc,
            'base': spec() if base is None else base, 'base_files': base_files,
            'flagged': set(flagged), 'others': set(others)}


def fired(tip, *pairs, **rest_of_it):
    return case(tip, rc=1, flagged=pairs, **rest_of_it)


def note(text, path=NOTE):
    return ((path, text + '\n'),)


CLAIMS_OF = spec()['claims']
RAISED = {WEAK, CITE, DOWN, LIFT}
SERIES = graph_spec({X: .90, M: .90, W: .30, Z: .50}, [(X, M), (M, W), (X, Z)])
TWO_ROUTES = graph_spec({X: .90, M: .90, M2: .90, W: .30}, [(X, M), (X, M2), (M, W), (M2, W)])
LOOP = graph_spec({X: .90, Y: .90, Z: .90, M: .90, M2: .90, W: .90}, [(X, Y), (Z, M), (M2, W)])
CHAIN = graph_spec({X: .85, M: .90, Z: .90}, [(X, M), (M, Z)])
SHARED = graph_spec({W: .30, X: .10, Y: .10, Z: .10}, [(SUP1, W), (SUP2, W)], {SUP1: .90, SUP2: .90},
                    [(SUP1, X), (SUP2, X), (SUP1, Y), (SUP2, Z)])
MASKED = graph_spec({X: .10, M: .50, W: .30}, [(X, M), (SUP1, W), (SUP2, W)], {SUP1: .90, SUP2: .90},
                    [(SUP1, X), (SUP2, X)])
STRONG = {EXP: ('run', [(CITE, .90)])}
OLD_SUP = graph_spec({X: .10, W: .30}, [(SUP1, W)], {SUP1: .90}, [(SUP1, X)])

#: name -> what the fixture must give. Verdicts are reasoned by hand from the min rule.
CASES = {
    'unchanged':          case(),
    'cut-binding':        fired(CUTTING, CUT),
    'cut-slack':          case(spec(deps=without((CITE, SOLID)))),
    'cut-within-band':    case(spec(deps=without((NEAR, NEAR2)))),
    'cut-plus-slack':     fired(spec(deps=without(CUT, (CITE, SOLID))), CUT),
    'add-edge':           case(spec(deps=spec()['deps'] + [(DOWN, SOLID)])),
    'raised-confidence':  case(spec(claims={**CLAIMS_OF, WEAK: .90}), others=RAISED),
    'no-longer-binding':  case(spec(deps=without(CUT), claims={**CLAIMS_OF, CITE: .25})),
    'held-against-fall':  fired(spec(deps=without(CUT), claims={**CLAIMS_OF, WEAK: .10, CITE: .40}), CUT),
    'rise-by-two-routes': fired(spec(deps=without(CUT), claims={**CLAIMS_OF, WEAK: .60}), CUT,
                                base=spec(claims={**CLAIMS_OF, WEAK: .60, CITE: .30}), others={CITE, DOWN}),
    'pending-target':     fired(spec(deps=without(CUT), claims={**CLAIMS_OF, WEAK: None}), CUT,
                                base=spec(claims={**CLAIMS_OF, WEAK: None})),

    'receipt':            case(CUTTING, note(LINE), flagged=[CUT]),
    'receipt-list-item':  case(CUTTING, note('  - ' + LINE), flagged=[CUT]),
    'receipt-docket':     case(CUTTING, note(LINE, '_orchestration/docket-entries/2026-01-01_x.md'), flagged=[CUT]),
    'receipt-other-edge': fired(CUTTING, CUT, files=note('%s %s -> %s: why' % (TOKEN, CITE, SOLID))),
    'receipt-target-only': fired(CUTTING, CUT, files=note('%s %s -> %s: why' % (TOKEN, DOWN, WEAK))),
    'receipt-no-reason':  fired(CUTTING, CUT, files=note('%s %s -> %s:' % (TOKEN, CITE, WEAK))),
    'receipt-mid-line':   fired(CUTTING, CUT, files=note('as noted, ' + LINE)),
    'receipt-prose':      fired(CUTTING, CUT, files=note('%s still rests on %s' % (CITE, WEAK))),
    'receipt-wrong-root': fired(CUTTING, CUT, files=note(LINE, 'manuscript/ave-kb/vol1/claim-quality.md')),
    'receipt-json':       fired(CUTTING, CUT, files=note(LINE, 'research/lane_results.json')),
    'receipt-old-line':   fired(CUTTING, CUT, base_files=note(LINE), files=note(LINE)),
    'receipt-touched':    fired(CUTTING, CUT, base_files=note(LINE), files=note(LINE + ' ')),
    'receipt-moved-in':   fired(CUTTING, CUT, base_files=note(LINE, 'notes/old.md'), files=note(LINE)),
    'receipt-new-reason': case(CUTTING, note(LINE + ', again'), base_files=note(LINE), flagged=[CUT]),

    'retired-binding':    fired(spec(deps=without(CUT, *SUPS),
                                     claims={k: v for k, v in CLAIMS_OF.items() if k != WEAK}),
                                CUT, *SUPS),
    'retired-slack':      case(spec(deps=without((CITE, SOLID)),
                                    claims={**{k: v for k, v in CLAIMS_OF.items() if k != SOLID}, WEAK: .90}),
                               others=RAISED),
    'retired-dep-moved':  fired(graph_spec({X: .85, Z: .10}), (X, M), (M, Z), base=CHAIN),
    'retired-clean':      case(graph_spec({X: .85, Z: .90}), base=CHAIN),
    'remint-no-citers':   fired(graph_spec({Y: .95, W: .63}), (X, W), base=graph_spec({X: .95, W: .63}, [(X, W)])),
    'remint-citers':      fired(graph_spec({Y: .90, W: .55, Z: .90}, [(Z, Y)]), (X, W), (Z, X),
                                base=graph_spec({X: .90, W: .55, Z: .90}, [(X, W), (Z, X)])),
    'remint-support':     case(graph_spec({X: .10, W: .30}, sups={SUP2: .90}, gives=[(SUP2, X)]),
                               base=OLD_SUP, others={X}),
    'dep-becomes-support': fired(spec(deps=without(SUPS[0]), gives=spec()['gives'] + [SUPS[0]]), SUPS[0],
                                 others=RAISED),

    'reversed-edge':      fired(spec(deps=without(CUT) + [(WEAK, CITE)]), CUT, others={CITE, DOWN}),
    'joint-only':         fired(spec(deps=without(*SUPS)), *SUPS),
    'joint-plus-slack':   fired(spec(deps=without((CITE, SOLID), *SUPS)), *SUPS),
    'joint-masked-parallel': fired(graph_spec(MASKED['claims'], sups=MASKED['sups'], gives=MASKED['gives']),
                                   (X, M), *((s, W) for s in (SUP1, SUP2)), base=MASKED),
    'joint-masked-series': fired(graph_spec(SERIES['claims']), (X, M), (M, W), (X, Z), base=SERIES),
    'joint-two-routes':   fired(graph_spec(TWO_ROUTES['claims']), (X, M), (X, M2), (M, W), (M2, W), base=TWO_ROUTES),
    'joint-not-mislabelled': fired(graph_spec(SHARED['claims'], sups=SHARED['sups'], gives=SHARED['gives']),
                                   (SUP1, W), (SUP2, W), base=SHARED),
    'joint-cycle':        fired(graph_spec(LOOP['claims'], [(Y, Z), (M, X), (M2, W)]), (X, Y), (Z, M),
                                base=LOOP),
    'joint-cycle-plus-slack': fired(graph_spec(LOOP['claims'], [(Y, Z), (M, X)]), (X, Y), (Z, M), base=LOOP),

    'exp-rescue':         case(spec(deps=without(CUT), exps=STRONG), base=spec(exps=STRONG)),
    'exp-unrun':          fired(spec(deps=without(CUT), exps={EXP: ('pending', STRONG[EXP][1])}), CUT,
                                base=spec(exps={EXP: ('pending', STRONG[EXP][1])})),
    'sup-pending-fraction': case(spec(deps=without(*SUPS), fraction='*pending*'), base=spec(fraction='*pending*')),
    'sup-fraction':       fired(spec(deps=without(*SUPS), fraction=.5), *SUPS, base=spec(fraction=.5)),
}

#: name -> (tree() arguments for the base, for the tip). Each must abort.
ABORTS = {
    'stale-index':   ({}, {'stale': WEAK}),
    'stale-support': ({}, {'stale': SUP1}),
    'stale-base':    ({'stale': WEAK}, {}),
    'empty-tip':     ({}, {'blank': (CLAIMS, EDGES)}),
    'empty-base':    ({'blank': (CLAIMS, EDGES)}, {}),
    'orphan-edge':   ({}, {'drop': (NEAR,)}),
    'bad-json':      ({}, {'garble': EDGES}),
}


def run_case(repo, root, name):
    c = CASES[name]
    base = tree(repo, root, c['base'], c['base_files'])
    tip = tree(repo, root, c['tip'], c['files'])
    res = scan(repo, base, tip)
    got = {pair(f['edge']) for f in res['findings']}
    rc = 1 if any(not f['receipt'] for f in res['findings']) else 0
    return rc == c['rc'] and got == c['flagged'] and set(res['others']) == c['others']


def run_abort(repo, root, name):
    base_args, tip_args = ABORTS[name]
    base, tip = tree(repo, root, spec(), **base_args), tree(repo, root, spec(), **tip_args)
    try:
        scan(repo, base, tip)
    except GateError:
        return True
    return False


def run_gate(out=print, only=None):
    """Every fixture verdict and every owed abort, or just `only`. Returns what failed."""
    root = tempfile.mkdtemp(prefix='solidity-ratchet-selftest-')
    failed = []
    try:
        repo = Repo(cwd=root, scrub_env=True)
        repo.git('init', '-q')
        for key, value in HOSTILE:
            repo.git('config', key, value)
        for name, run in [(n, run_case) for n in CASES] + [(n, run_abort) for n in ABORTS]:
            if only and name not in only:
                continue
            try:
                ok = run(repo, root, name)
            except (GateError, lib.SolidityCycleError) as e:
                ok, why = False, ' (%s)' % e
            else:
                why = ''
            out('  [%s] %s%s' % ('OK' if ok else 'BROKEN', name, why))
            if not ok:
                failed.append('fixture verdict wrong: %s%s' % (name, why))
    finally:
        shutil.rmtree(root, ignore_errors=True)
    return failed


def selftest():
    print('[solidity-ratchet] SELF-GATE')
    failed = run_gate()
    if failed:
        print('[solidity-ratchet] SELF-GATE FAILED: %s' % '; '.join(failed))
        return 1
    print('[solidity-ratchet] SELF-GATE OK: %d fixtures and %d aborts.' % (len(CASES), len(ABORTS)))
    return 0


#: mutation -> (the fixtures switching it off must break, what it switches off).
MUTATIONS = {
    'no-restore':         (('cut-binding',), 'stop finding removed edges'),
    'any-rise':           (('cut-within-band',), 'gate on any solidity rise instead of a band rise'),
    'rise-only':          (('held-against-fall',), 'exempt a cut that only stops a claim falling'),
    'source-only':        (('receipt-other-edge',), 'accept a receipt for another edge of the source'),
    'target-only':        (('receipt-target-only',), 'accept a receipt for another edge into the target'),
    'no-reason':          (('receipt-no-reason',), 'accept a receipt with no reason'),
    'token-anywhere':     (('receipt-mid-line',), 'accept a receipt that is not at the start of a line'),
    'any-root':           (('receipt-wrong-root',), 'accept a receipt outside the reviewed roots'),
    'any-file':           (('receipt-json',), 'accept a receipt in a file that is not Markdown'),
    'old-text':           (('receipt-old-line', 'receipt-touched', 'receipt-moved-in'),
                           'accept a receipt the base tree already holds'),
    'no-grep-pin':        (('receipt',), 'read receipts under the user\'s grep and colour config'),
    'no-stub':            (('retired-slack',), 'restore edges to retired claims as pending'),
    'skip-retired':       (('retired-dep-moved', 'remint-no-citers', 'remint-citers'),
                           'skip edges whose source left the index'),
    'kept-any-relation':  (('dep-becomes-support',), 'count a non-depends edge as keeping a dependency'),
    'cycle-passes':       (('reversed-edge',), 'treat an edge that cannot be restored as harmless'),
    'joint-cycle-passes': (('joint-cycle',), 'treat edges that close a cycle together as harmless'),
    'cycle-blames-all':   (('joint-cycle-plus-slack',), 'blame every removed edge for a cycle'),
    'no-joint':           (('joint-only',), 'test edges only one at a time'),
    'membership':         (('joint-masked-parallel', 'joint-masked-series'),
                           'let a claim named by one edge hide a lower joint reading'),
    'blame-all':          (('joint-plus-slack',), 'blame every removed edge for a joint effect'),
    'no-sufficiency':     (('joint-two-routes',), 'trust leave-one-out when several sets reach the band'),
    'others-tip':         (('joint-not-mislabelled',), 'call a rise not gated without restoring the edges'),
    'others-skip-named':  (('rise-by-two-routes',), 'hide the not-gated share of a flagged claim'),
    'no-experiments':     (('exp-rescue',), 'solve without run experiments'),
    'fraction-one':       (('sup-pending-fraction',), 'read a pending on-point fraction as 1'),
    'no-reconcile':       (('stale-index',), 'skip the reconcile'),
    'claims-only':        (('stale-support',), 'reconcile claims and not supports'),
    'tip-only':           (('stale-base',), 'reconcile the tip and not the base'),
    'allow-empty':        (('empty-tip', 'empty-base'), 'accept an index with no claims'),
    'allow-orphans':      (('orphan-edge',), 'accept an edge whose node is missing'),
    'skip-bad-json':      (('bad-json',), 'drop an unparseable index line'),
}


def mutation_receipt():
    print('[solidity-ratchet] MUTATION RECEIPT -- each listed rule, switched off, must break its fixtures')
    allgood = True
    for mutation, (cases, label) in MUTATIONS.items():
        MUTATE.add(mutation)
        try:
            failed = run_gate(out=lambda line: None, only=cases)
        finally:
            MUTATE.discard(mutation)
        tripped = len(failed) == len(cases)
        print('  [%s] %s -> %s' % ('OK' if tripped else 'BROKEN', label, ', '.join(cases)))
        allgood = allgood and tripped
    if not allgood:
        print('[solidity-ratchet] MUTATION RECEIPT FAILED')
        return 1
    print('[solidity-ratchet] MUTATION RECEIPT OK: %d rules, each switched off, broke their fixtures.'
          % len(MUTATIONS))
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
