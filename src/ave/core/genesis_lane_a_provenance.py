"""
Genesis Lane A — provenance in vacuum native units.

Convention (natural-units-cheatsheet.md, constants.py N_* block):
  ℓ_node = c = m_e = ℏ = τ_relax = 1
  Energy unit = m_e c² = 1
  V_YIELD = 1 native  (engine uses V_SNAP=1; r_yield = |V|_vsnap / √α)
  e = √α ≈ 0.0854 native  (native value of the elementary charge; ξ_topo = e/ℓ_node, the C/m constant, is distinct)

See research/2026-06-12_genesis-parameter-provenance-audit.md.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass

import numpy as np

from ave.core import chiral_lattice as cl
from ave.core.chiral_lattice_v10 import A_YIELD_SQ, CHI_SWEEP
from ave.core.chiral_lattice_v11 import DEFAULT_TAU_STEPS, DISCRETE_TAU_STEPS, DT_STEP
from ave.core.constants import (
    ALPHA,
    G,
    H_INFINITY,
    L_NODE,
    M_E,
    NATIVE_TO_SI_ENERGY,
    NATIVE_TO_SI_TIME,
    TAU_RELAX_NATIVE,
    TAU_RELAX_SI,
)

# √α = native numeric value of e, the unit charge in native units (e = ξ_topo·ℓ_node).
# NOT ξ_topo itself (the C/m constant e/ℓ_node); see natural-units-cheatsheet §4 and def-095760 object-4.
E_NATIVE_SQRT_ALPHA: float = float(np.sqrt(ALPHA))

# Regime I/II knee: A²_vsnap = 2α ⟺ r_yield² = 2 (lattice-impedance-decomposition §2).
R_YIELD_KNEE_NATIVE: float = float(np.sqrt(2.0))

# Pair-production C1: A²_vsnap ≥ 1 ⟺ r_yield ≥ 1/√α ≈ 11.7 (full Γ=-1 saturation).
R_SATURATION_NATIVE: float = float(1.0 / np.sqrt(ALPHA))

# Prereg P15-N: 0.9 × A²_vsnap = 2α threshold.
P15_A2_FRAC = 0.90
P15_R_YIELD_MIN = float(np.sqrt(P15_A2_FRAC * 2.0))

P15_E_FRAC_MIN = 0.55
P15_WIDTH_MAX = 2.5


@dataclass(frozen=True)
class CosmicLatentNative:
    """3Hρ_latent per native cell per native τ (cmb-thermal-attractor)."""

    rho_lambda_native: float
    h_infinity_native: float
    latent_power_native: float
    e_per_cell_per_tau_native: float
    e_yield_kinetic_native: float
    ratio_to_yield: float
    # SI audit trail only
    rho_lambda_si: float
    e_per_cell_per_tau_si: float


@dataclass(frozen=True)
class LocalNucleationNative:
    """Pair ramp: r_yield seed → r_yield knee over N_τ (pair-production §3)."""

    seed_r_yield: float
    target_r_yield: float
    e_seed_pair_native: float
    e_target_pair_native: float
    e_deficit_native: float
    n_latent_steps: int
    n_pocket_nodes: int
    delta_e_native_per_step_pair: float
    r_yield_threshold: float
    a2_vsnap_threshold: float


@dataclass(frozen=True)
class LaneATiming:
    discrete_tau_steps: int
    n_latent_steps: int
    n_quiescent_steps: int
    n_steps_total: int
    chi_shock: float


@dataclass(frozen=True)
class LaneAProvenance:
    unit_system: str
    cosmic: CosmicLatentNative
    local: LocalNucleationNative
    timing: LaneATiming
    injection_path: str


def vsnap_to_r_yield(a_vsnap: float) -> float:
    """Engine V_SNAP-normalized amplitude → native r_yield = V/V_YIELD."""
    return float(a_vsnap / E_NATIVE_SQRT_ALPHA)


def a2_vsnap_to_r_yield(a2_vsnap: float) -> float:
    return float(np.sqrt(max(a2_vsnap, 0.0) / ALPHA))


def field_energy_native(V: np.ndarray) -> float:
    """∑|V|² in engine V_SNAP units → native energy (E_unit = m_e c²)."""
    return float(np.sum(V * V) / ALPHA)


def cosmic_latent_native() -> CosmicLatentNative:
    """
    de Sitter ρ_Λ + source 3Hρ_latent in vacuum native units.

    H_native = H_SI · τ_relax_SI  (1 native time = ℓ_node/c).
    ρ_native = ρ_SI · ℓ_node³ / m_e.
    """
    rho_lambda_si = 3.0 * H_INFINITY**2 / (8.0 * np.pi * G)
    h_native = float(H_INFINITY * NATIVE_TO_SI_TIME)
    rho_native = float(rho_lambda_si * L_NODE**3 / M_E)
    latent_power_native = 3.0 * h_native * rho_native
    e_cell_tau = latent_power_native * TAU_RELAX_NATIVE  # one cell, one τ
    e_yield_kinetic = float(np.sqrt(ALPHA))
    e_cell_tau_si = e_cell_tau * NATIVE_TO_SI_ENERGY
    return CosmicLatentNative(
        rho_lambda_native=rho_native,
        h_infinity_native=h_native,
        latent_power_native=float(latent_power_native),
        e_per_cell_per_tau_native=float(e_cell_tau),
        e_yield_kinetic_native=e_yield_kinetic,
        ratio_to_yield=float(e_cell_tau / e_yield_kinetic),
        rho_lambda_si=float(rho_lambda_si),
        e_per_cell_per_tau_si=float(e_cell_tau_si),
    )


def _pair_seed_energy_native(r_yield: float) -> float:
    """Bond-0 transverse seed (1, ½) components; E_native ∝ r_yield²."""
    return 2.0 * (r_yield**2 + (0.5 * r_yield) ** 2)


def _pair_target_energy_native(r_yield: float, degree: int) -> float:
    """Uniform r_yield on all bonds of both pair nodes."""
    return 2.0 * float(degree) * (r_yield**2)


def local_nucleation_native(
    net: cl.LatticeNet,
    pocket_mask: np.ndarray,
    *,
    n_latent_steps: int = DEFAULT_TAU_STEPS,
) -> LocalNucleationNative:
    """
    Ω_freeze seed at r_yield=1 (native); ramp to knee r_yield=√2 (A²_vsnap=2α).
    """
    seed_r = 1.0  # √α Vsnap = 1 Vyield native (Ω_freeze IC scale)
    target_r = R_YIELD_KNEE_NATIVE
    e_seed = _pair_seed_energy_native(seed_r)
    e_target = _pair_target_energy_native(target_r, net.degree)
    e_deficit = max(e_target - e_seed, 0.0)
    n_pocket = max(int(pocket_mask.sum()), 1)
    n_deposit = 2
    delta_e = e_deficit / max(n_latent_steps * n_deposit, 1)
    return LocalNucleationNative(
        seed_r_yield=seed_r,
        target_r_yield=target_r,
        e_seed_pair_native=float(e_seed),
        e_target_pair_native=float(e_target),
        e_deficit_native=float(e_deficit),
        n_latent_steps=n_latent_steps,
        n_pocket_nodes=n_pocket,
        delta_e_native_per_step_pair=float(delta_e),
        r_yield_threshold=P15_R_YIELD_MIN,
        a2_vsnap_threshold=float(P15_A2_FRAC * A_YIELD_SQ),
    )


def seed_amp_vsnap() -> float:
    """Engine IC amplitude: r_yield=1 ⟹ |V|_vsnap = √α."""
    return E_NATIVE_SQRT_ALPHA


def lane_a_timing(*, smoke: bool = False) -> LaneATiming:
    n_tau = 10 if smoke else DEFAULT_TAU_STEPS
    n_latent = n_tau
    n_quiet = 2 * n_tau if smoke else 4 * n_tau
    return LaneATiming(
        discrete_tau_steps=n_tau,
        n_latent_steps=n_latent,
        n_quiescent_steps=n_quiet,
        n_steps_total=n_latent + n_quiet,
        chi_shock=0.5 if 0.5 in CHI_SWEEP else float(CHI_SWEEP[-1]),
    )


def build_lane_a_provenance(
    net: cl.LatticeNet,
    pocket_mask: np.ndarray,
    *,
    smoke: bool = False,
) -> LaneAProvenance:
    timing = lane_a_timing(smoke=smoke)
    cosmic = cosmic_latent_native()
    local = local_nucleation_native(
        net, pocket_mask, n_latent_steps=timing.n_latent_steps
    )
    path = "local_pair_ramp_native"
    if cosmic.ratio_to_yield > 0.01:
        path = "cosmic_mean_native"
    return LaneAProvenance(
        unit_system="vacuum_native (ℓ_node=c=m_e=ℏ=τ=1, E=m_e c², V_YIELD=1)",
        cosmic=cosmic,
        local=local,
        timing=timing,
        injection_path=path,
    )


def provenance_dict(p: LaneAProvenance) -> dict:
    return {
        "unit_system": p.unit_system,
        "injection_path": p.injection_path,
        "cosmic": asdict(p.cosmic),
        "local": asdict(p.local),
        "timing": asdict(p.timing),
        "native_identities": {
            "e_native_sqrt_alpha": E_NATIVE_SQRT_ALPHA,
            "r_yield_knee_sqrt2": R_YIELD_KNEE_NATIVE,
            "A2_vsnap_knee": A_YIELD_SQ,
            "tau_relax_native": TAU_RELAX_NATIVE,
            "discrete_tau_steps": DISCRETE_TAU_STEPS,
            "dt_step": DT_STEP,
        },
        "si_audit": {
            "tau_relax_si": TAU_RELAX_SI,
            "native_to_si_energy": NATIVE_TO_SI_ENERGY,
        },
    }
