# srs-z3 Migration Policy Charter (D1 RATIFICATION)

**Date:** 2026-07-03
**Charter authority:** Grant 2026-07-03 D1 RATIFICATION ("yup makes sense, ratify")
**Status:** POLICY CHARTERED — **execution is future-arc work; this document EXECUTES NOTHING.**
**Ruling record:** `research/2026-06-12_lattice-d1-adjudication-memo.md` (2026-07-03 addendum);
in-axiom `manuscript/common_equations/eq_axiom_1.tex:18`; def-entry `def-4b1a2c`
(`manuscript/ave-kb/common/vocabulary-register.md`).

> **THE RULING (record faithfully):** **srs-z3** — the true Sunada-K4 / Laves / srs
> net (degree-3, chiral, $I4_1 32$ — the object Axiom 1 names) — is **RATIFIED as the
> engine's production carrier**. The historical achiral **diamond z=4**
> (`TETRA_OFFSETS`) engine is re-tagged a **non-canonical instrument**
> (statics-pathological; verdicts carrier-tagged). This is an **ENGINEERING-FIDELITY**
> ruling: the engine implements the lattice the axiom already names — **NO new
> ontological claim beyond Axiom 1.** `mass = A1` (PR#260 / #311 ECHO-final) untouched.

## (a) POLICY

Three standing rules, effective on ratification. **These are policy, not a work
order — no code is changed by this document.**

1. **NEW engine work builds on srs-z3 by default.** Any new solver, driver,
   eigensolve, or operator that needs a substrate lattice uses the chiral srs z=3
   carrier (`build_srs_net` / `assemble_L_srs` / `SrsCageWinding` /
   `ave.topological.srs_dec`). A new module that builds on the diamond
   `TETRA_OFFSETS` stencil requires an explicit written justification (why the
   instrument, not the carrier) in its header and its result doc.

2. **Every existing `TETRA_OFFSETS` module gets, at next touch, ONE of:**
   - **MIGRATE** — re-home its operator onto srs (the substantive fix); OR
   - **an explicit scope tag** — a header line:
     `# non-canonical instrument: achiral diamond, statics-pathological — verdicts carrier-tagged`
     (the honest hold, when migration is not this-touch's scope).

   "At next touch" means: the module is not migrated on a schedule; it is migrated
   (or scope-tagged) the next time an arc opens it for any reason. No sweeping
   rewrite is chartered here.

3. **Every future engine verdict declares its carrier.** Result docs and pre-regs
   for any engine-based verdict state, in the verdict box, which carrier rendered
   it (srs-z3 or diamond-z4) and — if diamond — carry the CLASS-1 exposure caveat
   by reference (`research/2026-07-03_engine-verdict-exposure-sweep_result.md`).

**Scope guard.** This is engineering-fidelity, not re-derivation. Migrating a
module does NOT re-open its physics verdict unless the verdict was CLASS-1-exposed
(diamond statics pathology). LOW-graded verdicts (25 of 31 in the exposure sweep)
that ran on cubic / analytic / correct-achiral-null hosts are NOT migration
targets — they were never diamond-statics-exposed. The `mass = A1` identity is
untouched by any migration.

## (b) Module inventory by stencil

**Source:** the merged exposure-sweep triage
(`research/2026-07-03_engine-verdict-exposure-sweep_result.md` §3, the 31-row
table + §4 family notes) for the verdict-level stencil grading; **cross-checked**
against one grep of the actual `TETRA_OFFSETS` producers/consumers under
`src/ave/` (`grep -rln TETRA_OFFSETS src/ave/`, this arc's HEAD). The two agree:
every diamond-stencil verdict in the sweep routes through one of the library
modules below.

### B.1 — `src/ave/` library modules on the diamond `TETRA_OFFSETS` stencil

`TETRA_OFFSETS` is DEFINED at `src/ave/topological/cosserat_field_3d.py:134-139`
(the four odd-coordinate-sum diagonals — the source of the bipartite-checkerboard
nullspace). Ten library modules import or define it:

| Module | Role | Diamond-statics exposed? |
|:--|:--|:--|
| `topological/cosserat_field_3d.py` | **defines** `TETRA_OFFSETS` (`:134`) + the Grad/Div/helicity primitives | root of the stencil; the migration touches this first |
| `solvers/native_cage_imex.py` | Stage-2 native-cage IMEX `L_D = Div·diag(D)·Grad` (`:89,:99,:123`) | **YES — the load-bearing CLASS-1 operator** (HIGH #1) |
| `solvers/coupled_cage_winding.py` | Stage-3 A1↔ω PDE, EXTENDS Stage-2 `L_D` (`:29,:105`) | **YES** (inherits #1; HIGH #2) |
| `solvers/graded_vacuum_network.py` | graded-Z network on the 4 diamond diagonals (`:102,:130,:375`) | **YES** (statics `Div·Grad`) — but also builds srs via `build_srs_net` (`:87`) |
| `solvers/node_scattering_multiplicity.py` | Fork-A REFUTE-R3; uses the CONNECT-map, NOT the dense cube (`:25,:128`) | LOW (self-caught its R3 overclaim, Rule 12) |
| `core/scalar_grade_seed.py` | seeds A1 grade using `TETRA_OFFSETS` helicity (`:30,:36`) | seed helper; migrates with the operators it feeds |
| `topological/k4_cosserat_coupling.py` | `CoupledK4Cosserat` — K4⊗Cosserat time-domain (band-structure #20 host) | dynamical eigensolve (rank-2 tensor, no statics-nullspace bite per sweep §Family-3) — **name walk-back target (d), not a statics migrate** |
| `gravity/gw_propagation.py` | GW permutation-difference operators on the 4 diagonals (`:527,:535`) | LOW (#27 back-reaction leg live) — carrier-tag at next touch |
| `facade/unified_engine.py` | the diamond-K4 N³ node facade (`:91,:269`) | facade over the above; migrates when its backends do |
| `solvers/srs_cage_winding.py` | **the srs REPLACEMENT** — already on `build_srs_net` (3 struts/node), imports `TETRA_OFFSETS` only to CONTRAST it (`:16,:22,:49`) | **already srs — the migration TARGET pattern, not a source** |

### B.2 — the already-srs carrier modules (the migration destination)

These already run on srs z=3 — new work extends these, and diamond modules migrate
TOWARD them:

- `core/chiral_lattice.py` — `build_srs_net` (the z=3 chiral Laves / (10,3)-a /
  Sunada-K4 builder, `:11-13,199-217`) AND `build_diamond_net` (the achiral z=4
  builder — a walk-back name target, §(d)).
- `solvers/srs_cage_winding.py` — `SrsCageWinding` / `assemble_L_srs` (`Bᵀ·diag·B`,
  well-posed, nullspace dim 1).
- `topological/srs_dec.py` — the DEC 2-complex + exact `∂₁,∂₂` cochain calculus
  (`research/2026-07-03_srs-dec-operators_result.md`).

### B.3 — verdicts on NON-diamond hosts (NOT migration targets)

Per the sweep, 25 LOW rows ran on **cubic CrystalGraft / Cartesian 7-pt / analytic
/ parametric / correct-achiral-null / genuine-srs** hosts — never diamond-statics
exposed. Notably the **Q~30.8 cold-cage "clean negative"** (`Q=1/α` identity) is
CrystalEngine Cartesian 7-point (`crystal_engine.py:154`), NOT diamond — **not a
migration target**. These stay as-is; carrier declaration (policy 3) still applies
to their future re-runs.

## (c) MIGRATION PRIORITY ladder (by live-claim exposure)

Priority = which modules carry claims that **still matter** (a live verdict that
is CLASS-1-exposed by the diamond statics pathology). Read directly off the
exposure sweep's triage grades (`…_engine-verdict-exposure-sweep_result.md` §3,
§5): HIGH verdicts ride an exposed operator and are already status-demoted →
top priority; MEDIUM next; LOW last (mostly carrier-tag, not migrate). **One of
the three HIGH/MEDIUM-adjacent re-runs has ALREADY landed** (the localization
re-adjudication) and is folded in below.

| Rung | Module(s) | Live claim carried | Exposure | Migration action |
|:--:|:--|:--|:--|:--|
| **1** | `solvers/native_cage_imex.py` (+ `cosserat_field_3d.py` primitives) | Stage-2 bulk-self-trap **DISPERSE** (make-or-break localization) — HIGH #1 | CLASS-1 (98% N=8 / 67% N=24 nullspace) + CLASS-2 (Cartesian control) | **RE-RUN LANDED on srs** (`research/2026-07-03_localization-readjudication_result.md`: `[DISPERSES-ON-SRS-LIVE]`, verdict CONFIRMED on the clean carrier). Operator migration = fold `assemble_L_srs` in as the default; retire `L_D` to instrument. |
| **2** | `solvers/coupled_cage_winding.py` | Stage-3 cavity-pinning **DISPERSE-FALSIFIED** — HIGH #2 | CLASS-1 (same `L_D` on A1 block) + §5 self-admitted unwind artifact | **NOT yet re-run** (the readjudication arc gated the S3 cavity-pinning extension as downstream — a dispersing bulk core + external cavity). Top OPEN migration. |
| **3** | `solvers/native_cage_imex.py` / coupled eigensolve path | **#415** coupled A1+winding eigensolve DOES-NOT-EXIST (gate-d FAIL) — MED #8 | CLASS-1 `L_D` nullspace confirmed; A1 gates de-risked (opposite spectral end) | re-run the coupled eigensolve on srs (the nullspace maps to the far spectral end, so the A1 gates were not directly contaminated — MEDIUM, not HIGH). |
| **4** | diamond `TETRA_OFFSETS` phase-space path (`k4_cosserat_coupling.py` / #417 driver) | **#417** phase-space (2,3)-winding **BREAK** — MED #21 | CLASS-1 chiral-on-achiral category zone; carrier-detuning carries the negative independent of stencil | re-run the (2,3) BREAK on the chirality-CARRYING srs (diamond structurally cannot host the winding — the exact axis-5 finding). |
| **5** | `k4_bloch_dispersion.py` (script) / `cosserat_band_structure_two_sublattice.py` | K4 Bloch (q·ℓ)⁴ QUARTIC chord — MED #18 | CLASS-2 (hardcoded slope form), NOT CLASS-1 (rank-2 dynamical eigensolve) | **corpus already self-corrected** (`clm-k4d4ph` demoted; `srs_bloch_dispersion.py` is the srs positive control). Name walk-back (d) only; NO statics migrate. |
| **6** | `gravity/gw_propagation.py`, `node_scattering_multiplicity.py`, `unified_engine.py` facade | LOW verdicts (live but not statics-exposed) | LOW | carrier-tag at next touch; migrate opportunistically. |

**TOP-3 (by live-claim exposure), for the orchestrator:**
1. **`native_cage_imex.py`** — the load-bearing bulk-self-trap operator (re-run
   LANDED on srs; fold `assemble_L_srs` in as the default operator).
2. **`coupled_cage_winding.py`** — Stage-3 cavity-pinning, the top OPEN re-run
   (S3 extension on srs, gated downstream of the now-landed bulk-core result).
3. **`k4_cosserat_coupling.py` / #417 phase-space path** — the (2,3)-winding BREAK,
   where the diamond's structural inability to carry chirality is the exact
   ratification axis (axis 5 of the five-axis comparison).

## (d) Name walk-back plan ("K4" meaning diamond)

The P0 name walk-back (queued since the 2026-06-12 memo §5) is now **EXECUTABLE**
— chartered here, **executed by future arcs**. The target set: every file/symbol
that says "K4" while MEANING the achiral **diamond z=4** engine (referent (b) of
def-4b1a2c). **The A4-rotation-group "K4" (referent (c)) is NOT a target** — it is a
legitimate finite-group label. **The srs-net "K4" (referent (a)) is NOT a target**
— it IS the ratified carrier. Only the diamond-means-K4 usages are walked back.

**Enumerated targets (file:line, this arc's HEAD — verify-before-cite before any
future rename):**

| # | Symbol / string | Site | Current meaning | Proposed rename/retag |
|:--:|:--|:--|:--|:--|
| d1 | class `K4Lattice3D` | `src/ave/core/k4_tlm.py:101` | the achiral bipartite-FCC **diamond** lattice | `DiamondLattice3D` (alias `K4Lattice3D = DiamondLattice3D` retained one release for callers) |
| d2 | class `K4Lattice2D(K4Lattice3D)` | `src/ave/core/k4_tlm.py:556` | 2D diamond slice | `DiamondLattice2D` |
| d3 | banner `# K4 (DIAMOND) LATTICE 3D` + docstring "bipartite Diamond lattice" | `src/ave/core/k4_tlm.py:10,97` | diamond | banner → `# DIAMOND (achiral z=4) LATTICE — non-canonical instrument`; docstring keep "diamond", drop the "K4" conflation |
| d4 | module filename `k4_tlm.py` | `src/ave/core/k4_tlm.py` | "K4-TLM" = diamond TLM | rename → `diamond_tlm.py` (or `tlm_diamond.py`); shim import for one release |
| d5 | class `CoupledK4Cosserat` + "K4 scatter+connect pipeline" | `src/ave/topological/k4_cosserat_coupling.py:185` + docstring | "K4" = the diamond scatter/connect pipeline | `CoupledDiamondCosserat`; module → `diamond_cosserat_coupling.py` |
| d6 | `K4_BONDS` / `D_BONDS` | `src/scripts/vol_4_engineering/k4_bloch_dispersion.py:62,72` | the 4 diamond tetrahedral bond vectors | `DIAMOND_BONDS`; script name carries "k4" → `diamond_bloch_dispersion.py` |
| d7 | `k4_lattice_holonomy.py` — "the diamond/'K4' net" | `src/ave/topological/k4_lattice_holonomy.py:14` | **MIXED**: the A4 rotation group (referent (c), KEEP) reading OFF the diamond connect-map (referent (b)) | keep the `A4`/holonomy naming (referent (c) is correct); retag the connect-map source string "diamond/'K4' net" → "diamond net" (drop the "K4" alias); **flag for the migration arc**: the holonomy is read off the DIAMOND connect-map — a future arc must decide whether the srs connect-map changes the A4→2T port-permutation holonomy (a physics question, NOT a rename). |
| d8 | `build_diamond_net` (already correctly named) | `src/ave/core/chiral_lattice.py` | the achiral z=4 builder | **already honest** — no rename; scope-tag its callers as instrument. |

**Rename discipline (for the future execution arc, NOT done here):**
- Each rename ships with a one-release alias/shim so no caller breaks in a single
  commit (`K4Lattice3D = DiamondLattice3D`, etc.).
- Test files (`test_chiral_lattice*.py`, `test_k4_lattice_holonomy.py`,
  `test_node_scattering_multiplicity.py`, …) update symbol references in lockstep.
- The `K4 → A4` group chain (`finkelstein-misner-spin-half-derivation.md:52,56`,
  `electron-identification.md:52`) is **untouched** — that "K4" is the group, correct.
- **EXECUTE NOTHING in this arc.** This table is the walk-back SPEC; a future
  `analysis/srs-name-walkback` arc executes it with its own verification chain.

## (e) Cost note per phase

Rough effort scoping for the FUTURE execution arcs (not a commitment; sizing only):

| Phase | Scope | Cost | Risk / gate |
|:--|:--|:--|:--|
| **P0 — carrier-tag sweep** | add the `# non-canonical instrument …` header line to every B.1 diamond module NOT being migrated this pass; add carrier declaration to result-doc/prereg templates | **LOW** (~1 arc; mechanical, no physics) | none — pure documentation; `make verify` only |
| **P1 — operator migration (rung 1-2)** | fold `assemble_L_srs` in as the default operator for `native_cage_imex` + `coupled_cage_winding`; run the S3 cavity-pinning extension on srs | **MED-HIGH** (2-3 arcs) | **α / Lorentz-chain survival is a P1 ACCEPTANCE GATE** — the diamond hosted the α / Lorentz derivations; migrating the carrier must re-clear those chains on srs or the migration STOPS and the diamond stays as a documented α-instrument. This is the make-or-break of the whole migration. |
| **P2 — eigensolve + phase-space re-run (rung 3-4)** | #415 coupled eigensolve + #417 (2,3) BREAK on srs (the chirality-carrying carrier) | **MED** (1-2 arcs) | physics re-adjudication — verdicts may FLIP (srs carries the winding the diamond could not); honest closure per Rule 11 whichever way they land |
| **P3 — name walk-back (§d)** | execute the d1-d8 rename/retag spec with shims + lockstep test updates | **MED** (1 arc, mostly mechanical + one holonomy physics-question in d7) | d7 holonomy is a PHYSICS question (does the srs connect-map change the A4→2T holonomy?), not a rename — must be resolved before the d7 retag |
| **P4 — facade + LOW carrier-tags (rung 5-6)** | `unified_engine` facade, `gw_propagation`, `node_scattering_multiplicity` carrier-tags / opportunistic migrate | **LOW** (opportunistic, at-next-touch) | none load-bearing; the LOW verdicts were never diamond-statics exposed |

**The load-bearing cost is P1's α/Lorentz-chain re-clearance.** Everything else is
mechanical documentation or already-landed (the rung-1 localization re-run). If the
α/Lorentz chains do NOT survive on srs, the ratification still stands (srs IS the
axiom carrier), but the diamond is retained as a *documented calibration instrument*
for those specific chains — surfaced to Grant at that gate, not pre-decided here.

---

**Charter close.** This document CHARTERS the policy and ENUMERATES the inventory,
ladder, walk-back spec, and cost. It **executes nothing**. Future arcs
(`analysis/srs-*-migration`, `analysis/srs-name-walkback`) execute per-phase with
their own pre-regs and verification chains. Cross-refs: D1-memo addendum
(`research/2026-06-12_lattice-d1-adjudication-memo.md`), exposure sweep
(`research/2026-07-03_engine-verdict-exposure-sweep_result.md`), localization
re-adjudication (`research/2026-07-03_localization-readjudication_result.md`), srs
DEC operators (`research/2026-07-03_srs-dec-operators_result.md`), the K4 def-entry
(`def-4b1a2c`), and `_orchestration/index.md` (D1 adjudicated row).
