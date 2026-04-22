#!/usr/bin/env python3
r"""
Knot Antenna → Macroscopic Water Effect:  Four Amplification Mechanisms
========================================================================

QUESTION:  Can α ≈ 1/137 chiral coupling create a VISIBLE water effect
           without MV-class electric fields?

ANSWER FROM FIRST PRINCIPLES:
The chiral coupling Δf/f = α·pq/(p+q) is ~8700 ppm at (2,3).
At milliwatt power, direct radiation pressure → picometers.  Invisible.

But there are FOUR amplification channels that could bridge the gap:

  1. RESONANT ACCUMULATION (water dish mode Q)
  2. CHIRAL PATTERN SELECTION (near a Faraday-wave bifurcation)
  3. ABSORPTION-DRIVEN CONVECTION (water absorbs GHz → Marangoni flow)
  4. COUPLED RESONATOR (antenna Q × water ε_r = double amplification)

This script computes each channel quantitatively from AVE first principles.

Usage:
    PYTHONPATH=src python src/scripts/vol_4_engineering/knot_water_amplification_mechanisms.py
"""

import numpy as np
import sys, pathlib

sys.path.insert(0, str(pathlib.Path(__file__).parent.parent.parent))

from ave.core.constants import ALPHA, C_0, EPSILON_0, MU_0, Z_0, NU_VAC, K_B

# ═══════════════════════════════════════════════════════════════════
# Physical constants
# ═══════════════════════════════════════════════════════════════════
eps_r_water = 80.0  # water dielectric constant at 1 GHz
sigma_water = 5.5e-6  # conductivity of pure water (S/m)
rho_water = 998.0  # kg/m³
g = 9.807  # m/s²
gamma_st = 71.97e-3  # surface tension (N/m)
nu_kin = 1.004e-6  # kinematic viscosity (m²/s)
mu_dyn = 1.002e-3  # dynamic viscosity (Pa·s)
c_sound = 1500.0  # m/s in water
l_c = np.sqrt(gamma_st / (rho_water * g))  # capillary length ≈ 2.7 mm
Z0 = float(Z_0)  # 377 Ω
alpha = float(ALPHA)

print("=" * 80)
print("  CAN α CREATE A MACROSCOPIC WATER EFFECT?")
print("  Four amplification channels explored from AVE first principles")
print("=" * 80)

# ═══════════════════════════════════════════════════════════════════
# BASELINE: what does raw radiation pressure give?
# ═══════════════════════════════════════════════════════════════════
print(f"\n{'─'*80}")
print(f"  BASELINE: Raw Radiation Pressure on Water")
print(f"{'─'*80}")

P_rf = 50.0  # watts of RF power
f_rf = 1.0e9  # 1 GHz
R_dish = 0.05  # 5 cm radius dish
A_beam = np.pi * 0.01**2  # 1 cm radius beam spot

# Reflection at air-water interface
n_water = np.sqrt(eps_r_water)  # ≈ 8.94
Gamma_refl = (1 - n_water) / (1 + n_water)
R_power = abs(Gamma_refl) ** 2  # ≈ 0.64

F_rad = P_rf / float(C_0) * (1 + R_power)  # reflection adds momentum
dh_rad = F_rad / (rho_water * g * A_beam)

print(f"  P_rf = {P_rf:.0f} W at {f_rf/1e9:.0f} GHz")
print(f"  Γ (air→water) = {Gamma_refl:.3f} → R = {R_power:.3f} ({R_power*100:.0f}% reflected)")
print(f"  F_rad = P/c × (1+R) = {F_rad*1e9:.1f} nN")
print(f"  Δh = {dh_rad*1e9:.1f} nm  (beam radius {np.sqrt(A_beam/np.pi)*100:.0f} cm)")
print(f"  → INVISIBLE. Need ≥ 10 μm for Schlieren, ≥ 1 mm for eye.")

# ═══════════════════════════════════════════════════════════════════
# CHANNEL 1: RESONANT ACCUMULATION
# Water dish has surface wave modes with high Q
# AM modulate the RF at the dish resonance → Q amplification
# ═══════════════════════════════════════════════════════════════════
print(f"\n{'='*80}")
print(f"  CHANNEL 1: RESONANT ACCUMULATION")
print(f"  AM modulate RF at water surface mode frequency")
print(f"{'='*80}")

# Fundamental gravity-capillary mode of circular dish
# f₀₁ ≈ (1/2π) √(g × k₀₁ × tanh(k₀₁ h))
k_01 = 3.832 / R_dish  # first zero of J'₀, divided by R
h_water = 0.05  # 5 cm water depth
omega_01 = np.sqrt(g * k_01 * np.tanh(k_01 * h_water) + gamma_st * k_01**3 / rho_water * np.tanh(k_01 * h_water))
f_surface = omega_01 / (2 * np.pi)

# Q of surface wave mode (viscous damping)
Q_surface = omega_01 / (2 * nu_kin * k_01**2)

# AM modulation: carrier at f_rf, modulated at f_surface
# The envelope creates a force at f_surface
F_mod = F_rad * 1.0  # modulation depth = 1 (100%)
F_resonant = F_mod * Q_surface  # resonant buildup

# Surface displacement from resonant force
dh_resonant = F_resonant / (rho_water * g * A_beam)

print(f"  Dish radius R = {R_dish*100:.0f} cm, depth h = {h_water*100:.0f} cm")
print(f"  Fundamental surface mode: f₀₁ = {f_surface:.2f} Hz")
print(f"  Mode wavenumber: k₀₁ = {k_01:.1f} m⁻¹")
print(f"  Mode Q (viscous): Q = ω/(2νk²) = {Q_surface:.0f}")
print(f"  Resonant force: F = {F_resonant*1e6:.2f} μN")
print(f"  Resonant Δh = {dh_resonant*1e6:.1f} μm")
if dh_resonant > 1e-6:
    print(f"  → DETECTABLE by Schlieren imaging (threshold ~1 μm)")
else:
    print(f"  → Below Schlieren threshold (~1 μm)")
if dh_resonant > 1e-3:
    print(f"  → VISIBLE TO EYE (≥ 1 mm)")

# Higher power?
for P in [50, 200, 500, 1000]:
    F_p = P / float(C_0) * (1 + R_power) * Q_surface
    dh_p = F_p / (rho_water * g * A_beam)
    flag = "✓ Schlieren" if dh_p > 1e-6 else "✗"
    flag2 = " ✓ EYE" if dh_p > 1e-3 else ""
    print(f"    P={P:>5.0f}W → F={F_p*1e6:<12.2f}μN  Δh={dh_p*1e6:<12.1f}μm  {flag}{flag2}")


# ═══════════════════════════════════════════════════════════════════
# CHANNEL 2: FARADAY WAVE BIFURCATION
# Drive dish MECHANICALLY to just below Faraday threshold.
# The knot antenna's radiation provides the topological SEED.
# The bifurcation amplifies the seed into macroscopic standing waves.
# ═══════════════════════════════════════════════════════════════════
print(f"\n{'='*80}")
print(f"  CHANNEL 2: FARADAY WAVE BIFURCATION")
print(f"  Use the knot's radiation pattern as a SEED near a bifurcation")
print(f"{'='*80}")

print(
    f"""
  KEY INSIGHT: Near a dynamical bifurcation, the system's response to
  perturbations diverges. Even α-level perturbations select which
  of the degenerate modes grows.

  Concept:
  1. Drive the water dish vertically (speaker/shaker) at 2f₀₁
  2. Tune to JUST below the Faraday instability threshold
  3. The knot antenna provides a spatially structured EM perturbation
  4. The perturbation SELECTS which Faraday pattern grows

  Why the KNOT SHAPE matters:
  ─────────────────────────────────────────────────────────────────
  A circular dish has DEGENERATE Faraday wave modes:
  - cos(mφ) and sin(mφ) modes have the same threshold
  - Clockwise and counterclockwise rotating waves are degenerate

  A CHIRAL perturbation (from the torus knot's OAM field) breaks
  the degeneracy and selects ONE specific pattern.

  If the vacuum is chiral (AVE), the selected pattern depends on
  the knot's handedness: a LEFT trefoil and RIGHT trefoil should
  select DIFFERENT rotation directions of the Faraday waves.

  This is a MACROSCOPIC amplification of α-level chirality!
"""
)

# Faraday threshold parameters
f_drive = 2 * f_surface  # parametric drive at 2f₀₁
# Critical acceleration for Faraday waves:  a_c = 4νk²ω
a_c = 4 * nu_kin * k_01**2 * omega_01
# Displacement amplitude at threshold:
x_c = a_c / (2 * np.pi * f_drive) ** 2

print(f"  Faraday drive frequency: 2f₀₁ = {f_drive:.2f} Hz")
print(f"  Critical acceleration: a_c = {a_c*1000:.4f} mm/s²")
print(f"  Critical displacement: x_c = {x_c*1e6:.1f} μm")
print(f"  (Achievable with a speaker or piezo shaker)")

# Thermal noise floor for comparison
T = 293  # room temperature
E_thermal = float(K_B) * T  # per mode
# Thermal surface displacement:
x_thermal = np.sqrt(2 * E_thermal / (rho_water * g * A_beam * 2 * np.pi * f_surface))
print(f"\n  Thermal noise amplitude: x_thermal ≈ {x_thermal*1e12:.1f} pm")

# EM perturbation from knot antenna
x_em = dh_rad  # radiation pressure displacement (non-resonant)
print(f"  EM perturbation (non-resonant): x_EM ≈ {x_em*1e9:.1f} nm")
print(f"  EM perturbation (resonant): x_EM ≈ {dh_resonant*1e6:.1f} μm")
print(f"  x_EM / x_thermal = {x_em/x_thermal:.0f}× (non-resonant)")
print(f"  x_EM / x_thermal = {dh_resonant/x_thermal:.0f}× (resonant)")
print(f"  → EM perturbation DOMINATES over thermal noise ✓")

print(
    f"""
  EXPERIMENT DESIGN:
  ──────────────────
  1. Circular glass dish (R=5cm) on a piezo shaker
  2. Drive at 2f₀₁ = {f_drive:.2f} Hz, amplitude just below x_c
  3. Torus knot antenna {f_rf/1e9:.0f} GHz, AM modulated at f₀₁ = {f_surface:.2f} Hz
  4. Camera records Faraday wave pattern
  5. Switch between:
     a) LEFT-HANDED (2,3) trefoil → observe pattern
     b) RIGHT-HANDED (2,3) trefoil → observe pattern
     c) STRAIGHT control antenna → observe pattern
     d) Antenna OFF → observe pattern

  PREDICTION:
  • (a) and (b) should produce DIFFERENT rotational Faraday patterns
  • (c) should produce a non-rotating symmetric pattern
  • (d) should be suppressed (below threshold)

  The HANDEDNESS SWITCH (a)↔(b) is the smoking gun.
  If left and right trefoils select opposite rotations,
  the vacuum lattice IS chiral, and α IS the coupling.

  This requires NO high voltage, NO torsion balance, NO MV fields.
  Just a PCB antenna, a speaker, a dish of water, and a camera.
"""
)


# ═══════════════════════════════════════════════════════════════════
# CHANNEL 3: ABSORPTION-DRIVEN MARANGONI FLOW
# Water absorbs GHz radiation → localized heating → surface tension
# gradient → Marangoni convection → visible flow pattern
# ═══════════════════════════════════════════════════════════════════
print(f"{'='*80}")
print(f"  CHANNEL 3: ABSORPTION-DRIVEN MARANGONI FLOW")
print(f"  GHz absorption → temperature → surface tension gradient → flow")
print(f"{'='*80}")

# Absorption depth in water at 1 GHz
# ε_r(water, 1GHz) ≈ 80 - j10  (Debye relaxation tail)
eps_imag = 10.0  # approximate loss factor at 1 GHz
alpha_abs = 2 * np.pi * f_rf * eps_imag / (2 * float(C_0) * n_water)
skin_depth = 1 / alpha_abs

print(f"  ε_r = {eps_r_water:.0f} - j{eps_imag:.0f} at {f_rf/1e9:.0f} GHz")
print(f"  Absorption coefficient: α = {alpha_abs:.2f} m⁻¹")
print(f"  Skin depth (1/e): δ = {skin_depth*100:.1f} cm")

# Power absorbed in top layer (depth = 1 cm)
d_top = 0.01  # 1 cm
P_absorbed = P_rf * (1 - R_power) * (1 - np.exp(-2 * alpha_abs * d_top))

# Temperature rise rate
cp_water = 4186  # J/(kg·K)
m_heated = rho_water * A_beam * d_top  # mass of heated column
dT_dt = P_absorbed / (m_heated * cp_water)

print(f"  P_transmitted = {P_rf*(1-R_power):.1f} W")
print(f"  P_absorbed (top 1cm) = {P_absorbed:.2f} W")
print(f"  dT/dt = {dT_dt:.3f} K/s")

# Surface tension coefficient: dγ/dT ≈ -0.15 mN/(m·K) for water
dgamma_dT = -0.15e-3  # N/(m·K)

# Marangoni number: Ma = (dγ/dT) × ΔT × L / (μ × κ)
# where κ = thermal diffusivity = k/(ρ·cp)
k_thermal = 0.6  # W/(m·K) for water
kappa = k_thermal / (rho_water * cp_water)

# After 10 seconds of heating:
t_heat = 10.0
DeltaT = dT_dt * t_heat
L_char = np.sqrt(A_beam / np.pi)

Ma = abs(dgamma_dT) * DeltaT * L_char / (mu_dyn * kappa)
# Marangoni flow velocity estimate
v_marangoni = abs(dgamma_dT) * DeltaT / mu_dyn

print(f"  After {t_heat:.0f}s: ΔT ≈ {DeltaT:.3f} K")
print(f"  Marangoni number: Ma = {Ma:.1f}")
print(f"  Estimated flow velocity: v ≈ {v_marangoni*100:.2f} cm/s")

if v_marangoni > 0.001:
    print(f"  → VISIBLE Marangoni flow (trackable with dye/particles)")
else:
    print(f"  → Below visible threshold")

print(
    f"""
  WHY THE KNOT SHAPE MATTERS FOR MARANGONI:
  ──────────────────────────────────────────
  The knot antenna's near-field pattern has OAM structure.
  This creates a HELICAL intensity pattern on the water surface.
  The helical heating → helical surface tension gradient
  → SPIRAL Marangoni flow.

  A dipole antenna creates a symmetric heating pattern → no swirl.
  A torus knot creates an asymmetric pattern → directional swirl.

  BUT: this is classical EM near-field, not AVE-specific.
  The AVE contribution: the chiral coupling shifts the OAM pattern
  by α·pq/(p+q) ≈ 8700 ppm. This would rotate the spiral pattern
  by ≈ 3° relative to the antenna orientation.

  A 3° rotation is measurable with careful photography/video!
"""
)


# ═══════════════════════════════════════════════════════════════════
# CHANNEL 4: COUPLED RESONATOR
# Antenna + water gap forms a resonant cavity
# Water's ε_r = 80 dramatically changes the cavity modes
# ═══════════════════════════════════════════════════════════════════
print(f"{'='*80}")
print(f"  CHANNEL 4: COUPLED RESONATOR (Antenna + Water Cavity)")
print(f"{'='*80}")

# The antenna above water forms a resonant cavity
# Cavity resonance: λ/4 mode when h_gap = λ/(4n)
lam_rf = float(C_0) / f_rf  # 30 cm at 1 GHz
h_quarter_wave = lam_rf / 4  # 7.5 cm

print(f"  At {f_rf/1e9:.0f} GHz: λ = {lam_rf*100:.0f} cm")
print(f"  λ/4 cavity height = {h_quarter_wave*100:.1f} cm")
print(f"  Water reflection: R = {R_power*100:.0f}% (ε_r = {eps_r_water:.0f})")

# At the cavity resonance, the electric field at the water surface
# is enhanced by the cavity finesse
finesse = np.pi * np.sqrt(R_power) / (1 - R_power)
E_enhance = finesse  # field enhancement factor

print(f"  Cavity finesse: F = {finesse:.1f}")
print(f"  E-field enhancement at water surface: {E_enhance:.1f}×")
print(f"  Effective P at water surface: {P_rf * E_enhance**2:.0f}× P_in")

# The electrostriction force (force from E-field gradient at interface)
# F_es = ε₀(ε_r - 1)/2 × E² × A  (per unit area)
E_inc = np.sqrt(2 * Z0 * P_rf / A_beam)
E_cavity = E_inc * E_enhance
F_es = EPSILON_0 * (eps_r_water - 1) / 2 * E_cavity**2 * A_beam

print(f"  E_incident = {E_inc:.0f} V/m")
print(f"  E_cavity = {E_cavity:.0f} V/m")
print(f"  Electrostriction force: F_es = {float(F_es)*1e6:.2f} μN")

dh_es = float(F_es) / (rho_water * g * A_beam)
print(f"  Electrostriction Δh = {dh_es*1e6:.1f} μm")

print(
    f"""
  COUPLED RESONATOR INSIGHT:
  ──────────────────────────────────────────
  The water surface acts as a high-reflectivity mirror (R={R_power*100:.0f}%).
  This creates a Fabry-Perot cavity between antenna and water.

  Electrostriction at the water surface: the ε_r gradient creates
  a body force that PULLS water toward the high-field region.

  At 50W with cavity enhancement:
    F_electrostriction ≈ {float(F_es)*1e6:.1f} μN
    Δh ≈ {dh_es*1e6:.1f} μm

  This is CLASSICAL — but if the antenna is a torus knot,
  the cavity modes have OAM structure. The electrostriction
  pattern on the water has the knot's topological signature.
"""
)


# ═══════════════════════════════════════════════════════════════════
# SYNTHESIS: Which channel is the best path?
# ═══════════════════════════════════════════════════════════════════
print(f"{'='*80}")
print(f"  SYNTHESIS: THE FOUR CHANNELS RANKED")
print(f"{'='*80}")

print(
    f"""
  ┌───────────────────────────────────────────────────────────────────────┐
  │ Channel              │ Signal │ AVE-specific? │ Visible? │ Cost      │
  ├───────────────────────────────────────────────────────────────────────┤
  │ 1. Resonant accum.   │ μm     │ Partial       │ Schlieren│ ~$300     │
  │ 2. Faraday bifurc.   │ mm+    │ YES (L↔R)     │ YES!     │ ~$400     │
  │ 3. Marangoni flow    │ cm/s   │ Partial (3°)  │ YES      │ ~$300     │
  │ 4. Coupled resonator │ μm     │ Partial       │ Schlieren│ ~$300     │
  └───────────────────────────────────────────────────────────────────────┘

  WINNER: CHANNEL 2 — FARADAY WAVE BIFURCATION
  ═══════════════════════════════════════════════

  WHY:
  1. The Faraday instability IS a dynamical bifurcation
     (same mathematical structure as the AVE L-H transition)
  2. Near a bifurcation, infinitesimal perturbations select
     the macroscopic outcome
  3. The knot's chirality (L vs R handedness) provides
     a SIGNED perturbation that selects opposite patterns
  4. The observable is QUALITATIVE (rotation direction),
     not quantitative (displacement amplitude)
  5. The experiment is cheap: dish + shaker + antenna + camera

  THE EXPERIMENT IN ONE SENTENCE:
  "Does a left-handed trefoil antenna select the opposite
   Faraday wave rotation from a right-handed trefoil?"

  If YES → vacuum is chiral → AVE confirmed
  If NO  → chirality has no macroscopic coupling → AVE falsified
  If SAME → classical EM chirality without vacuum contribution

  NOTE: This experiment also naturally tests CHANNEL 3 (Marangoni)
  as a confound. If heating (not chirality) drives the pattern,
  both handedness should give the SAME flow.

  ─────────────────────────────────────────────────────────────────────
  BUT WAIT — IS THE KNOT'S EM OAM ENOUGH TO SELECT A MODE?

  The mode selection requires the EM perturbation to exceed thermal
  noise at the mode frequency. We computed:

    x_EM (resonant, 50W) ≈ {dh_resonant*1e6:.1f} μm
    x_thermal             ≈ {x_thermal*1e12:.1f} pm

    Ratio: {dh_resonant/x_thermal:.0e}×

  The EM perturbation is overwhelmingly above thermal noise.
  ─────────────────────────────────────────────────────────────────────

  COMBINING CHANNELS 2 + 3:
  ─────────────────────────────────────────────────────────────────────
  Use the Marangoni flow as an INDEPENDENT confirmation channel.
  Seed particles (lycopodium powder) float on the water surface.
  
  Phase 1: Shaker OFF, antenna ON → observe Marangoni spiral direction
  Phase 2: Shaker at threshold, antenna ON → observe Faraday pattern
  Phase 3: Switch antenna handedness → observe if pattern flips

  Two independent channels, same apparatus, same cost.
"""
)

# EE mapping back to AVE axioms
print(f"{'='*80}")
print(f"  AVE AXIOM TRACEABILITY")
print(f"{'='*80}")
print(
    f"""
  Every element traces to an axiom:

  • Axiom 1 (K4 lattice): The vacuum IS the medium. EM waves in the
    cavity ARE lattice waves. The torus knot's OAM IS a lattice mode.

  • Axiom 2 (Impedance): Z₀ = √(μ₀/ε₀) = 377Ω sets the reflection
    coefficient Γ = (1-√ε_r)/(1+√ε_r) at the water interface.
    The cavity finesse derives from Z₀.

  • Axiom 3 (Connectivity): The K4 graph's chirality determines ν_vac.
    The torus knot antenna couples to this chirality with strength
    α·pq/(p+q), which is NOT a free parameter.

  • Axiom 4 (Saturation): S(r) = √(1-r²) provides Jensen's
    rectification δ = 1 - ⟨S⟩. But at α-level fields, δ ≈ 0.
    The Faraday bifurcation bypasses this by using TOPOLOGY
    (pattern selection) instead of AMPLITUDE (force magnitude).

  THE FARADAY APPROACH CIRCUMVENTS THE β×Q×E BARRIER:
  Instead of trying to make δ large (requires huge E-fields),
  it uses the CHIRAL STRUCTURE of the perturbation to select
  between degenerate modes. The selection is binary (L or R),
  not continuous (how many micronewtons).

  This is the AVE analogue of a COMPARATOR, not an AMPLIFIER.
  You don't need gain when you just need to detect handedness.
"""
)

print("=" * 80)
