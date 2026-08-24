### ENTRY 2026-08-24-figure-provenance-ruling (2026-08-24): Grant — figure-bit-reproducibility closed, closure (c)

**RULING (Grant, verbatim):** *"go on 9, 10, 11"* — item 10 = the figure-bit-reproducibility
open item. Executed as the item's closure **(c)** (both halves), the option consistent with
the prior DUP-3 ratification ("as long as we can regenerate or lookup", 2026-08-21, which
already made LOOKUP the identity-bearing path):

1. **Policy recorded:** numeric artifacts are the identity-bearing outputs; matplotlib
   renders are DERIVED VIEWS — deterministic but not bit-reproducible across matplotlib
   versions; a tracked render's `Software` stamp is authoritative for its era; byte-identity
   checks between regenerated and tracked renders are a-priori unachievable across versions
   and the honest comparison is numeric-artifact identity + version-stamped renders.
2. **Pin landed:** `matplotlib==3.10.9` in pyproject.toml with the rationale comment;
   version bumps are deliberate re-baselining events, never incidental.

The open-item file is deleted by this commit; this entry is the record. Origin: the #991
repair lane's live-fire finding (2026-08-20; simulate_optical_caustic.py deterministic but
≠ tracked twin, 3.10.8 stamp vs 3.10.9 venv).
