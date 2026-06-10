# Sim math audit vs latest KB — ledger

**Date:** 2026-06-07 · **Branch:** `analysis/2026-06-07-vol0-kb-reconciliation-ledger` (off `main` @ `f1f927c8`) · **Lane:** auditor (READ-ONLY).
**Scope:** every simulation script's MATH vs the current KB — canonical-constant compliance (`src/ave/core/constants.py`), formula-vs-KB-derivation, asserted-output-vs-latest-KB-value, print-not-compute honesty. Cross-referenced to the Vol 0 ↔ KB ledger's Class-D drifts.

## Headline

**Combined: ~648 sim-units triaged (446 scripts pass + 202 engine/test supplement), ~591 SIM-MATCH (~91%).** The **value-consuming math is clean**: no engine *computes* a stale physics value from `T_EM=2.1e9` (the 10-OOM bug is gone tree-wide), the `7.21e34` Bingham number, hard-coded `z=3` (every connectivity is `coordination_z=4`), or `9/7`-as-light-deflection (only `gravity_ppn_coherence.py`, which is HOLD and *exists to expose* that mislabel). The C11 Mach-Zehnder sim is correctly fixed to ~250 rad.

**Two corrections to the first-pass headline (the supplement caught these):**
- **The A-034 "19" DID reach engine code** — `constants.py:46`, `universal_operators.py:36`, `master_equation_fdtd.py:27`, `scale_invariant.py:18` assert "19 catalog instances" in **docstrings/comments** (latest KB = 26). Documentation-severity (no engine math consumes the count), but real D1.
- **The dropped τ_yield-Bingham framing reached one engine** — `src/ave/core/lbm_3d.py:13` carries *"Yield stress τ_y = B_snap²/(2μ₀) (Bingham plastic)"* — the Bingham yield-stress framing the KB dropped 2026-04-20 (a different *form* than 7.21e34, but the retired framing).

So: the **physics the engines compute is canonical**; the staleness that reached code is **documentation/framing in a handful of files** + one genuinely-drifted *solver output* (the IE finding below).

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

## Supplement results (`wzbl5usf6`, 202 files: ~85 `src/ave/` engines + 90 tests + vol_2 subdirs + 23 `_archive`)

179/202 SIM-MATCH. **New HIGH-severity finding + the two headline corrections above + the HOLD-items confirmed live in code:**

### D1 — **Ionization-energy solver drift for heavy elements (NEW, HIGH)**
`src/ave/nuclear/{gallium_atom.py:10, germanium_atom.py:12, arsenic_atom.py:10}` compute (live `ionization_energy_e2k(Z)`) **IE = 3.20 / 4.66 / 6.00 eV** for Ga/Ge/As — but the KB IE table (`vol6/framework/ionization-energy-summary.md:28-30`) gives the AVE column as **5.999 / 7.763 / 9.742 eV**. ~2× discrepancy. This is **exactly the `radial_eigenvalue` drift pattern the A47 manifest was built to catch** — but for Z=31-33, *outside* the Z=1-14 range the manifest says was surgically restored + CI-locked. The flagship `verify_atomic_ie_manuscript_table.py` (cited at manifest:25 as the IE CI gate) **could not be located in `src/scripts/verify/`** — possible dangling reference / the gate doesn't exist for these Z. **Resolve: re-run the IE solver at Z=31-33 against the KB table; either the solver drifted or the table is from a restored state the engine no longer reproduces.**

### D1 — A-034 "19" in 4 engine docstrings (the headline correction): `constants.py:46`, `universal_operators.py:36`, `master_equation_fdtd.py:27`, `scale_invariant.py:18` → bump to 26.

### D3 — `lbm_3d.py:13` dropped-Bingham τ_yield framing (headline correction); the g-2 manifest stale-pin (confirmed both halves — `g_minus_2_lattice.py` header *already* says "SUPERSEDED 2026-05-13"; the manifest is the lone stale node; canonical generator `simulate_g2_direction2.py` unregistered).

### D4 — `src/ave/condensed/{gaas_doping.py:26, germanium_doping.py:33}` hard-code experimental band-gaps (1.424, 0.681 eV) overwriting the structural compute (no AVE-Core KB derivation — silicon-design migrated to AVE-APU, cross-repo); `src/ave/axioms/{navier_stokes.py:276, millennium.py:135}` assert `GLOBAL_EXISTENCE_PROVEN=True` / "RIGOROUS DERIVATION" with **zero computation** (sibling `yang_mills.py` is the honest one — discloses "NOT a Clay-Prize proof").

### HOLD — the three open items are LIVE in canonical code (good to know for adjudication):
- **O1 (Δc_crit=3):** `src/ave/topological/mixing_derivation.py` hard-codes `Delta_c_crit=3`.
- **O2 (BH Γ):** `src/ave/regime_3_saturated/black_hole_core.py` **already implements the sector-split correctly** — `r_sat=7GM/c²`, `S=√(1−ε²)`, **no bare Γ=−1** (EM stays GR). `rupture_solver.py` is an exemplary sector-split reference. So the O2 canonical resolution is *already in the engines* — only the KB *labels* lag.
- **O3 (amorphous z):** `src/ave/core/constants.py:480` hard-codes `Z_COORDINATION ≈ 51.25` (the amorphous-EMT root of `P_C·z₀²+(2P_C−10)z₀+12=0`) — the amorphous picture is baked into the canonical constants.

### B / M (supplement)
- B: `test_regime_map.py:214` (`3e8` for c, +0.07%), `test_framework_25_derived.py` (stale "25 SM from 3 inputs" vs current "structural closure" framing), `lense_thirring.py` + `entanglement_thread.py` (α/r_opt literals), `condensed/condensed_matter.py` (underived 1.2 prefactor), `silicon_doping.py` V_bi 1.04904 vs 1.0496, `silicon_nucleus.py` mass 26084 vs 26053.
- M: ~26 `_archive` engine-driven phase-test scratch (r7/r8/r9/r10) + vol_2 animations (no KB claim); `bjt_mechanics.py` (leaf removed from AVE-Core per REPO-ARCH-7). **tests-regression: 88/90 MATCH** — the regression layer is clean.
- **Latent code bug (robustness, no value impact):** `spectral_gap.py:269` `BARYON_LADDER[5]["mass_MeV"]` will KeyError (key is lowercase `mass_mev`) for crossing numbers outside {3,5,7,9,11,13}.

## Sync worklist (separate session)
0. **HIGH (do first — possible real solver drift):** re-run `ionization_energy_e2k(31/32/33)` for Ga/Ge/As vs the KB IE table (5.999/7.763/9.742 eV); the engine gives ~2× low. Locate or rebuild `verify_atomic_ie_manuscript_table.py` (manifest:25 cites it as the IE CI gate; it could not be found) and extend the lock past Z=14.
1. **META:** repoint `numerical-provenance-manifest.md` g-2 entry off the refuted `C_2=−0.0094` to Route-B `simulate_g2_direction2.py` (−0.32846); the gate currently certifies a walked-back value.
2. **Propagate the Sagnac retirement** into the 3 vol_4 forward-prediction sims (same fix as Vol 0 ledger D5 + Vol 4 leaves).
3. **V_BR 3.594→3.631** in the Vol 6 semiconductor figure generator.
4. **Confinement split:** use the sim's computed 0.999 to resolve the KB-internal 0.999/1.002 split (ledger D4).
5. **Birefringence** discriminator: exponent→coefficient framing.
6. **Honesty relabels (D4):** the 3 percolation-α scripts + `fractional_charge_solver.py` — either compute the asserted quantity or relabel as non-predictive demos.
7. **Fix 2 broken imports** (`simulate_geodynamo_vca`, `simulate_dt_fusion`).
8. **HOLD:** `gravity_ppn_coherence.py` rides the gravity-PPN adjudication (O-class).

## REBASE DELTA — re-verified against origin/main `60f170a0` (2026-06-08; +21 PRs since base `f1f927c8`)

- **g-2 manifest stale-pin — CONFIRMED STILL LIVE.** PR #135 (`lepton-sector-corrections`) did NOT touch the manifest; `numerical-provenance-manifest.md:35` still pins `C_2=−0.0094` as canonical and brands −0.328 "wrong." Finding stands.
- **NEW upstream infra — code-provenance-index (PR #136).** `src/scripts/verify/{CODE_PROVENANCE.md, code_provenance.jsonl (6-seed), verify_code_provenance.py (drift-gate verifier)}`. The 6 seeds cover **proton/lepton claim-ids** (clm-cmic3e, clm-k6olj8…), **not g-2 or IE** — so my g-2-manifest-stale and IE-drift (Ga/Ge/As) findings are exactly the **prime next seeds** for this gate. **Recommend: register `simulate_g2_direction2.py` (Route-B C_2) and the heavy-Z IE generators as the next code-provenance seeds** — this new infra is the right home for the sim worklist.
- **r_opt STL scale-bug (PR #137 §43) — MY AUDIT MISSED IT.** Upstream found a *real code-level scale bug* (~2290–4583×) in the STL geometry export (`generate_particle_stl.py` + `cosserat_field_3d.py`/`entanglement_thread.py`), now fixed (`assets/3d_models/ACCURATE_SCALING.md`). My sim-audit's drift-target list didn't include geometry-export scale, so it slipped — honest coverage gap, now resolved upstream.
- **`entanglement_thread.py` B-finding — partially addressed by #137:** `r_opt` default is now documented as the dimensionless coupling-budget ratio `κ_FS/c` (per the #133 relabel), not a bare length-literal. (`spectral_gap.py:269` KeyError untouched — still stands.)
- **Unchanged on origin/main:** the IE solver drift (Ga/Ge/As), A-034-in-docstrings, lbm_3d Bingham, Sagnac sims, confinement 0.999, V_BR, birefringence — all re-grep-confirmed present. The HOLD-in-code items (O1 mixing_derivation, O2 black_hole_core sector-split, O3 constants.py:480 z₀≈51.25) stand.

## Discipline
`ave-sweep-audit`, `ave-canonical-source` (constants.py compliance), `ave-driver-script-honesty` (print-vs-compute), `verify-before-cite` (skeptic re-verify each high-severity), `ave-evidence-framing-discipline`, `flag-don't-fix`. READ-ONLY — no sim/KB edits.
