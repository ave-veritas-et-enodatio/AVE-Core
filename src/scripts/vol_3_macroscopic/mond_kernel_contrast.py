"""
MOND Kernel Adjudication — two-kernel SPARC contrast (research driver).

Prereg: research/2026-07-20_mond-kernel-adjudication_prereg.md (frozen-by-push).

Runs BOTH kernels through the IDENTICAL SPARC pipeline and banks both arms'
full statistics + the frozen decision-tree verdict:

  - QUADRATIC arm (canonical, engine byte-untouched): S_quad = sqrt(1 - (g_N/a_0)^2)
    via the shipped ave.regime_3_saturated.galactic_rotation.ave_rotation_velocity
    (-> ave_saturation_acceleration -> saturation_factor -> universal_saturation).
  - LINEAR arm (research-only variant, NO engine file modified): S_lin = sqrt(1 - g_N/a_0),
    reusing the canonical g_N and drag prefactor sqrt(g_N * a_0); the ONLY change is
    the kernel factor.

Primary (gating) metric: Q=1 mean|residual|. Frozen threshold tau = 1.020%
(jackknife SE of the Q=1 mean|residual| under the quadratic baseline; see prereg S4).

Pipeline reuse: parse + baryonic-mass + constants + GalaxyModel + A0_LATTICE are
imported from the existing sparc_catalog_ingest / galactic_rotation modules so the
two arms differ in EXACTLY one line (the kernel factor).
"""

import json
import sys
from pathlib import Path

import numpy as np

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parents[2]
sys.path.insert(0, str(REPO_ROOT / "src"))
sys.path.insert(0, str(SCRIPT_DIR))

# --- identical pipeline pieces, imported (not reimplemented) ---
from sparc_catalog_ingest import (  # noqa: E402
    KPC,
    SPARC_FILE,
    baryonic_mass_kg,
    parse_sparc_table1,
)
from ave.regime_3_saturated.galactic_rotation import (  # noqa: E402
    A0_LATTICE,
    GalaxyModel,
    ave_rotation_velocity,  # QUADRATIC canonical arm (byte-untouched engine)
)

FROZEN_TAU = 0.010198  # jackknife SE of Q=1 mean|residual|, quadratic baseline (prereg S4)
EVAL_SCALE = 5.0       # r_eval / R_disk, identical to sparc_catalog_ingest


def _v_ave_linear(galaxy: GalaxyModel, r: float, a0: float = A0_LATTICE) -> float:
    """LINEAR-kernel rotation velocity (research variant; engine byte-untouched).

    Identical to the canonical ave_rotation_velocity EXCEPT the kernel factor:
      canonical: S_quad = sqrt(1 - (g_N/a0)^2)     [clipped to 0 for g_N >= a0]
      variant:   S_lin  = sqrt(1 - g_N/a0)         [clipped to 0 for g_N >= a0]
    Uses the canonical newtonian_acceleration + the same sqrt(g_N*a0) drag prefactor.
    """
    g_n = galaxy.newtonian_acceleration(r)
    r_ratio = g_n / a0
    s_lin = np.sqrt(max(1.0 - r_ratio, 0.0))
    g_drag = np.sqrt(max(g_n * a0, 0.0)) * s_lin
    g_eff = g_n + g_drag
    return float(np.sqrt(g_eff * r))


def _bin_stats(residuals: np.ndarray) -> dict:
    r = np.asarray(residuals, dtype=float)
    absr = np.abs(r)
    return {
        "n": int(r.size),
        "mean_residual": float(r.mean()),
        "median_residual": float(np.median(r)),
        "mean_abs_residual": float(absr.mean()),
        "rms_residual": float(np.sqrt(np.mean(r**2))),
        "std_residual": float(r.std(ddof=0)),
    }


def _jackknife_se_mean(x: np.ndarray) -> float:
    x = np.asarray(x, dtype=float)
    n = x.size
    theta_i = np.array([np.delete(x, i).mean() for i in range(n)])
    return float(np.sqrt((n - 1) / n * np.sum((theta_i - theta_i.mean()) ** 2)))


def run_contrast() -> dict:
    galaxies = parse_sparc_table1(SPARC_FILE)

    rows = []
    for g in galaxies:
        M_bar = baryonic_mass_kg(g)
        R_d = g["Rdisk_kpc"] * KPC
        model = GalaxyModel(name=g["name"], M_disk=M_bar, R_d=R_d)
        r_eval = EVAL_SCALE * R_d
        v_obs = g["Vflat_kms"]
        v_quad = ave_rotation_velocity(model, r_eval, a0=A0_LATTICE) / 1000.0  # km/s
        v_lin = _v_ave_linear(model, r_eval, a0=A0_LATTICE) / 1000.0            # km/s
        if v_obs <= 0 or v_quad <= 0 or v_lin <= 0:
            continue
        g_n = model.newtonian_acceleration(r_eval)
        rows.append(
            {
                "name": g["name"],
                "Q": g["Q"],
                "r_ratio_at_eval": g_n / A0_LATTICE,
                "v_obs": v_obs,
                "v_quad": v_quad,
                "v_lin": v_lin,
                "res_quad": (v_quad - v_obs) / v_obs,
                "res_lin": (v_lin - v_obs) / v_obs,
            }
        )

    res_quad_all = np.array([x["res_quad"] for x in rows])
    res_lin_all = np.array([x["res_lin"] for x in rows])

    out = {
        "a0_lattice": float(A0_LATTICE),
        "eval_scale_Rdisk": EVAL_SCALE,
        "frozen_tau": FROZEN_TAU,
        "n_valid": len(rows),
        "all_sample": {
            "quadratic": _bin_stats(res_quad_all),
            "linear": _bin_stats(res_lin_all),
        },
        "by_Q": {},
        "r_ratio_range": [float(min(x["r_ratio_at_eval"] for x in rows)),
                          float(max(x["r_ratio_at_eval"] for x in rows))],
    }

    for q in (1, 2, 3):
        subset = [x for x in rows if x["Q"] == q]
        if not subset:
            continue
        rq = np.array([x["res_quad"] for x in subset])
        rl = np.array([x["res_lin"] for x in subset])
        out["by_Q"][str(q)] = {
            "quadratic": _bin_stats(rq),
            "linear": _bin_stats(rl),
        }

    # --- PRIMARY (gating) metric + frozen decision tree ---
    q1 = [x for x in rows if x["Q"] == 1]
    q1_quad = np.abs([x["res_quad"] for x in q1])
    q1_lin = np.abs([x["res_lin"] for x in q1])
    p_quad = float(q1_quad.mean())
    p_lin = float(q1_lin.mean())
    delta = p_lin - p_quad  # lower is better; >0 => quadratic better

    out["primary"] = {
        "metric": "Q=1 mean|residual|",
        "n_Q1": len(q1),
        "quadratic": p_quad,
        "linear": p_lin,
        "delta_lin_minus_quad": delta,
        "abs_delta": abs(delta),
        "tau": FROZEN_TAU,
        "q1_quad_jackknife_se": _jackknife_se_mean(q1_quad),
    }

    if abs(delta) < FROZEN_TAU:
        verdict = "KERNEL-DEGENERATE-ON-SPARC"
        route = "form-level (S5): QUADRATIC is axiom-forced -> sweep fires"
    elif delta >= FROZEN_TAU:
        verdict = "QUADRATIC-WINS"
        route = "quadratic canonical -> sweep fires"
    else:  # delta <= -tau
        verdict = "LINEAR-WINS-HARD-GATE"
        route = "STOP: do not touch engine, do not re-bank headline, route to Grant"
    out["verdict"] = verdict
    out["route"] = route
    return out


def main():
    out = run_contrast()
    dst = SCRIPT_DIR / "mond_kernel_contrast_results.json"
    dst.write_text(json.dumps(out, indent=2))

    p = out["primary"]
    print("=" * 78)
    print("MOND KERNEL ADJUDICATION — two-kernel SPARC contrast")
    print("=" * 78)
    print(f"a_0 = {out['a0_lattice']:.4e} m/s^2 | eval @ {out['eval_scale_Rdisk']}*R_disk"
          f" | n_valid = {out['n_valid']}")
    print(f"r=g_N/a_0 range at eval: [{out['r_ratio_range'][0]:.4f}, {out['r_ratio_range'][1]:.4f}]")
    print()
    print("PRIMARY (gating) = Q=1 mean|residual|  (N={})".format(p["n_Q1"]))
    print(f"  QUADRATIC (canonical) : {p['quadratic']*100:.3f}%")
    print(f"  LINEAR    (variant)   : {p['linear']*100:.3f}%")
    print(f"  Delta (lin - quad)    : {p['delta_lin_minus_quad']*100:+.3f}%  "
          f"(|Delta| = {p['abs_delta']*100:.3f}%)")
    print(f"  frozen tau            : {p['tau']*100:.3f}%")
    print()
    print("SECONDARY (disclosed, non-gating):")
    for scope, label in [("all_sample", "ALL (135)")]:
        q = out[scope]["quadratic"]
        l = out[scope]["linear"]
        print(f"  {label} mean|res|: quad {q['mean_abs_residual']*100:.2f}%  "
              f"lin {l['mean_abs_residual']*100:.2f}%   | "
              f"RMS: quad {q['rms_residual']*100:.2f}%  lin {l['rms_residual']*100:.2f}%")
    for q in ("1", "2", "3"):
        if q in out["by_Q"]:
            bq = out["by_Q"][q]["quadratic"]
            bl = out["by_Q"][q]["linear"]
            print(f"  Q={q} (n={bq['n']:3d}) mean|res|: quad {bq['mean_abs_residual']*100:.2f}%  "
                  f"lin {bl['mean_abs_residual']*100:.2f}%")
    print()
    print(f"VERDICT: {out['verdict']}")
    print(f"ROUTE  : {out['route']}")
    print(f"\nBanked: {dst}")
    return out


if __name__ == "__main__":
    main()
