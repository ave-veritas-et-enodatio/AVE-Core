# Figure audit ledger — staleness + placement (vs latest KB)

**Date:** 2026-06-07/08 · **Branch:** `analysis/2026-06-07-vol0-kb-reconciliation-ledger` (on origin/main `60f170a0`) · **Lane:** auditor (READ-ONLY — recommendations only; no figure is regenerated, placed, or pruned here).
**Two passes:** (A) **staleness** of the 208 *placed* `\includegraphics` across 6 volumes; (B) **placement** of the *unplaced* assets. Each finding checked vs current KB + the Vol0-KB/sim ledger drift checklist; high-severity findings adversarially re-verified; completeness-critic over each.

## Headline

- **Placed figures: 416 figure-units examined, 352 clean (~85%).** The substantive staleness findings **corroborate the text + sim ledgers** — the same drifts (z=3/SRS, birefringence E⁴-vs-E², BH bare Γ=−1, proton halo-mass/two-tier, A-034, amorphous-z₀) recur in figure *captions/renders*. ⟹ **one canonical fix per drift propagates to prose + sims + figures together.**
- **Placement: ~6 figures genuinely belong in the manuscript and aren't there; ~30 are correctly research-only; 4 are stale; 3 are HOLD.** The fresh `research/figures/` engine-outputs are the high-value finds.

---

## PASS A — STALENESS of placed figures

### S1 — structural drift (rendered image depicts superseded structure)
- **`lattice_structure_3d.png`** @ `vol_1_foundations/chapters/01_fundamental_axioms.tex:182` — renders **z=3 SRS** (generator `simulate_3d_lattice.py` hardcodes 3 neighbors: `argsort[1:4]`, labels "SRS"); caption "Chiral SRS Net." KB = z=4 4-fold K4 diamond (`eq_axiom_1.tex:20`). **Confirmed.** *(Clean contrast: `k4_tlm_decoherence_3d.png`/`k4_tlm_winding_evolution.png` correctly say "Diamond z=4".)* **Fix: regenerate at z=4 (`argsort[1:5]`), relabel "Chiral Laves K4 Cosserat Crystal (z=4)".**

### S4 — caption-claim drift (caption asserts a value/status the KB changed)
- **`birefringence_killswitch.png`** @ `vol_4 ch11` — "QED scales E²; AVE demands E⁴." KB: both E²-leading, discriminator is the **coefficient** not the exponent. (Matches sim-audit D3.)
- **`simulate_black_hole_core.png`** @ `vol_4 ch11` — "Dielectric Rupture (Γ=−1) at the Event Horizon … hard wall." KB: BH horizon **Γ=0 for EM** (sector-split; "no BH echoes in this frame"). The figure caption **lags the sector-split the engine code already implements** (O2).
- **Three proton-mass captions** carry the **retired halo-volume-as-mass** / pre-two-tier framing: `borromean_proton_3d.png` ("central toroidal void derives the mass"), `visualize_topological_bounds.png` ("saturated 3D toroidal halo"), `cross_scale_verification.png` (proton-to-CODATA without the +0.74%/−0.002% two-tier). KB: mass = dual-reactance `V_total=2`; halo-volume retired; two-tier framing required (#132 Correction 3). *(Critic flagged a likely 4th: `mass_oscillator_flowchart.png` @ `vol_2 ch02:222` — borderline; "geometric configuration … eigenvalue converges" is defensible as the preserved F-S eigenvalue. Verify.)*
- **`flyby_monte_carlo.png`** @ `vol_3 ch14` — σ-match counts differ from canonical (2/6 within 1σ …).
- **`quantum_spin_gyroscopic_precession.png`** @ `vol_2 ch04` — frames (2,3)/trefoil as the electron body; KB: electron real-space = 0₁ unknot, (2,3) is **phase-space** only (matches #132 Correction 1).

### HOLD — depicts one side of an open adjudication (do NOT "fix")
- **`rigidity_percolation_kg_convergence.png`** (vol_1 ch01 + vol_3 ch01) + **`emt_packing_landscape.png`** (vol_1 ch02) — all render the **amorphous z₀≈51.25 EMT** derivation of K=2G → **O3**.

### S3 — provenance gap (content checklist-clean, but no generator found)
~19 figures: incl. **`cross_scale_universality.pdf`** (orphan generator; the rendered summary-table instance-count can't be checked against A-034's canonical 26 — latent 19→26 risk), and a cluster of vol_3 impedance-profile figures (`solar_system_impedance`, `planetary_magnetospheres`, `gw_schwarzschild_impedance` [confirmed Γ=0 EM — clean], `stellar_impedance_profile`, …). Content current; reproducibility unverifiable.

### Systemic / out-of-figure-scope (flagged for the prose worklist)
- **vol_2 build-chain:** **21 of 29 vol_2 `\includegraphics` targets don't resolve** — vol_2 figures are gitignored/uncommitted (`.gitignore:46`). Build issue, not content.
- **Body-text Sagnac (not figures):** `vol_1 …04:258-263`, `vol_9 …15:80,234` ("Ψ=7.15 decisively falsifies"), and **`vol_4 …11:107`** ("definitive near-term kill-switch") still frame Sagnac as a **live forward kill-switch** — retired to corroborative-null 2026-06-03. (Same drift as Vol0 ledger D5 + sim-audit Sagnac.)
- **Cross-volume E⁴:** the birefringence E⁴ caption recurs in `vol_1 ch03:278` (`vacuum_dielectric_saturation.png`) — though there it's the *legitimate* Euler-Heisenberg E⁴ Lagrangian regime label, not the retired exponent-discriminator. Adjudicate.

---

## PASS B — PLACEMENT of unplaced assets

### PLACE-NEW — current asset, target section is figure-less (skeptic-confirmed)
| Asset | Target | Note |
|---|---|---|
| `research/figures/electron_genesis_landmark_montage.png` | `vol_1 …03_quantum_and_signal_dynamics.tex` §"Internal Confinement and Matter Assembly" (~:198) | **PRIME.** REAL FDTD3DEngine self-trap montage, z=4 diamond, α canonical, (2,3)/spin **NOT** planted (validation.json). Subsection is figure-less (figs bracket at :173/:227). |
| `research/figures/photon_engine_real_strip.png` | `vol_1 …04_continuum_electrodynamics.tex` propagation region (~:66-72) | REAL K4-TLM + FDTD Yee output; figure-less until :214. (REPLACES the analytic `photon_vs_electron_cells_strip.png` — see LEAVE-STALE.) |
| `ie_validation_z1_14.pdf/.png` | `vol_2 …07_quantum_mechanics_and_orbitals.tex:40` | the canonical, scope-exact Z=1-14 IE validation (the *locked* range — distinct from the heavy-Z drift). **Use the corrected copy, not the vol_2/figures one showing Al(Z=13) OPEN.** |
| `lithium_7_density_z_pos.png` | `vol_6 …05_lithium.tex:29` (panel-1 of the two-up minipage) | element render, slot exists. |
| `circuit_be8_decay.pdf` | `vol_6 …06_beryllium.tex` §"Topological Area of Interest" | decay-circuit, figure-less section. |
| `circuit_orbital_phase_jitter.pdf` | `vol_2 …07_…orbitals.tex:264` §"The Mutual Cavity" | figure-less subsection. |

### HOLD — current/illustrative but blocked on an open call
- **`ave_electron_anatomy.png` + `_v2.png`** — hand-drawn schematic (not engine output) depicting the **contested (2,3)-winding** (validation.json: `PLANTED_ILLUSTRATIVE`, "does NOT emerge, P4 FAIL") + cubic-not-sphere. **Blocked on a NEW corpus inconsistency the audit surfaced:** `vol_2 …01_topological_matter.tex` is **internally split on electron topology — `:142` "0₁ Unknot" vs `:161` "Trefoil (3₁) → Electron"** (and `:198` "spherical 0Ω boundary" vs anatomy "cubic T_d"). Resolve the electron-topology/geometry inconsistency before placing an anatomy figure.
- **`tau_fold_validation.png`** (vol_5) — depicts τ_fold=3Q²·N with slope=0.13 (prediction barely tracks experiment); ties to the staged AVE-Protein impedance-folding negative. Hold.

### LEAVE-STALE — do not place (prune candidates)
- `photon_vs_electron_cells_strip.png` — analytic hand-drawn (`exp(−x²)cos`/`sech`), superseded by `photon_engine_real_strip.png`.
- `vol_2/figures/ie_validation_z1_14.png` — shows Al(Z=13) as OPEN +13.7% (stale; Z=1-12 match KB).
- `fig_mass_gap_ladder.pdf` — x-axis mislabels the electron bar.
- `fig_solar_spin_tensors.png` — hardcoded A_gm magnitudes + regime-label drift.
- *(critic-added, un-triaged but flagged):* `circuit_sagnac_rlvg.pdf` (retired-Sagnac).

### KEEP-RESEARCH-ONLY — legitimately not manuscript material (~30)
The 4 remaining genesis stage-frames + interstitial droplet (subsumed by the montage); `flux_tube_dynamics`/`lattice_polarization_saturation` (self-labeled schematics); the 4 alpha-map script outputs (support frozen pre-regs); the HOPF figures (**canonical-elsewhere** — AVE-HOPF owns them per AGENTS.md §6); 6 raster duplicates of placed vector PDFs; 14 vol_6 alternate-view element renders (section already has a figure); older `assets/` research panels (mostly superseded).

### Coverage gap (honest — placement pass was NOT exhaustive)
The orphan inventory I seeded (66) **undercounted**; the true orphan population is **~134** (my `find` missed `.gif`s, `vol_6/simulations/outputs/` nuclear renders, a 2nd `vol_6/circuits/` duplicate set, `vol_6` root `*_strain.png`). **~41 orphans + 6 GIFs went un-assessed** — mostly low-value element-strain / nuclear-sim renders / duplicate circuit sets. Notable un-assessed: `circuit_sagnac_rlvg.pdf` (retired-Sagnac → LEAVE-STALE), `vol3_sonoluminescence_collapse.png`, `vol3_tabletop_relativity_lorentz.png`, `metric_catalyzed_fusion.png`. **A complete orphan re-sweep (quote-tolerant refs + `.gif` + all subdirs) is the follow-up.**

---

## Cross-layer takeaway
The figure layer's staleness is the **same drift set** as the text + sim ledgers (z=3/SRS, birefringence-exponent, BH bare-Γ, proton halo-mass/two-tier, Sagnac-live, A-034 19→26, amorphous-z₀). So the eventual canonical fixes (when the HOLD items close + the sync runs) clean all three layers at once. The **one genuinely-new finding** from the figure passes is the **vol_2 ch01 electron-topology self-contradiction (0₁ unknot vs trefoil)** — surfaced only by trying to place the anatomy figure; it gates the anatomy placement and is a Grant-call (couples to the electron-identification phase-space-vs-real-space relabels in #132).

## Worklist (separate non-draft PR — these WOULD edit/place figures)
1. **Place the 6 PLACE-NEW** (montage→ch03, photon-strip→ch04, ie_validation→vol2 ch07, lithium_7→vol6, be8_decay→vol6, orbital_jitter→vol2). 
2. **Regenerate `lattice_structure_3d.png` at z=4** (S1) + the S4 caption fixes (birefringence exponent→coefficient, BH Γ→sector-split, proton halo→dual-reactance/two-tier).
3. **Prune/relabel** the 4 LEAVE-STALE; **fix the vol_2 build-chain** (gitignored figures).
4. **HOLD:** anatomy figures (gated on vol_2 ch01 electron-topology resolution); tau_fold (impedance-folding); amorphous-z₀ figures (O3).
5. **Follow-up:** complete orphan re-sweep (~41+6 un-assessed); propagate the Sagnac retirement to vol_4:107 / vol_9:80,234 prose.

## Discipline
`ave-sweep-audit`, `ave-canonical-source`, `verify-before-cite` (each S1/S4/PLACE-NEW adversarially re-verified), `ave-evidence-framing-discipline` (coverage gap recorded, not hidden), `flag-don't-fix`. READ-ONLY.
