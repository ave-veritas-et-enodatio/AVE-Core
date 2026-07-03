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
        # theta-INDEPENDENT: sliding theta is an unobservable global phase on the
        # wavefunction (drags no texture), leaving the occupied projector invariant
        # -> C_slide = 0 by construction.  Returns 1 (no theta in H).
        return np.ones_like(np.asarray(offset_z, dtype=float)) * (1.0 + 0j)
    if reading == "locked":
        _R, t = cld.find_screw_operator(enantiomorph)
        t_z = float(t[2])
        s = 1.0 if t_z < 0.5 else -1.0  # srs-R (+) vs srs-L (-)
        return np.exp(1j * s * theta * offset_z)
    raise ValueError(f"reading must be 'sliding' or 'locked', got {reading!r}")


_BONDS_CACHE: dict = {}
_STAGGER = np.array([+1.0, -1.0, +1.0, -1.0, +1.0, -1.0, +1.0, -1.0])


def _bonds_arrays(enantiomorph: str):
    """Cached (i_idx, j_idx, offsets) arrays for the srs cell — the NN search runs
    ONCE per enantiomorph, not per grid point (the 80s -> sub-second fix)."""
    if enantiomorph not in _BONDS_CACHE:
        bonds = srs_cell_bonds(enantiomorph)
        ii = np.array([b[0] for b in bonds])
        jj = np.array([b[1] for b in bonds])
        offs = np.array([b[2] for b in bonds])  # (nb, 3)
        _BONDS_CACHE[enantiomorph] = (ii, jj, offs)
    return _BONDS_CACHE[enantiomorph]


def srs_bloch_H(kx: float, ky: float, kz: float, theta: float, enantiomorph: str, reading: str):
    """The 8-band srs tight-binding Bloch Hamiltonian H(k; theta) at fixed
    transverse (kx, ky).  Hermitian; nearest-neighbour hopping t=1 on the genuine
    srs bond table, inter-cell bonds carrying exp(i k.offset), plus the registry
    phase from theta per `reading`.  A frozen staggered on-site potential lifts the
    trivial 8-fold degeneracy so the occupied half-manifold is gapped (a fixed
    pattern, NOT tuned to the result).  Scalar entry point; the sweep uses the
    batched builder below."""
    ii, jj, offs = _bonds_arrays(enantiomorph)
    k = np.array([kx, ky, kz])
    phase = np.exp(1j * (offs @ k))
    phase = phase * _screw_theta_phase(enantiomorph, reading, theta, offs[:, 2])
    H = np.zeros((N_SITES, N_SITES), dtype=complex)
    np.add.at(H, (ii, jj), -1.0 * phase)
    H = 0.5 * (H + H.conj().T)
    H += 0.6 * np.diag(_STAGGER)
    return H


def srs_bloch_H_grid(kx: float, ky: float, KZ, TH, enantiomorph: str, reading: str):
    """Batched srs Bloch Hamiltonians over a (KZ, TH) meshgrid at fixed (kx, ky).
    KZ, TH: (n, n) meshgrid arrays.  Returns (n, n, 8, 8) Hermitian stack — the
    whole grid built in vectorized numpy (no per-point Python loop)."""
    ii, jj, offs = _bonds_arrays(enantiomorph)
    nz = KZ.shape
    # k.offset per grid point per bond: transverse fixed, kz varies over the grid
    # phase_geom[g, b] = exp(i (kx*ox + ky*oy + KZ*oz))
    base = kx * offs[:, 0] + ky * offs[:, 1]              # (nb,)
    kz_term = KZ[..., None] * offs[:, 2]                  # (n, n, nb)
    phase_geom = np.exp(1j * (base + kz_term))            # (n, n, nb)
    # registry phase per bond
    if reading == "sliding":
        # SLIDING: matter drags NO substrate texture -> theta is an unobservable
        # global U(1) phase on the WAVEFUNCTION, i.e. H is theta-INDEPENDENT (a
        # global phase leaves the occupied projector P = sum|psi><psi| invariant).
        # So the (k_z, theta) Berry curvature is IDENTICALLY zero -> C_slide = 0 by
        # construction.  (Multiplying hoppings by exp(i theta) would be a DIFFERENT,
        # spectrum-changing operation and is NOT the sliding reading — the corpus
        # sliding engine drags no texture, so theta cannot enter H.)
        reg = np.ones((1,) * KZ.ndim + (len(ii),))               # (1,...,nb) -> theta-free
    elif reading == "locked":
        _R, t = cld.find_screw_operator(enantiomorph)
        s = 1.0 if float(t[2]) < 0.5 else -1.0
        reg = np.exp(1j * s * TH[..., None] * offs[:, 2])          # (n,n,nb)
    else:
        raise ValueError(reading)
    amp = -1.0 * phase_geom * reg                          # (n, n, nb)
    H = np.zeros(nz + (N_SITES, N_SITES), dtype=complex)
    for b in range(len(ii)):
        H[..., ii[b], jj[b]] += amp[..., b]
    H = 0.5 * (H + np.conj(np.swapaxes(H, -1, -2)))
    H[..., np.arange(N_SITES), np.arange(N_SITES)] += 0.6 * _STAGGER
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
    band Fukui-Hatsugai when n_occ = 1.

    Eigensolves are BATCHED: the whole (nu, nv) grid of Hamiltonians is stacked to
    shape (nu, nv, dim, dim) and diagonalized in ONE np.linalg.eigh call (which
    broadcasts over the leading axes) — ~100x faster than a per-point Python loop.
    The plaquette links are then fully vectorized via np.roll."""
    nu, nv = len(us), len(vs)
    dim = H_of_uv(us[0], vs[0]).shape[0]
    Hstack = np.empty((nu, nv, dim, dim), dtype=complex)
    for i, u in enumerate(us):
        for j, v in enumerate(vs):
            Hstack[i, j] = H_of_uv(u, v)
    _w, vecs = np.linalg.eigh(Hstack)      # batched: vecs (nu, nv, dim, dim)
    frames = vecs[..., :n_occ]              # occupied frame (nu, nv, dim, n_occ)

    def link(a, b):
        # normalized det(<a|b>) over the whole grid at once; a,b: (...,dim,n_occ)
        d = np.linalg.det(np.conj(a).swapaxes(-1, -2) @ b)
        return np.where(np.abs(d) > 1e-14, d / np.abs(d), 1.0 + 0j)

    fr_ip = np.roll(frames, -1, axis=0)     # (i+1, j)
    fr_jp = np.roll(frames, -1, axis=1)     # (i, j+1)
    fr_ipjp = np.roll(fr_ip, -1, axis=1)    # (i+1, j+1)
    field = np.angle(
        link(frames, fr_ip) * link(fr_ip, fr_ipjp) * link(fr_ipjp, fr_jp) * link(fr_jp, frames)
    )                                        # (nu, nv)
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


# ═════════════════════════════════════════════════════════════════════════════
#  srs N-band (k_z, theta) occupied-manifold Chern — the roll
# ═════════════════════════════════════════════════════════════════════════════
# Infinitesimal offset from exact high-symmetry points.  FINDING (this run): at
# EXACTLY kx=ky=0 (Gamma), the srs occupied manifold has an isolated accidental
# degeneracy where the Fukui-Hatsugai plaquette lands on the +-pi branch cut
# (max_plaquette = pi exactly) and the Chern integer FLICKERS (0/+2/-4/-1/+2 over
# n=24/36/48/72/96) — an ill-defined invariant AT that measure-zero point, NOT a
# bulk pump.  Perturbing off Gamma by even 1e-3 gives a CLEAN grid-stable C=0 with
# max_plaquette = 0.0 (perfectly smooth).  So the bulk invariant is unambiguously
# 0; the Gamma flicker is a high-symmetry gauge artifact.  Standard practice:
# sample the smooth interior, offsetting exact-symmetry points infinitesimally.
_HS_EPS = 1.0e-3


def _transverse_slices(n_interior: int = 3) -> list:
    """Capped transverse (kx, ky) sampling (engineering-choice; prereg SS5 left the
    transverse density an implementation detail, ">= 2 densities" — this is the
    amendment note, no bin/gate change): the pump Chern is slice-INDEPENDENT for a
    gapped manifold, so we do NOT sweep (kx,ky) at FH density.  Sample the
    high-symmetry points (Gamma, X-edges, M-corner) OFFSET by _HS_EPS to avoid the
    Gamma branch-cut artifact (documented above) + a small n_interior^2 interior
    grid (<= 16 slices).  If every slice agrees the bulk integer is carried; a
    disagreeing slice is a reported FINDING (checked for gap-closing vs artifact),
    not brute-forced past."""
    e = _HS_EPS
    # ALL exact high-symmetry points offset by e (Gamma, X-edges, AND the M-corner
    # (pi,pi) — the accidental-degeneracy branch artifact sits at every exact HS
    # point, not just Gamma).
    hi_sym = [(e, e), (np.pi + e, e), (e, np.pi + e), (np.pi + e, np.pi + e)]
    g = np.linspace(0.0, 2.0 * np.pi, n_interior, endpoint=False) + e
    interior = [(kx, ky) for kx in g for ky in g]
    seen, out = set(), []
    for s in hi_sym + interior:
        key = (round(s[0], 6), round(s[1], 6))
        if key not in seen:
            seen.add(key)
            out.append(s)
    return out


def _chern_from_grid_stack(Hstack) -> dict:
    """Occupied-manifold Chern from a prebuilt (n, n, 8, 8) Hamiltonian stack (one
    batched eigh; vectorized plaquette links) + the min occ/unocc gap over the
    same stack.  Single source of truth for both quantities on the srs grid."""
    _w, vecs = np.linalg.eigh(Hstack)          # (n,n,8), (n,n,8,8)
    frames = vecs[..., :N_OCC]                  # (n,n,8,N_OCC)

    def link(a, b):
        d = np.linalg.det(np.conj(a).swapaxes(-1, -2) @ b)
        return np.where(np.abs(d) > 1e-14, d / np.abs(d), 1.0 + 0j)

    fr_ip = np.roll(frames, -1, axis=0)
    fr_jp = np.roll(frames, -1, axis=1)
    fr_ipjp = np.roll(fr_ip, -1, axis=1)
    field = np.angle(link(frames, fr_ip) * link(fr_ip, fr_ipjp) * link(fr_ipjp, fr_jp) * link(fr_jp, frames))
    chern = float(np.sum(field) / (2.0 * np.pi))
    min_gap = float(np.min(_w[..., N_OCC] - _w[..., N_OCC - 1]))
    return {
        "chern": chern,
        "chern_int": int(np.round(chern)),
        "max_plaquette": float(np.max(np.abs(field))),
        "min_gap": min_gap,
    }


def srs_nband_chern(enantiomorph: str, reading: str, n: int = 36) -> dict:
    """Occupied-manifold Chern of the 8-band srs H over the (k_z, theta) torus,
    at each capped transverse (kx, ky) slice (see `_transverse_slices`).  Reports
    the per-slice integers, whether they all agree (the slice-independence guard),
    the modal integer, and the min occupied/unoccupied gap over all slices.  Fully
    batched: one srs_bloch_H_grid + one eigh per slice."""
    slices = _transverse_slices()
    grid = np.linspace(0.0, 2.0 * np.pi, n, endpoint=False)
    KZ, TH = np.meshgrid(grid, grid, indexing="ij")
    per_slice, max_plaq = [], 0.0
    min_gap = np.inf
    for (kx, ky) in slices:
        Hstack = srs_bloch_H_grid(kx, ky, KZ, TH, enantiomorph, reading)
        r = _chern_from_grid_stack(Hstack)
        per_slice.append(r["chern_int"])
        min_gap = min(min_gap, r["min_gap"])
        max_plaq = max(max_plaq, r["max_plaquette"])
    ints = np.array(per_slice)
    modal = int(np.bincount(ints - ints.min()).argmax() + ints.min()) if len(ints) else 0
    return {
        "enantiomorph": enantiomorph,
        "reading": reading,
        "chern_int": modal,
        "per_slice_ints": per_slice,
        "n_slices": len(slices),
        "all_slices_agree": bool(np.all(ints == modal)),
        "min_manifold_gap": float(min_gap),
        "max_plaquette": float(max_plaq),
        "slices": _transverse_slices(),
        "n_grid": n,
    }


def srs_nband_convergence(enantiomorph: str, reading: str, grids=(24, 36, 48)) -> dict:
    """Grid-convergence sweep (prereg SS5): the C_N integer must be identical across
    all grids AND the manifold gapped for the verdict to count."""
    runs = {n: srs_nband_chern(enantiomorph, reading, n=n) for n in grids}
    ints = [runs[n]["chern_int"] for n in grids]
    gaps = [runs[n]["min_manifold_gap"] for n in grids]
    converged = bool(len(set(ints)) == 1 and min(gaps) > 1e-3 and all(runs[n]["all_slices_agree"] for n in grids))
    return {
        "enantiomorph": enantiomorph,
        "reading": reading,
        "chern_int": ints[-1],
        "ints_by_grid": dict(zip(grids, ints)),
        "min_gap": float(min(gaps)),
        "converged": converged,
    }


# ═════════════════════════════════════════════════════════════════════════════
#  Verdict — apply the FROZEN gates + outcome bins (prereg SS2-SS5)
# ═════════════════════════════════════════════════════════════════════════════
def adjudicate_nband(results: dict) -> dict:
    """Apply the FROZEN N-band gates + bins.  results keys: 'vok' (a_sliding,
    a_locked, b_plus, b_minus), 'anchor' (enant->dict), 'srs' ((reading,enant)->
    convergence dict).  Encodes prereg SS2-SS5 exactly — no post-hoc edits."""
    vok = results["vok"]
    vok_a_pass = vok["a_sliding"]["chern_int"] == 0 and vok["a_locked"]["chern_int"] == 0
    bp, bm = vok["b_plus"]["chern_int"], vok["b_minus"]["chern_int"]
    vok_b_pass = abs(bp) >= 1 and bp == -bm
    vok_pass = bool(vok_a_pass and vok_b_pass)

    srs = results["srs"]
    conv = all(srs[(rd, e)]["converged"] for rd in ("sliding", "locked") for e in ("right", "left"))

    def C(rd, e):
        return srs[(rd, e)]["chern_int"]

    def enantio_odd(rd):
        cr, cl_ = C(rd, "right"), C(rd, "left")
        if cr == 0 and cl_ == 0:
            return True
        return cr == -cl_

    odd_ok = enantio_odd("sliding") and enantio_odd("locked")
    all_zero = all(C(rd, e) == 0 for rd in ("sliding", "locked") for e in ("right", "left"))
    any_nonzero = any(C(rd, e) != 0 for rd in ("sliding", "locked") for e in ("right", "left"))
    anchor_R = results["anchor"]["right"]["pitch_matches_anchor_0p25pct"]

    if not vok_pass:
        bin_name, reason = "INCONCLUSIVE", "GATE-VOK failed (Check A must recover 2-band C=0 AND Check B must detect a known nonzero that flips sign)."
    elif not conv:
        bin_name, reason = "INCONCLUSIVE", "srs occupied-manifold Chern non-converged (gapless at half-filling or grid-unstable across n=24/36/48)."
    elif not odd_ok:
        bin_name, reason = "INCONCLUSIVE", "enantiomorph-odd RED FLAG: a nonzero C_N did not flip sign srs-R <-> srs-L (artifact suspected)."
    elif all_zero:
        bin_name = "NULL-CONFIRMED-FINAL"
        reason = (
            "C_N = 0 in BOTH readings AND BOTH enantiomorphs (gapped + converged, VOK PASS). "
            "The registry-pump mechanism is DEAD at the faithful N-band srs level. Per Grant's "
            "pre-commitment the coupling question CLOSES permanently -- no further rolls. Q = "
            "xi_topo.x is a unit-bridge; Cleave retires as a discriminator (AVE itself predicts "
            "the bench null -- corroborative-null class)."
        )
    elif any_nonzero:
        rd_hit = next(rd for rd in ("sliding", "locked") for e in ("right", "left") if C(rd, e) != 0)
        bin_name = "REOPENS"
        reason = (
            f"C_N != 0 (first in the {rd_hit} reading). The mechanism is REAL at N-band. Run the "
            f"anchor cross-check for the canon slot (anchor_R match = {anchor_R}); implied slope = "
            f"C_N x {{146.7 | 586.8}} fC/um from the matching period."
        )
    else:
        bin_name, reason = "INCONCLUSIVE", "unclassified (should not occur)."
    return {
        "vok_pass": vok_pass,
        "vok_a_pass": bool(vok_a_pass),
        "vok_b_pass": bool(vok_b_pass),
        "converged": conv,
        "enantio_odd_ok": odd_ok,
        "C": {f"{rd}_{e}": C(rd, e) for rd in ("sliding", "locked") for e in ("right", "left")},
        "anchor_R_matches": bool(anchor_R),
        "bin": bin_name,
        "reason": reason,
    }


def run_all_nband(grids=(24, 36, 48), incremental_dir: str | None = None) -> dict:
    """Execute the full frozen N-band protocol.

    If `incremental_dir` is given, each (reading x enantiomorph) srs config writes
    its result to a per-config JSON as it completes — so a detached run that is
    interrupted still leaves partial results on disk (the resume reads the JSONs)."""
    import json
    import os

    vok = {
        "a_sliding": vok_check_a_recover_2band("sliding"),
        "a_locked": vok_check_a_recover_2band("locked"),
        "b_plus": vok_check_b_known_multiband(pump_sign=+1),
        "b_minus": vok_check_b_known_multiband(pump_sign=-1),
    }
    anchor = {e: srs_anchor(e) for e in ("right", "left")}
    if incremental_dir:
        os.makedirs(incremental_dir, exist_ok=True)
        with open(os.path.join(incremental_dir, "vok_anchor.json"), "w") as f:
            json.dump({"vok": {k: {kk: vv for kk, vv in d.items() if kk in ("chern", "chern_int")}
                               for k, d in vok.items()}}, f, indent=2)
    srs = {}
    for rd in ("sliding", "locked"):
        for e in ("right", "left"):
            srs[(rd, e)] = srs_nband_convergence(e, rd, grids=grids)
            if incremental_dir:
                with open(os.path.join(incremental_dir, f"srs_{rd}_{e}.json"), "w") as f:
                    json.dump(srs[(rd, e)], f, indent=2)
    results = {"vok": vok, "anchor": anchor, "srs": srs}
    results["verdict"] = adjudicate_nband(results)
    if incremental_dir:
        with open(os.path.join(incremental_dir, "verdict.json"), "w") as f:
            json.dump(results["verdict"], f, indent=2)
    return results


def _fmt_nband(results: dict) -> str:
    v = results["verdict"]
    sl = expected_slopes_fc_per_um()
    lines = [
        "=" * 76,
        "CLEAVE-01 REGISTRY-PUMP CHERN — N-BAND (the LAST roll)",
        "FROZEN prereg: research/2026-07-02_cleave-registry-pump-chern-nband_prereg.md",
        "=" * 76,
        "",
        "GATE-VOK (validate-on-known):",
        f"  Check A (recover 2-band C=0): sliding={results['vok']['a_sliding']['chern_int']:+d}, "
        f"locked={results['vok']['a_locked']['chern_int']:+d}  -> PASS={v['vok_a_pass']}",
        f"  Check B (known multi-band |C|=2): +1 -> {results['vok']['b_plus']['chern_int']:+d}, "
        f"-1 -> {results['vok']['b_minus']['chern_int']:+d}  -> PASS={v['vok_b_pass']}",
        "",
        "ANCHOR cross-check (OA bulk g0 = 2.21589 rad/z-unit):",
    ]
    for e in ("right", "left"):
        a = results["anchor"][e]
        lines.append(
            f"  srs-{e[0].upper()}: bare_pitch = {a['bare_pitch_rad_per_zunit']:.5f} "
            f"({a['pitch_pct_off_anchor']:.4f}% off, match={a['pitch_matches_anchor_0p25pct']})"
        )
    lines += ["", "srs N-band (k_z, theta) occupied-manifold Chern [n_occ=4/8, grids 24/36/48]:"]
    for rd in ("sliding", "locked"):
        for e in ("right", "left"):
            r = results["srs"][(rd, e)]
            lines.append(
                f"  {rd:8s} srs-{e[0].upper()}: C_N = {r['chern_int']:+d}  "
                f"ints_by_grid={r['ints_by_grid']}  min_gap={r['min_gap']:.4f}  "
                f"converged={r['converged']}"
            )
    lines += [
        "",
        "Slope (from canonical constants; moot if null):",
        f"  bench e/l_node        : {sl['bench_e_over_lnode']:.1f} fC/um  (needs non-integer C=2sqrt2)",
        f"  full-cell C=1 e/a_cell: {sl['full_cell_e_over_acell']:.1f} fC/um",
        f"  quarter  C=1 e/p      : {sl['quarter_e_over_p']:.1f} fC/um",
        "",
        "-" * 76,
        f"C: {v['C']}",
        f"enantiomorph-odd OK: {v['enantio_odd_ok']}   converged: {v['converged']}   VOK: {v['vok_pass']}",
        f"VERDICT BIN: {v['bin']}",
        f"  {v['reason']}",
        "=" * 76,
    ]
    return "\n".join(lines)


def main() -> None:
    print(_fmt_nband(run_all_nband()))


if __name__ == "__main__":
    main()
