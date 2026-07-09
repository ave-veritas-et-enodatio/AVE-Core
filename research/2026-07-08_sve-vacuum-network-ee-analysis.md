# SVE vacuum-network EE analysis — consolidated (Problem-8 Branch-no support · impedance provenance · DC small-signal model)

**Date:** 2026-07-08 · **Lane:** orchestration (SVE / birefringence Letter, round-3 Problem-8) · **Status:** three EE analyses complete + one in-flight
**Tree-proof (origin/main):** `0341cababa92fadc8e680710bd3706b113268fa6`
**Workflow runs:** K4-TLM network `wf_386f2f61-779` · DC small-signal `wf_b56b079c-259` · transverse/shear (in-flight) `wf_389cc1a6-0d0`

This doc consolidates the EE-network analyses run to (a) close the single-node-model rigor gap Grant flagged on the Problem-8 Branch-no decision, and (b) honestly tag the provenance of the vacuum characteristic impedance. All numbers re-run and verified against the operative artifacts.

---

## ★ VERDICTS

| Question | Verdict |
|---|---|
| Problem-8 loading cutoff (scalar/longitudinal K4-TLM network) | **BRANCH-NO CONFIRMED & HARDENED** — no network fence |
| Vacuum char. impedance Z₀ = 377 Ω | **STRUCTURALLY AN INPUT** (α-echo); K4 supplies only an O(1) coordination factor |
| Clean K4 geometric output | the **1/√3 velocity factor** (LC-product sector), not the impedance (L/C-ratio sector) |
| DC small-signal model | **BUILT**; negative-differential-capacitance at V_yield/√2 is real & derived |
| Neg-diff-cap = genesis seat? | **NO** — genesis correspondence refuted (skeptical prior held) |
| Transverse/shear sector (where 377 + the X-ray actually live) | **IN-FLIGHT** (`wf_389cc1a6-0d0`) |

**Net for the paper:** the round-3 Problem-8 decision (revert the static-loading branch) is supported on physics — the loading response reaches the band edge in both the lumped-node and the full network model, so Mertens' X-ray transport falsification stands. Z₀ = 377 Ω is honestly an imported constant, not a derived output. The DC model yields a real cRIO C_eff(V)-shape bench prediction.

---

## 1 — K4-TLM network: Branch-no hardened (loading cutoff)

Built on the **genuine** tetrahedral connectivity (canonical `k4_tlm.py` PORTS + unitary 4-port junction S = ½·11ᵀ − I; the Bloch operator T(k) = D(k)·S; z = 4 verified on all 128 nodes of `build_diamond_net`), NOT a Cartesian/1D/continuum strawman. Re-run confirms:

- **Gapless dispersion.** Band edge at the Nyquist point (~2.27 MeV), **ω_C = 511 keV sits mid-band** (phase 0.707), not at the edge. **1088 propagating modes in the 30–80 keV window** — no gap, no sub-band feature where a "fence" would need to live.
- **Static loading.** The loaded-defect impedance step Z_eff = Z₀/√S has amplitude-keyed, **frequency-independent** |Γ|, so it scatters across the *entire* passband up to the band edge — no frequency at which the loading stops.

**Result:** the single-lumped-node result was **not** a lumping artifact. Branch-no hardens on the network model; the loading response reaches ~MeV, so the X-ray transport kill (Pb halo resolved at 136 keV; shell Born ~1.5 kb vs 0.7 kb measured) stands. Three framings, adversarially verified, zero refutes.

**Sector caveat (see §4):** this was the **scalar/longitudinal** TLM sector. The X-ray is a transverse EM wave; the transverse recheck is in-flight.

## 2 — Impedance provenance: 377 Ω is an import

- The per-bond link impedance `√(L_node/C_node) = √(μ₀/ε₀) = 376.73 Ω` recovers to ~1e-16 — but **definitionally**, since L = μ₀ℓ_node and C = ε₀ℓ_node are fed in. Post-2019-SI, Z₀ = 2αh/e² — an **α-echo**.
- The K4 connectivity fixes the **LC product** (transit time / wave speed, calibrated to c) but leaves the **L/C ratio** (impedance) free — independent combinations. So the geometry cannot fix the impedance *value*.
- The connectivity does supply a genuine dimensionless coordination factor g (from the z = 4 scatter, S_ii = 2/z − 1 = −½), but **g is convention-dependent** across framings (1/3, 0.612, 0.433) — the tell that it is a bookkeeping dressing on a free-choice impedance, not a physical output. A real bulk-impedance output would be convention-invariant.
- **The one clean convention-independent K4 output is the velocity factor 1/√3** (LC-product / wave-speed sector). FORM/VALUE meta-pattern: the geometry forces *how fast* (a form), imports *what impedance* (a value).

**Verdict:** Z₀ = 377 Ω is **structurally an input** — the network cannot test it, only dress it. (Honest answer to "have we measured 377 Ω?" — no, it is definitional / α-tied.)

## 3 — DC small-signal model of the saturable node

The missing quadrant (we had AC large-signal = the Letter, AC small-signal = the χ(ω) run). Built from the canonical Ax4 kernel Q(V) = C₀·S(V)·V, S(V) = √(1 − (V/V_yield)²), C₀ = ε₀ℓ_node = 3.42e-24 F, V_yield = √α·V_snap = 43.65 kV.

- **★ Negative-differential-capacitance, derived not assumed.** The differential C_ss = dQ/dV crosses **zero exactly at x = V_b/V_yield = 1/√2** (re-run numeric root 0.70710678, 1.9e-11 from 1/√2; corroborated by the Q-V argmax and a sign-change bracket — the analytic formula kept out of the detection path). Above it, C_ss < 0 up to rupture (x = 1, S → 0). In volts: **V_b = V_yield/√2 = 30.87 kV**, E = E_YIELD/√2 = 7.99e16 V/m. Profile C_ss/C₀ = +1 (x=0) → 0 (x=0.707) → −0.19 (x=0.75) → −∞ (x→1). The zero is the root of (1 − 2x²), structurally distinct from the rupture root (1 − x²). This is the reactance divergence the AC small-signal run glimpsed at 0.707.
- **Interpretation: GENUINE-REACTIVE-INSTABILITY** — an active-element / negative-differential region (the reactive cousin of tunnel-diode NDR).
- **Genesis: NO-CORRESPONDENCE.** The hypothesis that the neg-diff-cap is the substrate-native seat of rupture/genesis/pair-production was **refuted** by the adversarial gate (both the network-stabilization and genesis-precursor framings failed; the surviving framing reports no genesis payoff). The skeptical prior held — the instability is a real kernel feature but seeds nothing.

## 4 — Sector caveat + transverse model (in-flight)

The K4-TLM (§1–2) is the **scalar bond-voltage** node — one amplitude per bond, **no E-vs-H distinction** — so it is the longitudinal/scalar sector and structurally *cannot* produce a transverse impedance E/H as an output (only import it); its 1/√3 is the longitudinal propagation factor. But 377 Ω is the **transverse** EM impedance, and the transport X-ray is a **transverse** wave. So the impedance question and the Branch-no recheck genuinely live in the **transverse/shear (T2) sector**, modeled via the 6×6 Cosserat Bloch solver (`k4_bloch_dispersion.py`). That run (`wf_389cc1a6-0d0`) tests: (i) transverse impedance output-vs-import (prior: absolute value still an import), (ii) the sector ratios ν = 2/7, v_L/v_T = √(10/3) from K = 2G as forced FORMS, (iii) transverse Branch-no recheck. **To be folded in when it lands.**

## 5 — cRIO bench prediction (from the DC model)

The DC small-signal C_eff(V) discriminator (the first cRIO experiment) predicts, on a **known saturable dielectric first** (shared ground): C_eff monotonically decreasing from C₀, a **zero-crossing at V_sat/√2**, and a neg-diff-cap region V ∈ (V_sat/√2, V_sat) that reads as a **reactance sign-flip / lock-in phase inversion** (possibly oscillation/hysteresis). This validates the kernel shape (1 − 2x²)/√(1 − x²).
- **Honest limit:** the *vacuum's* own zero-crossing is at 30.87 kV across ℓ_node — a Schwinger-scale field, **not bench-reachable**. The bench confirms the shape/mechanism on a real varactor, not the vacuum value.

## 6 — Open flag (flag-don't-fix): three "capacitance" senses

The corpus carries **three distinct capacitance definitions that behave oppositely**: the constitutive ε_eff = ε₀·S (decreasing), an "observable C_eff = 1/S → ∞" noted in the `epsilon_eff` docstring (diverging), and the differential C_ss = dQ/dV (going negative). The bench mapping cannot claim the neg-diff-cap zero-crossing is directly measurable until one canonical sense is pinned for the C_eff(V) discriminator. **Owed to the auditor lane before this reaches the Letter or the bench spec.**

## 7 — Honest meta

Three physically-appealing hypotheses raised in this arc — the longitudinal spin-weld (earlier), the √α response fence, and the neg-diff-cap genesis seat — were each refuted by the derivation / adversarial gate. The confirmed content here is the honest negatives (Branch-no, genesis-no) plus the honest tags (377 = import, 1/√3 = the one forced form) and one real bench-shape prediction. The discipline functioned as the reality-check.

## 8 — Provenance / gates

Anti-tautology gates passed on both completed runs (band edge computed from Bloch eigenvalues not assumed; 377 flagged definitional not fed as answer; neg-diff-cap fell out of the kernel to 1.9e-11, analytic formula out of the detection path). Scratchpad artifacts: `sve_k4tlm_pass1.py`, `sve_dc_smallsignal_phase1.py` (+ per-framing scripts). Findings-only; no canon edited. `[REVIEW: pending-orchestrator]` DO-NOT-MERGE.
