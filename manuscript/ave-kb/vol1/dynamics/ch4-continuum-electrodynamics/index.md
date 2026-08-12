[↑ Dynamics](../index.md)

<!-- kb-frontmatter
kind: index
subtree-claims: [clm-3npynp, clm-527k22, clm-8ep2b4, clm-ce8dg1, clm-crbl60, clm-djpx2v, clm-efo113, clm-fr3mos, clm-i4p11y, clm-lv3uw1, clm-m3z5ux, clm-usflef, clm-utnwkc, clm-uu1qbo, clm-xy252u, clm-yr6tu4]
subtree-experiments: []
-->

# Ch.4: Continuum Electrodynamics and The Dark Sector

The non-linear AVE master equation unifies expanding cosmology and electromagnetism by replacing constant $\varepsilon_0$ with field-dependent $\varepsilon_{eff}(V)$. Three analytical operating regimes are defined (linear acoustic, non-linear tensor, dielectric rupture). The MOND $a_0$ boundary is derived from the 1D Hoop Stress projection of the 3D expanding Hubble horizon, and dark matter is identified as unbroken kinematic mutual inductance of the spatial network.

## Key Results

| Result | Statement |
|---|---|
| Unifying AVE Master Equation | $\nabla^2 V - \mu_0\varepsilon_0\sqrt{1-(V/V_{yield})^2}\;\partial^2 V/\partial t^2 = 0$ |
| Field-Dependent Wave Speed | $c_{eff}(V) = c_0(1-(V/V_{yield})^2)^{-1/4}$ |
| Effective Inductive Node Mass | $m_{node} = \xi_{topo}^2\mu_0\ell_{node}$ |
| Macroscopic Bulk Mass Density | $\rho_{bulk} = \xi_{topo}^2\mu_0/(p_c\ell_{node}^2) \approx 7.91\times10^6$ kg/m$^3$ *(engine-lockstep re-pin 2026-08-03, Rule 12: prior value ~~$7.92\times10^6$~~; receipt at [`lc-electrodynamics.md`](lc-electrodynamics.md):35)* |
| Baseline 3D Vacuum Shear Modulus | $G_{vac} = \rho_{bulk} \cdot c^2 \approx 7.12\times10^{23}$ Pa (corrected 2026-05-17; cross-check $v_T = \sqrt{G_{vac}/\rho_{bulk}} = c$) |
| 1D String Tension Density (axial stiffness) | $G_{string} = m_e c^2/\ell_{node}^2 \approx 5.49\times10^{11}$ Pa (formerly mis-labeled as $G_{vac}$; distinct quantity per [`../../../vol2/appendices/app-f-solver-toolchain/derived-numerology.md:49-56`](../../../vol2/appendices/app-f-solver-toolchain/derived-numerology.md)) |
| Kinematic Network Mutual Inductance | $\nu_{kin} = \alpha c\ell_{node} \approx 8.45\times10^{-7}$ m$^2$/s |
| Macroscopic Yield Stress Limit | $\tau_{yield} = (\rho_{bulk}c^2)(6\times\mathcal{V}_{crossing})(p_c/8\pi)$ |
| Asymptotic Hubble Constant | $H_\infty = 28\pi m_e^3 cG/(\hbar^2\alpha^2) \approx 69.32$ km/s/Mpc |
| Geometric Drift Acceleration (MOND $a_0$) | $a_{genesis} = cH_\infty/(2\pi) \approx 1.07\times10^{-10}$ m/s$^2$ |
| Longitudinal (P) Wave | $c_L = \sqrt{(K_{vac}+\tfrac{4}{3}G_{vac})/\rho_{bulk}} = \sqrt{10/3}\,c \approx 1.83c$ at $K=2G$ ($\nu=2/7$; canonical vol_2 Ch 7). Prior $\sqrt{2}\,c = \sqrt{K/\rho}$ = bulk-modulus dilatational speed (omits $4G/3$ shear) — 2026-06-08 c_L reconciliation 🔴 **[DEMOTED 2026-08-11 — R40-B2a: NEEDS RE-DERIVATION, not dead; dated note at the end of this file]** |

## Derivations and Detail

| Document | Contents |
|---|---|
| [Master Equation](./master-equation.md) | D'Alembert operator, non-linear permittivity collapse, field-dependent wave speed, unifying master equation |
| [LC Electrodynamics](./lc-electrodynamics.md) | Node mass, bulk mass density, shear modulus, kinematic mutual inductance |
| [Operating Regimes Table](./operating-regimes-table.md) | Three-regime classification: linear acoustic, non-linear tensor, dielectric rupture |
| [Magnetic Saturation](./magnetic-saturation.md) | Macroscopic yield stress limit, zero-impedance slipstream, dark matter as unbroken $\eta_{eff}$ |
| [MOND from Hoop Stress](./mond-hoop-stress.md) | $H_\infty$ derivation, hoop stress projection, geometric drift acceleration |
| [Dark Sector Comparison](./dark-sector.md) | AVE vs observation: $H_\infty$, $a_0$, dark matter, dark energy |
| [Bullet Cluster](./bullet-cluster.md) | Refractive tensor shockwaves, DAMA/LIBRA vs XENONnT resolution |
| [Photon Identification (T₂-only Cosserat ω)](./photon-identification.md) | Canonical AVE-native photon: K4 4-port = $A_1 \oplus T_2$, $A_1$ dissipates monotonically, $T_2$ survives as photon; single-sector (microrotation $\omega$, $u = 0$); electron = photon + Axiom 4 TIR confinement at $V_{\text{yield}} = \sqrt{\alpha} V_{\text{snap}}$; Compton frequency as dynamical threshold for three regimes (transparent / bound / Compton-scatter) |
| [Photon EE Mapping (free $Z_0$/$\Gamma=0$ vs self-trapped $\Gamma=-1$)](./photon-ee-mapping.md) | Consolidation/translation leaf (the translation-circuit.md:173 "pending" E↔B leaf): free photon (single-sector $T_2$, matched $Z_0$, $\Gamma=0$, NO core) vs self-trapped electron (magnetic-branch $\mu_{eff}\to0$, $\Gamma=-1$ Local Bubble, shorted $\lambda/4$ resonator); carrier × envelope; the photon's own $E$↔$B$ as a LINEAR I/Q quadrature on $(V_{inc},V_{ref})$ / $V\leftrightarrow\Phi_{link}$, disambiguated from the parametric K4↔Cosserat pair-production bridge; carries the R·r≠¼ Class-B + helical-photon-retraction + autoresonance flags (genesis-self-lock TESTED-NEGATIVE 2026-06-14; mapping + detector-instrument still GAP) |
| [Photon Propagation Baseline ($v/c = \sqrt{2}$)](./photon-propagation-baseline.md) | Canonical empirical baseline: free photon on K4-TLM linear vacuum propagates at $v = c\sqrt{2}$ cardinal-axis (pure substrate-geometry, native Axiom 1); $v = c$ diagonal-axis; substrate-perspective verification of $T_2$-only, no-saturation, linear regime |
| [Breathing Soliton v14 Mode-I PASS](./breathing-soliton-v14-mode-i.md) | Master Equation FDTD hosts breathing soliton at 4/4 acceptance criteria: $V_{\text{peak}}$ mean $= 0.250$, FWHM stable, $\Delta n = 0.0111$ measurable, Q-factor $102.8$ vs $137$; validates boundary-envelope reformulation at dynamic engine level; three-level boundary distinction |
| [Preferred Frame + Emergent Lorentz from K4 Cubic Symmetry](./preferred-frame-and-emergent-lorentz.md) | K4 lattice rest frame = CMB rest frame; Earth moves through it at 370 km/s; cubic-symmetry ($Fd\bar{3}m$) suppresses observable anisotropy to $(q\ell_{node})^4 \sim 10^{-22}$ at optical scales; strict Lorentz invariance at observable wavelengths is EMERGENT not axiomatic; classifies Sagnac/preferred-frame matrix tests (A2 rotor-local works, C17 optical-wavelength predicts NULL, C7 Trans-Planckian survives as forward prediction) |

> Primary: [MOND Hoop Stress](./mond-hoop-stress.md) — path-stable leaf referenced from vol6 as `sec:galactic_saturation` and `eq:H_infinity`

---

## R40 batch-2a — NEEDS-RE-DERIVATION status note (2026-08-11)

**Class:** status demotion under **R40**. This note mints no `clm-`/`def-`/`exp-`/`sup-`/`ilk-`,
**moves no solidity number**, adjudicates no channel and opens no fork. Every byte of each demoted
claim is preserved; the stamped line gains a status marker only (honesty-lag pattern, Rule 12).

**The arc, in four clauses (R40's header form; clause 4 points at the LANDED artifact, not at a
ruling record).**

1. **The kill fired** — the walk-back that closed the bulk radiative-port reading.
2. **The premise localized to the imported `K = 2G` elastic modulus** — the compressible far-field
   branch was minted by a GR-imported modulus, not forced by the axioms.
3. **The axioms underdetermine the bulk sector** — the flat-direction finding: the written action
   conserves the Gauss function pointwise and never fixes its value.
4. **The replacement is the LANDED ratified bound-sector law — Axiom 5, Substrate DC Bias**, clauses
   **S** (deposit), **G** (bias coupling / bridge) and **Q** (quiescence), canonical at
   [`eq_axiom_5.tex`](../../../../common_equations/eq_axiom_5.tex) with its register entry in
   [`axiom-register.md`](../../../common/axiom-register.md) (§ *Axiom 5 — Substrate DC Bias*). Under
   clause **G** the A1 / bulk slot is a **bound response** — $\mathbf{u}_0 =
   -\mathcal{A}_g\nabla\varepsilon_{11}$, mechanism gloss **back-reaction** — with **no independent
   propagating branch, no port and zero longitudinal characteristic speed**. A bulk *wave speed*, a
   bulk *radiative port*, a bulk *band-branch* and a bulk *transit clock* therefore have **no
   referent**, and each row below owes its re-derivation on that footing.
   $\mathcal{A}_g$ (the **bias-coupling area**) is an `UNVALUED-RATIFIED-CONSTANT` per **R48**
   ([`interlock-register.md`](../../../common/interlock-register.md), § *𝒜_g — the bias-coupling
   area*): it is **not valued here or anywhere**, and **the calibration count stays 3**.

**Standing named-open debt — the honesty rider.** The ratified axiom does **not** discharge
everything. **THE BIAS PROPAGATION THEOREM is Axiom 5's standing named-open debt**, stated by the
axiom's own phase-structure paragraph, clause **(c1)**: clause G's elliptic law is the *static
abstraction of underived finite-speed bias dynamics*, and the $(u,\pi)$ no-signalling theorem does
**not** cover the bias read — the bias's finite propagation speed is *owed, not held*. Every row
tagged **⚑ BIAS-DEBT** below re-derives against the ratified axiom **with that debt standing**, never
against a closed replacement.

**Vocabulary.** Canonical nouns authored here: **the bound response** ($\mathbf{u}_0$), **the bias**
($\varepsilon_{11}$), the **DC operating point / quiescent point (Q-point)**; **back-reaction** is
the mechanism gloss. *"dress"*, *"grade"* as $\varepsilon_{11}$'s canonical noun, and *"halo"* for
the physics (the physics noun is the **near-field store / added-mass**) are RETIRED by **R50**;
*"retardation"* is retired by **R49(b)** in favour of **propagation delay / finite propagation
speed**. Corpus text quoted below is byte-exact and is never reworded.

**Rows carried in this file.**

- **`:27`** — stamped at `:27`. *(family: register-row)*  ⚑ **BIAS-DEBT**
  Quoted claim (content verified at HEAD; markup-reduced from the banked audit):
  ```text
  Longitudinal (P) Wave | $c_L = \sqrt{(K_{vac}+\tfrac{4}{3}G_{vac})/\rho_{bulk}} = \sqrt{10/3}\,c \approx 1.83c$ at $K=2G$
  ```
  Audited rationale, verbatim from the banked worklist:
  ```text
  Key-results register row recording the imported reading's state — prereg's explicit NEEDS class; re-route with the leaf-level dispositions.
  ```

  **Resolution.** The demoted carrier is the propagating A1 / bulk branch; under Axiom 5 clause G that slot is the **bound response**, so the re-derivation must be re-posed on the bound-sector constitutive law (bias $\varepsilon_{11}$, bound response $\mathbf{u}_0$, mechanism gloss back-reaction) rather than on a compression wave. **⚑ BIAS-DEBT:** this row's re-derivation turns on finite-speed bias dynamics, so the resolution is the ratified axiom **with THE BIAS PROPAGATION THEOREM standing** (clause (c1)) — the replacement is *owed, not held*.

**Records.** Ruling **R40** (the demotion sweep) · the banked worklist
[`r40_sweep_worklist_verified.json`](../../../../../research/drivers/r40_sweep_worklist_verified.json) · batch-0
scope verification and batch-1 execution records in `_orchestration/` · this batch's record
`_orchestration/2026-08-12_r40-sweep-batch2a.md`.

