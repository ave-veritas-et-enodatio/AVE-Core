#!/usr/bin/env python3
"""Inbound cite-shift checker.

The corpus pins by `path:NNN`. Any edit that moves a line silently re-points some
OTHER file's cite at different content. Nothing catches it: verify-md-links gates
only out-of-RANGE, verify-anchor-content is advisory and needs an adjacent excerpt.

The one question that matters: for every corpus cite targeting a file this branch
CHANGED, does the cited line still hold what it held at the merge-base?
base[N] != tip[N]  =>  the cite moved under its citer, silently.
A citer the branch itself rewrote is asked the same question from the number it
held at the base: see WHICH NUMBER.

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

WHICH NUMBER -- the cite a branch rewrote
-----------------------------------------
base[N] against tip[N] assumes the citer held N at the base. A branch that moves a
target line and updates the citer from `:old` to `:new` has REPAIRED the cite, and
that test then asks about the wrong line: it reads base[new], finds that line has
moved too, and reports SHIFTED with a wrong next number. A wrong re-pin read the
same, so until 2026-11-01 this script could not confirm a repair. The SHIFTED count
on #1037-#1039 did not fall after correct re-pins, and a byte check of base[old]
against tip[new], run by hand, had to stand in as the evidence.

When the citer line itself changed on the branch, the number it held at base is
recovered and the test is base[old] against tip[new]:

  RE-PINNED           base[old] == tip[new], and `new` is where the diff put that
                      line. A confirmed repair: counted, listed under -v, never
                      rot. The count is the evidence the hand check used to be.
  SHIFTED             the base content lives at another line. The re-pin is wrong
                      and the report gives the right number. Equal text does not
                      save it: unless the diff puts the cited line at `new`, `new`
                      is a look-alike.
  EDITED-IN-PLACE     the base content is gone and `new` falls in the hunk that
                      replaced it: the repair of a row that was also rewritten.
  RETARGETED          nothing moved under either number: base[new] == tip[new] (or
                      `new` is past the base end) and the cited line went nowhere
                      new. No repair, so nothing to confirm: advisory, listed under
                      -v, and never rot.
  UNCONFIRMED-RE-PIN  the base content is gone and `new` is neither its replacement
                      nor a line that kept still. Nothing can confirm this, so it
                      fails the run.

RETARGETED is the one departure from comparing the two lines, and it is measured.
On the 150 merges into main up to cbc668e7, base[old] != tip[new] alone raised 19
reports the plain test never made, every one on #915 and every one correct: its
hunks in `trampoline-framework.md` are 1->1 at :97, :220 and :713, so `:188` -> `:192`
moved nothing and corrected a cite already wrong at the base (the mass gap was
always at :192), and `:73` -> `:169` re-anchored a cite on text the same branch
added. So a re-pin adds a report to the plain test's only where it demonstrably
missed: the cited line moved and `new` is not where it went, on a line the plain
test passes because that line kept still, or `new` is past the end of the file.

The number is recovered by pairing the tip line with the base line it replaced:
first a line the branch moved whole, which holds what it held, so rows reversed
with their numbers intact are nobody's re-pin; then the same line but for its
numbers, anywhere in the file (a re-pin can move the line too), but only with no
rival on either side, because two rows alike but for their digits could pair either
way, and the wrong way passes a wrong re-pin and fails a right one; then what is
left of a hunk, line for line, when both sides are the same length (the prose
changed with the number). The k-th cite of the leaf on the tip line takes the k-th
on the base line, and the two lines must carry the same count, so swapped cites do
not read as two repairs. Anything else -- a new line, a line that gained a cite, a
reflowed line, a citer the branch renamed -- has no number to recover and keeps the
plain test, which can only report it.

A line rewritten in place therefore counts as the re-pin of the line it replaced,
however unrelated the new prose, as long as both cite the leaf. That is a choice.
The tool cannot read intent, a similarity threshold would be a number with nothing
measured behind it, and the mistake lands on the side of a report a person can read.

has-line asks a re-pinned cite for both of its numbers: a candidate has to hold the
number at the base and the new one at the tip. The old number alone would let a
wrong bare re-pin leave the gate, by keeping a short sibling the new number rules
out. The new one alone reads the wrong tree, and a re-pin can run past the base end
of the very file it addresses. A cite that kept its number reads one tree as it
always did.

WHICH LINE -- the address a SHIFTED report gives
------------------------------------------------
The address used to be the first identical line in the file, which misleads on any
repeated line: a `\\begin{itemize}` at :717 reported :6 when it had gone to :719.
It is now read off the hunks of base..tip. A line the diff left alone has moved by
the net shift of the hunks above it. A line the diff took out may have been put
back by another hunk (a block move); if several put-back lines qualify, the one
with the longest run of agreeing neighbours wins, and a tie gives no address. Every
address is CONFIRMED equal to the base line (after strip, the comparison the
verdict itself uses), so a wrong hunk costs the address and never invents one.

That changes the address and nothing else. SHIFTED against EDITED-IN-PLACE is still
the reach test: does the text survive anywhere in the file. A line the diff took
out whose text survives only at other lines therefore stays SHIFTED, says it has no
address, and does not guess. A re-pin onto one of those lines reads the same: no
address is the diff declining to agree, not agreeing. Nor does a blank line get a
pass for having no text to reach for: a re-pin onto another blank asks the diff
where the cited one went. A tie is the one case where no address leaves a re-pin
standing: either tied line is one the diff put there, so both pass and any other
line fails. A look-alike landing exactly on the cited address still reads HOLDS:
that is the plain test, which has no other line to compare.

LIVENESS -- a zero has to be earned, and NOT inferred from the run's own yield
------------------------------------------------------------------------------
A checker that finds nothing reports a clean it did not earn. Before any zero is
trusted, every run proves three things, none of them read off its own yield:

  * both revs resolve to a tree  (on a bad rev every git call returns nothing);
  * no git call failed           (`git grep` exiting 1 = "no match" is an answer,
                                 > 1 is an error; so is any `git diff-tree` error,
                                 which would silently cost every re-pin its number);
  * THE SELF-GATE holds          the --selftest fixtures, driven through this same
                                 scan() and git binary: a planted shifted cite IS
                                 reported, a cite to a same-named sibling is NOT, a
                                 correct re-pin passes, a wrong one fires.
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
  1  a cite PINNED to a changed file is SHIFTED, OUT-OF-RANGE or UNCONFIRMED-RE-PIN
  2  liveness failed -- no verdict was reached

SELF-TESTS
----------
    verify-inbound-cite-shift.py --selftest           can-it-fire + negative controls
    verify-inbound-cite-shift.py --mutation-receipt   each rule, removed, must trip
Both drive THIS scan() against a throwaway two-tree repo with the real git
binary. The negative control that matters: an explicit-path cite to file A must
NOT fire when same-named file B moves -- and the mutation receipt proves that
control is not vacuous, because under the pre-fix basename-only rule the very
same fixture DOES fire. REPINS, below, is the same discipline for WHICH NUMBER and
WHICH LINE: a table of one branch and every way a citer can respond to it, each
rule of those sections switched off in the receipt and shown to change a row.
"""
import collections, contextlib, os, posixpath, re, shutil, subprocess, sys, tempfile

THIS_REPO = 'AVE-Core'
SIBLING_REPO = re.compile(r'^(?:AVE-[A-Za-z0-9]+|Applied-Vacuum-Engineering)$')

PATH_CHARS = r'[A-Za-z0-9_./\\-]*'
PAT_TMPL = r'(' + PATH_CHARS + r'%s)[^A-Za-z0-9\s]{0,3}:(\d+)'
# `[leaf.md:NN](target)`: from the end of the cite to the link target that closes
# the link TEXT the cite sits in.
LINK_TAIL = re.compile(r'[^\[\]]{0,120}\]\(([^)\s]+)\)')
# A hunk header. Only the header is read: the lines themselves come from the blobs.
HUNK = re.compile(rb'^@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@', re.M)

ROT = ('SHIFTED', 'OUT-OF-RANGE', 'UNCONFIRMED-RE-PIN')

#: Rules switched OFF by --mutation-receipt. Empty in every real run.
MUTATE = set()


def line_count(lines):
    """The lines in a blob. `split('\\n')` leaves a '' after a final newline, and that
    is no line: a cite of it cites nothing."""
    return len(lines) - (lines[-1] == '' and 'phantom-line' not in MUTATE)


class Repo:
    """A git repo handle plus blob/tree caches.

    The real run uses the cwd and the caller's environment. The self-test fixtures
    use a throwaway directory with every GIT_* variable scrubbed: a fixture built
    while a git hook has GIT_DIR / GIT_INDEX_FILE exported would otherwise write
    into the REAL repo.
    """

    def __init__(self, cwd=None, scrub_env=False):
        self.cwd, self.env = cwd, None
        if scrub_env:
            self.env = {k: v for k, v in os.environ.items() if not k.startswith('GIT_')}
        self._blob, self._tree, self._hunks = {}, {}, {}
        self.diff_errors = []

    def raw(self, *a, stdin=None):
        r = subprocess.run(('git',) + a, capture_output=True, cwd=self.cwd,
                           env=self.env, input=stdin)
        self.err = r.stderr.decode('utf-8', 'replace').strip()
        return r.returncode, r.stdout

    def sh(self, *a):
        return self.raw(*a)[1].decode('utf-8', 'replace')

    def tree(self, rev):
        if rev not in self._tree:
            out = self.sh('ls-tree', '-r', '-z', '--name-only', rev)
            self._tree[rev] = [p for p in out.split('\0') if p]
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
        raw, i = self.raw('cat-file', '--batch', stdin=req)[1], 0
        for p in paths:
            j = raw.find(b'\n', i)
            head = raw[i:j].split() if j >= 0 else []
            lines = None
            if len(head) == 3 and head[2].isdigit():       # <sha> <type> <size>
                size = int(head[2])
                if head[1] == b'blob':
                    lines = raw[j + 1:j + 1 + size].decode('utf-8', 'replace').split('\n')
                i = j + 1 + size + 1
            else:                                          # `<name> missing`, or truncated
                i = j + 1 if j >= 0 else len(raw)
            self._blob[(rev, p)] = lines

    def hunks(self, base, tip, path):
        """[(a, c, s, d)]: base lines [a, a+c) became tip lines [s, s+d), in file order.

        Plumbing, so no diff.* setting of the caller's can change the answer, and
        -U0, so a line no hunk names is a line the diff left alone. git writes the
        start of a zero-length side as the line BEFORE the gap, hence the +1.
        """
        key = (base, tip, path)
        if key not in self._hunks:
            rc, out = self.raw('--literal-pathspecs', 'diff-tree', '-r', '-p', '-U0', '--text',
                               '--no-color', base, tip, '--', path)
            if rc != 0:
                self.diff_errors.append(path)
            self._hunks[key] = [
                (int(a) + (c == b'0'), int(c or 1), int(s) + (d == b'0'), int(d or 1))
                for a, c, s, d in HUNK.findall(out)]
        return self._hunks[key]


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


def addressees(m, leaf, src, text, same, has_line, held):
    """(candidate files, how) for the cite matched by `m` -- see the docstring.

    Context may only NARROW the set the path text allows, never step outside it.
    `held` is the number the cite held at base (see number_at_base). A re-pin is a
    claim about two trees, so has-line takes both numbers.
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
        was = n if 'has-line-at-tip' in MUTATE else held
        kept = [p for p in cands if has_line(p, was, was if 'has-line-at-held' in MUTATE else n)]
        # Past every tip end: no file holds both, and the number at base still narrows.
        if not kept:
            kept = [p for p in cands if has_line(p, was, was)]
        # A number dead at base addresses nothing: only the one it holds now can.
        if not kept and 'no-dead-fallback' not in MUTATE:
            kept = [p for p in cands if has_line(p, n, n)]
        if len(kept) < len(cands):
            cands, how = kept, how + ' + has-line'
    # narrowing b: an explicit path earlier on the same line
    if len(cands) > 1:
        p = _same_line_antecedent(text[:m.start(1)], leaf, cands)
        if p:
            cands, how = [p], how + ' + same-line path'
    return cands, how


# ----------------------------------------------------------- which number, which line

def leaf_cites(text, leaf):
    """The line-cites of `leaf` on one line of text. A name that merely ENDS in the
    leaf (`universal-operators.md` while `operators.md` changed) is not one of them."""
    return [m for m in re.finditer(PAT_TMPL % re.escape(leaf), text)
            if cite_comps(m.group(1))[0][-1] == leaf]


def _numberless(line):
    return re.sub(r'\d+', '#', line).strip()


def _pair_on(key, b, t, hunks, pairs, lone=False):
    """Pair the hunk lines not yet paired, anywhere in the file, that agree on `key`.
    `lone` takes a pair only when neither side has a rival."""
    gone, came = collections.defaultdict(list), collections.defaultdict(list)
    taken = set(pairs.values())
    for a, c, s, d in hunks:
        for i in range(a, a + c):
            if i not in taken:
                gone[key(b[i - 1])].append(i)
        for j in range(s, s + d):
            if j not in pairs:
                came[key(t[j - 1])].append(j)
    for k, news in came.items():
        if not lone or len(gone[k]) == len(news) == 1:
            pairs.update(zip(news, gone[k]))


def rewritten_lines(repo, base, tip, src):
    """{tip line: base line it replaced}, for the lines of `src` the branch rewrote."""
    b, t = repo.blob(base, src), repo.blob(tip, src)
    if b is None or t is None:
        return {}
    pairs, hunks = {}, repo.hunks(base, tip, src)
    # A line moved whole holds what it held. Identical lines hold the same numbers,
    # so it cannot matter which of them pairs with which.
    if 'no-exact-pairing' not in MUTATE:
        _pair_on(str.strip, b, t, hunks, pairs)
    # The same line but for its numbers, anywhere in the file: a re-pin can also
    # move the line, and git then shows it as two hunks.
    if 'no-numberless-pairing' not in MUTATE:
        _pair_on(_numberless, b, t, hunks, pairs, lone='no-lone-guard' not in MUTATE)
    # Otherwise what is left of a hunk, line for line, when both sides are the same
    # length: the prose changed along with the number.
    if 'no-hunk-pairing' not in MUTATE:
        taken = set(pairs.values())
        for a, c, s, d in hunks:
            olds = [i for i in range(a, a + c) if i not in taken or 'no-taken' in MUTATE]
            news = [j for j in range(s, s + d) if j not in pairs]
            if len(olds) == len(news) or 'no-same-length' in MUTATE:
                pairs.update(zip(news, olds))
    return pairs


def number_at_base(baseline, leaf, k, cites):
    """The number the k-th `leaf` cite on a tip line held on `baseline`, the base line
    that tip line replaced (None if it replaced none).

    Falls back to the number it holds now: on a line the branch left alone that IS
    the number at base, and a cite with nothing to recover from keeps the plain
    test, which can only report it.
    """
    n = int(cites[k].group(2))
    if baseline is None or 'no-repin' in MUTATE:
        return n
    olds = leaf_cites(baseline, leaf)
    if len(olds) != len(cites):
        return n
    return int(olds[0 if 'first-cite-only' in MUTATE else k].group(2))


def _agreeing_run(b, n, t, j):
    """How many lines around base line n and tip line j agree."""
    run = 0
    for step in (-1, 1):
        i, k = n - 1 + step, j - 1 + step
        while 0 <= i < len(b) and 0 <= k < len(t) and b[i].strip() == t[k].strip():
            run, i, k = run + 1, i + step, k + step
    return run


def lines_at_tip(hunks, b, t, n):
    """The lines base line n can live at, at tip, read off the hunks and CONFIRMED
    equal. None if the diff took it out for good -- the text may survive at a line
    that is not this one (a repeated `\\begin{itemize}`), and that is not an address.
    Two or more if put-back lines tie."""
    shift = 0
    for a, c, s, d in hunks:
        if n < a:
            break
        if n < a + c:
            shift = None                                   # the diff took this line out
            break
        shift = s + d - a - c
    if shift is not None:
        hits = [n + shift]
    elif 'no-block-move' in MUTATE:
        hits = []
    else:                                                  # a block move: put back by a hunk
        hits = [j for _, _, s, d in hunks for j in range(s, s + d)]
    if 'no-confirm' not in MUTATE:
        hits = [j for j in hits if 0 < j <= line_count(t) and t[j - 1].strip() == b[n - 1].strip()]
    if len(hits) > 1 and 'no-agreeing-run' not in MUTATE:
        runs = [_agreeing_run(b, n, t, j) for j in hits]
        hits = [j for j, r in zip(hits, runs) if r == max(runs)]
    return hits


def address_at_tip(hunks, b, t, n):
    """Where base line n lives at tip. 0 if the diff gives no single address."""
    hits = lines_at_tip(hunks, b, t, n)
    if 'no-agreeing-run' in MUTATE or 'no-tie' in MUTATE:
        hits = hits[:1]
    return hits[0] if len(hits) == 1 else 0


def verdict(repo, base, tip, target, b, t, held, n):
    """(kind, address at tip) for a cite that held line `held` at base and holds `n`.

    The two lines are both valid here; the caller has ruled out the other cases.
    """
    bl, tl, repin = b[held - 1].strip(), t[n - 1].strip(), held != n
    if repin and 'repin-no-compare' in MUTATE:
        return 'RE-PINNED', n
    if bl == tl and not repin:
        return 'HOLDS', 0
    # THE REACH TEST. Two very different things look identical at the cited address:
    #   SHIFTED  - the base content still exists in the file, at a DIFFERENT line.
    #              The address now returns someone else's subject, silently. Real rot.
    #   EDITED   - the base content is gone; the line was rewritten in place. The cite
    #              still points at the right row, with updated text. Usually the
    #              intended edit, not a defect.
    # Without this split the checker is the S4a scan again: a marker with no reach
    # test, 1.3% true-positive.
    seen = [j + 1 for j, l in enumerate(t) if l.strip() == bl] if bl else []
    hunks = repo.hunks(base, tip, target)
    # Blank has no text to reach for, so only a re-pin onto another blank asks the diff.
    ask = seen or (bl == tl and 'no-blank-address' not in MUTATE)
    if 'first-identical' in MUTATE:
        moved_to = seen[0] if seen else 0
    else:
        moved_to = address_at_tip(hunks, b, t, held) if ask else 0
    if bl == tl:
        # Equal text is thin evidence on a repeated line: the diff has the last word,
        # and no address is not its word. Either side of a tie is one it put there.
        put = lines_at_tip(hunks, b, t, held) if ask else []
        if 'no-tie-sides' in MUTATE:
            put = [moved_to]
        if n in put or 'no-diff-check' in MUTATE or ('no-address-agrees' in MUTATE and not moved_to):
            return 'RE-PINNED', n
        return 'SHIFTED', moved_to
    if not repin:
        return ('SHIFTED', moved_to) if seen else ('EDITED-IN-PLACE', 0)
    if not seen and 'no-landing' not in MUTATE and any(
            a <= held < a + c and s <= n < s + d for a, c, s, d in hunks):
        return 'EDITED-IN-PLACE', 0                        # onto the row that replaced it
    # Nothing moved under either number, so this is no repair and there is nothing
    # to confirm: the plain test has no complaint, and the cited line went nowhere.
    if (not 0 < n <= line_count(b) or b[n - 1].strip() == tl) and moved_to in (0, held) \
            and 'no-retarget' not in MUTATE:
        return 'RETARGETED', 0
    if seen:
        return 'SHIFTED', moved_to
    return ('EDITED-IN-PLACE' if 'no-unconfirmed' in MUTATE else 'UNCONFIRMED-RE-PIN'), 0


# ------------------------------------------------------------------- the scan

Finding = collections.namedtuple('Finding', 'src lno target n kind was now moved_to cands how held')


def scan(repo, base, tip):
    changed = [p for p in repo.sh('diff', '--name-only', '-z', base, tip).split('\0') if p]
    rewrites = dict.fromkeys(changed)                      # only these citers can hold a re-pin
    by_leaf = collections.defaultdict(list)
    for c in changed:
        by_leaf[c.rsplit('/', 1)[-1]].append(c)
    res = dict(base=base, tip=tip, changed=changed, found=0, tested=0, elsewhere=0,
               pinned=[], ambiguous=[], grep_errors=[], diff_errors=[])
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

    def has_line(path, held, n):                           # `held` at base, `n` at tip
        l = lines_of(path)
        if l is None or not 0 < held <= line_count(l):
            return False
        at_tip = repo.blob(tip, path)
        return held == n or 0 < n <= line_count(l if at_tip is None else at_tip)

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
        rc, out = repo.raw('grep', '-nIF', leaf, tip, '--')
        if rc > 1:                                         # 1 is "no match"; >1 is a failure
            res['grep_errors'].append(leaf)
        for line in out.decode('utf-8', 'replace').split('\n'):
            if not line.strip(): continue
            parts = line.split(':', 3)
            if len(parts) < 4: continue
            _, src, lno, text = parts[0], parts[1], parts[2], parts[3]
            cand[src].append((int(lno), text, leaf))

    for src, rows in cand.items():
        for lno, text, leaf in rows:
            same = universe.get(leaf, [])
            cites = leaf_cites(text, leaf)
            for k, m in enumerate(cites):
                n, cands, held = int(m.group(2)), None, None
                for target in by_leaf[leaf]:
                    if src == target and abs(lno - n) < 3: continue
                    b, t = repo.blob(base, target), repo.blob(tip, target)
                    if b is None or t is None: continue
                    res['found'] += 1
                    if cands is None:
                        if len(same) > 1:
                            repo.load(base, same)          # one batch for the has-line test
                        held = n
                        if src in rewrites:
                            if rewrites[src] is None:
                                rewrites[src] = rewritten_lines(repo, base, tip, src)
                            i = rewrites[src].get(lno)
                            baseline = repo.blob(base, src)[i - 1] if i else None
                            held = number_at_base(baseline, leaf, k, cites)
                        cands, how = addressees(m, leaf, src, text, same, has_line, held)
                    mine = [target] if 'basename-only' in MUTATE else cands
                    if target not in mine:
                        res['elsewhere'] += 1              # it addresses another file
                        continue
                    res['tested'] += 1
                    was = held                       # dead at base: only the plain test is left
                    if not 0 < held <= line_count(b) and 'no-dead-fallback' not in MUTATE:
                        was = n
                    bl = b[was-1] if 0 < was <= line_count(b) else None
                    tl = t[n-1] if 0 < n <= line_count(t) else None
                    if bl is None: continue          # never a valid address at base
                    moved_to = 0
                    if tl is None:
                        kind, tl = 'OUT-OF-RANGE', ''
                    else:
                        kind, moved_to = verdict(repo, base, tip, target, b, t, was, n)
                    f = Finding(src, lno, target, n, kind, bl, tl, moved_to, tuple(mine), how, was)
                    # C == {T}: the cite's own text pins the changed file. Anything
                    # wider is a name shared by files the text cannot tell apart.
                    if len(mine) == 1 or 'no-uniqueness' in MUTATE:
                        if kind != 'HOLDS':
                            res['pinned'].append(f)
                    else:
                        res['ambiguous'].append(f)
    res['pinned'] = sorted(set(res['pinned']))
    res['ambiguous'] = sorted(set(res['ambiguous']))
    res['diff_errors'] = sorted(set(repo.diff_errors))
    return res


def _show(f):
    b_, t_ = f.was.strip(), f.now.strip()
    mark = '  [differs beyond col 105]' if b_[:105] == t_[:105] else ''
    print(f'     was: {b_[:105]}{mark}')
    print(f'     now: {t_[:105]}{mark}')


def _arrow(f):
    """What the report says after the verdict: the re-pin, then the true address."""
    pin = f' -- re-pinned from :{f.held}' if f.held != f.n else ''
    if f.kind == 'RE-PINNED':
        return pin + ', confirmed: that line at base held this content'
    if f.kind == 'UNCONFIRMED-RE-PIN':
        return pin + '; the base content is gone and this is not the line that replaced it'
    if f.kind == 'RETARGETED':
        return pin + '; no repair: nothing moved under this number, so the aim was changed on purpose'
    if f.kind == 'SHIFTED' and not f.moved_to:
        note = 'the diff took this line out; its text survives only at other lines'
    elif f.moved_to:
        note = f'base content is now at :{f.moved_to}'
    else:
        return pin
    return f'{pin}; {note}' if pin else f' -- {note}'


def report(res, verbose=False):
    base, tip, changed = res['base'], res['tip'], res['changed']
    if not changed:
        print('no changed files'); return 0

    shifted = [f for f in res['pinned'] if f.kind in ROT]
    edited  = [f for f in res['pinned'] if f.kind == 'EDITED-IN-PLACE']
    repins  = [f for f in res['pinned'] if f.kind == 'RE-PINNED']
    aimed   = [f for f in res['pinned'] if f.kind == 'RETARGETED']
    amb     = res['ambiguous']
    amb_rot = [f for f in amb if f.kind in ROT]
    print(f'[inbound-cites] {base[:8]}..{tip[:8]}  changed-files={len(changed)}'
          f'  cites-found={res["found"]}  addressed-elsewhere={res["elsewhere"]}'
          f'  SHIFTED={len(shifted)} (real rot)  EDITED-IN-PLACE={len(edited)} (advisory)'
          f'  RE-PINNED={len(repins)} (confirmed repairs)  RETARGETED={len(aimed)} (advisory)'
          f'  AMBIGUOUS-BASENAME={len(amb)} (advisory; {len(amb_rot)} would read SHIFTED)')

    listed = shifted + (edited + repins + aimed if verbose else [])
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
        print(f'  {f.src}:{f.lno}  ->  {f.target}:{f.n}   [{f.kind}]{_arrow(f)}')
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
        others = [c for c in f.cands if c != f.target]
        more = f' (+{len(others) - 3} more)' if len(others) > 3 else ''
        print(f'  {f.src}:{f.lno}  ->  {leaf}:{f.n}   [AMBIGUOUS-BASENAME, {len(f.cands)} candidates'
              f' after: {f.how}]')
        print(f'     if it means {f.target}: {f.kind}{_arrow(f)}')
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


def main(base, tip, verbose=False, repo=None):
    repo = repo or Repo()
    dead, n_probes = liveness(repo, base, tip)
    res = None
    if not dead:
        res = scan(repo, base, tip)
        dead = ['`git grep` exited with an error while collecting citers of %r' % leaf
                for leaf in res['grep_errors']]
        dead += ['`git diff-tree` exited with an error on %r' % path for path in res['diff_errors']]
    if dead:
        print('[inbound-cites] ABORT: liveness failed -- a clean report here would be false.')
        for why in dead:
            print('  ' + why)
        return 2
    print('[inbound-cites] liveness OK — both revs resolve, no grep or diff error, self-gate %d/%d '
          '(a planted shifted cite fires; a cite to a same-named sibling does not; a correct '
          're-pin passes; a wrong one fires).' % (n_probes, n_probes))
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
])


def _numbered(tag, k):
    return ['%s line %d' % (tag, i) for i in range(1, k + 1)]


def _files(keys, moved=()):
    """Fixture tree. `moved` files get three lines inserted at the top, so every
    line below keeps its content at a NEW address -- the definition of SHIFTED."""
    files = {B: _numbered('vol1', 14), A: _numbered('letter', 40),
             THIRD: _numbered('vol2', 14), UNIQUE: _numbered('code', 20)}
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
    repo.sh('add', '-A', '-f', '.')
    rc, out = repo.raw('write-tree')
    tree = out.decode('ascii', 'replace').strip()
    if rc != 0 or not re.fullmatch(r'[0-9a-f]{40,64}', tree):
        raise FixtureError('`git write-tree` failed in %s: %s' % (root, repo.err or 'no output'))
    return tree


@contextlib.contextmanager
def two_trees(base_files, tip_files):
    """A throwaway repo holding a base tree and a tip tree: yields (repo, base, tip)."""
    root = tempfile.mkdtemp(prefix='inbound-cite-selftest-')
    try:
        repo = Repo(cwd=root, scrub_env=True)
        if repo.raw('init', '-q')[0] != 0:
            raise FixtureError('`git init` failed in %s: %s' % (root, repo.err or 'no output'))
        base = _write_tree(repo, root, base_files)
        yield repo, base, _write_tree(repo, root, tip_files)
    finally:
        shutil.rmtree(root, ignore_errors=True)


def fixture_repo(keys, moved):
    return two_trees(_files(keys), _files(keys, moved))


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


# One branch, one target changed every way a cite can care about, and one citing
# file with a line per way its author can respond: three lines go in at :5 (one of
# them a look-alike `\begin{itemize}`), `four` is rewritten, `block ...` moves to the
# end, the second `\item a` is taken out.

TARGET = 'manuscript/vol_1_foundations/target.md'
SHORT = 'docs/short/target.md'                         # only has-line tells a bare name apart
REPINNED = 'docs/repins.md'
ITEMIZE, ENDIZE = r'\begin{itemize}', r'\end{itemize}'
TARGET_BASE = ['one', ITEMIZE, r'\item a', ENDIZE,                   # :1-4
               'two', ITEMIZE, r'\item b', ENDIZE,                   # :5-8
               'three', 'four', 'five',                               # :9-11
               'block head', ITEMIZE, 'block tail',                   # :12-14
               'six', r'\item a', 'seven', 'eight', 'nine', 'ten',    # :15-20
               'eleven', 'twelve']                                    # :21-22
TARGET_TIP = ['one', ITEMIZE, r'\item a', ENDIZE,                    # :1-4
              'inserted 1', ITEMIZE, 'inserted 3',                    # :5-7
              'two', ITEMIZE, r'\item b', ENDIZE,                    # :8-11
              'three', 'four REWRITTEN', 'five',                      # :12-14
              'six', 'seven', 'eight', 'nine', 'ten',                 # :15-19
              'eleven', 'twelve',                                     # :20-21
              'block head', ITEMIZE, 'block tail']                    # :22-24
PATHED = 'vol_1_foundations/target.md'

# A second target for what the first has no room for. `same` :4 goes to both :6 and
# :8, a tie, and a third `same` keeps still at the end. The blanks :11 and :13 move.
EDGES = 'manuscript/vol_1_foundations/edges.md'
EDGES_BASE = ['swap a', 'x', 'swap b',                                # :1-3
              'same', 'p', 'q', 'r', 's', 't',                        # :4-9
              'one', '', 'two', '', 'three',                          # :10-14
              '  indented', 'same']                                   # :15-16
EDGES_TIP = ['swap b', 'x', 'swap a',                                 # :1-3
             'p', 'q', 'same', 'r', 'same', 's', 't',                 # :4-10
             'inserted', 'one', '', 'two', '', 'three',               # :11-16
             'indented', 'same']                                      # :17-18
EDGED = 'vol_1_foundations/edges.md'


def _cite(key, *numbers, leaf=PATHED):
    return key + ': ' + ' and '.join('`%s:%d`' % (leaf, n) for n in numbers)


def _rows(key, *rows, leaf=PATHED):
    """Table rows alike but for their digits: a row id and the number it cites."""
    return tuple('%s: row %d `%s:%d`' % (key, i, leaf, n) for i, n in rows)


def _edge(key, *numbers):
    return _cite(key, *numbers, leaf=EDGED)


BETWEEN = ('swap: anchor', 'swap: anchor too')          # two lines, so git keeps these and not a row

#: key -> (citing line at base, citing line at tip, what it must read as
#: [(number held at base, number at tip, kind, address reported)], what that proves).
REPINS = collections.OrderedDict([
    ('correct', (_cite('correct', 9), _cite('correct', 12), [(9, 12, 'RE-PINNED', 12)],
                 'a correct re-pin passes')),
    ('wrong', (_cite('wrong', 9), _cite('wrong', 13), [(9, 13, 'SHIFTED', 12)],
               'a wrong re-pin still fails, and the report gives the right number')),
    ('prose', ('prose: was worded `%s:11`' % PATHED, 'prose: reworded, and `%s:14`' % PATHED,
               [(11, 14, 'RE-PINNED', 14)], 'a re-pin on a line whose prose changed too passes')),
    ('moved', (_cite('moved', 17), _cite('moved', 16), [(17, 16, 'RE-PINNED', 16)],
               'a re-pin on a citer line that also moved passes')),
    ('two', (_cite('two', 18, 19), _cite('two', 17, 18),
             [(18, 17, 'RE-PINNED', 17), (19, 18, 'RE-PINNED', 18)],
             'two re-pins on one line are paired in order')),
    ('swapped', (_cite('swapped', 18, 19), _cite('swapped', 18, 17),
                 [(18, 18, 'SHIFTED', 17), (19, 17, 'SHIFTED', 18)],
                 'two cites swapped on one line fail: the right content, the wrong cite')),
    ('lookalike', (_cite('lookalike', 6), _cite('lookalike', 2), [(6, 2, 'SHIFTED', 9)],
                   'a re-pin onto an identical line elsewhere fails: the diff says :9')),
    ('lookalike-gone', (_cite('lookalike-gone', 16), _cite('lookalike-gone', 3), [(16, 3, 'SHIFTED', 0)],
                        'a re-pin onto a look-alike of a line the diff took out fails: no address is no agreement')),
    ('blank-right', (_edge('blank-right', 11), _edge('blank-right', 13), [(11, 13, 'RE-PINNED', 13)],
                     'a correct re-pin of a blank line passes: the diff says where it went')),
    ('blank-wrong', (_edge('blank-wrong', 11), _edge('blank-wrong', 15), [(11, 15, 'SHIFTED', 13)],
                     'a re-pin onto another blank line fails, with the right number')),
    ('tie-near', (_edge('tie-near', 4), _edge('tie-near', 6), [(4, 6, 'RE-PINNED', 6)],
                  'a re-pin onto one side of a tie passes: the diff put the line there')),
    ('tie-far', (_edge('tie-far', 4), _edge('tie-far', 8), [(4, 8, 'RE-PINNED', 8)],
                 'and so does one onto the other side: the diff cannot tell them apart')),
    ('tie-off', (_edge('tie-off', 4), _edge('tie-off', 18), [(4, 18, 'SHIFTED', 0)],
                 'a re-pin onto a look-alike off the tie fails, and does not guess a side')),
    ('tie-frozen', (_edge('tie-frozen', 4), _edge('tie-frozen', 4), [(4, 4, 'SHIFTED', 0)],
                    'a cite left on a tied line is reported with no address')),
    ('rewritten', (_cite('rewritten', 10), _cite('rewritten', 13), [(10, 13, 'EDITED-IN-PLACE', 0)],
                   'a re-pin onto the row that replaced the cited one is advisory')),
    ('gone', (_cite('gone', 10), _cite('gone', 5), [(10, 5, 'UNCONFIRMED-RE-PIN', 0)],
              'a re-pin away from content that is gone cannot be confirmed, and fails')),
    ('bare-past-end', (_cite('bare-past-end', 14, leaf='target.md'), _cite('bare-past-end', 24, leaf='target.md'),
                       [(14, 24, 'RE-PINNED', 24)],
                       'a bare re-pin past the end of the base file still has its addressee')),
    ('bare-wrong', (_cite('bare-wrong', 14, leaf='target.md'), _cite('bare-wrong', 23, leaf='target.md'),
                    [(14, 23, 'SHIFTED', 24)],
                    'a wrong bare re-pin past the end of the base file is not dropped silently')),
    ('bare-past-tip', (_cite('bare-past-tip', 14, leaf='target.md'), _cite('bare-past-tip', 25, leaf='target.md'),
                       [(14, 25, 'OUT-OF-RANGE', 0)],
                       'and one past the end of the tip file gates, one line past it: no such line exists')),
    ('bare-narrowed', (_cite('bare-narrowed', 5, leaf='target.md'), _cite('bare-narrowed', 12, leaf='target.md'),
                       [(5, 12, 'SHIFTED', 8)],
                       'a wrong bare re-pin only one file can hold at tip stays pinned to it, and gates')),
    ('deleted-sibling', ((_cite('deleted-sibling', 9), _cite('deleted-sibling', 11)), _cite('deleted-sibling', 12),
                         [(12, 12, 'SHIFTED', 22)],
                         'two rows alike, one gone and one re-pinned: nothing says which, so no number is read')),
    ('row-id', (_rows('row-id', (1, 9), (2, 11)), _rows('row-id', (2, 12)), [(12, 12, 'SHIFTED', 22)],
                'and a row that never held :9 does not pass on the strength of a sibling that did')),
    ('reversal', (_rows('reversal', (1, 9), (2, 11), (3, 14)), _rows('reversal', (3, 14), (2, 11), (1, 9)),
                  [(9, 9, 'SHIFTED', 12), (11, 11, 'SHIFTED', 14), (14, 14, 'SHIFTED', 24)],
                  'rows reversed with their numbers intact are nobody\'s re-pin')),
    ('swap', (_rows('swap', (1, 1), leaf=EDGED) + BETWEEN + _rows('swap', (2, 3), leaf=EDGED),
              _rows('swap', (2, 3), leaf=EDGED) + BETWEEN + _rows('swap', (1, 1), leaf=EDGED),
              [(1, 1, 'SHIFTED', 3), (3, 3, 'SHIFTED', 1)],
              'a target swap under two rows swapped whole does not read as two repairs')),
    ('rewrite', ('rewrite: an old sentence, `%s:9`' % PATHED, 'rewrite: nothing to do with it, `%s:2`' % PATHED,
                 [(9, 2, 'SHIFTED', 12)],
                 'a line rewritten in place is the re-pin of the line it replaced, whatever its prose')),
    ('longer', ('longer: was worded `%s:9`' % PATHED, ('longer: now worded `%s:12`' % PATHED, 'longer: and a new line'),
                [(12, 12, 'SHIFTED', 22)], 'a hunk that grew pairs nothing: which line replaced which is a guess')),
    ('taken', ('taken: see `%s:9`' % PATHED, ('taken: a new line, `%s:1`' % PATHED, 'taken: see `%s:12`' % PATHED),
               [(9, 12, 'RE-PINNED', 12)], 'a base line already paired is not paired twice')),
    ('added-cite', (_cite('added-cite', 9), _cite('added-cite', 12, 14),
                    [(12, 12, 'SHIFTED', 22), (14, 14, 'SHIFTED', 24)],
                    'a line that gained a cite pairs nothing: each cite keeps the plain test')),
    ('missed-onto-still', (_cite('missed-onto-still', 9), _cite('missed-onto-still', 2),
                           [(9, 2, 'SHIFTED', 12)],
                           'a re-pin that misses onto a line that kept still fails: its content moved')),
    ('past-tip-end', (_cite('past-tip-end', 9), _cite('past-tip-end', 99), [(9, 99, 'OUT-OF-RANGE', 0)],
                      'a re-pin past the end of the tip file fails, though the plain test skips it')),
    ('tip-end-plus-one', (_cite('tip-end-plus-one', 10), _cite('tip-end-plus-one', 25),
                          [(10, 25, 'OUT-OF-RANGE', 0)],
                          'the line after the last is out of range: a final newline is not a line')),
    ('frozen-past-base', (_cite('frozen-past-base', 23), _cite('frozen-past-base', 23), [],
                          'a cite one past the base end never had an address, so there is nothing to test')),
    ('retargeted', (_cite('retargeted', 1), _cite('retargeted', 3), [(1, 3, 'RETARGETED', 0)],
                    'a number changed with nothing moved under either is no repair: advisory')),
    ('retargeted-gone', (_cite('retargeted-gone', 10), _cite('retargeted-gone', 1),
                         [(10, 1, 'RETARGETED', 0)],
                         'and so is one away from gone content, onto a line that kept still')),
    ('retargeted-new', (_cite('retargeted-new', 10), _cite('retargeted-new', 24),
                        [(10, 24, 'RETARGETED', 0)],
                        'and so is one onto a line past the base end, which has no plain test')),
    ('base-end-plus-one', (_cite('base-end-plus-one', 10), _cite('base-end-plus-one', 23),
                           [(10, 23, 'RETARGETED', 0)],
                           'the first line past the base end reads as the next one does')),
    ('dead-at-base', (_cite('dead-at-base', 99), _cite('dead-at-base', 12), [(12, 12, 'SHIFTED', 22)],
                      'a re-pin from a number dead at base keeps the plain test, not silence')),
    ('dead-bare', (_cite('dead-bare', 99, leaf='target.md'), _cite('dead-bare', 12, leaf='target.md'),
                   [(12, 12, 'SHIFTED', 22)],
                   'and a bare one is not dropped by has-line, which no file can pass at :99')),
    ('frozen', (_cite('frozen', 9), _cite('frozen', 9), [(9, 9, 'SHIFTED', 12)],
                'a frozen cite is still reported')),
    ('reworded', ('reworded: was `%s:9`' % PATHED, 'reworded: now `%s:9`' % PATHED, [(9, 9, 'SHIFTED', 12)],
                  'a rewritten line that kept its number is still reported')),
    ('new-cite', (None, _cite('new-cite', 9), [(9, 9, 'SHIFTED', 12)],
                  'a cite with no base line keeps the plain test')),
    ('repeated', (_cite('repeated', 8), _cite('repeated', 8), [(8, 8, 'SHIFTED', 11)],
                  'a repeated line maps to where it went, not to the first look-alike at :4')),
    ('block', (_cite('block', 13), _cite('block', 13), [(13, 13, 'SHIFTED', 23)],
               'a repeated line in a moved block maps with its block, past the added look-alike at :6')),
    ('taken-out', (_cite('taken-out', 16), _cite('taken-out', 16), [(16, 16, 'SHIFTED', 0)],
                   'a line the diff took out gets no address, though its text survives at :3')),
    ('untouched', (_cite('untouched', 1), _cite('untouched', 1), [],
                   'a cite above every change holds')),
])


def _lines(row):
    return [row] if isinstance(row, str) else list(row or ())


def _repin_trees(keys):
    base, tip, last = [], [], []
    for i, key in enumerate(keys):
        was, now = REPINS[key][:2]
        base += _lines(was) + ['gap %d' % i]
        (last if key == 'moved' else tip).extend(_lines(now))
        tip.append('gap %d' % i)
    short = {SHORT: _numbered('short', 8)}
    return (dict(short, **{TARGET: TARGET_BASE, EDGES: EDGES_BASE, REPINNED: base}),
            dict(short, **{TARGET: TARGET_TIP, EDGES: EDGES_TIP, REPINNED: tip + last}))


class DiffThatLies(Repo):
    """A diff that reports nothing changed: what a broken parser or a bad cache
    would look like. An address read off it has to fail the confirmation."""

    def hunks(self, base, tip, path):
        return []


def repin_scan(keys=None, repo_cls=Repo):
    """Run the REAL scan() over the re-pin fixture.

    Returns ({key: [(held, n, kind, address)]}, exit code)."""
    with two_trees(*_repin_trees(keys or list(REPINS))) as (repo, base, tip):
        repo = repo_cls(cwd=repo.cwd, scrub_env=True)
        res = scan(repo, base, tip)
        lines = repo.blob(tip, REPINNED)
    got = collections.defaultdict(list)
    for f in res['pinned'] + [f for f in res['ambiguous'] if f.kind != 'HOLDS']:
        got[lines[f.lno - 1].split(':')[0]].append((f.held, f.n, f.kind, f.moved_to))
    rot = any(f.kind in ROT for f in res['pinned'])
    return {k: sorted(v) for k, v in got.items()}, (1 if rot else 0)


ALL = list(PROBES)
B_PINNED = {'explicit-B', 'no-manuscript-B', 'abbreviated-B', 'repo-root-B', 'absolute-B',
            'same-line-B', 'link-target-B', 'link-text-B'}
A_PINNED = {'explicit-A', 'elided-A', 'bare-has-line-A'}
AMBIG = {'bare-ambiguous', 'beside-B-bare'}


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

    # --- which number, which line: one branch, every way a citer can respond
    got, _ = repin_scan()
    for key, (_, _, want, label) in REPINS.items():
        say(got.get(key, []) == want, label, f"{key}: {got.get(key, 'not reported')}")
    got, rc = repin_scan(['correct', 'prose', 'moved', 'two', 'blank-right', 'tie-near', 'tie-far', 'untouched'])
    say(rc == 0, 'a branch whose citers carry only correct re-pins passes the run', f'exit {rc}')
    got, rc = repin_scan(['bare-narrowed'])
    say(rc == 1, 'a wrong bare re-pin gates: has-line reads it at both numbers, so a short sibling does not '
        'make it advisory', f'exit {rc}')
    got, _ = repin_scan(['frozen'], repo_cls=DiffThatLies)
    say(got.get('frozen') == [(9, 9, 'SHIFTED', 0)], 'a hunk address is confirmed equal: a diff that '
        'lies yields no address, and the verdict stands', f"{got.get('frozen', 'not reported')}")
    return ok


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

    def repin(mut, key, keys=None, repo_cls=Repo):
        MUTATE.update(mut.split('+'))
        try:
            return repin_scan(keys, repo_cls)[0].get(key, [])
        finally:
            MUTATE.difference_update(mut.split('+'))

    def repin_exit(mut, keys):
        MUTATE.add(mut)
        try:
            return repin_scan(keys)[1]
        finally:
            MUTATE.discard(mut)

    def kinds(rows):
        return {row[2] for row in rows}

    def addresses(rows):
        return {row[3] for row in rows}

    results.append(('M6 drop the re-pin rule: the correct re-pin must read SHIFTED again -- the reported defect',
                    kinds(repin('no-repin', 'correct')) == {'SHIFTED'}))
    results.append(('M7 accept any re-pin without comparing the lines: the wrong re-pin must pass',
                    kinds(repin('repin-no-compare', 'wrong')) == {'RE-PINNED'}))
    results.append(('M8 give every cite on a line the first number: the second of two re-pins must fail',
                    {'SHIFTED'} <= kinds(repin('first-cite-only', 'two'))))
    results.append(('M9 drop numberless pairing: the re-pin on a citer that also moved must fail',
                    kinds(repin('no-numberless-pairing', 'moved')) == {'SHIFTED'}))
    results.append(('M10 drop hunk pairing: the re-pin on a reworded line must fail',
                    kinds(repin('no-hunk-pairing', 'prose')) == {'SHIFTED'}))
    results.append(('M11 read has-line at one number: at the new one both bare re-pins past the base end must '
                    'fall silent, and at the old one the wrong bare re-pin must stop gating',
                    not repin('has-line-at-tip', 'bare-past-end') and not repin('has-line-at-tip', 'bare-wrong')
                    and repin_exit('has-line-at-held', ['bare-narrowed']) == 0))
    results.append(('M12 take equal text as proof: the re-pin onto a look-alike must pass',
                    kinds(repin('no-diff-check', 'lookalike')) == {'RE-PINNED'}))
    results.append(('M13 drop the unconfirmed verdict: the re-pin away from gone content must stop failing',
                    kinds(repin('no-unconfirmed', 'gone')) == {'EDITED-IN-PLACE'}))
    results.append(('M14 ignore where the replacement landed: the re-pin onto the rewritten row must fail',
                    kinds(repin('no-landing', 'rewritten')) == {'UNCONFIRMED-RE-PIN'}))
    results.append(('M15 revert to the first identical line: the repeated line must report :4 and the '
                    'line taken out :3', addresses(repin('first-identical', 'repeated')) == {4}
                    and addresses(repin('first-identical', 'taken-out')) == {3}))
    results.append(('M16 stop looking in other hunks: the moved block must lose its address',
                    addresses(repin('no-block-move', 'block')) == {0}))
    results.append(('M17 drop the agreeing run: the moved block must land on the added look-alike at :6',
                    addresses(repin('no-agreeing-run', 'block')) == {6}))
    results.append(('M18 drop the confirmation: a diff that lies must report the wrong address :9',
                    addresses(repin('no-confirm', 'frozen', ['frozen'], DiffThatLies)) == {9}))
    results.append(('M19 drop the fallback for a number dead at base: both such re-pins must vanish',
                    not repin('no-dead-fallback', 'dead-at-base') and not repin('no-dead-fallback', 'dead-bare')))
    results.append(('M20 drop the retarget rule: a deliberate correction must read as rot -- the false '
                    'positives measured on #915', kinds(repin('no-retarget', 'retargeted')) == {'SHIFTED'}
                    and kinds(repin('no-retarget', 'retargeted-gone')) == {'UNCONFIRMED-RE-PIN'}))
    results.append(('M21 read no address as agreement: the re-pin onto a look-alike of a deleted line must '
                    'pass -- the regression this rule closes',
                    kinds(repin('no-address-agrees', 'lookalike-gone')) == {'RE-PINNED'}))
    results.append(('M22 stop asking the diff about a blank line: the correct blank re-pin must fail and '
                    'the wrong one lose its address', kinds(repin('no-blank-address', 'blank-right')) == {'SHIFTED'}
                    and addresses(repin('no-blank-address', 'blank-wrong')) == {0}))
    results.append(('M23 ask only for the single address: both sides of a tie must fail -- the false '
                    'positive a bare `== new` makes', kinds(repin('no-tie-sides', 'tie-near')) == {'SHIFTED'}
                    and kinds(repin('no-tie-sides', 'tie-far')) == {'SHIFTED'}))
    results.append(('M24 drop the tie rule: a cite left on a tied line must be handed its first side as an '
                    'address', addresses(repin('no-tie', 'tie-frozen')) == {6}))
    results.append(('M25 let rivals pair in file order: a row must pass on the strength of its sibling',
                    kinds(repin('no-lone-guard', 'deleted-sibling')) == {'RE-PINNED'}
                    and kinds(repin('no-lone-guard', 'row-id')) == {'RE-PINNED'}))
    results.append(('M26 drop exact pairing: rows swapped whole over a target swap must read as two repairs',
                    kinds(repin('no-exact-pairing', 'swap')) == {'RE-PINNED'}))
    results.append(('M27 drop both: reversed rows with their numbers intact must change verdict',
                    repin('no-lone-guard+no-exact-pairing', 'reversal') != REPINS['reversal'][2]))
    results.append(('M28 drop the same-length guard: a hunk that grew must pair its first line',
                    kinds(repin('no-same-length', 'longer')) == {'RE-PINNED'}))
    results.append(('M29 pair a base line twice: the new line beside a re-pin must take its number',
                    len(repin('no-taken', 'taken')) == 2))
    results.append(('M30 count the final newline as a line: both boundaries must go back to reading off by one',
                    kinds(repin('phantom-line', 'tip-end-plus-one')) == {'RETARGETED'}
                    and kinds(repin('phantom-line', 'base-end-plus-one')) == {'UNCONFIRMED-RE-PIN'}))

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
        sys.exit('usage: verify-inbound-cite-shift.py <base> <tip> [-v] | --selftest | --mutation-receipt')
    sys.exit(main(args[0], args[1], '-v' in sys.argv))
