[↑ Ch.1 Vacuum Circuit Analysis](index.md)

<!-- kb-frontmatter
kind: leaf
claims: [clm-vca7r1]
-->

## Node-Up Small- and Large-Signal Response of the Vacuum LC Tank

The substrate cell is a single LC tank. Its two reactive grades respond to **different
drive variables**: the capacitive ($\varepsilon$) grade is a **varactor keyed on VOLTAGE**
$V$ (field $E$), while the inductive ($\mu$) grade is a **relativistic inductor keyed on the
circulating CURRENT** $I$ ([`relativistic-inductor.md`](relativistic-inductor.md):15,:18,
substitution $V\to I$). This duality — same Axiom-4 kernel, two different keyed arguments —
fixes the **operating-point** (large-signal) state of each grade independently, and therefore
fixes the **small-signal** index a probe sees. The asymmetry under a *static external* field
is the load-bearing consequence: a static $\mathbf{B}$ leaves the $\mu$ grade unloaded.

> **Derivation provenance.** The node-up V/I-keyed dual, the three-regime sweep with numbers, the
> rescue-guard, and the deferred VCA-R01 code-bug are derived in
> [`research/2026-06-22_node-up-small-large-signal_result.md`](../../../../../research/2026-06-22_node-up-small-large-signal_result.md)
> (FORK-1 resolution). The C4 / INVARIANT-S2 reconciliation behind §4 is in
> [`research/2026-06-22_c4-symmetric-loading-reconciliation.md`](../../../../../research/2026-06-22_c4-symmetric-loading-reconciliation.md).

## §0 — The node as a MULTI-PORT LC tank (6 DOF → ports → sectors)

> **[Resultbox — ADDITIVE, CONSISTENCY-class] The node is a multi-port LC tank.** The two-keyed-reactance
> picture of §1 is the $\varepsilon$/$\mu$ slice of a richer object: by **Axiom 1** each K4 node carries
> **6 spatial DOFs** (3 translational $\to\mathbf E$, 3 microrotational $\to\mathbf B$;
> [`manuscript/ave-kb/CLAUDE.md`](../../../CLAUDE.md):73), each an LC resonator, **plus** the saturation-state
> $A$ per tank — *the operating point* "analogous to DC bias on a semiconductor varactor"
> ([`manuscript/ave-kb/CLAUDE.md`](../../../CLAUDE.md):75 verbatim). Grouping the DOFs by which reactance and
> which sector they project to gives the **port map** (this is a re-expression of the canon, NOT a new DOF
> count — the 6 DOFs and the $A$-state are exactly Axiom 1 + the §75 operating-point state):

| Port / sector | DOF group (Ax 1) | Reactance role | Sat. factor at operating point $A$ | Effective param (verbatim `CLAUDE.md`:73,:75) |
|---|---|---|---|---|
| **MASS** — A1 dilatation | trace-of-translation (the $A_1$ breathing "3", longitudinal-V scalar) | longitudinal bond compliance $\to Z_{\mathrm{bulk}}$ | $S_{A_1}(A)$ | $C_{eff}=C_0/S(A)$ (the A1 stretch-compliance, ↑) |
| **CHARGE** — Cosserat micro-rotation (MECHANICAL) | the 3 microrotational $(2,3)$ winding "3" (Cosserat couple-stress / curvature grade) | **static reactive charge boundary** $\to Z_{\mathrm{shear}}$ (mechanical, $\rho\,c_{shear}$, Pa·s/m; the deformation-invariant $\mathrm{Link}$, lossless) | $S_{shear}(A)$ | $c_{shear}=c_0\sqrt{S}$ (the shear-grade speed) |
| **$\varepsilon$** — capacitive / electric (EM) | translational $\to\mathbf E$ (displacement / Coulomb) | transverse-T2 permittivity of $Z_{\mathrm{EM}}$ | $S_\varepsilon(A_V)$ | $\varepsilon_{eff}=\varepsilon_0 S(A)$ |
| **$\mu$** — magnetic constitutive (EM) | (param of the EM channel; sourced by the micro-rotation→$\mathbf B$ coupling, Ax 1) | inductive permeability of $Z_{\mathrm{EM}}=\sqrt{\mu_{eff}/\varepsilon_{eff}}$ — **Meissner lives here** | $S_\mu(A)$ | $\mu_{eff}=\mu_0 S(A)$ |
| **deviatoric-shear** — transverse-mechanical | traceless translation (deviatoric $G$) | transverse acoustic $\to Z_{\mathrm{shear}}$ | $S_{shear}(A)$ | $c_{shear}=c_0\sqrt{S}$ |

> **SECTOR-HEADER (read before using this table).** Which sector? — the table spans the substrate roles
> (MASS / CHARGE / $\varepsilon$ / $\mu$ / deviatoric-shear) across **two DOMAINS**: the MASS, CHARGE, and
> deviatoric-shear rows are **mechanical** ($Z_{\mathrm{bulk}}$, $Z_{\mathrm{shear}}$ — $\rho\times$speed,
> Pa·s/m), the $\varepsilon$ and $\mu$ rows are the **EM** constitutive params of
> $Z_{\mathrm{EM}}=\sqrt{\mu_{eff}/\varepsilon_{eff}}$ ($\Omega$). (The CHARGE micro-rotation winding and the
> deviatoric-shear translation are two distinct mechanical DOFs that both terminate on $Z_{\mathrm{shear}}$ —
> the charge "3" is the static-reactive $\mathrm{Link}$ boundary, the deviatoric-shear is the transverse
> acoustic wave.) Each row is tagged. Does the engine carry that DOF? — yes (3+3 spatial DOFs are the Master-Equation / Cosserat fields;
> the $A$-state is the saturation operating point, Op14/Op16). Cold or saturated? — the *columns* are the
> per-sector **saturation factors $S_\bullet(A)$**; the cold node is $A=0\Rightarrow S=1$ on every port. The
> effective parameters modulate with $S(A)$ exactly as `CLAUDE.md`:73,:75 give them: $\varepsilon_{eff}=\varepsilon_0 S$,
> $\mu_{eff}=\mu_0 S$, $C_{eff}=C_0/S$. **Two-"3"s guard:** the MASS row (A1 dilatation) and the CHARGE row
> (Cosserat $(2,3)$ micro-rotation) are **orthogonal grades** ($A1\perp T2$,
> [`master-equation.md`](../../../vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md):20) — distinct
> ports, never wired into one $(V_{inc},V_{ref})$ phasor (the genesis-24 no-double-count). The
> $C_{eff}=C_0/S$ (↑, A1 compliance) vs $\varepsilon_{eff}=\varepsilon_0 S$ (↓, T2 permittivity) split is the
> Grant-ratified sector split, NOT a sign error (`CLAUDE.md`:73).
>
> **DOMAIN-SEPARATION guard (units discipline, `resonant-lc-solitons.md`:120,:124,:129).** The CHARGE sector is
> the **MECHANICAL** Cosserat $(2,3)$ micro-rotation — the **static reactive charge boundary**
> ($\mathrm{Link}(\partial\Omega,F)\in\mathbb{Z}$, lossless, no real power, `resonant-lc-solitons.md`:124) whose
> saturation modulation is the **mechanical shear** $c_{shear}=c_0\sqrt{S}$ (deviatoric $G$), routed to
> $Z_{\mathrm{shear}}$ ($\rho\times$speed, Pa·s/m). It is **NOT** $\mu_{eff}=\mu_0 S$ — $\mu$ is the **EM**
> magnetic constitutive parameter (a param of $Z_{\mathrm{EM}}$, $\Omega$), its own row above. **The bridge
> between them is a TRANSDUCER, not a direct wire:** the Axiom-1 **micro-rotation$\leftrightarrow\mathbf B$**
> coupling (`CLAUDE.md`:71, "3 microrotational $\to\mathbf B$") read through the **TKI-transducer**
> ([def-tk1xfm](../../../common/vocabulary-register.md), Axiom-2 electromechanical dictionary, $\omega$/curl
> $\leftrightarrow\mathbf B$) is the candidate bridge — but def-tk1xfm is `status:proposed`-not-ratified and
> carries the *"identity-by-translation, NOT a derivation"* ceiling (`resonant-lc-solitons.md`:129) — **FLAGGED,
> not asserted as derived.** Do NOT direct-wire $\mu_{eff}$ onto the mechanical $Z_{\mathrm{shear}}$.

This multi-port view is the **node-constitutive companion** to the per-DOF *mechanical-translation* tensor of
[`per-dof-vacuum-node-circuit.md`](../../../vol9/ch3-pin-port-configuration/per-dof-vacuum-node-circuit.md)
(which refines only the 3 translation DOFs into a directional $(L_i,C_i)$ tensor): this table instead groups
**all 6 DOFs + the $A$-state** by *sector / port*, the axis that carries the MASS / CHARGE / $\varepsilon$ / $\mu$
roles. The two leaves are the same node read on two orthogonal axes (per-direction vs per-sector); neither is a
new primitive. **Consistency-vs-emergence: CONSISTENCY** — it re-expresses Axiom 1 + the §75 operating-point
state + the §73 varactor specialization; it originates no new dimensionful number.

## §1 — The LC-tank node and the two keyed reactances

Each substrate cell is a resonant LC tank ($L_{cell}=\mu_0\ell_{node}$, $C_{cell}=\varepsilon_0\ell_{node}$,
$\omega_C = 1/\sqrt{L_{cell}C_{cell}} = c_0/\ell_{node}$). Both reactive elements saturate through
the **single** Axiom-4 kernel $S(A)=\sqrt{1-(A/A_{yield})^2}$, but they are keyed on **different**
drive variables:

> **[Resultbox]** *The keyed-argument duality*
>
> $$
> \underbrace{C_{eff}(V) = \frac{C_0}{S(A_V)}, \quad A_V = \frac{V}{V_{yield}}}_{\varepsilon\text{-grade: VARACTOR, keyed on VOLTAGE}}
> \qquad\qquad
> \underbrace{L_{eff}(I) = \frac{L_0}{S(A_I)}, \quad A_I = \frac{I}{I_{max}}}_{\mu\text{-grade: RELATIVISTIC INDUCTOR, keyed on CURRENT}}
> $$
>
> with $V_{yield}\approx 43.65$ kV and $I_{max}=\xi_{topo}\,c\approx 124.4$ A
> ([`relativistic-inductor.md`](relativistic-inductor.md):15,:18).

The two forms are the same kernel under the substitution $V\to I$, $V_{yield}\to I_{max}$ — *"both
are projections of the single Axiom 4 kernel onto the electric and magnetic sectors,
respectively"* ([`relativistic-inductor.md`](relativistic-inductor.md):18). The physically
load-bearing fact is **which argument keys which grade**:

- The $\varepsilon$-grade (capacitive / transverse-T2 permittivity) responds to the **field
  amplitude** $V\sim E$ — a *potential* variable. A DC bias is a real operating point.
- The $\mu$-grade (microrotational / Cosserat-B inductive) responds to the **circulating
  current** $I$ — a *rate/flux* variable, $I\propto \oint \mathbf H\cdot d\boldsymbol\ell$ sustained
  by the vacuum's own circulation. By Lenz, internal circulation is induced only by $\partial\mathbf
  B/\partial t \ne 0$; a *static* external $\mathbf B$ (sustained by the magnet's current, not the
  vacuum's) carries no $dI/dt$ and induces **no** internal vacuum circulation.

> **Coordinate discipline (A46).** The kernel arguments $A_V$, $A_I$ are **phase-space / reactance**
> quantities (operating-point along the Axiom-4 arc), not real-space lattice-Cartesian field
> magnitudes. The $\mu$-grade is loaded by the *circulation* $I$, not by $|\mathbf B|$ at a cell.
> A test (or solver) that keys $\mu$-saturation on the static $|\mathbf B|$ magnitude measures the
> wrong coordinate — see §4 and the VCA-R01 code note in §5.

$B_{SNAP}=1.89\times10^9$ T is **not** a rival kernel argument for the $\mu$-grade: it is an
**energy-density** scale, fixed by $B_{SNAP}^2/2\mu_0 = m_ec^2/\ell_{node}^3 = 1.0$ (exactly the
soliton rest-energy density). The $\mu$-grade saturates on $I/I_{max}$, not $B/B_{SNAP}$.

## §2 — Large-signal operating point per grade (the three regimes R1/R2/R3)

The operating point is the large-signal state $(S_\varepsilon, S_\mu)$ the two grades settle into
under a given drive. Three regimes span the cases relevant to gravity, the bench, and the magnet (the
full per-regime sweep with numbers is tabulated in
[`research/2026-06-22_node-up-small-large-signal_result.md`](../../../../../research/2026-06-22_node-up-small-large-signal_result.md):§3):

| Regime | Drive | $S_\varepsilon$ | $S_\mu$ | $Z_{eff}$ | Small-signal $\delta n$ |
|---|---|---|---|---|---|
| **R1** symmetric internal | both grades (internal $\mathbf E$ **and** $\mathbf B$, e.g. mass-soliton) | $S$ | $S$ | $Z_0\sqrt{\mu_0 S/\varepsilon_0 S}=Z_0$ (invariant) | $n=1/\sqrt{S}$, $\delta n\approx+\tfrac14 A^2$ (isotropic; reflectionless) |
| **R2** static-E route | static $\mathbf E$ only ($\partial\mathbf B/\partial t=0$) | $<1$ | $1$ | $Z_0\sqrt{S_\mu/S_\varepsilon}=Z_0/\sqrt{S_\varepsilon}$ (changes) | $\delta n\approx-\tfrac14(E/E_{yield})^2$ (isotropic, common-mode; $\Gamma\ne0$) |
| **R3** static-B | static $\mathbf B$ only ($\partial\mathbf B/\partial t=0$) | $1$ | $1$ (no internal circulation) | $Z_0$ (unchanged) | $\delta n_\mu = 0$ **EXACTLY** |

- **R1 (symmetric internal loading)** is the canonical INVARIANT-S2 W6 operating point
  (`manuscript/ave-kb/CLAUDE.md`:75): when *both* sectors are driven, $S_\varepsilon=S_\mu=S$, so
  $Z=Z_0$ stays invariant and the boundary is reflectionless — Symmetric Gravity. A small-signal
  probe sees the common-mode (canonical ray/probe) index $n=1/\sqrt{S}$ ⟹ $\delta n=1/\sqrt{S}-1\approx
  +\tfrac14 A^2$ (canonical Op16 ray speed $c_{shear}=c_0\sqrt{S}$ drops; light slows, gravity-well-like;
  `operators.md`:56).
- **R2 (static-E / bench / HIBEF route)** is the Op14 Meissner-asymmetric case: a static $\mathbf E$
  has no $\partial\mathbf B/\partial t$ to load the $\mu$ grade, so it loads $\varepsilon$ only.
  $Z$ changes → $\Gamma\ne0$ → the vacuum-impedance-mirror bench mechanism. This is the **E-route**,
  and it is where the leading $\delta n\approx\tfrac14 A_V^2$ (and the OQ-1 par−perp differential
  $-\tfrac12 A_V^2$) lives. **Analytic V-keyed (varactor) law:** $S_\varepsilon=\sqrt{1-A_V^2}$,
  $S_\mu=1$ ⟹ $\delta n=\sqrt{S_\varepsilon}-1\to-\tfrac14 A_V^2$ to leading order
  ($A_V=E/E_{yield}$, $\mu$ unloaded). Direct-kernel positive control (evaluates the kernel, NOT
  the fdtd engine): `src/tests/test_vca_node_regime_sweep.py` (R2 sweep $E=10^{12}$–$10^{17}$ V/m;
  leading coefficient computed $=\tfrac14$).
- **R3 (static-B)** is the magnet case. $\partial\mathbf B/\partial t = 0$ ⟹ no internal vacuum
  circulation ⟹ $I_{vac}=0$ ⟹ $A_I=0$ ⟹ $S_\mu=1$ ⟹ $\mu_{eff}=\mu_0$ ⟹ $\delta n_\mu = 0$
  **analytically exact**. This is "flat" across $2.5\,\text{T}\to1\,\text{kT}$ **trivially**: the
  kernel argument $A_I=I_{vac}/I_{max}$ is *identically zero* under a static $\mathbf B$, so
  $S_\mu=\sqrt{1-0^2}=1$ at **every** field strength — not a numerical finding but a consequence of
  the $\mu$-grade being keyed on circulation, not $|\mathbf B|$. Direct-kernel positive control
  (evaluates the Axiom-4 kernel directly, NOT the fdtd engine): `src/tests/test_vca_node_regime_sweep.py`
  ($S_\mu=1$, $\delta n_\mu=0$ at $B=2.5,10,50,100,500,1000$ T).

## §3 — Small-signal probe → $\delta n$

A weak probe wave through a region held at operating point $(S_\varepsilon, S_\mu)$ sees the
linearized effective parameters $\varepsilon_{eff}=\varepsilon_0 S_\varepsilon$,
$\mu_{eff}=\mu_0 S_\mu$. The transverse-EM index is

$$
n = \frac{c_0}{c_{EM}} = \sqrt{\frac{\varepsilon_{eff}\,\mu_{eff}}{\varepsilon_0\,\mu_0}}
  = \sqrt{S_\varepsilon\, S_\mu}, \qquad
Z_{eff} = Z_0\sqrt{\frac{S_\mu}{S_\varepsilon}}.
$$

- **R1:** $S_\varepsilon=S_\mu=S$. The **canonical ray/probe observable** is the Op16 universal wave
  speed $c_{shear}=c_0\sqrt{S}$ ⟹ probe index $n=1/\sqrt{S}$, $\delta n=1/\sqrt{S}-1\approx+\tfrac14 A^2$
  (positive; light slows, gravity-well-like; `operators.md`:56). $Z_{eff}=Z_0$ (reflectionless,
  common-mode only). *(Phase-velocity aside, not the probe observable: the transverse-EM Maxwell
  **phase** index is $n_{EM}=\sqrt{S_\varepsilon S_\mu}=S$, i.e. phase velocity $c_{EM}=c_0/S$ which
  **rises** above $c_0$ and carries no energy — distinct from the canonical ray/probe index
  $n=1/\sqrt{S}$. The reciprocal "both-reactance signal" form $n=1/S$, $\delta n\approx+\tfrac12 A^2$
  is **rejected** — it propagates nothing; the universal propagating-wave speed is $c_0\sqrt{S}$ per
  Op16, not $c_0 S$.)*
- **R2:** $S_\varepsilon=S<1$, $S_\mu=1$ ⟹ $n=\sqrt{S}$, $\delta n_{iso}=\sqrt{S}-1\approx-\tfrac14
  A_V^2$ (isotropic), and $Z_{eff}=Z_0/\sqrt{S}$ ⟹ $\Gamma\ne0$. Under a linearly-polarized pump the
  $\varepsilon$-grade response is uniaxial, giving the OQ-1 birefringence
  $\delta n_{bir}=n_\parallel-n_\perp\approx-\tfrac12 A_V^2$ (clm-pp3qwf,
  [`vacuum-birefringence-e4.md`](../../falsification/ch12-falsifiable-predictions/vacuum-birefringence-e4.md)).
- **R3:** $S_\mu=1$ and (static-B-only) $S_\varepsilon=1$ ⟹ $n=1$, $\delta n_\mu = 0$ exactly,
  $Z_{eff}=Z_0$ — the vacuum is **transparent** to a static $\mathbf B$.

## §4 — The static-field asymmetry result

The keyed-argument duality forces an **asymmetry between the two static-field routes**:

> **[Resultbox]** *Static-field grade asymmetry*
>
> $$
> \boxed{\;\text{static } \mathbf E:\ S_\varepsilon < 1,\ S_\mu = 1\ \Rightarrow\ \delta n\ne0\ (\text{E-route})
> \qquad
> \text{static } \mathbf B:\ S_\varepsilon = 1,\ S_\mu = 1\ \Rightarrow\ \delta n = 0\ \text{EXACTLY}\;}
> $$

A static $\mathbf E$ is a real operating-point bias for the $V$-keyed varactor — it loads
$\varepsilon$ and shifts $n$. A static $\mathbf B$ ($\partial\mathbf B/\partial t = 0$) is **not** an
operating point for the $I$-keyed inductor: with no $dI/dt$ there is no induced internal vacuum
circulation, so $A_I=0$, $S_\mu=1$, $\mu_{eff}=\mu_0$, and the $\mu$-grade contributes **nothing**
to the index. The vacuum stays at $Z_0$ and is transparent.

This is the substrate reason behind two corpus-level consequences, canonicalized in the sibling
falsification leaf:

1. **PVLAS / BMV null is CONSISTENT with AVE** (not a falsification): those instruments apply a
   *static* (or quasi-DC) $\mathbf B$ and read birefringence. AVE predicts $\delta n_\mu = 0$ under
   static $\mathbf B$, so a null is the *expected* AVE result — see
   [`pvlas-static-b-verdict.md`](../../falsification/ch11-experimental-bench-falsification/pvlas-static-b-verdict.md).
2. **The real test is the E-route** (HIBEF-class facility field), where the $V$-keyed varactor is
   genuinely biased (R2), giving the OQ-1 differential coefficient $7.5/\alpha^3\approx1.93\times10^7$
   vs differenced Euler-Heisenberg. The facility landscape for this E-route test (HIBEF + the PW-laser
   field sources, with the magnetic-route facilities noted as **not** testing AVE) is surveyed in
   [`research/2026-06-22_vacuum-birefringence-facility-tolerance-survey.md`](../../../../../research/2026-06-22_vacuum-birefringence-facility-tolerance-survey.md).

The same asymmetry resolves the W6 / H3 tension flagged in the 2026-06-05 gravity-sign prereg: the
canonical "DC bias scales both grades" form is the **R1 symmetric-internal** operating point, NOT a
claim that *any* DC bias scales both; a static-external single-grade drive is R2 (E) or R3 (B).

## §4a — Meissner = the EM μ-sector shorting at saturation (EMERGENT, not bolted on)

> **SECTOR-HEADER.** Sector: the **EM $\mu$ (magnetic constitutive) sector** — a parameter of the EM channel
> $Z_{\mathrm{EM}}=\sqrt{\mu_{eff}/\varepsilon_{eff}}$ ($\Omega$), keyed (Ax 1) on the **mechanical** Cosserat
> micro-rotation circulation via the transducer below. Regime: the **saturated** large-signal operating point
> ($A\to A_{yield}$, the superconducting/yielded state). Mode: inductive (magnetic), **EM domain**. This
> subsection touches NEITHER the $\varepsilon$ param NOR the A1 dilatation-MASS port. **Domain note
> (`resonant-lc-solitons.md`:129):** Meissner is an event in the **EM** $\mu$-sector ($\mu_{eff}\to0$), NOT the
> mechanical micro-rotation channel $Z_{\mathrm{shear}}$ shorting; the two are bridged by a **transducer**, not a
> direct wire (see the transducer box below).

When the EM $\mu$-sector saturates, its effective inductive permeability rolls to zero,
$$\mu_{eff}=\mu_0\,S(A)\ \xrightarrow[A\to A_{yield}]{}\ 0 .$$
An EM channel with $\mu_{eff}\to0$ is an **inductive short**: $Z_{\mathrm{EM}}=\sqrt{\mu_{eff}/\varepsilon_{eff}}\to0$,
the magnetic-flux channel reflects at $\Gamma=-1$ and flux is **excluded** from the bulk. That is *exactly* the
**Meissner effect** — read here as a circuit event in the EM $\mu$-sector, not a separately-postulated mechanism:

> **[Resultbox] Meissner = the saturated EM μ-sector.** $\mu_{eff}=\mu_0 S(A)\to0$ at saturation $\Rightarrow$
> the EM inductive ($\mu$) channel shorts ($Z_{\mathrm{EM}}\to0$) $\Rightarrow$ applied flux reflects at
> $\Gamma=-1$ $\Rightarrow$ total expulsion of $\mathbf B$. This **falls out of the Axiom-4 saturation kernel
> acting on the EM $\mu$-sector** (keyed on the micro-rotation circulation, asymmetric loading $S_\mu<1$ while
> $S_\varepsilon$ held); it is EMERGENT, not bolted on
> ([`phase-transitions-impedance.md`](../../../vol3/condensed-matter/ch11-thermodynamics/phase-transitions-impedance.md):24
> verbatim: "when $\mu_{eff}\to0$ at saturation (Axiom 4), the magnetic field cannot penetrate the bulk.
> Applied magnetic flux reflects completely at the boundary ($\Gamma=-1$) … total expulsion of the B-field").

> **[Transducer box — FLAGGED, not asserted] The EM μ-sector is keyed to the mechanical micro-rotation by a
> TRANSDUCER, not a direct wire (`resonant-lc-solitons.md`:129).** The $\mu$-sector that shorts above is the
> **EM** magnetic constitutive parameter ($\mu_{eff}$, a param of $Z_{\mathrm{EM}}$, $\Omega$). The **CHARGE**
> sector is the **MECHANICAL** Cosserat $(2,3)$ micro-rotation — the static reactive charge boundary routed to
> $Z_{\mathrm{shear}}$ ($\rho\times$speed, Pa·s/m, `resonant-lc-solitons.md`:120,:124). These live in **different
> DOMAINS**, so the coupling that lets a mechanical micro-rotation *circulation* load the EM $\mu$ is the
> **Axiom-1 micro-rotation$\leftrightarrow\mathbf B$** map (`CLAUDE.md`:71, "3 microrotational $\to\mathbf B$")
> read through the **TKI-transducer** ([def-tk1xfm](../../../common/vocabulary-register.md), the Axiom-2
> electromechanical dictionary, $\omega$/curl $\leftrightarrow\mathbf B$). def-tk1xfm is
> `status:proposed`-not-ratified and carries the *"identity-by-translation, NOT a derivation"* ceiling
> (`resonant-lc-solitons.md`:129) — this bridge is **FLAGGED as a candidate, not asserted as derived**. Do NOT
> direct-wire $\mu_{eff}$ onto $Z_{\mathrm{shear}}$.

**Port-level orthogonality — why the Meissner (EM μ) sector cannot confine the mass port.** The MASS port is the
**A1 dilatation** (trace-of-translation, the longitudinal-V "3"); the Meissner sector is the **EM $\mu$** param,
keyed (via the transducer above) on the **Cosserat $(2,3)$ micro-rotation** circulation. These are
**orthogonal grades**: $A1\perp T2$
([`master-equation.md`](../../../vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md):20). At the
port level this is *translation-dilatation* $\perp$ *rotation-micro-rotation* — **different DOFs** — so the
EM $\mu$-sector (Meissner) has **no handle on the dilatation (mass) port**. This is the **resolved scoping verdict**:
the reading "the $(2,3)$ micro-rotation Meissner-confines the A1 mass" is **forbidden / falsified** (mass = A1,
PR#260; the two-"3"s are orthogonal sectors, never a nesting). Recorded as the verdict — **NOT re-asserted as a
nesting**.

> **PENDING / OPEN (no-overclaim, NOT done).** Whether a *transverse* self-Meissner (FORK-A) is realized in the
> electron is **UNVERIFIED** — it is an open build, flagged here, not a derived result. **The self-Meissner is a
> TRANSDUCED phenomenon** (this sharpens, not contradicts, the picture): the electron's own **mechanical**
> Cosserat micro-rotation *circulation* $\to\mathbf B$ (Ax-1 / def-tk1xfm transducer) $\to$ asymmetric load
> $\mu_{eff}\to0$ $\to$ $\Gamma=-1$ flux exclusion — i.e. the build runs *mechanical circulation $\to$ EM
> $\mu$-sector*, NOT a $\mu$-on-$Z_{\mathrm{shear}}$ direct wire. charge=Link STANDS; both internal dynamical
> loci tested NEGATIVE (#415, #417); the electron's two-natured structure is **two orthogonal self-confining
> sectors** (A1-mass + Cosserat-charge), **NOT** a charge-holds-mass nesting. CONSISTENCY-class re-expression of
> canon only; FORK-A + the $\alpha$-flip stay PENDING.

## §4b — The quiescent point: the electron as a SELF-BIASED multi-port LC circuit

> **SECTOR-HEADER + REGIME.** This subsection is the **bias-then-small-signal** re-expression of the whole node.
> Regime: the electron sits at the **saturated operating point**; the VCA (impedance network) is the
> **small-signal** response *around* it. CONSISTENCY-class: this names the previously-unnamed DC-bias step of the
> EE workflow and identifies the canon's saturation-state $A$ as the **quiescent point** — it derives no new
> number.

In electrical engineering a nonlinear reactive network is analyzed in three steps: **(1) set the DC bias** (the
quiescent / Q-point), **(2) linearize** the constitutive parameters at that bias, **(3) read off the AC /
small-signal impedance**. The substrate node is exactly such a network, and the AVE canon already supplies all
three — the **bias step has simply not been named** until now:

> **[Resultbox] The electron = a self-biased multi-port LC circuit at a self-set, self-stable Q-point.**
> - **Bias = the saturation-state $A$.** The operating point is the per-port $A$ along the Axiom-4 kernel
>   ("DC bias on a varactor", [`manuscript/ave-kb/CLAUDE.md`](../../../CLAUDE.md):75). The **MASS port** (A1
>   dilatation $\to Z_{\mathrm{bulk}}$, mechanical) is biased to $A\to1$ (the $V_{snap}$ rail, $Z_{bulk}\to0$,
>   $\Gamma=-1$ cage); the **CHARGE port** (mechanical Cosserat $(2,3)$ micro-rotation $\to Z_{\mathrm{shear}}$,
>   the static reactive charge boundary) is biased to $V_{yield}$ (the self-trap onset) — and the **EM
>   $\mu$-sector** (transduced from that micro-rotation circulation, §4a) reaches $\mu_{eff}\to0$ there (the
>   Meissner onset). The per-port $V_{yield}/V_{snap}$ **ladder** *is* the set of per-port quiescent biases.
> - **SELF-set:** there is no external bias network — **Axiom-4 self-saturation IS the bias mechanism**. The
>   soliton's own field drives each port to its $A$.
> - **SELF-stable:** the equilibrium $R\cdot r=\tfrac14$ is the **stable Q-point** (parked at the steady bias,
>   no net work; rest-mass = the DC energy stored at the Q-point — the virial-balanced $C\leftrightarrow L$
>   store recovering $E=m_ec^2$).
> - **The VCA is the small-signal network around this Q-point.** The graded impedance trio
>   ($Z_{\mathrm{EM}}/Z_{\mathrm{shear}}/Z_{\mathrm{bulk}}$) is the linearized AC response *around* the saturated
>   bias: $\varepsilon_{eff}=\varepsilon_0 S(A)$, $\mu_{eff}=\mu_0 S(A)$, $C_{eff}=C_0/S(A)$ evaluated **at** $A$
>   (CLAUDE.md:73,:75). This **completes the EE workflow** — DC-bias (the Q-point, the previously-unnamed step)
>   → linearize (the $S(A)$-modulated $\varepsilon/\mu/C$) → AC (the VCA impedance trio).

**Where each step already lives in canon (verify-before-cite):** the bias step (electron operating point on the
varactor C-V curve, $V_{snap}\approx511$ kV, $V_{yield}=\sqrt\alpha\,V_{snap}\approx43.65$ kV, the load-line
intersection) is the worked DC view of
[`cvr-dc-operating-point.md`](cvr-dc-operating-point.md):43-45; the small-signal index read-off is §3 above; the
VCA impedance trio is [`resonant-lc-solitons.md`](resonant-lc-solitons.md):114-131. This subsection only adds the
**name** ("quiescent point") and the **workflow ordering** (bias → linearize → AC) that ties them together.

> **PENDING / OPEN (no-overclaim).** Whether the Q-point *sets* $R\cdot r=\tfrac14$ **α-free** (the α-flip
> question) is **UNVERIFIED / open** — flagged, not done. The channel-impedance-mismatch $Q$ target stays
> **EMPTY** (the α-free cold-cage $Q\approx30.8\ne137$ is the corpus clean NEGATIVE,
> [`resonant-lc-solitons.md`](resonant-lc-solitons.md):131); $Q=137$ is not refilled. $V_{yield}=\sqrt\alpha\,
> V_{snap}$ exactly, so the two per-port biases are NOT independent (the $\sqrt\alpha$ is an α-echo). mass=A1
> (PR#260) untouched. CONSISTENCY-class throughout.

## §5 — Derived-vs-asserted ledger

| Element | Status | Basis |
|---|---|---|
| $C_{eff}=C_0/S(A_V)$, varactor keyed on $V$ | **DERIVED** | Axiom 4 dielectric specialization (`manuscript/ave-kb/CLAUDE.md`:73) |
| $L_{eff}=L_0/S(A_I)$, relativistic inductor keyed on $I$; $I_{max}=\xi_{topo}c$ | **DERIVED** | clm-p5cf3t ([`relativistic-inductor.md`](relativistic-inductor.md):15,:18), Topo-Kinematic mapping |
| R1 symmetric: $S_\varepsilon=S_\mu=S\Rightarrow Z=Z_0$ reflectionless | **DERIVED** | INVARIANT-S2 W6 (`manuscript/ave-kb/CLAUDE.md`:75) |
| R2 static-E: $S_\varepsilon<1,S_\mu=1\Rightarrow Z_0/\sqrt{S_\varepsilon}$, $\delta n\approx-\tfrac14 A_V^2$ | **DERIVED** | W6 static-E asymmetric clause + Op14 Meissner-asymmetric $Z_{eff}=Z_0\sqrt{S_\mu/S_\varepsilon}$ |
| R3 static-B: $S_\mu=1\Rightarrow\delta n_\mu=0$ exactly | **DERIVED (analytically exact)** | $I$-keyed inductor + Lenz (no $dI/dt$ ⟹ $I_{vac}=0$ ⟹ $A_I=0$ ⟹ $S_\mu=1$ identically); direct-kernel positive control `src/tests/test_vca_node_regime_sweep.py` |
| $B_{SNAP}$ = energy-density scale, not $\mu$-kernel argument | **DERIVED** | $B_{SNAP}^2/2\mu_0 = m_ec^2/\ell_{node}^3 = 1$ |
| OQ-1 par−perp differential $-\tfrac12 A_V^2$, ratio $7.5/\alpha^3$ | **DERIVED (E-route)** | clm-pp3qwf; the magnitude is an $\alpha$-echo (value rides $\alpha^{-3}$) |
| Which grade is "magnetic primary" vs "capacitive primary" under chirality | **ASSERTED** (degenerate) | wall-branch fork B3-DEGENERATE (PR#260); mute on this leaf's static-field result |
| §0 node = multi-port LC tank (6 DOF → MASS/CHARGE/$\varepsilon$/$\mu$ ports + $A$-state) | **CONSISTENCY** (re-expression) | Axiom 1 (`CLAUDE.md`:73) + operating-point state (`CLAUDE.md`:75); no new DOF/number |
| §4a Meissner = $\mu_{eff}=\mu_0 S\to0$ shorting the $\mu$-port (EMERGENT) | **CONSISTENCY** (re-expression) | `phase-transitions-impedance.md`:24 + Axiom 4; $A1\perp T2$ scoping (`master-equation.md`:20, PR#260) |
| §4b electron = self-biased multi-port LC at the self-set/stable Q-point; VCA = small-signal-around-Q | **CONSISTENCY** (re-expression) | saturation-state-$A$ bias (`CLAUDE.md`:75) + electron load-line (`cvr-dc-operating-point.md`:43-45) + VCA trio (`resonant-lc-solitons.md`:114-131); α-flip + transverse-self-Meissner are PENDING/open |

> **Consistency-vs-emergence tag.** This leaf is **CONSISTENCY / manifestation class**: it
> re-expresses the already-derived Axiom-4 kernel and the relativistic-inductor primitive (clm-p5cf3t)
> as the operating-point taxonomy and reads off the static-field asymmetry. The added §0 (multi-port map),
> §4a (Meissner-from-$\mu$), and §4b (quiescent-point / bias-then-small-signal) are likewise **CONSISTENCY-class
> re-expressions** of the saturation-operating-point + varactor + VCA canon — they name and re-order existing
> content (the previously-unnamed DC-bias step) and originate no new derivation; the transverse-self-Meissner
> build (FORK-A) and the α-flip ($R\cdot r=\tfrac14$ α-free) are flagged **PENDING/open**, not done. It originates no new
> dimensionful constant. The R2 ratio $7.5/\alpha^3$ is an **$\alpha$-echo** at the value level (AVE
> does not derive $\alpha$); the AVE-distinct CHORD is that the vacuum saturates at all (tree-level
> O(1) structure QED lacks) and that the static-B route is **exactly** transparent — a categorical
> prediction.

> **VCA-R01 code note (RESOLVED 2026-06-22).** The fdtd engine previously keyed $\mu$-saturation on the
> *static* $|\mathbf B|=\mu_0|\mathbf H|$ against $b_{yield}=B_{SNAP}$; that is now corrected. The
> **free-EM $\mu$-channel is LINEAR** ($\mu_{eff}=\mu_0$). The $\mu$-grade is the relativistic inductor
> ([`relativistic-inductor.md`](relativistic-inductor.md):15), which saturates only as the circulating
> current reaches $c$ — i.e. as the circulation rate $\omega\to\omega_C=c/\ell_{node}\approx7.76\times10^{20}$
> rad/s ($f_C=\omega_C/2\pi\approx1.24\times10^{20}$ Hz; gamma-ray scale, $\hbar\omega_C=m_e c^2=511$ keV).
> Any wave a Yee EM engine can represent has $\omega\ll\omega_C$
> ($\omega/\omega_C\lesssim10^{-6}$ even at optical), so $S_\mu=\sqrt{1-(\omega/\omega_C)^2}=1$ to machine
> precision; a static external $\mathbf B$ ($dB/dt=0$) likewise induces no circulation, so $S_\mu=1$,
> $\delta n_\mu=0$ exactly (regime R3). The old $|B|$-amplitude keying was wrong twice over: $B_{SNAP}$ is
> an energy-density scale, not the kernel argument, and amplitude is not the circulation rate.
>
> **Scope (caller-local).** Corrected at `fdtd_3d._compute_local_mu` plus the two energy readouts
> (`total_field_energy`, `energy_density`) and the JAX twin `fdtd_3d_jax._compute_local_mu_kernel`.
> `scale_invariant.mu_eff()` is **unchanged** — it is the sector-agnostic kernel used by genuine
> static-$B$ MATTER callers (`superconductor.meissner_mu_eff`, `yang_mills`), correct as-is. A free wave saturates $\mu$ only as $\omega\to\omega_C$, the **dispersive lattice cutoff**
> $\mu_{eff}(\omega)=\mu_0\sqrt{1-(\omega/\omega_C)^2}$, where $\hbar\omega_C=\hbar c/\ell_{node}=m_e c^2=511$ keV
> (the Compton / pair-production scale). This coarse-grid continuum engine ($dx\gg\ell_{node}$) never reaches
> $\omega_C$, so $\mu=\mu_0$ for the waves it represents; the cutoff is modeled separately. **The AVE-distinct
> $(q\,\ell_{node})^4$ lattice-dispersion test is now resolved (FORK-2) as a k-space Bloch eigensolve, NOT a
> temporal dispersive-$\mu(\omega)$ FDTD** (a coarse-grid $\mu(\omega)$ FDTD only validates the null $\mu=\mu_0$;
> the directional anisotropy is a k-space object in $D(\mathbf k)$). See
> [`k4-bloch-dispersion-quartic.md`](../../falsification/ch12-falsifiable-predictions/k4-bloch-dispersion-quartic.md)
> (clm-k4d4ph) and the §6 result-doc. The temporal cutoff $\omega_C$ (this note's subject) and that spatial
> quartic are DISTINCT mechanisms (ratio $\pi$). A **bound/self-trapped** circulation saturates $\mu$ at any frequency — that lives in the
> Cosserat engine (`cosserat_field_3d._compute_saturation_factors`, keyed on the micro-rotation curvature).
>
> **Tests.** The direct-kernel control `src/tests/test_vca_node_regime_sweep.py` (analytic node-up laws,
> $A_I=I_{vac}/I_{max}=0\Rightarrow S_\mu=1$) is unchanged and green. The engine test
> `src/tests/test_vca_r01_static_b_mu_keying.py` — static external $B\Rightarrow\mu_{eff}=\mu_0$ — now
> **PASSES** (was `xfail`), with a companion regression guard against the old $|B|$-amplitude keying.
> `code_fix_decision = resolved`. (Derivation + the $\omega_C$ scale argument:
> [`research/2026-06-22_node-up-small-large-signal_result.md`](../../../../../research/2026-06-22_node-up-small-large-signal_result.md):§6.)

---
