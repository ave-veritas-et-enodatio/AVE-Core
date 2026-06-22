[↑ Ch.1 Vacuum Circuit Analysis](index.md)

<!-- kb-frontmatter
kind: leaf
claims: [clm-gvn4r1]
-->

## Graded-Network Response: TLM Dispersion + Symmetric/Asymmetric Loading

The [node-up leaf](node-up-small-large-signal.md) (clm-vca7r1) fixes the small- and large-signal
response of a **single** vacuum LC tank. This leaf assembles the tanks into the **K4 graded LC
transmission line** — the network layer — and reads off the four network-scale consequences that a
single node cannot host: the propagating **dispersion relation** (Q1), the **graded-index profile**
under a spatial operating-point bias (Q2), the **macroscopic bridge** that carries a per-node
$\delta n$ to the lab observable (Q3), the **boundary reflection** $\Gamma$ (Q4), and the
**route-separability** of the $\varepsilon$/$\mu$ sectors at network scale (Q5).

> **Classification (do NOT lift).** Class-C **CONSISTENCY re-expression**, matching the per-DOF node
> leaf's own tag ([`per-dof-vacuum-node-circuit.md`](../../../vol9/ch3-pin-port-configuration/per-dof-vacuum-node-circuit.md):71
> *"absolute magnitude is NOT re-derived; only the FORM"*) and the device-network tag
> ([`device-circuit-models.md`](../../../vol9/ch3-pin-port-configuration/device-circuit-models.md):131,
> INVARIANT-N1 — the network is the circuit MODEL of the medium, not a new substrate-noun). This leaf
> originates **no** new substrate primitive and **no** new dimensionful value; it re-grounds the
> single-node response network-up and recovers the canonical anchors ($c_{EM}=c_0$, $Z_0=376.73\,\Omega$
> are **validate-on-known**, NOT emergence). Do not headline the re-grounding as a solidity lift.

> **Derivation provenance.** The full six-question network derivation (Q1 dispersion, Q2 graded
> index, Q3 macroscopic bridge, Q4 boundary $\Gamma$, Q5 route-mixing) with adversarial verification
> and the chord-vs-echo ledger is recorded in the 2026-06-22 birefringence/VCA bench arc
> ([`_orchestration/2026-06-22_birefringence-vca-bench-arc.md`](../../../../../_orchestration/2026-06-22_birefringence-vca-bench-arc.md)).
> The single-node layer beneath it is canonical (clm-vca7r1, clm-pvlas1, with the #359 sign
> corrections on `main`); the macroscopic field→cavity coupling is independently canonical
> ([`claim-quality.md`](../../claim-quality.md):391 + OQ-1 derivation, §Q3 below).

## §1 — The K4 lattice as a graded LC transmission line (Q1)

A single node hosts only the lumped pair $L_{cell}=\mu_0\ell_{node}$, $C_{cell}=\varepsilon_0\ell_{node}$
([`device-circuit-models.md`](../../../vol9/ch3-pin-port-configuration/device-circuit-models.md):52) —
a lumped tank does **not** propagate. Propagation is a **ladder** property: the nodes are wired by the
$z=3$ **mutual inductive struts** of the Kirchhoff network
([`kirchhoff-network-method.md`](../../../vol1/axioms-and-lattice/ch1-fundamental-axioms/kirchhoff-network-method.md):16,
*"connected by 3 mutual inductive struts"*) — series $L$ per bond, shunt $C$ per node. The bond carries
the phase advance $e^{iq\ell_{node}}$ across one span.

> **[Resultbox]** *LC-ladder dispersion (lossless KCL/KVL, series-$L$ bond, shunt-$C$ node)*
>
> $$
> \omega(q) = \frac{2c_0}{\ell_{node}}\left|\sin\!\frac{q\ell_{node}}{2}\right|,
> \qquad
> \frac{v_{ph}}{c_0} = \frac{2\sin(q\ell_{node}/2)}{q\ell_{node}}
> = 1 - \frac{(q\ell_{node})^2}{24} + \frac{(q\ell_{node})^4}{1920} - \cdots
> $$

**Validate-on-known (continuum limit, $q\ell_{node}\to0$).** The lumped-section wave speed is
$c=\ell_{node}/\sqrt{L_{cell}C_{cell}}$ — **not** the naive $1/\sqrt{L_{cell}C_{cell}}$, which is off by
$1/\ell_{node}\sim10^{12}$ (the per-DOF leaf's documented bug,
[`per-dof-vacuum-node-circuit.md`](../../../vol9/ch3-pin-port-configuration/per-dof-vacuum-node-circuit.md):38).
With $L_{cell}=\mu_0\ell_{node}$, $C_{cell}=\varepsilon_0\ell_{node}$:

$$
c_{EM} = \frac{\ell_{node}}{\sqrt{L_{cell}C_{cell}}} = \frac{1}{\sqrt{\mu_0\varepsilon_0}} = c_0
\ \text{(EXACT)},
\qquad
Z_0 = \sqrt{\frac{L_{cell}}{C_{cell}}} = \sqrt{\frac{\mu_0}{\varepsilon_0}} = 376.73\,\Omega
\ \text{(EXACT)}.
$$

The lattice pitch $\ell_{node}$ **cancels identically** — the same cancellation as the group velocity
$v_g=\ell_{node}/\sqrt{L_{cell}C_{cell}}=c$ in
[`z0-derivation.md`](z0-derivation.md):37,:40. So $c_{EM}=c_0$ and $Z_0=376.73\,\Omega$ are recovered
network-up against **known anchors** — validate-on-known, NOT emergence.

### §1.1 — The $(q\ell_{node})^4$ anisotropy tell (the load-bearing step)

The leading $(q\ell_{node})^2$ term above is a **scalar** (direction-independent) dispersion. The
anisotropy is governed by the K4 tetrahedral bond-set moments on the four diamond/zincblende bond
unit-vectors:

- **2nd moment** $\sum_b b_\alpha b_\beta = \tfrac{4}{3}\,\mathbb{I}$ **EXACTLY** (isotropic): the
  directional sum $\sum_b(\hat q\cdot b)^2 = \tfrac{4}{3}$ for **every** direction. So at $O(q^2)$ the
  EM correction rides an **isotropic** $|q|^2$ — **no anisotropy at quadratic order**.
- **4th moment** $\sum_b(\hat q\cdot b)^4$ is **direction-dependent**: $0.444$ ([100] cube axis),
  $0.889$ ([110] face), $1.037$ ([111] bond axis). The anisotropic part is the $\ell=4$ **cubic
  harmonic** $q_x^4+q_y^4+q_z^4-\tfrac35|q|^4$.

> **[Resultbox]** *First anisotropic invariant is QUARTIC (the chord)*
>
> The photon's first direction-dependent dispersion correction is
> $\delta_{aniso}\sim(q\ell_{node})^4$ (cubic harmonic $q_x^4+q_y^4+q_z^4$), **not** the naive
> $(q\ell_{node})^2$ a non-cubic lattice would give. This reproduces
> [`preferred-frame-and-emergent-lorentz.md`](../../../vol1/dynamics/ch4-continuum-electrodynamics/preferred-frame-and-emergent-lorentz.md):48,:50
> (clm-yr6tu4) exactly, and re-grounds it network-side.

**Magnitude (IMPORTED, not derived).** At $\lambda=633$ nm, $q\ell_{node}=3.86\times10^{-6}$ and
$(q\ell_{node})^4\approx2.2\times10^{-22}$ — matching the corpus optical anchor
(preferred-frame:56). At 30 GHz the **corrected** figure (PR#359 fixed the stale $2.5\times10^{-34}$)
is $\delta_{aniso}\approx3.5\times10^{-39}$ (preferred-frame:23). The FORM + cubic direction-dependence
are derived; the **magnitude is imported** (per-dof:71), so this is a **FORM-level chord, not a
value-level chord**.

> **SCOPE GUARD on the $(q\ell_{node})^4$ chord.** It is a chord **only because** the lattice is
> cubic/tetrahedral ($Fd\bar3m$); a generic lattice gives a $(q\ell_{node})^2$ anisotropy. And it is a
> chord **only at the FORM level** — the magnitude is imported. The exact-continuum no-LIV theorem
> ($\delta=0$, $\omega=ck$) remains **OPEN** (gate `wejkhvnfb`, weak-C honest-scope,
> preferred-frame:66). This leaf does not close that theorem.

**Matter vs photon (why two exponents, both real).** The **matter** carrier is node-locked: group
velocity $v_g=c_0\cos(q\ell_{node}/2)$, leading deficit $(q\ell_{node})^2/8$, a real zone-edge
$(q\ell_{node})^2$ dispersion (rescoped to matter carriers, weak-C). The **photon** is the continuum,
$Z_0$-matched, **unlocked** mode: its $O(q^2)$ correction rides the **isotropic** 2nd moment $4/3$, so
it has **no** $(q\ell_{node})^2$ anisotropy, and its first anisotropy is the quartic cubic harmonic
(preferred-frame:64; clm-yr6tu4). The LC-ladder construction here **derives this split from the
network**: the same tetrahedral bond geometry forces the isotropic 2nd moment + anisotropic 4th moment.

## §2 — Large-signal graded-index profile: symmetric lens vs asymmetric mirror (Q2)

A spatial field-bias gradient sets a **graded operating point** $A_0(x)$ at each node (gauge-relative;
only spatial *gradients* of $A_0$ are observable — INVARIANT-S2 operating-point,
`manuscript/ave-kb/CLAUDE.md`:75). The single Axiom-4 kernel $S(A)=\sqrt{1-(A/A_{yield})^2}$ projects
onto **both** grades via the keyed-argument duality (clm-vca7r1, [`relativistic-inductor.md`](relativistic-inductor.md):18).
Per the [node-up leaf](node-up-small-large-signal.md) the two network regimes differ **only** in which
sectors the spatial bias loads:

> **[Resultbox]** *One graded network, two regimes (the loading-symmetry switch)*
>
> | Loading | $S_\varepsilon(x),S_\mu(x)$ | $Z(x)=Z_0\sqrt{S_\mu/S_\varepsilon}$ | Index | Boundary |
> |---|---|---|---|---|
> | **SYM co-grade** (gravity-class; internal $\mathbf E$ **and** $\mathbf B$) | $S(x),\,S(x)$ | $Z_0$ **invariant** | $n=1/\sqrt{S}$, $\delta n\approx+\tfrac14 A^2$ | $\Gamma=0$ **reflectionless** |
> | **ASYM** (static-$\mathbf E$; $\partial\mathbf B/\partial t=0\Rightarrow S_\mu=1$) | $S(x),\,1$ | $Z_0(1-A^2)^{-1/4}$ **varies** | $\delta n\approx-\tfrac14 A^2$ | $\Gamma\ne0$ **reflective** |

**SYM co-grade (the achromatic lens = gravity-as-graded-index).** Both grades sit at the same graded
$A_0(x)$, so the graded factor $S(A_0(x))$ **cancels in the impedance ratio**: $Z(x)=Z_0$ at every node
(the lattice pitch cancels, [`z0-derivation.md`](z0-derivation.md):37). The phase velocity is still
graded — the canonical Op16 ray/probe index is $n=1/\sqrt{S}>1$ ($\delta n\approx+\tfrac14 A^2$,
positive; the Schwarzschild-tracking shear channel $c_{shear}=c_0\sqrt{S}$ drops, light **slows**,
gravity-well-like; `manuscript/ave-kb/common/operators.md`:56) — but the node-to-node reflection
$\Gamma=(Z_{i+1}-Z_i)/(Z_{i+1}+Z_i)=0$ identically. This is exactly the
[**Achromatic Impedance Matching**](../../../vol3/gravity/ch03-macroscopic-relativity/achromatic-impedance-matching.md)
leaf (clm-rd9cjm): $\mu'=n\mu_0$, $\varepsilon'=n\varepsilon_0$ co-scale ⟹ $Z_0'=\sqrt{\mu'/\varepsilon'}\equiv
Z_0$. The achromatic leaf is the SYM limit of this graded network.

**ASYM static-E (the vacuum-impedance mirror).** A static $\mathbf E$ has no $\partial\mathbf B/\partial t$
to drive circulation, so it loads **only** the $\varepsilon$-sector: $S_\varepsilon(x)<1$, $S_\mu=1$
(the kernel-argument discipline — the $\mu$-kernel sees zero circulating $I$, so $S_\mu=1$ is **forced**,
not assumed). The Op14 Meissner-asymmetric form ([`operators.md`](../../../common/operators.md):54) gives
$Z(x)=Z_0\sqrt{S_\mu/S_\varepsilon}=Z_0(1-A_0(x)^2)^{-1/4}$, reproducing
[`vacuum-impedance-mirror.md`](../../falsification/ch11-experimental-bench-falsification/vacuum-impedance-mirror.md):80
exactly, with leading $\delta n=(1-A^2)^{1/4}-1\approx-\tfrac14 A^2$ (mirror:122). Now $Z(x)$ varies, so
adjacent cells are mismatched and reflect: $\Gamma_{node}\ne0$. The vacuum-impedance mirror is the ASYM
limit of the same graded network.

> **The two leaves are the symmetric and asymmetric limits of one result.** $Z$-invariance is a
> property of the **ratio** (both sectors co-scale); index/clock grading is a property of the
> **magnitude** (either sector dropping). Symmetry of the loading is the switch — not the gradient
> profile.

> **Index-sign convention (carried, not re-opened).** The R1 ray/probe index is $n=1/\sqrt{S}$
> (PR#359 / Grant call (a); clm-vca7r1, node-up leaf §3). The phase-velocity aside $c_{EM}=c_0/S$
> (which rises, carries no energy) is distinct from the propagating ray index — see node-up §3. This
> leaf uses the canonical ray index throughout.

## §3 — The macroscopic bridge: per-node $\delta n$ to the lab observable (Q3, load-bearing)

The per-node $\delta n$ is a **dimensionless local index**, not a per-node phase "kick." Optical phase
accumulates over **path length**: each node contributes $d\phi=(2\pi/\lambda)\,n\,\ell_{node}$, and there
are $1/\ell_{node}$ nodes per meter, so

$$
\frac{\phi}{\text{meter}} = \frac{2\pi}{\lambda}\,n
\qquad\Rightarrow\qquad
\phi = \frac{2\pi}{\lambda}\int n\,dl
$$

— **$\ell_{node}$ cancels EXACTLY** (the same cancellation as $v_g=c$,
[`z0-derivation.md`](z0-derivation.md):40,:49; and the lumped-section $c_0$ recovery,
[`per-dof-vacuum-node-circuit.md`](../../../vol9/ch3-pin-port-configuration/per-dof-vacuum-node-circuit.md):38).
The accumulation is the **standard coherent optical-path integral**, NOT a per-node $\times N$ multiplication
and NOT a $\sqrt{N}$ random walk: adjacent nodes sit at the **same** smooth pump operating point (the pump
varies on $\sim\mu$m $\gg\ell_{node}=3.86\times10^{-13}$ m; $\sim2.6\times10^6$ nodes per probe wavelength),
so the per-node phases add **coherently** (linear-in-path).

> **[Resultbox]** *The macroscopic accumulation law (reproduces OQ-1 canonical)*
>
> $$
> \psi = \tfrac12\cdot\frac{2\pi}{\lambda}\cdot g_{eff}\cdot|\delta n_{bir}|\cdot L,
> \qquad
> \delta n_{bir} = -\tfrac12\,(E/E_{yield})^2,
> $$
>
> where $g_{eff}$ folds the cavity **Fabry-Perot finesse build-up** ($2F/\pi$ effective coherent
> passes) — **NOT** a per-node $\times N$ count.

**This bridge is already canonical — this leaf re-grounds it, does not re-derive it.** The OQ-1
field→cavity-phase coupling is **DERIVED / CLOSED (2026-06-21)**: the coupling is the exact differential
of the scalar Axiom-4 kernel (uniaxial probe tensor → cavity round-trip ellipticity), with $g$ pinned
per apparatus config ([`claim-quality.md`](../../claim-quality.md):391 + 431; derivation
`research/2026-06-21_oq1-field-to-cavity-phase-coupling-derivation.md`; driver
`src/scripts/vol_9_device/oq1_field_to_cavity_phase_coupling.py`, validate-on-known PASS vs PVLAS
$A_e$ to 0.35%). The driver does **not** smuggle coherence — it explicitly models the pulsed-pump
temporal-overlap-vs-finesse tradeoff (recommended config = CW high-$F$ polarimeter where static
birefringence persists and full finesse accumulates).

> **The birefringence COEFFICIENT survives the node→macroscopic translation intact.** The matched
> differential ratio $\delta n_{AVE}/\delta n_{QED}=7.5/\alpha^3\approx1.93\times10^7$
> ([`claim-quality.md`](../../claim-quality.md):399, clm-pp3qwf) depends on **neither** the network
> dispersion nor the apparatus $g_{eff}$ ($g_{eff}$ cancels in the AVE/QED ratio). The only
> network-intrinsic correction is the field-independent $(q\ell_{node})^4$ photon birefringence
> ($\sim2\times10^{-22}$, §1.1), which is 15–21 OOM below the field signal ($|\delta n_{field}|\sim
> 3\times10^{-6}$ at PW-class focal $E$) **and** anisotropic-only (common-mode group/phase dispersion
> cancels in the par−perp differential). So band structure does **not** modify the lab E-route
> coefficient.

## §4 — Boundary reflection $\Gamma$ is set by co-grading SYMMETRY, not gradient profile (Q4)

A biased region of length $L$ with profile $A(x)$ is **not** a single interface — it is a **cascade of
lossless TL sections** (Axiom-3 reactive, no loss term). Each section $dx$ is a uniform line of local
impedance $Z(A(x))$ and wavenumber $\beta(x)=k_0 n(A(x))$. The graded input impedance marches from the
far-side termination (unbiased vacuum $Z_0$) back to the near boundary via the lossless ABCD/Kirchhoff
recursion:

$$
Z_{in} = Z_{sec}\,\frac{Z_{load}+jZ_{sec}\tan(\beta\,dx)}{Z_{sec}+jZ_{load}\tan(\beta\,dx)},
\qquad
\Gamma = \frac{Z_{in}-Z_0}{Z_{in}+Z_0}
$$

(the $z=3$ Kirchhoff cascade,
[`kirchhoff-network-method.md`](../../../vol1/axioms-and-lattice/ch1-fundamental-axioms/kirchhoff-network-method.md):16;
$\Gamma$ is the Op3 reflection primitive, [`operators.md`](../../../common/operators.md):43,
`src/ave/axioms/scale_invariant.py`:44; $dx$ is a computational knob, **not** $\ell_{node}$).

> **[Resultbox]** *The criterion is SYM-vs-ASYM, not abrupt-vs-graded*
>
> - **SYM co-grade** (soliton/gravity): $Z(x)=Z_0$ **everywhere** ⟹ every section matched ⟹ $Z_{in}=Z_0$
>   ⟹ $\Gamma=0$ **achromatic even for an ABRUPT $n$-jump** — light bends, never reflects. This is the
>   AVE-distinct null.
> - **ASYM static-E**: $Z(x)$ departs from $Z_0$ ⟹ $\Gamma\ne0\approx A^2/8$ at the interface, with
>   Fabry-Perot fringes (top-hat region) and **adiabatic-taper suppression** ($\Gamma$ falls $\sim L^{-2}$
>   as the ramp lengthens). $\;$Op17 power gate $T^2=1-\Gamma^2$ holds exactly (lossless reactive, Axiom 3).

The amplitude channel ($\Gamma$) and the phase/birefringence channel (§2–§3) share the **same** SYM/ASYM
discriminator axis. The achromatic Gamma=0 null re-grounds the
[**achromatic-lens-test**](../../falsification/ch11-experimental-bench-falsification/achromatic-lens-test.md)
boundary case network-up; the ASYM reflective branch re-grounds
[`vacuum-impedance-mirror.md`](../../falsification/ch11-experimental-bench-falsification/vacuum-impedance-mirror.md):80.

> **Echo half (flag-don't-fix, surfaced not reframed).** The *existence* of an ASYM boundary $\Gamma$ is
> **not** AVE-distinct: any electro-optic / graded-index dielectric ($\mu=\mu_0$, $\varepsilon(E)$ shifts)
> reflects $\sim|\delta n|/2$ by standard graded-TL optics. And the bench magnitude is undetectable
> (per-node $A\sim3.9\times10^{-9}$ at 43.65 kV / 100 µm ⟹ $|\Gamma|\sim10^{-17}$) — the same re-scope
> that retired the mirror-leaf 70-σ headline (mirror:16). The AVE-distinct content is (a) the
> cross-polarization **isotropy** — the kernel keys off $|E|$ so $\Gamma_\parallel=\Gamma_\perp$ — and
> (b) the $V^2$ tree-level slope vs the QED loop.

## §5 — Routes don't mix at network scale; the chiral circulator is a CATEGORY-ERROR guard (Q5)

At the network scale the $\varepsilon$-route (static-E) and $\mu$-route (static-B) do **not** mix, for
three independent structural reasons:

1. **Keyed-argument duality** (clm-vca7r1). The two grades key on **different** conjugate variables:
   $\varepsilon$-varactor on voltage $V$, $\mu$-relativistic-inductor on circulating current $I$
   ([`relativistic-inductor.md`](relativistic-inductor.md):15,:18,
   *"projections of the single Axiom 4 kernel onto the electric and magnetic sectors"*). A static $\mathbf E$
   has no $\partial\mathbf B/\partial t$ ⟹ $I_{vac}=0$ ⟹ $A_I=0$ ⟹ $S_\mu=1$ **EXACTLY**; a static
   $\mathbf B$ leaves $S_\varepsilon$ untouched. The static-field routes are **structurally decoupled**.
2. **Grade orthogonality** ($A1\perp T2$). The grades are orthogonal reactances, never wired into one
   shared $(V_{inc},V_{ref})$ phasor
   ([`device-circuit-models.md`](../../../vol9/ch3-pin-port-configuration/device-circuit-models.md):149,
   the genesis-24 / $w_{pol}=0$ double-count guard;
   [`master-equation.md`](../../../vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md):20).
3. **No magnetoelectric term exists.** A grep of `src/ave` for any $\chi_{me}$ / E-induces-B / magnetoelectric
   cross-term returns **zero** hits.

> **[Resultbox]** *CATEGORY-ERROR GUARD — the chiral circulator is NOT the $\varepsilon$/$\mu$ route-coupling*
>
> The chiral circulator / $H_{couple}=\tilde\kappa\!\int g\,V\,\Omega_w$ (`src/ave/core/cross_sector_coupling.py`:76,
> [`device-circuit-models.md`](../../../vol9/ch3-pin-port-configuration/device-circuit-models.md):159–165)
> wires the **MECHANICAL bulk (A1 / mass-"3") grade** to the **shear (Cosserat / charge-"3") grade** —
> **NEITHER** of which is the $\varepsilon$-varactor or the $\mu$-inductor of the EM-transverse port. The
> EM port couples to the mechanical domain only through an **ideal transformer** ($\xi_{topo}^2$,
> `node_2domain_nport.py`), which scales an across/through pair losslessly and **cannot** convert a
> C-state ($V$) into an L-state ($I$). Citing the chiral circulator as the route-coupling element is a
> **category error** — it is inter-sublattice / inter-grade, not inter-$\varepsilon$/$\mu$, and its
> magnitude is un-computed (STATED-pending-engine, `cvr_model.py`:243, `open_ambiguity:true`).

**Consequence:** route-separability of the single-node fork is **PRESERVED at network scale**, and the
static-B-transparent verdict (R3, $\delta n_\mu=0$; clm-pvlas1) is **ROBUST**. The SYM case (both sectors
scale together) is **not** route-mixing but a **joint external drive** of both sectors (a soliton carrying
internal $\mathbf E$ **and** $\mathbf B$), not an E-bias inducing a $\mu$-response.

> **Out-of-scope-not-disproven (surfaced).** The route-cleanness chord is rigorous for the **static**
> drive and the verified network couplings on `main`. It is NOT a proof that no $\varepsilon$-$\mu$
> coupling can exist under a **time-varying** drive (a transformer + circulator under AC could in
> principle open higher-order paths) — but no such term is in the verified corpus.

## §6 — Chord-vs-echo ledger (symmetric-standard applied)

Per network-level prediction, asking *would SM / standard-optics / effective-medium give the same?*

| # | Network prediction | Class | Note |
|---|---|---|---|
| 1 | $c_{EM}=c_0$, $Z_0=376.73\,\Omega$ from the LC-ladder continuum limit | **ECHO** | any discrete LC ladder / TLM / phonon lattice recovers these; validate-on-known against known anchors |
| 2 | Leading $(q\ell_{node})^2$ **scalar** ladder dispersion | **ECHO** | generic to any discrete ladder; SM lattice-QFT has cutoff dispersion too |
| 3 | Photon's first anisotropy is **QUARTIC** $(q\ell_{node})^4$ (cubic harmonic) | **CHORD** (form) | AVE-distinct: K4 makes the 2nd moment exactly isotropic $(4/3)\mathbb{I}$ while the 4th carries the anisotropy. SCOPE: chord only because cubic/tetrahedral; magnitude imported (per-dof:71) |
| 4 | SYM $\Rightarrow Z=Z_0$ **achromatic $\Gamma=0$** reflectionless lens | **CHORD** (mechanism) / ECHO (value) | a co-doped $\mu_r=\varepsilon_r$ metamaterial also gives $\Gamma=0$; the AVE-distinct content is which physical drive (symmetric internal $\mathbf E$&$\mathbf B$ = gravity) realizes it + the cross-pol isotropy $\Gamma_\parallel=\Gamma_\perp$ |
| 5 | ASYM static-E $\Rightarrow Z_0(1-A^2)^{-1/4}$, $\Gamma\ne0$ reflective mirror | **ECHO** (form) | an $\varepsilon$-only graded medium reflects in standard EM; the AVE-distinct content is the COEFFICIENT (row 6) |
| 6 | Birefringence COEFFICIENT $\delta n_{AVE}/\delta n_{QED}=7.5/\alpha^3\approx1.93\times10^7$ | **MIXED** | CHORD = the vacuum saturates at all at tree-level $O(1)$ (vs QED's $\alpha^2$-loop); ECHO = the magnitude $7.5/\alpha^3$ is an $\alpha$-echo at the value level (claim-quality.md:399,405). Survives the macroscopic bridge intact (§3) |
| 7 | Static-B $\delta n_\mu=0$ **EXACTLY** at any field (R3) | **CHORD** | categorical: QED predicts a tiny nonzero static-B birefringence, AVE predicts exactly zero. Analytically exact (kernel argument identically zero); the cleanest network chord (clm-pvlas1) |

## §7 — Derived-vs-asserted ledger

| Element | Status | Basis |
|---|---|---|
| $c_{EM}=c_0$, $Z_0=376.73\,\Omega$ from continuum limit | **DERIVED** (validate-on-known) | LC-ladder section + $\ell_{node}$ cancellation (z0-derivation:37) |
| $(q\ell_{node})^2$ ladder dispersion FORM | **DERIVED** | KCL/KVL on lossless ladder (standard) |
| K4 2nd-moment $(4/3)\mathbb{I}$ isotropic, 4th-moment cubic-harmonic anisotropic | **DERIVED** | tetrahedral bond-set moments (preferred-frame:48,:50) |
| $(q\ell_{node})^4$ anisotropy **MAGNITUDE** ($\sim2.2\times10^{-22}$ optical, $3.5\times10^{-39}$ @ 30 GHz) | **IMPORTED** | per-dof:71 "magnitude NOT re-derived; only the FORM"; #359-corrected microwave figure |
| SYM $\Rightarrow Z=Z_0$ reflectionless, $\delta n\approx+\tfrac14 A^2$ | **DERIVED** | impedance ratio cancellation; achromatic leaf (clm-rd9cjm), INVARIANT-S2 W6 |
| ASYM static-E $\Rightarrow Z_0(1-A^2)^{-1/4}$, $\delta n\approx-\tfrac14 A^2$, $\Gamma\ne0$ | **DERIVED** | Op14 Meissner-asymmetric (operators.md:54); mirror:80,:122 |
| Macroscopic bridge: $\ell_{node}$-invariant coherent optical-path integral; coefficient survives | **DERIVED** (re-grounds OQ-1) | OQ-1 CLOSED 2026-06-21 (claim-quality.md:391,431); $\ell_{node}$ cancels (z0-derivation:40,:49) |
| R3 static-B $\delta n_\mu=0$ exact; routes decoupled at network scale | **DERIVED** (analytically exact) | $I$-keyed inductor + Lenz (clm-vca7r1, clm-pvlas1) |
| Birefringence-coefficient MAGNITUDE $1.93\times10^7=7.5/\alpha^3$ | **$\alpha$-ECHO** (value) | claim-quality.md:399,405 self-adjudicated; existence/tree-level $O(1)$ = chord |
| no-LIV / continuum-limit decoupling theorem ($\delta=0$ exactly) | **ASSERTED-OPEN** | gate `wejkhvnfb` (preferred-frame:66); weak-C honest-scope, NOT derived |
| chiral-circulator route-coupling MAGNITUDE | **ASSERTED-pending-engine** | device-circuit-models:163, cvr_model.py:243 (cubic-FDTD averages chirality out); NOT computed |

> **Consistency-vs-emergence tag.** This leaf is **CONSISTENCY class** (matches the per-DOF and
> device-network tags). It re-expresses the already-derived Axiom-4 kernel + LC-ladder + the single-node
> regime taxonomy (clm-vca7r1) as the network-scale response. It originates **no** new dimensionful
> constant: $c_0$/$Z_0$ are validate-on-known anchors; $\alpha$, $m_e$ are NOT predicted. The AVE-distinct
> **chords** are FORM-level (the $(q\ell_{node})^4$ quartic anisotropy, the achromatic $\Gamma=0$ null, the
> exactly-zero static-B birefringence, route-cleanness); the **echoes** are $c_{EM}=c_0$, $Z_0$, the scalar
> $(q\ell_{node})^2$ ladder dispersion, and the birefringence-coefficient magnitude.

> **VCA-R12 (code-is-not-the-lattice).** This leaf is an **analytic** derivation — no FDTD run is read AS
> the lattice. The five-element match-table closes on the analytic leg: kernel-arg per sector (VCA-R01:
> $\varepsilon\to V$, $\mu\to$ circulating $I$, never $\mu_0|H|$; relativistic-inductor.md:18); stencil =
> K4 tetrahedral $z=3$ bond set (kirchhoff-network-method.md:16); drive = static-E asymmetric / SYM
> internal; probe = the impedance-ratio + optical-path phase; constants from `src/ave/core/constants.py`
> ($Z_0$, $\ell_{node}$, $V_{yield}$, $I_{max}=124.4$ A). The live VCA-R01 engine bug
> (`fdtd_3d.py`:231 keys $\mu$ on static $|\mathbf B|$) is **independent** of this analytic leaf — see the
> node-up leaf §5 — and is **not** touched or rescued here.

---
