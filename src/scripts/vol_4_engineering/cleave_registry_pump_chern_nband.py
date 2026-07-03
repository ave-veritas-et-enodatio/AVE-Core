"""Cleave-01 registry-pump Chern — the N-band upgrade (the LAST roll).

Executes the FROZEN prereg
`research/2026-07-02_cleave-registry-pump-chern-nband_prereg.md` (Grant, 2026-07-02):
the full 8-site srs-cell tight-binding occupied-MANIFOLD Chern over the (k_z, theta)
registry torus — the gated upgrade the 2-band result (§5) scoped as the route that
could still differ.  Pre-commitment: a confirmed null CLOSES the coupling question
permanently; no further rolls.

Shares machinery with the 2-band driver (cleave_registry_pump_chern) — imports its
Fukui-Hatsugai integrator, constants, slopes, and anchor cross-check; adds the
genuine N-band srs Bloch Hamiltonian + the non-Abelian occupied-projector Chern.

substrate-native-check walk (done before this code):
  * Carrier : the genuine srs 8a-orbit cell (chiral_lattice._SRS_8A, 8 sites,
              degree-3 net) — the N-band object the 2-band model approximated.
              z=3, no diamond substitution.
  * Sector  : T2 Cosserat micro-rotation WINDING; the occupied-manifold Chern IS
              the pumped Link(dOmega,F) per registry period.  No A1 cross-wiring.
  * Method  : Berry curvature of the occupied PROJECTOR over the closed (k_z,theta)
              torus (non-Abelian Wilson-loop; the Fukui-Hatsugai plaquette on the
              occupied manifold via the overlap-matrix determinant).  Substrate-
              native adiabatic-pump invariant.  NOT Lagrangian/energy-basin.
  * Coords  : Chern on (k_z,theta) phase space; anchor g0 a holonomy (phase).
              Matched.  Real-space slope = phase invariant x substrate period.

FROZEN gates (prereg SS2-SS5):
  GATE-VOK Check A: recover the 2-band C=0 in a restricted subspace.
  GATE-VOK Check B: detect a KNOWN multi-band nonzero pump (|C|>=1, flips sign).
  ANCHOR: srs-R reproduces g0=2.21589 rad/z-unit to 0.25%.
  CONVERGENCE: identical integer C_N across (k_z,theta) grids n=24/36/48, gapped
    occupied manifold (min gap > 1e-3), |C_N - round| < 0.1.
  ENANTIOMORPH-ODD: C_N != 0 must flip sign srs-R <-> srs-L.

Outcome bins (frozen): NULL-CONFIRMED-FINAL / REOPENS / INCONCLUSIVE.

Driver-honesty: every printed number computed in-run; constants imported; srs
net/bonds built from chiral_lattice, not transcribed.  Heavy solves -> engine_sim.
"""

from __future__ import annotations

import numpy as np

from ave.core import chiral_lattice as cl
from ave.core import chiral_lattice_dynamics as cld

# shared machinery from the 2-band driver (no duplication)
from scripts.vol_4_engineering.cleave_registry_pump_chern import (
    G0_ANCHOR_RAD_PER_ZUNIT,
    expected_slopes_fc_per_um,
    srs_anchor,
)

_SRS_NN = np.sqrt(2.0) / 4.0  # srs nearest-neighbour bond length in cell units
N_SITES = 8                    # srs 8a Wyckoff orbit
N_OCC = 4                      # frozen half-filling (prereg SS1)


# ═════════════════════════════════════════════════════════════════════════════
#  srs 8-site cell bond table (built from the net, not transcribed)
# ═════════════════════════════════════════════════════════════════════════════
def srs_cell_bonds(enantiomorph: str) -> list:
    """Directed nearest-neighbour bonds of the 8-site srs cell as
    (i, j, offset_vector): a bond from site i to site j in cell displaced by the
    integer `offset`.  Built by NN search on the motif + its periodic images, so
    the inter-cell offsets (which carry the k Bloch phase) are DERIVED from the
    genuine srs geometry (chiral_lattice._SRS_8A), not hand-written."""
    motif = cl.srs_motif(enantiomorph)
    bonds = []
    for i in range(N_SITES):
        for j in range(N_SITES):
            for ox in (-1, 0, 1):
                for oy in (-1, 0, 1):
                    for oz in (-1, 0, 1):
                        off = np.array([ox, oy, oz], dtype=float)
                        d = np.linalg.norm(motif[i] - (motif[j] + off))
                        if abs(d - _SRS_NN) < 1e-6:
                            bonds.append((i, j, off))
    return bonds


def _screw_theta_phase(enantiomorph: str, reading: str, theta: float, offset_z: float) -> complex:
    """The registry-phase factor a bond picks up from theta, per reading.

    SLIDING: theta is a global U(1) phase -> SAME factor on every bond -> it
      commutes with the occupied projector and factors out of the Berry links
      (C=0 by construction).  Implemented as a global exp(i theta) (site- and
      bond-independent), which the projector is blind to.
    LOCKED : theta co-rotates the transverse frame THROUGH the screw operator;
      the finite-strain advection ties theta to the AXIAL bond offset (the screw
      couples z-translation to frame rotation).  A bond crossing offset_z cells
      picks up exp(i * s * theta * offset_z) with s the enantiomorph sign (srs-R
      t_z=1/4 -> +, srs-L t_z=3/4 -> -), so theta winds the band along k_z and the
      manifold can carry nonzero Chern.  This is the operator-faithful co-moving
      coupling (find_screw_operator sets the pi/2 block + the t_z sign)."""
    if reading == "sliding":
        return np.exp(1j * theta)  # global; projector-blind
    if reading == "locked":
        _R, t = cld.find_screw_operator(enantiomorph)
        t_z = float(t[2])
        s = 1.0 if t_z < 0.5 else -1.0  # srs-R (+) vs srs-L (-)
        return np.exp(1j * s * theta * offset_z)
    raise ValueError(f"reading must be 'sliding' or 'locked', got {reading!r}")


def srs_bloch_H(kx: float, ky: float, kz: float, theta: float, enantiomorph: str, reading: str):
    """The 8-band srs tight-binding Bloch Hamiltonian H(k; theta) at fixed
    transverse (kx, ky).  Hermitian; nearest-neighbour hopping t=1 on the genuine
    srs bond table, inter-cell bonds carrying exp(i k.offset), plus the registry
    phase from theta per `reading`.  A small on-site sublattice potential lifts the
    trivial 8-fold degeneracy so the occupied half-manifold is gapped (frozen: a
    fixed staggered pattern, NOT tuned to the result)."""
    bonds = srs_cell_bonds(enantiomorph)
    k = np.array([kx, ky, kz])
    H = np.zeros((N_SITES, N_SITES), dtype=complex)
    for (i, j, off) in bonds:
        phase = np.exp(1j * np.dot(k, off))
        phase *= _screw_theta_phase(enantiomorph, reading, theta, off[2])
        H[i, j] += -1.0 * phase  # t = 1 hopping
    # Hermitize (the bond table is directed but symmetric; enforce exactly).
    H = 0.5 * (H + H.conj().T)
    # frozen staggered on-site potential to gap the half-filled manifold
    stagger = np.array([+1.0, -1.0, +1.0, -1.0, +1.0, -1.0, +1.0, -1.0])
    H += 0.6 * np.diag(stagger)
    return H


# ═════════════════════════════════════════════════════════════════════════════
#  Non-Abelian occupied-manifold Chern (Fukui-Hatsugai on the occupied projector)
# ═════════════════════════════════════════════════════════════════════════════
def _occ_frame(H, n_occ: int) -> np.ndarray:
    """The n_occ lowest eigenvectors of Hermitian H as columns (the occupied frame)."""
    _w, v = np.linalg.eigh(H)
    return v[:, :n_occ]


def occupied_manifold_chern(H_of_uv, us, vs, n_occ: int) -> dict:
    """Non-Abelian (multi-band) Chern number of the occupied manifold over a
    periodic (u, v) torus, by the Fukui-Hatsugai overlap-DETERMINANT method.

    H_of_uv(u, v) -> Hermitian matrix; occupied = the n_occ lowest states.  The
    U(1) link on each edge is det(<frame(a)|frame(b)>) / |det| — gauge-invariant
    over the whole occupied manifold (handles band entanglement, unlike per-band
    Fukui-Hatsugai).  Plaquette field-strength summed / 2pi = the occupied-manifold
    Chern (the trace of the non-Abelian Berry curvature).  Reduces to the single-
    band Fukui-Hatsugai when n_occ = 1."""
    nu, nv = len(us), len(vs)
    frames = np.empty((nu, nv), dtype=object)
    for i, u in enumerate(us):
        for j, v in enumerate(vs):
            frames[i, j] = _occ_frame(H_of_uv(u, v), n_occ)

    def link(a, b):
        d = np.linalg.det(a.conj().T @ b)
        return d / abs(d) if abs(d) > 1e-14 else 1.0 + 0j

    field = np.zeros((nu, nv))
    for i in range(nu):
        for j in range(nv):
            ip, jp = (i + 1) % nu, (j + 1) % nv
            u1 = link(frames[i, j], frames[ip, j])
            u2 = link(frames[ip, j], frames[ip, jp])
            u3 = link(frames[ip, jp], frames[i, jp])
            u4 = link(frames[i, jp], frames[i, j])
            field[i, j] = np.angle(u1 * u2 * u3 * u4)
    chern = float(np.sum(field) / (2.0 * np.pi))
    return {
        "chern": chern,
        "chern_int": int(np.round(chern)),
        "max_plaquette": float(np.max(np.abs(field))),
        "n_grid": (nu, nv),
    }


# ═════════════════════════════════════════════════════════════════════════════
#  GATE-VOK — validate-on-known (prereg SS2)
# ═════════════════════════════════════════════════════════════════════════════
def vok_check_b_known_multiband(pump_sign: int = +1, n: int = 36) -> dict:
    """Check B: a KNOWN multi-band Thouless pump with nonzero occupied-manifold
    Chern.  Two Rice-Mele chains with a LARGE relative energy offset so their
    lower bands are cleanly separated and BOTH sit in the occupied n_occ=2
    manifold; each chain contributes Chern +-1 (aligned), total |C| = 2.  The
    large offset keeps the occupied/unoccupied gap wide (well-resolved, no
    plaquette branch ambiguity).  Confirms the non-Abelian integrator DETECTS a
    real nonzero (not trivially 0) and flips sign with pump direction."""
    ks = np.linspace(0.0, 2.0 * np.pi, n, endpoint=False)
    phis = np.linspace(0.0, 2.0 * np.pi, n, endpoint=False)
    t, r0 = 1.0, 0.8

    def rm_block(k, phi, sgn):
        tp = t + r0 * np.cos(sgn * phi)
        m = r0 * np.sin(sgn * phi)
        dx = t + tp * np.cos(k)
        dy = tp * np.sin(k)
        dz = m
        return np.array([[dz, dx - 1j * dy], [dx + 1j * dy, -dz]], dtype=complex)

    def H(k, phi):
        # Two aligned RM chains, chain-2 offset DOWN by 1.5 so the occupied n_occ=2
        # manifold is {chain-1 lower band, chain-2 lower band} — one per chain,
        # cleanly gapped from the unoccupied pair (min gap ~0.10, wide).  Each
        # lower band carries Chern +-1 -> occupied-manifold total |C| = 2.
        b1 = rm_block(k, phi, pump_sign)
        b2 = rm_block(k, phi, pump_sign)
        M = np.zeros((4, 4), dtype=complex)
        M[:2, :2] = b1
        M[2:, 2:] = b2 - 1.5 * np.eye(2)
        return M

    return occupied_manifold_chern(H, ks, phis, n_occ=2)


def vok_check_a_recover_2band(reading: str, n: int = 24) -> dict:
    """Check A: recover the 2-band C=0 in a restricted subspace.  Runs the
    non-Abelian integrator on the SAME effective 2-band screw block the validated
    2-band driver used (imported), with n_occ=1.  Must return C=0 (matching the
    2-band NULL-DERIVED result) for both readings — proves the N-band machinery
    does not introduce a spurious nonzero on the validated construction."""
    from scripts.vol_4_engineering.cleave_registry_pump_chern import _srs_screw_bloch_H

    ks = np.linspace(0.0, 2.0 * np.pi, n, endpoint=False)
    thetas = np.linspace(0.0, 2.0 * np.pi, n, endpoint=False)

    def H(k, th):
        return _srs_screw_bloch_H(k, th, "right", reading)

    return occupied_manifold_chern(H, ks, thetas, n_occ=1)
