"""Tests for the electron π₁ / spin-½ SELECTION analytical-topology result.

Locks the load-bearing claims of research/2026-07-08_electron-pi1-spinhalf_result.md:
  - π₁(SO(3)) = ℤ₂ (2π→−I, 4π→+I), demonstrated by the continuity-tracked lift.
  - The 2π spin loop is winding-INDEPENDENT (−I for every (p,q)) ⇒ selection admitted, not forced.
  - The (p,q) texture class = (p mod 2, q mod 2); (2,3) is (0,1), non-liftable via the ODD q=3 cycle.
  - ℤ₃ (L(3,1), |Δ_trefoil(−1)|=3) is the branched-cover-of-ambient invariant, distinct from Q.
  - ANTI-TAUTOLOGY: the derivation source never supplies a cos(φ/2)/exp(iσ·φ/2) half-angle INPUT.
"""

import inspect
import io
import tokenize

import scripts.vol_2_subatomic.electron_pi1_spinhalf_topology as mod


def _executable_code_only(src: str) -> str:
    """Return the module source with ALL string literals and comments blanked out,
    so an anti-tautology token scan sees only executable code — not docstrings or
    print-message labels that legitimately NAME the forbidden half-angle lift in
    order to say it is avoided."""
    out_tokens = []
    for tok in tokenize.generate_tokens(io.StringIO(src).readline):
        if tok.type in (tokenize.STRING, tokenize.COMMENT):
            continue
        out_tokens.append(tok.string)
    return " ".join(out_tokens)


def test_pi1_so3_is_z2_belt_trick():
    r = mod.pi1_so3_monodromy()
    assert r["monodromy_2pi"] == -1.0 or abs(r["monodromy_2pi"] + 1.0) < 1e-6
    assert abs(r["monodromy_4pi"] - 1.0) < 1e-6


def test_spin_loop_winding_independent_selection_not_forced():
    # The 2π global-rotation loop gives −I for EVERY winding; 4π gives +I.
    for p, q in [(2, 3), (2, 2), (1, 1), (3, 5)]:
        s = mod.spin_loop_monodromy(p, q)
        assert abs(s["spin_monodromy_2pi"] + 1.0) < 1e-6, (p, q)
        assert abs(s["spin_monodromy_4pi"] - 1.0) < 1e-6, (p, q)
    # Two characters ⇒ both quantizations admitted ⇒ topology does not FORCE.
    assert sorted(mod.character_set_z2()) == [-1, 1]


def test_texture_class_parity_dependent_but_distinct_from_spin():
    t = mod.texture_class(2, 3)
    assert t["H1_class_mod2"] == (0, 1)  # ODD q=3 activates the non-trivial cycle
    assert t["su2_liftable"] is False  # (2,3) does NOT globally lift to SU(2)
    assert abs(t["phi_cycle_monodromy"] - 1.0) < 1e-6  # (−1)^2 = +1
    assert abs(t["psi_cycle_monodromy"] + 1.0) < 1e-6  # (−1)^3 = −1
    # Contrast: both-even winding DOES lift (no texture obstruction).
    assert mod.texture_class(2, 2)["su2_liftable"] is True


def test_z3_is_branched_cover_of_ambient_not_config_space():
    z = mod.z3_branched_cover_order(2, 3)
    assert z["alexander_at_minus1"] == 3
    assert z["pi1_branched_cover_order"] == 3  # L(3,1), π₁ = ℤ₃ — distinct from Q's ℤ₂


def test_anti_tautology_no_half_angle_lift_on_path():
    """The ℤ₂ must trace to SO(3)'s own π₁, NOT to an inserted spinor. Assert the
    EXECUTABLE code (strings + comments stripped) contains no Pauli/σ spinor ansatz
    and no exp/half-angle rotor. (The half-angle appears only as an OUTPUT of the
    external Shepperd matrix→quaternion decomposition, which takes a full-angle
    MATRIX as input; docstrings/print-labels may NAME the forbidden lift to say it
    is avoided — those are excluded from the scan.)"""
    code = _executable_code_only(inspect.getsource(mod))
    forbidden_names = ["sigma", "Pauli", "pauli", "expm", "expi"]
    for tok in forbidden_names:
        assert tok not in code, f"anti-tautology: forbidden spinor token {tok!r} in executable code"
    # No numpy/scipy exponential-of-a-matrix rotor and no explicit half-angle division:
    assert "np.exp" not in code and "sp.exp" not in code
    assert "/ 2" not in code and "* 0.5" not in code and "0.5 *" not in code


def test_rot_z_uses_full_angle_not_half():
    # rot_z(2π) must equal identity (full-angle SO(3)); a half-angle rotor would give −I-like behavior.
    import numpy as np

    assert np.allclose(mod.rot_z(2.0 * np.pi), np.eye(3), atol=1e-9)
    assert np.allclose(mod.rot_z(np.pi) @ mod.rot_z(np.pi), np.eye(3), atol=1e-9)
