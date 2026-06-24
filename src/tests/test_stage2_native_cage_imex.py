"""Stage-2 NATIVE-CAGE IMEX — VALIDATION GATES (run BEFORE the make-or-break).

Prereg : research/2026-06-23_engine-stage2-native-cage_prereg.md (RE-FROZEN).
Companion explicit gates : src/tests/test_stage2_native_cage_run.py (G1-G8).

The IMEX changes ONLY the time-integration (explicit leapfrog → frozen-D
Crank–Nicolson). The operator/sign/CFL MATH is UNCHANGED, so the explicit G1-G8
still bind. These IMEX gates add:

  GX1  OPERATOR-UNCHANGED: the IMEX sparse L_D (assemble_L_D over TETRA_OFFSETS)
       reproduces the VALIDATED dense native operator
       graded_vacuum_network._native_laplacian_with_stiffness to machine eps,
       and is symmetric PSD. (Proves the IMEX did not perturb the G1-G8 math.)
  GX2  THE ENERGY-CONSERVATION / NO-SPURIOUS-DAMPING GATE (the IMEX-specific
       rigor guard — the analog of the explicit sign-check). Lossless linear
       limit (EM port closed, small amp): the IMEX must CONSERVE energy with NO
       secular decay. If it bleeds, it is over-damped and CANNOT call Mode-I vs
       Mode-III → the instrument is unreliable.
  GX3  BACKWARD-EULER IS DISSIPATIVE (negative control for GX2): the rejected
       backward-Euler form (I + dt²c0²L_D)V^{n+1}=2V^n−V^{n-1} DOES bleed energy
       on the same lossless linear cage — proving GX2 is a live discriminator
       (a damping scheme fails it), so a PASS is meaningful.
  GX4  UNCONDITIONAL STABILITY: the IMEX stays BOUNDED at a dt WELL ABOVE the
       explicit blow-up CFL on the stiff saturated operator (where explicit
       detonates) — the whole point of going implicit.

α-CLEAN: pure (1−A²) kernel; no ALPHA / Q_TANK / 137 / 0.00729 anywhere.
"""

import numpy as np

from ave.solvers.graded_vacuum_network import (
    _native_laplacian_with_stiffness,
    stiffness_profile,
)
from ave.solvers.native_cage_imex import (
    NativeCageIMEX,
    NativeCageIMEXConfig,
    assemble_L_D,
    build_grad_div_periodic,
    energy_conservation_gate,
)


# ── GX1: the IMEX operator IS the validated native operator (unchanged math) ──
def test_GX1_imex_sparse_LD_matches_validated_dense_operator():
    """The IMEX sparse L_D = Div·diag(D)·Grad (over TETRA_OFFSETS) must reproduce
    the validated dense _native_laplacian_with_stiffness EXACTLY, and be
    symmetric PSD. This is the 'operator unchanged' proof — IMEX only changes
    the time-stepper, NOT the spatial operator the G1-G8 validated."""
    N = 12
    rng = np.random.default_rng(3)
    V = rng.standard_normal((N, N, N))
    c = N // 2
    r = np.sqrt(((np.indices((N, N, N)) - c) ** 2).sum(0))
    A = np.minimum(0.85 / np.cosh(r / 2.5), 0.999)
    D = stiffness_profile(A, exponent=0.5, S_min=1e-3)

    Grad, Div = build_grad_div_periodic(N)
    L = assemble_L_D(Grad, Div, D)
    sparse_action = (L @ V.reshape(-1)).reshape(N, N, N)
    dense_action = _native_laplacian_with_stiffness(V, D)
    err = float(np.abs(sparse_action - dense_action).max())
    assert err < 1e-12, f"IMEX sparse L_D must match validated dense op, got {err:.2e}"

    asym = float(abs(L - L.T).max())
    assert asym < 1e-12, f"L_D must be symmetric, asymmetry {asym:.2e}"
    ev_min = float(np.linalg.eigvalsh(L.toarray()).min())
    assert ev_min > -1e-9, f"L_D must be PSD (min eig ≥ 0), got {ev_min:.2e}"


# ── GX2: THE energy-conservation / no-spurious-damping gate (the rigor guard) ──
def test_GX2_energy_conservation_no_spurious_damping():
    """LOSSLESS LINEAR LIMIT, EM port CLOSED, small amplitude: the IMEX must
    conserve energy with NO secular decay over many periods. PASS ⇒ the IMEX
    cannot be faking a 'bounded persistent core' by damping. FAIL ⇒ the
    instrument is unreliable and the make-or-break MUST NOT run."""
    g = energy_conservation_gate(N=16, amplitude=0.02, n_steps=600)
    assert g["passed"], (
        "ENERGY-CONSERVATION GATE FAILED — the IMEX is over-damped (spurious "
        f"dissipation): rel_drift_end={g['rel_drift_end']:.2e}, "
        f"secular_slope={g['secular_slope_per_time']:.2e}, "
        f"1/Q_num={g['inv_Q_numerical']:.2e}. The instrument CANNOT call Mode-I "
        "vs Mode-III — HALT."
    )
    # The effective numerical 1/Q must be ≪ any physical effect (O(1) over run).
    assert abs(g["inv_Q_numerical"]) < 1e-3, (
        f"numerical 1/Q={g['inv_Q_numerical']:.2e} not ≪ physical effect"
    )
    assert g["n_periods_resolved"] >= 5.0, (
        f"gate must span ≥5 periods, got {g['n_periods_resolved']:.1f}"
    )


# ── GX3: backward-Euler IS dissipative (negative control — GX2 is live) ──
def test_GX3_backward_euler_bleeds_energy_negative_control():
    """NEGATIVE CONTROL for GX2: the REJECTED backward-Euler form
    (I + dt²c0²L_D)V^{n+1}=2V^n−V^{n-1} DOES bleed energy on the same lossless
    linear cage. This proves the energy gate is a LIVE discriminator (a damping
    scheme fails it), so the CN PASS in GX2 is meaningful, not vacuous."""
    N = 16
    cfg = NativeCageIMEXConfig(N=N)
    eng = NativeCageIMEX(cfg)
    eng.em_port_closed = True
    eng.seed_sech(amplitude=0.02, radius=2.5)
    eng.set_dt_accuracy()

    from scipy.sparse import identity
    from scipy.sparse.linalg import cg

    ndof = N**3
    H0 = eng.total_energy()
    # backward-Euler step: (I + dt²c0²L_D)V^{n+1} = 2V^n − V^{n-1}  (NO ¼, NO LHS-avg)
    for _ in range(600):
        D = eng.stiffness_D()
        L_D = assemble_L_D(eng.Grad, eng.Div, D)
        coef = (eng.dt**2) * (eng.c0**2)
        v = eng.V.reshape(ndof)
        v_prev = eng.V_prev.reshape(ndof)
        rhs = 2.0 * v - v_prev
        A_sys = (identity(ndof, format="csr") + coef * L_D).tocsr()
        v_new, _ = cg(A_sys, rhs, rtol=1e-10, maxiter=2000, x0=v)
        eng.V_prev = eng.V.copy()
        eng.V = v_new.reshape(N, N, N)
        eng.time += eng.dt
    H_end = eng.total_energy()
    bleed = (H0 - H_end) / H0
    assert bleed > 0.05, (
        f"backward-Euler MUST bleed energy (it is dissipative), got bleed={bleed:.3e}; "
        "if ≈0 the energy gate is not discriminating and GX2 is vacuous"
    )


# ── GX4: unconditional stability above the explicit blow-up CFL ──
def test_GX4_imex_stable_above_explicit_blowup_cfl():
    """The IMEX stays BOUNDED at a dt WELL ABOVE the explicit CFL on a strongly-
    self-focusing sech (where the explicit leapfrog detonated, results JSON
    dt_robustness peak→15.6). dt_accuracy_factor=4 (≈4× the cold CFL); the
    explicit stepper at comparable fine dt blew up — the IMEX must not."""
    cfg = NativeCageIMEXConfig(N=16, dt_accuracy_factor=4.0)
    eng = NativeCageIMEX(cfg)
    eng.seed_sech(amplitude=0.85, radius=2.5)
    eng.set_dt_accuracy()
    mx = 0.0
    for _ in range(200):
        eng.step()
        mx = max(mx, float(np.abs(eng.V).max()))
        if not np.isfinite(mx):
            break
    assert np.isfinite(mx), "IMEX produced non-finite values (unconditional stability violated)"
    assert mx < 10.0, f"IMEX must stay bounded (<10 DETONATION_MAX_V), got {mx:.3f}"
