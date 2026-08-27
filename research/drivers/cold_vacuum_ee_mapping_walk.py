"""Cold-vacuum phase-space/real-space EE-mapping walk — the MEASURED lane.

Companion to research/2026-08-27_cold-vacuum-phase-real-space-ee-mapping_walk_RECORD.md
(§3 and §4). WALK-GRADE: this driver measures properties of the SHIPPED cold
scatter operator. It mints nothing and adjudicates nothing.

READ-ONLY on every engine primitive: imports ave.core.chiral_lattice and
ave.solvers.vacuum_varactor_scatter, mutates neither.

M1  cold specialisation of the junction spectrum, z=3 (ratified srs) and z=4
M2  the cold traceless collapse is SPECIAL: graded Y => balanced != traceless
M3  the circuit reading: node voltage and PORT CURRENTS in each eigenmode
M4  is a GLOBAL common-mode offset a symmetry? cold vs saturated
M5  gauge-breaking vs saturation depth (the (1-S) scaling)

alpha-free: every quantity here is linear algebra on dimensionless admittances.
"""
from __future__ import annotations
import numpy as np

from ave.core.chiral_lattice import (
    build_srs_net, scatter_matrix, scalar_tlm_step, lattice_energy,
)
from ave.solvers.vacuum_varactor_scatter import (
    admittance_scatter, bond_admittance_from_saturation, saturation_kernel,
)

SEED = 20260827


def m1_cold_specialisation() -> dict:
    """At A=0 the varactor operator IS the bedrock; spectrum {+1 once, -1 (z-1)}."""
    out = {}
    for z in (3, 4):
        S_bed = scatter_matrix(z)
        Y = bond_admittance_from_saturation(np.zeros(z))      # A=0 => S=1 => Y=Y0
        S_var = admittance_scatter(Y)
        w = np.sort(np.real(np.linalg.eigvals(S_var)))
        ones = np.ones(z) / np.sqrt(z)
        # orthonormal basis of the TRACELESS subspace {v : sum v = 0}
        B = np.linalg.svd(np.ones((1, z)))[2][1:].T
        out[f"z{z}"] = dict(
            bit_identical=bool(np.array_equal(S_bed, S_var)),
            n_plus1=int(np.sum(np.isclose(w, 1.0))),
            n_minus1=int(np.sum(np.isclose(w, -1.0))),
            common_residual=float(np.linalg.norm(S_var @ ones - ones)),
            traceless_residual=float(np.linalg.norm(S_var @ B + B)),
        )
    return out


def m2_graded_breaks_traceless() -> dict:
    """Cold => balanced == traceless. Graded => balanced != traceless."""
    out = {}
    cases = {"cold_uniform": np.ones(3),
             "graded_4decade": np.array([1e-2, 1.0, 1e2]),
             "one_bond_1e6": np.array([1.0, 1.0, 1e6])}
    for tag, Y in cases.items():
        S = admittance_scatter(Y)
        v_traceless = np.array([1.0, -1.0, 0.0])            # sum v = 0
        v_balanced = np.array([1.0, -Y[0] / Y[1], 0.0])     # sum Y_j v_j = 0
        out[tag] = dict(
            eig=[float(x) for x in np.sort(np.real(np.linalg.eigvals(S)))],
            traceless_residual=float(np.linalg.norm(S @ v_traceless + v_traceless)),
            balanced_residual=float(np.linalg.norm(S @ v_balanced + v_balanced)),
        )
    return out


def m3_circuit_reading() -> dict:
    """V_node = V_inc + V_ref (every port); I_port,i = Y_i (V_i^inc - V_i^ref)."""
    out = {}
    for z, tag, Y in [(3, "cold_z3", np.ones(3)), (4, "cold_z4", np.ones(4)),
                      (3, "graded_z3", np.array([1e-2, 1.0, 1e2]))]:
        S = admittance_scatter(Y)
        rows = []
        for a in (1.0, 0.25, -3.7):
            vi = a * np.ones(z)
            vr = S @ vi
            rows.append(dict(a=a,
                             V_node=float(np.mean(vi + vr)),
                             V_node_spread=float(np.ptp(vi + vr)),
                             I_max=float(np.max(np.abs(Y * (vi - vr))))))
        v = np.zeros(z); v[0] = 1.0; v[1] = -Y[0] / Y[1]
        vr = S @ v
        out[tag] = dict(common=rows,
                        diff_V_node_max=float(np.max(np.abs(v + vr))),
                        diff_I_max=float(np.max(np.abs(Y * (v - vr)))),
                        diff_I_sum=float(np.sum(Y * (v - vr))))
    return out


def _saturating_step(net, conn, V, N):
    """One scatter+connect step with the varactor READING the local |V|."""
    A = np.clip(np.abs(V), 0.0, 0.999)
    V_ref = np.empty_like(V)
    for u in range(N):
        V_ref[u] = admittance_scatter(bond_admittance_from_saturation(A[u])) @ V[u]
    src, dst = conn
    V_new = np.zeros_like(V)
    V_new.flat[dst] = V_ref.flat[src]
    return V_new


def m4_offset_symmetry(L: int = 3, steps: int = 8) -> dict:
    """Cold: a global common-mode offset rides EXACTLY. Saturated: it does not."""
    rng = np.random.default_rng(SEED)
    net = build_srs_net(L=L); N, d = net.n_nodes, net.degree
    conn = net.connect_index(); S_cold = scatter_matrix(d)
    V0 = rng.normal(size=(N, d)) * 0.02          # small: no saturation clipping
    out = {"n_nodes": N, "degree": d, "cold": {}, "saturated": {}}
    for delta in (0.001, 0.01, 0.05):
        A, B, worst = V0.copy(), V0 + delta, 0.0
        for _ in range(steps):
            A = scalar_tlm_step(net, A, S_cold, conn)
            B = scalar_tlm_step(net, B, S_cold, conn)
            worst = max(worst, float(np.max(np.abs((B - A) - delta))))
        out["cold"][str(delta)] = worst
        A, B = V0.copy(), V0 + delta
        per_step = []
        for _ in range(steps):
            A = _saturating_step(net, conn, A, N)
            B = _saturating_step(net, conn, B, N)
            per_step.append(float(np.max(np.abs((B - A) - delta))))
        out["saturated"][str(delta)] = dict(step1=per_step[0], last=per_step[-1],
                                            step1_over_delta=per_step[0] / delta)
    return out


def m5_breaking_vs_saturation(L: int = 3, delta: float = 0.01) -> dict:
    """The gauge freedom degrades CONTINUOUSLY, tracking (1 - S)."""
    rng = np.random.default_rng(7)
    net = build_srs_net(L=L); N, d = net.n_nodes, net.degree
    conn = net.connect_index()
    base = rng.normal(size=(N, d)); base /= np.abs(base).max()
    rows = []
    for scale in (0.0, 1e-4, 1e-3, 1e-2, 3e-2, 1e-1, 3e-1, 6e-1):
        V0 = base * scale
        A = _saturating_step(net, conn, V0, N)
        B = _saturating_step(net, conn, V0 + delta, N)
        maxA = float(np.abs(V0).max())
        one_minus_S = float(1.0 - saturation_kernel(np.array([min(maxA, 0.999)]))[0])
        rows.append(dict(scale=scale, max_A=maxA, one_minus_S=one_minus_S,
                         break_over_delta=float(np.max(np.abs((B - A) - delta)) / delta)))
    return {"rows": rows}


def main() -> dict:
    res = dict(m1=m1_cold_specialisation(), m2=m2_graded_breaks_traceless(),
               m3=m3_circuit_reading(), m4=m4_offset_symmetry(),
               m5=m5_breaking_vs_saturation())
    import json
    print(json.dumps(res, indent=2))
    return res


if __name__ == "__main__":
    main()
