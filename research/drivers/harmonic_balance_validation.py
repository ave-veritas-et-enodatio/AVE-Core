#!/usr/bin/env python
"""Validation driver — harmonic-balance solver, the three Stage-2 gates.

Build brief: _orchestration/2026-08-24_static-existence-build-brief.md Stage 2:
every gate COMPUTES its pass (reconcile-don't-declare); this driver writes the
receipts JSON that src/tests/test_harmonic_balance_srs.py::TestReceiptsReconciled
and research/drivers/harmonic_balance_number_check.py re-verify from the
committed files.

  GATE 1 — cold linear limit -> the arccos band structure. Drive the cold srs
    net across a theta sweep, fit k(theta), and check (i) the velocity factor
    c(smallest theta)/c_link against ANALYTIC_NETWORK_FACTOR = 1/sqrt(3)
    (imported; tolerance 2% = the frozen CS-2 gate of the Class-C prereg §5),
    (ii) theta_arccos(k_fit) == theta against the canonical TL map
    omega_n(k) = omega_link arccos(mu_n(k)/3) (srs-band-structure.md:38, built
    from the net's own Bloch adjacency), (iii) the CS-2-style band-edge
    criterion: every swept point with k <= the MEASURED cold-gate k_edge
    (loaded from engine_gamma_meanstest_results.json sanity block) has c
    within 5% of the analytic c0.

  GATE 2 — single-tone graded limit -> the MEASURED Class-C response map.
    The G-J geometry is loaded from the measured results JSON params (never
    re-declared), the target rows are the measured-VALID G-J table entries,
    and the solver's de-embedded interface Gamma (multi-load two-port,
    >= 3 absorber positions; see harmonic_balance_srs.interface_two_port for
    the declared coordinate map: time-window front-echo isolation ==
    far-side-matched interface response) is compared per point.
    Tolerance [ENGINEERING-CHOICE, tagged]: |dGamma| <= max(0.01,
    0.05 |Gamma_meas|) — floor from the two instruments' null floors
    (measured epsilon_0 = 0.00545; this instrument's cold null, computed
    below, < 1e-3) and the measured locus's own 0.2-2% spread vs the core
    curve; the two instruments are different estimator classes (pulse
    matched-filter vs steady-state fit), so agreement at this band is the
    honest claim. A theta-flatness receipt (A = 0.9 at theta 0.10/0.20)
    bounds the quasi-static-limit sensitivity of the declared theta = 0.15.

  GATE 3 — source-idle machinery on the known driven-vs-autonomous pair:
    an initialized lossless ring mode is source-idle (r_auto ~ 0, nothing
    touches the scaffold); a driven cold srs tank never is. Thresholds are
    declared inputs, verdicts computed.

Outputs (landed layout, ave-chart-instrument precedent):
  research/drivers/data/harmonic_balance_validation/receipts.json
  research/drivers/data/harmonic_balance_validation/run_log.txt
  research/figures/2026-08-24-harmonic-balance-solver/fig1_gate2_overlay.{png,pdf}
  research/figures/2026-08-24-harmonic-balance-solver/fig2_gate1_dispersion.{png,pdf}

The driver prints every parameter it actually uses (house rule).
Run: PYTHONPATH=src python research/drivers/harmonic_balance_validation.py
"""

from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import numpy as np

_REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(_REPO / "src"))

import ave.solvers.harmonic_balance_srs as hb  # noqa: E402
from ave.core.chiral_lattice import build_srs_net  # noqa: E402
from ave.core.chiral_lattice_dynamics import ANALYTIC_NETWORK_FACTOR  # noqa: E402

MEASURED_JSON = _REPO / "research" / "drivers" / "engine_gamma_meanstest_results.json"
DATA_DIR = _REPO / "research" / "drivers" / "data" / "harmonic_balance_validation"
FIG_DIR = _REPO / "research" / "figures" / "2026-08-24-harmonic-balance-solver"

# ── declared parameters (every one echoed to the run log) ────────────────────
P = {
    # gate 1
    "g1_L": 8,
    "g1_theta_sweep": [0.05, 0.10, 0.15, 0.20, 0.30, 0.40, 0.60, 0.80],
    "g1_src_plane": 0.5,
    "g1_abs_plane": 6.5,
    "g1_fit_region": [1.0, 5.8],
    "g1_velocity_tol": 0.02,  # the frozen CS-2 velocity gate (Class-C prereg §5)
    "g1_arccos_tol": 1e-3,  # rad/step, instrument tolerance (declared)
    "g1_band_edge_tol": 0.05,  # the CS-2 band criterion re-applied
    # gate 2 (geometry loaded from the measured JSON params at runtime)
    "g2_theta": 0.15,
    "g2_theta_flatness": [0.10, 0.20],
    "g2_flatness_A": 0.9,
    "g2_src_plane": 0.5,
    "g2_load_planes": [11.5, 12.0, 12.5],
    "g2_feed_fit": [1.5, 8.0],
    "g2_slab_margin": 0.5,
    "g2_tol_abs_floor": 0.01,  # ENGINEERING-CHOICE, rationale in module header
    "g2_tol_rel": 0.05,  # ENGINEERING-CHOICE
    # gate 3
    "g3_ring_N": 12,
    "g3_ring_m": 2,
    "g3_tank_L": 2,
    "g3_tank_theta": 0.3,
    "g3_source_tol": 1e-12,
    "g3_exchange_tol": 1e-12,
    "g3_r_auto_tol": 1e-10,
    # solver
    "solve_warmstart_first": 800,
    "solve_warmstart_next": 200,
    "solve_tol": 1e-11,
}

_LOG_LINES: list[str] = []


def log(msg: str) -> None:
    print(msg, flush=True)
    _LOG_LINES.append(msg)


def _plane_term(net, bt, conn, planes_drives, n_tones=1):
    specs = []
    for plane, drive_fwd, drive_bwd in planes_drives:
        f, b = hb.crossing_ports(net, bt, plane)
        specs.append((f, np.asarray(drive_fwd, dtype=np.complex128)))
        specs.append((b, np.asarray(drive_bwd, dtype=np.complex128)))
    return hb.make_termination(net, bt, conn, specs, n_tones)


# ═════════════════════════════════════════════════════════════════════════════
# GATE 1
# ═════════════════════════════════════════════════════════════════════════════
def gate1(measured_sanity: dict) -> dict:
    log("\n== GATE 1 — cold linear limit -> arccos band structure ==")
    L = P["g1_L"]
    net = build_srs_net(L=L)
    bt = hb.build_bond_table(net)
    conn = net.connect_index()
    a_nodes, _ = hb.scatter_weights(bt, hb.bond_admittance(np.zeros(bt.n_bonds)))
    term = _plane_term(
        net,
        bt,
        conn,
        [
            (P["g1_src_plane"], [1.0 + 0j], [0.0 + 0j]),
            (P["g1_abs_plane"], [0.0 + 0j], [0.0 + 0j]),
        ],
    )
    log(f"  net: srs L={L} (N={net.n_nodes}, ndof={net.n_nodes * net.degree}); "
        f"src plane {P['g1_src_plane']}, absorber {P['g1_abs_plane']} (cells); "
        f"fit region {P['g1_fit_region']} (cells)")
    points = []
    v_prev = None
    for theta in P["g1_theta_sweep"]:
        t0 = time.time()
        sol = hb.solve_tone(
            a_nodes, conn, theta, term, 0,
            tol=P["solve_tol"],
            warmstart=P["solve_warmstart_first"] if v_prev is None else P["solve_warmstart_next"],
            x0=v_prev,
        )
        v_prev = sol.v
        x, V = hb.plane_binned_voltage(net, a_nodes, sol.v, *P["g1_fit_region"])
        k0 = theta / ANALYTIC_NETWORK_FACTOR
        fit = hb.fit_k(x, V, 0.6 * k0, 1.4 * k0)
        band = hb.nearest_band_theta(net, fit["k"], theta)
        c = theta / fit["k"]
        points.append(
            {
                "theta": theta,
                "k_fit": fit["k"],
                "c": c,
                "theta_arccos": band["theta_band"],
                "band_index": band["band_index"],
                "fit_resid": fit["resid_rel"],
                "solve_resid": sol.residual_rel,
            }
        )
        log(f"  theta={theta:5.2f}: k={fit['k']:.6f} c={c:.6f} "
            f"theta_arccos={band['theta_band']:.6f} (band {band['band_index']}) "
            f"fit_resid={fit['resid_rel']:.1e} "
            f"solve_resid={sol.residual_rel:.1e} ({time.time() - t0:.1f}s)")

    c_small = points[0]["c"]
    vel_rel = abs(c_small - ANALYTIC_NETWORK_FACTOR) / ANALYTIC_NETWORK_FACTOR
    vel_pass = vel_rel < P["g1_velocity_tol"]
    arccos_dev = max(abs(p["theta_arccos"] - p["theta"]) for p in points)
    arccos_pass = arccos_dev < P["g1_arccos_tol"]
    # CS-2-style band-edge criterion against the MEASURED cold-gate k_edge
    k_edge_measured = float(measured_sanity["CS2_k_edge"])
    in_band = [p for p in points if p["k_fit"] <= k_edge_measured]
    band_devs = [abs(p["c"] - ANALYTIC_NETWORK_FACTOR) / ANALYTIC_NETWORK_FACTOR for p in in_band]
    band_edge_pass = bool(in_band) and all(d < P["g1_band_edge_tol"] for d in band_devs)
    out = {
        "L": L,
        "points": points,
        "c_smallest_theta": c_small,
        "analytic_network_factor": float(ANALYTIC_NETWORK_FACTOR),
        "velocity_rel_dev": vel_rel,
        "velocity_tol": P["g1_velocity_tol"],
        "velocity_pass": bool(vel_pass),
        "max_arccos_dev": arccos_dev,
        "arccos_tol": P["g1_arccos_tol"],
        "arccos_pass": bool(arccos_pass),
        "k_edge_measured": k_edge_measured,
        "n_points_in_band": len(in_band),
        "band_edge_max_rel_dev": max(band_devs) if band_devs else None,
        "band_edge_tol": P["g1_band_edge_tol"],
        "band_edge_pass": bool(band_edge_pass),
        "pass": bool(vel_pass and arccos_pass and band_edge_pass),
    }
    log(f"  velocity: c={c_small:.6f} vs 1/sqrt(3)={ANALYTIC_NETWORK_FACTOR:.6f} "
        f"rel {vel_rel:.3%} (tol {P['g1_velocity_tol']:.0%}) -> {'PASS' if vel_pass else 'FAIL'}")
    log(f"  arccos map: max|theta_arccos - theta| = {arccos_dev:.2e} rad "
        f"(tol {P['g1_arccos_tol']:.0e}) -> {'PASS' if arccos_pass else 'FAIL'}")
    log(f"  band edge: {len(in_band)} pts with k <= {k_edge_measured:.4f}, "
        f"max rel dev {max(band_devs):.3%} (tol {P['g1_band_edge_tol']:.0%}) "
        f"-> {'PASS' if band_edge_pass else 'FAIL'}")
    log(f"  GATE 1: {'PASS' if out['pass'] else 'FAIL'}")
    return out


# ═════════════════════════════════════════════════════════════════════════════
# GATE 2
# ═════════════════════════════════════════════════════════════════════════════
def _gj_gamma(net, bt, conn, inside, A, theta, x_I, load_planes):
    """De-embedded interface Gamma for the G-J grading at amplitude A."""
    Ab = np.zeros(bt.n_bonds)
    Ab[inside] = A
    a_nodes, _ = hb.scatter_weights(bt, hb.bond_admittance(Ab))
    k0 = theta / ANALYTIC_NETWORK_FACTOR
    xref = x_I * net.a_cell
    runs = []
    diag = []
    v_prev = None
    for x_abs in load_planes:
        term = _plane_term(
            net, bt, conn,
            [(P["g2_src_plane"], [1.0 + 0j], [0.0 + 0j]), (x_abs, [0.0 + 0j], [0.0 + 0j])],
        )
        sol = hb.solve_tone(
            a_nodes, conn, theta, term, 0,
            tol=P["solve_tol"],
            warmstart=P["solve_warmstart_first"] if v_prev is None else P["solve_warmstart_next"],
            x0=v_prev,
        )
        v_prev = sol.v
        xf, Vf = hb.plane_binned_voltage(net, a_nodes, sol.v, *P["g2_feed_fit"])
        fitf = hb.fit_k(xf, Vf, 0.6 * k0, 1.4 * k0)
        k = fitf["k"]
        xs, Vs = hb.plane_binned_voltage(
            net, a_nodes, sol.v, x_I + P["g2_slab_margin"], x_abs - P["g2_slab_margin"]
        )
        fits = hb.fit_two_waves(xs, Vs, k)
        runs.append(
            {
                "a": fitf["a"] * np.exp(-1j * k * xref),
                "b": fitf["b"] * np.exp(+1j * k * xref),
                "c": fits["a"] * np.exp(-1j * k * xref),
                "d": fits["b"] * np.exp(+1j * k * xref),
            }
        )
        diag.append(
            {
                "x_abs": x_abs,
                "solve_resid": sol.residual_rel,
                "feed_fit_resid": fitf["resid_rel"],
                "slab_fit_resid": fits["resid_rel"],
                "k_fit": k,
            }
        )
    two_port = hb.interface_two_port(runs)
    return two_port, diag


def gate2(measured: dict) -> dict:
    log("\n== GATE 2 — single-tone graded limit -> the MEASURED Class-C map ==")
    params = measured["params"]
    L = int(params["L"])
    x_I, x_B = float(params["x_I"]), float(params["x_B"])
    enant = params["enantiomorph"]
    log(f"  geometry from measured params: L={L}, enantiomorph={enant}, "
        f"x_I={x_I}, x_B={x_B} (G-J: bonds strictly inside)")
    log(f"  theta={P['g2_theta']} (in the measured pulse band; flatness receipt at "
        f"{P['g2_theta_flatness']}); loads {P['g2_load_planes']}; "
        f"feed fit {P['g2_feed_fit']}; slab margin {P['g2_slab_margin']}")
    net = build_srs_net(L=L, enantiomorph=enant)
    bt = hb.build_bond_table(net)
    conn = net.connect_index()
    x0, x1 = bt.b_x0, bt.b_x0 + bt.b_dx
    lo, hi = np.minimum(x0, x1), np.maximum(x0, x1)
    inside = (lo > x_I) & (hi < x_B)
    log(f"  net: N={net.n_nodes}, ndof={net.n_nodes * net.degree}; graded bonds "
        f"{int(inside.sum())}/{bt.n_bonds}")

    rows = measured["table"]["GJ"]
    valid_rows = [r for r in rows if r["valid"]]
    log(f"  target: {len(valid_rows)} measured-VALID G-J points "
        f"(A = {[r['A'] for r in valid_rows]})")

    # cold-null receipt (the CS-5 analog for THIS instrument)
    t0 = time.time()
    tp0, diag0 = _gj_gamma(net, bt, conn, inside, 0.0, P["g2_theta"], x_I, P["g2_load_planes"])
    cold_null = abs(tp0["gamma"])
    log(f"  cold null |Gamma(A=0)| = {cold_null:.2e} (deembed resid "
        f"{tp0['resid_rel']:.1e}; {time.time() - t0:.0f}s)")

    points = []
    for r in valid_rows:
        A = float(r["A"])
        t0 = time.time()
        tp, diag = _gj_gamma(net, bt, conn, inside, A, P["g2_theta"], x_I, P["g2_load_planes"])
        g_signed, phase = hb.signed_gamma(tp["gamma"])
        dev = abs(g_signed - float(r["gamma"]))
        tol_pt = max(P["g2_tol_abs_floor"], P["g2_tol_rel"] * abs(float(r["gamma"])))
        ok = dev <= tol_pt
        points.append(
            {
                "A": A,
                "gamma_measured": float(r["gamma"]),
                "gamma_solver": g_signed,
                "gamma_solver_phase": phase,
                "abs_dev": dev,
                "tol_point": tol_pt,
                "pass": bool(ok),
                "deembed_resid": tp["resid_rel"],
                "t_mag": abs(tp["t"]),
                "max_solve_resid": max(d["solve_resid"] for d in diag),
                "max_fit_resid": max(max(d["feed_fit_resid"], d["slab_fit_resid"]) for d in diag),
            }
        )
        log(f"  A={A:6.4g}: solver {g_signed:+.5f} (phase {phase:+.3f}) vs "
            f"measured {r['gamma']:+.5f}  |dev| {dev:.5f} tol {tol_pt:.3f} "
            f"-> {'PASS' if ok else 'FAIL'}  (deembed {tp['resid_rel']:.1e}, "
            f"{time.time() - t0:.0f}s)")

    # theta-flatness receipt at the declared A
    flat = []
    for th in P["g2_theta_flatness"]:
        tp, _ = _gj_gamma(net, bt, conn, inside, P["g2_flatness_A"], th, x_I, P["g2_load_planes"])
        gs, _ph = hb.signed_gamma(tp["gamma"])
        flat.append({"theta": th, "gamma_solver": gs})
        log(f"  flatness: theta={th} -> Gamma = {gs:+.5f}")
    g_at_primary = next(p["gamma_solver"] for p in points if p["A"] == P["g2_flatness_A"])
    flat_spread = max(abs(f["gamma_solver"] - g_at_primary) for f in flat)
    log(f"  flatness spread at A={P['g2_flatness_A']}: {flat_spread:.5f}")

    out = {
        "geometry_from": "engine_gamma_meanstest_results.json params",
        "L": L,
        "x_I": x_I,
        "x_B": x_B,
        "theta": P["g2_theta"],
        "load_planes": P["g2_load_planes"],
        "cold_null_abs_gamma": cold_null,
        "cold_null_deembed_resid": tp0["resid_rel"],
        "points": points,
        "n_points": len(points),
        "max_abs_dev": max(p["abs_dev"] for p in points),
        "tol_abs_floor": P["g2_tol_abs_floor"],
        "tol_rel": P["g2_tol_rel"],
        "theta_flatness": flat,
        "theta_flatness_spread": flat_spread,
        "pass": bool(all(p["pass"] for p in points)),
    }
    log(f"  GATE 2: {'PASS' if out['pass'] else 'FAIL'} "
        f"(max |dev| {out['max_abs_dev']:.5f} over {out['n_points']} points)")
    return out


# ═════════════════════════════════════════════════════════════════════════════
# GATE 3
# ═════════════════════════════════════════════════════════════════════════════
def gate3() -> dict:
    log("\n== GATE 3 — source-idle machinery on the known pair ==")
    thr = {
        "source_tol": P["g3_source_tol"],
        "exchange_tol": P["g3_exchange_tol"],
        "r_auto_tol": P["g3_r_auto_tol"],
    }
    log(f"  declared thresholds: {thr}")

    # autonomous side: initialized lossless ring mode
    N, m = P["g3_ring_N"], P["g3_ring_m"]
    ring = hb.build_ring_net(N)
    bt_r = hb.build_bond_table(ring)
    conn_r = ring.connect_index()
    a_r, Yp_r = hb.scatter_weights(bt_r, hb.bond_admittance(np.zeros(bt_r.n_bonds)))
    v, k = hb.ring_mode(N, m)
    sol_r = hb.ToneSolution(theta=k, v=v, residual_rel=0.0, converged=True, n_matvec=0, method="exact")
    rep_r = hb.source_idle_report(a_r, conn_r, None, [sol_r], Yp_r)
    ver_r = hb.idle_verdict(rep_r, **thr)
    log(f"  ring N={N} m={m} (theta=k={k:.4f}): r_auto={rep_r['max_r_auto']:.2e}, "
        f"source={rep_r['max_source_amp']}, exchange={rep_r['max_exchange_amp']} "
        f"-> idle={ver_r['idle']}")

    # driven side: source-terminated cold srs tank
    Lt, th_t = P["g3_tank_L"], P["g3_tank_theta"]
    tank = build_srs_net(L=Lt)
    bt_t = hb.build_bond_table(tank)
    conn_t = tank.connect_index()
    a_t, Yp_t = hb.scatter_weights(bt_t, hb.bond_admittance(np.zeros(bt_t.n_bonds)))
    term_t = _plane_term(tank, bt_t, conn_t, [(0.5, [1.0 + 0j], [0.0 + 0j])])
    sol_t = hb.solve_tone(a_t, conn_t, th_t, term_t, 0, warmstart=200, tol=P["solve_tol"])
    rep_t = hb.source_idle_report(a_t, conn_t, term_t, [sol_t], Yp_t)
    ver_t = hb.idle_verdict(rep_t, **thr)
    log(f"  driven tank L={Lt} theta={th_t}: r_auto={rep_t['max_r_auto']:.3f}, "
        f"source={rep_t['max_source_amp']:.3f}, exchange={rep_t['max_exchange_amp']:.3f} "
        f"-> idle={ver_t['idle']} (solve resid {sol_t.residual_rel:.1e})")

    out = {
        "thresholds": thr,
        "ring": {
            "N": N,
            "m": m,
            "theta": k,
            "max_source_amp": rep_r["max_source_amp"],
            "max_exchange_amp": rep_r["max_exchange_amp"],
            "max_r_auto": rep_r["max_r_auto"],
            "idle": ver_r["idle"],
        },
        "driven_tank": {
            "L": Lt,
            "theta": th_t,
            "max_source_amp": rep_t["max_source_amp"],
            "max_exchange_amp": rep_t["max_exchange_amp"],
            "max_r_auto": rep_t["max_r_auto"],
            "solve_resid": sol_t.residual_rel,
            "idle": ver_t["idle"],
        },
        "pass": bool(ver_r["idle"] and not ver_t["idle"]),
    }
    log(f"  GATE 3: {'PASS' if out['pass'] else 'FAIL'} "
        f"(ring idle={ver_r['idle']}, tank idle={ver_t['idle']})")
    return out


# ═════════════════════════════════════════════════════════════════════════════
# figures (white house style)
# ═════════════════════════════════════════════════════════════════════════════
def make_figures(g1: dict, g2: dict) -> None:
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    from ave.viz import style

    style.apply("print")
    FIG_DIR.mkdir(parents=True, exist_ok=True)

    # fig 1 — gate-2 overlay: measured points vs solver points vs core locus
    fig, ax = plt.subplots(figsize=style.figsize("single"))
    Ad = np.linspace(0.0, 0.999, 400)
    S = np.sqrt(np.clip(1.0 - Ad**2, 0.0, 1.0))
    z = np.sqrt(S)
    ax.plot(Ad, (z - 1.0) / (z + 1.0), color=style.COLORS["muted"], lw=1.0,
            label="core locus: $\\Gamma=(\\sqrt{S}-1)/(\\sqrt{S}+1)$, $S=\\sqrt{1-A^2}$")
    Am = [p["A"] for p in g2["points"]]
    Gm = [p["gamma_measured"] for p in g2["points"]]
    Gs = [p["gamma_solver"] for p in g2["points"]]
    ax.plot(Am, Gm, "o", color="#0072B2", ms=5, ls="none",
            label="measured G-J (Class-C pulse, valid points)")
    ax.plot(Am, Gs, "x", color="#D55E00", ms=6, mew=1.2, ls="none",
            label=f"HB solver (de-embedded interface, $\\theta$={g2['theta']}/step)")
    ax.axhline(0.0, color=style.COLORS["muted"], lw=0.5)
    ax.set_xlabel(style.axis_label("Grading amplitude", "A", ""))
    ax.set_ylabel(style.axis_label("Reflection coefficient", "\\Gamma", ""))
    ax.set_xlim(0, 1.0)
    style.legend(ax, where="right", fontsize=6.5)
    paths = style.save(fig, FIG_DIR / "fig1_gate2_overlay")
    log(f"Figure written: {[str(x) for x in paths]}")
    plt.close(fig)

    # fig 2 — gate-1 dispersion: solver k(theta) points vs the arccos curve
    fig, ax = plt.subplots(figsize=style.figsize("single"))
    kk = np.linspace(1e-4, max(p["k_fit"] for p in g1["points"]) * 1.1, 300)
    net = build_srs_net(L=2)
    th_bands = np.array([hb.arccos_theta(hb.bloch_mu(net, np.array([k, 0.0, 0.0]))) for k in kk])
    for n in range(th_bands.shape[1]):
        ax.plot(kk, th_bands[:, n], color=style.COLORS["muted"], lw=0.7,
                label="canonical TL bands: $\\theta_n=\\arccos(\\mu_n(k)/3)$" if n == 0 else None)
    ax.plot(kk, kk * ANALYTIC_NETWORK_FACTOR, ls=":", color=style.COLORS["muted"], lw=0.8,
            label="acoustic slope $c_0=1/\\sqrt{3}$")
    ax.plot([p["k_fit"] for p in g1["points"]], [p["theta"] for p in g1["points"]],
            "x", color="#D55E00", ms=6, mew=1.2, ls="none", label="HB solver (driven solve + k-fit)")
    ax.set_xlabel(style.axis_label("Wavevector", "k", "rad / bond length"))
    ax.set_ylabel(style.axis_label("Tone", "\\theta", "rad / step"))
    style.legend(ax, where="right", fontsize=6.5)
    paths = style.save(fig, FIG_DIR / "fig2_gate1_dispersion")
    log(f"Figure written: {[str(x) for x in paths]}")
    plt.close(fig)


# ═════════════════════════════════════════════════════════════════════════════
def main() -> int:
    log("HARMONIC-BALANCE SOLVER — Stage-2 validation gates (computed, never asserted)")
    log("=" * 78)
    log(f"repo: {_REPO}")
    log(f"measured data: {MEASURED_JSON}")
    log("parameters:")
    for key, val in P.items():
        log(f"  {key} = {val}")
    measured = json.loads(MEASURED_JSON.read_text())

    g1 = gate1(measured["sanity"])
    g2 = gate2(measured)
    g3 = gate3()

    receipts = {
        "driver": "research/drivers/harmonic_balance_validation.py",
        "measured_source": "research/drivers/engine_gamma_meanstest_results.json",
        "parameters": P,
        "gate1": g1,
        "gate2": g2,
        "gate3": g3,
        "all_pass": bool(g1["pass"] and g2["pass"] and g3["pass"]),
    }
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    (DATA_DIR / "receipts.json").write_text(json.dumps(receipts, indent=1))
    log(f"\nReceipts written: {DATA_DIR / 'receipts.json'}")

    make_figures(g1, g2)

    (DATA_DIR / "run_log.txt").write_text("\n".join(_LOG_LINES) + "\n")
    log(f"Run log written: {DATA_DIR / 'run_log.txt'}")
    log("=" * 78)
    log(f"GATES: 1={'PASS' if g1['pass'] else 'FAIL'} 2={'PASS' if g2['pass'] else 'FAIL'} "
        f"3={'PASS' if g3['pass'] else 'FAIL'} -> ALL {'PASS' if receipts['all_pass'] else 'FAIL'}")
    return 0 if receipts["all_pass"] else 1


if __name__ == "__main__":
    sys.exit(main())
