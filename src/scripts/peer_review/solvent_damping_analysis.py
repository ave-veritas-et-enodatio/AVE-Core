"""
Solvent Damping Noise-Floor Analysis
======================================

Gap 3A: Formulate cytosol noise as a reactive boundary load on the
         protein folding S11 engine. Quantify whether the thermal
         solvent bath degrades the predicted folding S11 minimum.

PHYSICS:
    In the AVE framework, the aqueous cytosol surrounding a folding
    protein is a broadband thermal noise source at body temperature
    (T = 310 K). This bath couples to the protein backbone at every
    exposed Calpha node via hydrogen-bond mediated shunt admittance.

    The question: does the solvent noise floor corrupt the S11
    impedance matching that drives folding, or is the folded state's
    S11 minimum stable against thermal loading?

    Three competing effects:
    1. DAMPING: Solvent adds resistive (real) admittance -> broadens
       resonances, reduces Q -> degrades S11 selectivity
    2. MASS LOADING: Water molecules add reactive (imaginary) admittance
       -> shifts resonant frequencies -> could detune the fold
    3. HYDROGEN BOND COUPLING: Solvent H-bonds act as stubs connecting
       the backbone to the thermal bath -> increases coupling to the
       noise floor BUT also provides the driving signal

    The analysis computes the S11 sensitivity to solvent loading as a
    function of shunt admittance magnitude.

FRAMING (framework-level proposal): the min-|S11|^2 impedance-folding
mechanism this analysis rests on is framework-level; the uniqueness of the
folding minimum is conjectured, not yet demonstrated by a closed derivation.
This figure characterises the solvent boundary load WITHIN that framework; it
is not a folding-feasibility verdict.

Run: PYTHONPATH=src python src/scripts/peer_review/solvent_damping_analysis.py
"""

import matplotlib
import numpy as np

from ave.core.constants import C_0, K_B, M_U, XI_TOPO, e_charge
from ave.solvers.transmission_line import build_nodal_y_matrix, s11_from_y_matrix
from ave.viz import style
from ave_path_util import manuscript_path

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

# =================================================================
# DERIVED SOLVENT CONSTANTS (all from axioms + water properties)
# =================================================================

# Body temperature
T_BODY = 310.0  # K

# Wien peak frequency at body temperature
# lambda_peak = b/T where b = 2898 um.K -> f_peak = c/lambda_peak
WIEN_B = 2.898e-3  # m.K
F_WIEN = C_0 * T_BODY / WIEN_B  # ~ 3.2e13 Hz ~ 32 THz
OMEGA_WIEN = 2 * np.pi * F_WIEN

# Thermal energy per mode
KT = K_B * T_BODY  # ~ 4.28e-21 J ~ 26.7 meV

# H-bond energy (from Op4 derivation, Vol 5 Ch 2)
E_HB_EV = 0.2158
E_HB_J = E_HB_EV * e_charge

# Number of solvent H-bonds per exposed Calpha node
N_HB_PER_NODE = 3.0

# H-bond spring constant (from Op4 curvature at d_HB = 1.754 A)
D_HB = 1.754e-10  # m
K_HB_SPRING = E_HB_J / D_HB**2  # N/m

# Solvent damping coefficient (Stokes-like friction for a Calpha node)
# gamma = 6 pi eta r where eta = 6.9e-4 Pa.s (cytosol at 37 C), r ~ 1.5 A
ETA_CYTOSOL = 6.9e-4  # Pa.s (water at 37 C)
R_CA = 1.5e-10  # m
GAMMA_STOKES = 6 * np.pi * ETA_CYTOSOL * R_CA  # friction coefficient

# Convert mechanical damping to electrical admittance via xi_topo^2
G_SOLVENT_PER_HB = GAMMA_STOKES * XI_TOPO**2
K_HB_ELECTRICAL = K_HB_SPRING * XI_TOPO**2

# Backbone impedance (reference, from Vol 5 amino acid analysis)
M_C = 12.011 * M_U  # Carbon mass [kg] (M_U from ave.core.constants)
K_CN = 461.0  # C-N force constant [N/m]
L_C = M_C / XI_TOPO**2
C_CN = XI_TOPO**2 / K_CN
Z_BACKBONE = np.sqrt(L_C / C_CN)
F_BACKBONE = 1 / (2 * np.pi * np.sqrt(L_C * C_CN))

# =================================================================
# CONTEXT PRINT
# =================================================================

print("=" * 80)
print("SOLVENT DAMPING NOISE-FLOOR ANALYSIS")
print("Gap 3A: Cytosol as Reactive Boundary Load on Protein S11")
print("Framework-level proposal — folding-minimum uniqueness conjectured")
print("=" * 80)

print(f"  T_body = {T_BODY:.0f} K   f_Wien = {F_WIEN/1e12:.1f} THz   kT = {KT/e_charge*1e3:.1f} meV")
print(f"  E_HB = {E_HB_EV:.4f} eV   kT/E_HB = {KT/E_HB_J:.4f}")
print(f"  eta = {ETA_CYTOSOL:.1e} Pa.s   gamma_Stokes = {GAMMA_STOKES:.2e} kg/s   n_HB = {N_HB_PER_NODE:.0f}")
print(f"  Z_backbone = {Z_BACKBONE:.4f} Ohm   f_backbone = {F_BACKBONE/1e12:.1f} THz")

# =================================================================
# SENSITIVITY SWEEP: S11 vs. solvent loading
# =================================================================

N_RESIDUES = 10
omegas = np.linspace(0.1, 5.0, 500)  # normalized frequency
Z_seg = np.ones(N_RESIDUES - 1) * 1.0  # normalized impedance
solvent_fractions = [0.0, 0.001, 0.01, 0.05, 0.1, 0.5, 1.0]

print("\n  S11 sensitivity to solvent loading:")
print(f"  {'Y_solv/Y_bb':>12s} {'min|S11|^2':>12s} {'delta':>10s} {'Q_eff':>8s}")
print("  " + "-" * 50)

s11_results = {}
s11_min_vacuum = None

for y_frac in solvent_fractions:
    s11_sweep = []
    for omega in omegas:
        gamma_l = 0.01 + 1j * omega  # small loss + propagation
        backbone_y = []
        for i in range(N_RESIDUES - 1):
            y = 1.0 / (Z_seg[i] * np.sinh(gamma_l) + 1e-12)
            backbone_y.append(-y)
        y_solv = y_frac * (0.3 + 0.7j * omega)  # dissipative + reactive
        self_y = [y_solv] * N_RESIDUES
        Y = build_nodal_y_matrix(N_RESIDUES, backbone_y, self_y=self_y)
        s11 = s11_from_y_matrix(Y, port=0, Y0=1.0)
        s11_sweep.append(float(np.abs(s11) ** 2))

    s11_sweep = np.array(s11_sweep)
    s11_results[y_frac] = s11_sweep
    min_s11 = np.min(s11_sweep)
    min_idx = np.argmin(s11_sweep)
    omega_min = omegas[min_idx]

    if y_frac == 0.0:
        s11_min_vacuum = min_s11
        delta = 0.0
    else:
        delta = min_s11 - s11_min_vacuum

    half_power = min_s11 + 0.5 * (1.0 - min_s11)
    bandwidth_mask = s11_sweep < half_power
    if np.sum(bandwidth_mask) > 1:
        bw_indices = np.where(bandwidth_mask)[0]
        bw = omegas[bw_indices[-1]] - omegas[bw_indices[0]]
        Q_eff = omega_min / max(bw, 1e-6)
    else:
        Q_eff = float("inf")

    print(f"  {y_frac:12.4f} {min_s11:12.6f} {delta:+10.6f} {Q_eff:8.1f}")

# =================================================================
# PHYSICAL LOADING RATIO
# =================================================================

Y_bb_typical = 1.0 / Z_BACKBONE
Y_solvent_actual = N_HB_PER_NODE * np.sqrt(
    G_SOLVENT_PER_HB**2 + (K_HB_ELECTRICAL / (2 * np.pi * F_BACKBONE)) ** 2
)
LOADING_RATIO = Y_solvent_actual / Y_bb_typical

print(f"\n  Physical solvent loading ratio Y_solv/Y_bb = {LOADING_RATIO:.2e}")
print(f"  -> solvent shunt is {LOADING_RATIO*100:.4f}% of backbone admittance")

# =================================================================
# GENERATE PUBLICATION FIGURE (white house style, Okabe-Ito)
# =================================================================
print("  Generating publication figure...")

style.apply()
fig, axes = plt.subplots(1, 3, figsize=style.figsize("wide"))

# Panel 1: S11 vs frequency for different solvent loadings
ax = axes[0]
cmap = plt.cm.viridis
for i, y_frac in enumerate(solvent_fractions):
    label = f"$Y_{{solv}}$ = {y_frac:.3f}" if y_frac > 0 else "Vacuum (no solvent)"
    ax.plot(
        omegas,
        10 * np.log10(s11_results[y_frac] + 1e-30),
        color=cmap(i / max(len(solvent_fractions) - 1, 1)),
        lw=1.4,
        label=label,
    )
ax.set_xlabel(style.axis_label("Normalized frequency", r"\omega/\omega_0", ""))
ax.set_ylabel(style.axis_label("Reflected power", r"|S_{11}|^2", "dB"))
ax.set_ylim([-40, 5])
style.legend(ax, where="below", ncol=2, fontsize=7)

# Panel 2: S11 minimum vs loading fraction
ax = axes[1]
mins = [float(np.min(s11_results[y])) for y in solvent_fractions]
ax.semilogy(solvent_fractions, mins, "o-", color=style.COLORS["ave"],
            lw=1.8, markersize=6)
ax.axhline(mins[0], color=style.COLORS["muted"], ls=":", lw=1.2,
           label="Vacuum baseline")
ax.axvline(LOADING_RATIO, color=style.COLORS["comparison"], ls="--", lw=1.4,
           label=f"Physical loading ({LOADING_RATIO:.1e})")
ax.set_xlabel(style.axis_label("Solvent loading", r"Y_{solv}/Y_{bb}", ""))
ax.set_ylabel(style.axis_label("Folding minimum", r"\min|S_{11}|^2", ""))
style.legend(ax, where="below", ncol=1, fontsize=7)

# Panel 3: Impedance mismatch
ax = axes[2]
freq_range = np.logspace(10, 14, 200)  # Hz
Z_bb = Z_BACKBONE * np.ones_like(freq_range)
Z_solv = 1.0 / (
    N_HB_PER_NODE * np.sqrt(
        G_SOLVENT_PER_HB**2 + (K_HB_ELECTRICAL / (2 * np.pi * freq_range)) ** 2
    ) + 1e-30
)
ax.loglog(freq_range / 1e12, Z_bb, "--", color=style.COLORS["accent"], lw=1.8,
          label=f"$Z_{{backbone}}$ = {Z_BACKBONE:.1f} $\\Omega$")
ax.loglog(freq_range / 1e12, Z_solv, "-", color=style.COLORS["ave"], lw=1.8,
          label="$Z_{solvent}(f)$")
ax.fill_between(freq_range / 1e12, Z_bb, Z_solv, alpha=0.08,
                color=style.COLORS["muted"])
ax.axvline(F_BACKBONE / 1e12, color=style.COLORS["muted"], ls=":", lw=1.2,
           label=f"$f_{{backbone}}$ = {F_BACKBONE/1e12:.1f} THz")
ax.set_xlabel(style.axis_label("Frequency", "f", "THz"))
ax.set_ylabel(style.axis_label("Impedance", "Z", r"$\Omega$"))
style.legend(ax, where="below", ncol=1, fontsize=7)

# Neutral, hedged framework note (plain datasheet prose, no internal grading
# tokens) — replaces the old fourth verdict/feasibility panel.
fig.text(
    0.5,
    -0.06,
    "Framework-level proposal: the minimum-$|S_{11}|^2$ impedance-folding "
    "mechanism is conjectured, not yet demonstrated by a closed derivation.",
    ha="center",
    va="top",
    fontsize=8,
    color=style.COLORS["muted"],
)

out_path = manuscript_path("vol_5_biology", "figures", "solvent_damping_analysis.png")
style.save(fig, out_path, formats=("png",))
plt.close(fig)
print(f"  -> Saved: {out_path}")
print("\n  Solvent damping analysis complete (framework-level characterisation).")
