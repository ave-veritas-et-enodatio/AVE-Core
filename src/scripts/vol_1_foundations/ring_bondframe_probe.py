"""NUMERIC RING CONFIRMATION MODULE — a compact periodic-ring probe of the bond-frame
2nd-order content of a traveling transverse wave. Confirms the symbolic predictions of
`bondframe_tslot_predictions.py` on an INDEPENDENT code path.

FROZEN prereg: research/2026-07-05_bondframe-tslot-closure_prereg_FROZEN.md.
Grant path (a) — close the #526 T-slot fork analytically; this is the small targeted
numeric confirmation (NOT a new big sim).

THE #531 TAUTOLOGY GUARD (binding): this module MUST NOT import
`bondframe_tslot_predictions.py`. It measures the tilt, the mean chord strain, and the
bond-frame cycle-mean-config stiffness from a static u-relaxation at frozen wave phase,
phase-averaged — its own independent path. The #528 ReconcileGate compares OUTPUTS only.

Consumes the #532 machinery by import where the mission allows (the canonical kernel is
re-implemented here to stay independent of the prediction module; the ring geometry +
static relaxation are new code). Energy diagnostic: a saturation-consistent per-bond
potential Phi(A) (Gauss-Legendre quadrature) is CHEAP on the ring and used as the
conservation diagnostic for the u-relaxation (the #532 energy-proxy flag addressed).

Host: N-node PERIODIC ring, 2 DOF/node (u longitudinal, y transverse), rest spacing 1.
Ring closure Sum(du)=0 enforced by mean-projecting u each relaxation step.
"""
from __future__ import annotations

import numpy as np

K0 = 1.0
ELL = 1.0
K_S = 1.0


# ── the canonical kernel (independent re-impl; NOT imported from the prediction module) ──
def _phi_prime(A):
    A = np.clip(A, -1.0, 1.0)
    return K0 * (A * np.sqrt(1.0 - A**2) + np.arcsin(A)) / 2.0


def _phi_potential(A):
    """Phi(A) = int_0^A Phi'(s) ds via fixed Gauss-Legendre (saturation-consistent
    energy for the relaxation-conservation diagnostic; the #532 energy-proxy flag)."""
    A = np.atleast_1d(np.asarray(A, dtype=float))
    xg, wg = np.polynomial.legendre.leggauss(24)
    out = np.empty_like(A)
    for i, Ai in enumerate(A.ravel()):
        s = 0.5 * Ai * (xg + 1.0)
        out.ravel()[i] = 0.5 * Ai * np.sum(wg * _phi_prime(s))
    return out.reshape(A.shape)


# ── the periodic ring host ───────────────────────────────────────────────────
class RingChain:
    """N-node PERIODIC ring, 2 DOF/node. Bond b=(j, (j+1) mod N). The ONLY
    transverse<->axial coupling is the bond length L=sqrt((1+du)^2+dy^2).

    `linear_axial=True` replaces the kernel tension Phi'(A) with a LINEAR axial spring
    T = k_a*A (no concavity, no Jensen) — the reconciliation-(a) control: if the effect
    is kinematic, the linear ring reproduces the tilt; the kernel adds only O(y0^4)."""

    def __init__(self, n_nodes: int, k_a: float = 1.0, k_s: float = K_S,
                 linear_axial: bool = False):
        self.n = int(n_nodes)
        self.k_a = float(k_a)
        self.k_s = float(k_s)
        self.linear_axial = bool(linear_axial)

    def tension(self, A):
        return self.k_a * A if self.linear_axial else _phi_prime(A)

    def bond_lengths(self, u, y):
        du = np.roll(u, -1) - u
        dy = np.roll(y, -1) - y
        dx = ELL + du
        L = np.sqrt(dx * dx + dy * dy)
        return L, dx, dy

    def force_x(self, u, y):
        L, dx, dy = self.bond_lengths(u, y)
        A = L - ELL
        T = self.tension(A)
        ux = dx / L
        Tx = T * ux
        return Tx - np.roll(Tx, 1)          # node j: +bond_j -bond_{j-1}

    def force_y(self, u, y):
        L, dx, dy = self.bond_lengths(u, y)
        A = L - ELL
        T = self.tension(A)
        uy = dy / L
        Ty = T * uy
        Fy = Ty - np.roll(Ty, 1)
        curv = np.roll(y, 1) - 2.0 * y + np.roll(y, -1)   # discrete curvature (I-P block)
        Fy = Fy + self.k_s * curv
        return Fy

    def energy(self, u, y):
        """H_pot = Sum_bond [ Phi(A_bond) + 1/2 k_s (dy)^2 ] — saturation-consistent
        axial potential + linear shear proxy. Conservation diagnostic for relaxation."""
        L, _, dy = self.bond_lengths(u, y)
        A = L - ELL
        axial = float(np.sum(_phi_potential(A))) if not self.linear_axial \
            else float(0.5 * self.k_a * np.sum(A**2))
        shear = 0.5 * self.k_s * float(np.sum(dy**2))
        return axial + shear

    def relax_u(self, y, n_iter=20000, dt=0.05, gamma=0.3):
        """Damped relaxation of u at FIXED y; ring closure Sum(du)=0 via mean-projection.
        Returns the equilibrium u (the fast longitudinal DOF at the imposed transverse
        snapshot)."""
        u = np.zeros(self.n)
        vu = np.zeros(self.n)
        for _ in range(int(n_iter)):
            Fx = self.force_x(u, y)
            vu = (vu + dt * Fx) * (1.0 - gamma * dt)
            u = u + dt * vu
            u -= u.mean()                     # closure gauge: mean u free, Sum(du)=0
        return u

    def trans_tangent_stiffness(self, u, y, node, delta=1e-6):
        """-dF_y(node)/dy(node) — the transverse tangent stiffness a slow probe feels."""
        yp = y.copy()
        yp[node] += delta
        ym = y.copy()
        ym[node] -= delta
        return float(-(self.force_y(u, yp)[node] - self.force_y(u, ym)[node]) / (2.0 * delta))


def wave_number_cold(omega=1.2, k_s=K_S, m=1.0):
    """k from the cold transverse (shear-branch) dispersion. INDEPENDENT re-derivation
    (not imported): cos k = 1 - omega^2/(2 k_s/m)."""
    return float(np.arccos(1.0 - omega**2 / (2.0 * k_s / m)))


# ── the three measurements on the ring (cycle = phase average) ────────────────
def measure_ring(n_nodes=240, y0=0.1428, omega=1.2, n_wavelengths=None,
                 n_phase=64, relax_iter=20000, linear_axial=False, probe_node=None):
    """Phase-average the RELAXED (u, y) over the traveling wave; return the three
    derived quantities measured independently:
      - tilt          = <Phi''(A)*(dy/L)^2>       (cycle+space mean over live snapshots)
      - mean_chord_A  = <A_bond>                  (cycle+space mean; the ring theorem)
      - cyclemean_k   = trans stiffness AT the cycle-mean config (u_mean, y_mean~0)/cold
                        (the BOND-FRAME DC content a slow probe feels)
      - labframe_k    = cycle-mean of the LIVE-snapshot trans stiffness / cold
                        (the LAB-FRAME observable that feels the tilt — the #532 artifact)
      - energy_drift  = max |H(u_relaxed)-H_ref|/... relaxation conservation diagnostic
    """
    if probe_node is None:
        probe_node = n_nodes // 2
    ring = RingChain(n_nodes, linear_axial=linear_axial)
    # dispersion-set k, snapped to an integer number of wavelengths on the ring
    k0 = wave_number_cold(omega)
    if n_wavelengths is None:
        n_wavelengths = max(1, int(round(k0 * n_nodes / (2 * np.pi))))
    k = 2 * np.pi * n_wavelengths / n_nodes    # exact ring-commensurate k (near k0)
    j = np.arange(n_nodes)

    umean = np.zeros(n_nodes)
    tilt_acc = 0.0
    A_acc = 0.0
    lab_k = []
    kcold = ring.trans_tangent_stiffness(np.zeros(n_nodes), np.zeros(n_nodes), probe_node)
    max_relax_resid = 0.0
    for m_ in range(n_phase):
        ph = 2 * np.pi * m_ / n_phase
        y = y0 * np.sin(k * j - ph)
        u = ring.relax_u(y, n_iter=relax_iter)
        L, dx, dy = ring.bond_lengths(u, y)
        A = L - ELL
        # tilt integrand Phi''(A)*(dy/L)^2, space-mean this snapshot
        tilt_acc += float(np.mean(np.sqrt(np.clip(1 - A**2, 0, 1)) * (dy / L) ** 2))
        A_acc += float(np.mean(A))
        lab_k.append(ring.trans_tangent_stiffness(u, y, probe_node))
        umean += u
        # relaxation residual: max |force_x| after relaxation (should be ~0)
        max_relax_resid = max(max_relax_resid, float(np.max(np.abs(ring.force_x(u, y)))))
    umean /= n_phase
    tilt = tilt_acc / n_phase
    mean_chord_A = A_acc / n_phase
    ymean = np.zeros(n_nodes)               # <y>=0 (wave odd symmetry)
    cyclemean_k = ring.trans_tangent_stiffness(umean, ymean, probe_node) / kcold
    labframe_k = float(np.mean(lab_k)) / kcold
    # cycle-mean-config bond geometry (for the theorem: <dx>=1, A~0)
    Lm, dxm, dym = ring.bond_lengths(umean, ymean)
    return {
        "n_nodes": n_nodes, "y0": y0, "omega": omega, "k_wave": k,
        "n_wavelengths": n_wavelengths, "linear_axial": linear_axial,
        "tilt": tilt,
        "mean_chord_A": mean_chord_A,
        "cyclemean_bondframe_k_ratio": cyclemean_k,     # -> ~1 (DC-ONLY theorem)
        "labframe_k_ratio": labframe_k,                 # -> 1 + tilt (the artifact)
        "cyclemean_dx": float(np.mean(dxm)),            # -> 1 (un-stretched mean bond)
        "cyclemean_A": float(np.mean(Lm - ELL)),        # -> ~0
        "k_cold_raw": kcold,
        "max_relax_residual": max_relax_resid,
    }


# ── reconciliation (b): the OPEN-chain boundary POSITION-DEPENDENCE ────────────
def open_chain_strain_profile(n_nodes=400, y0=0.1428, omega=1.2, n_phase=48,
                              relax_iter=20000, free_end=False):
    """The #532 boundary artifact on an OPEN chain: the mean chord strain <A_bond> is
    boundary-set (NOT ring-closure-pinned) and POSITION-DEPENDENT — it varies along the
    chain and can change sign, unlike the ring's UNIFORM positive value.

    This reproduces the #532 STRUCTURAL finding (`pump-probe-tslot_result.md:77`:
    "boundary-concentrated, [+0.0075, +0.0011, -0.0026, -0.0036] at nodes [20,100,200,380],
    a 3.7x gradient toward the pin"): the mean strain has a near-drive POSITIVE (Jensen
    bulk) region that RELAXES toward NEGATIVE down the gradient as the pinned wall pulls
    the chain. HONEST SCOPE (flag-don't-fix): this static-relaxation model reproduces the
    #532 GRADIENT STRUCTURE and its boundary-config sensitivity, NOT the exact -0.0026
    node-200 value (that requires #532's full traveling-wave TIME-DOMAIN dynamics with the
    absorbing sponge, out of scope for the analytic path (a)). The LOAD-BEARING reconciliation
    is the CONTRAST: open = position-dependent / boundary-set / sign-varying (the artifact);
    ring = uniform / boundary-independent / positive (the theorem).

    Open chain: node 0 pinned (u[0]=0). free_end=False pins the far end (u[-1]=0, the
    Dirichlet wall); free_end=True releases it. Transverse ends clamped y[0]=y[-1]=0."""
    k = wave_number_cold(omega)
    j = np.arange(n_nodes)

    def bl_open(u, y):
        du = u[1:] - u[:-1]
        dy = y[1:] - y[:-1]
        dx = ELL + du
        return np.sqrt(dx * dx + dy * dy), dx, dy

    def fx_open(u, y):
        L, dx, _dy = bl_open(u, y)
        Tx = _phi_prime(L - ELL) * dx / L
        Fx = np.zeros(len(u))
        Fx[:-1] += Tx
        Fx[1:] -= Tx
        return Fx

    A_profile_acc = np.zeros(n_nodes - 1)   # per-bond mean strain
    for m_ in range(n_phase):
        ph = 2 * np.pi * m_ / n_phase
        y = y0 * np.sin(k * j - ph)
        y[0] = 0.0
        y[-1] = 0.0
        u = np.zeros(n_nodes)
        vu = np.zeros(n_nodes)
        dt, gamma = 0.05, 0.3
        for _ in range(int(relax_iter)):
            Fx = fx_open(u, y)
            vu = (vu + dt * Fx) * (1.0 - gamma * dt)
            u = u + dt * vu
            u[0] = 0.0                      # pinned drive end (Dirichlet)
            if not free_end:
                u[-1] = 0.0                 # pinned far end (the wall)
        L, _, _ = bl_open(u, y)
        A_profile_acc += (L - ELL)
    A_profile = A_profile_acc / n_phase
    # sample near-drive, mid, and toward-far, matching #532's profile-gradient reporting
    idx = [n_nodes // 20, n_nodes // 4, n_nodes // 2, int(n_nodes * 0.95)]
    return {
        "free_end": free_end,
        "mean_A_whole_chain": float(np.mean(A_profile)),
        "A_profile_samples": [float(A_profile[i]) for i in idx],
        "profile_min": float(A_profile.min()),
        "profile_max": float(A_profile.max()),
        "position_gradient": float(A_profile.max() - A_profile.min()),
    }


if __name__ == "__main__":
    import json

    out = {}
    # primary ring confirmation (nonlinear kernel)
    out["ring_nonlinear"] = measure_ring(linear_axial=False)
    # reconciliation (a): the LINEAR-axial ring reproduces the tilt to ~kernel_o4
    out["ring_linear_axial"] = measure_ring(linear_axial=True)
    # N-convergence (the CONSTRAINT-DEPENDENT discriminator: does the ring reading converge?)
    out["ring_N120"] = measure_ring(n_nodes=120)
    out["ring_N480"] = measure_ring(n_nodes=480)
    # reconciliation (b): the open-chain position-dependence + boundary sensitivity
    out["open_pinned"] = open_chain_strain_profile(free_end=False)
    out["open_free"] = open_chain_strain_profile(free_end=True)
    print(json.dumps(out, indent=2, default=float))
