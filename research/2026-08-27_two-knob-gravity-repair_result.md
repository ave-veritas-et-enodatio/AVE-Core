# RESULT — the two-knob gravity repair: GR at $O(m)$ from wave mechanics, and the SN1987A falsifier on the scalar-index construction

**Date:** 2026-08-27 · **Branch:** `research/2026-08-27-two-knob-gravity-repair` · **Base:** `origin/main` @ `a3f4fef7`
**Lane:** implementer. Consolidates a four-lane derive workflow (`L1-group-vs-phase`, `L2-preferred-frame`, `L3-constitutive-map`, reconciliation) whose complete returns were read from the workflow journal, not from a summary.
**Concurrent lane, do not conflict:** `research/2026-08-27-ppn-tensor-derivation` documents the prior $F = 1/6$ result. **This document confirms that lane's arithmetic and supersedes its OUTLOOK.**
**Artifacts:** driver [`research/drivers/two_knob_gravity_repro.py`](drivers/two_knob_gravity_repro.py) · record [`research/drivers/two_knob_gravity_repro_results.json`](drivers/two_knob_gravity_repro_results.json)

---

## §0 — VERDICT

> # The perihelion defect is real, it is a **slot-swap**, and the repair is arithmetically clean.
>
> ### But nothing in the axioms forces the repair. **This is a repaired CONSISTENCY CHECK, not a derivation.** Read the box below before quoting anything above it.

Posed as wave mechanics on a graded lossless medium — **no metric anywhere in the chain** — the closed-orbit precession of a bound packet is set by exactly **three grading exponents of two independent constitutive functions**: the local characteristic speed $c_{\rm eff}(r) = c(1 - a_1 U + a_2 U^2)$ and the local internal rest frequency $\Omega(r) = \Omega_\infty(1 - b_1 U + b_2 U^2)$, with $U \equiv GM/c^2 r$:

$$\Delta\phi \;=\; \frac{\pi GM}{c^2 \ell_p}\left(4a_1 - b_1 - \frac{2b_2}{b_1}\right) \qquad\text{(non-relativistic limit)}$$

Canon's matter channel feeds **one** number into **both** slots. `ponderomotive-equivalence.md`:14 sets $n_{scalar}(r) = 1 + \epsilon_{11}(r)/7 = 1 + GM/c^2r$ (the **speed** slot) and `:19` then writes $U_{wave} = m_i c^2/n_{scalar}$ (the **clock** slot) — one symbol, two slots, one value. The Gordon construction at `gordon-optical-metric.md`:17 makes that wiring an **identity**: a scalar index gives $g_{00} = -1/n^2$, $g_{ij} = \delta_{ij}$ exactly, so $\Omega = \Omega_\infty/n$ **and** $c_{\rm eff} = c/n$, hence $a_1 = b_1$ and $b_2 = a_1^2$ are *forced* and the bracket collapses to the bare index slope. For $n = 1+U$ that is $1$, not $6$: **$F = 1/6$**, Mercury $7.163446''$/century against $42.98\pm0.04$ — **$-895\sigma$**.

Setting $(a_1, b_1, b_2) = (2, 1, \tfrac12)$ — the matter packet riding **light's own** $c_{\rm eff}(r)$, with an independently and **multiplicatively** graded clock — returns Mercury $42.980676''$/century ($+0.017\sigma$), Hulse–Taylor $4.2265976^\circ$/yr (measured $4.226585(4)$), solar limb $1.75119''$ (measured $1.7509$), $\gamma = 1$, $\beta = 1$. That is GR at $O(m)$.

### ⚠ THE CAVEAT, stated at the same volume as the fix

**$(2,1,\tfrac12)$ currently WORKS. Nothing yet FORCES it.** The difference between a derivation and a fit is exactly whether the constitutive map compels those exponents, and lane L3 was charged with that question. **It found that the map does not exist** — canon's only bias$\to$index object is Op19 (`operators.md`:59, status CANONICAL), whose licensed coefficient $\nu_{vac}$ is *"a kinematic ratio (transverse strain per longitudinal strain), not a modulus"* (2026-08-11 linearity audit), i.e. a strain-per-strain ratio being used as a strain-per-**index** ratio. The object that performs that conversion in any real medium is the rank-4 photoelastic tensor $p_{ijkl}$, which this corpus has never named, derived, measured or bounded (F-B4, `research/2026-07-31_anisotropy-observable_scoping.md`:657). L3's own finding, restated in its own labels: with $\gamma_\parallel = 1 + P\,U$, $\gamma_\perp = 1 + Q\,U$, deflection fixes $Q = 2$ and the Newtonian limit fixes one combination of $(P, Q, f)$ — **three unknowns, two measurements, so a one-parameter family survives.** $Q = 2$ is neither forced, nor forced elsewhere, nor simply free. And $b_2 = \tfrac12$ is a **third** number that L3's ledger does not reach at all: it follows if the clock grades multiplicatively ($\Omega = \Omega_\infty e^{-U}$) and from nothing else yet written.

**So the honest class of this result is:** the $F=1/6$ diagnosis is **DERIVED** and is a genuine internal defect; the repair is a **CONSISTENCY-class recalibration** that spends AVE's two already-imported numbers ($a_1 = 2$ from the GR-imported $\nu_{vac}\cdot 7$ chain; $b_1 = 1$ from Newton) plus one **ASSERTED** number ($b_2 = \tfrac12$). It mints nothing, moves no solidity, and is not an emergence claim.

### ⚠ AND ONE RESULT DOES NOT DEPEND ON ANY OF THAT

Because the gap drops out of $\omega^2 = c_{\rm eff}^2 k^2 + \Omega^2$ as $\omega \gg \Omega$, a fast massive packet **must** asymptote to its own channel's massless ray. I derived the deflection in closed form from the same ray equations:

$$\frac{\alpha\, b}{GM/c^2} \;=\; 2a_1 + 2b_1\!\left(\frac{1}{\beta^2} - 1\right) \;\xrightarrow[\beta\to1]{}\; 2a_1$$

Canon's matter channel has $a_1 = 1$; its light channel has $a_1 = 2$. **So an ultrarelativistic massive packet deflects at exactly HALF the photon value, forever** — $2.000400$ vs $4.000400$ (GR) in units $GM/bc^2$ at $v = 0.9999c$. This depends on $a_1$ alone: not on $b_2$, not on the repair, not on the photoelastic map. It is the sharpest single statement in this document, and it is already excluded by SN1987A (§5).

**Two lanes' verdicts I am NOT folding into this headline, because at least one of them outranks it:** L2 established that the medium carries at least two characteristic cones and therefore has **no boost generator in its invariance group**, and that canon cannot presently compute the PPN preferred-frame parameters $\alpha_1, \alpha_2, \alpha_3$ that measure the cost of that (§8). That is a foundational gap; the perihelion defect is a repairable wiring error.


## §1 — SECTOR HEADER

**MODE** — analytic derivation + high-precision quadrature. No engine driver, no lattice solve, no new constant.

**SECTOR / CHANNELS** — two propagating channels of one medium, read against one static source:
- **T2 transverse shear-EM** (the photon), gapless, `port-register.md`:47.
- **the gapped branch** on which a bound soliton sits, `port-register.md`:50 ($\omega^2 = c_\kappa^2 k^2 + m_\omega^2$). The gap is **not** a lattice nuisance: `src/ave/core/constants.py`:293 defines $\ell_{node} \equiv \hbar/(m_e c)$ and `:305` gives $\omega_C = c/\ell_{node}$ with $\hbar\,\omega_C = m_e c^2$, so the Cosserat gap and the electron rest frequency are the **same scale by construction**.

**SOURCE** — the A1-dilatation bias $\varepsilon_{11}(r) = 7GM/c^2 r$, radially graded around a static spherically-symmetric deposit. **IMPORTED** (§7, I1–I3).

**REGIME / PHASE-STATE** — crystalline, **cold**, sub-yield, **lossless-reactive** ($C$, $L$, $S$ all real; no $R$, no $G$), small-signal, static grading. $S \to 1$; Op14 saturation is **not** engaged — $\varepsilon_{11} = 1.79\times10^{-7}$ at Mercury's orbit and $1.486\times10^{-5}$ at the solar limb.

**CROSS-WIRING CHECK (A1 $\perp$ T2 ownership).** Nothing here couples the A1 dilatation channel to charge, spin, or the Cosserat $(2,3)$ winding. The A1 sector appears **only** as the source of the static bias; the two things being graded are a **propagation speed** and a **rest frequency**, both read by probes, neither of which is a charge or a mass assignment. The one place this document touches mass is $\Omega$ = the packet's own internal rest frequency, which is the A1 rest-energy read as a clock — stated, not cross-wired.

**A word on why the wave-mechanical framing is the substrate-native one, not a stylistic choice.** A metric merges the speed slot and the clock slot into $g_{00}$ and $g_{ij}$. A slot-swap is *invisible from inside a metric formulation* — you cannot see that one number is doing two jobs when the formalism has already fused the two jobs. Posing the question as *"what are the grading exponents of $c_{\rm eff}(r)$ and $\Omega(r)$?"* is what makes the defect visible in one line. That is the whole methodological content of this document.


## §2 — The derivation, medium-native, with no metric anywhere

*(placeholder — §2)*

## §3 — The defect: one knob wired to two slots. It is an identity, not an approximation

*(placeholder — §3)*

## §4 — The repair, and the two numbers canon already owns

*(placeholder — §4)*

## §5 — The falsifier that already fired: ultrarelativistic convergence and SN1987A

*(placeholder — §5)*

## §6 — Canon's competing Path-A route: what I verified, and what I do NOT assert

*(placeholder — §6)*

## §7 — The DERIVED / IMPORTED ledger, step by step

*(placeholder — §7)*

## §8 — L2: the preferred-frame state. This outranks the perihelion

*(placeholder — §8)*

## §9 — L3: the constitutive map. Is $(2,1,\tfrac12)$ forced? No

*(placeholder — §9)*

## §10 — THE IMPORT AUDIT — where GR/SM/QED vocabulary did thinking that should have been done in medium terms

*(placeholder — §10)*

## §11 — Lane cite corrections (verify-before-cite)

*(placeholder — §11)*

## §12 — Open items routed

*(placeholder — §12)*

## §13 — Completeness method and its blind spots

*(placeholder — §13)*

## §14 — Skill-selection plan and retro-pass

*(placeholder — §14)*
