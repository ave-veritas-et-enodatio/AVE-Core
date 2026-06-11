"""
Genesis v9 Phase-0 — REAL-dynamics observers for the two smokes.

PHASE-0 scaffold. NO genesis run. This module adds the *dynamical* smoke
observers on top of the graph library `chiral_lattice.py` (which is left
unmodified — graph + the minimal scalar scatter+connect step only). See
research/2026-06-11_genesis-v9-chiral-lattice_design.md.

substrate-native-check walk (done before this code, per Operating Principle 1):
  * Dynamics  : discrete K4/srs-TLM **scatter + connect** wave propagation
                (k4-tlm-simulator.md:36-40) — NOT Lagrangian, NOT gradient-descent,
                NOT continuum-Helmholtz, NOT energy-basin minimisation.
  * Sector    : Smoke A is the scalar/capacitive E-sector (one scalar per port);
                Smoke B's source is the trace-free transverse-EM pseudoscalar.
  * Objective : TLM dispersion eigenmode (V-sector), measured spectrally.
  * Coords A46: Smoke A measures a scalar wave speed = a real-space/spectral
                observable (matches the achiral corpus claim). Smoke B measures a
                reflection-odd pseudoscalar / a transverse-frame rotation = the
                chirality coordinate (matches the handedness corpus claim) — NOT a
                real-space lattice-Cartesian field amplitude vs phi^2.
  * Saturation: OFF (linear, A << 1). No local-clock modulation in Phase-0.
  * CP9       : energy + dispersion are DYNAMICALLY evolved by `scalar_tlm_step`
                (not an algebraic heuristic). The Smoke-B writhe is an explicitly-
                flagged GEOMETRIC SOURCE term (necessary-condition), and the
                screw-axis frame transport is an explicitly-flagged KINEMATIC
                (Bishop parallel-transport) holonomy — the converged *dynamical*
                polarization-rotation of a propagating transverse packet is the
                Phase-1 vector-TLM deliverable (design doc §3), not Phase-0.
  * CP10      : Smoke A runs CLOSED (no PML, no bulk force); conservation is exact.

consistency-vs-emergence tag: Smoke A is **CONSISTENCY-class** — it checks the
chiral net reproduces the canonical 3D link-line TLM network-velocity invariant
(c/c_link = 1/sqrt(3)) and the unitary energy conservation that already worked on
the cubic engine. It is not an emergence claim and is not a CODATA fit.
"""

from __future__ import annotations

import numpy as np

from ave.core import chiral_lattice as cl

# Analytic anchor: the 3D link-line TLM network velocity is c_link / sqrt(D=3).
# One scatter+connect step advances a signal exactly one bond (c_link = bond/step);
# the long-wavelength scalar mode propagates at the 3D-isotropic projection
# c0 = c_link / sqrt(3). This is the canonical 3D-TLM geometric factor and is the
# achiral "did-not-break-it" invariant the z=3 srs net must reproduce.
ANALYTIC_NETWORK_FACTOR = 1.0 / np.sqrt(3.0)


# ─────────────────────────────────────────────────────────────────────────────
# Smoke A — energy conservation (analytic backbone) + small-k scalar dispersion
# ─────────────────────────────────────────────────────────────────────────────
def connect_is_permutation(net: cl.LatticeNet) -> bool:
    """The CONNECT map is a bijection on the ports => Connect is a permutation
    matrix (orthogonal). With S orthogonal (S^T S = I), the one-step operator
    M = Connect . blockdiag(S) is orthogonal, so all eigenvalue moduli are 1 and
    Sum|V_inc|^2 is exactly conserved. This is the ANALYTIC energy-conservation
    proof; `energy_drift` below is its dynamical confirmation."""
    src, dst = net.connect_index()
    return (
        len(np.unique(src)) == len(src)
        and len(np.unique(dst)) == len(dst)
        and set(src.tolist()) == set(dst.tolist())
        and len(src) == net.n_nodes * net.degree
    )


def energy_drift(net: cl.LatticeNet, steps: int = 200, seed_node: int | None = None) -> float:
    """Max relative drift of the closed-system TLM energy over `steps` steps."""
    S = cl.scatter_matrix(net.degree)
    conn = net.connect_index()
    if seed_node is None:
        seed_node = int(np.where(net.interior_mask)[0][0])
    V = np.zeros((net.n_nodes, net.degree))
    V[seed_node] = 1.0
    E0 = cl.lattice_energy(V)
    drift = 0.0
    for _ in range(steps):
        V = cl.scalar_tlm_step(net, V, S, conn)
        drift = max(drift, abs(cl.lattice_energy(V) - E0) / E0)
    return drift


def measure_dispersion(
    net: cl.LatticeNet, axis: int = 2, m_values=(1, 2, 3, 4), n_steps: int = 800
):
    """Small-k scalar dispersion by standing-wave modal extraction.

    For each commensurate wavevector k_m = 2*pi*m/box along `axis`, seed a
    symmetric cosine Bloch profile cos(k.r) on every port, time-step the CLOSED
    scatter+connect loop, project the field onto the same cosine each step, and
    read the modal oscillation frequency omega(k) from the FFT peak (parabolic
    sub-bin interpolation). Returns a list of (k, omega, c=omega/k).

    c is the phase velocity in (Cartesian-length / step). Dividing by the bond
    length (c_link = bond/step) gives the dimensionless network factor compared
    against ANALYTIC_NETWORK_FACTOR.
    """
    S = cl.scatter_matrix(net.degree)
    conn = net.connect_index()
    r = net.pos
    out = []
    win = np.hanning(n_steps)
    for m in m_values:
        k = 2.0 * np.pi * m / net.box
        kr = k * r[:, axis]
        cos_kr = np.cos(kr)
        V = np.tile(cos_kr[:, None], (1, net.degree)).astype(float)
        amp = np.empty(n_steps)
        for t in range(n_steps):
            V = cl.scalar_tlm_step(net, V, S, conn)
            amp[t] = np.sum(cos_kr * V.mean(axis=1))
        amp -= amp.mean()
        F = np.abs(np.fft.rfft(amp * win))
        i = int(np.argmax(F[1:]) + 1)
        if 1 <= i < len(F) - 1:
            a, b, c2 = F[i - 1], F[i], F[i + 1]
            denom = a - 2.0 * b + c2
            delta = 0.5 * (a - c2) / denom if abs(denom) > 1e-30 else 0.0
        else:
            delta = 0.0
        omega = 2.0 * np.pi * (i + delta) / n_steps
        out.append((float(k), float(omega), float(omega / k) if k > 0 else 0.0))
    return out


def mean_bond_length(net: cl.LatticeNet) -> float:
    """Mean nearest-neighbour bond length (= c_link in Cartesian/step)."""
    lengths = []
    for u in range(net.n_nodes):
        for v in net.neighbors[u]:
            d = net.pos[v] - net.pos[u]
            d -= net.box * np.round(d / net.box)
            lengths.append(np.linalg.norm(d))
    return float(np.mean(lengths))


def network_velocity_factor(net: cl.LatticeNet, **kw) -> dict:
    """Dimensionless TLM network-velocity factor c(k->0)/c_link and linearity.

    c(k->0) is a linear-in-k^2 extrapolation of the measured dispersion. The
    factor should equal ANALYTIC_NETWORK_FACTOR (1/sqrt(3)) for both the chiral
    srs net and the cubic diamond reference — the achiral invariant.
    """
    disp = measure_dispersion(net, **kw)
    ks = np.array([k for k, _, _ in disp])
    cs = np.array([c for _, _, c in disp])
    c0 = float(np.polyfit(ks**2, cs, 1)[-1]) if len(ks) >= 2 else float(cs.mean())
    c_link = mean_bond_length(net)
    # linearity: spread of c(k) across the small-k window, relative to the mean
    linearity = float((cs.max() - cs.min()) / cs.mean())
    return {
        "c0": c0,
        "c_link": c_link,
        "factor": c0 / c_link,
        "c_of_k": cs.tolist(),
        "k": ks.tolist(),
        "linearity_spread": linearity,
    }


# ─────────────────────────────────────────────────────────────────────────────
# Smoke B — transverse polarization transport along the exact screw axis
#
# HONEST SCOPE (design doc §3): the converged *dynamical* polarization-plane
# rotation of a propagating transverse packet requires the full vector-TLM (a
# transverse 2-component field carried on the ports) and is the Phase-1
# deliverable. A minimal Phase-0 rendering of a launched packet was found to
# WANDER (box-dependent, sign-flipped between box sizes). The two channels run
# here at Phase-0 are:
#   (B1) the ring-WRITHE pseudoscalar (in chiral_lattice.net_ring_writhe) — the
#        reflection-ODD, box-independent geometric SOURCE term; the clean SIGNED
#        enantiomorph discriminator (opposite sign, zero on the achiral control).
#   (B2) Bishop (minimal-twist) parallel transport of a transverse frame along
#        the EXACT 4_1/4_3 screw orbit (below). What is EXACT and ROBUST: the
#        transport rotation is nonzero on the chiral helix and is MIRROR-ODD —
#        under the explicit mirror (x->-x) of a helix, Delta_theta and the helix's
#        signed torsion flip sign EXACTLY with magnitude preserved (+78.1 -> -78.1
#        deg/unit; tau +0.52 -> -0.52 rad). So the transverse channel carries a
#        genuine, signed, mirror-odd rotation.
#   *** Honest non-convergence (REAL-TEST CATCH, not rescued):*** the per-length
#        RATE does NOT cleanly converge at Phase-0. The discrete 4_1 orbit is a
#        coarse 4-gon-per-turn polygon: the per-screw-step Bishop increments are
#        jagged (std ~28 deg) and Delta_theta/L wobbles ~9% as the helix lengthens
#        (end / discreteness effects). An earlier "box-independent at L=4,6,8"
#        reading was a FALSE convergence signal — this helix does not depend on the
#        supercell L at all, so that constancy was trivial. This substantiates
#        design §3: a converged DYNAMICAL polarization-rotation rate needs the full
#        vector-TLM (transverse 2-field on the ports), which is Phase-1.
#   *** A46-flavoured limitation (reported, not hidden):*** chasing a single,
#        INDEPENDENTLY-found screw axis does NOT discriminate handedness — srs-R's
#        4_1 and srs-L's 4_3 orbit-helices are both geometrically right-handed,
#        because each enantiomorph space group (I4_1 32 / I4_3 32) contains screw
#        axes of BOTH senses. The global handedness lives in the reflection-ODD
#        coordinate (the writhe pseudoscalar B1 / the mirror operation), NOT in one
#        real-space screw-axis ray.
# Hence B1 (writhe) is the load-bearing SIGNED, converged, box-independent Phase-0
# channel; B2 confirms the transverse rotation is real and mirror-odd but is not a
# converged per-length rate at Phase-0. The literal "polarization rotation per unit
# length of a propagating packet" is Phase-1 (full vector-TLM).
# ─────────────────────────────────────────────────────────────────────────────
def find_screw_operator(enantiomorph: str):
    """Return (R, t): a proper 4-fold rotation R about z and fractional
    translation t with a quarter/three-quarter z-pitch that maps the srs motif
    (mod 1) to itself — i.e. the 4_1 (right) / 4_3 (left) screw operator."""
    motif = cl.srs_motif(enantiomorph)
    Rz = np.array([[0.0, -1.0, 0.0], [1.0, 0.0, 0.0], [0.0, 0.0, 1.0]])
    for R in (Rz, Rz.T):
        for j in range(len(motif)):
            t = np.mod(motif[j] - (R @ motif[0]), 1.0)
            Rm = np.mod((R @ motif.T).T + t, 1.0)
            ok = all(
                np.any(np.all(np.abs(((a - motif + 0.5) % 1.0) - 0.5) < 1e-6, axis=1))
                for a in Rm
            )
            if ok and (abs(t[2] % 1.0 - 0.25) < 1e-6 or abs(t[2] % 1.0 - 0.75) < 1e-6):
                return R, t
    return None, None


def screw_orbit_helix(enantiomorph: str, n_turns: int = 2, a_cell: float | None = None):
    """Cartesian coords of the open helix generated by orbiting one motif node
    under the exact screw operator (z climbs freely — an open, non-wandering helix)."""
    R, t = find_screw_operator(enantiomorph)
    if R is None:
        return None
    if a_cell is None:
        a_cell = 2.0 * np.sqrt(2.0)
    cur = cl.srs_motif(enantiomorph)[0].copy()
    coords = [cur.copy() * a_cell]
    for _ in range(4 * n_turns):
        cur = (R @ cur) + t
        coords.append(cur.copy() * a_cell)
    return np.array(coords)


def bishop_transport_rotation(coords: np.ndarray, axis: int = 2):
    """Bishop (minimal-twist) parallel transport of a transverse frame along the
    polyline `coords`. Returns (total_rotation_rad, axial_length, rate_per_len):
    the accumulated rotation of the transverse vector about `axis`, and per unit
    axial length. Magnitude is a geometric solid angle (handedness-blind)."""
    P = np.asarray(coords)
    T = np.diff(P, axis=0)
    Tn = T / np.linalg.norm(T, axis=1)[:, None]
    a0 = np.array([1.0, 0.0, 0.0])
    if abs(np.dot(a0, Tn[0])) > 0.9:
        a0 = np.array([0.0, 1.0, 0.0])
    e = a0 - np.dot(a0, Tn[0]) * Tn[0]
    e /= np.linalg.norm(e)
    frames = [e.copy()]
    for i in range(1, len(Tn)):
        t0, t1 = Tn[i - 1], Tn[i]
        ax = np.cross(t0, t1)
        s = np.linalg.norm(ax)
        if s > 1e-12:
            ax /= s
            ang = np.arctan2(s, np.dot(t0, t1))
            e = (
                e * np.cos(ang)
                + np.cross(ax, e) * np.sin(ang)
                + ax * np.dot(ax, e) * (1.0 - np.cos(ang))
            )
        e = e - np.dot(e, t1) * t1
        e /= np.linalg.norm(e)
        frames.append(e.copy())
    frames = np.array(frames)
    plane = [i for i in range(3) if i != axis]
    ang = np.unwrap(np.arctan2(frames[:, plane[1]], frames[:, plane[0]]))
    total = float(ang[-1] - ang[0])
    axial = float(P[-1, axis] - P[0, axis])
    return total, axial, (total / axial if abs(axial) > 1e-9 else 0.0)


def helix_signed_torsion(coords: np.ndarray) -> float:
    """Mean discrete signed torsion of the helix — the SIGNED handedness channel.
    Right-handed helix > 0, left-handed < 0. Complements the writhe pseudoscalar."""
    P = np.asarray(coords)
    taus = []
    for i in range(1, len(P) - 2):
        e1 = P[i] - P[i - 1]
        e2 = P[i + 1] - P[i]
        e3 = P[i + 2] - P[i + 1]
        n1 = np.cross(e1, e2)
        n2 = np.cross(e2, e3)
        denom = np.linalg.norm(n1) * np.linalg.norm(n2)
        if denom < 1e-12:
            continue
        sin_tau = np.dot(np.cross(n1, n2), e2 / np.linalg.norm(e2)) / denom
        taus.append(np.arcsin(np.clip(sin_tau, -1.0, 1.0)))
    return float(np.mean(taus)) if taus else 0.0
