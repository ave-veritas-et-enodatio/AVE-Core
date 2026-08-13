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

There is no hand-written section and no hand-maintained list ANYWHERE in this
file. Anything the board should show has to become one of those inputs first --
that is the forcing function that keeps it from rotting.

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

`--check` compares only the STABLE sections. The open-PR list changes whenever
anyone opens, merges, or retitles a PR -- including this board's own PR, which
made v1's `--check` red on arrival. Comparing the volatile section would make
the check cry wolf, and a check that cries wolf gets disabled. It is a LOCAL
guard against hand edits, not a CI gate. Freshness rides on the SHA in the
header: if it does not match `origin/main`, regenerate.
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

PR_LIMIT = 200
VOLATILE_HEADING = "## In flight"   # excluded from --check; see module docstring

# Rationale language a claim uses when it disclaims physical content. Used only
# to COUNT how much of the top tier is bookkeeping -- never to reclassify.
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
              if p.is_file() and p.suffix.lower() != ".md"]
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
        if meta["anchor"] not in src.read_text(encoding="utf-8", errors="replace"):
            die(f"{rel}: anchor text not found in {meta['source']}.\n"
                f"         anchor: {meta['anchor']!r}\n"
                f"         The source moved or was rewritten. Repoint the anchor; "
                f"do NOT convert it back to a line number.")

        seen[meta["id"]] = str(rel)
        meta["_file"] = str(rel)
        items.append(meta)

    if not items:
        die("open-items/ contains no items. If the program truly has zero open "
            "decisions, say so explicitly by adding a file that says that.")
    return items


def docketed_rulings() -> tuple[set[str], set[str]]:
    """Return (recorded, unclassified).

    `recorded` is derived from docket FILENAMES under the repo's own convention --
    `...-ruling-r52-...` and `...-rulings-r45-r47.md`, the latter expanded as an
    inclusive range. That set is precise and convention-backed.

    `unclassified` is every other R-number appearing in a docket BODY. Those may be
    rulings recorded in a batch file that names no numbers (e.g.
    `2026-08-06-rulings-final-batch.md`) or merely cross-references to rulings
    recorded elsewhere -- from the text alone the two are not separable.

    THE SELECTION RULE IS AN OPEN QUESTION, not a solved one. This function reports
    both sets and the board says so, rather than printing one confident number over
    an ambiguity. See open-items/ `ruling-selection-rule`."""
    if not DOCKET.is_dir():
        die(f"docket-entries directory not found at {DOCKET}")
    files = [f for f in sorted(DOCKET.glob("*.md")) if f.name != "README.md"]
    if not files:
        die("docket-entries/ is empty -- an empty scan is not a clean scan")

    recorded: set[str] = set()
    for f in files:
        stem = f.name.lower()
        for a, b in re.findall(r"\br(\d{1,3})-r(\d{1,3})\b", stem):
            lo, hi = sorted((int(a), int(b)))
            recorded |= {f"R{n}" for n in range(lo, hi + 1)}
        recorded |= {f"R{int(n)}" for n in re.findall(r"\br(\d{1,3})\b", stem)}

    in_bodies: set[str] = set()
    for f in files:
        in_bodies |= {f"R{int(n)}" for n in
                      re.findall(r"\bR(\d{1,3})\b", f.read_text(errors="replace"))}

    if not recorded:
        die("no ruling identifiers found in docket-entries/ filenames -- the "
            "naming convention changed and the propagation scan is now blind")
    return recorded, in_bodies - recorded


def main() -> int:
    check_only = "--check" in sys.argv

    # ---- inputs (all required) -------------------------------------------
    rows = load_claims()
    open_items = load_open_items()
    rulings, unclassified = docketed_rulings()

    claims = [r for r in rows if r.get("node_type") == "claim"]
    experiments = [r for r in rows if r.get("node_type") == "experiment"]
    if not claims:
        die("zero claim nodes found -- schema changed or index is broken")
    if not experiments:
        die("zero experiment nodes found -- schema changed or index is broken. "
            "Reporting '0 of 0 experiments run' would read as reassuring news "
            "about a broken index.")

    run(["git", "-C", str(REPO), "fetch", "--quiet", "origin", "main"],
        "git fetch origin main (the header SHA is the freshness signal; "
        "reading a stale ref would make it circular)")

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

    main_sha = run(["git", "-C", str(REPO), "rev-parse", "--short", "origin/main"],
                   "git rev-parse origin/main").strip()
    main_when = run(["git", "-C", str(REPO), "log", "-1", "--format=%ad",
                     "--date=short", "origin/main"], "git log origin/main").strip()

    # ---- the headline: is anything experimentally supported? --------------
    exp_solid = [c for c in claims if c.get("experimental_solidity") is not None]
    exp_run = [e for e in experiments if (e.get("status") or "").lower() == "run"]

    # ---- solidity distribution (band names derived, never hardcoded) -------
    bands = Counter(c.get("build_band") or "unknown" for c in claims)
    if sum(bands.values()) != len(claims):
        die("build-band tally does not equal the claim count -- refusing to print "
            "a table that silently drops rows")
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
    A(f"`origin/main` **{main_sha}** ({main_when}) · "
      f"{len(rows)} index records · {len(claims)} claims · {len(prs)} PRs open")
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
    if unclassified:
        A(f"> ⚑ **The ruling set is a derived approximation, and the selection rule "
          f"is an OPEN QUESTION.** The {len(rulings)} above come from docket "
          f"*filenames* (with `rN-rM` ranges expanded) — precise and "
          f"convention-backed. A further **{len(unclassified)}** R-numbers appear "
          f"only in docket *bodies* "
          f"({', '.join(sorted(unclassified, key=lambda t: int(t[1:])))}). From the "
          f"text alone there is no way to tell a ruling recorded in an unnumbered "
          f"batch file from a cross-reference to a ruling recorded elsewhere, so "
          f"they are counted separately rather than folded in either direction. "
          f"See `open-items/` → *ruling-selection-rule*.")
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
      "at all if any input fails. There is no hand-written section and no "
      "hand-maintained list — to add something to this board, make it derivable "
      "first.*")

    out = "\n".join(L) + "\n"

    if check_only:
        if not BOARD.is_file():
            die("BOARD.md does not exist -- run the generator")
        stable = lambda s: s.split(VOLATILE_HEADING)[0]  # noqa: E731
        if stable(BOARD.read_text(encoding="utf-8")) != stable(out):
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
