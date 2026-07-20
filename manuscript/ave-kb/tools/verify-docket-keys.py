#!/usr/bin/env python3
"""Warn-class docket entry-key lint (convention 2026-07-20: content-keyed IDs).

Parses `### ENTRY <key>` headers in the rulings docket. Flags duplicate keys.
Numeric-series duplicates predating 2026-07-20 are grandfathered (the frozen
series carries in-place collision notes). Always exits 0 (warn-class; gating
is a later promotion, per the anchor-checker precedent).
"""
import re, sys, collections, pathlib

DOCKET = pathlib.Path(__file__).resolve().parents[3] / "_orchestration" / "2026-07-10_rulings-docket.md"
GRANDFATHERED = {"22", "31", "32"}  # frozen-series artifacts (22 discovered by this lint first run)

def main() -> int:
    text = DOCKET.read_text(encoding="utf-8")
    keys = re.findall(r"^### ENTRY ([0-9A-Za-z][0-9A-Za-z._-]*)", text, re.M)
    counts = collections.Counter(keys)
    dups = {k: c for k, c in counts.items() if c > 1 and k not in GRANDFATHERED}
    print(f"[verify-docket-keys] entries: {len(keys)} | unique keys: {len(counts)} | "
          f"grandfathered numeric dups: {sorted(k for k in counts if counts[k] > 1 and k in GRANDFATHERED)}")
    if dups:
        print(f"[verify-docket-keys] WARN — duplicate entry keys (new-convention violations): {dups}")
    else:
        print("[verify-docket-keys] no new duplicate keys")
    return 0

if __name__ == "__main__":
    sys.exit(main())
