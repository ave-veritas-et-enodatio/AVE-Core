---
id: vol6-figure-provenance-hole
title: 13 vol_6 animation drivers are import-broken; 6 are sole provenance for cited figures and 8 cited figures have NO generator
status: ROUTED-TO-GRANT
owner: grant
opened: 2026-08-20
source: _orchestration/2026-08-17_repo-cleanup-epic.md
anchor: "generator-named-as-figure"
---

Found by the Wave-3 lane-1 verification pass (PR #991), minted per Grant's "add to the
board" (2026-08-20). This is a provenance hole in the PRINTED vol_6 record, not litter.

**The facts, lane-verified:**
- All 13 `src/scripts/vol_6_periodic_table/animations/animate_*.py` are **import-broken**:
  they `from periodic_table.simulations.simulate_element import …` and
  `importlib.util.find_spec('periodic_table')` returns None. They also write `.gif` output
  to a nonexistent relative directory.
- **6 of the 13 are the only in-tree provenance** for a `*_dynamic_flux.png` the manuscript
  cites (the chapters cite the same-stem `.png`).
- **A further 8 cited `*_dynamic_flux.png` have NO candidate generator at all** — the
  printed volume displays figures the tree cannot regenerate.
- The import-smoke test cannot catch this: `src/tests/test_scripts_import_smoke.py` scopes
  to `from ave.core.<mod> import NAME` shapes only.

**Why it is Grant-gated:** the fix forks on intent — (a) repair the imports (the
`periodic_table` package presumably predates the IP-partition; the private-repo stub at
`vol_6_periodic_table/simulations/spice_exporter.py` suggests the import target moved
there), (b) re-point the drivers at the in-tree `simulate_element`-class machinery if it
exists, or (c) accept the figures as non-regenerable originals and record THAT (which
changes their disposition class in every future census). (a)/(b) need someone who knows
where the vol_6 simulation stack actually lives post-partition; (c) is a provenance
declaration on published figures. None is a hygiene call.

**Discharge:** Grant picks the fork; one lane executes; the import-smoke test gains a
shape that would have caught this class.
