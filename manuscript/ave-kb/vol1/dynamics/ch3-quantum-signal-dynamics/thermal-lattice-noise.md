[↑ Ch.3 Quantum Signal Dynamics](index.md)
<!-- leaf: verbatim -->
<!-- path-stable: referenced from vol4/circuit-theory + vol3/cosmology as canonical thermal noise + T_V-rupt = 3.44 MK -->

# Thermal Lattice Noise + AVE-Native Vacuum Rupture Temperature $T_{V\text{-rupt}}$

The classical-equipartition derivation of thermal lattice noise on the K4 substrate yields **vacuum-substrate temperature thresholds** distinct from particle-plasma temperatures. The AVE-native vacuum rupture temperature $T_{V\text{-rupt}} \approx 3.44 \times 10^6$ K is the AVE-native analog of the Schwinger limit but stated as a **vacuum-substrate TEMPERATURE** rather than field strength — falsifiable: if any laboratory process succeeds in heating the vacuum itself (not just plasma) above 3.44 MK without spontaneous pair generation, AVE is falsified.

## Key Results

| Result | Statement |
|---|---|
| K4 photon $\langle V^2 \rangle_T$ (per port) | $k_B T / C_{\text{cell}} = k_B T / (\varepsilon_0 \ell_{\text{node}})$ |
| In natural units | $\langle V^2 \rangle_T = k_B T \cdot 4\pi / \alpha$ |
| **Vacuum rupture temperature** | $\boxed{T_{V\text{-rupt}} \approx 3.44 \times 10^6 \text{ K}}$ (where $\sigma_V = V_{\text{SNAP}}$) |
| Cosserat translation $\sigma_u$ | $\sqrt{k_B T / (2\pi)}$ in natural units |
| Cosserat rotation $\sigma_\omega$ | $0.17 \sqrt{k_B T}$ in natural units (massive field, mass-gap $m^2 = 4 G_c/I_\omega$) |
| $\sigma_\omega$ at CMB ($T = 2.7$ K) | $3.6 \times 10^{-6}$ — vanishingly small, effectively zero for pair creation |
| Engine-default for pair-creation runs | $T \sim 10^8$ K, gives $\sigma_\omega \sim 0.02$, sufficient thermal noise for cascade amplification |

## §1 — Classical equipartition framework

At temperature $T$, each quadratic DOF in the Lagrangian contributes energy $k_B T/2$ on average. For the coupled K4-Cosserat system:

- **K4 photon field** $V_{\text{inc}}[i, n]$ (4 ports per node): quadratic kinetic + quadratic potential
- **Cosserat translation** $u(r)$ + velocity $\dot u(r)$: $\tfrac{1}{2} \rho |\dot u|^2 + \tfrac{1}{2} G |\varepsilon|^2$ per volume
- **Cosserat rotation** $\omega(r)$ + velocity $\dot\omega(r)$: $\tfrac{1}{2} I_\omega |\dot\omega|^2 + \tfrac{1}{2} \gamma |\nabla \omega|^2 + \tfrac{1}{2} G_c \omega^2$ per volume (includes mass-gap term)

Each gives a distinct amplitude prediction.

## §2 — Vacuum-substrate $T$ vs. particle-plasma $T$ (CRITICAL DISTINCTION)

**The "T" in this derivation is the temperature of the K4 LATTICE SUBSTRATE itself** — the thermal amplitude of the scalar $V$ field on each bond's capacitance. It is NOT the kinetic temperature of any particle (electron, ion) residing IN the vacuum.

| System | Vacuum-substrate $T$ | Particle-kinetic $T$ | AVE rupture? |
|---|---|---|---|
| CMB | 2.7 K | 2.7 K (photon gas) | No |
| Earth's atmosphere | $\sim 2.7$ K (vacuum) | 300 K (air) | No |
| Sun's surface | $\sim 2.7$ K (vacuum) | 5,800 K (photosphere) | No |
| **Sun's core** | $\sim 2.7$ K (vacuum) | $1.5 \times 10^7$ K (plasma) | **No** — vacuum still cold |
| Hypothetical uniformly-heated lattice | $\boxed{3.44 \times 10^6}$ K | any | **YES** — $V$ ruptures |
| Early universe (nucleosynthesis) | $\sim 10^9$ K (coupled to photon gas) | $\sim 10^9$ K | **YES** — pair soup |

In solar plasma, the particles are hot but they don't thermalize the vacuum substrate to their kinetic temperature — the particles are excitations ON TOP of a still-cold K4 lattice. **Only in the very early universe, when matter-radiation coupling dominates, does the substrate itself get heated to particle-like temperatures.**

## §3 — Vacuum rupture temperature derivation

The condition $\sigma_V = V_{\text{SNAP}}$ (vacuum thermally saturates one port's rupture) gives the upper bound for thermal $V$ equilibrium to coexist with stable vacuum:

$$\frac{k_B T_{V\text{-rupt}}}{m_e c^2} = \frac{\alpha}{4\pi} \approx 5.805 \times 10^{-4}$$

In SI:

$$k_B T_{V\text{-rupt}} = 5.805 \times 10^{-4} \cdot (0.511 \text{ MeV}) \approx 296.7 \text{ eV}$$

$$\boxed{\, T_{V\text{-rupt}} \approx 3.44 \times 10^6 \text{ K} \,}$$

**Equivalently:** if the K4 substrate itself were in thermal equilibrium at $T > 3.44$ MK, the $V$ fluctuations would exceed $V_{\text{SNAP}}$ and the vacuum would spontaneously rupture into pairs. Below this threshold, the vacuum can sustain thermal noise without breaking.

**AVE-NATIVE PREDICTION** analogous to the Schwinger limit, but stated as a **vacuum-substrate TEMPERATURE** rather than field STRENGTH. **Falsifiable**: if any laboratory process succeeds in heating the VACUUM itself (not just plasma) above 3.44 MK without spontaneous pair generation, AVE is falsified.

## §4 — Cosserat rotational noise (the key one)

The rotational Lagrangian has:
- Kinetic: $\tfrac{1}{2} I_\omega |\dot\omega|^2$
- Mass-gap potential: $2 G_c |\omega|^2$ (from micropolar term; mass gap $m^2 = 4 G_c / I_\omega$ — see [Cosserat Mass-Gap](../../axioms-and-lattice/ch1-fundamental-axioms/cosserat-mass-gap.md))
- Gradient potential: $\tfrac{1}{2} \gamma |\nabla \omega|^2$

The $\omega$ field has a **MASS GAP** $m^2 = 4 G_c / I_\omega \neq 0$. **Crucial**: a massive field's thermal noise is FINITE at the origin, not UV-divergent.

For a massive scalar-like field $\omega$ at temperature $T$, classical equipartition gives:

$$\langle \omega^2(r) \rangle_T = \frac{k_B T}{4\pi^2 I_\omega} \int_0^{k_{\max}} \frac{k^2 \, dk}{c_R^2 k^2 + m^2}$$

In natural units ($I_\omega = \gamma = G_c = 1$, so $c_R = 1$, $m^2 = 4$):

$$\langle \omega^2 \rangle_T \approx \frac{1.14 \, k_B T}{4\pi^2} \approx 0.0288 \cdot k_B T$$

$$\sigma_\omega \approx 0.17 \cdot \sqrt{k_B T} \text{ (natural units, for } G_c = I_\omega = \gamma = 1\text{)}$$

| Temperature | $k_B T$ (in $m_e c^2$) | $\sigma_\omega$ (rad, natural units) |
|---|---|---|
| $T = 0$ | 0 | 0 |
| $T = 2.7$ K (CMB) | $4.56 \times 10^{-10}$ | $3.6 \times 10^{-6}$ |
| $T = 10^6$ K | $1.69 \times 10^{-4}$ | $2.2 \times 10^{-3}$ |
| $T = 10^9$ K | $1.69 \times 10^{-1}$ | $7.0 \times 10^{-2}$ |

**Engine default for $T = T_{\text{CMB}}$**: $\sigma_\omega \approx 3.6 \times 10^{-6}$ — vanishingly small, effectively zero for pair-creation purposes. This confirms the C1 prediction that **cold-vacuum cannot produce pairs** by thermal noise alone.

**Engine recommendation for pair-creation runs**: $T \sim 10^8$ K gives $\sigma_\omega \sim 0.02$, sufficient thermal noise for cascade amplification into observable pair creation.

## §5 — Cosserat translational noise (lattice-Nyquist cutoff)

The $u$ field is massless; its noise requires UV cutoff at $k_{\max} = \pi / \ell_{\text{node}}$:

$$\langle u^2 \rangle_T = \frac{k_B T}{G} \cdot \frac{k_{\max}}{2\pi^2} = \frac{k_B T}{2\pi G \ell_{\text{node}}}$$

In natural units ($G = \rho = 1$, $\ell_{\text{node}} = 1$):

$$\sigma_u^2 = \langle u^2 \rangle_T = \frac{k_B T}{2\pi}, \quad \sigma_{\dot u}^2 = \langle \dot u^2 \rangle_T = \frac{k_B T}{2\pi}$$

Both fields have the same characteristic scale $\sqrt{k_B T / (2\pi)}$ in natural units.

## §6 — K4 photon field $\langle V^2 \rangle_T$

Each bond's capacitance $C_{\text{cell}} = \varepsilon_0 \ell_{\text{node}}$ gives classical Johnson-Nyquist noise:

$$\langle V^2 \rangle_T = \frac{k_B T}{C_{\text{cell}}} = \frac{k_B T}{\varepsilon_0 \ell_{\text{node}}}$$

In lattice natural units ($\varepsilon_0 = \alpha / (4\pi)$):

$$\langle V^2 \rangle_T = \frac{k_B T \cdot 4\pi}{\alpha}$$

For numerical scales in $V_{\text{SNAP}}^2$ units:

| Temperature | $k_B T / (m_e c^2)$ | $\langle V^2 \rangle_T / V_{\text{SNAP}}^2$ | $\sigma_V / V_{\text{SNAP}}$ |
|---|---|---|---|
| $T = 0$ | 0 | 0 | 0 |
| $T = 2.7$ K (CMB) | $4.56 \times 10^{-10}$ | $1.57 \times 10^{-7}$ | $3.96 \times 10^{-4}$ |
| $T = 3.44 \times 10^6$ K (**$T_{V\text{-rupt}}$**) | $5.805 \times 10^{-4}$ | $1.0$ | $1.0$ |
| $T = 10^7$ K | $1.69 \times 10^{-3}$ | $2.91$ | $1.71$ ($> V_{\text{SNAP}}$) |
| $T = 10^9$ K | $1.69 \times 10^{-1}$ | $58.2$ | $7.63$ |

At $T = T_{V\text{-rupt}}$, $\sigma_V = V_{\text{SNAP}}$ — vacuum at one-sigma fluctuation reaches the rupture amplitude.

## §7 — Combined initialization recipe (engine integration)

For `VacuumEngine3D.initialize_thermal(T)`:

```python
def initialize_thermal(self, T: float):
    """Initialize (V_inc, u, omega, u_dot, omega_dot) from classical
    equipartition at T (in m_e c^2 units)."""
    if T <= 0:
        return  # cold vacuum is deterministic
    
    # K4 photon (V_inc per port)
    sigma_V = np.sqrt(T * 4 * np.pi / ALPHA) * V_SNAP
    self.k4.V_inc = rng.standard_normal(...) * sigma_V * mask_active
    
    # Cosserat rotation omega (massive, mass-gap m^2 = 4)
    mode_factor = np.pi - 2 * np.arctan(np.pi / 2)  # ~1.14
    sigma_omega = np.sqrt(T * mode_factor / (4 * np.pi**2 * self.cos.I_omega))
    self.cos.omega = rng.standard_normal(...) * sigma_omega * mask_alive
    
    # Cosserat velocities (equipartition)
    self.cos.omega_dot = rng.standard_normal(...) * np.sqrt(T / self.cos.I_omega) * mask_alive
    
    # Cosserat translation u (massless, Nyquist cutoff)
    sigma_u = np.sqrt(T / (2 * np.pi * self.cos.rho))
    self.cos.u = rng.standard_normal(...) * sigma_u * mask_alive
    self.cos.u_dot = rng.standard_normal(...) * np.sqrt(T / self.cos.rho) * mask_alive
```

For Phase III-B "cold EM vacuum + warm matter-precursor" runs, `thermalize_V=False` leaves $V_{\text{inc}} = 0$ and only thermalizes the Cosserat sector — valid at arbitrary $T$ since only the Cosserat sector is thermalized.

## Cross-references

- **Canonical scripts:**
  - `src/ave/topological/vacuum_engine.py` — `initialize_thermal(T)` method
  - `src/ave/core/constants.py:222` — $Z_0$, $V_{\text{SNAP}}$, $V_{\text{YIELD}}$
- **KB cross-cutting:**
  - [Cosserat Mass-Gap](../../axioms-and-lattice/ch1-fundamental-axioms/cosserat-mass-gap.md) — $m^2 = 4 G_c / I_\omega$ used in $\sigma_\omega$ derivation
  - [Universal Saturation-Kernel Catalog (A-034)](../../../common/universal-saturation-kernel-catalog.md) — $T_{V\text{-rupt}}$ as atomic-EM-scale row's temperature-side analog
  - [Lattice Impedance Decomposition](../../operators-and-regimes/ch6-universal-operators/lattice-impedance-decomposition.md) — $V_{\text{SNAP}}$ vs $V_{\text{YIELD}}$ normalization
  - [Pair Production Axiom Derivation](../../../vol2/particle-physics/ch01-topological-matter/pair-production-axiom-derivation.md) — pair-creation engagement at $V \geq V_{\text{SNAP}}$
- **Canonical manuscript:**
  - Vol 4 Ch 1:278 — per-bond $C_{\text{cell}} = \varepsilon_0 \ell_{\text{node}}$
  - E-042 (manuscript_pending) — $T_{V\text{-rupt}}$ canonization to manuscript queued
