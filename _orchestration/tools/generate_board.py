#!/usr/bin/env python3
"""Generate _orchestration/BOARD.md from the repo's own machine-readable state.

WHY THIS EXISTS
---------------
The hand-maintained board went 11 days stale, and the only view of program state
became a Claude report. The fix is structural, not disciplinary: the board is
GENERATED from artifacts that cannot drift, because they ARE the state.

  claims.jsonl      -> what we know and how solid it is
  open-items/       -> what we are waiting on (one file per item, frontmatter)
  docket-entries/   -> which rulings exist (drives the propagation-debt scan)
  gh pr list        -> what is in flight
  git               -> where main is

No section of the OUTPUT is hand-written: every figure is read at run time from
those inputs. Anything the board should show has to become one of them first --
that is the forcing function that keeps it from rotting.

The honest exceptions, all in this file and all disclosed at their definition:
SELF_DISCLAIM (a hand-curated phrase list -- a HEURISTIC, which is why the board
prints "~"), STATUS_ORDER and REQUIRED_KEYS (schema vocabularies, fail-loud so a
gap is caught not absorbed), PR_LIMIT, the 0.80 top-tier threshold, and the
12-char anchor floor. An earlier draft claimed "no hand-maintained list ANYWHERE",
which was false -- and its replacement enumerated the exceptions as a closed set
while the same commit added a sixth. Add to this list when you add a constant.

FAIL-LOUD CONTRACT
------------------
Every input is REQUIRED. If an input is missing, empty, or errors, this exits
non-zero and writes NOTHING. A board that reports "0 open PRs" because `gh`
failed, or "0 of 0 experiments" because the schema drifted, is the
degrades-to-a-pass class. There is no partial-board path: every count that can
be zero-by-breakage is checked against its own input being non-empty.

NO DATE PINS, NO LINE PINS, NO HAND-KEPT SETS
---------------------------------------------
Nothing hardcodes a date, a SHA, a count, or a line number. Every number is read
at run time and every set is derived. Two cautionary tales, both first-party:
  * the r40 span checker's date-pinned STAMP regex fails open and silently once
    the date moves;
  * v1 of THIS file shipped a hand-kept PROPAGATION_TOKENS list -- a
    hand-maintained tracker inside a generator written to abolish them, which
    understated the real debt by ~4x.

Open-item `source:` pointers are validated by ANCHOR TEXT, never line number.
v1 shipped line-pinned pointers and broke 14 of 15 of them in the same commit
that created them, by prepending a freeze header to the file they pointed into.

USAGE
    python3 _orchestration/tools/generate_board.py            # write BOARD.md
    python3 _orchestration/tools/generate_board.py --check    # fail if hand-edited

`--check` compares the stable sections with commit SHAs normalized out. TWO
things here are unstable for reasons that have nothing to do with a hand edit,
and both made an earlier `--check` red on arrival:
  * the open-PR list changes whenever anyone touches any PR, including this
    board's own PR -- so that section is excluded entirely;
  * the scanned-tree SHA is SELF-REFERENTIAL. A board committed in commit X can
    only ever name X's parent, because the SHA is read before the commit
    containing the board exists. So a committed board is permanently one SHA
    behind, forever, by construction.
A check that cries wolf gets disabled, and a disabled gate is a lie -- so SHAs
are normalized before comparison and everything else must match byte-for-byte.
This is a LOCAL guard against hand edits, not a CI gate.
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
from collections import Counter
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
CLAIMS = REPO / "manuscript/ave-kb/.index/claims.jsonl"
BOARD = REPO / "_orchestration/BOARD.md"
OPEN_ITEMS = REPO / "_orchestration/open-items"
DOCKET = REPO / "_orchestration/docket-entries"

# Display order, most-blocking first. A status outside this list is FATAL, not a
# skipped row -- a silently-dropped open item is the failure this directory exists
# to prevent. Ownership is read from the `owner` field, never inferred from status
# (v1 inferred it and contradicted its own printed table).
STATUS_ORDER = ["ROUTED-TO-GRANT", "OPEN-IN-WALK", "OPEN", "REGISTERED",
                "QUEUED", "PARKED"]
REQUIRED_KEYS = ["id", "title", "status", "owner", "opened", "source", "anchor"]
# `owner` DRIVES A PRINTED HEADLINE ("N of M open items are owned by Grant"), so it
# gets the same enum gate `status` has. It shipped as free text: `owner: grant
# (walking it)` -- a human-plausible annotation -- silently dropped an item out of
# the Grant-owned count with exit 0. Same silently-skipped class, different field.
OWNERS = ["grant", "lane", "unassigned"]

PR_LIMIT = 200
VOLATILE_HEADING = "## In flight"   # excluded from --check; see module docstring

# HAND-CURATED HEURISTIC, and the board prints "~" because of it. A claim that
# disclaims itself in words outside this list is NOT counted and nothing fails --
# demonstrated: 31 rationales rewritten to "BOOKKEEPING-ONLY, asserts no physical
# content" still reported the same figure. Treat the number as a floor, not a
# census. Used only to COUNT bookkeeping in the top tier -- never to reclassify.
SELF_DISCLAIM = [
    "definitional", "identity-grade", "true by construction",
    "zero predictive content", "not a physics prediction", "not a prediction",
    "disclaims", "derives nothing", "no emergence claim", "consistency-check",
    "algebra-not-prediction", "notation convention", "catalog",
]


def die(msg: str) -> None:
    print(f"[board] FATAL: {msg}", file=sys.stderr)
    print("[board] wrote nothing (fail-loud: a partial board is a false board)",
          file=sys.stderr)
    sys.exit(1)


def run(cmd: list[str], what: str) -> str:
    try:
        p = subprocess.run(cmd, capture_output=True, text=True, timeout=180)
    except Exception as e:  # noqa: BLE001 - any failure here is fatal
        die(f"{what}: {e}")
    if p.returncode != 0:
        die(f"{what} exited {p.returncode}: {p.stderr.strip()[:400]}")
    return p.stdout


def load_claims() -> list[dict]:
    if not CLAIMS.is_file():
        die(f"claims index not found at {CLAIMS}")
    rows = []
    for n, line in enumerate(CLAIMS.read_text(encoding="utf-8").splitlines(), 1):
        line = line.strip()
        if not line:
            continue
        try:
            rows.append(json.loads(line))
        except json.JSONDecodeError as e:
            die(f"{CLAIMS}:{n} is not valid JSON: {e}")
    if not rows:
        die("claims index parsed to zero records (an empty scan is not a clean scan)")
    return rows


def load_open_items() -> list[dict]:
    """Parse one-file-per-item frontmatter. Deliberately a small hand parser, not
    PyYAML: the schema is seven flat string keys, and a dependency is a thing that
    can be missing on someone else's machine.

    Uses rglob and accepts ONLY `.md` -- v1 used a flat glob, so a fragment in a
    subdirectory or saved as `.markdown` was silently skipped while the board
    reported a clean run."""
    if not OPEN_ITEMS.is_dir():
        die(f"open-items directory not found at {OPEN_ITEMS}")

    strays = [p for p in OPEN_ITEMS.rglob("*")
              if p.is_file() and p.suffix.lower() != ".md"
              and not p.name.startswith(".")]   # Finder drops .DS_Store in here
    if strays:
        die(f"non-.md file(s) in open-items/: {[s.name for s in strays]}. "
            f"Rename to .md or move out -- items are never silently skipped.")

    items, seen = [], {}
    for f in sorted(OPEN_ITEMS.rglob("*.md")):
        if f.name == "README.md":
            continue
        rel = f.relative_to(OPEN_ITEMS)
        lines = f.read_text(encoding="utf-8").splitlines()
        if not lines or lines[0].strip() != "---":
            die(f"{rel}: no frontmatter (first line must be '---')")
        try:
            end = lines.index("---", 1)
        except ValueError:
            die(f"{rel}: frontmatter is never closed")

        meta = {}
        for raw in lines[1:end]:
            if not raw.strip() or raw.lstrip().startswith("#"):
                continue
            if ":" not in raw:
                die(f"{rel}: frontmatter line is not 'key: value' -> {raw!r}")
            k, _, v = raw.partition(":")
            k = k.strip()
            if k in meta:
                die(f"{rel}: duplicate frontmatter key {k!r}. "
                    f"v1 took last-wins silently, which demoted an item's status.")
            v = v.strip()
            if len(v) >= 2 and v[0] in "\"'" and v.endswith(v[0]):
                # Quoted: verbatim. Anchors routinely contain '#' (issue numbers,
                # markdown headings), so comment-stripping must not touch them --
                # doing so truncated an anchor to the empty string and, worse,
                # silently truncated others mid-string while still validating.
                meta[k] = v[1:-1]
            else:
                # NO inline-comment stripping. Values here routinely contain '#'
                # (issue numbers, markdown headings); a '#' heuristic truncated a
                # title mid-string and an anchor to empty. Comments go on their
                # own line, which is already skipped above.
                meta[k] = v

        for k in REQUIRED_KEYS:
            if not meta.get(k):
                die(f"{rel}: frontmatter is missing required key '{k}'")
        if meta["owner"].lower() not in OWNERS:
            die(f"{rel}: owner {meta['owner']!r} is not one of {OWNERS}. It drives "
                f"a printed headline -- annotations belong in the body, not here.")
        if meta["status"] not in STATUS_ORDER:
            die(f"{rel}: status {meta['status']!r} is not one of {STATUS_ORDER}. "
                f"Fix the file or add the status -- items are never silently skipped.")
        if meta["id"] in seen:
            die(f"{rel}: duplicate id {meta['id']!r} (also in {seen[meta['id']]})")

        # ANCHOR VALIDATION -- the whole point of `anchor:`. A pointer that does not
        # resolve is worse than no pointer: it reads as evidence and is not.
        src = REPO / meta["source"]
        if not src.is_file():
            die(f"{rel}: source {meta['source']!r} does not exist")
        body = src.read_text(encoding="utf-8", errors="replace")
        hits = body.count(meta["anchor"])
        if hits == 0:
            die(f"{rel}: anchor text not found in {meta['source']}.\n"
                f"         anchor: {meta['anchor']!r}\n"
                f"         The source moved or was rewritten. Repoint the anchor; "
                f"do NOT convert it back to a line number.")
        # Membership alone is not a pointer: `anchor: the` resolves and pins nothing.
        if hits > 1:
            die(f"{rel}: anchor occurs {hits} times in {meta['source']} -- it must "
                f"identify ONE place. Lengthen it.\n         anchor: {meta['anchor']!r}")
        # A corpus node id (clm-/def-/sup-/exp-/ilk- + 6 chars = 10) is the most
        # rewrite-stable pointer available -- it survives rewording, which quoted
        # prose does not. A blunt 12-char floor rejected exactly those and pushed
        # authors toward prose, i.e. toward the thing that goes stale.
        is_node_id = re.fullmatch(r"(clm|def|sup|exp|ilk)-[a-z0-9]{6}", meta["anchor"])
        if not is_node_id and len(meta["anchor"]) < 12:
            die(f"{rel}: anchor {meta['anchor']!r} is too short to be a stable "
                f"pointer (min 12 chars, or a bare clm-/def-/sup-/exp-/ilk- node "
                f"id). Quote more of the source line.")

        seen[meta["id"]] = str(rel)
        meta["_file"] = str(rel)
        items.append(meta)

    if not items:
        die("open-items/ contains no items. If the program truly has zero open "
            "decisions, say so explicitly by adding a file that says that.")
    return items


def docketed_rulings() -> tuple[set[str], set[str]]:
    """Return (recorded, unclassified_filenames) -- two sets.

    `recorded` is the UNION of two conventions the corpus actually uses:
      * docket FILENAMES  -- `...-ruling-r52-...`, `...-rulings-r45-r47.md` (ranges
        expanded inclusively);
      * `## R<N> — ` HEADINGS inside any `*ruling*` docket file.

    THE HEADING RULE IS THE ONE THAT MATTERS. R1-R22 are all real rulings recorded
    under headings in five `rulings-*.md` files whose filenames carry no number at
    all (`2026-08-06-rulings-final-batch.md` etc.), and the corpus cites them as
    rulings in prose. A filename-only derivation missed every one, printed a debt
    ~1.8x too low, and -- worse -- shipped a disclosure telling the reader those
    numbers were "probably not rulings at all". They were.

    The union is decidable and it closes cleanly: R1-R53, no gaps, no duplicates,
    no file claiming a number another file claims. An earlier version of this
    function called the selection rule undecidable. It is not; nobody had grepped
    for the heading convention."""
    if not DOCKET.is_dir():
        die(f"docket-entries directory not found at {DOCKET}")
    files = [f for f in sorted(DOCKET.glob("*.md")) if f.name != "README.md"]
    if not files:
        die("docket-entries/ is empty -- an empty scan is not a clean scan")

    recorded: set[str] = set()
    for f in files:
        # filename convention: the number must sit in a `ruling-`/`rulings-` segment
        for m in re.finditer(r"\brulings?-((?:r\d{1,3}-?)+)", f.name.lower()):
            nums = [int(n) for n in re.findall(r"r(\d{1,3})", m.group(1))]
            if len(nums) == 2 and nums[1] > nums[0] + 1:
                recorded |= {f"R{n}" for n in range(nums[0], nums[1] + 1)}
            else:
                recorded |= {f"R{n}" for n in nums}
        # heading convention, inside any ruling-ish docket file
        if "ruling" in f.name.lower():
            recorded |= {f"R{int(n)}" for n in re.findall(
                r"^#{1,4} R(\d{1,3}) [-\u2014]", f.read_text(errors="replace"), re.M)}

    if not recorded:
        die("no ruling identifiers found in docket-entries/ by EITHER the filename "
            "or the heading convention -- both changed and the scan is now blind")

    # Surfaced, not absorbed: a bare rN in a filename outside a `ruling-` segment.
    loose: set[str] = set()
    for f in files:
        for a, b in re.findall(r"\br(\d{1,3})-r(\d{1,3})\b", f.name.lower()):
            lo, hi = sorted((int(a), int(b)))
            loose |= {f"R{n}" for n in range(lo, hi + 1)}
        loose |= {f"R{int(n)}" for n in re.findall(r"\br(\d{1,3})\b", f.name.lower())}
    return recorded, loose - recorded


def main() -> int:
    check_only = "--check" in sys.argv

    # ---- inputs (all required) -------------------------------------------
    rows = load_claims()
    open_items = load_open_items()
    rulings, unclassified_filenames = docketed_rulings()

    claims = [r for r in rows if r.get("node_type") == "claim"]
    experiments = [r for r in rows if r.get("node_type") == "experiment"]
    if not claims:
        die("zero claim nodes found -- schema changed or index is broken")
    if not experiments:
        die("zero experiment nodes found -- schema changed or index is broken. "
            "Reporting '0 of 0 experiments run' would read as reassuring news "
            "about a broken index.")

    # Best-effort refresh so the origin/main comparison is meaningful. NOT fatal:
    # the board must stay readable offline. See the divergence check below -- that,
    # not the fetch, is what makes the header honest.
    subprocess.run(["git", "-C", str(REPO), "fetch", "--quiet", "origin", "main"],
                   capture_output=True, timeout=180)

    pr_json = run(
        ["gh", "pr", "list", "--json", "number,title", "--limit", str(PR_LIMIT)],
        "gh pr list (is gh authenticated?)",
    )
    try:
        prs = json.loads(pr_json)
    except json.JSONDecodeError as e:
        die(f"gh returned unparseable JSON: {e}")
    if len(prs) >= PR_LIMIT:
        die(f"gh returned {len(prs)} PRs, at the --limit of {PR_LIMIT}; the list "
            f"may be truncated. Raise PR_LIMIT rather than under-report.")

    # THE SCANNED TREE IS HEAD, NOT origin/main. Every tracked-file input above was
    # read from the checkout. v2 printed origin/main's SHA beside numbers derived
    # from the branch -- so the board could print a count that was wrong for the SHA
    # printed next to it. Report what was actually scanned, and disclose divergence.
    head_sha = run(["git", "-C", str(REPO), "rev-parse", "--short", "HEAD"],
                   "git rev-parse HEAD").strip()
    head_when = run(["git", "-C", str(REPO), "log", "-1", "--format=%ad",
                     "--date=short", "HEAD"], "git log HEAD").strip()
    main_sha = run(["git", "-C", str(REPO), "rev-parse", "--short", "origin/main"],
                   "git rev-parse origin/main").strip()
    # Match the banner's WORDING exactly: "a tree that is not origin/main".
    # An ancestry predicate said something different and stayed silent when HEAD
    # was AHEAD of main -- a genuinely different tree, no banner.
    diverged = head_sha != main_sha

    # ---- the headline: is anything experimentally supported? --------------
    exp_solid = [c for c in claims if c.get("experimental_solidity") is not None]
    exp_run = [e for e in experiments if (e.get("status") or "").lower() == "run"]

    # ---- solidity distribution (band names derived, never hardcoded) -------
    bands = Counter(c.get("build_band") or "unknown" for c in claims)
    # (No tally guard here: `bands` is built by one increment per claim, so
    # sum(bands.values()) == len(claims) is an identity and a guard on it could
    # never fire. The real fix for the dropped-row defect is that the table below
    # renders every band NAME found in the data, plus an explicit total row.)
    top = sorted(
        (c for c in claims if isinstance(c.get("solidity"), (int, float))
         and c["solidity"] >= 0.80),
        key=lambda c: -c["solidity"],
    )
    disclaimed = sum(
        1 for c in top
        if any(t in (c.get("rationale") or "").lower() for t in SELF_DISCLAIM)
    )

    # ---- propagation debt: docketed rulings absent from the claims register -
    register_text = CLAIMS.read_text(encoding="utf-8")
    leaves = list(REPO.glob("manuscript/ave-kb/**/claim-quality.md"))
    if not leaves:
        die("no claim-quality.md leaves found -- the propagation scan would be "
            "red-by-construction rather than red-by-fact")
    for leaf in leaves:
        register_text += leaf.read_text(encoding="utf-8", errors="replace")
    # Word-boundary, not substring: v1's `"R51" in text` cleared the debt on any
    # incidental token (a SPICE designator `R54` lives in this repo already).
    unpropagated = sorted(
        (t for t in rulings if not re.search(rf"\b{t}\b", register_text)),
        key=lambda t: int(t[1:]),
    )

    # ---- review state, parsed from the title convention -------------------
    def state(t: str) -> str:
        u = t.upper()
        for token, label in (("[REVIEW: CLEARED]", "CLEARED"),
                             ("PENDING-ORCHESTRATOR", "pending-review"),
                             ("RECORDS-CLASS", "records-class")):
            if token in u:
                return label
        return "unlabelled"

    # ---- render -----------------------------------------------------------
    L: list[str] = []
    A = L.append
    A("<!-- GENERATED FILE - DO NOT EDIT BY HAND.")
    A("     Regenerate: python3 _orchestration/tools/generate_board.py")
    A("     Hand edits are overwritten; `--check` catches them. -->")
    A("")
    A("# AVE program board")
    A("")
    A(f"Scanned tree **{head_sha}** ({head_when}) · {len(rows)} index records · "
      f"{len(claims)} claims · {len(prs)} PR{'' if len(prs) == 1 else 's'} open")
    A("")
    if diverged:
        A(f"> ⚑ **This board was generated from a tree that is not `origin/main`** "
          f"(`{main_sha}`). Every count below describes **{head_sha}**. Regenerate "
          f"on main before reading these as program state.")
        A("")
    A("## The number that frames everything")
    A("")
    A(f"**{len(exp_solid)} of {len(claims)} claims carry any experimental support. "
      f"{len(exp_run)} of {len(experiments)} experiments have been run.**")
    A("")
    if not exp_solid:
        A("Every solidity score in this corpus is a **derivation** score. Nothing has "
          "been measured. That is what the testing pivot exists to change, and until "
          "one experiment runs, this line does not move.")
        A("")
    A("## What we know")
    A("")
    A("| build band | claims |")
    A("|---|---|")
    for band, n in bands.most_common():
        A(f"| {band} | {n} |")
    A(f"| **total** | **{sum(bands.values())}** |")
    A("")
    A(f"**Top tier (solidity ≥ 0.80): {len(top)} claims — of which ~{disclaimed} "
      f"self-disclaim** as definitional, catalog, notation, or consistency-class "
      f"in their own rationale. Read the top of the ranking with that in mind.")
    A("")
    A("## What we are waiting on")
    A("")
    grant_owed = [i for i in open_items if i["owner"].lower() == "grant"]
    A(f"**{len(grant_owed)} of {len(open_items)} open items are owned by Grant.** "
      f"Nothing fires on those without his word — including the PARKED ones, which "
      f"need an explicit word to unpark.")
    A("")
    A("| item | status | owner | open since |")
    A("|---|---|---|---|")
    for i in sorted(open_items, key=lambda i: (STATUS_ORDER.index(i["status"]),
                                               i["opened"])):
        A(f"| [{i['title']}](open-items/{i['_file']}) | {i['status']} | "
          f"{i['owner']} | {i['opened']} |")
    A("")
    A("## Propagation debt")
    A("")
    A(f"**{len(unpropagated)} of {len(rulings)} docketed rulings appear nowhere in "
      f"the claims register.**")
    A("")
    if unpropagated:
        A(", ".join(unpropagated))
        A("")
        A("A ruling that lives only in the docket has changed the change-log, not "
          "the state. Claims still carry scores earned under the superseded "
          "reading. The scan is word-boundary over `claims.jsonl` plus "
          f"{len(leaves)} `claim-quality.md` leaves.")
        A("")
    if unclassified_filenames:
        A(f"> ⚑ **{len(unclassified_filenames)} `R<N>` token(s) sit in a docket "
          f"FILENAME outside a `ruling-`/`rulings-` segment and are not counted "
          f"above: {', '.join(sorted(unclassified_filenames, key=lambda t: int(t[1:])))}. "
          f"Classify them — rename into the convention, or confirm they are not "
          f"rulings.")
        A("")
    A(VOLATILE_HEADING)
    A("")
    A("*(volatile — excluded from `--check`, since any PR retitle would otherwise "
      "make the check cry wolf)*")
    A("")
    if prs:
        A("| PR | state | title |")
        A("|---|---|---|")
        for p in sorted(prs, key=lambda p: -p["number"]):
            A(f"| #{p['number']} | {state(p['title'])} | {p['title'][:80]} |")
    else:
        A("No open PRs.")
    A("")
    A("---")
    A("")
    A("*Generated from `claims.jsonl`, `open-items/`, `docket-entries/`, "
      "`gh pr list`, and `git`. Every input is required; this file is not written "
      "at all if any input fails. No section here is hand-written — to add "
      "something to this board, make it derivable first. The generator does carry "
      "a few hand-curated constants, enumerated and disclosed in its docstring; "
      "the `~` on the self-disclaim figure is one of them showing through.*")

    out = "\n".join(L) + "\n"
    # Rendered lines, not list elements: a value carrying an embedded newline
    # produces two heading lines from one element, which the element count missed.
    stable_guard_count = sum(1 for ln in out.splitlines() if ln == VOLATILE_HEADING)

    if check_only:
        if not BOARD.is_file():
            die("BOARD.md does not exist -- run the generator")
        # Line-anchored, not substring: open-item TITLES are author-controlled and
        # render above this point, so a title containing the heading text would move
        # the split upward and drop the propagation number out of the guarded region.
        # Normalize SHAs: see the module docstring. A committed board names its
        # own parent commit and can never name itself, so an un-normalized compare
        # is red on every commit of BOARD.md -- which is how this defect recurred
        # three times.
        def split(text: str) -> str:
            stable = re.split(rf"^{re.escape(VOLATILE_HEADING)}$", text, flags=re.M)[0]
            return re.sub(r"\b[0-9a-f]{7,40}\b", "<sha>", stable)
        if stable_guard_count != 1:
            die(f"{VOLATILE_HEADING!r} occurs {stable_guard_count} times as a line in "
                f"the rendered board; the --check split would be ambiguous. An "
                f"open-item title is probably colliding with it.")
        if split(BOARD.read_text(encoding="utf-8")) != split(out):
            print("[board] STALE: BOARD.md's stable sections do not match "
                  "generated content.", file=sys.stderr)
            print("[board] fix: python3 _orchestration/tools/generate_board.py",
                  file=sys.stderr)
            return 1
        print("[board] OK - BOARD.md's stable sections are current")
        return 0

    BOARD.write_text(out, encoding="utf-8")
    print(f"[board] wrote {BOARD.relative_to(REPO)} "
          f"({len(claims)} claims, {len(open_items)} open items, {len(prs)} PRs, "
          f"{len(unpropagated)}/{len(rulings)} rulings unpropagated)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
