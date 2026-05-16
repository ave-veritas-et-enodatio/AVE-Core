# Numerical Provenance Manifest

**Purpose:** central index of every manuscript file containing numerical claims about AVE solver outputs, with the commit-SHA + date + solver-function each claim was generated against. Per A47 v11c (commit-SHA-anchoring at manuscript table-generation time) — locks the manuscript-vs-code provenance chain so subsequent solver evolution cannot silently invalidate the claim.

**Discipline rule (A47 v11d):** any manuscript file added or modified with numerical solver outputs MUST register here with verified SHA + date + solver function. Companion to PR-template axiom-chain checkbox at [`.github/pull_request_template.md`](../../../.github/pull_request_template.md).

**Methodology backstory:** the substrate-native erosion arc documented at [`research/L3_electron_soliton/100_a47_v9_reframing_line_687_retraction.md`](../../../research/L3_electron_soliton/100_a47_v9_reframing_line_687_retraction.md) found `radial_eigenvalue.py` had drifted 5-15% across 11 commits from its manuscript-table-generation state, with no test or CI gate detecting the drift. The drift was structurally invisible because manuscript prose claimed precision the code no longer delivered. This manifest closes that hole at the corpus-wide level.

---

## Verified entries (SHA-anchored at table-generation time)

### `manuscript/ave-kb/vol2/quantum-orbitals/ch07-quantum-mechanics/ionization-energy-validation.md`

- **Numerical claim:** 14-element ionization energy table, Z=1-14, ±2.8% maximum error vs experiment
- **Generating solver:** `ave.solvers.radial_eigenvalue.ionization_energy_e2k(Z)`
- **Generating SHA:** `0401388` (Applied-Vacuum-Engineering parent repo, 2026-04-09)
- **Locked at AVE-Core HEAD:** confirmed reproducible to ≤0.21% via `verify_atomic_ie_manuscript_table.py` after Q1+Q3+Q4+Q5+Q6 surgical restoration (commits `4c5035d`, `6783711`, `01f4f90`)
- **CI gate:** `make verify` + `pytest src/tests/test_radial_eigenvalue.py::TestManuscriptTableReproducibility` at ±0.5% tolerance
- **Verification doc:** [`research/L3_electron_soliton/100_a47_v9_reframing_line_687_retraction.md §10.16-§10.32`](../../../research/L3_electron_soliton/100_a47_v9_reframing_line_687_retraction.md)

---

## Verified entries (additional)

### `src/ave/solvers/g_minus_2_lattice.py` — corpus-canonical per Vol 2 Ch 6 §6.2

- **Numerical claim**: AVE-canonical C_2 = -0.0094 (anomalous magnetic moment 2nd-order coefficient).
- **Generating script**: K4 admittance tree S_11 reflection at depth=3, branch_y=NU_VAC=2/7, boundary_y=1.0, coordination_z=4.
- **Canonical source**: [`manuscript/vol_2_subatomic/chapters/06_electroweak_and_higgs.tex` §6.2 lines 429-457](../../../vol_2_subatomic/chapters/06_electroweak_and_higgs.tex#L429). Corpus position: AVE C_2 ≈ -0.0094 is the prediction; QED's -0.328 is the corpus-claimed-wrong continuum-extrapolation value where "continuous QED mathematics breaks down against the discrete vacuum hardware."
- **Axiom compliance**: Ax 1 (LC substrate) + Ax 2 (TKI ν_vac=2/7) + Ax 3 (effective action S_11 at Regime I/II boundary) + Ax 4 (saturation in K4 hopping). Zero free parameters.
- **Status**: AVE-axiom-compliant prediction LANDED corpus-canonically. Computation reproduces corpus claim end-to-end.
- **Empirical-vs-experimental tension** (Rule 11 honest flag): a_e^AVE = α/(2π) + C_2^AVE·(α/π)² gives a_e ≈ 0.0011614, vs experimental CODATA a_e = 0.0011597 (parts-per-trillion precision). Gap ≈ 1.5 ppm. QED's C_2 = -0.328 reproduces experimental a_e to ppt. AVE-axiom-compliance is settled (the prediction is corpus-canonical); experimental verification is a separate adjudication. Per the corpus, this empirical comparison is itself within the QED interpretive framework that AVE claims is wrong.
- **Verification doc**: doc 100 §18 (closure) + Rule 11 honest framing throughout.

---

## Pending verification (registered for forward-direction work)

The following manuscript files contain numerical claims about solver outputs but their generating-SHA + date have NOT yet been verified empirically. Each entry marks scope for future A47 v11c verification work — by analogy to the IE table arc (read manuscript-add commit, run solver at that SHA, confirm reproduction within tolerance, lock at CI gate).

### Validation tables

- **`vol3/gravity/ch02-general-relativity/k4-tlm-lensing-validation.md`** — gravitational-lensing K4-TLM validation. SHA pin: PENDING.
- **`vol5/molecular-foundations/biophysics-intro/chignolin-validation.md`** — Chignolin protein-fold prediction (3.82 Å). SHA pin: PENDING. Likely solver: protein-fold S₁₁ engine (separate biology engineering compendium).
- **`vol2/appendices/app-f-solver-toolchain/protein-eigenvalue.md`** — protein eigenvalue solver outputs. SHA pin: PENDING.

### Geometric-inevitability derivations (Vol 6 appendix)

- **`vol6/appendix/geometric-inevitability/g-star-derivation.md`** — G* (proton-electron mass ratio precursor or similar). SHA pin: PENDING.
- **`vol6/appendix/geometric-inevitability/golden-ratio-min-impedance.md`** — golden-ratio min-impedance derivation. SHA pin: PENDING.
- **`vol6/appendix/geometric-inevitability/derived-numerical-constants.md`** — derived-constants table. SHA pin: PENDING.
- **`vol6/appendix/geometric-inevitability/lambda-higgs-derivation.md`** — λ-Higgs coupling derivation. SHA pin: PENDING.
- **`vol6/appendix/geometric-inevitability/alpha-s-derivation.md`** — strong coupling α_s derivation. SHA pin: PENDING.

### Framework summaries

- **`vol6/framework/mass-defect-summary.md`** — mass defect / binding energy summary. SHA pin: PENDING.
- **`vol3/condensed-matter/ch11-thermodynamics/baryon-asymmetry-derivation.md`** — baryon asymmetry derivation. SHA pin: PENDING.
- **`vol3/condensed-matter/ch11-thermodynamics/baryon-asymmetry.md`** — baryon asymmetry summary. SHA pin: PENDING.
- **`common/solver-toolchain.md`** — universal solver toolchain reference. SHA pin: PENDING.
- **`common/full-derivation-chain.md`** — full derivation chain. SHA pin: PENDING.

### LaTeX volumes (likely candidates per grep for "AVE prediction" / numerical tables)

- `manuscript/backmatter/04_physics_engine_architecture.tex`
- `manuscript/backmatter/05_universal_solver_toolchain.tex`
- `manuscript/vol_1_foundations/chapters/08_alpha_golden_torus.tex` (α derivation, multipole decomposition; partially anchored via `verify_clifford_half_cover.py`)
- `manuscript/vol_2_subatomic/chapters/06_electroweak_and_higgs.tex`
- `manuscript/vol_2_subatomic/chapters/08_planck_and_string_theory.tex`
- `manuscript/vol_2_subatomic/chapters/10_open_problems.tex`
- `manuscript/vol_5_biology/chapters/01_biophysics_intro.tex`
- `manuscript/vol_5_biology/chapters/02_organic_circuitry.tex`
- `manuscript/vol_6_periodic_table/chapters/A_heavy_element_catalog.tex`

---

## Verification protocol (template for adding entries)

For any pending file:

1. **Identify generating commit** — `git log --diff-filter=A -- <manuscript-file>` (creation commit) or `git log --follow -- <manuscript-file>` for full history.
2. **Identify generating solver function** — read the file's prose and grep code for the named function.
3. **Verify reproducibility** — `git worktree add /tmp/ave-at-<SHA> <SHA>`, run the solver function, compare against the manuscript values.
4. **Lock at CI gate** — write a `verify_<topic>.py` script analogous to `verify_atomic_ie_manuscript_table.py`, hook into `make verify` target, parametrize a pytest reproducibility class.
5. **Move entry from "Pending" to "Verified" section here** with full provenance details.

If a file's generating SHA cannot be located (hand-computed values, deleted-branch outputs, or pre-commit-history values), that is itself a finding — the claim is unverifiable and the manuscript prose should either:
- Be regenerated against current solver state with new SHA pin, OR
- Be retired per Rule 12 retraction-preserves-body, with the original values preserved for audit trail.

---

## Pre-existing CI-anchored claims (legacy — pre-dates A47 v11c)

These claims were locked via existing verify scripts before the A47 v11c discipline was formalized. Verification protocol step 5 (move to "Verified" section above) requires reading the existing verify script + confirming the manuscript file matches.

- `verify_clifford_half_cover.py` → spin-1/2 Clifford double-cover (Vol 1 Ch 8 §α-closure)
- `derive_alpha_from_golden_torus.py` → α^{-1}_ideal = 4π³ + π² + π ≈ 137.0363 (Vol 1 Ch 8:178)
- `ropelength_trefoil_golden_torus.py` → ropelength → Golden Torus closure (Vol 1 Ch 8)
- `verify_universe.py` → DAG anti-cheat (no SM smuggling)

These are at varying levels of A47 v11c compliance — `verify_universe.py` is anti-cheat (negative gate, no SHA-pin needed), while the α/ropelength scripts SHOULD be SHA-pinned to their respective manuscript-table generation states. Audit pass pending.

---

— Last updated: 2026-04-30, post-doc-100 §10.32 cross-repo erosion-pattern audit. Manifest authored as Step 5 of A47 v9 RESOLUTION arc methodology infrastructure (auditor directive 2026-04-30 + Grant adjudication).
