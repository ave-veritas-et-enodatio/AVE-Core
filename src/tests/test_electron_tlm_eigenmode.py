"""
Test: single-electron TLM eigenmode validation (Path A, K4-only).

Validates four pre-registered predictions from manuscript/predictions.yaml:
  - P_electron_tlm_topological_charge
  - P_electron_tlm_energy_conservation
  - P_electron_tlm_golden_torus_convergence
  - P_electron_tlm_alpha_derivation

These assert that a seeded (2,3) V_inc ansatz on the K4 TLM lattice is a
stable closed-system eigenmode — the precondition for Stage 6 pair-
nucleation work per research/L3_electron_soliton/66_single_electron_first_pivot.md.

**Path independence:** uses only K4 state (V_inc, lattice energy, K4-extracted
geometry, K4-extracted crossing count). Zero Cosserat reads. Runs without
instantiating Cosserat sector. Path B (coupled K4+Cosserat) is a downstream
extension; failure here would block it.

**Test grid:** N=48 (CI-friendly, ~1-2 min total). The pre-registered
predictions cite N=96³ (publication config in tlm_electron_soliton_eigenmode.py
main()). Any scale-dependence of pass/fail would itself be a Round 6 axiom-
layer flag caught here — if N=48 fails but N=96 would pass, that's physics
information not a test artifact.
"""
from __future__ import annotations

import numpy as np
import pytest

from ave.core.constants import V_YIELD
from scripts.vol_1_foundations.tlm_electron_soliton_eigenmode import (
    extract_alpha_inverse,
    extract_crossing_count_tlm,
    run_tlm_electron,
    solve_eigenmode_self_consistent,
)


PHI = (1.0 + np.sqrt(5.0)) / 2.0
PHI_SQ = PHI ** 2                            # Golden Torus R/r target ≈ 2.618
ALPHA_TARGET = 4 * np.pi**3 + np.pi**2 + np.pi  # α⁻¹ = 137.0363 per Vol 1 Ch 8


# ─── CI-friendly grid config ────────────────────────────────────────────────
N_GRID = 48
R_TARGET = 12.0
R_OVER_PHI_SQ = R_TARGET / PHI_SQ
AMP = 0.9 * float(V_YIELD)
N_STEPS = 400


# ─── L3 closure xfail reason (Rule 11 + Rule 12 falsification record) ──────
# These 6 physics-content tests assert P_electron_tlm_topological_charge,
# P_electron_tlm_golden_torus_convergence, and P_electron_tlm_alpha_derivation
# pre-registered predictions. The L3 closure (doc 79 v5.1 A-014, Mode III
# canonical at 10 pre-reg tests at bond-cluster scale) + E-094 closure (doc
# 100 §10.36-§10.37, Mode III at corpus-canonical bond-pair scale + IC) +
# Flag 2 calibration (doc 100 §10.38, closure scope at ℓ_node-and-coarser
# sampling) empirically falsified the K4-only-V_inc-ansatz precondition.
# Per Vol 2 Ch 1:9, corpus electron tube radius = ℓ_node/(2π) ≈ 0.16 cells
# = sub-ℓ_node, structurally below K4-TLM at this test's ℓ_node sampling.
# Per Rule 11 (clean falsification = framework working at full strength) +
# Rule 12 (preserve body): assertions retained verbatim; xfail strict=True
# signals XPASS if the K4-only path ever recovers (would invalidate the
# L3 closure and re-open Track A).
L3_CLOSURE_XFAIL = pytest.mark.xfail(
    strict=True,
    reason=(
        "L3 closure A-014 + E-094 + Flag 2: K4-only V_inc ansatz "
        "empirically falsified at multiple scales × IC classes. "
        "Corpus electron is sub-ℓ_node (Vol 2 Ch 1:9, tube radius "
        "ℓ_node/(2π) ≈ 0.16 cells), structurally below K4-TLM at "
        "ℓ_node sampling. See research/L3_electron_soliton/79 + "
        "research/L3_electron_soliton/100 §10.36-§10.38."
    ),
)


# ─── Module-level cached runs (each fixture runs once per test module) ──────
@pytest.fixture(scope="module")
def golden_torus_run() -> dict:
    """Single closed-system TLM run with Golden Torus seed."""
    return run_tlm_electron(
        N=N_GRID, R=R_TARGET, r=R_OVER_PHI_SQ,
        n_steps=N_STEPS, sample_every=50, amplitude=AMP,
        nonlinear=False, pml_thickness=0, op3_bond_reflection=True,
        verbose=False,
    )


@pytest.fixture(scope="module")
def perturbed_run() -> dict:
    """Closed-system TLM run with perturbed seed (R+30%, r-30%)."""
    return run_tlm_electron(
        N=N_GRID, R=R_TARGET * 1.3, r=R_OVER_PHI_SQ * 0.7,
        n_steps=N_STEPS, sample_every=50, amplitude=AMP,
        nonlinear=False, pml_thickness=0, op3_bond_reflection=True,
        verbose=False,
    )


@pytest.fixture(scope="module")
def op6_from_golden_torus() -> dict:
    """Op6 self-consistency from Golden Torus seed."""
    return solve_eigenmode_self_consistent(
        N=N_GRID, R_seed=R_TARGET, r_seed=R_OVER_PHI_SQ, amplitude=AMP,
        n_steps=300, sample_every=300, max_iter=6, tol=1e-3, verbose=False,
    )


@pytest.fixture(scope="module")
def op6_from_perturbed() -> dict:
    """Op6 self-consistency from perturbed seed."""
    return solve_eigenmode_self_consistent(
        N=N_GRID, R_seed=R_TARGET * 1.3, r_seed=R_OVER_PHI_SQ * 0.7,
        amplitude=AMP,
        n_steps=300, sample_every=300, max_iter=6, tol=1e-3, verbose=False,
    )


# ═══════════════════════════════════════════════════════════════════════════
# P_electron_tlm_topological_charge
#   N_crossings = 3 for electron (2,3) Hopf soliton — topological integer,
#   no tolerance.
# ═══════════════════════════════════════════════════════════════════════════
class TestTopologicalChargePreservation:
    @L3_CLOSURE_XFAIL
    def test_golden_torus_seed_preserves_three_crossings(self, golden_torus_run):
        c = extract_crossing_count_tlm(
            golden_torus_run["lattice"],
            R_major=float(golden_torus_run["R_rms"]),
        )
        assert c == 3, (
            f"Golden Torus seed: N_crossings = {c}, expected 3. Topology "
            f"dispersed or re-wound — (2,3) V_inc ansatz is not a closed-"
            f"system eigenmode of the K4 TLM at this amplitude."
        )

    @L3_CLOSURE_XFAIL
    def test_perturbed_seed_preserves_three_crossings(self, perturbed_run):
        c = extract_crossing_count_tlm(
            perturbed_run["lattice"],
            R_major=float(perturbed_run["R_rms"]),
        )
        assert c == 3, (
            f"Perturbed seed (R+30%/r-30%): N_crossings = {c}, expected 3. "
            f"Basin of attraction does not span the ±30% perturbation, OR "
            f"topology dispersed within basin."
        )


# ═══════════════════════════════════════════════════════════════════════════
# P_electron_tlm_energy_conservation
#   Closed-system ΔE/E₀ < 0.5% — integrator kill-switch.
# ═══════════════════════════════════════════════════════════════════════════
class TestEnergyConservation:
    def test_golden_torus_seed_conserves_energy(self, golden_torus_run):
        energy = golden_torus_run["energy"]
        E_var = (energy.max() - energy.min()) / energy[0]
        assert E_var < 0.005, (
            f"Golden Torus seed: ΔE/E₀ = {E_var * 100:.3f}%, expected < 0.5%. "
            f"Integrator dissipative — audit K4Lattice3D.step() for sources "
            f"(scatter matrix, Op3 bond reflection, Op14 memristive path) "
            f"before trusting other Round 6 results."
        )

    def test_perturbed_seed_conserves_energy(self, perturbed_run):
        energy = perturbed_run["energy"]
        E_var = (energy.max() - energy.min()) / energy[0]
        assert E_var < 0.005, (
            f"Perturbed seed: ΔE/E₀ = {E_var * 100:.3f}%, expected < 0.5%."
        )


# ═══════════════════════════════════════════════════════════════════════════
# P_electron_tlm_golden_torus_convergence
#   Op6 self-consistency converges from both seeds to R/r = φ² within ±5%.
# ═══════════════════════════════════════════════════════════════════════════
class TestGoldenTorusConvergence:
    @L3_CLOSURE_XFAIL
    def test_op6_converges_from_golden_torus_seed(self, op6_from_golden_torus):
        assert op6_from_golden_torus["converged"], (
            f"Op6 did NOT converge from Golden Torus seed within "
            f"{op6_from_golden_torus['iterations']} iterations — "
            f"self-consistency fails for the exact target."
        )
        R = op6_from_golden_torus["final_R"]
        r = op6_from_golden_torus["final_r"]
        ratio = R / max(r, 1e-9)
        rel = abs(ratio - PHI_SQ) / PHI_SQ
        assert rel < 0.05, (
            f"GT-seed Op6 converged to R/r = {ratio:.3f}, target φ² = "
            f"{PHI_SQ:.3f}, deviation {rel * 100:.2f}% > 5%. Self-consistent "
            f"eigenmode geometry is not Golden Torus."
        )

    @L3_CLOSURE_XFAIL
    def test_op6_converges_from_perturbed_seed(self, op6_from_perturbed):
        assert op6_from_perturbed["converged"], (
            f"Op6 did NOT converge from perturbed seed within "
            f"{op6_from_perturbed['iterations']} iterations — basin of "
            f"attraction does not span ±30% perturbation."
        )
        R = op6_from_perturbed["final_R"]
        r = op6_from_perturbed["final_r"]
        ratio = R / max(r, 1e-9)
        rel = abs(ratio - PHI_SQ) / PHI_SQ
        assert rel < 0.05, (
            f"Perturbed-seed Op6 converged to R/r = {ratio:.3f}, target "
            f"φ² = {PHI_SQ:.3f}, deviation {rel * 100:.2f}% > 5%."
        )


# ═══════════════════════════════════════════════════════════════════════════
# P_electron_tlm_alpha_derivation
#   α⁻¹ from dynamically-evolved (R_rms, r_rms) matches 137.0363 within 2%.
#   Distinct from P01 (static Golden Torus geometry).
# ═══════════════════════════════════════════════════════════════════════════
class TestAlphaFromDynamicalEigenmode:
    @L3_CLOSURE_XFAIL
    def test_alpha_from_golden_torus_seed(self, op6_from_golden_torus):
        alpha_inv = op6_from_golden_torus["final_alpha_inv"]
        assert alpha_inv is not None and np.isfinite(alpha_inv), (
            f"GT-seed: α⁻¹ = {alpha_inv} — invalid extraction (likely R ≤ r "
            f"or r = 0 at converged geometry)."
        )
        rel = abs(alpha_inv - ALPHA_TARGET) / ALPHA_TARGET
        assert rel < 0.02, (
            f"GT-seed: α⁻¹ = {alpha_inv:.4f}, target {ALPHA_TARGET:.4f}, "
            f"deviation {rel * 100:.2f}% > 2%. Dynamically-evolved eigenmode "
            f"does not carry the Ch 8 multipole geometry that yields 137.036."
        )

    @L3_CLOSURE_XFAIL
    def test_alpha_from_perturbed_seed(self, op6_from_perturbed):
        alpha_inv = op6_from_perturbed["final_alpha_inv"]
        assert alpha_inv is not None and np.isfinite(alpha_inv), (
            f"Perturbed seed: α⁻¹ = {alpha_inv} — invalid extraction."
        )
        rel = abs(alpha_inv - ALPHA_TARGET) / ALPHA_TARGET
        assert rel < 0.02, (
            f"Perturbed seed: α⁻¹ = {alpha_inv:.4f}, target "
            f"{ALPHA_TARGET:.4f}, deviation {rel * 100:.2f}% > 2%."
        )
