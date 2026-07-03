# RESULT — Writhe arc GATE-0: pair feasibility

**Status:** RUN-COMPLETE. **VERDICT: STABLE-IN-A-WINDOW** (RR pairs stable for d ≥ 34 cells = 1.5·L_core; near-contact d=24 UNSTABLE). **Transmission question: T-SYMMETRY-ZEROED** (probed numerically) + answered analytically. **The arc PROCEEDS** to steps 1–5 — HELD for Grant's review, with the stable-d window {34, 44} as the measurement domain.
**Prereg (FROZEN):** [`2026-07-03_writhe-gate0-pair-feasibility_prereg.md`](2026-07-03_writhe-gate0-pair-feasibility_prereg.md)
**Charter:** [`_orchestration/2026-07-02_writhe-force-ratio-build-brief.md`](../_orchestration/2026-07-02_writhe-force-ratio-build-brief.md) (§3 step 0)
**Driver:** [`src/scripts/vol_4_engineering/writhe_gate0_pair_feasibility.py`](../src/scripts/vol_4_engineering/writhe_gate0_pair_feasibility.py)
**Results:** `src/scripts/vol_4_engineering/writhe_gate0_pair_feasibility_results.json`
**Branch:** `analysis/writhe-gate0-pair-feasibility` (PR for orchestrator audit + Grant merge; NO self-merge).
**Classification (`consistency-vs-emergence`):** CONSISTENCY-class. **NO |F| ratio claim of any kind** (that is the HELD campaign).

---

## 1. Validation gates (the honest floor — runs FIRST, gates everything)

| gate | requirement | measured | PASS? |
|---|---|---|---|
| S1 static planted-integer floor | Q_link=3, w_tor=2, null=0 | Q_link=3, w_tor=2, null_Q_link=0 | ✅ |
| live single knot in Gate-0 N=96 | reads (w_tor, w_pol)=(2,3) | (2, 3), alias 0.167 | ✅ |
| **validate-on-known overall** | both above | | **✅ PASS → pair verdicts count** |

The setup reproduces the S1 single-knot result in the Gate-0 N=96 domain before any pair verdict is taken (prereg §3.4). A pair failure below is attributable to the pair, not to a broken setup.

---

## 2. The mini-bin that fired: STABLE-IN-A-WINDOW (prereg §4 bin 3)

RR pair d-sweep, all thresholds frozen in the prereg (§3), window = 600 steps (the S1-certified conservation window), warmup 50, 7 reads + endpoint:

| d (cells) | d / L_core | verdict | winding (all reads) | E_frac end | sep drift | alias max | failing criteria |
|---|---|---|---|---|---|---|---|
| 24 | 1.09 (near-contact) | **UNSTABLE** | (3,3) at step 340 (else (2,3)) | 0.9418 | 0.0099 | **0.50** | `winding_conserved`, `alias_ok` |
| 34 | 1.55 (intermediate) | **STABLE** | (2,3) all 8 reads | 0.9504 | 0.0001 | 0.25 | — |
| 44 | 2.00 (well-separated) | **STABLE** | (2,3) all 8 reads | 0.9503 | 0.0000 | 0.25 | — |

**BIN: STABLE-IN-A-WINDOW.** Stable at d ∈ {34, 44}, UNSTABLE at d=24. The stable-d window IS the measurement domain for the HELD campaign.

### 2.1 The numbers, read honestly

- **d=34 and d=44 are cleanly STABLE.** Both knots read (2,3) at every one of the 8 checkpoints (steps 85→600); interior ω-energy retained 95.0% (≥50% floor); separation drift 0.0001 / 0.0000 (≤30% bound); alias max 0.25 (≤0.34 tolerance). No merger (peaks never approached 0.5·d₀), no dispersal, winding integer held. The pair is a genuine two-knot bound configuration at controlled separation.
- **d=24 (near-contact, ~1 core-diameter gap between the R=11 torus centers, 2R=22) is UNSTABLE — and the failure is precise, not catastrophic.** The knots do NOT disperse (E retained 94.2%) and do NOT merge (separation held 24.7–25.3). The failure is a **single transient winding-integrity break at step 340**: both knots momentarily read **(3,3)** with alias **0.50** (> the 0.34 tolerance), then recover to (2,3) for the remaining reads. Per the frozen criteria (7/7 reads must be (2,3), alias ≤ 0.34), this fails `winding_conserved` and `alias_ok`. Interpretation: at near-contact the two tori's tube fields overlap strongly enough to transiently corrupt the poloidal winding read of the near sides — the winding DOF is not cleanly separable per-knot at d ≈ 1·L_core. This is a real "the pair-force observable is not well-defined at this d" signal (the near-knot winding is contaminated), captured exactly as the prereg intended, not a rescue-able numerical glitch.

### 2.2 Enantiomorph cross-check (optional, labeled — prereg §1.2)

The LL (both-enantiomorph) pair sweep MATCHES RR exactly: LL bin = STABLE-IN-A-WINDOW (d=24 UNSTABLE, d=34/44 STABLE), identical energy/alias numbers. `LL_matches_RR = True`. The pair-feasibility physics is handedness-agnostic at this gate, as pre-registered — no red flag (a divergence would have been surfaced to Grant, not silently resolved).

---

## 3. The transmission question — status: T-SYMMETRY-ZEROED (probed) + answered analytically

The brief's Gate-0 amendment: can a parity-even linear medium carry the wall-generated handedness-dependent stress to a mid-plane T⁰ⁱ, or must the inter-knot region be driven near-yield?

### 3.1 Answered analytically (prereg §5.1)

**Load-bearing architectural finding (flag-don't-fix):** the κ_chiral saturation-bias term `_reflection_density_asymmetric` (`A²_μ = (1 + κ_chiral·h_local)·A²_μ_base`) lives in the **JAX `CosseratField3D` engine** (`src/ave/topological/cosserat_field_3d.py:554`) — **NOT** in the S1 seed host `CrystalGraftV4`. (The brief cites the path as `src/ave/core/cosserat_field_3d.py`; the actual path is `src/ave/topological/…` — a citation-path discrepancy in the brief, flagged.) In the S1 isolated-knot host the buckle is OFF, so **no κ_chiral term is active at all**. In this host handedness is a purely geometric/kinematic property of the seeded ω-winding sign, evolving under the LINEAR ω wave equation `a_ω = c_ω²∇²ω − ω_gap²ω`.

**Consequence:** the candidate mid-plane carrier is the ω-sector field-momentum flux `T⁰ˣ_ω = (∂_tω)·(∂_xω)` (the winding carrier's own momentum flux, the ω analogue of the mass-sector scalar). Because the ω wave equation is linear, two knots' overlap is a linear superposition and the momentum flux is quadratic in ω — so a cross-term exists that flips sign under mirroring one knot. **Analytical answer: wall-supplied saturation is NOT required for a handedness-imprint in this host; the linear ω overlap already carries a handedness-dependent quadratic momentum-flux cross-term, without driving the cold medium near yield.** This must be (and was) tested, not assumed.

### 3.2 Probed numerically — T-SYMMETRY-ZEROED (prereg §5.2)

On the stable RR pair (d=34), mid-plane ω-T⁰ⁱ over the window:

| quantity | value | reading |
|---|---|---|
| `\|Φ_mid\|_max` | 1.35e-16 | machine-zero |
| single-knot floor (max) | 6.56e-3 | nonzero (one off-center knot's breathing reaches XC) |
| ω-flux oddness residual `max\|T⁰ˣ(x)+T⁰ˣ(N−1−x)\|` | 2.12e-15 | machine-zero |
| ω-flux amplitude | 1.39e-1 | the T⁰ˣ scale |
| mid-plane ω overlap amp | 2.00e-2 | the knots DO overlap at XC |
| flux-odd-symmetric | True | odd-resid ≪ 1% of flux amp |

**Verdict: T-SYMMETRY-ZEROED.** The RR pair's `Φ_mid` is machine-zero (1.35e-16) NOT because there is no field at the mid-plane — the knots demonstrably overlap there (mid ω amp 2.00e-2) — but because the **ω-momentum-flux T⁰ˣ is EXACTLY ODD about XC** (odd-residual 2.12e-15 ≪ 1% of flux amplitude 0.139). The face-integral of an odd density is zero by antisymmetry. This is precisely the mass-sector M2 caveat (`mass_sector_field_momentum_T0i.py:276`: for a symmetric head-on pair, T⁰ˣ is odd about the face → "Φ_x = 0 by reflection symmetry … SYMMETRY-FORCED").

**This is the parity-EVEN observable being symmetry-zeroed — NOT a transmission null, and explicitly NOT a cold-medium wrong-regime null** (the brief forbids booking one). The handedness signal is parity-ODD, and the like-handed RR (and LL) configurations are mirror-symmetric in exactly the way that zeroes a parity-even mid-plane flux. **Resolving whether a handedness-dependent stress reaches the mid-plane requires the parity-ODD RL/LR configurations** — which are the HELD four-configuration campaign (brief steps 1–5), not Gate-0.

### 3.3 A driver-time symmetry-detector correction (flag-don't-fix, recorded)

The first run's transmission bin was mislabeled T-DOCUMENTED-OPEN by a naive symmetry detector that used the FULL vector-field mirror `ω(x) vs ω(N−1−x)` (residual 0.57 → "not symmetric"). That test is WRONG for a winding pair: a spatial mirror also flips the internal winding chirality, so an RR pair is neither pure-even nor pure-odd under it even though its FLUX is exactly odd. The detector was corrected to test the physically correct quantity — the oddness of the flux T⁰ˣ about XC — which lands the pre-registered T-SYMMETRY-ZEROED bin. Both runs produced identical stability numbers; only the transmission-bin attribution changed (correctly).

---

## 4. Reproducibility

Two independent full runs (`--with-LL`) produced **identical stability numbers** (winding reads, E_frac, sep drift, alias, Φ_mid, floor). The verdict is not run-to-run fragile. Every printed number is computed in-run (`ave-driver-script-honesty`); validate-on-known gates the pair verdict.

---

## 5. What Gate-0 does NOT establish (honest scope — prereg §6)

- **NO |F| ratio claim of any kind.** Gate-0 measured pair feasibility + per-knot winding conservation + (on the stable RR pair) a mid-plane ω-T⁰ⁱ presence/symmetry check. It did **not** measure `R = |F|_co / |F|_anti`, did **not** compare RR vs RL/LR forces, did **not** touch the four-configuration campaign. That is the HELD arc.
- **NO handedness-force claim.** The T-SYMMETRY-ZEROED result establishes only that the parity-EVEN mid-plane flux of a like-handed pair is symmetry-forced to zero — it says NOTHING about whether a co-vs-anti force ratio ≠ 1 exists. The parity-odd contrast (the actual chord candidate) lives in the RL/LR configs (HELD).
- **NO emergence claim.** CONSISTENCY-class only.
- **Scope of the host.** All results are on the S1 isolated-knot host (`CrystalGraftV4`, buckle OFF). The κ_chiral saturation engine (`CosseratField3D`, JAX) is a DIFFERENT code path not exercised here; Gate-0 says nothing about that engine's pair behavior — and the transmission analysis (§3.1) shows the κ_chiral term is not the mechanism in THIS host.
- **The unstable end.** The pair-force observable is NOT well-defined at d ≈ 1·L_core (d=24: transient winding contamination). The HELD campaign's measurement domain is the stable window d ∈ {34, 44} (≥ 1.5·L_core), where the near-knot winding reads cleanly.

---

## 6. What survives + what the arc proceeds with (for Grant's review of the HELD campaign)

- **The engine CAN host a controlled winding pair** — the pair-force observable is well-defined at current engine capability, in the window d ∈ {34, 44} cells (1.5–2.0·L_core). The Cleave lesson held: the cheap-decisive Gate-0 ran before the expensive campaign and returned a clean, actionable answer.
- **A validated pair driver** (`writhe_gate0_pair_feasibility.py`): S1-seed reuse + lossless roll translation + per-knot local-frame readout + half-region centroid tracking + the ω-sector T⁰ⁱ observable — reusable for the four-configuration campaign.
- **Two driver-time corrections** (Rule 10, both recorded): (1) knot centers are the half-region ω-energy CENTROIDS, NOT the top-2 |ω|² peaks (which land on tube crossings); (2) the flux-oddness test (not the full-vector mirror) is the correct symmetry statement for a winding pair's Φ_mid.
- **The transmission question is set up for the HELD campaign:** the mechanism in this host is the linear ω-overlap quadratic momentum-flux cross-term (§3.1), and the like-handed configs symmetry-zero the parity-even mid-plane flux (§3.2) — so the campaign must read the parity-ODD RL/LR contrast to answer transmission. Do NOT book the RR/LL Φ_mid=0 as a cold-medium null.
- **HELD (pending Grant's review):** the four-configuration T⁰ⁱ campaign (brief steps 1–5) — RR/LL/RL/LR at matched separation, the ratio R = |F|_co/|F|_anti, the knob-invariance + α→2α tests, the separation-scaling, and the SM-counterfactual + prior-art scan. Gate-0 does not start it.
