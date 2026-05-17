# 47 — Thermal Lattice Noise Amplitude from Axiom 1 (Classical Equipartition Derivation)

**Status:** foundational derivation (2026-04-22)
**Parent plan:** `~/.claude/plans/document-list-for-next-chat-compressed-thunder.md` Stage 1b
**Depends on:** [46_vacuum_engine_scope.md](46_vacuum_engine_scope.md) C1 (cold vacuum is
  deterministic; thermal noise is bandwidth-limited electrical noise at finite T)
**Alternative (deferred):** LC-resonance-eigenmode thermal population — more AVE-native
  but requires eigenmode analysis of the K4 lattice. Deferred per plan P1-C.

**Purpose:** Derive the RMS amplitude of the thermal lattice noise in (V, u, ω) fields
for a K4-TLM at temperature T, in classical equipartition (the simplest AVE-native
starting point). This sets the initial-condition noise level for the `T>0` mode of
`VacuumEngine3D`.

## 1. Framework — classical equipartition on the K4 lattice

At temperature T, each quadratic DOF in the Lagrangian contributes energy `kT/2` on
average (classical equipartition). For the coupled K4-Cosserat system, the DOFs are:

- **K4 photon field** `V_inc[i, n]` (4 ports per node): quadratic kinetic + quadratic potential
- **Cosserat translation** `u(r)` + velocity `u̇(r)`: `½ρ|u̇|² + ½G|ε|²` per volume
- **Cosserat rotation** `ω(r)` + velocity `ω̇(r)`: `½I_ω|ω̇|² + ½γ|∇ω|² + ½G_c·ω²` per volume (includes mass gap term)

Each gives a distinct amplitude prediction.

## 2. Scalar K4 photon field ⟨V²⟩_T

The K4-TLM's per-bond capacitance C_cell = ε_0 · ℓ_node (Vol 4 Ch 1:278) means each
bond acts as a capacitor with classical Johnson-Nyquist noise:

$$\langle V^2 \rangle_T = \frac{k_B T}{C_{cell}} = \frac{k_B T}{\varepsilon_0 \ell_{node}}$$

In lattice natural units (m_e = c = ℏ = 1, ℓ_node = 1, ε_0 = α/(4π) from
`constants.py`):

$$\langle V^2 \rangle_T = \frac{k_B T \cdot 4\pi}{\alpha}$$

For numerical scales in m_e c² units:

| Temperature | k_B T / (m_e c²) | ⟨V²⟩_T in V_SNAP² units | σ_V / V_SNAP |
|---|---|---|---|
| T = 0 | 0 | 0 | 0 |
| T = 2.7 K (CMB) | 4.56·10⁻¹⁰ | 1.57·10⁻⁷ | 3.96·10⁻⁴ |
| T = 3.44 × 10⁶ K (**AVE rupture, see §2.4**) | 5.805·10⁻⁴ | **1.0** | **1.0** |
| T = 10⁷ K | 1.69·10⁻³ | 2.91 | 1.71 (> V_SNAP) |
| T = 10⁹ K | 1.69·10⁻¹ | 58.2 | 7.63 |

### 2.1 Interpretation — vacuum temperature vs. particle-plasma temperature (corrected 2026-04-22)

**Critical distinction, added after Phase III-B dry runs revealed the scale:**

The "T" in this derivation is the temperature of the K4 LATTICE SUBSTRATE
itself — the thermal amplitude of the scalar V field on each bond's capacitance.
It is NOT the kinetic temperature of any particle (electron, ion) residing
IN the vacuum.

Concrete examples of the distinction:

| System | Vacuum-substrate T | Particle-kinetic T | AVE rupture? |
|---|---|---|---|
| CMB | 2.7 K | 2.7 K (photon gas) | No |
| Earth's atmosphere | ~2.7 K (vacuum) | 300 K (air) | No |
| Sun's surface | ~2.7 K (vacuum) | 5,800 K (photosphere) | No |
| **Sun's core** | **~2.7 K (vacuum)** | **1.5 × 10⁷ K (plasma)** | **No — vacuum still cold** |
| Hypothetical uniformly-heated lattice | **3.44 × 10⁶ K** | any | **YES — V ruptures** |
| Early universe (nucleosynthesis) | ~10⁹ K (coupled to photon gas) | ~10⁹ K | **YES — pair soup** |

In solar plasma, the particles are hot but they don't thermalize the vacuum substrate
to their kinetic temperature — the particles are excitations ON TOP of a still-cold
K4 lattice. Only in the very early universe, when matter-radiation coupling dominates,
does the substrate itself get heated to particle-like temperatures.

### 2.2 V rupture threshold T_V-rupt

The condition `σ_V = V_SNAP` (vacuum thermally saturates one port's rupture)
gives the upper bound for thermal V equilibrium to coexist with stable vacuum:

$$\frac{k_B T_{V\text{-rupt}}}{m_e c^2} = \frac{\alpha}{4\pi} \approx 5.805 \times 10^{-4}$$

In SI:
$$k_B T_{V\text{-rupt}} = 5.805 \times 10^{-4} \cdot (0.511 \text{ MeV}) \approx 296.7 \text{ eV}$$
$$\boxed{T_{V\text{-rupt}} \approx 3.44 \times 10^{6} \text{ K}}$$

Equivalently: if the K4 substrate itself were in thermal equilibrium at T > 3.44 MK,
the V fluctuations would exceed V_SNAP and the vacuum would spontaneously rupture
into pairs. Below this threshold, the vacuum can sustain thermal noise without
breaking.

This is an AVE-NATIVE PREDICTION analogous to the Schwinger limit, but stated
as a vacuum-substrate TEMPERATURE rather than field STRENGTH. Falsifiable: if
any laboratory process succeeds in heating the VACUUM itself (not just plasma)
above 3.44 MK without spontaneous pair generation, AVE is falsified.

### 2.3 Implication for Phase III-B simulation

For stable numerical simulation of "cold K4 substrate with warm matter-precursor",
`VacuumEngine3D.initialize_thermal(T, thermalize_V=False)` leaves V_inc = 0 and
only thermalizes the Cosserat (u, ω) fields. This corresponds to a physical
state where:
- The K4 lattice is at T=0 (cold EM vacuum)
- The rotational sector has a warm-bath initial condition
- CW photon sources drive coherent V; V is NOT thermal

This is valid for any T < 3.44 MK equivalent. Above this, the "vacuum" cannot
be in thermal equilibrium — any attempted simulation at higher vacuum-substrate T
will produce numerical blowup (correctly reflecting the physical instability).

**Engine default recommendation**: T = 2.7 K (CMB) for realistic ambient simulations.
Phase III-B tests T = 0 (cold null) and T = 0.1 m_e c² = 5.93 × 10⁸ K
**Cosserat-only** (V_inc forced to zero), representing a "hot matter-precursor
sector in a cold EM vacuum" — non-equilibrium but numerically stable.

## 3. Cosserat translational field ⟨u²⟩_T, ⟨u̇²⟩_T

The Cosserat Lagrangian (from Phase I) has:
- Kinetic: `L_kin = ½ρ|u̇|² d³r`
- Strain potential: `W_u ~ ½G|ε(u, ω)|²` where ε involves first derivatives of u

At T, each MODE of u has ⟨u̇²⟩ = kT/ρ per component, ⟨u²⟩ depends on spatial spectrum.

For a 3D field on a lattice with Nyquist cutoff `k_max = π/ℓ_node`, the number of
modes per volume is (k_max/π)³ = 1/ℓ_node³ per mode-density-volume. The RMS amplitude
of u at a single site, integrated over all modes, is approximately:

$$\langle u^2(r) \rangle_T \approx \frac{k_B T}{G} \cdot \frac{1}{(2\pi)^3} \int d^3k \frac{1}{k^2}$$

The integral from 0 to k_max diverges linearly at UV (no IR problem because of the
"noise floor" interpretation — there's no physics at k > k_max):

$$\langle u^2 \rangle_T = \frac{k_B T}{G} \cdot \frac{k_{max}}{2\pi^2} = \frac{k_B T}{G} \cdot \frac{1}{2\pi \ell_{node}}$$

In natural units (G=ρ=1, ℓ_node=1):

$$\sigma_u^2 = \langle u^2 \rangle_T = \frac{k_B T}{2\pi}$$

$$\sigma_{\dot u}^2 = \langle \dot u^2 \rangle_T = \frac{k_B T \cdot k_{max}}{2\pi^2 \rho} \cdot c_T^2 / 1 = \frac{k_B T}{2\pi}$$
(both fields have the same characteristic scale √(kT/2π) in natural units)

## 4. Cosserat rotational field ⟨ω²⟩_T, ⟨ω̇²⟩_T (the KEY ONE)

The rotational Lagrangian (Phase I, 41_):
- Kinetic: `½I_ω|ω̇|²`
- Mass-gap potential: `2·G_c·|ω|²` (from the micropolar term W_micropolar, per 41_ §6 Finding 2: mass gap m² = 4·G_c/I_ω)
- Gradient potential: `½γ·|∇ω|²`

The ω field has a **MASS GAP** m² = 4G_c/I_ω ≠ 0 (Phase I finding). This is CRUCIAL:
a massive field's thermal noise is FINITE at the origin, not UV-divergent.

For a massive scalar-like field ω at temperature T, classical equipartition gives:

$$\langle \omega^2(r) \rangle_T = \frac{k_B T}{4\pi^2 I_\omega} \int_0^{k_{max}} \frac{k^2 dk}{c_R^2 k^2 + m^2}$$

where c_R = √(γ/I_ω) is the rotational wave speed. In natural units (I_ω=γ=G_c=1, so c_R=1, m²=4):

$$\langle \omega^2 \rangle_T = \frac{k_B T}{4\pi^2} \int_0^{\pi} \frac{k^2 dk}{k^2 + 4}$$

Evaluating the integral from 0 to π:
$$\int_0^\pi \frac{k^2}{k^2+4} dk = \int_0^\pi \left(1 - \frac{4}{k^2+4}\right) dk = \pi - 4 \cdot \frac{1}{2}\tan^{-1}(\pi/2) \approx \pi - 2\tan^{-1}(1.57) \approx 3.14 - 2.0 \approx 1.14$$

So:
$$\langle \omega^2 \rangle_T \approx \frac{1.14 k_B T}{4\pi^2} \approx 0.0288 \cdot k_B T$$

$$\sigma_\omega \approx 0.17 \cdot \sqrt{k_B T}  \quad \text{(in natural units, for G_c=I_ω=γ=1)}$$

For reference at various T:

| Temperature | k_B T (in m_e c²) | σ_ω (rad, natural units) |
|---|---|---|
| T = 0 | 0 | 0 |
| T = 2.7 K | 4.56·10⁻¹⁰ | 3.63·10⁻⁶ |
| T = 10⁶ K | 1.69·10⁻⁴ | 2.21·10⁻³ |
| T = 10⁹ K | 1.69·10⁻¹ | 6.99·10⁻² |

**Comparison to previous placeholder**: I used σ=0.01 in my earlier Phase III-B attempt,
which corresponds to T ≈ 2·10⁷ K — a very hot vacuum. Not unreasonable for pair-creation-
regime physics but not an "ambient" value.

**Engine default for T=CMB**: σ_ω ≈ 3.6·10⁻⁶ (vanishingly small, effectively zero for
pair-creation purposes — confirming the C1 prediction that cold-vacuum cannot produce pairs).

**Engine recommendation for pair-creation runs**: T ~ 10⁸ K gives σ_ω ~ 0.02, sufficient
thermal noise for cascade amplification into observable pair creation.

## 5. Combined (u, ω, V) initialization recipe

For `VacuumEngine3D.initialize_thermal(T)`:

```python
def initialize_thermal(self, T: float):
    """Initialize (V_inc, u, ω, u_dot, ω_dot) from classical equipartition at T.
    
    T is in dimensionless m_e c² units (or SI Kelvin converted via k_B/m_e c²).
    All noise is Gaussian white; spatial masks apply (mask_alive).
    """
    if T <= 0:
        # C1: cold vacuum is deterministic, all zero
        return
    
    # Scalar V field
    sigma_V = np.sqrt(T * 4 * np.pi / ALPHA) * V_SNAP  # in SI volts
    self.k4.V_inc = rng.standard_normal(self.k4.V_inc.shape) * sigma_V
    self.k4.V_inc *= self.k4.mask_active[..., None, None]
    
    # Cosserat rotational ω (massive via G_c)
    # Mode integral from 0 to π: (π - 2·arctan(π/2)) ≈ 1.14 for m²=4
    mode_factor = np.pi - 2 * np.arctan(np.pi / 2)
    sigma_omega = np.sqrt(T * mode_factor / (4 * np.pi**2 * self.cos.I_omega))
    self.cos.omega = rng.standard_normal(self.cos.omega.shape) * sigma_omega
    self.cos.omega *= self.cos.mask_alive[..., None]
    
    # Cosserat velocities (equipartition with kinetic terms)
    sigma_omega_dot = np.sqrt(T / self.cos.I_omega)
    self.cos.omega_dot = rng.standard_normal(self.cos.omega_dot.shape) * sigma_omega_dot
    self.cos.omega_dot *= self.cos.mask_alive[..., None]
    
    # Similarly for u (massless, needs k_max cutoff):
    sigma_u = np.sqrt(T / (2 * np.pi * self.cos.rho))  # natural-unit form
    self.cos.u = rng.standard_normal(self.cos.u.shape) * sigma_u
    self.cos.u_dot = rng.standard_normal(self.cos.u_dot.shape) * np.sqrt(T / self.cos.rho)
    self.cos.u *= self.cos.mask_alive[..., None]
    self.cos.u_dot *= self.cos.mask_alive[..., None]
```

Caveats:
- This is WHITE noise. The proper AVE-native version would have a specific spectral
  shape set by the K4 eigenmodes (deferred per L1).
- The u-field is technically massless; its noise should have a spectral structure.
  The `σ_u ~ √(kT/2π)` estimate is a heuristic.
- Temperature in this function is in units of m_e c² (so T=1 means kT = electron mass).
  For SI conversion, use `k_B · T_kelvin / (m_e · c²)`.

## 6. What this derivation DOES and DOES NOT resolve

### Does:
- Provides concrete σ values at various T for engine initialization
- Confirms C1 numerically: at T=2.7 K, σ_ω ~ 10⁻⁶ (effectively zero for pair creation)
- Identifies AVE-native vacuum-substrate rupture temperature: **T_V-rupt ≈ 3.44 × 10⁶ K** (§2.2)
- Distinguishes vacuum-substrate T from particle-plasma T (§2.1 table) — only the
  former governs rupture of the LC network itself
- Phase III-B uses `thermalize_V=False` to simulate "cold EM vacuum + warm matter-precursor"
  which is valid at arbitrary T since only the Cosserat sector is thermalized

### Does NOT resolve:
- Whether CLASSICAL equipartition is the correct long-wavelength limit of AVE
  (might need quantum corrections at high energies)
- The proper SPECTRAL structure of the noise (white vs. structured)
- How thermal noise feeds back on the running α (which has δ_strain corrections)
- Whether the mode integral cutoff at k_max = π is physically correct or if it
  should be something like π·α (restricted to long wavelengths for "real vacuum")

### Open research (later):
- **L1-B path** from doc 46_: decompose the K4 LC network into eigenmodes and
  derive the thermal occupation of each. Would give a proper spectral noise structure.

## 7. Summary

| Field | σ at T (natural units, lattice ℓ=m_e=c=ℏ=1) | σ at T = CMB (2.7K) | σ at T ~ 10⁸ K |
|---|---|---|---|
| V_inc per port | √(4πT/α) | 4·10⁻⁴ | 5.4 |
| u translation | √(T/(2π)) | 8.5·10⁻⁶ | 0.14 |
| ω rotation | 0.17·√T | 3.6·10⁻⁶ | 0.055 |

**Phase III-B recommended T value**: ~10⁸ K (in m_e c² units: kT ≈ 1.7·10⁻² → σ_ω ≈ 0.02).
This is comparable to my previous σ=0.01 placeholder — so Phase III-B ran at roughly
"10⁷-10⁸ K-equivalent" without knowing it. The next run should parameterize T
explicitly and report its value in physical units.

## 8. Engine integration

This derivation feeds Stage 2c of the parent plan (build `ThermalBath` source /
initialization). The `VacuumEngine3D.initialize_thermal(T)` method uses the
formulas in §5. The T parameter in Phase III-B's configuration matrix takes
values from {0, T_CMB ≈ 2.7K, T_pair ~ 10⁸ K} per the plan.
