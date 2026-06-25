# RESULT — FORK-A α-flip: does the Q-point PRESSURE-EQUILIBRIUM force R·r=¼ α-free?

**Date:** 2026-06-24 · **Lane:** implementer · **Branch:** `analysis/forka` (worktree `/tmp/forka`, off `origin/main` `bffc16b9`, POST #419)
**Scope:** the live α-flip question flagged PENDING/open at
[`node-up-small-large-signal.md`](../manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/node-up-small-large-signal.md):324
and [`resonant-lc-solitons.md`](../manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/resonant-lc-solitons.md):138 —
does the electron's self-biased quiescent-point (Q-point) *pressure-equilibrium* FORCE `R·r=¼` (the Golden-Torus
product) **without α**? If yes → the charge echo flips to a CHORD (α becomes derived). If α re-enters → it stays
the 4th echo.
**Driver:** [`src/scripts/forka_alpha_flip/qpoint_pressure_equilibrium.py`](../src/scripts/forka_alpha_flip/qpoint_pressure_equilibrium.py)
**Class (consistency-vs-emergence):** **CONSISTENCY (negative).** No new dimensionful constant; the attempt to lift
`R·r=¼` to emergence FAILS, and the failure mechanism is named.

**VERDICT: ECHO.** The Q-point pressure-equilibrium does **NOT** force `R·r=¼` α-free. α re-enters via the √α bias
ladder, AND the pressure balance fixes a *scale* (r, or an (R,r) relation), not the *product* `R·r` — the product
still requires the phasor-area = Nyquist-cell-area IDENTIFICATION (the Class-B INPUT). FORK-2: the pressure balance
is physically identical to S3's conservative `H_couple` slosh → this framing is a RELABEL, chord BARRED.

---

## 0. TL;DR

The Golden-Torus closure needs **two** equations in `(R,r)` (plus `d=1`):
- **regime (a)+(b)** give `R − r = ½` — genuinely **α-free** (Nyquist cutoff + self-avoidance). One equation.
- **regime (c)** is the one under audit: it supplies the **product** `R·r = ¼`, and the canon already classifies
  it Class-B because the closing step is a **named identification** (`πRr = π(d/2)²`, phasor-area = Nyquist-cell
  cross-section area), an INPUT, not derived from K4 + Cosserat primitives
  ([`ch8-alpha-golden-torus.md`](../manuscript/ave-kb/vol1/ch8-alpha-golden-torus.md):48,:59).

The fork asks: can the self-biased **pressure-equilibrium** supply that second equation as a *derived* output,
α-free? Three independent findings say **no**:

1. **α re-enters at the bias ladder.** The two per-port quiescent biases are `V_snap` (MASS) and
   `V_yield = √α·V_snap` (CHARGE/winding) — NOT independent; the √α is an explicit α-echo
   (`constants.py`:460, INVARIANT-C1). The winding-port inside pressure scale is `α × (mass-port pressure)`.
2. **The pressure balance fixes a scale, not the product.** A thin-tube Laplace balance gives `r` alone. The
   FULL torus mean-curvature Laplace balance gives `<2H> = (1/r)(2 − R/√(R²−r²))` — a genuine `(R,r)` relation
   but **NOT** `R·r=¼` and NOT proportional to `R·r`. No pressure condition produces the *product* `R·r`; that
   requires the AREA identification, i.e. the same Class-B INPUT.
3. **FORK-2 RELABEL.** The pressure balance is a conservative (Ax-3 lossless), no-pump, no-net-work reactive
   store — energetically **identical** to S3's `H_couple` slosh (`device-circuit-models.md`:201,:203,:207,
   PR #321). It moves energy but originates no new dimensionless number. "Pressure-equilibrium sets R·r=¼" is a
   relabel of the same conservative virial balance + the same area INPUT.

**ECHO. The charge stays the 4th echo** (alongside α-value, G, K=2G — the FORM-deriving / VALUE-importing
meta-finding, [`form-deriving-value-importing.md`](../manuscript/ave-kb/common/form-deriving-value-importing.md)).

## 1. The frame under test (verify-before-cite)

**The Q-point (POST #419, on main).** The electron = a **self-biased multi-port LC circuit at a self-set,
self-stable Q-point** ([`node-up-small-large-signal.md`](../manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/node-up-small-large-signal.md):298-315,
`resonant-lc-solitons.md`:133-138):
- **Bias = the saturation-state `A`** (Axiom-4 self-saturation IS the bias mechanism; no external bias network).
- **MASS port** (A1 dilatation → `Z_bulk`) biases to `A→1`, the `V_snap` rail, `Z_bulk→0`, `Γ=−1` cage.
- **CHARGE/winding port** (Cosserat (2,3) micro-rotation → `Z_shear`, the static reactive charge boundary)
  biases to `V_yield`, the self-trap onset.
- **SELF-stable:** the canon ASSERTS "the `R·r=¼` equilibrium is the stable Q-point" (`:135`) — but this is a
  *statement that the parked point sits at `R·r=¼`*, NOT a derivation that the equilibrium *forces* it. That
  gap is exactly this fork.

**The bias ladder is NOT independent (verified numerically):**
```
V_YIELD / V_SNAP = 0.08542454313193604
√α               = 0.08542454313193604   (exact match)
```
`V_YIELD = np.sqrt(ALPHA) * V_SNAP` at `constants.py`:460 (INVARIANT-C1). The corpus already flags this:
"`V_yield = √α V_snap` exactly, so the two per-port biases are NOT independent (the √α is an α-echo)"
(`node-up-small-large-signal.md`:328; `resonant-lc-solitons.md`:127).

**The route-2 trap that KILLED the prior lift** ([`ch8-alpha-golden-torus.md`](../manuscript/ave-kb/vol1/ch8-alpha-golden-torus.md):11):
> "the unit-bridge is α-free on input but closing to R·r=¼ requires *substituting* α (it forces R·r→4π²α ≠ ¼;
> a kinematic unit-bridge absorbs α, cannot predict it)."

**The corpus clean NEGATIVE that is NOT refilled:** the α-free cold-cage channel-impedance-mismatch
`Q ≈ 30.8 ≠ 137` (`resonant-lc-solitons.md`:131); `Q=137` is not refilled.

## 2. STEP 1–2 — the α-free geometry vs the product INPUT

The Golden-Torus system has THREE unknowns `(R, r, d)` and needs three equations:

| Regime | Equation | α-status | Provenance |
|---|---|---|---|
| (a) Nyquist | `d = 1 ℓ_node` | **α-free** | Ax-1 sampling cutoff |
| (b) crossing/self-avoidance | `2(R − r) = d ⇒ R − r = ½` | **α-free** | self-avoidance |
| (c) screening (the audit target) | `πRr = π(d/2)² ⇒ R·r = ¼` | **INPUT (Class B)** | named area-identification |

Regimes (a)+(b) are clean. They leave **one** equation in `(R,r)`: `R − r = ½`. The closure to the Golden Torus
`(R,r) = (φ/2, (φ−1)/2)` requires the SECOND equation, the **product** `R·r=¼`. Substituting `R·r=¼` into
`R−r=½` gives `2R² − R − ½ = 0 ⇒ R = (1+√5)/4 = φ/2` — the driver confirms `R·r ≈ 0.250000`, `R/r ≈ 2.618 = φ²`.
But this is **conditional on the INPUT**; the whole fork is whether the pressure balance can SUPPLY that product
α-free instead of asserting it.

## 3. STEP 3 — the route-2 trap (R·r → 4π²α), re-confirmed

The route-2 kinematic unit-bridge identifies the phasor enclosed area `πRr` (per-cycle reactive energy, via
`∮V dI`) with a real-space area through an impedance conversion. When the conversion is written in SI and reduced,
the dimensionless residue is α (because `Z_0 = 2αh/e²`). The closed form is `R·r = 4π²α`. Driver output:

```
4 π² α  at physical α   = 0.288087   vs  1/4 = 0.250000
to FORCE R·r=1/4 you must SET α = 1/(16π²) ≈ 0.006333  (physical α ≈ 0.007297)
```

So the kinematic area-bridge is an **α-ABSORBER, not an α-predictor**: it can only reproduce `¼` if you feed it
the wrong α. This re-confirms ch8's route-2 closed-NEGATIVE. **Any pressure route that ultimately closes through
a phasor-area = real-space-area identification inherits this same trap.**

## 4. STEP 4 — the pressure-equilibrium attempt (the fork)

**Substrate-native statement of the equilibrium.** Pressure is energy-density (Pa = J/m³). The self-biased
Q-point is the parked two-sided balance on the (2,3) winding torus:

- **INSIDE push `P_in`** — the confined reactive store (the breather's virial `C↔L` energy density) pushing the
  cage OUTWARD. Its SCALE is set by the per-port self-bias the soliton self-saturates to:
  `u ~ ½ ε₀ (V/ℓ)²`. The winding/CHARGE port saturates to `V_yield`; the MASS port to `V_snap`.
- **OUTSIDE push `P_out`** — the cold-vacuum bulk stiffness `K_bulk = √2 ρ c₀` (at `K=2G`, ν=2/7 GR-import)
  pushing IN, plus the tube's curvature (Laplace-like) surface term `γ_surf · (mean curvature)`.

**(i) α RE-ENTERS at the inside-pressure scale.** With `V_yield = √α V_snap`:
```
u_wind / u_mass = (V_yield / V_snap)² = (√α)² = α ≈ 7.30e-03
```
The winding-port inside pressure is `α × (mass-port pressure)`. Any equilibrium written on the winding port
inherits α from the bias ladder — this is the route-2-class α-reentry, now at the *pressure* level rather than
the *area* level.

**(ii) The pressure balance fixes a SCALE, not the PRODUCT R·r.** A thin-tube Laplace balance `u_wind = γ_surf/r`
solves for `r` alone. I tested the **strongest version** — the FULL torus mean-curvature, which DOES carry an
R-dependent term (`2H(θ) = 1/r + cos θ/(R + r cos θ)`). Its exact poloidal average (driver, analytic = numeric
quadrature to 9 digits) is:
```
<2H> = (1/r)(2 − R/√(R²−r²))         analytic = numeric = 2.970566259  at golden torus
```
This is a genuine `(R,r)` relation, but it is **NOT** `R·r=¼` and **NOT** proportional to `R·r`. There is no
pressure condition — thin-tube or full-torus — that produces the **product** `R·r`. The product is an AREA
object; it requires the `πRr = π(d/2)²` identification, which is exactly the route-(c)/route-2 Class-B INPUT.
The mean-curvature term's R-dependence does NOT collapse to `R·r` (the naive "cos integrates to zero" is FALSE —
the `R + r cosθ` denominator makes the second term survive; I caught and corrected this mid-derivation, and the
surviving term is `R/√(R²−r²)`, not anything that builds `R·r`).

**Net:** the pressure-equilibrium supplies, at most, `R−r=½` (already had it, α-free) plus a *scale* condition on
`r` (or an `<2H>` relation) — and where it touches the winding port it carries √α. It does **not** add an
independent, α-free `R·r=¼` equation.

## 5. STEP 5 — the FORK-2 guard vs S3 H_couple

**What S3's `H_couple` is** (`device-circuit-models.md`:201,:203,:207,:215, PR #321 verdict PARTIAL): the
conservative bulk↔shear skew-Hermitian circulator coupling — norm-conserved to `1.1e-12/40k steps` (**no pump**),
transfers 100% bulk→shear (it **sloshes**, NOT isolation, NOT inert), but its non-reciprocity **magnitude is
IMPOSED** (echo); only the FORM is α-free. It is the canonical "conservative coupling that sloshes, no net pump."

**The guard question:** what is PHYSICALLY DIFFERENT in the pressure-equilibrium fork?

**Answer: nothing.** The pressure balance is *also* a conservative reactive store (Axiom-3 lossless): inside push
= outside push at the parked Q-point, NO net work, NO pump — the **same energetic character** as `H_couple`'s
slosh. It moves energy between `C` and `L` (the virial breather) and between inside and outside (the cage), but it
**originates no new dimensionless number**: its only SCALE is the bias ladder, whose ratio IS √α.

Therefore "the pressure-equilibrium SETS `R·r=¼`" is a **RELABEL** of the same conservative virial balance, plus
the same area-identification INPUT for the product. It adds no force that selects the *product* `R·r`. **Per the
fork-2 guard discipline: if nothing physical differs from the conservative slosh, this is a relabel — say so
plainly and bar the chord.** Chord BARRED.

## 6. NO-α-HIDING trace (load-bearing)

Every dimensionful constant that could enter the `R·r` derivation, traced for α-presence:

| Constant | Role in the pressure balance | α-status |
|---|---|---|
| `ε₀` | sets pressure UNITS; cancels in the ratio | **α-free** |
| `ℓ_node` | Nyquist pitch (Ax-1) | **α-free** |
| `V_snap = m_e c²/e` | MASS-port bias scale (value-level) | **α-free** |
| `V_yield = √α·V_snap` | CHARGE/winding-port bias (INVARIANT-C1, `constants.py`:460) | **CARRIES α** |
| `K_bulk = √2 ρ c₀` | outside stiffness at `K=2G` (ν=2/7 GR-import) | α-free (a *separate* echo) |
| `γ_surf` | line/surface tension; SCALE rides `V_yield` if winding-port | **α-laden** (winding-port) |
| `Z_0 = 2αh/e²` | any phasor-area → real-space-area unit-bridge | **CARRIES α** (the route-2 trap) |

**Two distinct α-injection channels found, both fatal to a chord:**
1. **The √α bias ladder** (`V_yield = √α V_snap`): the winding-port inside pressure is `α × mass-port pressure`.
   This is a *ratio* that reduces to α — exactly the smuggling pattern the guard warns about.
2. **The phasor-area unit-bridge** (`Z_0 ∝ α`): any closure of the *product* `R·r` through an area identification
   reduces to `R·r = 4π²α` (route-2 trap).

Either channel makes `R·r` an α-echo. There is no α-free path from the pressure-equilibrium to the *product*
`R·r=¼`. The driver's no-α-hiding trace prints this table and the `u_wind/u_mass = α` reduction explicitly.

## 7. The over-determination coincidence-magnet tell

The discipline flags ½/¼ over-determination as a **coincidence-magnet** (a flag, not a confirmation;
[`feedback_challenge_canonical_negative`], 2026-06-04 α-¼ re-challenge). This fork triggers it twice:
- `R − r = ½` (regime b) and `R·r = ¼` (regime c) are *both* clean low-integer fractions, and they conspire to
  give exactly the golden ratio. The seductive narrative is "the substrate self-selects the golden torus." But
  `R − r = ½` is the ONLY α-free equation; `R·r = ¼` is the INPUT doing all the α-relevant work, and it is
  precisely the over-determined-looking ¼ that the route-2 trap shows is α in disguise (`R·r = 4π²α`, and
  `4π²·(1/137) ≈ 0.288 ≠ ¼`). The `¼` is NOT a clean geometric output; it is the *value* you'd need IF α were
  `1/(16π²)` — which it isn't.
- The "pressure-equilibrium parks at `R·r=¼`" assertion (`resonant-lc-solitons.md`:135) is the over-determination
  re-appearing as a *narrative* convergence: a second lane (the Q-point frame) re-explaining an already-closed
  negative (route-2). Per the multi-lane failure-mode memory, *convergence that re-explains an already-closed
  negative is the tell of a shared seductive blind-spot*, not corroboration. The pressure frame and the area-
  bridge frame are the SAME conservative balance viewed twice; they do not independently confirm `¼`.

## 8. Verdict + what would flip it

**VERDICT: ECHO.** The self-biased Q-point pressure-equilibrium does NOT force `R·r=¼` α-free. The charge stays
the 4th echo, joining the α-value, G, and K=2G (FORM-deriving / VALUE-importing meta-finding). This is a clean
negative with a single named mechanism (Rule 11 honest closure): the pressure balance is a conservative slosh
that fixes scales, not the product; the product needs the area-INPUT; and α re-enters via the √α bias ladder
AND/OR the `Z_0 ∝ α` unit-bridge.

**What would flip it to a CHORD** (the live flip-condition, kept open per the scoped-echo register,
`ch8-alpha-golden-torus.md`:13): a derivation that forces the **product** `R·r=¼` (equivalently `πRr = π(d/2)²`)
from K4 + Cosserat primitives ALONE — i.e. a substrate mechanism that (a) does NOT route through a phasor-area =
real-space-area identification (the `Z_0 ∝ α` trap), and (b) does NOT use the winding-port bias whose scale is
`√α V_snap`. The pressure-equilibrium route fails both. This is NOT a route-space exhaustion claim — a
not-yet-named α-free product mechanism could still exist; this fork closes only the **pressure-equilibrium**
named route.

**Flag-don't-fix items surfaced (NOT resolved here):**
- The canon's `resonant-lc-solitons.md`:135 / `node-up-small-large-signal.md`:308 ASSERT "`R·r=¼` is the
  stable Q-point." That is a *statement of where the parked point sits*, consistent with the bias ladder; it is
  NOT (and the leaves correctly flag it PENDING) a derivation that the equilibrium *forces* `¼`. This fork
  confirms the PENDING flag should stand. No edit to those leaves is made here (auditor lands canon changes).
- The `γ_surf` line-tension scale provenance (does it ride `V_yield` or `V_snap`?) is the one genuinely
  under-specified input; either way the product-vs-scale obstruction stands, but its α-status flips on this
  choice. Surfaced for Grant, not resolved.

## 9. Pre-registration (frozen)

See the standalone frozen pre-reg: [`2026-06-24_forka-alpha-flip_prereg.md`](2026-06-24_forka-alpha-flip_prereg.md).
The adjudication criteria below were frozen BEFORE running the driver; the result above did not drop or weaken any
of them (Rule 11 — no post-hoc criterion-dropping to convert ❌→✅).

**Frozen flip-condition test.** The Q-point pressure-equilibrium flips the charge echo→CHORD **iff** ALL of:
- **(P1)** A pressure-balance equation is written whose SOLUTION yields the **product** `R·r` (not merely `r`, `R`,
  or an `<2H>(R,r)` relation), AND
- **(P2)** that equation's value is `R·r = ¼` (within strain tolerance), AND
- **(P3)** the no-α-hiding trace shows NO α, √α, or α-reducible ratio in any load-bearing constant of the closure
  (specifically: not via `V_yield = √α V_snap`, not via `Z_0 ∝ α`), AND
- **(P4)** the mechanism is PHYSICALLY DISTINCT from S3's conservative `H_couple` slosh (adds a force selecting the
  product, not a relabel of the virial balance).

**Pre-registered outcomes:**
- **CHORD** if P1∧P2∧P3∧P4 all hold.
- **ECHO** if P3 fails (α re-enters) OR P1 fails (only a scale, not the product) OR P4 fails (relabel).
- **FORK-for-Grant** if P1∧P2 hold but P3 is ambiguous pending the `γ_surf` provenance call.

**Observed:** P1 FAILS (pressure fixes a scale / `<2H>` relation, not the product) AND P3 FAILS (√α bias ladder;
`Z_0 ∝ α` if the product is forced via area) AND P4 FAILS (relabel of the conservative slosh). → **ECHO** on
three independent grounds.
