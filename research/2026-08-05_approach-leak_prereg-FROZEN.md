# The APPROACH LEAK — shear→rotation conversion on the graded approach to `r_sat` — FROZEN PRE-REGISTRATION

**Date:** 2026-08-05 · **Branch:** `research/approach-leak`
**Dispatch:** the approach-leak lane, the last open number under the channel-scoped kernel-collapse
ruling — `_orchestration/docket-entries/2026-08-05-ruling-kernel-collapse-rescope.md`:18, verbatim:
*"the leak is one computable number (a coupled two-channel scattering computation, routed as the
approach-leak lane)"*.
**Class:** DERIVATION prereg (research-doc; mints no `clm-`/`def-`/`exp-`/`sup-`/`ilk-`; propagates
to no KB/manuscript leaf; changes no solidity; edits no falsification ledger). Engine `src/ave` is
**byte-untouched and never imported**.
**SVA pilot case 7** — the v0.2 header, all eleven rows, per-row pilot notes returned at result.
**Written against `origin/main` = `c4fdced0`.**

> **THIS FILE IS FROZEN AND PUSHED ALONE**, before any driver code exists and before any number
> produced by this instrument exists. No gate, tolerance, bin boundary, frozen numeric parameter,
> pattern-battery entry, verdict wording or method element of §2–§8 may be changed after any result
> of this lane is seen.

---

## §0 — Standard Vacuum Analysis header (SVA v0.2-pilot, eleven rows)

 1. **SECTOR / OWNERSHIP:** the incident/reflected wave is **shear (T2-translational, the `G`-bond
    channel)**; the converted quantity is the **Cosserat micro-rotation `ω` (channel 4 of
    `port-register.md`:47–50, the couple-stress / `(2,3)`-winding channel)**. The conversion
    operator is the `G_c` antisymmetric-strain bond and NOTHING else. **Cross-wiring check done:**
    mass is A1 dilatation and is NOT in this lane; charge is the Cosserat winding INTEGER and is
    NOT in this lane; the gap `m² = 4G_c/I_ω` is the T2/ω **flywheel clock gap**, explicitly
    **re-scoped away from the rest-mass store** (`cosserat-mass-gap.md`:149, Rule-12 note). No
    statement of this lane crosses a sector boundary.
 2. **REGIME / PHASE-STATE:** **MODE** — small-signal AC, a **scattering problem at REAL drive
    frequency**, not an eigenvalue problem. **REGIME** — sub-yield lossless-reactive on `r > r_sat`;
    the `A ≥ 1` interior is Regime IV and **is not in the domain** (fenced out for every mirrored
    channel by the ruling). **PHASE-STATE** — cold lattice, Op14 ON as a **static constitutive
    grade**, `A(r) = r_sat/r`, `A = 1` exactly at `r_sat`. **DC bias point** = the gravitational
    grading itself. Small-signal is exact here because the DRIVE amplitude is infinitesimal; the
    LARGE quantity is the static bias, which is carried exactly and not linearized.
    **A null in which the effect cannot exist under the frozen construction is an ARTIFACT-class
    finding, not a falsification**, and every null below is classified.
 3. **CIRCUIT STATEMENT:** two coupled reactive ladders sharing a per-cell mutual element. Ladder 1
    (shear) is the certified `[L=ρ][C=1/μ]` line of `2026-08-05_last-bond-kernel-collapse_result.md`
    §3.1. Ladder 2 (rotation) is a **series-resonant** ladder: a shunt compliance `1/(4G_c)`, a
    series micro-inertance `I_ω`, and a per-cell coupling `γ` — i.e. **a high-pass / cutoff line
    whose cutoff IS the gap**. The observable is: *how much of the drive current in ladder 1 leaves
    through the mutual element into ladder 2 and does not come back.* **TOTAL-vs-SLOT:** the
    measured object is the **total** relative micro-rotation `ε_antisym = A_macro − ω_micro` (a
    single terminal quantity), NOT the two rotations separately — the split is a slot.
 4. **PLANE & PROJECTION:** every per-cell quantity is referenced to the **cell-centre plane of
    intact cell `n`**, `n = 1` the innermost intact cell, nodes at `x_n = (n−1+θ)ℓ_node` outward
    from `r_sat` — **byte-identical to the echo-delay v2 placement** (`2026-08-05_echo-delay-v2-
    reach-through_prereg-FROZEN.md`:245). This lane declares **NO Γ and NO Z at a wall plane** and
    therefore inherits no sign convention: it reports an **amplitude RATIO and an INTEGER CELL
    COUNT**, both plane-invariant. The one signed object it touches is quoted, not recomputed.
    **Spectral-lane projection:** the rotational branch is selected by **character** — the
    `ω`-dominated branch of the Cosserat dispersion (`cosserat-mass-gap.md`:160: gapped branches
    `ω`-fraction `1.000000`) — not by a sort index.
 5. **CONSTITUTIVE PROVENANCE:** `S(A) = (1−A²)^{1/2}` **DERIVED** (Ax 4). `A(r) = r_sat/r`
    **DERIVED-FORM / VALUE-IMPORTED** (the `7` in `r_sat = 7GM/c²` rides GR-imported `ν_vac = 2/7`).
    `ℓ_node = ħ/(m_e c)` **IMPORTED-VALUE / DEFINITIONAL**. `ω_C = c₀/ℓ_node` **IDENTITY**
    (`constants.py`:305). `ω_m = 2ω_C`, equivalently `G_c/I_ω = ω_C²` — **RULED** (A-008 corollary
    §3.3 of `2026-08-05_a008-factor-propagation_note.md`), and this lane uses ONLY the ratio, never
    the absolute moduli. `c_R = √2 c₀ = √(2γ/I_ω)` **DERIVED-ENGINE-FAITHFUL / Grant-ratified
    2026-06-23** (`cosserat-mass-gap.md`:104). ★ **`G_c(A)` grading exponent `a` and `I_ω(A)`
    grading exponent `b`: BOTH `UNDETERMINED-CANON` at freeze — to be RECEIPTED two-method and
    BRACKETED, never assumed.** `ρ = ρ_bulk` (RHO-A) vs `ρ_eff = ρ_bulk/S³` (RHO-B) **FORKED
    (FORK-3(b), OPEN)** — both run. Vector band top `β ∈ {5.4414, 17.0111} ω_C`
    **BRACKETED(pending-ruling)** — both ends run. The **rotational** band top is
    `UNDETERMINED-CANON` (`srs-band-structure.md`:118: the microrotation channel is *"a named
    follow-on not surveyed at this Cauchy-translational level"*) and is BRACKETED, not chosen.
 6. **ENERGY LEDGER:** **RIM.** Every quantity in this lane is a within-system reactive exchange
    between two lossless reactive ladders. **No port is crossed and no loss word is used anywhere
    in this lane.** The ledger question this lane must ANSWER (not assume) is whether the rotational
    channel constitutes a **continuum-counted port** at the drive frequency — which is exactly the
    question "are there propagating rotational states at `ω`". If there are none, the admixture is
    a reactive store on the Axiom-3 rim and the time-averaged transported power is **zero by the
    reality of the transfer function**, which this lane proves rather than asserts (§2.5).
 7. **CALIBRATABILITY:** the primary target `ζ_max` is a **dimensionless amplitude ratio** at a
    declared plane; the secondary target `N_open` is an **integer count**. The margin is reported
    in **orders of magnitude of a ratio**. Nothing in the primary chain normalizes against an
    external standard. **The one place an absolute-modulus ratio enters (`G_c/G`, in the residual
    back-action on the shear channel) is quarantined into its own output field and its own bin.**
 8. **DISCRIMINATION CLASS:** **DC→AC coupling** — a static DC bias (the gravitational grading)
    modulating an AC transport property (the rotational cutoff). **Tautology filter:** the target
    is NOT "does a gapped branch reject a below-gap drive" (that is a restatement of `ω < ω_gap`);
    it is **whether the graded bias ever drives the local gap below the drive on the physically
    existing lattice**, which is a competition between two independent powers of `ℓ_node/r_sat` and
    can go either way. **SM counterfactual:** GR + a matter field has no saturating modulus and no
    rotational gap that rides it; the entire question does not arise there. **Fence:** nothing in
    this lane is surfaced as an AVE-vs-competitor discriminator — the ECO free-reflectivity
    degeneracy carried at `2026-08-05_echo-delay-v2-reach-through_result.md` HEADLINE applies here
    unchanged and is restated at result.
 9. **CERTIFICATION PLAN:** gates and bins frozen in §5–§7 below, before any number exists; this
    prereg lands as its own pushed commit. **UNRUN ≠ PASSED.** Negative controls named in §5.3
    (reproduce the predecessor's `S_last` and the v2.4 band endpoints from their own shipped
    artifacts before computing anything new). **Derived gate constants get a pre-freeze
    second-method check** — the two closed forms of §2.6 are each evaluated two ways in §5.2.
    **Self-referentiality:** this lane's scan surface is restricted to `git ls-files` output with
    this lane's own artifacts excluded BY CONSTRUCTION (the pilot-5 `G-SCAN` repair, applied).
10. **ADJUDICATION ROUTING:** §7 states which bin propagates what. **The fence on this lane's own
    result is frozen in §8**, including the explicit statement that a `GAP-CLOSED` verdict does NOT
    license any claim about the rotational channel AT or INSIDE `r_sat` (the carve-out's frontier
    question, routed elsewhere), and that MeV-scale rotational radiation is OUT OF SCOPE.
11. **NUMERICAL CONDITIONING:** **NAMED CANCELLATIONS.** (i) `1 − A²` at the innermost node, where
    `ℓ_node/r_sat ≈ 6e-19` — **catastrophic in float64, returns exactly `0`**; computed instead from
    the cancellation-free `S² = x(2r_sat + x)/(r_sat + x)²`, carried from the predecessor lanes.
    (ii) `1 − (ω/ω_m)²` in the driven-response denominator, where the ratio is `~1e-9` — computed
    with `expm1`/`fma`-free explicit form and evaluated at `dps = 60`, and the SMALL quantity `ζ`
    is formed as a ratio of squares, never as a difference of near-equal numbers.
    (iii) `Σ_n ζ_n²` — a convergent `Σ1/(n−1+θ)²` whose closed form is `ψ'(θ)`; the sum is
    **never truncated numerically** but compared against `ψ'(θ)` from mpmath's `polygamma`.
    **DYNAMIC RANGE.** `ℓ_node/r_sat ∈ [~4e-17, ~4e-19]` over the mass grid; `S ∈ [~1e-9, 1]`;
    `S² ∈ [~1e-18, 1]`; `ζ ∈ [~1e-37, ~1e-18]`; `N_open ∈ ℤ≥0`; the gap-margin ratio spans `~1e9`
    to `~1e37`. **WORKING PRECISION.** mpmath `dps = 60` for **every** closed form, every gate
    comparison and every quantity built from `ℓ_node/r_sat`. float64 appears **nowhere on a verdict
    path**; the one float64 use is the JSON echo of already-gated mp values, and it is not gated.
    **ERROR-PROPAGATION MODEL AND ITS METRIC:** this lane has **no iterated map** — every reported
    quantity is a closed form evaluated once at `dps = 60`. The error model is therefore
    round-off-only, bounded by `10^{-58}` relative, and the metric it contracts in is the trivial
    one (no accumulation). **This is stated so a successor that adds a cascade knows it does not
    inherit a contraction argument from here.** **REGEX ENGINES NAMED:** METHOD A = `git grep -P`
    (PCRE, ASCII `\w`); METHOD B = Python `re` on `str` (Unicode `\w`). **No pattern in this lane's
    battery uses `\b`** — the FLAG-UNIWB divergence class, avoided by construction rather than
    detected after the fact.

---

## §1 — THE OBJECT, STATED BEFORE ANY FRAMEWORK WORD

A shear wave runs inward down the graded approach and meets a total mirror at the last bond. On the
way in it passes through a region where the substrate's shear bond and its rotation bond are
**mutually coupled** by one term — the `G_c` antisymmetric-strain bond, which penalizes any
mismatch between the macro-rotation carried by the shear wave and the node's own micro-rotation.
**The question is whether any of the shear wave's energy leaves through that mutual element and
travels away as rotation instead of coming back as echo.**

In circuit terms: ladder 1 carries the signal; ladder 2 is tapped off it through a mutual element;
ladder 2 is a **cutoff line**. Below cutoff, a tap into a cutoff line is a **reactive stub** — it
stores and returns, it does not carry. Above cutoff it is a **second output port** and the signal
splits. **The whole lane is: where is the cutoff, and does the bias ever push it below the drive on
lattice cells that actually exist.**

### §1.1 — The three canon facts this lane stands on, quoted

**(a) The rotational branch is gapped, and the gap is set by `G_c/I_ω`.**
`cosserat-mass-gap.md`:59, verbatim: $\omega^2 = c^2k^2 + \frac{4G_c}{I_\omega}$, i.e.
`m² = 4G_c/I_ω`, empirically Verlet-validated to `0.35 %` (`:81`).

**(b) The gap's SCALE is the A-008-pinned `2m_ec²`.** `2026-08-05_a008-factor-propagation_note.md`
§0, verbatim: *"$E_g = \hbar\omega_m$ — not $2\hbar\omega_m$. Numerically $\hbar\omega_m = 2m_ec^2 =
1.022$ MeV"*, with §3.3's corollary *"$G_c/I_\omega = \omega_C^2 = 1$"* — **the ratio is RULED**
even though the absolute moduli are placeholders. **This lane uses ONLY the ratio.**

**(c) The rotational curvature slope is `c_R = √2 c₀`.** `cosserat-mass-gap.md`:104, Grant-ratified
2026-06-23, engine-faithful to `W_κ = γ Σκ²` with no `½`; `c_R = √(2γ/I_ω)`.

Together: **cold rotational dispersion** $\omega^2(k) = 2c_0^2k^2 + (2\omega_C)^2$, band bottom
`2ω_C`, no propagating state below it.

### §1.2 — The one coupling, and its equation of motion (derived, not asserted)

From `cosserat-mass-gap.md`:51, $\varepsilon^A_{ij} = \tfrac12(\partial_iu_j-\partial_ju_i) -
\epsilon_{ijk}\omega_k$. Write the macro-rotation carried by the shear wave as `A_z ≡
½(∂_xu_y−∂_yu_x)` and the node micro-rotation as `ω_z`. Then $\varepsilon^A_{xy} = A_z-\omega_z$
and $\varepsilon^A_{yx} = -(A_z-\omega_z)$, so with `W_micro = G_c Σ_ij (ε^A_ij)²`:

```
W_micro           =  2 G_c (A_z - omega_z)^2
I_omega * d2(omega_z)/dt2  =  -dW/d(omega_z)  =  4 G_c (A_z - omega_z)
  =>   d2(omega_z)/dt2 + omega_m^2 * omega_z  =  omega_m^2 * A_z ,   omega_m^2 = 4 G_c / I_omega
```

**This is a driven series-resonant tank whose resonance IS the gap, driven by the shear wave's own
macro-rotation, with the SAME `G_c` setting both the drive strength and the gap.** That identity is
why the answer is a pure ratio and carries no absolute modulus (SVA row 7).

Steady state at real drive frequency `ω`:

```
omega_z / A_z            =  omega_m^2 / (omega_m^2 - omega^2)
zeta  ==  |eps^A| / |A_z| =  |A_z - omega_z| / |A_z|  =  (omega/omega_m)^2 / |1 - (omega/omega_m)^2|
```

**`ζ` is THE LEAK MEASURE.** It is the fraction of the shear wave's own rotation content that
appears as **relative** (energy-storing) micro-rotation — i.e. the fraction that actually engages
the `G_c` bond. Deep below the gap `ζ → (ω/ω_m)² → 0`: the micro-rotation is **slaved** to the
macro-rotation, the mutual element sees no differential, and nothing is tapped. Above the gap the
denominator changes sign and `ζ` passes through resonance — that is the CHANNEL-OPENS regime.

### §1.3 — The graded gap, and the ONE exponent the whole lane turns on

Let `G_c^eff(r) = G_c·S(r)^a` and `I_ω^eff(r) = I_ω·S(r)^{−b}`. Then

```
omega_m(r)  =  2 omega_C * S(r)^p ,        p == (a + b)/2         [the GAP EXPONENT]
```

**`a` and `b` are the two numbers canon does not state.** The engine's coded choice is `a = 2`
(`cosserat_field_3d.py`:767 multiplies `W_micropolar * G_c` by `S_eps_sq`, and `:761` defines
`S_eps_sq = clip(1 − eps_sq/epsilon_yield², 0, 1)`, which is `S_ε²`, so the effective modulus is
`G_c·S_ε²`). No canon leaf states `a`; no canon leaf states `b`. **Both are receipted two-method in
§5.1 and BRACKETED in §4, never assumed.**

> ⚑ **FLAG-EXP, declared at freeze against the dispatch's own stated expectation.** The dispatch
> states *"gap² = 4G_c·S_ε/I_ω ⇒ gap ∝ √S_ε"*, i.e. `a = 1, b = 0, p = 1/2`. **The engine codes
> `a = 2`** (the kernel it multiplies by is `S_eps_sq ≡ S²`, not `S`), giving `p = 1`. This lane
> runs BOTH and reports the discrepancy as a flag; §2.6 shows the BIN is identical for every
> `p < 2`, so the flag is disclosed and non-blocking, and that is stated here BEFORE the run rather
> than discovered after it.

---

## §2 — THE DERIVATION, WRITTEN OUT AT FREEZE (so the run is read as a CHECK, not a discovery)

**Frozen:** `every closed form in section 2 is available before any code exists; the driver's job is`
`to evaluate them at declared precision and to run the receipts, NOT to discover them; any`
`quantity the driver produces that is not derivable from section 2 is reported as an UNPLANNED`
`DIAGNOSTIC and adjudicates nothing.`

### §2.1 — The profile and the lattice (carried byte-identical from the predecessors)

```
A(r) = r_sat / r ,  r_sat = 7GM/c^2 ,  S = sqrt(1 - A^2)
x  == r - r_sat ,  nodes at x_n = (n - 1 + theta) * l_node ,  n = 1, 2, ...  (n=1 = innermost intact cell)
S_n^2 = x_n (2 r_sat + x_n) / (r_sat + x_n)^2                 [EXACT, cancellation-free]
S_n^2 -> 2 x_n / r_sat        as x_n/r_sat -> 0                [near-wall form]
S_1   -> sqrt(2 theta * l_node / r_sat)                        [the LAST-CELL FLOOR]
```

Write the single mass-carrying dimensionless ratio once and use it everywhere:

```
x  ==  l_node / r_sat  =  l_node c^2 / (7 G M)
```

### §2.2 — The drive, in the same units

```
Omega  ==  omega * r_sat / c_0            [the v2.4 hyperboloidal frequency variable]
omega / omega_C  =  Omega * x             [since omega_C = c_0 / l_node]
```

### §2.3 — The crossing condition, and the CELL COUNT

The local gap falls to the drive where `ω_m(r) = ω`:

```
2 omega_C S^p = omega       =>    S_open^p = Omega * x / 2       =>    S_open = (Omega x / 2)^(1/p)
```

The number of **intact lattice cells** at which the drive sits at or above the local gap:

```
N_open(Omega, p, theta)  =  # { n >= 1 : S_n <= S_open }
                         =  max( 0 , floor( x_open / l_node - theta + 1 ) ) ,
   x_open / l_node  =  (1 / (2x)) * (Omega x / 2)^(2/p)          [near-wall inversion]
```

**`N_open = 0` is the GAP-CLOSED statement and `N_open ≥ 1` is the CHANNEL-OPENS statement, and it
is an INTEGER — an integer either matches or it does not.** Computed BOTH by this inversion and by
a direct node-by-node count from the exact cancellation-free `S_n`; the two must agree as exact
integers (gate `G-COUNT`).

### §2.4 — ★ THE KNIFE-EDGE AT `p = 2`, WHICH IS THE WHOLE STRUCTURE OF THE ANSWER

`GAP-CLOSED ⟺ S_open < S_1`. Substituting the two closed forms:

```
(Omega x / 2)^(1/p)   <   sqrt(2 theta x)
```

Taking logs and letting `x → 0` (every astrophysical mass has `x < 1e-16`), the `x`-powers are
`x^{1/p}` on the left and `x^{1/2}` on the right, so

```
p < 2   =>   LHS vanishes FASTER than RHS   =>   GAP-CLOSED , and the margin GROWS without bound as x -> 0
p > 2   =>   LHS vanishes SLOWER            =>   CHANNEL-OPENS, and the margin grows the other way
p = 2   =>   the x-dependence CANCELS EXACTLY: the verdict becomes MASS-INDEPENDENT and is decided
             by the pure numbers Omega, theta alone -- GAP-CLOSED iff Omega < 4 theta
```

**This is the lane's FORM-class content and it is ratio-only**: `p = 2` is the exact knife-edge, the
verdict is a competition between two powers of `ℓ_node/r_sat`, and NO absolute modulus appears.
**Frozen:** `the result doc must report the knife-edge exponent p_crit = 2 and the mass-independence`
`AT p = 2 as a derived structural statement, must report which bracketed members fall on which side`
`of it, and must NOT present p_crit = 2 as a measurement.`

### §2.5 — ★ WHY NO TIME-AVERAGED POWER TRANSPORTS WHEN `N_open = 0` (the energy-ledger row, proved)

Below the gap the transfer function `ω_z/A_z = ω_m²/(ω_m² − ω²)` is **REAL** — `ω_m² − ω² > 0` at
every cell, and the rotational branch supplies **no propagating state at `ω`**, hence **no radiation
resistance**, hence no imaginary part. The instantaneous power delivered into the rotational tank is

```
P(t) = (dW_micro/dt) = 4 G_c (A_z - omega_z) * d(omega_z)/dt
```

With `A_z = Â cos ωt` and `ω_z = (real gain)·Â cos ωt`, `(A_z − ω_z) ∝ cos ωt` and
`dω_z/dt ∝ −sin ωt`, so `P(t) ∝ −sin ωt cos ωt` and

```
<P>_period  =  0   EXACTLY
```

**No port is crossed; the admixture is a reactive store on the Axiom-3 rim.** This is a THEOREM of
the reality of the transfer function, and the frozen gate `G-REAL` verifies the reality of the
denominator at every swept point rather than assuming it. **Frozen:** `the zero-time-averaged-power`
`statement is presented as a DERIVATION whose one empirical input is the sign of (omega_m^2 -`
`omega^2), and the driver must report the minimum of that quantity over the entire sweep rather`
`than merely its sign.`

### §2.6 — ★ THE LEAK BOUND, AND ITS IDENTITY WITH THE BIN

Evaluate `ζ` at the cell where the gap is smallest, i.e. `n = 1`:

```
zeta_max  =  (omega / omega_m(S_1))^2 / |1 - (omega/omega_m(S_1))^2| ,   omega_m(S_1) = 2 omega_C S_1^p
```

and, at `p = 1` where the near-wall forms are exact to `O(x)`, the closed form collapses to a pure
number:

```
zeta_max  ->  Omega^2 * x / (8 theta)        [p = 1, leading order]
```

More usefully, for ANY `p`, in terms of the SAME two closed forms that decide the bin:

```
(omega/omega_m(S_1))  =  (S_open / S_1)^p        =>        zeta_max  =  (S_open/S_1)^(2p) / |1 - (S_open/S_1)^(2p)|
```

> ★ **THE BIN AND THE LEAK BOUND ARE THE SAME INEQUALITY.** `GAP-CLOSED ⟺ S_open < S_1 ⟺ ζ_max < 1`,
> and `ζ_max` is *exactly how far below unity*. One number does both jobs. **Frozen:** `the result`
> `doc must state this identity and must report zeta_max as the shipped leak bound, in the same`
> `table as N_open.`

**Decay depth of the converted near-field, in cells.** Below the gap, `k² = (ω²−ω_m²)/c_R² < 0`, so
`k = iκ` with

```
kappa  =  sqrt(omega_m^2 - omega^2) / c_R   ->   omega_m(r) / c_R      (since omega << omega_m)
d_cells  ==  1 / (kappa * l_node)  =  c_R / (omega_m(r) l_node)  =  sqrt(2) c_0 / (2 omega_C S^p l_node)
          =  1 / ( sqrt(2) * S^p )                                   [in CELLS]
```

reported at both ends of the approach (`S = 1` far field; `S = S_1` last cell).

**Residual back-action on the shear channel (the ONE place an absolute-modulus ratio enters).**
The stored relative-rotation energy per cell against the shear energy is `2(G_c/G)ζ_n²`, and

```
zeta_n  =  zeta_max * (S_1/S_n)^(2p)   =  zeta_max * (theta/(n-1+theta))^p        [near-wall, p]
SUM_n zeta_n^2  =  zeta_max^2 * theta^(2p) * SUM_n (n-1+theta)^(-2p)
                =  zeta_max^2 * theta^2 * psi'(theta)                              [at p = 1, CONVERGENT]
```

**Frozen:** `the total residual phase perturbation on the reflected shear wave is reported as`
`2*(G_c/G)*zeta_max^2*theta^2*psi_1(theta) at p = 1 and as the corresponding zeta(2p) sum at other`
`p, it is reported in its OWN output field tagged PLACEHOLDER-CONDITIONED because it rides the`
`absolute-modulus ratio G_c/G which is an engine placeholder, and the SCALE-UNDERDETERMINED bin`
`fires on that field and on that field alone.`

### §2.7 — What is NOT derived here, and is therefore bracketed

The **rotational band TOP** is not stated by canon (`srs-band-structure.md`:118 — the microrotation
channel is an unsurveyed named follow-on). It matters ONLY in the `CHANNEL-OPENS` arm, where one
must ask whether the drive is inside the band or above its top. **Frozen:** `the rotational band top`
`is BRACKETED at three declared members -- (T1) the continuum-dispersion extrapolation to the srs`
`Nyquist wavevector sqrt(2)pi/l_node, giving omega_top = 2 omega_C sqrt(pi^2 + 1); (T2) the scalar`
`vector-channel lower bracket end 5.4414 omega_C; (T3) the vector upper bracket end 17.0111`
`omega_C -- all three are REPORTED and NONE is chosen, and if the GAP-CLOSED bin fires the bracket`
`is MOOT and must be reported as moot rather than silently dropped.`

---

## §3 — METHOD (frozen order of operations)

1. **Read the predecessors' shipped artifacts READ-ONLY** and reproduce their numbers before
   computing anything new (`G-NC-BAND`, `G-NC-SLAST`). No predecessor file is written by this lane.
2. **Run the canon-absence pattern battery** (§5.1), two methods, no `\b`, scan surface =
   `git ls-files` with this lane's own artifacts excluded by construction.
3. **Evaluate the §2 closed forms** at `dps = 60` over the full frozen sweep (§4).
4. **Compute `N_open` two ways** — closed-form inversion and direct node-by-node count over the
   exact cancellation-free `S_n` — and require exact integer agreement (`G-COUNT`).
5. **Compute `ζ_max` two ways** — from the transfer function directly, and from the `(S_open/S_1)`
   identity of §2.6 — and require agreement (`G-ZID`).
6. **Report the knife-edge structure**: `p_crit`, which bracket members fall on which side, and the
   mass-independence at `p = 2` (`G-KNIFE`).
7. **Run the self-tests** (§6). Every one must FIRE.
8. **Run the whole thing twice**, emit one JSON, require identical digest (`G-DET`).

**Frozen:** `the driver is committed BEFORE any result JSON exists, and the prereg is committed and`
`pushed ALONE before the driver exists.`

---

## §4 — THE FROZEN SWEEP (no member may be added, dropped or re-weighted after a number is seen)

```
mass grid          M/M_sun in {1, 10, 62, 100} ,  M_ref = 62         [byte-identical to echo-delay v2]
theta              in {1.0, 0.5}                                     [sub-cell placement, carried]
drive band         Omega in [Omega_R - |Omega_I|, Omega_R + |Omega_I|], 65 points inclusive
                   endpoints read PROGRAMMATICALLY from the v2.4 shipped JSON
                   research/drivers/coldq_pole_v2p4_root_results.json
                   keys certified_root/Omega_re_mp and certified_root/Omega_im_mp
gap exponent p     in {0.5, 1.0, 1.5, 2.0, 2.5, 3.0}                 [the BRACKET; see below]
density branch     in {RHO-A, RHO-B}                                 [FORK-3(b), both run]
vector band top    beta in {5.4414, 17.0111} omega_C                 [BRACKETED(pending-ruling)]
rot band top       in {T1 = 2*sqrt(pi^2+1), T2 = 5.4414, T3 = 17.0111} * omega_C   [REPORTED, none chosen]
```

**The `p` bracket, and why exactly these six.** `p = (a+b)/2` with `a` the `G_c(A)` exponent and `b`
the `I_ω(A)` exponent. The enumerated members and their provenance:

| `p` | `(a, b)` | provenance of the member | side of `p_crit = 2` |
|---|---|---|---|
| `0.5` | `(1, 0)` | **the dispatch's stated expectation** (`gap ∝ √S_ε`) | below |
| `1.0` | `(2, 0)` | **the engine's coded `a`** (`cosserat_field_3d.py`:767 × `:761`) with `I_ω` ungraded as canon's Lagrangian writes it (`cosserat-mass-gap.md`:30) | below |
| `1.5` | `(3, 0)` or `(0, 3)` | a filler member, so the bracket is not two-point | below |
| `2.0` | `(1, 3)` | the dispatch's `a` with the **RHO-B analogy** `I_ω ∝ S^{−3}` | **ON the knife-edge** |
| `2.5` | `(2, 3)` | the **engine's `a`** with the **RHO-B analogy** for `I_ω` | above |
| `3.0` | `(3, 3)` | the loosest member, so the above-knife arm is not single-point | above |

**Frozen:** `no member of the p bracket is preferred, all six are run, and the result doc must`
`report the bin SEPARATELY for each member and must NOT collapse them into a single verdict unless`
`every member agrees; the RHO-B analogy for I_omega is DECLARED HERE AS AN ANALOGY AND NOT AS`
`CANON, because canon states no I_omega grading law, and the result doc must repeat that`
`declaration at every site where a p >= 2 member is quoted.`

**Reporting grid size.** `4 masses × 2 θ × 65 band points × 6 p × 2 ρ-branch = 6240 rows.`

---

## §5 — THE GATES (frozen before any number exists; UNRUN ≠ PASSED)

### §5.1 — The canon-absence pattern battery (two methods, no `\b`, engines named)

**METHOD A = `git grep -P` (PCRE, ASCII `\w`). METHOD B = Python `re` on `str` (Unicode `\w`).**
Scan surface = the output of `git ls-files` for `manuscript/`, `research/`, `src/`, restricted to
tracked text files, **with this lane's own four artifacts excluded by construction** (the prereg,
the driver, the number-check and the result doc — the pilot-5 `G-SCAN` self-reference repair).

| id | pattern (identical string handed to both engines) | what its ABSENCE would receipt |
|---|---|---|
| `P1` | `G_c\s*\(\s*A\s*\)` | no `G_c(A)` grading law is written as a function of the amplitude |
| `P2` | `G_c[^\n]{0,24}(S\^|S_\\?eps|S\(A\)|\\sqrt\{1)` | no `G_c`-times-kernel grading law in prose or math |
| `P3` | `I_\\?omega\s*\(\s*A\s*\)|I_\{?\\?omega\}?\s*\(\s*A\s*\)` | no `I_ω(A)` grading law |
| `P4` | `(I_\\?omega\|micro.?inertia)[^\n]{0,40}(S\^\|/\s*S\|S\(A\))` | no `I_ω`-rides-a-kernel statement |
| `P5` | `(rotational\|Cosserat\|micro.?rotation)[^\n]{0,40}band\s*top` | no rotational band top is stated |

**Frozen:** `the two methods must return the SAME hit set per pattern; if they disagree the`
`DISAGREEMENT is the reported result, the UNION is used, and nothing is reconciled silently. A`
`pattern returning zero hits on BOTH methods is an ABSENCE RECEIPT and is reported as such; a`
`pattern returning hits is reported with every hit quoted verbatim, and if any hit is a genuine`
`grading law then the corresponding p-bracket member is superseded by it and the result doc says`
`so in its headline.`

### §5.2 — Derived-constant second-method checks (pre-freeze, per SVA row 9)

| derived constant | method 1 | method 2 |
|---|---|---|
| `p_crit = 2` | the log-slope argument of §2.4 | direct: solve `(Ωx/2)^{1/p} = √(2θx)` for the `p` at which `d/d(ln x)` of both sides agree |
| `ζ_max` at `p = 1` | the transfer function evaluated at `S_1` | the closed form `Ω²x/(8θ)` |
| `Σ_n (n−1+θ)^{-2}` | mpmath `polygamma(1, θ)` | direct summation to `1e7` terms plus an exact Euler–Maclaurin tail |

### §5.3 — The gate table

| gate | what it certifies | frozen tolerance |
|---|---|---|
| **G-NC-BAND** ★ | the frozen band endpoints, read PROGRAMMATICALLY from the v2.4 shipped JSON, reproduce `Ω_R` and `\|Ω_I\|` to EXACT STRING EQUALITY at the JSON's own `_mp` rendering | exact string |
| **G-NC-SLAST** ★ | this lane's `S_1` at `M_ref = 62 M_⊙`, `θ = 1`, computed from the exact cancellation-free form, reproduces the predecessor's shipped `S_last` | `1e-40` rel |
| **G-COND** | the naive float64 `1 − A²` at the innermost node returns exactly `0.0`, while the cancellation-free `S²` returns a positive number | naive `== 0.0` exactly AND `S² > 0` |
| **G-COUNT** ★ | `N_open` by closed-form inversion equals `N_open` by direct node-by-node count over the exact `S_n`, at every one of the 6240 rows | exact integers |
| **G-ZID** ★ | `ζ_max` from the transfer function equals `ζ_max` from the `(S_open/S_1)^{2p}` identity | `1e-45` rel |
| **G-REAL** ★ | `ω_m²(S_n) − ω²` is strictly positive at every intact cell of every row for which `N_open = 0` — the reality of the transfer function, which the zero-power theorem stands on; the MINIMUM over the whole sweep is reported, not merely its sign | `> 0` strictly |
| **G-KNIFE** | at `p = 2` exactly, the quantity `S_open/S_1` is INDEPENDENT of mass: its spread across the four-mass grid is zero | `1e-45` |
| **G-SUM** | `Σ_n (n−1+θ)^{-2}` by summation-plus-tail equals `polygamma(1, θ)` | `1e-30` rel |
| **G-SCAN** | METHOD A and METHOD B hit sets identical per pattern | identical sets |
| **G-DET** ★ | two full runs, identical digest, byte-identical JSON apart from `_runtime_sec` | identical digest |

**Frozen:** `any RUN gate FAILS, or any self-test fails to fire, or any gate is UNRUN => this lane`
`reports LEAK-NOT-CERTIFIED, adjudicates NO bin, and routes to a successor with a new version`
`number. No tolerance is retuned after a number is seen.`

---

## §6 — THE FIREABILITY SELF-TESTS (each MUST fire; a gate that cannot fail is not a gate)

| self-test | frozen firing condition |
|---|---|
| **FT-COUNT** | injecting a drive `Ω` scaled by `1e30` must make `N_open ≥ 1` at `M_ref, θ = 1, p = 1` — i.e. the counter CAN return a non-zero and the `0` is a measurement, not a hard-coded floor |
| **FT-ZID** | perturbing the transfer-function `ζ_max` by a relative `1e-40` must make `G-ZID` fail |
| **FT-REAL** | injecting `p = 12` (far above the knife-edge) at `M_ref` must drive `ω_m²(S_1) − ω²` NEGATIVE at at least one cell, so `G-REAL` is falsifiable |
| **FT-KNIFE** | at `p = 1.99` and `p = 2.01` the mass-spread of `S_open/S_1` must be NON-zero and of OPPOSITE sign in its mass-trend, so `G-KNIFE`'s zero at `p = 2` is a real knife-edge and not a coincidence of the grid |
| **FT-COND** | the naive float64 `1 − A²` at the innermost node must return exactly `0.0` |
| **FT-SCAN** | a sentinel string placed in a file OUTSIDE the scanned tree must return zero hits on both methods, and a sentinel known to be inside the tree must return the same non-zero set on both — **the sentinels are sited outside `manuscript/`, `research/` and `src/` by construction** (the pilot-5 repair) |

---

## §7 — THE BINS (frozen; the verdict is one of these and nothing else)

| bin | condition |
|---|---|
| **`GAP-CLOSED`** | `N_open = 0` at EVERY row of the frozen sweep for the member(s) in question; the margin is REPORTED as `log10(S_1/S_open)` and as the minimum `ω_m(S_1)/ω` over the band; `ζ_max` is shipped as the evanescent leak bound; the decay depth in cells is shipped at both ends; the zero-time-averaged-power theorem is stated with `G-REAL`'s measured minimum; the residual observable is named or declared nil |
| **`CHANNEL-OPENS`** | `N_open ≥ 1` at any row; the crossing radius is shipped as `(r_open − r_sat)/ℓ_node` and as `S_open`; the coupled two-channel transfer `\|T_conv\|²(ω)` is computed on the discrete graded chain with exact per-cell matrices, both channels, the `G_c S_ε` coupling, and reported across the band |
| **`SCALE-UNDERDETERMINED`** | fires on any output field whose MAGNITUDE rides an absolute modulus that is an engine placeholder; **may co-fire with either of the above**; the affected field is named and quarantined |
| **`UNDERDETERMINED-CANON`** | a needed grading law is absent; the missing laws are ENUMERATED exactly, with two-method absence receipts; **may co-fire with either of the first two** |

**Frozen bin-arithmetic:** `if different members of the p bracket land in different bins, the result`
`doc reports BOTH bins, states exactly which members give which, and reports UNDERDETERMINED-CANON`
`as a co-firing bin naming the exponent that decides it. It does NOT pick a member. It does NOT`
`report a single headline bin unless every member of the bracket agrees.`

> ★ **HAND-EVALUATED AT FREEZE AND DISCLOSED, so the run is read as a CHECK and not as a
> discovery.** Substituting `x = ℓ_node/r_sat ≈ 6e-19` at `M_ref = 62 M_⊙` and the band top
> `Ω ≈ 2.86` into §2.3–§2.4 by hand indicates: **`N_open = 0` for every member with `p < 2`, with a
> margin of roughly nine orders of magnitude in `S` at `p = 1` and roughly eighteen at `p = 0.5`;
> `N_open ≥ 1` for `p = 2.5` and `p = 3`; and `p = 2` on the knife-edge decided by `Ω` vs `4θ`.**
> The result doc must present these as CONFIRMED DERIVATIONS where they hold and must report any
> departure from this hand-evaluation as an instrument finding requiring diagnosis.

---

## §8 — THE FENCE (what this lane does NOT license, frozen)

1. **Nothing about the rotational channel AT or INSIDE `r_sat`.** This lane's domain stops at the
   innermost intact cell. The ruling's carve-out — *"unwalled at `r_sat`, its own wall being a κ-amplitude
   surface"* — and the ROUTED frontier question *"the rotational channel behaves at `r_sat` like a
   penetrating radiation"* are **NOT touched**. **MeV-scale rotational radiation is OUT OF SCOPE**;
   one cross-reference line at result and nothing more.
2. **No adjudication of the cross-grade aggregation fork** (L∞ vs normalized-L2), which the
   predecessor lane established is canonically underdetermined. This lane brackets and reports.
3. **No adjudication of FORK-3(b)**, of the `β` bracket, of the `K(A)` fork, of `FLAG-CAUSAL`, or of
   any predecessor's bins.
4. **No promotion of the engine's coded `a = 2` to canon**, and no invention of an `I_ω` grading law.
   The `p ≥ 2` members exist to bracket, not to assert.
5. **No AVE-vs-competitor discrimination claim.** The ECO free-reflectivity degeneracy stands.
6. **No KB or manuscript edit, no `src/ave` edit, and no predecessor-artifact edit.** Every
   predecessor file this lane reads is byte-untouched; the receipts are in the result doc.
7. **No claim minted.** No `clm-`/`def-`/`exp-`/`sup-`/`ilk-`. No solidity moved.
