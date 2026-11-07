#!/usr/bin/env python3
"""Inbound cite-shift checker.

The corpus pins by `path:NNN`. Any edit that moves a line silently re-points some
OTHER file's cite at different content. Nothing catches it: verify-md-links gates
only out-of-RANGE, verify-anchor-content is advisory and needs an adjacent excerpt.

The one question that matters: for every corpus cite targeting a file this branch
CHANGED, does the cited line still hold what it held at the merge-base?
base[N] != tip[N]  =>  the cite moved under its citer, silently.

THE ADDRESSING RULE -- which file does `some/path/leaf.ext:NNN` address?
------------------------------------------------------------------------
A cite is tested against a changed file ONLY when the cite's own text pins that
file. The finder collects by basename (it has to -- most cites abbreviate), and
until 2026-09-19 every cite was then tested against EVERY changed file sharing
that basename: the path the author actually wrote was never read. Measured
instance: a 13-line insertion into `manuscript/vol_1_foundations/main.tex`
reported SHIFTED=4 -- one citer spelling out
`papers/2026_birefringence_letter/main.tex:60`, three bare `main.tex:53` in a
ledger about the Letter's abstract. Nine tracked files are named `main.tex`; not
one of the four cites addressed vol_1's.

The candidate set C of a cite is read off its path text, most specific reading
first. The cite is tested against changed file T iff T is in C, and it can FAIL
the run only when C == {T}:

  1. LINK TARGET. `[text](../x/leaf.md):NN` and `[leaf.md:NN](../x/leaf.md)`: the
     markdown link target, resolved against the CITING file's directory, is the
     addressee. Exact -- it is what the link means.
  2. NAMED REPO ROOT. `AVE-Core/...` anchors the path at this repo's root (exact
     match) -- looked for FIRST and wherever it sits, because an absolute path
     reaches it through the workspace umbrella directory. Any other
     `AVE-<Name>/...` or `Applied-Vacuum-Engineering/...` addresses a sibling
     repo, and C is empty whatever the basename -- unless the path is a component
     suffix of a file tracked HERE (a fixture directory is named `AVE-Sib`).
  3. EXPLICIT PATH (the captured text contains a `/`). Leading `./` and `../`
     segments are dropped, then C = the tracked files the path is a COMPONENT
     SUFFIX of. `vol_1_foundations/main.tex` and
     `manuscript/vol_1_foundations/main.tex` name the same file -- a leading
     `manuscript/` is optional by construction -- while
     `papers/2026_birefringence_letter/main.tex` is a suffix of exactly one file
     and therefore never of vol_1's.
       ONLY if the path is a suffix of NO tracked file is it read as an
     ABBREVIATION: each cited directory must match, in order, a directory of the
     candidate -- equal, a word-boundary prefix (`vol_1` ~ `vol_1_foundations`),
     or an explicit elision (`vol4/.../theory.md`, `ch14-.../`). Gaps are allowed
     (`vol_1/02_x.tex` skips `chapters/`).
       A path that matches nothing even as an abbreviation (a renamed directory,
     a stale layout) carries no usable directory information: the basename
     decides, under rule 4, exactly as if no path had been written.
  4. BARE BASENAME. C = every tracked file with that basename. One file: the
     cite is pinned, as it always was. More than one: NARROWING, below -- a bare
     name shared by 2+ tracked files is NEVER reported SHIFTED on the name alone.

"Tracked" means present in the base OR the tip tree: a same-named file the branch
adds or deletes still makes a bare name ambiguous. A captured name that merely
ENDS in the leaf (`universal-operators.md` while `operators.md` changed) is not a
cite of the leaf at all, and is dropped.

NARROWING, when C still holds 2+ files:
  a. HAS-LINE. A file that does not HAVE line NNN is not the addressee -- the
     "never a valid address at base" test this script always applied to the
     changed file, applied to every candidate. Sound (no guess about intent) and
     it does most of the work: `main.tex:320` can only be the 1,236-line Letter,
     never a 63-line volume main.
  b. SAME LINE. An explicit path to a same-named file written EARLIER ON THE SAME
     LINE is inherited when it pins exactly one member of C
     (`.../ch14-leaky-cavity-particle-decay/theory.md:43 states ... note
     theory.md:8 carries ...`).
  c. Otherwise the cite is AMBIGUOUS-BASENAME: still tested against the changed
     file, printed in its own ADVISORY bucket with the verdict it WOULD get and
     the other files it could mean, and it NEVER fails the run. The repair is the
     author's: spell the path.

NOT a narrowing rule, deliberately: "the citing file's own directory holds a file
of that name". Measured on this corpus it is wrong about as often as right outside
a markdown link -- `README.md:6` "badge" cites under `_orchestration/` address the
ROOT README, not `_orchestration/README.md`; `translation-circuit.md:181` is cited
from beside a 12-line same-named sibling; `provenance.md:854` from beside a
117-line one. Inside a markdown link the same-directory reading is exact, and
rule 1 already has it.

LIVENESS -- a zero has to be earned, and NOT inferred from the run's own yield
------------------------------------------------------------------------------
A checker that finds nothing reports a clean it did not earn. Before any zero is
trusted, every run proves four things, none of them read off its own yield:

  * both revs resolve to a tree  (on a bad rev every git call returns nothing);
  * no `git grep` exited > 1     (1 = "no match" is an answer; an error is not);
  * every object read was READ   git grep reports an unreadable blob ONLY on stderr
                                 and still exits 0 or 1, its lines simply absent;
                                 `cat-file --batch` answers `missing`, exactly as for
                                 a path the tree does not hold, or -- for a blob big
                                 enough to stream -- sends part of it and exits 128;
                                 diff and ls-tree exit non-zero on an unreadable
                                 subtree. Read naively, each is a citer or a changed
                                 file that is not there, or a shorter one. The run
                                 works from the repo top level: from a subdirectory
                                 git grep and ls-tree see only that subtree;
  * THE SELF-GATE holds          the --selftest fixtures, driven through this same
                                 scan() and git binary: a planted shifted cite IS
                                 reported, a cite to a same-named sibling is NOT, and
                                 each damaged object in LOST ABORTS.
Any failure aborts with exit 2 instead of printing a zero.

Until 2026-09-19 liveness WAS inferred from yield: "changed files but ZERO cites
resolved => the FINDER is broken". That cannot tell "nothing to find" from "finder
broken" -- the one distinction a liveness control exists to draw. Measured on the
30 merges into main up to ed1c7b4a: exit 2 on 15 of them, and the finder was
broken in none. Eleven changed only files that no corpus line cites; four had
cites only into files the branch ADDED, which have no base content to move. The
addressing rule makes honest zeros more common still (203 cites found, none
addressed to the changed file), so the inference had to go. verify-fired-riders.py
never had this problem because its control is a FIXED positive control; this one
now has that shape too.

EXIT CODES
----------
  0  no pinned cite moved (the advisory buckets may still be non-empty)
  1  a cite PINNED to a changed file is SHIFTED or OUT-OF-RANGE
  2  no verdict was reached: liveness failed, an object could not be read, the
     arguments were wrong, or the gate crashed. Every mode runs under guarded(): an
     uncaught traceback exits 1, which is the verdict "a pinned cite moved".

SELF-TESTS
----------
    verify-inbound-cite-shift.py --selftest           can-it-fire + negative controls
    verify-inbound-cite-shift.py --mutation-receipt   each rule, removed, must trip
Both drive THIS scan() against a throwaway two-tree repo with the real git
binary. The negative control that matters: an explicit-path cite to file A must
NOT fire when same-named file B moves -- and the mutation receipt proves that
control is not vacuous, because under the pre-fix basename-only rule the very
same fixture DOES fire.
"""
import collections, contextlib, os, posixpath, re, shutil, subprocess, sys, tempfile, traceback

THIS_REPO = 'AVE-Core'
SIBLING_REPO = re.compile(r'^(?:AVE-[A-Za-z0-9]+|Applied-Vacuum-Engineering)$')

PATH_CHARS = r'[A-Za-z0-9_./\\-]*'
PAT_TMPL = r'(' + PATH_CHARS + r'%s)[^A-Za-z0-9\s]{0,3}:(\d+)'
# `[leaf.md:NN](target)`: from the end of the cite to the link target that closes
# the link TEXT the cite sits in.
LINK_TAIL = re.compile(r'[^\[\]]{0,120}\]\(([^)\s]+)\)')

ROT = ('SHIFTED', 'OUT-OF-RANGE')

#: Rules switched OFF by --mutation-receipt. Empty in every real run.
MUTATE = set()


class GateError(RuntimeError):
    """The machinery failed -- an object it needed could not be read. A clean report
    past this point would be false."""


#: stderr is where git grep reports an unreadable blob (see scan()), so nothing else may
#: write there: trace2 can be switched on from git CONFIG as well as the environment
#: (`[trace2] normalTarget = 2` reaches the fixtures too) and the environment overrides
#: config; a translated git would spell `warning:` some other way.
QUIET = {'GIT_TRACE2': '0', 'GIT_TRACE2_EVENT': '0', 'GIT_TRACE2_PERF': '0', 'LC_ALL': 'C'}


class Repo:
    """A git repo handle plus blob/tree caches.

    The real run uses the cwd and the caller's environment minus GIT_TRACE* (env-only
    tracing, to stderr), plus QUIET. The self-test fixtures use a throwaway directory
    with every GIT_* variable scrubbed: a fixture built while a git hook has GIT_DIR /
    GIT_INDEX_FILE exported would otherwise write into the REAL repo.
    """

    def __init__(self, cwd=None, scrub_env=False):
        scrub = 'GIT_' if scrub_env else 'GIT_TRACE'
        self.cwd = cwd
        self.env = {k: v for k, v in os.environ.items() if not k.startswith(scrub)}
        self.env.update(QUIET)
        self._blob, self._tree = {}, {}

    def raw(self, *a, stdin=None):
        r = subprocess.run(('git',) + a, capture_output=True, cwd=self.cwd,
                           env=self.env, input=stdin)
        self.err = r.stderr.decode('utf-8', 'replace').strip()
        return r.returncode, r.stdout

    def sh(self, *a):
        return self.raw(*a)[1].decode('utf-8', 'replace')

    def checked(self, *a):
        """stdout of a git call that must succeed. An unreadable subtree makes diff and
        ls-tree exit non-zero with nothing on stdout: read naively, "no changed files"."""
        rc, out = self.raw(*a)
        if rc != 0 and 'unchecked-git' not in MUTATE:
            raise GateError('`git %s` exited %d: %s' % (' '.join(a), rc, self.err or 'no stderr'))
        return out.decode('utf-8', 'replace')

    def tree(self, rev):
        """{path: object type} for every entry of `rev`, in ls-tree order."""
        if rev not in self._tree:
            types = {}
            for row in self.checked('ls-tree', '-r', '-z', rev).split('\0'):
                meta, tab, path = row.partition('\t')     # <mode> SP <type> SP <oid> TAB <path>
                if tab:
                    types[path] = meta.split(' ')[1]
            self._tree[rev] = types
        return self._tree[rev]

    def blob(self, rev, path):
        if (rev, path) not in self._blob:
            self.load(rev, [path])
        return self._blob[(rev, path)]

    def load(self, rev, paths):
        """Read many blobs in ONE git process (129 files are named index.md)."""
        paths = [p for p in paths if (rev, p) not in self._blob]
        if not paths:
            return
        req = ''.join('%s:%s\n' % (rev, p) for p in paths).encode('utf-8')
        rc, raw = self.raw('cat-file', '--batch', stdin=req)
        # A blob too big to inflate in one go is STREAMED: git prints its full-size
        # header, then part of the body, then dies (`fatal: unable to stream`, exit 128).
        # Kept, the part reads as a shorter file and every cite past it as "never valid".
        if rc != 0 and 'short-read-ok' not in MUTATE:
            raise GateError('`git cat-file --batch` exited %d reading %s: %s'
                            % (rc, rev, self.err or 'no stderr'))
        i = 0
        for p in paths:
            j = raw.find(b'\n', i)
            head = raw[i:j].split() if j >= 0 else []
            lines = None
            if len(head) == 3 and head[2].isdigit():       # <sha> <type> <size>
                size = int(head[2])
                if raw[j + 1 + size:j + 2 + size] != b'\n' and 'short-read-ok' not in MUTATE:
                    raise GateError('%s:%s: `git cat-file --batch` announced %d bytes and sent '
                                    '%d' % (rev, p, size, len(raw) - j - 1))
                if head[1] == b'blob':
                    lines = raw[j + 1:j + 1 + size].decode('utf-8', 'replace').split('\n')
                i = j + 1 + size + 1
            else:                                          # `<name> missing`, or truncated
                i = j + 1 if j >= 0 else len(raw)
            # `missing` is also the answer for a blob the tree HOLDS but the object
            # store cannot produce -- read as "no such file", every cite to it is
            # skipped and the run reports a clean it did not earn. Only the tree can
            # tell the two apart. (A gitlink is `commit`, never readable here: absent.)
            if lines is None and self.tree(rev).get(p) == 'blob' and 'missing-is-absent' not in MUTATE:
                reply = b' '.join(head).decode('utf-8', 'replace') or 'no reply'
                raise GateError('%s:%s is a blob in that tree, but `git cat-file --batch` cannot '
                                'read it (%s)' % (rev, p, reply))
            self._blob[(rev, p)] = lines


# ------------------------------------------------------------- addressing rule

def cite_comps(g):
    """Captured path text -> (components, anchored-at-this-repo-root, names-a-sibling-repo)."""
    comps = g.replace('\\_', '_').replace('\\', '/').split('/')
    dirs = comps[:-1]
    # THIS repo first, wherever it sits: an absolute path reaches it THROUGH the
    # workspace umbrella directory (`.../AVE-staging/AVE-Core/...`), and the
    # umbrella's own name matches the sibling pattern.
    if THIS_REPO in dirs:
        k = len(dirs) - 1 - dirs[::-1].index(THIS_REPO)
        return comps[k + 1:], True, False
    sibling = any(SIBLING_REPO.match(c) for c in dirs)
    # leading '', '.', '..', '...' say nothing about WHICH directory
    while len(comps) > 1 and set(comps[0]) <= {'.'}:
        comps.pop(0)
    return comps, False, sibling


def _dir_match(c, t):
    if c == t:
        return True
    if c.endswith('..'):                                   # elision: `vol_3...`, `ch14-...`
        c = c.rstrip('.')
        return bool(c) and t.startswith(c)
    return t.startswith(c) and not t[len(c)].isalnum()     # `vol_1` ~ `vol_1_foundations`


def _abbreviates(comps, path):
    """Every cited directory matches, IN ORDER, a directory of `path`; gaps allowed."""
    t, k = path.split('/'), 0
    for c in comps[:-1]:
        if set(c) <= {'.'}:                                # a bare `...` is a gap
            continue
        while k < len(t) - 1 and not _dir_match(c, t[k]):
            k += 1
        if k >= len(t) - 1:
            return False
        k += 1
    return True


def path_candidates(comps, anchored, sibling, same):
    """The files in `same` (one basename) that the cited path can name, and how."""
    if anchored:
        hit = [p for p in same if p == '/'.join(comps)]
        if hit:
            return hit, 'repo-root path'
    if len(comps) == 1:
        return list(same), 'bare basename'
    hit = [p for p in same if p.split('/')[-len(comps):] == comps]
    if hit:
        return hit, 'path'
    # Out of this repo ONLY once it has failed to be a path in it: a directory
    # here may itself be named like a sibling (a test fixture is).
    if sibling:
        return [], 'sibling repo'
    hit = [p for p in same if _abbreviates(comps, p)]
    if hit:
        return hit, 'abbreviated path'
    return list(same), 'unmatched path'


def _link_addressee(src, target, same):
    target = target.split('#', 1)[0].replace('\\_', '_')
    if not target or '://' in target:
        return None
    if target.startswith('/'):
        p = target.lstrip('/')
    else:
        p = posixpath.normpath(posixpath.join(posixpath.dirname(src), target))
    return p if p in same else None


def _same_line_antecedent(before, leaf, cands):
    hit = None
    for m in re.finditer('(' + PATH_CHARS + re.escape(leaf) + ')', before):
        comps, anchored, sibling = cite_comps(m.group(1))
        if comps[-1] != leaf or (len(comps) < 2 and not anchored):
            continue                                       # a bare name pins nothing
        c, how = path_candidates(comps, anchored, sibling, cands)
        if how not in ('unmatched path', 'bare basename') and len(c) == 1:
            hit = c[0]                                     # nearest preceding wins
    return hit


def addressees(m, leaf, src, text, same, has_line):
    """(candidate files, how) for the cite matched by `m` -- see the docstring.

    Context may only NARROW the set the path text allows, never step outside it.
    """
    comps, anchored, sibling = cite_comps(m.group(1))
    if 'address-nothing' in MUTATE:
        return [], 'mutated'
    n = int(m.group(2))

    # 1. markdown link target -- resolved against the CITING file's directory
    target = None
    if text[max(0, m.start(1) - 2):m.start(1)] == '](' and text[m.end(1):m.end(1) + 1] == ')':
        target = m.group(1)
    elif text.rfind('[', 0, m.start(1)) > text.rfind(']', 0, m.start(1)):
        tail = LINK_TAIL.match(text, m.end())
        if tail and tail.group(1).split('#', 1)[0].rsplit('/', 1)[-1] == leaf:
            target = tail.group(1)
    if target:
        p = _link_addressee(src, target, same)
        if p:
            return [p], 'link target'

    # 2-4. repo root / explicit path / sibling repo / abbreviation / bare basename
    cands, how = path_candidates(comps, anchored, sibling, same)

    # narrowing a: a file without line N is not the addressee
    if len(cands) > 1 and 'no-has-line' not in MUTATE:
        kept = [p for p in cands if has_line(p, n)]
        if len(kept) < len(cands):
            cands, how = kept, how + ' + has-line'
    # narrowing b: an explicit path earlier on the same line
    if len(cands) > 1:
        p = _same_line_antecedent(text[:m.start(1)], leaf, cands)
        if p:
            cands, how = [p], how + ' + same-line path'
    return cands, how


# ------------------------------------------------------------------- the scan

Finding = collections.namedtuple('Finding', 'src lno target n kind was now moved_to cands how')


def scan(repo, base, tip):
    changed = [p for p in repo.checked('diff', '--name-only', '-z', base, tip, '--').split('\0') if p]
    by_leaf = collections.defaultdict(list)
    for c in changed:
        by_leaf[c.rsplit('/', 1)[-1]].append(c)
    res = dict(base=base, tip=tip, changed=changed, found=0, tested=0, elsewhere=0,
               pinned=[], ambiguous=[], grep_errors=[])
    if not by_leaf:
        return res

    # every file, in either tree, sharing a changed file's basename
    universe = collections.defaultdict(set)
    for rev in (base, tip):
        for p in repo.tree(rev):
            leaf = p.rsplit('/', 1)[-1]
            if leaf in by_leaf:
                universe[leaf].add(p)
    universe = {leaf: sorted(ps) for leaf, ps in universe.items()}

    def lines_of(path):                                    # base if it existed there, else tip
        b = repo.blob(base, path)
        return b if b is not None else repo.blob(tip, path)

    def has_line(path, n):
        l = lines_of(path)
        return l is not None and 0 < n <= len(l)

    # candidate citers: any tracked line at TIP mentioning a changed file's leaf
    # name followed (within a few punctuation chars) by :NNN. git grep -I skips
    # binaries. Deliberately over-broad; resolved targets are validated after.
    # NOTE: candidate collection uses git grep with a FIXED STRING (-F), never a
    # regex. An earlier version passed an ERE to git grep and a near-identical
    # pattern to Python's re: inside a POSIX bracket expression a backslash is
    # LITERAL, so `[...\]]` demanded a literal ']' before the colon and the stage
    # silently under-collected -- it missed a citer I had already proved by hand.
    # One engine does the finding, one does the precision. Never two.
    # An unreadable blob is reported ONLY on stderr (`error: ... unable to read`) while
    # grep exits 0 or 1 with that file's lines missing from stdout: a citer never found.
    # So anything on stderr but a `warning:` is an error too.
    cand = collections.defaultdict(list)
    for leaf in by_leaf:
        rc, out = repo.raw('grep', '-nIF', leaf, tip, '--')
        noise = [l for l in repo.err.splitlines() if not l.startswith('warning:')]
        if 'grep-stderr-ok' in MUTATE:
            noise = []
        if rc > 1 or noise:                                # 1 is "no match"; >1 is a failure
            res['grep_errors'].append((leaf, 'exit %d%s' % (rc, ': ' + noise[0] if noise else '')))
        for line in out.decode('utf-8', 'replace').split('\n'):
            if not line.strip(): continue
            parts = line.split(':', 3)
            if len(parts) < 4: continue
            _, src, lno, text = parts[0], parts[1], parts[2], parts[3]
            cand[src].append((int(lno), text, leaf))

    for src, rows in cand.items():
        for lno, text, leaf in rows:
            same = universe.get(leaf, [])
            for m in re.finditer(PAT_TMPL % re.escape(leaf), text):
                if cite_comps(m.group(1))[0][-1] != leaf:
                    continue          # `universal-operators.md` is not a cite of `operators.md`
                n, cands = int(m.group(2)), None
                for target in by_leaf[leaf]:
                    if src == target and abs(lno - n) < 3: continue
                    b, t = repo.blob(base, target), repo.blob(tip, target)
                    if b is None or t is None: continue
                    res['found'] += 1
                    if cands is None:
                        if len(same) > 1:
                            repo.load(base, same)          # one batch for the has-line test
                        cands, how = addressees(m, leaf, src, text, same, has_line)
                    mine = [target] if 'basename-only' in MUTATE else cands
                    if target not in mine:
                        res['elsewhere'] += 1              # it addresses another file
                        continue
                    res['tested'] += 1
                    bl = b[n-1] if 0 < n <= len(b) else None
                    tl = t[n-1] if 0 < n <= len(t) else None
                    if bl is None: continue          # never a valid address at base
                    kind, moved_to = 'HOLDS', []
                    if tl is None:
                        kind, tl = 'OUT-OF-RANGE', ''
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
                    f = Finding(src, lno, target, n, kind, bl, tl,
                                moved_to[0] if moved_to else 0, tuple(mine), how)
                    # C == {T}: the cite's own text pins the changed file. Anything
                    # wider is a name shared by files the text cannot tell apart.
                    if len(mine) == 1 or 'no-uniqueness' in MUTATE:
                        if kind != 'HOLDS':
                            res['pinned'].append(f)
                    else:
                        res['ambiguous'].append(f)
    res['pinned'] = sorted(set(res['pinned']))
    res['ambiguous'] = sorted(set(res['ambiguous']))
    return res


def _show(f):
    b_, t_ = f.was.strip(), f.now.strip()
    mark = '  [differs beyond col 105]' if b_[:105] == t_[:105] else ''
    print(f'     was: {b_[:105]}{mark}')
    print(f'     now: {t_[:105]}{mark}')


def report(res, verbose=False):
    base, tip, changed = res['base'], res['tip'], res['changed']
    if not changed:
        print('no changed files'); return 0

    shifted = [f for f in res['pinned'] if f.kind in ROT]
    edited  = [f for f in res['pinned'] if f.kind == 'EDITED-IN-PLACE']
    amb     = res['ambiguous']
    amb_rot = [f for f in amb if f.kind in ROT]
    print(f'[inbound-cites] {base[:8]}..{tip[:8]}  changed-files={len(changed)}'
          f'  cites-found={res["found"]}  addressed-elsewhere={res["elsewhere"]}'
          f'  SHIFTED={len(shifted)} (real rot)  EDITED-IN-PLACE={len(edited)} (advisory)'
          f'  AMBIGUOUS-BASENAME={len(amb)} (advisory; {len(amb_rot)} would read SHIFTED)')

    listed = shifted + (edited if verbose else [])
    if res['found'] == 0:
        # An honest zero: liveness was PROVEN before the scan (see liveness()), so
        # "no cite names a changed file" is a finding, not a symptom.
        print('  clean — no corpus line-cite names a file this branch changed and that '
              'existed at the base; nothing could have moved')
    elif not listed:
        print('  clean — every corpus cite pinned to a changed file still holds its content')
    else:
        print()
    for f in listed:
        arrow = f' -- base content is now at :{f.moved_to}' if f.moved_to else ''
        print(f'  {f.src}:{f.lno}  ->  {f.target}:{f.n}   [{f.kind}]{arrow}')
        print(f'     pinned by: {f.how}')              # the rule to argue with, if this is wrong
        _show(f)
        print()

    amb_listed = amb if verbose else amb_rot
    if amb_listed:
        print()
        print('  AMBIGUOUS-BASENAME (advisory -- never fails the run). The cite names a file by a')
        print('  basename that 2+ tracked files share, and nothing in its text says which. IF it')
        print('  means the changed file it has moved; spell the path and this checker can tell.')
        print()
    for f in amb_listed:
        leaf = f.target.rsplit('/', 1)[-1]
        arrow = f' -- base content is now at :{f.moved_to}' if f.moved_to else ''
        others = [c for c in f.cands if c != f.target]
        more = f' (+{len(others) - 3} more)' if len(others) > 3 else ''
        print(f'  {f.src}:{f.lno}  ->  {leaf}:{f.n}   [AMBIGUOUS-BASENAME, {len(f.cands)} candidates'
              f' after: {f.how}]')
        print(f'     if it means {f.target}: {f.kind}{arrow}')
        print(f'     it could equally mean: {", ".join(others[:3])}{more}')
        if f.kind != 'HOLDS':
            _show(f)
        print()
    return 1 if shifted else 0


def liveness(repo, base, tip):
    """(reasons this run could NOT be trusted to report a zero, probes run). No
    reasons means alive.

    LIVENESS CONTROL, same shape as verify-fired-riders.py's: a FIXED positive
    control, proven before the scan, never inferred from what the scan yields. A
    checker that resolves nothing reports a clean it did not earn -- but "this
    branch's files are cited by nobody" is a true and common state, so yield is
    not evidence either way (see the docstring: 15 false aborts in 30 merges).
    The named failure modes are each tested directly instead: a bad rev, an
    erroring grep (scan() records those), and a bad pattern or a dead decider --
    which is what the self-gate is for. Measured precedent for the last one: an
    earlier build of this very script passed an ERE to `git grep` and a
    near-identical pattern to Python's `re`. Inside a POSIX bracket expression a
    backslash is LITERAL, so the git-grep arm silently under-collected and the
    script reported 3 moved cites where there were 79. One engine finds, one
    engine decides -- never two.
    """
    dead = []
    for name, rev in (('base', base), ('tip', tip)):
        if repo.raw('rev-parse', '--verify', '--quiet', rev + '^{tree}')[0] != 0:
            dead.append('%s rev %r does not resolve to a tree -- every git call on it '
                        'returns nothing' % (name, rev))
    lines = []
    try:
        if not run_gate(out=lines.append):
            dead.append('the self-gate FAILED -- this build cannot fire, or fires on a cite it must not:')
            dead += ['  ' + l.strip() for l in lines if '[FAIL]' in l]
    except (FixtureError, OSError) as exc:
        # Still exit 2 -- liveness was not proven -- but name the real cause.
        dead.append('the self-gate could not be BUILT (an environment fault, not a verdict '
                    'about the checker): %s' % exc)
    return dead, len(lines)


def guarded(mode):
    """Make any crash in `mode` an exit 2. An uncaught traceback exits 1, and 1 is the
    verdict "a pinned cite moved" -- a gate that could not run must never say that."""
    def run(*args, **kwargs):
        try:
            return mode(*args, **kwargs)
        except Exception as exc:
            traceback.print_exc()
            print('[inbound-cites] ABORT: the gate crashed (%s: %s) -- no verdict was reached.'
                  % (type(exc).__name__, exc))
            return 2
    return run


@guarded
def main(base, tip, verbose=False, repo=None):
    if repo is None:
        # From a subdirectory git grep searches only that subtree and ls-tree lists
        # paths relative to it: a clean that read a fraction of the corpus.
        repo = Repo(cwd=Repo().checked('rev-parse', '--show-toplevel').strip())
    dead, n_probes = liveness(repo, base, tip)
    res = None
    if not dead:
        try:
            res = scan(repo, base, tip)
        except GateError as exc:
            dead = [str(exc)]
        else:
            dead = ['`git grep` failed while collecting citers of %r (%s)' % err
                    for err in res['grep_errors']]
    if dead:
        print('[inbound-cites] ABORT: liveness failed -- a clean report here would be false.')
        for why in dead:
            print('  ' + why)
        return 2
    print('[inbound-cites] liveness OK — both revs resolve, every object read, self-gate %d/%d '
          '(a planted shifted cite fires; a cite to a same-named sibling does not; a damaged object '
          'aborts).' % (n_probes, n_probes))
    return report(res, verbose)


# ------------------------------------------------------------------- fixtures
#
# One throwaway repo, three files named main.tex (B, A, and a third that never
# changes), one unique basename, two citing files. Trees are built with
# `git write-tree`: no commit, so no identity, no hooks, no signing.

B = 'manuscript/vol_1_foundations/main.tex'            # the short volume main
A = 'papers/letter/main.tex'                           # the long same-named sibling
THIRD = 'manuscript/vol_2_subatomic/main.tex'
UNIQUE = 'src/unique_mod.py'
CITERS = 'docs/citers.md'
NOTES = 'manuscript/vol_1_foundations/notes.md'        # a citer BESIDE B
LONG = 'manuscript/vol_1_foundations/tables.tex'       # big enough that git STREAMS it

#: probe key -> (citing file, citing text). Every cite targets a line that exists.
PROBES = collections.OrderedDict([
    ('explicit-A',      (CITERS, 'Letter abstract floor, `papers/letter/main.tex:5` (explicit path to A)')),
    ('explicit-B',      (CITERS, 'vol 1 frontmatter, `manuscript/vol_1_foundations/main.tex:5`')),
    ('no-manuscript-B', (CITERS, 'same file without the leading dir: `vol_1_foundations/main.tex:6`')),
    ('abbreviated-B',   (CITERS, 'abbreviated volume dir: `vol_1/main.tex:7`')),
    ('elided-A',        (CITERS, 'elided path: `papers/.../main.tex:8`')),
    ('repo-root-B',     (CITERS, 'rooted at this repo: `AVE-Core/manuscript/vol_1_foundations/main.tex:9`')),
    ('absolute-B',      (CITERS, 'absolute, through the workspace umbrella dir: '
                                 '`/Users/someone/AVE-staging/AVE-Core/manuscript/vol_1_foundations/main.tex:13`')),
    ('sibling-repo',    (CITERS, 'another repo entirely: `AVE-HOPF/manuscript/vol_1_foundations/main.tex:5`')),
    ('same-line-B',     (CITERS, 'see `manuscript/vol_1_foundations/main.tex` frontmatter, then `main.tex:10`')),
    ('bare-ambiguous',  (CITERS, 'a bare `main.tex:4` names nobody in particular')),
    ('bare-has-line-A', (CITERS, 'a bare `main.tex:30` -- only the Letter is that long')),
    ('suffix-collision', (CITERS, 'a different file whose name ENDS in the leaf: `domain.tex:5`')),
    ('unique',          (CITERS, 'a basename only one file carries: `unique_mod.py:10`')),
    ('link-target-B',   (NOTES, 'link form, target beside the citer: [frontmatter](main.tex):11')),
    ('link-text-B',     (NOTES, 'link form, cite inside the text: [`main.tex:12`](./main.tex)')),
    ('beside-B-bare',   (NOTES, 'a bare `main.tex:3` from beside B is STILL ambiguous -- no same-directory rule')),
    ('long-file',       (CITERS, 'a long file, cited near its end: `tables.tex:290`')),
])


def _numbered(tag, k):
    return ['%s line %d' % (tag, i) for i in range(1, k + 1)]


def _files(keys, moved=()):
    """Fixture tree. `moved` files get three lines inserted at the top, so every
    line below keeps its content at a NEW address -- the definition of SHIFTED."""
    files = {B: _numbered('vol1', 14), A: _numbered('letter', 40),
             THIRD: _numbered('vol2', 14), UNIQUE: _numbered('code', 20),
             LONG: _numbered('table row of a long file', 300)}
    for p in moved:
        files[p] = ['inserted %d' % i for i in (1, 2, 3)] + files[p]
    for citer in (CITERS, NOTES):
        files[citer] = [PROBES[k][1] for k in keys if PROBES[k][0] == citer] or ['(no cites)']
    return files


class FixtureError(RuntimeError):
    """The throwaway repo could not be BUILT. An environment fault (a read-only
    TMPDIR, a git that will not init), never a verdict about the checker."""


def _write_tree(repo, root, files):
    for name in os.listdir(root):
        if name != '.git':
            full = os.path.join(root, name)
            shutil.rmtree(full) if os.path.isdir(full) else os.remove(full)
    for path, lines in files.items():
        full = os.path.join(root, path)
        os.makedirs(os.path.dirname(full), exist_ok=True)
        with open(full, 'w', encoding='utf-8') as fh:
            fh.write('\n'.join(lines) + '\n')
    if repo.raw('add', '-A', '-f', '.')[0] != 0:
        raise FixtureError('`git add` failed in %s: %s' % (root, repo.err or 'no output'))
    rc, out = repo.raw('write-tree')
    tree = out.decode('ascii', 'replace').strip()
    if rc != 0 or not re.fullmatch(r'[0-9a-f]{40,64}', tree):
        raise FixtureError('`git write-tree` failed in %s: %s' % (root, repo.err or 'no output'))
    return tree


@contextlib.contextmanager
def fixture_repo(keys, moved, damage=()):
    """A throwaway repo holding a base tree and a tip tree: yields (repo, base, tip).

    `damage`: ('base' | 'tip', path, 'delete' | 'truncate') -- after both trees are
    written, that object (blob or subtree) is deleted from the object store, or its
    loose file cut to half, so the trees still name it."""
    root = tempfile.mkdtemp(prefix='inbound-cite-selftest-')
    try:
        repo = Repo(cwd=root, scrub_env=True)
        if repo.raw('init', '-q')[0] != 0:
            raise FixtureError('`git init` failed in %s: %s' % (root, repo.err or 'no output'))
        base = _write_tree(repo, root, _files(keys))
        tip = _write_tree(repo, root, _files(keys, moved))
        for side, path, how in damage:
            rc, out = repo.raw('rev-parse', '--verify', '--quiet',
                               '%s:%s' % (base if side == 'base' else tip, path))
            oid = out.decode('ascii', 'replace').strip()
            if rc != 0 or not re.fullmatch(r'[0-9a-f]{40,64}', oid):
                raise FixtureError('no object for %s:%s to damage: %s' % (side, path, repo.err or oid))
            loose = os.path.join(root, '.git', 'objects', oid[:2], oid[2:])
            try:
                if how == 'delete':
                    os.remove(loose)
                else:
                    with open(loose, 'rb') as fh:
                        data = fh.read()
                    os.chmod(loose, 0o644)
                    with open(loose, 'wb') as fh:
                        fh.write(data[:len(data) // 2])
            except OSError as exc:
                raise FixtureError('could not %s the object for %s:%s: %s' % (how, side, path, exc))
        yield repo, base, tip
    finally:
        shutil.rmtree(root, ignore_errors=True)


def fixture_scan(keys, moved):
    """Run the REAL scan() over a throwaway repo.

    Returns ({probe: kind} pinned, {probe: kind} ambiguous, exit code, raw result)."""
    with fixture_repo(keys, moved) as (repo, base, tip):
        res = scan(repo, base, tip)
    where = {}
    for citer in (CITERS, NOTES):
        for i, k in enumerate([k for k in keys if PROBES[k][0] == citer], 1):
            where[(citer, i)] = k
    pinned = {where[(f.src, f.lno)]: f.kind for f in res['pinned']}
    amb = {where[(f.src, f.lno)]: f.kind for f in res['ambiguous']}
    return pinned, amb, (1 if any(k in ROT for k in pinned.values()) else 0), res


ALL = list(PROBES)
B_PINNED = {'explicit-B', 'no-manuscript-B', 'abbreviated-B', 'repo-root-B', 'absolute-B',
            'same-line-B', 'link-target-B', 'link-text-B'}
A_PINNED = {'explicit-A', 'elided-A', 'bare-has-line-A'}
AMBIG = {'bare-ambiguous', 'beside-B-bare'}

Lost = collections.namedtuple('Lost', 'side path damage keys moved how rule false_clean')

#: An object git cannot read, and what the run must do about it. Each fixture plants
#: `keys`, moves `moved` (exit 1 with every object present), then damages `side:path`.
#: `how` is how git reports it; `rule` the MUTATE key that turns the report into an
#: abort; `false_clean` what the run prints with that rule switched off. The citer
#: case comes twice because git grep's exit code is no signal: alone the lost file
#: makes it exit 1 ("no match"), beside any other match -- the usual case in a real
#: corpus -- exit 0.
LOST = collections.OrderedDict([
    ('citer blob (the only match)', Lost('tip', CITERS, 'delete', ['explicit-B'], [B],
        'git grep says so only on stderr, and exits 1 as for no match',
        'grep-stderr-ok', 'exit 0, cites-found=0')),
    ('citer blob (beside a match)', Lost('tip', CITERS, 'delete', ['explicit-B', 'beside-B-bare'], [B],
        'git grep says so only on stderr, and exits 0 for the other match',
        'grep-stderr-ok', 'exit 0, cites-found=1')),
    ('changed-file blob (deleted)', Lost('base', B, 'delete', ['explicit-B'], [B],
        '`cat-file --batch` answers `missing`, as for a path the tree does not hold',
        'missing-is-absent', 'exit 0, cites-found=0')),
    ('changed-file blob (cut short)', Lost('base', LONG, 'truncate', ['long-file'], [LONG],
        '`cat-file --batch` prints the full-size header, part of the body, then exits 128',
        'short-read-ok', 'exit 0, cites-found=1')),
    ('subtree (deleted)', Lost('tip', 'manuscript', 'delete', ['explicit-B'], [B],
        '`git diff` exits 128 with nothing on stdout -- "no changed files"',
        'unchecked-git', 'exit 0, cites-found=0')),
])


def lost_object_verdict(name, damaged=True):
    """What scan() makes of LOST[name]'s fixture once its object is damaged: 'ABORT' when
    the abort names the damaged path or object id, or else the verdict reached. An
    abort for any other reason (stray stderr, say) proves nothing about the loss.
    `damaged=False` runs the same fixture whole: the control, which must exit 1."""
    c = LOST[name]
    side, path = c.side, c.path
    res, why = None, ''
    damage = [(side, path, c.damage)] if damaged else []
    with fixture_repo(c.keys, c.moved, damage=damage) as (repo, base, tip):
        oid = repo.sh('rev-parse', '%s:%s' % (base if side == 'base' else tip, path)).strip()
        try:
            res = scan(repo, base, tip)
            why = ' | '.join(e[1] for e in res['grep_errors'])
        except GateError as exc:
            why = str(exc)
    if why:
        return 'ABORT' if (path in why or (oid and oid in why)) else 'ABORT, but not naming it: ' + why[:150]
    return 'exit %d, cites-found=%d' % (1 if any(f.kind in ROT for f in res['pinned']) else 0,
                                        res['found'])


def run_gate(out=print):
    ok = True

    def say(good, label, detail):
        nonlocal ok
        ok = ok and good
        out(f"  [{'PASS' if good else 'FAIL'}] {label}: {detail}")

    def rot(d):
        return {k for k, v in d.items() if v in ROT}

    # --- B (the short volume main) moves; A, its long same-named sibling, does not
    pinned, amb, rc, _ = fixture_scan(ALL, moved=[B])
    say('explicit-B' in rot(pinned), 'can-it-fire: an explicit-path cite to B is SHIFTED when B moves',
        f"{pinned.get('explicit-B', 'NOT FLAGGED -- THE CHECKER IS DEAD')}, exit {rc}")
    say('explicit-A' not in pinned and 'explicit-A' not in amb,
        'negative control: an explicit-path cite to same-named file A does NOT fire when B moves',
        'not tested against B' if 'explicit-A' not in pinned else 'FLAGGED -- the path text was ignored')
    diff = sorted(rot(pinned) ^ B_PINNED)
    say(not diff, 'every spelling that pins B fires (suffix, no-manuscript, abbreviation, repo root, '
        'absolute through the umbrella dir, same-line, both link forms)', f'{len(rot(pinned) & B_PINNED)}/{len(B_PINNED)}'
        + (f' -- MISMATCH on {diff}' if diff else ''))
    say(rot(amb) == AMBIG, 'a bare basename shared by 3 files is AMBIGUOUS-BASENAME, never SHIFTED -- '
        'even from beside B', f'{sorted(rot(amb))} advisory, {sorted(AMBIG & rot(pinned))} gating')
    quiet = {'elided-A', 'sibling-repo', 'bare-has-line-A', 'suffix-collision', 'unique'}
    say(not quiet & (set(pinned) | set(amb)), 'cites that cannot mean B are not reported at all '
        '(elided path to A, sibling repo, line only A has, `domain.tex`, another basename)',
        f'{sorted(quiet & (set(pinned) | set(amb))) or "none reported"}')

    # --- the mirror image: A moves, B does not
    pinned, amb, rc, _ = fixture_scan(ALL, moved=[A])
    say(rot(pinned) == A_PINNED, 'mirror: when A moves, exactly the cites that pin A fire '
        '(explicit, elided, and the bare cite only A has the line for)',
        f'{sorted(rot(pinned))}, exit {rc}')
    say('explicit-B' not in pinned, 'mirror negative control: the explicit-path cite to B stays silent',
        'not tested against A' if 'explicit-B' not in pinned else 'FLAGGED')

    # --- the reported defect in miniature: explicit-to-A + bare cites, B moves
    pinned, amb, rc, res = fixture_scan(['explicit-A', 'bare-ambiguous'], moved=[B])
    say(rc == 0 and not pinned and rot(amb) == {'bare-ambiguous'} and res['found'] == 2,
        'replay of the measured false positive: 2 cites found, SHIFTED=0, run passes, 1 advisory',
        f"found={res['found']} SHIFTED={len(rot(pinned))} advisory={sorted(rot(amb))} exit {rc}")

    # --- an honest zero: the only changed file is one nobody cites
    pinned, amb, rc, res = fixture_scan([], moved=[UNIQUE])
    say(res['found'] == 0 and not res['grep_errors'] and rc == 0,
        'a changed file that NO line cites is an honest zero, not evidence of a broken finder',
        f"found={res['found']} grep-errors={len(res['grep_errors'])} exit {rc}")

    # --- pre-existing behaviour: a unique basename still fires on the name alone
    pinned, amb, rc, _ = fixture_scan(ALL, moved=[UNIQUE])
    say(rot(pinned) == {'unique'} and not amb, 'a bare cite of a UNIQUE basename still fires on the name alone',
        f'{sorted(rot(pinned))}, exit {rc}')

    # --- an object that cannot be read aborts the run; it is never a file that is not there
    for name, c in LOST.items():
        v = lost_object_verdict(name)
        say(v == 'ABORT', f'a damaged {name} aborts the run ({c.how})', v)
    return ok


@guarded
def mutation_receipt():
    print('[inbound-cites] MUTATION RECEIPT -- each rule, switched off, must change the verdict')
    results = []

    def probe(mut, keys, moved):
        MUTATE.add(mut)
        try:
            pinned, amb, rc, _ = fixture_scan(keys, moved)
        finally:
            MUTATE.discard(mut)
        return {k for k, v in pinned.items() if v in ROT}, {k for k, v in amb.items() if v in ROT}

    pinned, _ = probe('basename-only', ALL, [B])
    results.append(('M1 revert to the pre-fix rule (every same-named changed file is an addressee): '
                    'the negative control must FIRE', 'explicit-A' in pinned))
    pinned, amb = probe('no-uniqueness', ALL, [B])
    results.append(('M2 drop the uniqueness rule: the ambiguous bare cites must become gating SHIFTED',
                    AMBIG <= pinned and not amb))
    pinned, amb = probe('no-has-line', ALL, [A])
    results.append(('M3 drop the has-line test: the bare cite only A is long enough to hold must fall '
                    'from pinned to ambiguous', 'bare-has-line-A' in amb and 'bare-has-line-A' not in pinned))
    pinned, amb = probe('address-nothing', ALL, [B])
    results.append(('M4 blind the resolver: can-it-fire must go silent', not pinned and not amb))
    MUTATE.add('address-nothing')
    try:
        dead = not run_gate(out=lambda line: None)
    finally:
        MUTATE.discard('address-nothing')
    results.append(('M5 ...and the gate must report itself dead rather than pass', dead))
    for k, (name, c) in enumerate(LOST.items(), 6):
        MUTATE.add(c.rule)
        try:
            v = lost_object_verdict(name)
        finally:
            MUTATE.discard(c.rule)
        whole = lost_object_verdict(name, damaged=False)
        results.append((f'M{k} read a damaged {name} as if whole or absent ({c.rule}): the run must print the false '
                        f'clean the abort exists to prevent, {c.false_clean} -- got {v}; the fixture whole '
                        f'must fire -- got {whole}', v == c.false_clean and whole.startswith('exit 1,')))

    allgood = True
    for label, tripped in results:
        print(f"  [{'OK' if tripped else 'BROKEN'}] {label} -> "
              f"{'probe holds (good)' if tripped else 'probe FAILS (BAD)'}")
        allgood = allgood and tripped
    if not allgood:
        print('[inbound-cites] MUTATION RECEIPT FAILED')
        return 1
    print('[inbound-cites] MUTATION RECEIPT OK: every perturbation trips and every probe holds.')
    return 0


@guarded
def selftest():
    print('[inbound-cites] SELF-TEST -- can-it-fire + negative controls (throwaway repo, real git)')
    if not run_gate():
        print('[inbound-cites] SELF-TEST FAILED')
        return 1
    print('[inbound-cites] SELF-TEST OK')
    return 0


if __name__ == '__main__':
    if '--selftest' in sys.argv:
        sys.exit(selftest())
    if '--mutation-receipt' in sys.argv:
        sys.exit(mutation_receipt())
    args = [a for a in sys.argv[1:] if a != '-v']
    if len(args) != 2:
        # 2, not sys.exit(<str>)'s 1: an empty `$(git merge-base ...)` in the Makefile
        # leaves one argument, and that is a gate that could not run, not a verdict.
        print('usage: verify-inbound-cite-shift.py <base> <tip> [-v] | --selftest | --mutation-receipt',
              file=sys.stderr)
        sys.exit(2)
    sys.exit(main(args[0], args[1], '-v' in sys.argv))
