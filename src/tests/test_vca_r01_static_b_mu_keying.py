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

THE LIVE BUG (VCA-R01, documented; fix flagged for a separate validated PR):
  src/ave/core/fdtd_3d.py:231,:245,:396-397,:425-426 and
  src/ave/axioms/scale_invariant.py:198 key mu-saturation on the STATIC field
  magnitude B_local = mu_0 * |H| against b_yield = B_SNAP. B_SNAP is an
  ENERGY-DENSITY scale (B_SNAP^2/2mu0 = m_e c^2 / l_node^3 = 1), NOT the
  mu-grade kernel argument (which is I/I_max). So the current code SATURATES
  mu under a large static B, contradicting (a) the I-keyed relativistic-inductor
  primitive and (b) the engine's own Lenz/Faraday coupling (a static B has no
  dB/dt to induce internal circulation).

WHY THE FIX IS NOT APPLIED IN THIS PR (flag-don't-guess; substrate-first):
  The correct I-keyed implementation is subtle/ambiguous and NOT yet derived:
    1. No per-cell circulation -> I_max threshold mapping exists in the corpus.
       Keying on I = closed-loop integral of H . dl (or the rate dB/dt) and
       mapping it onto I_max = xi_topo*c = 124.4 A on a Yee grid is a DERIVATION,
       not a variable swap; inventing the threshold would violate
       substrate-first-for-numbers.
    2. Two distinct mu-saturation paths coexist — the simple mu_eff(|B|) here
       and the chirality-aware _update_saturation_kernels(omega, ...) in
       cosserat_field_3d.py. A correct fix must reconcile both.
    3. scale_invariant.mu_eff() is called from 8 modules (yang_mills, plasma,
       gravity, solvers, ...) passing a B-magnitude; changing its semantics
       ripples through all of them and needs each re-validated.

  This test is marked xfail(strict=False): it ENCODES the desired R3 behaviour
  (static B -> S_mu = 1) so the eventual validated fix flips it to PASS. Until
  then it documents the bug as a live, machine-checked TODO rather than a prose
  note. See node-up-small-large-signal.md:S5 (VCA-R01 code note).
"""

import numpy as np
import pytest

from ave.core.fdtd_3d import FDTD3DEngine


@pytest.mark.xfail(
    reason="VCA-R01: mu-grade keys on static |B| (=mu0|H|) vs b_yield=B_SNAP, "
    "not on circulating current I. A large STATIC B must give S_mu=1 / "
    "mu_eff=mu0 (relativistic inductor, no dB/dt -> no internal circulation). "
    "Fix flagged for a separate validated PR (I-keyed threshold not yet "
    "derived; substrate-first — do not guess). "
    "See node-up-small-large-signal.md:S5.",
    strict=False,
)
def test_static_external_B_leaves_mu_unloaded():
    """A static (DC) external B near b_yield must NOT saturate the mu-grade.

    Desired (R3, I-keyed): S_mu = 1, mu_eff = mu_0, delta_n_mu = 0 exactly,
    independent of |B|. Current code (|B|-keyed) instead drives mu_eff -> 0 as
    |B| -> b_yield, so this assertion fails (xfail) until VCA-R01 is fixed.
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


def test_static_B_keying_bug_is_present_as_documented():
    """Positive control: confirm the |B|-keyed defect IS present as described,
    so the xfail above is documenting a real live bug (not a phantom).

    With |B|-keying, a static |B| = 0.9*b_yield drives S_mu = sqrt(1-0.9^2)
    ~= 0.436, i.e. mu_eff is materially below mu_0. This test PASSES on the
    current (buggy) code and will need updating WHEN VCA-R01 is fixed.
    """
    eng = FDTD3DEngine(nx=8, ny=8, nz=8, dx=0.01, linear_only=False)
    H_target = 0.9 * eng.b_yield / eng.mu_0
    Hx_static = np.full((eng.nx, eng.ny, eng.nz), H_target)

    mu_eff = eng._compute_local_mu(Hx_static)
    expected_buggy = eng.mu_0 * np.sqrt(1.0 - 0.9**2)

    assert np.allclose(np.mean(mu_eff), expected_buggy, rtol=1e-3), (
        "Expected the documented |B|-keyed behaviour (mu_eff = mu_0*sqrt(1-0.81)). "
        "If this fails, VCA-R01 may already be fixed — update both tests."
    )
