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

Every step below carries a **DERIVED** or **IMPORTED** tag. That ledger is the point of the document; the numbers are downstream of it. I re-did the whole chain myself in `sympy` and cross-checked the result with a 60-digit `mpmath` ray quadrature that uses no series expansion at all. Both legs are in [`research/drivers/two_knob_gravity_repro.py`](drivers/two_knob_gravity_repro.py).

### Step 1 — the constitutive start · **DERIVED** (EE-native, lossless-reactive)

A graded lossless LC ladder with a shunt stiffness:

$$\partial_t\!\left[C(\mathbf r)\,\partial_t\psi\right] \;=\; \nabla\!\cdot\!\left[\tfrac{1}{L(\mathbf r)}\nabla\psi\right] - S(\mathbf r)\,\psi$$

$C$, $L$, $S$ real — no $R$, no $G$, no dissipative term anywhere. WKB gives

$$\omega^2 \;=\; c_{\rm eff}^2(\mathbf r)\,k^2 + \Omega^2(\mathbf r), \qquad c_{\rm eff}^2 = \frac{1}{LC}, \qquad \Omega^2 = \frac{S}{C}$$

**Two knobs, and they are genuinely independent in the medium's own terms:** $c_{\rm eff}^2 = 1/(LC)$ is the *product*, while the achromatic-impedance theorem (`achromatic-impedance-matching.md`) pins the *ratio* $L/C \equiv Z_0^2$ — so $Z = Z_0$ constrains $L/C$ and says nothing about $LC$. The gap $\Omega^2 = S/C$ rides the Cosserat micro-rotation stiffness ($m_\omega^2 = 4G_c/I_\omega$, `port-register.md`:50), which no impedance theorem touches. *(Caveat recorded, not buried: the reconciliation lane pushed back on calling these "two independent knobs", on the ground that in a $Z$-matched medium a bound mode is a cavity mode of the **same** graded tensor and its clock is a second projection of one object rather than a free function. Both readings are live; §9 is where that matters.)*

### Step 2 — the ray equations · **DERIVED**

Hamiltonian ray tracing on $H = \omega(\mathbf k,\mathbf r)$: $\dot{\mathbf r} = \partial_{\mathbf k}\omega$, $\dot{\mathbf k} = -\partial_{\mathbf r}\omega$, with $\omega$ conserved (static medium) and the Bouguer invariant $r\,k\sin\psi = \text{const}$. With $u \equiv 1/r$ and $f(u) \equiv \big(\omega^2 - \Omega^2\big)/c_{\rm eff}^2$:

$$\left(\frac{du}{d\phi}\right)^{2} = \frac{f(u)}{p_\phi^{2}} - u^{2} \qquad\Longrightarrow\qquad u'' + u = \frac{f'(u)}{2p_\phi^{2}}$$

Nothing metric enters. This is the eikonal orbit of a wave in a graded medium.

### Step 3 — the precession law · **DERIVED** (reproduced independently this session)

With $c_{\rm eff} = c(1 - a_1U + a_2U^2)$, $\Omega = \Omega_\infty(1 - b_1U + b_2U^2)$, $U = GM/c^2r$, $W \equiv \Omega_\infty^2$, $E \equiv \omega^2 - W$, my `sympy` run returns

$$f'(u)\big|_{u^0} = \frac{2m\,(Ea_1 + Wb_1)}{c^2}, \qquad f'(u)\big|_{u^1} = \frac{2m^2\,\big(3Ea_1^2 - 2Ea_2 + 4Wa_1b_1 - Wb_1^2 - 2Wb_2\big)}{c^2}$$

so $u'' + (1-\varepsilon)u = 1/\ell_p$ and $\Delta\phi = \pi\varepsilon$ gives

$$\boxed{\;\Delta\phi \;=\; \frac{\pi\,\mu\,\big(3Ea_1^{2} - 2Ea_2 + 4Wa_1b_1 - Wb_1^{2} - 2Wb_2\big)}{\ell_p\,\big(Ea_1 + Wb_1\big)}\;}\qquad \mu \equiv \frac{GM}{c^2}$$

$$\text{NR limit } (E\to0):\qquad \Delta\phi \;=\; \frac{\pi GM}{c^{2}\ell_p}\left(4a_1 - b_1 - \frac{2b_2}{b_1}\right)$$

**Both forms match L1's exactly** (`sympy` difference $\equiv 0$, printed in the driver). Two structural facts fall out of the formula and are worth naming because they are counter-intuitive:

- **$a_2$ drops out of the NR precession entirely.** The *second-order speed* grading is unobservable in a slow orbit. So GR's exact isotropic $a_2 = 9/4$ and the exponential repair's $a_2 = 2$ are indistinguishable here — a real difference that shows up only at relativistic speeds.
- **$b_2$ does not drop out.** The *second-order clock* grading is the whole $\beta$ sector.

### Step 4 — the force law · **DERIVED in FORM, calibrated in VALUE**

At low $k$, $\omega \approx \Omega(r)\big(1 + c_{\rm eff}^2k^2/2\Omega^2\big)$, $v_g = c_{\rm eff}^2k/\omega$, $\dot{\mathbf k} = -\nabla\Omega$, so

$$\boxed{\;\mathbf a \;=\; -\,c^{2}\,\nabla \ln \Omega\;}$$

**A body accelerates down the gradient of the logarithm of its own internal rest frequency.** That is Newtonian gravity with no metric, no equivalence principle and no geodesic — and it is the most transferable statement in this result. It is the FORM that makes $b_1$ the Newtonian knob.

**But be precise about what it forces.** Substituting $\Omega = \Omega_\infty(1-b_1U)$ gives $\mathbf a = -b_1\,GM\hat{\mathbf r}/r^2$, so *Newton fixes $b_1 = 1$*. The **form** is derived; the **value** is a calibration to the Newtonian limit. L1 tagged $b_1 = 1$ DERIVED; the reconciliation lane corrected that to *"a fit to Newton"*, and **the reconciliation lane is right**. I carry the corrected tag. This is the framework's standing FORM-derived / VALUE-imported signature, third instance in this document alone.

### Step 5 — cross-check against exact quadrature · **DERIVED** (no series used)

Independent numeric leg: solve for $(\omega^2, p_\phi^2)$ such that the turning points sit exactly at $r_{peri} = 6\times10^6$, $r_{apo} = 10^7$ (units $GM/c^2 = 1$), then integrate the apsidal angle at 60 digits with the endpoint square-root singularities factored out. Result is $\Delta\phi\,\ell_p/(\pi GM/c^2)$:

| grading model | analytic prediction | 60-digit quadrature |
|---|---|---|
| GR, exact isotropic Schwarzschild | 6 | `6.000002763` |
| Gordon scalar $n = 1+U$ (**AVE matter, as canon stands**) | 1 | `0.9999999667` |
| Gordon scalar $n = 1+2U$ (AVE light index) | 2 | `1.999999867` |
| two-knob, exponential clock: $c_{\rm eff} = c\,e^{-2U}$, $\Omega = \Omega_\infty e^{-U}$ | 6 | `6.000003033` |
| two-knob, **additive** clock ($b_2 = 0$) | 7 | `7.000006617` |

The residual $\sim 3\times10^{-6}$ is the finite-orbit $O(GM/c^2r)$ correction, not integration error.

### Step 6 — PPN identity · **DERIVED, and used ONLY as reporting language**

$a_1 = 1+\gamma$, $b_1 = 1$, $b_2 = \beta - \tfrac12$ turns the NR bracket into $4 + 4\gamma - 2\beta$, and $6(2-\beta+2\gamma)/3$ expands to the same thing — `sympy` difference $\equiv 0$. **This is a verification that my ray formula is right, not its foundation.** The whole derivation above ran without it. I record the identity here because it is how a reader outside the program will check the algebra, and because it establishes that the $F = 1/6$ result the concurrent `ppn-tensor-derivation` lane reports is **not a PPN artifact** — the same number falls out of a construction with no metric in it.


## §3 — The defect: one knob wired to two slots. It is an identity, not an approximation

**This is the load-bearing paragraph of the document.**

`gordon-optical-metric.md`:17 writes the construction verbatim:

> $$g_{\mu\nu}^{AVE} = \eta_{\mu\nu} + \left(1 - \frac{1}{n^{2}(r)}\right) u_{\mu} u_{\nu}$$

For a **static** medium, $u^\mu = (1,0,0,0)$, and with $\eta = \mathrm{diag}(-1,1,1,1)$ this gives, **exactly**:

$$g_{00} = -\frac{1}{n^{2}}, \qquad g_{ij} = \delta_{ij}$$

Now project the gapped branch onto it. $g^{\mu\nu}p_\mu p_\nu = -M^2$ with $g^{00} = -n^2$, $g^{ij} = \delta^{ij}$ gives $\omega^2 = (k^2 + M^2)/n^2$, i.e.

$$c_{\rm eff} = \frac{c}{n} \qquad\textbf{AND}\qquad \Omega = \frac{\Omega_\infty}{n}$$

**One knob wired to both slots.** For $n = 1 + a_N U$ the `sympy` expansion returns $c_{\rm eff}/c$ and $\Omega/\Omega_\infty$ as the *same* series, so

$$a_1 = b_1 = a_N \quad\text{and}\quad b_2 = a_N^2 \quad\text{are FORCED}$$

and the NR bracket collapses:

$$4a_N - a_N - \frac{2a_N^2}{a_N} \;=\; a_N \qquad\text{— the bare index slope, with no room for a second constitutive number.}$$

**This is an identity, not an approximation.** There is no expansion order at which the Gordon scalar construction recovers a second knob, no weak-field limit in which it becomes accurate, and no choice of $n(r)$ that repairs it — every scalar index gives $\Delta\phi/(\pi GM/c^2\ell_p) = $ its own slope, so the only $n$ that gives $6$ is $n = 1 + 6U$, which then breaks light deflection by $3\times$ and Newton by $6\times$.

For canon's matter index $n_{scalar} = 1 + GM/c^2r$ (`ponderomotive-equivalence.md`:14, `double-deflection.md`:22, `closure-roadmap`:205): slope $1$, so $\Delta\phi = \pi GM/c^2\ell_p$ and

$$F \;\equiv\; \frac{\Delta\phi_{\rm AVE}}{\Delta\phi_{\rm GR}} \;=\; \frac{1}{6}$$

**Confirming the concurrent lane's arithmetic.** `research/2026-08-27-ppn-tensor-derivation` reports $F = 1/6$ from a PPN-tensor route. I reproduce it here from a construction with no metric in it, by two independent methods (series Binet and 60-digit quadrature), and the quadrature lands `0.9999999667`. **That lane's number is right.** What this document supersedes is its OUTLOOK: $F = 1/6$ is not a statement about AVE's spatial sector being absent, it is a statement about **one number being asked to do two jobs**, and it is repairable without touching the $1/7 : 2/7$ projection ratio.

### The observational cost of the swap, my numbers

Orbital elements are mine (Mercury $a = 5.790905\times10^{10}$ m, $e = 0.205630$, $P = 87.9691$ d; $GM_\odot = 1.32712440018\times10^{20}$ m$^3$s$^{-2}$; PSR B1913+16 $M_{tot} = 2.828378\,M_\odot$, $P_b = 0.322997448911$ d, $e = 0.6171334$; $R_\odot = 6.957\times10^8$ m):

| observable | AVE as canon stands | repaired $(2,1,\tfrac12)$ | measured |
|---|---|---|---|
| Mercury perihelion | **`7.163446`** ″/cy — **$-895.4\sigma$** | `42.980676` ″/cy — $+0.017\sigma$ | $42.98\pm0.04$ |
| Hulse–Taylor periastron | **`0.70443293`** °/yr | `4.2265976` °/yr | $4.226585(4)$ |
| solar-limb deflection | `1.75119` ″ (light channel, $a_1=2$) | `1.75119` ″ | $1.7509$ |
| matter deflection at $v\to c$ | **half the photon** (§5) | equal to the photon | equal (GR) |

Two calibration checks on the wrong-way branches, so the reader can see how sharp $b_2$ is: matter riding the *light* index ($a_1=b_1=2$, $F=1/3$) gives `14.326892` ″/cy ($-716\sigma$); the repair with an **additive** clock ($b_2 = 0$, bracket $= 7$) gives `50.144122` ″/cy ($+179\sigma$). **$b_2$ moves Mercury by $179\sigma$.** It is not a rounding detail; it is the single remaining underived number in the $O(m)$ sector.


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
