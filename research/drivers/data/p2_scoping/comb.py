"""Commensurate mixing-comb closure for a 2:3 pair on integer time steps."""
import json
import numpy as np

def fold(t):
    t = float(np.mod(t, 2*np.pi))
    return 2*np.pi - t if t > np.pi else t

for M in (8, 10, 12, 16, 20, 24, 30, 36):
    w = 2*np.pi/M
    if 3*w >= np.pi:
        print(json.dumps(dict(M=M, note="3*omega >= pi: the 2:3 pair does not fit the (0,pi) domain")))
        continue
    lines, dead, alias = {}, [], {}
    for k in range(1, 4*M+1):
        ff = fold(k*w)
        key = int(round(ff/w)) if abs(ff/w - round(ff/w)) < 1e-9 else None
        if ff < 1e-12 or abs(ff-np.pi) < 1e-12:
            dead.append(k); continue
        lines.setdefault(key, []).append(k)
    print(json.dumps(dict(
        M=M, omega=round(w, 5), theta_2=round(2*w, 5), theta_3=round(3*w, 5),
        n_distinct_lines=len(lines),
        line_ks=sorted(lines.keys()),
        aliases_onto_line={str(k): v[:4] for k, v in sorted(lines.items())},
        forbidden_k_mod_M=sorted(set(k % M for k in dead)),
    )), flush=True)
