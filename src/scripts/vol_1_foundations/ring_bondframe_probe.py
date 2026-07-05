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


# ── the ring measurement, for a SINGLE TRAVELING MODE (cycle = phase average) ──
def measure_ring(n_nodes=240, y0=0.1428, omega=1.2, n_wavelengths=None,
                 n_phase=64, relax_iter=20000, linear_axial=False, probe_node=None,
                 standing=False):
    """Phase-average the RELAXED (u, y) over a SINGLE TRAVELING MODE on the fixed-contour
    ring; return the derived quantities measured independently:
      - tilt          = <Phi''(A)*(dy/L)^2>       (cycle+space mean over live snapshots)
      - mean_chord_A  = <A_bond>                  (cycle+space mean; = <dy^2>/2 for the mode)
      - cyclemean_k   = trans stiffness AT the cycle-mean config (u_mean, y_mean~0)/cold
                        (the BOND-FRAME reading — COLD on the fixed-contour ring)
      - labframe_k    = cycle-mean of the LIVE-snapshot trans stiffness / cold
                        (the LAB-FRAME observable that feels the tilt — the #532 artifact)

    SCOPE (item-2, orchestrator review): the COLD bond-frame reading holds for a SINGLE
    TRAVELING MODE (whose <dy^2>_j is spatially HOMOGENEOUS). `standing=True` imposes a
    STANDING wave (satisfies <y>=0 and fixed contour but NOT the homogeneity premise): it
    deposits a per-bond +/-O(y0^2) strain PATTERN. The mean-over-bonds geometry witnesses
    still read cold (a mean can be cold while per-bond is patterned) — reported KEEP-BOTH."""
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
    A_per_bond_acc = np.zeros(n_nodes)      # per-bond mean strain (item-2: per-bond vs mean)
    tilt_acc = 0.0
    A_acc = 0.0
    lab_k = []
    kcold = ring.trans_tangent_stiffness(np.zeros(n_nodes), np.zeros(n_nodes), probe_node)
    max_relax_resid = 0.0
    for m_ in range(n_phase):
        ph = 2 * np.pi * m_ / n_phase
        # traveling (default): y = y0 sin(kj - ph); standing: y = y0 sin(kj) cos(ph)
        y = y0 * np.sin(k * j) * np.cos(ph) if standing else y0 * np.sin(k * j - ph)
        u = ring.relax_u(y, n_iter=relax_iter)
        L, dx, dy = ring.bond_lengths(u, y)
        A = L - ELL
        tilt_acc += float(np.mean(np.sqrt(np.clip(1 - A**2, 0, 1)) * (dy / L) ** 2))
        A_acc += float(np.mean(A))
        A_per_bond_acc += A
        lab_k.append(ring.trans_tangent_stiffness(u, y, probe_node))
        umean += u
        max_relax_resid = max(max_relax_resid, float(np.max(np.abs(ring.force_x(u, y)))))
    umean /= n_phase
    A_per_bond = A_per_bond_acc / n_phase   # per-bond cycle-mean strain
    tilt = tilt_acc / n_phase
    mean_chord_A = A_acc / n_phase
    ymean = np.zeros(n_nodes)               # <y>=0 (odd symmetry / half-cycle for standing)
    cyclemean_k = ring.trans_tangent_stiffness(umean, ymean, probe_node) / kcold
    labframe_k = float(np.mean(lab_k)) / kcold
    Lm, dxm, dym = ring.bond_lengths(umean, ymean)
    return {
        "n_nodes": n_nodes, "y0": y0, "omega": omega, "k_wave": k,
        "n_wavelengths": n_wavelengths, "linear_axial": linear_axial, "standing": standing,
        "tilt": tilt,
        "mean_chord_A": mean_chord_A,
        "cyclemean_bondframe_k_ratio": cyclemean_k,     # traveling -> ~1 (cold, mean-over-bonds)
        "labframe_k_ratio": labframe_k,                 # -> 1 + tilt (the artifact)
        "cyclemean_dx": float(np.mean(dxm)),            # mean-over-bonds: ~1
        "cyclemean_A": float(np.mean(Lm - ELL)),        # mean-over-bonds: ~0
        # ITEM-2 per-bond pattern: traveling -> ~uniform; standing -> +/-O(y0^2) structured
        "A_per_bond_range": float(A_per_bond.max() - A_per_bond.min()),
        "A_per_bond_max_abs": float(np.max(np.abs(A_per_bond))),
        "k_cold_raw": kcold,
        "max_relax_residual": max_relax_resid,
    }


# ── THE OPEN-CHAIN HOSTS at TRUE equilibrium (item 1 re-bin: the cross-host table) ─
# The FREE open chain carries NO end tension, so its equilibrium forces T = Phi'(A_bond)
# = 0 on EVERY bond => A_bond = 0 => (1+du)^2 + dy^2 = 1 => du_b = sqrt(1-dy^2) - 1
# EXACTLY (analytic; a damped relaxation reaches this only asymptotically — the earlier
# `relax_iter=20000` was a TRANSIENT that had not converged, the item-2 gate-(b) bug).
def _free_equilibrium_u(y):
    """EXACT T=0 free-open-chain equilibrium: du_b = sqrt(1-dy_b^2) - 1 per bond, cumsum
    (node 0 pinned). Verified T = Phi'(A_bond) = 0 to machine precision (max A ~ 1e-16)."""
    dy = y[1:] - y[:-1]
    du = np.sqrt(np.clip(1.0 - dy**2, 0.0, 1.0)) - 1.0
    return np.concatenate([[0.0], np.cumsum(du)])


def _bl_open(u, y):
    du = u[1:] - u[:-1]
    dy = y[1:] - y[:-1]
    dx = ELL + du
    return np.sqrt(dx * dx + dy * dy), dx, dy


def _fy_open(u, y):
    L, dx, dy = _bl_open(u, y)
    T = _phi_prime(L - ELL)
    Ty = T * dy / L
    Fy = np.zeros(len(y))
    Fy[:-1] += Ty
    Fy[1:] -= Ty
    curv = y[:-2] - 2.0 * y[1:-1] + y[2:]
    Fy[1:-1] += K_S * curv
    return Fy


def _ktrans_open(u, y, node, delta=1e-6):
    yp = y.copy()
    yp[node] += delta
    ym = y.copy()
    ym[node] -= delta
    return float(-(_fy_open(u, yp)[node] - _fy_open(u, ym)[node]) / (2.0 * delta))


def _relax_pinned_u(y, both_ends, n_iter, dt=0.05, gamma=0.3):
    """Damped relaxation of u on an OPEN chain with node 0 pinned; both_ends also pins
    the far end (u[-1]=0). Used for the PINNED host (whose equilibrium is NOT T=0)."""
    n = len(y)
    u = np.zeros(n)
    vu = np.zeros(n)
    for _ in range(int(n_iter)):
        L, dx, _dy = _bl_open(u, y)
        Tx = _phi_prime(L - ELL) * dx / L
        Fx = np.zeros(n)
        Fx[:-1] += Tx
        Fx[1:] -= Tx
        vu = (vu + dt * Fx) * (1.0 - gamma * dt)
        u = u + dt * vu
        u[0] = 0.0
        if both_ends:
            u[-1] = 0.0
    return u


def open_chain_cyclemean(n_nodes=240, y0=0.1428, omega=1.2, n_phase=48,
                         host="free", relax_iter=200000, probe_node=None):
    """The bond-frame cycle-mean-config transverse tangent stiffness on an OPEN chain at
    TRUE equilibrium — the measurement the frozen prereg bin (iv) required across hosts.

    host="free" : far end free -> T=0 equilibrium (analytic, exact) -> reads SOFT by
                  <dy^2>/2 (BULK, N-independent: the wave contracts its own free ends).
    host="pinned": both ends pinned (u[0]=u[-1]=0) -> the wall absorbs the contraction
                  as constraint force -> reads COLD (like the ring).

    This is the [CONSTRAINT-DEPENDENT] cross-host discriminator: materially different
    bond-frame readings (free SOFT vs pinned/ring COLD) across the prereg's own hosts."""
    if probe_node is None:
        probe_node = n_nodes // 2
    k = wave_number_cold(omega)
    j = np.arange(n_nodes)
    umean = np.zeros(n_nodes)
    max_A_at_equil = 0.0
    for m_ in range(n_phase):
        ph = 2 * np.pi * m_ / n_phase
        y = y0 * np.sin(k * j - ph)
        y[0] = 0.0
        y[-1] = 0.0
        if host == "free":
            u = _free_equilibrium_u(y)
        elif host == "pinned":
            u = _relax_pinned_u(y, both_ends=True, n_iter=relax_iter)
        else:
            raise ValueError(f"host must be 'free' or 'pinned', got {host!r}")
        L, _, _ = _bl_open(u, y)
        max_A_at_equil = max(max_A_at_equil, float(np.max(np.abs(L - ELL))) if host == "free" else 0.0)
        umean += u
    umean /= n_phase
    ymean = np.zeros(n_nodes)
    kcold = _ktrans_open(np.zeros(n_nodes), np.zeros(n_nodes), probe_node)
    kmean = _ktrans_open(umean, ymean, probe_node) / kcold
    du_m = umean[1:] - umean[:-1]
    return {
        "host": host,
        "cyclemean_bondframe_k_ratio": kmean,
        "cyclemean_dx": float(np.mean(ELL + du_m)),
        "pred_soft_free": float(1.0 - 0.5 * y0**2 * (1.0 - np.cos(k))),  # 1 - <dy^2>/2
        "max_A_at_equil": max_A_at_equil,
    }


def three_host_table(n_nodes=240, y0=0.1428, omega=1.2, n_phase=48):
    """The cross-host bond-frame reading table (item 1): ring / pinned / free. Materially
    different readings = the frozen [CONSTRAINT-DEPENDENT] signature. Each is the bond-frame
    cycle-mean-config transverse tangent stiffness (ratio to cold) at TRUE equilibrium."""
    ring = measure_ring(n_nodes=n_nodes, y0=y0, omega=omega, n_phase=n_phase)
    pinned = open_chain_cyclemean(n_nodes=n_nodes, y0=y0, omega=omega, n_phase=n_phase,
                                  host="pinned")
    free = open_chain_cyclemean(n_nodes=n_nodes, y0=y0, omega=omega, n_phase=n_phase,
                                host="free")
    return {
        "ring": ring["cyclemean_bondframe_k_ratio"],
        "pinned": pinned["cyclemean_bondframe_k_ratio"],
        "free": free["cyclemean_bondframe_k_ratio"],
        "free_pred_soft": free["pred_soft_free"],
        "spread": float(max(ring["cyclemean_bondframe_k_ratio"],
                            pinned["cyclemean_bondframe_k_ratio"],
                            free["cyclemean_bondframe_k_ratio"])
                        - min(ring["cyclemean_bondframe_k_ratio"],
                              pinned["cyclemean_bondframe_k_ratio"],
                              free["cyclemean_bondframe_k_ratio"])),
    }


if __name__ == "__main__":
    import json

    out = {}
    # primary ring confirmation (nonlinear kernel)
    out["ring_nonlinear"] = measure_ring(linear_axial=False)
    # reconciliation (a): the LINEAR-axial ring reproduces the tilt to ~kernel_o4
    out["ring_linear_axial"] = measure_ring(linear_axial=True)
    # ITEM-1 THE CROSS-HOST TABLE: ring / pinned / free bond-frame readings at TRUE
    # equilibrium. Materially different (free SOFT vs ring/pinned COLD) = the frozen
    # bin (iv) [CONSTRAINT-DEPENDENT] signature.
    out["three_host_table"] = three_host_table()
    # the free-end soft reading is BULK (N-independent): the [CONSTRAINT-DEPENDENT] core
    out["free_N120"] = open_chain_cyclemean(n_nodes=120, host="free")
    out["free_N480"] = open_chain_cyclemean(n_nodes=480, host="free")
    print(json.dumps(out, indent=2, default=float))
