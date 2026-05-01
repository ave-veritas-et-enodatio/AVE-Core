# Parent repo FDTD + photon-helical-confinement infrastructure: full research per A47 v10 direct verification

**Date:** 2026-05-01
**Predecessor:** [doc 104 §8.10 self-audit corrections](104_round_13_layer_3_entry.md) + Grant directive 2026-05-01 ("can you research for any rifle photon simulations in the applied vacuum engineering archived repo?" + "yes fully research")
**Status:** working analysis — parent repo audit per A47 v10 cross-repo direct-verification rule

---

## §1 — Research scope

Grant prompted research on parent Applied-Vacuum-Engineering archive for "rifle photon" simulations — Grant's plumber-physics term for photon-as-helical-confined-EM-packet (rifling = polarization rotation along propagation axis). Connects to L3 arc Round 14+ candidate (γ) sub-ℓ_node infrastructure for canonical electron testing.

Parallel deep research via three Explore agents covering:
1. Static visualization scripts (`simulate_helical_confinement.py` + `plot_photon_helical_spin.py`)
2. FDTD3DEngine implementation + `visualize_photon_helicity.py`
3. Corpus manuscript framework for photon→electron formation

All findings A47 v10 direct-verification format (file:line referenced) + A43 v2 verbatim corpus citations.

---

## §2 — Finding 1: helical-confinement scripts are STATIC VISUALIZATIONS, not FDTD simulations

The two scripts originally surfaced as "rifle photon simulations" are ANALYTICAL VISUALIZATIONS, NOT runnable simulations of dynamics:

### §2.1 — `simulate_helical_confinement.py` (83 lines)

[`/Users/grantlindblom/Applied-Vacuum-Engineering/src/scripts/vol_1_foundations/simulate_helical_confinement.py`](../../../Applied-Vacuum-Engineering/src/scripts/vol_1_foundations/simulate_helical_confinement.py)

- **Algorithm:** static visualization from analytical formulas; NO time-stepping, NO FDTD integration
- **Impedance profile:** Z(z) = exp(0.4z), exponential ramp [1 → ~55] over z ∈ [0, 10]
- **Wave vector formula:** k_z = 2.0 × Z(z) (analytical, hardcoded, no derivation in script)
- **Transverse radius formula:** R(z) = 1/√Z(z) (analytical, hardcoded)
- **Final state:** R(z=10) ≈ 0.13, "stationary spin-1 spring" per script line 37 — but as DRAWN parametric curve, not a relaxed eigenmode of any equation
- **Output:** single PNG illustration; no numerical observables computed
- **Pass/fail:** none; purely illustrative

### §2.2 — `plot_photon_helical_spin.py` (159 lines)

[`/Users/grantlindblom/Applied-Vacuum-Engineering/src/scripts/vol_2_subatomic/plot_photon_helical_spin.py`](../../../Applied-Vacuum-Engineering/src/scripts/vol_2_subatomic/plot_photon_helical_spin.py)

- **Algorithm:** static multi-panel visualization, parametric curves
- **Three panels:** linear wave → impedance-gradient compression → toroidal helix
- **Hardcoded final state:** R_major=1.5, R_minor=0.5, n_winds=3 (FIXED parametric values, not computed)
- **Output:** single PNG (300 dpi, 18×7 in) — used as `photon_helical_spin.png` in Vol 2 Ch 1 (`01_topological_matter.tex` figure caption)
- **Connection to corpus constants:** NONE — no ℓ_node, m_e, α references in the script
- **Pass/fail:** none

### §2.3 — Honest finding

These scripts are **manuscript figure generators**, not computational tests of physics. They illustrate the corpus narrative but do not VALIDATE it dynamically. Per Rule 14 substrate-derives-the-answer: a parametric curve is not a substrate-physics test.

Implication: parent does NOT have a runnable photon-helical-confinement simulation. The "rifle photon" picture is corpus-narrative + manuscript-figure, not engine-empirical.

---

## §3 — Finding 2: FDTD3DEngine is real but UNFIT for sub-ℓ_node corpus electron testing

The parent has a real FDTD solver at [`/Users/grantlindblom/Applied-Vacuum-Engineering/src/ave/core/fdtd_3d.py`](../../../Applied-Vacuum-Engineering/src/ave/core/fdtd_3d.py) (NumPy backend) + [`fdtd_3d_jax.py`](../../../Applied-Vacuum-Engineering/src/ave/core/fdtd_3d_jax.py) (JAX backend, GPU-capable).

### §3.1 — Architecture (verbatim per direct-read agent report)

- **Class:** `FDTD3DEngine.__init__(nx, ny, nz, dx, linear_only, v_yield, b_yield, use_pml, pml_layers)` at fdtd_3d.py:49–125
- **Step method:** `step()` at fdtd_3d.py:512–520 — sequential H-update (Faraday) + E-update (Ampere) + boundary
- **Tracked fields:** Ex, Ey, Ez, Hx, Hy, Hz (6-component Maxwell on Yee grid)
- **Constitutive model — Axiom 4 saturation:**
  - ε_eff = ε₀·√(1 − (E·dx / V_yield)²) at fdtd_3d.py:186-217
  - μ_eff = μ₀·√(1 − (B / B_yield)²) at fdtd_3d.py:219-242
- **Coordinate system:** Cartesian uniform Yee staggered; finite-difference 1st order in space
- **Time-stepping:** leapfrog; CFL dt = dx/(c√3) at fdtd_3d.py:77
- **Boundary conditions:** Mur 1st-order ABC default; PML option (polynomial-graded conductivity)

### §3.2 — Sub-ℓ_node capability assessment

- **No sub-cell resolution.** Pure uniform Yee grid; finest feature is 1 cell.
- **dx is computational parameter, not physical lattice pitch** — user can set dx freely
- **No spectral methods** (no FFT-based derivatives)
- **No mesh refinement / AMR**
- **Memory scaling problem:** to resolve corpus electron R = ℓ_node/(2π) ≈ 0.16 ℓ_node, would need dx ≤ ℓ_node/10 = 3.86×10⁻¹⁴ m. At a 100 ℓ_node domain → 1000³ grid = ~1B cells, infeasible

### §3.3 — Test infrastructure

- **5 test files** at parent's `tests/` covering FDTD3DEngine
- **Validated:** dipole radiation, linear/nonlinear equivalence at weak fields, nonlinear divergence at strong fields, energy conservation, CFL stability, JAX-NumPy backend equivalence
- **NOT validated:** sub-ℓ_node confinement, particle-formation, AVE subatomic predictions
- 17 files import FDTD3DEngine (mostly Vol 4 PONDER-01 ponderomotive thrust simulations + Vol 7 hardware metrics)

### §3.4 — Honest finding

FDTD3DEngine is a **validated macroscopic photon propagator with Axiom 4 saturation kernel**. It is NOT a confined-state solver and NOT fit for sub-ℓ_node corpus electron testing without major redesign (spectral methods, AMR, OR a separate micro-domain at dx ≤ ℓ_node/100).

The Axiom-4-augmented FDTD demonstrates the saturation-kernel mathematics works in principle (impedance increases, wave compresses, ε_eff/μ_eff modulate). It does NOT demonstrate the corpus claim "photon condenses into electron at impedance saturation" — that claim is unrun.

---

## §4 — Finding 3: corpus framework asserts photon→electron but doesn't derive it computationally

Per A43 v2 verbatim grep on parent manuscript:

### §4.1 — Verbatim corpus claim (Vol 2 Ch 1 §1)

[`Applied-Vacuum-Engineering/manuscript/vol_2_subatomic/chapters/01_topological_matter.tex:160`](../../../Applied-Vacuum-Engineering/manuscript/vol_2_subatomic/chapters/01_topological_matter.tex#L160) figure caption "Spin-1 Helical Confinement of an EM Wave":

> *"A spatial solver demonstrating how a propagating Transverse EM Wave winds into a stationary Spin-1 helical loop when encountering extreme localised network impedance (Z → Z_crit). The discrete sequential excitation of the M_A LC nodes guarantees charge containment, establishing the physical derivation of confined point-particles via continuum wave-crashing."*

The figure caption claims a "spatial solver" demonstrates this — but the underlying figure is `photon_helical_spin.png` from `plot_photon_helical_spin.py`, which is **parametric visualization, not a solver output** (per §2.2 above).

### §4.2 — Pair production / annihilation

[`01_topological_matter.tex:152`](../../../Applied-Vacuum-Engineering/manuscript/vol_2_subatomic/chapters/01_topological_matter.tex#L152) verbatim:

> *"e⁻(+ω) + e⁺(−ω) → 2γ &nbsp;&nbsp; E_total = 2 m_e c² = 1.022 MeV"*

Annihilation direction stated; **inverse pair-production direction NOT computationally modeled** in parent.

### §4.3 — Computational proof chapter doesn't include photon→electron

[`Applied-Vacuum-Engineering/manuscript/vol_2_subatomic/chapters/09_computational_proof.tex:59`](../../../Applied-Vacuum-Engineering/manuscript/vol_2_subatomic/chapters/09_computational_proof.tex#L59):

> *"Topological Pair Production: exact 0 params"*

This appears as a FUTURE PREDICTION in the verification table, NOT a validated result.

### §4.4 — Spin-1/2 emergence from spin-1 photon NOT derived

The corpus asserts photon (spin-1) → electron (spin-1/2) at impedance saturation. The mechanism for HALF-spin emerging from integer-spin source is **not explicitly derived** in any parent manuscript chapter via grep. Per A-008 (in AVE-Core COLLABORATION_NOTES.md): the SO(3)/SU(2) double-cover mechanism IS the standard answer at substrate-medium level — but the parent doesn't computationally bridge "free photon traveling" to "Cosserat ω-field 4π closure on confined unknot."

### §4.5 — Honest finding

The corpus framework for photon-helical-confinement → electron-formation is **asserted in narrative/figure-caption form, NOT derived computationally**. The "spatial solver demonstrating" referenced in Vol 2 Ch 1 figure caption refers to a parametric visualization, not a real solver. The framework's flagship "0-parameter" claim for topological pair production is listed as future prediction, not validated result.

This is a substantive corpus-foundation finding: the L3 arc on AVE-Core has been hunting for the canonical electron eigenmode on K4-TLM substrate, but the corpus picture of HOW that eigenmode forms (photon condensation via impedance saturation) is itself unrun in the parent.

---

## §5 — Implications for L3 arc Round 14+

### §5.1 — Round 14 candidate (γ) sub-ℓ_node infrastructure: parent does NOT provide it

Doc 102 §7.4 + doc 103 §6 + doc 104 §8.10.6 named candidate (γ) "sub-ℓ_node infrastructure (spectral solver / mesh-refined K4-TLM) for sub-ℓ_node corpus-electron testing." Per §3 finding: parent's FDTD3DEngine is uniform-Yee-grid, no spectral, no AMR. NOT fit for sub-ℓ_node corpus-electron testing. Round 14 (γ) would require new infrastructure.

### §5.2 — Round 14 candidate (β) CoupledK4Cosserat coupling-channel: parent does NOT have analog

Per §3.4: parent's FDTD3DEngine doesn't model K4 sublattice topology, Cosserat torsion, Op14 coupling. The K4-Cosserat coupling channel that AVE-Core's CoupledK4Cosserat tries to capture (doc 103 §4.6) doesn't have a parent equivalent.

### §5.3 — The corpus claim itself is corpus-narrative, not corpus-validated

The L3 arc has been treating "corpus electron at K4-TLM substrate" as a corpus-canonical claim awaiting computational validation. Per §4 finding: the corpus claim is NARRATIVE + FIGURE CAPTION, with the underlying "spatial solver" being a parametric visualization. The corpus itself hasn't computationally established the photon-helical-confinement → electron-formation mechanism.

This doesn't FALSIFY the corpus claim — it just clarifies that the framework asserts the picture without yet computationally deriving it. Per Rule 11 + A47 v11b: not "🔴 corpus falsified" but "⏸ corpus picture asserted-not-derived; computational establishment is forward work."

### §5.4 — Auditor's prior critique re-anchored

The auditor's pass-4 noted *"the α derivation finding... is still open and doc 103 doesn't address it. Both derivation chains (parent's packing-fraction + AVE-Core's Vol 1 Ch 8) are SI substitutions per the prior audit."* This research extends the audit-level finding: the parent's photon-helical-confinement → electron-formation claim is also asserted-not-derived computationally. The corpus has multiple framework-level claims that are narrative + figure-caption, not solver-validated.

This is a meta-finding about the corpus's computational establishment, NOT a falsification of the framework's physical claims. Per Rule 15: this is manuscript-author-lane / corpus-author-lane material; implementer + auditor surface the finding.

---

## §6 — What this research does NOT do

- Does NOT claim the corpus's photon-→-electron picture is wrong (just unrun)
- Does NOT promote the K4 V_inc/V_ref Layer 3 test status from doc 104 §8.10.5 ⏸ to 🔴 (this finding extends the structural-context, doesn't falsify)
- Does NOT touch parent repo (read-only research)
- Does NOT modify AVE-Core production code
- Does NOT pre-register Round 14+ tests (still pending Grant adjudication on direction)
- Does NOT adjudicate whether the corpus framework's "0-parameter pair production" claim (Vol 2 Ch 9:59) is structurally defensible or substitution (manuscript-author lane)

---

## §7 — Forward direction questions for Grant

Per Rule 16 + Rule 15 lane discipline, this finding raises framework-level questions that are corpus-author-lane:

**Q1 — Does the corpus's photon-helical-confinement → electron-formation claim have a computational substrate elsewhere?**

Either (a) the parent has runnable infrastructure I missed in this research → I should re-grep with different search terms, OR (b) the picture has not been computationally established and the "spatial solver demonstrating" language in Vol 2 Ch 1:160 figure caption overstates current empirical status.

**Q2 — Does the L3 arc's hunt for "canonical electron at K4-TLM substrate" have well-defined corpus targets?**

Doc 92 §6 closed K4-at-ℓ_node-cannot-host-corpus-electron-at-corpus-scale per Nyquist. Doc 104 §8 confirmed via Round 13 (α) that canonical (V_inc, V_ref) quadrature IC at chair-ring also produces DC residual. The L3 arc's targets have been corpus-stated geometric values (R/r=φ², Vol 1 Ch 8 multipole sum), but per doc 100 §25 those bracket. If the corpus's photon→electron mechanism itself is asserted-not-derived, what are the well-defined corpus targets the L3 arc should be hunting?

**Q3 — Round 14 candidate selection given this finding:**

- (α') Characterize-engine's-natural-output (per doc 104 §8.10.6 corrected): doesn't depend on parent infrastructure or corpus-claim-validation status; honest forward physics. Implementer-lane.
- (β) CoupledK4Cosserat 4M× runaway: AVE-Core engineering, no parent dependency.
- (γ) Sub-ℓ_node infrastructure: NEW SOLVER work, parent doesn't provide it. Hours-to-days of new code.
- (δ) Framework reflection: this research extends the auditor's prior α-derivation finding into the photon→electron mechanism finding. Manuscript-author-lane.

Implementer-lane lean: (α') as immediate next move; (β) as Round 15+ if α' surfaces coupling-channel observables; (γ) as separate engineering arc if Grant prioritizes; (δ) as Grant-only.

---

— Doc 105 closure of parent FDTD + photon-helical-confinement research per Grant directive 2026-05-01 ("yes fully research"). Three substantive findings: (1) parent's "rifle photon" simulations are static visualizations not FDTD; (2) FDTD3DEngine is validated macroscopic propagator unfit for sub-ℓ_node testing; (3) corpus's photon-helical-confinement → electron-formation framework is asserted-not-derived computationally. Per Rule 11/12/14/15/16 + A43 v2 + A47 v10 + A47 v11b discipline: surfaces finding without retracting corpus picture; cleanest forward direction (α') Round 14 doesn't depend on this finding's adjudication.

---

## §8 — Auditor pass-5 verification + corrections to §4.3 (2026-05-01)

Auditor reviewed doc 105 same-day. Substantive verification of §2 / §3 / §4 findings via independent grep. Two corrections owed; per Rule 12 preserve-body, §1-§7 unchanged; corrections appended.

### §8.1 — Auditor verification confirmed

- **Vol 2 Ch 1:160 figure caption:** auditor read shows even more explicit label than I cited — *"(Simulation Output). A spatial solver demonstrating..."* The "(Simulation Output)" prefix explicitly labels the figure as solver output. Auditor verified verbatim. My §4.1 citation stands and is strengthened.
- **simulate_helical_confinement.py:** auditor confirmed parametric, not FDTD, at lines 32-50 (Z_profile = np.exp(0.4*z), R = 1.0/np.sqrt(Z_profile), x/y as parametric helix coordinates). My §2.1 stands.
- **FDTD3DEngine substrate-modeling absence:** auditor's grep returned 0 hits for K4/Cosserat/Op14/sublattice/torsion in fdtd_3d.py. My §3 stands.
- **17 importing files:** verified — mostly Vol 4 PONDER-01 ponderomotive thrust (macroscopic validation), not corpus-electron-related. My §3.4 stands.

### §8.2 — 🔴 CORRECTION to §4.3: "FUTURE prediction" framing was wrong

Auditor flagged my §4.3 "FUTURE prediction" framing for Vol 2 Ch 9:59 needed verification of column convention. Re-grep this turn surfaces Vol 2 Ch 9:55-65 verification table verbatim:

```
\begin{tabular}{lllrl}
\toprule
\textbf{Domain} & \textbf{Prediction} & \textbf{Regime} & \textbf{Agreement} & \textbf{Params} \\
\midrule
...
Superconductor $B_c(T)$ (5 materials) & $\sqrt{1-(T/T_c)^2}$ & II/III & exact & 0 \\
London depth ($\lambda_L$)    & 37--150 nm             & II/III & exact  & 0 \\
Seismic $\Gamma_{\text{Moho}}$ & 0.29                  & I     & matches PREM & 0 \\
GW lossless propagation       & $V_{GW}/V_{snap} = 10^{-28}$ & I & exact & 0 \\
Topological Pair Production   & $H_{net}=0 \to e^+ + e^-$    & IV    & exact & 0 \\
Protein folding (CLN025)      & RMSD = 2.59 \AA        & I     & sub-3 \AA & 0 \\
\bottomrule
```

**The table presents Topological Pair Production as VALIDATED**: Agreement column = "exact", Params column = "0", same format as actually-validated entries (Superconductor B_c with 5 materials, GW propagation, Protein folding). The Regime column shows "IV" for Topological Pair Production — but Regime IV is shown elsewhere in the table as a regime designator for validated entries (Galactic rotation NGC 3198 at "I/IV", Multi-galaxy RAR at "I-IV"). **No column convention or footnote distinguishes Regime IV as future-vs-validated within the verification table.**

The "Anomaly Catalog: Proposed Tests" section at line 91+ IS explicitly labeled future ("identified as targets for future AVE verification"), but Topological Pair Production is NOT in that future-tests section. It's in the Verification Summary table as a validated entry.

**My §4.3 framing "FUTURE PREDICTION ... NOT a validated result" was wrong.** The corpus rhetoric presents this as validated. The corrected reading is significantly stronger:

> **Vol 2 Ch 9:59 verification table presents Topological Pair Production as VALIDATED (Agreement="exact", Params=0), alongside actually-validated entries. But per §2 + §3 + §4.1 findings, the underlying script for the Vol 2 Ch 1 figure cited as "Simulation Output" is parametric visualization, not solver output. The corpus rhetoric presents it as validated; the computational basis is parametric visualization.**

This is corpus-rhetoric vs computational-reality gap, not just "asserted-not-derived." It composes with the auditor's prior pattern findings:

- Both α derivation chains are SI substitutions, not parameter-free derivations
- Theorem 3.1 dual-angle α⁻¹ "at machine precision" collapsed to tautology (per auditor pass-4)
- Test infrastructure (test_ch8_alpha_golden_torus.py) hardens patches via tautological regression assertions (per auditor catalog candidate)
- **Vol 2 Ch 1 photon-helical-confinement figure presents parametric visualization as "Simulation Output"; Vol 2 Ch 9 verification table presents the same picture as VALIDATED**

Per Rule 12 retraction-preserves-body: §4.3 body preserved verbatim above; this §8.2 supplies the corrected reading.

### §8.3 — Auditor's additional finding I missed: docstring overstates code

Auditor flagged simulate_helical_confinement.py docstring as overstating what code does. Verified verbatim this turn at line 2:

> *"Natively computes the spatial collapse of a linear EM wave into a stationary helical spin-1 topology strictly due to increasing local network impedance."*

But the code (per §2.1 + §8.1 verification) is parametric visualization (Z_profile = exp(0.4*z) + R = 1/sqrt(Z_profile) + parametric helix coordinates). It does NOT "natively compute the spatial collapse" — it draws a parametric curve. The docstring overstates.

This is an A47 v11d-style discipline issue: computation-claim-in-docstring must match what the code does. Auditor flags as catalog candidate (A47 v18 or similar — manuscript/script computation-rhetoric vs implementation-reality discipline). Catalog amendment is auditor-lane.

### §8.4 — Implications for the framework-level (δ) lane

The §8.2 corrected reading is significantly stronger than my original §4.3. The corpus's external rhetoric ("47 verified predictions, 0 free parameters" pattern, with Vol 2 Ch 9:55-65 Verification Summary table as the canonical anchor) presents Topological Pair Production as validated alongside actually-validated entries — but the underlying computational basis is parametric visualization, not solver output. The figure caption explicitly says "(Simulation Output)" while the figure is parametric.

If this same pattern (claimed validation that the codebase doesn't deliver) holds for OTHER entries in the same table — which the auditor's pattern-recognition flag suggests it might — the framework's external-credibility claims need recalibration at the corpus-author / manuscript-author lane.

This composes into the (δ) framework-reflection lane that doc 104 §8.10.6 + my §7 named as Grant-only. Per Rule 15 lane discipline: implementer + auditor surface; corpus-author adjudicates.

### §8.5 — Net status post-§8

- §1-§7 substantive content stands per auditor verification
- §4.3 specific "FUTURE prediction" framing 🔴 CORRECTED — actual reading is "validated rhetoric vs parametric-visualization computational basis"
- §8.3 docstring-overstates-code finding added (auditor catalog-candidate)
- §8.4 framework-rhetoric pattern strengthened — composes with prior audit findings into (δ)-lane reframe question

The Round 14 forward direction recommendations (α' / β / γ / δ) per §7 are unchanged. The corrected §4.3 reading sharpens the (δ) reflection but doesn't change the within-lane (α') / (β) / (γ) options.

— §8 closure of auditor pass-5 verification + §4.3 correction per Rule 12 preserve-body + A47 v11b substitution-not-retraction. Vol 2 Ch 9:55-65 verification table column structure verbatim-grepped this turn (auditor flag closed); docstring-overstates-code finding added. The §4.3 correction strengthens the framework-rhetoric vs computational-reality gap finding without changing the doc 105 substantive conclusions.
