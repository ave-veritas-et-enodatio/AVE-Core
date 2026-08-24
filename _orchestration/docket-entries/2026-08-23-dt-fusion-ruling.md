### ENTRY 2026-08-23-dt-fusion-ruling (2026-08-23): Grant — dt-fusion partitioned-symbol adjudication: option (c) retire; salvaged concept minted as an epic

**The question** (open-item `dt-fusion-partitioned-symbol`, opened 2026-08-23 by the PR #992
lane, closed by this ruling's executing commit): `simulate_dt_fusion.py:5` imports
`generate_fusion_netlist`, which the IP-partition stub `spice_exporter.py` never defined in
this repo — restore a public-safe implementation (a), stub it (b), or retire the driver (c)?

**Evidence walked before the ruling** (orchestrator, 2026-08-23, verified receipts):

- The symbol never existed in this repo: `git log 1ffdef0e -S 'def generate_fusion_netlist'`
  returns 0 hits (receipt pinned to the pre-ruling base — the `--all` form stops reproducing
  once this record, which quotes the string, lands; blind-audit finding 1.1); the repo was
  born partitioned (`de9d2293`), the stub arrived next day
  (`2670d50e`) preserving only `generate_spice_netlist` (as a no-op).
- The full implementation — 84 lines of the 196-line archive file — survives in the
  pre-partition historical archive
  (`Applied-Vacuum-Engineering/src/scripts/vol_6_periodic_table/simulations/spice_exporter.py:113`),
  not in any private sibling repo (0 hits in the private mirrors).
- The driver's complete output is ALREADY tracked in this repo
  (`spice_netlists/dt_fusion_transient.cir`, in-tree since initial release) — the function is
  a template-printer whose printed result is public, so no option changes disclosure.
- Zero consumers: hand-authored figure, independent animation, static banked netlist.
- Content walk of the archive implementation: three load-bearing choices are underived
  (1 µH/1 pF "standard values" tank; `K = SPICE_K_SCALAR/d = 0.5/d` clamped 0.999; fixed
  1.5d collision offset with a 1 GHz sine mislabeled "AC ramp"), and the emitted topology is
  an all-to-all star-to-ground array — not the K4/srs substrate graph.

**RULING (Grant, 2026-08-23, verbatim):** "C, and add a full orchestration epic on the
planning, validation, and execution of the idea given to us by this effort"

**Execution (this commit + branch):**

1. `simulate_dt_fusion.py` → `src/scripts/_archive/vol_6_periodic_table/` with a MANIFEST
   row (partition-orphaned class). Its two strict-xfail entries leave the import-smoke
   dict (the stale-entry liveness guard forces this once `_archive` excludes the file).
2. Open-item file deleted; this entry is the record.
3. **The salvaged concept becomes an epic**: an external-circuit-solver (SPICE-class)
   cross-check of the engine's linear-regime dynamics on the SUBSTRATE'S OWN graph with
   canonical constants — the one idea the orphaned effort surfaces that survives the
   content walk. Epic doc: `_orchestration/2026-08-23_external-solver-crosscheck-epic.md`
   (same branch). The epic is planning-first: no implementation is authorized by this
   ruling; each phase gates on its own GO.

**Not touched:** `spice_exporter.py` stub (still the no-op interface for
`simulate_element.py`), the tracked netlists, the figure, the animation.
