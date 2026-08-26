"""P2 SCOPING probe 2 — outer fixed-point convergence NUMERICS ONLY.
Prints iteration counts, contraction ratios, residual logs. No field content.
"""
import json, sys, time
import numpy as np
sys.path.insert(0, "/Users/grantlindblom/AVE-staging/AVE-Core/src")
from ave.core.chiral_lattice import build_srs_net
import ave.solvers.harmonic_balance_srs as hb

L = 6
THETAS = (0.4, 0.6)
net = build_srs_net(L=L); bt = hb.build_bond_table(net); conn = net.connect_index()
f, b = hb.crossing_ports(net, bt, 0.5)


def term(d, n_tones=2):
    return hb.make_termination(
        net, bt, conn,
        [(f, np.full((n_tones, len(f)), d + 0j)), (b, np.zeros((n_tones, len(b))))],
        n_tones)


def contraction(hist):
    """ratio dA_{n+1}/dA_n over the tail — the outer map's measured contraction."""
    d = np.array([h["dA_inf"] for h in hist])
    d = d[d > 0]
    if len(d) < 3:
        return None
    r = d[1:] / d[:-1]
    return float(np.median(r[-5:])) if len(r) >= 5 else float(np.median(r))


print("=== A. relax sweep x drive (iteration counts + measured contraction) ===")
rows = []
for d in (0.1, 0.3, 0.5, 0.7, 0.9, 1.1):
    for relax in (1.0, 0.7, 0.5, 0.3, 0.15):
        t0 = time.perf_counter()
        try:
            res = hb.solve_self_consistent(
                net, bt, hb.ToneSet(thetas=THETAS), term(d),
                relax=relax, outer_tol=1e-10, max_outer=400,
                solve_kwargs={"tol": 1e-11, "warmstart": 0})
            row = dict(drive=d, relax=relax, n_outer=res.n_outer,
                       conv=bool(res.converged), contraction=contraction(res.history),
                       secs=round(time.perf_counter() - t0, 2),
                       tone_res_log10=[round(float(np.log10(max(s.residual_rel, 1e-300))), 1)
                                       for s in res.sols])
        except Exception as e:
            row = dict(drive=d, relax=relax, error=type(e).__name__ + ": " + str(e)[:80])
        rows.append(row); print(json.dumps(row), flush=True)

print("=== B. initial-guess sensitivity (same drive, 4 starts) ===")
d = 0.5
starts = {
    "zeros": np.zeros(bt.n_bonds),
    "uniform_0.3": np.full(bt.n_bonds, 0.3),
    "uniform_0.8": np.full(bt.n_bonds, 0.8),
    "random": np.random.default_rng(7).uniform(0.0, 0.9, bt.n_bonds),
}
final = {}
for name, A0 in starts.items():
    res = hb.solve_self_consistent(
        net, bt, hb.ToneSet(thetas=THETAS), term(d), A_init=A0,
        relax=0.5, outer_tol=1e-11, max_outer=600, solve_kwargs={"tol": 1e-11})
    final[name] = res.A_bond
    print(json.dumps(dict(start=name, n_outer=res.n_outer, conv=bool(res.converged),
                          contraction=contraction(res.history))), flush=True)
ref = final["zeros"]
for name, A in final.items():
    print(json.dumps(dict(start=name, log10_max_abs_diff_vs_zeros=round(
        float(np.log10(max(np.max(np.abs(A - ref)), 1e-300))), 2))), flush=True)

print("=== C. warmstart effect on inner matvec count (cold start, tone 0) ===")
a_cold, _ = hb.scatter_weights(bt, hb.bond_admittance(np.zeros(bt.n_bonds)))
for ws in (0, 50, 200, 800):
    t0 = time.perf_counter()
    s = hb.solve_tone(a_cold, conn, THETAS[0], term(0.5), 0, tol=1e-11, warmstart=ws)
    print(json.dumps(dict(warmstart=ws, n_matvec=s.n_matvec, conv=bool(s.converged),
                          res_log10=round(float(np.log10(max(s.residual_rel, 1e-300))), 1),
                          secs=round(time.perf_counter() - t0, 3))), flush=True)

print("=== D. inner solve conditioning vs tone placement (cold, matvec count) ===")
for th in (0.05, 0.1, 0.2, 0.4, 0.6, 0.9, 1.2, 1.5, 1.9, 2.4, 2.9, 3.1):
    try:
        s = hb.solve_tone(a_cold, conn, th, term(0.5), 0, tol=1e-11, warmstart=0)
        print(json.dumps(dict(theta=th, n_matvec=s.n_matvec, conv=bool(s.converged),
                              res_log10=round(float(np.log10(max(s.residual_rel, 1e-300))), 1))), flush=True)
    except Exception as e:
        print(json.dumps(dict(theta=th, error=str(e)[:80])), flush=True)
