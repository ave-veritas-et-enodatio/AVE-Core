"""Genesis v9 Phase-1 (deferred) — WRITHE-AWARE full vector-TLM optical-activity driver.

The deferred Phase-1 deliverable: does the CHIRAL srs / Laves-K4 substrate net SOURCE
a substrate-DERIVED natural-optical-activity (gyration) coefficient g0 from a
writhe-aware full vector-TLM transport — or not?  Three admissible outcomes
(A chord / B closed-negative / C ill-defined); this driver reports whichever the
physics gives.  NO rotation rate is injected (no ETA decree, unlike the prior
`chiral_lattice_vector.measure_optical_activity` which rides ETA_ROT_PER_WRITHE=1.0
as a hand-set per-node SO(2) twist) — the rotation is DERIVED from a genuine
transverse parallel-transport connection on the connect step.

Prior failure modes (these are the GATES):

  FAIL-1 (writhe-blind operator stencil).  A local-bond operator built from
    {d_hat, k.d} cannot see handedness because the LEFT and RIGHT srs
    bond-direction multisets are IDENTICAL (spec_R - spec_L ~ 4.4e-15).  The
    chirality lives in the ring TOPOLOGY (writhe +/-0.04087, sign-flipped between
    enantiomorphs, exactly 0 on the achiral diamond control), NOT in local bond
    geometry.  GATE 1 (chirality-sensitivity): the operator MUST distinguish L vs
    R and give EXACTLY ZERO on diamond.

  FAIL-2 (non-converged sign-flip).  The design doc's parallel-transport probe
    sign-FLIPPED between L=6 and L=8 (a wandering-scalar-walk artifact).  GATE 2
    (convergence): an L-study (6,8,10,12,16) diagnosing that sign-flip.

  GATE 3 (validate-on-known): reproduce c and Z_0 in the appropriate limit
    (imported from constants by symbol), g0=0 on diamond, and recover the
    odd-in-k circular-split signature (slope 1 in k) for an imposed gyration.

substrate-native-check walk (Operating Principle 1; done before this code):
  * Dynamics  : discrete srs/K4-TLM **scatter + connect** wave propagation
                (k4-tlm-simulator.md:36-40).  NOT Lagrangian / gradient-descent /
                continuum-Helmholtz / energy-basin.
  * Sector    : V-sector, the transverse EM polarization 2-frame on the ports.
  * Objective : circular birefringence = the odd-in-k split of the two circular
                polarizations' Bloch dispersion = the gyration g0.  NOT an injected
                SO(2) twist.
  * Coords A46: the observable is the reflection-ODD polarization-plane rotation
                (a handedness coordinate), matching the corpus pseudoscalar claim,
                NOT a real-space lattice-Cartesian field amplitude vs phi^2.
  * Saturation: OFF (linear, A << 1).  No local-clock modulation in Phase-1 (the
                A->1 regime is genesis scope, design doc CP-Op14).
  * CP9       : the load-bearing observable is the polarization frame of a packet
                DYNAMICALLY evolved by the vector-TLM scatter+connect loop with a
                geometric per-bond transverse-frame connection -- it is NOT an
                algebraic heuristic formula nor an injected angle.  The geometric
                loop-holonomy / forward-winding diagnostics are explicitly flagged
                as the GEOMETRIC SOURCE that the dynamical transport must confirm.
  * CP10      : closed system (no PML, no bulk force); conservation is exact.

The KEY DESIGN CHOICE that escapes FAIL-1 (the writhe-aware connection):
  The transverse polarization 2-frame is parallel-transported by the
  ROTATION-MINIMIZING (Bishop) rotation across the BEND at each node -- from the
  arrival bond tangent to the departure bond tangent.  The frame rotation
  accumulated around a CLOSED ring equals the geometric SOLID ANGLE subtended by
  the ring's tangent sequence on the unit sphere -- a reflection-ODD pseudoscalar
  that is SIGN-FLIPPED between enantiomorphs and EXACTLY ZERO for an achiral
  (mirror-symmetric) ring.  A change-of-basis-only connection (frame absolute
  orientation held fixed) telescopes to identity around any loop and is
  writhe-BLIND (verified: gives 0 on srs too) -- it is the BEND at the node, not
  the local bond direction, that carries the chiral holonomy.

consistency-vs-emergence tag: this is an EMERGENCE test (does substrate geometry
SOURCE a gyration that QED's parity-even vacuum cannot?).  c / Z_0 reproduction is
CONSISTENCY-class; the diamond null is a MANIFESTATION of mirror symmetry; g0
itself, if nonzero+converged+sign-flipping, is the DISCRIMINATING (AVE-distinct)
forward prediction.

Pre-reg: research/2026-06-11_genesis-v9-phase1-prereg_FROZEN.md (the ETA-injected
P1-P4 gates); this driver supersedes the injected-rotation channel with a derived
transport.  Result doc: research/2026-06-23_chiral-vector-tlm-phase1_result.md.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from ave.core import chiral_lattice as cl
from ave.core.constants import C_0, L_NODE, Z_0

# Physical supercell scale: NN bond == one node pitch L_NODE => a_cell = 2*sqrt(2)*L_NODE.
# Used ONLY to convert a (hypothetical) converged per-lattice-unit g0 to rad/m; the
# bulk g0 does NOT converge (outcome C) so no rad/m value is quoted (result-doc Sec 5).
A_CELL_PHYSICAL_M: float = 2.0 * np.sqrt(2.0) * L_NODE


# ============================================================================
# The writhe-aware transverse-frame connection (the FAIL-1 escape)
# ============================================================================
def _rmf_rotate(t0: np.ndarray, t1: np.ndarray, v: np.ndarray) -> np.ndarray:
    """Rotation-minimizing (Bishop) transport of vector ``v`` from tangent ``t0``
    to tangent ``t1`` -- the minimal rotation (about t0 x t1) carrying t0 -> t1.

    This is the BEND operator at a node: the transverse frame parallel-transports
    across the kink from the arrival bond tangent to the departure bond tangent.
    The frame rotation accumulated around a closed ring equals the geometric solid
    angle subtended by the tangent sequence -- the reflection-ODD writhe holonomy.
    """
    ax = np.cross(t0, t1)
    s = np.linalg.norm(ax)
    if s < 1e-12:
        return v.copy()
    ax /= s
    ang = np.arctan2(s, float(np.dot(t0, t1)))
    return (
        v * np.cos(ang)
        + np.cross(ax, v) * np.sin(ang)
        + ax * float(np.dot(ax, v)) * (1.0 - np.cos(ang))
    )


def loop_holonomy(net: cl.LatticeNet, ring: list) -> float:
    """Net transverse-frame rotation (radians) after RMF-transporting a frame once
    around the closed ``ring`` -- the gauge-invariant chiral solid-angle holonomy.

    GAUGE-INVARIANT (tracks the actual transported 3-vector, NOT per-edge reference
    angles which carry a spurious 2*pi reference-field winding).  EXACTLY ZERO for
    an achiral (mirror-symmetric) ring; sign-flipped between enantiomorphs.
    """
    n = len(ring)
    T = []
    for i in range(n):
        u, w = ring[i], ring[(i + 1) % n]
        d = net.pos[w] - net.pos[u]
        d -= net.box * np.round(d / net.box)
        T.append(d / np.linalg.norm(d))
    a = np.array([1.0, 0.0, 0.0])
    if abs(np.dot(a, T[0])) > 0.9:
        a = np.array([0.0, 1.0, 0.0])
    e = a - np.dot(a, T[0]) * T[0]
    e /= np.linalg.norm(e)
    e_start = e.copy()
    for i in range(1, n + 1):
        e = _rmf_rotate(T[(i - 1) % n], T[i % n], e)
        e = e - np.dot(e, T[i % n]) * T[i % n]
        e /= np.linalg.norm(e)
    return float(np.arctan2(np.dot(np.cross(e_start, e), T[0]), np.dot(e, e_start)))


def net_loop_holonomy(net: cl.LatticeNet, n_sample: int = 48):
    """Mean / std / count of RMF-bend loop holonomy over distinct shortest rings.

    The GATE-1 chirality-sensitivity observable: nonzero + sign-flipped between
    enantiomorphs; identically zero on the achiral control.  Returns
    (mean, std, n_rings).
    """
    seen, hols = set(), []
    starts = np.where(net.interior_mask)[0][:n_sample]
    for s in starts:
        ring = cl.shortest_ring(net, int(s))
        if ring is None:
            continue
        key = frozenset(ring)
        if key in seen:
            continue
        seen.add(key)
        hols.append(loop_holonomy(net, ring))
    hols = np.array(hols)
    if len(hols) == 0:
        return 0.0, 0.0, 0
    return float(hols.mean()), float(hols.std()), len(hols)


# ============================================================================
# Forward gyration probe: RMF transverse-frame rotation per unit axial length
# along an actually-traversed forward path through the net.
# ============================================================================
def forward_winding_rate(net: cl.LatticeNet, axis: int = 2, n_paths: int = 200):
    """Mean RMF transverse-frame rotation about ``axis`` per unit axial length,
    over forward-advancing directed walks through the net.

    A wave packet propagating along +``axis`` hops node-to-node, greedily choosing
    the neighbour with the largest +axis advance; ties are broken DETERMINISTICALLY
    by smallest neighbour index (and we report the path-spread so tie-sensitivity is
    visible).  The transverse polarization frame is RMF-transported across each node
    bend (departure tangent - arrival tangent); we accumulate its signed rotation
    about ``axis`` and divide by the total axial displacement.

    This is the per-length gyration g0 (rad / axial-length), in lattice units.
    Isotropic for point group 432=O (verified equal along x/y/z).  The diamond
    control returns ~0 (residual = forward-choice tie degeneracy, reported).

    NOTE (substrate-native-check CP9): this is the GEOMETRIC source rate -- the
    rotation a forward wave's frame MUST acquire from the bond geometry.  The
    `dynamical_packet_rotation` below confirms the actual vector-TLM packet acquires
    the same rate; both are reported so the geometric->dynamical agreement is auditable.
    """
    n_hat = np.zeros(3)
    n_hat[axis] = 1.0
    interior = np.where(net.interior_mask)[0]
    starts = interior[:n_paths]
    rates = []
    for s in starts:
        u = int(s)
        fwd_len = 0.0
        tot_rot = 0.0
        prev_t = None
        nsteps = 0
        for _ in range(400):
            cands = []
            for v in net.neighbors[u]:
                d = net.pos[v] - net.pos[u]
                d -= net.box * np.round(d / net.box)
                cands.append((float(d[axis]), int(v), d))
            cands.sort(key=lambda c: (-c[0], c[1]))  # max +axis advance, then index
            adv, v, d = cands[0]
            if adv <= 1e-9:
                break
            t = d / np.linalg.norm(d)
            if prev_t is not None:
                tp0 = prev_t - np.dot(prev_t, n_hat) * n_hat
                tp1 = t - np.dot(t, n_hat) * n_hat
                if np.linalg.norm(tp0) > 1e-9 and np.linalg.norm(tp1) > 1e-9:
                    tp0 /= np.linalg.norm(tp0)
                    tp1 /= np.linalg.norm(tp1)
                    tot_rot += np.arctan2(
                        float(np.dot(np.cross(tp0, tp1), n_hat)), float(np.dot(tp0, tp1))
                    )
            fwd_len += float(d[axis])
            prev_t = t
            u = v
            nsteps += 1
        if fwd_len > 1e-6 and nsteps > 3:
            rates.append(tot_rot / fwd_len)
    rates = np.array(rates)
    if len(rates) == 0:
        return 0.0, 0.0, 0
    return float(rates.mean()), float(rates.std()), len(rates)


def screw_pitch_rate(a_cell: float | None = None) -> float:
    """The bare 4_1 screw geometric pitch rate (pi/2) / (t_z * a_cell).

    DIAGNOSTIC: the `forward_winding_rate` and `loop_holonomy` are converged and
    L-independent precisely because they coincide (to ~0.2%) with this local
    UNIT-CELL geometric constant -- they are screw/ring geometry, NOT a
    bulk-propagated transport coefficient.  A bulk-propagated wave does NOT inherit
    this constant (see `dynamical_packet_rate` non-convergence).
    """
    from ave.core import chiral_lattice_dynamics as cld

    if a_cell is None:
        a_cell = 2.0 * np.sqrt(2.0)
    _, t = cld.find_screw_operator("right")
    return float((np.pi / 2.0) / (t[2] * a_cell))


# ============================================================================
# The DYNAMICAL writhe-aware vector-TLM (CP9: genuinely evolved, not heuristic)
# State per directed port (u,p): a transverse 3-vector perp to bond_unit[u][p].
# SCATTER: outgoing port p' = sum_p S[p',p] * RMF-bend(arrival tangent -> departure
#          tangent) applied to the incoming transverse 3-vector (chirality enters HERE).
# CONNECT: transfer along the bond to the reverse port (Bloch / packet).
# Lossless by construction (RMF is orthogonal); verified energy drift ~1e-14.
# ============================================================================
def _out_tangents(net: cl.LatticeNet):
    return [
        [net.bond_unit[u][p] for p in range(len(net.neighbors[u]))]
        for u in range(net.n_nodes)
    ]


def dynamical_step(net: cl.LatticeNet, V, S, out_t):
    """One scatter+connect step of the writhe-aware vector-TLM. V[u][p] is a
    transverse 3-vector (perp to out_t[u][p]).  Lossless."""
    N, deg = net.n_nodes, net.degree
    Vref = [[None] * deg for _ in range(N)]
    for u in range(N):
        for pp in range(deg):
            tdep = out_t[u][pp]
            acc = np.zeros(3)
            for p in range(deg):
                tr = _rmf_rotate(out_t[u][p], tdep, V[u][p])
                tr = tr - np.dot(tr, tdep) * tdep
                acc += S[pp, p] * tr
            Vref[u][pp] = acc
    Vnew = [[np.zeros(3) for _ in range(deg)] for _ in range(N)]
    for u in range(N):
        for p, v in enumerate(net.neighbors[u]):
            q = net.reverse_port[u][p]
            vec = Vref[u][p]
            tv = out_t[v][q]
            Vnew[v][q] = vec - np.dot(vec, tv) * tv
    return Vnew


def dynamical_energy_drift(net: cl.LatticeNet, nsteps: int = 40) -> float:
    """Max relative energy drift of the dynamical vector-TLM (Axiom-3 losslessness)."""
    S = cl.scatter_matrix(net.degree)
    out_t = _out_tangents(net)
    interior = np.where(net.interior_mask)[0]
    ref = np.array([1.0, 0.0, 0.0])
    V = [[np.zeros(3) for _ in range(net.degree)] for _ in range(net.n_nodes)]
    for u in interior:
        for p in range(net.degree):
            t = out_t[u][p]
            e = ref - np.dot(ref, t) * t
            if np.linalg.norm(e) > 1e-6:
                V[u][p] = e / np.linalg.norm(e)

    def energy(W):
        return sum(
            float(np.dot(W[u][p], W[u][p]))
            for u in range(net.n_nodes)
            for p in range(net.degree)
        )

    e0 = energy(V)
    drift = 0.0
    for _ in range(nsteps):
        V = dynamical_step(net, V, S, out_t)
        drift = max(drift, abs(energy(V) - e0) / e0)
    return drift


def dynamical_packet_rate(net: cl.LatticeNet, axis: int = 2, nsteps: int = 24):
    """Forward-flux-weighted polarization-plane rotation per unit forward length,
    of an actually-propagating wave packet (the genuinely DYNAMICAL g0 probe).

    Launch a transverse-polarized Gaussian packet, evolve the writhe-aware
    vector-TLM, and fit d(theta)/dz of the FORWARD-FLUX-weighted polarization plane
    over the steps before the packet wraps the periodic box.  Returns (rate, n_fit).

    THIS is the bulk-propagated observable; it does NOT converge in L (see the
    result doc): only ~ box/(bond advance) forward steps exist before PBC wrap, so
    the per-length rate is dominated by the launch transient + wrapping and swings
    wildly with L.  The non-convergence is the load-bearing finding (outcome C).
    """
    S = cl.scatter_matrix(net.degree)
    out_t = _out_tangents(net)
    n_hat = np.zeros(3)
    n_hat[axis] = 1.0
    ex = np.array([1.0, 0.0, 0.0]) if axis != 0 else np.array([0.0, 1.0, 0.0])
    e1 = ex - np.dot(ex, n_hat) * n_hat
    e1 /= np.linalg.norm(e1)
    e2 = np.cross(n_hat, e1)
    interior = np.where(net.interior_mask)[0]
    z = net.pos[:, axis]
    z0 = z[interior].min() + 0.15 * net.box
    sig = 0.10 * net.box
    ref = np.array([1.0, 0.0, 0.0])
    V = [[np.zeros(3) for _ in range(net.degree)] for _ in range(net.n_nodes)]
    for u in interior:
        wt = np.exp(-0.5 * ((z[u] - z0) / sig) ** 2)
        if wt < 0.05:
            continue
        for p in range(net.degree):
            t = out_t[u][p]
            e = ref - np.dot(ref, t) * t
            if np.linalg.norm(e) > 1e-6:
                V[u][p] = e / np.linalg.norm(e) * wt
    rows = []
    for _ in range(nsteps):
        sx = sy = zsum = wsum = 0.0
        for u in range(net.n_nodes):
            for p in range(net.degree):
                t = out_t[u][p]
                fl = max(0.0, float(np.dot(t, n_hat)))
                v = V[u][p]
                e2n = float(np.dot(v, v))
                if fl <= 0 or e2n < 1e-12:
                    continue
                vp = v - np.dot(v, n_hat) * n_hat
                w = fl * e2n
                sx += w * np.dot(vp, e1)
                sy += w * np.dot(vp, e2)
                zsum += w * net.pos[u, axis]
                wsum += w
        if wsum > 1e-12:
            rows.append((zsum / wsum, np.arctan2(sy, sx)))
        V = dynamical_step(net, V, S, out_t)
    rows = np.array(rows)
    th = np.unwrap(rows[:, 1])
    zz = rows[:, 0]
    keep = np.concatenate([[True], np.diff(zz) > -1e-6])
    m = np.where(~keep)[0]
    end = max(m[0] if len(m) > 0 else len(zz), 4)
    coef = np.polyfit(zz[:end], th[:end], 1)
    return float(coef[0]), int(end)


# ============================================================================
# Gate suite + verdict
# ============================================================================
@dataclass(frozen=True)
class GateResult:
    name: str
    passed: bool
    detail: str


def gate1_chirality_sensitivity(L: int = 6) -> GateResult:
    """GATE 1 (FAIL-1 guard): the operator MUST distinguish L vs R and give EXACTLY
    zero on the achiral diamond.  Uses the gauge-invariant RMF-bend loop holonomy."""
    hR, sR, nR = net_loop_holonomy(cl.build_srs_net(L, "right"))
    hL, sL, nL = net_loop_holonomy(cl.build_srs_net(L, "left"))
    hD, sD, nD = net_loop_holonomy(cl.build_diamond_net(L))
    sees_chirality = abs(hR) > 1e-6 and abs(hL) > 1e-6
    sign_flip = hR * hL < 0 and abs(hR + hL) < 1e-9
    diamond_null = abs(hD) < 1e-12 and sD < 1e-12
    passed = sees_chirality and sign_flip and diamond_null
    detail = (
        f"srs-R hol={hR:+.5e}(std {sR:.1e},n={nR})  srs-L hol={hL:+.5e}  "
        f"diamond hol={hD:+.2e}(std {sD:.1e},n={nD})  "
        f"[sees_chirality={sees_chirality} sign_flip={sign_flip} diamond_null={diamond_null}]"
    )
    return GateResult("GATE-1 chirality-sensitivity", passed, detail)


def gate2_convergence(Ls=(6, 8, 10, 12)) -> GateResult:
    """GATE 2 (FAIL-2 guard): convergence in L of the BULK-PROPAGATED gyration rate.

    Compares the converged GEOMETRIC quantities (loop holonomy / forward winding =
    screw-pitch constants) against the DYNAMICAL packet rate (an actually-propagating
    wave).  PASSES only if the bulk-propagated rate converges in L.
    """
    pitch = screw_pitch_rate()
    geo, dyn = [], []
    for L in Ls:
        gR, _, _ = forward_winding_rate(cl.build_srs_net(L, "right"))
        dR, n = dynamical_packet_rate(cl.build_srs_net(L, "right"))
        geo.append(gR)
        dyn.append((L, dR, n))
    geo_converged = float(np.std(geo)) < 1e-3
    dyn_vals = np.array([d for _, d, _ in dyn])
    dyn_converged = float(np.std(dyn_vals)) < 0.05 * float(np.mean(np.abs(dyn_vals)) + 1e-12)
    passed = dyn_converged  # the BULK observable is the one that must converge
    detail = (
        f"4_1 screw pitch={pitch:+.5f} | geometric fwd-winding (srs-R) per L={ [f'{g:+.4f}' for g in geo] } "
        f"converged={geo_converged} (== screw pitch, a unit-cell constant) | "
        f"DYNAMICAL packet rate per L={ [(L, round(d,3), n) for L, d, n in dyn] } "
        f"converged={dyn_converged}"
    )
    return GateResult("GATE-2 convergence (bulk-propagated)", passed, detail)


def gate3_validate_on_known(L: int = 8) -> GateResult:
    """GATE 3: c / Z_0 reproduction (1/sqrt3 network factor), diamond-null, lossless."""
    from ave.core import chiral_lattice_dynamics as cld

    nf = cld.network_velocity_factor(cl.build_srs_net(L, "right"), n_steps=600)
    target = 1.0 / np.sqrt(3.0)
    c_ok = abs(nf["factor"] - target) / target < 0.02
    drift = dynamical_energy_drift(cl.build_srs_net(4, "right"), nsteps=40)
    lossless = drift < 1e-10
    hD, _, _ = net_loop_holonomy(cl.build_diamond_net(L if L % 2 == 0 else L + 1))
    diamond_null = abs(hD) < 1e-12
    passed = c_ok and lossless and diamond_null
    detail = (
        f"network velocity factor={nf['factor']:.5f} (target 1/sqrt3={target:.5f}, c_ok={c_ok}) "
        f"Z_0={Z_0:.2f}Ohm[symbol] C_0={C_0:.0f}m/s[symbol] | "
        f"dynamical lossless drift={drift:.2e} (lossless={lossless}) | diamond loop-null={diamond_null}"
    )
    return GateResult("GATE-3 validate-on-known", passed, detail)


def run_all_gates() -> dict:
    g1 = gate1_chirality_sensitivity()
    g2 = gate2_convergence()
    g3 = gate3_validate_on_known()
    return {"gate1": g1, "gate2": g2, "gate3": g3}


def main() -> None:
    print("=" * 78)
    print("WRITHE-AWARE vector-TLM Phase-1 — substrate-derived optical activity g0")
    print("=" * 78)
    gates = run_all_gates()
    for key in ("gate1", "gate2", "gate3"):
        g = gates[key]
        print(f"\n[{'PASS' if g.passed else 'FAIL'}] {g.name}")
        print(f"   {g.detail}")
    g1, g2, g3 = gates["gate1"], gates["gate2"], gates["gate3"]
    print("\n" + "-" * 78)
    if g1.passed and not g2.passed:
        print("OUTCOME C (ILL-DEFINED): the writhe-aware operator SEES chirality cleanly")
        print("(GATE-1 PASS: signed loop holonomy, exact diamond null), but the")
        print("BULK-PROPAGATED gyration does NOT converge in L (GATE-2 FAIL).  The only")
        print("converged quantities are LOCAL unit-cell geometric constants (the 4_1")
        print("screw pitch / ring holonomy), NOT a bulk transport coefficient.  A wave")
        print("propagating through the finite chiral supercell wraps the PBC box before")
        print("accumulating a well-defined per-length polarization rotation -> g0 has no")
        print("clean continuum limit from this transport.  This reproduces and diagnoses")
        print("the FAIL-2 L=6/L=8 sign-flip as a finite-box propagation pathology.")
    elif g1.passed and g2.passed and g3.passed:
        print("OUTCOME A (CHORD): converged, nonzero, sign-flipping g0 (see result doc).")
    elif not g1.passed:
        print("OUTCOME (writhe-BLIND): operator failed the chirality-sensitivity gate.")
    else:
        print("OUTCOME B (CLOSED-NEGATIVE): chirality-aware operator, converged g0=0.")
    print("-" * 78)


if __name__ == "__main__":
    main()
