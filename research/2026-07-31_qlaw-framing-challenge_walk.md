# Q-law — ADVERSARIAL FRAMING CHALLENGE + VACUUM-CIRCUIT MAPPING (pre-derivation walk material)

**Date:** 2026-07-31
**Lane:** implementer, framing-challenge mode (no derivation, no pre-reg, nothing minted)
**Status:** 🟡 WALK MATERIAL — this document exists to be walked with Grant, not to be believed
**Provenance:** Grant's conditional yes on the cold-Q derivation, 2026-07-31, verbatim `[sic]`:
*"Yes but challenge all framing, assumptions, and map to the vacuum circuits and physical lattice walk first"*.
Upstream: [`research/2026-07-30_qlaw-derivation_scoping.md`](2026-07-30_qlaw-derivation_scoping.md)
(routes R1–R6, findings F1–F9, walk questions Q1–Q8) — read that first; this document
**challenges** it rather than extending it.

## What this document is NOT

- **NOT a derivation.** No solver was run. No route was pursued. No `Q` was computed.
- **NOT a pre-registration.** No bin is frozen. The success bins stay in the upstream scoping doc, DRAFT.
- **NOT a claim.** No claim-id is minted. No existing claim's solidity is changed. No corpus file is modified.
- **NOT an adjudication.** Every fork below is *surfaced with both paths*; none is picked. Where this
  document's own analysis points to an answer (CF-5), the answer is routed to Grant for ratification and
  explicitly fenced as **not yet canon**.
- **NOT a retitle of the upstream scoping doc.** F1–F9 stand as written; this document adds CF-1…CF-15
  in a separate numbering space so the two sets never collide.

## Sections

- §0 — Sector / regime / phase-state / coordinate header
- **PART 1** — §1 Adversarial framing challenge (A1–A9, verdict table, CF-1…CF-15)
- **PART 2** — §2 The vacuum-circuit mapping (EE-first)
- **PART 3** — §3 The lattice walk (sit-inside-the-cell, one page)
- §4 — The fork menu for Grant (one plumber question per OPEN fork)
- Appendix A — Step-0 skill-selection plan + retro-pass
- Appendix B — verify-before-cite battery (two-method receipts)

---

## §0 — Sector / regime / phase-state / coordinate header (declared BEFORE any physics word)

- **MODE.** Post-merger remnant ringing down. The object under challenge is the **cold** ($a_*=0$)
  anchor: $\omega_R M_g = 18/49$, $Q = \ell = 2$, against the frozen corrected-Kerr reference
  $Q_{GR}(0) = 2.10021$ (upstream §2.0).
- **SECTOR.** The **observable** is a **transverse shear (T2)** oscillation. The **bias field** that
  builds the cavity is the **A1 radial dilatation** $\varepsilon_{11} = 7GM/(c^2r)$. These are
  orthogonal grades (A1 ⊥ T2) and must not be cross-wired: the A1 strain is the **DC operating point**,
  the T2 shear mode is the **small-signal AC** riding on it. Receipt for the identification of
  $\varepsilon_{11}$ as the Axiom-4 amplitude: [`common/vocabulary-register.md:309`](../manuscript/ave-kb/common/vocabulary-register.md)
  — *"$\varepsilon_{11} = 7GM/(c^2 r)$ … the A1-dilatation radial 'strain' that IS the Axiom-4 saturation amplitude $A$"*.
- **REGIME.** Far field = **Regime I** (linear, lossless, reactive; a legal radiating port).
  Near the wall = **Regime III→IV** soft-mode transition ($G_{shear}\to 0$).
  Inside $r_{sat}$ = **Regime IV** (ruptured topology; shear cannot propagate at all).
- **PHASE-STATE.** Op14 **ON** at and near the boundary; the DC strain is at yield ($A = 1$) exactly at
  $r_{sat} = 7GM/c^2$; $\Gamma_{EM} = 0$ (SYM saturation, $Z_{EM} = Z_0$ invariant),
  $\Gamma_{shear} = \Gamma_{bulk} = -1$ per [`vol3/claim-quality.md:122`](../manuscript/ave-kb/vol3/claim-quality.md).
- **COORDS (A46 / `phase-space-coordinate-check`).** The confrontation lives in the
  **dimensionless-eigenvalue register** ($\omega_R M_g$, $\omega_I M_g$, $Q$) that AVE and GR share —
  no phase-space/real-space mismatch. **But PART 2 introduces a second register, the impedance plane**
  ($Z$, $\Gamma$, Smith), and the two are only *exactly* interchangeable for an isolated single pole.
  That caveat is **CF-14** and it is a live A46-class item for the derivation pre-reg, not a formality.
- **CLASS CEILING (`consistency-vs-emergence`), inherited unchanged from upstream §2.1.** Every object
  here rides $\nu_{vac} = 2/7$, whose **VALUE is GR-IMPORTED** via $K = 2G$. Nothing in this document
  can be headlined as value-level emergence. Where this document produces a number, its class is stated
  inline; most are **IDENTITY** (algebraic re-expression of two canonical lines) or
  **arithmetic-consistency observation on banked corpus inputs** — the same class as upstream §1.3/§2.0.

---

## PART 1 — ADVERSARIAL FRAMING CHALLENGE

### §1.0 — Verdict table

**Legend.** **FORCED** = canon (axioms + ratified leaves) leaves no alternative. **CHOICE** = a
defensible pick that canon states but does not derive; a different pick is admissible. **OPEN-FORK** =
two or more live readings, both canonically supported or neither excluded; the substrate has not been
asked.

| # | Assumption under challenge | Verdict | Load-bearing findings |
|---|---|---|---|
| **A1** | The resonator is the wall rim at $r_{sat}$ (the "bell") | **OPEN-FORK** — four candidate resonators, canon has explored one; and the standing chain contains **two different radii** for the same mode | CF-1, CF-2, CF-3, CF-9, CF-10 |
| **A2** | Sector ownership: observable is shear (T2); no A1 admixture | **FORCED** at linear order (A1 = DC bias, T2 = AC signal; any A1 product lands at $2\omega$ or DC, not $\omega$). **Sub-fork OPEN**: does the anisotropic vessel state split the rim modes? | CF-12 |
| **A3** | Mode geometry: whispering-gallery $\ell = 2$, linear-$\ell$ dispersion | **OPEN-FORK** on $\ell$ vs $\sqrt{\ell(\ell+1)}$ (upstream F4, binned UNDETERMINED). **Separate GAP, not a fork**: the radial-overtone index $n$ has **no AVE object at all** | CF-8, and §2.6 probe E15 |
| **A4** | The loss channel is radiation outward into the graded exterior | **FORCED by canon** that the wall is lossless and contributes **nothing** to $Q$ — which makes the corpus's own label ("$Q$ from the $\Gamma=-1$ TIR boundary") a mis-attribution. **OPEN** off the exact $A=1$ point: $\lvert\Gamma\rvert < 1$ there, and the transmitted shear has nowhere to go as shear | CF-11, CF-15 |
| **A5** | The local shear speed exponent ($\sqrt{S}$ vs $S^{1/4}$) is the biggest open input | **RECLASSIFIED → CHANNEL fork, and CLOSED for the shear integrand at $\sqrt{S}$** by three-way over-determination in the $(L,C)$ constitutive pair. **Routed to Grant for ratification; NOT canon until he rules.** | **CF-5, CF-6** ★ |
| **A6** | The $(1+\nu)$ loading factor | **CHOICE** — the FORM (a Poisson factor on a shell mode) is plausible and unexceptional; the SPECIFIC $r_{sat}/(1+\nu)$ is **asserted, not derived**, and its VALUE is GR-imported (upstream F3). It also implies a tangential phase speed of $1.286\,c_0$ | CF-1, CF-4 |
| **A7** | Which $Q$ the derivation targets ($\omega_R/2\omega_I$) | **FORCED** — the $\tau$ observable is the physical ratio; the integer mode-count reading coincides only at $a_*=0$ (upstream §1.6 fourth reading). **New caveat:** port-$Q$ and pole-$Q$ diverge once the exterior carries a branch cut | CF-14 |
| **A8** | Boundary condition at the wall: $\Gamma = -1$ | **FORCED** at $\lvert\Gamma\rvert = 1$ (#260 B3-DEGENERATE). The **sign is Q-neutral in the loss ledger** (a lossless termination either way) but **Q-relevant through the frequency**: short vs open moves the rim between a node and an antinode, a quarter-wave shift in effective length | CF-13 |
| **A9** | Where the radiated energy goes; re-reflection from the taper | **OPEN-FORK** — the strain grade is $\approx 0.41$ wavelengths thick, i.e. **borderline** between adiabatic and lumped, exactly the regime where partial re-reflection is expected and $Q$ is $O(1)$. Re-reflection **does** feed back into $Q$ by definition (it is the taper's input impedance). The echo cavity is **wall ↔ taper**, not wall ↔ light-ring | CF-9, and §2.3 |

---

### §1.1 — A1: what IS the resonator? (the "bell")

**The assumption.** The ringdown is an $\ell = 2$ shear oscillation riding the rim of the saturation
wall at $r_{sat} = 7GM/c^2$, with $\omega_R M_g = \ell(1+\nu_{vac})/x_{sat}$.

**Is the keying forced or inherited?** Inherited. The five-step chain at
[`vol2/appendices/app-f-solver-toolchain/regime-eigenvalue-method.md:14-18`](../manuscript/ave-kb/vol2/appendices/app-f-solver-toolchain/regime-eigenvalue-method.md)
is a *procedure*, and it keys to $r_{sat}$ because step 2 locates $r_{sat}$ and steps 3–4 build off it.
Nothing in Ax 1–4 says the resonant mode of a *graded* medium sits at the point where the grade
terminates. In a graded resonator the mode sits where the substrate puts it — that is an eigenvalue
output, not an input.

#### ★ CF-1 — the canonical five-step chain uses TWO different radii for the same mode

Verbatim, same file, adjacent steps:

> `:52` — $r_{\mathrm{eff}} = \dfrac{r_{\mathrm{sat}}}{1 + \nu_{\mathrm{vac}}} = \dfrac{7}{1 + \tfrac{2}{7}} = \dfrac{49}{9}\,M_g \approx 5.444\,M_g$
>
> `:55` — **Step 4: Eigenfrequency.** The $\ell = 2$ tangential standing wave **at $r_{\mathrm{eff}}$**
>
> `:63` — The mode **orbits tangentially at $r_{\mathrm{sat}}$** with $\ell$ wavelengths fitting around
> the circumference. Each wavelength subtends angle $2\pi/\ell$, and the curvature radiation loss per
> cycle scales as $1/\ell$

*[emphasis added on "at $r_{\mathrm{eff}}$" and "at $r_{\mathrm{sat}}$"; both phrases are unbolded in the source.]*

$\omega_R$ is taken from $r_{eff} = 5.444\,M_g$; $Q = \ell$ is taken from a mode-counting picture on the
circumference at $r_{sat} = 7\,M_g$. **The two numbers this lane is trying to reconcile are read off two
different circles.** If $\ell$ wavelengths genuinely fit around $2\pi r_{sat}$, then
$\omega_R M_g = \ell/x_{sat} = 2/7 = 0.2857$, not $18/49 = 0.3673$ — a 22% shift, and the
$(1+\nu_{vac})$ factor disappears.

**Steelman.** $r_{eff}$ is not a location — it is an *effective electrical length* (a velocity-factor /
end-effect correction), and the ring is physically at $r_{sat}$. That reading is coherent and is what
PART 2 adopts to build the circuit. But then: (i) the corpus's own word for it, "**effective cavity
radius**" (`:16`, `:52`), is a category label that hides a circuit length; and (ii) the leak fraction
$1/\ell$ is a statement about the circumference the mode *wraps*, so if the mode wraps $r_{sat}$ while
its frequency is set by $r_{eff}$, the per-cycle leak picks up a factor $(1+\nu_{vac})^{\pm1}$ =
$9/7 = 1.286$ or $7/9 = 0.778$ — i.e. **the upstream F7 leak-constant $c_1$ has a candidate home here,
of exactly the right size class** (upstream H1 wants $c_1 \approx 1.05$; neither $9/7$ nor $7/9$ is
$1.05$, so this is a *candidate*, not an answer).

**Class:** arithmetic-consistency observation on two verbatim canonical lines. NOT a claim.
**Verdict:** the resonator's radius is a **CHOICE the chain makes twice, inconsistently**.

#### ★ CF-2 — $r_{eff}$ sits 22% INSIDE the shear-reflecting wall

$r_{eff} = 49M_g/9 = 5.444\,M_g$ against $r_{sat} = 7\,M_g$. The Poisson correction points **inward**,
into the region canon calls Regime IV, where
[`vol3/cosmology/ch15-black-hole-orbitals/electron-bh-isomorphism.md`](../manuscript/ave-kb/vol3/cosmology/ch15-black-hole-orbitals/electron-bh-isomorphism.md)
states verbatim: *"Gravitational waves, being **transverse shear waves**, **cannot propagate** in the
ruptured interior"*. Under the literal "cavity radius" reading, the eigen-radius is inside the region
where the mode cannot exist.

**Steelman:** identical to CF-1's — $r_{eff}$ is a length, not a place. **But the two findings are one
fork with two horns:** either $r_{eff}$ is a radius (and it is inadmissible), or it is an electrical
length (and the chain's own prose mislabels it, and CF-4 bites).

#### ★★★ CF-3 — the rim frequency is computed with the COLD far-field speed at the radius where canon puts the local shear speed at exactly ZERO

Step 4 writes $\omega_R = \ell\cdot c/r_{eff}$ with $c = c_0$, the unsaturated speed. Canon at the same
boundary says the shear speed vanishes:

- [`vol3/gravity/ch02-general-relativity/saturating-modulus-and-backreaction.md:60`](../manuscript/ave-kb/vol3/gravity/ch02-general-relativity/saturating-modulus-and-backreaction.md)
  — *"**SHEAR softens:** $c_{\text{shear}}=c_0\sqrt{S}=c_0(1-A^2)^{1/4}\to0$ — a **derived** $\sqrt{S}$ projection, NOT a second kernel."*
- [`common/operators.md`](../manuscript/ave-kb/common/operators.md) Op16 — $c_{shear} = c_0\cdot\sqrt{S}$, CANONICAL.
- [`vol4/circuit-theory/ch1-vacuum-circuit-analysis/op14-local-clock-modulation.md:13`](../manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/op14-local-clock-modulation.md)
  — the local matter clock rides that same shear speed, $\omega_{local} = \omega_{global}(1-A^2)^{1/4}$,
  $\to 0$ at $A^2\to1$.

Evaluated with canonical **local** quantities at the wall, the rim mode's frequency is **zero**, not
$18/49$. **The standing eigenvalue is a cold-cavity, hard-wall, far-field-speed calculation wearing
saturated-wall language.** Every piece of Op14/Ax-4 saturation content the corpus owns —
$c_{shear}\to0$, $\omega_{local}\to0$, the $Z$-grade, $\rho_{eff}\to\infty$ — is **absent from the
number $18/49$ and absent from $Q = \ell$.**

**Steelman (and it is a good one).** The mode is not *at* the wall; it lives in the graded exterior
where $c_{shear}$ is finite, and $18/49$ is a stand-in for a proper graded eigenvalue problem whose
answer happens to be nearby. That steelman is correct — **and it is the whole argument for firing R2/R7
rather than patching the spin machinery.** It also predicts the sign of the fix: a mode that lives in a
region of *reduced* $c_{shear}$ rings *lower* than the cold estimate, while GR wants $\omega_R$
**lower** ($0.3737$ vs the standing $0.3673$ is AVE *under*; but the standing catalog $\omega_R$ is
**+2.63% over** — upstream §1.3). The two ends disagree in sign, which is itself informative and is
exactly the kind of thing a graded eigenvalue solve would settle.

**Class:** consistency observation across four canonical statements. NOT a claim, NOT a derivation.

#### ★ CF-4 — the two-radius reading implies a tangential phase speed of $1.286\,c_0$

Take Step 5's geometry literally (ring at $r_{sat}$, $\ell$ wavelengths around the circumference) and
Step 4's frequency: $\lambda = 2\pi r_{sat}/\ell$, so
$v_\varphi = \omega_R\lambda/2\pi = \ell c_0(1+\nu_{vac})/r_{sat}\cdot r_{sat}/\ell = c_0(1+\nu_{vac}) = 1.286\,c_0$.
A tangential wave running around the rim at $1.286\,c_0$ — in a region where canon says the local shear
speed is $\le c_0$ and heading to $0$.

**Steelman.** Shell theory *does* put Poisson factors on membrane eigenfrequencies, and a
"frequency-raising" factor is not by itself superluminal *if the mode is not a simple travelling
tangential wave* (a flexural shell mode has a different dispersion). But then the $\ell$-wavelengths-
around-the-circumference picture — which is the *entire source of $Q = \ell$* — no longer applies, and
$Q$ has to come from somewhere else. **The two halves of the standing derivation are load-bearing on
mutually exclusive mode pictures.**

#### ★ CF-9 — the light-ring cavity is geometrically INVERTED for the shear channel

Upstream R3 (§2.4) proposes a cavity *"bounded **inside** by the $\Gamma_{shear} = -1$ mirror at
$r_{sat}$ and **outside** by the light-ring potential barrier."* Canon says the light ring is **inside**
the mirror. Verbatim,
[`regime-eigenvalue-method.md:47`](../manuscript/ave-kb/vol2/appendices/app-f-solver-toolchain/regime-eigenvalue-method.md):

> *"The photon sphere at $r_{ph} = 3M_g$ lies **inside** the saturated region."*

*[the source emphasises "inside" in italics.]* And the Kerr prograde branch
$r_{ph}^+ = 2M_g(1+\cos[\tfrac23\arccos(-a_*)])$ runs from $3\,M_g$ at $a_*=0$ down to $1\,M_g$ at
$a_*=1$ — **always** inside $r_{sat} = 7\,M_g$. There is no annulus between the shear mirror and a
light-ring barrier; the barrier is behind the mirror, unreachable by shear waves.

**What the substrate has instead.** The graded profile has *its own* turning point, outside the wall.
Illustrative locator on canonical inputs only — $A(r) = 7M_g/r$, $c_{shear} = c_0\sqrt{S}$,
$V_{eff}\propto \ell(\ell+1)\,c_{shear}^2(r)/r^2$ — the stationary point is at $A^2 = 2/3$, i.e.
$r^\star \approx 8.573\,M_g$; under the un-propagated Family-E exponent ($c\propto S^{1/4}$) it moves to
$A^2 = 4/5$, $r^\star \approx 7.826\,M_g$. Both are **outside** $r_{sat}$, where $c_{shear}$ is finite
($c_{shear}(r^\star)/c_0 = 0.760$ at the canonical exponent), and **neither is near $r_{ph}$.**

> ⚠ **Fence on the two numbers above.** They are a one-line stationary-point evaluation of a textbook
> effective potential on canonical inputs, offered **to locate the fork, not to answer it**. They are
> **not a derivation, not a claim, not pre-registered**, they neglect the medium-gradient terms, and
> they move by ~10% under the A5 exponent — which is precisely the point being made.

**Consequence for R3:** R3 should be **re-scoped** from "light-ring barrier-transmission cavity" to
"the substrate's own graded-shear turning point," which is R2's object. R3 and R2 are then one route,
not two — and the echo by-product survives the re-scope (the echo cavity is wall ↔ taper).

#### ★ CF-10 — a true interface mode does not ring down; the corpus's own word "curvature radiation" is the right one

The fourth candidate resonator in the brief is an interface mode *on* the wall. Name it correctly: the
interior is a $G_{shear} = 0$ **fluid**, so a solid/fluid interface wave is **Scholte**-class, not
Stoneley (which is solid/solid). On a *flat* interface a Scholte wave is genuinely trapped — real
wavenumber, no leakage, $Q \to \infty$. **A finite ringdown $Q$ therefore rules out a pure interface
mode.** What survives is a *curved*-interface surface wave, which leaks by curvature — and
"curvature radiation loss per cycle" is exactly the corpus's own phrase at `regime-eigenvalue-method.md:63`.

So this challenge **strengthens** the corpus's mechanism word while renaming the mode: the object is a
**curvature-leaking whispering-gallery mode**, i.e. an $\ell$-th spherical multipole of the exterior
graded medium. That is candidate resonator (b)+(c) fused, and it is the one PART 2 maps.

**A1 verdict: OPEN-FORK.** Four candidates — (a) rim ring at $r_{sat}$; (b) distributed mode of the
graded shell; (c) interface/Scholte mode on the wall; (d) curvature-leaking whispering-gallery mode
(= b ∩ c). Canon has explored (a) only, and explored it with two radii (CF-1) and a cold speed (CF-3).
Candidate (c) is **excluded by its own physics** (CF-10, $Q\to\infty$). The live fork is (a) vs (d).

---

### §1.2 — A2: sector ownership

**FORCED half.** The DC strain that builds the wall is **A1** ($\varepsilon_{11}$, the dilatation); the
ringing observable is **T2** (transverse shear). This is the canonical sector split and it is clean:
in circuit terms the A1 strain is the **varactor's DC bias** and the T2 shear mode is the
**small-signal AC** riding it. The important structural consequence, which the corpus does not state
but which follows from the split: **any A1 admixture in the ringdown observable is a mixing product —
it lands at $2\omega$ or at DC, not at $\omega$.** That is a testable structural prediction and it is a
good independent reason to believe Op21's **single-channel** classification of BH ringdown
([`op21-multi-mode-mode-counting.md`](../manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/op21-multi-mode-mode-counting.md) §1 table row)
is right at linear order — a stronger reason than the corpus currently gives.

**Mode conversion at the anisotropic vessel state — OPEN.**

#### CF-12 — the vessel-state anisotropy is not carried anywhere in the ringdown chain

[`research/2026-07-21_boundary-strain-amplitude_result.md:96`](2026-07-21_boundary-strain-amplitude_result.md)
(R6, Grant's ratified vessel-state walk) states verbatim that at a yield-scale boundary the shell is a
*"**pressure vessel (hoop tension + radial compression)**"* and $k_{shear,eff}$ is *"**anisotropic**:
hoop bonds STIFFEN, radial bonds SOFTEN toward buckling"*, with the pre-stress dominating the bare
$k_s$ by $\sim10\times$.

An anisotropic rim does not have one $\ell = 2$ mode; it has a **hoop-polarised branch and a
radial/flexural branch** at different frequencies, generically coupled — i.e. mode conversion *is* a
channel, and $Q^{-1}$ becomes a sum.

**Honest fence:** that result is about a **localized breather core**, not the BH wall. Transplanting it
is an untested move. **Flagged, not asserted.** But it is the single most plausible route to a
"both (i) and (ii)" answer to upstream Q1 — which would be a substantive correction to a ratified leaf
(Op21's single-channel classification), not a detail.

---

### §1.3 — A3: mode geometry

- **$\ell$ vs $\sqrt{\ell(\ell+1)}$** — OPEN-FORK, already binned UNDETERMINED upstream (F4). No new
  evidence here; but see CF-8, which gives the fork a sharper handle: whichever dispersion is right, the
  quantity that controls the radiation is the **electrical size** $k r$, and CF-8 shows the standing
  chain sets $kr = \ell$ *exactly*. Under $\sqrt{\ell(\ell+1)}$ it would set $kr = \sqrt{\ell(\ell+1)} = 2.449$,
  which is a *different point on the same universal curve*. So the fork does not change the **kind** of
  object $Q$ is; it changes where on the curve you evaluate it. That is a much cheaper fork than it looked.
- **Whispering-gallery vs radial overtones — a GAP, not a fork.** GR's QNM spectrum is a ladder in the
  overtone index $n$; **AVE has no object for $n$ at all.** The five-step chain produces exactly one
  resonance. A tapered line has radial resonances as a matter of course, so the absence is a modelling
  gap, not a physical prediction of "no overtones". Recorded as failure-mode probe **E15** in §2.6.

---

### §1.4 — A4: the loss channel

#### CF-11 — canon already says the wall contributes NOTHING to $Q$; the corpus's own label says otherwise

`regime-eigenvalue-method.md:63` attributes the loss to *"curvature radiation"* from the orbiting mode —
i.e. to the **outward** side. The wall is a **perfect** reflector. Therefore, in the corpus's own
physics, **$Q$ is set entirely by the outer radiation impedance and the $\Gamma_{shear} = -1$ mirror
contributes exactly zero to the loss ledger.** But the canonical leaf that carries the derivation is
titled *"Op21 Multi-Mode Mode-Counting **at the $\Gamma = -1$ Saturation/TIR Boundary**"* and
`qnm-quality-factor.md` files $Q = \ell$ as *"an axiom-manifestation of Ax 3 + Ax 4 **at the
$\Gamma = -1$ saturation/TIR boundary**"*.

This is upstream Q2 restated with its circuit consequence: **the Q-law is a radiation-resistance
problem, full stop.** The wall's only role is to set the boundary *phase* (A8/CF-13). Naming it as the
source of $Q$ is a mis-attribution of where the physics lives — and it is why the corpus has never
computed a radiated power (upstream F7).

#### CF-15 — off the exact $A = 1$ point, $\lvert\Gamma\rvert < 1$, and the transmitted shear has nowhere to go AS SHEAR

$\Gamma_{shear} = -1$ is exact only in the limit $S \to 0$. At any finite offset from the wall, $S > 0$,
$Z_{shear} > 0$, and there is a nonzero transmission coefficient (Op17: $T^2 = 1 - \Gamma^2$). Nothing
in the corpus computes it. And once inside, $G_{shear} = 0$: **a shear wave cannot propagate in the
interior at all.** So the transmitted energy must do one of three things:

1. **Mode-convert** to a bulk/A1 wave at the interface (the interior *does* support bulk waves) — a
   real, standard elastodynamic P–SV conversion at a solid/fluid interface, and a **second loss channel**
   that would break Op21's single-channel classification.
2. **Reflect back** from a deeper structure (the compact shell) — then it is not a loss at all, it is a
   delay, and it feeds the echo.
3. **Be absorbed** — which requires a bulk $\mathrm{Re}\{Z\}$ in the interior. That is an **Axiom-3
   violation** unless it is licensed as a port (cf. the RADIATIVE-PORT carve at
   [`vol4/simulation/ch14-leaky-cavity-particle-decay/theory.md`](../manuscript/ave-kb/vol4/simulation/ch14-leaky-cavity-particle-decay/theory.md)).

**Nobody has checked which.** This is a first-class fork and it is *not* in the upstream route list.
It is also the honest form of the brief's "is $\Gamma=-1$ exactly lossless?" question: **at the wall,
yes; near the wall, no, and the corpus has never asked how near.**

---

### §1.5 — A5: the $S$-exponent in the shear speed (the brief called this the biggest unresolved input)

**It is not an exponent fork. It is a CHANNEL fork, and the shear channel is over-determined-consistent.**
This is the single largest deliverable of the framing challenge, and it comes straight out of firing
`ave-ee-first-mapping` rather than staying in elastic language.

#### ★★★ CF-5 — go to $(L, C)$ and the register collapses into three channels with no exponent freedom left

A transmission line has exactly **two** independent constitutive functions per unit length, $L$ and $C$.
Everything else is an **output**: $Z = \sqrt{L/C}$, $c = 1/\sqrt{LC}$. Canon states $Z(S)$, $c(S)$, **and**
a $Z\!\leftrightarrow\!c$ relation — three statements for two degrees of freedom. That over-determination
*is* the standing $\sqrt S$-vs-$S^{1/4}$ flag. Resolve it by declaring $L$ and $C$ from the lattice
primitive and letting $Z$ and $c$ both fall out. Doing that, **every canonical impedance/speed statement
in the corpus lands in exactly one of three branches, and each branch is internally exact:**

| branch | $L$ per length | $C$ per length | $\Rightarrow Z$ | $\Rightarrow c$ | canonical receipts |
|---|---|---|---|---|---|
| **SYM** — "gravity, BH interior, particle confinement" | $L_0 S$ ($\mu$ scales) | $C_0 S$ ($\varepsilon$ scales) | $Z_0$ **invariant** | $c_0/S$ | [`manuscript/ave-kb/claim-quality.md:111`](../manuscript/ave-kb/claim-quality.md) verbatim: *"both $\mu$ and $\varepsilon$ scale by $S$. Result: $Z_{sym} = Z_0$ (impedance invariant); $c_{EM,sym} = c_0/S \to \infty$"* |
| **ASYM** — strong EM field only | $L_0$ ($\mu$ frozen) | $C_0 S$ ($\varepsilon_{eff}=\varepsilon_0 S$ rolls off) | $Z_0/\sqrt S \to \infty$ (**open**) | $c_0/\sqrt S$ | `manuscript/ave-kb/claim-quality.md:112` verbatim: *"only $\varepsilon$ scales by $S$. Result: $Z_{asym} = Z_0/\sqrt{S} \to \infty$ (medium opaque); $c_{EM,asym} = c_0/\sqrt{S} \to \infty$"*; this is **Op14's** $Z_{eff}=Z_0/\sqrt S$ ([`common/operators.md:54`](../manuscript/ave-kb/common/operators.md)) |
| **SHEAR (T2)** — the ringdown's own channel | $L_0 \leftrightarrow \rho$ (inertia unsaturated) | $C_0/S \leftrightarrow 1/G_{shear}$ (compliance diverges as $G_{shear}=G_0S \to 0$) | $Z_{sh,0}\sqrt S \to 0$ (**short**, $\Gamma=-1$) | $c_0\sqrt S \to 0$ | [`vol3/claim-quality.md:122`](../manuscript/ave-kb/vol3/claim-quality.md) ($Z_{shear}=\rho c_{shear}\to0 \Rightarrow \Gamma_{shear}=-1$); `operators.md` Op16 ($c_{shear}=c_0\sqrt S$); `saturating-modulus-and-backreaction.md:60`; the #260 B3 banner's $Z=Z_0\sqrt S$, $\lvert\Gamma\rvert=1$ |

Three canonical statements about the shear channel — $Z_{shear}=\rho\,c_{shear}\to0$,
$c_{shear}=c_0\sqrt S$, and the Ax-4 compliance divergence $C_{eff}=C_0/S$
([`nonlinear-vacuum-capacitance.md:27`](../manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/nonlinear-vacuum-capacitance.md))
— are **simultaneously satisfied by one constitutive pair with zero freedom left over.**
**$S^{1/4}$ appears in none of the three branches.**

> **⚑ Honest residual on the SHEAR row (do not paper over).** `nonlinear-vacuum-capacitance.md:14`
> explicitly labels the diverging $C_0/S$ the *"**longitudinal-A1 bond compliance** ($1/k_a$, the
> stretch-reactance), **NOT** the transverse dielectric capacitance"*. The SHEAR row above therefore
> uses the **shear** bond compliance $1/G_{shear}$ with $G_{shear} = G_0 S$, which is licensed by
> `saturating-modulus-and-backreaction.md:60` projecting **the same $A$** into shear ("a **derived**
> $\sqrt{S}$ projection, NOT a second kernel"), not by the A1 varactor line. Whether the shear
> compliance's kernel *argument* is the A1 amplitude (canon's projection) or its own transverse swing
> (the per-deformation-coordinate reading of Ax 4,
> [`research/2026-07-21_boundary-strain-amplitude_result.md:13`](2026-07-21_boundary-strain-amplitude_result.md))
> is a live residual — the same residual as upstream Q3's $A$-vs-$A^2$ item.

#### ★★ CF-6 — the $S^{1/4}$ Family-E exponent is an artifact of one relation, and that relation is not a fixed-inductance relation in ANY branch

The flagged item at
[`vol3/gravity/ch02-general-relativity/k4-tlm-lensing-validation.md:30-33`](../manuscript/ave-kb/vol3/gravity/ch02-general-relativity/k4-tlm-lensing-validation.md) reads verbatim:

> ⚑ **Downstream flag (auditor):** with $Z_0/\sqrt{S}$, the $c_{\text{local}} = c_0\sqrt{Z_0/Z_{\text{local}}}$
> relation below yields $c_0 S^{1/4}$, which still differs from the canonical shear/lensing slow-down
> $c_{\text{shear}} = c_0\sqrt{S}$. That $c_{\text{local}}$ derivation relation is a SEPARATE
> un-propagated item, NOT silently rewritten here

**In both fixed-$L$ branches the correct relation is $c/c_0 = Z/Z_0$ exactly** — check it:
SHEAR gives $Z/Z_0=\sqrt S$ and $c/c_0=\sqrt S$ ✓; ASYM gives $Z/Z_0=1/\sqrt S$ and $c/c_0=1/\sqrt S$ ✓.
(In SYM the relation does **not** hold, because SYM moves $L$ too — $Z/Z_0=1$ while $c/c_0=1/S$; that is
the correct and expected behaviour, and it is a useful signature of which branch you are in.)

The relation $c = c_0\sqrt{Z_0/Z}$ demands a **different** constitutive pair. Solving
$Z/Z_0=\sqrt{\lambda/\gamma}=S^{-1/2}$ and $c/c_0=(\lambda\gamma)^{-1/2}=S^{1/4}$ for
$L = L_0\lambda$, $C = C_0\gamma$ gives

$$\lambda = S^{-3/4}, \qquad \gamma = S^{1/4}$$

i.e. an **inductance that rises** as $S^{-3/4}$ and a **capacitance that falls** as $S^{1/4}$ — quarter-
and three-quarter powers that appear nowhere in canon, and a capacitance moving in the **opposite
direction from the canonical Ax-4 varactor** ($C_{eff}=C_0/S$, rising). **The $S^{1/4}$ exponent has no
constitutive home.**

**Flag-don't-fix, and stated as such.** Both readings are on the record with paths and verbatim text;
neither is reframed and **no corpus file is modified**. Routed to Grant/auditor.

**A5 verdict.** For the **shear** integrand this document's analysis says the exponent is **pinned at
$\sqrt S$** by three-way over-determination, and $S^{1/4}$ is an EM/ASYM-branch artifact carried in on
an inconsistent relation. **That is a proposal for ratification, NOT a ruling and NOT canon.** Until
Grant rules, the derivation lane should carry $\sqrt S$ as primary **and record the $S^{1/4}$
counterfactual** (it moves the graded turning point $8.573 \to 7.826\,M_g$, CF-9) — the KEEP-BOTH
pattern, not a silent pick.

#### ★ CF-7 — which $\rho$ carries the shear wave at the wall? The two candidates flip the termination

Canon writes $Z_{shear} = \rho\,c_{shear}$ and lets $Z\to0$ *because* $c_{shear}\to0$ — holding $\rho$
fixed. But canon **also** says the effective inertial density diverges at the same place. Verbatim,
[`vol3/cosmology/ch15-black-hole-orbitals/interior-singularity-resolution.md`](../manuscript/ave-kb/vol3/cosmology/ch15-black-hole-orbitals/interior-singularity-resolution.md) `:14-21`:

> *"The effective inertial density of collapsing matter diverges as the topological yield approaches zero:
> $\rho_{eff} = \rho_0/S_{topo}^3$ where $S_{topo}(r) = \sqrt{1 - \varepsilon_{11}^2}$"*

If **that** $\rho$ is the one in the wave impedance, then
$Z_{shear} = \rho_0 S^{-3}\cdot c_0\sqrt S = Z_{sh,0}\,S^{-5/2} \to \infty$ — an **OPEN**, $\Gamma=+1$,
not a short. The taper's direction reverses.

**Steelman (and it is probably right).** The leaf's own words are *"effective inertial density of
**collapsing matter**"* — the frozen infalling matter, not the lattice's own inertia for shear-wave
propagation. Legitimately two different objects. **But the corpus never says which $\rho$ enters
$Z_{shear} = \rho c_{shear}$**, and the near-wall $Z$-profile — which *is* the $Q$ integrand — is
undetermined until it does. **Plumber form: is the frozen infalling matter part of the pipe wall, or is
it the water in the pipe?**

---

### §1.6 — A6: the $(1+\nu_{vac})$ loading factor

**CHOICE, on two axes.**

- **FORM.** A Poisson factor on a shell/membrane eigenfrequency is entirely ordinary elasticity — the
  form is unexceptional and this challenge does not dispute it. **What is asserted, not derived, is the
  specific $r_{eff} = r_{sat}/(1+\nu_{vac})$** (`regime-eigenvalue-method.md:16`, `:52` — the whole
  justification is the one sentence *"The saturation boundary defines the 1D strain threshold. The
  orbital mode lives in 3D — the effective cavity radius accounts for transverse Poisson coupling"*).
- **VALUE.** $\nu_{vac} = 2/7$ is **GR-IMPORTED** via $K = 2G$ (upstream F3, PR #261). Not re-opened here.
- **CIRCUIT READING.** In EE the factor is a **velocity factor / end-effect correction on the ring's
  electrical length** — the same object as the end-effect that makes a half-wave dipole physically
  shorter than $\lambda/2$. That is a clean and honest mapping *except* for its **direction**: it acts
  as a velocity factor **greater than one** ($v_\varphi = 1.286\,c_0$, CF-4). **A passive line cannot
  have $VF > 1$ in its own medium.** Recorded as failure-mode probe **E11** in §2.6 — this is one of
  the few places in this whole mapping where the circuit picture says *"that element does not exist"*.

**What the honest options are.** (i) The factor is a genuine shell-mode correction and the
$\ell$-wavelengths-around-the-circumference picture (hence $Q=\ell$) must be replaced by shell dispersion.
(ii) The factor is a placeholder for a computed graded eigenvalue and should be **retired** rather than
justified (upstream Q5 already reaches this conclusion from a different direction: a *fit* would have
picked exponent $0.355$, not $0.5$). (iii) The factor belongs to the frequency and not to the geometry,
in which case CF-1's leak-fraction correction $(1+\nu)^{\pm1}$ is live.

---

### §1.7 — A7: which $Q$?

**FORCED** to the physical $Q = \omega_R/2\omega_I$ — the $\tau$ observable is governed by it, and the
integer mode-count reading coincides with it only at $a_*=0$ (upstream §1.6's fourth reading, and
`op21-multi-mode-mode-counting.md` §1's propagated B1 note: *"an integer that can only jump cannot track
a ratio that moves smoothly"*). Nothing new to challenge. But the **circuit** reading adds two things:

#### ★★★ CF-8 — $ka = \ell$ is an IDENTITY, and it names what $Q = \ell$ actually is

The standing chain sets $\omega_R = \ell c/r_{eff}$. Therefore the mode's **electrical size** is

$$k\,r_{eff} \;=\; \frac{\omega_R}{c}\,r_{eff} \;=\; \ell \qquad\text{(exactly, by construction; }= 2.000\text{ at }\ell=2)$$

This is not a coincidence and it is not a new result — it is a one-line re-expression of two canonical
lines. **CLASS: IDENTITY** (`consistency-vs-emergence`), NOT emergence, NOT a claim.

What it *buys* is the substrate-native name for the object: in antenna/spherical-mode theory, $ka = \ell$
is exactly the **radiation cutoff of the $\ell$-th spherical mode** — the boundary between the reactive
/ evanescent regime ($ka < \ell$, energy stored, high $Q$) and the freely-radiating regime ($ka > \ell$,
energy leaves, $Q \to O(1)$). So:

> **The cold $Q = \ell$ is a claim about the external ($=$ radiation) $Q$ of a spherical multipole of
> order $\ell$, evaluated exactly at its own radiation cutoff.**

That quantity is a **closed-form standard-EE object** — the spherical-mode wave impedance
$Z_\ell(x) = j\eta\,h_\ell'(x)/h_\ell(x)$ and the Chu / Collin–Rothschild stored-energy integral. It is
computable with no free parameters, in the shear channel, from $\eta = Z_{sh,\infty}$. **That is the
missing computation upstream F7 says has never been done**, and it is what upstream R1's "computed
radiation resistance" route should actually compute.

This is an `ave-ee-first-mapping` **trigger-7 IDENTITY-COLLAPSE**: the mode-count $\ell$ and the
electrical size $ka$ are one bench object, seen from two sides. **It is proposed as candidate route
R7 in §4; it is NOT executed here.**

#### CF-14 — port-$Q$ and pole-$Q$ coincide only for an isolated single pole (an A46-class caution)

$Q = X/R$ at a port and $Q = \lvert\omega\rvert/2\lvert\mathrm{Im}\,\omega\rvert$ from a pole are the
same number for a lone second-order resonance. A **tapered** exterior contributes a **branch cut**, not
just poles; then the port-$Q$ (what a circuit calculation returns) and the pole-$Q$ (what the GR
comparator is) can differ, and the difference is not a small correction — it is the difference between
"how lossy is the port" and "where is the QNM in the complex plane". **The derivation pre-reg must
declare which object it computes and how it maps to the frozen C-$\tau$ comparator.** Recorded per
`phase-space-coordinate-check`: same register (dimensionless eigenvalue), but the *transfer* between
impedance-plane and complex-frequency-plane is an assumption, not an identity.

---

### §1.8 — A8: the boundary condition at the wall

**FORCED at $\lvert\Gamma\rvert = 1$; the sign is degenerate.** Cited honestly, verbatim from the
PR #260 B3-DEGENERATE banner (e.g.
[`vol3/cosmology/ch15-black-hole-orbitals/lattice-extreme-bh-rationality.md:28`](../manuscript/ave-kb/vol3/cosmology/ch15-black-hole-orbitals/lattice-extreme-bh-rationality.md)):

> *"the magnetic-vs-electric fork is DEGENERATE on the equilibrium observables ($Z=Z_0\sqrt{S}$,
> $\lvert\Gamma\rvert=1$ both ways), the asymmetry chirality-set not substrate-forced"*

#### CF-13 — the sign is Q-neutral in the loss ledger and Q-relevant through the frequency

- **Loss ledger:** $\lvert\Gamma\rvert = 1$ either way $\Rightarrow$ zero transmitted power $\Rightarrow$
  the wall contributes **nothing** to $Q$ under either sign. **So for the leak, A8 genuinely does not matter.**
- **Frequency:** a short puts a *node* at the rim; an open puts an *antinode*. That is a **quarter-wave
  shift in the resonator's effective radial length**, which moves $\omega_R$, which moves
  $Q = \omega_R/2\omega_I$. **So for the eigenvalue, A8 matters — and the standing chain never uses the
  radial boundary condition at all** (it is a purely tangential $\ell$-counting argument, which has no
  radial degree of freedom to apply a boundary condition to).

**That absence is itself the finding**: the standing derivation is *insensitive* to A8 because it has no
radial structure. Any route that gives the cavity radial structure (R2 / R7) immediately becomes
sensitive to it, and the #260 degeneracy no longer protects the answer.

---

### §1.9 — A9: where does the radiated energy go?

The exterior is a **tapered line** from $Z_{shear}(r_{sat}) \to 0$ (or $\to\infty$, CF-7) up to
$Z_{shear}(\infty) = \rho_0 c_0$. Two numbers decide whether that taper reflects:

- **Mode wavelength (far field):** $\lambda_\infty = 2\pi c/\omega_R = 2\pi M_g/(18/49) = 17.10\,M_g$.
- **Grade scale:** the strain profile $A = 7M_g/r$ does essentially all its work between $r_{sat}=7\,M_g$
  and $\sim 2r_{sat}$, i.e. over $\sim 7\,M_g$.

$\Rightarrow$ **the whole taper is $\approx 0.41$ wavelengths long.** *(Arithmetic on canonical inputs;
IDENTITY/consistency class, not a claim.)*

**This is the number the elastic picture never computes and the circuit picture demands.** A taper much
longer than $\lambda$ is adiabatic (reflectionless, low $Q$, energy just leaves). A taper much shorter
than $\lambda$ is a lumped discontinuity (strongly reflecting, high $Q$). **$0.41\lambda$ is the
borderline** — the one regime where neither limit applies, where partial reflection is guaranteed, and
where $Q$ comes out $O(1)$ rather than $\gg1$ or $\approx 1$. **The observed $Q\approx2$ is exactly what
a borderline taper gives.** That is a structural consistency the corpus has never noticed and it is a
genuine point in the standing picture's favour.

**Does re-reflection feed back into $Q$?** Yes — *by definition*. Loaded $Q$ is set by the **input
impedance of the taper seen at the rim**, and a partially-reflecting taper is exactly what makes
$\mathrm{Re}\{Z_{in}\} \neq Z_{sh,\infty}$. There is no separate "echo correction"; the echo and the $Q$
are two readings of the same $Z_{in}$.

**And that relocates the corpus's own echo prediction.** `vol3/claim-quality.md:123` banks
*"gravitational ringdown **echoes are predicted** (reflect $\Rightarrow$ echo)"*. Per CF-9 the second
mirror is **not** the light ring (which is inside the wall) — it is the **taper's own turning point** at
$\approx 7.8$–$8.6\,M_g$. The echo delay is therefore $\Delta t \approx 2\int_{r_{sat}}^{r^\star} dr/c_{shear}(r)$,
a **short** delay set by the near-wall slow-down (the integrand diverges as $(r-r_{sat})^{-1/4}$, which
is integrable — a finite delay), **not** the long light-ring delay that published LIGO echo searches
target. **This materially changes the exposure upstream Q7 asks Grant about**: the risk is not
"AVE's echo is excluded", it is "AVE's echo is at a different delay than anyone has searched".

---

## PART 2 — THE VACUUM-CIRCUIT MAPPING (EE-first)

`ave-ee-first-mapping` fired as the **primary** framing skill, per the brief. Canonical home for the
mapping catalog: [`common/translation-tables/translation-circuit.md`](../manuscript/ave-kb/common/translation-tables/translation-circuit.md)
(§4 primitive↔component catalog, §4.5 tool tracker, §4.6/§4.7 tiered rows).
**Nothing is landed in that leaf by this document** — see §2.7.

### §2.1 — The one load-bearing move: declare $(L, C)$, let $Z$ and $c$ fall out

Stated in full at **CF-5**. The whole of the standing impedance-register confusion is a
**two-degrees-of-freedom problem being described with three statements.** The circuit discipline is:
a transmission line is specified by $L$ and $C$ per unit length and by nothing else. The mechanical
dictionary for the shear channel is the standard one:

$$L \;\leftrightarrow\; \rho \ (\text{node inertia}), \qquad C \;\leftrightarrow\; 1/G_{shear}\ (\text{bond compliance})$$
$$\Rightarrow\quad Z_{shear}=\sqrt{L/C}=\sqrt{\rho\,G_{shear}}=\rho\,c_{shear},\qquad c_{shear}=1/\sqrt{LC}=\sqrt{G_{shear}/\rho}$$

The first output **is** `vol3/claim-quality.md:122`'s $Z_{shear} = \rho\,c_{shear}$, verbatim. That is
the means-test PASS that licenses the rest of the mapping.

### §2.2 — Element table: circuit element ↔ lattice primitive ↔ canonical leaf

| # | Ringdown object | Circuit element | Lattice primitive | Canonical receipt | Mapping |
|---|---|---|---|---|---|
| **E1** | inertia of a node against transverse displacement | **series $L$ per unit length**, $L = L_0$ (unsaturated) | K4 node translational DOF | `translation-circuit.md` §4 ("K4 node intrinsic LC"; "Translational E DOFs at node → Capacitor" is the *EM* row — the mechanical dual swaps $L\!\leftrightarrow\!C$, see ⚑ below) | clean |
| **E2** | shear bond compliance $1/G_{shear}(A)$ | **shunt $C$ per unit length**, $C = C_0/S$ | Ax 4 kernel projected into shear | `saturating-modulus-and-backreaction.md:52,60`; `nonlinear-vacuum-capacitance.md:27` (form) | clean, with the CF-5 kernel-argument residual |
| **E3** | local shear speed | $1/\sqrt{LC} = c_0\sqrt S$ | Op16 | `common/operators.md` Op16; `saturating-modulus…:60` | clean |
| **E4** | local shear characteristic impedance | $\sqrt{L/C} = Z_{sh,0}\sqrt S$ | three-channel impedance law | `vol3/claim-quality.md:122` | clean |
| **E5** | the wall at $r_{sat}$ ($A=1$) | **short-circuit termination**, $Z\to0$, $\Gamma=-1$ | Ax 4 saturation / Regime-IV melt | `vol3/claim-quality.md:122-123`; `op21-…:§2.2` | clean; **sign degenerate** (#260), and Q-neutral in the loss ledger (CF-13) |
| **E6** | the graded exterior $r > r_{sat}$ | **non-uniform (tapered) transmission line**, $Z(r) = Z_{sh,0}\sqrt{S(A(r))}$, $A = 7M_g/r$ | Op14 graded network | `temporal-spatial-lattice-decomposition.md:14`; `saturating-modulus…:51,60` | clean — **this is the $Q$ integrand** |
| **E7** | far cold lattice | **matched load** $Z_\infty = \rho_0 c_0$ (the line's own reference) | Regime I linear lossless | §0 REGIME header | clean |
| **E8** | the $\ell=2$ rim oscillation | **ring resonator** = closed loop of $\ell$ full wavelengths; equivalently the $\ell$-th **spherical mode** of the exterior | Op21 single-channel wavelength count | `op21-…:§2.3` | clean |
| **E9** | the "$1/\ell$ leak per cycle" | **external (radiation) $Q$ of the $\ell$-th spherical mode at $ka=\ell$** | curvature radiation from a curved-interface surface wave | CF-8; `regime-eigenvalue-method.md:63` | ★ **NEW correspondence — candidate row, NOT landed** (§2.7) |
| **E10** | $Q$ itself | **loaded $Q$** $= \omega W_{stored} / P_{out} = X_{rim}/\mathrm{Re}\{Z_{in}^{taper}\}$ | — | template at [`theorem-3-1-q-factor.md`](../manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/theorem-3-1-q-factor.md) ($Q_{tank}=\omega_C L_e/R$ at $R = Z_0/4\pi$) | clean in FORM; ⚠ **sector caution**: the template is an **EM**-channel calculation ($Z_0 \equiv Z_{EM}$) and this is a **shear** problem — the upstream R1 leak risk, restated |
| **E11** | the $(1+\nu_{vac})$ factor | **velocity factor / end-effect correction** on the ring's electrical length | Poisson transverse coupling | `regime-eigenvalue-method.md:16,52` | ⚠ **NO CLEAN MAPPING** — acts as $VF = 1.286 > 1$; a passive line cannot exceed its own medium's speed. **Failure-mode probe** |
| **E12** | $\rho_{eff} = \rho_0/S^3$ (topological halting) | would be a **series $L$ diverging at the wall** $\Rightarrow Z\to\infty \Rightarrow$ **open** termination | infalling-matter inertia | `interior-singularity-resolution.md:19` | ⚠ **CONFLICTS with E1/E5.** Failure-mode probe / CF-7 |
| **E13** | the predicted echo | **multiple reflection between E5 and the partially-reflecting taper E6** | — | `vol3/claim-quality.md:123` | clean; delay $= 2\int_{r_{sat}}^{r^\star} dr/c_{shear}$ (CF-9) |
| **E14** | spin $a_*$ / frame dragging $\Omega$ | **a non-reciprocal (gyrotropic) bias on the ring — a ferrite-circulator loading**, splitting CW from CCW | Cosserat micro-rotation bias | `frame-dragging-impedance-convolution.md:15`; the Park/FOC reading at `kerr-q-correction.md:49-61` | ⚠ **PARTIAL** — the corpus models it as a **frequency offset** $\omega\to\omega-m\Omega$ (a rotating-frame Doppler), which is **not the same EE object** as a circulator's nonreciprocal mode split. Both are legitimate EE devices; they make different $Q$ predictions. **FLAG** |
| **E15** | radial overtone index $n$ | **higher-order radial resonances of the tapered line** (they exist automatically) | — | — | ⚠ **NO CORPUS OBJECT AT ALL.** Failure-mode probe / gap |

> ⚑ **Dual-convention note (stated so it cannot silently flip a sign).** The `translation-circuit.md` §4
> rows map the **EM** channel (translational DOF → capacitor, micro-rotational DOF → inductor). The
> **mechanical/shear** channel uses the **impedance analogy's dual** (inertia → $L$, compliance → $C$),
> which is what reproduces $Z_{shear} = \rho c_{shear}$. Both are standard; mixing them is exactly the
> open/short trap that `translation-circuit.md:119` already documents on the substrate side — verbatim:
> *"$\Gamma = -1$ saturation TIR boundary | **Short-circuit ($Z \to 0$) / Total reflection** … NOT the
> dielectric-yield boundary: $\tau_{yield}$ is the **electric** branch ($\varepsilon_{eff} \to 0$,
> $Z \to \infty$, **open-circuit**, $\Gamma \to +1$)"*. This document uses the mechanical dual
> **throughout PART 2** and says so here once.

### §2.3 — The taper, quantitatively (the number the elastic picture never computes)

$$\lambda_\infty = \frac{2\pi c}{\omega_R} = \frac{2\pi M_g}{18/49} = 17.10\,M_g, \qquad
\text{grade scale} \sim r_{sat} = 7\,M_g \;\Rightarrow\; \frac{\text{taper length}}{\lambda} \approx 0.41$$

*(Arithmetic on canonical inputs. IDENTITY/consistency class. Not a claim.)*

| taper regime | reflection | resulting $Q$ | is this us? |
|---|---|---|---|
| $L_{taper} \gg \lambda$ | adiabatic, $\Gamma_{in}\to0$ | low, $Q \to \sim1$ | no |
| $L_{taper} \ll \lambda$ | lumped discontinuity, $\lvert\Gamma_{in}\rvert\to1$ | high, $Q \gg 1$ | no |
| $L_{taper} \sim 0.4\lambda$ | **partial, frequency-dependent** | **$O(1)$, a few** | **yes — and $Q\approx2$ is what that gives** |

**This is the structural reason $Q$ is small, and it is invisible in elastic language.** The elastic
picture says "perfect mirror inside, radiation outside" and has no way to ask *how many wavelengths thick
is the impedance ramp*. The circuit picture asks that first, because it is the only question that
decides whether a taper reflects.

### §2.4 — $Q$ as the taper's input-impedance mismatch (and what $Q = \ell$ becomes)

The loaded $Q$ of a resonator coupled through a taper is

$$Q \;=\; \frac{\omega\,W_{stored}}{P_{radiated}} \;=\; \frac{X_{rim}}{\mathrm{Re}\{Z_{in}(r_{sat})\}}$$

where $Z_{in}(r_{sat})$ is the **input impedance of the tapered line E6 terminated in the matched cold
lattice E7, transformed back to the rim.** Three consequences, each of which reframes something in the
standing derivation:

1. **The wall is not in this formula.** E5 is a lossless termination on the *other* side; it sets the
   standing-wave phase, not the loss. This is CF-11 in one line: **$Q$ is a taper problem, not a wall problem.**
2. **"Leak per cycle $= 1/\ell$" becomes "$\mathrm{Re}\{Z_{in}\}/X_{rim} = 1/\ell$"** — i.e. upstream
   F7's uncomputed proportionality constant $c_1$ is precisely the ratio of the taper's **input
   resistance** to the rim mode's **reactance**. That is a computable number, not a convention.
3. **At $ka = \ell$ (CF-8), the taper-free limit of that ratio is a textbook closed form.** Strip the
   grade (set $S\equiv1$) and E6 becomes free space; then $Z_{in}$ is exactly the $\ell$-th spherical-mode
   wave impedance $Z_\ell(x) = j\eta\,h_\ell'(x)/h_\ell(x)$ evaluated at $x = ka = \ell$, and $Q$ is the
   Chu/Collin–Rothschild external $Q$ of that mode. **The graded profile is then a correction on top of a
   known cold answer** — which is a far better-posed derivation than starting from a scaling assertion.

> **This is the derivation-lane target this framing challenge recommends** (candidate **R7**, §4).
> It is stated, not executed. Executing it is the derivation lane's job, after Grant's walk.

### §2.5 — What each picture makes obvious, and what each hides

**The CIRCUIT picture makes obvious (and the elastic picture hides):**

1. **Only $(L,C)$ are free.** Three canonical statements for two DOF ⇒ the whole $\sqrt S$-vs-$S^{1/4}$
   flag is an over-determination, not a physics fork (CF-5/CF-6). Elastic language never forces you to
   count degrees of freedom, so the corpus carried three inconsistent registers for a year.
2. **Taper length in wavelengths is the question** (§2.3). Elasticity gives you "there is a gradient";
   circuits give you "0.41 λ, therefore borderline, therefore $Q = O(1)$".
3. **The wall drops out of the loss ledger** (CF-11). The elastic "perfect reflector ⇒ TIR ⇒ high $Q$"
   intuition is exactly backwards about *where* $Q$ comes from.
4. **$ka = \ell$ is an identity** and it names the object (CF-8). The elastic phrase "$\ell$ wavelengths
   fit around the circumference" conceals that this is the antenna radiation-cutoff condition, with a
   closed-form answer sitting right there.
5. **$VF > 1$ is impossible** (E11/CF-4). Elasticity happily writes a Poisson factor; a transmission line
   refuses to propagate faster than $1/\sqrt{LC}$.
6. **A resonator has exactly one electrical length.** CF-1's two-radius split is invisible in prose and
   glaring the moment you ask "so how long is the line?"

**The ELASTIC picture makes obvious (and the circuit picture hides):**

1. **Polarisation and grade structure.** A scalar TL has one field; the substrate has A1 dilatation, T2
   shear (two polarisations) and the Cosserat micro-rotation. **The circuit cannot carry the A1 ⊥ T2
   split** — this is exactly disanalogy (ii) already banked at `translation-circuit.md` §4.7.3 for the
   network-duality row, live again here.
2. **Angular structure ($\ell$, $m$).** A 1-D line has no $\ell$; you have to *import* the spherical-mode
   ladder to get one. That is why E8/E9 map to spherical modes rather than to a lumped ring.
3. **Mode conversion at an interface.** P↔SV conversion at a solid/fluid boundary (CF-15) is elementary
   elastodynamics and has no scalar-circuit counterpart at all.
4. **What the interior can carry.** The circuit says "short". The elastic picture says "shear cannot
   exist there but bulk can" — which is precisely the CF-15 disposal question, and only the elastic
   picture even poses it.

### §2.6 — Failure-mode probes (elements with no clean mapping)

Per `ave-ee-first-mapping` §"Failure-mode probes" — honest list, four entries:

| probe | element | why it fails to map | what it would take |
|---|---|---|---|
| **P1** | **E11** — $(1+\nu_{vac})$ as $VF = 1.286 > 1$ | passive lines cannot exceed $1/\sqrt{LC}$; the factor is not a line property | either a shell-dispersion object (a *different* wave type, not a TL mode), or retirement of the factor |
| **P2** | **E12** — $\rho_{eff} = \rho_0/S^3$ | it is a *matter* inertia, not a line inertia; if it were the line's, the termination flips short→open | canon must say which $\rho$ enters $Z_{shear}=\rho c_{shear}$ (CF-7 / FORK-3) |
| **P3** | **E14** — spin as Doppler-offset vs circulator-bias | a rotating-frame frequency shift and a gyrotropic nonreciprocity are different devices with different loaded-$Q$ structure | decide whether $\Omega$ is a kinematic frame rate or a material bias (upstream Q4, now with an EE-sharp form) |
| **P4** | **E15** — radial overtone $n$ | not a mapping failure but a **corpus gap**: the circuit *has* the object, AVE has no name for it | either derive the radial ladder or state why the AVE cavity is single-layer |

**Not a failure mode, recorded to prevent a false one:** $\ell$ itself. EE does not derive *which*
integer; the spherical-mode ladder supplies the family and topology/geometry supplies the index — the
standard `translation-circuit.md` §7 Probe-1/Probe-5 verdict (geometry/topology content EE does not
furnish, but cross-checks once fixed).

### §2.7 — Landing note (Step 6 discipline, deliberately NOT executed)

`ave-ee-first-mapping` Step 6 says a **new** substrate↔EE correspondence is not done until it is landed
in `translation-circuit.md` §4 + mirrored into the skill + cross-ref'd. This document establishes two
candidate rows:

- **Candidate row (a) — E9:** *"Op21 $1/\ell$ per-cycle leak at a curved saturation boundary" ↔ "external
  (radiation) $Q$ of the $\ell$-th spherical mode at $ka=\ell$ (Chu / Collin–Rothschild)"*.
- **Candidate row (b) — E14:** *"frame-dragging $\Omega$ at a spinning saturation wall" ↔ "gyrotropic
  (ferrite-circulator) bias on a ring resonator"*.

**Neither is landed, and that is deliberate.** Step 6 lands *established* correspondences; these are
**hypotheses generated by a framing challenge**, means-test **not yet run** (running it *is* the
derivation). Landing an unvalidated row would put a hypothesis in the canonical catalog — the exact
failure mode `ave-mechanism-claims-discipline` exists to stop. **Routed to the auditor lane to land
if and when the derivation validates them.**

---
