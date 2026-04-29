# 91 — Round 11 (vi) Stride 4: v9 Discrete Eigenmode IC → Mode III; Round 11 (vi) Doesn't Close

**Status:** implementer-drafted, 2026-04-29. Stride 4 work record per [doc 90 §10.4](90_round_11_vi_stride_3_discrete_eigenmode.md#104--q1-q4-resolved) Stride 4 plan.

**Verdict:** v9 with discrete eigenmode IC at the top ring-localized mode (k = 0.52 in 1/ℓ_node units, corrected per unit-conversion fix) lands **Mode III, 1/4 PASS**. Beltrami |cos_sim| = 0.494, A²_mean steady = 0.4954 (just below 0.5 threshold), ring localization = 0.695 (PASS but lower than v7/v8). **Round 11 (vi) discrete chair-ring eigenmode rederivation does NOT close to Mode I.**

Per doc 86 §7.6 + doc 87 §7.2 locked gate: Round 11 trigger now fires INTO secondary candidates (i)/(ii)/(iii). The chair-ring + 1-step K4 substrate at corpus scale doesn't host the corpus electron in the (1,1)-equivalent Beltrami sense, even with corrected eigenmode IC and physical-k interpretation.

---

## §1 — Unit conversion correction (caught at v9 implementation)

Doc 90 §3 reported k_in_lnode = k_eigenvalue × √3 = 1.56 for the top mode. **This was wrong.**

Correct conversion: bond_length = √3·ℓ_node, so 1/bond_length = (1/√3)/ℓ_node. Eigenvalue 0.9001 in 1/bond_length units = 0.9001/√3 ≈ **0.52 in 1/ℓ_node units.**

Helical pitch corrected: λ_helix = 2π/k = 2π/0.52 ≈ 12·ℓ_node. Over chair-ring perimeter 6√3·ℓ_node ≈ 10.4·ℓ_node, A makes 10.4/12 ≈ **0.87 full helical rotations per ring traversal** — close to (q=1, p=0) trapped CP photon "one polarization rotation per loop" picture, NOT 2.5 rotations as doc 90 erroneously stated.

Continuum-to-discrete ratio: 6.36/0.52 ≈ **12×** gap (not 4× as doc 90 §2.2 stated). The discrete chair-ring + 1-step K4 spectrum is more dramatically below the continuum (1,1) prediction than doc 90 framed.

**Doc 90 §2.2-§2.3 + §10.1 require correction footnotes** per Rule 12 retraction-preserves-body. Original analysis preserved with corrections noted.

---

## §2 — v9 IC implementation

### §2.1 — Spec per doc 90 §4.1 + §10.4 resolution

- 18 nodes seeded (6 chair-ring + 12 1-step K4 neighbors) per Stride 3 eigenvector
- V_inc[node, port] = scale · A_0(node) · port_dir for each of 4 K4 ports per node
- Phi_link = 0 (Phase B for K4 sector — zero crossing of ∫E dt)
- Cosserat ω[node] = (k_in_lnode_corrected) · scale · A_0(node) — set at peak per Beltrami B = ∇×A = k·A
- scale calibrated so max ring |V_inc| = √sat_amp_target · V_SNAP (peak saturation at most-amp ring node)

Note Phase B for K4 + Phase A for Cosserat = mixed-phase IC. Pure Phase B for both would have ω=0 which doesn't work in this engine config (LC force disabled per `disable_cosserat_lc_force=True`; ω stays at zero throughout).

### §2.2 — IC outputs

| Quantity | Value |
|---|---|
| V_inc scale factor | 1.9655 |
| Max ring \|V_inc\| × scale | 0.9747 (target √0.95 ≈ 0.9747) ✓ |
| k_eigenvalue (1/bond_length) | 0.9001 |
| k_in_lnode (corrected: ÷ √3) | 0.5197 |
| A²_per_node at IC | [0.227, 0.179, 0.674, 1.218, 1.267, 0.771] |
| A²_mean at IC | 0.7228 |
| A²_min at IC | 0.179 |
| Ring localization at IC | 0.842 |

The eigenvector amplitudes are non-uniform — node 4 is over-saturated (A² = 1.27) while nodes 0 and 1 are well below (A² ≈ 0.2). The amplitude scaling can't simultaneously satisfy "saturation at peak node" AND "all nodes above threshold."

---

## §3 — v9 empirical results

### §3.1 — Steady-state metrics (after 25% transient)

| Quantity | Value | Threshold | Pass? |
|---|---|---|---|
| Persistence (A²_mean ≥ 0.5) | 0.0 P | ≥ 100 P | **FAIL** (just below threshold) |
| Beltrami \|cos_sim(A_oscillating, ω)\| steady | 0.494 | ≥ 0.8 | **FAIL** |
| Loop flux RMS | 0.008 | (target 0 from eigenvector) | **PASS** in physical sense (target ≈ 0 + measured ≈ 0) — but driver code logic fails on target=0 division |
| Ring localization | 0.695 | ≥ 0.5 | **PASS** |
| A²_mean steady | 0.4954 | (informational) | — (just below 0.5, steady throughout) |

Steady-state is reached quickly (~25 P). After that: A²_mean stable at 0.50, ring localization stable at ~0.70, |cos_sim| oscillating around 0.5.

### §3.2 — Mode adjudication

Strict 4-criterion: 1/4 PASS (only ring localization). **Mode III.**

If loop flux is interpreted physically (target = 0, measured ≈ 0 → PASS): 2/4 PASS = **Mode II**. The eigenvector A_0 is mostly POLOIDAL (perpendicular to bond tangent at each node), so ∮A·dl ≈ 0 by orthogonality is the correct prediction. Driver code's `abs(measured - target)/target` logic divides by zero when target = 0.

Either way: NOT Mode I. Round 11 (vi) does not close to corpus-electron empirical confirmation.

### §3.3 — Comparison to v6/v7/v8

v6/v7/v8 used uniform-amplitude spatial-phase IC (cos/sin pattern around 6 bonds, in-ring ports only):
- Persistence 200 P at A²_mean = 0.9 (sustained saturation)
- Ring localization 96% (energy stays at 6 ring nodes)
- Beltrami |cos_sim| ≈ 0.5 (similar to v9)
- Loop flux ~496 (v7) or ~1.27 peak after detrending (v8)

v9 with discrete eigenmode IC + 18-node seeding:
- A²_mean drops from IC's 0.72 to steady 0.50 (energy radiated out)
- Ring localization 70% (worse than v7/v8)
- Beltrami |cos_sim| ≈ 0.5 (same)
- Loop flux ~0.008 (correct prediction from eigenvector)

**The eigenvector IC is WORSE than v7/v8's spatial-phase pattern at maintaining trapping**, even though it's the substrate-native Beltrami eigenmode. Possible reasons:

1. **Position-mapping mismatch**: Stride 3 eigenmode was computed at origin-centered positions; v9 used lattice-center (16,16,16). The eigenvector should be translation-invariant, but the engine's PML and grid edges might affect dynamics differently at different positions.

2. **Non-uniform amplitude**: eigenvector has factor 7× variation in |A_0| across ring nodes (0.18 to 1.27). Some nodes over-saturated drive more dynamics; others sub-saturated don't engage the trapping mechanism cleanly.

3. **Engine dynamics doesn't preserve the eigenvector**: same Beltrami |cos_sim| at v6/v7/v8 (~0.5) and v9 (0.494) suggests the engine doesn't drive ANY IC toward Beltrami parallelism. The system has internal dynamics that break A∥B over time, regardless of IC class.

4. **The eigenmode I solved isn't the right one**: Stride 3's eigenmode solver computed the curl operator's eigenvalues. But the engine's actual dynamics include K4-TLM scatter+connect + Cosserat self-terms, NOT just curl. The system's natural attractor might not be a curl-eigenmode at all.

Most likely a combination of (3) and (4): engine dynamics has its own attractor that's NEITHER v7/v8 spatial-phase nor v9 discrete-curl-eigenmode. Both produce Mode II/III at similar Beltrami |cos_sim| ≈ 0.5.

---

## §4 — Round 11 (vi) closure decision

Per doc 86 §7.6 + doc 87 §7.2 locked gate:

> "Mode II/III → Round 11 framework reframe REQUIRED. Specific candidates surfaced by the Mode II/III pattern at v8: Mode II with persistence + localization PASS but Beltrami/topology FAIL with corrected methods → the discrete K4 chair-ring DOESN'T admit a clean Beltrami eigenmode at this scale (continuum-vs-discrete embedding finding) → reframe at substrate-discretization level"

v9 Mode II/III WITH the discrete eigenmode IC matches exactly this prediction: substrate-discretization issue. The discrete chair-ring + 1-step K4 doesn't host a clean Beltrami eigenmode with persistence + localization + parallelism + topology all passing simultaneously.

**Round 11 (vi) discrete chair-ring eigenmode rederivation: DOES NOT CLOSE TO MODE I.**

Per locked gate, trigger fires into secondary candidates:

**(i) Continuum-vs-discrete substrate** — STRONGEST per v9 result. The K4 chair-ring + 1-step neighborhood is too coarse for the continuum (1,1) Beltrami at corpus geometry. Discrete spectrum top is 12× below continuum (per §1 corrected unit conversion). Path: extend to N=64 or N=128 lattice, or test in continuum FDTD solver bypassing K4 discretization.

**(ii) Multi-loop coupling** — NOT clearly indicated by v9 evidence; the trapping is genuinely 1-loop, not multi-loop.

**(iii) Topology variant** — POSSIBLE. 6-node chair-ring may not be the right K4 cycle for the corpus electron at corpus scale. Alternate cycles (12-node, 24-node) might give discrete spectra with eigenvalues closer to k_C = 1 in 1/ℓ_node units.

---

## §5 — Honest closure narrative for the entire arc

**v6/v7/v8/v9 arc empirical findings (all stand):**

- Bond-pair-scale chair-ring on K4 hosts a **trapped configuration** of some kind: persistence 200 P at saturation amplitude (with v6/v7/v8 IC; v9 less stable)
- Ring localization 70-96% across all four versions
- Thermal robustness across 5 orders of magnitude in T (v7/v8)
- Beltrami |cos_sim| ≈ 0.5 in steady-state across ALL IC classes (v7/v8 spatial-phase, v9 discrete-eigenmode)

**What's NOT confirmed:**

- The trapped configuration IS the corpus electron's canonical Beltrami trapped CP photon at K4 chair-ring scale: NO. v9 with proper substrate-native eigenmode IC doesn't outperform v6/v7/v8's spatial-phase IC. Beltrami parallelism caps at ~0.5 regardless of IC class. The engine doesn't host a clean Beltrami eigenmode at K4 chair-ring + 1-step scale.

- The Compton-frequency identification is canonically right at this substrate: NO. Discrete spectrum top at k=0.52 in 1/ℓ_node units (not k=1 Compton). The substrate-native curl eigenvalue at chair-ring + 1-step K4 is 12× below continuum (1,1) prediction at corpus geometry.

**Round 11 (vi) closure interpretation:**

The framework's claim "trapped photon = (1,1) Beltrami at corpus geometry on chair-ring + 1-step K4" doesn't hold at this substrate resolution. The chair-ring + 1-step K4 substrate at K4 sampling density CAN'T host the canonical Beltrami trapped CP photon — discrete spectrum is 12× below continuum prediction.

**This is empirically supported across 4 driver versions** with consistent Mode II/III results regardless of IC class.

Round 11 secondary candidates (i)/(iii) are now load-bearing. The path forward is either:
- (i) finer-than-K4 substrate to test if continuum (1,1) Beltrami works at higher resolution
- (iii) different topology (alternate K4 cycle, e.g., 12-node) to test if a longer ring's discrete spectrum has eigenvalues closer to Compton

Either is substantial work. Round 11 (vi) closure-narrative: the corpus electron at canonical (1,1) Beltrami structure is **NOT empirically supported** on K4 chair-ring at bond-pair scale; framework needs substrate-resolution refinement OR topology variant.

---

## §6 — Auditor-lane queue additions

- **A43 v17 candidate (added 2026-04-29):** unit-conversion error in Stride 3 (doc 90 §2 + §10) — k_in_lnode_units = k_eigenvalue × √3 was wrong; should DIVIDE by √3. Doc 90 has corrected per Rule 12 footnote here. Auditor-lane formal entry.
- **Doc 90 §2.2-§2.3, §10.1 correction footnotes** per Rule 12 retraction-preserves-body — original analysis preserved with corrections noted.
- **v9 → Round 11 (vi) closure narrative:** v9 Mode III with corrected eigenmode IC confirms the v8 walkback. The chair-ring + 1-step K4 substrate at K4 sampling density doesn't host the corpus electron's canonical Beltrami structure. Round 11 secondary candidates (i)/(iii) are next.

---

## §7 — References

- [Doc 86](86_path_alpha_v7_helical_beltrami_thermal_sweep.md) §7 gate decision (Round 11 trigger condition)
- [Doc 87](87_path_alpha_v8_round_11_ignition.md) §7 v8 Round 11 ignition + candidate enumeration
- [Doc 88](88_round_11_vi_stride_1_a43_v14.md) Stride 1: A43 v14 + dimensional inconsistency
- [Doc 89](89_round_11_vi_stride_2_topological_mismatch.md) Stride 2 + Grant correction (3D-connected)
- [Doc 90](90_round_11_vi_stride_3_discrete_eigenmode.md) Stride 3 discrete eigenmode (with §1 correction footnote needed)
- [`r10_path_alpha_v9_discrete_eigenmode.py`](../../src/scripts/vol_1_foundations/r10_path_alpha_v9_discrete_eigenmode.py) v9 driver
- [`r10_path_alpha_v9_discrete_eigenmode_results.json`](../../src/scripts/vol_1_foundations/r10_path_alpha_v9_discrete_eigenmode_results.json) v9 result
- [`COLLABORATION_NOTES.md`](../../.agents/handoffs/COLLABORATION_NOTES.md) Rule 14, 16, A40, A43 v2/v14/v15/v16/v17
