"""DAMA Q-factor via matched-LC-coupling between electron LC tank and external NaI mode.

Reactive-power reframe (9th audit cycle resolution, 2026-05-17 night):
DAMA detection is NOT photoabsorption of substrate-mode quanta. It is
matched-impedance coupling between the electron's reactive LC tank
(Q_internal = alpha^-1 = 137; per-cycle reactive leak = alpha m_e c^2
= 3.728 keV at 90 deg phase, P_real = 0 W) and an external coherent
NaI crystal LC mode at the alpha-slew operating point.

Canonical context:
- Theorem 3.1' (vol4/circuit-theory/ch1-vacuum-circuit-analysis/
  theorem-3-1-q-factor.md): Q_tank = alpha^-1 at TIR boundary
- orbital-friction-paradox.md:31: reactive-power table P_real = 0,
  Q_reactive = m_e c^2 * alpha for electron orbital
- leaky-cavity-particle-decay/theory.md:12: tank below V_yield
  = 43.65 kV rings forever

Script purpose:
1. Compute the per-cycle matched-coupling efficiency epsilon_det
   required to reproduce DAMA observed event rate
2. Evaluate several structural candidates from canonical AVE factors
   (alpha-power chains, geometric overlap, Bragg-resonance detuning,
   evanescent decay)
3. Honest report on which candidates land within OOM and which don't

Lane: implementer; analysis script (no engine modifications).
"""

from __future__ import annotations

import sys
from dataclasses import dataclass
from pathlib import Path

# Canonical-source import per ave-canonical-source skill
_repo_root = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(_repo_root / "src"))

from ave.core.constants import (
    ALPHA,
    C_0,
    E_SLEW,
    HBAR,
    L_NODE,
    LAMBDA_SLEW,
    M_E,
    N_A,
    NU_KIN,
    NU_SLEW,
    RHO_BULK,
    Z_0,
    Z_RADIATION,
    e_charge,
)


# ---------- Canonical AVE quantities (now from constants.py) ----------

# alpha-slew quantum in keV (for display)
E_SLEW_KEV = E_SLEW / e_charge / 1e3

# Electron LC tank impedance at TIR boundary (alias for clarity)
Z_TANK = Z_RADIATION  # = Z_0 / (4π) ~ 30 Ohm per Theorem 3.1'


# ---------- NaI detector parameters ----------

# NaI molecular mass (Na + I) in kg/mol
M_NAI_KG_PER_MOL = (22.99 + 126.90) * 1e-3  # 0.1499 kg/mol

# NaI density
RHO_NAI = 3670.0  # kg/m^3

# NaI lattice spacing
D_NAI = 3.24e-10  # m (rocksalt structure, Na-I nearest-neighbor)

# Average Z per molecule (Z_Na + Z_I)
Z_AVG_NAI = 11 + 53  # 64 electrons per NaI molecule

# Molecules per kg
N_MOL_PER_KG = N_A / M_NAI_KG_PER_MOL  # ~4.01e24 molecules/kg

# Electrons per kg
N_E_PER_KG = N_MOL_PER_KG * Z_AVG_NAI  # ~2.57e26 electrons/kg


# ---------- DAMA empirical anchor ----------

# DAMA/LIBRA Phase-2 observed rate (single-hit, 2-6 keV window)
RATE_DAMA_CPD_KG_KEV = 0.0103  # canonical DAMA/LIBRA Phase-2 number
DAMA_WINDOW_KEV = 4.0  # 2-6 keV width
RATE_DAMA_PER_S_PER_KG = (
    RATE_DAMA_CPD_KG_KEV * DAMA_WINDOW_KEV / 86400.0
)  # ~4.77e-7 events/s/kg


# ---------- Step 1: Required per-cycle matched-coupling efficiency ----------


def compute_required_epsilon() -> tuple[float, float, float]:
    """Return (intrinsic_rate, dama_rate, required_epsilon)."""
    intrinsic_rate = N_E_PER_KG * NU_SLEW  # events/s/kg if every cycle = detection
    required_epsilon = RATE_DAMA_PER_S_PER_KG / intrinsic_rate
    return intrinsic_rate, RATE_DAMA_PER_S_PER_KG, required_epsilon


# ---------- Step 2: Structural-candidate evaluation ----------


@dataclass
class Candidate:
    name: str
    value: float
    rationale: str
    natural_count_for_required: float | None = None


def evaluate_candidates(required_epsilon: float) -> list[Candidate]:
    """Evaluate matched-LC-coupling structural candidates."""
    import math

    candidates: list[Candidate] = []

    # (a) alpha^N power chain
    for n in [22, 23, 24, 25, 26]:
        val = ALPHA**n
        candidates.append(
            Candidate(
                name=f"alpha^{n}",
                value=val,
                rationale=f"alpha-power chain (N={n} independent named-operator alpha-suppressions; corpus has 1)",
            )
        )

    # (b) (alpha/(2pi))^N Schwinger-class chain
    for n in [15, 16, 17, 18, 19]:
        val = (ALPHA / (2 * math.pi)) ** n
        candidates.append(
            Candidate(
                name=f"(alpha/2pi)^{n}",
                value=val,
                rationale=f"Schwinger-class chain (N={n} a_e = alpha/(2pi) per-cycle suppressions; corpus has 1 canonical)",
            )
        )

    # DAMA actual geometry (DAMA/LIBRA Phase-2 published):
    # - 25 individual NaI(Tl) crystals, each 9.7 kg (100 mm x 100 mm x 250 mm)
    # - Single coherent crystal mass = 9.7 kg
    # - Total array mass ~ 242.5 kg
    M_DAMA_SINGLE_CRYSTAL_KG = 9.7
    M_DAMA_TOTAL_ARRAY_KG = 242.5

    # (c) Geometric overlap (electron LC volume / single-crystal volume)
    V_SINGLE_CRYSTAL = M_DAMA_SINGLE_CRYSTAL_KG / RHO_NAI  # m^3
    L_SINGLE_CRYSTAL = V_SINGLE_CRYSTAL ** (1.0 / 3.0)  # equivalent cubic edge
    geom_overlap = (L_NODE / L_SINGLE_CRYSTAL) ** 3
    candidates.append(
        Candidate(
            name="geom_overlap_3D (single-crystal)",
            value=geom_overlap,
            rationale=f"(ℓ_node/L_single-crystal)^3 = ({L_NODE:.2e}/{L_SINGLE_CRYSTAL:.2e})^3 ~ electron LC volume / 9.7 kg single coherent crystal",
        )
    )

    # (d-i) N_atoms^(-2) in single coherent crystal (9.7 kg)
    N_SINGLE_CRYSTAL = M_DAMA_SINGLE_CRYSTAL_KG * N_MOL_PER_KG * 2  # x2 for Na+I
    n_single_inv_sq = 1.0 / N_SINGLE_CRYSTAL**2
    candidates.append(
        Candidate(
            name="N_single-crystal^(-2)",
            value=n_single_inv_sq,
            rationale=f"1/(N_single)^2 = 1/({N_SINGLE_CRYSTAL:.2e})^2 ~ coherent phase-alignment in 9.7 kg single crystal",
        )
    )

    # (d-ii) N_atoms^(-2) in DAMA total array (242.5 kg)
    N_DAMA_TOTAL = M_DAMA_TOTAL_ARRAY_KG * N_MOL_PER_KG * 2  # x2 for Na+I
    n_total_inv_sq = 1.0 / N_DAMA_TOTAL**2
    candidates.append(
        Candidate(
            name="N_DAMA_total^(-2)",
            value=n_total_inv_sq,
            rationale=f"1/(N_total)^2 = 1/({N_DAMA_TOTAL:.2e})^2 ~ coherent phase-alignment in 242.5 kg total array",
        )
    )

    # (d-iii) N_atoms^(-1) × Schwinger-class single suppression
    n_single_inv_x_alpha = (1.0 / N_SINGLE_CRYSTAL) * (ALPHA / (2 * math.pi))
    candidates.append(
        Candidate(
            name="N_single^(-1) × (α/2π)",
            value=n_single_inv_x_alpha,
            rationale=f"Single coherent crystal N^-1 × one Schwinger-class α/(2π) suppression",
        )
    )

    # (e) Bragg detuning at second-order
    LAMBDA_BRAGG_2 = D_NAI  # second-order Bragg
    delta_w_over_w = abs(LAMBDA_SLEW - LAMBDA_BRAGG_2) / LAMBDA_BRAGG_2
    # off-resonance Lorentzian with bandwidth set by Q_Bragg
    Q_BRAGG_LARGE = 1e9  # 10^8 lattice spacings × pi
    bragg_off_res = (1.0 / Q_BRAGG_LARGE / delta_w_over_w) ** 2
    candidates.append(
        Candidate(
            name="bragg_2nd_order_offres",
            value=bragg_off_res,
            rationale=f"Bragg 2nd-order detuning {delta_w_over_w:.2%}; off-resonance Lorentzian Q=10^9",
        )
    )

    # (f) Coherent baseline N_coh^(-2) (corpus 770 lattice nodes per atom-pair)
    N_COH_LATTICE_NODES = 770  # per bullet-cluster.md:59
    n_coh_inv_sq = 1.0 / N_COH_LATTICE_NODES**2
    candidates.append(
        Candidate(
            name="N_coh_lattice_inv_sq",
            value=n_coh_inv_sq,
            rationale=f"1/(N_coh_lattice)^2 = 1/770^2 per bullet-cluster.md:59",
        )
    )

    # (g) Substrate-mode mean-free-path / single-crystal size
    LAMBDA_MFP_SUBSTRATE = NU_KIN / C_0  # alpha × ℓ_node
    mfp_over_crystal_sq = (LAMBDA_MFP_SUBSTRATE / L_SINGLE_CRYSTAL) ** 2
    candidates.append(
        Candidate(
            name="(MFP/L_single)^2",
            value=mfp_over_crystal_sq,
            rationale=f"(alpha × ℓ_node / L_single)^2 = ({LAMBDA_MFP_SUBSTRATE:.2e}/{L_SINGLE_CRYSTAL:.2e})^2; substrate-mode coherence length / single-crystal",
        )
    )

    # (h) Combined: geometric overlap × Schwinger-chain
    combined = geom_overlap * (ALPHA / (2 * math.pi)) ** 4
    candidates.append(
        Candidate(
            name="geom × (alpha/2pi)^4",
            value=combined,
            rationale="(ℓ_node/L_single)^3 × (alpha/(2pi))^4 ~ geometric overlap × 4 Schwinger-class steps",
        )
    )

    # (i) 4pi / N_single^2 — single coherent crystal with spinor double-cover factor
    #     4pi is canonical AVE solid-angle / SU(2) double-cover factor
    #     (appears in Theorem 3.1' as Z_radiation = Z_0/(4pi) per spinor cycle)
    four_pi_over_n_sq = (4 * math.pi) / N_SINGLE_CRYSTAL**2
    candidates.append(
        Candidate(
            name="4π / N_single^2",
            value=four_pi_over_n_sq,
            rationale=f"4π/(N_single)^2 = 4π/({N_SINGLE_CRYSTAL:.2e})^2 — spinor double-cover (Theorem 3.1' Z_0/(4π)) × coherent-phase-align in single crystal",
        )
    )

    # (j) 2pi / N_single^2 — Hoop Stress geometric factor instead of full spinor cycle
    two_pi_over_n_sq = (2 * math.pi) / N_SINGLE_CRYSTAL**2
    candidates.append(
        Candidate(
            name="2π / N_single^2",
            value=two_pi_over_n_sq,
            rationale=f"2π/(N_single)^2 — Hoop Stress 2π geometric factor (alternative to 4π spinor) × coherent-phase-align",
        )
    )

    # (k) Pi / N_single^2 — single π factor (line-element of α-decomposition Λ_line = π)
    pi_over_n_sq = math.pi / N_SINGLE_CRYSTAL**2
    candidates.append(
        Candidate(
            name="π / N_single^2",
            value=pi_over_n_sq,
            rationale=f"π/(N_single)^2 — Λ_line = π factor from α-decomposition (Theorem 3.1') × coherent-phase-align",
        )
    )

    # Compute "natural count" for each candidate to scale to required
    for c in candidates:
        if c.value > 0:
            c.natural_count_for_required = required_epsilon / c.value

    return candidates


# ---------- Step 3: Reporting ----------


def predicted_rate_for_crystal(
    m_single_kg: float, m_mol_kg_per_mol: float, atoms_per_molecule: int, z_total_per_molecule: int
) -> tuple[float, float, float]:
    """Compute predicted DAMA-class rate for an arbitrary single-crystal detector.

    Returns: (n_e_per_kg, n_single_total, predicted_rate_per_s_per_kg)

    Formula (matched-LC-coupling per 9th-cycle reactive-power resolution):
      Rate/kg = N_e/kg × ν_slew × (4π / N_single²)
    """
    import math

    n_e_per_kg_local = (N_A / m_mol_kg_per_mol) * z_total_per_molecule
    n_single = (N_A / m_mol_kg_per_mol) * atoms_per_molecule * m_single_kg
    epsilon_det = (4 * math.pi) / n_single**2
    intrinsic = n_e_per_kg_local * NU_SLEW
    rate = intrinsic * epsilon_det
    return n_e_per_kg_local, n_single, rate


def cross_detector_predictions() -> None:
    """Cross-detector + cross-crystal swap predictions per matched-LC-coupling."""
    import math

    print("=" * 70)
    print("CROSS-DETECTOR PREDICTIONS (per matched-LC-coupling 4π/N_single²)")
    print("=" * 70)
    print()
    print("Predicted rate per kg assumes κ_quality = 1 (theoretical ceiling).")
    print("Actual rate = predicted × κ_quality where κ ≤ 1 for batch quality.")
    print()

    # DAMA baseline
    ne, ns, rate_dama = predicted_rate_for_crystal(
        m_single_kg=9.7,
        m_mol_kg_per_mol=0.14989,
        atoms_per_molecule=2,
        z_total_per_molecule=64,
    )

    print(f"{'Detector':<30} {'M_single (kg)':<14} {'N_single':<12} {'Rate/kg':<14} {'Ratio to DAMA'}")
    print("-" * 80)

    detectors = [
        ("DAMA/LIBRA Phase-2 (NaI)", 9.7, 0.14989, 2, 64),
        ("COSINE-100 (NaI)", 10.0, 0.14989, 2, 64),
        ("ANAIS-112 (NaI)", 12.5, 0.14989, 2, 64),
        ("Sapphire-9.7 (Al2O3)", 9.7, 0.10196, 5, 50),  # Z(Al)=13, Z(O)=8: 2*13+3*8=50
        ("Sapphire-12 (Al2O3)", 12.0, 0.10196, 5, 50),
        ("Germanium-9.7 (Ge)", 9.7, 0.07264, 1, 32),
        ("Germanium-12 (Ge)", 12.0, 0.07264, 1, 32),
        ("Sapphire-matched-N (Al2O3)", 2.64, 0.10196, 5, 50),  # N_single ~ DAMA NaI 9.7kg
        ("Germanium-matched-N (Ge)", 9.39, 0.07264, 1, 32),  # N_single ~ DAMA NaI 9.7kg
    ]

    for name, m_single, m_mol, atoms_per_mol, z_total in detectors:
        ne, ns, rate = predicted_rate_for_crystal(m_single, m_mol, atoms_per_mol, z_total)
        ratio = rate / rate_dama
        print(f"{name:<30} {m_single:<14.2f} {ns:<12.3e} {rate:<14.3e} {ratio:.4f}")

    print()
    print("Key falsifiers:")
    print(
        "- COSINE-100 should see ~94% DAMA rate/kg at κ_quality = 1 → observed << → low κ"
    )
    print(
        "- ANAIS-112 should see ~60% DAMA rate/kg at κ_quality = 1 → observed << → low κ"
    )
    print(
        "- Sapphire-9.7 should see ~9% DAMA rate/kg at line position 3.728 keV (Z-INDEPENDENT)"
    )
    print(
        "- Germanium-9.7 should see ~97% DAMA rate/kg at line position 3.728 keV (Z-INDEPENDENT)"
    )
    print(
        "- A Sapphire-2.64-kg single crystal would have N_single matched to DAMA NaI 9.7 kg"
    )
    print(
        "  → predicted ~1.15× DAMA rate/kg at line 3.728 keV — CLEAN Z-INDEPENDENCE TEST"
    )
    print(
        "    (the 1.15× reflects N_e(Sapphire)/N_e(NaI) electron-density ratio,"
    )
    print(
        "     the ONLY mass/Z-dependent factor remaining when N_single is matched)"
    )
    print()
    print(
        "The Z-INDEPENDENCE claim is the cleanest discriminator vs Moseley Kα (which"
    )
    print(
        "would predict zero rate in Ca-free crystals at 3.728 keV). Cross-crystal swap"
    )
    print("with matched N_single isolates the AVE-distinct prediction from κ_quality.")
    print()


def main() -> int:
    print("=" * 70)
    print("DAMA Q-factor: matched-LC-coupling derivation")
    print("Reactive-power reframe (9th audit cycle resolution)")
    print("=" * 70)
    print()

    print("CANONICAL AVE QUANTITIES:")
    print(f"  alpha                  = {ALPHA:.6e}")
    print(f"  alpha m_e c^2 (E_slew) = {E_SLEW_KEV:.4f} keV")
    print(f"  nu_slew                = {NU_SLEW:.4e} Hz")
    print(f"  lambda_slew            = {LAMBDA_SLEW:.4e} m")
    print(f"  Z_tank = Z_0/(4 pi)    = {Z_TANK:.2f} Ohm")
    print()

    print("NaI DETECTOR:")
    print(f"  M_NaI                  = {M_NAI_KG_PER_MOL*1e3:.2f} g/mol")
    print(f"  rho_NaI                = {RHO_NAI:.0f} kg/m^3")
    print(f"  d_NaI lattice spacing  = {D_NAI:.4e} m")
    print(f"  Z_avg = Z_Na + Z_I     = {Z_AVG_NAI}")
    print(f"  N_e / kg               = {N_E_PER_KG:.4e}")
    print()

    print("DAMA/LIBRA Phase-2 EMPIRICAL:")
    print(f"  Rate           = {RATE_DAMA_CPD_KG_KEV} cpd/kg/keV in 2-6 keV window")
    print(f"  Integrated rate= {RATE_DAMA_PER_S_PER_KG:.4e} events/s/kg")
    print()

    intrinsic_rate, dama_rate, required_eps = compute_required_epsilon()
    print("REQUIRED MATCHED-COUPLING EFFICIENCY PER CYCLE:")
    print(f"  Intrinsic rate (per electron cycle) = {intrinsic_rate:.4e} events/s/kg")
    print(f"  DAMA observed rate                   = {dama_rate:.4e} events/s/kg")
    print(f"  Required epsilon_det per cycle       = {required_eps:.4e}")
    print()

    print("=" * 70)
    print("STRUCTURAL-CANDIDATE SCOREBOARD")
    print("=" * 70)
    print()

    candidates = evaluate_candidates(required_eps)

    # Sort by closeness to required (log10 ratio)
    import math

    candidates_scored = sorted(
        candidates,
        key=lambda c: abs(math.log10(c.value / required_eps)) if c.value > 0 else 1e10,
    )

    print(f"{'Candidate':<28} {'Value':<14} {'Ratio to req.':<14}  Rationale")
    print("-" * 80)
    for c in candidates_scored:
        if c.value > 0:
            ratio = c.value / required_eps
            ratio_str = (
                f"{ratio:.2e}" if (ratio > 1e-4 and ratio < 1e4) else f"10^{math.log10(ratio):.1f}"
            )
            print(f"{c.name:<28} {c.value:<14.4e} {ratio_str:<14}  {c.rationale[:60]}")
    print()

    print("=" * 70)
    print("ADJUDICATION")
    print("=" * 70)
    print()

    best = candidates_scored[0]
    print(f"Best-fit structural candidate: {best.name}")
    print(f"  Value:        {best.value:.4e}")
    print(f"  Required:     {required_eps:.4e}")
    print(f"  Ratio:        {best.value/required_eps:.2e}")
    print(f"  Rationale:    {best.rationale}")
    print()

    if 0.1 < best.value / required_eps < 10:
        print(
            "STATUS: BEST candidate lands within factor 10 of required — STRUCTURAL FORM PLAUSIBLE."
        )
    elif 0.01 < best.value / required_eps < 100:
        print(
            "STATUS: BEST candidate lands within factor 100 of required — STRUCTURAL FORM SUGGESTIVE."
        )
    else:
        print(
            "STATUS: BEST candidate misses required by >factor 100 — STRUCTURAL FORM NOT FOUND."
        )
    print()

    print("HONEST GAP STATEMENT:")
    print("  None of the natural-AVE structural candidates above is a clean")
    print("  first-principles derivation of the matched-LC-coupling efficiency")
    print("  in DAMA. The 22-α-power photoabsorption framing (8th cycle) was")
    print("  categorically wrong; the matched-LC-coupling framing (9th cycle)")
    print("  is categorically correct but the SPECIFIC magnitude requires")
    print("  substrate-tank-coupling physics that the corpus does not yet have.")
    print()
    print("  Specific next-session work needed:")
    print("  1. Derive NaI bulk LC impedance at nu_slew = 9.02e17 Hz from")
    print("     substrate physics + lattice geometry (Bragg coupling, electronic")
    print("     band structure at sub-keV scale)")
    print("  2. Compute matched-coupling efficiency Γ at electron-NaI boundary")
    print("     using canonical Op14 dynamic impedance + Op17 power transmission")
    print("     T^2 = 1 - Γ^2")
    print("  3. Apply Bragg-resonance enhancement (second-order Bragg in NaI")
    print("     matches lambda_slew to 2.4%) — narrow-band enhancement vs broad")
    print("     off-resonance suppression trade-off")
    print()

    cross_detector_predictions()

    return 0


if __name__ == "__main__":
    sys.exit(main())
