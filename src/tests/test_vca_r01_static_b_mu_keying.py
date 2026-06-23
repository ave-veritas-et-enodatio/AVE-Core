"""VCA-R01 regression: the magnetic (mu) grade must key on the circulating
CURRENT I (relativistic inductor), NOT on the static |B| magnitude.

Canonical physics (verified node-up, grep-confirmed at origin/main):
  - mu-grade = ideal relativistic INDUCTOR, L_eff(I) = L_0 / S(I/I_max),
    I_max = xi_topo * c ~= 124.4 A
    (manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/
     relativistic-inductor.md:15,:18; node-up-small-large-signal.md:S2-S4).
  - A STATIC external B (dB/dt = 0, sustained by the magnet's transport
    current, NOT by the vacuum's circulation) induces NO internal vacuum
    circulation -> I_vac = 0 -> A_I = 0 -> S_mu = 1 -> mu_eff = mu_0 ->
    delta_n_mu = 0 EXACTLY (regime R3; PVLAS/BMV static-B null is therefore
    CONSISTENT with AVE, not a falsification —
    manuscript/ave-kb/vol4/falsification/ch11-experimental-bench-falsification/
    pvlas-static-b-verdict.md).

VCA-R01 (FIXED): the free-EM mu-channel is now LINEAR (mu_eff = mu_0).
  The mu-grade is the relativistic inductor; it saturates only as the circulating
  current reaches c, i.e. as the circulation rate omega -> omega_C = c/l_node
  ~= 7.76e20 rad/s (f_C ~= 1.24e20 Hz; gamma-ray scale, hbar*omega_C = m_e c^2 =
  511 keV). Any wave a Yee EM engine can represent runs
  at omega << omega_C (omega/omega_C <~ 1e-6 even at optical), so
  S_mu = sqrt(1 - (omega/omega_C)^2) = 1 to machine precision; a static external B
  (dB/dt = 0) likewise induces no circulation, so S_mu = 1 exactly (regime R3).
  The earlier code keyed mu on the static amplitude |B| = mu_0*|H| against
  b_yield = B_SNAP — wrong twice over: B_SNAP is an energy-density scale, not the
  kernel argument, and amplitude is not the circulation rate.

  The fix is LOCAL to the fdtd-vacuum caller (fdtd_3d._compute_local_mu, the two
  energy readouts, and the JAX twin fdtd_3d_jax._compute_local_mu_kernel).
  scale_invariant.mu_eff() is UNCHANGED — it is the sector-agnostic kernel used by
  genuine static-B MATTER callers (superconductor.meissner_mu_eff, yang_mills),
  correct as-is. A free wave saturates mu only as omega -> omega_C, the dispersive
  lattice cutoff (hbar*omega_C = m_e c^2 = 511 keV); this coarse-grid engine never
  reaches omega_C (a dispersive-mu(omega) model handles the cutoff — separate
  workstream). Bound/self-trapped circulation saturates mu at any frequency (Cosserat
  engine, cosserat_field_3d._compute_saturation_factors, keyed on micro-rotation
  curvature).

  test_static_external_B_leaves_mu_unloaded now PASSES (was xfail). The companion
  test guards against regression to the old |B|-amplitude keying.
  See node-up-small-large-signal.md:S5 (VCA-R01 code note, RESOLVED).
"""

import numpy as np

from ave.core.fdtd_3d import FDTD3DEngine


def test_static_external_B_leaves_mu_unloaded():
    """A static (DC) external B near b_yield must NOT saturate the mu-grade.

    R3 (VCA-R01 fixed): S_mu = 1, mu_eff = mu_0, delta_n_mu = 0 exactly,
    independent of |B| — the free-EM mu-channel is linear, so a static external
    B carries no induced circulation and leaves mu unloaded.
    """
    eng = FDTD3DEngine(nx=8, ny=8, nz=8, dx=0.01, linear_only=False)

    # Impose a strong, STATIC, spatially-uniform H => |B| ~ 0.9 * b_yield.
    # Static = imposed once, no time evolution (dB/dt = 0). This is the PVLAS
    # magnet case: the field is sustained externally, not by vacuum circulation.
    H_target = 0.9 * eng.b_yield / eng.mu_0
    Hx_static = np.full((eng.nx, eng.ny, eng.nz), H_target)

    mu_eff = eng._compute_local_mu(Hx_static)

    # I-keyed primitive: a static external B carries no internal circulation
    # (I_vac = 0, A_I = 0) so S_mu = 1 and mu_eff = mu_0 EXACTLY.
    assert np.allclose(mu_eff, eng.mu_0, rtol=1e-9), (
        "Static external B must leave the mu-grade unloaded (S_mu=1, "
        f"mu_eff=mu_0={eng.mu_0:.6e}); got mu_eff={np.mean(mu_eff):.6e}. "
        "The engine is keying mu-saturation on static |B| instead of the "
        "circulating current I (VCA-R01)."
    )


def test_static_B_does_not_amplitude_saturate_mu():
    """Regression guard: the OLD |B|-amplitude keying must stay gone.

    Under the removed bug a static |B| = 0.9*b_yield drove
    mu_eff = mu_0*sqrt(1-0.9^2) ~= 0.436*mu_0. After VCA-R01 the free-EM mu is
    linear, so mu_eff = mu_0 and is nowhere near that old saturated value. If this
    regresses, the |B|-amplitude keying has returned.
    """
    eng = FDTD3DEngine(nx=8, ny=8, nz=8, dx=0.01, linear_only=False)
    H_target = 0.9 * eng.b_yield / eng.mu_0
    Hx_static = np.full((eng.nx, eng.ny, eng.nz), H_target)

    mu_eff = eng._compute_local_mu(Hx_static)
    old_buggy = eng.mu_0 * np.sqrt(1.0 - 0.9**2)

    assert np.allclose(mu_eff, eng.mu_0, rtol=1e-12), (
        "Free-EM mu must be linear (mu_eff = mu_0) under a static B (VCA-R01)."
    )
    assert not np.allclose(np.mean(mu_eff), old_buggy, rtol=1e-2), (
        "mu_eff collapsed toward the OLD |B|-amplitude-saturated value — "
        "the VCA-R01 |B|-keying has regressed."
    )
