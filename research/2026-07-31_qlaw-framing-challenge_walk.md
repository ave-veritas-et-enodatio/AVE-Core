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
- **NOT a retitle of the upstream scoping doc.** F1–F9 stand as written; this document adds CF-1…CF-16
  in a separate numbering space so the two sets never collide.

## Sections

- §0 — Sector / regime / phase-state / coordinate header
- **PART 1** — §1 Adversarial framing challenge (A1–A9, verdict table, CF-1…CF-16)
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
| **A1** | The resonator is the wall rim at $r_{sat}$ (the "bell") | **OPEN-FORK** — four candidate resonators, canon has explored one; and the standing chain uses **two different radii** for the same mode **without declaring which reading it intends** (cutoff radius vs physical wall — one mode described twice, or two places) | CF-1, CF-2, CF-3, CF-9, CF-10 |
| **A2** | Sector ownership: observable is shear (T2); no A1 admixture | **FORCED** at linear order (A1 = DC bias, T2 = AC signal; any A1 product lands at $2\omega$ or DC, not $\omega$). **Sub-fork OPEN**: does the anisotropic vessel state split the rim modes? | CF-12 |
| **A3** | Mode geometry: whispering-gallery $\ell = 2$, linear-$\ell$ dispersion | **OPEN-FORK** on $\ell$ vs $\sqrt{\ell(\ell+1)}$ (upstream F4, binned UNDETERMINED). **Separate GAP, not a fork** — *corrected 2026-07-31 (F1 repair pass, audit F2)*: AVE **does** own a radial-overtone object ($n_r$, Op6); what is true is narrower — **the BH-ringdown chain does not instantiate it** | CF-8, and §2.6 probe E15 |
| **A4** | The loss channel is radiation outward into the graded exterior | **FORCED by canon** that the wall is lossless and contributes **nothing** to $Q$ — which makes the corpus's own label ("$Q$ from the $\Gamma=-1$ TIR boundary") a mis-attribution. **OPEN** off the exact $A=1$ point: $\lvert\Gamma\rvert < 1$ there, and the transmitted shear has nowhere to go as shear | CF-11, CF-15 |
| **A5** | The local shear speed exponent ($\sqrt{S}$ vs $S^{1/4}$) is the biggest open input | **RECLASSIFIED → CHANNEL fork, and CLOSED for the shear integrand at $\sqrt{S}$** by three-way over-determination in the $(L,C)$ constitutive pair. **Routed to Grant for ratification; NOT canon until he rules.** | **CF-5, CF-6**, CF-16 ★ |
| **A6** | The $(1+\nu)$ loading factor | **CHOICE** — the FORM (a Poisson factor on a shell mode) is plausible and unexceptional; the SPECIFIC $r_{sat}/(1+\nu)$ is **asserted, not derived**, and its VALUE is GR-imported (upstream F3). Its arithmetic content is that the physical wall sits $9/7$ **above the $\ell$-th mode's own radiation cutoff** ($k r_{sat} = 2.571$) — a *result*, not a defect (CF-4 retracted 2026-07-31) | CF-1, CF-4 |
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

#### ★ CF-1 — the canonical five-step chain uses TWO different radii for the same mode, and never states which reading it intends

> **⚠ Downgraded 2026-07-31 (repair pass, PR #814 audit F1).** This finding was originally written as an
> **inconsistency**. It is not one. Under the spherical-multipole reading established in the corrected
> **CF-4** below, $r_{eff}$ is the $\ell$-th mode's **radiation-cutoff radius** and $r_{sat}$ is the
> **physical wall** — *one mode described twice*, at two radii that stand in the fixed ratio
> $r_{sat}/r_{eff} = 1+\nu_{vac}$. What is genuinely open, and what this finding now says, is that
> **the chain never states which of the two readings it is using**, so a reader cannot tell whether
> "effective cavity radius" means a place or a cutoff. The steelmen below are unchanged and still stand.

Verbatim, same file, adjacent steps:

> `:52` — $r_{\mathrm{eff}} = \dfrac{r_{\mathrm{sat}}}{1 + \nu_{\mathrm{vac}}} = \dfrac{7}{1 + \tfrac{2}{7}} = \dfrac{49}{9}\,M_g \approx 5.444\,M_g$
>
> `:55` — **Step 4: Eigenfrequency.** The $\ell = 2$ tangential standing wave **at $r_{\mathrm{eff}}$** …
>
> `:63` — The mode **orbits tangentially at $r_{\mathrm{sat}}$** with $\ell$ wavelengths fitting around
> the circumference. Each wavelength subtends angle $2\pi/\ell$, and the curvature radiation loss per
> cycle scales as $1/\ell$ …

*[emphasis added on "at $r_{\mathrm{eff}}$" and "at $r_{\mathrm{sat}}$"; both phrases are unbolded in the
source. Both quotes are truncated: `:55` continues with a colon into the displayed equation, and `:63`
continues "…, giving:" into the Resultbox.]*

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
**Verdict (revised 2026-07-31, F1):** the resonator's radius is a **reading the chain never declares**.
Under the multipole reading the two radii are the same mode's cutoff radius and physical wall; under the
literal reading they are two places and CF-2 bites. The chain's own prose does not distinguish them.

#### ★ CF-2 — $r_{eff}$ sits 22% INSIDE the shear-reflecting wall **under the literal (place) reading only**

$r_{eff} = 49M_g/9 = 5.444\,M_g$ against $r_{sat} = 7\,M_g$. The Poisson correction points **inward**,
into the region canon calls Regime IV, where
[`vol3/cosmology/ch15-black-hole-orbitals/electron-bh-isomorphism.md`](../manuscript/ave-kb/vol3/cosmology/ch15-black-hole-orbitals/electron-bh-isomorphism.md)
states verbatim: *"Gravitational waves, being **transverse shear waves**, **cannot propagate** in the
ruptured interior"*. Under the literal "cavity radius" reading, the eigen-radius is inside the region
where the mode cannot exist.

**Steelman:** identical to CF-1's — $r_{eff}$ is a length, not a place. **The two findings are one fork
with two horns:** either $r_{eff}$ is a radius (and it is inadmissible), or it is **not a place at all**
— the $\ell$-th mode's cutoff radius, a spectral quantity — and the chain's own word "effective cavity
**radius**" invites the wrong reading.

> **⚠ Downgraded 2026-07-31 (F1).** The original text closed this horn with "*and CF-4 bites*". **It does
> not** — CF-4's $VF>1$ objection is retracted below, so the cutoff-radius horn carries **no** residual
> defect. The live content of CF-1/CF-2 is now entirely the **undeclared reading**, not an inconsistency.

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

#### 🔴 CF-4 — RETRACTED 2026-07-31 (repair pass, PR #814 audit F1). The "$v_\varphi > c_0$ is impossible" objection was a framing artifact; the $1.286$ is $r_{sat}/r_{eff}$, and that is a *result*, not a defect

**What was wrong.** "A passive line cannot have $VF > 1$" is a **uniform-TEM** statement. It is true of a
TEM transmission line, which has exactly one propagation constant $1/\sqrt{LC}$. It was applied here to
the **azimuthal phase velocity of a spherical multipole**, which is a different object and which
**exceeds $c_0$ above cutoff by definition**. For an $\ell$-th multipole the azimuthal phase speed at
radius $r$ is $v_\varphi(r) = \omega r/\ell$; it equals $c_0$ **exactly at** $kr=\ell$ and rises linearly
with $r$ beyond it. No energy moves superluminally — the **radial group** velocity carries the power and
stays subluminal. A phase front sweeping a large circle faster than $c_0$ is the ordinary above-cutoff
behaviour of every waveguide and every spherical mode; it is the same thing as $v_\varphi = \omega/\beta
= c/\sqrt{1-(f_c/f)^2} > c$ in a hollow guide.

**The arithmetic, restated correctly — and it is the real content of $(1+\nu_{vac})$.**
CF-8 gives $k\,r_{eff} = \ell$ exactly. That **is** the radiation-cutoff condition, so $r_{eff}$ is the
$\ell$-th mode's **cutoff radius**. Then

$$k\,r_{sat} \;=\; k\,r_{eff}\cdot\frac{r_{sat}}{r_{eff}} \;=\; \ell\,(1+\nu_{vac}) \;=\; \tfrac{9}{7}\cdot 2 \;=\; \mathbf{2.571},
\qquad v_\varphi(r_{sat}) \;=\; \frac{\omega_R\,r_{sat}}{\ell} \;=\; \tfrac97 c_0 \;=\; 1.286\,c_0$$

**$1.286$ is not a velocity-factor violation — it *is* $r_{sat}/r_{eff}$**, the factor by which the
physical wall sits above the $\ell$-th mode's own cutoff. And $v_\varphi(r_{eff}) = c_0$ **exactly**,
which is the cutoff condition written a third way. *(CLASS: IDENTITY — three re-expressions of
$\omega_R M_g = 18/49$, $r_{eff}=49M_g/9$, $r_{sat}=7M_g$.)*

**Canon carries superluminal phase velocities on its own account.** `manuscript/ave-kb/claim-quality.md:111-112`,
quoted verbatim in this very document's CF-5 table: *"$c_{EM,sym} = c_0/S \to \infty$ (EM phase velocity
rises)"* and *"$c_{EM,asym} = c_0/\sqrt{S} \to \infty$ (EM evanescent, no energy transport)"*. **A framing
challenge that forbids $v_\varphi > c_0$ deletes two of the three branches in its own CF-5 table.** That
self-collision is the tell that the objection, not the corpus, was wrong.

**FORK-4 is therefore re-posed, not closed.** The two-radius structure is still an open physics question
— but the open question is no longer "explain the impossible velocity". It is the audit's plumber form:

> **The standing chain puts the physical wall exactly $9/7$ above the mode's own cutoff radius. Is that
> the $(1+\nu_{vac})$ factor's actual job — a cutoff-to-wall ratio — or is the coincidence accidental?**

**Decision-relevant arithmetic — where on the curve you evaluate matters more than the fork looked.**

> **⚑ AUDITOR-ARITHMETIC (provenance: PR #814 compact audit, 2026-07-31).** Yaghjian–Best $Q_Z$ for the
> $\ell=2$ spherical mode: **$1.962$ at $ka=2$** (cutoff / $r_{eff}$) vs **$0.965$ at $ka=2.571$**
> (wall / $r_{sat}$) vs **$1.100$ at $ka=2.449$** (the $\sqrt{\ell(\ell+1)}$ fork of A3).
> **The cutoff-vs-wall choice moves $Q$ by a factor of $\sim2$.** This is a **spin-1 vector-multipole**
> estimator — see the sector caution now carried at CF-8/E10/R7 (F10): the GW observable is a **spin-2
> tensor** multipole and its impedance relation is *not* imported here. Illustrative locator for the
> fork's size, **not a derivation, not a claim, not pre-registered**.

> **⚑ IMPLEMENTER RE-COMPUTATION (2026-07-31, flag-don't-fix — the two do not agree numerically).**
> Re-running the standard Yaghjian–Best estimator
> $Q_Z = \tfrac{1}{2R}\sqrt{(x R')^2 + (x X' + \lvert X\rvert)^2}$ on the spherical-mode wave impedance
> $Z_\ell(x)/\eta = j\,\hat H_\ell'(x)/\hat H_\ell(x)$, $\hat H_\ell(x) = x h^{(2)}_\ell(x)$, $x = ka$,
> I get **$1.863 / 0.839 / 0.973$** for the same three points, **not** $1.962/0.965/1.100$. Running the
> *exact* Chu / Collin–Rothschild stored-energy $Q$ instead (validated to 4 digits against the closed
> forms $1/x + 1/x^3$ at $\ell=1$ and $3/x + 6/x^3 + 18/x^5$ at $\ell=2$) gives **$2.812 / 1.679 / 1.837$**.
> **All three estimators agree on the decision-relevant fact** — cutoff → wall moves $Q$ down by
> $40$–$55\%$, i.e. by roughly $2\times$ — **and they disagree on the absolute number by up to $50\%$**,
> because $Q_Z$ is a high-$Q$ approximation and this problem sits at $Q\sim2$. **That estimator spread is
> CF-14 (port-$Q$ vs pole-$Q$) showing up as a number rather than as a caution.** Surfaced, not resolved.

> **Preserved original (Rule 12), superseded 2026-07-31 — retained verbatim, NOT refilled with a new
> hypothesis.** *"CF-4 — the two-radius reading implies a tangential phase speed of $1.286\,c_0$. Take
> Step 5's geometry literally (ring at $r_{sat}$, $\ell$ wavelengths around the circumference) and Step
> 4's frequency: $\lambda = 2\pi r_{sat}/\ell$, so $v_\varphi = \omega_R\lambda/2\pi = c_0(1+\nu_{vac}) =
> 1.286\,c_0$. A tangential wave running around the rim at $1.286\,c_0$ — in a region where canon says
> the local shear speed is $\le c_0$ and heading to $0$. **Steelman.** Shell theory does put Poisson
> factors on membrane eigenfrequencies, and a 'frequency-raising' factor is not by itself superluminal
> if the mode is not a simple travelling tangential wave (a flexural shell mode has a different
> dispersion). But then the $\ell$-wavelengths-around-the-circumference picture — which is the entire
> source of $Q = \ell$ — no longer applies, and $Q$ has to come from somewhere else. The two halves of
> the standing derivation are load-bearing on mutually exclusive mode pictures."*
>
> The final sentence is the part that does not survive: under the multipole reading the two halves are
> **the same picture** — $\ell$ wavelengths around the cutoff circle *is* $ka=\ell$.

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
  overtone index $n$. ~~**AVE has no object for $n$ at all.**~~
  🔴 **CORRECTED 2026-07-31 (repair pass, PR #814 audit F2) — the original sentence was FALSE.**
  **AVE owns a radial-overtone object and has for a long time: $n_r$, and Op6 owns it.** Receipts,
  verified two-method (Appendix B rows 21–24):
  - [`vol2/quantum-orbitals/ch07-quantum-mechanics/radial-eigenvalue-solver.md:160`](../manuscript/ave-kb/vol2/quantum-orbitals/ch07-quantum-mechanics/radial-eigenvalue-solver.md)
    verbatim: *"where $n_r = n - l - 1$ is the number of radial nodes (Step 1(h)). **This phase-matching
    condition IS Op6**: the eigenvalue $E$ is the value for which the total phase equals $n_r \pi$."*
    The condition itself is $\int_0^{R_a} k_{in}\,dr + \int_{R_a}^{r_{max}} k_{out}\,dr + \phi_\Gamma = n_r\pi$
    — **a radial phase integral with an explicit reflection phase $\phi_\Gamma$ at the inner boundary.**
  - [`vol2/quantum-orbitals/ch07-quantum-mechanics/de-broglie-standing-wave.md:226`](../manuscript/ave-kb/vol2/quantum-orbitals/ch07-quantum-mechanics/de-broglie-standing-wave.md)
    verbatim table row: *"| Radial | Phase per bounce between turning points | $n_r$ | Radial quantum number |"*.
  - [`common/operators.md:189`](../manuscript/ave-kb/common/operators.md) verbatim:
    *"Op6 (eigenvalue target → radial nodes $n_r$), Op10 ($c=3$ invariant → angular nodes $l$)"* —
    **the angular/radial split is explicitly operator-owned in canon.**

  **The narrow true statement, which is what this finding now asserts:** *the BH-ringdown chain does not
  instantiate $n_r$.* The five-step chain produces exactly one resonance and never writes a radial phase
  integral. Canon already **knows** this and scopes the claim accordingly —
  [`vol3/claim-quality.md:205`](../manuscript/ave-kb/vol3/claim-quality.md) verbatim:
  *"'$Q = \ell$' is the lattice-derived form; for higher modes ($\ell > 2$) this disagrees with GR
  overtone structure — **the claim is the fundamental mode, not the full QNM spectrum**."*
  So this is a **chain-coverage gap, not a corpus-vocabulary gap**, and it is a *smaller* finding than
  originally written — but it is now a **sharper** one, because the object that would close it already
  exists and has a canonical phase-matching form to apply. Recorded as probe **E15** in §2.6.

  > **⚠ Routed, NOT repaired here — a corpus error this repair pass found while verifying the above.**
  > Two canonical leaves cross-wire the **angular** index with the **overtone** index. Verbatim, identical
  > row in both: *"| First excitation | Cinquefoil $c = 5$ (proton) | $\ell = 3$ **(1st GW overtone)** |"* —
  > [`vol2/appendices/app-f-solver-toolchain/knot-mode-isomorphism.md:22`](../manuscript/ave-kb/vol2/appendices/app-f-solver-toolchain/knot-mode-isomorphism.md)
  > and [`common/solver-toolchain.md:440`](../manuscript/ave-kb/common/solver-toolchain.md).
  > **$\ell = 3$ is the octupole — a different *angular* multipole, not an overtone of $\ell = 2$.** The
  > GW overtone index is $n$ (radial), and $\ell$ and $n$ are independent quantum numbers. The row's own
  > ladder line two rows above (*"$\ell = 2, 3, 4, 5, \ldots$"*) is fine; only the "(1st GW overtone)"
  > gloss is wrong. **Flag-don't-fix: not repaired in this lane** (it is a Vol-2 appendix + common-toolchain
  > leaf, outside this branch's two-file scope). **Routed to the auditor lane with both paths and the
  > verbatim row.**

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

#### ★ CF-16 — a corroborating honesty-lag: the 2026-06-22 clock-exponent correction did not propagate, and the leaf that lags contradicts itself four lines apart

The CF-5 table's SHEAR row is independently corroborated by a correction canon has already made
elsewhere. [`op14-local-clock-modulation.md:13`](../manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/op14-local-clock-modulation.md),
verbatim:

> **Matter-clock exponent (corrected to the $1/4$ shear form, 2026-06-22).** The local matter clock rides
> the **shear** speed $c_{\text{shear}} = c_0\cdot(1-A^2)^{1/4} = c_0\sqrt{S}$ … the matter-clock forms
> are $\omega_{\text{local}} = \omega_{\text{global}}(1-A^2)^{1/4}$ … **The earlier $(1-A^2)^{1/2}$
> exponent was the pre-split single-speed model … it was off by a factor of 2 in the exponent and is now
> corrected**

That corrected form, $\omega_{local} \propto \sqrt S$, is **exactly** what the SHEAR branch's
$\omega = 1/\sqrt{LC}$ gives with $L$ fixed and $C = C_0/S$. Two independent routes, same exponent.

**The lag.** [`vol3/cosmology/ch04-generative-cosmology/op14-cosmic-horizon-profile.md`](../manuscript/ave-kb/vol3/cosmology/ch04-generative-cosmology/op14-cosmic-horizon-profile.md)
still carries the **superseded** exponent at `:22` and `:43`
($\omega_{local} = \omega_{global}\cdot\sqrt{1-A^2}$, i.e. $\propto S$) — and `:41` cites
`op14-local-clock-modulation.md:13`, **which is the very line that retracts it.** Worse, the same leaf
writes the **corrected** form four lines later at `:47`
($\omega_{local}(r\to R_H) = \omega_{global}\cdot\sqrt{S(A(R_H))}$). **One leaf, both exponents, four
lines apart.**

**Flag-don't-fix.** Not repaired here; not in this lane's scope (it is a cosmology leaf, and the
ringdown does not consume it). Surfaced with both line numbers for the auditor lane. **Why it matters
to this lane anyway:** it is a third, independent instance of the same failure class as CF-5/CF-6 — an
exponent register that drifted because $Z$, $c$ and $\omega$ were maintained as three separate
statements instead of as outputs of one $(L,C)$ pair.

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
- **CIRCUIT READING (corrected 2026-07-31, F1).** The original text read this factor as a
  **velocity factor** and objected that it acts as $VF>1$. **That objection is retracted** — see the
  superseded CF-4. A ring resonator is not a uniform TEM line, and the azimuthal phase velocity of an
  $\ell$-th spherical multipole exceeds $c_0$ above its own cutoff **by definition**. The honest circuit
  reading is instead a **cutoff-to-wall ratio**: $k\,r_{eff} = \ell$ makes $r_{eff}$ the mode's cutoff
  radius, $k\,r_{sat} = \ell(1+\nu_{vac}) = 2.571$, and $(1+\nu_{vac})$ is exactly how far above cutoff
  the physical wall sits. Whether that is the factor's *job* or a coincidence is **FORK-4**, re-posed.

**What the honest options are.** (i) The factor is a genuine shell-mode correction and the
$\ell$-wavelengths-around-the-circumference picture (hence $Q=\ell$) must be replaced by shell dispersion.
(ii) The factor is a placeholder for a computed graded eigenvalue and should be **retired** rather than
justified (upstream Q5 already reaches this conclusion from a different direction: a *fit* would have
picked exponent $0.355$, not $0.5$). (iii) The factor belongs to the frequency and not to the geometry,
in which case CF-1's leak-fraction correction $(1+\nu)^{\pm1}$ is live. (iv) **New, and now the leading
reading:** the factor's content is $r_{sat}/r_{eff}$ — the mode's wall-above-cutoff ratio — in which case
it is not a correction to a length at all but a statement about *where the wall is relative to the
mode's own spectrum*, and the derivation must reproduce it rather than assert it.

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
| **E11** | the $(1+\nu_{vac})$ factor | **wall-above-cutoff ratio** $r_{sat}/r_{eff}$ on the $\ell$-th spherical mode ($k r_{eff}=\ell$ ⇒ $k r_{sat} = 2.571$) | Poisson transverse coupling | `regime-eigenvalue-method.md:16,52` | **MAPS CLEANLY (corrected 2026-07-31, F1).** The earlier "$VF>1$, no clean mapping" reading is **retracted** — a spherical multipole's azimuthal $v_\varphi$ exceeds $c_0$ above cutoff by definition. What is open is whether the ratio is *derived* or coincidental (**FORK-4**) |
| **E12** | $\rho_{eff} = \rho_0/S^3$ (topological halting) | would be a **series $L$ diverging at the wall** $\Rightarrow Z\to\infty \Rightarrow$ **open** termination | infalling-matter inertia | `interior-singularity-resolution.md:19` | ⚠ **CONFLICTS with E1/E5.** Failure-mode probe / CF-7 |
| **E13** | the predicted echo | **multiple reflection between E5 and the partially-reflecting taper E6** | — | `vol3/claim-quality.md:123` | clean; delay $= 2\int_{r_{sat}}^{r^\star} dr/c_{shear}$ (CF-9) |
| **E14** | spin $a_*$ / frame dragging $\Omega$ | **a non-reciprocal (gyrotropic) bias on the ring — a ferrite-circulator loading**, splitting CW from CCW | Cosserat micro-rotation bias | `frame-dragging-impedance-convolution.md:15`; the Park/FOC reading at `kerr-q-correction.md:49-61` | ⚠ **PARTIAL** — the corpus models it as a **frequency offset** $\omega\to\omega-m\Omega$ (a rotating-frame Doppler), which is **not the same EE object** as a circulator's nonreciprocal mode split. Both are legitimate EE devices; they make different $Q$ predictions. **FLAG** |
| **E15** | radial overtone index $n$ | **higher-order radial resonances of the tapered line** (they exist automatically) | **Op6 radial phase-matching**, $\int k\,dr + \phi_\Gamma = n_r\pi$ | `radial-eigenvalue-solver.md:160`; `de-broglie-standing-wave.md:226`; `operators.md:189` | **CORRECTED 2026-07-31 (F2).** The earlier "NO CORPUS OBJECT AT ALL" is **false** — canon owns $n_r$ via Op6. The true gap is narrower: **the BH-ringdown chain does not instantiate it** (and `vol3/claim-quality.md:205` already scopes the claim to the fundamental mode). Probe / chain-coverage gap |

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
5. **~~$VF > 1$ is impossible~~ — RETRACTED 2026-07-31 (F1).** The original entry read: *"Elasticity
   happily writes a Poisson factor; a transmission line refuses to propagate faster than $1/\sqrt{LC}$."*
   That is a **uniform-TEM** statement misapplied to a spherical multipole's azimuthal phase velocity,
   which exceeds $c_0$ above cutoff by definition — and canon's own SYM/ASYM branches carry
   $c_{EM}\to\infty$ (`manuscript/ave-kb/claim-quality.md:111-112`). **What the circuit picture actually
   makes obvious here is the replacement:** $(1+\nu_{vac}) = r_{sat}/r_{eff} = k r_{sat}/\ell$ is a
   **wall-above-cutoff ratio**, a spectral statement the elastic "Poisson correction" language hides.
   See the superseded CF-4.
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

Per `ave-ee-first-mapping` §"Failure-mode probes" — honest list, **three** entries after the 2026-07-31
repair pass (P1 was withdrawn; it is retained in the table so the count is auditable):

| probe | element | why it fails to map | what it would take |
|---|---|---|---|
| ~~**P1**~~ | ~~**E11** — $(1+\nu_{vac})$ as $VF = 1.286 > 1$~~ | 🔴 **WITHDRAWN 2026-07-31 (F1).** Original: *"passive lines cannot exceed $1/\sqrt{LC}$; the factor is not a line property"* — a uniform-TEM statement misapplied to a multipole's azimuthal phase velocity. **E11 maps cleanly** as $r_{sat}/r_{eff}$ | not a mapping failure; the open item is **FORK-4** (is the cutoff-to-wall ratio derived or coincidental?) |
| **P2** | **E12** — $\rho_{eff} = \rho_0/S^3$ | it is a *matter* inertia, not a line inertia; if it were the line's, the termination flips short→open | canon must say which $\rho$ enters $Z_{shear}=\rho c_{shear}$ (CF-7 / FORK-3) |
| **P3** | **E14** — spin as Doppler-offset vs circulator-bias | a rotating-frame frequency shift and a gyrotropic nonreciprocity are different devices with different loaded-$Q$ structure | decide whether $\Omega$ is a kinematic frame rate or a material bias (upstream Q4, now with an EE-sharp form) |
| **P4** | **E15** — radial overtone $n$ | **CORRECTED 2026-07-31 (F2).** Not a mapping failure and **not a corpus-vocabulary gap** — the original *"AVE has no name for it"* is false; canon owns $n_r$ (Op6, `operators.md:189`). The gap is **chain coverage**: the BH-ringdown chain never writes a radial phase integral | apply Op6's own phase-matching condition to the graded shear cavity — **FORK-9**, re-posed |

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

## PART 3 — THE LATTICE WALK (sit inside the cell)

*Convention, stated once: force ↔ voltage, velocity ↔ current, so $Z = F/v$, inertia is $L$ and bond
compliance is $C$. A vanishing $Z$ is a **free surface** — zero force, maximum motion. All numbers below
are $S(A)$ evaluated at $A = 7M_g/r$; arithmetic on canonical inputs, IDENTITY class, not claims.*

**Hop 0 — you are the node sitting exactly on the wall, $r = 7\,M_g$, $A = 1$.**
Your four K4 bonds are at yield. The shear stiffness holding you sideways is **exactly zero**
($G/G_0 = S = 0$). Push you tangentially and nothing pushes back. You are a free surface: **force node,
motion antinode.** A shear wave arriving from outside cannot get past you — not because something blocks
it, but because there is nothing on the far side to push against. It turns around, and its force wave
comes back inverted. That is $\Gamma_{shear} = -1$, and **you have taken no energy from it.** Whatever
makes the ringdown die, it is not you.
> ⇢ **FORK-3 bites here.** If the frozen infalling matter's $\rho_{eff} = \rho_0/S^3$ is *your* inertia
> rather than a separate substance sitting on you, you are not a free surface at all — you are
> infinitely heavy, $Z\to\infty$, a **clamped** surface: motion node, force antinode. Same $\lvert\Gamma\rvert$,
> opposite phase, and the whole standing-wave pattern outside you shifts by a quarter wavelength.

**Hop 1 — one node out, $r/r_{sat} = 1.01$.**
$A = 0.990$, $S = 0.140$: your bond is now $14\%$ as stiff as cold vacuum and the shear speed here is
$0.375\,c_0$. Crossing this one hop takes $2.7\times$ longer than it would in flat space. Impedance
$Z/Z_{sh,0} = 0.375$. The wave has just gone from $Z = 0$ to $Z = 0.375$ in a single node: **the ramp is
steepest right at the wall**, which is exactly where a taper reflects hardest.

**Hops 2–10 — climbing the ramp.**

| $r/r_{sat}$ | $r$ [$M_g$] | $A$ | $G/G_0 = S$ | $c_{shear}/c_0 = \sqrt S$ | $Z/Z_{sh,0}$ |
|---|---|---|---|---|---|
| 1.00 | 7.00 | 1.000 | 0.000 | 0.000 | 0.000 |
| 1.01 | 7.07 | 0.990 | 0.140 | 0.375 | 0.375 |
| 1.10 | 7.70 | 0.909 | 0.417 | 0.645 | 0.645 |
| 1.22 | 8.57 | 0.816 | 0.577 | 0.760 | 0.760 |
| 1.50 | 10.50 | 0.667 | 0.745 | 0.863 | 0.863 |
| 2.00 | 14.00 | 0.500 | 0.866 | 0.931 | 0.931 |
| 3.00 | 21.00 | 0.333 | 0.943 | 0.971 | 0.971 |
| 5.00 | 35.00 | 0.200 | 0.980 | 0.990 | 0.990 |

Each hop outward, the DC radial strain $\varepsilon_{11} = 7M_g/r$ relaxes, the Ax-4 kernel $S$ recovers,
and your neighbour's bond is a little stiffer than yours. **Every hop is therefore a small impedance
step, and every step throws a little of the wave back inward.** The ringdown's decay is the sum of what
*doesn't* get thrown back. Note where the work happens: by $r = 2r_{sat}$ the ramp is $93\%$ done, by
$5r_{sat}$ it is flat. **The entire horn is between $7$ and $\sim15\,M_g$ — about half a wavelength.**
> ⇢ **FORK-2 (A5) bites on the whole column.** These are $\sqrt S$ numbers. Under $S^{1/4}$ every
> $c/c_0$ and $Z/Z_0$ entry moves toward $1$ (the ramp gets *shallower*, the horn gets *gentler*, the
> reflection *smaller*, $Q$ *lower*). The column is the $Q$ integrand; the exponent is not a footnote.

**Hop ~11, $r \approx 8.6\,M_g$ — the turning point.**
Here $\ell(\ell+1)c_{shear}^2/r^2$ peaks. Two effects race: going outward the medium gets *faster*
(helping the wave escape) but the centrifugal $\ell(\ell+1)/r^2$ term falls (letting it escape too). The
stationary point of their product is the substrate's own barrier crest — the object GR calls the
light-ring barrier, sitting here at $1.22\,r_{sat}$ rather than at $r_{ph} = 3\,M_g$, which is buried
$5.6\,M_g$ behind your back inside the melt.
> ⇢ **FORK-6 bites here.** If the echo has a second mirror, this is it — **not** the light ring. The
> round trip is $\sim3\,M_g$ of very slow medium, not $\sim10\,M_g$ of fast medium.

**Hops 12 → ∞ — out into the cold.**
Past $\sim3r_{sat}$ every hop is like the last: $Z$ flat at $\rho_0c_0$, $c$ flat at $c_0$. This is
Regime I, a matched line, a legal radiating port. Energy that reaches here **never comes back**. This —
and only this — is the loss in the $Q$ ledger.

**Now run one full cycle of the bell.**
Two wavelengths wrapped around the rim; the mode's electrical size is $ka = \ell = 2$ **exactly**
(CF-8). Per radian of phase, the fraction of stored energy that makes it out past hop ~12 is what the
corpus writes as $1/\ell$ and never computes. In the walk you can see what that number is made of:
(i) how much reactive energy is stored in the sloshing near the rim, (ii) how much gets past the
steepest part of the ramp at hops 1–3, (iii) how much of *that* survives the turning point at hop 11.
**Three factors, all computable from the column above, and the corpus replaces all three with the
word "scales as".**
> ⇢ **FORK-1 and FORK-4 bite on "the mode".** Where is it actually sloshing? Under the *literal* reading
> the frequency comes from a circle at $5.44\,M_g$ — a radius you would have to walk *inward* past the
> wall to reach, through hops where shear does not exist — while the leak comes from a circle at
> $7\,M_g$, where you are standing and where the shear speed is zero.
> **Corrected 2026-07-31 (F1):** under the *multipole* reading those are not two circles at all.
> $5.44\,M_g$ is the $\ell=2$ mode's **cutoff radius** — a spectral marker, not a place you can stand —
> and $7\,M_g$ is where you *are*, at $k r = 2.571$, i.e. $9/7$ **above** that cutoff. The mode is
> above cutoff here and therefore radiating, which is exactly why $Q$ is $O(1)$. The live question is
> no longer "which circle" but **"is the wall's position relative to the cutoff derived or assumed?"**

**The one-sentence version for the walk.**
> You are standing on a free surface at the bottom of a stiffness ramp that climbs to full vacuum
> stiffness over about half a wavelength. The bell is not the wall — the wall just refuses to absorb.
> The bell is the ramp, and $Q$ is asking how leaky a half-wavelength horn is when the thing radiating
> into it is exactly at its own cutoff.

---

## §4 — THE FORK MENU FOR GRANT

One plumber question per open fork. **Nothing below is asked rhetorically — each answer changes what the
derivation lane computes.**

| # | Fork | The plumber question | Options |
|---|---|---|---|
| **FORK-1** | **A1 — where does the bell live?** | *Is this a bell (mass at a radius) or a horn (a taper that resonates)?* | (a) a ring at the rim $r_{sat}$; (b) a distributed mode of the graded shell, radius = solver **output**; (c) an interface/Scholte mode on the wall — **already excluded**, it wouldn't ring down (CF-10); (d) a curvature-leaking whispering-gallery mode = (b) evaluated at its own turning point |
| **FORK-2** | **A5 — the $S$-exponent, reclassified** | *At the wall, does the vacuum go **soft** (compliant, $C\to\infty$, short) or **stiff-and-opaque** ($Z\to\infty$, open)? You can't have both in one channel.* | (a) ratify the three-branch $(L,C)$ table (§CF-5) ⇒ shear pinned at $\sqrt S$, $S^{1/4}$ is an ASYM/EM artifact; (b) reject the channel assignment and keep $S^{1/4}$ live in the shear integrand; (c) KEEP-BOTH and make the derivation report both |
| **FORK-3** | **CF-7 — which $\rho$?** | *Is the frozen infalling matter part of the pipe wall, or is it the water in the pipe?* | (a) $\rho_0$, cold lattice inertia ⇒ free surface, $\Gamma=-1$; (b) $\rho_{eff}=\rho_0/S^3$ ⇒ clamped surface, $\Gamma=+1$, taper reverses; (c) two different substances, and canon must say so at `vol3/claim-quality.md:122` |
| **FORK-4** *(re-posed 2026-07-31, F1)* | **A6/CF-1 — the two radii** | *The standing chain puts the physical wall exactly $9/7$ above the mode's own cutoff radius ($k r_{eff} = \ell$, $k r_{sat} = \ell(1+\nu) = 2.571$). **Is that the $(1+\nu)$ factor's actual job** — the wall-to-cutoff ratio — or is the coincidence accidental?* | (a) **yes, that is its job** — then the derivation must *produce* $9/7$ from the graded profile, not assert it, and $Q$ must be evaluated at $ka = 2.571$ (where $Q$ is $\sim2\times$ smaller than at cutoff); (b) coincidence — the factor is a shell-membrane correction and the wall/cutoff coincidence is unexplained; (c) retire $(1+\nu)$ and let a graded solve output both radii. **Superseded option:** the original menu's *"then explain $VF>1$"* is withdrawn — there is nothing to explain (CF-4) |
| **FORK-5** | **CF-15 — disposal** | *A hair off the wall the mirror isn't perfect and some shear crosses. Shear can't propagate in there. Where does it go?* | (a) mode-converts to bulk/A1 at the interface (a **second** loss channel ⇒ Op21's single-channel classification breaks); (b) reflects off the compact shell (a delay, not a loss ⇒ feeds the echo); (c) absorbed (needs a bulk $\mathrm{Re}\{Z\}$ ⇒ Ax-3 violation unless port-licensed) |
| **FORK-6** | **A9/CF-9 — which echo cavity?** | *Where's the second mirror?* | (a) the graded turning point at $\approx7.8$–$8.6\,M_g$ (this doc's reading — a **short** delay through **slow** medium); (b) the light ring at $r_{ph}$ — but it is buried inside the wall (CF-9); (c) no second mirror, the taper is adiabatic and there is no echo |
| **FORK-7** | **A2/CF-12 — vessel anisotropy** | *Is the wall a pressure vessel? Hoop bonds tight, radial bonds slack — does the rim ring in two different notes?* | (a) yes, R6 transplants to the BH wall ⇒ split rim modes + mode conversion ⇒ $Q^{-1}$ is a sum; (b) no, R6 is core-local and does not transplant; (c) untested — make it a gate in the derivation pre-reg |
| **FORK-8** | **E14 — what kind of device is spin?** | *Is frame dragging a Doppler shift (the whole ring moving past you) or a magnetic bias on a circulator (CW and CCW seeing different media)?* | (a) Doppler / Park rotating frame — the standing $\omega\to\omega-m\Omega$; (b) gyrotropic bias — nonreciprocal, **different loaded $Q$ per sense**, a prediction the standing law does not make; (c) both, at different orders |
| **FORK-9** *(re-posed 2026-07-31, F2)* | **A3/E15 — overtones** | *Canon already owns the radial-overtone object — $n_r$, via Op6's phase-matching condition $\int k\,dr + \phi_\Gamma = n_r\pi$, written for the atomic cavity. **Does that condition apply to a graded shear cavity with a $\Gamma = -1$ inner wall?** A horn has more than one resonance; does this one, and does Op6 already tell us its ladder?* | (a) **yes — fire Op6 on the graded shear profile** with $\phi_\Gamma = \pi$ at the wall (or $0$, per A8's sign degeneracy) and read off the $n_r$ ladder; then AVE has a GR-comparable overtone spectrum for free; (b) no — Op6 is scoped to the Coulomb/atomic $Z$-profile and the shear cavity needs its own condition; (c) leave as a declared chain-coverage gap. **Superseded option:** the original menu's *"(a) derive the radial ladder (then AVE has an $n$ index)"* is withdrawn — **AVE already has the index** |
| **FORK-10** | **A7/CF-14 — which $Q$ object?** | *Are we measuring how lossy the port is, or where the pole sits? For a taper those aren't the same number.* | (a) port-$Q$ ($X/R$ at the rim); (b) pole-$Q$ (complex-frequency eigenvalue of the graded problem, directly comparable to the frozen C-$\tau$ comparator); (c) compute both and report the gap as a diagnostic |

**And the one scope question that gates the rest** (upstream Q8, unchanged and still unanswered): **is
the B1-ratified cold $Q = \ell$ anchor in scope?** Everything in this document says the tension lives
there (upstream F8: $88\%$ of the deficit is present at zero spin). If the anchor is out of scope, the
derivation lane can still run — but its reachable outcome is a *cold-broken, catalog-matching*
inconsistency, which is a sharper falsifier than the present uniform offset, not a resolution.

---

## Appendix A — Step-0 skill-selection plan + retro-pass

Written as a 60-second plan before PART 1; retro-checked before push, per the standing
pre-workstream skill-selection discipline.

| skill / discipline | planned | fired? | where it bit |
|---|---|---|---|
| **`ave-ee-first-mapping`** (mandatory — the mapping IS the deliverable) | YES | **YES, and it was the whole lane** | Step 2 lookup put $\Gamma=-1$ on the **short/open two-branch** row (`translation-circuit.md:119`), which forced the $(L,C)$ question, which produced **CF-5/CF-6** — the reclassification of the standing $\sqrt S$-vs-$S^{1/4}$ flag from an exponent fork to a channel fork. Trigger 7 (IDENTITY-COLLAPSE) fired unplanned and produced **CF-8** ($ka \equiv \ell$). Step 6 (land new rows) was **deliberately NOT executed** — §2.7. |
| **`substrate-native-check`** | YES | YES, partial-by-design | No solver is scaffolded, so the full walk defers to the derivation lane. What *was* done: the §0 sector/regime/phase-state header; the K4 bond/node identification behind E1/E2; and the **sector-ownership** pass that produced A2's "A1 = DC bias, T2 = AC signal, any admixture lands at $2\omega$" statement. |
| **`pre-test-physics-check`** | YES | YES → the entire §4 fork menu | Every fork is asked **before** design, in plumber form, per the Rule-16 strengthening. FORK-1 is upstream Q1 sharpened by CF-1/2/3; FORK-2/3/5/6/8/9/10 are **new** and were not askable before the circuit mapping existed. |
| **`phase-space-coordinate-check` (A46)** | YES | YES, and it caught something | Cheap pass on the eigenvalue register (matched, §0 COORDS). **But it bit on the second register**: PART 2 works in the impedance plane, and port-$Q$ ≡ pole-$Q$ only for an isolated pole. That is **CF-14**, a real pre-reg item, not a formality. |
| **`verify-before-cite`** | YES | YES, on every quote — **two-method, and the second method changed an answer** | Battery in Appendix B. It bit twice: (i) the SYM/ASYM lines are in `manuscript/ave-kb/claim-quality.md`, **not** `common/claim-quality.md` — a first-draft path error caught by a file-variant re-check; (ii) grepping for the *engine's* view of the impedance conflict surfaced the verbatim `cosserat_field_3d.py` FLAG comment, which is a stronger receipt than any leaf. |
| **`consistency-vs-emergence`** | YES | YES, per-number | Every number in this document is tagged inline: **IDENTITY** ($ka=\ell$; $0.41\lambda$; the hop table) or **arithmetic-consistency observation on canonical inputs** ($r^\star \approx 8.573\,M_g$). The upstream $\nu_{vac}$ class ceiling is inherited unchanged and restated in §0. **No emergence-class language appears anywhere.** |
| **`pure-AVE-corpus`** | YES | YES, standing | No external, non-physics context in this document, its commits, its branch name, or the docket fragment. |
| **flag-don't-fix** (durable directive) | YES | YES, 16 times | CF-1…CF-16 are surfaced with paths + verbatim content and **zero corpus files modified**. CF-5 is the hard case — the analysis points to an answer, and the answer is **routed for ratification, not applied**. |
| **Rule 11 / honest closure** | YES | Structurally | CF-10 **closes** a candidate (a Scholte mode cannot ring down) rather than keeping it alive for optionality. CF-9 **kills the geometry** of an upstream route (R3) rather than re-scoping it silently — it is re-scoped explicitly and the reason is named. |
| **lane discipline (Rule 15)** | YES | YES | Framing lane: no derivation, no solver, no claim, no pre-reg, no `COLLABORATION_NOTES`, no manuscript edit, no `translation-circuit.md` row. CF-1…CF-16 go to the **auditor** lane; FORK-1…FORK-10 go to **Grant**. |

**Retro-pass — applied-set drift (three, all corpus-forced):**

1. **`ave-cavity-class-identification` fired by analogy and was not planned.** The skill is scoped to
   AVE-Neurology applied phenomena, but its *discipline* — "name the cavity class before asserting a
   shared operator mechanism" — is exactly A1. Op21 claims BH ringdown and the electron tank share the
   $\Gamma=-1$ mode-counting mechanism; this lane's A1 shows the **BH cavity class itself is
   unidentified** (four candidates, §1.1). Recorded here rather than back-dated.
2. **`ave-ee-first-mapping` trigger 7** was not in the plan (only triggers 1/2/4 were) and produced CF-8,
   the highest-value structural finding.
3. **`ave-mechanism-claims-discipline`** was not planned and became load-bearing at §2.7 — it is the
   reason the two new translation-circuit rows are **not landed**.

**One skill deliberately NOT fired:** `ave-discrimination-check`. Correct at derivation-fire time (does
the landed law discriminate AVE from GR?), not at framing time. Noted rather than silently skipped — the
discrimination candidate to test then is the FORK-6 echo delay, whose *value* this lane has just moved.

---

## Appendix B — verify-before-cite battery (two-method)

Every quoted line was verified by **two independent methods** — a ranged read (`sed`/`Read`) **and** a
pattern grep whose scope differs from the read's — per the `verify-before-cite` two-method rule and the
upstream lane's own lesson that varying only the *file* is not enough.

| # | Cited object | Method 1 | Method 2 | Result |
|---|---|---|---|---|
| 1 | `regime-eigenvalue-method.md:16,47,52,55,58,63` (the five-step chain, $r_{eff}$, $r_{ph}$ inside, "orbits tangentially at $r_{sat}$") | ranged read `:1-40`, `:40-80` | targeted `grep -n` on `Poisson correction\|r_{\mathrm{eff}}\|photon sphere at\|orbits tangentially\|curvature radiation loss` | **CONFIRMED**; line numbers exact |
| 2 | `vol3/claim-quality.md:121,122,123` (channel split; $Z_{shear}=\rho c_{shear}$; echoes predicted) | ranged read `:115-130` | `grep -n "" \| sed -n '120,124p'` (independent numbering path) | **CONFIRMED** |
| 3 | `saturating-modulus-and-backreaction.md:51,52,60` ($A=\varepsilon_{11}$, $S=(1-A^2)^{1/2}$, SHEAR softens) | full-file `Read` | `grep -n 'c_{\text{shear}}\|SHEAR softens\|A=\varepsilon_{11}'` | **CONFIRMED** |
| 4 | `common/operators.md:54` (Op14 $Z_0/\sqrt S$) + Op16 row ($c_{shear}=c_0\sqrt S$) | ranged read `:50-58` | KB-wide `grep` for `Z_0/\sqrt{S}\|Z_0\sqrt{S}` (19 hits across 15 files, all classified) | **CONFIRMED**, and the grep is what exposed the multi-register spread |
| 5 | `manuscript/ave-kb/claim-quality.md:111,112` (SYM / ASYM branches) | ranged read `:110-113` | KB-wide grep for `Z_0/\sqrt{S}` returning this file | **CONFIRMED — and a first-draft path error corrected**: the lines are in `ave-kb/claim-quality.md`, not `ave-kb/common/claim-quality.md` (`grep -n SYMMETRIC` on the latter → **0 hits**) |
| 6 | `nonlinear-vacuum-capacitance.md:14,27` ($C_{eff}=C_0/S$; the A1-vs-T2 sector note) | `grep -n 'C_{eff}\|C_0/S'` | ranged read of the returned lines | **CONFIRMED**; the `:14` sector note is why CF-5's SHEAR row carries an explicit residual |
| 7 | `k4-tlm-lensing-validation.md:22-33` (register correction + the downstream $c_{local}$ flag) | ranged read `:18-45` | KB-wide grep `Z_0/S^` returning `:28,:30` | **CONFIRMED** |
| 8 | `interior-singularity-resolution.md:14-21` ($\rho_{eff}=\rho_0/S_{topo}^3$) | `grep -n 'rho_\|S_{topo}'` | ranged read of returned lines | **CONFIRMED** |
| 9 | `electron-bh-isomorphism.md` ("cannot propagate"; $c_g = c(1-\varepsilon^2)^{1/4}$; two-channel table) | ranged read `:28-50` | independent `find`-located path check | **CONFIRMED** |
| 10 | PR#260 B3-DEGENERATE banner ($Z=Z_0\sqrt S$, $\lvert\Gamma\rvert=1$ both ways) | KB-wide `grep -rn "B3"` | verified the *identical* banner sentence (`grep -rl` on the banner's own wording) at **8** independent leaves, incl. `lattice-extreme-bh-rationality.md:28`, `cvr-reflection-smith.md:27`, `vol4/circuit-theory/ch1-vacuum-circuit-analysis/index.md:37`, `common/dual-reactance-storage-taxonomy.md:189`, `vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md`; a separate #260 *reference* (not the banner) at `chirality-and-antimatter.md:43` | **CONFIRMED**, multi-site |
| 11 | `op14-local-clock-modulation.md:13,19` (the 2026-06-22 exponent correction) | `grep -n 'Matter-clock exponent\|omega_{\text{local}}'` | ranged read `:13-16`, `:8-16` | **CONFIRMED** |
| 12 | `op14-cosmic-horizon-profile.md:22,41,43,47` (the lagging exponent + the self-contradiction) | ranged read `:40,46` | `grep -n 'omega_{\text{local}}\|sqrt{1 - A^2}'` (returns `:22,:43,:47` — three sites, two exponents) | **CONFIRMED** — this is CF-16 |
| 13 | `common/vocabulary-register.md:309` ($\varepsilon_{11}$ IS the Ax-4 amplitude $A$) | `sed -n '309p'` | upstream scoping doc §2.3 quotes the same line independently | **CONFIRMED** |
| 14 | `translation-circuit.md:119` (short-vs-open two-branch row) + §4.7.3 disanalogy (ii) | `sed -n '119p'`, `sed -n '354,362p'` | section-header map via `grep -n '^#'` | **CONFIRMED** |
| 15 | `research/2026-07-21_boundary-strain-amplitude_result.md:13,96` (vessel state R6, hoop-stiffen / radial-soften) | workspace-wide `grep -rln hoop` | `grep -rn 'hoop-stiffen\|radial-soften'` returning `:13,:96,:106,:112` | **CONFIRMED**; scope caveat (core-local, not BH wall) recorded in CF-12 |
| 16 | `src/ave/topological/cosserat_field_3d.py:419-424` — the engine's own impedance-conflict FLAG | ranged read `:418-430` | `grep -n 'Z_eff\|2nd-impedance'` | **CONFIRMED** verbatim: *"⚑ FLAG (2nd-impedance conflict, task #12, NOT resolved here): this OPEN Z=Z0/√S coexists with the live-wall SHORT Z=Z0·√(S_μ/S_ε) in this SAME file, and with operators.md:54 (Z0/√S) vs k4-tlm-lensing-validation.md:22 (Z0/S^{1/4}). The exponent/sign reconciliation across Op14 forms is a separate physics-review item"* |
| 17 | `op21-multi-mode-mode-counting.md` §1 table + §2.2/§2.3/§2.4 ($\Gamma=-1$ forcing, $1/\ell$ leak, $Q=\ell$) | ranged read `:20-110` | cross-check against `theorem-3-1-q-factor.md` "Op21 multi-mode generalization" paragraph (independent leaf, same $1/\ell$ statement) | **CONFIRMED** |
| 18 | `theorem-3-1-q-factor.md` ($Q_{tank}=\omega_C L_e/R$, $R = Z_0/(4\pi)$ radiation impedance) | ranged read `:30-115` | upstream scoping §2.2 cites `:40-42`, `:79-83` independently | **CONFIRMED**; sector caution recorded at E10 |
| 19 | `qnm-quality-factor.md` (Resultbox $Q=\ell$; the B1 ruling banner) | full-file read | `grep` of the B1 banner text in `op21-…` (propagated copy, same wording) | **CONFIRMED** |
| 20 | Currency of the upstream state (#810–#812 merged; scoping doc at its merged content) | `git log --oneline` at `origin/main` = `512e1ef4` | full read of `research/2026-07-30_qlaw-derivation_scoping.md` (928 lines) + its docket fragment | **CONFIRMED**; this document is written against `512e1ef4` |

**Rows 21–28 — added by the 2026-07-31 repair pass (PR #814 audit).** Same two-method rule.

| # | Cited object | Method 1 | Method 2 | Result |
|---|---|---|---|---|
| 21 | `radial-eigenvalue-solver.md:160` ($n_r = n-l-1$; *"This phase-matching condition IS Op6"*) | ranged read `:155-165` | `grep -rn "n_r"` across `manuscript/ave-kb/` filtered to the leaf | **CONFIRMED**; line exact — **this is the receipt that falsifies the original "no AVE object" claim (F2)** |
| 22 | `de-broglie-standing-wave.md:226` (Radial \| $n_r$ \| Radial quantum number) | ranged read `:222-230` | same KB-wide `n_r` grep, independent path | **CONFIRMED** |
| 23 | `operators.md:189` (*"Op6 (eigenvalue target → radial nodes $n_r$)"*) | ranged read `:186-192` | same KB-wide `n_r` grep | **CONFIRMED** |
| 24 | `vol3/claim-quality.md:205` (*"the claim is the fundamental mode, not the full QNM spectrum"*) | ranged read `:200-210` | — | **CONFIRMED**; canon already scopes the QNM claim, which is why F2's corrected form is the narrow one |
| 25 | `knot-mode-isomorphism.md:22` + `common/solver-toolchain.md:440` (*"$\ell = 3$ (1st GW overtone)"*) | ranged read `:18-26` / `:436-444` | independent `find`-located paths, identical row text in both leaves | **CONFIRMED — and it is a corpus ERROR** ($\ell$ is angular, $n$ is the overtone index). **Routed, not repaired** (F2) |
| 26 | `manuscript/ave-kb/claim-quality.md:111-112` (SYM/ASYM **superluminal phase velocities**) | ranged read `:108-114` | the existing row-5 KB-wide grep | **CONFIRMED**; *"$c_{EM,sym} = c_0/S \to \infty$ (EM phase velocity rises)"* — the receipt that retracts CF-4 (F1) |
| 27 | `interior-singularity-resolution.md:14`, `:23` (**scope** of $\rho_{eff}$: *"collapsing matter"* / *"infalling matter"*) | ranged read `:12-26` | the existing row-8 grep | **CONFIRMED**; both sites scope to matter, not to the lattice's shear inertia (F7) |
| 28 | `k4-tlm-lensing-validation.md:22` now reads $Z_0/\sqrt S$; `:25-29` is the 2026-07-14 KEEP-BOTH correction banner | ranged read `:18-36` | `grep -n "Register correction\|Downstream flag"` | **CONFIRMED — and it makes the engine FLAG's third clause STALE** (F4) |

**Numerical receipts added by the repair pass** (all re-run in this lane, stated with their estimator):

| quantity | value | method |
|---|---|---|
| $Q_Z(\ell{=}2)$ at $ka = 2 / 2.4495 / 2.5714$ | $1.863 / 0.973 / 0.839$ | Yaghjian–Best $Q_Z = \tfrac{1}{2R}\sqrt{(xR')^2+(xX'+\lvert X\rvert)^2}$ on $Z_\ell/\eta = j\hat H_\ell'/\hat H_\ell$ |
| exact Chu / Collin–Rothschild $Q$, same three points | $2.812 / 1.837 / 1.679$ | stored-energy integral; **validated to 4 digits** against $1/x+1/x^3$ ($\ell{=}1$) and $3/x+6/x^3+18/x^5$ ($\ell{=}2$) |
| $Q_Z$ ladder at $ka = \ell$, $\ell = 1,2,3,4,10$ | $1.581 / 1.863 / 2.117 / 2.352 / 3.534$ | as above |
| exact CR ladder at $ka = \ell$, $\ell = 1,2,3,4,10$ | $2.000 / 2.812 / 3.641 / 4.482 / 9.657$ | as above — **linear in $\ell$, slope $\approx0.86$** |

**Numerical receipts** (all computed inline, all from canonical inputs only, all IDENTITY or
arithmetic-consistency class — **no engine run, no solver, no fitted parameter**):

| quantity | value | inputs |
|---|---|---|
| $k\,r_{eff} = (\omega_R/c)\,r_{eff}$ | $\mathbf{2.000} = \ell$ **exactly** | $\omega_R M_g = 18/49$, $r_{eff}=49M_g/9$ |
| $\lambda_\infty = 2\pi c/\omega_R$ | $17.10\,M_g$ | $\omega_R M_g = 18/49$ |
| taper length / $\lambda$ | $\approx 0.41$ | grade scale $\sim r_{sat}=7M_g$ |
| $k\,r_{sat} = \ell(1+\nu_{vac})$ (wall's electrical size) | $\mathbf{2.571}$ | $\omega_R M_g = 18/49$, $r_{sat}=7M_g$ |
| $v_\varphi(r_{sat}) = \omega_R r_{sat}/\ell$ | $1.286\,c_0 = (1+\nu_{vac})c_0$ — **above-cutoff phase velocity, not a defect** (CF-4 retracted 2026-07-31) | $\omega_R$, $r_{sat}$, $\ell$ |
| $v_\varphi(r_{eff}) = \omega_R r_{eff}/\ell$ | $c_0$ **exactly** — the cutoff condition, third re-expression | $\omega_R$, $r_{eff}$, $\ell$ |
| turning point, canonical $c\propto\sqrt S$ | $A^2 = 2/3$, $r^\star = 8.573\,M_g$ | $A = 7M_g/r$, $V\propto c_{shear}^2/r^2$ |
| turning point, Family-E $c\propto S^{1/4}$ | $A^2 = 4/5$, $r^\star = 7.826\,M_g$ | same, exponent varied |
| $c_{shear}(r^\star)/c_0$ | $0.760$ | canonical exponent |
| hop table $G/G_0$, $c/c_0$, $Z/Z_0$ | §3 | $S = \sqrt{1-(7M_g/r)^2}$ |

**What was NOT verified, stated so it is not mistaken for verified:** the Chu / Collin–Rothschild
external-$Q$ value at $ka=\ell=2$ was **not computed** (that is the derivation). The vessel-state R6
transplant to the BH wall was **not tested**. The $\nu_{vac}\to0$ cancellation sensitivity of any
candidate ratio was **not run** — it remains a pre-reg requirement per upstream §2.1.

---
