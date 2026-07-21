#!/usr/bin/env python3
"""DEEP-RAIL k-SCALING ADJUDICATOR — rho_N(k.r_core), the gravitational-sector survival test.

THE decisive question (merged #770 §8.2 owed follow-on): how does the caged/uncaged
far-field compression rho_N scale with k.r_core? The lattice runs at k.r_core ~ O(1);
the physical regime is ~1e-25. Survival threshold rho_N <= kappa_max^2/kappa_env^2 = 3.82e-3.
  BIN-1 SCALING-SUPPRESSED : rho_N falls with a frozen positive power p, extrapolation < threshold
  BIN-2 SCALING-FLAT       : rho_N k-independent -> the 78x floor stands, kill confirmed
  BIN-3 MIXED/FORM-UNDET.  : data cannot discriminate -> state what range/precision/box would
  BIN-4 UNDETERMINED       : unforced verdict-controlling choice -> stop

Prereg (FROZEN, criteria committed + pushed ALONE first):
    research/2026-07-20_deep-rail-kscaling_prereg-FROZEN.md
Discharges: research/2026-07-20_constituent-cage-ensemble_result.md §8.2 (#770);
            research/2026-07-20_envelope-boundary-walk_RECORD.md §6-3 (the Lloyd claim).

═══════════════════════════════════════════════════════════════════════════════
SUBSTRATE-FIRST SECTOR HEADER (fired before any standard-physics term)
═══════════════════════════════════════════════════════════════════════════════
  SECTOR : TRANSLATIONAL (Cauchy-grade) vector sector of the chiral srs-z3 net
           (ave.core.chiral_lattice._SRS_8A/_SRS_NN; rank-2 Phi_b = k_a d^d + k_s(I-d^d)).
           Rule-14 reuse of the #770 constituent_cage_ensemble machinery. NOT a Cartesian Laplacian.
  REGIME : DEEP-RAIL caged sources (S_RAIL <= 1e-4 -> Gamma_bulk <= -0.95, the canon bulk-only
           wall, electron-bh-isomorphism.md:26). Cages = CONSTITUTIVE GRADE (no kinematic pin).
  COORDS : A46 RADIATIVE-vs-STATIC split. The Lloyd claim (walk §6-3) suppresses the RADIATIVE
           moment ONLY; the static texture (mass) is EXPLICITLY untouched. So the verdict
           coordinate is the RADIATIVE F_bulk at the drive frequency Omega (Leg K, driven +
           lock-in). k.r_core = Omega*r_cage/c_P,cold. The static-release rho_N (leg5 reuse) is
           the fenced TEXTURE CONTROL, k.r_core = r_cage/sigma.
  CLASS  : lattice-derived EMPIRICAL legs (K/W/C1/S) + analytic Lloyd FORM (Leg A, deriv doc).
           Every VALUE dimensionless; alpha-CLEAN.

★ANTI-SEDUCTION (BOTH ways; the #770 lesson NAMED): #761/#767/#770 landed kill-direction with
 review-caught defects (#770 FABRICATED a 'ROBUST ... pressure-tested' string into the JSON while
 no scan ran). Kill-momentum AND suppression-seduction are both live. EVERY scan ships its data +
 code path here; NO prose-string conclusions; the verdict cites ONLY frozen-criteria JSON outputs.

ENGINE BYTE-UNTOUCHED: reuses research/drivers/constituent_cage_ensemble.py primitives, which
 import ave.core.* read-only. This driver adds only the DRIVEN lock-in primitive + the fit.

Run: PYTHONPATH=src:src/scripts/vol_1_foundations python3 research/drivers/deep_rail_kscaling.py
"""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path

import numpy as np

# ── Rule-14 reuse of the #770 machinery (engine byte-untouched; ave.core.* read-only) ──
_CCE_PATH = Path(__file__).with_name("constituent_cage_ensemble.py")
_spec = importlib.util.spec_from_file_location("cce", _CCE_PATH)
cce = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(cce)

RHO_STAR = cce.RHO_STAR        # 9.77337, DERIVED from nu_Hill=2/7 (imported, not fit)
K_S = cce.K_S                  # 1.0

# frozen kill-line numbers (§1 of the prereg)
KAPPA_MAX2 = 1.3e-4            # double-pulsar delta_DP (Kramer 2021) [import]
KAPPA_ENV2 = 0.034            # uncaged coarse-grained baseline (#767) [canon]
RHO_N_THRESHOLD = KAPPA_MAX2 / KAPPA_ENV2   # = 3.82e-3, survival threshold [derived]


# ═════════════════════════════════════════════════════════════════════════════
# ★LEG K PRIMITIVE — DRIVEN radiative lock-in (isolates the RADIATIVE moment at Omega)
# ═════════════════════════════════════════════════════════════════════════════
def driven_lockin(L, wall_class, N, Omega, r_cage, s_rail, cP,
                  sigma_s=0.7, cage_w=1.0, R_lobe=3.5, pack=1.0, r_meas=None,
                  shell_w=1.0, F0=0.02, cfl=0.2, sponge_w=6.0, gamma0=4.0,
                  n_settle_cross=5.0, n_lockin_per=8.0, rho_star=RHO_STAR, k_s=K_S):
    """Drive each caged core's interior with a HARMONIC RADIAL BODY FORCE (a compression
    source at frequency Omega; NO kinematic pin — free dynamics everywhere on the source).
    An outer graded-damping SPONGE ring (thickness sponge_w) is the outgoing-radiation
    port (the Ax3 far-field loss channel), so the drive reaches steady state. Lock-in the
    r_meas shell (INSIDE the sponge — PML-excluded) radial displacement onto sin/cos(Omega t)
    -> the RADIATIVE compression moment F_bulk (and tangential -> F_shear).
    Returns F_bulk, F_shear, energy drift over the lock-in window, drive transverse fraction.
    Deterministic (no per-step RNG)."""
    pos, bi, bj, dhat, mid = cce.build_finite_srs(L)
    Npt = pos.shape[0]
    half = L / 2.0
    if r_meas is None:
        r_meas = half - sponge_w - 1.5
    centers = cce._ensemble_centers(N, L, R_lobe, pack)
    c0 = np.array([half] * 3)
    Phi_cold = cce.bond_tensors(dhat, rho_star, k_s)
    omega_max = cce.omega_max_cold(Phi_cold, bi, bj, Npt)
    dt = cfl * 2.0 / omega_max
    ka, ks = cce.cage_stiffness(dhat, mid, rho_star, k_s, centers, r_cage, cage_w,
                                wall_class, s_rail=s_rail)
    Phi = cce.bond_tensors(dhat, ka, ks)

    # harmonic radial breathing body-force profile per core (curl-free compression drive)
    fdir = np.zeros((Npt, 3))
    for c in centers:
        rel = pos - np.asarray(c, float)
        rr = np.linalg.norm(rel, axis=1)
        rhat_c = rel / (rr[:, None] + 1e-30)
        fdir += (F0 * np.exp(-(rr ** 2) / (2.0 * sigma_s ** 2)))[:, None] * rhat_c

    # measurement shell about the ensemble centroid c0 (radial/tangential split)
    rel0 = pos - c0
    r0 = np.linalg.norm(rel0, axis=1)
    rhat0 = rel0 / (r0[:, None] + 1e-30)
    shell = (r0 >= r_meas) & (r0 < r_meas + shell_w)
    ns = int(shell.sum())

    # drive transverse fraction (radial drive -> ~0; reported per the frozen deliverable)
    src = r0 < (r_meas)  # interior region where the drive lives
    f_par = np.sum(fdir[src] * rhat0[src], axis=1)
    f_perp = fdir[src] - f_par[:, None] * rhat0[src]
    drive_perp_frac = float(np.sum(f_perp ** 2) / (np.sum(fdir[src] ** 2) + 1e-30))

    # sponge damping gamma(r): 0 inside, quadratic ramp in the outer cube-shell ring
    xabs = np.max(np.abs(pos - c0), axis=1)
    edge = half - sponge_w
    gamma = np.where(xabs > edge, gamma0 * ((xabs - edge) / sponge_w) ** 2, 0.0)

    u = np.zeros((Npt, 3))
    v = np.zeros((Npt, 3))
    T = 2.0 * np.pi / Omega
    cross = 2.0 * half / cP
    t_settle = n_settle_cross * cross
    t_end = t_settle + n_lockin_per * T
    n_steps = int(np.ceil(t_end / dt)) + 2

    def drive(t):
        ramp = 0.5 * (1.0 - np.cos(np.pi * min(t / (0.5 * t_settle), 1.0)))
        return ramp * np.sin(Omega * t)

    F = cce.forces(u, Phi, bi, bj, Npt) + fdir * drive(0.0)
    As_r = np.zeros(ns); Ac_r = np.zeros(ns)
    As_t = np.zeros((ns, 3)); Ac_t = np.zeros((ns, 3))
    nwin = 0
    H_win = []
    for step in range(n_steps):
        t = step * dt
        if t >= t_settle:
            us = u[shell]
            u_par = np.sum(us * rhat0[shell], axis=1)
            u_perp = us - u_par[:, None] * rhat0[shell]
            s = np.sin(Omega * t); cth = np.cos(Omega * t)
            As_r += u_par * s; Ac_r += u_par * cth
            As_t += u_perp * s; Ac_t += u_perp * cth
            nwin += 1
            if step % 20 == 0:
                H_win.append(cce.hamiltonian(u, v, Phi, bi, bj, Npt))
        u = u + v * dt + 0.5 * F * dt ** 2
        F_new = cce.forces(u, Phi, bi, bj, Npt) + fdir * drive(t + dt)
        # semi-implicit linear damping -gamma*v (sponge = radiation port)
        v = (v + 0.5 * (F + F_new) * dt) / (1.0 + gamma[:, None] * dt)
        F = F_new
    nwin = max(nwin, 1)
    F_bulk = float(np.sum((As_r / nwin) ** 2 + (Ac_r / nwin) ** 2))
    F_shear = float(np.sum((As_t / nwin) ** 2 + (Ac_t / nwin) ** 2))
    H_win = np.array(H_win)
    drift = float((H_win.max() - H_win.min()) / (abs(H_win.mean()) + 1e-30)) if len(H_win) > 1 else 9.9
    return {"F_bulk": F_bulk, "F_shear": F_shear, "k_rcore": Omega * r_cage / cP,
            "Omega": Omega, "r_cage": r_cage, "energy_drift_win": drift,
            "drive_transverse_frac": drive_perp_frac, "n_shell": ns, "r_meas": float(r_meas),
            "dt": float(dt), "n_lockin": nwin}


def _rhoN_driven(L, N, Omega, r_cage, s_rail, cP, **kw):
    cg = driven_lockin(L, "bulk_only", N, Omega, r_cage, s_rail, cP, **kw)
    un = driven_lockin(L, "none", N, Omega, r_cage, s_rail, cP, **kw)
    rho = cg["F_bulk"] / (un["F_bulk"] + 1e-30)
    sig = cg["F_shear"] / (un["F_shear"] + 1e-30)   # shear ratio sigma_N (consistency gate)
    return {"k_rcore": cg["k_rcore"], "Omega": Omega, "r_cage": r_cage, "s_rail": s_rail,
            "rho_N": rho, "sigma_N": sig, "F_bulk_caged": cg["F_bulk"],
            "F_bulk_uncaged": un["F_bulk"], "energy_drift_win": max(cg["energy_drift_win"],
            un["energy_drift_win"]), "drive_transverse_frac": cg["drive_transverse_frac"],
            "r_meas": cg["r_meas"]}


# ═════════════════════════════════════════════════════════════════════════════
# FROZEN MODEL COMPARISON (§3): F0 const / F2 Lloyd (k.r)^2 / Fp free-p / Fap plateau+power
# ═════════════════════════════════════════════════════════════════════════════
def fit_forms(krc, rho):
    """Fit the 4 frozen candidate forms over ADMISSIBLE points; compare by corrected AIC.
    All RSS computed in log(rho) space (Fap fit in linear rho, residual mapped to log for
    comparability — frozen §3). Returns per-form fit + the min-AICc winner + deltas + the
    F2/Fp extrapolation to k.r_core=1e-25 vs the survival threshold."""
    krc = np.asarray(krc, float); rho = np.asarray(rho, float)
    ok = (krc > 0) & (rho > 0)
    krc, rho = krc[ok], rho[ok]
    n = len(krc)
    lx, ly = np.log(krc), np.log(rho)

    def aicc(rss, kparams):
        kk = kparams + 1  # + variance
        if n - kk - 1 <= 0 or rss <= 0:
            return float("inf")
        return n * np.log(rss / n) + 2 * kk + 2 * kk * (kk + 1) / (n - kk - 1)

    forms = {}
    if n >= 3:
        # F0 constant: ly ~ c
        c0 = float(np.mean(ly))
        rss0 = float(np.sum((ly - c0) ** 2))
        forms["F0_const"] = {"a": float(np.exp(c0)), "RSS_log": rss0, "AICc": aicc(rss0, 1)}
        # F2 Lloyd: ly ~ log(a) + 2 lx
        la2 = float(np.mean(ly - 2.0 * lx))
        rss2 = float(np.sum((ly - (la2 + 2.0 * lx)) ** 2))
        forms["F2_lloyd_kr2"] = {"a": float(np.exp(la2)), "p_fixed": 2.0, "RSS_log": rss2,
                                 "AICc": aicc(rss2, 1)}
        # Fp free power: ly ~ log(a) + p lx  (linear regression)
        A = np.vstack([np.ones(n), lx]).T
        coef, *_ = np.linalg.lstsq(A, ly, rcond=None)
        resid = ly - A @ coef
        rssp = float(np.sum(resid ** 2))
        # 1-sigma on slope p
        dof = max(n - 2, 1)
        s2 = rssp / dof
        cov = s2 * np.linalg.inv(A.T @ A)
        p_se = float(np.sqrt(cov[1, 1]))
        forms["Fp_free_power"] = {"a": float(np.exp(coef[0])), "p": float(coef[1]),
                                  "p_1sigma": p_se, "RSS_log": rssp, "AICc": aicc(rssp, 2)}
    # Fap plateau+power (fit in linear rho; residual -> log)
    if n >= 5:
        try:
            from scipy.optimize import curve_fit

            def model(x, a, b, p):
                return a + b * np.power(x, p)
            p0 = [float(np.min(rho)), float(np.max(rho) - np.min(rho)), 2.0]
            popt, _ = curve_fit(model, krc, rho, p0=p0, maxfev=20000,
                                bounds=([0, -np.inf, 0.1], [np.inf, np.inf, 6.0]))
            pred = np.clip(model(krc, *popt), 1e-12, None)
            rssap = float(np.sum((ly - np.log(pred)) ** 2))
            forms["Fap_plateau_power"] = {"a": float(popt[0]), "b": float(popt[1]),
                                          "p": float(popt[2]), "RSS_log": rssap,
                                          "AICc": aicc(rssap, 3)}
        except Exception as e:  # noqa: BLE001
            forms["Fap_plateau_power"] = {"note": f"fit failed: {e}", "AICc": float("inf")}
    else:
        forms["Fap_plateau_power"] = {"note": f"n={n} < 5 (AICc needs n>=k+2); unfittable",
                                      "AICc": float("inf")}

    finite = {k: v["AICc"] for k, v in forms.items() if np.isfinite(v.get("AICc", np.inf))}
    winner = min(finite, key=finite.get) if finite else None
    best = finite.get(winner, None) if winner else None
    deltas = {k: (a - best) for k, a in finite.items()} if best is not None else {}

    # extrapolation of the power forms to the physical k.r_core = 1e-25
    krc_phys = 1e-25
    extrap = {}
    if "F2_lloyd_kr2" in forms and "a" in forms["F2_lloyd_kr2"]:
        extrap["F2_at_1e-25"] = forms["F2_lloyd_kr2"]["a"] * krc_phys ** 2
    if "Fp_free_power" in forms and "p" in forms["Fp_free_power"]:
        extrap["Fp_at_1e-25"] = forms["Fp_free_power"]["a"] * krc_phys ** forms["Fp_free_power"]["p"]
    return {"n_admissible": n, "forms": forms, "min_AICc_form": winner,
            "delta_AICc": deltas, "extrapolation_to_physical_krc": extrap,
            "survival_threshold_rho_N": RHO_N_THRESHOLD}


# ═════════════════════════════════════════════════════════════════════════════
# LEG W — WALL-DEPTH ladder (run_c2_speeds reuse; both classes; #770 review-repair under freeze)
# ═════════════════════════════════════════════════════════════════════════════
def legW_rail_ladder(cP_cold, cS_cold, ladder=(0.03, 0.003, 1e-4, 1e-6, 0.0)):
    def gamma(cr, cc):
        return (cr - cc) / (cr + cc)
    out = {"ladder": list(ladder), "cold": {"cP": cP_cold, "cS": cS_cold},
           "bulk_only": {}, "symmetric": {}}
    for s in ladder:
        key = f"{s:g}"
        cPb, cSb, _ = cce.run_c2_speeds(s * RHO_STAR, K_S)          # rail k_a only
        out["bulk_only"][key] = {"cP": cPb, "cS": cSb, "gamma_bulk": gamma(cPb, cP_cold),
                                 "gamma_shear": gamma(cSb, cS_cold),
                                 "shear_transmission_1plusGamma": 1.0 + gamma(cSb, cS_cold),
                                 "cP_over_cS": cPb / (cSb + 1e-30)}
        if s == 0.0:
            out["symmetric"][key] = {"cP": 0.0, "cS": 0.0, "gamma_bulk": -1.0,
                                     "gamma_shear": -1.0, "cP_over_cS": None,
                                     "note": "degenerate melt point cP=cS=0; analytic Gamma=-1 both"}
        else:
            cPs, cSs, _ = cce.run_c2_speeds(s * RHO_STAR, s * K_S)  # rail both
            out["symmetric"][key] = {"cP": cPs, "cS": cSs, "gamma_bulk": gamma(cPs, cP_cold),
                                     "gamma_shear": gamma(cSs, cS_cold),
                                     "cP_over_cS": cPs / (cSs + 1e-30)}
    b0 = out["bulk_only"]["0"]
    out["canon_bulk_only_wall_realizable"] = bool(b0["gamma_bulk"] < -0.99 and b0["cS"] > 0.1)
    return out


# ═════════════════════════════════════════════════════════════════════════════
# LEG C1 — CONVERGED charged-line (deep rail; frozen window-half convergence criteria)
# ═════════════════════════════════════════════════════════════════════════════
def legC1_converged_charged_line(L, wall_class, s_rail, cP, cS, r_cage=3.0, cage_w=1.2,
                                 r_meas=6.0, shell_w=1.0, sigma=1.2, amp=0.06, cfl=0.2):
    """Reuses the #770 leg12 physics (single deep-rail cage, curl-free seed, free evolve) but
    splits the reflection-free window into HALVES and reports the window-half agreement — the
    frozen convergence criterion the #770 Leg-1 (0.65) failed (halves swung 0.33->1.60)."""
    pos, bi, bj, dhat, mid = cce.build_finite_srs(L)
    N = pos.shape[0]
    center = np.array([L / 2.0] * 3)
    Phi_cold = cce.bond_tensors(dhat, RHO_STAR, K_S)
    omega_max = cce.omega_max_cold(Phi_cold, bi, bj, N)
    dt = cfl * 2.0 / omega_max
    if wall_class == "none":
        ka, ks = cce.cage_stiffness(dhat, mid, RHO_STAR, K_S, [], r_cage, cage_w, "none")
    else:
        ka, ks = cce.cage_stiffness(dhat, mid, RHO_STAR, K_S, [center], r_cage, cage_w,
                                    wall_class, s_rail=s_rail)
    Phi = cce.bond_tensors(dhat, ka, ks)
    rel = pos - center
    r = np.linalg.norm(rel, axis=1)
    ext = (r >= r_meas) & (r < r_meas + shell_w)
    u = cce.texture_displacement(pos, center, amp, sigma)
    u[r > r_cage] = 0.0
    v = np.zeros((N, 3))
    t_P = r_meas / cP
    t_reflect = (2.0 * (L / 2.0) - r_meas) / cP
    t_mid = 0.5 * (t_P + t_reflect)
    n_steps = int(np.ceil(1.02 * t_reflect / dt)) + 3
    F = cce.forces(u, Phi, bi, bj, N)
    th1 = np.zeros(N); th2 = np.zeros(N); n1 = 0; n2 = 0
    for step in range(n_steps):
        t = step * dt
        if t_P <= t < t_mid:
            th1 += cce.node_dilatation(u, bi, bj, dhat, N); n1 += 1
        elif t_mid <= t < t_reflect:
            th2 += cce.node_dilatation(u, bi, bj, dhat, N); n2 += 1
        u = u + v * dt + 0.5 * F * dt ** 2
        F_new = cce.forces(u, Phi, bi, bj, N)
        v = v + 0.5 * (F + F_new) * dt
        F = F_new
    n1 = max(n1, 1); n2 = max(n2, 1)
    h1 = float(np.sqrt(np.mean((th1 / n1)[ext] ** 2)))
    h2 = float(np.sqrt(np.mean((th2 / n2)[ext] ** 2)))
    return {"wall_class": wall_class, "s_rail": s_rail, "r_meas": r_meas,
            "theta_dc_ext_rms_firsthalf": h1, "theta_dc_ext_rms_secondhalf": h2,
            "window_half_disagreement": abs(h1 - h2) / (0.5 * (h1 + h2) + 1e-30),
            "theta_dc_ext_rms_full": 0.5 * (h1 + h2)}


# ═════════════════════════════════════════════════════════════════════════════
# LEG S — SHEAR-GATE diagnosis (leg5 reuse; near-field / N-dependence BEFORE gating)
# ═════════════════════════════════════════════════════════════════════════════
def legS_shear_diagnosis(L, s_rail, cP, cS, Ns=(1, 2, 4, 8), r_meas_scan=(6.0, 7.5, 9.0)):
    """Diagnose sigma_N = F_shear^caged/F_shear^uncaged (the #770 0.60x/0.23x readings) BEFORE
    gating: N-dependence (fixed r_meas) + near-field contamination (vary r_meas). The Leg-W
    wall shear-transmission 1+Gamma_shear at deep rail is the intrinsic floor the gate must
    not mistake for a cage effect. Static-release leg5 reuse (deterministic)."""
    out = {"s_rail": s_rail, "N_dependence": {}, "r_meas_dependence": {}}
    for N in Ns:
        cg = cce.leg5_ensemble_scaling(L, "bulk_only", N, cP, cS, s_rail=s_rail)
        un = cce.leg5_ensemble_scaling(L, "none", N, cP, cS, s_rail=s_rail)
        out["N_dependence"][str(N)] = float(cg["shell_E_perp"] / (un["shell_E_perp"] + 1e-30))
    for rm in r_meas_scan:
        cg = cce.leg5_ensemble_scaling(L, "bulk_only", 4, cP, cS, s_rail=s_rail, r_meas=rm)
        un = cce.leg5_ensemble_scaling(L, "none", 4, cP, cS, s_rail=s_rail, r_meas=rm)
        out["r_meas_dependence"][f"{rm:g}"] = float(cg["shell_E_perp"] / (un["shell_E_perp"] + 1e-30))
    return out


# ═════════════════════════════════════════════════════════════════════════════
# STATIC TEXTURE CONTROL (leg5 reuse; the "untouched texture", FENCED from the Lloyd verdict)
# ═════════════════════════════════════════════════════════════════════════════
def static_texture_control(L, s_rail, cP, cS):
    """The static-release rho_N (leg5). Walk §6-3: the static texture (mass) is UNTOUCHED by
    the image — so its plateau is EXPECTED and does NOT test Lloyd. Two panels:
      (a) k.r_core = r_cage/sigma scan (Route sigma vs Route r_cage) — the two-route collapse
          check for the STATIC observable (feasibility showed it does NOT collapse -> the static
          observable is not a clean function of k.r_core);
      (b) aggregation rho_N(N) at deep rail (N=1,2,4,8) — the #770 plateau ~0.3."""
    def rhoN(N, r_cage, sigma, r_meas=7.5):
        cg = cce.leg5_ensemble_scaling(L, "bulk_only", N, cP, cS, r_cage=r_cage, sigma=sigma,
                                       s_rail=s_rail, r_meas=r_meas)
        un = cce.leg5_ensemble_scaling(L, "none", N, cP, cS, r_cage=r_cage, sigma=sigma,
                                       s_rail=s_rail, r_meas=r_meas)
        return float(cg["shell_E_par"] / (un["shell_E_par"] + 1e-30))
    route_sigma = {f"{r_cage/sig:.3f}": {"k_rcore": r_cage / sig, "sigma": sig, "r_cage": r_cage,
                                         "rho_N": rhoN(1, r_cage, sig)}
                   for r_cage, sig in [(2.0, 2.8), (2.0, 2.0), (2.0, 1.4), (2.0, 1.0), (2.0, 0.8)]}
    route_rcage = {f"{r_cage/1.0:.3f}": {"k_rcore": r_cage / 1.0, "sigma": 1.0, "r_cage": r_cage,
                                         "rho_N": rhoN(1, r_cage, 1.0)}
                   for r_cage in (1.2, 1.6, 2.0, 2.8, 4.0)}
    aggregation = {str(N): rhoN(N, 1.6, 1.0) for N in (1, 2, 4, 8)}
    return {"observable": "STATIC-release rho_N (leg5) — the UNTOUCHED texture control, FENCED "
                          "from the Lloyd radiative verdict (walk §6-3; prereg §0 A46)",
            "route_sigma_fixed_rcage2p0": route_sigma, "route_rcage_fixed_sigma1p0": route_rcage,
            "aggregation_rho_N_by_N_deeprail": aggregation}


# ═════════════════════════════════════════════════════════════════════════════
# LEG K — the driven radiative rho_N(k.r_core) scan (the centerpiece)
# ═════════════════════════════════════════════════════════════════════════════
def legK_driven_kscan(L, cP, s_rail, N=1, drift_gate=0.30):
    """Two independent routes to k.r_core, deep rail. Route Omega (vary Omega, r_cage=1.6);
    Route r (vary r_cage, Omega=0.65). Convergence probe at the reference point (settle 5 vs 7
    crossings). Admissible = energy-drift over the lock-in window <= drift_gate. Fit the frozen
    forms over admissible points from BOTH routes pooled; route-collapse check at matched k.r_core."""
    route_omega = []
    for Om in (0.30, 0.45, 0.65, 0.90, 1.30, 1.90):
        route_omega.append(_rhoN_driven(L, N, Om, 1.6, s_rail, cP))
    route_rcage = []
    for rc in (1.0, 1.6, 2.2, 3.0, 3.8):
        route_rcage.append(_rhoN_driven(L, N, 0.65, rc, s_rail, cP))
    for pt in route_omega + route_rcage:
        pt["admissible"] = bool(pt["energy_drift_win"] <= drift_gate)
    # convergence probe at reference (Omega=0.486, r_cage=1.6 -> k.r_core~1.5)
    conv = {}
    for nsc in (5.0, 7.0):
        p = _rhoN_driven(L, N, 0.486, 1.6, s_rail, cP, n_settle_cross=nsc,
                         n_lockin_per=(8.0 if nsc == 5.0 else 10.0))
        conv[f"settle{nsc:g}cross"] = {"rho_N": p["rho_N"], "drift": p["energy_drift_win"]}
    conv["settle_stability_delta_rho_N"] = abs(conv["settle5cross"]["rho_N"]
                                               - conv["settle7cross"]["rho_N"])
    # pooled admissible fit
    adm = [p for p in route_omega + route_rcage if p["admissible"]]
    krc = [p["k_rcore"] for p in adm]
    rho = [p["rho_N"] for p in adm]
    fit = fit_forms(krc, rho) if len(krc) >= 3 else {"n_admissible": len(krc),
                                                     "note": "n<3; unfittable -> FORM-UNDETERMINED"}
    # route-collapse check: interpolate each route to the other's k.r_core, compare within 30%
    collapse = _route_collapse_check(route_omega, route_rcage)
    return {"s_rail": s_rail, "N": N, "drift_gate": drift_gate,
            "route_omega": route_omega, "route_rcage": route_rcage,
            "convergence_probe": conv, "fit": fit, "route_collapse": collapse,
            "n_admissible": len(adm)}


def _route_collapse_check(ro, rr, tol=0.30):
    """Do the two routes agree within tol at matched k.r_core (admissible points only)?"""
    ao = [(p["k_rcore"], p["rho_N"]) for p in ro if p.get("admissible")]
    ar = [(p["k_rcore"], p["rho_N"]) for p in rr if p.get("admissible")]
    if len(ao) < 2 or len(ar) < 2:
        return {"decidable": False, "note": "fewer than 2 admissible points on a route"}
    ao.sort(); ar.sort()
    ko, vo = np.array([a[0] for a in ao]), np.array([a[1] for a in ao])
    kr, vr = np.array([a[0] for a in ar]), np.array([a[1] for a in ar])
    lo, hi = max(ko.min(), kr.min()), min(ko.max(), kr.max())
    if hi <= lo:
        return {"decidable": False, "note": "no overlapping admissible k.r_core range"}
    xs = np.linspace(lo, hi, 5)
    vo_i = np.interp(xs, ko, vo); vr_i = np.interp(xs, kr, vr)
    rel = np.abs(vo_i - vr_i) / (0.5 * (vo_i + vr_i) + 1e-30)
    return {"decidable": True, "overlap_krc": [float(lo), float(hi)],
            "max_rel_disagreement": float(rel.max()), "mean_rel_disagreement": float(rel.mean()),
            "collapses_within_tol": bool(rel.max() <= tol), "tol": tol}


# ═════════════════════════════════════════════════════════════════════════════
# FIGURE (white house style; ave.viz.style; honest axes/units; legend outside data)
# ═════════════════════════════════════════════════════════════════════════════
def make_figure(out, path_png):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from ave.viz import style
    style.apply()
    C = style.COLORS

    fig, (axL, axR) = plt.subplots(1, 2, figsize=(10.6, 4.3))

    # (L) rho_N vs k.r_core: driven radiative (both routes) + static texture control
    lk = out["legK_driven_kscan_s1e-4"]
    ro = [(p["k_rcore"], p["rho_N"], p["admissible"]) for p in lk["route_omega"]]
    rr = [(p["k_rcore"], p["rho_N"], p["admissible"]) for p in lk["route_rcage"]]
    for pts, mk, col, lab in ((ro, "o", C["ave"], "driven radiative, Route Ω"),
                              (rr, "s", C["comparison"], "driven radiative, Route r_cage")):
        adm = [(k, r) for k, r, a in pts if a]
        nad = [(k, r) for k, r, a in pts if not a]
        if adm:
            axL.plot([k for k, _ in adm], [r for _, r in adm], mk, color=col, ms=8, label=lab)
        if nad:
            axL.plot([k for k, _ in nad], [r for _, r in nad], mk, color=col, ms=8,
                     mfc="none", alpha=0.5)
    stat = out["static_texture_control_s1e-4"]["route_rcage_fixed_sigma1p0"]
    sk = [v["k_rcore"] for v in stat.values()]
    sr = [v["rho_N"] for v in stat.values()]
    axL.plot(sk, sr, "^:", color=C["muted"], ms=6, label="static texture (leg5; UNTOUCHED, fenced)")
    axL.axvline(np.pi, color=C["accent"], ls="--", lw=1)
    axL.annotate("first cage\ncavity resonance\nk·r_core=π", xy=(np.pi, 1.15),
                 xytext=(np.pi * 1.02, 1.28), fontsize=6.5, color=C["accent"])
    axL.axhline(RHO_N_THRESHOLD, color=C["data"], ls=":", lw=1.2)
    axL.annotate("survival threshold ρ_N=3.8e-3\n(kill line; %.0f× below the O(1) band)"
                 % (0.3 / RHO_N_THRESHOLD), xy=(1.0, RHO_N_THRESHOLD),
                 xytext=(0.9, 6e-3), fontsize=6.5, color=C["data"])
    axL.set_xscale("log"); axL.set_yscale("log")
    axL.set_xlabel("k·r_core  (drive wavenumber × core radius; dimensionless)")
    axL.set_ylabel("ρ_N = caged / uncaged far-field compression")
    axL.set_xlim(0.3, 9.0)
    axL.set_ylim(2e-3, 4.0)
    axL.legend(loc="lower left", fontsize=6.2, frameon=False)
    axL.annotate("open = drift-gate FAIL (inadmissible);\nresonance comb (not a power law, not flat)\n⇒ FORM-UNDETERMINED",
                 xy=(0.5, 0.5), xytext=(0.33, 0.018), fontsize=6.0, color=C["muted"])

    # (R) Leg W rail ladder: bulk-only Gamma_bulk -> -1 with c_S FINITE (canon wall realizable)
    lw = out["legW_rail_ladder"]
    depths = [s for s in lw["ladder"] if s > 0]
    gb = [lw["bulk_only"][f"{s:g}"]["gamma_bulk"] for s in depths]
    cs = [lw["bulk_only"][f"{s:g}"]["cS"] for s in depths]
    ax2 = axR.twinx()
    axR.plot(depths, gb, "o-", color=C["ave"], ms=7, label="bulk-only Γ_bulk → −1")
    ax2.plot(depths, cs, "s--", color=C["comparison"], ms=6, label="bulk-only c_S (FINITE)")
    axR.set_xscale("log")
    axR.invert_xaxis()
    axR.axhline(-1.0, color=C["muted"], ls=":", lw=1)
    axR.set_xlabel("S_RAIL  (rail depth; → 0 = canon wall)")
    axR.set_ylabel("Γ_bulk (bulk-only rail)")
    ax2.set_ylabel("c_S  (shear speed, lattice units)")
    axR.set_ylim(-1.05, -0.4)
    ax2.set_ylim(0.0, 0.35)
    axR.annotate("canon bulk-only wall REALIZABLE:\nΓ_bulk→−1 with shear alive (#770)",
                 xy=(1e-4, -0.956), xytext=(3e-3, -0.62), fontsize=6.5, color=C["data"])
    h1, l1 = axR.get_legend_handles_labels()
    h2, l2 = ax2.get_legend_handles_labels()
    axR.legend(h1 + h2, l1 + l2, loc="lower left", fontsize=6.5, frameon=False)

    fig.savefig(path_png, dpi=150, bbox_inches="tight")
    fig.savefig(str(Path(path_png).with_suffix(".pdf")), bbox_inches="tight")
    plt.close(fig)


def main():
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--L", type=int, default=24)
    ap.add_argument("--out", default=str(Path(__file__).with_name("deep_rail_kscaling_results.json")))
    args = ap.parse_args()

    cP, cS, cpcs = cce.run_c2_speeds(RHO_STAR, K_S)
    out = {
        "provenance": {
            "class": "deep-rail k-scaling adjudicator; rho_N(k.r_core), the gravitational-sector "
                     "survival measurement; discharges #770 §8.2. Cages = CONSTITUTIVE GRADE "
                     "(no kinematic pin); RADIATIVE moment isolated by driven lock-in (Leg K); "
                     "engine byte-untouched (reuses constituent_cage_ensemble.py primitives).",
            "prereg": "research/2026-07-20_deep-rail-kscaling_prereg-FROZEN.md (FROZEN, pushed ALONE)",
            "kappa_max2_double_pulsar": KAPPA_MAX2,
            "kappa_env2_uncaged_767": KAPPA_ENV2,
            "rho_N_survival_threshold": RHO_N_THRESHOLD,
            "first_cage_cavity_resonance_krc": float(np.pi),
        },
        "spectral_cold": {"cP": cP, "cS": cS, "cP_over_cS": cP / cS, "cP_over_cS_dir": cpcs},
    }
    # ── LEG W — wall-depth ladder (fast; both classes) ──
    out["legW_rail_ladder"] = legW_rail_ladder(cP, cS)
    # ── LEG S — shear-gate diagnosis (before gating) ──
    out["legS_shear_diagnosis_s1e-4"] = legS_shear_diagnosis(args.L, 1e-4, cP, cS)
    # ── LEG C1 — converged charged-line (deep rail; window-half convergence) ──
    out["legC1_converged_charged_line_s1e-4"] = {
        wc: legC1_converged_charged_line(args.L, wc, 1e-4, cP, cS)
        for wc in ("bulk_only", "symmetric", "none")}
    # ── STATIC texture control (leg5 reuse; fenced) ──
    out["static_texture_control_s1e-4"] = static_texture_control(args.L, 1e-4, cP, cS)
    # ── ★LEG K — the driven radiative rho_N(k.r_core) scan (centerpiece) ──
    out["legK_driven_kscan_s1e-4"] = legK_driven_kscan(args.L, cP, 1e-4, N=1)
    # deep cross-check at s_rail=1e-6 (Route Omega, 3 points)
    xchk = [_rhoN_driven(args.L, 1, Om, 1.6, 1e-6, cP) for Om in (0.45, 0.90, 1.30)]
    for pt in xchk:
        pt["admissible"] = bool(pt["energy_drift_win"] <= 0.30)
    out["legK_driven_kscan_s1e-6_xcheck"] = {"route_omega": xchk}

    Path(args.out).write_text(json.dumps(out, indent=2))
    make_figure(out, str(Path(args.out).with_name("deep_rail_kscaling.png")))

    # ── console summary (frozen-criteria outputs only) ──
    lk = out["legK_driven_kscan_s1e-4"]
    print("spectral cold cP/cS =", round(cP / cS, 4), " survival threshold rho_N =",
          "%.3e" % RHO_N_THRESHOLD)
    lw = out["legW_rail_ladder"]
    print("LEG W bulk-only Gamma_bulk ladder:",
          " ".join("s=%s->%+.4f" % (s, lw["bulk_only"][f"{s:g}"]["gamma_bulk"]) for s in lw["ladder"]),
          "| c_S(s=0)=%.4f FINITE | canon wall realizable: %s" % (
              lw["bulk_only"]["0"]["cS"], lw["canon_bulk_only_wall_realizable"]))
    print("LEG K (driven radiative rho_N, s=1e-4): n_admissible=%d (drift-gate<=0.30)" % lk["n_admissible"])
    for p in lk["route_omega"]:
        print("   Route-Om k.rc=%.3f rho_N=%.4f sigma_N=%.3f drift=%.2e %s" % (
            p["k_rcore"], p["rho_N"], p["sigma_N"], p["energy_drift_win"],
            "ADM" if p["admissible"] else "inadm"))
    for p in lk["route_rcage"]:
        print("   Route-rc k.rc=%.3f rho_N=%.4f sigma_N=%.3f drift=%.2e %s" % (
            p["k_rcore"], p["rho_N"], p["sigma_N"], p["energy_drift_win"],
            "ADM" if p["admissible"] else "inadm"))
    fit = lk["fit"]
    if "forms" in fit:
        print("LEG K fit: min-AICc form = %s | Fp p=%.2f±%.2f | deltas=%s" % (
            fit["min_AICc_form"], fit["forms"].get("Fp_free_power", {}).get("p", float("nan")),
            fit["forms"].get("Fp_free_power", {}).get("p_1sigma", float("nan")),
            {k: round(v, 2) for k, v in fit["delta_AICc"].items()}))
        print("LEG K extrapolation to k.rc=1e-25:", fit["extrapolation_to_physical_krc"],
              " (survival needs < %.2e)" % RHO_N_THRESHOLD)
    rc = lk["route_collapse"]
    print("LEG K route-collapse:", rc)
    cp = lk["convergence_probe"]
    print("LEG K convergence probe: settle-stability delta_rho_N=%.4f (settle5 drift=%.2e settle7 drift=%.2e)" % (
        cp["settle_stability_delta_rho_N"], cp["settle5cross"]["drift"], cp["settle7cross"]["drift"]))
    c1 = out["legC1_converged_charged_line_s1e-4"]["bulk_only"]
    print("LEG C1 charged-line (bulk_only, s=1e-4): window-half disagreement=%.3f (converged if<=0.25)" %
          c1["window_half_disagreement"])
    ls = out["legS_shear_diagnosis_s1e-4"]
    print("LEG S sigma_N by N:", ls["N_dependence"], "| by r_meas:", ls["r_meas_dependence"])
    return out


if __name__ == "__main__":
    main()
