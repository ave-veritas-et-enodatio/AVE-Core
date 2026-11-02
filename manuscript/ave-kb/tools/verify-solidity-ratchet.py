#!/usr/bin/env python3
"""Solidity ratchet.

Solidity is `min` over a claim's declared dependencies, so deleting the weakest
`depends-on` bullet lifts the claim and everything downstream of it. No other gate
compares solidity across revs: refresh regenerates the index, the verifier finds it
fresh, and `make verify` stays green, while the cite-shift gate fires only if the
deletion moves a cited line. Measured at cbc668e7: of 408 `depends` edges into a claim,
removing any one of 53 moves the citing claim up a build band.

The one question: of the `depends` edges into a claim that the merge-base has and the tip
does not, put back every one with no receipt, together and each alone, and re-solve the
tip. If that lowers any claim's band, a deletion is holding the band up and the branch
owes a receipt. A receipted edge stays off while the rest are tested, so an edge that
binds only through it goes slack and owes nothing, and an edge that binds without it
still fires. The test is against the restored solve and not the base band, because the
same cut also stops a claim falling when its dependency was downgraded, and there the
band never rises at all. Pending ranks lowest, because None is the bottom of the solve's
min and max.

A claim that left the index is tested as if it had stayed at its base confidence, with
its authored lifts and without those edges, so nothing here pairs an old id with a new
one. A re-mint or a split owes a receipt whenever the edge binds at that confidence, even
if the new id keeps the dependency, and so does a deleted leaf. Measured at cbc668e7:
renaming any one of 73 of the 331 claims fires and owes 1 to 4 receipts, 107 edges in
all, though ids are stable (INVARIANT-S8) and no claim left the index across the 113
index changes measured.

THE RECEIPT
-----------
A line in a Markdown file at a path the base tree does not have, under research/ or
_orchestration/docket-entries/ and outside any _archive/ directory, reading

    dep-removed: <source> -> <target>: <why>

One edge per line, with nothing before `dep-removed:` but indentation or a `- ` or `* `
marker. The rule reads lines and not Markdown, so a line in a code fence or a comment
counts. No base text line holding the token, in any case, may also hold both ids and the
reason, whitespace aside. So an old line moved, quoted, re-indented or left in a one-line
dump does not count, nor does a fragment of its reason, and a changed word makes a new
reason. Not seen: a dump that escapes the reason, a line wrapped in two, a binary file.
Ids match as substrings, which is exact while every id has one length, as all do today.
The path test keeps the line out of any document the base has. A rename is a new path, so
it passes and shows in the diff. The gate checks only that a reason is present and new:
it forces the deletion into the open and leaves judging it to review. The claim's own
entry cannot carry the line, because that entry is the edit under test and a line there
folds into its rationale. A line that holds the token and both ids of an edge still owed,
in either order, but is no receipt for it, is reported under that edge with why.

WHAT IT DOES NOT GATE
---------------------
Raised confidence, raised support quality or on-point fraction, run experiments, and a
support added or re-minted under a new id all lift bands too. Those are authored
judgments, visible where they are written. For that report the removed edges go back in
index order, leaving out any that would close a cycle with those already back and any
whose source support left the tip. A rise that survives is printed as `not gated`, so a
claim that rose both ways shows both. With any edge left out it prints as `not tested`,
and the edges left out are named, since what they hold or lift does not show. A claim the
removed edges hold lower than any listed line shows, as when receipted edges carry it,
prints too. Every claim new at the tip is printed, since a re-mint that also raises
confidence clears the fire. Each branch is judged against its own merge-base, so a rise
split across two branches is not joined up.

THE SOLVE
---------
The graph is rebuilt from the committed `.index/` of each rev and solved by
kb_index_lib.compute_solidity_full, the one computation behind the published values.
Before any verdict both revs must hold at least one claim, every edge must name nodes the
rev holds, and every recorded solidity must reproduce exactly. A rev that fails is empty,
truncated or stale, or this reconstruction has drifted; either way a clean report would
be false, so the run aborts. An index that lost a line without orphaning an edge or moving
a value passes here, and the verifier's freshness check in `make verify` catches it.

That function rounds a reading only when the claim has deps, where SCHEMA.md states it
unconditionally, so a slack edge can round a fractional lift up across a band. A subset
of the edges can then read lower than the whole set, and a receipt on a slack edge can
turn exit 0 into exit 1 with no band moved. Exit 0 rests on each edge and the whole set,
not on every subset. No value at cbc668e7 reaches this: no support has a numeric quality.

Exit codes: 0 no unexplained lift, 1 at least one, 2 the gate itself could not run. In
every mode a crash or a fixture that raises is a 2: an uncaught traceback exits 1, which
would read as a verdict. A `warning:` from git grep is ignored and anything else on its
stderr aborts, so a partial clone that has to fetch can exit 2 until it has the blobs.

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
    #: Band names, lowest first, read off the library so a renamed band needs no edit here.
    BANDS = list(dict.fromkeys(
        [lib.derive_build_band(None)] + [lib.derive_build_band(n / 100) for n in range(101)]))
except Exception as e:
    print('[solidity-ratchet] ABORT: cannot use kb_index_lib: %s' % e)
    sys.exit(2)

CLAIMS = 'manuscript/ave-kb/.index/claims.jsonl'
EDGES = 'manuscript/ave-kb/.index/depends-on.jsonl'
RECEIPT_ROOTS = ('research/', '_orchestration/docket-entries/')
TOKEN = 'dep-removed:'

_ID = r'[a-z]{3}-[a-z0-9]+'
MENTION = re.compile(r'%s\s*(%s)\s*->\s*(%s)\s*:([^\r]*)' % (TOKEN, _ID, _ID))
RECEIPT = re.compile(r'\s*(?:[-*]\s+)?' + MENTION.pattern)

#: Rules switched OFF by --mutation-receipt. Empty in every real run.
MUTATE = set()


class GateError(Exception):
    """The machinery failed. A clean report past this point would be false."""


class Repo:
    """A git repo handle. Fixtures scrub GIT_* so a hook's GIT_DIR cannot reach the real repo,
    and a real run scrubs GIT_TRACE*, which writes to stderr."""

    def __init__(self, cwd=None, scrub_env=False):
        scrub = 'GIT_' if scrub_env else 'GIT_TRACE'
        self.cwd, self.env = cwd, {k: v for k, v in os.environ.items() if not k.startswith(scrub)}

    def git(self, *args, ok=(0,), strict=False):
        """Stdout with its bytes kept, so a bare CR stays in its line. `strict` also fails on
        stderr past any `warning:`: grep reports an unreadable blob only there."""
        p = subprocess.run(('git',) + args, cwd=self.cwd, env=self.env, capture_output=True)
        stderr = p.stderr.decode('utf-8', 'replace')
        if p.returncode not in ok or (strict and any(
                not line.startswith('warning:') for line in stderr.splitlines())):
            raise GateError('git %s exited %d: %s' % (' '.join(args), p.returncode, stderr.strip()))
        return p.stdout.decode('utf-8', 'replace')


class Graph:
    """One rev's claim graph, as its committed index records it."""

    def __init__(self, nodes, edges):
        self.ids = {r['id'] for r in nodes}
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
    orphans = [e for e in graph.edges if e['source'] not in graph.ids or e['target'] not in graph.ids]
    if orphans and 'allow-orphans' not in MUTATE:
        raise GateError('%s: %d edges name a node the index does not hold, so it is '
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


def load(repo, rev, reconciled=True):
    try:
        graph = Graph(records(repo, rev, CLAIMS), records(repo, rev, EDGES))
        check_whole(graph, rev)
        if reconciled:
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
    """`depends` edges into a claim at the base and not the tip, one per (source, target)."""
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
    too, with the supports and experiments behind them. Tip records win, and a tip edge
    always has its node (check_whole), so a tip claim reads here what it reads at the tip.
    """
    back = {n for e in gone for n in pair(e)} & (set(base.claims) - set(tip.claims))
    if 'no-stub' in MUTATE:
        back = set()
    if 'all-retired' in MUTATE:
        back = set(base.claims) - set(tip.claims)
    kinds = ('supports',) if 'no-exp-lifts' in MUTATE else ('supports', 'strengthens')
    lifts = [e for e in base.edges if e['target'] in back and e['relation'] in kinds]
    sources = {e['source'] for e in lifts}
    world = Graph([], tip.edges + lifts)
    world.claims = {**{c: base.claims[c] for c in back}, **tip.claims}
    for name in ('supports', 'experiments'):
        was = {i: r for i, r in getattr(base, name).items() if i in sources}
        now = getattr(tip, name)
        setattr(world, name, {**now, **was} if 'stale-lifts' in MUTATE else {**was, **now})
    return world


def held_up(tip, restored):
    """Claims whose band the restored solve takes away, with what they would read."""
    if 'any-rise' in MUTATE:
        return {c: restored[c] for c, v in tip.items() if v != restored[c]}
    if 'any-move' in MUTATE:
        return {c: restored[c] for c, v in tip.items() if rank(v) != rank(restored[c])}
    return {c: restored[c] for c, v in tip.items() if rank(v) > rank(restored[c])}


def split_cycles(edges, read):
    """(edges that restore together, {(source, target): 'alone' or 'jointly'} for the rest,
    (source, target) -> the other edges of its cycle).

    `read` returns None for a set that closes a cycle. Such a set is cut down, edge by
    edge, to the ones that still close it, so an edge with no part in the cycle goes back
    with the others. The loop takes the separate cycles one at a time.
    """
    free, cycle, loops = [], {}, {}
    for e in edges:
        if read([e]) is not None:
            free.append(e)
        elif 'cycle-passes' not in MUTATE:
            cycle[pair(e)] = 'alone'
    while read(free) is None:
        closing = free
        if 'cycle-blames-all' not in MUTATE:
            for e in free:
                if read(rest(closing, e)) is None:
                    closing = rest(closing, e)
        if 'joint-cycle-passes' not in MUTATE:
            cycle.update((pair(e), 'jointly') for e in closing)
            loops.update((pair(e), [pair(o) for o in rest(closing, e)]) for e in closing)
        free = [e for e in free if not any(e is c for c in closing)]
    return free, cycle, loops


def owed(edges, singles, against, read):
    """(the `edges` that hold a band, edge -> {claim: reading} held only with other edges,
    (edge, claim) -> the other edges of that set).

    Singles do not bound the joint: two supports can each hold a claim up alone, and two
    edges in series bind only together. So a claim the whole set takes below every single
    is blamed on a minimal set: each edge is dropped if the rest still reach that band,
    which leaves a bystander unnamed. What was named is then set aside and the remainder
    tested again, so one report lists all that is owed and not one layer a run.
    """
    left, flagged, jointly, partners = list(edges), [], {}, {}
    while True:
        lowest = {}
        for e in left:
            for c, v in singles[pair(e)].items():
                lowest[c] = min(lowest.get(c, rank(v)), rank(v))
        whole = {} if 'no-joint' in MUTATE else against(left)
        for c, v in whole.items():
            if rank(v) < lowest.get(c, len(BANDS)):
                need = left
                if 'blame-all' not in MUTATE:
                    for e in left:
                        if rank(read(rest(need, e))[c]) <= rank(v):
                            need = rest(need, e)
                for e in need:
                    jointly.setdefault(pair(e), {})[c] = read(need)[c]
                    partners[pair(e), c] = [pair(o) for o in rest(need, e)]
        hit = [e for e in left if singles[pair(e)] or pair(e) in jointly]
        if not hit:
            return flagged, jointly, partners
        flagged += hit
        left = [e for e in left if not any(e is h for h in hit)]
        if 'one-layer' in MUTATE:
            return flagged, jointly, partners


def token_lines(repo, tree):
    """(path, text) for each text line in `tree` holding the token, in any case.

    A path can hold a newline and a line can hold a NUL, so a row is read up to its NUL and
    then up to its newline. `-z` keeps git from quoting the path.
    """
    pins = () if 'no-grep-pin' in MUTATE else ('--no-color', '--no-line-number', '--no-column')
    fold = () if 'token-case' in MUTATE else ('-i',)
    out = repo.git('grep', '-I', '-z', *fold, *pins, '-F', '-e', TOKEN, tree, '--', ok=(0, 1),
                   strict='grep-stderr-ok' not in MUTATE)
    return [(where.split(':', 1)[1], text) for where, text in re.findall(r'([^\0]*)\0([^\n]*)\n', out)]


def refusal(path, edge, reason, old, at_base):
    """Why a line naming `edge` is no receipt for it, or None. No `reason`: it is not its line."""
    if reason is None:
        return ('it does not read `%s %s -> %s: <why>`, one edge to a line, with only indentation '
                'or a `- ` or `* ` marker before it' % (TOKEN, *edge))
    if not (path.startswith(RECEIPT_ROOTS) or 'any-root' in MUTATE):
        return 'it is not under %s' % ' or '.join(RECEIPT_ROOTS)
    if not (path.endswith('.md') or 'any-file' in MUTATE):
        return 'it is not in a .md file'
    if '/_archive/' in path and 'archived' not in MUTATE:
        return 'it is in an _archive/ directory'
    if path in at_base and 'old-file' not in MUTATE:
        return 'the base has this file, and a receipt goes in a new one'
    if not (reason.lower() != '<why>' and any(ch.isalnum() for ch in reason) or 'no-reason' in MUTATE):
        return 'it gives no reason'
    if 'old-text' not in MUTATE and any(all(i in was for i in edge) and reason in was for was in old):
        return 'a base line holding %s already holds both ids and this reason' % TOKEN
    return None


def receipts(repo, base, tip, gone):
    """({(source, target): path} for each receipt, {(source, target): [(path, why not)]})."""
    base_tree, tip_tree = (repo.git('rev-parse', rev + '^{tree}').strip() for rev in (base, tip))
    at_base = set(repo.git('ls-tree', '-r', '--name-only', '-z', base_tree).split('\0'))
    old = [' '.join(text.split()) for _, text in token_lines(repo, base_tree)]
    found, refused = {}, {}
    for path, text in token_lines(repo, tip_tree):
        line = MENTION.search(text) if 'token-anywhere' in MUTATE else RECEIPT.match(text)
        parsed = line.group(1, 2) if line else None
        for edge in {parsed} - {None} | {p for p in map(pair, gone) if p[0] in text and p[1] in text}:
            reason = ' '.join(line[3].split()) if edge == parsed else None
            why = refusal(path, edge, reason, old, at_base)
            if why:
                refused.setdefault(edge, []).append((path, why))
            else:
                found.setdefault(edge, path)
    return found, refused


def find_receipt(edge, found):
    for (source, target), path in found.items():
        if ((source == edge['source'] or 'target-only' in MUTATE)
                and (target == edge['target'] or 'source-only' in MUTATE)):
            return path
    return None


def scan(repo, base_rev, tip_rev):
    base, tip = load(repo, base_rev, reconciled='tip-only' not in MUTATE), load(repo, tip_rev)
    base_f = solve(base)[0]
    gone = removed_edges(base, tip)
    world = with_retired(base, tip, gone)
    live = solve(world)[0]

    def read(edges):
        """Finals with `edges` restored, or None if they close a cycle."""
        try:
            return solve(world, edges)[0]
        except lib.SolidityCycleError:
            return None

    def against(edges):
        """Claims the given edges hold up."""
        held = held_up(live, read(edges))
        if 'rise-only' in MUTATE:
            return {c: v for c, v in held.items() if rank(live[c]) > rank(base_f.get(c))}
        return held

    found, refused = receipts(repo, base_rev, tip_rev, gone) if gone else ({}, {})
    paths = {pair(e): find_receipt(e, found) for e in gone}
    singles = {pair(e): {} if read([e]) is None else against([e]) for e in gone}
    free, cycle, loops = split_cycles(gone if 'no-residual' in MUTATE else
                                      [e for e in gone if not paths[pair(e)]], read)
    flagged, jointly, partners = owed(free, singles, against, read)
    listed = {pair(e) for e in flagged} | set(cycle)
    findings = [{'edge': e, 'cycle': cycle.get(pair(e)), 'loop': loops.get(pair(e), []),
                 'holds': singles[pair(e)],
                 'jointly': jointly.get(pair(e), {}), 'receipt': paths[pair(e)],
                 'partners': {c: partners[pair(e), c] for c in jointly.get(pair(e), {})},
                 'refused': refused.get(pair(e), [])}
                for e in gone if pair(e) in listed or paths[pair(e)]]
    known, restorable = world.claims.keys() | tip.supports.keys(), []
    for e in gone:
        if e['source'] in known and read(restorable + [e]) is not None:
            restorable.append(e)
    after = live if 'others-tip' in MUTATE else read(restorable)
    shown = {}
    for f in findings:
        for c, v in list(f['holds'].items()) + list(f['jointly'].items()):
            shown[c] = min(shown.get(c, len(BANDS)), rank(v))
    others = [c for c in sorted(tip.claims) if c in base_f
              and rank(after[c]) > rank(base_f[c]) and rank(live[c]) > rank(base_f[c])
              and not ('others-skip-named' in MUTATE and c in shown)]
    return {'gone': gone, 'findings': findings, 'others': others, 'base': base_f, 'tip': live,
            'after': after, 'retired': sorted(set(base.claims) - set(tip.claims)),
            'carried': [c for c in sorted(held_up(live, after)) if rank(after[c]) < shown.get(c, len(BANDS))],
            'new': sorted(set(tip.claims) - set(base.claims)),
            'stuck': [pair(e) for e in gone if not any(e is r for r in restorable)]}


def show(value):
    return '*pending*' if value is None else '%g' % value


def reading(value):
    return '%s (%s)' % (lib.derive_build_band(value), show(value))


def edges(pairs):
    return ', '.join('%s -> %s' % p for p in pairs)


def report(res, base, tip):
    open_ = [f for f in res['findings'] if not f['receipt']]
    verb = 'not tested' if res['stuck'] and res['others'] else 'not gated'
    print('[solidity-ratchet] %s..%s  removed-edges=%d  listed=%d  receipted=%d  UNEXPLAINED=%d  '
          'retired-claims=%d  new-claims=%d  other-band-rises=%d (%s)'
          % (base[:8], tip[:8], len(res['gone']), len(res['findings']),
             len(res['findings']) - len(open_), len(open_), len(res['retired']), len(res['new']),
             len(res['others']), verb))
    name = lambda c: c + (' (gone from the tip, read as if it stayed)' if c in res['retired'] else '')
    for f in res['findings']:
        e = f['edge']
        print('\n  %s -x-> %s  %s' % (e['source'], e['target'],
                                      'receipt: ' + f['receipt'] if f['receipt'] else 'UNEXPLAINED'))
        if f['cycle'] == 'alone':
            print('     restoring it closes a cycle, so its effect cannot be computed')
        elif f['cycle'] == 'jointly':
            print('     restoring it with %s closes a cycle, so they cannot go back together'
                  % edges(f['loop']))
        for c, restored in sorted(f['holds'].items()):
            print('     holds %s at %s; restored it reads %s' % (
                name(c), reading(res['tip'][c]), reading(restored)))
        for c, restored in sorted(f['jointly'].items()):
            print('     with %s, holds %s at %s; restored together it reads %s' % (
                edges(f['partners'][c]), name(c), reading(res['tip'][c]), reading(restored)))
        if not f['receipt']:
            for path, why in f['refused']:
                print('     the line in %s does not count: %s' % (path, why))
        if e.get('context'):
            print('     dropped: %s' % e['context'])
    for c in res['others']:
        print('\n  %s: %s  %s -> %s  (%s -> %s)' % (
            verb, c, lib.derive_build_band(res['base'][c]), lib.derive_build_band(res['after'][c]),
            show(res['base'][c]), show(res['after'][c])))
    if res['stuck']:
        print('\n  left out of the restore: %s. What they hold or lift does not show here.'
              % edges(res['stuck']))
    for c in res['carried']:
        print('\n  held up by the removed edges: %s at %s; with them back it reads %s' % (
            name(c), reading(res['tip'][c]), reading(res['after'][c])))
    for c in res['retired']:
        print('\n  gone from the tip: %s  %s' % (c, reading(res['base'][c])))
    for c in res['new']:
        print('\n  new at the tip: %s  %s' % (c, reading(res['tip'][c])))
    if open_:
        print(ADVICE % (' or '.join(RECEIPT_ROOTS), TOKEN))
        return 1
    return 0


ADVICE = """
Each UNEXPLAINED edge is one of these:
  - The input still bears load: restore the edge. The solver reads no prose, so a cap
    written in the rationale changes nothing.
  - Its source or target left the index: the edge cannot come back under that id, even if
    a new id keeps the dependency. Add the line below.
  - Restoring it closes a cycle, alone or with the edges printed: break a tip edge on that
    loop, after which the edges are tested, or add the line below.
  - The dependency is really gone: add the line below.

The line starts a line of a new Markdown file under %s, committed on this branch, with a
reason the base does not already hold. A file in docket-entries/ keeps that directory's
shape: `YYYY-MM-DD-<lane-slug>.md`, holding its `### ENTRY` block.

    %s <source> -> <target>: <why>"""


def guarded(mode):
    """Make any crash in `mode` an exit 2."""
    def run(*args, **kwargs):
        try:
            return mode(*args, **kwargs)
        except Exception as e:
            traceback.print_exc()
            print('[solidity-ratchet] ABORT: %s: %s' % (type(e).__name__, e))
            return 2
    return run


@guarded
def main(base, tip, repo=None):
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


# ------------------------------------------------------------------- fixtures
#
# One throwaway repo with hostile grep, colour and ignore config. Trees are built with
# `git write-tree`: no commit, so no identity, no hooks, no signing.
#
#   WEAK 0.30 <- CITE 0.85 -> SOLID 0.90        DOWN 0.85 -> CITE
#   WEAK <- SUP1, SUP2 (quality 0.90) both supporting LIFT 0.10 in full
#   NEAR 0.80 -> NEAR2 0.70                     same band either way

WEAK, SOLID, CITE, DOWN, LIFT = 'clm-weak00', 'clm-solid0', 'clm-cite00', 'clm-down00', 'clm-lift00'
NEAR, NEAR2, SUP1, SUP2 = 'clm-near00', 'clm-near02', 'sup-one000', 'sup-two000'
X, Y, Z, M, M2, W = 'clm-xxxxxx', 'clm-yyyyyy', 'clm-zzzzzz', 'clm-mmmmmm', 'clm-nnnnnn', 'clm-wwwwww'
P, Q, R, S = 'clm-pppppp', 'clm-qqqqqq', 'clm-rrrrrr', 'clm-ssssss'
EXP = 'exp-one000'
NOTE = 'research/2026-01-01_fixture_result.md'
OLD = 'notes/old.md'
HOSTILE = (('grep.lineNumber', 'true'), ('grep.column', 'true'), ('color.ui', 'always'))


def graph_spec(claims, deps=(), sups=None, gives=(), exps=None, fraction=1.0, axioms=()):
    return {'claims': claims, 'sups': sups or {}, 'deps': list(deps), 'gives': list(gives),
            'exps': exps or {}, 'fraction': fraction, 'axioms': list(axioms)}


def spec(**changes):
    s = graph_spec({WEAK: .30, SOLID: .90, CITE: .85, DOWN: .85, LIFT: .10, NEAR: .80, NEAR2: .70},
                   [(CITE, WEAK), (CITE, SOLID), (DOWN, CITE), (NEAR, NEAR2), (SUP1, WEAK), (SUP2, WEAK)],
                   {SUP1: .90, SUP2: .90}, [(SUP1, LIFT), (SUP2, LIFT)])
    s.update(changes)
    return s


def without(*pairs):
    return [d for d in spec()['deps'] if d not in pairs]


def tree(repo, root, s, files=(), stale=None, to=.99, drop=(), blank=(), garble=None, lose=(),
         retype=False):
    def edge(a, b, relation, **extra):
        return {'source': a, 'target': b, 'relation': relation, 'target_kind': 'claim', **extra}
    edges = [edge(a, b, 'depends', context=None) for a, b in s['deps']]
    edges += [edge(a, b, 'supports', fraction=s['fraction']) for a, b in s['gives']]
    edges += [edge(x, c, 'strengthens', strength=v) for x, (_, gives) in s['exps'].items() for c, v in gives]
    edges += [edge(a, b, 'depends', context=None, target_kind='axiom') for a, b in s.get('axioms', ())]
    nodes = [{'node_type': 'claim', 'id': c, 'confidence': v, 'solidity': None} for c, v in s['claims'].items()]
    nodes += [{'node_type': 'support', 'id': c, 'quality': v, 'solidity': None} for c, v in s['sups'].items()]
    nodes += [{'node_type': 'experiment', 'id': x, 'status': v[0]} for x, v in s['exps'].items()]
    nodes += [{'node_type': 'axiom', 'id': b} for _, b in s.get('axioms', ())]
    finals, sups = solve(Graph(nodes, edges))
    for r in nodes:
        if r['node_type'] in ('claim', 'support'):
            r['solidity'] = (finals if r['node_type'] == 'claim' else sups).get(r['id'])
        if r['id'] == stale:
            r['solidity'] = to
    nodes = [r for r in nodes if r['id'] not in drop]
    texts = {CLAIMS: '\n'.join(map(json.dumps, nodes)) + '\n',
             EDGES: '\n'.join(map(json.dumps, edges)) + '\n'}
    texts.update({path: '' for path in blank})
    if retype:
        texts[CLAIMS] = texts[CLAIMS].replace('"node_type": "claim"', '"node_type": "entry"')
    if garble:
        texts[garble] += '{"truncated\n'
    for p in Path(root).iterdir():
        if p.name != '.git':
            shutil.rmtree(p) if p.is_dir() else p.unlink()
    for path, text in list(texts.items()) + list(files):
        Path(root, path).parent.mkdir(parents=True, exist_ok=True)
        Path(root, path).write_text(text, encoding='utf-8')
    repo.git('add', '-A', '-f')
    sha = repo.git('write-tree').strip()
    for path in lose:
        blob = repo.git('rev-parse', '%s:%s' % (sha, path)).strip()
        Path(root, '.git', 'objects', blob[:2], blob[2:]).unlink()
    return sha


def says(source, target, why='why'):
    return '%s %s -> %s: %s' % (TOKEN, source, target, why)


CUT = (CITE, WEAK)
SUPS = ((SUP1, WEAK), (SUP2, WEAK))
CUTTING = spec(deps=without(CUT))
LINE = says(*CUT, 'the bound no longer applies')


def case(tip=None, files=(), base=None, base_files=(), rc=0, flagged=(), others=()):
    return {'tip': spec() if tip is None else tip, 'files': files, 'rc': rc,
            'base': spec() if base is None else base, 'base_files': base_files,
            'flagged': set(flagged), 'others': set(others)}


def fired(tip, *pairs, **rest_of_it):
    return case(tip, rc=1, flagged=pairs, **rest_of_it)


def note(text, path=NOTE):
    return ((path, text + '\n'),)


def no_deps(graph):
    return {**graph, 'deps': []}


def masked(single):
    """X held by a single dep at `single` and by both supports, each with a dep on W."""
    return graph_spec({X: .10, M: single, W: .30}, [(X, M), (SUP1, W), (SUP2, W)],
                      {SUP1: .90, SUP2: .90}, [(SUP1, X), (SUP2, X)])


CLAIMS_OF = spec()['claims']
RAISED = {WEAK, CITE, DOWN, LIFT}
TWO_CAPS = graph_spec({X: .90, W: .30, Z: .50}, [(X, W), (X, Z)])
SERIES = graph_spec({X: .90, M: .90, W: .30, Z: .50}, [(X, M), (M, W), (X, Z)])
SERIES2 = graph_spec({X: .90, M: .90, W: .30}, [(X, M), (M, W)])
TWO_ROUTES = graph_spec({X: .90, M: .90, M2: .90, W: .30}, [(X, M), (X, M2), (M, W), (M2, W)])
BYSTANDER = graph_spec({**TWO_ROUTES['claims'], Y: .90, Z: .95}, TWO_ROUTES['deps'] + [(Y, Z)])
TWO_LAYERS = graph_spec({X: .10, W: .30, M: .50}, [(SUP1, W), (SUP2, W), (SUP1, M), (SUP2, M)],
                        {SUP1: .90, SUP2: .90}, [(SUP1, X), (SUP2, X)])
LOOP = graph_spec({X: .90, Y: .90, Z: .90, M: .90, M2: .90, W: .90}, [(X, Y), (Z, M), (M2, W)])
LOOP_TIP = graph_spec(LOOP['claims'], [(Y, Z), (M, X), (M2, W)])
TWO_LOOPS = graph_spec({X: .90, Y: .90, Z: .90, M: .90, P: .90, Q: .90, R: .90, S: .90, M2: .90, W: .30,
                        NEAR: .80, SOLID: .90},
                       [(X, Y), (Z, M), (P, Q), (R, S), (M2, W), (NEAR, SOLID)])
TWO_LOOPS_TIP = graph_spec(TWO_LOOPS['claims'], [(Y, Z), (M, X), (Q, R), (S, P)])
TWO_LOOPS_OWE = ((X, Y), (Z, M), (P, Q), (R, S), (M2, W))
CHAIN = graph_spec({X: .85, M: .90, Z: .90}, [(X, M), (M, Z)])
SHARED = graph_spec({W: .30, X: .10, Y: .10, Z: .10}, [(SUP1, W), (SUP2, W)], {SUP1: .90, SUP2: .90},
                    [(SUP1, X), (SUP2, X), (SUP1, Y), (SUP2, Z)])
ROUNDS_UP = graph_spec({X: .10, W: .72, Z: .99}, [(X, Z), (SUP1, W), (SUP2, W)], {SUP1: .95, SUP2: .95},
                       [(SUP1, X), (SUP2, X)], fraction=.9)
STRONG = {EXP: ('run', [(CITE, .90)])}
OLD_SUP = graph_spec({X: .10, W: .30}, [(SUP1, W)], {SUP1: .90}, [(SUP1, X)])
KEPT_DEP = graph_spec({X: .95, W: .55}, [(X, W)])
STAGED = graph_spec({X: .10, W: .50, Z: .15}, [(X, Z), (SUP1, W), (SUP2, W)], {SUP1: .90, SUP2: .90},
                    [(SUP1, X), (SUP2, X)])
LIFTED_BY_RUN = graph_spec({X: .90, W: .30}, [(X, W)], exps={EXP: ('run', [(W, .90)])})
ROUNDED = graph_spec({X: .10, W: .72, Z: .99}, [(X, Z), (SUP1, W)], {SUP1: .93}, [(SUP1, X)], fraction=.9)
ROUNDED2 = graph_spec({X: .10, W: .72, Z: .99}, [(X, Z), (SUP1, W), (SUP2, W)], {SUP1: .80, SUP2: .80},
                      [(SUP1, X), (SUP2, X)], fraction=.9)
RECEIPT_ORDER = {**masked(.20), 'deps': [(SUP1, W), (X, M), (SUP2, W)]}
PARALLEL = graph_spec({X: .10, W: .30}, [(SUP1, W), (SUP2, W)], {SUP1: .90, SUP2: .90}, [(SUP1, X), (SUP2, X)])
LOST_TO_ROUNDING = graph_spec({X: .10}, sups={SUP1: .72}, gives=[(SUP1, X)], fraction=.9)
PHANTOM_BASE = graph_spec({X: .10, Z: .99}, [(X, Z)], {SUP1: .60}, [(SUP1, X)], fraction=.9)
PHANTOM_TIP = graph_spec({X: .10, Z: .99}, sups={SUP1: .72}, gives=[(SUP1, X)], fraction=.9)
AXIOM = 'axm-one000'
ON_AXIOM = graph_spec({X: .90}, axioms=[(X, AXIOM)])
RETYPED = graph_spec({X: .90, W: .30}, [(X, W)])

#: name -> what the fixture must give. Verdicts are reasoned by hand from the min rule.
CASES = {
    'unchanged':          case(),
    'cut-binding':        fired(CUTTING, CUT),
    'cut-slack':          case(spec(deps=without((CITE, SOLID)))),
    'cut-within-band':    case(spec(deps=without((NEAR, NEAR2)))),
    'cut-plus-slack':     fired(spec(deps=without(CUT, (CITE, SOLID))), CUT),
    'cut-two-binding':    fired(no_deps(TWO_CAPS), (X, W), (X, Z), base=TWO_CAPS),
    'lift-dropped-too':   case(graph_spec({X: .10, W: .30}, sups={SUP1: .90}),
                               base=graph_spec({X: .10, W: .30}, [(X, W)], {SUP1: .90}, [(SUP1, X)])),
    'add-edge':           case(spec(deps=spec()['deps'] + [(DOWN, SOLID)])),
    'raised-confidence':  case(spec(claims={**CLAIMS_OF, WEAK: .90}), others=RAISED),
    'no-longer-binding':  case(spec(deps=without(CUT), claims={**CLAIMS_OF, CITE: .25})),
    'held-against-fall':  fired(spec(deps=without(CUT), claims={**CLAIMS_OF, WEAK: .10, CITE: .40}), CUT),
    'held-over-a-fall':   fired(spec(deps=without(CUT), claims={**CLAIMS_OF, WEAK: .10}), CUT),
    'rise-by-two-routes': fired(spec(deps=without(CUT), claims={**CLAIMS_OF, WEAK: .60}), CUT,
                                base=spec(claims={**CLAIMS_OF, WEAK: .60, CITE: .30}), others={CITE, DOWN}),
    'pending-target':     fired(spec(deps=without(CUT), claims={**CLAIMS_OF, WEAK: None}), CUT,
                                base=spec(claims={**CLAIMS_OF, WEAK: None})),
    'staged-first-half':  case({**STAGED, 'deps': [(X, Z)]}, base=STAGED),

    'receipt':            case(CUTTING, note(LINE), flagged=[CUT]),
    'receipt-list-item':  case(CUTTING, note('  - ' + LINE), flagged=[CUT]),
    'receipt-star-item':  case(CUTTING, note('* ' + LINE), flagged=[CUT]),
    'receipt-tight':      case(CUTTING, note('%s%s->%s:why' % (TOKEN, CITE, WEAK)), flagged=[CUT]),
    'receipt-wide-marker': case(CUTTING, note('-   ' + LINE), flagged=[CUT]),
    'receipt-wide-indent': case(CUTTING, note('\u00a0' + LINE), flagged=[CUT]),
    'receipt-spaced-colon': case(CUTTING, note('%s %s -> %s : why' % (TOKEN, *CUT)), flagged=[CUT]),
    'receipt-docket':     case(CUTTING, note(LINE, '_orchestration/docket-entries/2026-01-01-x.md'), flagged=[CUT]),
    'receipt-in-fence':   case(CUTTING, note('```\n%s\n```' % LINE), flagged=[CUT]),
    'receipt-digit-reason': case(CUTTING, note(says(*CUT, '7')), flagged=[CUT]),
    'receipt-renamed-file': case(CUTTING, ((NOTE, 'context\n%s\n' % LINE),),
                                 base_files=note('context', 'research/2025-01-01_old.md'), flagged=[CUT]),
    'receipt-suffix-archive': case(CUTTING, note(LINE, 'research/foo_archive/x.md'), flagged=[CUT]),
    'receipt-same-name':  case(CUTTING, note(LINE, 'research/sub/2026-01-01_fixture_result.md'),
                               base_files=note('context'), flagged=[CUT]),
    'receipt-binary-neighbour': case(CUTTING, note(LINE) + (('data/0bin.md', '\0%s x\n' % TOKEN),), flagged=[CUT]),
    'receipt-support':    case(spec(deps=without(*SUPS)), note('\n'.join(says(*e) for e in SUPS)), flagged=SUPS),
    'receipt-on-slack':   case(spec(deps=without((CITE, SOLID))), note(says(CITE, SOLID)), flagged=[(CITE, SOLID)]),
    'receipt-other-edge': fired(CUTTING, CUT, files=note(says(CITE, SOLID))),
    'receipt-target-only': fired(CUTTING, CUT, files=note(says(DOWN, WEAK))),
    'receipt-no-reason':  fired(CUTTING, CUT, files=note('%s %s -> %s:' % (TOKEN, CITE, WEAK))),
    'receipt-blank-reason': fired(CUTTING, CUT, files=note('%s %s -> %s:   ' % (TOKEN, CITE, WEAK))),
    'receipt-placeholder': fired(CUTTING, CUT, files=note(says(*CUT, '<why>'))),
    'receipt-placeholder-upper': fired(CUTTING, CUT, files=note(says(*CUT, '<WHY>'))),
    'receipt-reason-past-cr': fired(CUTTING, CUT, files=((NOTE, '%s %s -> %s:\rthe next line\n' % (TOKEN, *CUT)),)),
    'receipt-invisible-reason': fired(CUTTING, CUT, files=note(says(*CUT, '​'))),
    'receipt-mid-line':   fired(CUTTING, CUT, files=note('as noted, ' + LINE)),
    'receipt-one-word':   fired(CUTTING, CUT, files=note('noted: ' + LINE)),
    'receipt-glued':      fired(CUTTING, CUT, files=note('-' + LINE)),
    'receipt-numbered':   fired(CUTTING, CUT, files=note('1. ' + LINE)),
    'receipt-plus-item':  fired(CUTTING, CUT, files=note('+ ' + LINE)),
    'receipt-double-marker': fired(CUTTING, CUT, files=note('- * ' + LINE)),
    'receipt-backticked': fired(CUTTING, CUT, files=note('%s `%s` -> `%s`: why' % (TOKEN, *CUT))),
    'receipt-bare-arrow': fired(CUTTING, CUT, files=note('%s %s > %s: why' % (TOKEN, *CUT))),
    'receipt-reversed':   fired(CUTTING, CUT, files=note(says(WEAK, CITE))),
    'receipt-two-on-a-line': fired(no_deps(TWO_CAPS), (X, W), (X, Z), base=TWO_CAPS,
                                   files=note('%s; %s' % (says(X, W), says(X, Z)))),
    'receipt-upper-token': fired(CUTTING, CUT, files=note(LINE.replace(TOKEN, TOKEN.upper()))),
    'receipt-prose':      fired(CUTTING, CUT, files=note('%s still rests on %s' % (CITE, WEAK))),
    'receipt-binary':     fired(CUTTING, CUT, files=note('\0\n' + LINE)),
    'receipt-wrong-root': fired(CUTTING, CUT, files=note(LINE, 'manuscript/ave-kb/vol1/claim-quality.md')),
    'receipt-orchestration': fired(CUTTING, CUT, files=note(LINE, '_orchestration/notes.md')),
    'receipt-nested-root': fired(CUTTING, CUT, files=note(LINE, 'manuscript/research/x.md')),
    'receipt-root-prefix': fired(CUTTING, CUT, files=note(LINE, '_orchestration/docket-entries-old/x.md')),
    'receipt-archived':   fired(CUTTING, CUT, files=note(LINE, 'research/_archive/2026-01-01_x.md')),
    'receipt-deep-archive': fired(CUTTING, CUT, files=note(LINE, 'research/sub/_archive/x.md')),
    'receipt-docket-archive': fired(CUTTING, CUT, files=note(LINE, '_orchestration/docket-entries/_archive/x.md')),
    'receipt-json':       fired(CUTTING, CUT, files=note(LINE, 'research/lane_results.json')),
    'receipt-md-suffix':  fired(CUTTING, CUT, files=note(LINE, 'research/x.md.bak')),
    'receipt-markdown':   fired(CUTTING, CUT, files=note(LINE, 'research/x.markdown')),
    'receipt-upper-md':   fired(CUTTING, CUT, files=note(LINE, 'research/x.MD')),
    'receipt-old-file':   fired(CUTTING, CUT, base_files=note('context'), files=note('context\n' + LINE)),
    'receipt-old-unicode-file': fired(CUTTING, CUT, base_files=note('context', 'research/\u00e9.md'),
                                      files=note('context\n' + LINE, 'research/\u00e9.md')),
    'receipt-moved-in':   fired(CUTTING, CUT, base_files=note(LINE, OLD), files=note(LINE)),
    'receipt-touched':    fired(CUTTING, CUT, base_files=note(LINE, OLD), files=note(LINE + ' ')),
    'receipt-rewrapped':  fired(CUTTING, CUT, base_files=note(LINE, OLD),
                                files=note(LINE.replace('no longer', 'no   longer'))),
    'receipt-was-quoted': fired(CUTTING, CUT, base_files=note('as noted, ' + LINE, OLD), files=note(LINE)),
    'receipt-was-table':  fired(CUTTING, CUT, base_files=note('| %s |' % LINE, OLD), files=note(LINE)),
    'receipt-was-json':   fired(CUTTING, CUT, base_files=note('{"line": "%s"}' % LINE, 'data/x.json'),
                                files=note(LINE)),
    'receipt-was-second': fired(CUTTING, CUT, base_files=note('%s | %s' % (says(DOWN, CITE, 'other'), LINE), OLD),
                                files=note(LINE)),
    'receipt-was-minified': fired(CUTTING, CUT, files=note(LINE), base_files=note(
        json.dumps([says(DOWN, CITE, 'other'), LINE]), 'data/x.json')),
    'receipt-was-backticked': fired(CUTTING, CUT, files=note(LINE), base_files=note(
        '%s `%s` -> `%s`: the bound no longer applies' % (TOKEN, *CUT), OLD)),
    'receipt-was-upper':  fired(CUTTING, CUT, files=note(LINE),
                                base_files=note(LINE.replace(TOKEN, TOKEN.upper()), OLD)),
    'receipt-was-cr':     fired(CUTTING, CUT, base_files=note('old\r' + LINE, OLD), files=note(LINE)),
    'receipt-was-spaced': fired(CUTTING, CUT, base_files=note(LINE.replace('no longer', 'no   longer'), OLD),
                                files=note(LINE)),
    'receipt-fragment':   fired(CUTTING, CUT, base_files=note(LINE, OLD), files=note(says(*CUT, 'bound'))),
    'receipt-new-reason': case(CUTTING, note(LINE + ', again'), base_files=note(LINE, OLD), flagged=[CUT]),
    'receipt-new-case':   case(CUTTING, note(LINE), base_files=note(LINE.replace('bound', 'BOUND'), OLD), flagged=[CUT]),
    'receipt-new-case-up': case(CUTTING, note(LINE.replace('bound', 'BOUND')), base_files=note(LINE, OLD), flagged=[CUT]),
    'receipt-reason-is-a-line': case(CUTTING, note(says(*CUT, says(DOWN, CITE, 'old'))), flagged=[CUT],
                                     base_files=note(says(DOWN, CITE, 'old'), OLD)),
    'receipt-reason-reused': case(CUTTING, note(LINE), flagged=[CUT], base_files=note(
        '%s\n%s' % (says(CITE, SOLID, 'the bound no longer applies'),
                    says(DOWN, WEAK, 'the bound no longer applies')), OLD)),

    'retired-binding':    fired(spec(deps=without(CUT, *SUPS),
                                     claims={k: v for k, v in CLAIMS_OF.items() if k != WEAK}),
                                CUT, *SUPS),
    'retired-slack':      case(spec(deps=without((CITE, SOLID)),
                                    claims={**{k: v for k, v in CLAIMS_OF.items() if k != SOLID}, WEAK: .90}),
                               others=RAISED),
    'retired-dep-moved':  fired(graph_spec({X: .85, Z: .10}), (X, M), (M, Z), base=CHAIN),
    'retired-clean':      case(graph_spec({X: .85, Z: .90}), base=CHAIN),
    'retired-dead-leaf':  fired(graph_spec({W: .55}), (X, W), base=KEPT_DEP),
    'retired-run-lift':   case(graph_spec({X: .90}), base=LIFTED_BY_RUN),
    'retired-lift-lowered': case(graph_spec({W: .30}, sups={SUP1: .20}),
                                 base=graph_spec({X: .10, W: .30}, [(X, W)], {SUP1: .90}, [(SUP1, X)])),
    'retired-run-undone': fired(graph_spec({X: .90}, exps={EXP: ('pending', [])}), (X, W), base=LIFTED_BY_RUN),
    'retired-bystander':  case(graph_spec({W: .30}, sups={SUP1: .90}), base=OLD_SUP),
    'remint-no-citers':   fired(graph_spec({Y: .95, W: .63}), (X, W), base=graph_spec({X: .95, W: .63}, [(X, W)])),
    'remint-citers':      fired(graph_spec({Y: .90, W: .55, Z: .90}, [(Z, Y)]), (X, W), (Z, X),
                                base=graph_spec({X: .90, W: .55, Z: .90}, [(X, W), (Z, X)])),
    'remint-keeps-dep':   fired(graph_spec({Y: .95, W: .55}, [(Y, W)]), (X, W), base=KEPT_DEP),
    'split-keeps-dep':    fired(graph_spec({Y: .95, Z: .95, W: .55}, [(Y, W), (Z, W)]), (X, W), base=KEPT_DEP),
    'remint-raised':      case(graph_spec({Y: .95, W: .60}), base=graph_spec({X: .50, W: .60}, [(X, W)])),
    'remint-support':     case(graph_spec({X: .10, W: .30}, sups={SUP2: .90}, gives=[(SUP2, X)]),
                               base=OLD_SUP, others={X}),
    'dep-becomes-support': fired(spec(deps=without(SUPS[0]), gives=spec()['gives'] + [SUPS[0]]), SUPS[0],
                                 others=RAISED),

    'reversed-edge':      fired(spec(deps=without(CUT) + [(WEAK, CITE)]), CUT, others={CITE, DOWN}),
    'joint-only':         fired(spec(deps=without(*SUPS)), *SUPS),
    'joint-plus-slack':   fired(spec(deps=without((CITE, SOLID), *SUPS)), *SUPS),
    'joint-masked-parallel': fired(no_deps(masked(.50)), (X, M), *((s, W) for s in (SUP1, SUP2)), base=masked(.50)),
    'joint-masked-series': fired(no_deps(SERIES), (X, M), (M, W), (X, Z), base=SERIES),
    'joint-at-single':    fired(no_deps(masked(.30)), (X, M), (SUP1, W), (SUP2, W), base=masked(.30)),
    'joint-below-single': fired(no_deps(masked(.20)), (X, M), (SUP1, W), (SUP2, W), base=masked(.20)),
    'joint-after-receipt': fired(no_deps(masked(.20)), (X, M), (SUP1, W), (SUP2, W), base=masked(.20),
                                 files=note(says(X, M))),
    'joint-two-layers':   fired(no_deps(TWO_LAYERS), (SUP1, W), (SUP2, W), (SUP1, M), (SUP2, M), base=TWO_LAYERS),
    'joint-layer-receipted': fired(no_deps(TWO_LAYERS), (SUP1, W), (SUP2, W), (SUP1, M), (SUP2, M), base=TWO_LAYERS,
                                   files=note(says(SUP1, W) + '\n' + says(SUP2, W))),
    'joint-all-receipted': case(no_deps(TWO_LAYERS), note('\n'.join(says(*e) for e in TWO_LAYERS['deps'])),
                                base=TWO_LAYERS, flagged=TWO_LAYERS['deps']),
    'receipt-frees-series': case(no_deps(SERIES2), note(says(M, W)), base=SERIES2, flagged=[(M, W)]),
    'receipt-frees-parallel': case(no_deps(PARALLEL), note(says(SUP1, W)), base=PARALLEL, flagged=[(SUP1, W)]),
    'joint-layer-order':  fired(no_deps(RECEIPT_ORDER), (X, M), (SUP1, W), (SUP2, W), base=RECEIPT_ORDER),
    'joint-two-routes':   fired(no_deps(TWO_ROUTES), (X, M2), (M, W), (M2, W), base=TWO_ROUTES),
    'joint-bystander':    fired(no_deps(BYSTANDER), (X, M2), (M, W), (M2, W), base=BYSTANDER),
    'joint-not-mislabelled': fired(no_deps(SHARED), (SUP1, W), (SUP2, W), base=SHARED),
    'joint-cycle':        fired(LOOP_TIP, (X, Y), (Z, M), base=LOOP),
    'joint-cycle-plus-slack': fired(graph_spec(LOOP['claims'], [(Y, Z), (M, X)]), (X, Y), (Z, M), base=LOOP),
    'joint-cycle-half-receipted': case(LOOP_TIP, note(says(X, Y)), base=LOOP, flagged=[(X, Y)]),
    'two-cycles':         fired(TWO_LOOPS_TIP, *TWO_LOOPS_OWE, base=TWO_LOOPS),
    'two-cycles-receipted': case(TWO_LOOPS_TIP, note('\n'.join(says(*e) for e in TWO_LOOPS_OWE)),
                                 base=TWO_LOOPS, flagged=TWO_LOOPS_OWE),

    'slack-rounds-up':    fired(no_deps(ROUNDS_UP), (SUP1, W), (SUP2, W), base=ROUNDS_UP),
    'slack-rounds-up-receipted': case(no_deps(ROUNDS_UP), note(says(SUP1, W) + '\n' + says(SUP2, W)),
                                      base=ROUNDS_UP, flagged=[(SUP1, W), (SUP2, W)]),
    'restore-raises':     case({**ROUNDS_UP, 'deps': [(SUP1, W), (SUP2, W)]}, base=ROUNDS_UP),
    # These pin the library rounding only with deps, as the abort `stale-by-rounding` does. If it
    # rounds every reading, all of them change except `rounding-no-receipt`, the control.
    'rounding-holds-a-band': fired(no_deps(ROUNDED), (SUP1, W), base=ROUNDED),
    'rounding-slack-receipt': fired(no_deps(ROUNDED2), (X, Z), (SUP1, W), (SUP2, W), base=ROUNDED2,
                                    files=note(says(X, Z))),
    'rounding-no-receipt': case(no_deps(ROUNDED2), base=ROUNDED2),
    'rounding-no-phantom-rise': case(PHANTOM_TIP, base=PHANTOM_BASE),

    'exp-rescue':         case(spec(deps=without(CUT), exps=STRONG), base=spec(exps=STRONG)),
    'exp-unrun':          fired(spec(deps=without(CUT), exps={EXP: ('pending', STRONG[EXP][1])}), CUT,
                                base=spec(exps={EXP: ('pending', STRONG[EXP][1])})),
    'sup-pending-fraction': case(spec(deps=without(*SUPS), fraction='*pending*'), base=spec(fraction='*pending*')),
    'sup-fraction':       fired(spec(deps=without(*SUPS), fraction=.5), *SUPS, base=spec(fraction=.5)),
    'axiom-cut':          case(no_deps({**ON_AXIOM, 'axioms': []}), base=ON_AXIOM),
}

#: name -> (tree() arguments for the base, for the tip, optionally the tip's and the base's
#: spec). Each must abort.
ABORTS = {
    'stale-index':   ({}, {'stale': WEAK}),
    'stale-support': ({}, {'stale': SUP1}),
    'stale-base':    ({'stale': WEAK}, {}),
    'stale-same-band': ({}, {'stale': WEAK, 'to': .31}),
    'stale-by-rounding': ({}, {'stale': X, 'to': .65}, LOST_TO_ROUNDING),
    'stale-to-null': ({}, {'stale': WEAK, 'to': None}),
    'stale-from-null': ({}, {'stale': WEAK, 'to': .70}, spec(claims={**CLAIMS_OF, WEAK: None})),
    'empty-tip':     ({}, {'blank': (CLAIMS, EDGES)}),
    'empty-base':    ({'blank': (CLAIMS, EDGES)}, {}),
    'retyped-claims': ({'retype': True}, {'retype': True}, no_deps(RETYPED), RETYPED),
    'orphan-edge':   ({}, {'drop': (NEAR,)}),
    'orphan-target': ({}, {'drop': (NEAR2,), 'stale': NEAR, 'to': None}),
    'orphan-lift':   ({}, {'drop': (SUP1,)}, graph_spec({X: .10}, sups={SUP1: .90}, gives=[(SUP1, X)],
                                                        fraction='*pending*')),
    'orphan-lift-target': ({}, {'drop': (X,)}, graph_spec({X: .10, W: .30}, sups={SUP1: .90}, gives=[(SUP1, X)],
                                                          fraction='*pending*')),
    'orphan-run-target': ({}, {'drop': (X,)}, graph_spec({X: .10, W: .30}, exps={EXP: ('run', [(X, .90)])})),
    'orphan-run-source': ({}, {'drop': (EXP,)}, graph_spec({X: .10, W: .30}, exps={EXP: ('pending', [(X, .90)])})),
    'bad-json':      ({}, {'garble': EDGES}),
    'unreadable-base': ({'files': note(LINE + '\nfirst', OLD), 'lose': (OLD,)}, {'files': note(LINE)}, CUTTING),
    'unreadable-base-beside-a-hit': ({'files': note(LINE + '\nsecond', OLD) + note(says(DOWN, CITE), 'notes/hit.md'),
                                      'lose': (OLD,)}, {'files': note(LINE)}, CUTTING),
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
    base_args, tip_args, *specs = ABORTS[name]
    tip_spec, base_spec = [*specs, spec(), spec()][:2]
    base = tree(repo, root, base_spec, **base_args)
    tip = tree(repo, root, tip_spec, **tip_args)
    try:
        scan(repo, base, tip)
    except GateError:
        return True
    return False


#: How a fixture that raised is recorded: a mutant that only crashes has proved nothing.
CRASHED = 'fixture raised: '


def run_gate(out=print, only=None):
    """Every fixture verdict and every owed abort, or just `only`. Returns what failed."""
    root = tempfile.mkdtemp(prefix='solidity-ratchet-selftest-')
    failed = []
    try:
        repo = Repo(cwd=root, scrub_env=True)
        repo.git('init', '-q')
        for key, value in HOSTILE:
            repo.git('config', key, value)
        Path(root, '.git', 'info').mkdir(exist_ok=True)
        Path(root, '.git', 'info', 'exclude').write_text('*\n', encoding='utf-8')
        for name, run in [(n, run_case) for n in CASES] + [(n, run_abort) for n in ABORTS]:
            if only and name not in only:
                continue
            try:
                ok = run(repo, root, name)
            except (GateError, lib.SolidityCycleError) as e:
                out('  [BROKEN] %s (%s)' % (name, e))
                failed.append('%s%s (%s)' % (CRASHED, name, e))
                continue
            out('  [%s] %s' % ('OK' if ok else 'BROKEN', name))
            if not ok:
                failed.append('fixture verdict wrong: %s' % name)
    finally:
        shutil.rmtree(root, ignore_errors=True)
    return failed


@guarded
def selftest():
    print('[solidity-ratchet] SELF-GATE')
    failed = run_gate()
    if failed:
        print('[solidity-ratchet] SELF-GATE FAILED: %s' % '; '.join(failed))
        return 2 if any(f.startswith(CRASHED) for f in failed) else 1
    print('[solidity-ratchet] SELF-GATE OK: %d fixtures and %d aborts.' % (len(CASES), len(ABORTS)))
    return 0


#: mutation -> (the fixtures switching it off must break, what it switches off).
MUTATIONS = {
    'no-restore':         (('cut-binding',), 'stop finding removed edges'),
    'any-rise':           (('cut-within-band',), 'gate on any solidity rise instead of a band rise'),
    'any-move':           (('restore-raises',), 'count a restore that raises a band as one that holds it'),
    'rise-only':          (('held-against-fall',), 'exempt a cut that only stops a claim falling'),
    'source-only':        (('receipt-other-edge',), 'accept a receipt for another edge of the source'),
    'target-only':        (('receipt-target-only',), 'accept a receipt for another edge into the target'),
    'no-reason':          (('receipt-no-reason', 'receipt-blank-reason', 'receipt-placeholder',
                            'receipt-placeholder-upper', 'receipt-invisible-reason'),
                           'accept a receipt with no reason'),
    'token-anywhere':     (('receipt-mid-line', 'receipt-one-word', 'receipt-glued', 'receipt-numbered',
                            'receipt-plus-item', 'receipt-double-marker'),
                           'accept a receipt that is not at the start of a line'),
    'any-root':           (('receipt-wrong-root', 'receipt-orchestration', 'receipt-nested-root',
                            'receipt-root-prefix'),
                           'accept a receipt outside the reviewed roots'),
    'any-file':           (('receipt-json', 'receipt-md-suffix', 'receipt-upper-md', 'receipt-markdown'),
                           'accept a receipt in a file that is not Markdown'),
    'archived':           (('receipt-archived', 'receipt-deep-archive', 'receipt-docket-archive'),
                           'accept a receipt in an archive'),
    'old-file':           (('receipt-old-file',), 'accept a receipt in a file the base has'),
    'old-text':           (('receipt-moved-in', 'receipt-touched', 'receipt-rewrapped', 'receipt-was-quoted',
                            'receipt-was-table', 'receipt-was-json', 'receipt-was-second',
                            'receipt-was-minified', 'receipt-was-backticked', 'receipt-was-cr',
                            'receipt-was-spaced', 'receipt-fragment'),
                           'accept a receipt the base tree already holds'),
    'token-case':         (('receipt-was-upper',), 'miss a base line whose token is in another case'),
    'no-grep-pin':        (('receipt',), 'read receipts under the user\'s grep and colour config'),
    'grep-stderr-ok':     (('unreadable-base', 'unreadable-base-beside-a-hit'),
                           'read an unreadable blob as no match'),
    'no-stub':            (('retired-slack',), 'restore edges to retired claims as pending'),
    'all-retired':        (('retired-bystander',), 'put back retired claims no removed edge touches'),
    'no-exp-lifts':       (('retired-run-lift',), 'drop a retired claim\'s experiment lifts'),
    'stale-lifts':        (('retired-lift-lowered', 'retired-run-undone'),
                           'read a retired claim\'s lifts at the base and not the tip'),
    'skip-retired':       (('retired-dep-moved', 'remint-no-citers', 'remint-citers'),
                           'skip edges whose source left the index'),
    'kept-any-relation':  (('dep-becomes-support',), 'count a non-depends edge as keeping a dependency'),
    'cycle-passes':       (('reversed-edge',), 'treat an edge that cannot be restored as harmless'),
    'joint-cycle-passes': (('joint-cycle', 'two-cycles'), 'treat edges that close a cycle together as harmless'),
    'cycle-blames-all':   (('joint-cycle-plus-slack', 'two-cycles'), 'blame every removed edge for a cycle'),
    'no-joint':           (('joint-only',), 'test edges only one at a time'),
    'no-residual':        (('receipt-frees-series', 'receipt-frees-parallel'), 'test receipted edges with the others'),
    'one-layer':          (('joint-at-single', 'joint-below-single', 'joint-two-layers'),
                           'stop at the first edges named'),
    'blame-all':          (('joint-plus-slack', 'joint-bystander'), 'blame every removed edge for a joint effect'),
    'others-tip':         (('joint-not-mislabelled',), 'call a rise not gated without restoring the edges'),
    'others-skip-named':  (('rise-by-two-routes',), 'hide the not-gated share of a flagged claim'),
    'no-experiments':     (('exp-rescue',), 'solve without run experiments'),
    'fraction-one':       (('sup-pending-fraction',), 'read a pending on-point fraction as 1'),
    'no-reconcile':       (('stale-index',), 'skip the reconcile'),
    'claims-only':        (('stale-support',), 'reconcile claims and not supports'),
    'tip-only':           (('stale-base',), 'reconcile the tip and not the base'),
    'allow-empty':        (('empty-tip', 'empty-base'), 'accept an index with no claims'),
    'allow-orphans':      (('orphan-edge', 'orphan-target', 'orphan-lift', 'orphan-lift-target',
                            'orphan-run-target', 'orphan-run-source'), 'accept an edge whose node is missing'),
    'skip-bad-json':      (('bad-json',), 'drop an unparseable index line'),
}


@guarded
def mutation_receipt():
    print('[solidity-ratchet] MUTATION RECEIPT -- each listed rule, switched off, must break its fixtures')
    allgood, crashed = True, False
    for mutation, (cases, label) in MUTATIONS.items():
        MUTATE.add(mutation)
        try:
            failed = run_gate(out=lambda line: None, only=cases)
        finally:
            MUTATE.discard(mutation)
        raised = any(f.startswith(CRASHED) for f in failed)
        tripped = len(failed) == len(cases) and not raised
        print('  [%s] %s -> %s' % ('OK' if tripped else 'BROKEN', label, ', '.join(cases)))
        allgood, crashed = allgood and tripped, crashed or raised
    if not allgood:
        print('[solidity-ratchet] MUTATION RECEIPT FAILED')
        return 2 if crashed else 1
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
