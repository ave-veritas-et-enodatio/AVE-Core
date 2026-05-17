[↑ Ch.1 — Topological Matter](index.md)
<!-- leaf: verbatim -->
<!-- path-stable: referenced from vol1 ch4 photon-identification + vol2 ch04 quantum-spin + vol3 ch15 bh-orbitals + vol4 simulation ch14 as canonical electron identification -->

# Electron — Canonical Identification + First-Principles Axiom Audit

The AVE-native canonical identification of the electron, structured to parallel [`../../../vol1/dynamics/ch4-continuum-electrodynamics/photon-identification.md`](../../../vol1/dynamics/ch4-continuum-electrodynamics/photon-identification.md). The electron is **a self-trapped photon** (per photon-identification.md §4) — same K4 transverse-Cosserat-microrotation wave at amplitude above $V_{yield} = \sqrt{\alpha} \cdot V_{snap} \approx 43.65$ kV, where Axiom 4 saturation engages and self-creates a $\Gamma = -1$ TIR cavity. **The electron is not a separate particle from the photon; it is the same K4-substrate wave above the saturation threshold.**

This leaf carries three things:
1. **Canonical 4-property definition** (§1)
2. **First-principles axiom audit per property** (§2) — flags which properties are axiom-derived vs calibration-circular vs structurally-pending
3. **Cross-corpus framing translation guide** (§3) with 8 corpus framings + reconciliation matrix back to §1 properties

## §1 — Canonical 4-property definition

The electron in AVE is defined by **four tightly-coupled topological/dynamical properties** (equivalent statements; any one plus the others' implicit conditions implies the rest):

1. **Real-space topology: $0_1$ unknot** — the simplest closed flux-tube loop at minimum ropelength $2\pi$ on the K4 lattice. Tube circumference $\ell_{node}$, tube radius $\ell_{node}/(2\pi)$, loop length $2\pi \cdot \ell_{node}$.
2. **Phase-space winding: $(2,3)$ Clifford-torus** — in the bond-pair LC tank's $(V_{inc}, V_{ref})$ phasor space, the electron's winding pattern is the $(2,3)$ Clifford-torus configuration on the standard $\mathbb{T}^2 \subset S^3 \subset \mathbb{C}^2$ at the Golden Torus $R = \varphi/2$, $r = (\varphi-1)/2$, $d = 1$ (per [`../../../vol1/ch8-alpha-golden-torus.md`](../../../vol1/ch8-alpha-golden-torus.md)). **The $(2,3)$ "trefoil" is the phase-space winding pattern, NOT a real-space trefoil knot.**
3. **Self-saturated TIR cavity ($\Gamma = -1$ at $V_{yield}$)** — when the underlying transverse Cosserat-microrotation wave's amplitude crosses $V_{yield} = \sqrt{\alpha} \cdot V_{snap} \approx 43.65$ kV, Axiom 4 engages: $C_{eff} \to \infty$, $Z_{local} \to 0$, $\Gamma \to -1$. The lattice self-creates a perfect TIR mirror at the wave's location, trapping it as a standing wave inside the self-created cavity.
4. **T₂-only Cosserat-microrotation core** — the trapped wave is the same canonical photon (T₂ irrep, $u = 0$, $\omega \neq 0$) defined in [`../../../vol1/dynamics/ch4-continuum-electrodynamics/photon-identification.md`](../../../vol1/dynamics/ch4-continuum-electrodynamics/photon-identification.md) §3. Above saturation the core dynamics are unchanged; only the boundary condition flips from impedance-matched ($\Gamma = 0$) to TIR ($\Gamma = -1$).

> **Symmetric framing with the photon (corollary of property 3+4):** photon and electron are TWO amplitude phases of the same underlying K4 transverse-Cosserat-microrotation wave. Below $V_{yield}$ → photon (impedance-matched, free); above $V_{yield}$ → electron (self-trapped, standing wave). The boundary is a dynamical threshold, not an ontological one. Per the photon-identification §4.0 symmetric framing block.

## §2 — First-principles axiom audit per property

The audit applies the four-axiom test (per `manuscript/ave-kb/CLAUDE.md` INVARIANT-S2) to each property: **which axiom(s) derive it, and is the derivation rigorous from first principles or does it embed circularity/calibration/hand-waving?**

### Topological/dynamical properties (the 4 from §1)

| Property | Axiom support | Derivation status | Open items |
|---|---|---|---|
| 1. $0_1$ unknot real-space topology | Ax1 (K4 lattice supports flux-tube topology, smallest stable defect) + Ax2 (TKI: $[Q] \equiv [L]$, closed loop conservation) | ✅ axiom-derived | None — unknot uniqueness follows from K4 + ropelength minimality + Ax2 closure |
| 2. $(2,3)$ Clifford-torus phase-space winding | Ax3 (Min Reflection picks Golden Torus geometry via S₁₁ minimization) + Ax1 (Clifford torus on $S^3$ is K4-induced phase space) + Ax2 (spin-½ half-cover) | ✅ axiom-derived **with one pending uniqueness item** | Ropelength-minimality uniqueness of canonical Clifford-torus embedding $r_1 = r_2 = 1/\sqrt{2}$ on K4 (foreword line 37; Phase-1 classical-topology question; does not affect numerical predictions) |
| 3. Self-saturated TIR cavity ($\Gamma = -1$ at $V_{yield}$) | Ax4 (saturation kernel $S(A) = \sqrt{1-A^2}$; $A \to 1 \Rightarrow S \to 0 \Rightarrow C_{eff} \to \infty \Rightarrow Z \to 0 \Rightarrow \Gamma \to -1$) | ✅ axiom-derived | None |
| 4. T₂-only Cosserat-microrotation core | Ax1 ($T_d$ symmetry forces $A_1 \oplus T_2$ decomposition; Gauss's law forbids $A_1$ longitudinal → $T_2$ survives) | ✅ axiom-derived (inherited from photon-identification §3) | None |

### Observable properties (mass, charge, spin, g-factor, gravitational coupling, etc.)

These are the quantities a laboratory measures on an electron. Each must be either derived from axioms OR honestly scoped as a calibration anchor.

| Observable | Axiom support | Derivation status | Notes |
|---|---|---|---|
| **Rest mass $m_e c^2 \approx 511$ keV** | — | ⚠ **CALIBRATION ANCHOR, not derivation** | $m_e$ is the SI calibration of "smallest stable soliton mass." $\ell_{node} = \hbar/(m_e c)$ is then derived from this calibration (foreword line 34). The identity $m_e c^2 = \hbar\omega_C = \hbar c / \ell_{node}$ is the AVE-native ↔ SI conversion of this calibration anchor, NOT an independent prediction of $m_e$ from first principles. The framework is honest about this. |
| **Charge $e$** | Ax2 TKI ($[Q] \equiv [L]$; topological winding number of $0_1$ unknot through K4 bond-port) | ✅ axiom-derived | $e$ is the topological invariant of the closed flux loop. |
| **Spin-½** | Ax1 (K4 rotation group $T = A_4 \to 2T \subset SU(2)$ double cover) + Finkelstein-Misner / Dirac belt-trick on extended unknot defect embedded in SO(3) manifold | ✅ axiom-derived | The $\pi^2$ Clifford-torus half-cover used in α derivation is the automatic group-theoretic consequence of $SU(2) \to SO(3)$ 2-to-1 cover, not an imported QM postulate (per foreword line 37). |
| **$g = 2$ (gyromagnetic ratio)** | SO(3) $\omega$-field period $2\pi$ vs spinor observable period $4\pi$ ratio | ✅ axiom-derived | Group-theoretic; ratio falls out of the double-cover structure. |
| **$g - 2$ Petermann coefficient at 50 ppm** | Vol 2 Ch 6 [`q-g19a-petermann-saliency-closure.md`](../ch06-electroweak-higgs/q-g19a-petermann-saliency-closure.md) Route-B derivation: $\delta = -\alpha \cdot n_q / 2$ from α-suppression + LC equipartition 1/2 + $n_q$-locking | ⚠ **PARTIAL closure** | Linear-in-$n_q$ additivity assumption awaits K4-Cosserat Lagrangian numerical confirmation (Q-G47 Sessions 19+ per foreword line 106). Structural closure verified; rigorous closure pending. |
| **Compton wavelength $\ell_C = \hbar/(m_e c) = \ell_{node}$** | Direct identification with Ax1 calibration anchor | ⚠ **DEFINITIONAL, not derivation** | Same as rest mass — this IS the calibration anchor restated. Honest. |
| **Magnetic moment $\mu_B = e\hbar/(2m_e)$** | Derives from $e$ (Ax2) + spin-½ (Ax1) + $\hbar$ (Ax1 action quantum) + $m_e$ (calibration) | ✅ axiom-derived from above components | Combines axiom-derived parts (e, spin) with calibration ($m_e$). |
| **Long-range refractive-index tail (gravitational coupling)** | Ax4 saturation kernel + Op14 cross-sector trading propagates $S(r)$ outward as $1/r^2$ → refractive index $n(r) = 1 + 2GM/(rc^2)$ | ✅ axiom-derived | Per Vol 3 Ch 2 [`refractive-index-of-gravity.md`](../../../vol3/gravity/ch03-macroscopic-relativity/refractive-index-of-gravity.md). |
| **Stability (non-decay)** | Ax2 (TKI: topology = charge; charge conservation IS loop conservation) + Ax1 (K4 lattice topological protection) | ✅ axiom-derived | Per `common/grants-random-tangents.md` (on sibling branch `analysis/divergence-test-substrate-map`, not yet merged to L3) Entry #001 (f.3): two-reason trap (topological + impedance) explicit. |

### Honest scoping summary

- **8 of 8 topological/dynamical properties** derive from the four axioms; one open uniqueness sub-item (ropelength minimality of Clifford-torus embedding) noted in the corpus and does not affect numerical predictions.
- **6 of 8 observable properties** derive cleanly from axioms.
- **1 observable (rest mass $m_e$)** is honestly scoped as a calibration anchor, not a first-principles prediction. The framework chooses $m_e$ as the smallest-stable-soliton mass; $\ell_{node}$ follows. Saying "$m_e c^2 = \hbar c / \ell_{node}$" is a SI ↔ AVE-native unit conversion, not a derivation of $m_e$.
- **1 observable ($g - 2$ Petermann coefficient)** has structural closure with one pending rigorous-derivation item ($n_q$-additivity), tracked at C3-MUON-DELTA in the divergence-test-substrate-map (on sibling branch).

**Net assessment:** the electron is honestly axiom-derived, with explicit calibration-anchoring of $m_e$ and one pending closure on family-wide g-2 saliency. No hand-waving in the core 4-property definition.

## §3 — Cross-corpus framing translation guide

The corpus describes the electron from **eight distinct angles**, each correct, each emphasizing a different aspect of the same underlying object. This translation guide collects framings with verbatim quotes + file:line citations + maps back to canonical §1 properties.

| # | Framing | Emphasis | Canonical source | Verbatim quote |
|---|---|---|---|---|
| 1 | **Self-trapped photon** | Photon-electron unification; dynamical threshold at $V_{yield}$ | [`../../../vol1/dynamics/ch4-continuum-electrodynamics/photon-identification.md`](../../../vol1/dynamics/ch4-continuum-electrodynamics/photon-identification.md) line 7, §4, §4.0 | *"The electron is this object [the photon] plus Axiom 4 saturation confinement: when the photon's amplitude crosses $V_{yield} = \sqrt{\alpha} \cdot V_{snap}$, the lattice self-creates a $\Gamma = -1$ TIR cavity that traps the photon into a standing wave. The electron is a self-trapped photon."* |
| 2 | **$0_1$ unknot at minimum ropelength $2\pi$** | Knot topology + self-energy resolution | [`electron-unknot.md`](electron-unknot.md) | *"The electron ($e^-$) is identified as the fundamental ground-state topological defect: an Electromagnetic Unknot — a single closed flux tube loop at minimum ropelength = $2\pi$. The unknot has circumference $\ell_{node}$ and tube radius $\ell_{node}/(2\pi)$."* |
| 3 | **Real-space $0_1$ + phase-space $(2,3)$ Clifford-torus winding** | Real-space vs phase-space topology disambiguation | [`../../../vol4/simulation/ch14-leaky-cavity-particle-decay/theory.md` line 12](../../../vol4/simulation/ch14-leaky-cavity-particle-decay/theory.md); [`../ch04-quantum-spin/spin-as-precession.md` line 6](../ch04-quantum-spin/spin-as-precession.md); [`../ch04-quantum-spin/larmor-derivation.md` line 6](../ch04-quantum-spin/larmor-derivation.md); [`../../../vol1/ch8-alpha-golden-torus.md`](../../../vol1/ch8-alpha-golden-torus.md) | *"An electron is the $0_1$ unknot in real space carrying a $(2,3)$ Clifford-torus winding pattern in phase space... The trefoil lives in the bond-pair LC tank's $(V_{inc}, V_{ref})$ phasor trajectory, not in the real-space flux-tube topology."* |
| 4 | **Substrate-perspective: 6 observables** | What each lattice node locally experiences when an electron exists | [`substrate-perspective-electron.md`](substrate-perspective-electron.md) | *"Charge, mass, spin, magnetic moment, gravitational coupling, Compton wavelength are all EMERGENT readings of the substrate's joint state at the canonical electron configuration — not extra properties added on top."* (6 substrate observables: $A^2$ saturation, TIR wall, topological circulation, B-flux, Op14 refractive tail, K4-Cosserat coupling) |
| 5 | **Topological flywheel / gyroscope** | Spin as literal classical angular momentum $L = I\omega$ | [`../ch04-quantum-spin/larmor-derivation.md` line 8](../ch04-quantum-spin/larmor-derivation.md); [`../ch04-quantum-spin/spin-as-precession.md` line 6](../ch04-quantum-spin/spin-as-precession.md) | *"If the electron is a topological flywheel, its quantum spin ($S = \frac{1}{2}\hbar$) is not an intrinsic probability descriptor; it is literal, classical angular momentum ($\mathbf{L} = I\boldsymbol{\omega}$) born of the circulating metric network."* |
| 6 | **Beltrami standing wave** | $\mathbf{E}$ and $\mathbf{B}$ orthogonal, closed-loop feed; $\nabla \times \mathbf{A} = k\mathbf{A}$ | [`electron-unknot.md`](electron-unknot.md) | *"A Beltrami standing wave where the continuous $\mathbf{E}$ and $\mathbf{B}$ field lines are mutually orthogonal and feed into each other in a closed topological loop ($\nabla \times \mathbf{A} = k\mathbf{A}$), permanently trapping the energy."* |
| 7 | **LC tank cavity resonance at Compton frequency** | $\omega_C = c/\ell_{node}$ is single-bond LC eigenfrequency; resonance + saturation = electron | [`../../../vol4/circuit-theory/ch1-vacuum-circuit-analysis/theorem-3-1-q-factor.md`](../../../vol4/circuit-theory/ch1-vacuum-circuit-analysis/theorem-3-1-q-factor.md); Vol 4 Ch 1 | *"$\omega_C = c/\ell_{node}$ (Compton frequency = LC tank eigenfrequency)"* — combined with photon-identification §4 step C-F: at $\omega_C$ + $V \to V_{yield}$, the LC tank traps the photon into a standing wave |
| 8 | **Constructive topological trap (vs BH destructive)** | Topology preservation vs destruction; permanent non-radiating ground state | [`../../../vol3/cosmology/ch15-black-hole-orbitals/constructive-destructive-paradox.md` lines 8, 11](../../../vol3/cosmology/ch15-black-hole-orbitals/constructive-destructive-paradox.md) | *"Electron (Constructive): The topological unknot is a stable geometric structure. The confined photon maintains its $0_1$ knot invariant indefinitely. Topology is preserved. The electron is a permanent, non-radiating ground state."* |

### Reconciliation matrix — framing × canonical property

Every framing above maps cleanly to one or more of the four canonical properties from §1:

| Framing | Property 1 ($0_1$ unknot real-space) | Property 2 ($(2,3)$ phase-space) | Property 3 (TIR cavity at $V_{yield}$) | Property 4 (T₂-microrotation core) |
|---|---|---|---|---|
| 1. Self-trapped photon | implied (photon-trap topology = unknot) | implied (Golden Torus geometry implicit in trap) | **explicit** | **explicit** (photon = T₂) |
| 2. $0_1$ unknot ropelength | **explicit** | implicit | implied (ropelength minimum requires saturation trap) | implied (transverse only by Beltrami) |
| 3. Real-space + phase-space | **explicit** | **explicit** | implied | implicit |
| 4. Substrate-perspective | "topological circulation pattern" | implicit | "self-formed TIR wall" | "T₂-only Cosserat-microrotation core" |
| 5. Topological flywheel | implied (closed loop = flywheel) | implied ($\omega$-circulation in phase space) | implied | "circulating metric network" = T₂ microrotation |
| 6. Beltrami standing wave | "closed topological loop" | implicit | "permanently trapping the energy" | "$\mathbf{E}$ and $\mathbf{B}$ mutually orthogonal" = transverse |
| 7. LC tank resonance | implied (loop = single-bond tank) | implied (Golden Torus = resonant geometry) | "$V \to V_{yield}$ traps photon" | implicit |
| 8. Constructive topological trap | "topological unknot...stable geometric structure" | implicit | "confined photon...indefinitely" = TIR cavity | implicit |

**All 8 framings are equivalent statements of the same physical object** — the canonical 4 properties capture them all. Choice of framing depends on reader domain:
- Knot theorist → framing 2 (ropelength)
- Field theorist → framing 6 (Beltrami) or 1 (self-trapped photon)
- Circuit engineer → framing 7 (LC tank resonance)
- Group theorist → framing 4 (substrate-perspective) or 1 (photon→electron)
- Mechanical engineer → framing 5 (topological flywheel)
- Cosmologist → framing 8 (constructive vs destructive trap)

### Related-but-non-definitional uses

Locations that reference the electron in context where it appears as observable consequence rather than definition; logged here but NOT considered framings:

- [`../../../vol3/gravity/ch01-gravity-yield/leaky-cavity-decay.md` line 12](../../../vol3/gravity/ch01-gravity-yield/leaky-cavity-decay.md): *"The electron is an extended $0_1$ Unknot flux tube loop..."* — restates framing 2 in the Heavy Fermion Paradox-resolution context; cites Ax1 for tube-diameter bound at $\ell_{node}$.
- [`../../../vol3/condensed-matter/ch09-condensed-matter-superconductivity/bcs-alternative-framework.md` line 14](../../../vol3/condensed-matter/ch09-condensed-matter-superconductivity/bcs-alternative-framework.md): *"the electron is not a point particle; it is a $0_1$ topological flux loop (unknot) spinning at a high AC frequency"* — restates framing 2 + 5 in BCS-superconductivity context.
- [`../../../vol4/circuit-theory/ch1-vacuum-circuit-analysis/relativistic-inductor-newtonian-limit.md` line 18](../../../vol4/circuit-theory/ch1-vacuum-circuit-analysis/relativistic-inductor-newtonian-limit.md): *"The electron is a $0_1$ unknot soliton on the chiral Laves K4 Cosserat crystal substrate. At rest, the soliton's total energy decomposes 50/50 inductive/capacitive by virial equipartition"* — adds 50/50 virial energy split, a derived consequence not a defining property.
- [`../../quantum-orbitals/ch07-quantum-mechanics/geometry-pipeline.md` line 61](../../quantum-orbitals/ch07-quantum-mechanics/geometry-pipeline.md): *"Each electron is a node on the LC lattice"* — atomic-orbital context simplification; electron-as-node abstraction for KCL solver, NOT a fundamental definition.

### 🚩 Flagged corpus citation issue

[`../../appendices/app-f-solver-toolchain/sm-translation-toolchain.md` line 22](../../appendices/app-f-solver-toolchain/sm-translation-toolchain.md):
> *"The electron is an impedance mismatch ($\Gamma=-1$) that traps a **longitudinal** wave, bouncing at $E=V(r)$."*

**This contradicts the canonical photon = purely transverse framing** (photon-identification.md §3 properties 1 + 4; Vol 3 Ch 2:139). The electron traps a transverse wave (the T₂ Cosserat-microrotation photon), not a longitudinal one. Either:
- (a) "Longitudinal" here is used loosely to mean "1D wave along a path in the atomic-orbital cavity" (the cavity is approximated as a 1D acoustic resonator for orbital-solver purposes), not "longitudinal EM polarization." If so the wording is misleading but not physically wrong — just needs disambiguation.
- (b) An actual physics inconsistency that should be flagged for correction.

**Resolution required: Grant adjudication.** Until resolved, sm-translation-toolchain.md:22 should NOT be cited as a canonical electron definition.

## §4 — Maintenance discipline

If a **9th definitional framing** surfaces in the corpus, add to the §3 table above + reconcile to one or more of the canonical 4 properties in §1. Do NOT let the corpus drift toward a 9th independent definition; force every new use of "electron is..." to map to one of the 4 properties to maintain definitional unity.

If a new **observable property** is discovered or sharpened (e.g., further g-2 precision, anomalous magnetic moment refinements), add to the §2 audit table with explicit axiom traceability + circularity/calibration flagging.

**$m_e$ as calibration anchor must remain explicitly flagged.** If the framework EVER claims to derive $m_e$ from first principles (rather than calibrate it), the calibration-anchor flag must be revisited; that would be a major closure event analogous to the ν_vac=2/7 or α=1/(4π³+π²+π) derivations.

---

> → Primary: [`../../../vol1/dynamics/ch4-continuum-electrodynamics/photon-identification.md`](../../../vol1/dynamics/ch4-continuum-electrodynamics/photon-identification.md) — canonical photon definition; electron = photon + TIR confinement (symmetric framing in §4.0)
> → Primary: [`electron-unknot.md`](electron-unknot.md) — $0_1$ unknot ropelength derivation + self-energy paradox resolution; framing #2 source
> → Primary: [`substrate-perspective-electron.md`](substrate-perspective-electron.md) — substrate-observable view; framing #4 source
> → Primary: [`../../../vol1/ch8-alpha-golden-torus.md`](../../../vol1/ch8-alpha-golden-torus.md) — Golden Torus $(2,3)$ phase-space winding derivation; property 2 source
> ↗ See also: [`../ch04-quantum-spin/spin-as-precession.md`](../ch04-quantum-spin/spin-as-precession.md), [`../ch04-quantum-spin/larmor-derivation.md`](../ch04-quantum-spin/larmor-derivation.md) — topological flywheel framing (#5)
> ↗ See also: [`../../../vol3/cosmology/ch15-black-hole-orbitals/electron-bh-isomorphism.md`](../../../vol3/cosmology/ch15-black-hole-orbitals/electron-bh-isomorphism.md) — electron ↔ BH isomorphism (Γ=-1 confinement at every scale)
> ↗ See also: [`../ch06-electroweak-higgs/q-g19a-petermann-saliency-closure.md`](../ch06-electroweak-higgs/q-g19a-petermann-saliency-closure.md) — g-2 derivation (partial closure status per §2 audit)
> ↗ See also: `common/grants-random-tangents.md` (on sibling branch `analysis/divergence-test-substrate-map`, not yet merged to L3) Entry #001 (f.3) — the two-reason trap (topological + impedance) for why the electron can't untangle, with the boundary-observables-m-q-j.md:73 "interior causally disconnected" key insight
