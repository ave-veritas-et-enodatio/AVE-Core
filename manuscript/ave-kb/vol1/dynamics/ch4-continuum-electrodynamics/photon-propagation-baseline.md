[↑ Ch.4 Continuum Electrodynamics](index.md)
<!-- leaf: verbatim -->
<!-- path-stable: referenced from photon-identification + L3 closure synthesis as canonical photon-on-substrate baseline -->

# Photon Propagation Baseline: $v_{\text{meas}}/c = \sqrt{2}$ Cardinal-Axis Kinematics

Canonical empirical baseline for free photon propagation on the K4-TLM substrate in the linear-vacuum regime. The wavefront speed along cardinal axes (x̂, ŷ, ẑ) is $v = c \cdot \sqrt{2}$ — a **pure substrate-geometry effect native to Axiom 1**, not an SM/QED import. Along diagonal axes (port unit vectors $\hat{p}_n$) the speed reduces to $v = c$. This anisotropy is the K4 lattice's distinguishing kinematic signature; any photon-physics test on the K4-TLM substrate measures against this baseline.

## Key Results

| Result | Statement |
|---|---|
| Cardinal-axis wavefront speed (measured) | $v_{\text{meas}} = 4.348 \times 10^8$ m/s; $v/c = 1.450 \approx \sqrt{2}$ |
| Diagonal-axis predicted speed | $v = c$ (along port unit vectors $\hat{p}_n = (1, 1, 1)/\sqrt{3}$ etc.) |
| Substrate physical mechanism | Port projections onto cardinal axes are $\pm 1/\sqrt{3}$; 4-port pattern forces each lattice step to advance by one full cardinal cell → effective $\sqrt{2}$ speed |
| $A_1$ vs $T_2$ propagation speeds | $A_1$ (longitudinal): $c \sqrt{2} = \sqrt{K_{\text{bulk}} / \rho}$; $T_2$ (transverse photon): $c = \sqrt{G / \rho}$ |
| Amplitude regime | $0.01 \cdot V_{\text{SNAP}} \approx 5.1$ kV (sub-yield, linear vacuum throughout — no Axiom 4 engagement) |
| AVE compliance | Pure $T_2$ projected source $(-\tfrac{1}{2}, -\tfrac{1}{2}, +\tfrac{1}{2}, +\tfrac{1}{2}) \cdot 1/\sqrt{2}$ for $+\hat{x}$; soft source with PML absorbing reverse-going component |

## §1 — Substrate-physics framing

The K4-TLM substrate has **anisotropic kinematics native to Axiom 1**:

### K4 port-mode propagation speeds

| Port-mode | Wave character | Speed | Substrate origin |
|---|---|---|---|
| $A_1 \propto (1, 1, 1, 1)$ | Scalar / longitudinal | $c \cdot \sqrt{2} = \sqrt{K_{\text{bulk}} / \rho}$ | Bulk modulus $K_{\text{bulk}}$ governs scalar compression speed |
| $T_2$ (chiral-transverse triplet) | **The photon** (per [photon-identification](photon-identification.md)) | $c = \sqrt{G / \rho}$ | Shear modulus $G$ governs transverse shear speed |

The K4 magic-angle condition $K = 2G$ (Vol 1 Ch 2 macroscopic moduli) makes the substrate's $A_1$ and $T_2$ speeds related by $v_{A_1} / v_{T_2} = \sqrt{2}$ — the same $\sqrt{2}$ that shows up in cardinal-axis kinematics.

### Cardinal-axis vs diagonal-axis kinematics

| Propagation direction | Wavefront speed | Mechanism |
|---|---|---|
| Cardinal (along $\hat{x}, \hat{y}, \hat{z}$) | $v = c \cdot \sqrt{2}$ | Port projections onto cardinal axes are $\pm 1/\sqrt{3}$; 4-port pattern forces each lattice step to advance by one full cardinal cell |
| Diagonal (along port unit vectors $\hat{p}_n = (1, 1, 1)/\sqrt{3}$ etc.) | $v = c$ | Junction-diagonal photon, no cardinal-axis $\sqrt{2}$ factor |

**This is pure substrate-geometry**, not Special Relativity violation. The substrate-internal speed $c$ is the canonical AVE wave speed (Vol 1 Ch 1); cardinal-axis $\sqrt{2}$ is a lattice-projection artifact that disappears in the continuum limit and at diagonal-axis injection.

## §2 — Test setup

Default config (`src/scripts/vol_1_foundations/photon_propagation.py`):

| Parameter | Value |
|---|---|
| Lattice | $N = 96$ (96³ K4-TLM cube) |
| PML thickness | 8 |
| Source plane | $x_{\text{source}} = 16$ (just inside $-x$ PML) |
| Wavelength | $\lambda_{\text{cells}} = 10$ (visualization choice; not matched to Compton or SM scale) |
| Transverse Gaussian σ | $\sigma_{yz} = 8$ |
| Temporal envelope σ | $t_\sigma = 0.75$ periods |
| Amplitude | $0.01 \cdot V_{\text{SNAP}} \approx 5.1$ kV (sub-yield) |
| Time steps | 240 (~17 periods of recording) |
| Direction | $+\hat{x}$ (cardinal-axis) |
| $T_2$ projection | ON (pure transverse photon) |

**Source design**: time-domain plane source, NOT spatial IC. $V_{\text{inc}}[x_0, y, z, \text{forward ports}] += \text{envelope}(t) \cdot \sin(\omega t)$. Soft source (additive) at $x = x_0$; injects in $\pm \hat{x}$ direction; PML on $-x$ boundary absorbs the reverse-going component. Forward-port weights: $T_2$-projected ($\sum w = 0$) for pure transverse photon; raw weights = 50% $A_1$ + 50% $T_2$ mixed.

**For $+\hat{x}$**: pure $T_2$ pattern is $(-\tfrac{1}{2}, -\tfrac{1}{2}, +\tfrac{1}{2}, +\tfrac{1}{2}) \cdot 1/\sqrt{2}$.

**Pre-registered measurement**: peak energy density arrival time at two reference planes $x_a = 36$, $x_b = 76$. Velocity = $(x_b - x_a) \cdot dx / (t_b - t_a)$.

## §3 — Empirical result

| Quantity | Value |
|---|---|
| $t_{\text{arrival}, a}$ (peak at $x = 36$) | $1.274 \times 10^{-7}$ s |
| $t_{\text{arrival}, b}$ (peak at $x = 76$) | $2.194 \times 10^{-7}$ s |
| $v_{\text{meas}}$ | $4.348 \times 10^8$ m/s |
| $v / c$ | **$1.450 \approx \sqrt{2}$** |
| Amplitude (in $V_{\text{SNAP}}$ units) | $0.01$ (sub-yield) |

**Verdict**: Photon propagates cleanly along $+\hat{x}$. Wavefront speed $= c \cdot \sqrt{2}$, matching pre-registered cardinal-axis kinematics for K4 substrate. Phase A infrastructure validated.

## §4 — What the lattice does (substrate-perspective)

With a photon present, the K4-TLM lattice nodes near the propagating packet experience:

- **$|V_{\text{inc}}|^2$ rises locally** as the wave reaches each node — small but nonzero ($A^2_{\text{local}} \approx 10^{-4} \ll V_{\text{yield}}^2 \approx 7 \times 10^{-3}$)
- **$A^2_{\text{local}}$ well below saturation cusp** at $\sqrt{2\alpha} \approx 0.121$ → substrate stays in **Regime I (linear vacuum)** throughout
- **No Op14 saturation engagement** — $Z_{\text{eff}} \approx Z_0$, $c_{\text{eff}} \approx c_0$
- **No TIR wall formation** — field passes through without trapping
- **Wavefront propagates at $\sqrt{2} c$ (cardinal-axis kinematics)** — pure substrate-geometry effect, native Axiom 1
- **No Cosserat coupling** — Op14 cross-block is zero ($\omega = 0$ throughout, K4 $V_{\text{inc}} / V_{\text{ref}}$ carries the photon alone)

This is the substrate doing exactly what corpus framework predicts for an unperturbed photon in linear vacuum: **clean propagation at the substrate's transverse mode speed ($T_2$), with cardinal-axis anisotropy adding the $\sqrt{2}$ factor.**

**The free photon is NOT the canonical electron** — no trap mechanism is engaged at sub-yield amplitude in linear vacuum. This is the baseline against which any electron-formation test would be compared.

## §5 — Role in the photon → electron derivation chain

This baseline anchors the photon-to-electron formation chain (see [photon-identification §4](photon-identification.md)):

1. **Baseline (this leaf)**: free photon at sub-yield amplitude propagates at $\sqrt{2} c$ cardinal-axis on linear-vacuum K4-TLM, no trap, no saturation
2. **Amplitude crosses $V_{\text{yield}} = \sqrt{\alpha} V_{\text{snap}}$**: Axiom 4 engages, $C_{\text{eff}} \to \infty$ locally
3. **TIR wall formation**: $Z_{\text{local}} \to 0$, $\Gamma \to -1$, lattice creates its own perfect TIR mirror
4. **Standing-wave trap**: photon's transverse wave reflects off self-created walls; becomes bound state
5. **Bound state = electron**: $m_e c^2 = \hbar \omega_C$, $e =$ topological winding, $\hbar/2 =$ Finkelstein–Misner spinor double-cover, $\alpha = 1/137 =$ TIR leakage rate per cycle

Any deviation from this chain at the photon-baseline level (this leaf's result) would indicate an engine implementation issue, not framework physics — making this the **calibration test for photon-physics work on K4-TLM**.

## Cross-references

- **Canonical script:** `src/scripts/vol_1_foundations/photon_propagation.py` — Phase A K4-TLM wave-packet launcher (471 lines)
- **Companion script (numerical-only, pending GIF):** `src/scripts/vol_1_foundations/photon_propagation_diagonal.py` — diagonal-axis variant predicting $v = c$
- **Visualization artifacts** (regenerable from canonical script via the photon_propagation Phase A wave-packet launcher):
  - Cardinal-axis side-by-side animation (`|V|^2` xy-slice at $z = N/2$ on log color scale, with interior centroid $x(t)$ trajectory)
  - NPZ data with full frames + centroids + times for post-hoc analysis
- **KB cross-cutting:**
  - [Photon Identification](photon-identification.md) — canonical $T_2$-only photon definition + electron-formation mechanism
  - [Master Equation](master-equation.md) — substrate dielectric specialization of Axiom 4
  - [Vol 1 Ch 2 Macroscopic Moduli](../../axioms-and-lattice/ch2-macroscopic-moduli/index.md) — magic-angle $K = 2G$ relating $A_1$ and $T_2$ speeds
- **Canonical manuscript:**
  - Vol 1 Ch 1 (Axiom 1) — substrate $\sqrt{2}$ cardinal-axis kinematics
  - Vol 1 Ch 4 (continuum electrodynamics) — Master Equation context
