# CRUX result: A²_μ (K4↔Cosserat / Op14 trace-reversal microrotation) does NOT scale with resonant Q — WALL, not KNOB

**Date:** 2026-06-09 · **Branch:** `analysis/2026-06-09-a2mu-vs-Q-crux` (off `analysis/2026-06-09-saturation-temporal-preregs`)
**Status:** RESULT — clean negative. The resonant-Q-compensation hypothesis is **falsified**.
**Driver:** `src/scripts/vol_1_foundations/a2mu_vs_Q_crux.py` (+ `..._lockwindow.py`) · **Data:** `research/2026-06-09_a2mu-vs-Q-crux_data.json` · **Figure:** `research/2026-06-09_a2mu-vs-Q-crux_figure.png`

---

## VERDICT (one box)

| axis | finding |
|---|---|
| **Three-way** | **WALL** — composite: dominantly **WALL-engine** (no dynamical K4→microrotation pump that scales with Q), with the cold-start floor being **WALL-physics** (framework-predicted traceless-photon null). **NOT a KNOB.** |
| **A²_μ measured…** | **DYNAMICALLY** — read the actually-evolved `engine.cos.omega` curvature (`PairNucleationGate._compute_A2_mu`). The algebraic chirality factor `(1+κ_chiral·h)` is a ≤0.88 % modulation and cannot move the verdict. |
| **A²_μ vs Q range** | Cold: **0.000 exactly** at all Q (autoresonant ≡ fixed-f). Seeded: **flat 0.0039 → 0.012** across a **10× range of A²_K4 build-up**, identical legacy-pump-ON vs A28-pump-OFF. **Zero Q-scaling.** |
| **Stable A²_μ≈1 lock?** | **NO.** Hard cliff: A²_μ sits at the seed floor while K4 is sub-rupture, then **detonates to 10⁵–10⁷** the instant K4 ruptures (A²_K4>1). It crosses the entire [0.012, 1] range and the bound-state band [0.5, 2] in a single step. `in_band_run = 0` everywhere (one isolated transient record at amp=1.15). |
| **Hypothesis** | `Q=α⁻¹≈137` resonant cavity lifts A²_μ from O(α) to O(1): **FALSIFIED.** |

---

## 1. The crux question

The AVE-distinct symmetric/gravity/electron branch hinges on the K4↔Cosserat trace-reversal coupling
(`Op14 = z_local`). That coupling is **α-weak**: `κ_chiral = α·κ̃(p,q)`
(`src/ave/topological/cosserat_field_3d.py:110-119`; for the electron (2,3) winding
`KAPPA_CHIRAL_ELECTRON = α·1.2 ≈ 8.757e-3`, verified at runtime). Un-amplified, the documented
Cosserat microrotation saturation sits at **A²_μ ≈ 0.012 ≈ O(α)**
(`research/_archive/L3_electron_soliton/70_phase5_resume_methodology.md:58`, verbatim:
*"Gate still NO-FIRE because Cosserat A²_μ peaked at 0.012 (K4→Cosserat coupling weakness)."* — VERIFIED).

**Hypothesis under test:** a resonant cavity at `Q = α⁻¹ ≈ 137` makes `Q·κ_chiral ~ O(1)`, lifting A²_μ to O(1)
and (per the refined question) locking it at the Γ=−1 bound-state boundary A²_μ≈1 — the electron-stability condition.

---

## 2. substrate-native-check — the load-bearing dynamical-vs-heuristic distinction (FIRED)

Walked before any code. The decisive structural facts, read from the engine:

1. **A²_μ depends ONLY on the Cosserat ω-field curvature.** `A²_μ_base = κ(ω)²/ω_yield²`
   (`cosserat_field_3d.py:511`, `_reflection_density_asymmetric`; ω_yield = π, verified). The K4 voltage V²
   feeds **A²_ε** (electric sector), *not* A²_μ. So a K4 drive can raise A²_μ **only indirectly**, by pumping ω.
2. **The only dynamical V→ω pump is `CoupledK4Cosserat._compute_coupling_force_on_cosserat()`**
   (`k4_cosserat_coupling.py:412-458`), the `∂L_c/∂(u,ω)` force added each Cosserat sub-step. It returns
   **exactly zero** when `disable_cosserat_lc_force=True` — the **A28 double-count correction**
   (`k4_cosserat_coupling.py:240-251`). Under A28-correct, there is **no** dynamical K4→microrotation pump.
3. **At ω=0 the pump force vanishes (ω=0 is a fixed point).** A cold, *traceless* photon carries no
   trace to reverse into the microrotation — exactly the picture in
   `2026-06-09_electron-emergence-self-focusing-tracereversal-picture.md` §0. Corpus-confirmed:
   `research/_archive/L3_electron_soliton/50_autoresonant_pair_creation.md:131` (VERIFIED) —
   *"All 4 T=0 runs give max A²_cos = 0.000 exactly (bit-level)… Autoresonant drive on a cold vacuum behaves
   identically to fixed-f CW — zero Cosserat response."*

**Consequence for the measurement:** to answer KNOB-vs-WALL you must measure the *dynamically evolved* ω, not
an algebraic formula. We do: `_compute_A2_mu` reads `engine.cos.omega`. A `CosseratBeltramiSource`, by contrast,
**directly overwrites ω at a slab** so its A²_μ is *set by the source amplitude* (`A²_μ ≈ (amp·k/π)²`,
`vacuum_engine.py:859-863`) — that is the **algebraic / heuristic** path, run separately as a control.

Checkpoint 7 (PML exclusion): `mask_alive = mask_A|mask_B` does **not** exclude PML; all extractions here AND
the interior box `pml ≤ i,j,k ≤ N−pml−1` (Rule 10). Checkpoint 6 (reactance pair): both C-state (ω/A²_μ) and
L-state (ω_dot) tracked over the window; H reported. Checkpoint 8 (precursor): the generative precursor (photon /
K4 drive) is seeded and the dynamics are let to build ω — the finished (2,3) is never planted.

---

## 3. The Q knob (reported honestly) + anchors

The engine has **no scalar "Q" parameter.** Resonant build-up is governed by (i) **drive amplitude** (sets how
high the driven sector's A² climbs) and (ii) **resonance tracking** — `AutoresonantCWSource` (PLL regenerative
feedback that tracks the Duffing-softened resonance = the high-Q mechanism) vs fixed-f `CWSource` (detuning-limited
= low-Q). We use the **realized peak A²_K4** as the empirical resonant-build-up axis and contrast autoresonant vs
fixed-f as the Q-quality axis.

Anchors (both VERIFIED in source): **0.012** — `70_…:58` (Phase-5e, K4 autoresonant on a T=0.1 *thermally*-seeded
ω). **1.009** — `vacuum_engine.py:104-105` / `doc 50_`; but `doc 50_:57` records the audit:
*"20-seed sweep… 0/20 seeds reach 1.009… The 1.009 headline is now known to be a tail outcome"* (thermal-init
variance, not coupling). See Flag #1.

---

## 4. Method — three arms (N=32, pml=6, ω_yield=π; forward simulation, no fit)

- **Arm 1 — cold T=0, K4-only, legacy pump ON:** AutoresonantCWSource vs fixed-f CWSource, amp ∈ {0.3, 0.6, 1.0}.
- **Arm 2 — seeded ω (clean interior Beltrami, A²_μ≈0.012 anchor) + K4 autoresonant drive:** amp ∈ {0.3, 0.6, 1.0, 1.5},
  run **both** `disable_cosserat_lc_force=False` (legacy pump ON) and `True` (A28 pump OFF). The pure amplification test.
- **Arm 3 — Beltrami-painted ω (algebraic source baseline):** amp ∈ {0.2, 0.5, 1.0, 1.75}.
- **Lock-window confirmation:** legacy pump ON, seed calibrated to realize **exactly 0.01200**, fine amp sweep
  {1.00 … 1.40} with sustained-in-band [0.5, 2.0] detection.

---

## 5. Results

**Arm 1 (cold T=0, K4-only):**

| source | amp | A²_K4 (build-up) | A²_μ | ω_max |
|---|---|---|---|---|
| autoresonant | 0.3 / 0.6 / 1.0 | 0.032 / 0.124 / 0.324 | **0.000 (exact)** | **0.000 (exact)** |
| fixed-f | 0.3 / 0.6 / 1.0 | 0.032 / 0.129 / 0.355 | **0.000 (exact)** | **0.000 (exact)** |

→ Cold photon ⇒ identically zero microrotation; the Q knob (autoresonant vs fixed-f) has **no effect.**
Reproduces `doc 50_:131` in a clean own-run.

**Arm 2 (seeded ω≈0.0035, K4 drive) — the crux:**

| config | amp=0.3 | amp=0.6 | amp=1.0 | amp=1.5 |
|---|---|---|---|---|
| A²_K4 build-up | 0.032 | 0.124 | 0.326 | 7.13 (ruptured) |
| **legacy pump ON** peak A²_μ | 0.003921 | 0.003919 | 0.003916 | **1.205e6** (detonation) |
| **A28 pump OFF** peak A²_μ | 0.003922 | 0.003922 | 0.003922 | 0.003922 |

→ Below K4 rupture, A²_μ is **flat to 4 sig figs across a 10× A²_K4 range AND identical between pump-ON and
pump-OFF** — the dynamical "pump" contributes nothing. At amp=1.5 the legacy pump does **not** lift A²_μ to ~1;
it **numerically detonates to 1.2e6** the moment K4 itself ruptures (A²_K4=7.13). This is the documented A28
double-count pathology (`k4_cosserat_coupling.py:248-250`, *"|ω| grew 1700× in one step"*), not a physical lock.

**Arm 3 (Beltrami-painted, algebraic):** measured interior A²_μ = 0.0004 / 0.0026 / 0.0103 / 0.0318 at
amp = 0.20 / 0.50 / 1.00 / 1.75 — i.e., A²_μ is set by the *source amplitude*, the dynamical coupling plays no
part. (It tops out ~0.032 interior, ~30× below the source's own naive `(amp·k/π)²` estimate, because the
tetrahedral curvature operator + interior/PML masking reduce the realized curvature — and well below the 1.009
anchor, which came from thermal-noise seeding + the strain ε² term + no PML exclusion; see Flag #1.)

**Lock-window confirmation (legacy pump ON, seed realized = exactly 0.01200):**

| amp | A²_K4 | max A²_μ | final A²_μ | rupture | in-band[0.5,2] run | records >1e3 |
|---|---|---|---|---|---|---|
| 1.00 | 0.326 | 1.36e-2 | 5.9e-3 | F | 0 | 0 |
| 1.10 | 1.99 | 2.79e5 | 4.4e4 | T | 0 | 5 |
| 1.15 | 4.38 | 6.28e5 | 6.7e4 | T | **1** | 12 |
| 1.20 | 7.63 | 5.95e5 | 1.5e4 | T | 0 | 17 |
| 1.30 | 7.68 | 8.51e6 | 4.1e3 | T | 0 | 29 |
| 1.40 | 6.81 | 7.97e5 | 8.0e3 | T | 0 | 38 |

→ **Hard cliff, no lock window.** A²_μ stays at the ~0.012 floor while K4 is sub-rupture, then jumps to 10⁵–10⁷
the instant K4 ruptures. It never *sits* in the bound-state band [0.5, 2] — `in_band_run = 0` everywhere except a
single transient record at amp=1.15. The stable A²_μ≈1 boundary-lock the electron-stability hypothesis requires
**does not exist** in this engine.

**Figure:** `research/2026-06-09_a2mu-vs-Q-crux_figure.png` — left: A²_μ vs resonant build-up (peak A²_K4) with the
0.012 and 1.009/rupture anchors; right: seeded-ω A²_μ(t) trajectories (the lone amp=1.5 detonation spike to 1.2e6
vs all others flat at the floor).

---

## 6. Mechanism (why WALL) — single explanation for all arms

Two structural facts, both substrate-native, jointly close the branch:

1. **Traceless-photon null (WALL-physics, framework-predicted).** A²_μ is built from ω-curvature only; the dynamical
   V→ω pump `∂L_c/∂ω` vanishes at ω=0. A cold photon (the physical generative precursor) cannot seed the
   microrotation — ω=0 is a fixed point. This is precisely the
   `…tracereversal-picture.md` §0 claim ("a photon is traceless… carries no volumetric trace to reverse into the
   microrotational sector"). The framework's own picture **predicts** the cold-start null.

2. **The implemented coupling is not a controllable amplifier (WALL-engine).** Given a seed, the only dynamical
   channel (the legacy `∂L_c/∂(u,ω)` force) is either (a) **inert** — below K4 rupture it produces output
   bit-indistinguishable from pump-OFF, with A²_μ independent of Q — or (b) **explosive** — at K4 rupture it is the
   A28 double-count force that detonates A²_μ to 10⁶. There is no regime in which it gently, controllably lifts A²_μ
   toward 1. The α-weak coupling is **not** rescued by resonant build-up: `Q·κ_chiral ~ O(1)` does not manifest as a
   dynamical A²_μ ~ O(1).

The documented "autoresonant reaches A²_cos≈1" is **algebraic source-painting or thermal-noise tail**, never a
resonant amplification of the trace-reversal coupling.

**regime/phase-state framing (`ave-regime-phase-state-check` fired):** A²_μ lives in the **mechanical-shear /
microrotation** sector; the K4 drive in **EM-transverse**. The 0.012 anchor sits at r≈√0.012≈0.11 ≈ r₁=√(2α)≈0.117
— the linear→nonlinear boundary. The hypothesis needs coherent transfer EM-transverse→shear pushing the shear sector
to r→1; the data show no such transfer exists below the K4's own rupture, and above it the response is a non-physical
detonation.

---

## 7. Flags (flag-don't-fix — NOT silently resolved)

- **Flag #1 — engine header overclaims a retracted anchor.** `vacuum_engine.py:104-105` states the autoresonant
  drive *"reaches A²_cos = 1.009 at ω·τ=1.8"* as a clean result. `doc 50_:57,125` retracts it: 0/20 reproducible,
  *"known to be a tail outcome"* (thermal-init variance). The header is **stale** relative to its own audit doc.
  Surfaced for adjudication — not edited here.
- **Flag #2 — Rule 10 PML gap in a canonical driver.** `phase5e_cool_from_above.py:184` extracts A²_μ over
  `engine.cos.mask_alive`, which does **not** exclude PML cells. Minor for that run (the response was tiny) but a
  Rule-10 corollary gap. Surfaced, not edited.
- These do **not** change the verdict; both, if anything, *strengthen* it (the 1.009 "resonance" was never a
  dynamical coupling result).

---

## 8. Classification + provenance

- **DERIVED:** the structural claim that A²_μ couples to the K4 sector *only* via the `∂L_c/∂ω` force, which A28
  zeroes and which vanishes at ω=0 — read directly from engine source (§2).
- **VERIFIED:** both anchors (0.012 @ `70_:58`; 1.009 @ `vacuum_engine.py:104` + retraction @ `doc 50_:57`);
  constants (α, κ_chiral, ω_yield) imported from `ave.core.constants` / measured at runtime; the cold-vacuum null
  reproduced against `doc 50_:131`; all sweep numbers from forward simulation (no fit, no hardcoded physics literal).
- **BLOCKED:** the resonant-Q-compensation route to electron stability. A²_μ does not scale with Q; no stable
  A²_μ≈1 lock window exists. Per **Rule 11 (honest closure)**: one mechanism (the only dynamical pump is the
  A28-double-count force — inert below rupture, detonation above; ω=0 fixed point at cold) explains every arm. The
  branch closes clean. Per **Rule 12 (substitution-not-retraction)**: this slot is *not* refilled with a rescue
  hypothesis here. If a real K4→microrotation pump is to be claimed, it needs a **new** dynamical coupling term
  (not the A28 force) with its own derivation + verification chain and a new version number.

**Skills fired:** substrate-native-check (load-bearing dynamical-vs-heuristic; Checkpoints 6/7/8) · ave-canonical-source
· ave-regime-phase-state-check (shear vs transverse mode; r₁ boundary) · verify-before-cite (0.012, 1.009, κ_chiral,
the doc-50 retraction — all grepped) · ave-driver-script-honesty (constants imported, no fit-to-target, anchors labeled
inputs) · ave-engineering-program-rigor (figure with anchors + savefig).

**Engine integrity:** H reported each step; rupture flagged (A²≥1) — crossed in every legacy-pump amp≥1.1 run (it is
the K4 rupture that triggers the A²_μ detonation), never crossed in any sub-rupture or A28-pump-OFF run.
