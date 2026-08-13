#!/usr/bin/env python3
"""Generate _orchestration/BOARD.md from the repo's own machine-readable state.

WHY THIS EXISTS
---------------
The hand-maintained board went 11 days stale, and the only view of program state
became a Claude report. The fix is structural, not disciplinary: the board is
GENERATED from artifacts that cannot drift, because they ARE the state.

  claims.jsonl  -> what we know and how solid it is
  open-items/   -> what we are waiting on (one file per item, frontmatter)
  gh pr list    -> what is in flight
  git           -> where main is

There is no hand-written section. Anything the board should show has to become one of
those inputs first -- that is the forcing function that keeps it from rotting.

FAIL-LOUD CONTRACT
------------------
Every input is REQUIRED. If an input is missing or errors, this exits non-zero
and writes NOTHING. A board that silently reports "0 open PRs" because `gh`
failed is worse than no board -- that is the degrades-to-a-pass class this repo
has been bitten by repeatedly. There is no partial-board path.

NO DATE PINS, NO SELF-REFERENCE
-------------------------------
Nothing here hardcodes a date, a SHA, or a count. Every number is read at run
time. (The r40 span checker's date-pinned STAMP is the cautionary tale: it
fails open and silently once the date moves.)

USAGE
    python3 _orchestration/tools/generate_board.py            # write BOARD.md
    python3 _orchestration/tools/generate_board.py --check    # fail if hand-edited

`--check` IS NOT A CI GATE, and deliberately so. One of its inputs (the open-PR
list) changes whenever anyone opens, merges, or retitles a PR, so a CI check
would go red for reasons that have nothing to do with the branch under test --
a gate that cries wolf gets disabled, and a disabled gate is a lie. `--check` is
a LOCAL guard: it catches someone editing the generated file by hand. Freshness
is carried by the SHA in the header instead: if it does not match `origin/main`,
the board is stale and you regenerate. Wiring this into CI requires first
splitting the volatile (PR) section from the tracked-file-derived section.
"""
from __future__ import annotations

import json
import subprocess
import sys
from collections import Counter
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
CLAIMS = REPO / "manuscript/ave-kb/.index/claims.jsonl"
BOARD = REPO / "_orchestration/BOARD.md"
OPEN_ITEMS = REPO / "_orchestration/open-items"

# Display order, most-blocking first. An item whose status is not in this list is a
# FATAL error, not a skipped row -- a silently-dropped open item is precisely the
# failure this directory exists to prevent.
STATUS_ORDER = ["ROUTED-TO-GRANT", "OPEN-IN-WALK", "OPEN", "REGISTERED",
                "QUEUED", "PARKED"]
REQUIRED_KEYS = ["id", "title", "status", "owner", "opened", "source"]

# Rulings that must reach the claims register, not just the docket. Each entry
# is (label, token to search for in the register + claim-quality leaves).
# Add a row when a ruling lands; the board then tracks its propagation debt.
PROPAGATION_TOKENS = ["R51", "R52", "R53", "R54"]

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
        p = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
    except Exception as e:  # noqa: BLE001 - any failure is fatal here
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
    """Parse one-file-per-item frontmatter. Deliberately a 20-line parser, not PyYAML:
    the schema is six flat string keys, and a dependency is a thing that can be missing
    on someone else's machine."""
    if not OPEN_ITEMS.is_dir():
        die(f"open-items directory not found at {OPEN_ITEMS}")
    items, seen = [], {}
    for f in sorted(OPEN_ITEMS.glob("*.md")):
        if f.name == "README.md":
            continue
        lines = f.read_text(encoding="utf-8").splitlines()
        if not lines or lines[0].strip() != "---":
            die(f"{f.name}: no frontmatter (first line must be '---')")
        try:
            end = lines.index("---", 1)
        except ValueError:
            die(f"{f.name}: frontmatter is never closed")
        meta = {}
        for raw in lines[1:end]:
            if not raw.strip() or raw.lstrip().startswith("#"):
                continue
            if ":" not in raw:
                die(f"{f.name}: frontmatter line is not 'key: value' -> {raw!r}")
            k, _, v = raw.partition(":")
            meta[k.strip()] = v.strip()
        for k in REQUIRED_KEYS:
            if not meta.get(k):
                die(f"{f.name}: frontmatter is missing required key '{k}'")
        if meta["status"] not in STATUS_ORDER:
            die(f"{f.name}: status {meta['status']!r} is not one of {STATUS_ORDER}. "
                f"Fix the file or add the status -- items are never silently skipped.")
        if meta["id"] in seen:
            die(f"{f.name}: duplicate id {meta['id']!r} (also in {seen[meta['id']]})")
        seen[meta["id"]] = f.name
        meta["_file"] = f.name
        items.append(meta)
    if not items:
        die("open-items/ contains no items. If the program truly has zero open "
            "decisions, say so explicitly by adding a file that says that.")
    return items


def main() -> int:
    check_only = "--check" in sys.argv

    # ---- inputs (all required) -------------------------------------------
    rows = load_claims()
    open_items = load_open_items()
    claims = [r for r in rows if r.get("node_type") == "claim"]
    experiments = [r for r in rows if r.get("node_type") == "experiment"]
    if not claims:
        die("zero claim nodes found -- schema changed or index is broken")

    pr_json = run(
        ["gh", "pr", "list", "--json", "number,title,isDraft", "--limit", "100"],
        "gh pr list (is gh authenticated?)",
    )
    try:
        prs = json.loads(pr_json)
    except json.JSONDecodeError as e:
        die(f"gh returned unparseable JSON: {e}")

    main_sha = run(["git", "-C", str(REPO), "rev-parse", "--short", "origin/main"],
                   "git rev-parse origin/main").strip()
    main_when = run(["git", "-C", str(REPO), "log", "-1", "--format=%ad",
                     "--date=short", "origin/main"], "git log origin/main").strip()

    # ---- the headline: is anything experimentally supported? --------------
    exp_solid = [c for c in claims if c.get("experimental_solidity") is not None]
    exp_run = [e for e in experiments if (e.get("status") or "").lower() == "run"]

    # ---- solidity distribution -------------------------------------------
    bands = Counter(c.get("build_band") or "unknown" for c in claims)
    top = sorted(
        (c for c in claims if isinstance(c.get("solidity"), (int, float))
         and c["solidity"] >= 0.80),
        key=lambda c: -c["solidity"],
    )
    disclaimed = sum(
        1 for c in top
        if any(t in (c.get("rationale") or "").lower() for t in SELF_DISCLAIM)
    )

    # ---- propagation debt: rulings that never reached the register --------
    register_text = CLAIMS.read_text(encoding="utf-8")
    for leaf in REPO.glob("manuscript/ave-kb/**/claim-quality.md"):
        register_text += leaf.read_text(encoding="utf-8", errors="replace")
    unpropagated = [t for t in PROPAGATION_TOKENS if t not in register_text]

    # ---- review state, parsed from the title convention -------------------
    def state(t: str) -> str:
        if "[REVIEW: CLEARED]" in t:
            return "CLEARED"
        if "records-class" in t:
            return "records-class"
        if "pending-orchestrator" in t:
            return "pending-review"
        return "unlabelled"

    # ---- render -----------------------------------------------------------
    L: list[str] = []
    A = L.append
    A("<!-- GENERATED FILE - DO NOT EDIT BY HAND.")
    A("     Regenerate: python3 _orchestration/tools/generate_board.py")
    A("     Hand edits are overwritten. Verify with --check before committing. -->")
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
    for band in ["ok-to-build", "ok-with-caveats", "input-only", "do-not-build",
                 "refuted", "unknown"]:
        if bands.get(band):
            A(f"| {band} | {bands[band]} |")
    A("")
    A(f"**Top tier (solidity ≥ 0.80): {len(top)} claims — of which ~{disclaimed} "
      f"self-disclaim** as definitional, catalog, notation, or consistency-class "
      f"in their own rationale. Read the top of the ranking with that in mind.")
    A("")
    A("## What we are waiting on")
    A("")
    grant_owed = [i for i in open_items
                  if i["status"] in ("ROUTED-TO-GRANT", "OPEN-IN-WALK")]
    A(f"**{len(grant_owed)} of {len(open_items)} open items need Grant's word.** "
      f"Nothing fires on those without it.")
    A("")
    A("| item | status | owner | open since |")
    A("|---|---|---|---|")
    for i in sorted(open_items, key=lambda i: (STATUS_ORDER.index(i["status"]),
                                               i["opened"])):
        A(f"| [{i['title']}](open-items/{i['_file']}) | {i['status']} | "
          f"{i['owner']} | {i['opened']} |")
    A("")
    A("## In flight")
    A("")
    if prs:
        A("| PR | state | title |")
        A("|---|---|---|")
        for p in sorted(prs, key=lambda p: -p["number"]):
            A(f"| #{p['number']} | {state(p['title'])} | {p['title'][:80]} |")
    else:
        A("No open PRs.")
    A("")
    A("## Propagation debt")
    A("")
    if unpropagated:
        A(f"**{len(unpropagated)} ruling(s) have not reached the claims register: "
          f"{', '.join(unpropagated)}.**")
        A("")
        A("A ruling that lives only in the docket has changed the change-log, not the "
          "state. Claims still carry scores earned under the superseded reading.")
    else:
        A("All tracked rulings are referenced in the claims register.")
    A("")
    A("---")
    A("")
    A("*Generated from `claims.jsonl`, `open-items/`, `gh pr list`, and `git`. "
      "Every input is required; this file is not written at all if any input fails. "
      "There is no hand-written section \u2014 to add something to this board, make it "
      "derivable first.*")

    out = "\n".join(L) + "\n"

    if check_only:
        if not BOARD.is_file():
            die("BOARD.md does not exist -- run the generator")
        if BOARD.read_text(encoding="utf-8") != out:
            print("[board] STALE: BOARD.md does not match generated content.",
                  file=sys.stderr)
            print("[board] fix: python3 _orchestration/tools/generate_board.py",
                  file=sys.stderr)
            return 1
        print("[board] OK - BOARD.md is current")
        return 0

    BOARD.write_text(out, encoding="utf-8")
    print(f"[board] wrote {BOARD.relative_to(REPO)} "
          f"({len(claims)} claims, {len(prs)} PRs, "
          f"{len(unpropagated)} unpropagated ruling(s))")
    return 0


if __name__ == "__main__":
    sys.exit(main())
