"""P2 SCOPING probe 2b — outer-loop acceleration + guess sensitivity. NUMERICS ONLY."""
import json, sys, time
import numpy as np
sys.path.insert(0, "/Users/grantlindblom/AVE-staging/AVE-Core/src")
from ave.core.chiral_lattice import build_srs_net
import ave.solvers.harmonic_balance_srs as hb

L = 4
THETAS = (2*2*np.pi/12, 3*2*np.pi/12)
net = build_srs_net(L=L); bt = hb.build_bond_table(net); conn = net.connect_index()
f, b = hb.crossing_ports(net, bt, 0.5)


def term(d, n_tones=2):
    return hb.make_termination(net, bt, conn,
        [(f, np.full((n_tones, len(f)), d + 0j)), (b, np.zeros((n_tones, len(b))))], n_tones)


def E(A, tm, prev=None):
    """one envelope map application A -> E(A); returns (A_new, sols, matvecs)."""
    a_nodes, _ = hb.scatter_weights(bt, hb.bond_admittance(A))
    sols = [hb.solve_tone(a_nodes, conn, th, tm, tone_index=m,
                          x0=(prev[m] if prev else None), tol=1e-12, warmstart=0)
            for m, th in enumerate(THETAS)]
    return hb.envelope_A_bond(bt, sols), sols, sum(s.n_matvec for s in sols)


def picard(A0, tm, relax, tol=1e-10, maxit=200):
    A = A0.copy(); prev = None; hist = []; mv = 0
    for it in range(1, maxit+1):
        An, sols, m = E(A, tm, prev); mv += m; prev = [s.v for s in sols]
        d = float(np.max(np.abs(An - A))); hist.append(d)
        A = (1-relax)*A + relax*An
        if d < tol:
            return dict(it=it, conv=True, hist=hist, matvec=mv), A
    return dict(it=maxit, conv=False, hist=hist, matvec=mv), A


def anderson(A0, tm, depth=6, beta=1.0, tol=1e-10, maxit=200):
    """Anderson/DIIS mixing on the residual F(A) = E(A) - A."""
    A = A0.copy(); prev = None; hist = []; mv = 0
    Gs, Fs = [], []
    for it in range(1, maxit+1):
        GA, sols, m = E(A, tm, prev); mv += m; prev = [s.v for s in sols]
        F = GA - A
        d = float(np.max(np.abs(F))); hist.append(d)
        if d < tol:
            return dict(it=it, conv=True, hist=hist, matvec=mv, depth=depth), A
        Gs.append(GA); Fs.append(F)
        if len(Gs) > depth: Gs.pop(0); Fs.pop(0)
        k = len(Fs)
        if k == 1:
            A = A + beta*F
        else:
            dF = np.column_stack([Fs[i+1]-Fs[i] for i in range(k-1)])
            dG = np.column_stack([Gs[i+1]-Gs[i] for i in range(k-1)])
            gamma, *_ = np.linalg.lstsq(dF, Fs[-1], rcond=None)
            A = Gs[-1] - dG @ gamma
        A = np.clip(A, 0.0, 0.999)
    return dict(it=maxit, conv=False, hist=hist, matvec=mv, depth=depth), A


print("=== A. strongly-engaged point: Picard relax sweep (capped) vs Anderson ===")
D = 0.9
tm = term(D)
A0 = np.zeros(bt.n_bonds)
for relax in (1.0, 0.7, 0.5, 0.3):
    t0 = time.perf_counter()
    r, _ = picard(A0, tm, relax, maxit=150)
    print(json.dumps(dict(method=f"picard(relax={relax})", it=r["it"], conv=r["conv"],
        tail_ratio=round(float(np.median(np.array(r["hist"][-6:-1])/np.array(r["hist"][-5:]))), 4) if len(r["hist"])>6 else None,
        log10_final=round(float(np.log10(max(r["hist"][-1],1e-300))),2),
        matvec=r["matvec"], secs=round(time.perf_counter()-t0,1))), flush=True)
for depth in (3, 6, 10):
    t0 = time.perf_counter()
    r, _ = anderson(A0, tm, depth=depth, maxit=150)
    print(json.dumps(dict(method=f"anderson(depth={depth})", it=r["it"], conv=r["conv"],
        log10_final=round(float(np.log10(max(r["hist"][-1],1e-300))),2),
        matvec=r["matvec"], secs=round(time.perf_counter()-t0,1))), flush=True)

print("=== B. amplitude continuation (warm-started ladder) to the same endpoint ===")
t0 = time.perf_counter(); A = np.zeros(bt.n_bonds); tot_it = 0; tot_mv = 0
for d in (0.3, 0.5, 0.7, 0.8, 0.9):
    r, A = picard(A, term(d), 1.0, maxit=150)
    tot_it += r["it"]; tot_mv += r["matvec"]
    print(json.dumps(dict(rung=d, it=r["it"], conv=r["conv"])), flush=True)
print(json.dumps(dict(method="continuation+picard", total_it=tot_it, matvec=tot_mv,
                      secs=round(time.perf_counter()-t0,1))), flush=True)

print("=== C. initial-guess sensitivity at a mildly engaged point ===")
tm2 = term(0.5)
starts = {"zeros": np.zeros(bt.n_bonds),
          "uniform_0.3": np.full(bt.n_bonds, 0.3),
          "uniform_0.8": np.full(bt.n_bonds, 0.8),
          "random": np.random.default_rng(7).uniform(0.0, 0.9, bt.n_bonds)}
fin = {}
for name, A0s in starts.items():
    r, A = picard(A0s, tm2, 1.0, tol=1e-12, maxit=300)
    fin[name] = A
    print(json.dumps(dict(start=name, it=r["it"], conv=r["conv"], matvec=r["matvec"])), flush=True)
ref = fin["zeros"]
print(json.dumps({k: round(float(np.log10(max(np.max(np.abs(v-ref)),1e-300))),2) for k,v in fin.items()}), flush=True)

print("=== D. inner conditioning vs tone placement (cold network, matvec count) ===")
a_cold, _ = hb.scatter_weights(bt, hb.bond_admittance(np.zeros(bt.n_bonds)))
for th in (0.05,0.1,0.2,0.4,0.5236,0.8,1.0472,1.5,1.5708,2.0,2.5,3.0,3.10):
    s = hb.solve_tone(a_cold, conn, th, tm2, 0, tol=1e-11, warmstart=0)
    print(json.dumps(dict(theta=round(th,4), n_matvec=s.n_matvec, conv=bool(s.converged),
                          res_log10=round(float(np.log10(max(s.residual_rel,1e-300))),1))), flush=True)

print("=== E. warmstart effect (cold network, one tone) ===")
for ws in (0, 50, 200, 800):
    t0=time.perf_counter()
    s = hb.solve_tone(a_cold, conn, THETAS[0], tm2, 0, tol=1e-11, warmstart=ws)
    print(json.dumps(dict(warmstart=ws, n_matvec=s.n_matvec, conv=bool(s.converged),
                          res_log10=round(float(np.log10(max(s.residual_rel,1e-300))),1),
                          secs=round(time.perf_counter()-t0,3))), flush=True)
