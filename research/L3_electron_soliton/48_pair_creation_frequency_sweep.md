# 48 — Phase III-B Pair-Creation Frequency Sweep (σ(ω) Falsifiable Prediction)

**Status:** in progress (sweep running 2026-04-22) — **placeholder doc; results to be appended when sweep completes**
**Parent plan:** `~/.claude/plans/document-list-for-next-chat-compressed-thunder.md` Stage 3
**Depends on:**
  - [46_vacuum_engine_scope.md](46_vacuum_engine_scope.md) — engine architecture + C1-C6 findings
  - [47_thermal_lattice_noise.md](47_thermal_lattice_noise.md) — thermal-state derivation
  - [44_pair_creation_from_photon_collision.md](44_pair_creation_from_photon_collision.md) (reframed) — Phase III-B first attempt

**Purpose:** First full test of `VacuumEngine3D` (Stage 2 deliverable). Measures
the falsifiable prediction C5 from doc 46_: **σ(ω) has a knee near ω·τ_relax ≈ 1
if the cascade-saturation mechanism is active in AVE pair creation**.

## 1. Experimental design

### 1.1 Configuration matrix (4×3×2 = 24 runs)

| Parameter | Values | Physical meaning |
|---|---|---|
| Wavelength λ (cells) | {3.5, 5, 7, 10} | ω·τ_relax = {1.80, 1.26, 0.90, 0.63} — spans crossover |
| Amplitude (V_SNAP units) | {0.3, 0.5, 0.7} | Standing-wave anti-node peaks at 0.6, 1.0, 1.4·V_SNAP |
| Temperature (m_e c² units) | {0, 1.7e-2} | T=0 cold null (C1 control); T~10⁸ K for pair regime |

### 1.2 Engine setup (per run)

- `VacuumEngine3D(N=48, pml=6, temperature=T, amplitude_convention="V_SNAP")`
- Two `CWSource` counter-propagating at x=8 and x=40 with t_ramp=20, t_sustain=150
- Observers: `RegimeClassifierObserver`, `TopologyObserver`, `EnergyBudgetObserver`
- Run 240 outer steps

### 1.3 Pre-registered predictions

- **P_IIIb-α** (cold vacuum baseline): at T=0, no Cosserat response at any (λ, amp).
  Confirms C1 — cold vacuum is deterministic, cannot bootstrap pair creation.
  **Expected outcome:** `max A²_cos < 1e-6` across all 12 cold runs.

- **P_IIIb-β** (classical regime): at T>0, λ=10 (ω·τ = 0.63, below crossover),
  Cosserat response scales with amplitude. If pair forms, classical-Schwinger-like.

- **P_IIIb-γ** (cascade regime): at T>0, λ=3.5 (ω·τ = 1.80, above crossover),
  Cosserat response is ENHANCED compared to λ=10 at same amplitude.
  **This is the specific cascade signature from Thread 1 of pre-Phase-III research.**

- **P_IIIb-δ** (knee signature): at T>0, σ(ω) shows a sharp or smooth knee near
  ω·τ_relax ≈ 1. If absent, the cascade mechanism is amplitude-only (no frequency
  enhancement).

## 2. Results

*TO BE FILLED IN AFTER SWEEP COMPLETES.*

### 2.1 Raw results table

| Run | λ | amp | T | ω·τ | max A²_total | max A²_cos | max Q_H | max #centroids | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| — | — | — | — | — | — | — | — | — | — |

### 2.2 Cold-vacuum control (T = 0, 12 runs)

*[max A²_cos across all cold runs here]*

### 2.3 σ(ω) at fixed amplitude (the key plot)

*[Insert `/tmp/phase_iiib_sigma_omega.png`]*

### 2.4 Verdicts against pre-registered predictions

| Prediction | Adjudication | Evidence |
|---|---|---|
| P_IIIb-α | — | — |
| P_IIIb-β | — | — |
| P_IIIb-γ | — | — |
| P_IIIb-δ | — | — |

## 3. Interpretation

*TO BE FILLED IN.*

### 3.1 What the data says about the cascade mechanism

*[if σ(ω) has a knee near ω·τ = 1: cascade confirmed]*
*[if σ(ω) is flat: amplitude-only response, cascade NOT a frequency-dependent effect in AVE]*
*[if σ(ω) has a different shape: new physics, document it]*

### 3.2 What the data says about temperature dependence

*[compare T=0 vs T>0 results at matched (λ, amp) points]*

### 3.3 What the data says about the S1-D coupling

*[does the current coupling produce reasonable pair-creation dynamics, or is an augmented Lagrangian needed?]*

## 4. Implications and next steps

*TO BE FILLED IN BASED ON RESULTS.*

## 5. Artifacts

- [`src/scripts/vol_1_foundations/vacuum_engine_pair_creation.py`](../../src/scripts/vol_1_foundations/vacuum_engine_pair_creation.py)
- `/tmp/phase_iiib_sweep.npz` — raw results
- `/tmp/phase_iiib_sweep_summary.png` — 4-panel summary
- `/tmp/phase_iiib_sigma_omega.png` — σ(ω) falsifiable-prediction plot
- `/tmp/phase_iiib_sweep_log.txt` — per-run log

## 6. Known limitations flagged forward

- **N=48 instead of N=64**: smaller lattice for compute budget. If interesting
  features emerge, rerun top configs at N=64 for refinement.
- **T>0 uses classical Maxwell-Boltzmann** (P1-C path from parent plan),
  not full K4-eigenmode thermal distribution. Deferred unless results demand it.
- **Temperature of "1.7e-2 m_e c²"** corresponds to ~10⁸ K — far above any physical
  lab conditions. Represents early-universe pair-creation-regime temperature.
- **Centroid count** uses `threshold_frac=0.3` and `min_cluster_size=8`; on noisy
  thermal-initialized states these may produce spurious "noise bumps" rather than
  physical solitons. Post-hoc filtering may be needed if many small centroids appear.
