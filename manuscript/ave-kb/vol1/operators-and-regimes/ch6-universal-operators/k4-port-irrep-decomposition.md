[↑ Ch.6 Universal Operators](index.md)
<!-- leaf: verbatim -->
<!-- path-stable: referenced from photon-identification + L3 closure synthesis as canonical K4 4-port irrep decomposition -->

# K4 4-Port Irrep Decomposition: $A_1 \oplus T_2$ + S-Matrix Eigenvalues

The K4 4-port amplitude space decomposes under the tetrahedral group $T_d$ as $V_{\text{4-port}} = A_1 \oplus T_2$. The K4-TLM scattering matrix $S = (1/2)\mathbf{1} - I$ has eigenvalues $\{+1, -1, -1, -1\}$: the $+1$ eigenvector is the $A_1$ "common mode" (all ports equal); the $-1$ triplet spans $T_2$ (traceless). **This is the canonical group-theoretic foundation** for: photon identification (T₂-only Cosserat $\omega$ microrotation), photon-electron formation mechanism (A₁ dissipates via Gauss's law forbidding longitudinal EM; T₂ survives), $A_1$ vs $T_2$ propagation-speed split ($c\sqrt{2}$ vs $c$), and Cosserat sector mapping (A₁ ↔ translational $u$; T₂ ↔ microrotational $\omega$).

## Key Results

| Result | Statement |
|---|---|
| K4 scattering matrix | $S_{ij} = (1/2) - \delta_{ij}$ for $z_{\text{local}} = 1$ |
| Matrix form | $S = (1/2) \mathbf{1} - I$ (all-ones matrix minus identity) |
| Irrep decomposition under $T_d$ | $V_{\text{4-port}} = A_1 \text{ (1D)} \oplus T_2 \text{ (3D)}$ |
| $A_1$ eigenvalue | $+1$ (basis $(1, 1, 1, 1)/2$ — scalar/longitudinal) |
| $T_2$ eigenvalue | $-1$, triply degenerate (basis spans traceless 3D subspace — vector-like/transverse) |
| Eigenvalue sum | $4 \cdot 1 = 4$ (trace of 4×4 correlation matrix) |
| $A_1$ Cosserat mapping | Translational $u$ (isotropic, longitudinal) — propagates at $c \sqrt{2}$ |
| $T_2$ Cosserat mapping | Microrotational $\omega$ (anisotropic, transverse) — propagates at $c$; **THIS IS THE PHOTON** |
| Bare scattering unitarity | Without Op3 dissipation, $A_1$ propagates forever, $T_2$ reflects forever, no energy loss |
| Op3 asymmetric dissipation | $A_1$ loses energy monotonically; $T_2$ settles into quasi-stable pattern |
| Physical origin of asymmetry | Gauss's law forbids longitudinal EM in vacuum: $\nabla \cdot \mathbf{E} = 0$ |

## §1 — Group-theoretic foundation

Under the tetrahedral point group $T_d$ (the symmetry of the four tetrahedral neighbors on K4), the 4-port amplitude space decomposes into irreducible representations as:

$$V_{\text{4-port}} = A_1 \text{ (1D)} \oplus T_2 \text{ (3D)}$$

### $A_1$ — totally symmetric rep (1D)

Basis vector: $(1, 1, 1, 1)/2$ — **all four ports carry equal amplitude.**

Physically: **isotropic, scalar, longitudinal.**

At a node, this is a scalar "breathing" excitation — the node as a whole compresses/expands without directional bias. **Maps to Cosserat translational sector $u$.**

### $T_2$ — 3D triplet rep

Basis spans the traceless 3D subspace $\{v : \sum_i v_i = 0\}$ — **for every excitation at one port, an equal and opposite excitation exists at some combination of other ports.**

Physically: **anisotropic, vector-like, transverse.**

The node as a whole has no net scalar displacement; instead it has a directional (vector-like) excitation. **Maps to Cosserat microrotational sector $\omega$.**

## §2 — Scattering matrix and eigenvalues

The K4 scattering matrix in AVE's TLM implementation (`src/ave/core/k4_tlm.py:36-65`):

$$S_{ij} = (1/2) - \delta_{ij} \text{ for } z_{\text{local}} = 1$$

i.e., $S = (1/2) \mathbf{1} - I$ where $\mathbf{1}$ is the all-ones matrix and $I$ is the 4×4 identity, acting on the 4-vector of port amplitudes.

### Computing $S$ on each irrep

**On $A_1$ basis $(1, 1, 1, 1)/2$:**

$$S \cdot v = ((1/2) \cdot 4 - 1) \cdot v = (2 - 1) \cdot v = +1 \cdot v$$

**$A_1$ eigenvalue: $+1$.**

**On any traceless vector ($A_1$-orthogonal):** $\mathbf{1} \cdot v = 0$, so:

$$S \cdot v = (-I) \cdot v = -v$$

**$T_2$ eigenvalue: $-1$** (triply degenerate).

### Physical interpretation

The $+1$ eigenvalue on $A_1$ means the bare scattering **preserves the $A_1$ mode exactly** (like a DC bias passing through a reflector unchanged). The $-1$ eigenvalue on $T_2$ means $T_2$ modes **flip sign on scatter** — the standard traveling-wave reflection behavior.

## §3 — Empirical eigenvalue measurement

`src/scripts/vol_1_foundations/phasor_discovery.py` at $N = 64$, $n_{\text{steps}} = 300$, seeded $(2, 3)$ Golden-Torus voltage ansatz at $(R, r) = (16.0, 6.108)$, amplitude $0.5$. Snapshot port-correlation eigenvalues at steps 100/200/300:

| Step | $\lambda_1$ | $\lambda_2$ | $\lambda_3$ | $\lambda_4$ |
|---|---|---|---|---|
| 100 | 1.654 | 1.215 | 1.130 | **0.001** |
| 200 | 1.642 | 1.210 | 1.147 | **0.000** |
| 300 | 1.653 | 1.203 | 1.144 | **0.000** |

Sum of eigenvalues $= 4.0$ at each step (trace of 4×4 correlation matrix = 4; sanity check passes). **The smallest eigenvalue is exactly zero, stable across time.** The port-space of the soliton lives in a 3D subspace of the nominal 4D port space — **exactly the $T_2$ subspace**, with $A_1$ fully dissipated.

## §4 — How Op3 dissipation breaks the symmetry

The bare K4-TLM with $S = (1/2)\mathbf{1} - I$ is unitary. $A_1$ would propagate forever, $T_2$ would reflect forever, no energy loss.

The bond-level **Op3 reflection** (`op3_bond_reflection=True`) adds an impedance mismatch at each bond: $Z_{\text{eff}} = Z_0 / \sqrt{S_{\text{sat}}}$ where $S_{\text{sat}}$ is the Axiom-4 saturation factor.

This impedance mismatch dissipates energy **asymmetrically** for the two sectors:

- **$A_1$** — common-mode "DC" across all ports — has **no spatial gradient in port space**. Its reflection at bonds produces **destructive interference** with neighboring nodes' $A_1$ components. **$A_1$ loses energy monotonically until it reaches zero.**
- **$T_2$** — carries spatial structure. Reflection at bonds **redirects flux into standing-wave patterns**. $T_2$ dissipates more slowly, settling into a **quasi-stable configuration**.

## §5 — Physical correctness: Gauss's law forbids longitudinal EM

This asymmetric dissipation is **physically correct** for electromagnetic waves on a Maxwell-substrate: **longitudinal components ($\nabla \cdot \mathbf{E} \neq 0$) are forbidden in vacuum by Gauss's law**, so any $A_1$-type longitudinal excitation must dissipate to leave only the transverse ($\nabla \cdot \mathbf{E} = 0$) sector.

**The K4 scattering realizes this constraint automatically through $T_d$ symmetry.** No additional physics needs to be imposed; the substrate's tetrahedral symmetry forces the right EM behavior.

## §6 — Propagation-speed split

The two irreps propagate at different speeds on the K4 substrate:

| Mode | Propagation speed | Substrate origin |
|---|---|---|
| $A_1$ (longitudinal) | $c \cdot \sqrt{2} = \sqrt{K_{\text{bulk}} / \rho}$ | Bulk modulus $K_{\text{bulk}}$ governs scalar compression |
| $T_2$ (transverse photon) | $c = \sqrt{G / \rho}$ | Shear modulus $G$ governs transverse shear |

The K4 magic-angle condition $K = 2G$ (Vol 1 Ch 2 macroscopic moduli) makes the substrate's $A_1$ and $T_2$ speeds related by $v_{A_1} / v_{T_2} = \sqrt{2}$ — the same $\sqrt{2}$ that shows up in cardinal-axis kinematics (see [photon-propagation-baseline](../../dynamics/ch4-continuum-electrodynamics/photon-propagation-baseline.md)).

## §7 — Cosserat sector mapping

The $A_1 \oplus T_2$ decomposition aligns directly with the Cosserat split:

| K4 port-space rep | Physical character | Cosserat sector | Mass content |
|---|---|---|---|
| $A_1$ (1D) | Isotropic, longitudinal | Translational $u$ | Massless (propagates at $c\sqrt{2}$) |
| $T_2$ (3D) | Anisotropic, transverse | Microrotational $\omega$ | **Massive** (mass-gap $m^2 = 4 G_c / I_\omega$, see [Cosserat Mass-Gap](../../axioms-and-lattice/ch1-fundamental-axioms/cosserat-mass-gap.md)) |

This mass split is **exactly what's needed**: the photon ($T_2$) needs to be massless when propagating freely (and it does — at sub-saturation amplitudes the $T_2$ mode is massless); the bound electron's Cosserat shell IS the massive mode that the same $T_2$ sector hosts at saturation.

## §8 — Implications

1. **Photon identification:** $T_2$-only is the canonical AVE-native photon ([photon-identification](../../dynamics/ch4-continuum-electrodynamics/photon-identification.md)). $A_1$ dissipating is the Gauss's-law constraint enforced automatically by $T_d$ symmetry — NOT an additional postulate.
2. **Electron formation:** the canonical electron emerges when a $T_2$ photon at $\omega = \omega_C$ self-saturates at the bond LC tank. The $T_2$ → bound-state transition is the saturation engagement at $V \to V_{\text{yield}}$.
3. **Universal kernel structure:** the same $T_d$ irrep machinery generalizes to other tetrahedrally-coordinated substrates (e.g., diamond lattices in solid-state physics). The K4-specific instance here is the AVE substrate's signature.
4. **No imported QM:** all of this comes from $T_d$ symmetry on the K4 lattice + Maxwell-substrate consistency. **No need to import "transverse vs longitudinal" as a separate postulate** — it emerges from substrate-native group theory.

## Cross-references

- **Canonical scripts:**
  - `src/ave/core/k4_tlm.py:36-65` — scattering matrix implementation
  - `src/scripts/vol_1_foundations/phasor_discovery.py` — empirical eigenvalue measurement
- **KB cross-cutting:**
  - [Photon Identification (T₂-only)](../../dynamics/ch4-continuum-electrodynamics/photon-identification.md) — canonical photon as $T_2$ Cosserat $\omega$ microrotation
  - [Photon Propagation Baseline](../../dynamics/ch4-continuum-electrodynamics/photon-propagation-baseline.md) — empirical $v = c\sqrt{2}$ cardinal-axis and $A_1$/$T_2$ speed split
  - [K4 Rotation Group $T = A_4$](../../axioms-and-lattice/ch1-fundamental-axioms/k4-rotation-group.md) — full rotation symmetry $T = A_4$ on the same port basis (orientation-preserving subgroup of $T_d$)
  - [Cosserat Mass-Gap](../../axioms-and-lattice/ch1-fundamental-axioms/cosserat-mass-gap.md) — $T_2$ massive mode at $m^2 = 4 G_c / I_\omega$
  - [Lattice Impedance Decomposition](lattice-impedance-decomposition.md) — Op3 bond reflection via $Z_{\text{eff}}(r) = Z_0 / \sqrt{S}$
  - [Universal Saturation-Kernel Catalog (A-034)](../../../common/universal-saturation-kernel-catalog.md) — Op3/Op14 saturation framework
- **Canonical manuscript:**
  - Vol 1 Ch 1 (Axiom 1) — K4 lattice + tetrahedral connectivity
  - Vol 1 Ch 2 (Macroscopic Moduli) — magic-angle $K = 2G$
  - Vol 1 Ch 4 (Continuum Electrodynamics) — Master Equation context
