"""Stage-2 NATIVE-CAGE — THE MAKE-OR-BREAK driver (run ONLY after G1-G8 pass).

Prereg : research/2026-06-23_engine-stage2-native-cage_prereg.md (RE-FROZEN).

The genuinely-open question (§0.2): does a seeded SECH precursor (v14 Mode-I:
N=24, A=0.85, sech) TIME-DOMAIN self-trap and PERSIST (Mode I) or DISPERSE
(Mode III) on the native tetrahedral K4 stencil, with the co-acting cage engaged?

Two-sided result (§0.4): Mode III on the native stencil WITH the correct MINUS
sign + sech seed + co-acting cage is a LEGITIMATE FALSIFICATION (the self-trap is
a Cartesian artifact), reported as such — NOT debugged toward a rescue (§11).

Observable (§7.1): mean interior-peak |V| (PML-excluded), NOT centroid.
Control  (§8a):   matched-amplitude GAUSSIAN must DISPERSE (apparatus-sees-it).
N-robust (§8a I-7): verdict must agree at N=20, 24, 32.

α-clean. NO ALPHA / Q_TANK / 137 anywhere.
"""

import json

import numpy as np

from ave.core.master_equation_fdtd import MasterEquationFDTD
from ave.solvers.native_cage_fdtd import NativeCageConfig, NativeCageFDTD

# v14 Mode-I frozen window (test_master_equation_v14_mode_i.py:39-41).
N_STEPS_TOTAL = 600
N_STEPS_TRANSIENT = 200
SEED_AMP = 0.85
SEED_RADIUS = 2.5
DX = 0.5


def _gaussian_seed(N, *, amp, sigma, dx):
    c = N // 2
    i, j, k = np.indices((N, N, N))
    r2 = ((i - c) ** 2 + (j - c) ** 2 + (k - c) ** 2) * (dx**2)
    return amp * np.exp(-r2 / (2.0 * sigma**2))


def run_native(N, *, profile, amp=SEED_AMP, radius=SEED_RADIUS, sign=-1.0):
    cfg = NativeCageConfig(N=N, dx=DX, sign=sign)
    eng = NativeCageFDTD(cfg)
    if profile == "sech":
        eng.seed_sech(amplitude=amp, radius=radius)
    elif profile == "gaussian":
        eng.seed_field(_gaussian_seed(N, amp=amp, sigma=radius, dx=DX))
    else:
        raise ValueError(profile)
    dt_info = eng.set_dt_from_seed(n_iter=200)
    res = eng.run_record(N_STEPS_TOTAL, N_STEPS_TRANSIENT)
    res["dt_info"] = dt_info
    res["N"] = N
    res["profile"] = profile
    return res


def run_cartesian_reference(N=24):
    """C-1: re-run the v14 Mode-I on the Cartesian engine (the reference axis)."""
    eng = MasterEquationFDTD(N=N, dx=DX, V_yield=1.0, c0=1.0, cfl_safety=0.4, pml_thickness=4)
    c = N // 2
    coords = np.arange(N) - c
    X, Y, Z = np.meshgrid(coords, coords, coords, indexing="ij")
    r = np.sqrt(X**2 + Y**2 + Z**2) * DX
    seed = SEED_AMP * (1.0 / np.cosh(r / SEED_RADIUS))
    eng.V[:] = seed
    eng.V_prev[:] = seed.copy()
    t = eng.pml_thickness
    interior = np.zeros((N, N, N), dtype=bool)
    interior[t:N - t, t:N - t, t:N - t] = True
    v_peak, n_min = [], []
    for step in range(N_STEPS_TOTAL):
        eng.step()
        if step >= N_STEPS_TRANSIENT:
            v_peak.append(float(np.abs(eng.V[interior]).max()))
            n_min.append(float(eng.refractive_index()[interior].min()))
    v_peak = np.array(v_peak)
    return {
        "v_peak_mean_post": float(v_peak.mean()),
        "v_peak_std_over_mean_post": float(v_peak.std() / max(v_peak.mean(), 1e-9)),
        "n_em_min_over_window": float(np.array(n_min).min()),
        "max_abs_over_run": float(np.abs(eng.V).max()),
    }


def classify(sech, gauss):
    """Apply the frozen §8a bins. Returns (verdict, bins-dict)."""
    mean_post = sech["v_peak_mean_post"]
    som = sech["v_peak_std_over_mean_post"]
    n_em_min = sech["n_em_min_over_window"]
    max_abs = sech["max_abs_over_run"]
    gauss_late = gauss["v_peak_mean_post"]  # the matched-amplitude disperse level

    bins = {
        "I-1 mean V_peak > 0.2": mean_post > 0.2,
        "I-2 breathing std/mean > 0.05": som > 0.05,
        "I-3 not diverging std/mean < 0.5": som < 0.5,
        "I-4 saturation engaged n_EM < 0.97": n_em_min < 0.97,
        "I-5 above radiation floor (>1.5x gaussian late)": mean_post > 1.5 * gauss_late,
        "I-6 bounded max|V| < 10": max_abs < 10.0,
    }
    mode_i = all(bins.values())
    # Control: the Gaussian MUST disperse (mean V_peak shrinks toward floor).
    # We register disperse as: gaussian post-transient mean below the sech's, and
    # below half the seed amplitude (cage_stiffening_wall.py:76 late<0.5·seed).
    gauss_disperses = gauss_late < 0.5 * SEED_AMP
    verdict = "MODE_I_PERSIST" if mode_i else "MODE_III_DISPERSE"
    return verdict, bins, gauss_disperses, gauss_late


def main():
    out = {"prereg": "research/2026-06-23_engine-stage2-native-cage_prereg.md",
           "frozen_update": "V^{n+1} = 2V^n - V^{n-1} - dt^2*c0^2*L_native[V^n] (MINUS)"}

    # PRIMARY: native sech + native gaussian control, N=24.
    sech24 = run_native(24, profile="sech")
    gauss24 = run_native(24, profile="gaussian")
    verdict, bins, gauss_disperses, gauss_late = classify(sech24, gauss24)

    # N-robustness (I-7): verdict must agree at N=20, 32.
    nrobust = {}
    for Nn in (20, 32):
        s = run_native(Nn, profile="sech")
        g = run_native(Nn, profile="gaussian")
        v, b, gd, gl = classify(s, g)
        nrobust[str(Nn)] = {
            "verdict": v, "v_peak_mean_post": s["v_peak_mean_post"],
            "std_over_mean": s["v_peak_std_over_mean_post"],
            "gaussian_late": g["v_peak_mean_post"], "gaussian_disperses": gd,
            "max_abs": s["max_abs_over_run"], "dt": s["dt_info"]["dt"],
            "rho": s["dt_info"]["rho_measured"],
        }

    # C-1: Cartesian reference reproduces v14 Mode-I.
    cart = run_cartesian_reference(24)
    cart_mode_i = (cart["v_peak_mean_post"] > 0.2 and
                   0.05 < cart["v_peak_std_over_mean_post"] < 0.5 and
                   cart["n_em_min_over_window"] < 0.97)

    out["primary_N24"] = {
        "verdict": verdict,
        "bins": {k: bool(v) for k, v in bins.items()},
        "sech": {
            "v_peak_mean_post": sech24["v_peak_mean_post"],
            "v_peak_std_over_mean_post": sech24["v_peak_std_over_mean_post"],
            "n_em_min_over_window": sech24["n_em_min_over_window"],
            "max_abs_over_run": sech24["max_abs_over_run"],
            "gamma_bulk_min_over_run": sech24["gamma_bulk_min_over_run"],
            "dt": sech24["dt_info"]["dt"],
            "rho_measured": sech24["dt_info"]["rho_measured"],
            "dt_cartesian_sanity": sech24["dt_info"]["dt_cartesian_sanity"],
        },
        "gaussian_control": {
            "v_peak_mean_post": gauss24["v_peak_mean_post"],
            "disperses": bool(gauss_disperses),
        },
    }
    out["n_robustness"] = nrobust
    out["n_robust_agree"] = (verdict == nrobust["20"]["verdict"] == nrobust["32"]["verdict"])
    out["cartesian_reference_C1"] = {**cart, "reproduces_v14_mode_i": bool(cart_mode_i)}

    # Gamma deepening trend (§8b): does gamma_bulk_min deepen over the run?
    gh = sech24["gamma_min_hist"]
    out["gamma_deepening"] = {
        "gamma_t0": float(gh[0]),
        "gamma_min_over_run": float(gh.min()),
        "deepened_below_t0": bool(gh.min() < gh[0] - 0.005),
        "sign_safe_always_negative": bool((gh < 0).all()),
    }

    # apparatus validity: control must disperse, else VOID.
    out["apparatus_valid_control_disperses"] = bool(gauss_disperses)

    # ── Rule-10 integrator-time diagnostic: dt-resolution robustness + the
    # nonlinear-instability finding (the make-or-break verdict is dt-entangled). ──
    out["dt_robustness"] = dt_resolution_sweep()

    print(json.dumps(out, indent=2))
    return out


def dt_resolution_sweep():
    """Rule-10 finding: the frozen measured-ρ dt (≈0.66) is CFL-stable but
    temporally UNDER-RESOLVES the nonlinear self-focusing transient (only ~23
    steps to the Cartesian self-focus time t≈15). At finer dt the native sech
    SELF-FOCUSES initially (peak grows above seed, like Cartesian) but then goes
    SECULARLY UNSTABLE (energy pumped into the A_cap saturation ceiling) — NOT a
    clean dispersion and NOT a clean persistence. ISOLATION: the instability is
    triggered ONLY by self-focusing into the steep 1/S(A→1) kernel — the LINEAR
    (amp=0.02) and NON-focusing GAUSSIAN runs stay bounded at the same fine dt.
    So the explicit leapfrog treatment of the nonlinear stiffness D=1/S(V) is
    unstable in the deep-saturation regime; the make-or-break verdict is
    CONTAMINATED and INCONCLUSIVE pending an implicit/stabilized nonlinear step.
    This function records the empirical sweep that establishes that."""
    T_TOTAL, T_TRANS = 150.0, 50.0

    def run_to_time(profile, dt_abs, N=24, amp=0.85):
        cfg = NativeCageConfig(N=N)
        eng = NativeCageFDTD(cfg)
        if profile == "sech":
            eng.seed_sech(amplitude=amp, radius=SEED_RADIUS)
        elif profile == "gaussian":
            eng.seed_field(_gaussian_seed(N, amp=amp, sigma=SEED_RADIUS, dx=DX))
        eng.set_dt_from_seed(n_iter=200)
        eng.dt = dt_abs
        pk, ts, mx = [], [], 0.0
        while eng.time < T_TOTAL:
            eng.step()
            mx = max(mx, float(np.abs(eng.V).max()))
            pk.append(eng.interior_peak_abs_V())
            ts.append(eng.time)
        pk, ts = np.array(pk), np.array(ts)
        post = pk[ts >= T_TRANS]
        return {
            "dt": dt_abs, "nsteps": len(pk), "peak_max": float(pk.max()),
            "max_abs_run": mx, "mean_post": float(post.mean()),
            "som": float(post.std() / max(post.mean(), 1e-9)),
            "unstable": bool(mx > 10.0),
        }

    sweep = {}
    for dt_abs in (0.66, 0.165, 0.066, 0.0264):
        s = run_to_time("sech", dt_abs)
        g = run_to_time("gaussian", dt_abs)
        sweep[f"{dt_abs:.4f}"] = {
            "sech": s, "gaussian_mean_post": g["mean_post"],
            "gaussian_unstable": g["unstable"],
            "self_focuses_above_seed": bool(s["peak_max"] > SEED_AMP),
        }
    # Linear-amplitude control (isolates the nonlinearity as the instability source).
    sweep["linear_control_amp0.02_dt0.066"] = run_to_time("sech", 0.066, amp=0.02)
    return sweep


if __name__ == "__main__":
    main()
