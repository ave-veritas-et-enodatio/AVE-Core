"""
Keeper unit tests for the sonic-horizon handedness OAM probe (R1 follow-up).

Pins the probe-validity FIX for the 2026-06-10 sonic-horizon-closure panel
follow-up. The prior probe set the density perturbation as

    sonic_horizon_flow.py:184  ->  dens = amp * ring * np.cos(m * phi)

which is EVEN in m (cos(mφ) = cos(−mφ)), so the +m (co) and −m (counter) probes
were BIT-IDENTICAL fields. The reported handedness "asym = 0.0000" was therefore
the PROBE's m-symmetry, not the medium's, and the handedness BLIND verdict was an
artifact (see research/2026-06-10_sonic-horizon-closure_result.md, Verdict
Addendum §1 / §4-bis). The prereg §2.2 froze a genuine e^{imφ} winding.

This defect class is INVISIBLE to `make verify` — the engine integrates and
conserves energy/momentum fine with the broken probe; only a +m-vs-−m comparison
exposes it. These tests are the keeper.

Pins:
  1. +m and −m injected fields are PHYSICALLY DISTINCT (not bit-identical, and
     not a trivial global sign-flip — which would also give R(+m)=R(−m) since
     reflectance is quadratic in the field).
  2. The probe carries a nonzero second-order acoustic OAM L2 ∝ m with OPPOSITE
     sign for ±m -> a genuine quadrature e^{imφ} winding.
  3. The probe velocity is CURL-FREE (bulk / divergence channel, prereg §2.2;
     u = ∇Φ via the engine's FD stencil).
  4. On a NON-rotating (static) mirror, R(+m) ≈ R(−m) (the φ→−φ symmetry floor;
     the repaired probe does NOT manufacture a spurious handedness asymmetry).
  5. KEEPER: on a ROTATING reference, R(+m) != R(−m) beyond the static floor
     (frame-dragging selectivity) — the assertion the OLD cos(m·φ) probe could
     NEVER pass (it gave EXACTLY equal R for ±m on any target).

Engine:   src/ave/core/sonic_horizon_flow.py::add_oam_pulse, ::oam_second_order
Research: research/2026-06-10_sonic-horizon-closure_result.md (Verdict Addendum, §4-bis)
"""

import numpy as np
import pytest

from ave.core.sonic_horizon_flow import SonicHorizonFlow2D


def _inject(m, N=96, amp=1e-3, r0=0.34, width=0.05):
    e = SonicHorizonFlow2D(N=N, nu_art=5e-4, rho_diff=5e-4)
    e.add_oam_pulse(m=m, r0=r0, amp=amp, width=width, inward=True)
    return e


def _reflectance(make_ref, m, N=128, nprobe=450, r_meas=0.30, r_launch=0.34,
                 amp=1e-3, width=0.03):
    """Flux-through-circle reflectance of an m-OAM pulse off the reference set by
    ``make_ref(e)`` — a compact, self-contained mirror of the Stage-D driver
    measurement (incident inward + reflected outward flux on the SAME circle,
    difference-field = probe-run minus baseline-run)."""
    e0 = SonicHorizonFlow2D(N=N, nu_art=5e-4, rho_diff=5e-4)
    make_ref(e0)
    r = e0.R + 1e-12
    dr = 1.5 * e0.dx
    ring = (np.abs(r - r_meas) < dr) & e0.interior
    nx = (e0.X / r)[ring]
    ny = (e0.Y / r)[ring]

    def flux(e):
        ur = e.u[ring] * nx + e.v[ring] * ny
        return float(np.sum(e.c0**2 * e.rho[ring] * ur))

    st = (e0.rho.copy(), e0.u.copy(), e0.v.copy(), e0.cav_mask.copy(), e0.static_mirror.copy())
    eb = SonicHorizonFlow2D(N=N, nu_art=5e-4, rho_diff=5e-4)
    eb.rho, eb.u, eb.v, eb.cav_mask, eb.static_mirror = (a.copy() for a in st)
    base = [flux(eb)]
    for _ in range(nprobe):
        eb.step()
        base.append(flux(eb))
    ep = SonicHorizonFlow2D(N=N, nu_art=5e-4, rho_diff=5e-4)
    ep.rho, ep.u, ep.v, ep.cav_mask, ep.static_mirror = (a.copy() for a in st)
    ep.add_oam_pulse(m=m, r0=r_launch, amp=amp, width=width, inward=True)
    prb = [flux(ep)]
    for _ in range(nprobe):
        ep.step()
        prb.append(flux(ep))
    cum = np.cumsum(np.array(prb) - np.array(base)) * ep.dt
    imin = int(np.argmin(cum))
    cmin = float(cum[imin])
    e_inc = -cmin
    e_refl = float(np.max(cum[imin:])) - cmin
    return e_refl / e_inc if e_inc > 1e-30 else 0.0


class TestSonicHorizonOAMProbe:
    def test_pm_fields_distinct(self):
        """(1) ±m injected fields are physically distinct — directly catches the
        bit-identical cos(m·φ) bug, AND rules out a trivial global sign-flip."""
        ep, em = _inject(+1), _inject(-1)
        assert np.max(np.abs(ep.rho - em.rho)) > 1e-9, "±m density fields are bit-identical (the cos(mφ) bug)"
        assert np.max(np.abs(ep.u - em.u)) > 1e-9, "±m velocity fields are bit-identical"
        # a global sign-flip (rho(-m) == -rho(+m)) would also yield R(+m)=R(-m):
        assert np.max(np.abs(ep.rho + em.rho)) > 1e-9, "±m are a trivial sign-flip, not distinct circulations"

    def test_oam_second_order_sign(self):
        """(2) nonzero quadrature OAM L2 ∝ m, opposite sign for ±m."""
        ep, em = _inject(+1), _inject(-1)
        lp, lm = ep.oam_second_order(), em.oam_second_order()
        assert lp > 0.0 and lm < 0.0, f"OAM sign not m-odd: L2(+1)={lp:.3e} L2(-1)={lm:.3e}"
        assert lp == pytest.approx(-lm, rel=1e-6), "L2(+m) and L2(-m) are not antisymmetric"

    def test_probe_is_curl_free(self):
        """(3) u = ∇Φ is bulk/divergence-channel (curl-free), prereg §2.2."""
        ep = _inject(+1)
        z = ep.vorticity()
        ratio = float(np.max(np.abs(z)) * ep.dx / (np.max(np.abs(ep.u)) + 1e-30))
        assert ratio < 1e-6, f"probe carries shear/vorticity (ratio={ratio:.2e}); must be bulk-channel"

    def test_static_mirror_symmetry_floor(self):
        """(4) on a NON-rotating mirror R(+m) ≈ R(−m): the φ→−φ symmetry floor.
        The repaired probe must NOT manufacture a spurious handedness asymmetry."""
        def mk(e):
            e.set_static_mirror(radius=0.20)

        rp = _reflectance(mk, +1, nprobe=300)
        rm = _reflectance(mk, -1, nprobe=300)
        assert abs(rp - rm) < 1e-6, f"spurious probe asymmetry on a symmetric target: {abs(rp - rm):.2e}"

    def test_rotating_reference_selective(self):
        """(5) KEEPER: on a ROTATING reference R(+m) != R(−m) beyond the static
        floor — frame-dragging selectivity. The OLD cos(m·φ) probe gave EXACTLY
        equal R for ±m on ANY target and could never pass this."""
        def mk(e):
            e.energize_solid_body(M_edge=0.9, R_core=0.18)
            for _ in range(220):
                e.step()

        rp = _reflectance(mk, +1, nprobe=450)
        rm = _reflectance(mk, -1, nprobe=450)
        assert abs(rp - rm) > 1e-5, f"no handedness asymmetry on a rotating reference: {abs(rp - rm):.2e}"
        assert rp > rm, f"co-rotating (m=+1) should reflect more than counter: R_co={rp:.5f} R_ct={rm:.5f}"
