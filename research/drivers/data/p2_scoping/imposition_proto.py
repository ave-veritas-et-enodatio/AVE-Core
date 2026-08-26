"""P2 SCOPING probe 4 — PROTOTYPE of the alpha-agnostic winding-imposition plumbing.

Scratch-only prototype (the corpus is read-only for this session). Exercises the
interface against the shipped solver to prove the signatures close. Prints
STRUCTURE and NUMERICS only -- no solved-field content.
"""
from dataclasses import dataclass, replace
import json, sys
import numpy as np
sys.path.insert(0, "/Users/grantlindblom/AVE-staging/AVE-Core/src")
from ave.core.chiral_lattice import build_srs_net, LatticeNet
import ave.solvers.harmonic_balance_srs as hb


# ── 1. the boundary set, with the net's OWN cyclic coordinates ────────────────
@dataclass(frozen=True)
class BoundaryLoop:
    """A closed boundary port set + a cyclic coordinate per port.

    ports : (n,) flat directed INCIDENT slot indices (u*degree+p) -- what a
            Termination imposes.
    ang   : (n, 2) float, each port's (phi, psi) in rad on the boundary's own
            two cyclic directions. For a PBC plane cut x=const the cut surface
            IS a 2-torus: (phi, psi) = 2*pi*(y, z)/box, read off the bond
            midpoint. No Cartesian posit enters the DRIVE beyond this labelling.
    """
    ports: np.ndarray
    ang: np.ndarray
    label: str = ""


def plane_cut_loop(net: LatticeNet, bt, plane_cells: float, side: str = "fwd") -> BoundaryLoop:
    f, b = hb.crossing_ports(net, bt, plane_cells)
    slots = f if side == "fwd" else b
    d = net.degree
    box = net.box
    ang = np.zeros((len(slots), 2))
    for i, s in enumerate(slots):
        u, p = divmod(int(s), d)
        v = net.neighbors[u][p]
        mid = net.pos[u] + 0.5 * (
            (net.pos[v] - net.pos[u]) - box * np.round((net.pos[v] - net.pos[u]) / box))
        ang[i] = 2 * np.pi * np.mod(mid[1:3], box) / box
    return BoundaryLoop(ports=np.asarray(slots, dtype=np.int64), ang=ang,
                        label=f"plane[x={plane_cells},{side}]")


# ── 2. the imposition: a CLASS + a representative label, never an amplitude law ─
@dataclass(frozen=True)
class WindingImposition:
    """alpha-AGNOSTIC (2,3)-class imposition (epic guard 8).

    winding    : (p, q) INTEGERS -- the topological class, the only invariant.
    tube_phase : the representative label (the 'alpha' of guard 8): the inter-tone
                 relative phase. NOT an invariant; two values = two representatives.
    amp        : engineering drive scale, declared and swept. Carries no
                 fine-structure constant and no canon operating point.
    carrier    : where the class is written --
                 'tone'    : winding rides the TONE RATIO (theta_1:theta_2 = p:q),
                             port phases uniform -> the phase-space reading;
                 'spatial' : winding rides the boundary loop angles
                             exp(i(p*phi + q*psi)), one tone -> the real-space
                             reading;
                 'both'    : tone ratio AND loop texture (the mixed reading).
                 WHICH ONE THE PREREG MEANS IS A PHYSICS CALL, NOT AN ENGINEERING
                 ONE (epic guard 3 -- the (2,3) is a phase-space portrait).
    project_common_mode : quotient the per-tone drive by its own mean over the
                 loop (the decision-1 receipt: a uniform specification is gauge).
    """
    winding: tuple
    tube_phase: float
    amp: float
    loop: BoundaryLoop
    carrier: str = "tone"
    project_common_mode: bool = True

    def drive(self, n_tones: int) -> np.ndarray:
        p, q = self.winding
        n = len(self.loop.ports)
        phi, psi = self.loop.ang[:, 0], self.loop.ang[:, 1]
        d = np.zeros((n_tones, n), dtype=np.complex128)
        tone_phase = np.zeros(n_tones)
        tone_phase[1:] = self.tube_phase       # tube phase = inter-tone offset
        for m in range(n_tones):
            spatial = (np.exp(1j * (p * phi + q * psi))
                       if self.carrier in ("spatial", "both") else np.ones(n))
            d[m] = self.amp * np.exp(1j * tone_phase[m]) * spatial
        if self.project_common_mode:
            d = d - d.mean(axis=1, keepdims=True)
        return d

    def common_mode_receipt(self, n_tones: int) -> dict:
        raw = replace(self, project_common_mode=False).drive(n_tones)
        pro = replace(self, project_common_mode=True).drive(n_tones)
        return {
            "log10_rel_common_mode": float(np.log10(max(
                np.linalg.norm(raw - pro) / max(np.linalg.norm(raw), 1e-300), 1e-300))),
            "n_ports": int(len(self.loop.ports)),
        }


def make_winding_termination(net, bt, conn, imp: WindingImposition, n_tones: int,
                             absorb_side: BoundaryLoop | None = None):
    specs = [(imp.loop.ports, imp.drive(n_tones))]
    if absorb_side is not None:
        specs.append((absorb_side.ports, np.zeros((n_tones, len(absorb_side.ports)))))
    return hb.make_termination(net, bt, conn, specs, n_tones)


# ── 3. exercise ───────────────────────────────────────────────────────────────
if __name__ == "__main__":
    L = 4
    net = build_srs_net(L=L); bt = hb.build_bond_table(net); conn = net.connect_index()
    fwd = plane_cut_loop(net, bt, 0.5, "fwd")
    bwd = plane_cut_loop(net, bt, 0.5, "bwd")
    print(json.dumps(dict(loop=fwd.label, n_ports=int(len(fwd.ports)),
                          ang_span_phi=round(float(np.ptp(fwd.ang[:, 0])), 4),
                          ang_span_psi=round(float(np.ptp(fwd.ang[:, 1])), 4),
                          n_distinct_phi=int(len(np.unique(np.round(fwd.ang[:, 0], 9)))),
                          n_distinct_psi=int(len(np.unique(np.round(fwd.ang[:, 1], 9)))))))
    thetas = (2 * 2 * np.pi / 12, 3 * 2 * np.pi / 12)   # the 2:3 pair on the M=12 comb
    for carrier in ("tone", "spatial", "both"):
        for alpha in (0.0, 2 * np.pi / 5):
            imp = WindingImposition(winding=(2, 3), tube_phase=alpha, amp=0.4,
                                    loop=fwd, carrier=carrier)
            rec = imp.common_mode_receipt(2)
            try:
                term = make_winding_termination(net, bt, conn, imp, 2, absorb_side=bwd)
                res = hb.solve_self_consistent(
                    net, bt, hb.ToneSet(thetas=thetas), term,
                    relax=1.0, outer_tol=1e-10, max_outer=200,
                    solve_kwargs={"tol": 1e-11})
                out = dict(carrier=carrier, tube_phase=round(alpha, 4), **rec,
                           n_outer=res.n_outer, conv=bool(res.converged),
                           tone_res_log10=[round(float(np.log10(max(s.residual_rel, 1e-300))), 1)
                                           for s in res.sols])
            except Exception as e:
                out = dict(carrier=carrier, tube_phase=round(alpha, 4), **rec,
                           error=type(e).__name__ + ": " + str(e)[:90])
            print(json.dumps(out), flush=True)
