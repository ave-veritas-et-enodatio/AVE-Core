"""P2 ENGINEERING SCOPING — cost/scaling of the two-tone graded HB solve.
NUMERICS ONLY. No field content is printed anywhere in this script.
"""
import json, os, resource, sys, time
import numpy as np

sys.path.insert(0, "/Users/grantlindblom/AVE-staging/AVE-Core/src")
from ave.core.chiral_lattice import build_srs_net
import ave.solvers.harmonic_balance_srs as hb

DRIVE = 0.2          # engineering amplitude, numerics only
THETAS = (0.4, 0.6)  # 2:3 ratio, canonical (0, pi)


def rss_mb():
    return resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / (1024 * 1024)


def run(L, max_outer=60, relax=0.7, outer_tol=1e-10, warmstart=0, tol=1e-11):
    rec = {"L": L}
    t0 = time.perf_counter()
    net = build_srs_net(L=L)
    t1 = time.perf_counter()
    bt = hb.build_bond_table(net)
    t2 = time.perf_counter()
    conn = net.connect_index()
    t3 = time.perf_counter()
    rec.update(
        n_nodes=net.n_nodes, degree=net.degree, ndof=net.n_nodes * net.degree,
        n_bonds=int(bt.n_bonds),
        t_build_net=t1 - t0, t_bond_table=t2 - t1, t_connect=t3 - t2,
    )
    f, b = hb.crossing_ports(net, bt, 0.5)
    rec["n_crossing_fwd"] = int(len(f))
    term = hb.make_termination(
        net, bt, conn,
        [(f, np.full((2, len(f)), DRIVE + 0j)), (b, np.zeros((2, len(b))))], 2,
    )
    rec["n_terminated"] = int(len(term.ports))
    # --- single cold tone solve (linear cost probe) ---
    a_cold, _ = hb.scatter_weights(bt, hb.bond_admittance(np.zeros(bt.n_bonds)))
    t = time.perf_counter()
    s = hb.solve_tone(a_cold, conn, THETAS[0], term, 0, tol=tol, warmstart=warmstart)
    rec["t_tone_cold"] = time.perf_counter() - t
    rec["n_matvec_cold"] = s.n_matvec
    rec["conv_cold"] = bool(s.converged)
    rec["res_cold_log10"] = float(np.log10(max(s.residual_rel, 1e-300)))
    # --- matvec microbenchmark ---
    v = np.random.default_rng(0).standard_normal((net.n_nodes, net.degree)) + 0j
    n_rep = max(3, int(2e6 / max(rec["ndof"], 1)))
    t = time.perf_counter()
    for _ in range(n_rep):
        hb.apply_M(a_cold, conn, v)
    rec["t_matvec"] = (time.perf_counter() - t) / n_rep
    # --- full two-tone self-consistent solve ---
    m0 = rss_mb()
    t = time.perf_counter()
    res = hb.solve_self_consistent(
        net, bt, hb.ToneSet(thetas=THETAS), term,
        relax=relax, outer_tol=outer_tol, max_outer=max_outer,
        solve_kwargs={"tol": tol, "warmstart": warmstart},
    )
    rec["t_selfconsistent"] = time.perf_counter() - t
    rec["rss_after_mb"] = rss_mb()
    rec["rss_delta_mb"] = rec["rss_after_mb"] - m0
    rec["n_outer"] = res.n_outer
    rec["outer_converged"] = bool(res.converged)
    rec["dA_hist_log10"] = [float(np.log10(max(h["dA_inf"], 1e-300))) for h in res.history]
    rec["tone_res_log10_last"] = [float(np.log10(max(r, 1e-300))) for r in res.history[-1]["residuals"]]
    rec["matvec_per_tone_solve"] = [s.n_matvec for s in res.sols]
    return rec


if __name__ == "__main__":
    Ls = [int(x) for x in sys.argv[1:]] or [2, 3, 4]
    out = []
    for L in Ls:
        r = run(L)
        out.append(r)
        print(json.dumps({k: v for k, v in r.items() if k != "dA_hist_log10"}), flush=True)
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), "scale_results.json")
    with open(p, "a") as fh:
        for r in out:
            fh.write(json.dumps(r) + "\n")
