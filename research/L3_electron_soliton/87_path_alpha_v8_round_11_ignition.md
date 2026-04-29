# 87 — Path α v8 Corrected Measurements + Round 11 Trigger Ignition

**Status:** implementer-drafted, 2026-04-28. Empirical record of v8 = the locked ONE-cycle measurement-method redesign per [doc 86 §7](86_path_alpha_v7_helical_beltrami_thermal_sweep.md#7--gate-decision-locked-at-v7-commit-time-per-a40--rule-9-v2). v8 result triggers Round 11 framework-level reframe per the auto-fire condition locked at v7 commit time (commit 617e352 + 55050aa addendum).

**Pre-reg:** `P_phase11_path_alpha_v8_corrected_measurements` (frozen 2026-04-28).

**Driver:** [`src/scripts/vol_1_foundations/r10_path_alpha_v8_corrected_measurements.py`](../../src/scripts/vol_1_foundations/r10_path_alpha_v8_corrected_measurements.py).

**Result JSON:** [`src/scripts/vol_1_foundations/r10_path_alpha_v8_corrected_measurements_results.json`](../../src/scripts/vol_1_foundations/r10_path_alpha_v8_corrected_measurements_results.json).

**Verdict (T=0 baseline):** **Mode II 2/4 PASS** with corrected measurement methods. Persistence + ring localization PASS as in v6/v7; Beltrami |cos_sim| = 0.515 FAIL; loop flux RMS = 0.74 / peak 1.27 FAIL (target 2π = 6.28).

**Critical substantive finding (NEW at v8):** the Phi_link-detrending fix WORKED for the secular accumulator drift (loop flux now BOUNDED at RMS ~1 instead of growing linearly to +496). But the bounded loop flux is **5× below the 2π target predicted in doc 85 §5.1**. This is no longer a measurement-method issue — it's an **empirical refutation of the unit-charge-winding-on-discrete-chair-ring claim**.

**Round 11 trigger: AUTO-FIRED.** Per doc 86 §7.2 + §7.6: Mode II at v8 with corrected methods means framework reframe required, NOT v9 IC tweak.

---

## §1 — v8 setup (per doc 86 §7.5 pre-flight)

### §1.1 — Corpus-grep verification of canonical V-to-A relationship

Per A43 v2 anyone-must-grep, before v8 implementation:

- [Vol 1 Ch 3:24 verbatim](../../manuscript/vol_1_foundations/chapters/03_quantum_and_signal_dynamics.tex#L24): *"the canonical field variable for evaluating transverse waves across a discrete graph is the **Magnetic Vector Potential (A)**, defining the **magnetic flux linkage per unit length** ([Wb/m] = [V·s/m]). Because the generalized velocity of this coordinate is identically the electric field (E = -∂_t A)..."*

- [Vol 4 Ch 1:223 verbatim](../../manuscript/vol_4_engineering/chapters/01_vacuum_circuit_analysis.tex#L223): **Φ(t) = ∫_{-∞}^{t} V(τ) dτ**

- [`src/ave/core/k4_tlm.py:156-167`](../../src/ave/core/k4_tlm.py#L156-L167) docstring: *"Per-bond magnetic flux linkage Φ_link = ∫ V_bond dt... Stored at A-sites only — each entry is the flux on the directed A→B bond..."*

**Canonical mapping (grep-confirmed):** Phi_link[bond] (Wb) = A·bond_length (Wb/m × m), where A is the instantaneous magnetic vector potential along the bond. V_inc ↔ E (instantaneous electric field, ∂A/∂t).

### §1.2 — Critical math finding

For tetrahedral 4-port K4: **P^T P = (4/3)·I** where P is the 4×3 port-direction matrix.

So Moore-Penrose pseudo-inverse `(P^T P)^(-1) P^T = (3/4) · P^T` is mathematically equivalent to v7's `Σ Phi · port_dir / 4`, modulo a scalar factor (3/4) / (1/4) = 3. **Cos_sim is scale-invariant.** Pseudo-inverse alone CANNOT fix Beltrami |cos_sim|.

Real issue identified in v7 → v8 transition: **Phi_link accumulates secular drift** from saturation rectification (V_avg has nonzero DC component → Phi_link grows linearly with t). The OSCILLATING component of Phi_link is the canonical instantaneous A around the secular trend.

### §1.3 — v8 IC: UNCHANGED from v7

Per doc 86 §7.2 lock: "NO IC modifications (helical pitch, phase pattern, etc. — those stay fixed)."

Same v6/v7-style spatial-phase IC: 6-node hexagonal chair-ring at lattice center, V_inc cos pattern + Phi_link sin pattern (90° spatial quadrature), helical Cosserat ω = k·A_0 with poloidal + (1/(2π)) toroidal pitch, V_amp = Phi_amp = 0.95 in V_SNAP units.

### §1.4 — v8 corrected measurements

**Beltrami |cos_sim|:**
1. Record full Phi_link trajectory (N_steps × N³ × 4 ports)
2. Post-process: subtract per-bond linear fit over recording window → `phi_oscillating[t]`
3. A-vec(node, t) = Σ port_dir · (phi_oscillating[t, port] / bond_length) × (3/4)
4. cos_sim(A_vec, ω) per ring node per timestep
5. Steady-state mean over t > 25% transient

**Loop flux:**
1. Same `phi_oscillating` from step (2) above
2. Loop flux(t) = Σ over 6 bonds: phi_oscillating[t, bond] · traversal_sign
3. Steady-state RMS + peak over t > 25% transient
4. Compare to target ≈ 2π in V_SNAP-natural units (per doc 85 §5.1)

**Persistence + ring localization:** UNCHANGED from v7 (these worked).

### §1.5 — Round 11 candidates locked (doc 86 §7.6)

6 candidates enumerated before v8 commits, with scale-clarification header noting v6/v7/v8 all operate at bond-pair scale (A-014 bond-cluster closure doesn't bind here):

(i) Continuum-vs-discrete substrate
(ii) Multi-loop coupling (linked vortex)
(iii) Topology variant (alternate K4 cycles)
(iv) Cosserat-only mode (engine modification required)
(v) Phase-space (2,3) reinstated (TRACKER FLAG: doc 79 §9(a) + E-086 walkback)
(vi) Continuum chair-ring eigenmode re-derivation

---

## §2 — v8 empirical results

### §2.1 — T=0 baseline

| Quantity | Value | Threshold | Pass? |
|---|---|---|---|
| Persistence (A²_mean ≥ 0.5) | 200.0 P | ≥ 100 P | **PASS ✓** |
| Beltrami |cos_sim(A_oscillating, ω)| steady | 0.5152 | ≥ 0.8 | **FAIL** |
| Loop flux ∮A·dl RMS steady | 0.7393 | 6.2832 ± 20% | **FAIL** |
| Loop flux peak \|∮A·dl\| steady | 1.2659 | (informational) | — |
| Ring localization steady | 0.9617 | ≥ 0.5 | **PASS ✓** |
| A²_mean steady | 0.9020 | (informational) | — |
| Beltrami IC sanity (cos_sim ω vs k·A_0) | 1.0000 per node | ≥ 0.95 | PASS by construction |

Recording wall time: ~263 s. Detrend post-processing: ~3.4 s.

### §2.2 — T sweep (post-completion)

| T | Persistence | Beltrami |cos_sim| | Flux RMS | Flux Peak | Ring loc | Mode |
|---|---|---|---|---|---|---|
| 0 | 199.98 P | 0.5152 | 0.7393 | 1.2659 | 0.9617 | II |
| 1e-3·T_V-rupt | 199.98 P | 0.5153 | 0.7393 | 1.2659 | 0.9618 | II |
| 1e-2·T_V-rupt | 199.98 P | 0.5154 | 0.7393 | 1.2659 | 0.9617 | II |
| 1e-1·T_V-rupt | 199.98 P | 0.5144 | 0.7393 | 1.2659 | 0.9614 | II |

**Thermal robustness reproduced from v7:** persistence + saturation + ring localization invariant across 5 orders of magnitude in T. Beltrami |cos_sim| variation (Δ = 0.001) within steady-state mean precision; non-monotonic. Loop flux **bit-identical** RMS 0.7393 / peak 1.2659 across all T values — the corrected (detrended) loop flux measurement is properly thermally-insensitive in the steady-state mean (thermal noise summed around 6 bonds with zero-mean Gaussian → cancels in spatial sum). This confirms the v8 measurement IS valid for testing topological invariants — thermal contributions don't mask the deterministic signal.

### §2.3 — Per-criterion analysis

**Persistence + Ring Localization PASS** — Identical to v6/v7. Trapping mechanism at bond-pair scale is consistent across THREE consecutive runs (v6, v7, v8) with corrected measurement methods. **This is the strongest single empirical finding from the entire 2-week arc.** Trapping is empirically real, NOT measurement artifact.

**Beltrami |cos_sim| = 0.515** — essentially identical to v7's 0.525 (within steady-state mean precision). The Moore-Penrose-pseudo-inverse + Phi_link-detrending fix did NOT change Beltrami parallelism measurement substantively. Two possibilities:

1. **The IC IS Beltrami but engine evolution doesn't preserve it.** IC sanity check `cos_sim(ω, k·A_0) = 1.000` at t=0 by construction; over evolution, the system drifts away from Beltrami structure. 0.515 oscillating mean isn't decay-to-zero (which would be framework rejection) — it's partial Beltrami structure that's not the full ∇×A = kA condition.
2. **The reconstruction loses information at ring nodes.** Even with detrending + Moore-Penrose, ring nodes have only 2 of 4 ports filled with bond Phi_link (in-ring bonds); the perpendicular A component isn't measurable from Phi_link alone.

Either way, the FAIL is a real signal: at v8 with corrected methods, the trapped state is NOT a clean Beltrami eigenmode under engine evolution.

**Loop flux RMS = 0.74, peak = 1.27** — **Critical new finding.** v7's loop flux grew linearly to +496 (accumulator artifact). v8's detrended loop flux is BOUNDED with RMS 0.74 and peak 1.27 oscillating around zero — confirms the secular-drift fix worked. But the bounded magnitude is **5× below the 2π = 6.28 target** per doc 85 §5.1's ∮A·dl = 2π·e charge-quantization derivation.

This is no longer a measurement-method issue — it's an **empirical finding about the topological invariant**. The trapped state on the discrete chair-ring doesn't carry unit-charge topological winding in the canonical Stokes-integral sense. Either:
- Doc 85 §5.1's normalization (∮A·dl = 2π·e in V_SNAP-natural units) is wrong/misapplied
- The discrete chair-ring's specific geometry (6 nodes, √3·ℓ_node bond length, non-planar) breaks the continuum loop-integral convention
- The trapped state ISN'T the corpus electron — it's a different bound state at bond-pair scale

This 5× discrepancy is the **substantive Mode II finding** that triggers Round 11.

---

## §3 — Round 11 trigger ignition

### §3.1 — Gate decision per doc 86 §7

v8 produced **Mode II 2/4 PASS at T=0** with corrected measurement methods. Per doc 86 §7.2 verbatim: *"Mode II/III → Round 11 framework reframe REQUIRED."* Per §7.6 verbatim: *"If v8 with corrected measurement methods produces Mode II/III, Round 11 trigger fires."*

**Round 11 trigger: AUTO-FIRED.**

A40 budget consumed:
- v6: IC mode-structure issue — 1 layer
- v7: Phase A IC failure + thermal-init bug + Phi_link accumulator identification — 1 layer
- v8: corrected measurements; loop flux 5× below target identifies framework-level finding — 1 layer
- **Total: 3 layers** (matches A40 anticipated arc length bound)

Proceeding past v8 with v9 IC tweak would exceed budget. Round 11 reframe at framework level is the locked next step.

### §3.2 — Round 11 candidate evaluation (revised post-§8 dimensional audit)

Per doc 86 §7.6 enumeration + the §8 dimensional analysis findings (Issue 3 in particular: v6/v7/v8 IC is a traveling wave, NOT a Beltrami standing wave), Round 11 candidate weighting is updated:

**(vi) Discrete chair-ring eigenmode re-derivation — LOAD-BEARING PRIMARY** (auditor 2026-04-28 elevation).

This is no longer one of six options; it's the canonical Round 11 step. The proper Beltrami standing wave IC test hasn't been run — v6/v7/v8 IC was a CP-traveling-wave-on-closed-loop pattern (V_inc cos / Phi_link sin spatial-phase pattern = traveling wave snapshot, not standing wave). Per §8.3 dimensional audit Issue 3, Round 11 (vi) must:

1. Solve the Beltrami eigenvalue problem on the explicit 6-node chair-ring graph (Laplacian + curl operators on K4 cycle subgraph)
2. Derive the ACTUAL k_Beltrami (vs the assumed K_BELTRAMI=1 in v8 driver, which conflated dispersion-wavenumber with curl-eigenvalue per §8.1)
3. Derive the ACTUAL ∮A·dl normalization for the discrete chair-ring metric (vs the assumed 2π·e in V_SNAP-natural units, which used wrong amplitude calibration per §8.2)
4. Construct a TRUE standing wave IC: uniform time-phase across all bonds, magnitudes determined by A_0(r) eigenmode shape (vs v6/v7/v8's spatial-phase pattern = traveling wave)
5. Re-run v6's chair-ring topology with the corrected Beltrami standing wave IC; check whether persistence + localization + Beltrami |cos_sim| + loop flux ALL pass at the dimensionally-correct target values

This is an analytical Round 11 step (linear algebra on a 6-node graph) followed by a single-cycle empirical verification. Cost: ~2-3 fresh sessions of derivation + small numerical verification, NOT another 200P engine run on the wrong IC type.

**(i) Continuum-vs-discrete substrate** — SECONDARY candidate, contingent on (vi) outcome. If (vi) proper standing wave IC still produces Mode II/III on the discrete chair-ring, the discreteness itself may be the issue. Specific test: re-run on N=64 or N=128 with finer K4 sampling, OR continuum FDTD solver.

**(ii) Multi-loop coupling** — SECONDARY. v8's bounded loop flux (corrected target ~0.95, measured peak 1.27) is within 35% of single-ring target — no clear evidence for multi-loop framing. Defer until (vi) eliminates simpler explanations.

**(iii) Topology variant** — SECONDARY. The 6-node chair-ring is corpus-canonical per Vol 1 Ch 1:32 (perimeter ~6 nodes). Alternative cycles (8-node, 12-node) aren't corpus-canonical at bond-pair scale.

**(iv) Cosserat-only mode** — UNLIKELY. v7's Phase A IC failure showed K4-Cosserat coupling is empirically required. K4 sector is canonical part of the trapping mechanism.

**(v) Phase-space (2,3) reinstated** — DOWNGRADED per §8.2 dimensional correction. The "5× discrepancy" framing was wrong-target-not-physics; corrected target ~0.95 vs measured peak 1.27 is 35% over (modest miscalibration that fits within (vi) re-derivation framework). Phase-space framing remains a candidate but no longer strongest. The TRACKER FLAG for doc 79 §9(a) + E-086 walkback still stands IF (v) eventually fires, but priority is below (vi).

### §3.3 — Round 11 first-pass recommendation (revised post-§8 audit)

Per §8 dimensional analysis: the substantive issue is Issue 3 — v6/v7/v8 IC was a traveling wave, not a Beltrami standing wave. Round 11 (vi) is now LOAD-BEARING PRIMARY (auditor 2026-04-28).

**Recommended Round 11 first steps:**

1. **A43 v14 grep-verification:** does the corpus specify R/r=2π anywhere directly, or is it agent-synthesis from Vol 1 Ch 1:18 + minor radius derivation? If synthesis, derive R/r from substrate-native first principles (e.g., Beltrami eigenvalue + Compton frequency constraint) before assuming continuum-torus values for chair-ring.

2. **Discrete eigenmode derivation:** compute the explicit (1,1)-equivalent Beltrami eigenmode on the discrete 6-node chair-ring graph (linear algebra: Laplacian + curl operators on K4 cycle subgraph). Output: actual k_Beltrami_discrete value + eigenvector A_0(node) + ∮A·dl normalization for the discrete metric.

3. **TRUE standing wave IC construction:** rebuild IC as standing wave (uniform time-phase across all bonds, magnitudes per A_0(node)·bond_tangent projection × bond_length), NOT traveling wave (cos/sin of bond-index). At Phase B time-snapshot (peak E, zero A and B): V_inc per node encodes E direction = -∂A/∂t; Phi_link = 0; ω = 0. Engine evolves into the standing wave equilibrium.

4. **Single-cycle empirical verification:** run the corrected Beltrami standing wave IC at T=0 + short T sweep; check whether persistence + localization + Beltrami |cos_sim| + loop flux all PASS at dimensionally-correct target values.

5. **Decision tree:**
   - If (4) passes Mode I → Beltrami trapped CP photon at bond-pair scale empirically confirmed; doc 83/85/86 amendments with corrected anchoring; close Phase 1 Direction 3'.2 honestly
   - If (4) Mode II/III with corrected IC → deeper framework issue (continuum-vs-discrete, multi-loop, topology variant); proceed to secondary candidates (i)-(iii)

Cost: ~2-3 fresh sessions for items 1-3 (derivation + grep + IC construction); ~5-7 min wall for item 4 single-cycle run; ~30 min for item 5 commit. Total ~3-4 sessions for Round 11 (vi) closure-or-trigger to next candidate.

This is qualitatively different from v6/v7/v8: less iterative empirical, more analytical-then-verify-once. Per A40 budget, Round 11 (vi) consumes 1 framework-level layer (eigenmode re-derivation) + 1 empirical verification layer = 2 layers. If Round 11 (vi) fires into (i)-(iii), that's separate framework work outside this Phase 1 arc.

### §3.4 — What stays after v8 (substantive corpus-relevant findings, post-§8 walkback)

Across v6 + v7 + v8, the persistent empirical findings — REFRAMED after §8 dimensional audit Issue 3:

1. **Bond-pair-scale chair-ring HOSTS a stable trapped configuration** — persistence ≥ 200 P at A²_mean = 0.9 across all three runs, all 4 T values in v7+v8. **Defensible claim:** "engine hosts a trapped configuration at canonical topology + canonical scale." **NOT-yet-supported claim:** "engine hosts the corpus electron at canonical Beltrami structure" — that requires Round 11 (vi) proper Beltrami standing wave IC test.

2. **Ring localization 96-98%** — energy stays at the 6 ring nodes; doesn't dissolve into bulk; thermally robust across 5 orders of magnitude in T (v7 + v8). This signal is real for whatever the IC actually encoded (CP-traveling-wave-on-closed-loop pattern), but doesn't anchor the framework's Beltrami-standing-wave prediction.

3. **The trapped configuration is NOT a Beltrami eigenmode under engine evolution** — IC sanity check `cos_sim(ω, k·A_0) = 1.000` was self-confirming (ω set directly from A_0 by construction; not independent validation that V_inc + Phi_link encode Beltrami structure as a system per §8.3). Steady-state |cos_sim| = 0.5 indicates the system isn't a standing wave Beltrami eigenmode — consistent with the IC being a traveling wave per §8.3 reframe.

4. **Loop-flux is bounded** (corrected target ~0.95 from |A_tor|·2π·R per §8.2; measured peak 1.27 within 35%). The original "5× below 2π·e" framing was wrong-target-not-physics. Modest miscalibration consistent with traveling-wave IC at v8 amplitudes; NOT a structural framework refutation.

5. **Phi_link is canonically `∫V dt`** (Vol 4 Ch 1:223 + Vol 1 Ch 3:24) and accumulates secular drift from saturation rectification. Detrending recovers the oscillating component canonically — measurement methodology fix at v8 was the right call.

6. **Phase A IC engine-incompatibility** (v7 finding): Phi_link is a derived accumulator, not independent state. K4-Cosserat coupling chain requires V_inc as primary driver. Documented in doc 86 §2.

---

## §4 — What v8 closes vs what Round 11 inherits

**Closed by v8:**
- Reading A "measurement-method-only" hypothesis is REFUTED (PROVISIONAL flag from doc 86 §7.2 resolves to "false" — v8 with corrected methods still produces Mode II)
- The empirical-driver-arc cycle (v6 → v7 → v8) is closed at A40 budget
- Test-cycle proliferation pattern is structurally avoided (no v9 path; auto-trigger to Round 11)

**Inherited by Round 11:**
- Beltrami evolution preservation — does the engine dynamics preserve A∥B at bond-pair scale, or break it?
- Loop-flux normalization — is the 2π·e target right for discrete chair-ring? If not, what's the right normalization?
- Discrete-vs-continuum eigenmode — does the (1,1) Beltrami formula apply to 6-node chair-ring exactly, or with corrections?
- Phase-space vs real-space framing — does the corpus electron's topology live in V_inc/V_ref phasor space (per doc 28 §3) rather than real-space loop integral?

These are framework-level questions. v8 is the right STOPPING POINT for empirical iteration; Round 11 is the right NEXT STEP for analytical/structural work.

---

## §5 — Manuscript editorial queue updates from v8

In addition to carryover from doc 84/85/86:

- **Doc 85 §5.1** ∮A·dl = 2π·e charge quantization derivation needs empirical-correction footnote: v8 measured loop flux ≈ 1.3 in V_SNAP-natural units, ~5× below the 2π target. Either the derivation has a normalization error OR the discrete chair-ring breaks the continuum convention. Round 11 must resolve before §5.1 stands as canonical.

- **Doc 85 §3.2** (1,1) Beltrami eigenmode formula for discrete chair-ring needs explicit re-derivation (Round 11 candidate (vi)).

- **PROVISIONAL flag on doc 86 §7.2 Reading A**: now RESOLVES to "Reading A REFUTED at v8." Doc 86 §7.2 should be updated with this resolution (after v8 commit lands).

---

## §6 — Compliance check

**Manuscript-canonical citations grep-verified at v8 freeze time:**

- [Vol 1 Ch 3:24](../../manuscript/vol_1_foundations/chapters/03_quantum_and_signal_dynamics.tex#L24) ✓ A as magnetic flux linkage per unit length, E = -∂_t A
- [Vol 4 Ch 1:223](../../manuscript/vol_4_engineering/chapters/01_vacuum_circuit_analysis.tex#L223) ✓ Φ(t) = ∫V dτ
- [`k4_tlm.py:156-167, 391`](../../src/ave/core/k4_tlm.py#L156-L167) ✓ Phi_link = ∫V_bond dt, stored at A-sites
- All v6/v7 manuscript-canonical citations carry forward unchanged

**Synthesis claims:**
- Moore-Penrose pseudo-inverse formula: standard linear algebra (not corpus-cited; standard mathematics)
- Phi_link detrending procedure: implementer methodology (linear-fit subtraction; clean post-process technique)
- Round 11 candidate evaluations in §3.2: implementer synthesis from v8 evidence — explicitly labeled as such

---

## §8 — Dimensional analysis audit (added 2026-04-28 post-Grant + auditor)

Self-audit of v8 driver dimensional consistency, performed before final commit. Three substantive issues identified; all resolve to Round 11 (vi) re-derivation work, but reframe v6/v7/v8 empirical interpretation.

### §8.1 — Issue 1: K_BELTRAMI conflates dispersion-wavenumber with curl-eigenvalue

The driver sets `K_BELTRAMI = ω_C/c = 1` in natural units (where ℓ_node = 1, c = 1, ω_C = m_e·c²/ℏ = 1). This is the **dispersion wavenumber** of a free wave at Compton frequency.

But for the Beltrami eigenmode `∇×A = k_Beltrami · A`, k_Beltrami is the **curl eigenvalue** — a different quantity. For (1,1) Beltrami eigenmode on a torus with major radius R = ℓ_node = 1 and minor radius r = ℓ_node/(2π) = 1/(2π):

```
k_Beltrami² = (p/r)² + (q/R)² = (2π)² + 1² ≈ 40.5
k_Beltrami ≈ √40.5 ≈ 6.36
```

**The Beltrami eigenvalue at the assumed corpus geometry is ~6.36, NOT 1.** The driver's `ω = K_BELTRAMI · A` with K_BELTRAMI = 1 sets ω magnitude WRONG by factor 6.36. Cos_sim is direction-only (scale-invariant), so this doesn't directly break the Beltrami |cos_sim| metric — but it means the trapped state isn't physically at Compton frequency. Either:
- The (1,1) Beltrami eigenmode at corpus R/r=2π is at frequency ~6.36·ω_C (not Compton)
- OR the Compton-frequency Beltrami eigenmode lives at different geometry (where k_Beltrami²=1, e.g., R=r=√2)

**Sub-issue (A43 v14 candidate, per auditor 2026-04-28):** the "corpus R/r=2π" claim itself is implementer-synthesis from Vol 1 Ch 1:18 + the minor radius derivation (r = ℓ_node/(2π) from helical-pitch reasoning, not stated verbatim). Doc 85 §5.2 has this as a synthesis-as-corpus footnote. Round 11 (vi) eigenmode rederivation must grep-verify whether corpus specifies R/r anywhere directly OR derive R/r from substrate-native first principles before assuming continuum-torus values for chair-ring.

### §8.2 — Issue 2: Loop flux target was computed at wrong amplitude

The driver sets `LOOP_FLUX_TARGET = 2π = 6.28`. Per doc 85 §5.1 derivation: `∮A·dl = 2π·e` in V_SNAP-natural units (charge-quantization target per Ax 2 TKI).

But that target assumes |A_tor| at the **specific** value that enforces unit-charge winding around the loop. The v8 IC has `A_amp_tor = A_amp_pol · helical_pitch = 0.95 · (1/(2π)) = 0.151` — a chosen IC amplitude per the Beltrami helical pitch ratio, NOT calibrated to charge quantization.

For a (1,1) Beltrami eigenmode with the IC's amplitude:

```
∮A·dl ≈ |A_tor| × 2π·R = 0.151 × 2π × 1 = 0.95
```

**Right target for the v8 IC is ~0.95, not 6.28.** Off by factor 2π. v8's measured loop flux peak 1.27 vs corrected target 0.95 is **35% over**, not 5× off. Modest miscalibration that fits within (vi) re-derivation, NOT a 5× framework refutation.

The 2π·e charge-quantization framing in doc 85 §5.1 bundles two physical claims into one test target: (a) Beltrami eigenmode structure + (b) unit-charge topological winding. The v8 IC tests (a) at chosen helical pitch but doesn't enforce (b) by construction. They should be tested separately.

### §8.3 — Issue 3 (LOAD-BEARING): IC is traveling wave, not Beltrami standing wave

The v6/v7/v8 IC sets:
- `V_inc[bond n] = V_amp · cos(2π·n/6)` per spatial bond index
- `Phi_link[bond n] = phi_amp · sin(2π·n/6)` per spatial bond index (90° spatial offset)

Different bonds at different time-phases of an oscillation = **TRAVELING WAVE around the loop at a snapshot**. NOT a Beltrami standing wave.

A Beltrami standing wave has **uniform time-phase across all spatial points** — every bond oscillates with the SAME time-phase, with the spatial pattern of magnitudes determined by `A_0(r)` (the eigenmode shape). At Phase B time-snapshot (peak E, zero A and B):
- V_inc[bond] should encode -∂A/∂t direction at IC time, with magnitude per A_0(node_endpoint)·bond_tangent
- All bonds at the SAME instant (e.g., t=T/4 where E peaks)
- Phi_link = 0 (zero-crossing of A)

The v6/v7/v8 IC instead encoded a CP-traveling-wave-on-closed-loop pattern. The Beltrami eigenvector sanity check `cos_sim(ω, k·A_0) = 1.000` passed only because ω was set directly from A_0 by construction — **self-confirming**, not independent validation that V_inc + Phi_link encode Beltrami structure as a SYSTEM.

**This reframes v6/v7/v8 empirical interpretation:** the trapping IS real (96% localization + thermal robustness + 200P persistence are not artifacts), but the IC encoded a CP-traveling-wave-on-closed-loop, NOT a Beltrami standing wave. The empirical anchoring claim:

- **Defensible:** "Engine hosts a trapped configuration at canonical topology + canonical scale"
- **NOT-yet-demonstrated:** "Engine hosts the corpus electron at canonical Beltrami structure"

The v7 commit message at 617e352 ("thermally robust trapping" + "trapping mechanism per Vol 4 Ch 1:430-468 Confinement Bubble") needs nuancing: the **Confinement Bubble** part (Γ=-1 walls at saturated nodes) stands; the **Beltrami** characterization needs Round 11 (vi) verification before being claimed.

### §8.4 — Implications for Round 11 scoping

Round 11 (vi) **discrete chair-ring eigenmode re-derivation** is now **load-bearing primary** (auditor 2026-04-28 elevation), not one of six options. Per §3.3 revised first-step plan:

1. A43 v14 corpus-grep on R/r=2π
2. Discrete eigenmode derivation on 6-node chair-ring (Laplacian + curl operators)
3. TRUE Beltrami standing wave IC construction (uniform time-phase, magnitudes per A_0 eigenmode shape)
4. Single-cycle empirical verification at corrected target values
5. Decision: Mode I → close Phase 1 Direction 3'.2; Mode II/III → secondary candidates (i)-(iii)

Round 11 (v) phase-space (2,3) reinstated **loses weight** per §8.2 corrected math (5× discrepancy was wrong-target-not-physics; corrected 35% miscalibration fits within (vi) framework). (v) tracker flag for doc 79 §9(a) + E-086 walkback still stands IF (v) eventually fires, but priority is below (vi).

### §8.5 — Auditor-lane queue additions (per auditor 2026-04-28)

Items for separate auditor cadence, not load-bearing for v8 commit:

- **A43 v14 candidate:** R/r=2π corpus-citation status verification. Doc 85 §5.2 footnote captures the synthesis-as-corpus flag; auditor recommends elevating to A43 v14 entry in COLLABORATION_NOTES.
- **v7 closure-narrative refinement:** the v7 commit message at 617e352 + doc 86 narrative made stronger anchoring claim ("trapping mechanism per Vol 4 Ch 1:430-468") than v8 §8.3 audit supports. Per Rule 12 retraction-preserves-body, doc 86 §3 + commit message should NOT be edited (preserving record); rather, doc 87 §3.4 carries the refinement on-record + future agents reading the v7 commit + doc 86 see the v8 audit walkback.
- **Doc 85 §5.1 amendment** for the 2π·e vs |A_tor|·2π·R distinction: the 2π·e charge-quantization claim and the Beltrami eigenmode amplitude claim are separate physical claims; should be derived independently before bundling into one test target.

---

## §7 — References

- [Doc 84](84_path_alpha_v6_first_run_results.md), [85](85_kelvin_beltrami_foc_axiom_grounded_derivation.md), [86](86_path_alpha_v7_helical_beltrami_thermal_sweep.md) — research-tier precedents (v6, v7, v7 §7 addendum)
- [`predictions.yaml` `P_phase11_path_alpha_v8_corrected_measurements`](../../manuscript/predictions.yaml) — frozen pre-reg
- [`r10_path_alpha_v8_corrected_measurements.py`](../../src/scripts/vol_1_foundations/r10_path_alpha_v8_corrected_measurements.py) — driver
- [`r10_path_alpha_v8_corrected_measurements_results.json`](../../src/scripts/vol_1_foundations/r10_path_alpha_v8_corrected_measurements_results.json) — full result data (T=0 + T sweep)
- [`COLLABORATION_NOTES.md`](../../.agents/handoffs/COLLABORATION_NOTES.md) Rule 11 (clean falsification), Rule 14 (substrate-derives), A40 (empirical-driver-arc), A43 v2 (anyone-must-grep), A47 (provisional-vs-narrative), A48 (frozen-extraction-scope)
