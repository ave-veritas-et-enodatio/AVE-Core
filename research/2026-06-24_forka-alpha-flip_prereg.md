# PRE-REG (FROZEN) — FORK-A α-flip: Q-point pressure-equilibrium → R·r=¼ α-free?

**Date frozen:** 2026-06-24 · **Lane:** implementer · **Branch:** `analysis/forka` (worktree `/tmp/forka`, off `bffc16b9`, POST #419)
**Frozen BEFORE running** [`src/scripts/forka_alpha_flip/qpoint_pressure_equilibrium.py`](../src/scripts/forka_alpha_flip/qpoint_pressure_equilibrium.py).
**Companion result:** [`2026-06-24_forka-alpha-flip.md`](2026-06-24_forka-alpha-flip.md).

---

## Question (Grant-directed)

Does the electron's self-biased quiescent-point (Q-point) **pressure-equilibrium** — the two-sided longitudinal
vacuum-pressure balance (inside reactive store vs outside bulk stiffness + tube curvature) on the (2,3) winding
torus — **FORCE `R·r = ¼` WITHOUT α**?
- If YES → the charge echo flips to a **CHORD** (α becomes derived from the Golden-Torus product).
- If α RE-ENTERS (via the `Φ/τ/μ₀` unit-bridge, the `R·r → 4π²α` route-2 trap, or any ratio reducing to α) → it
  stays the **4th ECHO**.

## Frozen flip-condition (the chord requires ALL four)

- **(P1) PRODUCT, not scale.** A pressure-balance equation whose solution yields the **product** `R·r` — not
  merely `r`, `R`, or an `<2H>(R,r)` curvature relation.
- **(P2) VALUE.** That product equals `R·r = ¼` within strain tolerance (`δ_strain ≈ 2.225e-6`).
- **(P3) NO α-HIDING.** The no-α-hiding trace shows NO α, √α, or α-reducible ratio in any load-bearing constant of
  the closure. Specifically banned channels: `V_yield = √α V_snap` (`constants.py`:460), and `Z_0 = 2αh/e²` in any
  phasor-area → real-space-area unit-bridge (the route-2 `R·r → 4π²α` trap).
- **(P4) PHYSICALLY DISTINCT from H_couple.** The mechanism adds a force that SELECTS the product `R·r`, and is not
  energetically identical to S3's conservative `H_couple` slosh (no-pump, no-net-work reactive store). If nothing
  physical differs from the conservative slosh, it is a RELABEL.

## Pre-registered outcome map (no post-hoc criterion-dropping, Rule 11)

| Outcome | Condition |
|---|---|
| **CHORD** | P1 ∧ P2 ∧ P3 ∧ P4 all hold |
| **ECHO** | P3 fails (α re-enters) OR P1 fails (only a scale) OR P4 fails (relabel) |
| **FORK-for-Grant** | P1 ∧ P2 hold but P3 ambiguous pending the `γ_surf` line-tension provenance call |

## Discipline applied (frozen)

- substrate-native-first: pressure = energy-density = reactive-store / volume; bias = Axiom-4 saturation-state `A`.
- no-α-hiding: trace EVERY dimensionful constant; any α / √α / α-reducible ratio in the closure = ECHO.
- symmetric-standard: SM does not derive α either; the AVE-distinct chord (if any) is in the PRODUCT mechanism, not
  the numeric match.
- over-determination coincidence-magnet: ½/¼ over-determination is a FLAG, not a confirmation; narrative
  convergence (Q-point re-explaining route-2) is a shared-blind-spot tell, not corroboration.

## Adjudication criteria are frozen here

The result doc records the observed outcome against THIS map without weakening any of P1–P4. If the driver had
shown an α-free product equation, that would have been logged as CHORD (or FORK-for-Grant); the criteria do not
move to fit the result.
