"""Half-flux selection test, framing 3 of 3: hopf-action-phase.

Test whether promoting the engine's EXISTING _hopf_density Chern-Simons term
(cosserat_field_3d.py:319-381) from the ENERGY functional (:708 W_hopf*k_hopf) to a
PHASE in the action e^{iS} (i*theta*H) yields the fermion sign (pi phase / half flux)
on the (2,3) odd-q rotation loop AND the trivial phase on the (2,2) even-q control --
with theta derived from K4 discreteness ALONE (no alpha, no half-angle lift, no fitted
k_hopf).

RESULT: [HALF-FLUX-ECHO]. The engine Hopf charge Q_H is a homotopy invariant of the
static field, so it is UNCHANGED by the rigid 2pi frame rotation -> accrued loop phase
theta*dQ_H = 0 for ANY theta (Q_H spread over the loop ~1e-16). It cannot produce the
fermion -1. (This null is gauge-invariant: it is a property of the Hopf invariant, not
of the Coulomb-gauge reconstruction of A used inside _hopf_density.) The static
Q_H ~ p*q carries p*q-parity, not q-parity, so no single theta discriminates odd vs
even q. See research/2026-07-08_electron-halfflux-selection_result.md
"""

from __future__ import annotations

import numpy as np
import jax.numpy as jnp

from ave.topological.cosserat_field_3d import _hopf_density, _project_omega_to_nhat  # noqa: F401


def seed_omega_pq(nx, ny, nz, p, q, R_target, r_target, amp=1.0):
    """Replicate initialize_electron_2_3_sector EXACTLY but with general (p,q).
    theta = p*phi + q*psi ; omega = envelope*(cos theta, sin theta, 0)."""
    cx, cy, cz = (nx - 1) / 2.0, (ny - 1) / 2.0, (nz - 1) / 2.0
    idx = np.indices((nx, ny, nz))
    i, j, k = idx[0], idx[1], idx[2]
    mask_A = (i % 2 == 0) & (j % 2 == 0) & (k % 2 == 0)
    mask_B = (i % 2 == 1) & (j % 2 == 1) & (k % 2 == 1)
    mask_alive = mask_A | mask_B
    x = i - cx
    y = j - cy
    z = k - cz
    rho_xy = np.sqrt(x**2 + y**2)
    rho_tube = np.sqrt((rho_xy - R_target) ** 2 + z**2)
    phi = np.arctan2(y, x)
    psi = np.arctan2(z, rho_xy - R_target)
    r_opt = r_target if r_target > 0 else 1.0
    envelope = amp * (np.sqrt(3.0) / 2.0) * np.pi / (1.0 + (rho_tube / r_opt) ** 2)
    theta = p * phi + q * psi
    omega = np.zeros((nx, ny, nz, 3))
    omega[..., 0] = envelope * np.cos(theta)
    omega[..., 1] = envelope * np.sin(theta)
    omega[..., 2] = 0.0
    omega *= mask_alive[..., None]
    return omega, mask_alive


def hopf_charge(omega, mask_alive, dx):
    """Engine Q_H = (1/4pi^2) integral of _hopf_density over alive cells."""
    rho = _hopf_density(jnp.asarray(omega), dx)
    mask = jnp.asarray(mask_alive).astype(rho.dtype)
    integral = float(jnp.sum(rho * mask) * (dx**3))
    return integral / (4.0 * np.pi**2)


def rot_z_vec(omega, alpha):
    """Rigid global SO(3) frame rotation R_z(alpha) applied to the omega VECTOR."""
    c, s = np.cos(alpha), np.sin(alpha)
    out = np.empty_like(omega)
    out[..., 0] = c * omega[..., 0] - s * omega[..., 1]
    out[..., 1] = s * omega[..., 0] + c * omega[..., 1]
    out[..., 2] = omega[..., 2]
    return out


def loop_hopf_trace(omega, mask_alive, dx, n_steps=9):
    """Q_H sampled along the closed 2pi frame-rotation loop alpha:0->2pi.
    If Q_H is a homotopy invariant it is constant, so the accrued phase of a term
    theta*Q_H around the loop is ZERO."""
    alphas = np.linspace(0.0, 2.0 * np.pi, n_steps)
    return alphas, [hopf_charge(rot_z_vec(omega, a), mask_alive, dx) for a in alphas]


def main():
    N = 40
    dx = 1.0
    R_target = 10.0
    r_target = 4.0
    windings = [(2, 3), (2, 2), (1, 1), (3, 5), (1, 2), (3, 4)]

    print("=" * 78)
    print("hopf-action-phase :: engine _hopf_density promoted to a PHASE  e^{i theta H}")
    print(f"grid {N}^3  dx={dx}  R={R_target}  r={r_target}   (engine seeder replicated)")
    print("=" * 78)

    qh = {}
    for (p, q) in windings:
        omega, mask = seed_omega_pq(N, N, N, p, q, R_target, r_target)
        qh[(p, q)] = hopf_charge(omega, mask, dx)
    print("\n[A] Static engine Hopf charge Q_H (this is what the CS term integrates to):")
    for (p, q) in windings:
        print(f"    (p,q)=({p},{q})  q {'ODD ' if q % 2 else 'EVEN'}  Q_H = {qh[(p, q)]:+.4f}    (p*q = {p*q})")

    print("\n[B] ACCRUED phase around the 2pi rotation loop  (Q_H along alpha:0->2pi):")
    print("    If Q_H is loop-invariant, ANY theta gives ZERO accrued phase.")
    for (p, q) in [(2, 3), (2, 2), (1, 1)]:
        omega, mask = seed_omega_pq(N, N, N, p, q, R_target, r_target)
        alphas, trace = loop_hopf_trace(omega, mask, dx, n_steps=9)
        dqh = max(trace) - min(trace)
        print(f"    (p,q)=({p},{q}): Q_H spread over the loop = {dqh:.2e}  "
              f"-> accrued theta*dQ_H = 0 for any theta   [start={trace[0]:+.4f} end={trace[-1]:+.4f}]")


if __name__ == "__main__":
    main()
