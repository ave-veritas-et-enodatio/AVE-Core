# RESULT — X33 clock-architecture discriminator: **BRANCH S (walk PINS) — the bracket is an ARCHITECTURE fork, in-engine-undecidable**

**Date:** 2026-07-09 · **Branch:** `analysis/x33-clock-architecture` (off main @ 37eaded5) · **Task:** X33 (Grant-fired)
**Prereg (FROZEN):** [`research/2026-07-09_x33-clock-architecture_prereg_FROZEN.md`](2026-07-09_x33-clock-architecture_prereg_FROZEN.md)
**Derivation:** [`research/2026-07-09_x33-clock-architecture_derivation.md`](2026-07-09_x33-clock-architecture_derivation.md)
**Driver:** [`src/scripts/vol_1_foundations/x33_clock_architecture.py`](../src/scripts/vol_1_foundations/x33_clock_architecture.py)
**Data:** [`research/2026-07-09_x33-clock-architecture_result.json`](2026-07-09_x33-clock-architecture_result.json) · **Figure:** `src/scripts/vol_1_foundations/_output/x33_clock_architecture.png`
**Class (consistency-vs-emergence):** **CONSISTENCY / characterization.** A math+numerics typing of the substrate's
own clock architecture. ω_C = c₀/ℓ_node IDENTITY; 1/√3 Class-B manifestation; ρ* GR-imported (ν=2/7). No CODATA on
any verdict path; **this is not an empirical vote — it is an exact-spectrum computation.**

---

## 0. TL;DR — the verdict

**Grant's question:** does the substrate's synchronous walk actually PIN the multi-channel band ceiling, or does
stiffness lift it even under one universal tick? **Answer: it PINS — decisively and from first principles.**

- The **honestly-constructed** synchronous multi-channel coined walk (coin derived from the physical
  energy-normalized shunt scatter, ρ* entering through the transmission coefficients — NOT assumed) has ceiling
  **π√3 · ω_C = 5.44140 ω_C for EVERY ρ\* ∈ {1, 9.77337, 100, 1000}** (deviation from π√3 = **0.00e+00**). The
  literal walk unitary's maximum eigenphase is **exactly π** (the tick Nyquist) at all four ρ*.
- The **continuous** (lumped ω=√eig D) architecture's ceiling **LIFTS unboundedly**: 2.45 → 5.58 → 17.37 → 54.79
  (elastic units), a **22× rise** from ρ*=1 to ρ*=1000.
- **⇒ BRANCH S.** The architecture fork is REAL. The synchronous walk pins at the tick Nyquist; the continuum lifts
  with √stiffness; **each engine confirms its OWN architecture** and the fork **cannot be settled in-engine.** The
  discriminating observable is the **longitudinal-only window** (below).

**All 6 gates PASS.** The pin is not an artifact of a bad normalization choice — it is the honest scatter+connect
walk (the literal unitary matches the normalized-arccos map to 1.2e-13), and its mechanism is named algebraically
(coin eigenvalues ±1, ρ-independent; bipartite π-mode saturates the eigenphase at π).

---

## 1. Gate ledger (all PASS)

| Gate | Condition (frozen, prereg §5) | Result | Pass |
|---|---|---|---|
| **G1** scalar-limit | k_a=k_s → validated scalar arccos band | srs top **5.44140** (π√3), velocity factor **0.577350** (1/√3), 1D top **3.14159** (π) | ✅ |
| **G2** walk=scatter+connect | literal energy-normalized coined-walk UNITARY eigenphases = ±arccos(eig Ã) | unitarity err **4.0e-14**; arccos-match err **1.2e-13**; max‖θ‖/π = **1.0** ∀ρ* | ✅ |
| **G3** low-k agreement | walk & continuum give the SAME acoustic velocities (VRH) | walk/cont slope ratio spread **9.2e-7** (9 samples) — single constant | ✅ |
| **G4** continuum LIFTS | √eig(D) ceiling rises with ρ* (contrast partner) | lift ratio (ρ=1000/ρ=1) = **22.37×** | ✅ |
| **G5** bipartite pin locus | λ̃_max = eig_max(S^{-1/2}D S^{-1/2}) = 2 exactly ∀ρ* | max dev from 2 = **2.2e-15** | ✅ |
| **G6** coin eigenvalue locus | coin eigs = ±1 independent of ρ* | {+1×3, −1×6} ∀ρ* (dev < 1e-9) | ✅ |

**Adjudication (prereg §4, no post-hoc drop):** the frozen rule was — walk ceiling ρ-independent to < 1e-6 → Branch
S; walk ceiling lift ratio(1000/1) > 3 → Branch L. **Measured walk deviation = 0.00e+00 (< 1e-6) → Branch S.** The
continuum's 22.37× lift confirms the contrast is real (the pin is not because "nothing lifts anything").

---

## 2. The decisive spectrum numbers

**srs vector cell (12 bands), ceiling vs ρ\*:**

| ρ* | walk top (ω_C) | λ̃_max | continuous top (elastic √-units) |
|---|---|---|---|
| 1.0 | **5.441398** | 2.000000 | 2.4495 |
| 9.77337 (canonical) | **5.441398** | 2.000000 | 5.5846 |
| 100 | **5.441398** | 2.000000 | 17.3734 |
| 1000 | **5.441398** | 2.000000 | 54.7890 |

The walk column is **flat to all printed digits** (π√3 = 5.441398092702653). The λ̃_max column is **2.000000
exactly** — the bipartite π-mode, the reason for the pin. The continuous column lifts ∝ √stiffness (sub-√ρ* because
the top mode is not purely axial, but unbounded).

**1D two-channel zig-zag chain (θ=35°, 4 bands), verifies reduction + pin/lift on a tractable exactly-solvable
model:** at k_a=k_s the walk θ-ceiling = π (1D scalar arccos band, continuous top = 2.0); at ρ*=9.77 the walk
θ-ceiling is **still π** (pinned) while the continuous top lifts to 5.25; at ρ*=100 the walk θ-ceiling is **still π**
while continuous lifts to 16.4. (Figure: both architectures overlaid, one fixed low-k calibration.)

---

## 3. Where the stiffness enters (the survey's "tell", resolved — deliverable)

The survey's flag — *"the symmetric S^{-1/2} normalization divides out the stiffness that should lift the top"* — is
**CONFIRMED and mechanistically located**, and it is **NOT an artifact**:

- The **energy-normalized coin** `C_i = 2|w_i⟩⟨w_i| − I`, `|w_i⟩` stacked from `√Φ_b · S_i^{-1/2}`, is the **unique
  power-conserving (unitary) form** of the physical shunt scatter (derivation §1). The √S normalization is FORCED by
  unitarity, not chosen.
- **ρ\* enters ONLY the coin eigenVECTOR** `|w_i⟩`. The coin eigenVALUES are **±1 for any ρ\*** (G6: a Householder
  reflection). Stiffness is structurally locked out of the spectrum.
- The walk = normalized-arccos exactly (G2, spectral mapping theorem). The **bipartite π-mode** gives
  `eig_min(Ã) = −1` ⇒ ceiling `= ω_link·arccos(−1) = π·ω_link`, **ρ-independent** (G5). That is the pin.
- The continuum has no unitary tick, so `√eig(D)` is not bounded by `arccos(−1)` and lifts (G4).

So the normalized-arccos "pin" is the honest walk; the lumped/per-channel-link "lift" (12.41 / 17.01) is the honest
continuum. **Neither is a mistake — they are two different clock architectures**, and they agree everywhere except
the zone edge (G3).

---

## 4. The discriminating OBSERVABLE (Branch S deliverable) — the longitudinal-only window

Because the walk pins ALL branches at π√3·ω_C while the continuum lets the stiff longitudinal branch reach
`√(2·stiffness_axial) > π√3·ω_C`, there is a frequency band where **only the k_a-dominated (longitudinal) branch
propagates**:

- **Under continuous / lifted:** the longitudinal-only window is **[2.78, 8.69] MeV** (= [π√3·ω_C, π√3·√ρ*·ω_C]).
- **Under synchronous walk / pinned:** **ABSENT** — every branch ends at π√3·ω_C = 2.78 MeV; there is nothing above.

**This is the empirical fork.** An experiment (or a corpus-anchored physical argument) that detects propagating
longitudinal excitations in the 2.78–8.69 MeV band would confirm the continuous architecture; their absence (a hard
band edge at 2.78 MeV for ALL polarizations) confirms the synchronous-walk architecture. **The engine cannot decide
this** (see §5); it is surfaced to Grant.

---

## 5. Op5 CLOCK TYPE (deliverable) — Op5 is a PINNING clock

**Op5's scatter+connect IS a synchronous discrete-time unitary walk** (one universal tick = one bond crossing;
`connect_is_permutation` = the topological shift; the scatter = the unitary coin). Consequences:

1. **The Op5 engine will ALWAYS report the pinned ceiling** π√3·ω_C = 5.441 ω_C for any ρ*, and **cannot see the
   stiffness lift.** Any band-top read off `chiral_lattice_dynamics` / a scatter+connect solver is pinned by
   construction — this is the corpus-native value (#604 measured it as 1/√3 by direct time-stepping).
2. **The lifted reading (12.41 / 17.01 ω_C) requires a DIFFERENT engine** — a continuous-time / Hamiltonian
   `ω = √eig(D)` solver (the elastic Born-Huang matrix). That engine will always report the lift.
3. **⇒ The bracket [5.441, 17.011] ω_C (#607's pending fork) is an ARCHITECTURE fork, not a modelling ambiguity to
   be numerically resolved.** Each engine confirms its own architecture. It is **in-engine-undecidable**; only
   Grant/corpus can anchor which clock the vacuum runs. (Per Regime/phase-state discipline: a walk-engine null on
   the lift is an ARTIFACT of the pinning architecture, not a falsification of the lift.)

---

## 6. Consumers (updates the #607 pending fork)

- **(a) The #607 pending-Grant decision (single-scale π√3 vs stiffness-lifted π√3·√ρ*)** is now **TYPED**: it is not
  "which number is right" but "**which clock is the vacuum**." Single-scale = synchronous-walk clock (pinned);
  stiffness-lifted = continuous clock. **Recommended framing for the board:** replace the "band-top scale" decision
  with a "**clock architecture**" decision, discriminator = the longitudinal-only window [2.78, 8.69] MeV.
- **(b) FORK-A tone floor.** The conservative (stiffness-lifted) floor 17.01 ω_C remains safe under BOTH
  architectures (the walk's pinned top 5.441 is BELOW it, so tones clearing 17.01 clear both) — **no change to the
  #607 conservative tone placement 18.51/17.51 ω_C.** If Grant anchors the synchronous-walk clock, the floor may
  drop to the scalar 5.94/6.94; until then the conservative floor stands.
- **(c) FPB-corner coexistence window.** The longitudinal-only window **[2.78, 8.69] MeV exists under the continuous
  clock and is absent under the walk clock** — the #606 FPB-corner marker/board line inherits the same architecture
  conditional (it is NOT a settled widening; it is contingent on the clock ruling).

---

## 7. Consistency-vs-emergence + corpus-state consequence

**CONSISTENCY / characterization.** ω_C IDENTITY (`OMEGA_C`); 1/√3 Class-B (`ANALYTIC_NETWORK_FACTOR`); ρ*
GR-imported (ν=2/7, bisected — reused from the survey, not re-derived). Every gate COMPUTED vs an
independently-derived canonical number (π√3, 1/√3, the survey's λ̃_max=2). The walk unitary is built and
diagonalized (G2) so the arccos map is DERIVED. No α/Q_TANK on any verdict path; forward computation only.
Born-Huang/vector pipeline REUSED (Rule 14) from the validated `srs_vector_band_survey.py`.

**Corpus-state consequence (for the auditor to land, not this lane):**
1. **PR #607's pending-Grant "single-scale vs stiffness-lifted vector band top" decision is RE-TYPED** as a **clock
   architecture** fork (synchronous-walk-pins vs continuous-lifts), **in-engine-undecidable**, with a named
   empirical discriminator (the longitudinal-only window [2.78, 8.69] MeV). The board row should be updated from
   "band-top scale" to "clock architecture" and flagged as requiring a Grant/corpus anchor, not a numeric run.
2. **The survey's §5/§6 tell** ("S^{-1/2} divides out stiffness — cannot be the physical band top") is **resolved to
   a FORK, not a defect**: the S^{-1/2} normalization is the FORCED energy-normalization of the honest walk coin;
   the pin is the genuine synchronous-walk result, the lift the genuine continuum result. The survey's phrasing
   "which cannot be the physical band top of a stiffness-anisotropic lattice" should be softened to "which is the
   band top under the synchronous-walk clock; the continuum clock lifts it."
3. **Op5 is typed as a PINNING (synchronous discrete-time unitary walk) clock** — a reusable methodological fact:
   scatter+connect band-tops are pinned by construction; do not use the Op5 engine to adjudicate a stiffness-lift
   question (it will confirm its own architecture). Candidate for a `substrate-native-check` / regime-discipline
   note.

These are ledger rows + note updates surfaced to the auditor's manuscript / COLLABORATION_NOTES queue; the manual
entries are the auditor's to land (lane discipline). No leaf edit from this lane.
