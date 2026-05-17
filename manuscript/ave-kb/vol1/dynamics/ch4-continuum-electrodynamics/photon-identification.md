[↑ Ch.4 Continuum Electrodynamics](index.md)
<!-- leaf: verbatim -->
<!-- path-stable: referenced from vol1 ch3-quantum-signal-dynamics + vol2 ch01 + vol3 ch02 as canonical photon identification -->

# Photon = T₂-Only Cosserat Microrotation; Electron = Photon + TIR Confinement

The AVE-native canonical identification of the photon: under the K4 tetrahedral group $T_d$, the 4-port amplitude space decomposes as $A_1 \oplus T_2$. The $A_1$ scalar/longitudinal sector dissipates monotonically (Gauss's law: $\nabla \cdot \mathbf{E} = 0$ in vacuum forbids longitudinal EM); the $T_2$ transverse triplet survives as the photon. **The photon is the K4-TLM's stable T₂-only bound state** — a knotted transverse Cosserat shear wave with $u = 0$ and $\omega \neq 0$. The electron is **this object plus Axiom 4 saturation confinement**: when the photon's amplitude crosses $V_{\text{yield}} = \sqrt{\alpha} \cdot V_{\text{snap}}$, the lattice self-creates a $\Gamma = -1$ TIR cavity that traps the photon into a standing wave. **The electron is a self-trapped photon.**

## Key Results

| Result | Statement |
|---|---|
| K4 4-port irrep decomposition | $V_{\text{4-port}} = A_1 \text{ (1D, scalar/longitudinal)} \oplus T_2 \text{ (3D, transverse/microrotational)}$ |
| Scattering matrix eigenvalues | $S = (1/2) \mathbf{1} - I$ has eigenvalues $\{+1, -1, -1, -1\}$ — $+1$ on $A_1$, $-1$ triplet on $T_2$ |
| Empirical port-correlation (steps 100/200/300) | $\{1.65, 1.22, 1.13, 0.00\}$ — $A_1$ exactly dissipated, $T_2$ survives 3-mode split |
| Photon = T₂-only canonical | $u = 0$ (no Cosserat translation), $\omega \neq 0$ (pure microrotation), no saturation ($\Delta\phi \ll \alpha$), linear $Z = Z_0$ |
| Electron = photon + TIR confinement | At $V \to V_{\text{yield}} = \sqrt{\alpha} V_{\text{snap}}$: $C_{\text{eff}} \to \infty$, $Z \to 0$, $\Gamma \to -1$ → self-trapped standing wave |
| Compton frequency as dynamical threshold | $\omega = \omega_C = c / \ell_{\text{node}}$ is genuine threshold for photon → electron transition (resonance + saturation) |
| Three regimes | $\omega < \omega_C$ (transparent) / $\omega = \omega_C$ (bound → electron) / $\omega > \omega_C$ (Compton scattering) |

## §1 — The $A_1 \oplus T_2$ decomposition of K4 port space

### Group-theoretic foundation

The K4 scattering matrix (`src/ave/core/k4_tlm.py:36-65`):

$$S_{ij} = (1/2) - \delta_{ij} \text{ for } z_{\text{local}} = 1$$

$S = (1/2) \mathbf{1} - I$ where $\mathbf{1}$ is the all-ones matrix and $I$ is the 4×4 identity, acting on the 4-vector of port amplitudes.

Under $T_d$ (the symmetry of the four tetrahedral neighbors on K4), the 4-port amplitude space decomposes as:

$$V_{\text{4-port}} = A_1 \text{ (1D)} \oplus T_2 \text{ (3D)}$$

- **$A_1$** — totally symmetric rep. Basis vector $(1, 1, 1, 1) / 2$. Physically: isotropic, scalar, longitudinal.
- **$T_2$** — 3D triplet. Basis spans the traceless 3D subspace $\{v : \sum_i v_i = 0\}$. Physically: anisotropic, vector-like, transverse.

### Scattering eigenvalues

- On $A_1$ basis $(1, 1, 1, 1)/2$: $S \cdot v = ((1/2) \cdot 4 - 1) \cdot v = (2 - 1) \cdot v = +1 \cdot v$. **$A_1$ eigenvalue: $+1$.**
- On any traceless vector ($A_1$-orthogonal): $\mathbf{1} \cdot v = 0$, so $S \cdot v = (-I) \cdot v = -v$. **$T_2$ eigenvalue: $-1$** (triply degenerate).

The bare scattering is unitary — $A_1$ would propagate forever, $T_2$ would reflect forever, no energy loss.

### How dissipation breaks the symmetry

The bond-level Op3 reflection adds an impedance mismatch at each bond: $Z_{\text{eff}} = Z_0 / \sqrt{S_{\text{sat}}}$ where $S_{\text{sat}}$ is the Axiom-4 saturation factor.

This impedance mismatch dissipates energy **asymmetrically** for the two sectors:

- $A_1$ has no spatial gradient in port space; its reflection at bonds produces destructive interference with neighboring nodes' $A_1$ components. **$A_1$ loses energy monotonically until it reaches zero.**
- $T_2$ modes carry spatial structure; their reflection redirects flux into standing-wave patterns. **$T_2$ dissipates more slowly, settling into a quasi-stable configuration.**

This asymmetric dissipation is **physically correct** for EM waves on a Maxwell-substrate: longitudinal components ($\nabla \cdot \mathbf{E} \neq 0$) are forbidden in vacuum by Gauss's law, so any $A_1$-type longitudinal excitation must dissipate. The K4 scattering realizes this constraint automatically through $T_d$ symmetry.

## §2 — Empirical observation: $A_1$ exactly dissipated

`src/scripts/vol_1_foundations/phasor_discovery.py` at $N = 64$, $n_{\text{steps}} = 300$, seeded $(2, 3)$ Golden-Torus voltage ansatz at $(R, r) = (16.0, 6.108)$, amplitude $0.5$. Snapshot port-correlation eigenvalues at steps 100/200/300:

| Step | $\lambda_1$ | $\lambda_2$ | $\lambda_3$ | $\lambda_4$ |
|---|---|---|---|---|
| 100 | 1.654 | 1.215 | 1.130 | **0.001** |
| 200 | 1.642 | 1.210 | 1.147 | **0.000** |
| 300 | 1.653 | 1.203 | 1.144 | **0.000** |

Sum of eigenvalues $= 4.0$ at each step (trace of 4×4 correlation matrix = 4; sanity check passes). **The smallest eigenvalue is exactly zero, stable across time.** The port-space of the soliton lives in a 3D subspace of the nominal 4D port space — exactly the $T_2$ subspace.

## §3 — Photon definition (three tightly-coupled properties)

From Vol 3 Ch 2:139:
> *"A photon is a purely transverse Cosserat shear wave; it carries no rest mass and has no longitudinal (scalar) component. It is therefore mechanically blind to the isotropic bulk and couples instead to the transverse cross-sectional strain of the lattice."*

From Vol 4 Ch 1:491-495:
> *"When massless Bosons (photons) propagate, they act as linear transverse shear waves. Because they do not possess a static inductive core, they do not geometrically saturate the dielectric lattice ($\Delta\phi \ll \alpha$). The local metric impedance remains perfectly matched at $Z_0 \approx 376.7$ Ω."*

The photon in AVE is defined by **four tightly-coupled properties** (equivalent statements; any one implies the others):

1. **Purely transverse** — no longitudinal/scalar component (forbidden by Gauss's law in vacuum; realized automatically by K4 $A_1 \oplus T_2$ symmetry, $A_1$ dissipates to zero).
2. **Microrotation sector only** — excites $\omega$ (Cosserat microrotation) with $u = 0$ (Cosserat translation). The photon lives entirely in the rotational sector of the K4 lattice's 6 DOFs per node.
3. **Sub-saturation** — $\Delta\phi \ll \alpha$, lattice stays in linear regime, no Axiom 4 kernel engagement.
4. **Impedance-matched at $Z_0$** — local lattice impedance $Z_{\text{local}} = Z_0 \approx 376.7$ Ω perfectly matched everywhere; reflection coefficient $\Gamma = 0$ at every bond; no scattering or reflection. *This is the wave-engineer's restatement of property 3: linear regime $\Leftrightarrow$ no impedance modulation $\Leftrightarrow$ perfect impedance match.* The Vol 4 Ch 1:491-495 quote above states exactly this.

The $A_1 \oplus T_2$ decomposition aligns directly:

| K4 port-space rep | Physical character | Cosserat sector |
|---|---|---|
| $A_1$ (1D) | Isotropic, longitudinal | Translational $u$ |
| $T_2$ (3D) | Anisotropic, transverse | Microrotational $\omega$ |

With $A_1$ fully dissipated ($\lambda_4 = 0$ exactly) and $T_2$ surviving ($\lambda_{1\ldots3} = 1.65, 1.22, 1.13$), the simulation's steady-state soliton has:
- Zero longitudinal/scalar amplitude → property 1 (purely transverse) ✓
- Pure microrotation-sector content → property 2 ($u = 0$, $\omega \neq 0$) ✓
- Amplitude $0.5 < V_{\text{yield}}$ → property 3 (no saturation) ✓

**All three AVE-photon properties are satisfied. The TLM's stable bound state under the $(2, 3)$ ansatz is the photon.**

> **Doc 107 correction.** Doc 105's dual-sector helical-photon framing ($u \neq 0$ AND $\omega \neq 0$) is empirically wrong per the engine result. The canonical photon is **single-sector** ($T_2$ only, microrotation $\omega$, no translation $u$). The engine's empirically observed "$u$ driven by $\omega$" coupling is a sub-saturation Op14 effect, not photon-physical content.

## §4 — Electron = photon + TIR confinement (mechanism)

### §4.0 — Symmetric framing: photon and electron are two amplitude phases of the same underlying object

The K4-TLM substrate carries transverse Cosserat-microrotation wave excitations (T₂ sector). Whether such an excitation is observed as **a photon** or **an electron** depends only on its amplitude relative to $V_{\text{yield}} = \sqrt{\alpha} \cdot V_{\text{snap}} \approx 43.65$ kV:

- **$\Delta\phi \ll \alpha$ $\Rightarrow$ photon:** sub-yield amplitude, lattice stays linear, $Z_{\text{local}} = Z_0$ impedance-matched, $\Gamma = 0$ at every bond, free propagation as a transverse Cosserat-microrotation wave.
- **$\Delta\phi \to \alpha$ $\Rightarrow$ electron:** at-yield amplitude triggers Axiom 4 self-saturation, $C_{\text{eff}} \to \infty$, $Z_{\text{local}} \to 0$, $\Gamma \to -1$ TIR cavity self-creates, the transverse wave is trapped into a standing wave inside the self-created mirror.

**The boundary is a dynamical threshold** (analogous to a varactor's breakdown voltage or a Josephson junction's critical current), not a fundamental ontological difference between two different kinds of particle. Photon emission (the electron → photon transition) is the reverse process: amplitude drops, lattice de-saturates, $\Gamma$ moves off $-1$, the trapped standing wave escapes as a free photon at frequency $\omega_C$.

This framing is what makes "the electron is a self-trapped photon" (line 7) precise: same K4 transverse-Cosserat-microrotation wave, parameterized only by whether self-saturation has engaged.

### §4.1 — The trapping mechanism step-by-step

The electron differs from the photon by **one additional piece of physics**: Axiom 4 saturation engages. The mechanism, step-by-step:

| Step | What happens |
|---|---|
| **A** | Take a transverse $T_2$ configuration (a photon) with frequency $\omega = \omega_C = c / \ell_{\text{node}}$ |
| **B** | This photon drives each single-bond LC tank it crosses at resonance — the single-bond LC resonates at exactly $\omega_C$ |
| **C** | At resonance, voltage builds up in the capacitor sector each cycle. The tank accumulates reactive energy without being able to shed it (off-resonance paths are closed) |
| **D** | When $V \to V_{\text{yield}} = \sqrt{\alpha} \cdot V_{\text{snap}} \approx 43.65$ kV, Axiom 4 engages: $C_{\text{eff}} = C_0 / \sqrt{1 - (V/V_{\text{yield}})^2} \to \infty$ |
| **E** | Local impedance $Z = \sqrt{\mu_0 / C_{\text{eff}}} \to 0$. Reflection coefficient $\Gamma = (Z_{\text{local}} - Z_0) / (Z_{\text{local}} + Z_0) \to -1$. **The lattice has created its own perfect TIR mirror at the photon's location.** |
| **F** | The photon's transverse wave is now trapped — the $\Gamma = -1$ boundary reflects it back inward on every attempt to propagate outward. The photon becomes a standing wave in a self-created cavity. **That standing wave is the electron.** |

All electron observables are projections of this bound configuration:

- **Rest mass** $m_e c^2 = \hbar \omega_C$ — resonant energy held in the trapped standing wave
- **Charge $e$** — topological winding number of the confined $(2, 3)$ configuration (Axiom 2: $[Q] \equiv [L]$)
- **Spin-½** — the $4\pi$ double-cover of the extended-unknot Finkelstein–Misner kink at the confinement boundary
- **$\alpha = 1/137$** — the TIR-boundary leakage rate per cycle ([Theorem 3.1 Q-factor](../../../vol4/circuit-theory/ch1-vacuum-circuit-analysis/theorem-3-1-q-factor.md))
- **Magnetic moment, $g$-factor, etc.** — composites of the above

## §5 — Photon emission, pair production, Compton scattering (consequences)

### §5.1 Photon emission as reverse process

An electron emits a photon when the TIR condition transiently fails. Local amplitude drops below $V_{\text{yield}}$, Axiom 4 comes off saturation, $C_{\text{eff}}$ becomes finite, $Z_{\text{local}}$ returns toward $Z_0$, $\Gamma$ moves off $-1$. The trapped transverse wave propagates out as a photon at frequency $\omega_C$ (or shifted if the electron is in an excited state or recoils).

**Electron and photon are two phases of the same substrate dynamics**: bound (saturated) and free (unsaturated). The boundary is $V = V_{\text{yield}}$ at $\omega = \omega_C$.

### §5.2 Pair production

A single gamma photon at frequency $2\omega_C$ (energy $2 m_e c^2$) can trigger saturation at two distinct lattice regions simultaneously, creating two TIR bubbles. The photon's transverse field pattern splits across the two bubbles with opposite chirality, producing an electron/positron pair. **Threshold $E > 2 m_e c^2 = 1.022$ MeV** is the minimum energy to saturate the lattice at two points.

Two-photon processes at $\omega < \omega_C$ can also produce pairs if their intermodulation frequency (Vol 4 Ch 1 §"Condensate IMD Spectroscopy") hits $\omega_C$. The IMD sideband serves as the effective saturation-driver frequency.

### §5.3 Compton scattering

A photon at $\omega > \omega_C$ is above the lattice resonance. Off-resonance, the lattice barely responds (inductive-reactance dominates). But if the photon locally deposits enough energy to briefly push an adjacent region past saturation, it excites a transient electron that absorbs some energy, and the photon emerges with shifted frequency. **Compton scattering = transient saturation event.**

## §6 — Compton frequency as dynamical threshold

$\omega_C = c / \ell_{\text{node}}$ is the natural frequency of the lattice at single-bond scale — not a calibration but a derived consequence of lattice geometry and vacuum impedance $Z_0 = \sqrt{\mu_0 / \varepsilon_0}$.

The voltage threshold $V_{\text{yield}} = \sqrt{\alpha} \cdot V_{\text{snap}}$ is also set by geometry: $V_{\text{snap}} = m_e c^2 / e$ is the voltage quantum corresponding to one rest-mass energy per elementary charge, and $\alpha$ is the dimensionless saturation fraction (Vol 1 Ch 1 Axiom 4, Vol 1 Ch 8 α derivation).

The electron's rest energy:

$$m_e c^2 = \hbar \omega_C = \hbar c / \ell_{\text{node}}$$

This is the energy of a photon at the lattice self-saturation frequency.

### Three regimes

| Regime | Photon frequency | LC tank response | Saturation | Physical state |
|---|---|---|---|---|
| Low | $\omega < \omega_C$ | Off-resonance | No | Photon passes transparently |
| **Resonance** | $\omega = \omega_C$ | Full resonance | **Yes** | **Photon → bound → electron** |
| High | $\omega > \omega_C$ | Off-resonance | Transient only | Compton-like scattering |

The electron's Compton frequency is a **genuine dynamical threshold** for the photon-to-electron transition. Analogous to a Josephson junction's critical current or a varactor's breakdown voltage — a specific parameter value at which the system's behavior qualitatively changes.

## Cross-references

- **Canonical manuscript:**
  - Vol 3 Ch 2:139 — photon as purely transverse Cosserat shear wave
  - Vol 4 Ch 1:491-495 — photon as linear transverse shear wave; $\Delta\phi \ll \alpha$
  - Vol 1 Ch 4 (continuum electrodynamics) — Master Equation context
- **KB cross-cutting:**
  - [Theorem 3.1 Q-factor](../../../vol4/circuit-theory/ch1-vacuum-circuit-analysis/theorem-3-1-q-factor.md) — $\alpha^{-1}$ as TIR-boundary leakage rate per cycle
  - [Photon Propagation Baseline](photon-propagation-baseline.md) — empirical $v_{\text{meas}}/c = \sqrt{2}$ cardinal-axis kinematics
  - [L3 Electron-Soliton Closure Synthesis](../../../vol2/particle-physics/ch01-topological-matter/l3-electron-soliton-synthesis.md) — rest-energy Virial sum at bond-pair LC tank
  - [Boundary Observables $\mathcal{M}, \mathcal{Q}, \mathcal{J}$](../../../common/boundary-observables-m-q-j.md) — substrate observability rule at TIR boundary
- **Canonical scripts:**
  - `src/scripts/vol_1_foundations/phasor_discovery.py` — empirical $A_1 \oplus T_2$ split observation
  - `src/scripts/vol_1_foundations/photon_propagation.py` — Phase A K4-TLM wave-packet launcher
