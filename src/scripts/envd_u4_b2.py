"""
ENV-D U4 extended run — tasks (b) and (b2).

Runs U4 at one or more n_sub values.  For each run logs:
  - H(t) at every outer step
  - Kicked-site A2(t) at every outer step
  - eps_sq(t) at the kicked site (for |eps|^2 crossing detection)
  - x(t) = 1 - A2 at kicked site (for x=0 crossing detection)
  - max |omega| over whole field at every outer step
  - Crossing events for x=0 and |eps|^2=1
  - Max kicked-site A2
  - H trend: linear-fit slope, H_end-H0, mean(last quarter) - mean(first quarter)

Pre-registration sha: 5a9128a6266c (Math ruling on U4 discriminators).

Outputs written to ~/AVE-staging/runs/:
  envd_u4_b2_nsub{N}_trace.npz   — H, A2, eps_sq, omega_max arrays
  envd_u4_b2_nsub{N}_events.txt  — crossing events and H trend

Usage (default: n_sub=129,258,516, N_OUTER=2000):
    nohup caffeinate -i ~/AVE-staging/AVE-Core/.venv/bin/python \\
        /path/to/envd_u4_b2.py > ~/AVE-staging/runs/envd_u4_b2.log 2>&1 &

Usage (n_sub=1024, N_OUTER=2000 — reproduces D1024 from PR #1059):
    ~/AVE-staging/AVE-Core/.venv/bin/python src/scripts/envd_u4_b2.py 1024

Usage (smoke test: n_sub=1024, N_OUTER=5):
    ~/AVE-staging/AVE-Core/.venv/bin/python src/scripts/envd_u4_b2.py 1024 5

Arguments:
    argv[1] (optional): comma-separated n_sub values, e.g. "129,258,516" or "1024"
                        Default: "129,258,516"
    argv[2] (optional): N_OUTER steps override (integer).  Default: 2000.
"""

import sys, os, platform
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

import numpy as np
import jax
import jax.numpy as jnp

jax.config.update("jax_enable_x64", True)

from ave.topological.cosserat_field_3d import (
    CosseratField3D,
    _compute_strain,
    _compute_curvature,
)

RUNS_DIR = os.path.expanduser("~/AVE-staging/runs")
os.makedirs(RUNS_DIR, exist_ok=True)

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

N = 16
DX = 1.0
DELTA = 1e-3
OMEGA_YIELD = float(np.pi)
EPSILON_YIELD = 1.0
N_OUTER = int(sys.argv[2]) if len(sys.argv) > 2 else 2000
_N_SUB_ARG = sys.argv[1] if len(sys.argv) > 1 else "129,258,516"
N_SUB_LIST = [int(x) for x in _N_SUB_ARG.split(",")]


def build_solver():
    return CosseratField3D(
        N, N, N, pml_thickness=0,
        reflection_form="bond", reflection_delta=DELTA,
    )


def get_kick_site():
    s = build_solver()
    cx = cy = cz = N // 2
    alive = np.argwhere(s.mask_alive)
    dists = np.sum((alive - np.array([cx, cy, cz])) ** 2, axis=1)
    idx = np.argmin(dists)
    return tuple(alive[idx])


def compute_a2_at_site(solver, ki, kj, kk):
    u_j = jnp.asarray(solver.u)
    w_j = jnp.asarray(solver.omega)
    eps = _compute_strain(u_j, w_j, DX)
    kappa = _compute_curvature(w_j, DX)
    eps_sq = float(jnp.sum(eps[ki, kj, kk] ** 2))
    kappa_sq = float(jnp.sum(kappa[ki, kj, kk] ** 2))
    return eps_sq / EPSILON_YIELD ** 2 + kappa_sq / OMEGA_YIELD ** 2, eps_sq


# ---------------------------------------------------------------------------
# Single run
# ---------------------------------------------------------------------------

def run_u4(n_sub_fixed, cfl_dt, kick_site, label):
    ki, kj, kk = kick_site
    dt_sub = cfl_dt / n_sub_fixed

    solver = build_solver()
    kick_rate = 3.0 * float(np.sqrt(2.0)) * EPSILON_YIELD / cfl_dt
    solver.omega_dot[ki, kj, kk] = [0.0, 0.0, kick_rate * 0.1]
    solver.omega[ki, kj, kk] = [0.0, 0.0, 0.0]

    H0 = solver.total_energy() + solver.kinetic_energy()

    H_arr = np.empty(N_OUTER + 1, dtype=np.float64)
    A2_arr = np.empty(N_OUTER + 1, dtype=np.float64)
    eps_sq_arr = np.empty(N_OUTER + 1, dtype=np.float64)
    omega_max_arr = np.empty(N_OUTER + 1, dtype=np.float64)  # max |omega| over whole field

    a2_init, eps_sq_init = compute_a2_at_site(solver, ki, kj, kk)
    H_arr[0] = H0
    A2_arr[0] = a2_init
    eps_sq_arr[0] = eps_sq_init
    # per-site Euclidean length: sqrt(wx^2+wy^2+wz^2) then max over sites
    omega_max_arr[0] = float(np.max(np.sqrt(np.sum(np.asarray(solver.omega)**2, axis=-1))))

    nan_found = False
    crossing_x0 = []      # step indices where x=1-A2 crosses 0 (i.e., A2 crosses 1)
    crossing_eps1 = []     # step indices where eps_sq crosses 1

    prev_x = 1.0 - a2_init
    prev_eps_sq = eps_sq_init

    print(f"\n[{label}] n_sub={n_sub_fixed}  dt_sub={dt_sub:.4e}  H0={H0:.6e}")

    for step in range(N_OUTER):
        for sub in range(n_sub_fixed - 1):
            solver.step(dt_sub, apply_pml=False)
        solver.step(dt_sub, apply_pml=True)

        if not np.isfinite(solver.u).all() or not np.isfinite(solver.omega).all():
            nan_found = True
            print(f"  [{label}] NaN at outer step {step}")
            H_arr[step + 1] = np.nan
            A2_arr[step + 1] = np.nan
            eps_sq_arr[step + 1] = np.nan
            omega_max_arr[step + 1] = np.nan
            break

        H = solver.total_energy() + solver.kinetic_energy()
        a2, eps_sq = compute_a2_at_site(solver, ki, kj, kk)
        x = 1.0 - a2

        H_arr[step + 1] = H
        A2_arr[step + 1] = a2
        eps_sq_arr[step + 1] = eps_sq
        # per-site Euclidean length
        omega_max_arr[step + 1] = float(np.max(np.sqrt(np.sum(np.asarray(solver.omega)**2, axis=-1))))

        # Crossing detection
        if prev_x * x < 0:   # sign change
            crossing_x0.append(step + 1)
        if (prev_eps_sq - 1.0) * (eps_sq - 1.0) < 0:
            crossing_eps1.append(step + 1)

        prev_x = x
        prev_eps_sq = eps_sq

        if (step + 1) % 200 == 0:
            dH = abs(H - H0) / max(abs(H0), 1e-12)
            print(f"  [{label}] step={step+1:4d}  H={H:.6e}  |H-H0|/H0={dH:.4e}"
                  f"  A2_kick={a2:.4f}  max|omega|={omega_max_arr[step+1]:.4f}")

    # Trim if nan
    valid = N_OUTER + 1 if not nan_found else (np.argmax(np.isnan(H_arr)) if np.any(np.isnan(H_arr)) else N_OUTER + 1)

    H_valid = H_arr[:valid]
    A2_valid = A2_arr[:valid]
    eps_sq_valid = eps_sq_arr[:valid]
    omega_max_valid = omega_max_arr[:valid]

    max_dH = float(np.max(np.abs(H_valid - H0)) / max(abs(H0), 1e-12))
    max_a2 = float(np.nanmax(A2_valid))
    monotone_H = bool(np.all(np.diff(H_valid) >= 0))

    # H trend (more informative than per-step monotone flag for noisy pumping)
    if len(H_valid) >= 4:
        t_arr = np.arange(len(H_valid), dtype=np.float64)
        h_slope = float(np.polyfit(t_arr, H_valid, 1)[0])
        quarter = max(1, len(H_valid) // 4)
        h_mean_diff = float(H_valid[-quarter:].mean() - H_valid[:quarter].mean())
    else:
        h_slope = float("nan")
        h_mean_diff = float("nan")
    h_end_minus_h0 = float(H_valid[-1]) - float(H0)

    a2_peak_step = int(np.nanargmax(A2_valid))
    omega_max_at_a2_peak = float(omega_max_valid[a2_peak_step])

    print(f"  [{label}] DONE  max|H-H0|/H0={max_dH:.4e}  max_A2_kick={max_a2:.4f}"
          f"  x0_crossings={len(crossing_x0)}  eps1_crossings={len(crossing_eps1)}"
          f"  H_monotone={monotone_H}")
    print(f"  [{label}] H trend: slope={h_slope:.4e}  H_end-H0={h_end_minus_h0:.4e}"
          f"  mean(last_Q)-mean(first_Q)={h_mean_diff:.4e}")
    print(f"  [{label}] A2 peak step={a2_peak_step}"
          f"  max|omega|_at_A2_peak={omega_max_at_a2_peak:.6f} (pi={np.pi:.6f})"
          f"  end A2={A2_valid[-1]:.6f}")

    # Save trace
    trace_path = os.path.join(RUNS_DIR, f"envd_u4_b2_nsub{n_sub_fixed}_trace.npz")
    np.savez(
        trace_path,
        H=H_valid,
        H0=np.float64(H0),
        A2_kick=A2_valid,
        eps_sq_kick=eps_sq_valid,
        omega_max=omega_max_valid,
        n_sub=np.int64(n_sub_fixed),
        dt_sub=np.float64(dt_sub),
        max_dH=np.float64(max_dH),
        max_a2_kick=np.float64(max_a2),
        monotone_H=np.bool_(monotone_H),
        h_slope=np.float64(h_slope),
        h_end_minus_h0=np.float64(h_end_minus_h0),
        h_mean_diff=np.float64(h_mean_diff),
        a2_peak_step=np.int64(a2_peak_step),
        omega_max_at_a2_peak=np.float64(omega_max_at_a2_peak),
    )
    print(f"  [{label}] Trace saved: {trace_path}")

    # Save events
    events_path = os.path.join(RUNS_DIR, f"envd_u4_b2_nsub{n_sub_fixed}_events.txt")
    with open(events_path, "w") as f:
        f.write(f"n_sub={n_sub_fixed}  dt_sub={dt_sub:.6e}  H0={H0:.15g}\n")
        f.write(f"max_dH_over_H0={max_dH:.6e}  max_A2_kick={max_a2:.6f}\n")
        f.write(f"H_monotone_nondecreasing={monotone_H}\n")
        f.write(f"H_slope={h_slope:.6e}  H_end_minus_H0={h_end_minus_h0:.6e}"
                f"  H_mean_lastQ_minus_firstQ={h_mean_diff:.6e}\n")
        f.write(f"A2_peak_step={a2_peak_step}"
                f"  omega_max_at_A2_peak={omega_max_at_a2_peak:.12g}"
                f"  end_A2={A2_valid[-1]:.12g}\n")
        f.write(f"\nx=0 crossings (outer step index): {crossing_x0}\n")
        f.write(f"|eps|^2=1 crossings (outer step index): {crossing_eps1}\n")
        f.write(f"\n# H(t) around x=0 crossings (±5 steps):\n")
        for ev in crossing_x0:
            lo, hi = max(0, ev - 5), min(len(H_valid) - 1, ev + 5)
            f.write(f"  crossing at step={ev}:\n")
            for s in range(lo, hi + 1):
                f.write(f"    step={s}  H={H_valid[s]:.12e}  A2={A2_valid[min(s,len(A2_valid)-1)]:.6f}"
                        f"  eps_sq={eps_sq_valid[min(s,len(eps_sq_valid)-1)]:.6f}\n")
        f.write(f"\n# H(t) around |eps|^2=1 crossings (±5 steps):\n")
        for ev in crossing_eps1:
            lo, hi = max(0, ev - 5), min(len(H_valid) - 1, ev + 5)
            f.write(f"  crossing at step={ev}:\n")
            for s in range(lo, hi + 1):
                f.write(f"    step={s}  H={H_valid[s]:.12e}  A2={A2_valid[min(s,len(A2_valid)-1)]:.6f}"
                        f"  eps_sq={eps_sq_valid[min(s,len(eps_sq_valid)-1)]:.6f}\n")
    print(f"  [{label}] Events saved: {events_path}")

    return {
        "n_sub": n_sub_fixed,
        "max_dH": max_dH,
        "max_a2_kick": max_a2,
        "nan": nan_found,
        "monotone_H": monotone_H,
        "h_slope": h_slope,
        "h_end_minus_h0": h_end_minus_h0,
        "h_mean_diff": h_mean_diff,
        "x0_crossings": crossing_x0,
        "eps1_crossings": crossing_eps1,
        "trace_path": trace_path,
        "events_path": events_path,
    }


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    # Build a reference solver to get cfl_dt
    ref = build_solver()
    cfl_dt = ref.cfl_dt

    # Run-start platform banner (Math Addendum 4 / R26.168 knot-run provenance)
    _omega_dtype = np.asarray(ref.omega).dtype
    _u_dtype = np.asarray(ref.u).dtype
    print(f"[platform] {platform.platform()}")
    print(f"[jax] backend={jax.default_backend()}  version={jax.__version__}"
          f"  omega_dtype={_omega_dtype}  u_dtype={_u_dtype}")

    print(f"cfl_dt = {cfl_dt:.8e}")
    print(f"N_OUTER = {N_OUTER}  n_sub_list = {N_SUB_LIST}")

    kick_site = get_kick_site()
    print(f"Kick site: {kick_site}")

    results = []
    for n_sub in N_SUB_LIST:
        r = run_u4(n_sub, cfl_dt, kick_site, label=f"U4 n_sub={n_sub}")
        results.append(r)

    print("\n" + "="*60)
    print("SUMMARY")
    print("="*60)
    d_vals = {}
    for r in results:
        ns = r["n_sub"]
        d = r["max_dH"]
        d_vals[ns] = d
        print(f"  D{ns:4d} = {d:.4e}  max_A2_kick={r['max_a2_kick']:.4f}"
              f"  monotone_H={r['monotone_H']}  NaN={r['nan']}")
        print(f"         H slope={r['h_slope']:.4e}"
              f"  H_end-H0={r['h_end_minus_h0']:.4e}"
              f"  mean_diff(lastQ-firstQ)={r['h_mean_diff']:.4e}")

    print()
    sorted_keys = sorted(d_vals.keys())
    for i in range(len(sorted_keys) - 1):
        n1, n2 = sorted_keys[i], sorted_keys[i + 1]
        ratio = d_vals[n1] / max(d_vals[n2], 1e-15)
        print(f"  r(D{n1}/D{n2}) = {ratio:.3f}")

    print()
    for r in results:
        print(f"  Trace: {r['trace_path']}")
        print(f"  Events: {r['events_path']}")
