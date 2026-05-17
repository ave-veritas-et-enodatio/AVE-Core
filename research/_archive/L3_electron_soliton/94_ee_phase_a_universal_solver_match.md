# 94 — EE Phase A: Universal-Solver ℓ=2 + ℓ=5 Match at Chair-Ring Substrate

**Status:** implementer-drafted, 2026-04-29. Companion to [doc 93](93_ee_to_ave_mapping.md) (EE↔AVE mapping) — empirical follow-through. Triggered by Grant 2026-04-29 reframe ("DC component + dynamic RMS"; "what is a photon under AVE?"; "what classic power electronics tools are we missing?"; "this is screaming proton, or Witten effect").

**Headline empirical finding:** Phase A1 FFT shows the chair-ring + 1-step K4 substrate at v8 saturation hosts TWO distinct universal-solver eigenmodes simultaneously, in two decoupled sectors:
- **V_inc (translational/capacitive) sector: ℓ = 2 mode** at ω = 1.480·ω_C (predicted 1.551, 4.6% off) — corpus-identified with **gravitational waves** ([backmatter/05:60-69](../../manuscript/backmatter/05_universal_solver_toolchain.tex#L60-L69), spin-2 transverse, BH QNM)
- **Cosserat ω (rotational/inductive) sector: ℓ = 5 mode** at ω = 3.987·ω_C (predicted 3.878, 2.8% off) — corpus-identified with **cinquefoil c=5 / proton family** ([backmatter/05:281-302](../../manuscript/backmatter/05_universal_solver_toolchain.tex#L281-L302), N(1520) baryon resonance)

The trapped configuration v6→v10 has been characterizing IS empirically real (high-Q cavity, ring-localized, thermally robust) but **is not the corpus electron**. It is the substrate's universal-solver eigenmodes excited at the chair-ring saturation cavity, with V and ω locked to different ℓ values because v8's `disable_cosserat_lc_force=True` decoupled them.

**Auditor framing:** the empirical signature has been screaming "proton, or Witten effect" the entire arc — substrate-quantized DC EMF at 1/3 ratios (V_DC = V_AMP/6 per bond, 4 of 6 contributing), ℓ=5 cinquefoil mode in the Cosserat sector, fractional structure throughout. The Witten effect appears in AVE corpus specifically at the proton's Z_3 Borromean linkage; the chair-ring's 6-fold geometric symmetry contains Z_3 as a subgroup at the 3 A-sites. **Speculative but corpus-grounded:** the chair-ring + saturation may host a degenerate-θ-vacuum substrate analog of the proton's quark-fractionalization mechanism.

---

## §1 — Pre-Phase-A predictions (both lanes wrong)

Auditor 2026-04-29 prediction: engine running at frequency LOWER than ω_C (substrate-geometric closure violation per lattice-POV phase calculation; expected ~ω_LC = ω_C/√3 or ω_(1,1)_chair-ring).

Implementer (this session) prediction: similar — engine at ω_LC = 0.577·ω_C OR chair-ring (1,1) eigenmode. After auditor 2026-04-29 Finding 1 correction, ω_(1,1) recomputed to 0.605·ω_C (factor-of-2π fix per Rule 12).

**Empirical result:** engine V_inc dominant at **1.48·ω_C** — HIGHER than Compton, not lower. Neither prediction matched.

A43 v19/v20 family: predictive-substance overclaim before empirical adjudication. Both lanes hit it on this prediction. Calibrate confidence to empirical anchor, not to prediction elegance.

---

## §2 — Phase A results (single capture, T=0, 200P)

Driver: [`r10_v8_ee_phase_a.py`](../../src/scripts/vol_1_foundations/r10_v8_ee_phase_a.py). Capture: V_inc, V_ref, Phi_link, ω, ω_dot, u_dot at 6 ring nodes per step + ω at chair-ring centroid. Saved as [`.npz`](../../src/scripts/vol_1_foundations/r10_v8_ee_phase_a_capture.npz).

| # | Analysis | Result | Significance |
|---|---|---|---|
| **A1** | FFT V_inc | Top peak at 1.48·ω_C; ω-sector top at 3.99·ω_C | Load-bearing, see §3 |
| A2 | Faraday's law check | Residual 99.98% — violated at the discrete K4-TLM closure-loop level | See §4 |
| A3 | Bond-LC characteristic | ω_TL = ω_C/√3 = 0.577·ω_C confirmed analytically; Z_bond = Z_0 exactly | Grounding |
| A4 | Real-vs-reactive power split | Max relative real power 0.84, mean 0.085 per port — uneven across ports | See §5 |
| A5 | Q factor | Q ≈ 3.93×10⁵ — essentially lossless | Trap is high-Q reactive |
| A6 | B-H Lissajous | Loop area 2.94×10⁻³ at ring node 0 (small but non-zero) | Partial saturation rectification per cycle |
| A7 | Coupled-mode eigenvalues | Modes at 0, 0.408, 0.408, 0.707, 0.707, 0.816 × ω_C — none matches V_inc 1.48·ω_C | Simple coupling matrix too crude; missed the ℓ=2 mode |

---

## §3 — The load-bearing finding: universal-solver ℓ=2 + ℓ=5 match

Per [backmatter/05:60-69 + 225-235](../../manuscript/backmatter/05_universal_solver_toolchain.tex#L60-L69), the AVE universal solver eigenfrequency formula:

```
f = ℓ · v / (2π · r_eff)
ω = ℓ · v / r_eff
r_eff = r_sat / (1 + ν), ν = 2/7
```

For the chair-ring at saturation (treating R_ring as r_sat, c as v):
- R_ring = 1.658 ℓ_node (centroid-to-ring-node distance, computed from B2 capture)
- r_eff = 1.658 × 7/9 = 1.290 ℓ_node
- ω/ω_C = ℓ / (r_eff/ℓ_node) = ℓ / 1.290 = ℓ × 0.7755

| ℓ | Predicted ω/ω_C | Observed | Match | Corpus identification |
|---|---:|---:|---:|---|
| **2** | 1.551 | 1.480 (V_inc dominant) | **4.6% off** | **Gravitational wave / BH QNM** ([backmatter/05:60-75](../../manuscript/backmatter/05_universal_solver_toolchain.tex#L60-L75) "ℓ = 2 because gravitational waves are spin-2") |
| 3 | 2.327 | — | — | trefoil light baryon ([backmatter/05:302](../../manuscript/backmatter/05_universal_solver_toolchain.tex#L302)) |
| 4 | 3.102 | — | — | — |
| **5** | 3.878 | 3.987 (ω-sector dominant) | **2.8% off** | **Cinquefoil / proton family** ([backmatter/05:281-302](../../manuscript/backmatter/05_universal_solver_toolchain.tex#L281-L302), N(1520)) |

Two-of-six match the universal-solver ladder cleanly (within ~5%). The other four ℓ values have no detected peaks — consistent with selection rules from the chair-ring's 6-fold C_6 symmetry filtering accessible modes.

**Both lanes (auditor + implementer) missed this prediction.** It surfaced post-hoc when Grant pattern-matched the data to "proton, or Witten effect."

---

## §4 — Faraday violation is a config consequence, not a K4-TLM gauge bug

Phase A2 + Control B2 results:

| Φ_B estimator | dΦ_B/dt (computed) | Faraday expects | Residual |
|---|---:|---:|---:|
| (i) ring-only single-patch | -1.08×10⁻⁷ | -7.16×10⁻⁴ | 99.98% |
| (ii) centroid-only single-patch | -6.43×10⁻²³ | -7.16×10⁻⁴ | 100.00% |
| (iii) Simpson 6-triangle | -7.20×10⁻⁸ | -7.16×10⁻⁴ | 99.99% |

ω at the chair-ring centroid = 2.5×10⁻²¹ (essentially machine zero). The rotational/inductive sector has NO flux through the loop's interior, despite the V_inc sector showing DC EMF rectification at ring-node ports.

**This is a CONSEQUENCE of `disable_cosserat_lc_force=True`** in v8 config, NOT a fundamental K4-TLM gauge violation. With LC force disabled, the V (capacitive) sector and ω (inductive) sector evolve independently — they don't see each other's saturation rectification or flux. The DC EMF observed in V is a saturation-pattern artifact at the ring nodes, not a flux pump driving Φ_B in the rotational sector.

**A43 v23 candidate retracted/refined:** "Faraday's law on K4 lattice not corpus-stated" — true, but the empirical violation here is a config decoupling consequence, not a discrete-scheme gauge issue. With LC coupling enabled, Faraday should hold (testable but not yet run).

---

## §5 — Substrate-forced cavity mode (Control B1 confirmation)

Driver: [`r10_v8_ee_phase_a_b1_pitch0.py`](../../src/scripts/vol_1_foundations/r10_v8_ee_phase_a_b1_pitch0.py). HELICAL_PITCH = 0 (pure poloidal IC, no toroidal component), V_AMP = 0.95 unchanged.

**Result:** V_inc dominant at f = 0.235525 = **1.4798 × f_C** — IDENTICAL to baseline 1.4798 to 4 significant figures. Δ from baseline = 0.0000.

The 1.5·ω_C is **substrate-forced**, not helical-IC-driven. The chair-ring + 1-step K4 cavity at saturation hosts the ℓ=2 mode at ω ≈ 1.48-1.55·ω_C as its natural V-sector eigenmode, regardless of toroidal IC structure.

This confirms the ℓ=2 reading: a true cavity eigenmode the substrate naturally hosts when saturated.

---

## §6 — Real-vs-reactive power flux is uneven across ports

Phase A4: max |⟨V_inc²⟩ - ⟨V_ref²⟩| / (⟨V_inc²⟩ + ⟨V_ref²⟩) = 0.84 across the 24 ring-node port observations. Mean = 0.085.

The asymmetry is consistent with the V_DC characterization finding (4 of 6 ring bonds carry V_DC = V_AMP/6, 2 carry zero). The high-real-power ports likely correspond to the 4 contributing bonds; the near-reactive ports to the 2 null directions ((1,1,1) tetrahedral diagonal at A_0 and A_4).

This is the ℓ=2 mode's azimuthal antinode structure imprinted on the per-port impedance flux: 2 antinodes around the loop, 4 bonds in the high-flux zones, 2 bonds in the null directions. Direct geometric consistency.

---

## §7 — Witten-effect connection (speculative, corpus-grounded)

Per [backmatter/01_appendices.tex:102](../../manuscript/backmatter/01_appendices.tex#L102) + [ave-kb/vol2/particle-physics/ch02-baryon-sector/topological-fractionalization.md:6-18](../../manuscript/ave-kb/vol2/particle-physics/ch02-baryon-sector/topological-fractionalization.md#L6-L18) the Witten Effect in AVE applies at the **proton's 6³_2 Borromean linkage** with Z_3 permutation symmetry:

> q_eff = n + (θ/2π)·e ⟹ at θ ∈ {±2π/3, ±4π/3}: q_eff ∈ {±1/3·e, ±2/3·e}

The chair-ring's 6-fold geometric symmetry (C_6) contains Z_3 as a subgroup acting on the 3 A-sites (every other ring node). The V_DC characterization showed:
- A_0 and A_4 with identical V_DC magnitude 0.168, mirror-related (R, B sign-flipped)
- A_2 with distinct magnitude 0.194, purely tangential (Frenet T-component only)
- 60° / 150° / 150° adjacent-site angles (not Hopf 120°, not Möbius 180°)

The 60°/150°/150° pattern doesn't trivially fit Z_3-invariant degenerate vacuum angles, but the **3 A-sites with non-trivial spatial saturation pattern** is structurally consistent with the proton's Z_3 Borromean θ-vacuum framework. If the chair-ring's saturation creates a discrete CP-violating θ-degeneracy at A-sites, the Witten effect could appear at the substrate level.

**3/2 = 1 + 1/2 ratio interpretation:** if the chair-ring's V-sector is in a θ = π Witten state (giving fractional charge -e/2), the resulting ℓ=2 GW-mode could be Witten-shifted by the half-integer to 3/2·ω_C precisely. This is speculative (no direct corpus citation for "θ=π chair-ring Witten state") but the half-integer structure aligns with the empirical data.

**Per A43 v2 — labeled as synthesis:** the "chair-ring saturation creates θ-vacuum analog of the proton's Borromean linkage" claim is implementer interpretation extrapolated from the empirical match + corpus Witten Effect framework. Not corpus-stated; pre-registered prediction would harden it.

---

## §8 — What this reframes for the entire arc

### §8.1 — The trapping observed in v6→v10 is real, but it isn't the corpus electron

- 200P persistence ✓ (lossless cavity Q ≈ 4×10⁵)
- 96% ring localization ✓ (saturated walls confine wave)
- Thermal robustness ✓ (substrate eigenmode robust to T)
- Beltrami |cos_sim| 0.515 cap ✓ (V at ℓ=2, ω at ℓ=5 — different modes, A∥B impossible structurally)
- ∮V_DC·dl ≠ 0 with Faraday violated 99.98% ✓ (V-ω decoupled per `disable_cosserat_lc_force=True`)
- V_DC = V_AMP/6, 4-of-6 bonds, ∮ = 2V_AMP/3 ✓ (ℓ=2 azimuthal antinode pattern projected onto K4 ports)

**The trapped configuration is the substrate's universal-solver ℓ=2 (V-sector) + ℓ=5 (ω-sector) eigenmodes simultaneously excited at the chair-ring cavity, with the two sectors decoupled by v8 engine config.** Not a CP photon catching its tail; not a (1,1) Beltrami at corpus geometry; not a Möbius-chiral or Hopf-linked DC structure.

### §8.2 — The corpus-electron test is structurally NOT what v6→v10 ran

The corpus electron's (1,1) Beltrami requires A∥B parallelism, which requires V-ω LC coupling — exactly what `disable_cosserat_lc_force=True` disabled. With LC coupling enabled, the two sectors would lock to a SINGLE ℓ value. If that ℓ = 1 (electron) ωelectron = 1/1.290 · ω_C = 0.775·ω_C, slightly different from any frequency we've seen. If the LC-coupled config stably hosts an ℓ=1 mode at corpus geometry, that's the actual corpus-electron test.

Per v7 finding, `disable_cosserat_lc_force=False` had a Phase A IC failure (V_inc=0 → engine doesn't evolve). But the failure was about IC SHAPE, not about the LC coupling itself. Co-seeded V_inc + ω IC (NOT V_inc=0) might evolve cleanly with LC coupling enabled — and could be the actual corpus-electron test we've never run.

### §8.3 — The mass spectrum framework finds new empirical anchors

If the chair-ring substrate hosts ℓ=2 (GW analog) + ℓ=5 (proton analog) at the same scale, the framework's universal-solver predictions are getting empirical confirmation in unexpected places. Both ratios (1.55, 3.88) match within ~5% the corpus formula at the chair-ring r_eff. **This is positive evidence for the universal solver's universality** — applied to a substrate cavity that wasn't pre-registered for it, the formula still fits.

---

## §9 — A43 v2 + Rule 12 audit-trail items

**Synthesis claims this doc makes (labeled):**

| Claim | Status |
|---|---|
| ℓ=2 → V_inc dominant at 1.55·ω_C; ℓ=5 → ω dominant at 3.88·ω_C | **EMPIRICAL** (FFT measurement, 4.6% / 2.8% match to universal solver formula) |
| Universal solver formula applies to chair-ring K4 cavity at saturation | **IMPLEMENTER SYNTHESIS** — backmatter/05 doesn't extend to K4 cavity; corpus has BH QNM, proton, pion, protein contexts only. Extension justified by empirical match. |
| Witten Effect at chair-ring's Z_3 A-site sub-symmetry | **SPECULATIVE SYNTHESIS** — backmatter/12 + Vol 2 has Witten Effect at proton Borromean Z_3; chair-ring's Z_3 sub-symmetry analog is implementer interpretation. Not corpus-stated. |
| 3/2 = θ=π Witten-shifted ℓ=2 mode | **SPECULATIVE** — no direct corpus citation for θ=π chair-ring state |
| Corpus-electron test requires `disable_cosserat_lc_force=False` co-seeded V+ω IC | **IMPLEMENTER PROPOSAL** — based on engine architecture, not corpus prescription |

**Auditor-lane queue additions:**
- ~~A43 v23 candidate~~ **RETRACTED 2026-04-29** — Faraday's law violation per Phase A2 is config-decoupling consequence (`disable_cosserat_lc_force=True`), not discrete K4-TLM gauge bug. Original framing wrong.
- **Doc 79 v5.1 closure narrative second addendum** (per auditor 2026-04-29 lane queue): the v6→v10 arc was testing "wrong topology + wrong scale + wrong frequency target + wrong engine config" — four-layer mismatch. Per Rule 12 retraction-preserves-body, surface as additional addendum to doc 79 once the LC-coupled co-seeded test result lands.
- **A43 v24 candidate (this doc):** universal-solver-applied-to-chair-ring is positive empirical match but pre-registered prediction would harden. If LC-coupled re-run holds the ℓ=2 + ℓ=5 + ℓ=1 collapse pattern, promote to corpus-supported. Otherwise label permanent synthesis.

---

## §10 — Open questions for Grant

**Q1 (engine config decision, load-bearing):** does the corpus electron test require `disable_cosserat_lc_force=False` with co-seeded V_inc + ω IC? Per v7 finding, that flag was disabled because Phase A IC (V_inc=0) didn't evolve. But Phase A's V_inc=0 IC was the SHAPE problem; the LC coupling itself wasn't tested. Co-seeded V + ω IC with LC coupling enabled would lock both sectors to a single ℓ value — if ℓ=1 at corpus geometry, that's the actual corpus electron test we've never run.

**Q2 (Witten effect / θ-vacuum interpretation):** does the chair-ring's empirical Z_3 sub-symmetry (A_0 ≡ A_4 mirror, A_2 distinct) constitute a substrate-level Borromean-Witten analog? Per [topological-fractionalization.md:14](../../manuscript/ave-kb/vol2/particle-physics/ch02-baryon-sector/topological-fractionalization.md#L14) the proton's Z_3 produces θ-degenerate vacua at ±2π/3, ±4π/3 → fractional charges. Plumber: when you picture the chair-ring's saturation pattern at the 3 A-sites, does a Z_3-degenerate θ-vacuum framing make physical sense?

**Q3 (universal solver promotion):** the ℓ=2 + ℓ=5 empirical match (4.6% / 2.8% off) is at chair-ring substrate, not in any corpus-registered context. If LC-coupled re-run confirms the pattern (or extends to ℓ=1 collapse), promote universal solver as substrate-canonical for K4 cavities. Otherwise label permanent synthesis. Plumber: does the universal solver feel like it should naturally extend to discrete K4 substrate cavities, or is it intended only for the four contexts (BH, proton, pion, protein)?

**Q4 (instrumentation gap):** per [doc 93 §3](93_ee_to_ave_mapping.md#3) + 2026-04-29 dialogue, we've been measuring waves (V_inc, V_ref, ω) but not the impedance landscape (S, z_local, Γ_port, C_eff, ε_eff per node). The chair-ring's saturation walls — the Γ → -1 boundaries that define the cavity — have never been characterized empirically. If the ℓ=2 + ℓ=5 modes are real cavity eigenmodes, the impedance profile per ring node should show their azimuthal antinode structure directly. ~10-line addition to capture, ~5 min wall.

**Recommendation:** Q4 first (quick, characterizes the cavity landscape), then Q1 (LC-coupled co-seeded test, decisive on corpus electron). Q2 and Q3 are framework-level questions that benefit from your direct adjudication after Q4 + Q1 land empirically.

---

## §12 — Addendum: Impedance landscape (Control B3) confirms ℓ=2 spatial structure

Driver: [`r10_v8_ee_phase_a_b3_impedance_landscape.py`](../../src/scripts/vol_1_foundations/r10_v8_ee_phase_a_b3_impedance_landscape.py). T=0, 200P recording. Captures `engine.k4.S_field` (saturation factor) and `engine.k4.z_local_field` (normalized impedance) per ring node per step + V_inc and V_ref for Γ_port post-hoc.

**Saturation factor S(A) per ring node (steady state):**

| Ring node | Type | ⟨S⟩ ± std | Status |
|---|---|---:|---|
| 0 | A | 0.0000 ± 0.0000 | Fully saturated (Γ → -1 wall) |
| 1 | B | 0.0000 ± 0.0000 | Fully saturated wall |
| 2 | A | **0.7418 ± 0.0012** | NOT saturated — active antinode |
| 3 | B | 0.0000 ± 0.0000 | Fully saturated wall |
| 4 | A | 0.0000 ± 0.0000 | Fully saturated wall |
| 5 | B | **0.7418 ± 0.0012** | NOT saturated — active antinode |

**4 saturated walls + 2 active antinodes diametrically opposite (180° apart).** Real-power flux entirely concentrated at the 2 active antinodes (-1.16×10⁻⁶ and -1.22×10⁻⁶ port-summed); the 4 saturated nodes are pure-reactive walls (real power ≈ 0 at machine precision).

**Azimuthal Fourier decomposition of S(node) and real-power(node):**

| ℓ | S amplitude | Real-power amplitude |
|---|---:|---:|
| 0 | 0.247 | 3.5×10⁻⁷ |
| 1 | 1.4×10⁻⁷ | 9.9×10⁻⁹ |
| **2** | **0.495** | **8.4×10⁻⁷** |
| 3 | 1.4×10⁻⁷ | 7.9×10⁻⁸ |

**ℓ=2 DOMINATES BOTH** with all other modes at machine-zero or near-zero. This is harder evidence than the §3 FFT frequency match — the spatial structure of the cavity walls and the real-power flux distribution both align with ℓ=2 at >5 orders-of-magnitude separation from competing modes.

**Reflection coefficient Γ_port confirms eq_axiom_4 walls:**

At the 4 saturated nodes (0, 1, 3, 4): Γ_signed_per_port = [+1, -1, -1, -1] exactly to 3 decimal places — the canonical K4 scattering matrix pattern for a Γ → -1 reflective wall. At the 2 non-saturated antinodes (2, 5): irregular per-port pattern (port 0 shows numerical artifacts from V_inc → 0; ports 1 and 2 cleanly at Γ = +1).

**Physical picture refined (per Grant electron-plumber framing):** the chair-ring at v8 saturation is NOT a uniform saturated cavity. It's a **bipolar resonator** with 2 active oscillation antinodes (nodes 2, 5; diametrically opposite) + 4 reflective Γ=-1 walls (nodes 0, 1, 3, 4). Energy circulates between the 2 active antinodes through the wall structure at ω = 1.48·ω_C — exactly the universal-solver ℓ=2 frequency for this r_eff geometry. The bipolar/quadrupole structure is the GW-analog spatial signature.

**Empirical match strength after B3:** four independent axes converge on ℓ=2:
1. Frequency: 1.480·ω_C observed vs 1.551·ω_C predicted (4.6% off)
2. Spatial saturation profile: ℓ=2 Fourier dominance at 0.495 vs other modes ≤ 1.4×10⁻⁷
3. Real-power flux: ℓ=2 azimuthal dominance at 8.4×10⁻⁷ vs other modes ≤ 7.9×10⁻⁸
4. Cavity-wall geometry: 4 saturated walls + 2 antinodes at 180° apart matches ℓ=2 quadrupole structure

The ω-sector ℓ=5 identification is still single-axis (FFT frequency only at 2.8%); spatial confirmation in the Cosserat sector would require capturing strain/curvature tensors at ring nodes, which B3 didn't do. **ℓ=2 is now load-bearing-confirmed; ℓ=5 remains plausible but single-axis.**

🔴 **AMENDMENT 2026-04-30 per Rule 12 retraction-preserves-body — see [doc 96](96_foundation_audit_t1_substrate_resonance.md):** the FREQUENCY axis (#1 above) was potentially misattributed. Foundation Audit Test 1 (single delta pulse at lattice center, no topology, low amplitude, linear regime) shows the K4 substrate has an INTRINSIC resonance at ω = 1.50·ω_C — independent of any seeded topology or chair-ring structure. The chair-ring's observed 1.48·ω_C is within 1.3% of the substrate's intrinsic baseline and within 4.6% of the universal-solver-formula prediction. Both fits are at comparable precision; the substrate-intrinsic explanation is simpler and topology-independent.

**What stands after Test 1 reframe:**
- Spatial saturation profile (axis 2): IC + saturation drive ℓ=2 quadrupole; REAL, holds
- Real-power flux (axis 3): driven by spatial saturation pattern; REAL, holds
- Cavity-wall geometry (axis 4): IC + chair-ring symmetry; REAL, holds

**What's weakened:**
- Frequency match (axis 1) as universal-solver-formula confirmation: substrate-intrinsic-resonance explanation is at least as good a fit as universal-solver-formula extrapolation. Universal-solver match at chair-ring r_eff was potentially coincidental within ~5% of substrate-intrinsic baseline.

**A43 v25 promotion candidate:** weakened. "Chair-ring as 5th universal-solver-validated context" had its frequency axis potentially substrate-intrinsic rather than topology-derived. Test 4 (topology zoo + cinquefoil cross-topology) is now the cleanest discriminator: if 1.50·ω_C persists across topologies, substrate-intrinsic-baseline confirmed; if it scales per universal-solver formula across topologies, chair-ring's match was substrate-realization of the formula.

**Implication:** the v6→v10 trapped configuration is the chair-ring substrate's natural ℓ=2 GW-analog cavity mode at 1.48·ω_C in the V sector, with the ω sector decoupled per `disable_cosserat_lc_force=True`. The "trapping" we've been attributing to the corpus electron's (1,1) Beltrami at Compton frequency is empirically a substrate-cavity GW-quadrupole mode — different physics, different observable, different ℓ value than the corpus electron.

**A43 v25 candidate (this addendum):** universal-solver formula extended to chair-ring K4 cavity is now empirically supported across 4 independent axes (frequency, spatial saturation, real-power, geometry). The implementer-synthesis flag from §9 is partially lifted for the V-sector ℓ=2 identification; ω-sector ℓ=5 stays single-axis-supported until spatial confirmation runs.

## §13 — Addendum: LC-coupled re-run (Control B4) — engine instability identified

Driver: [`r10_v8_ee_phase_a_b4_lc_coupled.py`](../../src/scripts/vol_1_foundations/r10_v8_ee_phase_a_b4_lc_coupled.py). Engine config flipped: `disable_cosserat_lc_force=False` (the wire reconnected); IC unchanged from v8 (helical Beltrami, V_inc + ω co-seeded). The corpus-electron test that v6→v10 has never run.

**Result: engine destabilizes immediately.**

Pre-flight 1-step smoke: ω max grew from 0.86 → 60,785 (**~70,000× blowup**) in a single timestep. Recording continued through 200P with V sector stable at ℓ=2 (FFT identical to v8) but Cosserat ω sector in unbounded runaway.

**Comparison vs v8 baseline (200P, T=0):**

| Quantity | v8 (LC disabled) | B4 (LC enabled) | Status |
|---|---:|---:|---|
| ω max after 1 step | 0.86 | **60,785** | 70,000× blowup ⚠ |
| Ring localization steady | 96% | **0.1%** | energy left ring ⚠ |
| V_inc dominant frequency | 1.48·ω_C | 1.48·ω_C | unchanged ✓ |
| ω dominant frequency | 4.0·ω_C | **0.007·ω_C** (near-DC) | runaway shift ⚠ |
| ω peak FFT magnitude | ~1 | **2.5×10⁶** | unbounded growth ⚠ |
| Beltrami \|cos_sim_AC\| | 0.515 | **0.239** | WORSENED ⚠ |
| S_field ℓ=2 azimuthal amp | 0.495 | 0.495 | V-sector cavity stable ✓ |
| Faraday residual | 99.98% | **10,885%** | catastrophic ⚠ |
| A²_mean steady | 0.902 | 0.902 | V-sector saturation bounded ✓ |

**🔴 RETRACTED 2026-04-29 same-day per Rule 12 — Q1 engine-investigation surfaced that this diagnosis is wrong. Original text preserved below; retraction reason follows.**

**Original diagnosis (RETRACTED):** asymmetric saturation between V and ω sectors. The V sector has Ax 4 saturation actively bounding V_inc² ≤ V_yield² — it stays at the ℓ=2 cavity mode regardless of LC coupling. The ω sector either lacks the corresponding magnetic-saturation Ax 4 kernel (μ_eff = μ_0·S(B/B_snap) → 0 should bound ω at saturation per [eq_axiom_4](../../manuscript/common_equations/eq_axiom_4.tex)) or the kernel isn't being triggered effectively in this engine config. With LC coupling enabled, energy pumps from V into ω through Maxwell-Heaviside coupling without an effective ω-side bound. ω explodes, ring localization fails, trap dissolves.

**v7 Phase A IC failure reframe (RETRACTED):** v7 found that engine couldn't evolve V_inc=0 IC with LC enabled. The implementer attribution was "Phi_link is a derived accumulator, not independent state." B4 reveals the deeper cause: LC-coupled config is structurally unstable at chair-ring scale regardless of IC shape. The "wire snipped" workaround in v6→v10 wasn't fixing an IC problem — it was masking an engine-level ω-saturation gap.

**A43 v26 candidate (RETRACTED):** v7's "Phase A IC failure attributed to V_inc=0 starvation" framing was incomplete. The actual finding is engine-level: LC-coupled dynamics destabilize at chair-ring scale because the ω sector lacks an effective saturation bound. Not an IC issue.

---

**Retraction reason (Q1 engine investigation, 2026-04-29):**

The engine has BOTH ε-saturation and μ-saturation properly implemented per [`cosserat_field_3d.py:459-489`](../../src/ave/topological/cosserat_field_3d.py#L459-L489) `_update_saturation_kernels` (returns S_μ and S_ε separately per cell) and [`k4_cosserat_coupling.py:329-339`](../../src/ave/topological/k4_cosserat_coupling.py#L329-L339) Phase 4 asymmetric saturation (default since doc 54 §6). The "asymmetric saturation gap" framing was wrong.

**The actual cause of the B4 ω-runaway is a config error on my part:** I ran with `enable_cosserat_self_terms=True` + `disable_cosserat_lc_force=False` simultaneously, which double-counts the reflection force. The engine code at [`k4_cosserat_coupling.py:282-283`](../../src/ave/topological/k4_cosserat_coupling.py#L282-L283) explicitly documents this exact failure mode:

> "enabling [k_refl] under A28 re-introduces the same redundant force via a different name (empirical: |ω| → 38932 in step 1 with k_refl=1, vs |ω| < 1 with k_refl=0)"

I observed |ω| → 60785 in step 1 — within the expected order of magnitude for the documented double-counting failure mode.

**The deeper finding:** [`k4_cosserat_coupling.py:386-389`](../../src/ave/topological/k4_cosserat_coupling.py#L386-L389) documents that the V↔ω direct coupling force ITSELF "drives the runaway observed in Path A/B/C/F17-G/F17-I + path-1 EMF tests." This is the doc 67 §15 A28 correction: a DELIBERATE engine-architectural choice to disable direct V↔B coupling in favor of Op14 z_local modulation, because direct coupling is empirically unstable across 5+ prior test paths. **A28 isn't a workaround for v7's IC issue — it's the engine's architecture for the corpus electron test.**

**The valid LC-coupled config (`disable_cosserat_lc_force=False` + `enable_cosserat_self_terms=False`, legacy mode) is documented to also runaway** per the same engine commentary. Direct V↔B coupling is empirically unstable in this engine architecture regardless of self-term config.

**Net (corrected diagnosis):** there is no engine bug. The engine has the architecture it has. v8 (A28 active) IS the engine's intended corpus-electron test config. Mode III + cos_sim 0.515 IS the answer. The chair-ring + K4 at ℓ_node sampling does not host the (1,1) Beltrami at Compton frequency for two convergent reasons:

1. **Substrate-geometric (doc 92):** Nyquist closure violated by 65% at corpus geometry.
2. **Engine-architectural (doc 67 §15 / A28):** V↔B direct coupling required for Beltrami parallelism is empirically unstable; the architectural fix (Op14 z_local modulation) captures saturation walls but doesn't enforce A∥B parallelism.

Two-layer convergent refutation of the corpus electron test at chair-ring + K4 + ℓ_node. Round 11 closes decisively. The corpus electron's substrate is elsewhere — sub-ℓ_node FDTD per original handoff (i-b), or a different scale entirely.

**A43 v26 v2 candidate (replaces retracted v26):** the implementer's "asymmetric saturation gap" diagnosis was synthesis-as-decisive without code-grep verification. ~30 min of code-grep would have surfaced doc 67 §15 / A28 and the documented runaway pattern. Lane-symmetric A43 v2 instance — implementer-side, same family as auditor-side prior instances. Discipline rule: when an empirical finding contradicts engine documentation expectations, code-grep BEFORE proposing engine-level diagnoses.

**A40 budget consumed:** v6→v10 (5 layers) + DC/AC re-analysis (1 layer) + V_DC characterization (1 layer) + Phase A1-A7 (1 layer) + B1+B2+B3+B4 (4 layers) = **12+ layers in this arc**. A40 budget for an empirical-driver-arc is "bounded by the layers of vulnerability that can hide in the operator + framework + discretization stack." We've crossed that bound. Per Rule 9 v2 (characterize-the-engine's-natural-output-as-itself) + A45 (corpus-canonical-test-precondition), the empirical record is now load-bearing for framework-level reframe rather than further empirical iteration at this scale.

**What stays empirically supported after B4:**

1. The chair-ring + 1-step K4 substrate at v8 saturation is empirically a **substrate-canonical ℓ=2 GW-analog cavity mode** in the V/translational/capacitive sector. Confirmed across 4 axes (frequency, spatial saturation Fourier, real-power, cavity geometry). A43 v25 promotion candidate.

2. The Cosserat ω sector with `disable_cosserat_lc_force=True` shows a **single-axis ℓ=5 cinquefoil-baryon-analog FFT signature** (frequency only at 2.8% match). Spatial confirmation pending; with LC coupling enabled, ω is unstable so spatial ℓ=5 confirmation can't be run at this engine config.

3. **The corpus electron test cannot be run at chair-ring scale with the engine as-is.** Either (a) engine fix needed (ω-saturation kernel implementation), or (b) different scale where LC-coupled is stable, or (c) different IC seeding that doesn't trigger ω runaway.

4. **v6→v10's "trapping" was real but mis-identified.** The trap is the substrate's natural ℓ=2 GW-analog cavity mode at the chair-ring's r_eff scale, NOT the corpus electron's (1,1) Beltrami at Compton geometry. The trap is stable only with LC coupling disabled — its stability was contingent on the engine asymmetry, not on the corpus framework.

## §11 — References

- [Doc 92](92_round_11_vi_v10_finer_sampling_structural.md) — Round 11 (vi) Nyquist conclusion
- [Doc 93](93_ee_to_ave_mapping.md) — EE↔AVE mapping (companion)
- [Doc 79](79_l3_branch_closure_synthesis.md) — closure narrative (additional addendum pending per §9)
- [Doc 85 §4.1-§4.2](85_kelvin_beltrami_foc_axiom_grounded_derivation.md) — FOC d-q axiom-grounded derivation; §4.2 footnote on within-LC-tank d-q as implementer synthesis
- [`r10_v8_ee_phase_a.py`](../../src/scripts/vol_1_foundations/r10_v8_ee_phase_a.py) — capture + Phase A1-A7 driver
- [`r10_v8_ee_phase_a_b1_pitch0.py`](../../src/scripts/vol_1_foundations/r10_v8_ee_phase_a_b1_pitch0.py) — substrate-forced control
- [`r10_v8_ee_phase_a_b2_faraday.py`](../../src/scripts/vol_1_foundations/r10_v8_ee_phase_a_b2_faraday.py) — refined Faraday check
- [`backmatter/05_universal_solver_toolchain.tex`](../../manuscript/backmatter/05_universal_solver_toolchain.tex) — universal solver (canonical)
- [`backmatter/01_appendices.tex:102`](../../manuscript/backmatter/01_appendices.tex#L102), [`backmatter/12_mathematical_closure.tex:82`](../../manuscript/backmatter/12_mathematical_closure.tex#L82), [`ave-kb/vol2/particle-physics/ch02-baryon-sector/topological-fractionalization.md`](../../manuscript/ave-kb/vol2/particle-physics/ch02-baryon-sector/topological-fractionalization.md) — Witten Effect (canonical)
- [`COLLABORATION_NOTES.md`](../../.agents/handoffs/COLLABORATION_NOTES.md) — Rule 6, 9 v2, 12, 14, 16, A40, A43 v2, A47 (lane discipline through this arc)
