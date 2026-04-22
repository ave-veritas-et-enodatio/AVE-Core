import numpy as np

from ave.regime_1_linear.fluids_factory import WaterMolecule
from ave.regime_3_saturated.cavitation_collapse import AxiomaticRayleighPlesset, PayloadConfig


def test_sonoluminescence_topological_bounce():
    """
    Validates that the Axiom 4 topological yield limit successfully halts
    the mathematical collapse of the Rayleigh-Plesset equation before infinite
    singularity, preventing non-physical fluid velocities > c_0.
    """
    water = WaterMolecule()
    payload = PayloadConfig(gas_type="vapor")

    # Extreme acoustic drive (should collapse violently)
    R0 = 4.0e-6
    f_ac = 26.5e3
    P_amp = 1.6 * 101325

    solver = AxiomaticRayleighPlesset(
        fluid=water,
        R0_m=R0,
        acoustic_freq_hz=f_ac,
        acoustic_amp_pa=P_amp,
        payload=payload,
        T_celsius=20.0,
    )

    T_cycle = 1.0 / f_ac
    sol = solver.solve_collapse((0, T_cycle), max_step=1e-8)

    # R_array = sol.y[0]  # bulk lint fixup pass
    U_array = sol.y[1]

    # Must never exceed the speed of sound (+0.1% margin for ODE integrator slop)
    max_mach = np.max(np.abs(U_array)) / solver.c_sound
    assert max_mach <= 1.001, f"Relativistic metric boundary violated! Mach={max_mach}"

    # Must stop when it hits the metric wall
    assert abs(max_mach - 1.0) < 0.05, "Did not reach topological yield wall during collapse."
