# Stage-3 cavity-pinning — make-or-break RESULT (the source-of-truth disposition)

**Date:** 2026-06-24 · **Lane:** full-engine re-route, Stage 3 ("THE CONFINEMENT / MUTUAL-PINNING PAYOFF") · **Status:** SETTLED NEGATIVE — canonical source doc.
**Verdict:** 🔴 **DISPERSE-FALSIFIED — the winding + H_couple + cavity does NOT pin the dispersing A1 core. Energy-conservation-certified (physics, not numerics).**

**Scope-lock (read first):** this is the DEEPER negative the pre-reg §0 named before the run. It is **NOT** "the electron is falsified." **mass = A1 (PR#260) is UNTOUCHED.** What is falsified is the *sanctioned successor localization mechanism* — that the now-conserved (2,3) Cosserat winding ω (S1) + the conservative A1↔ω lock H_couple (S2) + the |Γ|→1 cavity at V_snap HOLDS the A1 core that Stage-2 showed disperses bare. Per Rule 12 (substitution-not-retraction): the slot is **RETRACTED, not refilled** — no new pinning hypothesis is minted here.

**Prereg (frozen, pre-run):** [`research/2026-06-24_engine-s3-cavity-pinning_prereg.md`](2026-06-24_engine-s3-cavity-pinning_prereg.md) (SHA-pin `0b5691cd`).
**Solver:** `src/ave/solvers/coupled_cage_winding.py` (the coupled real-space A1↔ω PDE on the native K4 stencil; Crank–Nicolson / Cayley, GMRES).
**Gate module:** `src/ave/core/s3_cavity_pinning_gate.py` (HALT gates 1–3 + the DELTA binner).
**Validation gates:** `src/tests/test_s3_cavity_pinning.py` (T1–T7, 8 passed).
**Results JSON:** `results/engine_s3_cavity_pinning_results.json`.

---

## 1. The pre-registered question and its disposition

The frozen make-or-break (prereg §1): on a **real-space coupled A1↔ω PDE on the native tetrahedral TETRA_OFFSETS stencil**, seed an already-localized A1 eigen-precursor (POSITED persistence) carrying the S1-conserved (2,3) winding ω, with the S2 conservative skew-Hermitian H_couple A1↔ω lock ENGAGED and the `|Γ|→1` cavity at V_snap:

- **MAKE (pinned):** the A1-core centroid-spread / interior energy-localization holds BOUNDED over the full run — clears the Stage-2 Mode-I PERSIST bar that A1-alone FAILED — energy-conservation-certified on a CLOSED box (|rel_drift| ≤ 1e-5; NO PML, NO damping), robust across sech AND gaussian.
- **BREAK (disperses):** reproduces Stage-2 Mode-III — winding + H_couple + cavity does NOT pin the core.

**The result is the DELTA** between (coupled, winding ON) and (winding OFF / ω=0 = A1-alone). The pre-reg's two-sided disposition (§0): TRUE ⇒ boundary/topological localization demonstrated; FALSE ⇒ a DEEPER negative, "RETRACT, do not refill (Rule 12)."

**DISPOSITION: the BREAK branch FIRED.** The IF-conditional written into the pre-reg before the run resolved to its falsification arm, energy-conservation-certified, seed-robust, dt-stable, and N-robust. This is the discipline working at full strength (Rule 11 honest closure): a clean negative, a single mechanism explaining it, branch closed — NOT debugged toward a rescue.

## 2. The DISPERSE result (the DELTA)

Production run: N=24, dx=0.5, sech seed A=0.85 radius=2.5, the (2,3) winding template (R=7, r=2.3), H_couple ON (rate=0.3, χ=+1, front-gated), Crank–Nicolson / Cayley, dt=0.066, 600 steps (200-step transient + 400-step recording).

| Quantity | winding ON | winding OFF (A1-alone) | Reading |
|---|---|---|---|
| `verdict` | **DISPERSE** | DISPERSE (Mode-III) | the make-or-break BREAK arm |
| A1-core centroid spread (seed→post→end) | 3.98 → 5.89 → **6.51** | 3.98 → 6.36 → 7.41 | **ON spread GROWS** — only ~8% tighter than OFF; NOT held bounded |
| spread DELTA (OFF/ON, post) | — | **1.08** | far below the ≥1.30 bar — no real localization DELTA |
| interior peak (post mean) | 1.42 | 0.35 | ON peak high (Rabi-pumped), OFF sheds below the radiation floor |
| interior A1 energy (post mean) | 257 | 184 | ie DELTA ON/OFF = 1.40 (real, but see §3) |

**The honest physics (§3).** The winding-ON case *does* show a real interior-energy DELTA (the peak stays high, ~1.4× the interior energy of A1-alone). But that DELTA is **NOT a pinned localized core**: it is the H_couple **Rabi-pumping** the central peak (the A1↔ω exchange deposits ω energy into the A1 peak, pushing it ABOVE the seed amplitude, 0.85→1.42) **plus** energy held on the *extended torus shell* (the ω template lives at radius R=7, in the interior). The decisive A46 real-space localization observable — the A1-core **centroid spread** — **grows in both ON and OFF** (3.98→6.51 vs 3.98→7.41). The core disperses; the coupling merely redistributes some energy onto the torus and pumps the peak, it does not confine the core.

**Seed-robust / dt-stable / N-robust.** DISPERSE at sech AND gaussian; at dt = 0.132 / 0.066 / 0.033 (all energy-conserving to ~1e-9); at N = 20 / 24 / 32. The verdict does not depend on the seed profile, the timestep, or the box size.

## 3. The energy + genesis-24 certification (why this is physics, not numerics)

The top trap (pre-reg §3 trap 1) is **damping-bought localization**. The instrument is certified clean on a CLOSED box (NO PML, NO damping):

- **Joint energy conserved:** `|rel_drift_max| = 2.5e-10` ≪ the 1e-5 bar (Crank–Nicolson / Cayley is exactly unitary; the generator H is Hermitian to machine precision). A bounded core, had one appeared, could NOT have been bought by dissipation.
- **BOTH separately conserved (genesis-24, pre-reg §4):** the ω-winding **integer holds (2,3)** across the whole run (read off the quadrature-invariant `|b_ω|·ê_w`). The DISPERSE verdict is therefore NOT an artifact of the winding bleeding into the A1 scalar — the winding is intact AND the core still disperses. (a1_drain +15.6%, om_drain −10.5% reflect the *reactive* Rabi exchange, not a one-way bleed: the per-grade energies slosh back and forth while the total + the winding integer are conserved.)

This is the cleaner, stronger statement: even with the winding **demonstrably conserved**, the coupling does not pin the core.

## 4. The immune system (all green — the negative result is trustworthy)

| Control | Result | What it rules out |
|---|---|---|
| winding-OFF reproduces Mode-III in-harness (HERO-CANARY) | ✅ peak 0.35, ie 641→60, spread 3.98→7.41 | the DELTA is measured against a live in-harness Mode-III floor |
| closed-box energy gate (G2) | ✅ rel_drift 2.5e-10 | damping-bought localization |
| BOTH conserved (energy + winding integer) | ✅ (2,3) held; total drift 2.5e-10 | genesis-24 winding-bled-into-A1 fake |
| slaved-arm reachable-False (S1 gate) | ✅ slaved independence False, real arm independent | ω := grad(V) (genesis-24) |
| GX3 backward-Euler bleeds | ✅ bleed = 1.0 | the energy gate is a live discriminator |
| GX5 passive radiative port | ✅ Hmax/H0 = 1.0 | the 142× PML energy-injection artifact |
| gaussian disperses | ✅ peak 0.33 | seed-profile-dependent self-trap |
| Cartesian-v14 self-traps | ✅ v_peak 0.62, n_EM 0.61 | the apparatus can SEE a trap when one exists |
| dispersive-vector ω unwinds (control) | ✅ winding 3→−1 | the rigid-template (winding-conserved) representation is load-bearing |

## 5. The instrument (the genuine new work) and one load-bearing build finding

**Build (pre-reg §5 NEEDS-NEW-COUPLED-PDE, FORK-PDE-HOST = extend `native_cage_imex`).** A real-space coupled A1↔ω PDE on the native TETRA_OFFSETS stencil: A1 the dispersing bulk-dilatation breather (the Stage-2 scalar cage operator UNCHANGED), ω the Cosserat winding DOF (its OWN field, seeded by `seed_pq_winding`, NEVER grad(V)), coupled by the S2 conservative skew-Hermitian H_couple lifted from its C^{2M} GENERATOR/FORM onto the lattice. The whole generator is Hermitian ⇒ Crank–Nicolson / Cayley is exactly unitary ⇒ joint energy conserved (the coupled analog of the Stage-2 IMEX energy guard).

**Load-bearing build finding (Rule 10, run early).** A free analytic-signal **vector** ω field on the native stencil UNWINDS the (2,3) winding integer even UNCOUPLED — the Schrödinger spatial operator smears the direction field (3→0→−1). That does NOT represent S1's established topological conservation; it is an instrument artifact. The genesis-24 guard (pre-reg §4) REQUIRES the ω-winding be separately certified conserved, so ω is represented S1-faithfully as a complex LC-quadrature amplitude `b_ω(x)` on a **fixed seeded winding template** `ê_w(x)`: the (2,3) integer is carried by the frozen template (conserved by construction), the dynamical `b_ω` carries the charge-sector energy that disperses and couples to A1. The winding read is taken off the **quadrature-invariant** `|b_ω|·ê_w` (the `Re(b_ω)` read is corrupted by the LC L-state quadrature zeros — a read artifact, not topology). The dispersive-vector form is retained as a documented winding-NOT-conserved control (§4).

## 6. Honest flags / scope

- **CONSISTENCY-class (pre-reg §6).** S3 tested the localization MECHANISM, NOT the α-free chord (S4). The DISPERSE verdict does not touch the chord-vs-echo question; it closes the *winding-pins-the-core* mechanism. Q=137 stays EMPTY (anti-substitution); the result depends on `ave.core.constants` only through the operating point V_snap (√α-laden, declared), which is NOT on the verdict-determining path (the verdict reads the real-space spread DELTA, α-free).
- **The interior-energy DELTA is real but does NOT clear the pin bar.** It reflects Rabi-pumping + energy held on the torus shell, not a confined core. The centroid-spread (the load-bearing A46 localization observable) grows in both ON and OFF. We report the ie DELTA honestly and do NOT headline it as a pin.
- **Posited-persistence scope (pre-reg §0 FORK FORMATION-SCOPE).** S3 seeded an already-localized precursor and asked whether the mechanism HOLDS it. Formation/genesis is out of scope (the separately-tracked keystone-pump). This result does not bear on formation.
- **|Γ|→1 / V_snap is the operating point, not a gate.** The cavity enters via S(A→1) at the core (the bulk-branch Smith-Γ→−1 is diagnostic); "touching −1" is not used as a falsifiable observable (pre-reg §2).

## 7. Reproduce

```
PYTHONPATH=/tmp/s3-impl/src /Users/grantlindblom/AVE-staging/AVE-Core/.venv/bin/python \
  -m ave.core.s3_cavity_pinning_gate          # full make-or-break → results JSON
PYTHONPATH=/tmp/s3-impl/src /Users/grantlindblom/AVE-staging/AVE-Core/.venv/bin/python \
  -m pytest src/tests/test_s3_cavity_pinning.py -q   # T1–T7 validation gates (8 passed)
```

Branch-only (`analysis/engine-s3-cavity-pinning`); NEVER self-merge — Grant merges.
