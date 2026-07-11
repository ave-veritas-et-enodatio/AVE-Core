"""
Tests for the x42 atomic-eigencavity driver
===========================================

Prereg: research/2026-07-10_x42-atomic-eigencavity_prereg_FROZEN.md
Driver: scripts.vol_2_subatomic.x42_atomic_eigencavity

Two lanes (CI cost partition, pyproject `engine_sim` marker):
  * DEFAULT (fast) — the load-bearing LOGIC: the M2 a₀ identity, the exact reuse
    of the canonical Op5 section primitive, the analytic muonic marks + §3
    operating point, and — critically (P11) — that every gate can FIRE on a
    planted defect and PASS on a valid input, using synthetic eigenvalue lists
    (no driver run needed).
  * engine_sim (opt-in) — the full phase-closure driver runs (hydrogen 1/n²,
    muonic reduced-mass scaling, sabotage via the 1/r² plant, Z²-scaling).

FROZEN marks (constants at prereg time): E_1=-RY_EV, a₀=A_0, a_μ=284.748 fm,
E_1(μH)=-2.528493 keV.
"""

import numpy as np
import pytest

from ave.core.constants import A_0, ALPHA, L_NODE, M_E, RY_EV
from ave.solvers.radial_eigenvalue import _abcd_section

import scripts.vol_2_subatomic.x42_atomic_eigencavity as x42


# ---------------------------------------------------------------------------
# DEFAULT lane — logic, identities, gate-firing (fast; no driver scan)
# ---------------------------------------------------------------------------


def test_m2_a0_identity_exact():
    """M2: a₀ = ℓ_node/α to float precision (canon identity, not a fit)."""
    assert abs(L_NODE / ALPHA - A_0) / A_0 < 1e-12


def test_dress_section_reuses_canonical_op5_exactly():
    """The driver's section (m=m_e, dress_exp=1) IS radial_eigenvalue._abcd_section.

    Proves the muonic (m→m_r,μ) and sabotage (dress_exp→2) runs are single-
    parameter perturbations of the CANONICAL Op5 primitive, not a re-derivation.
    """
    from ave.core.constants import e_charge

    for E_eV in (13.6, 3.4, 1.5):
        E_J = -E_eV * e_charge
        for r1, r2 in ((0.01 * A_0, 0.05 * A_0), (0.5 * A_0, 0.9 * A_0), (2.0 * A_0, 3.0 * A_0)):
            for l in (0, 1):
                got = x42.dress_section(r1, r2, E_J, 1.0, l, m_probe=M_E, dress_exp=1)
                ref = _abcd_section(r1, r2, E_J, 1.0, l, 0.0)
                assert np.allclose(got, ref, rtol=1e-12, atol=1e-14), (E_eV, r1, r2, l)


def test_de_broglie_index_is_cascade_local_wavenumber():
    """D1 entailed-form check — wires in `de_broglie_refractive_index` (was dead
    code): the imported de Broglie index IS the executed cascade's local radial
    wavenumber. For l=0 / linear network, k²(r)·a₀² == n(r,ξ)² element-wise
    across the integration grid. Makes the imported-FORM entailment explicit and
    machine-checked (review live-trace ratio 1.0000000000000004). n(r,ξ) is the
    DEFECT'S dispersion, NOT a medium impedance (vol2/claim-quality.md:344)."""
    from ave.core.constants import e_charge

    Z = 1
    E_eV = RY_EV  # ground-state binding, ξ = |E|/Ry = 1
    E_J = -E_eV * e_charge
    xi = abs(E_eV) / RY_EV
    r_turn = 2.0 * Z * A_0 / xi  # n(r,ξ)=0 classical turning point
    # classically-allowed region, kept below the turning point so n² ≥ ξ > 0
    r = np.geomspace(1e-4 * A_0, 0.5 * r_turn, 500)
    n_sq = x42.de_broglie_refractive_index(r, xi, Z_eff=Z) ** 2
    k2_a0_sq = x42.local_wavenumber_sq(r, E_J, Z, l=0, saturate=False) * A_0**2
    assert np.allclose(k2_a0_sq, n_sq, rtol=1e-11, atol=0.0)
    assert np.max(np.abs(k2_a0_sq / n_sq - 1.0)) < 1e-11


def test_muonic_analytic_marks_match_frozen():
    """M3 frozen marks: a_μ ≈ 284.748 fm, E_1(μH) ≈ -2.528493 keV."""
    mm = x42.muonic_marks()
    assert abs(mm["a_mu_fm"] - 284.748) / 284.748 < 5e-3
    assert abs(mm["E_n_muH_eV"][1] - (-2528.493)) / 2528.493 < 5e-3
    # reduced-mass ratios (declared convention)
    assert abs(mm["mr_mu_over_me"] - 185.84083) < 1e-3
    assert abs(mm["mr_mu_over_mr_H"] - 185.94205) < 1e-3


def test_muonic_orbit_is_sub_lattice_cell_flag():
    """SUBSTRATE FLAG (prereg): a_μ (285 fm) < ℓ_node (386 fm) — sub-Nyquist."""
    mm = x42.muonic_marks()
    assert mm["a_mu_vs_ell_node"] < 1.0
    assert mm["a_mu_m"] < L_NODE


def test_muonic_operating_point_is_not_deep_linear():
    """Brief §3: A_dielectric ~ 0.12, O(0.1), NOT deep-linear like H (~1e-4)."""
    A = x42.muonic_operating_point_A()
    assert 0.08 < A["A_dielectric"] < 0.20
    # decisively larger than ordinary hydrogen's per-node ratio
    assert A["A_dielectric"] > 50 * A["hydrogen_A_dielectric_ref"]
    # the Ax-4 kernel arg the ODE actually uses stays deep-linear
    assert A["A_rupture"] < 0.05


def test_gates_pass_on_valid_synthetic_spectrum():
    """G-MARK / G-FORM / G-INT all PASS on the exact Rydberg ladder."""
    good = [RY_EV / n**2 for n in (1, 2, 3, 4)]
    assert x42.gate_mark(good)[0]
    assert x42.gate_form(good)[0]
    assert x42.gate_int(good)[0]


def test_gate_mark_fires_on_detuned_closure_integer():
    """P11 sabotage (b): detuned closure Ry/(n+0.4)² — G-MARK and G-INT FIRE."""
    detuned = [RY_EV / (n + 0.4) ** 2 for n in (1, 2, 3, 4)]
    assert not x42.gate_mark(detuned)[0]  # fired
    assert not x42.gate_int(detuned)[0]  # fired


def test_gate_mark_fires_on_empty_spectrum():
    """P11 sabotage (a) shadow: a profile with no eigenvalues at the marks FIRES."""
    assert not x42.gate_mark([])[0]
    assert not x42.gate_form([])[0]
    assert not x42.gate_int([])[0]


def test_gate_form_fires_on_non_rydberg_form():
    """G-FORM fires when E_n·n² is NOT constant (form broken)."""
    # equally spaced (harmonic-oscillator-like) levels break the 1/n² form
    bad = [10.0, 8.0, 6.0, 4.0]
    assert not x42.gate_form(bad)[0]


# ---------------------------------------------------------------------------
# engine_sim lane (opt-in) — the full phase-closure driver runs
# ---------------------------------------------------------------------------


@pytest.mark.engine_sim
def test_hydrogen_phase_closure_reproduces_1_over_n2():
    """M1 branch (i): ABCD B_total=0 spectrum == Ry/n² within 0.5%; gates PASS."""
    eigs = x42.phase_closure_spectrum(Z=1, l=0, n_max=4, N_sec=4000)
    # ground state through n=4 must be present and on the marks
    assert x42.gate_mark(eigs)[0]
    assert x42.gate_form(eigs)[0]
    assert x42.gate_int(eigs)[0]
    # explicit ground state = -RY_EV
    E1 = max(eigs)
    assert abs(E1 - RY_EV) / RY_EV < 5e-3


@pytest.mark.engine_sim
def test_m2_eigenmode_scale_extracted_from_eigenfunction():
    """M2 frozen sub-mark (prereg :115 'closure scale from driver | eigenmode-
    scale extraction'), implemented at repair time: ⟨r⟩ of the inward-integrated
    ground-state eigenfunction == 1.5·a_scale within the frozen 0.5% tolerance —
    a genuine measurement of the eigenmode SHAPE scale from the ODE eigenfunction
    (not the box unit restated: r_max ≈ 133×⟨r⟩)."""
    res = x42.ground_state_mean_radius(Z=1, l=0, N_sec=4000)
    # ⟨r⟩ = 1.5·a_scale for the 1s state (textbook shape factor); frozen 0.5% tol
    assert abs(res["mean_r_over_a_scale"] - 1.5) / 1.5 < 5e-3
    # ground-state eigenvalue lands on the M1 mark (self-consistency)
    assert abs(res["E1_eV"] - RY_EV) / RY_EV < 5e-3
    # eigenfunction is regular at r_min (physical decaying mode, not the growing branch)
    assert res["inner_regularity"] < 1e-2


@pytest.mark.engine_sim
def test_muonic_spectrum_same_network_heavier_probe():
    """M3 via driver: swap probe m_e→m_r,μ, reproduce reduced-mass-scaled marks."""
    eigs = x42.muonic_spectrum(n_max=3, N_sec=4000)
    ry_mu = RY_EV * x42.M_R_MU / M_E
    assert x42.gate_mark(eigs, ry_scale=ry_mu)[0]
    E1 = max(eigs)
    assert abs(E1 - ry_mu) / ry_mu < 5e-3  # ground state -2.5285 keV


@pytest.mark.engine_sim
def test_sabotage_wrong_exponent_dress_fires_gate():
    """P11 sabotage (a): the 1/r² plant does NOT carry a Rydberg ladder — FIRES."""
    eigs_bad = x42.phase_closure_spectrum(Z=1, l=0, dress_exp=2, N_sec=4000)
    assert not x42.gate_mark(eigs_bad)[0]  # gate fired on the plant


@pytest.mark.engine_sim
def test_Z2_scaling_bare_ion():
    """M4: bare hydrogenic Z=2 ground state == 4·RY_EV within 0.5% (Z² scaling)."""
    eigs = x42.phase_closure_spectrum(Z=2, l=0, n_max=2, N_sec=4000)
    E1 = max(eigs)
    assert abs(E1 - 4.0 * RY_EV) / (4.0 * RY_EV) < 5e-3
