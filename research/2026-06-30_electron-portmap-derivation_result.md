# RESULT — Electron Port-Coupling Network: does a self-braced standing electron BIND?

**Date:** 2026-06-30 · **Lane:** implementer · **Branch:** `analysis/electron-portmap-derivation`
(worktree `/private/tmp/electron-portmap`, off `origin/main` @ `778823e9`).
**Prereg (frozen FIRST):** [`2026-06-30_electron-portmap-derivation_prereg_FROZEN.md`](2026-06-30_electron-portmap-derivation_prereg_FROZEN.md)
(frozen commit `a6c03c72`). Adjudication criteria §5 followed exactly; none dropped (Rule 11).
**Type:** DERIVATION / ANALYSIS. **NO simulation.** Self-consistency of the symbolic chain only.
**Class (consistency-vs-emergence):** **C — CONSISTENCY** throughout (the mechanism, if it binds,
is a FORM-chord peer-with-SM; the SIZE is a scale tied to imported `L_NODE`; `R·r=¼` is a Class-B
input; α appears only through the flagged echo channels). NOT Class-D emergence.

> **UPDATE 2026-06-30 (Grant T2 ruling landed — verdict lifts CONDITIONAL-BIND → BINDS).** The single
> blocking input this result forked on — the `def-vyvsn1` grade-attribution of `V_yield` — was
> **RULED = T2** by Grant (2026-06-30). `V_yield` is the transverse Cosserat (T2) self-trap wall; the
> longitudinal-A1 mass channel does NOT saturate until the higher `V_snap = V_yield/√α` (≈11.7×). So
> the electron's A1 mass core operates at strain **`A = V_yield/V_snap = √α ≈ 0.085`** — deeply
> sub-saturated. At `A=√α` the §2.3 deep-saturation runaway **never fires on the mass channel**: the
> pull is Coulomb-class (`p ≈ 1–2 ≪ 3`), the `r⁻³` brace out-steepens it, `dF_net/dr > 0` → **stable
> self-braced electron.** The §5 verdict is updated to **BINDS (under the Grant T2 ruling)**. This is
> the SYMBOLIC verdict at `A=√α`; the greenlit sim CONFIRMS the deep-core slope + α-robustness. Still
> Class-C (`A=√α`, `m_e`, α all imported/echo). See §5.3. The two former open items — def-vyvsn1 and
> the `S^0.25`-vs-`S^0.5` exponent — are RESOLVED (§7.2).

---

## 0. HEADLINE (the four deliverable answers, one line each)

> **INWARD-LEG SIGN: COMPRESSIVE (inward).** The rectified time-average of the μ→A1 back-reaction
> lowers the effective bulk compliance stiffness at the amplitude peak (`C_eff=C_0/S` softens, the
> ponderomotive index `n_grav=S^(−1/2)` rises), and the self-consistent index gradient lenses the
> envelope into itself. `⟨F_A1⟩` is inward. (V1 holds.) **DERIVED, not assumed** — see §2, incl.
> the honest caveat that the SAME `S→0` limit makes the varactor a runaway (positive feedback),
> which is exactly why a brace is REQUIRED and why its steepness is the whole question.
>
> **BRACE: the winding DC-circulation angular-momentum reactive pressure `∝ L_w²/(m r³)`, backstopped
> by the topological ropelength hard-wall at `r → r_floor ~ (1/2π)·(perimeter floor)`.** Candidate (c)
> saturation-stiffening is NOT an independent brace — it is the SAME `S→0` that drives the pull
> (it cannot both pull and brace at the same sign). Candidate (a) IS present (the (2,3) winding
> carries a nonzero DC circulation `L_w`, and centrifugal-reactive pressure scales `r^{−3}`, steeper
> than the pull). Candidate (b) is a HARD floor, not a smooth brace. **Derived which is present: (a)
> smooth + (b) hard-wall; (c) disqualified as a brace.**
>
> **EQUILIBRIUM: `r* ~ L_NODE` (Compton scale) — order-consistent, NOT independently derived.**
> The `r^{−3}` brace vs the pull crosses at a scale set by `L_w` and the envelope stiffness; both
> are tied to the imported `L_NODE=ℏ/(m_e c)` and the `R·r=¼` Class-B input. Scale-consistent (V5),
> but this is calibration-consistency, NOT a derivation of the size.
>
> **STABILITY VERDICT: BINDS (under the Grant 2026-06-30 T2 ruling) — see §5.** The `r^{−3}`
> centrifugal brace vs a `~r^{−1..−2}` (Coulomb-class) ponderomotive pull gives a stable well
> (`dF_net/dr>0`). The one thing that could have broken it — the `S→0` varactor runaway of the deep-
> saturation core — **does not fire on the mass channel**, because the T2 ruling puts the A1 core at
> `A=V_yield/V_snap=√α≈0.085`, i.e. sub-saturated (`S(√α)=√(1−α)≈0.996`), far from the `S→0` limit.
> With the runaway off the table, the brace out-steepens the (sub-saturation, `p<3`) pull and the
> electron binds as a stable self-braced reactive soliton. Stated precisely in §5.3. *(The pre-ruling
> reading was CONDITIONAL/FORK; the ruling closed the fork toward BIND — see the §5.3 UPDATE box.)*

**One-paragraph plain reading.** The electron picture DOES assemble as a real reactive port network
with a genuine inward pull and a genuine reactive (lossless) outward brace — so it is NOT an
immediate NO (the naive "there's no brace at all → implosion" failure does not occur; a brace IS
present, and it is reactive, not the forbidden dissipative crutch). BUT the same nonlinearity that
supplies the pull (the `S→0` varactor runaway) is a positive feedback whose steepness competes with
the brace's steepness, and at the symbolic level the winner depended on an un-adjudicated
grade/exponent input. **That input is now adjudicated (Grant 2026-06-30 T2 ruling):** the runaway
lives on the deep-saturation A1 channel, but the A1 mass core operates at `A=√α≈0.085` — sub-
saturated — so the runaway never fires there. With the runaway off the mass channel, the pull is
Coulomb-class (`p≈1–2`), the `r^{−3}` brace out-steepens it, and the network **BINDS** as a stable
self-braced reactive soliton. This is the SYMBOLIC verdict at the `A=√α` operating point; the greenlit
sim confirms the deep-core slope and the α-robustness. Reported as **BINDS (under the T2 ruling)** —
a closed fork, not a manufactured PASS: the ruling is Grant's physics call, and the operating point
`A=√α` it forces is an exact α-echo (Class-C), not a fitted convenience.

---

## 1. THE PORT NETWORK (reuse the 3-channel graded-impedance structure; pose the STABILITY question)

### 1.1 Ports (native Cosserat, NOT Cartesian)

Reusing the canonical three-channel graded-vacuum-impedance network
(`resonant-lc-solitons.md`:120–124; the coupled-eigensolve H-structure,
`coupled_eigensolve.py`), with the ROLE labels the engine-reroute Resultbox fixed:

| Port | Sector | Reactance kind | Impedance | Bias rail | State variable(s) | Role |
|---|---|---|---|---|---|---|
| **P_A1** | A1 dilatation = MASS envelope | **Capacitive** (varactor `C_eff=C_0/S`) | `Z_bulk=ρc_bulk` | `A→1` (`V_snap` core) | strain `A=|V|/V_yield`; conjugate momentum `π_V` | the compressive mass "3" |
| **P_μ (DC)** | Cosserat (2,3) winding = CHARGE | **Inductive**, static circulation | `Z_shear=ρc_shear` | `V_yield` self-trap | `Link(∂Ω,F)=−1`; DC circulation `L_w` | static topological charge boundary (no real power) |
| **P_μ (AC)** | Cosserat (2,3) winding = the ringing | **Inductive**, oscillating | `Z_shear` | — | `b_ω` amplitude; `ω_dot` (the L-state) | the AC circulation that gets RECTIFIED |
| **P_Γ** | Γ=−1 wall = TERMINATION | reflective (Op17-bounded BC) | `Z_core=Z_0√S→0` | at the `S→0` shell | `Γ = (Z_core−Z_0)/(Z_core+Z_0) → −1` | the self-woven perfect mirror |
| **P_EM** | radiative carrier port | matched, `Z_0` | `Z_0=376.7Ω` | — | far-field coupling | the α-leak CARRIER (NOT in the binding loop; work-exchanging) |
| **P_ε** | T2 transverse permittivity | capacitive `ε_eff=ε_0 S` | `Z_wave=√(μ/ε)→∞` | rupture read | transverse polarization | enters ONLY as the wall's dual (sign-selector), see §1.4 |

**Sector-ownership discipline (memory: A1⊥T2 cross-wiring watch).** Mass = A1 (P_A1). Charge =
Cosserat winding (P_μ). μ-sign = the wall's chirality selector. These are NEVER cross-wired. The
binding loop we analyze is **P_A1 ↔ P_μ(AC/DC), terminated by P_Γ**. P_EM is the radiative carrier
(work-exchanging, α-leak) — it sits OUTSIDE the reactive binding loop and is the reason the electron
has a finite loaded Q but does NOT decay (`resonant-lc-solitons.md`:92,100–104). P_ε is the wall's
capacitive-vs-inductive dual (wall-fork H3, `resonant-lc-solitons.md`:108); it is a SIGN selector,
not an independent binding DOF.

### 1.2 The couplings (the graph edges)

```
                          P_EM (Z_0, radiative CARRIER — OUTSIDE the binding loop, α-leak)
                            :  (loaded-Q coupling only; no net binding force)
                            :
   ┌─────────────────────── P_Γ (Γ=−1 wall) ───────────────────────┐
   │  reflective BC: Z_core=Z_0√S → 0 as A→1 (self-woven mirror)    │
   │                                                                │
   │   ┌──────────────┐   κ_couple = S(A)-front-gated   ┌────────┐  │
   │   │   P_A1        │◄───────── mutual  ────────────►│  P_μ    │  │
   │   │ MASS envelope │   (varactor C_eff=C_0/S;        │ CHARGE  │  │
   │   │  capacitive   │    ponderomotive n_grav=S^-1/2) │inductive│  │
   │   │  C_eff=C_0/S  │                                 │ DC: L_w │  │
   │   └──────────────┘                                 │ AC: b_ω │  │
   │          ▲                                          └────────┘  │
   │          │ rectified DC compression (§2)  centrifugal r^-3 (§3) │
   └──────────┴─────────────────────────────────────────────────────┘
```

Two coupling edges carry the binding physics:

1. **μ(AC) → A1 back-reaction (the INWARD leg, §2).** The AC winding circulation, run through the
   saturation nonlinearity, has a nonzero DC time-average that acts on the A1 envelope. Coupling is
   the S(A)-front-gated mutual term (the `coupled_cage_winding` front gate; `κ_chiral=α·κ̃(2,3)`,
   `research/2026-06-09_...:52`). This is a **ponderomotive / parametric** coupling — the fast AC
   drives a slow DC envelope force.
2. **A1 → μ(DC) reaction (the BRACE leg, §3).** Compressing the A1 envelope (shrinking `r`) forces
   the DC circulation `L_w` into a smaller loop; conservation of the winding integer + circulation
   raises the reactive centrifugal pressure `∝ L_w²/(m r³)`. This is the outward push.

### 1.3 Losslessness — CONFIRMED via Tellegen (not asserted)

**Tellegen's theorem:** for ANY network obeying Kirchhoff's laws (KCL at nodes, KVL around loops),
`Σ_branches V_k · I_k* = 0` — a topological identity independent of the branch constitutive laws.
Split into real + imaginary: the real part is `Σ Re(V_k I_k*) = total dissipated power`.

Every branch in the binding loop (P_A1, P_μ-DC, P_μ-AC, P_Γ) is a **purely reactive** element:
- P_A1: `C_eff=C_0/S` — an ideal (lossless) nonlinear capacitor. `Z = 1/(jωC_eff)` is purely
  imaginary.
- P_μ: `Z_shear=ρc_shear` mechanical reactance; the DC circulation is a persistent current in a
  lossless inductor; the (2,3) `Link` is a STATIC topological constraint carrying NO real power
  (`resonant-lc-solitons.md`:124, "lossless-REACTIVE constraint carrying no real power").
- P_Γ: `Γ=−1` is a UNIT-modulus reflection — `|Γ|²=1`, zero power transmitted across the wall
  (`resonant-lc-solitons.md`:52, "100% ... reflects internally").

With every binding-loop branch impedance purely imaginary, `Re(V_k I_k*) = 0` for each, so
`Σ Re(V_k I_k*) = 0` — **the network dissipates zero real power.** To be precise about what does the
work: **given the all-reactive port assignment (Axiom 3), losslessness of the total falls out via
Tellegen** — Tellegen is the topological identity that turns "each branch is reactive" into "the sum
dissipates nothing" without any further assumption; the reactive assignment is the physics input
(Ax3), Tellegen is the bookkeeping that makes it a total-network statement. **#83's dissipative branch
is exactly what breaks it** — a single real-part (`e^{−η dt M}`) branch makes `Σ Re(V_k I_k*) ≠ 0`.
**This is the guard that disqualifies the #83 artifact:** the retracted "stable loop" bought its localization with a
viscosity term `e^{−η dt M}`, which is a REAL-part (dissipative) branch — it would show up as
`Σ Re(V_k I_k*) = −η·(…) ≠ 0`, violating Tellegen for a lossless substrate (Axiom 3). Our binding
loop has NO such branch: the ONLY real-power port is P_EM, and P_EM is explicitly OUTSIDE the binding
loop (it is the radiative carrier / loaded-Q coupling, not a binding force). **Losslessness of the
binding loop: CONFIRMED. (V4 holds.)**

## 2. INWARD LEG — DERIVE THE SIGN (do not assume)

**Question:** is the time-average of the μ(AC)→A1 back-reaction COMPRESSIVE (inward) or EXPANSIVE?

### 2.1 The ponderomotive rectification (the fast→slow average)

The winding runs an AC circulation at the tank frequency `ω_C`: locally `A(r,t) = Ā(r) + δA(r)cos(ω_C t)`,
where `Ā` is the slow (DC) envelope and `δA` the fast AC swing. The A1 bulk sector sees this strain
through the varactor compliance and the ponderomotive index. The DC force on the slow envelope is the
time-average of the fast field's stress. Two equivalent substrate reads, both give the same sign:

**(i) Compliance / capacitance read (energy of the varactor).** The reactive energy stored in the A1
bond capacitor is `U_C = ½ Q²/C_eff = ½ Q² S(A)/C_0` (using `C_eff=C_0/S`). The ponderomotive force on
the slow envelope is `F = −∂⟨U⟩/∂r` at fixed reactive charge. Now `S(A)=√(1−A²)` DECREASES as `A`
grows, and `A` grows as the envelope COMPRESSES (same reactive charge squeezed into a smaller,
higher-strain volume). So along "compress → `r`↓ → `A`↑ → `S`↓", the stored `U_C=½Q²S/C_0` DROPS.
Energy is LOWERED by compressing ⇒ the force `F=−∂U/∂r` points toward SMALLER `r`. **Inward.**

Cross-check the standard varactor intuition: `C_eff=C_0/S → ∞` as `A→1` (`resonant-lc-solitons.md`:32).
A capacitor whose capacitance DIVERGES as you compress it is a capacitor that WANTS to be compressed
(at fixed charge, `U=½Q²/C` falls as `C` rises). This is exactly the SELF-FOCUSING varactor: the more
strained the core, the softer (higher-C) it gets, the more energy is released by compressing further.

**(ii) Refractive-index read (the ponderomotive lens).** `boundary_invariants.py`:129–133 fixes the
sign LOCK `n_grav = S^(−1/2)`, with the mass integrand `n_grav−1 > 0` where strained. `n_grav` RISES
as `A→1` (`S→0`). A wave concentrating strain raises its own local index; the index gradient `∇n>0`
toward the core bends rays INWARD (Fermat / ponderomotive `F=−∇U_wave`,
`research/2026-06-09_...self-focusing...`:15). **The field lenses itself inward. Inward.**

Both reads agree: **the time-averaged μ→A1 back-reaction is COMPRESSIVE.** (V1 HOLDS.)

### 2.2 The rectification IS the mechanism (why AC → DC envelope)

The sign came out inward *because* `S(A)=√(1−A²)` is an EVEN, concave-down function of `A`: the fast
AC swing `A=Ā+δA cos ω_C t` gives, to second order, `⟨S(A)⟩ ≈ S(Ā) + ½ S''(Ā) δA²` with
`S''(A) = −(1−A²)^{−3/2} < 0` everywhere. So the AC swing DEPRESSES the time-averaged `⟨S⟩` below
`S(Ā)` by `½|S''|δA²` — a strictly nonlinear (∝ amplitude²) DC softening. **The winding's AC
oscillation rectifies, through the concave saturation kernel, into a DC reduction of the envelope
stiffness = a DC inward (ponderomotive) compression.** This is the "AC circulation rectified into a
DC compression = rest mass" hypothesis, DERIVED (not assumed) from `S''<0`. The rectified DC envelope
IS the mass envelope (the `⟨U⟩` lowering IS the binding energy well). The rest-mass ledger (§6) reads
the same store.

### 2.3 The HONEST caveat — the inward leg is a POSITIVE FEEDBACK, not a well by itself

The sign is inward — but note WHAT KIND of inward. Because `S'' < 0` and steepens as `A→1`
(`|S''| = (1−A²)^{−3/2}` diverges), the DC softening `∝ |S''|δA²` GROWS as the core compresses. More
compression → more softening → more inward force. **This is a RUNAWAY (self-focusing) positive
feedback, NOT a restoring well.** By itself the inward leg has `dP/dr < 0` with `|dP/dr|` GROWING as
`r→r_core` (the pull gets stronger, faster, the more you compress). A pull that self-steepens toward
collapse is precisely the "would IMPLODE unless braced" of the hypothesis. So §2 confirms the pull's
sign AND confirms the pull is dangerous — the entire question now rests on whether §3's brace
out-steepens this runaway. **The inward leg alone predicts IMPLOSION;** the electron exists only if
the brace wins the steepness contest (§5). This is the honest framing — the inward sign is not, by
itself, good news for binding.

## 3. BRACE LEG — DERIVE WHICH reactance supplies it

Three candidates were pre-registered. We derive which are actually present in the network and their
`r`-scaling, and we do NOT assume (a).

### 3.1 Candidate (a) — winding DC-circulation angular-momentum reactive pressure: **PRESENT**

The (2,3) winding carries a nonzero DC circulation. Its home is the inductive shear channel P_μ. The
circulation is a persistent loop current `I_w` with flux linkage `Φ_w = L_ind I_w`; the associated
angular momentum of the circulating field is `L_w = m_eff · (circulation)`. The winding integer
`Link(∂Ω,F) = −1` (electron) is a TOPOLOGICAL invariant — it is CONSERVED under any smooth
compression of the loop (`resonant-lc-solitons.md`:124; charge = static Link, deformation-invariant).
Conservation of a fixed circulation quantum in a shrinking loop is the substrate-native version of
angular-momentum conservation `L_w = const` as `r` shrinks.

The reactive (centrifugal) pressure of a conserved circulation confined to radius `r`:
```
   U_rot(r) = L_w² / (2 I(r)),   I(r) = m_eff r²   (moment of inertia of the circulating field)
   ⇒ U_rot(r) = L_w² / (2 m_eff r²)
   ⇒ B_a(r) = −dU_rot/dr = + L_w² / (m_eff r³)          (OUTWARD, ∝ r^{−3})
```
This is a genuine reactive (lossless) outward pressure — it is the stored inductive/kinetic energy of
the circulation, no real power, Axiom-3-clean. It is PRESENT because the winding demonstrably carries
a nonzero circulation (the whole charge sector). **Scaling: `B_a ∝ r^{−3}`.** This is the load-bearing
brace candidate: `r^{−3}` is steeper than any ponderomotive pull that scales as `r^{−1}` or shallower
(§3.4), so it CAN out-run the pull as `r→0` — the necessary property of a brace.

> **Verify-don't-assume note.** We did NOT assume (a). We derived that a conserved winding circulation
> (which the charge sector requires to exist) produces an `r^{−3}` reactive pressure by the standard
> `L²/2I` centrifugal-energy argument, and that this is lossless (reactive store, no dissipative port).
> The one genuinely open input is the MAGNITUDE of `L_w` (the circulation quantum), which sets the
> equilibrium scale (§4) — flagged, not assumed.

### 3.2 Candidate (b) — topological ropelength floor: **PRESENT as a HARD WALL (not a smooth brace)**

The (2,3) torus knot has a ropelength: the minimum length of unit-diameter tube needed to tie it. A
knotted/linked winding cannot be compressed below its ropelength floor without the tube self-
intersecting — i.e. without UNWINDING (changing the Link integer, forbidden while the charge is
conserved). Substrate-native: the Nyquist pitch `d = 1 ℓ_node` (Ax-1) sets the minimum tube diameter;
the (2,3) closed curve on the Golden torus has a minimum perimeter `∼ 2π R_min` with `R_min ≳ O(ℓ_node)`.
So there is a HARD FORBIDDEN WALL at `r → r_floor ~ (1/2π)·(ropelength·ℓ_node)`, below which the
configuration cannot go while carrying `Link=−1`.

**This is NOT a smooth `r`-power brace — it is a vertical wall** (`B_b → ∞` as `r→r_floor⁺`, `B_b=0`
above it). It cannot set a SMOOTH equilibrium (there is no finite crossing of a vertical wall with a
finite pull; the pull would just pin the envelope AT `r_floor`). Its role is a BACKSTOP: it prevents
literal collapse to `r=0` even if (a) fails to arrest the runaway first. A pull pinned at `r_floor` is
a HARD-wall equilibrium, not a self-braced reactive well — and it would generically be a stiff,
non-smooth, possibly-unstable-to-unwinding state. **Derived: (b) is present as a hard floor, load-
bearing as a collapse-backstop, but it is not the smooth reactive brace the picture wants.**

### 3.3 Candidate (c) — saturation stiffening `D=1/S→∞`: **DISQUALIFIED as an independent brace**

The confinement operator `L=adjoint_div(D∇)`, `D=1/S(A)` (`fork_b_saturation_tank`;
`mass-sector-characterization_synthesis.md`:32) has `D→∞` at the saturated core — a stiff-core
breather. It is tempting to read this stiffness as an outward brace. **But it is the SAME `S→0` that
supplies the INWARD pull (§2).** The varactor compliance `C_eff=C_0/S→∞` (soft, wants compression)
and the stiffness `D=1/S→∞` (stiff) are the SAME kernel `1/S` read in two sectors — they are the
capacitive vs the wave-impedance faces of one saturation, RESOLVED as a sector split, not two
independent forces (`resonant-lc-solitons.md`:41, INVARIANT-S2, Grant-ratified). A single nonlinearity
cannot supply BOTH a pull and an equal-and-opposite brace of the same sign structure — that would be
asserting the mechanism balances itself by construction (a tautology, the coincidence-magnet tell).

**Derived: (c) is NOT an independent brace.** It is the pull's own kernel; counting it as a brace
would double-count `1/S`. (This is exactly the trap the #83 artifact fell into differently — there the
"cage" was a dissipative `e^{−ηM}`; here the temptation is to reuse `1/S` as its own antagonist. Both
are disqualified: one by Tellegen/Axiom-3, this one by no-double-counting.)

### 3.4 The `r`-scaling contest (the crux, set up here, evaluated in §5)

The pull `P(r)` from §2: the ponderomotive DC compression from the rectified varactor. Its `r`-scaling
depends on how the strain `A(r)` and swing `δA(r)` scale with the envelope radius. For a fixed reactive
charge `Q` in a shell of radius `r`, `A ∼ Q/(r·something)` grows as `r` shrinks; the ponderomotive
energy `⟨U⟩ ∼ −½Q²|S''(Ā)|δA²/C_0` deepens. Away from the deep-saturation limit (`Ā` not yet near 1),
`P(r)` scales like a Coulomb/self-energy pull, `P ∼ r^{−1}` to `r^{−2}` (a standard soliton self-energy
gradient). **The brace (a) scales `r^{−3}`.** So:

```
   BRACE (a):  B_a(r) ∝ r^{−3}          (steeper — dominates as r→0)
   PULL:       P(r)  ∝ r^{−1..−2}        (shallower, IN THE SUB-SATURATION regime)
   ⇒ crossing at a finite r*  (B and P equal) — a well, IF the pull stays shallower than −3.
```
BUT §2.3's runaway: in the DEEP-saturation core (`Ā→1`), the pull's effective stiffness `∝ |S''(Ā)|
= (1−Ā²)^{−3/2}` DIVERGES. If `(1−Ā²)` itself scales as a power of `r` near the core, the pull can
acquire an effective `r`-exponent STEEPER than `−3`, overrunning the brace. Pre-ruling, **the verdict
hinged on whether `P(r)` stays shallower than `r^{−3}` all the way in, or whether the `S→0` runaway
makes it steeper before the brace arrests it** — evaluated in §5. **Post-ruling (T2), this crux is
moot for the electron:** the deep-saturation core (`Ā→1`, `V→V_snap`) is a real feature of the A1
varactor, but the electron's mass core operates at `A=√α≈0.085` (Regime I), never entering the
deep-saturation core — so the runaway never fires and the pull stays Coulomb-class (`p<3`). See §5.2.

## 4. EQUILIBRIUM — the SIZE

Solving inward-pull = outward-brace with the §3.4 model `P(r)=c_P r^{−p}`, `B_a(r)=c_B r^{−3}`
(`c_B = L_w²/m_eff`):
```
   c_P r*^{−p} = c_B r*^{−3}   ⇒   r* = (c_P/c_B)^{1/(p−3)}       (sympy-verified, §5)
```
`r*` is finite and positive whenever `p ≠ 3` and `c_P, c_B > 0`. The equilibrium SCALE is set by the
ratio of the pull prefactor `c_P` (the rectified self-energy strength, tied to the reactive charge and
`V_yield`) to the brace prefactor `c_B = L_w²/m_eff` (the circulation quantum). Both prefactors carry
the substrate's one length scale `L_NODE = ℏ/(m_e c)` (`constants.py`:282) and the winding's `R·r=¼`
Golden-torus geometry (`ch8-alpha-golden-torus.md`). So:

- **`r* ~ O(L_NODE)` = the Compton scale.** Order-consistent with the canonical electron size
  (`L_NODE ≈ 3.86×10⁻¹³ m`, the reduced Compton length) and with `R·r=¼` at `d=1 ℓ_node`. **(V5
  holds — an ORDER-consistent scale.)**
- **This is calibration-consistency, NOT a derivation of the size.** Per Fork-A (#419), the pressure
  balance fixes a SCALE, not the product `R·r=¼` (which is a Class-B INPUT), and `L_w`, `V_yield=√α
  V_snap` both carry imported values (`m_e`, α). We do NOT claim to derive `r*`; we claim it is
  order-consistent with the imported Compton scale, which is the most a Class-C consistency result
  can claim. `m_e` VALUE is calibrated; only the FORM (a finite crossing exists) is derived.

**Honest note on `p=3` marginality.** If the pull happens to scale EXACTLY as `r^{−3}` (same as the
brace), the crossing degenerates: `r*` is either undefined (prefactors unequal → no crossing, runaway
one way) or a scale-free continuum (prefactors equal → neutral). The (2,3) winding's own `r^{−3}`-like
self-energy makes `p=3` a live possibility, not a measure-zero curiosity — see §5.

---

## 5. STABILITY CRITERION (the MAKE-OR-BREAK) — symbolic + evaluation

### 5.1 The criterion, symbolically

Net inward force `F_net(r) = P(r) − B(r)` (pull minus brace). The equilibrium `r*` is STABLE iff a
small expansion (`r>r*`) produces a NET INWARD (restoring) force and a small compression (`r<r*`)
produces a NET OUTWARD force — i.e. `dF_net/dr|_{r*} > 0`. With `P=c_P r^{−p}`, `B=c_B r^{−3}`, at the
crossing (sympy-verified above):
```
   dF_net/dr |_{r*}  =  (X / r*) · (3 − p),   where X = P(r*) = B(r*) > 0.
   ⇒  sign(dF_net/dr|_{r*})  =  sign(3 − p).
```

**THE CRITERION (frozen §5 form, now filled):**
```
   ┌────────────────────────────────────────────────────────────────────┐
   │  STABLE   ⇔  p < 3   (pull SHALLOWER than the r^{−3} brace)         │
   │  UNSTABLE ⇔  p > 3   (pull STEEPER — out-runs the brace)            │
   │  MARGINAL ⇔  p = 3   (scale-free prefactor contest, no smooth well) │
   └────────────────────────────────────────────────────────────────────┘
```
Physically: the brace must out-STEEPEN the pull at the crossing for the well to restore. The `r^{−3}`
centrifugal brace beats any pull shallower than `r^{−3}`; it LOSES to any pull steeper than `r^{−3}`.

### 5.2 Evaluation — the two regimes; why the verdict was CONDITIONAL, and why the T2 ruling makes it BIND

**Regime I — SUB-saturation pull (`Ā` not near 1).** A localized soliton's ponderomotive self-energy
pull, away from the deep-saturation limit, scales like a Coulomb-class self-energy gradient,
`P ∝ r^{−1}` to `r^{−2}` (`p ∈ [1,2] < 3`). **In this regime, `p < 3` ⇒ STABLE well.** The brace
out-steepens the pull; `dF_net/dr>0`; the electron binds as a self-braced reactive soliton. This is
the "electron viable" branch.

**Regime II — DEEP-saturation core (`Ā→1`, the near-yield regime this prereg's SECTOR HEADER
declares LIVE).** Here the §2.3 runaway bites: the pull's effective stiffness carries `|S''(Ā)| =
(1−Ā²)^{−3/2}`. If, as the envelope compresses, `(1−Ā²) ∝ r^{q}` for some `q>0`, the ponderomotive
pull acquires an EXTRA steepening `r^{−3q/2}` on top of its base exponent. For a shell whose strain
saturates linearly in the compression (`q≈1`), the pull can reach `p_eff ≈ base + 3/2`, which crosses
`p=3` from below — i.e. **in the deep core the pull can become STEEPER than `r^{−3}` (`p>3`) ⇒ the
crossing there is UNSTABLE.** The `r^{−3}` centrifugal brace, which wins in Regime I, can LOSE to the
`S→0` varactor runaway in Regime II.

**The competition is between two `r^{−3}`-class terms** (the brace's exact `r^{−3}` and the deep-core
pull's runaway approach to and past `r^{−3}`), so it is a PREFACTOR + higher-order contest that the
leading-order symbolic scaling does NOT resolve **in the deep-saturation regime.** The `p=3` marginal
case (§4) is exactly the boundary this contest sits on. Pre-ruling, the winner depended on:
- the circulation quantum `L_w` (brace prefactor `c_B`) — magnitude still OPEN (§3.1),
- the strain-vs-radius law `(1−Ā²)∝r^q` near the core — depended on the grade-attribution of `V_yield`
  (`def-vyvsn1`) and the `S^{0.25}`-vs-`S^{0.5}` exponent.

**But this whole Regime-II contest is now MOOT for the electron (Grant 2026-06-30 T2 ruling).** The
ruling puts the A1 mass core at `A=V_yield/V_snap=√α≈0.085` — **Regime I, not Regime II.** The deep-
saturation runaway is a real feature of the A1 varactor, but it only bites as `Ā→1` (`V→V_snap`),
which the electron's mass core never reaches (it sits 11.7× below `V_snap`). At `A=√α` the pull is
squarely Coulomb-class (`p∈[1,2]<3`) and the `r^{−3}` brace out-steepens it. The two former grade/
exponent inputs are also settled: `def-vyvsn1=T2` (§7.2), and the `S^{0.25}`-vs-`S^{0.5}` exponent is
`S^{0.5}` canonical (Grant F1, §7.2) — and MOOT at the operating point anyway, since
`S(A=√α)=√(1−α)≈0.996`, so `S^{0.5}≈S^{0.25}≈1` there (the exponent only ever mattered under the now-
rejected deep-saturation A1 framing).

**With the operating point fixed at `A=√α`, the stability verdict is no longer CONDITIONAL — it BINDS
(Regime I). Therefore the stability verdict is BINDS (under the T2 ruling).**

### 5.3 VERDICT (frozen adjudication applied — no criterion dropped; T2 ruling folded)

> **UPDATE 2026-06-30 — the fork is CLOSED toward BIND (Grant T2 ruling).** The pre-ruling §5.3 (below,
> preserved) read FORK-FOR-GRANT / CONDITIONAL-BIND because the LIVE regime turned on the
> un-adjudicated `def-vyvsn1` grade-attribution of `V_yield`. **Grant RULED `V_yield=T2` (2026-06-30):**
> `V_yield` is the transverse Cosserat self-trap wall; the A1 mass channel saturates only at
> `V_snap=V_yield/√α`. **This relocates the electron's A1 mass core operating point to `A=V_yield/V_snap
> =√α≈0.085` — Regime I (sub-saturation), NOT Regime II.** The deep-saturation runaway (which made V3
> regime-dependent) simply does not occur on the mass channel: `S(√α)=√(1−α)≈0.996`, 11.7× below the
> `S→0` core. So V3 `dF_net/dr>0` **HOLDS** at the actual operating point, and the split resolves toward
> STABLE-EQUILIBRIUM-EXISTS. **Revised verdict: BINDS (under the Grant T2 ruling).**

Mapping to the frozen §5 prereg verdicts (post-ruling column in **bold**):
- (V1) inward sign COMPRESSIVE — **HOLDS** (§2).
- (V2) a reactive brace PRESENT with a finite crossing — **HOLDS** (§3.1, §4); the crossing exists
  and is reactive/lossless.
- (V3) `dF_net/dr>0` at `r*` — pre-ruling: HOLDS in Regime I (`p<3`), FAILS in Regime II (`p>3`).
  **Post-ruling: the electron's operating point is `A=√α` (Regime I), so V3 HOLDS** — the runaway
  never fires on the sub-saturated mass channel.
- (V4) no dissipative port required — **HOLDS** (§1.3, Tellegen).
- (V5) `r*` order-consistent with Compton scale — **HOLDS** (§4).

With the T2 ruling fixing the operating point in Regime I, V1–V5 ALL hold ⇒ **STABLE-EQUILIBRIUM-
EXISTS.** The frozen "FORK-FOR-GRANT if the brace-steepness is genuinely AMBIGUOUS at the symbolic
level (depends on an un-adjudicated grade-attribution of `V_yield`...)" clause is now discharged: the
grade-attribution was the fork, Grant adjudicated it T2, and the resolution lands in the BINDING
regime. No criterion was dropped and no adjudication axis was moved post-hoc to force ✅ — the fork's
own named condition (`V_yield` grade) was resolved by the third source of truth (Grant), exactly as the
frozen prereg specified.

> **VERDICT: BINDS (under the Grant 2026-06-30 T2 ruling).** A self-braced reactive electron network
> assembles (real inward pull, real lossless outward brace, no dissipative crutch) and BINDS STABLY.
> The T2 ruling puts the A1 mass core at `A=√α≈0.085` (sub-saturation, Regime I), where the pull is
> Coulomb-class (`p≈1–2 ≪ 3`), the `r^{−3}` centrifugal brace out-steepens it, and `dF_net/dr>0` →
> stable well. The `S→0` varactor runaway (the only thing that could have broken the bind) lives on the
> deep-saturation A1 channel at `V→V_snap`, which the mass core never reaches — so it never fires. This
> is the SYMBOLIC verdict at the `A=√α` operating point; the greenlit sim CONFIRMS (not decides) the
> deep-core `p`-slope and the α-robustness (§7). Still **Class-C** throughout: `A=√α`, `m_e`, and α (via
> `V_yield=√α V_snap`) are all imported/echo — a FORM-chord, not emergence.
>
> **Pre-ruling §5.3 text (preserved, git is the trail — this was the honest CONDITIONAL before the
> ruling): FORK-FOR-GRANT / CONDITIONAL-BIND** — the network bound stably in the sub-saturation regime
> (`p<3`) but the LIVE near-yield regime's `r^{−3}`-brace-vs-`S→0`-runaway prefactor contest was not
> resolved symbolically, turning on `L_w` and the `V_yield` grade fork. The ruling closed that fork.

---

## 6. REST-MASS / INERTIA LEDGER

### 6.1 The DC store = rest mass (canonical, reused, verified)

The rectified DC envelope (§2.2) IS the stored reactive energy of the LC tank. Canonically
(`resonant-lc-solitons.md`:17–23, verify-before-cite): peak inductive energy `E_mag=½L_e I_max²` with
the relativistic-inductor hardware limit `I_max=ξ_topo·c`; the Virial theorem for a lossless LC tank
gives `E_elec=E_mag=½m_e c²`; summing the two isolated ledgers recovers `E_total=m_e c²`. So the DC
envelope stored energy = rest mass. In our port language: `P_A1`'s capacitive store (the compressed
varactor) + `P_μ`'s inductive store (the DC circulation `L_w`) are the two virial halves; their sum is
`E_0=m_e c²`. **The two ports we identified as the pull-source and the brace-source are the SAME two
ports whose reactive stores sum to the rest mass** — the mechanism and the mass ledger are one object,
which is the internally-consistent version of the hypothesis (mass = the self-braced store).

### 6.2 The SAME reactance's opposition-to-change = inertia

Inertia is the reactive back-EMF of the same store (`clm-jwyy6l`, `vol2/claim-quality.md`:666,
verify-before-cite): `E_mass=½L_eff|A|²`, back-EMF `V=−L_eff dI/dt` = the resistance to acceleration
(`M_inertial ≡ L_drag`). This is the "mass IS inductive resistance" of the hypothesis, DERIVED as the
Lenz reaction of the DC-circulation inductor `L_e`: accelerating the soliton changes the circulation's
flux linkage, and `−L_e dI/dt` opposes the change. The DC STORE (rest energy) and the OPPOSITION-TO-
CHANGE (inertia) are the same inductance `L_e` read as energy vs as impedance — one reactance, two
faces. This is the internally-consistent closure the picture wanted: the store that braces the
envelope IS the reactance whose Lenz-opposition is the inertial mass.

### 6.3 DOWNSTREAM CHECK — FLAGGED OPEN (not resolved here)

The EXACT rest-mass = inertial-mass equality (`m_rest = m_inertial`) is NOT closed by §6.1–6.2. It
requires the boosted winding-field momentum to come out `p = E_0 v/c²` (the relativistic-consistency
of the moving reactive store — that the same `L_e` gives BOTH `E_0=½m_e c²`-per-arm AND the correct
relativistic `p`). The reactance is α-encoded through the SI definition (`theorem-3-1:32`:
`ω_C L_e = ℏ/e² = Z_0/(4πα)`, so `L_e=(ℓ_node/e)² m_e` carries `e,ℏ` CODATA). **This is an OPEN
named downstream check** — a relativistic-consistency / boosted-momentum derivation — NOT resolved in
this static existence/stability analysis. Flagged per the prereg §derivation-plan item 6. It is the
right next object AFTER the stability fork (§5) is settled, because a store that is unstable (§5
Regime II fail) would not have a well-defined boost at all.

---

## 7. SOLIDITY, OPEN ITEMS, AND WHAT A GREENLIT SIM WOULD SETTLE

### 7.1 Solidity of each part

| Part | Claim | Solidity |
|---|---|---|
| §1 network | 3-channel reactive port map; binding loop = P_A1↔P_μ, P_Γ termination, P_EM outside | **SOLID** (reuse of canonical `resonant-lc-solitons.md` structure) |
| §1.3 Tellegen | binding loop lossless (Σ Re(V I*)=0); #83 dissipative crutch disqualified | **SOLID** (Tellegen is a topological identity; all binding branches imaginary) |
| §2 inward sign | COMPRESSIVE; two independent reads agree; rectification from `S''<0` | **SOLID** (sympy-verified `S''=−(1−A²)^{−3/2}<0`; sign-lock `n_grav=S^{−1/2}` cited) |
| §2.3 runaway | inward leg is self-steepening positive feedback (`|S''|→∞`) | **SOLID** (same sympy) |
| §3.1 brace (a) | winding DC circulation `r^{−3}` reactive pressure PRESENT, lossless | **SOLID form, OPEN magnitude** (`L_w` quantum un-fixed) |
| §3.2 brace (b) | ropelength hard-wall backstop | **SOLID as a floor**, not a smooth brace |
| §3.3 brace (c) | saturation stiffening DISQUALIFIED (same `1/S` as the pull) | **SOLID** (no-double-counting) |
| §4 equilibrium | `r*~L_NODE` (Compton) order-consistent | **CONSISTENCY** (scale imported, not derived) |
| §5 stability | `sign(dF_net/dr)=sign(3−p)`; STABLE iff `p<3`; at `A=√α`, `p∈[1,2]<3` | **SOLID criterion + BINDING evaluation** (T2 ruling fixes `A=√α`, Regime I) |
| §5.3 verdict | BINDS (under Grant 2026-06-30 T2 ruling) | the honest state (fork closed by Grant) |
| §6 mass/inertia | DC store=rest mass, same `L_e`'s Lenz-opposition=inertia | **CONSISTENCY** (canonical reuse) |
| §6.3 downstream | `p=E_0 v/c²` relativistic-consistency | **OPEN, flagged** |

### 7.2 Open items (post-ruling — two RESOLVED, one input + one downstream check remain)

**RESOLVED this session (2026-06-30):**
- **(R1) The `V_yield` grade-attribution fork (def-vyvsn1) — RULED = T2 (Grant 2026-06-30).** `V_yield`
  is the transverse Cosserat (T2) self-trap wall; the A1 mass channel saturates only at
  `V_snap=V_yield/√α`. Consequence: the electron's A1 core operates at `A=√α≈0.085` (Regime I,
  sub-saturation), which is why the §5 verdict lifts to BINDS. Landed in `def-vyvsn1` (status SOLID),
  `pair-production-axiom-derivation.md`:93–104 (T2 horn), `nonlinear-vacuum-capacitance.md`:16 (A1 horn
  re-keyed to `V_snap`). Was the single load-bearing input for the §5 verdict.
- **(R2) The `S^{0.25}`-vs-`S^{0.5}` exponent — RESOLVED = `S^{0.5}` canonical (Grant F1, this
  session).** Not a defect: `S^{0.5}` is canonical; `S^{0.25}` is a reduced-form via a factor-of-2
  projection. And it is MOOT at the operating point: `S(A=√α)=√(1−α)≈0.996`, so `S^{0.5}≈S^{0.25}≈1`
  there — the exponent only ever mattered under the (now-rejected) deep-saturation A1 framing. `S^{0.5}`
  used throughout.

**STILL OPEN:**
1. **The circulation quantum `L_w` magnitude** (§3.1) — the ONE remaining open INPUT. Sets the brace
   prefactor `c_B = L_w²/m_eff` and thus the equilibrium scale `r*` (§4). It does NOT change the §5
   BIND verdict (the sign `sign(3−p)` is `L_w`-independent at `A=√α`); it sets the SIZE, not the
   stability. Flagged, not assumed.
2. **The `p=E_0 v/c²` boosted-momentum downstream check** (§6.3) — OPEN, DEFERRED (relativistic-
   consistency of the moving reactive store; the right next object now that §5 binds).
3. **NOT a route-space exhaustion.** This closes the analytic question for the CANONICAL 3-channel
   network with the winding-circulation brace at the `A=√α` operating point. A not-yet-named additional
   reactive brace could still shift the SIZE; not claimed exhausted.

The greenlit sim = **measure the deep-core `p`-slope at `A=√α` + run the α-robustness sweep** (confirm
the symbolic BIND, not decide it) — see §7.3.

### 7.3 What a greenlit sim WOULD settle (the fork is a MEASUREMENT, not a debugging gap)

The §5 verdict now BINDS symbolically (under the T2 ruling, `A=√α`); the greenlit sim **CONFIRMS**
(does not decide) it by measuring **the `r`-slope of the ponderomotive pull `P(r)` vs the `r^{−3}`
brace at the self-consistent `A=√α` operating point, plus an α-robustness sweep** (does the BIND
survive as `A=√α` is varied around the echo point). Per Rule-10 empirical-driver discipline this is a
clean, well-posed measurement:
- record BOTH reactance states (the C-state `V_inc/ω` AND the L-state `Φ_link/ω_dot`) over the
  recording window (reactance-pair-tracking) — a snapshot at one phase cannot distinguish the static
  brace from the oscillator caught at peak;
- sample at the energy-density PEAK (`top-K |field|²`) of the shell, NOT the centroid (the centroid of
  a shell is the empty middle);
- filter PML cells before any top-K extraction;
- fit `P(r)` and `B(r)` slopes with a LOCAL-clock modulation `ω_local(r)=ω_global·√(1−A²(r))` since
  Op14 saturation is active at the load-bearing core.
At `A=√α` the symbolic analysis predicts `p ∈ [1,2] < 3` → STABLE-EQUILIBRIUM-EXISTS (electron
viable); the sim CONFIRMS if the measured deep-core `p` at `A=√α` comes out `< 3` (expected), and the
α-robustness sweep confirms the BIND is not knife-edge at the `√α` echo point. A measured `p > 3` at
`A=√α` would be a surprise that REOPENS the symbolic reading (the sim would then be the discriminator,
not a confirmation). The symbolic analysis supplied the criterion `sign(3−p)` and — via the T2 ruling
— the operating point `A=√α` at which to evaluate it, which is the deliverable's job: determine
ANALYTICALLY the feedback path, the brace, the equilibrium, and the stability criterion BEFORE any sim.

### 7.4 Classification (consistency-vs-emergence — final)

**Class C — CONSISTENCY, throughout.** The mechanism (a reactive brace against a rectified pull) is at
best a FORM-chord: it gives the SM-absent mechanism for a stable localized electron mass, but the SIZE
is a scale tied to imported `L_NODE`/`R·r=¼` (Class-B input), and every dimensionful anchor (`m_e`, α
via `V_yield=√α V_snap` and `Z_0=2αh/e²`) is imported/echo. There is NO Class-D emergence here (no
dimensionless observable computed free of the target). The BIND verdict (under the T2 ruling) does not
change the class: the STABLE pass is a Class-C FORM-chord (mass VALUE definitional), consistent
with the mass-sector ceiling (`mass-sector-characterization_synthesis.md` §2). α touches the result
ONLY through the flagged echo channels; it is not headlined as emergence (A47 v17 family). **The T2
ruling REINFORCES the Class-C tag:** the operating point that makes the electron bind is `A=√α` — an
exact α-echo (`V_yield=√α V_snap`), an imported value dressed as an operating point, not a free
parameter the substrate selects. The BIND verdict is a FORM-chord (the mechanism), not a VALUE
emergence.

### 7.5 Guards walked (checklist)

- **substrate-native-check:** equilibrium posed as reactive PRESSURE balance at a self-set Q-point, NOT
  an energy-landscape minimum / gradient descent / Helmholtz eigensolve (CP1–5); the inward force is a
  BOUNDARY/ponderomotive read, not a singular bulk force term (CP10); ports are native Cosserat, not
  Cartesian.
- **phase-space-coordinate-check:** the (2,3) winding is treated in its PHASE-SPACE home (the circulation
  / Link integer on the Clifford torus), not as a real-space geometric torus (the wrong-locus error the
  #415 eigensolve made); `R·r=¼` handled as the phase-space product INPUT, not a real-space fit; the sim
  spec (§7.3) records the reactance PAIR in native (C-state, L-state) coordinates.
- **consistency-vs-emergence:** classified Class-C throughout (§7.4); α/`m_e` echo channels flagged.
- **ave-prereg:** frozen prereg `a6c03c72` BEFORE deriving; existing coupled-network + electron leaves
  greped first (§prior-state); criteria applied, none dropped.
- **ave-canonical-source:** constants from `src/ave/core/constants.py` (`L_NODE`, `V_SNAP`, `V_YIELD`,
  `ALPHA`, `Z_0`); no hardcoded targets.
- **verify-before-cite:** every file:line quoted was greped this session; the `S''` and `sign(3−p)` math
  sympy-verified in-commit.
- **flag-don't-fix:** the `V_yield` grade fork, the `S^{0.25}`/`S^{0.5}` exponent, and the `L_w`
  magnitude were surfaced as Grant-adjudication items — NOT silently resolved. Two of the three were
  then RESOLVED by the correct authority: `def-vyvsn1=T2` and `S^{0.5}` canonical are **Grant rulings
  (2026-06-30)**, not implementer fixes; `L_w` remains open (flagged, §7.2). The verdict lifted to BIND
  because Grant closed the fork, not because the implementer reframed it.
- **honest-closure (Rule 11):** no criterion dropped; the pre-ruling CONDITIONAL verdict was reported
  as-is and is PRESERVED in §5.3 (git is the trail); the lift to BIND came from Grant resolving the
  fork's OWN named condition (the `V_yield` grade), not from moving an adjudication axis post-hoc to
  convert ❌→✅; no dissipative brace introduced to force a balance (#83 lesson); no new hypothesis
  refills a slot (A47 v11b) — the T2 ruling substitutes the adjudicated meaning into the existing slot.

### 7.6 Provenance / reproducibility

- Symbolic checks (in-commit, reproducible): `S(A)=√(1−A²)` ⇒ `S''=−(1−A²)^{−3/2}<0` (§2);
  `dF_net/dr|_{r*} = (X/r*)(3−p)` for `P=c_P r^{−p}`, `B=c_B r^{−3}` (§5) — both via `sympy`.
- Canonical anchors (verify-before-cite, this session): `resonant-lc-solitons.md`:17–52,92,100–104,
  120–127; `boundary_invariants.py`:129–133; `constants.py`:154,282,455,464; `ch8-alpha-golden-torus.md`;
  `mass-sector-characterization_synthesis.md`:32; `theorem-3-1:32`; `clm-jwyy6l`.
- Prior negatives held as prior odds: `2026-06-24_engine-coupled-eigensolve_result.md` (#415/#417
  eigenmode DOES-NOT-EXIST); `2026-06-26_stabilized-electron-feedback-loop_result.md` (#83 RETRACTED
  artifact); `2026-06-24_forka-alpha-flip.md` (#419 pressure fixes a scale, not `R·r=¼`).
- NO simulation run (per scope). **The original derivation was research/-only; the 2026-06-30 T2-ruling
  FOLD additionally landed the Grant ruling into the KB** — `def-vyvsn1` (status proposed→SOLID,
  `vocabulary-register.md`), the two reconciled leaves (`pair-production-axiom-derivation.md`:93–104 T2
  horn, `nonlinear-vacuum-capacitance.md`:16 A1 horn re-keyed to `V_snap`), the `resonant-lc-solitons.md`
  :127 threshold note, and the `interlock-register.md`:219 FLAG-1 downgrade; `.index/claims.jsonl`
  regenerated via `make refresh-kb-metadata`. Branch-only; orchestrator opens the PR after an
  independent verify.
- **Ruling provenance (2026-06-30):** `def-vyvsn1=T2` (Grant), `S^{0.25}`/`S^{0.5}`→`S^{0.5}` canonical
  (Grant F1). Arithmetic re-verified this session: `√α=0.0854`, `1/√α=11.71`, `S(√α)=√(1−α)=0.9963`;
  `constants.py:455` (V_SNAP), `:464` (V_YIELD).
