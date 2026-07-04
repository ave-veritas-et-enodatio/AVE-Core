"""RETROFIT DEMO — the five-guard adoption on the Stage-2 micropolar Bloch pipeline.

ENGINE-HARDENING ARC item 2 (demonstration consumer). Shows the ~five-line adoption
of the `ave.validation` harness on the newest/cleanest micropolar driver's core
computation: the 6-DOF (u, φ) micropolar Bloch force-constant matrix Φ(k) on the
chiral srs-z3 lattice (`ave.core.micropolar_bloch.micropolar_phi`, the engine Stage-2
`srs_chiral_micropolar` driver builds on this).

WHY a retrofit demo. The Stage-2 micropolar driver's load-bearing verdicts are
"which modes exist / what does the k=0 spectrum do". Before this arc, a "mode absent"
read there would have carried the SAME exposure the Stage-1 blind readout did — no
same-pipeline positive control, no liveness read, no structural-degeneracy guard on
the k=0 acoustic sum. This test wires the harness in and shows each guard firing on
the real Φ(k), so the adoption pattern is copy-pasteable into the driver itself.

THE FIVE-LINE ADOPTION (the copy-paste target, see test_micropolar_five_line_adoption):
    live  = spectral_liveness(seed, Phi0_real)                 # (e) read liveness
    ok_pc = planted_source_control(reader, planted).passed     # (a) positive control
    deg   = detect_global_sum_degeneracy(Phi0_real)            # (b) is the sum forced?
    indep = stub_and_compare(compute, module_path=..., ...)    # (c) runtime independence
    audit = audit_solve_path("…micropolar_bloch.py", ...)      # (d) equation audit

Real-space Brillouin coords; cold linear, sat OFF; α-CLEAN; CONSISTENCY class (this
is instrument-hardening, not a physics claim). mass=A1 untouched.
"""

import numpy as np
import pytest

from ave.core import chiral_lattice as cl
from ave.core.micropolar_bloch import micropolar_phi
from ave.validation import (
    audit_solve_path,
    detect_global_sum_degeneracy,
    planted_source_control,
    spectral_liveness,
    stub_and_compare,
)


def _srs_bonds(enantiomorph="right"):
    """(i, j, delta) minimum-image bond list on the L=1 srs supercell — the same
    bond build the Stage-2 driver's srs_bonds uses."""
    net = cl.build_srs_net(1, enantiomorph)
    a = float(net.box)
    pos = net.pos.copy()
    bonds = []
    for i in range(net.n_nodes):
        for j in net.neighbors[i]:
            d = pos[j] - pos[i]
            d -= a * np.round(d / a)
            bonds.append((i, j, d))
    return pos, bonds


@pytest.fixture(scope="module")
def micropolar():
    """The k=0 micropolar Bloch matrix Φ0 (real) + a random-k Φ for the pipeline."""
    pos, bonds = _srs_bonds("right")
    n = len(pos)
    Phi0 = micropolar_phi(np.zeros(3), pos, bonds, k_axial=1.0, k_shear=0.6, gamma=0.2, kappa_rot=0.3, lever=1.0)
    Phi0_real = np.real(Phi0)  # k=0 Φ is real-symmetric (a rigid body costs no energy)
    return pos, bonds, n, Phi0_real


# ─────────────────────────────────────────────────────────────────────────────
# (e) spectral-liveness — read the seed's live fraction before any verdict
# ─────────────────────────────────────────────────────────────────────────────
def test_retrofit_spectral_liveness(micropolar):
    pos, bonds, n, Phi0 = micropolar
    # a seed orthogonal to the 6-dim k=0 nullspace (3 translation + 3 micro-rotation)
    rng = np.random.default_rng(0)
    seed = rng.standard_normal(6 * n)
    live = spectral_liveness(seed, Phi0, n_bands=6)
    # a generic random seed has most of its energy OUTSIDE the rigid nullspace.
    assert live.live_energy_fraction > 0.5
    # with kappa_rot>0 the micro-rotations are GAPPED; only the 3 uniform translations
    # are exact zero-modes (a rigid SHIFT costs no energy, but a micro-rotation does).
    # Rule-10 finding: the naive "6 rigid modes" assumption is wrong for kappa_rot>0.
    assert live.nullspace_dim == 3


# ─────────────────────────────────────────────────────────────────────────────
# (a) planted-source positive control — the readout can register a KNOWN mode
# ─────────────────────────────────────────────────────────────────────────────
def test_retrofit_planted_source(micropolar):
    pos, bonds, n, Phi0 = micropolar
    from ave.validation import project_out_nullspace

    # readout = elastic energy the mode carries = ‖Φ0·x‖ (zero for a rigid mode).
    def reader(x):
        return float(np.linalg.norm(Phi0 @ x))

    # planted = a KNOWN live mode: a random field projected off the rigid nullspace.
    seed = np.random.default_rng(1).standard_normal(6 * n)
    planted = project_out_nullspace(seed, Phi0)
    res = planted_source_control(reader, planted, floor=1e-9, label="micropolar_live_mode")
    assert res.passed
    assert res.registered  # the elastic reader registers a non-rigid mode
    assert res.baseline < 1e-9  # a zero field carries no energy (no hallucination)


# ─────────────────────────────────────────────────────────────────────────────
# (b) structural-degeneracy — the k=0 GLOBAL translation sum is nullspace-forced
# ─────────────────────────────────────────────────────────────────────────────
def test_retrofit_structural_degeneracy(micropolar):
    pos, bonds, n, Phi0 = micropolar
    # Φ0 annihilates the uniform TRANSLATION (a rigid shift costs no energy), so the
    # translation-weighted global sum wᵀ(Φ0·x) is structurally forced — a "net force
    # along x = 0" read is topology, not physics. For this BLOCK operator the forcing
    # weight is the STRUCTURED translation-null vector (v[0::6]=1), NOT the flat all-
    # ones (Rule-10 finding: the flat-1 default is scalar-operator-only).
    w_transl_x = np.zeros(6 * n)
    w_transl_x[0::6] = 1.0
    res = detect_global_sum_degeneracy(Phi0, weight=w_transl_x)
    assert res.degenerate
    assert not res.safe_to_use
    assert res.kind == "global_sum_nullspace"

    # and the flat-1 weight is NOT forced here (it mixes translation + gapped rotation),
    # so the detector correctly returns safe-to-use for that wrong weight — proving it
    # is not a rubber-stamp.
    res_flat = detect_global_sum_degeneracy(Phi0)
    assert res_flat.safe_to_use


# ─────────────────────────────────────────────────────────────────────────────
# (c) runtime-independence — Φ(k) does not depend on the winding reader
# ─────────────────────────────────────────────────────────────────────────────
def test_retrofit_runtime_independence(micropolar):
    pos, bonds, n, Phi0 = micropolar

    # the micropolar Φ is pure elastic geometry — it must NOT depend on the winding
    # integer reader (a phase-space object). Stub it and demand bit-identity.
    def compute():
        return np.real(
            micropolar_phi(np.zeros(3), pos, bonds, k_axial=1.0, k_shear=0.6, gamma=0.2, kappa_rot=0.3, lever=1.0)
        )

    res = stub_and_compare(
        compute,
        module_path="ave.solvers.srs_cage_winding",
        attr="compute_Q_link_srs",
        stub=lambda *a, **k: {"Q_link": 999999, "w_tor": -7},
        label="Phi_indep_of_winding",
    )
    assert res.passed and res.max_abs_diff == 0.0


# ─────────────────────────────────────────────────────────────────────────────
# (d) equation-audit — the micropolar operator module is α-clean in its own code
# ─────────────────────────────────────────────────────────────────────────────
def test_retrofit_equation_audit():
    def exercise():
        pos, bonds = _srs_bonds("right")
        micropolar_phi(np.zeros(3), pos, bonds)

    res = audit_solve_path("src/ave/core/micropolar_bloch.py", exercise=exercise)
    # the operator module itself routes no α-carrier (it is pure elastic geometry).
    assert res.driver_clean, f"micropolar_bloch falsely flagged: {res.forbidden_in_driver}"


# ─────────────────────────────────────────────────────────────────────────────
# THE five-line adoption, end-to-end — the copy-paste template a driver adopts.
# ─────────────────────────────────────────────────────────────────────────────
def test_micropolar_five_line_adoption(micropolar):
    pos, bonds, n, Phi0 = micropolar
    from ave.validation import project_out_nullspace

    seed = np.random.default_rng(7).standard_normal(6 * n)
    planted = project_out_nullspace(seed, Phi0)

    def reader(x):
        return float(np.linalg.norm(Phi0 @ x))

    w_transl = np.zeros(6 * n)
    w_transl[0::6] = 1.0  # the block operator's null weight

    # ── the five lines a Stage-2 micropolar verdict should run BEFORE it is believed:
    live = spectral_liveness(planted, Phi0)  # (e)
    pc_ok = planted_source_control(reader, planted, floor=1e-9).passed  # (a)
    deg = detect_global_sum_degeneracy(Phi0, weight=w_transl)  # (b)
    indep = stub_and_compare(  # (c)
        lambda: np.real(micropolar_phi(np.zeros(3), pos, bonds)),
        module_path="ave.solvers.srs_cage_winding",
        attr="compute_Q_link_srs",
        stub=lambda *a, **k: {"Q_link": 0},
    ).passed
    audit_ok = audit_solve_path(  # (d)
        "src/ave/core/micropolar_bloch.py",
        exercise=lambda: micropolar_phi(np.zeros(3), pos, bonds),
    ).driver_clean

    # the composite verdict-readiness gate:
    assert live.live_energy_fraction > 0.5
    assert pc_ok  # instrument is live (can register a known mode)
    assert not deg.safe_to_use  # the global sum is forced ⇒ use a resolved read
    assert indep  # Φ does not smuggle the winding integer
    assert audit_ok  # the operator module is α-clean
