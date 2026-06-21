[↑ Vol 9: The Vacuum Datasheet](../index.md)

<!-- kb-frontmatter
kind: index
subtree-claims: []
subtree-experiments: []
-->

# Ch.10 Magnetic and Microrotational Characteristics

Chapter 10 of the Vol 9 datasheet documents the substrate's microrotational (B-sector) DOF — the rotational half of the Cosserat micropolar 6 DOF / node structure (Axiom 1). Documents bond inductance $L_{cell} = \mu_0\, \ell_{node}$ (microrotational analog of bond capacitance), magnetic-rotation node-destruction field $B_{snap}$, Cosserat couple-stress modulus $\gamma_c$, rotation-sector mass-gap $m_\omega \sim 1$ MeV (ferrite-Curie analog), and Cosserat characteristic length $l_c = \sqrt{\gamma_c / G_{vac}}$ identified with the weak-force range $r_W$.

## Substrate-native framing

Per Axiom 1 (CLAUDE.md INVARIANT-S2 verbatim): the natural vacuum is a 3D chiral Laves K4 Cosserat crystal with **micropolar nodes carrying 6 DOFs each: 3 translational → E, 3 microrotational → B; the Cosserat rotational DOF IS the substrate-native origin of intrinsic spin**.

The magnetic sector of the substrate is the rotational half of those 6 DOFs / node:

- **3 microrotational DOFs / node** — independent Cosserat micro-rotation coordinates $\boldsymbol{\omega}(\mathbf{r}, t)$ at every K4 node (not derived from $\mathbf{u}$ as in classical Cauchy elasticity; this independence is the defining feature of a Cosserat micropolar continuum).
- **Inductive coupling $\mu_0$** — bond-level microrotation density. Per-bond inductance $L_{cell} = \mu_0\, \ell_{node}$ is the microrotational analog of bond capacitance $C_{cell} = \varepsilon_0\, \ell_{node}$.
- **Magnetic field $\mathbf{B}$** — substrate-observable signature of microrotational density. Macroscopic $\mathbf{B}$ is the coarse-grained microrotation field; $\mathbf{B}$ is not abstracted from a more primitive mechanical quantity, it IS the substrate's Cosserat rotational state.
- **Substrate-native origin of intrinsic spin** — the same Cosserat microrotational DOF, integrated across an extended closed soliton defect, produces the SU(2) / SO(3) double-cover spin-½ representation classically via the Finkelstein–Misner kink mechanism.

## Fork-A chirality finding (session add — gyrator vs circulator; magnitude imposed-echo)

The substrate's $I4_1 32$ chirality enters the magnetic/microrotational sector as a **non-reciprocal inter-tank coupling**. Per the Fork-A node-coupling result (PR #321 merged; canonical at [`device-circuit-models.md`](../ch3-pin-port-configuration/device-circuit-models.md):159-165,201-217 and `research/2026-06-20_node-circulator-coupling.md`), a **conservative skew-Hermitian circulator coupling EXISTS** between the bulk (mass/A1) and shear (charge/Cosserat) sublattice tanks — it is bounded/lossless (norm conserved to $1.1\times10^{-12}$/40k steps, does NOT pump), transfers helicity (100% bulk$\to$shear, vs the failed graft-v3 $\sim$2%), and acts on the poloidal winding (ON $\ne$ OFF). The verdict is **PARTIAL**:

- The **2-port skew is RECIPROCAL** — forward(bulk$\to$shear) $==$ reverse, RH $==$ LH; it *is* the lossless reciprocal **optical-activity GYRATOR** (the reciprocal-Faraday polarization-plane rotator, `def-0pt1ac`), **NOT** a one-way router.
- **Genuine chiral non-reciprocity needs the 3-PORT loop** (EM$\leftrightarrow$shear$\leftrightarrow$bulk, the EM/photon port as the 3rd leg) — the **CIRCULATOR**, whose gauge-invariant loop phase $3\chi\theta_\chi$ flips with the handedness $\chi$, but the asymmetry is small ($1.75\times10^{-3}$).
- The **non-reciprocity MAGNITUDE is IMPOSED** ($\theta_\chi = 2\pi\nu_{vac}$, $\tilde\kappa = 6/5$ plugged, $\alpha$-free) because the cubic-FDTD chiral-crystal engine averages chirality out (`cvr_model.py`:243). So the row reads **ECHO at the non-reciprocity magnitude** — the same FORM-deriving / VALUE-importing verdict ([`form-deriving-value-importing.md`](../../common/form-deriving-value-importing.md)) as the rest of the node: the coupling FORM is forced (trivially, by losslessness), its magnitude is imported.

**Discipline: do NOT call the reciprocal 2-port a "circulator."** Reserve **circulator** = non-reciprocal inter-tank coupling (needs the 3-port); **gyrator** = the reciprocal optical-activity rotator. The chiral coupling that HOPF-01/02 reads is consistency-class, magnitude-imposed.

## Primary canonical sources

- [`common/trampoline-framework.md`](../../common/trampoline-framework.md) line 188 — Cosserat rotation-sector mass-gap $m_\omega^2 = 4 G_c / I_\omega$; ferrite-Curie analog; Verlet-validated at E-046.
- [`vol2/particle-physics/ch05-electroweak-mechanics/gauge-boson-masses.md`](../../vol2/particle-physics/ch05-electroweak-mechanics/gauge-boson-masses.md) line 39 — Cosserat characteristic length $l_c = \sqrt{\gamma_c / G_{vac}}$ identified with weak-force range $r_W$; $W^\pm / Z^0$ as evanescent cutoff modes (`clm-5zuo7g`, `clm-q8un7j`).
- [`vol2/particle-physics/ch01-topological-matter/finkelstein-misner-spin-half-derivation.md`](../../vol2/particle-physics/ch01-topological-matter/finkelstein-misner-spin-half-derivation.md) — SU(2) / SO(3) double-cover spin-½ from Cosserat micro-rotation on extended closed defect (`clm-salw2h`).
- [`common/translation-tables/translation-circuit.md`](../../common/translation-tables/translation-circuit.md) §4, `clm-eemap1` — EE-as-substrate-native META framework; magnetic / microrotational primitive → EE inductance / transformer / ferrite-Curie projection.
- [`vol9/ch3-pin-port-configuration/device-circuit-models.md`](../ch3-pin-port-configuration/device-circuit-models.md):159-165,201-217 (`def-ch1crc`, `def-0pt1ac`) — the chiral circulator (non-reciprocal inter-tank, 3-port) vs the optical-activity gyrator (reciprocal 2-port); Fork-A PARTIAL verdict, non-reciprocity magnitude imposed-echo.
- CLAUDE.md INVARIANT-S2 Axiom 1 verbatim — canonical statement: the substrate is the 3D chiral Laves K4 Cosserat crystal; 6 DOFs / node with 3 microrotational → B; Cosserat rotational DOF IS substrate-native origin of intrinsic spin.

## Cross-references

- **Ch.9 Mechanical Characteristics** ([`../ch9-mechanical-characteristics/index.md`](../ch9-mechanical-characteristics/index.md)) — Cosserat couple-stress $\gamma_c$ as bulk mechanical primitive; mechanical-side derivation of $l_c = \sqrt{\gamma_c / G_{vac}}$.
- **Ch.11 Topological Characteristics** ([`../ch11-topological-characteristics/index.md`](../ch11-topological-characteristics/index.md)) — SU(2) / SO(3) double cover via Finkelstein–Misner kink; $(2, 3)$ Clifford-torus electron winding; chirality implications of $I4_1 32$ right-handed substrate.
- **Ch.6 Temperature Characteristics** — Cosserat-Curie thermal-freeze of B-modes at $T_{CMB}$; $\delta_{strain}$ mechanism; Cosserat-rotation-sector mass-gap thermal-mode-population ASYM class (Q-DELTA-MAP-1 closed 2026-05-28).
- **Ch.2 Absolute Maximum Ratings** — $B_{snap}$ as substrate-rupture threshold via B-sector (`clm-82dxbj`).
- **Ch.4 DC Electrical Characteristics** — $\mu_0$ as substrate-native bond microrotation density.

## Manuscript counterpart

[`manuscript/vol_9_vacuum_datasheet/chapters/10_magnetic_microrotational_characteristics.tex`](../../../vol_9_vacuum_datasheet/chapters/10_magnetic_microrotational_characteristics.tex)

---
