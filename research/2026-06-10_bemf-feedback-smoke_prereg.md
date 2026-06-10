# BEMF-feedback SMOKE — close the OBSERVED-NOT-FED-BACK loop as the inductive reaction-half (PREREG, FROZEN)

**Date:** 2026-06-10 · **Branch:** `analysis/2026-06-10-bemf-feedback-smoke` (off `analysis/2026-06-10-graft-v4-photon-helicity`) · **Lane:** implementer
**Engine (NEW):** [`src/ave/core/crystal_graft_bemf.py`](../src/ave/core/crystal_graft_bemf.py) (subclass of `CrystalGraftV4`)
**Driver:** [`src/scripts/vol_1_foundations/bemf_feedback_smoke_run.py`](../src/scripts/vol_1_foundations/bemf_feedback_smoke_run.py)
**Status at freeze:** outcome bins + test design + the derived reaction term FROZEN before the headline saturation/payment numbers. Apparatus pre-checks done (sign-probe + OFF-reproduces-5.035) and recorded in §6 as calibration, not adjudication.

## §0 — GRANT RATIFICATION (2026-06-10, recorded VERBATIM)

> The locked-motor unification — **BEMF = the payment** (drive balanced by back-EMF at steady state), **cavitation pocket = the compliance**, the **C3 commit = the latch** — components of ONE circuit, not competitors.

HARD CONSTRAINTS: canonical-AVE-only; pure-corpus.

## §1 — THE TARGET (verified, `verify-before-cite`)

The corpus convergence (electron-synthesis-epic §7, line 81, commit `fe896f12`, Grant 2026-06-07, verbatim):

> **★ CONVERGENCE (Grant 2026-06-07) — the missing equilibration channel IS the dark-wake/back-EMF, OBSERVED-NOT-FED-BACK.** `DarkWakeObserver` (`vacuum_engine.py:1457`) measures the lattice's mutual-inductance back-EMF (`M_inertial≡L_drag`, `:1478`) but is **read-only — `τ_zx`/back-EMF is absent from the EOM**.

The engine computes a BEMF-class observable (`DarkWakeObserver`, τ_zx ∝ Z_local·∂|V|²/∂x) but never feeds it to dynamics. **This test closes that loop as PHYSICS** — the Lenz reaction as the conservative REACTION-HALF of the chiral source coupling (the functional-derivative pair the v2 H_couple validated), NOT an ad-hoc damper bolted on.

**Why this is needed (the v4 failure, `verify-before-cite` against `2026-06-10_graft-v4-photon-helicity_result.md`):** v4's rigid-rotation LOCK (`π_ω ← π_ω − η·Ω×r`) was demoted **C → LOCK-FAIL** by a 4-lens panel: the |L_ω| doubling ratio was **RH 5.03 / χ-null 3.97 / live-wall 5.19** vs the **1.3** gate, and **η-INVARIANT** (5.27→5.65 as η 0.1→0.5) — the *linear-damper-against-a-growing-source* signature: the source never paid for its torque. The named gap: *"a non-depleting chiral director that never pays for its torque — the missing primitive is a BOUNDED, helicity-TRANSFERRING coupling."*

## §2 — FROZEN CONFIG (the v4 RH runaway config; UNCHANGED across all compared arms)

`N=72`, `pml_thickness=6`, `source_mode=abc`, `lam_sign=1`, `(p,q)=(2,3)`, `S_min=2e-3`, `A_cap=0.999`, `omega_gap=1.0`, `wall_center=0.62`, `wall_width=0.30`, `κ̃=6/5`. Seed: breather `(σ=14, frac=0.999)` + RH photon `(σ=9, λ=10, amp=0.35, helicity=+1)`. Frozen wall window. `n_steps=1200`; |L_ω|_max checkpoints `(300, 600, 1200)`; `ratio_4L = L_max(1200)/L_max(300)`; STOP gate `≤ 1.3`. **OFF arm verified to reproduce the v4 baseline `5.035`.**

## §3 — THE DERIVED LENZ REACTION TERM (`ave-fundamental-ground-up-implementation`; STEP 2)

The v4 source coupling is the **capacitive/potential** half of the LC tank (frozen `g`, live photon `w`):

```
H_couple = κ̃ ∫ g_wall · V · [w·(∇×ω)]        f_V = −κ̃ g[w·(∇×ω)] ;  f_ω = −κ̃ ∇×(g V w)  (BUCKLE)
```

It conserves `E_V+E_ω+H_couple` but pumps |L_ω| secularly (≈t^2.2) — no inductive term opposes the RATE of buildup. The **missing reaction-half is the inductive/kinetic MIRROR of the SAME coupling** — a single Lagrangian velocity-coupling term:

```
L_BEMF = κ_L ∫ g_wall · [w·(∇×ω)] · V̇          (the mutual-inductance / back-EMF energy)
```

whose Euler–Lagrange conjugate pair is:

```
f_V^BEMF = −κ_L g [w·(∇×π_ω)]      (BACK-EMF on the source ∝ circulation RATE π_ω  =  −dΦ/dt, Lenz)
f_ω^BEMF = +κ_L ∇×(g π_V w)        (forward inductive drive on ω ∝ source RATE π_V, the conjugate)
```

**Conservative / reactive, NOT a damper:** `P_V^BEMF + P_ω^BEMF = ∫f_V^BEMF·π_V + ∫f_ω^BEMF·π_ω = 0` exactly in the continuum (curl integration-by-parts). The BEMF does NO net work — it TRANSFERS reactively between source (V) and circulation (ω), exactly as a motor back-EMF stores/returns rather than dissipates. **This is the capacitive buckle (C) + inductive BEMF (L) = the full reactive LC tank = Grant's locked-motor unification (one circuit).**

**Reconciliation observer vs dynamics (per brief):** the `DarkWakeObserver` τ_zx ∝ Z_local·∂|V|²/∂x is a **V-sector-only METER** of the same Lenz back-reaction (it cannot see the ω circulation). `f_V^BEMF = −κ_L g[w·(∇×π_ω)]` is the **TRUE cross-sector DYNAMICAL reaction** (couples to the circulation rate). Same `M_inertial≡L_drag` physics; the **functional-derivative form IS the dynamics, τ_zx IS the meter**. A crystal-engine `tau_zx_proxy()` is computed only as the cross-check; never fed back.

**GAIN:** `κ_L` = the inductive coupling gain. **DERIVED value `κ_L = κ̃ = 6/5`** (the inductive half of the SAME mutual coupling — same geometry). Adjudication requires the verdict be **gain-robust** across a κ_L sweep OR the gain DERIVED; a tuned gain is a FLAG. α-free (κ_L inherits κ̃ topology; the Lenz sign is ±1).

## §4 — OUTCOME BINS (FROZEN; Rule 11 — applied to the data, not moved to fit)

Arms: **OFF** (`κ_L=0`, reproduces the v4 runaway), **BEMF_pos** (`+κ_L`), **BEMF_neg** (`−κ_L`). Run at the v4-lock config (lock_eta=0.05, PRIMARY) and lock-OFF (BEMF-alone, SECONDARY).

- **PAYS-AND-BOUNDS** — |L_ω| ratio_4L → **1.0** (≤1.3) on the LENZ sign; AND the PAYMENT signature emerges: source-delivered power into the rigid-rotation mode falls as the back-EMF rises, **steady-state drive≈BEMF**, the source-side reservoir transfers to the circulation through the reactive BEMF channel (`work_V<0`, `work_omega>0`), **ledger-closed** (`|work_V+work_omega|/|work_omega|` ≤ the measured floor); AND the operator-consistent stencil ledger does NOT detonate.
- **BOUNDS-WITHOUT-PAYING** (suspicious — a damper in disguise) — |L_ω| bounds but WITHOUT the payment signature: either the bounding sign DRAINS the circulation back to the source (`work_omega<0` — a reactive brake, not a motor), or the stencil ledger drifts DOWN (dissipation).
- **DETONATES** (the trilinear failure mode recurs) — |L_ω| and/or max|ω| and/or the stencil ledger blow up under the LENZ sign. Honest C; localize why the reaction-half differs from v4's depleting (`photon_deplete=True`) coupling.
- **INERT** — sign-flip does nothing: BEMF_pos ≈ BEMF_neg ≈ OFF (ratio within the floor). The feedback does not couple.

**The FALSIFIABLE control (frozen):** **ANTI-LENZ (the sign opposite the bounding one) must detonate FASTER than OFF** (higher ratio_4L and/or growing max|ω|). If the sign-flip does nothing → INERT. The sign-probe (§6) found `+κ_L` is the **source-depletes** direction (`work_V<0`); the PREDICTION is that the bounding sign and the source-depleting sign COINCIDE (the motor picture) → `+κ_L` = LENZ. If instead `−κ_L` (circulation-draining) is the only bounding sign → BOUNDS-WITHOUT-PAYING.

## §5 — APPARATUS-FLOOR ATTRIBUTION (`ave-apparatus-floor-attribution`; measure MY config's floor FIRST)

- **Ledger-closure floor:** `|work_V+work_omega|/|work_omega|`. Sign-probe measured `≈ 4.5e-8/1.69 ≈ 2.7e-8` (machine-precision; the conjugate pair cancels exactly). The payment-ledger closes WAY above any ±6.5%-class instrument floor.
- **|L_ω| ratio floor:** OFF reproducibility (deterministic FDTD, no RNG → bit-identical) + the `κ_L→0` continuity (a tiny κ_L must reproduce OFF) + `no_photon` (no source ⇒ |L_ω|≈0, ratio is noise). The 1.0-gate is saturation-across-doublings, NOT the secular-blind bound.
- **Clip/sweep:** the only new knob is `κ_L`. Verdict must be gain-robust (κ_L sweep ±{0.3,0.6,1.2,2.4}) or the gain DERIVED (κ_L=κ̃=6/5). `max|ω|` is the detonation gate (PML-excluded, `omega_intensity`).

## §6 — APPARATUS CALIBRATION (pre-freeze; recorded, NOT adjudication)

1. **OFF reproduces v4:** unified single-trajectory `ratio_4L = 5.035` (vs v4 `5.03`). Method EXACT (deterministic prefix = separate-run doubling).
2. **Conjugate pair exact:** sign-probe `work_V+work_omega = −4.5e-8` vs `|work| ≈ 1.69` — the BEMF is reactive (no net work), confirming reaction-half not damper.
3. **Sign of transfer:** `+κ_L` ⇒ `work_V<0, work_omega>0` (source→circulation = payment direction); `−κ_L` reverses.
4. The naive `H_total` (½c0²|∇V|²) drifts ~+35% in OFF too — the known undepleting-photon pump; the ledger uses the operator-consistent `stencil_energy` (E_V_lin, E_omega, H_couple) + tracks the BEMF channel separately.

**Skills fired:** `substrate-native-check` (CP9 dynamical not heuristic; CP10 boundary frozen-wall coupling), `ave-conserved-vs-pumped` (the BEMF energizes+locks reactively, the source pays the circulation), `ave-apparatus-floor-attribution` (§5), `ave-fundamental-ground-up-implementation` (§3, both halves from ONE Lagrangian), `ave-driver-script-honesty` (all numbers from the evolved field), `ave-canonical-source` (the canonical back-EMF chain), `verify-before-cite` (§1 quote + v4 result re-greped), `phase-space-coordinate-check` (|L_ω| and the ω reactance pair are the native coordinates; the BEMF couples the velocity quadratures π_V, π_ω).
