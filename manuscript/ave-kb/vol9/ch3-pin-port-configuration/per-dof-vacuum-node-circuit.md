[↑ Ch.3 Pin/Port Configuration](index.md)

<!-- kb-frontmatter
kind: leaf
no-claim: "Vol-9 Class-C CONSISTENCY re-expression — the per-DOF node-constitutive layer (reactive tensor (L_i,C_i) per translation DOF) BENEATH AVE_VACUUM_CELL (§1) and the graded vacuum impedance network (§6). Unifies three already-asserted behaviors (isotropic achromatic / deviatoric birefringence / high-k (qℓ)⁴ anisotropy) into one node-constitutive structure. Originates NO new substrate primitive and NO value-prediction; the c₀/Z₀ recovered in the isotropic continuum limit are KNOWN anchors (validate-on-known gate), not emergent values."
-->

> 🔴 **QED-NORMALIZATION CORRECTION (2026-07-03; Rule-12 — body preserved below, git is the trail).**
> The birefringence coefficient ratio "7.5/α³ ≈ 1.93×10⁷" referenced below carries an understated QED
> denominator. **Corrected: 7.5π/α² ≈ 4.42×10⁵** (propagating, the headline). The node-constitutive structure
> (per-DOF (Lᵢ,Cᵢ), the deviatoric-strain split, the (qℓ)⁴ anisotropy) is UNAFFECTED — only the field-E²-index
> AVE/QED magnitude ratio changes. Canonical:
> [`../../vol4/falsification/ch12-falsifiable-predictions/vacuum-birefringence-e4.md`](../../vol4/falsification/ch12-falsifiable-predictions/vacuum-birefringence-e4.md);
> reconciliation `research/2026-07-03_birefringence-qed-normalization-correction.md`.

## Per-DOF Vacuum Node Circuit (node-constitutive layer, canonical leaf)

**Classification:** Class C — CONSISTENCY re-expression. The cell-level `AVE_VACUUM_CELL` ([`device-circuit-models.md`](device-circuit-models.md):52) gives ONE scalar reactive pair per node ($L_{\mathrm{cell}}=\mu_0\ell_{\mathrm{node}}$, $C_{\mathrm{cell}}=\varepsilon_0\ell_{\mathrm{node}}$). This leaf makes that pair a **constitutive TENSOR**: each translation DOF $i\in\{x,y,z\}$ carries its OWN reactive pair $(L_i,C_i)$. This is the node-level structure REQUIRED beneath the cell model, because **a scalar node cannot represent the directional anisotropy that shear induces** — and it is the missing node-constitutive layer beneath the graded vacuum impedance network ([`device-circuit-models.md`](device-circuit-models.md):127, §6).

**Skills applied (2026-06-19 pass):** `substrate-native-check` (K4 bond-set, not Cartesian grid) · `consistency-vs-emergence` v1.3 (Class-C tag; structural-vs-asserted table §5) · `pre-test-physics-check` · `verify-before-cite` (anchors re-grepped on HEAD `bb206fa2`) · `phase-space-coordinate-check` (mechanical-displacement coords, distinct from A1 phasor).

**Discipline:** This leaf is the **source of truth** for the per-DOF node-constitutive layer. The CODE demonstration is `src/ave/core/vacuum_node_circuit.py` + driver `src/scripts/vol_9_device/per_dof_node_dispersion_demo.py` (results `_output/per_dof_node_dispersion_demo.json`); tests `src/tests/test_vacuum_node_circuit.py` (22 passing).

> ↗ See also: [`device-circuit-models.md`](device-circuit-models.md) §1 (cell model this extends), §6 (graded network this underlies); [`achromatic-impedance-matching.md`](../../vol3/gravity/ch03-macroscopic-relativity/achromatic-impedance-matching.md) (the SYM ε·μ co-scale, behavior 1); [`vacuum-birefringence-e4.md`](../../vol4/falsification/ch12-falsifiable-predictions/vacuum-birefringence-e4.md) (strain birefringence, behavior 2); [`preferred-frame-and-emergent-lorentz.md`](../../vol1/dynamics/ch4-continuum-electrodynamics/preferred-frame-and-emergent-lorentz.md) §2 + `clm-pp3qwf` ((qℓ)⁴ cubic anisotropy, behavior 3); `research/2026-06-19_electrical-mechanical-projection-map.md` (the EM↔mechanical grade-domain seams this leaf must NOT collapse).

---

### 1. The per-DOF node circuit (constitutive tensor)

Between any two substrate nodes the cell model assigns one $(L_{\mathrm{cell}},C_{\mathrm{cell}})$. The per-DOF node refines this: the reactive pair is **diagonal in the three translation directions**, with a per-DOF multiplier on the cold baseline:

$$L_i = \lambda^L_i\,L_{\mathrm{cell}} = \lambda^L_i\,\mu_0\ell_{\mathrm{node}}, \qquad C_i = \lambda^C_i\,C_{\mathrm{cell}} = \lambda^C_i\,\varepsilon_0\ell_{\mathrm{node}}, \qquad i\in\{x,y,z\}.$$

The cold vacuum is $\lambda^L_i=\lambda^C_i=1$ on every DOF (isotropic). A STATE (saturation, shear strain) is a choice of the six multipliers $\{\lambda^L_i,\lambda^C_i\}$. The three regimes below are three such choices.

**Why a tensor and not a scalar.** A scalar node has one $(L,C)$ and therefore one $c$, one $Z$ — it is intrinsically isotropic and **cannot** carry a direction-dependent wave speed. Birefringence (behavior 2) is by definition a direction/polarization split of $c$; it has NO representation on a scalar node. The per-DOF tensor is the minimal node-constitutive structure that can host it. This is the structural reason the layer is REQUIRED, not a convenience.

### 2. Directional wave speed and impedance

Because $L_{\mathrm{cell}},C_{\mathrm{cell}}$ are **lumped per-node** values (Henries, Farads), $\sqrt{L_iC_i}$ is the propagation DELAY across one node-span of length $\ell_{\mathrm{node}}$; the section wave speed carries the $\ell_{\mathrm{node}}$ factor:

> **[Resultbox]** *Per-DOF wave speed and impedance*
>
> $$c_i = \frac{\ell_{\mathrm{node}}}{\sqrt{L_i C_i}} = \frac{1}{\sqrt{\lambda^L_i\lambda^C_i}}\cdot\frac{1}{\sqrt{\mu_0\varepsilon_0}}, \qquad Z_i = \sqrt{\frac{L_i}{C_i}} = \sqrt{\frac{\lambda^L_i}{\lambda^C_i}}\cdot\sqrt{\frac{\mu_0}{\varepsilon_0}}.$$

**VALIDATE-ON-KNOWN (the Build-A wire-first lesson).** For the cold node ($\lambda=1$): $c_i = 1/\sqrt{\mu_0\varepsilon_0} = c_0$ and $Z_i = \sqrt{\mu_0/\varepsilon_0} = Z_0 \approx 376.73\,\Omega$ on every DOF. The CODE asserts this to `rtol 1e-12` and HALTs if it fails (`per_dof_node_dispersion_demo.py`; `test_cold_node_recovers_c0_exactly`, `test_cold_node_recovers_Z0_exactly`). **The validate-gate CAUGHT a real bug:** the naive per-unit-length form $c=1/\sqrt{LC}$ gives $c_0/\ell_{\mathrm{node}}$ (off by $\sim10^{12}$); only the lumped-section form $c=\ell_{\mathrm{node}}/\sqrt{LC}$ recovers $c_0$. A model that does not recover $c_0/Z_0$ in the isotropic continuum limit is wrong.

---

### 3. The three behaviors as structural consequences (the value of the model)

ONE circuit, THREE behaviors — each a choice of the per-DOF multipliers. This is a CONSISTENCY re-expression: it does not add a new mechanism, it shows three already-asserted behaviors are consequences of one node-constitutive tensor.

#### 3.1 ISOTROPIC (volumetric saturation $S$) → achromatic + isotropic

When the node is volumetrically strained, BOTH $L$ and $C$ co-scale EQUALLY across all $i$: $\lambda^L_i=\lambda^C_i=n$ for every $i$. This is the node-level form of the SYM $\varepsilon\cdot\mu$ co-scale: $\mu'=n\mu_0$, $\varepsilon'=n\varepsilon_0$ ([`achromatic-impedance-matching.md`](../../vol3/gravity/ch03-macroscopic-relativity/achromatic-impedance-matching.md):20). Consequence:

$$c_i = \frac{c_0}{n}\ \text{(uniform, isotropic)}, \qquad Z_i = Z_0\ \text{(INVARIANT)} \Rightarrow \Gamma = \frac{Z_i-Z_0}{Z_i+Z_0} = 0.$$

Light **bends** (the wave speed drops by $1/n$) but does **NOT disperse** ($n$ is the same in every direction) and does **NOT reflect** ($Z=Z_0$, matched). This is the achromatic impedance-matched lens, derived at the node. CODE: `isotropic_saturated`; `test_isotropic_saturation_Z_invariant` ($\Gamma=0$ to `atol 1e-12`).

#### 3.2 DEVIATORIC (shear strain) → birefringence FORM

A deviatoric (traceless, volume-preserving) strain SPLITS the pairs: it adds to one direction what it removes from another. Applied on the $\varepsilon/C$ side (the metric-varactor sector that carries the index, [`vacuum-birefringence-e4.md`](../../vol4/falsification/ch12-falsifiable-predictions/vacuum-birefringence-e4.md):12) with amplitude $\delta$:

$$\lambda^C = (1+\delta,\,1-\delta,\,1), \quad \lambda^L = (1,1,1) \;\Rightarrow\; L_xC_x \neq L_yC_y \;\Rightarrow\; c_x \neq c_y.$$

The directional split $\Delta c/c = (c_x-c_y)/\bar c$ is **strain-induced birefringence** — a $\delta n$ between polarizations. The model reproduces the **FORM** $\delta n \propto (\text{deviatoric strain})$: the CODE shows $\Delta c/c$ monotone and $\approx-\delta$ to leading order (`test_birefringence_form_scales_with_deviatoric_strain`). This is the node-level origin of the shipped strain-birefringence falsifier ([`vacuum-birefringence-e4.md`](../../vol4/falsification/ch12-falsifiable-predictions/vacuum-birefringence-e4.md), `clm-pp3qwf`). **The specific coefficient ($\delta n\propto E^4$/$E^2$ magnitude, the AVE-vs-QED discriminator) is a SEPARATE quantitative test and is NOT re-derived here** — only that the model PRODUCES birefringence from deviatoric strain.

> **Field-exponent RESOLVED (2026-06-24, KEEP-BOTH additive — sentence above unedited).** The "$\delta n\propto E^4$/$E^2$ magnitude" phrasing above left the *field exponent* as an open AVE-vs-QED axis. It is **closed:** the field-dependent index shift is **$E^2$-leading for BOTH** AVE and QED — the historical "$E^4$" was a $\sqrt\varepsilon$ conflation (the permittivity-saturation DEPTH $1-S=+A^2/2$ is $E^2$-leading; the index observable $n=\sqrt S$ gives $\delta n_{iso}=-\tfrac14 A^2$). The AVE-vs-QED discriminator that remains is the **COEFFICIENT** (matched par−perp differential ratio $7.5/\alpha^3\approx1.93\times10^7$, an $\alpha$-echo) and the **E-vs-B keying asymmetry**, NOT the exponent — see [`vacuum-birefringence-e4.md`](../../vol4/falsification/ch12-falsifiable-predictions/vacuum-birefringence-e4.md):41 (clm-pp3qwf, commit `ad26d357`) and the Vol-9 IM3 datasheet [`vacuum-node-im3-distortion.md`](vacuum-node-im3-distortion.md). **Note the distinct mechanism:** this leaf's *deviatoric-strain* split and the $(q\ell_{node})^4$ lattice anisotropy (§3.3, [`k4-bloch-dispersion-quartic.md`](../../vol4/falsification/ch12-falsifiable-predictions/k4-bloch-dispersion-quartic.md)) are **wavevector**-quartic (spatial-dispersion FORMS), categorically separate from the **field**-$E^2$ index shift — the field-exponent retraction does NOT touch the $(q\ell)^4$ chord.

#### 3.3 HIGH-k ($\lambda\sim\ell_{\mathrm{node}}$) → the discreteness anisotropy tells

> **🔴 PHOTON $(q\ell)^4$ DEMOTED → CONDITIONAL on the unproven weak-C theorem (2026-06-25, P1b; body below PRESERVED unedited).** The **MATTER $(q\ell)^2$ row stands**; the **PHOTON $(q\ell)^4$ row is DEMOTED, not refuted.** The genuine 24×24 chiral-srs Bloch eigensolve (P1b, branch `engine/p1b-modes-live`, driver `srs_bloch_dispersion.py`, verified) measures the photon band-edge anisotropy at **slope-2** (1.9999; $a_2{=}{+}0.056$ dominant over $a_4{=}{-}0.0017$; both enantiomorphs; cross-checked by raw $[100]$–$[111]$ ratio $=4.0=\mathcal O(k^2)$), **NOT slope-4.** The `slope 4.000` in the table below and in `per_dof_node_dispersion_demo.json` is the hardcoded `photon_birefringence` **inserted exponent** (`vacuum_node_circuit.py:302`) — the SAME re-stated exponent demoted at [`k4-bloch-dispersion-quartic.md`](../../vol4/falsification/ch12-falsifiable-predictions/k4-bloch-dispersion-quartic.md):92-103 (clm-k4d4ph 0.70→0.60), NOT an eigensolve result. The distinctive photon quartic requires **weak-C** (the photon's $\mathcal O(q^2)$ EM correction must be isotropic so the first anisotropy is quartic — the "DERIVED (the FORM)" grading in the table and in §5) — an **OPEN theorem** (gate wejkhvnfb); the genuine eigensolve does NOT exhibit it. The quartic **could RETURN if weak-C is proven.** Small-k emergent-Lorentz isotropy SURVIVES (this is band-edge anisotropy, not a low-k Lorentz violation); $\delta{=}0$ continuum-exact OPEN on the same lever.

The discrete K4 lattice dispersion $\omega(q)$, built from the **actual tetrahedral bond set** (not a Cartesian stencil — §4), exposes the lattice anisotropy as $q\ell_{\mathrm{node}}\to\mathcal O(1)$. There are TWO distinct tells, and the corpus already holds them apart:

| Carrier | Anisotropy order | Why | CODE |
|---|---|---|---|
| **MATTER** (node-LOCKED) | $(q\ell_{\mathrm{node}})^2$ | the mechanical dynamical-matrix tensor $\sum_b \hat b_a\hat b_b(\hat q\!\cdot\!\hat b)^2$ is already anisotropic at $\mathcal O(q^2)$ — the zone-edge bending | `directional_anisotropy`; slope $2.000$ |
| **PHOTON** (continuum, unlocked) | $(q\ell_{\mathrm{node}})^4$ | the $\mathcal O(q^2)$ EM correction is the ISOTROPIC cubic invariant $|q|^2$; the FIRST anisotropic invariant is the QUARTIC $q_x^4+q_y^4+q_z^4$ (cubic point group) | `photon_birefringence`; slope $4.000$ |

This reproduces the corpus's own matter-vs-photon split ([`preferred-frame-and-emergent-lorentz.md`](../../vol1/dynamics/ch4-continuum-electrodynamics/preferred-frame-and-emergent-lorentz.md) §2, [`binary-kill-switches.md`](../../vol4/falsification/ch12-falsifiable-predictions/binary-kill-switches.md):17,19): the lattice-locked matter carrier sees the $(q\ell)^2$ zone-edge dispersion; the continuum photon does NOT (it is sub-saturation, $Z_0$-matched), so its leading anisotropy is the $(q\ell)^4$ optical birefringence "by inheriting the lattice's cubic symmetry" ($\delta_{\mathrm{aniso}}\approx2.2\times10^{-22}$ at $\lambda=633$ nm, `clm-pp3qwf`). The achromatic isotropy of §3.1 is exact only in the continuum limit $\lambda\gg\ell_{\mathrm{node}}$ ($q\ell\to0$); the $(q\ell)^4$ tell is the residual. **The absolute magnitude is NOT re-derived; only the FORM (the (qℓ)⁴ scaling + the cubic direction-dependence).**

> **HONEST GRADE-FINDING (flag-don't-fix, surfaced at build-time).** The per-DOF MECHANICAL node naturally yields the **$(q\ell)^2$ MATTER** form; the **$(q\ell)^4$ PHOTON** form is the EM-mode cubic-invariant statement, NOT a mechanical dynamical-matrix eigenvalue. They are the same lattice's two carrier classes, exactly as the corpus splits them. The model does not collapse them into one — a generic mechanical lattice wave splits at $(q\ell)^2$; only the EM transverse mode's $\mathcal O(q^2)$ isotropy pushes the photon split to $(q\ell)^4$.

---

### 4. Grade clarity (the hard guard)

**The per-DOF $(L_i,C_i)$ is the MECHANICAL displacement-direction constitutive layer of the EM-translation sector** — the cell's three translational $\mathbf u\to\mathbf E$ modes ([index](index.md):17). It is NOT, and must never be wired into:

- the **A1 $(V_{\mathrm{inc}},V_{\mathrm{ref}})$ dilatation-MASS phasor** (the "mass-3"; $V_{\mathrm{ref}}$ is a read-only projection of the same scalar $V$, not an independent DOF — the genesis-24 / $w_{\mathrm{pol}}=0$ double-count, [`master-equation.md`](../../vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md):20), nor
- the **Cosserat $(2,3)$ micro-rotation WINDING** (the "charge-3"; orthogonal, $A1\perp T2$, [`master-equation.md`](../../vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md):20).

The three translation DOF here are the mechanical displacement directions $u_i$ (3 translational, [index](index.md):17), which project to the EM-transverse channel. The graded-network's **EM / shear / bulk wave-channel triple is a SEPARATE axis** (substrate GRADES living in mixed impedance DOMAINS — $\Omega$ vs $\rho c$, [`device-circuit-models.md`](device-circuit-models.md):139). Do **NOT** collapse the per-DOF-translation axis into the grade axis (the seam-7 refuted-bijection guard, `research/2026-06-19_electrical-mechanical-projection-map.md`:65). This leaf lives entirely inside the EM-translation grade and models its node-level directional anisotropy; it touches neither the mass-sector store nor the charge winding.

**Substrate-native (the RANK-2 lesson).** The per-DOF tensor sits on the **K4 / tetrahedral bond set** (`K4_BOND_DIRECTIONS`, the four ports of [`k4_tlm.py`](../../../../src/ave/core/k4_tlm.py):110-117), NOT a Cartesian 6-port grid. The $(q\ell)^4$ anisotropy is read off the DIFFERENCE between bond-direction and face-direction propagation — the cubic ($Fd\bar3m$) symmetry the continuum photon inherits. The tetrahedral 2nd-moment $\sum_b(\hat q\!\cdot\!\hat b)^2 = 4/3$ for EVERY direction (`test_tetrahedral_second_moment_isotropic`) is the $\mathcal O(q^2)$ isotropy; the 4th-moment is the first cubic anisotropy. A Cartesian-stencil dispersion would mis-attribute the anisotropy order.

---

### 5. What is structurally-derived vs asserted (consistency-vs-emergence)

| Element | Class | Status |
|---|---|---|
| Per-DOF reactive tensor $(L_i,C_i)$ as the layer beneath the scalar cell | **structural** | DERIVED — the minimal structure that can host directional $c$; a scalar node provably cannot |
| $c_i=\ell_{\mathrm{node}}/\sqrt{L_iC_i}$, $Z_i=\sqrt{L_i/C_i}$ | **structural** | DERIVED — lumped-section TLM identity |
| Isotropic co-scale $\Rightarrow Z=Z_0,\Gamma=0$ (achromatic) | **structural** | DERIVED — the SYM $\varepsilon\mu$ co-scale at the node (re-expresses achromatic-impedance-matching.md) |
| Deviatoric split $\Rightarrow$ birefringence EXISTS | **structural** | DERIVED (the FORM) — re-expresses the strain-birefringence falsifier's node origin |
| Birefringence COEFFICIENT ($\delta n\propto E^2$ magnitude; "$E^4$" was the $\sqrt\varepsilon$-conflation field-exponent, RETRACTED clm-pp3qwf) | — | **NOT re-derived** — separate quantitative test (vacuum-birefringence-e4.md, clm-pp3qwf); field-exponent is $E^2$ for both AVE+QED, discriminator = coefficient + E-vs-B keying |
| $(q\ell)^2$ matter zone-edge / $(q\ell)^4$ photon birefringence ORDERS | **structural** | DERIVED (the FORM) — re-expresses preferred-frame §2 group theory; the matter/photon split is the corpus's own |
| $(q\ell)^4$ ABSOLUTE magnitude ($\approx2.2\times10^{-22}$) | — | **NOT re-derived** — clm-pp3qwf, asserted upstream |
| $c_0$, $Z_0$ recovered in the isotropic continuum limit | **consistency** | KNOWN ANCHORS — validate-on-known gate, NOT a value-prediction |
| $\alpha$, $m_e$ values | — | **NOT PREDICTED** — the model is structural; no value-echo leaks in |

**Bottom line:** the model is a CONSISTENCY re-expression. Its content is *one node-constitutive structure → three behaviors as consequences*. It originates no new substrate primitive and no new value. It is honest about the boundary: the FORMS (achromatic, birefringence-exists, the $(q\ell)$ anisotropy orders) are structural consequences; the coefficients/magnitudes/$\alpha$/$m_e$ are NOT re-derived here.

---

### Verify-before-cite audit log (2026-06-19, HEAD `bb206fa2`)

| Cited anchor | Verification |
|---|---|
| `device-circuit-models.md`:52 ($L_{\mathrm{cell}}=\mu_0\ell$, $C_{\mathrm{cell}}=\varepsilon_0\ell$) | grep ✓ |
| `device-circuit-models.md`:127,139 (graded network §6; mixed impedance domains) | grep ✓ |
| `achromatic-impedance-matching.md`:20 ($\mu'=n\mu_0$, $\varepsilon'=n\varepsilon_0$) | grep ✓ |
| `vacuum-birefringence-e4.md`:12 (only $\varepsilon$ strained, $n=\sqrt S$); coefficient = separate test | grep ✓ |
| `preferred-frame-and-emergent-lorentz.md` §2 ($q^2$ isotropic / $q^4$ first cubic anisotropic invariant) | grep ✓ (lines 47-50) |
| `binary-kill-switches.md`:17,19 (matter $(q\ell)^2$ zone-edge vs photon $(q\ell)^4$ birefringence) | grep ✓ |
| `master-equation.md`:20 (two-3s fence; $V_{\mathrm{ref}}$ not independent) | grep ✓ |
| `k4_tlm.py`:110-117 (tetrahedral bond directions = K4 ports) | grep ✓ |
| CODE results (c₀/Z₀ recovery, slopes 2.000 / 4.000, Γ=0) | `per_dof_node_dispersion_demo.json`; 22/22 tests ✓ |

---
