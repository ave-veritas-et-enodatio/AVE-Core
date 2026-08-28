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

### 4.1 — What the repair is, in medium terms

A well-posed medium does not carry two unrelated indices. It carries **one speed function and one gap function**:

$$\omega_{\rm light}^2 = c_{\rm eff}^2(r)\,k^2, \qquad \omega_{\rm matter}^2 = c_{\rm eff}^2(r)\,k^2 + \Omega^2(r)$$

Same $c_{\rm eff}$, one extra term. So the matter packet **rides light's own characteristic speed** ($a_1 = 2$, whatever light uses) and carries its **own independently graded clock** ($b_1 = 1$, set by Newton). If that clock grades *multiplicatively* shell-by-shell — $\Omega = \Omega_\infty e^{-U}$ rather than $\Omega_\infty(1-U)$ — then $b_2 = \tfrac12$ and the bracket is $8 - 1 - 1 = 6$: **GR at $O(m)$, $\gamma = 1$, $\beta = 1$.**

Note what this does **not** require: no new field, no new constant, no change to the $1/7 : 2/7$ projection ratio, and no metric.

### 4.2 — Canon already owns both first-order numbers, in one leaf, under the right names

`manuscript/ave-kb/vol3/gravity/ch01-gravity-yield/temporal-spatial-lattice-decomposition.md`:24, **verified verbatim at HEAD `a3f4fef7`**:

> $n_{temporal}$ (slope 2) is the **bulk/coordinate-time** temporal propagation index — what a signal *traversing* the gradient accumulates (Shapiro-class integrated delay, $\approx 1/g_{00}$). It is **distinct** from the **local clock rate / gravitational redshift**, which is a slope-1 quantity: the proper tick of a clock *sitting* at $r$ is $\sqrt{g_{00}} = \sqrt{S} \approx 1 - GM/(c^2 r)$, giving redshift $z \approx GM/(c^2 r)$. The two are bridged by $z = (n_{temporal} - 1)/2$ — a propagating signal picks up $2\times$ the local clock effect.

Read that against the two slots:

| canon's object, same leaf, same line | this document's slot | value |
|---|---|---|
| $n_{temporal} = 1 + \tfrac27\varepsilon_{11} = 1 + 2U$, *"what a signal traversing the gradient accumulates"* | **speed** | $a_1 = 2$ |
| $\sqrt{S} \approx 1 - GM/c^2r$, *"the proper tick of a clock sitting at $r$"* | **clock** | $b_1 = 1$ |
| the bridge $z = (n_{temporal}-1)/2$ | **is literally** $b_1 = a_1/2$ | — |

And `claim-quality-closure-roadmap.md`:205 names the projection's job in its own words, **verified verbatim**: *"n_scalar(r) = 1 + GM/c²r for MASSIVE PARTICLES (ponderomotive, **only time component at leading order**)."*

**The $1/7$ projection was always the clock grading.** $(1/7)\cdot\varepsilon_{11} = (1/7)(7GM/c^2r) = U$, which is exactly the slope-1 clock. **The error was never the $1/7 : 2/7$ ratio.** The ratio is right and the $1/7$ is doing the job canon says it does. The error is feeding that $1/7$ into a **Gordon optical index**, which then overwrites the *speed* slot with the same number.

### 4.3 — ⚑ Two flags on this reading, surfaced not resolved

**Flag A — "channel-agnostic" is an interpretation, not a canon statement.** The brief that dispatched this lane called $n_{temporal}$ *channel-agnostic*. The leaf says *"what a signal traversing the gradient accumulates"*, which reads that way — but the same line also equates it to $\approx 1/g_{00}$, which is a **temporal-metric** object, and the leaf's own label is "temporal". Reading $n_{temporal}$ as the common $a_1$ of **both** channels is what the repair needs, and the leaf does not say it. **This is the interpretive step the repair rests on, and it is un-adjudicated.** Routed as an open item (§12).

**Flag B — $1/|g_{00}|$ is not the optical index; they agree only at first order.** The reconciliation lane caught this and I reproduced it. For exact isotropic Schwarzschild:

$$n_{opt} = 1 + 2U + \tfrac{7}{4}U^2, \qquad \frac{1}{|g_{00}|} = 1 + 2U + 2U^2$$

They agree at $O(U)$ and split at $O(U^2)$ — **exactly the order where the perihelion lives.** Canon makes that identification at `temporal-spatial-lattice-decomposition.md`:24 (*"$\approx 1/g_{00}$"*, with the $\approx$ doing real work) and the identification is what generates the whole double-index structure: once $n = 1+2U$ is labelled *temporal only*, a separate "spatial" index $(9/7)$ and a separate matter scalar $(1/7)$ become necessary. **Read as a full optical index, $n = 1+2U$ already contains $\gamma = 1$.**

Corroborating detail I derived while checking Flag B: exact isotropic Schwarzschild has grading exponents $(a_1, a_2, b_1, b_2) = (2, \tfrac94, 1, \tfrac12)$. So the repair's $b_2 = \tfrac12$ **is** GR's $\beta = 1$, and the exponential ansatz's $a_2 = 2$ differs from GR's $\tfrac94$ — a real difference that the NR perihelion cannot see (because $a_2$ drops out) but a relativistic orbit could.


## §5 — The falsifier that already fired: ultrarelativistic convergence and SN1987A

### 5.1 — The theorem · **DERIVED**, and it imports nothing

For **any** gapped dispersion $\omega^2 = c_{\rm eff}^2 k^2 + \Omega^2$, the gap term is negligible when $\omega \gg \Omega$. So an ultrarelativistic massive packet **must** trace the same ray as the massless mode of its own channel. This is a property of the dispersion relation. It uses no metric, no equivalence principle, and no GR input.

I derived the deflection in closed form from the same Binet equation used in §2 (unbound orbit, $u = A(1+e\cos\phi)$, $\alpha = 2/e$, $e = 1/(Ab)$, $\ell_p = b^2E/\big(\mu(Wb_1 + Ea_1)\big)$, $E = W\gamma^2\beta^2$):

$$\boxed{\;\frac{\alpha\,b}{GM/c^{2}} \;=\; 2a_1 \;+\; 2b_1\!\left(\frac{1}{\beta^{2}} - 1\right)\;} \qquad \xrightarrow[\ \beta\to1\ ]{}\ 2a_1$$

The $\beta\to1$ limit is $2a_1$ — **exactly the massless ray of the same channel** — for any $b_1$. The theorem is visible in the algebra.

| $v/c$ | GR $(a_1{=}2,\,b_1{=}1)$ | AVE as canon stands $(a_1{=}1,\,b_1{=}1)$ | ratio |
|---|---|---|---|
| 0.1 | `202.000000` | `200.000000` | 0.99010 |
| 0.5 | `10.000000` | `8.000000` | 0.80000 |
| 0.9 | `4.469136` | `2.469136` | 0.55249 |
| 0.99 | `4.040608` | `2.040608` | 0.50502 |
| 0.9999 | `4.000400` | `2.000400` | 0.50005 |
| **photon** | `4.000000` | **`4.000000`** (light channel, $a_1 = 2$) | — |

(Units $GM/bc^2$. My closed form reproduces L1's independent quadrature to every digit it reported: `202.0009 / 10.00004 / 4.46915 / 4.04062 / 4.000412` for GR, `200.0002 / 8.000006 / 2.469138 / 2.04061 / 2.000402` for AVE.)

**AVE's massive packet converges to `2.000`, its own channel's photon sits at `4.000`. Ratio $1/2$, forever.** GR converges to $1$. This depends on $a_1$ **alone** — not on $b_1$, not on $b_2$, not on the repair, not on the missing photoelastic map. It is the cleanest discriminator in this whole arc, and the repair ($a_1 = 2$ for both channels) fixes it as a side effect.

### 5.2 — SN1987A: my own arithmetic, my own method, stated

**The coupling-selection rule is canon's, verified verbatim** at `double-deflection.md`:20:

> **Matter (scalar coupling).** A fast-moving massive particle is an isotropic 3D volumetric wave packet carrying finite rest energy. It couples to the *scalar* (isotropic bulk) component of the lattice strain via the $1/7$ volumetric projection

A neutrino has rest mass. By canon's own rule it takes $n = 1 + U$, while the photon takes $n = 1 + 2U$.

**My method — deliberately chosen to avoid an enclosed-mass guess.** For a flat rotation curve, $GM(<r)/r = v_c^2$, so the index argument $U = GM(<r)/(c^2r) = (v_c/c)^2$ is **constant along the path**. With $v_c = 220$ km s$^{-1}$ and $D_{\rm LMC} = 51.4$ kpc:

- $U = (v_c/c)^2 = 5.38523\times10^{-7}$
- path length $= 1.58604\times10^{21}$ m
- photon potential-delay excess $\int 2U\,dl/c = $ **`65.9498` d**
- AVE matter excess $\int U\,dl/c = $ **`32.9749` d**
- **predicted $\nu$-vs-$\gamma$ differential $= $ `32.9749` d $= 791$ h**
- observed SN1987A $\nu$–$\gamma$ offset $\approx 3$ h $= 1.08\times10^4$ s
- **ratio predicted / observed $= 264$**

**And here is the model-free version of the same statement, which is the one to quote.** AVE-as-canon-stands predicts $(n_\nu - 1)/(n_\gamma - 1) = 1/2$ — a **50%** fractional difference in the two species' gravitational delay. The SN1987A coincidence bounds that fraction at $3\,\text{h} / 65.9\,\text{d} \approx 2\times10^{-3}$. **The violation is a factor of $\sim\!250$, and the factor is independent of the Galactic mass model** — the model enters both the numerator and the denominator of the fraction and cancels. A factor-2 error in $v_c^2$ moves the *days*; it does not move the $0.5$-versus-$2\times10^{-3}$ statement. (This lines up with the published SN1987A Shapiro-delay tests, which bound the species-differential at the few$\times10^{-3}$ level — **externally retrieved, tentative-standing**, not used to derive anything above.)

### 5.3 — ⚑ Escape hatches, named before this is called a kill

1. **Does canon actually assign the neutrino to the scalar channel?** The rule at `double-deflection.md`:20 is about *"a fast-moving massive particle"*, and I did not find a leaf that assigns the neutrino to a specific AVE channel. `neutrino-flavor-mixing.md`:12 treats MSW as *"impedance-dependent mode coupling between propagation channels"* without naming which channel carries the free neutrino. **This is genuinely open.** If AVE's neutrino turns out not to be an A1-massive packet, SN1987A stops being the cheap data point — but **the structural defect survives**, because the theorem is about any massive packet, and the same $1/2$ applies to a $0.9999c$ electron or proton.
2. **The Galactic mass model.** Handled above by working in the fractional statement.
3. **Is the $\sim$3 h offset the right observable?** It is an astrophysical coincidence (shock-breakout timing), not a null measurement. That loosens it by at most an order of magnitude and does not reach a factor of 250.

### 5.4 — This test appears nowhere in the corpus

Two independent searches over the whole worktree at `a3f4fef7` (`grep -ril` and `rg -il`, `.git` excluded) for `1987A` and `sn1987` return **0 files each**. Method blind spot: single-line regex; a phrase wrapped across lines would be missed; sibling repos under `AVE-staging/` were not searched. So: *absent from AVE-Core at `a3f4fef7` by these patterns*, not "absent from the program".


## §6 — Canon's competing Path-A route: what I verified, and what I do NOT assert

The brief warned that *"a false accusation of an arithmetic error in canon is itself a serious defect."* I took that seriously and the section is written to that standard: I state exactly what I verified, and I explicitly decline to assert the part I could not settle.

### 6.1 — Cite correction first

L1's finding attributed the test-mass Lagrangian to `anomalous-perihelion-advance.md`:10,:20. **It is not there.** Those two lines (duplicated text, verified verbatim) state the *conclusion* and the $V_{eff}$:

> The substrate's $n_{scalar}(r) = 1 + GM/c^2r$ … gives the effective potential $V_{eff}(r) = L^2/(2mr^2) - GMm/r - GML^2/(mc^2r^3) + O(\phi^2/c^4)$ — the $-GML^2/(mc^2r^3)$ correction term coefficient is **1**, IDENTICAL to GR Schwarzschild. Perihelion advance $\Delta\phi = 6\pi GM/c^2 a(1-e^2)$ is therefore substrate-native at leading PPN-1, NOT borrowed from GR.

The **Lagrangian** lives at `claim-quality-closure-roadmap.md`:205, verified verbatim: *"test mass Lagrangian L = -mc²√(1-n_scalar²v²/c²)/n_scalar"*. Same claim, different file. L1 did cite `:205` as carrying "same text"; the precise location of the Lagrangian is the correction.

### 6.2 — What I verified, exactly · **DERIVED**

That Lagrangian **is** the geodesic Lagrangian of the Gordon scalar metric. For $ds^2 = -A\,c^2dt^2 + B\,d\mathbf x^2$ the geodesic Lagrangian is $\mathcal L = -mc^2\sqrt{A - Bv^2/c^2}$; setting $A = 1/n^2$, $B = 1$ gives exactly $-\big(mc^2/n\big)\sqrt{1 - n^2v^2/c^2}$. So it inherits §3's identity: $c_{\rm eff} = c/n$ **and** $\Omega = \Omega_\infty/n$.

And for a scalar index **linear** in $u$, $n = 1 + q\,\mu u$, the orbit equation is not merely approximately soluble — it is **exact**, because

$$f(u) = \frac{\omega^2 n^2 - W}{c^2} = \frac{\omega^2 - W}{c^2} + \frac{2\omega^2 q\mu}{c^2}u + \frac{\omega^2 q^2\mu^2}{c^2}u^2$$

is **exactly quadratic in $u$**, so $u'' + (1-\varepsilon)u = C$ holds with no truncation. Eliminating $\omega^2/(c^2p_\phi^2)$ via $C = 1/\ell_p$ gives $\varepsilon = q\mu/\ell_p$ and

$$\boxed{\;\Delta\phi \;=\; \frac{\pi\,q\,GM}{c^{2}\ell_p}\;}\qquad\text{for any packet speed — }E\text{ cancels identically.}$$

**At $q = 1$ (canon's $n_{scalar}$): $\Delta\phi = \pi GM/c^2\ell_p$, which is one sixth of the $6\pi GM/c^2\ell_p$ the leaf concludes.** Cross-checked by the independent 60-digit quadrature: `0.9999999667`.

> **So the stated conclusion does not follow from the stated Lagrangian.** That claim I assert, and it is verified two ways, non-perturbatively.

### 6.3 — What I do NOT assert

L1 reported that the intermediate step *"the coefficient is 1"* reads $q/2 = \tfrac12$ in canon's own chart, where GR reads $3/2$. **I could not confirm that specific number, and I got a different one.** My Hamiltonian route through the same Lagrangian returned a $L_z^2/r^3$ coefficient of $GMq/(4mc^2)$, and a hand expansion of the same object gave $-2q\,GML_z^2/(mc^2r^3)$. Three workings, three answers.

**That disagreement is itself the finding, and it is more useful than any of the three numbers.** The $V_{eff}$ split is **not chart-independent**: it depends on the time parameter (coordinate vs proper), on the radial coordinate (isotropic vs areal), and on how the energy-dependent $O(U)/r$ and $O(U^2)/r^2$ terms generated by this Lagrangian are apportioned. Those terms *also precess* — a $1/r^2$ term shifts the apsidal angle just as a $1/r^3$ term does. Reading the advance off the $1/r^3$ coefficient alone is valid only in the chart where the GR textbook $V_{eff}$ is derived (areal $r$, proper-time parametrisation), where those companion terms are absent.

**So the precise, defensible statement is:** canon's shortcut compares a $1/r^3$ coefficient computed in one chart against a textbook value computed in another, and the intermediate quantity it compares is not chart-invariant. **I am not asserting that canon's arithmetic at that step is wrong.** I am asserting that the step cannot carry the conclusion, and that the chart-independent observable — which I computed exactly, twice — is $\pi q\,GM/c^2\ell_p$.

### 6.4 — Status of the affected nodes

`clm-qyn8t0` sits at solidity 0.55, build-band *"use as input only, don't build deeper"*. The leaf already carries a 2026-05-17 scope correction downgrading the result to a consistency check; what `:10`/`:20` then assert is that the consistency check is *substrate-native*. **That assertion is what falls.** Flag-don't-fix: I have edited nothing in the KB. §12 routes it.

**Symmetric-standard note.** Reading a perihelion off a $1/r^3$ coefficient by pattern-match to a textbook is an extremely common shortcut, and the SM/GR literature does it constantly without incident — because there the chart is usually the textbook's. This is a chart-hygiene failure, not a competence failure, and it is the kind of error that a metric-first framing makes easy and a wave-mechanical framing makes impossible (the ray integral has no $V_{eff}$ to mis-split).


## §7 — The DERIVED / IMPORTED ledger, step by step

### 7.1 — DERIVED (from a constitutive law, with no metric in the chain)

| # | step | who | my status |
|---|---|---|---|
| D1 | $\omega^2 = c_{\rm eff}^2k^2 + \Omega^2$, $c_{\rm eff}^2 = 1/(LC)$, $\Omega^2 = S/C$, from a graded lossless LC ladder with shunt stiffness | L1 | reproduced |
| D2 | $v_p v_g = c_{\rm eff}^2$ identically; $\omega/\Omega = 1/\sqrt{1-v^2/c_{\rm eff}^2}$ falls out of the gapped branch with no relativity postulated | L1 | accepted, not re-derived |
| D3 | force law $\mathbf a = -c^2\nabla\ln\Omega$ | L1 | reproduced — **FORM derived, $b_1{=}1$ VALUE calibrated to Newton** |
| D4 | $\Delta\phi = \dfrac{\pi GM}{c^2\ell_p}\big(4a_1 - b_1 - 2b_2/b_1\big)$, and the exact $E,W$ form | L1 | **reproduced in `sympy`, difference $\equiv 0$** |
| D5 | Gordon scalar $\Rightarrow a_1 = b_1$, $b_2 = a_1^2$ FORCED $\Rightarrow$ bracket $=$ bare index slope $\Rightarrow F = 1/6$ | L1 | **reproduced, 2 methods** (`0.9999999667`) |
| D6 | Ax3 $\min|\Gamma|^2 \Rightarrow Z(x) = Z_0 \Rightarrow \epsilon_{ij}\propto\mu_{ij} \Rightarrow$ Fresnel determinant is a perfect square $\Rightarrow$ **no gravitational birefringence at any order**, and the optical metric *emerges* as the inverse principal symbol | L3 | accepted, not re-run — **credited: a real derivation from a non-GR premise** |
| D7 | Ax4's kernel $\sqrt{1-A^2}$ is **even** $\Rightarrow$ zero $O(m)$ index gradient $\Rightarrow$ solar-limb deflection $3.6\times10^{-5}$″ against $1.75$″ | L3 | accepted, not re-run |
| D8 | two distinct cones ($v_L^2/v_T^2 = 4/3 + K/G \geq 4/3$) $\Rightarrow$ the medium's invariance group has **no boost generator** | L2 | accepted, not re-run |
| D9 | ultrarelativistic-convergence theorem; AVE leaves it at exactly half | L1 | **reproduced, and upgraded to closed form** (§5.1) |
| D10 | $n_{opt}$ and $1/|g_{00}|$ agree at $O(U)$, split at $O(U^2)$ ($7/4$ vs $2$) | recon | **reproduced** |
| D11 | exact isotropic Schwarzschild has $(a_1,a_2,b_1,b_2) = (2, \tfrac94, 1, \tfrac12)$ | mine | derived here |
| D12 | canon's Path-A Lagrangian has an **exactly quadratic** $f(u)$, so $\Delta\phi = \pi q GM/c^2\ell_p$ non-perturbatively | mine | derived here (§6.2) |
| D13 | $\alpha b/(GM/c^2) = 2a_1 + 2b_1(1/\beta^2 - 1)$ in closed form | mine | derived here (§5.1) |
| D14 | cubic point group protects rank-2 **exactly** and does **not** protect rank-4 — so a cubic lattice does not make the deflection isotropic for free; that is an extra condition on the missing $p_{ijkl}$ ($p_{11} - p_{12} = 2p_{44}$) | L2 + recon | accepted, not re-run |

### 7.2 — IMPORTED, with canon's own stamp at file:line

| # | object | canon's own words | verified |
|---|---|---|---|
| I1 | $\kappa = c^4/7G$ **and** $\nu_{vac} = 2/7$ | `eq_axiom_5.tex`:134 — *"kappa = c^4/7G and nu = 2/7 stay GR-imported (#261 untouched)"* | ✅ verbatim |
| I2 | $\nu_{vac} = 2/7$ not crystalline-forced | `double-deflection.md`:60 — *"$\nu=2/7$ is **not** crystalline-lattice-forced — it is the GR-imported $K=2G$ value"*, re-confirmed at the ratified $z{=}3$ srs carrier by PR#506 | ✅ verbatim |
| I3 | therefore $\varepsilon_{11} = 7GM/c^2r$, and therefore $a_1 = \nu_{vac}\cdot 7 = 2$ | rides I1+I2 through the elliptic solve | ✅ chain checked |
| I4 | Ax4's yield anchor $A_{yield}$ | `eq_axiom_4.tex` — *"inherits from the GR-imported $K=2G$ — FORM-derived, VALUE-imported"* | reported by L3/recon; line number contested (§11) |
| I5 | $b_1 = 1$ | **not stamped anywhere as an import.** It is calibrated to the Newtonian limit through $\mathbf a = -c^2\nabla\ln\Omega$. Tagged here as VALUE-calibrated | mine |
| I6 | Mercury / Hulse–Taylor / solar-limb / Cassini targets | data, used only at the reporting step | — |
| I7 | $v_c = 220$ km/s, $D_{\rm LMC} = 51.4$ kpc, SN1987A $\sim$3 h offset | external astrophysical inputs, tentative-standing | — |

### 7.3 — ASSERTED (the one that decides the result)

| # | object | status |
|---|---|---|
| **A1** | $b_2 = \tfrac12$, equivalently *"the clock grades multiplicatively, $\Omega = \Omega_\infty e^{-U}$"* | **ASSERTED.** No axiom, no leaf, and no lane derives it. It is worth $179\sigma$ on Mercury. |
| **A2** | that $n_{temporal}$'s slope 2 is the **speed** grading of *both* channels rather than a temporal-metric component | **INTERPRETIVE.** §4.3 Flag A. |

### 7.4 — The one-line reading of the ledger

**AVE forces the FORM and imports the VALUE — third and fourth instance in this document alone.** The precession law's *shape* (two constitutive functions, three exponents, $a_2$ absent) is genuinely derived from the medium. Every *number* that enters it is either GR-imported ($a_1 = 2$, through the $\nu_{vac}\cdot 7$ chain canon itself stamps), calibrated to a measurement ($b_1 = 1$ to Newton), or asserted ($b_2 = \tfrac12$).

**Symmetric-standard check, in AVE's disfavour and then in its favour.** GR fixes **one** constant ($G$, from the Newtonian limit) and then *predicts* the deflection factor 2 relative to Soldner and the perihelion $6\pi$. AVE, as this ledger stands, spends two measurements on two constants and asserts a third. **That is genuinely weaker and I report it as weaker.** Conversely: D6 — Ax3's $\min|\Gamma|^2 \Rightarrow Z = Z_0 \Rightarrow$ zero gravitational birefringence, with the optical metric falling out as the **inverse principal symbol of the wave operator** — is a real derivation from a premise GR does not have, it runs in the medium$\to$metric direction, and it is machine-checkable. GR gets the same fact from the equivalence principle, which is not.


## §8 — L2: the preferred-frame state. This outranks the perihelion

This section reports the `L2-preferred-frame` lane **as its journal entry actually states it**, with the cites I re-verified marked. L2's own verdict opens: *"AVE is a preferred-frame theory exactly, not approximately."* The reconciliation lane, which re-ran L2's greps independently, concluded: *"yes, there is a foundational gap here and it outranks the perihelion."* **I concur, and the reason is structural: the perihelion defect is a repairable wiring error with one number owed; this one is a class of arithmetic the corpus cannot presently perform at all.**

### 8.1 — Does canon confront the aether-drift bounds?

**Partly, in one channel, and not in the channel that matters.**

Canon is **candid at the axiom level** — `eq_axiom_3.tex`:27, verified verbatim: *"**Lorentz invariance** follows only *in the continuum limit* — it is **emergent**, not exact: the discrete K4 substrate is a preferred-frame medium."* And `relational-cancellation-identity.md`:36 states the frame *is* detectable and *"the CMB dipole IS the detection"*. **This is not a hidden problem; canon names it.**

What is missing is **arithmetic**. Two independent search methods over the whole worktree at `a3f4fef7` (`grep -ril` and `rg -il`, `.git` excluded) return:

| pattern | files |
|---|---|
| `preferred-frame parameter` | **0** |
| `crystal momentum` | **0** |
| `umklapp` | **1** — `temporal-saturation-regime-classifier.md`, and there only inside a **gap list** |
| `photoelast` (family) | **4** — all research/orchestration scoping docs; **none in `manuscript/` or `src/`** |

L2 additionally reports that every `alpha_1` / `alpha_2` / `alpha_3` hit in the corpus is a nuclear-alpha or element-circuit symbol, never a PPN preferred-frame parameter, and that all 20 `Nordtvedt` hits are the $\eta_{\rm Nordtvedt}$ EP test, never expanded into its $\alpha_i$, $\zeta_i$ terms. **So the PPN preferred-frame parameters are absent from the corpus as physics objects.**

The bounds L2 re-retrieved (**external, tentative-standing**): $|\alpha_1| < 3.4\times10^{-5}$, $|\alpha_2| < 1.6\times10^{-9}$, $|\alpha_3| < 4.0\times10^{-20}$. L2 flags that its dispatch's $\alpha_2 < 10^{-7}$ was **two orders too loose**, and that $\alpha_2$ is precisely the parameter a two-cone medium is most likely to source — it is what the spin-0/spin-1 vs spin-2 speed difference controls in vector-tensor and Einstein-aether theories, and AVE's ratio is $1.83$, not $1$.

**And L2 declines to compute one.** Its finding 9, verbatim: *"I am NOT asserting an $\alpha_2$ value for AVE: the object required to compute one — the boost response and limiting speed of a bound matter excitation on a two-cone medium — is explicitly UNDERIVED in canon"*, citing `research/2026-08-06_lc1-one-speed_result.md`:340 row 5: *"the corpus does not establish the limiting speed of a bound matter excitation in a medium with $v_L > v_T$ … Enumerated, flagged (§10 FLAG-LC1-D), NOT folded into the verdict, and no speed is guessed."* **That absence IS the answer: the framework cannot presently compute the numbers the bounds constrain.**

### 8.2 — Is the self-cancellation argument derived or asserted?

**Asserted, at walk level — and canon's own cancellation leaf rules this case OUT of itself.**

The self-cancellation framing lives at `_orchestration/2026-08-04_lorentz-compliance-arc-brief.md`:21-23 (L2's cite): *"Uniform saturation is unobservable from inside (self-cancellation — the phase-only doctrine IS the emergence mechanism)"* — an orchestration brief whose own header records five kill tests, all UNSTARTED.

The canonical leaf that formalises cancellation excludes the frame case explicitly. `relational-cancellation-identity.md`:47-52, **verified verbatim at HEAD**:

> ⚑ [`preferred-frame-and-emergent-lorentz.md`] is **NOT an instance** — it is this leaf's **contrast exhibit** (§2): its undetectability is *dynamical and finite*, and the frame it discusses *is* detectable.

So canon claims a **finite dynamical suppression**, not an exact cancellation. The only quantified form of that suppression is the $(q\ell_{node})^4 \approx 2.2\times10^{-22}$ cubic-symmetry number — **and L2 shows it does not cover the boost channel.**

### 8.3 — L2's refutation of the leaf's escape clause, which I re-verified verbatim

`preferred-frame-and-emergent-lorentz.md`:112, **verified verbatim at HEAD**:

> on weak-C-fails the recovered $O(k^2)$ term is the *isotropic* 2nd moment, so the leading *anisotropic* term is STILL quartic and a Hughes–Drever / cavity anisotropy bound (which tests frame-dependent $\delta c/c$, not an isotropic scalar dispersion) does not collide on either branch.

**L2's counter, which is kinematics and does not depend on any coefficient:** an isotropic dispersive law $\omega^2 = c^2k^2(1 + a_2(k\ell)^2)$ makes $\omega^2 - c^2k^2 = a_2c^2\ell^2k^4 \neq 0$, and $k^4$ **is not boost-invariant**. *A term that is isotropic in one frame is anisotropic in every other.* Transporting through the plane-wave Doppler factor $D = \gamma(1-\beta\cos\theta)$ gives one-way $\delta v/c = 2a_2(k\ell)^2\beta\cos\theta$ and two-way $a_2(k\ell)^2\beta^2(5\cos^2\theta - 1)$.

Numbers at $\beta_{\rm CMB} = 1.2342\times10^{-3}$, $\ell_{node} = 3.8616\times10^{-13}$ m, $a_2 = +0.056$, $\lambda = 633$ nm: one-way $2.0\times10^{-15}$, two-way sidereal $6.3\times10^{-18}$ — against the leaf's headline $(q\ell)^4 = 2.2\times10^{-22}$. **4.5 orders larger, with a $\nu^2$ rather than $\nu^4$ signature, landing AT the $\sim10^{-17}$ optical rotating-cavity class rather than below it.**

**Two honest brakes, both from the lanes themselves.** (i) The *magnitude* rides $a_2 = +0.056$, which is a P1b eigensolve output that L2 mis-cited (§11) and which the reconciliation lane traced to a **demoted bullet** driven from an off-main branch — treat the number as a scoping estimate. (ii) The channel fires only on the **weak-C-fails** branch, gate `wejkhvnfb` OPEN. **The kinematic point does not depend on $a_2$ at all.**

L2 also flags a citation-band mismatch in the leaf's headline comparison: `Nagel et al. 2015` is a $\sim$10 GHz **microwave** whispering-gallery experiment, and `Sanner et al. 2019` is a Yb$^+$ **optical-clock** (matter-sector) test — neither is an optical photon-sector cavity-anisotropy bound. The reconciliation lane partially softened this (the leaf does say *"per SME operator"* at `:22`); the band mismatch stands and it matters, because the boost channel scales as $\nu^2$ while the leaf's quartic scales as $\nu^4$, so instrument choice changes which channel dominates.

### 8.4 — The $O(1)$ item that needs no $k$-expansion at all

L2's sharpest number, reproduced independently by the reconciliation lane from #506's shipped moduli at $\rho^* = 9.7734$ ($C_{11} = 0.7279$, $C_{12} = 0.3232$, $C_{44} = 0.2488$): the cubic Christoffel branches give a transverse speed ratio $\sqrt{C_{44}/C'} = \sqrt{A} = 1.10885$ exactly, $A = 1.22955$ — a **10.32% direction-dependent shear speed and a 10.3% shear birefringence at zeroth order in $k$**. And because `port-register.md`:47 makes the photon the **transverse-$u$** branch, the photon rides the *same* rank-4 tensor as the shear GW.

The group theory is why the quartic argument cannot reach it, and L2 verified it by explicit averaging over all 24 proper rotations of point group 432: **a rank-2 material tensor is forced to be exactly isotropic; a rank-4 elastic tensor retains three independent constants.** Cubic symmetry protects $\epsilon$ and $\mu$ exactly and does **not** protect $C_{ijkl}$.

The only thing making the 10% vanish is the operating-point choice $\rho_{bond} = 1$ — where #506 records $A = 1.000$ **and** $K = -0.0589$, a negative bulk modulus at which the medium cannot carry A1 dilatation mass. **And the derivation that was supposed to force $\rho_{bond} = 1$ from Axiom 3 is 🔴 DEMOTED** (2026-08-11, R40-B2a), stamped at `preferred-frame-and-emergent-lorentz.md`:54 (I verified the stamp verbatim) but, per L2, **not** stamped on the two claim-quality rationale rows that assert *"the emergent-Lorentz isotropy is now protected two independent ways"* (`vol1/claim-quality.md`:1746, `vol4/claim-quality.md`:663). That is a demotion-propagation gap on the single load-bearing defence.

### 8.5 — Umklapp and the discrete-translation / momentum-conservation question

**Untreated, and the thresholds are exact because $\ell_{node}$ is definitional.** I recomputed all three from `constants.py`:293 ($\ell_{node} \equiv \hbar/m_ec$) and CODATA:

| carrier | zone edge $q = \pi/\ell_{node}$ |
|---|---|
| photon | $E = \pi\,m_ec^2 = $ **`1.605351` MeV** (the $\pi$ is definitional, not a coincidence) |
| electron | kinetic **`1.173718` MeV** |
| **proton** | kinetic **`1.37335` keV** |

**What this implies for momentum conservation.** On a lattice, spatial translation symmetry is **discrete**; the conserved bookkeeping quantity is crystal momentum defined **modulo a reciprocal-lattice vector**, and Umklapp is a reactive three-wave phase-matching condition (*not* a drag — see L2's import #3 in §10). Now read the axiom: `eq_axiom_3.tex`:27, **verified verbatim**, names its Noether legs as **time-translation invariance** and the **residual gauge family** $\mathbf A \to \mathbf A + \nabla\lambda(\mathbf x)$. **Spatial translation is not among them.** L2 reports that the only assertion of momentum conservation it found is a docstring at `src/ave/topological/vacuum_engine.py`:1477, and that the one place momentum closure was load-bearing — the dark wake — is 🔴 DEMOTED 2026-08-11 and self-flags at `dark-wake-bemf-foc-synthesis.md`:122 as *"an explicit open gap, not a framework claim."*

$\alpha_3$ is precisely the PPN parameter that is nonzero for theories with a preferred frame **and** non-conserved momentum. It is bounded at $|\alpha_3| < 4\times10^{-20}$ — one of the tightest numbers in physics. **AVE has the first condition by its own axiom text and cannot presently rule out the second.**

Two sharp consequences L2 names and canon does not carry: (a) if the weak-C gate fails for light, photons above $\sim$1.6 MeV are Bloch modes and vacuum Umklapp/Bragg opens — which MeV $\gamma$-ray astronomy excludes far more directly than the birefringence horn (LHAASO's 13 TeV photon from GRB221009A sits $2.5\times10^7$ zone edges out); (b) if the leaf's weak-C RESCOPE means the **centre-of-mass** wave rather than the soliton's internal mode, every cosmic ray above $\sim$keV has momentum defined only modulo a reciprocal-lattice vector. **Canon does not disambiguate the two readings.**

### 8.6 — The two-cone theorem, and why the boost channel is not $(q\ell)^4$-suppressible

L2's exact symbolic result: a boost $L(\beta)$ built to preserve the cone $\omega^2 = v_1^2q^2$ maps $\omega^2 = v_2^2q^2$ to a form with a cross term; requiring $L^{\mathsf T}Q(v_2)L = k\,Q(v_2)$ for **any** conformal $k$ returns the unique solution $\{\beta = 0, k = 1\}$. **With $v_1 \neq v_2$ the maximal common invariance group has no boost generator — rotations and translations only.**

Canon supplies the two cones at `port-register.md`:47 (photon T2 at $c$) and `:49` (A1 bulk radiative at $\sqrt{10/3}\,c \approx 1.83c$). This is **not** a $(q\ell)^4$-suppressible statement: the cone ratio is $1.83$, not $1 + 10^{-22}$. And the floor survives the $K = 2G$ import — `research/2026-08-06_lc1-one-speed_result.md`:181-197 derives $v_L^2/v_T^2 = 4/3 + K/G$ and states that $v_L = c$ needs $K = -G/3$, *"a negative bulk modulus… There is no stable configuration of this medium with a single wave speed."* At $K = 0$ the ratio floor is still $\sqrt{4/3}$.

**Correction I owe on this cite (verify-before-cite):** the reconciliation lane flagged that the row carrying the A1 speeds is **DEMOTED twice**. I checked: `port-register.md`:**49** — not `:50` as the reconciliation lane wrote — carries `🔴 [DEMOTED 2026-08-11 — R40-B1]` **and** `🔴 [DEMOTED 2026-08-11 — R40-B2a]`, two stamps on one row (count verified by `gsub` on the line, 2 hits). **The two-cone *existence* survives** because LC-1 §2.2 derives it independently of the row; the specific *values* $\sqrt2 c$ / $\sqrt{10/3}\,c$ ride a demoted row.

### 8.7 — The $O(\beta^2)$ item L2 correctly refused to assert

`research/2026-07-08_p6-lv-sector-classification_result.md`:44-50 assigns the frame anchor to **A1** and the LV response to **T2**. If a bound A1 excitation's kinematics track the A1 cone, a boosted atom's inertia rides $\gamma_L = 1/\sqrt{1-\beta^2/v_L^2}$ while its emission rides $\gamma_T$, and $\gamma_T/\gamma_L - 1 = 0.35\beta^2 = 5.3\times10^{-7}$ at $\beta_{\rm CMB}$ — Hughes–Drever / $\alpha_2$ shape, **four orders above the $|\alpha_2| < 1.6\times10^{-9}$ bound if the coefficient is $O(1)$.**

L2 marks this **UNDERDETERMINED, not DERIVED**, because the premise — that a bound A1 excitation's kinematics track the A1 cone — is exactly FLAG-LC1-D. **That is the correct call and I am not upgrading it.** It is also the single calculation that would settle whether AVE's preferred frame is affordable.

Canon does already carry one derived $O(\beta)$ preferred-frame prediction: `research/2026-07-08_p6-frame-boost-dependence_result.md`:31 gives a $P_{\rm flip}$ first-harmonic amplitude $4\beta \approx 4.94\times10^{-3}$ phased to the CMB dipole, self-described as *"a strong Lorentz-violation prediction in the nonlinear photon sector"*, with a nonlinear-SME bound check owed.


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
