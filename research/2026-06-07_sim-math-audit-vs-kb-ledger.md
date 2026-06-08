# Sim math audit vs latest KB — ledger

**Date:** 2026-06-07 · **Branch:** `analysis/2026-06-07-vol0-kb-reconciliation-ledger` (off `main` @ `f1f927c8`) · **Lane:** auditor (READ-ONLY).
**Scope:** every simulation script's MATH vs the current KB — canonical-constant compliance (`src/ave/core/constants.py`), formula-vs-KB-derivation, asserted-output-vs-latest-KB-value, print-not-compute honesty. Cross-referenced to the Vol 0 ↔ KB ledger's Class-D drifts.

## Headline (reassuring)

**446 sims triaged, 412 SIM-MATCH (92%).** **None of the manuscript-text drifts the Vol 0 ledger surfaced propagated into the simulation layer:** no `T_EM=2.1e9` (the 10-OOM historical bug — gone tree-wide), no `τ_yield=7.21e34` Bingham form, no "19-instance" A-034 census, no hard-coded `z=3` (every connectivity is `coordination_z=4`), no `9/7`-as-light-deflection in production code. The C11 Mach-Zehnder sim (`electron_interferometry_parallax.py`) is **correctly fixed to ~250 rad** (the factor-7 driver bug repair landed in code). The drift lives in manuscript prose, not the engines.

## THE headline finding (meta) — the provenance gate itself is stale

`common/numerical-provenance-manifest.md:33-44` still pins `src/ave/solvers/g_minus_2_lattice.py`'s **`C_2 = −0.0094`** as *"corpus-canonical … LANDED … reproduces corpus claim end-to-end"* and brands `−0.328` *"the corpus-claimed-**wrong** value."* **The latest KB inverted this:** `vol_2_subatomic/chapters/06_electroweak_and_higgs.tex:460` is titled **"The K4-Bethe-Tree Substrate Was Wrong"**; canonical is now Route-B Cosserat-(2,3)-trefoil **`C_2 = −0.32846`** (`q-g19a-petermann-saliency-closure.md:10`). `grep "0.0094"` across the KB returns exactly two files — the closure doc (which *refutes* it) and the manifest (which still *endorses* it). The solver's own docstring is already annotated with the Route-B correction, but `compute_c2_structural()` still returns −0.0094 **and the A47 provenance gate still vouches for it**, while the actually-canonical generator (`vol_2_subatomic/simulate_g2_direction2.py` `route_b_correlation()` → −0.32846) is **unregistered**. The provenance infrastructure is the most-stale artifact in the chain.
**Fix:** repoint `numerical-provenance-manifest.md` g-2 entry to Route-B / `simulate_g2_direction2.py`; mark `g_minus_2_lattice.py compute_c2_structural()` as the refuted K4-tree route (Rule 12 preserve-body).

## Findings by class (34 from the cluster pass; supplement pending — see below)

### D1 — value drift (output ≠ latest KB)
- **`vol_2_subatomic/generate_verification_trace.py:37`** — `F_conf = 3(m_p/m_e)α⁻¹T_EM` → **0.999 GeV/fm (160,030 N)**, computed from canonical constants. KB chain `full-derivation-chain.md:571,880` = **1.002 GeV/fm (160,584 N)**. ⟹ the **sim is evidence the formula yields 0.999**, so the confinement-split (Vol 0 ledger D4) likely resolves toward 0.999, with `full-derivation-chain`'s 1.002 the rounded/drifted side. Adjudicate the split using the sim's computed value.
- **`vol_6_periodic_table/circuits/generate_all_semiconductor_circuits.py:409,541`** — `V_BR = 3.594 MeV` **hard-coded as a LaTeX string** (not computed). KB latest = **3.631 MeV** (`vol6/claim-quality.md:16`, clm-jy8h1x). Stale figure value.

### D3 — formula superseded (KB walked it back)
- **Sagnac forward-prediction (3 sims):** `vol_4_engineering/{simulate_sagnac_kinematic_entrainment.py, simulate_sagnac_rlvg_tolerances.py, plot_sagnac_entrainment.py}` — all frame Sagnac kinematic entrainment as a live AVE-distinct **forward kill-switch**, but it was **retired to corroborative-null 2026-06-03** (`sagnac-rlve.md:12`). **Same systemic drift as Vol 0 ledger D5** (text + Vol 4 leaves + these sims all carry the stale forward framing — the retirement never propagated).
- **`vol_4_engineering/simulate_vacuum_birefringence_E4.py:75,114`** — frames the AVE-vs-QED discriminator as the **exponent** (AVE E⁴ vs QED E²). KB: both are E²-leading; the discriminator is the **coefficient** `1/(4·a_EH·α³)`, not the exponent. Superseded framing.
- **`src/ave/solvers/g_minus_2_lattice.py`** `C_2=−0.0094` — the sim side of the meta finding above (refuted K4-tree route).

### D4 — print-not-compute (asserts a value it doesn't compute)
- **`vol_1_foundations/derive_alpha_m4_pro.py:137`** + **`boinc_alpha_derivation.cpp:217`** — banner *"RIGIDITY PERCOLATION METRIC REACHED"* / *"derive α via percolation rank"*, but the rank is **never computed** (admitted in-comment: *"will hang a laptop… instead we print the organic geometric tracking"*); the printed "prediction" is the **circular `8π/p_c`** (= inverse of `p_c=8πα`) on an arbitrary sweep radius — numerically yields ~83.8 at the break, not 137. *(The percolation route to α/z₀ is itself KB-OPEN — couples to HOLD-item O3; the finding is honesty, not value.)*
- **`vol_4_engineering/simulate_rigidity_percolation.py:49-50`** — claims *"deriving α from pure graph geometry"*; the genuine EMT z₀-quadratic derivation lives in `born_huang_percolation` — this one mislabels.
- **(critic-recovered) `vol_2_subatomic/standard_model_simulations/fractional_charge_solver.py:106-108`** — prints `+0.666e (Up)`, `−0.333e (Down)` under `[ANALYTICAL OUTPUT]`, but only plots three parametric cos/sin loops — **no flux integrated**. Uncaught initially (vol_2 glob missed the subdir).

### HOLD — depends on an open adjudication (NOT drift)
- **`verify/gravity_ppn_coherence.py:18,312-317`** — computes light deflection via the **9/7 "spatial" index** → `δ=18GM/bc²` (4.5× GR). This is the **open gravity-PPN adjudication** (W1 outlier; branch `analysis/gravity-ppn-coherence` unmerged) — its *purpose* is to expose the (9/7)-controls-light-deflection mislabel. Imports canonical `G,C_0,M_SUN` and recomputes GR. Resolve with the gravity-PPN thread, not as a sim bug.

### B — provenance gap (value OK / backs a claim, but hard-coded or not SHA-pinned)
- `src/ave/solvers/spice_netlist_compiler.py` — `v_yield=43653.7` hard-coded (KB `√α·V_SNAP≈43653.9`, `constants.py:387`); `i_max=124.4` placeholder (no canonical I_max). Should import.
- `verify/muon_g2_fermilab_anchor.py:122` — `Δc_2=9.30e-4` hard-coded as a corpus-quote, not computed (the forward prediction is asserted, not derived).
- `vol_1_foundations/photon_saturation_animation.py:337` — `1/137.036` inline for `sqrt(2α)` instead of `ALPHA`.
- `vol_3_macroscopic/simulate_cosmology_bao.py:23` — re-implements `H_∞` locally instead of importing `H_INFINITY` (value correct).
- `trampoline_framework/generate_all.py:367` — `α` inline (correct value, no import).
- `vol_6/circuits/make_heavy_circuits.py:109` — `M=32.8, V_R/V_BR=0.994` hard-coded LaTeX (matches KB, not derived).

### M — orphan / broken / scratch (18)
- **Broken imports (would crash):** `vol_3/simulate_geodynamo_vca.py:12` imports `GRAVITATIONAL_CONSTANT` (no such symbol — it's `G`, `constants.py:156`); `vol_6/simulations/simulate_dt_fusion.py` imports nonexistent `generate_fusion_netlist`; `vol_6/simulations/spice_exporter.py` empty body (intentional IP-partition stub).
- **Shared non-canonical-mass pattern (critic):** empirical PDG `M_P=1.00727 / M_N=1.00866 amu` hard-coded in ≥3 vol_2 sims (`assemble_uranium.py:41`, `simulate_uranium_fission.py:42`, `visualize_isotope_stability.py:30`) vs AVE-derived `M_P_MEV_AVE=938.2539` (`constants.py:950`) — a *systemic* non-canonical pattern, not 3 unrelated orphans.
- Remainder: visualization/demo scripts with phenomenological params (neutrino-oscillation GIF, borromean plots, normalized-unit FDTD) — no KB claim mapped.

## Coverage — first pass + SUPPLEMENT IN FLIGHT

**Cluster pass covered (446):** vol_1 (200), vol_2 (48 — glob miss of 4 subdir files, +1 D4 recovered by critic), vol_3 (63), vol_4 (49), vol_6 (42), verify (16), peer_review+trampoline (14), `src/ave/solvers` (14).
**Supplement running (`wzbl5usf6`, ~140 files):** the **~85 `src/ave/` canonical engines** the first pass skipped (`gravity/ topological/ regime_1-4/ nuclear/ condensed/ plasma/ axioms/ core/` — incl. `cosserat_field_3d.py` the canonical electron substrate, `black_hole_core.py` the BH-Γ HOLD engine, the doping engines behind Vol 6), the **90-test regression layer** (incl. the manifest-flagship `test_radial_eigenvalue.py`), vol_2 subdirs, `_archive` (23). **This section will be appended when the supplement lands.**

## Sync worklist (separate session)
1. **META (do first):** repoint `numerical-provenance-manifest.md` g-2 entry off the refuted `C_2=−0.0094` to Route-B `simulate_g2_direction2.py` (−0.32846); the gate currently certifies a walked-back value.
2. **Propagate the Sagnac retirement** into the 3 vol_4 forward-prediction sims (same fix as Vol 0 ledger D5 + Vol 4 leaves).
3. **V_BR 3.594→3.631** in the Vol 6 semiconductor figure generator.
4. **Confinement split:** use the sim's computed 0.999 to resolve the KB-internal 0.999/1.002 split (ledger D4).
5. **Birefringence** discriminator: exponent→coefficient framing.
6. **Honesty relabels (D4):** the 3 percolation-α scripts + `fractional_charge_solver.py` — either compute the asserted quantity or relabel as non-predictive demos.
7. **Fix 2 broken imports** (`simulate_geodynamo_vca`, `simulate_dt_fusion`).
8. **HOLD:** `gravity_ppn_coherence.py` rides the gravity-PPN adjudication (O-class).

## Discipline
`ave-sweep-audit`, `ave-canonical-source` (constants.py compliance), `ave-driver-script-honesty` (print-vs-compute), `verify-before-cite` (skeptic re-verify each high-severity), `ave-evidence-framing-discipline`, `flag-don't-fix`. READ-ONLY — no sim/KB edits.
