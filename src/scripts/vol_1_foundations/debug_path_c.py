"""Quick diagnostic: trace what extract_crossing_count_tlm and
extract_chirality_measured see on the same TLM lattice, after evolution.
"""
import numpy as np
from ave.core.constants import V_YIELD
from scripts.vol_1_foundations.tlm_electron_soliton_eigenmode import (
    PHI,
    run_tlm_electron,
    extract_crossing_count_tlm,
    extract_chirality_measured,
    _contour_winding,
)


def main():
    from ave.core.k4_tlm import K4Lattice3D
    from scripts.vol_1_foundations.tlm_electron_soliton_eigenmode import (
        initialize_2_3_voltage_ansatz,
    )

    PHI_SQ = PHI ** 2
    N = 48
    R_target = 12.0
    r_target = R_target / PHI_SQ  # 4.58
    amp = 0.5 * float(V_YIELD)

    # First check initial state (no evolution)
    print(f"=== INITIAL STATE (no TLM evolution) at {N}^3 ===")
    lattice0 = K4Lattice3D(N, N, N, dx=1.0, pml_thickness=0,
                            nonlinear=False, op3_bond_reflection=True)
    initialize_2_3_voltage_ansatz(lattice0, R=R_target, r=r_target,
                                  amplitude=amp)
    c_init = extract_crossing_count_tlm(lattice0, R_major=R_target)
    chi_init = extract_chirality_measured(lattice0, R_major=R_target)
    print(f"  crossing count (init) = {c_init}")
    print(f"  p_init = {chi_init['p_measured']:+.3f}  "
          f"amp_ratio_p = {chi_init['amp_ratio_p']:.4f}")
    print(f"  q_init = {chi_init['q_measured']:+.3f}  "
          f"amp_ratio_q = {chi_init['amp_ratio_q']:.4f}")

    print(f"\n=== AFTER EVOLUTION ===")
    print(f"Running TLM at {N}^3, R={R_target}, r={r_target:.3f}, amp={amp:.3e}...")
    result = run_tlm_electron(
        N=N, R=R_target, r=r_target, n_steps=150, amplitude=amp,
        nonlinear=False, pml_thickness=0, op3_bond_reflection=True,
        sample_every=200, verbose=False,
    )
    lattice = result['lattice']
    R_rms = result['R_rms']
    r_rms = result['r_rms']
    print(f"After evolution: R_rms={R_rms:.3f}, r_rms={r_rms:.3f}")

    # Original crossing count function
    print("\n--- extract_crossing_count_tlm ---")
    c_orig = extract_crossing_count_tlm(lattice, R_major=R_rms)
    print(f"  crossing count = {c_orig}")

    # New chirality function
    print("\n--- extract_chirality_measured ---")
    chi = extract_chirality_measured(lattice, R_major=R_rms)
    print(f"  p_measured = {chi['p_measured']:+.3f}")
    print(f"  q_measured = {chi['q_measured']:+.3f}")
    print(f"  chi_measured = {chi['chi_measured']:+.4e}")
    print(f"  amp_ratio_p = {chi['amp_ratio_p']:.4f}")
    print(f"  amp_ratio_q = {chi['amp_ratio_q']:.4f}")
    print(f"  valid = {chi['valid']}")

    # Manual sweep with diagnostic output
    print("\n--- Manual contour sweep diagnostic ---")
    print(f"{'r_minor':<10}{'p_w':<10}{'p_amp':<10}{'q_w':<10}{'q_amp':<10}")
    for r_minor in np.linspace(1.0, max(3.0, R_rms * 0.5), 8):
        p_w, p_amp = _contour_winding(lattice, R_rms, r_minor, 'toroidal')
        q_w, q_amp = _contour_winding(lattice, R_rms, r_minor, 'poloidal')
        print(f"{r_minor:<10.3f}{p_w:<10.4f}{p_amp:<10.4f}{q_w:<10.4f}{q_amp:<10.4f}")


if __name__ == "__main__":
    main()