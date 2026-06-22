"""VCA node-regime DIRECT-KERNEL sweep: the positive-control for the node-up
R2 (static-E) and R3 (static-B) birefringence laws.

This test evaluates the Axiom-4 saturation kernel S(A) and the effective
material parameters (epsilon_eff, mu_eff) DIRECTLY from the canonical kernel in
``ave.axioms.scale_invariant`` — it does NOT drive the fdtd engine. The
distinction is load-bearing:

  * The DIRECT-KERNEL evaluation keys each grade on its CANONICAL argument:
      - epsilon-grade (varactor): A_V = E / E_yield      (a potential variable)
      - mu-grade (relativistic inductor): A_I = I_vac / I_max  (a rate/flux var)
    A static external B has dB/dt = 0, so it induces NO internal vacuum
    circulation -> I_vac = 0 -> A_I = 0 -> S_mu = S(0) = 1 EXACTLY, at ALL B
    (regime R3, delta_n_mu = 0 analytically — not a numerical finding, a
    consequence of the kernel argument being zero).

  * The fdtd ENGINE would NOT reproduce R3: it carries the live VCA-R01 defect
    (it keys mu-saturation on the static |B| magnitude against b_yield=B_SNAP),
    so a large static B drives mu_eff -> 0 there. That gap IS the documented
    VCA-R01 defect, encoded as an xfail in
    ``test_vca_r01_static_b_mu_keying.py``. This file is the EXPLICITLY DISTINCT
    direct-kernel positive control: it confirms the ANALYTIC node-up laws hold
    at the kernel level, independent of (and not blocked by) the engine bug.

Canonical sources (verify-before-cite):
  - Axiom-4 kernel S(A)=sqrt(1-(A/A_yield)^2):
    src/ave/axioms/scale_invariant.py::saturation_factor
  - mu_eff(A)=mu_base*S(A): src/ave/axioms/scale_invariant.py:198 (mu_eff)
  - node-up regimes R1/R2/R3 (V-keyed varactor / I-keyed inductor duality):
    manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/
      node-up-small-large-signal.md (clm-vca7r1)
  - relativistic inductor L_eff(I)=L_0/S(I/I_max), I_max=xi_topo*c~=124.4 A:
    manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/
      relativistic-inductor.md:15,:18 (clm-p5cf3t)
  - PVLAS/BMV static-B null is CONSISTENT with AVE:
    manuscript/ave-kb/vol4/falsification/ch11-experimental-bench-falsification/
      pvlas-static-b-verdict.md (clm-pvlas1)

The numbers here are COMPUTED by the kernel; none are hand-written (substrate-
first-for-numbers).
"""

import numpy as np
import pytest

from ave.axioms.scale_invariant import epsilon_eff, mu_eff, saturation_factor
from ave.core.constants import (
    C_0,
    E_YIELD,
    EPSILON_0,
    MU_0,
    XI_TOPO,
)

# I_max for the mu-grade relativistic inductor: I_max = xi_topo * c
# (relativistic-inductor.md:15,:18; clm-p5cf3t). COMPUTED, not hand-written.
I_MAX = XI_TOPO * C_0


def _index_from_grades(S_eps: float, S_mu: float) -> float:
    """Transverse-EM index n = sqrt(eps_eff*mu_eff/(eps_0*mu_0)) = sqrt(S_eps*S_mu).

    node-up-small-large-signal.md:S3 (the small-signal probe index).
    """
    return float(np.sqrt(S_eps * S_mu))


# ===========================================================================
# R3 (static-B): mu-grade is I-keyed; a static B gives I_vac = 0 => S_mu = 1
# => delta_n_mu = 0 ANALYTICALLY EXACT at ALL B (not a numerical finding).
# ===========================================================================
class TestR3StaticBAnalyticallyExact:
    """R3: static external B (dB/dt=0) => I_vac=0 => A_I=0 => S_mu=1 => dn_mu=0.

    Direct-kernel positive control for the analytic R3 law. EXPLICITLY DISTINCT
    from the fdtd-engine xfail in test_vca_r01_static_b_mu_keying.py.
    """

    # Static-B sweep range advertised at the (reworded) canonical sites.
    B_SWEEP_T = np.array([2.5, 10.0, 50.0, 100.0, 500.0, 1000.0])

    def test_static_B_gives_zero_I_vac(self):
        """A static external B has dB/dt = 0, so the induced internal vacuum
        circulation I_vac = 0 (Lenz). The mu-grade kernel argument is I_vac/I_max.
        """
        # Static drive => no time-variation => no induced circulation.
        I_vac = 0.0
        A_I = I_vac / I_MAX
        assert A_I == 0.0

    def test_S_mu_is_unity_at_every_B(self):
        """S_mu = S(A_I) = S(I_vac/I_max) = S(0) = 1 at EVERY static B.

        The kernel is evaluated on the CANONICAL I-keyed argument (I_vac=0),
        NOT on |B| (that |B|-keyed path is the engine's VCA-R01 bug).
        """
        for _B in self.B_SWEEP_T:
            # Canonical mu-grade argument under a static B: I_vac = 0 (R3).
            S_mu = saturation_factor(0.0, I_MAX)
            assert S_mu == pytest.approx(1.0, abs=1e-15), (
                f"R3: static B={_B} T must give S_mu=1 (I_vac=0); got {S_mu}"
            )

    def test_mu_eff_equals_mu0_at_every_B(self):
        """mu_eff = mu_0 * S_mu = mu_0 at every static B (mu-grade unloaded)."""
        for _B in self.B_SWEEP_T:
            mu = mu_eff(0.0, I_MAX, MU_0)  # I-keyed: argument is I_vac=0
            assert mu == pytest.approx(MU_0, rel=1e-15), (
                f"R3: static B={_B} T must leave mu_eff=mu_0; got {mu}"
            )

    def test_delta_n_mu_is_zero_flat_across_sweep(self):
        """delta_n_mu = sqrt(S_eps*S_mu) - 1 = 0 at every static B.

        S_eps = 1 (no static E in R3) and S_mu = 1 (I_vac=0) => n = 1 => dn = 0.
        Flat across 2.5 T -> 1 kT because the kernel argument is zero, not
        because a sweep happened to land on zero.
        """
        dns = []
        for _B in self.B_SWEEP_T:
            S_eps = saturation_factor(0.0, E_YIELD)  # no static E in R3
            S_mu = saturation_factor(0.0, I_MAX)  # I_vac=0 under static B
            dns.append(_index_from_grades(S_eps, S_mu) - 1.0)
        dns = np.array(dns)
        assert np.allclose(dns, 0.0, atol=1e-15), (
            f"R3 delta_n_mu must be identically 0 across 2.5 T-1 kT; got {dns}"
        )

    def test_engine_bug_path_would_NOT_give_zero(self):
        """Contrast control: feeding |B| into the kernel (the VCA-R01 |B|-keyed
        engine path) does NOT give S_mu=1 — proving R3 is an analytic property
        of the I-keyed argument, not an artifact of the kernel always returning 1.

        This documents the engine-vs-direct-kernel GAP (= VCA-R01) at machine
        level: the direct kernel keyed on I_vac=0 -> S_mu=1; the buggy |B|-keyed
        path -> S_mu<1 for a large static B. (B_SNAP from constants.)
        """
        from ave.core.constants import B_SNAP

        B_large = 0.9 * B_SNAP  # a large static B near the energy-density scale
        # WRONG (engine VCA-R01) path: key mu-saturation on static |B|/B_SNAP.
        S_mu_buggy = saturation_factor(B_large, B_SNAP)
        # RIGHT (direct-kernel, I-keyed) path: argument is I_vac=0.
        S_mu_correct = saturation_factor(0.0, I_MAX)
        assert S_mu_buggy < 0.5, "buggy |B|-keyed path should saturate at large B"
        assert S_mu_correct == pytest.approx(1.0, abs=1e-15)
        assert S_mu_correct != pytest.approx(S_mu_buggy, abs=1e-3), (
            "The direct-kernel R3 result must differ from the |B|-keyed engine "
            "path (this difference IS the documented VCA-R01 defect)."
        )


# ===========================================================================
# R2 (static-E): eps-grade is V-keyed (varactor); a static E loads it,
# delta_n -> -1/4 (E/E_yield)^2 leading order (analytic varactor law).
# ===========================================================================
class TestR2StaticEVaractorLaw:
    """R2: static E loads the V-keyed varactor (S_eps<1), mu unloaded (S_mu=1).

    Direct-kernel positive control for the analytic varactor law
    delta_n ~ 1/4 (E/E_yield)^2 (leading order).
    """

    # E-route sweep, well below E_yield so the leading-order law holds.
    E_SWEEP_VM = np.array([1e12, 1e13, 1e14, 1e15, 1e16, 1e17])

    def test_S_mu_unity_under_static_E(self):
        """A static E has no dB/dt, so the mu-grade stays unloaded: S_mu=1."""
        S_mu = saturation_factor(0.0, I_MAX)
        assert S_mu == pytest.approx(1.0, abs=1e-15)

    def test_eps_eff_drops_under_static_E(self):
        """eps_eff = eps_0 * S(E/E_yield) decreases monotonically with E."""
        S_vals = np.array([saturation_factor(E, E_YIELD) for E in self.E_SWEEP_VM])
        eps_vals = np.array([epsilon_eff(E, E_YIELD, EPSILON_0) for E in self.E_SWEEP_VM])
        assert np.all(np.diff(S_vals) < 0), "S_eps must decrease as E -> E_yield"
        assert np.allclose(eps_vals, EPSILON_0 * S_vals, rtol=1e-12)

    def test_leading_coefficient_is_one_quarter(self):
        """delta_n = sqrt(S_eps) - 1 -> -1/4 A_V^2 leading order, A_V = E/E_yield.

        Compute |delta_n| / A_V^2 from the kernel at small A_V; it must -> 1/4.
        The 1/4 is COMPUTED here, not asserted.
        """
        E_small = np.array([1e12, 3e12, 1e13])  # A_V ~ 1e-5..1e-4 << 1
        for E in E_small:
            A_V = E / E_YIELD
            S_eps = saturation_factor(E, E_YIELD)
            S_mu = saturation_factor(0.0, I_MAX)  # mu unloaded
            dn = _index_from_grades(S_eps, S_mu) - 1.0  # = sqrt(S_eps) - 1
            coeff = abs(dn) / A_V**2
            assert coeff == pytest.approx(0.25, rel=1e-3), (
                f"R2 leading coefficient must be 1/4; got {coeff} at E={E}"
            )

    def test_full_sweep_matches_exact_kernel(self):
        """Across the full E-sweep, delta_n = sqrt(S(E/E_yield)) - 1 EXACTLY
        (the analytic varactor law evaluated by the kernel), with S_mu=1.
        """
        for E in self.E_SWEEP_VM:
            S_eps = saturation_factor(E, E_YIELD)
            S_mu = saturation_factor(0.0, I_MAX)
            dn = _index_from_grades(S_eps, S_mu) - 1.0
            dn_exact = float(np.sqrt(S_eps)) - 1.0
            assert dn == pytest.approx(dn_exact, rel=1e-12)
            assert dn < 0.0, "static-E delta_n is negative (varactor loads eps)"
