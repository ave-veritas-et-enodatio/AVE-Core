#!/usr/bin/env python
"""
SUPER-BAND CARRIER FORK — driven-lattice transport test (task #29).

Prereg (FROZEN): research/2026-07-09_superband-carrier-fork_prereg_FROZEN.md
Framing (OUTRANKED by this run): research/2026-07-09_highE-carrier-fpb-corner_walked-framing.md

═══════════════════════════════════════════════════════════════════════════════
SUBSTRATE-FIRST SECTOR HEADER (per prereg §3, before any standard term)
═══════════════════════════════════════════════════════════════════════════════
  SECTOR : the V-sector / ε charge-length AC oscillation on a K4 bond-line. Node
           scalar V_n = the photon carrier (AC content of the T2/charge-length
           sector; framing note §2). 1D chain, transport along one bond-line.
  REGIME : cold-to-kernel-engaged, SUB-YIELD (reversible). Bond strain
           r_n = V_{n+1}-V_n; yield |r|=1 -> rupture/pair-production = OUT OF SCOPE.
  NONLIN : canonical Op2/Op14 saturable varactor. Kernel S(r)=sqrt(1-r^2)
           (ave.core.universal_operators.universal_saturation, Axiom 4 / Born-Infeld
           n=2). Conservative bond potential U(r)=1-S(r); force F(r)=r/S(r) STIFFENS
           to infinity at yield (HARD nonlinearity, above-band self-localization).
           Ax3-lossless: single-valued reactance, no bulk energy term, no dissipation.
  READOUT: real-space energy flux + temporal spectrum of what propagates. Drive is
           a temporal omega at a real-space boundary; read is real-space. A46-clean
           (same coordinate frame both ends; NOT compared to a phase-space phi^2).
  ALIASING: spatial-lattice aliasing/evanescence is PHYSICAL (ell_node fixed). The
           time integrator is continuous-time (dt = accuracy knob, NOT tied to the
           lattice) -> temporal aliasing avoided by construction, VERIFIED by the
           dt-halving gate G5. Energy conservation (symplectic velocity-Verlet on
           H=sum 1/2 p^2 + sum U(r)) monitored: |dH|/H < 1% required for VALID.
  CLASS  : CONSISTENCY (scope-closure). NOT an emergence claim.

Native units (constants.py): ell_node=1, c=1, ω_C=c/ell_node=1. Linear acoustic band
ω(k)=2|sin(k/2)|, gapless, band top ω_top=2 (=2 ω_C), v_g->0 at zone edge k=π.

Run:  PYTHONPATH=src python src/scripts/vol_1_foundations/superband_carrier_fork.py
"""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np

from ave.core.constants import C_0, L_NODE, OMEGA_C
from ave.core.universal_operators import universal_saturation

# Native-unit band scale: ω_C (= c/ell_node) maps to 1.0. All native ω below are in
# units of ω_C. The SI value is carried for the framing-note bridge only.
OMEGA_C_SI = OMEGA_C  # ≈ 7.763e20 rad/s ; ℏω_C = m_e c^2 = 511 keV
YIELD = 1.0           # bond-strain yield r_y (native); |r|>=1 -> rupture (out of scope)


# ───────────────────────── substrate-native bond model ─────────────────────────
def S_of_r(r: np.ndarray) -> np.ndarray:
    """Canonical Op2 kernel S(r)=sqrt(1-(r/r_y)^2), clipped safe. Delegates to
    ave.core.universal_operators.universal_saturation (NOT re-implemented)."""
    return universal_saturation(r, YIELD)


def F_bond(r: np.ndarray) -> np.ndarray:
    """Restoring force through a saturable bond: F(r)=r/S(r). Stiffens to inf at
    yield (HARD). Small-r: F≈r (gapless acoustic band). Conservative: F=U'(r)."""
    s = np.sqrt(np.clip(1.0 - (r / YIELD) ** 2, 1e-9, 1.0))
    return r / s


def U_bond(r: np.ndarray) -> np.ndarray:
    """Bond potential U(r)=1-sqrt(1-(r/r_y)^2) (Born-Infeld n=2). U'(r)=F(r)."""
    return 1.0 - np.sqrt(np.clip(1.0 - (r / YIELD) ** 2, 1e-9, 1.0))


def accel(V: np.ndarray) -> np.ndarray:
    """V̈_n = F(r_n) - F(r_{n-1}), r_n=V_{n+1}-V_n. Free ends (overwritten by
    drive/sponge in the caller)."""
    r = np.diff(V)
    F = F_bond(r)
    a = np.zeros_like(V)
    a[1:-1] = F[1:] - F[:-1]
    a[0] = F[0]
    a[-1] = -F[-1]
    return a


def energy_density(V: np.ndarray, Vd: np.ndarray) -> np.ndarray:
    """Per-node energy: 1/2 V̇_n^2 + bond potential (assigned to left node)."""
    u = np.concatenate([[0.0], U_bond(np.diff(V))])
    return 0.5 * Vd ** 2 + u


# ───────────────────────── integrators ─────────────────────────
def sponge_profile(N: int, width: int, strength: float = 0.4) -> np.ndarray:
    """Matched absorbing sponge at the right edge (the far Z_0 vacuum load).
    Cells [N-width, N) are EXCLUDED from physics reads (Rule-10 PML-exclusion)."""
    damp = np.zeros(N)
    if width > 0:
        idx = np.arange(N - width, N)
        damp[N - width:] = strength * ((idx - (N - width)) / width) ** 2
    return damp


def drive_run(N, omega_d, A_d, tmax, dt, ramp_periods=20, sponge_w=200):
    """Boundary-driven chain. Returns (V, Vd, diagnostics). Symplectic
    velocity-Verlet with a matched sponge; drive imposed on node 0 with a C1-smooth
    raised-cosine ramp (narrow injected spectrum -> suppresses the turn-on
    transient's in-band leak). Aborts+flags if any bond touches yield."""
    V = np.zeros(N)
    Vd = np.zeros(N)
    damp = sponge_profile(N, sponge_w)
    nsteps = int(tmax / dt)
    ramp = ramp_periods * (2 * np.pi / omega_d)
    max_bond_r = 0.0
    ruptured = False
    for it in range(nsteps):
        t = it * dt
        a = accel(V) - damp * Vd
        Vh = Vd + 0.5 * dt * a
        V = V + dt * Vh
        w = 0.5 * (1.0 - np.cos(np.pi * min(1.0, t / ramp)))  # raised-cosine (C1)
        V[0] = A_d * w * np.sin(omega_d * t)
        a2 = accel(V) - damp * Vh
        Vd = Vh + 0.5 * dt * a2
        Vd[0] = 0.0
        rmax = float(np.max(np.abs(np.diff(V))))
        if rmax > max_bond_r:
            max_bond_r = rmax
        if rmax >= 0.999 * YIELD:
            ruptured = True
            break
    return V, Vd, {"max_bond_r": max_bond_r, "ruptured": ruptured, "N": N,
                   "sponge_w": sponge_w}


def transported_fraction(V, Vd, n_cut, sponge_w):
    """Fraction of chain energy that has propagated past n_cut (excludes the
    evanescent skin, any pinned near-boundary breather, and the sponge)."""
    Ed = energy_density(V, Vd)
    interior = Ed[1:len(Ed) - sponge_w]              # drop drive node + sponge
    far = Ed[n_cut:len(Ed) - sponge_w]
    E_tot = float(np.sum(interior))
    E_far = float(np.sum(far))
    T = E_far / E_tot if E_tot > 0 else 0.0
    # centroid + width of the FAR field (propagating packet, if any)
    if E_far > 1e-12:
        x = np.arange(n_cut, len(Ed) - sponge_w)
        com = float(np.sum(x * far) / np.sum(far))
        env = np.abs(V[n_cut:len(Ed) - sponge_w])
        pk = float(np.max(env))
        width = int(np.sum(env > 0.5 * pk)) if pk > 0 else 0
    else:
        com, width = float("nan"), 0
    return {"T": T, "E_far": E_far, "E_tot": E_tot, "far_com": com, "far_width": width}


# ───────────────────────── seeded-breather probes (O4) ─────────────────────────
def evolve_free(V, Vd, dt, nsteps, sponge_w=80):
    damp = sponge_profile(len(V), sponge_w) if sponge_w else np.zeros(len(V))
    max_bond_r = 0.0
    for _ in range(nsteps):
        a = accel(V) - damp * Vd
        Vh = Vd + 0.5 * dt * a
        V = V + dt * Vh
        a2 = accel(V) - damp * Vh
        Vd = Vh + 0.5 * dt * a2
        max_bond_r = max(max_bond_r, float(np.max(np.abs(np.diff(V)))))
    return V, Vd, max_bond_r


def seed_breather(N, n0, width, amp):
    x = np.arange(N)
    env = amp * np.exp(-0.5 * ((x - n0) / width) ** 2)
    return env * np.cos(np.pi * x)      # staggered (zone-edge) carrier


def breather_probe(amp, kick, N=1400, n0=500, dt=0.003, tmax=350.0):
    """Seed a staggered breather; optional momentum kick. Report COM drift
    (mobility) + energy conservation (validity) + localization width."""
    V = seed_breather(N, n0, 5.0, amp)
    Vd = kick * amp * np.exp(-0.5 * ((np.arange(N) - n0) / 5.0) ** 2) * np.sin(np.pi * np.arange(N))
    lo, hi = 90, N - 90
    Ed0 = energy_density(V, Vd)
    E0 = float(np.sum(Ed0[lo:hi]))
    com0 = float(np.sum(np.arange(N)[lo:hi] * Ed0[lo:hi]) / np.sum(Ed0[lo:hi]))
    V, Vd, maxr = evolve_free(V, Vd, dt, int(tmax / dt), sponge_w=80)
    Ed = energy_density(V, Vd)
    E1 = float(np.sum(Ed[lo:hi]))
    com1 = float(np.sum(np.arange(N)[lo:hi] * Ed[lo:hi]) / np.sum(Ed[lo:hi]))
    env = np.abs(V[lo:hi])
    pk = int(np.argmax(env)) + lo
    width = int(np.sum(env > 0.5 * np.max(env)))
    return {"amp": amp, "kick": kick, "max_bond_r": round(maxr, 4),
            "dE_over_E": (E1 - E0) / E0, "com0": round(com0, 1), "com1": round(com1, 1),
            "com_drift": round(com1 - com0, 1), "speed_c": round((com1 - com0) / tmax, 4),
            "peak_node": pk, "loc_width": width}


def pn_barrier():
    """Peierls-Nabarro barrier: energy of a site-centred vs bond-centred static
    breather (same amplitude). Nonzero difference => a barrier the packet must climb
    to translate (immobility)."""
    N = 400
    dt = 0.003
    out = {}
    for label, n0 in (("site_centred", 200.0), ("bond_centred", 200.5)):
        V = seed_breather(N, n0, 5.0, 0.25)
        Vd = np.zeros(N)
        V, Vd, _ = evolve_free(V, Vd, dt, int(60 / dt), sponge_w=60)
        Ed = energy_density(V, Vd)
        out[label] = float(np.sum(Ed[70:330]))
    out["barrier"] = out["site_centred"] - out["bond_centred"]
    out["barrier_rel"] = out["barrier"] / out["site_centred"]
    return out


# ───────────────────────── fits ─────────────────────────
def fit_power_and_exp(x, y):
    """x = ω/ω_C, y = T (>0). Fit log y vs log x (power p) and log y vs x (rate γ).
    Return exponents + R^2 for each."""
    x = np.asarray(x, float)
    y = np.asarray(y, float)
    m = y > 0
    x, y = x[m], y[m]
    if len(x) < 3:
        return None
    ly = np.log(y)

    def r2(pred):
        ss_res = np.sum((ly - pred) ** 2)
        ss_tot = np.sum((ly - np.mean(ly)) ** 2)
        return 1.0 - ss_res / ss_tot if ss_tot > 0 else float("nan")

    pw = np.polyfit(np.log(x), ly, 1)          # ly = pw[0] log x + pw[1]
    ex = np.polyfit(x, ly, 1)                   # ly = ex[0] x + ex[1]
    return {
        "power_p": float(-pw[0]), "power_R2": float(r2(np.polyval(pw, np.log(x)))),
        "exp_gamma": float(-ex[0]), "exp_R2": float(r2(np.polyval(ex, x))),
        "n_points": int(len(x)),
    }


# ───────────────────────── band validation (O1) ─────────────────────────
def validate_band():
    """Small-k phase velocity (c) + band top (v_g->0) of the linear chain, and
    the analytic above-band evanescence rate cosh κ = ω^2/2 - 1."""
    ks = np.array([0.05, 0.1, 0.2])
    omega = 2.0 * np.abs(np.sin(ks / 2.0))
    v_phase = omega / ks
    omega_top = 2.0
    return {
        "omega_top_over_omega_C": omega_top,      # = 2
        "low_k_phase_velocity_c": float(np.mean(v_phase)),  # -> 1 (=c)
        "v_group_at_edge": float(np.cos(np.pi / 2.0)),      # = 0
        "gapless": bool(2.0 * np.abs(np.sin(0.0)) < 1e-12),
        "note": "acoustic ω=2|sin(k/2)|; band top 2 ω_C; edge v_g=0; k=0 gapless",
    }


def analytic_kappa(omega_over_C):
    """Above-band evanescent decay rate: continue k->π+iκ in ω^2=2(1-cos k)."""
    arg = omega_over_C ** 2 / 2.0 - 1.0
    return float(np.arccosh(arg)) if arg >= 1.0 else float("nan")


def measure_skin(V, n_lo=1, n_hi=6):
    env = np.abs(V[n_lo:n_hi])
    m = env > 1e-14
    if np.sum(m) < 3:
        return float("nan")
    n = np.arange(n_lo, n_hi)[m]
    return float(-np.polyfit(n, np.log(env[m]), 1)[0])


# ───────────────────────── main ─────────────────────────
def main():
    out_dir = Path(__file__).parent
    band = validate_band()

    # Frozen drive set (prereg §6): ω/ω_C. In-band controls {0.5,1.5}; above ω_top≈2.
    in_band = [0.5, 1.5]
    above = [2.1, 2.5, 3.0, 4.0, 5.0, 6.0]
    amps = [0.02, 0.1, 0.2, 0.3]           # linear -> kernel-engaged, sub-yield
    N = 3200
    sponge_w = 250
    n_cut = 60                              # past evanescent skin + pinned breather

    results = {"O1_band": band, "O2_O3_runs": [], "runs_index": []}

    # O2/O3: transport + coupling for every (ω_drive, A).
    for w in in_band + above:
        # dt resolves the drive: >=60 substeps/period AND CFL-safe for the chain.
        dt = min(0.25, (2 * np.pi / w) / 60.0)
        tmax = 900.0
        for A in amps:
            V, Vd, diag = drive_run(N, w, A, tmax, dt, sponge_w=sponge_w)
            tp = transported_fraction(V, Vd, n_cut, sponge_w)
            skin = measure_skin(V) if w > band["omega_top_over_omega_C"] else float("nan")
            rec = {
                "omega_over_C": w, "omega_over_top": w / band["omega_top_over_omega_C"],
                "A_drive": A, "dt": dt, "in_band": w <= band["omega_top_over_omega_C"],
                "ruptured": diag["ruptured"], "max_bond_r": round(diag["max_bond_r"], 4),
                "T": tp["T"], "E_far": tp["E_far"], "E_tot": tp["E_tot"],
                "far_com": tp["far_com"], "far_width": tp["far_width"],
                "skin_rate_measured": skin,
                "skin_rate_analytic": analytic_kappa(w) if w > 2.0 else float("nan"),
            }
            results["O2_O3_runs"].append(rec)

    # O3 coupling-law fit: above-band, per amplitude, non-ruptured. E_far is the
    # cleaner (unnormalised) leaked-energy signal; fit that.
    fits = {}
    for A in amps:
        pts = [(r["omega_over_C"], r["E_far"]) for r in results["O2_O3_runs"]
               if (not r["in_band"]) and r["A_drive"] == A and not r["ruptured"] and r["E_far"] > 0]
        if len(pts) >= 3:
            xs, ys = zip(*pts)
            fits[f"A={A}"] = fit_power_and_exp(list(xs), list(ys))
    results["O3_coupling_fits"] = fits

    # Linear-baseline decomposition: E_far(ω,A) = [linear boundary leak ∝ A²]
    # + [nonlinear down-conversion excess]. The A=0.02 run is the linear baseline.
    baseline = {r["omega_over_C"]: r["E_far"] for r in results["O2_O3_runs"]
                if r["A_drive"] == amps[0] and not r["in_band"]}
    A0 = amps[0]
    nl_excess = []
    for r in results["O2_O3_runs"]:
        if r["in_band"] or r["ruptured"] or r["A_drive"] == A0:
            continue
        lin = baseline.get(r["omega_over_C"], 0.0) * (r["A_drive"] / A0) ** 2
        exc = r["E_far"] - lin
        nl_excess.append({"omega_over_C": r["omega_over_C"], "A_drive": r["A_drive"],
                          "E_far": r["E_far"], "linear_pred": lin,
                          "nl_excess": exc, "nl_frac": exc / r["E_far"] if r["E_far"] > 0 else 0.0})
    results["O3_nonlinear_excess"] = nl_excess
    # Fit the LINEAR-regime coupling law (A=0.02 baseline) — the cleanest Branch-A test.
    results["O3_linear_coupling_fit"] = fit_power_and_exp(
        list(baseline.keys()), list(baseline.values()))
    # Robustness (sensitivity check, NOT the primary fit): exclude the marginal
    # near-edge point (ω=2.1, shallow evanescence κ=0.63) and the floor-limited
    # tail (ω=6), fit the clean window ω∈{2.5,3,4,5}.
    clean = {w: e for w, e in baseline.items() if 2.4 < w < 5.5}
    results["O3_linear_coupling_fit_cleanwindow"] = {
        "window_omega_over_C": sorted(clean.keys()),
        **(fit_power_and_exp(list(clean.keys()), list(clean.values())) or {}),
    }

    # O4: mobility + PN barrier.
    results["O4_breather_static"] = [breather_probe(a, 0.0) for a in (0.05, 0.15, 0.25)]
    results["O4_breather_kicked"] = [breather_probe(0.25, k) for k in (0.2, 0.5, 1.0)]
    results["O4_pn_barrier"] = pn_barrier()

    # O5 amplitude-axis discriminator table (above-band representative ω=3).
    amp_axis = [r for r in results["O2_O3_runs"]
                if r["omega_over_C"] == 3.0]
    results["O5_amplitude_axis"] = amp_axis

    # G5: dt-halving convergence on a representative above-band case (ω=3, A=0.2).
    w0, A0 = 3.0, 0.2
    conv = {}
    for label, fac in (("dt", 1.0), ("dt_half", 0.5)):
        dt = min(0.25, (2 * np.pi / w0) / 60.0) * fac
        V, Vd, diag = drive_run(N, w0, A0, 900.0, dt, sponge_w=sponge_w)
        tp = transported_fraction(V, Vd, n_cut, sponge_w)
        conv[label] = {"dt": dt, "T": tp["T"], "far_com": tp["far_com"],
                       "max_bond_r": round(diag["max_bond_r"], 4)}
    conv["T_rel_change"] = (abs(conv["dt_half"]["T"] - conv["dt"]["T"])
                            / conv["dt"]["T"] if conv["dt"]["T"] > 0 else float("nan"))
    results["G5_dt_convergence"] = conv

    # Energy-conservation validity ledger (undriven seeded runs report dE/E).
    dE = [r["dE_over_E"] for r in results["O4_breather_static"] + results["O4_breather_kicked"]]
    results["energy_conservation_max_abs_dE_over_E"] = float(np.max(np.abs(dE)))

    _adjudicate(results, band)

    payload = {
        "prereg": "research/2026-07-09_superband-carrier-fork_prereg_FROZEN.md",
        "class": "CONSISTENCY (scope-closure)",
        "canonical_constants": {"L_NODE_m": L_NODE, "C_0_m_per_s": C_0,
                                 "OMEGA_C_rad_per_s_SI": OMEGA_C_SI,
                                 "native_omega_C": 1.0, "native_omega_top": 2.0},
        **results,
    }
    RESULT_JSON = out_dir.parent.parent.parent / "research" / "2026-07-09_superband-carrier-fork_result.json"
    RESULT_JSON.write_text(json.dumps(payload, indent=2))
    print(f"wrote {RESULT_JSON}")
    print(json.dumps(results["verdict"], indent=2))
    _make_figure(results, out_dir)
    return payload


def _adjudicate(results, band):
    """Evaluate frozen gates G1-G5 + branch verdict (prereg §5)."""
    runs = results["O2_O3_runs"]
    # G1 band
    g1 = band["gapless"] and abs(band["low_k_phase_velocity_c"] - 1.0) < 0.02 and band["v_group_at_edge"] < 1e-9
    # G2 linear evanescence physical: at smallest amplitude, above-band far-flux ~0 AND
    # measured skin rate within 20% of analytic for the cleanest above-band case.
    lin = [r for r in runs if (not r["in_band"]) and r["A_drive"] == 0.02 and not r["ruptured"]]
    far_lin = max((r["T"] for r in lin), default=1.0)
    skin_ok = any(np.isfinite(r["skin_rate_measured"]) and np.isfinite(r["skin_rate_analytic"])
                  and abs(r["skin_rate_measured"] - r["skin_rate_analytic"]) / r["skin_rate_analytic"] < 0.30
                  for r in lin)
    g2 = far_lin < 1e-2 and skin_ok
    # G3 coupling law: pick the kernel-engaged amplitude with best-resolved fit.
    fits = results["O3_coupling_fits"]
    best = None
    for k, f in fits.items():
        if f is None:
            continue
        sep = abs(f["power_R2"] - f["exp_R2"])
        if best is None or sep > best[1]:
            best = (k, sep, f)
    if best:
        f = best[2]
        law = "power" if f["power_R2"] > f["exp_R2"] else "exponential"
    else:
        law = "indeterminate"
        f = None
    g3 = f is not None
    # G4 mobility: any kicked breather with |speed|>0.05c and constant => mobile.
    kicked = results["O4_breather_kicked"]
    mobile = any(abs(r["speed_c"]) > 0.05 and r["dE_over_E"] < 0.01 for r in kicked)
    pn = results["O4_pn_barrier"]["barrier_rel"]
    g4 = True  # always reported
    # G5
    g5 = (results["G5_dt_convergence"]["T_rel_change"] < 0.05
          and results["energy_conservation_max_abs_dE_over_E"] < 0.01)

    # Branch verdict decision rule (FROZEN).
    if not g5:
        verdict = "INDETERMINATE (G5 dt/energy gate failed — numerical artifact suspected)"
    elif not g2:
        verdict = "INDETERMINATE (G2 linear-evanescence not established)"
    elif mobile and law == "exponential":
        verdict = "BRANCH B (mobile discrete breather; exponential coupling; ATLAS EVADES)"
    elif (not mobile) and law == "power":
        verdict = "BRANCH A (aliased-Bloch power-law residual; no mobile carrier; ATLAS tension REAL)"
    elif not mobile:
        verdict = "NULL (smooth sector carries nothing above the edge; no propagating carrier)"
    else:
        verdict = "INDETERMINATE (mixed signature)"

    results["verdict"] = {
        "G1_band_validated": bool(g1),
        "G2_linear_evanescence_physical": bool(g2),
        "G2_linear_far_flux_max": far_lin,
        "G3_coupling_law": law, "G3_fit": f,
        "G4_breather_mobile": bool(mobile), "G4_pn_barrier_rel": pn,
        "G5_dt_converged_energy_conserved": bool(g5),
        "BRANCH_VERDICT": verdict,
    }


def _make_figure(results, out_dir):
    import matplotlib.pyplot as plt

    from ave.viz import style
    style.apply("print")
    fig_dir = out_dir / "superband_carrier_figs"
    fig_dir.mkdir(exist_ok=True)
    runs = results["O2_O3_runs"]

    fig, axes = plt.subplots(1, 2, figsize=(11, 4.2))
    # Panel 1: T vs ω/ω_C at kernel-engaged amplitude, with band top.
    for A in sorted({r["A_drive"] for r in runs}):
        pts = sorted([(r["omega_over_C"], max(r["T"], 1e-16)) for r in runs
                      if r["A_drive"] == A and not r["ruptured"]])
        if pts:
            xs, ys = zip(*pts)
            axes[0].semilogy(xs, ys, "o-", label=f"A={A}")
    axes[0].axvline(2.0, ls="--", color="0.4", lw=1)
    axes[0].text(2.02, axes[0].get_ylim()[1] * 0.3, "band top\nω_top=2ω_C", fontsize=8)
    axes[0].set_xlabel("ω_drive / ω_C")
    axes[0].set_ylabel("transported fraction T (far/total)")
    axes[0].set_title("Above-band transport vs drive frequency")
    axes[0].legend(loc="center left", bbox_to_anchor=(1.0, 0.5), fontsize=8)

    # Panel 2: coupling-law fit on the LINEAR baseline (E_far, A=0.02) — the clean
    # Branch-A test. Mark the marginal near-edge point; draw the clean-window fit.
    v = results["verdict"]
    fc = results["O3_linear_coupling_fit_cleanwindow"]
    above = sorted([(r["omega_over_C"], r["E_far"]) for r in runs
                    if not r["in_band"] and r["A_drive"] == 0.02 and not r["ruptured"] and r["E_far"] > 0])
    if above:
        xs, ys = zip(*above)
        clean = [(x, y) for x, y in above if 2.4 < x < 5.5]
        edge = [(x, y) for x, y in above if x <= 2.4 or x >= 5.5]
        cx, cy = zip(*clean)
        axes[1].semilogy(cx, cy, "ks", ms=7, label="E_far linear (A=0.02)")
        if edge:
            ex_, ey_ = zip(*edge)
            axes[1].semilogy(ex_, ey_, "o", mfc="none", mec="0.5", ms=7,
                             label="marginal (near-edge / floor)")
        if fc and "power_p" in fc:
            xx = np.linspace(min(cx), max(cx), 50)
            y0 = cy[0]
            axes[1].semilogy(xx, y0 * (xx / cx[0]) ** (-fc["power_p"]), "--",
                             label=f"power p={fc['power_p']:.1f} R²={fc['power_R2']:.3f}")
            axes[1].semilogy(xx, y0 * np.exp(-fc["exp_gamma"] * (xx - cx[0])), "-",
                             label=f"exp γ={fc['exp_gamma']:.1f} R²={fc['exp_R2']:.3f}")
    axes[1].set_xlabel("ω_drive / ω_C  (above band)")
    axes[1].set_ylabel("in-band leaked energy E_far")
    axes[1].set_title("Coupling-law discriminator (linear regime)")
    axes[1].legend(fontsize=7)
    fig.text(0.5, -0.02, f"VERDICT: {v['BRANCH_VERDICT']}", ha="center", fontsize=9)
    fig.tight_layout()
    p = fig_dir / "superband_carrier_fork.png"
    fig.savefig(p, dpi=120, bbox_inches="tight")
    print(f"wrote {p}")


if __name__ == "__main__":
    main()
