> **Notation (2026-06-18):** Substrate object symbol `$\mathcal{M}_A$` **retired** (Grant adjudication). Use prose: *substrate*, *chiral LC network*, *chiral Laves K4 Cosserat crystal*. Body below preserved per Rule-12.

# AVE Field & Symbol Registry — All-Sectors Normative Nomenclature (research-doc DRAFT)

> **Status: research-doc DRAFT — NOT canon. Auditor/Grant-gated.** This is a draft of a future
> `common/` KB leaf (the `translation-circuit.md` / `vocabulary-register.md` precedent) and a
> candidate Vol-9 symbol-table appendix (§Promotion path). It **proposes** normative names; it
> **renames nothing** in existing canon. Every proposed rename or annotation of an existing leaf is
> staged in the **RENAME-QUEUE (§5)** for auditor/Grant adjudication — flag-don't-fix. The registry
> body is NEW prose; it extends and cross-links three disambiguation assets canon already owns
> (`master-equation.md:20` two-"3"s box, `dark-back-reaction-taxonomy.md`, the
> `vocabulary-register.md` `def-` spine), it does not re-litigate them.
>
> **Discipline tags applied:** `verify-before-cite` (every anchor in this doc was grep-verified this
> session against `AVE-Core @ origin/main f2ed89d5` or the named unmerged branch via git objects;
> two failed/unverified cites are quarantined in §6.3 and one misfiled-anchor cite was corrected this
> session — see §6.3 and §3.10 flag (1)), `ave-representation-capability-check`
> (this registry IS that skill's instrument — every field entry carries its real-space DOF capability
> AND its phase-space representation AND the declared bridge between them, so a name can never silently
> double-count a carrier against an engine DOF), `ave-evidence-framing-discipline` (each anchor tagged
> origin/main vs UNMERGED-branch; engine-construct vs canon), `flag-don't-fix`.

## How to read an entry

Every **field** entry carries the **real / phase / bridge** decomposition (the rule-4 instrument):

- **real-space component(s)** — what lives on the K4 lattice: tensor rank, elastic sector, units.
- **phase-space representation** — what the phasor / winding / Smith layer sees: which angles or
  amplitudes, on which torus or chart.
- **the declared bridge** — the explicit map between the two (e.g. the TLM traveling-wave split, the
  Park transform). Where canon declares no bridge, the cell reads **UNDECLARED** — that is registry
  content (a U6-class open question, §6.2), **not** a gap to paper over.

Port-class, ledger-class, operator-class and constant-class entries carry the same columns; where a
column is not applicable the cell reads **n/a** (a real statement: e.g. a port has no lattice rank).

---

## 1. Sector map

The substrate carries **three elastic propagation channels** plus the phase-space/topology layers that
*read* them. Every symbol in the registry is filed under exactly one sector; homonyms that span sectors
are split (Rule 1) and each split carries its own channel tag (Rule 3).

| Sector | What it is | Carrier DOF | Propagation speed | Canonical anchor |
|---|---|---|---|---|
| **EM-transverse** | trace-free transverse EM wave on the chiral LC network | photon: $T_2$-only Cosserat shear ($u=0$, $\omega\neq0$) | $c_{EM}=c_0(1-A^2)^{-1/2}$ (**rises**) | `axiom-definitions.md:16`; `photon-identification.md:9-11`; `substrate-temporal-values-definition.md:28` |
| **Shear (mechanical deviatoric)** | the $G=\mu$ deviatoric channel; the **matter clock**; the dark-wake home | transverse shear strain $\tau_{zx}$ | $c_{shear}=c_0(1-A^2)^{+1/4}$ (**freezes**) | `substrate-temporal-values-definition.md:29`; `dark-back-reaction-taxonomy.md:21` |
| **Bulk-longitudinal (volumetric)** | the $K$ compression channel; A1 dilatation-mass; the de Broglie pilot home | longitudinal scalar $V$, density $\bar\rho$ | $c_{bulk}=c_0\sqrt{1+\bar\rho/(1-\bar\rho^2)}$ (**freezes at $\bar\rho_{cav}$**) | `substrate-temporal-values-definition.md:30`; `master-equation.md:18-20` |
| **Cosserat (micro-rotation)** | the per-node intrinsic-spin DOF; charge = Beltrami helicity | micro-rotation $\omega$, displacement $u$ | (couple-stress; $\ell_c=\sqrt6\,\ell_{node}$) | `axiom-definitions.md:16`; `cosserat-mass-gap.md:108` |
| **Phasor / Smith layer** | read-only projection of the bulk-$V$ onto the K4 four-port bond basis | $(V_{inc},V_{ref})$, $\Gamma$, $z_{local}$ | n/a (a chart, not a channel) | `master_fdtd_phasor_bridge.py:16-19` |
| **Topology / winding layer** | the integer invariants the phase-space layer carries | $(p,q)$, $w_{tor}$, $w_{pol}$, $H_{bel}$, $\Phi_{link}$ | n/a | `ch8-alpha-golden-torus.md:29`; `master-equation.md:20` |
| **Kernel** | the saturation scalars that modulate every channel | $A$, $S(A)$, $c_{eff}$ | regime-free scalars | `substrate-temporal-values-definition.md:6` |
| **Ports** | terminal/circuit reactions — never name a field (Rule 2) | BEMF, $Z_L$, drive EMF | n/a | `dark-back-reaction-taxonomy.md`; `2026-06-08_rrad-l-darkwake_result.md:111` |
| **Operators / ledgers** | observers and conserved tallies read off the fields | winding extractor, $H_{bel}$, $L_{bulk}$, $|L_\omega|$, the burst detector | n/a | `common/operators.md`; `2026-06-10_genesis-v5-seeded-snap_result.md` |

### 1a. The "dark sector" — precise definition entry

> **dark [back-reaction]** *(genus, canon-owned)* — a substrate-coupled channel that is
> **non-radiating-into-observable-EM-modes**: real momentum/energy is deposited into the hidden
> lattice $\mathcal{M}_A$ rather than radiated into observable far-field EM. The qualifier **"dark"
> is about *detectability* (EM-transverse-invisible), NOT about *which elastic channel* carries it.**
> Verbatim canon: `dark-back-reaction-taxonomy.md:17` ("non-radiating-into-observable-EM-modes …
> dark-sector sense"). (origin/main)

**Channel-precise consequence — "dark" spans TWO elastic channels:**

- The **dark wake** (thrust species, $\tau^{far}_{zx}$) lives in the **SHEAR** channel — far-field
  radiated Maxwell/Cauchy shear stress (`dark-back-reaction-taxonomy.md:21`; the shear-vs-bulk mode
  split, `2026-06-08_rrad-l-darkwake_result.md:210-222`, origin/main).
- The **bulk-acoustic pilot / vent pulse** (de Broglie store, birth pulse) lives in the
  **BULK-longitudinal** channel (`de-broglie-standing-wave.md:50`, origin/main).

So "dark" is a **detectability qualifier that spans the shear and bulk channels** — naming something
"dark" never settles its channel; the channel must still be stated (Rule 3). This is exactly why the
historical single-$\tau_{zx}$ "dark wake" was a symbol-level conflation (§4, worked example W1).

---

## 2. The four normative rules

1. **One symbol = one object.** A glyph names exactly one physical object. Homonyms are split by
   subscript/superscript and each gets its own row. (Prevents: the live $\Gamma$ homonym, the $S$
   five-way, the $\nu$ triple, the $z_0$ cluster — §4.)

2. **Port-class names never name fields or modes.** BEMF, $R_{rad}$, $Z_L$, EMF are terminal/circuit
   reactions; they may *meter* a field but they are not the field. (Prevents: the BEMF-names-$\tau_{zx}$
   class — §4 W2; the 2026-06-10 PORT-only ruling, corr-0.117 receipt.)

3. **Channel stated in every definition.** Every field/mode entry declares bulk-longitudinal / shear /
   EM-transverse / Cosserat-rotational. "Longitudinal" alone is forbidden — it is four-way ambiguous
   (bulk compression, shear $\tau_{zx}$, forbidden-EM, port $R_{rad,L}$). (Prevents: §4 W3.)

4. **Phase-space and real-space symbols are never compared without an explicit declared bridge.**
   A real-space lattice-Cartesian measurement and a phase-space $\varphi^2$/Clifford-torus quantity
   may only be equated through a named map (TLM split, Park transform). Absent that map the comparison
   is uninformative (A46); the registry cell reads **UNDECLARED** rather than silently bridging.
   (Prevents: the "137 = phase-space cell-count" closed-negative; the genesis-24 $w_{pol}=0$
   double-count — §4 W4.)

---

## 3. The registry table

Organized by sector. Anchors tagged `(main)` = `AVE-Core @ origin/main f2ed89d5`; `[branch X]` =
named **UNMERGED** branch (verified via git objects this session, not yet canon). Engine-construct rows
that are not yet canon carry a `[branch X]`/`[branch UNMERGED]` tag AND an explicit engine/apparatus class
— that tag **is** the not-canon marker. No novel-objects-report row (N1–N11) is promoted into this table as
a blessed row; those remain in the companion report pending the §Promotion gate.

### 3.1 EM-transverse sector

| Symbol | Normative name | Class | Channel | Real-space component(s) (rank/sector/units) | Phase-space representation | Declared bridge (or UNDECLARED) | Canonical anchor | NOT-this |
|---|---|---|---|---|---|---|---|---|
| $E$ | electric field | field projection | EM-transverse | translational DOF projection (capacitive $\varepsilon_0$); rank-1 polar vector per node; V/m | component of the $A_1{\oplus}T_2$ 4-port irrep ($T_2$ triplet) | $E$ = the $\varepsilon_0$/translational projection of $u$; bridge = the $A_1{\oplus}T_2$ irrep decomposition | `axiom-definitions.md:16`; `photon-identification.md:21` (main) | NOT the longitudinal scalar $V$; NOT the vector potential $A$-field |
| $B$ | magnetic field | field projection | EM-transverse | microrotational DOF projection (inductive $\mu_0$); rank-1 axial vector per node; T | $T_2$ triplet, transverse | $B$ = the $\mu_0$/microrotational projection of $\omega$; bridge = $A_1{\oplus}T_2$ decomposition | `axiom-definitions.md:16` (main) | NOT $\omega$ itself (B is the EM **projection** of the Cosserat micro-rotation); NOT $H_{bel}$ |
| $w$ | photon transverse-shear field | field | EM-transverse carrier ($T_2$-only Cosserat shear) | transverse shear, $u=0$, $\omega\neq0$; the K4-TLM $T_2$-only bound state | when free: a travelling $T_2$ mode (no trapped phasor). When TIR-trapped (electron) the $(2,3)$ winding lives on its $(V_{inc},V_{ref})$ torus | free photon → **UNDECLARED** (no trapping, no phasor); trapped → Park-along-contours | `crystal_engine.py:22` [branches v5/edatasheet]; `photon-identification.md:9-11` (main) | NOT the winding integers $w_{tor},w_{pol}$; NOT the dark-energy EOS $w_{vac}$; NOT the S11 fit $w_0$; NOT the mechanical-shear $\tau_{zx}$ |
| $c_{EM}$ | EM-transverse phase speed | kernel/speed | EM-transverse | $c_{EM}=c_0(1-A^2)^{-1/2}$ — **rises** ($\to\infty$ at $A\to1$); the $\alpha$-speed / Maxwell phase velocity | n/a | n/a (scalar field of $A$) | `substrate-temporal-values-definition.md:28` (main) | NOT $c_{shear}$ (matter clock, freezes); NOT $c_{bulk}$; the c_EM-vs-c_shear split is the §4 W3 hazard |

> **Channel subtlety (registry note, not a fork).** The photon $w$ and the mechanical dark-wake
> $\tau_{zx}$ are **both transverse in tensor structure** but live in **different channels with
> different speeds**: $w$ rides $c_{EM}$ (rises; the Maxwell/$\alpha$ channel), the mechanical
> deviatoric shear rides $c_{shear}$ (freezes; the matter clock). "Transverse" alone does not pin the
> channel — Rule 3 forces the $c_{EM}$/$c_{shear}$ tag. (`substrate-temporal-values-definition.md:28-29`)

### 3.2 Shear (mechanical deviatoric) sector

| Symbol | Normative name | Class | Channel | Real-space component(s) (rank/sector/units) | Phase-space representation | Declared bridge (or UNDECLARED) | Canonical anchor | NOT-this |
|---|---|---|---|---|---|---|---|---|
| $\tau^{far}_{zx}$ | dark wake (thrust species) | radiated field/stress | **shear** (mechanical deviatoric) | far-field radiated longitudinal-shear stress; rank-2 Cauchy stress; $\mathrm{N\,m^{-2}}$; $\tau^{far}_{zx}=\rho_{Op14}Z_{vac}\nabla|E|^2$ | n/a (real-space motion-trail) | radiated species: a real-space stress, **no phasor projection** (UNDECLARED by construction) | `dark-back-reaction-taxonomy.md:21` (main); mode split `2026-06-08_rrad-l-darkwake_result.md:210-222` (main) | NOT $\Sigma_{near}$ (g-2 reactive-power **rate**, $V^2$/time, not a stress); NOT the bulk pilot; NOT the near-field transverse-inductive double-slit wake (`ohmic:11`) |
| $\Sigma_{near}$ / $-\dot\Sigma_{near}$ | dark resonance (g-2 species) | near-field reactive store / rate | near-field reactive (**not a propagating channel**) | reactive self-energy $\Sigma_{near}\propto V^2$; the retarded rate $-\dot\Sigma_{near}=-dV^2/dt$ has dim $V^2$/time | lives in the Cosserat $(2,3)$ d/q phase space (saliency $\delta$, $A_2$ coefficient) | $-\dot\Sigma_{near}$ enters $A_2=\frac2{\pi\alpha}\langle(S_d-S_q)(-\dot\Sigma_{near})\rangle$ — declared in d/q phase space | `dark-back-reaction-taxonomy.md:31-35` (main) | NOT a shear stress (the old "$\tau_{zx}=-dV^2/dt$" was a symbol-level category error); NOT the AMO CPT/EIT "dark resonance" (firewall, `:37-39`) |
| $X_L$ | longitudinal-shear near-field reactance | port reactance (filed here for its channel) | **shear** near-field reactive | $\mathrm{Im}\{Z_{rad,L}\}$ = near-field reactive stored energy ($\Sigma_{near}$ species); $\Omega$ | n/a | $X_L=\omega\langle U_{stored}\rangle/(\tfrac12|I|^2)$ | `2026-06-08_rrad-l-darkwake_result.md:111-114` (main) | NOT the electron's BULK $m_ec^2\alpha$ pilot store — explicitly "different elastic channels" (`:210-222`); the bulk-vs-shear store question is the OPEN pilot fork (§6.1, C19) |
| $c_{shear}$ | shear (matter-clock) speed | kernel/speed | **shear** | $c_{shear}=c_0(1-A^2)^{+1/4}$ — **freezes** ($\to0$ at $A\to1$); group/energy-transport/rest-mass speed; the matter clock; tracks Schwarzschild $c\sqrt{1-r_s/r}$ | n/a | n/a | `substrate-temporal-values-definition.md:29` (main) | NOT $c_{EM}$ (rises); NOT $c_{bulk}$ |

### 3.3 Bulk-longitudinal (volumetric) sector

| Symbol | Normative name | Class | Channel | Real-space component(s) (rank/sector/units) | Phase-space representation | Declared bridge (or UNDECLARED) | Canonical anchor | NOT-this |
|---|---|---|---|---|---|---|---|---|
| $V$ | longitudinal scalar (A1 dilatation-mass) | field | **bulk-longitudinal** | the Heaviside/Gibbs-excised compression scalar; rank-0 per-node; standing $V$ = Lane-1 mass presence ($m_ec^2$ = trapped acoustic compression); the order-parameter channel | projected (read-only) onto $(V_{inc},V_{ref})$ on the K4 bond Smith chart | $V_{phys}=\tfrac12(V_{here}+V_{nbr})$; $V_{inc}=\tfrac12(V_{phys}+Z_0 I_{phys})$, $V_{ref}=\tfrac12(V_{phys}-Z_0 I_{phys})$ | `master-equation.md:18-20`; `master_fdtd_phasor_bridge.py:16-17` (main) | NOT the orbital potential $V(r)$ (homonym, `de-broglie:42`); NOT the $(V_{inc},V_{ref})$ projection (those are read-only, **not** independent DOF — the double-count lesson); distinguish **standing** $V$ (mass) vs **propagating** $V$ |
| $\bar\rho$ | bulk density perturbation | field | **bulk-longitudinal** | EOS $p(\bar\rho)=\rho_0c_0^2[\bar\rho-\tfrac12\ln(1-\bar\rho^2)]$; rank-0 scalar; dimensionless density ratio | n/a (real-space) | n/a | EOS `cavitation_flow.py:165-166` (main) | NOT the Pearson correlation $\rho$; NOT $\rho_{Op14}$; NOT $\rho_{latent}$ (dark-energy density); NOT the freeze floor $\bar\rho_{cav}$ (the clamp threshold, distinct object) |
| $\bar\rho_{cav}$ | cavitation floor — **operational canon** (floor-VALUE epistemic status CONTESTED, §3.10 flag) | bulk threshold constant | **bulk-longitudinal** | $\bar\rho_{cav}=-1/\varphi\approx-0.618$; the $c_{bulk}$ freeze floor ($c_{bulk}^2(\bar\rho_{cav})=0$) | n/a | n/a | **defined** `cavitation_flow.py:64` (`RHO_CAV=-1.0/PHI`); **consumed** by the merged Vol-4 probe `cavitation_core_probe.py:35,69,237,249` (PR#161); freeze-floor relation `substrate-temporal-values-definition.md:30,61` (main) | the constant lives in `cavitation_flow.py:64`, **NOT** `constants.py` (the rectifier-prereg "from constants.py" attribution is misfiled → RENAME-QUEUE R8). Floor-VALUE $-1/\varphi$: CANDIDATE per `cavitation_flow.py:62` comment ("floor is CANDIDATE") + `v5 prereg:74` ("cite as candidate, never canonical") vs "Q2 resolved" per `substrate-temporal-values:61` — CONTESTED, surfaced not resolved (flag-don't-fix) |
| bulk-acoustic pilot | de Broglie matter-wave reactive store | field / near-field store | **bulk-longitudinal** (canonical reading — fork OPEN) | longitudinal acoustic pressure waves governed by the vacuum Bulk Modulus; $n_{acoustic}(r)\propto1/\sqrt{E-eV(r)}$ | the standing-wave resonance $2\pi r=n\lambda$ | acoustic-impedance reflection at $E-eV(r)=0$ (total reflection, $\Gamma=-1$) | `de-broglie-standing-wave.md:50` (main) | the transverse-inductive reading (`ohmic-decoherence-born.md:11`) is the OPEN fork (§6.1); NOT the far-field dark wake $\tau^{far}_{zx}$ |
| $c_{bulk}$ | bulk (compressional) speed | kernel/speed | **bulk-longitudinal** | $c_{bulk}=c_0\sqrt{1+\bar\rho/(1-\bar\rho^2)}$; stiffens at $\bar\rho\to+1$; freezes at $\bar\rho_{cav}$ | n/a | n/a | `substrate-temporal-values-definition.md:30` (main) | NOT $c_{shear}$; NOT $c_{EM}$; NOT the legacy overloaded $c_{eff}$ (§4 W5) |

### 3.4 Cosserat (micro-rotation) sector

| Symbol | Normative name | Class | Channel | Real-space component(s) (rank/sector/units) | Phase-space representation | Declared bridge (or UNDECLARED) | Canonical anchor | NOT-this |
|---|---|---|---|---|---|---|---|---|
| $\omega$ | Cosserat micro-rotation | field | **Cosserat-rotational** ($T_2$) | 3 microrotational DOF per node (inductive $\mu_0$, magnetic); the winding carrier; charge $=H_{bel}$ | the $(2,3)$ winding angles on the $(V_{inc},V_{ref})$ Clifford torus (2 d-axis, 3 q-axis) | $\omega(x,t)\leftrightarrow(2,3)$ via **Park-along-contours** (d/q projection) | `axiom-definitions.md:16`; `master-equation.md:20`; `ch8-alpha-golden-torus.md:29` (main) | NOT fluid vorticity $\zeta=2\Omega$ (disambiguated `claim-quality.md:195`); NOT the frequencies $\omega_\oplus,\omega_I,\omega_C$; NOT $B$ (which is $\omega$'s EM projection) |
| $u$ | translational displacement | field | translational (A1 longitudinal + transverse) | 3 translational DOF per node (capacitive $\varepsilon_0$, electric); A1-bearing | n/a (real-space) | $E$ = the $\varepsilon_0$ projection of $u$ | `axiom-definitions.md:16`; `cosserat-mass-gap.md:28` (main) | NOT $\omega$; A1 ($u$) is **massless**, $T_2$ ($\omega$) carries the mass-gap content (`cosserat-mass-gap.md:108` — a confusion-prone channel statement, RENAME-QUEUE §5) |
| $\pi_u$ | canonical momentum of $u$ | field momentum | translational | conjugate to $u$ | UNDECLARED | **UNDECLARED** in origin/main core engine (grep `cosserat_master_equation_fdtd.py` = 0 hits) | engine-level only [branch v5] | NOT $u$; NOT $\pi_\omega$ |
| $\pi_\omega$ | canonical momentum of $\omega$ | field momentum | Cosserat-rotational | conjugate to $\omega$; engine $\pi_\omega=(\omega-\omega_{prev})/dt$ | UNDECLARED (no canon real↔phase bridge) | **UNDECLARED** — used in `bemf\_emf=\kappa_L\|g[w\cdot(\nabla\times\pi_\omega)]\|` | `electron_spec_suite.py:57` [branch v5]; `2026-06-10_bemf-feedback-smoke_result.md:79` [branch bemf, UNMERGED] | NOT $\pi_u$; NOT BEMF (BEMF is the port that reads $\nabla\times\pi_\omega$, not the momentum) |
| $\zeta=2\Omega$ | rotor-local vorticity | derived field | bulk flow (rigid-rotor curl) | solid-body vorticity, $\mathrm{curl}=2\Omega\neq0$; rank-1 axial | n/a | n/a | `divergence-test-substrate-map.md:50` (main) | NOT the Cosserat micro-rotation $\omega$ (this is **fluid** vorticity); NOT angular velocity $\Omega$ |

### 3.5 Phasor / Smith layer

| Symbol | Normative name | Class | Channel | Real-space component(s) (rank/sector/units) | Phase-space representation | Declared bridge (or UNDECLARED) | Canonical anchor | NOT-this |
|---|---|---|---|---|---|---|---|---|
| $V_{inc},V_{ref}$ | incident/reflected bond phasors | **read-only projection** of $V$ | bulk (phasor layer) | n/a — not an independent lattice DOF | the two travelling-wave amplitudes on each K4 bond at $Z_0$ | $V_{inc}=\tfrac12(V_{phys}+Z_0I_{phys})$, $V_{ref}=\tfrac12(V_{phys}-Z_0I_{phys})$ — the TLM split | `master_fdtd_phasor_bridge.py:16-17`; `master-equation.md:20` (main) | NOT independent DOF ("$V_{ref}$ is a read-only projection of the same scalar $V$"); never wire the winding into these (the genesis-24/$w_{pol}=0$ double-count) |
| $\Gamma$ (reflection) | reflection coefficient / Smith coordinate | operator + chart coordinate | sector-resolved (conjugate-variable sign) | n/a | $\Gamma=V_{ref}/V_{inc}$ on the Smith chart; $|\Gamma|\to1$ at the rim (phase-change signature) | Op3 $\Gamma=(Z_2-Z_1)/(Z_2+Z_1)$; wall ruling $\Gamma_{flow}=-\Gamma_{pressure}$ | `operators.md:43`; `2026-06-10_matter-as-vapor-locked-pump_framing.md:56,65` (main) | NOT the Kelvin circulation $\Gamma$ (LIVE homonym, §4 C-Γ); NOT $\Gamma_{pack}/\Gamma_{steric}$; NOT $\Gamma_{sagnac}$ (a gain, not a reflection); $\Gamma=-1$ names two sector-distinct walls (bulk pocket vs shear cavity) |
| $z_{local}$ | local bond impedance | phasor diagnostic | bulk (phasor layer) | n/a | per-bond $z$ from the saturation kernel $S(A)$, $A=|V|/V_{yield}$ | `z_local` uses $S(A)$ | `master_fdtd_phasor_bridge.py:7` (main) | NOT $Z_0$ (vacuum impedance 376.73 Ω); NOT $z_0$ (coordination number ~51.25); the $z$ cluster is §4 C-z0 |

### 3.6 Topology / winding layer

| Symbol | Normative name | Class | Channel | Real-space component(s) (rank/sector/units) | Phase-space representation | Declared bridge (or UNDECLARED) | Canonical anchor | NOT-this |
|---|---|---|---|---|---|---|---|---|
| $(p,q)$ | phase-space winding pattern | topology/geometry | phase-space | electron = $0_1$ **unknot** in real space (no real-space crossings) | $(2,3)$ lives on the $(V_{inc},V_{ref})$ Clifford torus ($T^2\subset S^3\subset\mathbb{C}^2$); 2 d-axis, 3 q-axis | declared bridge = Park projection (lab shadow $\leftrightarrow$ d/q) | `ch8-alpha-golden-torus.md:29` (main) | NOT a real-space trefoil knot ("the trefoil lives in phase space; the soliton lives in real space"); link to `vocabulary-register.md` `def-3638f2` (winding, status ambiguous, OPEN sub-flag) — do NOT recoin |
| $R,r$ | Golden-Torus phasor semi-axes | phase-space geometry | phase-space | n/a | $R=\varphi/2\approx0.809$, $r=(\varphi-1)/2\approx0.309$, $R\cdot r=1/4$; $(R,r,d)=(\varphi/2,(\varphi-1)/2,1)$ | phasor enclosed area = Nyquist cell cross-section (Class-B substrate-mechanism, **not** independently derived) | `ch8-alpha-golden-torus.md:111,116`; `constants.py:200-202` (main) | NOT the real-space radii ($r_{meas}\geq3$-cell floor, $R_{II}=\sqrt3/2$ regime boundary) — rule-4 bridge required |
| $w_{tor},w_{pol}$ | toroidal/poloidal winding integers | topology ledger | phase-space | n/a | integer winding read from Park-along-contours; extractor floor $r\geq3$ cells | Park-along-contours = the real↔phase bridge | `2026-06-09_crystal-engine_result.md:16,112` (main); `master-equation.md:20` ($w_{pol}=0$) | NOT the photon field $w$; NOT $w_{vac}$; NOT $w_0$ |
| $H_{bel}$ | Beltrami helicity ledger (charge) | ledger / topological charge | **Cosserat-rotational** | charge $=H_{bel}=\int\omega\cdot(\nabla\times\omega)$ | n/a (a real-space volume integral over the rotational field) | n/a | `master-equation.md:20` (main); instrument floor $\pm6.5\%$ at $N=72$ `2026-06-10_apparatus-floors_note.md:147-161` [branch floors] | NOT the Hamiltonian $H_{total}$ (homonym); closure claims tighter than $\pm6.5\%$ are apparatus, not physics |
| $\Phi_{link}$ | bond flux linkage | ledger / bond variable | longitudinal-$V$ $\leftrightarrow$ $\omega$ trading (Op14 cross-sector) | accumulates $V_{phys}\cdot dt$ on directed A→B bonds (K4 convention) | n/a (a real-space bond accumulator) | declared at `master_fdtd_phasor_bridge.py:19` | `master_fdtd_phasor_bridge.py:19`; Op14 $\rho(H_{cos},\Sigma|\Phi_{link}|^2)=-0.990$ `operators.md:54` (main) | NOT the interferometric phase $\Delta\Phi\approx250$ rad (`de-broglie:58`) |

### 3.7 Kernel

| Symbol | Normative name | Class | Channel | Real-space component(s) (rank/sector/units) | Phase-space representation | Declared bridge (or UNDECLARED) | Canonical anchor | NOT-this |
|---|---|---|---|---|---|---|---|---|
| $A$ | physical strain amplitude | kernel input | regime-free scalar | the substrate-native amplitude variable; dimensionless ($A=|V|/V_{yield}$ in the bond context) | n/a | n/a | `substrate-temporal-values-definition.md:6` (main) | NOT the vector-potential $A$-field; NOT the saliency $A_2$/Petermann; NOT the irrep label $A_1$ |
| $S(A)$ | universal saturation kernel | kernel | regime-free scalar | $S(A)=\sqrt{1-A^2}$ (Op2: $S(A,A_c)=\sqrt{1-(A/A_c)^2}$) | n/a | n/a | `operators.md:42`; `substrate-temporal-values-definition.md:6` (main) | "$S$ is used inconsistently elsewhere" — NOT the S-matrix $[S]$ (Op5), NOT the S11 observable, NOT $S_d/S_q$ saliency, NOT $S_{min}$ floor (§4 W6, five-way) |
| $c_{eff}$ | **OVERLOADED legacy speed (deprecate)** | kernel | channel-dependent (the problem) | three distinct referents: (a) stale pre-split $c_0\sqrt{1-A^2}$; (b) bulk EOS $c_{eff}^2=c_0^2(1+\bar\rho/(1-\bar\rho^2))$; (c) Op13 generic "local saturated $c_{eff}$" | n/a | n/a | `substrate-temporal-values-definition.md:51`; `operators.md:53` (main) | the pre-split (a) is STALE (off by factor 2 in exponent vs the $c_{EM}/c_{shear}$ split); use $c_{EM}/c_{shear}/c_{bulk}$ instead (§4 W5) |

### 3.8 Ports

> **Rule 2 governs this whole sector: a port may *meter* a field but is not the field.**

| Symbol | Normative name | Class | Channel | Real-space component(s) | Phase-space representation | Declared bridge (or UNDECLARED) | Canonical anchor | NOT-this |
|---|---|---|---|---|---|---|---|---|
| BEMF | back-EMF (Lenz terminal reaction) | **PORT** (not a field/mode) | port/terminal | n/a — appears only against **changes**; zero at steady circulation | n/a | dynamical form $\mathrm{bemf\_emf}=\kappa_L\|g[w\cdot(\nabla\times\pi_\omega)]\|$ (a cross-sector reaction read at the port) | 2026-06-10 PORT-only ruling; corr$(\mathrm{bemf\_emf},\tau_{zx})=+0.117$ `2026-06-10_bemf-feedback-smoke_result.md:79` [branch bemf, UNMERGED] | NOT $\tau_{zx}$ (the meter; "distinct objects, NOT interchangeable"); NOT a screening-current field — **RECONCILED 2026-06-10 (N11):** the persistent screening current IS the field; the BEMF is its **Faraday-induced PORT signature**; the Meissner analogy is bounded **Meissner-CLASS** (lens, not identity). See novel-objects N11 + framing §11.6 (`2026-06-10_matter-as-vapor-locked-pump_framing.md`, on the rename-queue-execution branch); NOT $R_{rad,L}{+}jX_L$ (the longitudinal-shear **radiation impedance**, §3.8 $Z_L$ row — also port-class but a DISTINCT port object: BEMF is the terminal Lenz reaction, $R_{rad,L}{+}jX_L$ is the wake-drag$+$reactive-store impedance the wake presents); the 0.117 is a coincidence-magnet (§4 C-0.117) |
| $Z_L=R_{rad,L}+jX_L$ | longitudinal-shear radiation impedance | port impedance | **shear** ($X_L$ near-field; $R_{rad,L}$ radiated) | $R_{rad,L}=P_{rad,L}/(\tfrac12|I|^2)$ = wake drag; $X_L$ = near-field reactive store; $\Omega$ | n/a | $R_{rad,L}=\oint_{far}\langle I_k\rangle\cdot dA_k/(\tfrac12|I|^2)$ | `2026-06-08_rrad-l-darkwake_result.md:111-114,210-222` (main) | $X_L$ is **shear**, explicitly NOT the electron's **bulk** $m_ec^2\alpha$ reactance ("different elastic channels") — the which-channel-stores-the-pilot question is the OPEN fork (§6.1) |
| drive EMF | FOC d/q chiral-photon drive arm | port/source | EM-transverse drive | n/a | the d/q drive vector | FOC d/q Park (BH-QNM co-rotating frame) | `genesis-24` prereg:28 (main); v5 commit 45f6d104 [branch v5] | NOT BEMF (the reaction); NOT the winding-extraction Park-along-contours (different Park) |

### 3.9 Operators / ledgers

| Symbol | Normative name | Class | Channel | Real-space component(s) | Phase-space representation | Declared bridge (or UNDECLARED) | Canonical anchor | NOT-this |
|---|---|---|---|---|---|---|---|---|
| winding extractor | Park-along-contours winding read | operator/observer | phase-space $(V_{inc},V_{ref})$ chart | extractor floor $r\geq3$ cells; reads $w_{tor},w_{pol}$ | the d/q winding integers | Park transform = the declared real↔phase bridge (lab trefoil shadow $\leftrightarrow$ $(2,3)$ d-q) | `2026-06-09_crystal-engine_result.md:16`; `2026-06-07_electron-coherence-reynolds-mapping.md:359` (main) | NOT the FOC d/q Park (BH-QNM drive frame) — same name, different operator (§4 C-Park) |
| $L_{bulk}$ | physical (motion-locked) angular momentum | conserved invariant | **bulk flow** | physical AM of the bulk flow; motion-locked (drive-off ratio 0.97–0.99); $\nu_{art}$-invariant | n/a | n/a | `2026-06-10_genesis-v5-seeded-snap_result.md:25,225-230` [branch v5] | NOT $|L_\omega|$ (which tracks the `lock_eta` apparatus knob = a clip, not physics); NOT inductance $L$ |
| $\|L_\omega\|$ | micro-rotation angular momentum (apparatus reading) | apparatus reading | **Cosserat-rotational** | tracks the `lock_eta` clip (5.38→0.067) | n/a | n/a | `2026-06-10_genesis-v5-seeded-snap_result.md:45,88` [branch v5] | NOT $L_{bulk}$ (the conserved physical AM); the "~8 OOM energy-weight" phrasing is **UNVERIFIED** (§6.3) — do not cite |
| burst detector | D6 longitudinal-burst detector | observer/instrument | **bulk-longitudinal** ledger | calibrated floor $F_{0d}=3.84\times10^{-5}$ (known-null free run) | n/a | n/a | `longitudinal_burst_detector.py`; `2026-06-10_genesis-v5-seeded-snap_result.md:92,98-101` [branch v5] | NOT a transverse field spike; reads the bulk EOS ledger |
| snap state machine | per-cell normal$\leftrightarrow$snapped | engine state machine (v5) | **bulk-longitudinal** | on crossing floor $Z_{bulk}=\rho c\to0$ ⇒ $\Gamma\to-1$ boundary-class (sonic-horizon reflector); hysteresis-by-bookkeeping | $|\Gamma|\to1$ Smith-rim interior | $Z_{bulk}\to0\Rightarrow\Gamma\to-1$ | `unified_genesis_engine.py` (commit 5e6485a8); `2026-06-10_genesis-v5-seeded-snap_prereg.md:47,72-74` [branch v5] | NOT the shear-sector $\Gamma=-1$ EE cavity ("same algebra, not an identity" — sector-resolve) |

### 3.10 Constants layer (cite `constants.py`, do NOT duplicate)

| Symbol | Normative name | Anchor (`src/ave/core/constants.py`, main) | NOT-this |
|---|---|---|---|
| $Z_0$ | characteristic (vacuum) impedance $\approx376.73\,\Omega$ — **transverse-EM only** ($Z_0 \equiv Z_{EM}$; three-impedance law §3.11) | `constants.py:98` | NOT $z_0$ coordination ($\approx51.25$); NOT $z_{local}$; **NOT** $Z_{shear}$ / $Z_{bulk}$ (the shear/bulk acoustic impedances — §3.11) |
| $\ell_{node}$ | node pitch $=\hbar/(m_ec)$ (reduced Compton; the voxel tick) | `constants.py:239` | NOT $\ell_c$ |
| $\ell_c$ | Cosserat coupling length $=\sqrt6\,\ell_{node}$ | `constants.py:255` | one object, **three names** in canon (§4 C-ℓc): "lattice Cosserat coupling length" / "couple-stress length" / "characteristic length"; $\ell_c/d=\sqrt6$-from-K4 still OPEN |
| $\xi_{topo}$ | topological charge-density bridge $=e/\ell_{node}$ | `constants.py:267` | NOT the integer linking charge $\mathcal{Q}$ |
| $\varphi$ | golden ratio (torus $R=\varphi/2$) | `constants.py:200`; `ch8-alpha-golden-torus.md:77` | NOT the FCC packing fraction $\varphi=\pi\sqrt2/6$ (homonym, §4 C-φ); $\bar\rho_{cav}=-1/\varphi$ uses the golden-ratio sense |
| $\nu_{vac}$ | Poisson ratio $2/7$ | `constants.py:508` | NOT $\nu_{kin}$ (kinematic, comment spells it "$\nu_{vac\_kin}$" — §4 C-ν); NOT $\nu_{art}$ (artificial-viscosity knob) |
| $V_{LONG}$ | longitudinal speed $\sqrt{2G/\rho}$ | `constants.py:652` | NOT $c_{bulk}$; NOT $c_0$ |
| $R_{GOLDEN\_TORUS}$ | $\varphi/2$; MINOR $=(\varphi-1)/2$; $R\cdot r=1/4$ | `constants.py:200-202` | NOT the real-space radii |
| $\alpha$ / ALPHA_COLD_INV / DELTA_STRAIN | fine-structure / cold output / thermal strain | `constants.py:135-152,204,227` | — |

> **Constants hygiene flags (verified this session):** (1) `constants.py` contains **no `RHO_CAV`**
> (constants.py-scoped grep = 0) — **but the symbol exists**: `RHO_CAV = -1.0/PHI` is defined at
> `cavitation_flow.py:64` and consumed by the **merged** Vol-4 probe `cavitation_core_probe.py:35,69,237,249`
> (PR#161, = this baseline). So the `2026-06-09_rectifier-stage1-biased-diode_prereg.md:34` line
> "RHO_CAV=-1/phi (from constants.py)" is **not a non-existent symbol but a misfiled file attribution**
> ("from constants.py" → should read `cavitation_flow.py:64`); RENAME-QUEUE R8. **Correction note:** an
> earlier draft of this registry over-generalized the constants.py-scoped negative to "no RHO_CAV at
> origin/main — grep count 0" and quarantined the cite as FALSE; that was the *challenge-canonical-negative
> / grep-configs-not-conclusions* failure — corrected this session against the cavitation-core-probe PR#161
> merge that **is** the baseline. (2) `constants.py:1012` comment "NU_VAC already defined at line 127" is a
> **stale internal anchor** — `NU_VAC` is at line 508.

### 3.11 The three-impedance law (channel-subscript LAW rows)

> **THE LAW (Grant-ratified 2026-06-11):** *every $Z$/$\Gamma$/boundary symbol carries a channel
> subscript.* **$Z_0 \equiv Z_{EM}$ is the TRANSVERSE-EM impedance only** — it is NOT the shear or bulk
> impedance. The corpus already owns the three-channel ledger (§1, §3.1–3.3) and the $K \equiv 2G_{vac}$
> bulk-vs-shear relation (`cauchy-implosion-resolution.md:14`); this makes the subscript discipline
> NORMATIVE for every impedance/reflection statement. Source of record: vocab-operator-unification audit
> §4(a) (`2026-06-11_vocab-operator-unification-audit.md`).

| Channel | LAW symbol | $Z$ formula | dimension | cold value ($A^2\to0$) | speed (saturation) | wall $\Gamma$ | anchor |
|---|---|---|---|---|---|---|---|
| **EM-transverse** | $Z_{EM} \equiv Z_0$ | $\sqrt{\mu/\varepsilon}$ | $\Omega$ (electrical) | $376.73\,\Omega$ (`constants.py:98`) | $c_{EM}=c_0(1-A^2)^{-1/2}$ (**rises**) | $\Gamma_{EM}=0$ under SYM scaling | §3.1; `operators.md:41` (Op1); `electron-bh-isomorphism.md:24` |
| **Shear (deviatoric)** | $Z_{shear}$ | $\rho\,c_{shear}=\rho c_0(1-A^2)^{1/4}$ | $\mathrm{Pa\cdot s/m}$ (acoustic) | $\rho_0 c_0$ | $c_{shear}=c_0(1-A^2)^{1/4}$ (**freezes**) | $G\to0\Rightarrow Z_{shear}\to0\Rightarrow \Gamma_{shear}\to-1$ | §3.2; `operators.md:56` (Op16); `electron-bh-isomorphism.md:30-34` |
| **Bulk-longitudinal** | $Z_{bulk}$ | $\rho\,c_{bulk}$ ($K\equiv2G_{vac}$) | $\mathrm{Pa\cdot s/m}$ (acoustic) | $\rho_0 c_0$ | $c_{bulk}=c_0\sqrt{1+\bar\rho/(1-\bar\rho^2)}$ (**freezes at $\bar\rho_{cav}$; $\to0$ at snap**) | $c_{bulk}\to0\Rightarrow Z_{bulk}\to0\Rightarrow \Gamma_{bulk}\to-1$ (sonic-horizon reflector) | §3.3; §3.9 snap-state machine; `cauchy-implosion-resolution.md:14`; engine `bubble-physics:107` |

**Channel-subscript law statement (normative):** henceforth every $Z$, $\Gamma$, reflection, or boundary
symbol is written with its channel subscript ($Z_{EM}$ / $Z_{shear}$ / $Z_{bulk}$; $\Gamma_{EM}$ /
$\Gamma_{shear}$ / $\Gamma_{bulk}$). An unsubscripted $Z_0$ defaults to $Z_{EM}$ (the transverse-EM
impedance, $376.73\,\Omega$), NEVER the shear or bulk impedance. The three-valued saturated-wall boundary
(EM-transparent $\Gamma_{EM}=0$, shear-reflecting $\Gamma_{shear}=-1$, bulk-reflecting $\Gamma_{bulk}=-1$)
is three channels' views of ONE boundary (audit §4(d) candidate-resolution; the astrophysical case is the
open Grant question below).

**AMBIGUOUS-channel assignment (Harvest-D, vocab audit §4(b); verified absence, NOT a fabricated claim):**

| Site | gap | assigned channel | one-line justification |
|---|---|---|---|
| `manuscript/ave-kb/vol3/{cosmology,gravity}` BH/horizon leaves | NO leaf states $Z_{bulk}$ at $r_s$/$r_{sat}$ (grep-confirmed) | **bulk-longitudinal** ($Z_{bulk}\to0\Rightarrow\Gamma_{bulk}=-1$) | the only corpus $Z_{bulk}\to0\Rightarrow\Gamma_{bulk}=-1$ statements are engine-scale (§3.9 snap, `bubble-physics:107`); the heliopause acoustic-matching + `cauchy-implosion:14` $K\equiv2G$ are the only astrophysical bulk-channel statements — the horizon $Z_{bulk}$ is the unwritten third value. **ASSIGNMENT records the channel; ASSERTING it at a leaf is the §4(d) Grant question** (flag-don't-fix). |

> **Provenance / KEEP-BOTH:** these LAW rows EXTEND the registry (they add §3.11; they do not edit the
> §3.1–3.3 sector rows or the §4 ledger). Source of record: the 2026-06-11 vocab-operator-unification
> audit §4(a)/(b) (Harvest-D). The two CONCLUSION-CHANGING MIS-SCOPED sites — #1
> `invariant-gravitational-impedance.md` (reverses "zero reflection") and #3
> `electron-bh-isomorphism.md:30-34` (reverses "NOT through $\Gamma$") — are §4(d)-entangled and are
> FLAGGED to Grant, NOT edited. The editable MIS-SCOPED notes (#2 `gw-impedance-perturbation.md`, #4
> `03_pin_port_configuration.tex`, #5 `de-broglie-standing-wave.md`) cite this §3.11.

---

## 4. Collision ledger (worked examples)

Each collision is a worked NOT-this example; the rule that prevents it is named. Already-RESOLVED
collisions are cited as **precedents the registry extends** (it does not re-litigate them).

### 4.1 Worked examples (the mechanism failures)

- **W1 — the dark-wake $\tau_{zx}$ conflation (RESOLVED in canon; Rule 3).** One $\tau_{zx}$ symbol once
  named two physically distinct objects on a *signature* resemblance: the far-field thrust shear stress
  ($\tau^{far}_{zx}$, shear, $\mathrm{N\,m^{-2}}$) and the g-2 near-field reactive-power **rate**
  ($\Sigma_{near}$, $V^2$/time). Resolved by the near/far field-zone split at
  `dark-back-reaction-taxonomy.md:11,31,41-50` ("a symbol-level category error … a reactive-power rate,
  not a stress"). **Rule 3** (channel + dimension stated) prevents it. PR#144 mode split
  (`2026-06-08_rrad-l-darkwake_result.md:210-222`) further separated $X_L$ (shear) from $m_ec^2\alpha$
  (bulk). The registry **cites** this as the model worked example.

- **W2 — BEMF (port) naming a field (Rule 2).** Pre-2026-06-10 engine docstrings and leaves wrote the
  dark wake $\tau_{zx}$ AS "the back-EMF" (`vacuum_engine.py:1487` "the dark wake IS the
  mutual-inductance back-EMF response"; `claim-quality.md:731` "Lenz Back-EMF Freezes Topological
  $\omega$"). The 2026-06-10 ruling: BEMF is **PORT-class only**; corr$(\mathrm{bemf\_emf},\tau_{zx})=
  +0.117$ — "distinct objects … NOT interchangeable" (`2026-06-10_bemf-feedback-smoke_result.md:79`,
  [branch UNMERGED]). **Rule 2** prevents it. These engine/leaf sites are RENAME-QUEUE (§5), not edits.

- **W3 — "longitudinal" is four-way channel-ambiguous (Rule 3).** (a) bulk/A1 compression
  (`de-broglie-standing-wave.md:50`; `crystal_engine.py:8`); (b) **shear** "longitudinal shear strain
  $\tau_{zx}$" (`dark-back-reaction-taxonomy.md:11`; `rrad-l` prereg:1 "longitudinal-shear radiation
  impedance"); (c) **forbidden EM** "Gauss forbids longitudinal EM" (`k4-port-irrep-decomposition.md`);
  (d) **port** "longitudinal radiation resistance $R_{rad,L}$" (`rradL` prereg). **Rule 3** forces a
  channel subscript every time; the bare word is banned.

- **W4 — phase-space vs real-space compared without a bridge (Rule 4).** The documented closed-negative
  "137 cell-count is a phase-space Clifford-torus quantity" (`claim-quality-closure-roadmap.md`); and the
  genesis-24/crystal $w_{pol}=0$ **double-count** — wiring the $(2,3)$ winding into the breather's own
  $(V_{inc},V_{ref})$ phasor (which is a read-only projection of the same scalar $V$, not an independent
  DOF). **Rule 4** + the `master-equation.md:20` box prevent it: real↔phase only through a named map
  (Park; TLM split).

- **W5 — $c_{eff}$ overload (Rules 1+3).** The stale pre-split single-speed $c_{eff}=c_0\sqrt{1-A^2}$
  (`op14-local-clock-modulation.md:17,31`, flagged STALE — off by a factor 2 in the exponent) vs the
  bulk EOS $c_{eff}$ (`rarefaction result:138`) vs Op13 generic. Resolved by the three-speed taxonomy
  ($c_{EM}$ rises / $c_{shear}$ freezes / $c_{bulk}$ freezes), `substrate-temporal-values-definition.md:50-52`.

- **W6 — $S$ five-way (Rule 1).** $S(A)=\sqrt{1-A^2}$ kernel / Op5 S-matrix $[S]$ / S11 observable /
  $S_d,S_q$ saliency / $S_{min}$ floor knob. Canon already avoids $S$ in the temporal-values
  definitions ("$S$ is used inconsistently elsewhere", `:6`) by writing in $A$ directly. **Rule 1**:
  each $S$-referent gets its own row.

### 4.2 Homonym collisions (one glyph, many objects — all Rule 1)

| Tag | Glyph | Referents (with channel) | Live? | Anchors |
|---|---|---|---|---|
| C-Γ | $\Gamma$ | Smith reflection $\Gamma=V_{ref}/V_{inc}$ **vs** Kelvin circulation $\Gamma$ (built value $\Gamma=80.75$) — the two senses collide **inside the same v5 arc** | **LIVE** | Smith-$\Gamma$ `…genesis-v5-seeded-snap_prereg.md:46`; circulation-$\Gamma$ symbol (no value) `…prereg.md:52,247`; the **built value** $\Gamma=80.75$ is in `…genesis-v5-seeded-snap_result.md:59,123` [branch v5]; plus $\Gamma_{pack}/\Gamma_{steric}$ `operators.md:48-49`; $\Gamma_{sagnac}$ gain `dark-wake-bemf-foc-synthesis.md:25` |
| C-0.117 | 0.117 | corr$(\mathrm{bemf\_emf},\tau_{zx})=+0.117$ **vs** Op14 onset $\sqrt{2\alpha}\approx0.117$ **vs** $p_G=6/z_0$ rigidity threshold — three unrelated 0.117s | near-miss | `2026-06-10_bemf-feedback-smoke_result.md:79` [branch]; coincidence-magnet flag |
| C-φ | $\varphi$ | golden ratio ($R=\varphi/2$) **vs** FCC packing fraction $\varphi=\pi\sqrt2/6$ | LIVE (canon) | `ch8-alpha-golden-torus.md:77` vs `omega-freeze-cosmic-grain-cascade.md:180`; $\bar\rho_{cav}=-1/\varphi$ only well-defined under the golden sense |
| C-ν | $\nu$ | Poisson $\nu_{vac}=2/7$ **vs** kinematic $\nu_{kin}=\alpha c\ell_{node}$ (comment spells it "$\nu_{vac\_kin}$") **vs** artificial-viscosity knob $\nu_{art}$ | near-miss | `constants.py:508` vs `:655` vs `2026-06-10_genesis-v5-seeded-snap_result.md:64` [branch] |
| C-z0 | $z_0$/$Z_0$ | coordination $z_0\approx51.25$ (α-circular) **vs** impedance $Z_0=376.73\,\Omega$ **vs** $z_{local}$ bond impedance | LIVE | `claim-quality-closure-roadmap.md:32` vs `constants.py:98` vs `master_fdtd_phasor_bridge.py:7` |
| C-ℓc | $\ell_c$ | **one object, three names**: "lattice Cosserat coupling length" / "Cosserat couple-stress length" / "Cosserat characteristic length" | naming-only | `constants.py:255` / `substrate-temporal-values-definition.md:32` / `claim-quality.md:1036`; $\ell_c/d=\sqrt6$-from-K4 OPEN |
| C-Park | Park transform | FOC d/q Park (BH-QNM co-rotating drive frame) **vs** Park-along-contours (winding extractor) | LIVE | `dark-wake-bemf-foc-synthesis.md:22` vs `2026-06-10_genesis-v5-seeded-snap_result.md:44` [branch] |
| C-L | $L$ | inductance $L_{eff}/L_{drag}$, $[Q]\equiv[L]$ TKI **vs** $L_{bulk}$ (physical AM) **vs** $|L_\omega|$ (micro-rotation AM, apparatus) | LIVE | `dark-wake-bemf-foc-synthesis.md:19,52` vs `2026-06-10_genesis-v5-seeded-snap_result.md:45` [branch] |
| C-w | $w$ | photon shear field $w$ **vs** winding $w_{tor}/w_{pol}$ **vs** dark-energy EOS $w_{vac}$ **vs** S11 fit $w_0$ | LIVE | `crystal_engine.py:22` [branch] / `master-equation.md:20` / `appendices-overview.md:101` / `electron-s11-sweep_result.md:65` [branch] |
| C-two-3s | "3" | A1 dilatation-MASS (Heaviside scalar) **vs** Cosserat $(2,3)$ WINDING (helicity) | **RESOLVED in canon** | disambiguation box `master-equation.md:20` (Rule 12, Grant-ratified); registry **cites**, does not re-create |

> The Op-number collision is also live and canon-flagged: the chemistry/molecular Op2/Op3/Op14 catalog
> (CLAUDE.md INVARIANT-N3) is **not** the Vol 1 Ch 6 Op2 (Saturation)/Op3 (Reflection)/Op14 (Dynamic
> Impedance) catalog — `operators.md:23`. Rule 1 applies; cite the Vol-1-Ch-6 sense by default.

---

## 5. RENAME-QUEUE (auditor/Grant-gated — NOT applied)

The registry **renames nothing**. Every proposed rename/annotation of an existing leaf is staged here
for adjudication. Each row: item | current name | proposed | basis | affected files.

> **🟢 EXECUTION UPDATE (2026-06-10, Grant rename-queue adjudication):** rows **R1–R8 + N11 are ADJUDICATED (Grant 2026-06-10) and EXECUTED** on branch `analysis/2026-06-10-rename-queue-execution` (off `main`). Every edit landed as a **Rule-12 annotation / dated note** (frozen prereg bodies untouched per Rule 11; code-comment/docstring fixes in-place); no leaf body was rewritten and **no file was renamed** (the R3 filename rename remains an optional auditor follow-up). Per-row commit cross-refs in the **EXECUTION STATUS** block below the table.

| # | Item | Current name/usage | Proposed (candidate) | Basis | Affected files |
|---|---|---|---|---|---|
| R1 | electron ontology | "The electron is a **self-trapped photon**" ($T_2$-only + TIR, no A1 content) | annotate with a cross-link to the two-objects box ("unknot **dilatation-mass carrying** the $(2,3)$ winding — two objects, not one"); reconcile the ontology | tension between two canon leaves; one says $T_2$-only, the other says A1-mass **+** $T_2$-winding | `photon-identification.md:11`; `master-equation.md:20`; confusion-prone channel line `cosserat-mass-gap.md:108` |
| R2 | BEMF-names-a-field | "the dark wake **IS** the … back-EMF"; "Lenz Back-EMF Freezes Topological $\omega$" | re-tag PORT-only: the wake is **metered** by the Lenz mechanism, the wake is not the BEMF | 2026-06-10 PORT-only ruling (Rule 2); corr 0.117 receipt | `vacuum_engine.py:46,1478,1487`; `dark-wake-bemf-foc-synthesis.md:125`; `claim-quality.md:731` |
| R3 | leaf title | `dark-wake-bemf-foc-synthesis.md` | retitle to separate the **field** (dark wake $\tau^{far}_{zx}$, shear) from the **port** (BEMF) — e.g. "dark-wake / BEMF-port / FOC synthesis" with explicit class tags | Rule 2 (the title lumps a field and a port); flagged in task brief | `dark-wake-bemf-foc-synthesis.md` (title + intro) |
| R4 | $\ell_c$ tri-name | "lattice Cosserat coupling length" / "Cosserat couple-stress length" / "Cosserat characteristic length" | pick ONE normative name across canon (naming-only; same object) | Rule 1 (one object, three names) | `constants.py:255`; `substrate-temporal-values-definition.md:32`; `claim-quality.md:1036` |
| R5 | bare "longitudinal" | unqualified "longitudinal" at shear/EM/port sites | channel-subscript every usage (bulk / shear / EM-forbidden / port-$R_{rad,L}$) | Rule 3 (four-way ambiguous) | `dark-back-reaction-taxonomy.md:11`; `vacuum_engine.py:46,1458,1477`; `rrad-l` prereg:1 |
| R6 | stale $c_{eff}$ | $\omega_{local}=\omega_0\sqrt{1-A^2}$ (single-speed, $(1-A^2)^{1/2}$) | repoint to $c_{shear}=c_0(1-A^2)^{1/4}$ (matter clock) | already canon-flagged STALE (factor-2 exponent) | `op14-local-clock-modulation.md:17,31` |
| R7 | `constants.py:1012` anchor | comment "NU_VAC already defined at line 127" | correct to line 508 | stale internal anchor (verified) | `constants.py:1012` |
| R8 | `RHO_CAV` file attribution | "RHO_CAV=−1/φ (from `constants.py`)" | correct to "from `cavitation_flow.py:64`" (the other primitives on that line ARE in `constants.py`; `RHO_CAV` is not) | wrong-file anchor (verified: `RHO_CAV` defined `cavitation_flow.py:64`, consumed `cavitation_core_probe.py`, PR#161; absent from `constants.py`) | `2026-06-09_rectifier-stage1-biased-diode_prereg.md:34` |

> R1 is the load-bearing one for the auditor: it is a genuine **electron-definition tension between two
> canon leaves**, not a typo. Per flag-don't-fix it is surfaced with both verbatim readings, NOT
> reframed to match. Auditor/Grant adjudicate which ontology is normative (or whether the
> "self-trapped photon" line needs the two-objects annotation).

### EXECUTION STATUS — 2026-06-10 (ADJUDICATED + EXECUTED; branch `analysis/2026-06-10-rename-queue-execution`)

All rows adjudicated by Grant 2026-06-10 and executed as Rule-12 annotations (one commit per ruling, mechanical-first / load-bearing-last). `make verify` green per commit.

| Row | Status | Commit | Execution form |
|---|---|---|---|
| R7 | ADJUDICATED + EXECUTED | `44d5656a` | in-place comment fix (`constants.py:1012`: line 127 → **508**) |
| R8 | ADJUDICATED + EXECUTED | `54f0e98c` | **frozen prereg** (Rule 11) → Rule-12 appended amendment; only `RHO_CAV` repointed to `cavitation_flow.py:64` (the other 4 primitives ARE in `constants.py` — precise split, not a blanket swap) |
| R4 | ADJUDICATED + EXECUTED | `a271894f` | normative "Cosserat coupling length"; dated naming-notes at all 3 sites (bodies preserved) |
| R5 | ADJUDICATED + EXECUTED | `8ecce849` | channel-subscript → shear/port; code docstrings in-place; taxonomy leaf + **frozen** rrad-l prereg via Rule-12 notes |
| R6 | ADJUDICATED + EXECUTED | `721dade0` | STALE-flags repoint $\omega_{local}$ to $c_{shear}=c_0(1-A^2)^{1/4}$ (temporal-values:29); brief refs 17/31 **drifted** → actual table-row 19 + eq 33 annotated |
| R2 | ADJUDICATED + EXECUTED | `05c873e7` | field/port retag (classical lexicon: wake FIELD / $R_{rad,L}$ radiation resistance / Faraday–Lenz back-EMF); code in-place + 2 leaf notes |
| R3 | ADJUDICATED + EXECUTED | `254be06d` | antenna-zone title-clarification block under H1; **filename kept** (rename = optional auditor follow-up) |
| N11 | ADJUDICATED + RECONCILED | `c969e575` (framing §11.6) + this commit (registry §3.8 + novel-objects N11) | screening-current = field; BEMF = its Faraday PORT signature; Meissner-CLASS lens, not identity |
| R1 | ADJUDICATED + EXECUTED | `0b2b4b66` | provenance-vs-state + first-order-class phase-change ontology; evidence table w/ per-signature tags; cross-links at `master-equation.md:20` + `cosserat-mass-gap.md:108` |

Two items surfaced (flag-don't-fix), NOT silently fixed: (1) the **R3 filename rename** is link-breaking → left to the auditor; (2) the **N11 "Meissner/D1-picture section"** named in the ruling does **not exist by that name** in the framing doc — the note was placed at §11 (its nearest home) and the absence surfaced.

---

## 6. Open forks, undeclared bridges, and quarantined cites

### 6.1 The pilot-mode fork (OPEN — Grant-gated; registry records BOTH, resolves neither)

| Reading | Channel | Verbatim anchor |
|---|---|---|
| **Bulk-acoustic** | bulk-longitudinal | `de-broglie-standing-wave.md:50` "longitudinal acoustic pressure waves governed by the vacuum's **Bulk Modulus**" (main, MATCH verified) |
| **Transverse-inductive** | EM-transverse / near-field | `ohmic-decoherence-born.md:11` "the continuous **transverse inductive wake**" (main, MATCH verified) |

Both verbatim cites stand. The fork is **real and OPEN** (`pilotwake-bhphase-survey_note.md:6`,
[branch UNMERGED]). The same fork surfaces in the port layer as **C19**: `X_L` is the **shear** near-field
store (`rrad-l result:111-114,210-222`) yet the propulsion/seed reading wants $X_L$ = the **bulk**
added-mass pilot store — "which elastic channel stores the pilot" is exactly this fork. **Do not resolve.**

### 6.2 U6-class UNDECLARED bridges (registry content, not gaps to paper over)

| Object | Real-space | Phase-space | Bridge status |
|---|---|---|---|
| $\pi_u,\pi_\omega$ (canonical momenta) | conjugate to $u,\omega$ | — | **UNDECLARED** in origin/main core (grep `cosserat_master_equation_fdtd.py` = 0); engine-level only [branch v5] |
| free photon $w$ | travelling $T_2$ mode | — | **UNDECLARED** — a free (untrapped) photon has no trapped phasor; the bridge exists only once TIR-trapped (electron) |
| $V_{inc}$ (phasor) ↔ latent heat (real-space ledger) | standing $V$ as latent heat of freeze | $V_{inc}$ amplitude | **declared but hypothesis-class** on an unmerged branch (`v5 prereg:38`); not yet canon |

### 6.3 Quarantined cites (verified FALSE/UNVERIFIED this session — do NOT import)

- **`RHO_CAV` file attribution** — CORRECTED (an earlier draft over-quarantined this as "FALSE"; that
  was the *challenge-canonical-negative* failure — a constants.py-scoped grep over-generalized to
  "origin/main", carried past the PR#161 cavitation-core-probe merge that **is** the baseline).
  `2026-06-09_rectifier-stage1-biased-diode_prereg.md:34` lists "RHO_CAV=−1/φ" among "canonical primitives
  (from `constants.py`)". The symbol is **real and operational canon**: `RHO_CAV = -1.0/PHI` is defined at
  `cavitation_flow.py:64` and consumed by the **merged** Vol-4 probe `cavitation_core_probe.py:35,69,237,249`
  (PR#161, = this baseline). Only the **file attribution** is wrong — it lives in `cavitation_flow.py`, NOT
  `constants.py` (constants.py-scoped grep = 0). Cite the symbol from `cavitation_flow.py:64`; the misfiled
  "from constants.py" is RENAME-QUEUE R8. The floor-VALUE $-1/\varphi$ epistemic status is itself CONTESTED
  across canon sites (CANDIDATE per `cavitation_flow.py:62` + `v5 prereg:74` vs "Q2 resolved" per
  `substrate-temporal-values:61`) — surfaced §3.3, **not** resolved (flag-don't-fix). The dated
  "GREEN-FIELD" status (`per-node-time-dilation prereg:45`, 2026-06-09) predates the PR#161 merge.
- **"channel-ledger ratification leans bulk"** — FAILED. Recorded as a failed cite at
  `pilotwake-bhphase-survey_note.md:86` (the string "channel-ledger" appears nowhere in `research/` or
  `manuscript/ave-kb/`). Do not import the "leans bulk" lean; the §6.1 fork stands on the two verbatim
  cites alone.
- **"~8 OOM" $L_{bulk}/|L_\omega|$ energy-weight** — UNVERIFIED. The "~8 orders-of-magnitude
  energy-weight" phrasing was **not found verbatim** this session; the nearest receipt is the v5 T3 row
  magnitudes (`2026-06-10_genesis-v5-seeded-snap_result.md:45`). The two-angular-momenta distinction is
  real; the specific "8 OOM" figure is not sourced — do not cite it.

---

## 7. Promotion path (both named; auditor-gated)

This research-doc is the staging draft. Two promotion targets, neither taken here:

1. **A `common/` KB leaf** — the `translation-circuit.md` / `vocabulary-register.md` precedent. Candidate
   home `manuscript/ave-kb/common/field-symbol-registry.md`, written as a **no-claim** leaf that
   **extends** (does not duplicate) the three existing disambiguation assets: the `master-equation.md:20`
   two-"3"s box, `dark-back-reaction-taxonomy.md`, and the `vocabulary-register.md` `def-` spine (each
   homonym row should ultimately mint or cross-link a `def-` node — e.g. link `def-3638f2` for "winding"
   rather than recoin). Promotion = auditor lands the leaf + the `def-` materialization.

2. **A Vol-9 symbol-table appendix/chapter** — a single normative "Symbol & Field Registry" appendix in
   Vol 9 (the cell-datasheet/engineering volume), carrying the §3 table as the front-of-book symbol
   index with the real/phase/bridge columns. Candidate: a Vol-9 appendix chapter
   (`vol9 … /symbol-field-registry.md`), auditor-gated.

Both targets are **auditor-gated**. The RENAME-QUEUE (§5) is a separate adjudication stream: those
items are applied to existing canon only after Grant/auditor sign-off, never by this doc.

> **Lane note.** This is implementer-lane output: it surfaces the empirical nomenclature findings and
> stages the candidates. The auditor lands the `common/`-leaf and Vol-9 manual entries and adjudicates
> the RENAME-QUEUE; Grant adjudicates the §6.1 pilot fork and the R1 electron-definition tension.





