"""Regression: LANE W step-0 pair-field FORM multipole analysis.

Locks the three load-bearing invariants of the step-0 verdict
(`research/2026-07-03_lanew-pair-field-form_prereg.md` §3, [MULTIPOLE-FORM]):

  1. LIVENESS: the open-Green's-fn pipeline reads a PLANTED Coulomb pair at
     exponent -1 (attract/repel signs correct) and a planted dipole pair at -3.
     If this fails, the texture exponent is a pipeline artifact and the run is
     VOID. (Guards the periodic-box exponent-steepening artifact the prereg §3.8
     surfaced: the FIX is the open Green's fn, and this test proves it reads -1.)

  2. MONOPOLE ZERO (forced): the A44 gyrotropic-neutral texture around ONE (2,3)
     winding has sum(rho) ~ 0 for BOTH the scalar (engine f_V) and covariant
     (beta DEC) forms -- Gauss-no-boundary (beta note §4.2). No net monopole =>
     the Coulomb FORM cannot fire from a monopole moment.

  3. MULTIPOLE-FORM verdict: the scalar-form pair interaction exponent is
     dipole-dipole (p <= -2.5, NOT Coulomb -1), and the covariant far-field |phi|
     exponent is quadrupole (steeper than dipole). The bin is [MULTIPOLE-FORM].
"""

import importlib.util
import os

import numpy as np

_DRIVER = os.path.join(
    os.path.dirname(__file__),
    "..", "scripts", "vol_4_engineering", "lanew_pair_field_form_step0.py",
)


def _load():
    spec = importlib.util.spec_from_file_location("lanew_step0", os.path.abspath(_DRIVER))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _engine_and_mask(m):
    e = m._build_isolated_knot(m.N, m.R, m.r, lock_on=True, amplitude=m.AMPLITUDE)
    return e, e.interior_mask()


def test_liveness_pipeline_reads_coulomb_minus1():
    """Invariant 1 — planted Coulomb pair -> -1, planted dipole -> -3, signs correct.

    This is the Step-3.8 liveness gate: it certifies the open-Green's-fn pipeline
    is not returning steep exponents by construction. A true monopole pair MUST
    read -1; a true dipole pair MUST read -3. (The periodic-FFT pipeline reads
    -2.8 for a Coulomb pair -- the prereg §3.8 artifact -- so this test also
    guards that the OPEN pipeline, not the periodic one, is the pipeline of record.)
    """
    m = _load()
    _, mask = _engine_and_mask(m)
    live = m.liveness_controls(mask)
    assert live["PASS"], f"liveness controls failed: {live}"
    assert abs(live["unlike_coulomb_exponent"] + 1.0) < 0.05
    assert abs(live["like_coulomb_exponent"] + 1.0) < 0.05
    assert abs(live["planted_dipole_exponent"] + 3.0) < 0.3
    assert live["unlike_all_attract"] and live["like_all_repel"]


def test_a44_texture_monopole_is_zero():
    """Invariant 2 — the A44 neutral texture has zero net monopole (both forms)."""
    m = _load()
    e, mask = _engine_and_mask(m)
    dx = e.dx
    om = e.omega
    for texfn in (m.texture_scalar, m.texture_covariant):
        mp = m.multipoles(texfn(om, dx), mask)
        assert abs(mp["monopole_sum_rho"]) < 1e-12, (
            f"{texfn.__name__} texture not neutral: sum(rho)={mp['monopole_sum_rho']}")
        # the texture is REAL (nonzero unsigned charge) -- not a trivial zero field
        assert mp["sum_abs_rho"] > 0.1


def test_multipole_form_verdict():
    """Invariant 3 — scalar pair exponent is dipole-dipole (NOT Coulomb -1),
    covariant far-field is quadrupole -> bin [MULTIPOLE-FORM]."""
    m = _load()
    e, mask = _engine_and_mask(m)
    scalar = m.analyze_texture("S", m.texture_scalar, e, mask)
    covariant = m.analyze_texture("C", m.texture_covariant, e, mask)
    live = m.liveness_controls(mask)

    pS = scalar["pair"]["exponent_clean"]
    # scalar (engine f_V) form: clean dipole-dipole exponent, well steeper than -1
    assert np.isfinite(pS)
    assert pS <= -2.5, f"scalar exponent {pS} not multipole (dipole-dipole ~ -3)"
    assert abs(pS + 1.0) > 0.5, f"scalar exponent {pS} is Coulomb-close -- not expected"
    # covariant form: dipole vanishes, far-field |phi| is quadrupole-steep
    assert covariant["multipoles"]["dipole_mag"] < 1e-6
    assert covariant["far_field_phi_exponent"] < -2.0

    bin_name, _ = m.classify(scalar, covariant, live)
    assert bin_name == "MULTIPOLE-FORM", f"expected MULTIPOLE-FORM, got {bin_name}"
