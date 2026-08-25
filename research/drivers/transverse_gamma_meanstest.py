#!/usr/bin/env python
"""Reciprocal-loading pulse reflection Gamma(A) on the 2-component transverse
vector-TLM carrier (static-existence Stage 1 / epic P1).

Executes research/2026-08-24_transverse-gamma-meanstest_prereg_FROZEN.md
verbatim. Driver-script honesty: every parameter actually used is printed at run
start; no silent defaults.

Machinery: the NEW module src/ave/solvers/transverse_graded_scatter.py (the
Stage-1 named extension; its 25 pytest gates are VOID-linked and must be green
before this driver runs). Engine imports are READ-ONLY. The chart forms are the
in-tree ave.viz.ave_chart instrument (shared A-axis parametrization; the T-ELEC
two-port form is the exact mirror -core).

Configs: TMAG (load="magnetic", Y = Y0/sqrt(S), the REPRODUCTION config — its
component-0 dynamics are mathematically the merged Class-C G-J scalar run, so it
is gated as R-1/R-2/R-3 reproduction against the banked
engine_gamma_meanstest_results.json, never claimed as an independent transverse
measurement) and TELEC (load="electric", Y = Y0*sqrt(S) — the new measurement:
the eps-side impedance loading has never been run on any channel).

SHA-checksum scope (prereg SS4.2, the Class-C result's own words): the t=0 hash
and the end-of-run hash are both computed from the SAME in-memory coefficient
array. The check can therefore detect in-place mutation of that array during the
run, and nothing else; it is NOT evidence that the stepper read S from that array
rather than from some copy or other source, and it cannot detect a leak that
never writes back. The freeze is over-determined by the E_Y drift gate, CS-4,
and the structural read of vector_graded_step (no A-update, no V-dependence).

The per-run V3 STRICT + reconcile check lives in the companion script
transverse_gamma_meanstest_check_sentinels.py (consumes the shipped sentinel
series; its full output is a REQUIRED appendix of the result doc).
"""
from __future__ import annotations

import hashlib
import json
import math
import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent
sys.path.insert(0, str(REPO / "src"))

from ave.core import chiral_lattice as cl  # noqa: E402
from ave.core import chiral_lattice_dynamics as cld  # noqa: E402
from ave.solvers import transverse_graded_scatter as tgs  # noqa: E402

OUT = dict(
    results=HERE / "transverse_gamma_meanstest_results.json",
    rawdir=HERE / "data" / "transverse_gamma_meanstest",
    figstem=REPO / "research" / "figures" / "2026-08-24-transverse-gamma-meanstest"
    / "fig1_gamma_overlay",
    banked=HERE / "engine_gamma_meanstest_results.json",
)

# ---------------------------------------------------------------------------
# FROZEN parameters (prereg sections in brackets); ALL printed at run start
# ---------------------------------------------------------------------------
P = dict(
    L=24,                      # [E1] Class-C D1 receipt adopted
    enantiomorph="right",      # [E8] optical activity OFF; achiral
    x_s=2.0, x_p=6.0, x_I=9.0, x_B=15.0, W_slab=6.0,   # [E2]
    wrap_margin_cells=11.0,
    sigma_x_cells=1.5,         # [E3] baseband Gaussian, comp-0 polarized
    back_monitor_x=15.5,       # [E2]
    sentinel_x=19.5, sentinel_thresh=0.01,             # [E2]
    bm_measurable_frac=0.01,   # DRIVER-DECLARED operationalization of the
                               # prereg's "no measurable back-monitor transit"
                               # fallback: a run's Fb enters the branch-(a)
                               # centroid pool only if max|Fb| >= this fraction
                               # of the launch peak (logged as deviation D1)
    A_grid=[0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.85,
            0.9, 0.925, 0.95, 0.9682, 0.98, 0.99],     # [E4] frozen literals
    T_cold=200, T_run=170, hard_cap=6000,              # [E5]
    guard_sigmas=2.0,          # [E6]
    discord_tol=0.2, discord_max_pts=4,                # [E6]
    cs2_tol=0.02, cs2_band_dev=0.05, cs2_band_frac=0.95, cs3_tol=0.05,  # [E7]
    cs1_drift=1e-10, cs4_dev=1e-12, v2_drift=1e-8, cs5_cap=0.02,        # [E7]
    theta_floor=0.05, delta_floor=0.01,                # [E7]
    cs6a_tol=1e-14, cs6b_tol=1e-12, cs6b_angle=0.7, cs6b_A=0.9,         # [E7]
    cs7_tol=1e-12, cs7_A=(0.5, 0.9), ct1_tol=1e-15,    # [E7]
    r2_tol=1e-6,               # [E7] reproduction bound vs banked G-J
    v5_leak=1e-12,             # [E7]
    sweep_closes_base=(60, 64, 70, 74),                # [E11] + close_f
    stability_closes=(70, 74),                         # [E11] + close_f
    tail_span=8, tail_frac=0.02,                       # [E11]
    stab_median_frac=0.1, trunc_count=3,               # [E11]
    floor_min_pts=3, mirror_min_pts=3,                 # [E7]
    dispersion_axis=0, m_values=(1, 2, 3, 4), n_steps_disp=800,         # [CS-2]
)
CONFIGS = {"TMAG": "magnetic", "TELEC": "electric"}


def banner(msg):
    print("\n" + "=" * 78 + f"\n{msg}\n" + "=" * 78, flush=True)


# ---------------------------------------------------------------------------
# Rig: net + module bond tables + geometry index sets (cell units for planes)
# ---------------------------------------------------------------------------
class Rig:
    def __init__(self, p):
        self.p = p
        self.net = cl.build_srs_net(L=p["L"], enantiomorph=p["enantiomorph"])
        net = self.net
        self.a = net.a_cell
        self.N, self.deg = net.n_nodes, net.degree
        self.conn = net.connect_index()
        self.box_cells = net.box / self.a
        self.xu = net.pos[:, 0] / self.a
        self.tables = tgs.BondTables(net)
        self.nb = self.tables.n_bonds
        # +x-propagating launch weighting (Class-C D2-corrected sign, adopted)
        self.wport = np.zeros((self.N, self.deg))
        for u in range(self.N):
            for pp in range(self.deg):
                self.wport[u, pp] = max(0.0, -net.bond_unit[u][pp][0])
        self.idx_probe_fwd, self.idx_probe_bwd = self._crossing_ports(p["x_p"])
        self.idx_bm_fwd, _ = self._crossing_ports(p["back_monitor_x"])
        self.idx_sent_fwd, self.idx_sent_bwd = self._crossing_ports(p["sentinel_x"])
        for name, idx in (("probe", self.idx_probe_fwd),
                          ("back-monitor", self.idx_bm_fwd),
                          ("sentinel", self.idx_sent_fwd)):
            assert len(idx) > 0, (
                f"{name} plane has no crossing bonds — the frozen geometry does "
                f"not fit this box (L={p['L']}); fail loud, never silently")

    def _crossing_ports(self, plane):
        """Flat (node*deg+port) indices for forward/backward waves on bonds
        crossing `plane` (component axis applied by the caller)."""
        net = self.net
        fwd, bwd = [], []
        x0 = self.tables.b_x0
        x1 = self.tables.b_x0 + self.tables.b_dx
        crossing = np.where((x0 - plane) * (x1 - plane) < 0.0)[0]
        for bi in crossing:
            u0, u1 = self.tables.bonds[bi]
            um, up = (u0, u1) if x0[bi] < x1[bi] else (u1, u0)
            p_up = net.neighbors[up].index(um)
            p_um = net.neighbors[um].index(up)
            fwd.append(up * self.deg + p_up)
            bwd.append(um * self.deg + p_um)
        return np.array(fwd, dtype=np.int64), np.array(bwd, dtype=np.int64)

    def a_field(self, A):
        """Far-side slab grading [prereg 4.3]: A on bonds with BOTH endpoints in
        x_I < x < x_B; bonds crossing x_I stay cold. Same region for both
        configs (the loading map is the config axis)."""
        p = self.p
        x0 = self.tables.b_x0
        x1 = self.tables.b_x0 + self.tables.b_dx
        lo, hi = np.minimum(x0, x1), np.maximum(x0, x1)
        Ab = np.zeros(self.nb)
        Ab[(lo > p["x_I"]) & (hi < p["x_B"])] = A
        return Ab

    def build_scatter(self, Ab, load):
        """Per-node coefficients + Y_port + SHA of the stacked coefficients.
        SHA scope: see the module docstring note at the top of this file."""
        Y_port = self.tables.port_admittance(Ab, load)
        a_nodes = tgs.scatter_coeffs(Y_port)
        sha = hashlib.sha256(np.ascontiguousarray(a_nodes).tobytes()).hexdigest()
        return a_nodes, Y_port, sha

    def launch(self):
        """Baseband Gaussian plane pulse, +x directional weighting, linearly
        polarized in component 0; component 1 identically zero [4.3 E3]."""
        p = self.p
        g = np.exp(-((self.xu - p["x_s"]) ** 2) / (2.0 * p["sigma_x_cells"] ** 2))
        V = np.zeros((self.N, self.deg, 2))
        V[:, :, 0] = g[:, None] * self.wport
        return V

    def run(self, a_nodes, Y_port, T):
        """T graded steps from the launch; per-step records on component 0 +
        the lattice-wide component-1 leak sentinel (V5)."""
        V = self.launch()
        EY0 = tgs.energy_Y(V, Y_port)
        F = np.zeros(T + 1)
        B = np.zeros(T + 1)
        Fb = np.zeros(T + 1)
        s_fwd = np.zeros(T + 1)
        s_bwd = np.zeros(T + 1)
        leak = np.zeros(T + 1)
        eydrift = 0.0
        V0 = V[:, :, 0]
        for t in range(1, T + 1):
            V = tgs.vector_graded_step(V, a_nodes, self.conn)
            V0 = V[:, :, 0]
            F[t] = V0.flat[self.idx_probe_fwd].sum()
            B[t] = V0.flat[self.idx_probe_bwd].sum()
            Fb[t] = V0.flat[self.idx_bm_fwd].sum()
            s_fwd[t] = np.abs(V0.flat[self.idx_sent_fwd]).max()
            s_bwd[t] = np.abs(V0.flat[self.idx_sent_bwd]).max()
            leak[t] = np.abs(V[:, :, 1]).max()
            eydrift = max(eydrift, abs(tgs.energy_Y(V, Y_port) - EY0) / EY0)
        return dict(F=F, B=B, Fb=Fb, sent_fwd=s_fwd, sent_bwd=s_bwd,
                    c1_leak=leak, ey_drift=eydrift)


# ---------------------------------------------------------------------------
# Pulse moments, windows, extraction [4.4] — ported from the Class-C driver
# ---------------------------------------------------------------------------
def pulse_moments(F, t_lo=0, t_hi=None):
    F = np.asarray(F)
    t_hi = len(F) - 1 if t_hi is None else t_hi
    t = np.arange(len(F))
    for _ in range(2):
        m = (t >= t_lo) & (t <= t_hi)
        w = F[m] ** 2
        c = float((t[m] * w).sum() / w.sum())
        s = float(np.sqrt(((t[m] - c) ** 2 * w).sum() / w.sum()))
        t_lo, t_hi = max(0, int(c - 3 * s)), min(len(F) - 1, int(c + 3 * s))
    return c, s


def extract_gamma(F, B, w_inc, w_refl):
    """Matched-filter signed Gamma + unsigned energy cross-check — the Class-C
    estimator verbatim (both D7 operationalizations are DECLARED spec here:
    the 25%-template-energy lag admissibility floor and the window-restricted
    denominator)."""
    T_len = len(F)
    tmpl = np.zeros(T_len)
    i0, i1 = w_inc
    tmpl[i0:i1 + 1] = F[i0:i1 + 1]
    E_tmpl = float((tmpl ** 2).sum())
    r0, r1 = w_refl
    mask = np.zeros(T_len, dtype=bool)
    mask[r0:r1 + 1] = True
    best = None
    for tau in range(1, T_len - i0):
        sh = np.zeros(T_len)
        hi = min(T_len, i1 + 1 + tau)
        sh[i0 + tau:hi] = tmpl[i0:i0 + (hi - i0 - tau)]
        den = float((sh[mask] ** 2).sum())
        if den < 0.25 * E_tmpl:
            continue
        num = float((B[mask] * sh[mask]).sum())
        if best is None or abs(num) > abs(best[0]):
            best = (num, den, tau)
    if best is None:
        return dict(gamma=0.0, gammaE=0.0, tau=None, EF=E_tmpl, EB=0.0,
                    tmpl_contained=False)
    num, den, tau = best
    E_F = float((F[i0:i1 + 1] ** 2).sum())
    E_B = float((B[r0:r1 + 1] ** 2).sum())
    return dict(gamma=num / den, gammaE=math.sqrt(E_B / E_F), tau=tau,
                EF=E_F, EB=E_B, tmpl_contained=bool(i1 + tau <= r1))


def derive_windows(rig, sanity, t_back_centroid_min):
    """Windows per the pinned Class-C rule (prereg 4.4): incident = t_cF +- 2s;
    reflected close = earliest of (a) back-monitor min-centroid -> front (-2s)
    -> guard (-2s), (b) cold wrap-sentinel projection -> guard (-2s)."""
    p = rig.p
    t_cF, s_t, c = sanity["t_cF"], sanity["sigma_t"], sanity["c_meas"]
    g = p["guard_sigmas"] * s_t
    w_inc = (max(1, int(round(t_cF - g))), int(round(t_cF + g)))
    t_open = w_inc[1] + 1
    closes = []
    t_wrap_probe = None
    for key, dist_cells in (
            ("sent_bwd", p["sentinel_x"] - p["x_p"]),
            ("sent_fwd", rig.box_cells - p["sentinel_x"] + p["x_p"])):
        cross = np.where(sanity["cold"][key] > p["sentinel_thresh"])[0]
        if len(cross):
            t_arr = float(cross[0]) + dist_cells * rig.a / c
            if t_wrap_probe is None or t_arr < t_wrap_probe:
                t_wrap_probe = t_arr
    if t_wrap_probe is not None:
        closes.append(t_wrap_probe - g)
    t_back = None
    if t_back_centroid_min is not None:
        t_back = t_back_centroid_min + (p["back_monitor_x"] - p["x_p"]) * rig.a / c
        closes.append((t_back - 2 * s_t) - g)
    t_close = int(math.floor(min(closes))) if closes else len(sanity["cold"]["F"]) - 2
    return dict(w_inc=list(w_inc), w_refl=[t_open, t_close],
                t_wrap_probe=t_wrap_probe, t_back_return=t_back,
                constructible=bool(t_close > t_open))

# ---------------------------------------------------------------------------
# Cold + structure gates [5] — pre-graded set; run is VOID on any failure
# ---------------------------------------------------------------------------
def pre_graded_gates(rig):
    p = rig.p
    out = {}
    banner("PRE-GRADED GATES (prereg 5) — CS-1..CS-4, CS-6, CS-7, CT-1")

    # CS-1: closed-system conservation, uniform coefficients, actual launch
    a_uni = tgs.scatter_coeffs(np.ones((rig.N, rig.deg)))
    V = rig.launch()
    E0 = float(np.sum(V * V))
    drift = 0.0
    traj_uni = []
    for _ in range(p["T_cold"]):
        V = tgs.vector_graded_step(V, a_uni, rig.conn)
        traj_uni.append(V[:, :, 0].copy())
        drift = max(drift, abs(float(np.sum(V * V)) - E0) / E0)
    out["CS1_drift"] = drift
    out["CS1_pass"] = drift < p["cs1_drift"]
    print(f"CS-1 vector energy drift (uniform, {p['T_cold']} steps): {drift:.3e} "
          f"(gate < {p['cs1_drift']:.0e}) -> {'PASS' if out['CS1_pass'] else 'FAIL'}")

    # CS-4: all-cold graded machinery vs uniform SCALAR trajectory, comp 0
    a_cold, Y_cold, _ = rig.build_scatter(np.zeros(rig.nb), "magnetic")
    S_uni = cl.scatter_matrix(rig.deg)
    Vs = rig.launch()[:, :, 0]
    Vv = rig.launch()
    dev, leak = 0.0, 0.0
    for t in range(p["T_cold"]):
        Vs = cl.scalar_tlm_step(rig.net, Vs, S_uni, rig.conn)
        Vv = tgs.vector_graded_step(Vv, a_cold, rig.conn)
        dev = max(dev, float(np.abs(Vv[:, :, 0] - Vs).max()))
        leak = max(leak, float(np.abs(Vv[:, :, 1]).max()))
    out["CS4_dev"] = dev
    out["CS4_pass"] = dev <= p["cs4_dev"]
    out["CS6a_leak"] = leak
    out["CS6a_pass"] = leak <= p["cs6a_tol"]
    print(f"CS-4 all-cold vector-vs-scalar regression: max|dV| = {dev:.3e} "
          f"(gate <= {p['cs4_dev']:.0e}) -> {'PASS' if out['CS4_pass'] else 'FAIL'}")
    print(f"CS-6a decoupling: max comp-1 = {leak:.3e} "
          f"(gate <= {p['cs6a_tol']:.0e}) -> {'PASS' if out['CS6a_pass'] else 'FAIL'}")

    # CS-2: scalar dispersion receipt (valid for the vector channel via CS-6a)
    nv = cld.network_velocity_factor(
        rig.net, axis=p["dispersion_axis"], m_values=p["m_values"],
        n_steps=p["n_steps_disp"])
    fac, target = nv["factor"], cld.ANALYTIC_NETWORK_FACTOR
    rel = abs(fac - target) / target
    c_link = cld.mean_bond_length(rig.net)
    k1 = nv["c_of_k"][0] / c_link
    rel_k1 = abs(k1 - target) / target
    ks, cs = np.array(nv["k"]), np.array(nv["c_of_k"])
    devs = np.abs(cs - nv["c0"]) / nv["c0"]
    good = devs < p["cs2_band_dev"]
    all_in_band = bool(good.all())
    k_edge = float(ks[good].max()) if good.any() else 0.0
    sigma_x = p["sigma_x_cells"] * rig.a
    frac_analytic = math.erf(k_edge * sigma_x)
    nbins = p["L"]
    prof, _ = np.histogram(rig.xu * rig.a, bins=nbins, range=(0, rig.net.box),
                           weights=rig.launch()[:, :, 0].sum(axis=1))
    cnt, _ = np.histogram(rig.xu * rig.a, bins=nbins, range=(0, rig.net.box))
    prof = prof / np.maximum(cnt, 1)
    Fk = np.abs(np.fft.rfft(prof - prof.mean())) ** 2
    kf = 2 * np.pi * np.fft.rfftfreq(nbins, d=rig.net.box / nbins)
    frac_disc = float(Fk[kf <= k_edge].sum() / Fk.sum()) if Fk.sum() > 0 else 0.0
    out.update(CS2_factor=fac, CS2_target=target, CS2_rel=rel,
               CS2_smallest_k=k1, CS2_rel_smallest_k=rel_k1,
               CS2_k=ks.tolist(), CS2_c=cs.tolist(), CS2_k_edge=k_edge,
               CS2_edge_is_bound_from_below=all_in_band,
               CS2_band_frac_analytic=frac_analytic,
               CS2_band_frac_discrete=frac_disc)
    out["CS2_pass"] = (rel < p["cs2_tol"]) and (rel_k1 < p["cs2_tol"]) and \
        (min(frac_analytic, frac_disc) >= p["cs2_band_frac"])
    print(f"CS-2 network factor: polyfit {fac:.6f} (rel {rel:.4%}), smallest-k "
          f"{k1:.6f} (rel {rel_k1:.4%}) vs 1/sqrt(3); gate < {p['cs2_tol']:.0%} each")
    print(f"CS-2 band edge k <= {k_edge:.4f} "
          f"({'bound-from-below: ALL sampled k in band' if all_in_band else 'measured rolloff'}); "
          f"pulse fraction below edge: analytic {frac_analytic:.5f} / discrete "
          f"{frac_disc:.5f} (gate >= {p['cs2_band_frac']:.2f}) "
          f"-> {'PASS' if out['CS2_pass'] else 'FAIL'}")

    # Cold reference run (defines timing); CS-3 TOF
    cold = rig.run(a_cold, Y_cold, p["T_cold"])
    t_cF, sigma_t = pulse_moments(cold["F"], 0, 3 * int(
        (p["x_p"] - p["x_s"]) * rig.a / cld.ANALYTIC_NETWORK_FACTOR))
    out["t_cF"], out["sigma_t"] = t_cF, sigma_t
    v_tof = (p["x_p"] - p["x_s"]) * rig.a / t_cF
    rel3 = abs(v_tof - nv["c0"]) / nv["c0"]
    out.update(CS3_v_tof=v_tof, CS3_c0=nv["c0"], CS3_rel=rel3)
    out["CS3_pass"] = rel3 < p["cs3_tol"]
    print(f"CS-3 TOF velocity: {v_tof:.5f} vs c0 {nv['c0']:.5f} (rel {rel3:.4%}, "
          f"gate < {p['cs3_tol']:.0%}) -> {'PASS' if out['CS3_pass'] else 'FAIL'}; "
          f"t_cF = {t_cF:.2f}, sigma_t = {sigma_t:.2f}")
    out["cold"] = cold
    out["c_meas"] = nv["c0"]

    # CS-6b: SO(2) equivariance at a graded operator, BOTH loading maps
    out["CS6b"] = {}
    cs6b_ok = True
    for cfg, load in CONFIGS.items():
        g = tgs.gate_so2_equivariance(
            rig.net, rig.tables, rig.a_field(p["cs6b_A"]), load,
            angle=p["cs6b_angle"], steps=100)
        g["pass"] = bool(g["max_abs_dev"] <= p["cs6b_tol"])
        out["CS6b"][cfg] = {k: g[k] for k in ("max_abs_dev", "angle", "steps", "pass")}
        cs6b_ok = cs6b_ok and g["pass"]
        print(f"CS-6b SO(2) equivariance [{cfg}/{load}] @A={p['cs6b_A']}: "
              f"max|d| = {g['max_abs_dev']:.3e} (gate <= {p['cs6b_tol']:.0e}) "
              f"-> {'PASS' if g['pass'] else 'FAIL'}")
    out["CS6b_pass"] = cs6b_ok

    # CS-7: load-map reconcile vs the guarded universal_dynamic_impedance
    out["CS7"] = {}
    cs7_ok = True
    for cfg, load in CONFIGS.items():
        for A in p["cs7_A"]:
            g = tgs.gate_cs7_reconcile(A, load, tol=p["cs7_tol"])
            out["CS7"][f"{cfg}_A{A}"] = g
            cs7_ok = cs7_ok and g["pass"]
            print(f"CS-7 reconcile [{cfg}/{load}] A={A}: |dY| = {g['abs_dev']:.2e} "
                  f"(gate <= {p['cs7_tol']:.0e}) -> {'PASS' if g['pass'] else 'FAIL'}")
    out["CS7_pass"] = cs7_ok

    # CT-1: implementation identity (NOT a transverse-vertex measurement)
    g = tgs.gate_ct1_vertex(tol=p["ct1_tol"])
    out["CT1"] = g
    out["CT1_pass"] = g["pass"]
    print(f"CT-1 implementation identity: dev_diag {g['dev_diag']:.1e}, dev_off "
          f"{g['dev_off']:.1e}, vs bedrock {g['dev_vs_bedrock']:.1e} "
          f"(gate <= {p['ct1_tol']:.0e}) -> {'PASS' if g['pass'] else 'FAIL'} "
          f"[implementation receipt only; prereg 2.6]")

    # Module gates T1(a)/T1(b) re-invoked for the run log (pytest is the gate)
    out["T1"] = {}
    t1_ok = True
    for cfg, load in CONFIGS.items():
        ga = tgs.gate_t1a_global_uniform(rig.net, rig.tables, 0.9, load)
        gb = tgs.gate_t1b_boundary_set(rig.tables, rig.a_field(0.9), load)
        out["T1"][cfg] = {"t1a": ga, "t1b": {k: gb[k] for k in
                          ("n_deviating", "n_mixed", "sets_equal", "max_dev", "pass")}}
        t1_ok = t1_ok and ga["pass"] and gb["pass"]
        print(f"T1 [{cfg}]: (a) uniform-collapse max|d| = {ga['max_abs_dev']:.2e} "
              f"{'PASS' if ga['pass'] else 'FAIL'}; (b) boundary-set "
              f"{gb['n_deviating']}/{gb['n_mixed']} nodes, sets_equal="
              f"{gb['sets_equal']}, max_dev = {gb['max_dev']:.3f} "
              f"{'PASS' if gb['pass'] else 'FAIL'}")
    out["T1_pass"] = t1_ok
    return out


# ---------------------------------------------------------------------------
# Classifiers [6.2] + per-loading verdicts [6.3]
# ---------------------------------------------------------------------------
def classify(rows, theta, delta, p, *, want_shape=False):
    v = [r for r in rows if r["valid"]]
    out = {"n_valid": len(v)}
    supra = [r for r in v if abs(r["gamma"]) > theta]
    if supra:
        top = max(supra, key=lambda r: r["A"])
        out["SIGN_top"] = float(np.sign(top["gamma"]))
        out["SIGN_top_A"] = top["A"]
    else:
        out["SIGN_top"] = None  # UNDEFINED
        out["SIGN_top_A"] = None
    crossings = []
    for a, b in zip(v[:-1], v[1:]):
        if (np.sign(a["gamma"]) != np.sign(b["gamma"])
                and abs(a["gamma"]) > theta and abs(b["gamma"]) > theta):
            crossings.append((a["A"], b["A"], "-+" if a["gamma"] < 0 else "+-"))
    out["crossings"] = crossings
    out["delta_sign_profile"] = [(r["A"], float(np.sign(r["gamma"])))
                                 for r in v if abs(r["gamma"]) > delta]
    g = [r["gamma"] for r in v]
    dec = all(g[i + 1] <= g[i] + delta for i in range(len(g) - 1))
    inc = all(g[i + 1] >= g[i] - delta for i in range(len(g) - 1))
    out["MONOTONE"] = dec or inc
    out["monotone_dir"] = "dec" if dec else ("inc" if inc else "none")
    fitpts = [r for r in v if 0.0 < r["A"] <= 0.5]
    if len(fitpts) >= p["floor_min_pts"]:
        Aarr = np.array([r["A"] for r in fitpts])
        Garr = np.array([r["gamma"] for r in fitpts])
        slope, intercept = np.polyfit(Aarr, Garr, 1)
        out["floor_intercept"] = float(intercept)
        out["FLOOR"] = bool(abs(intercept) > theta)
    else:
        out["floor_intercept"] = None
        out["FLOOR"] = f"NOT-COMPUTABLE ({len(fitpts)} valid pts in 0<A<=0.5)"
    if want_shape:
        n_cross = len(crossings)
        if n_cross == 0 and out["MONOTONE"] and out["monotone_dir"] == "inc":
            out["SHAPE"] = "ELEC-CORE-like"
        elif n_cross == 1 and crossings[0][2] == "-+":
            out["SHAPE"] = "ELEC-VERTEX-like"
        else:
            out["SHAPE"] = "OTHER"
    return out


def mirror_diag(rows_m, rows_e, theta, p, invalid_m, invalid_e):
    """MIRROR [6.2]: symmetrized-denominator antisymmetry defect over co-valid
    informative points; NOT-COMPUTABLE / N-A rules frozen."""
    if invalid_m or invalid_e:
        return {"status": "NOT-COMPUTABLE (a loading is INVALID-EXTRACTION)"}
    bm = {r["A"]: r for r in rows_m if r["valid"]}
    be = {r["A"]: r for r in rows_e if r["valid"]}
    pts = []
    for A in sorted(set(bm) & set(be)):
        gm, ge = bm[A]["gamma"], be[A]["gamma"]
        if max(abs(gm), abs(ge)) > theta:
            pts.append((A, abs(ge + gm) / max(abs(gm), abs(ge), theta)))
    if len(pts) < p["mirror_min_pts"]:
        return {"status": f"N/A ({len(pts)} co-valid informative pts "
                          f"< {p['mirror_min_pts']})", "points": pts}
    vals = [x[1] for x in pts]
    return {"status": "computed", "n_points": len(pts),
            "max": float(np.max(vals)), "median": float(np.median(vals)),
            "points": pts}


def telec_verdict(cls, invalid, window_unstable, escalated):
    """SS6.3 T-ELEC partition, first-match order."""
    if invalid:
        return ("INVALID-EXTRACTION", "informative-point discordance tally > 4")
    if window_unstable or escalated:
        why = []
        if window_unstable:
            why.append("S1: SIGN_top/theta-crossing count changed across stability closes")
        if escalated:
            why.append("S3: magnitude escalation (truncation-suspect/median fraction)")
        return ("INDETERMINATE-WINDOW", "; ".join(why))
    if cls["SIGN_top"] is None:
        return ("INDETERMINATE", "no valid point above theta anywhere")
    n_cross = len(cls["crossings"])
    plus_minus = any(d == "+-" for *_, d in cls["crossings"])
    if cls["SIGN_top"] == 1.0 and not plus_minus and n_cross <= 1:
        return ("DRAWS-OPEN", f"{n_cross} theta-crossing(s); SHAPE per 6.2 = "
                              f"{cls.get('SHAPE')}")
    return ("NONE", "complement of DRAWS-OPEN within a valid extraction")

# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    np.random.seed(0)
    banner("DRIVER PARAMETERS (all values actually used; no silent defaults)")
    for k, v in P.items():
        print(f"  {k} = {v}")
    for k, v in OUT.items():
        print(f"  {k} = {v}")

    rig = Rig(P)
    net = rig.net
    print(f"\nNet: {net.name}, carrier={net.carrier}, N={rig.N} nodes, degree="
          f"{rig.deg}, box={rig.box_cells:.0f} cells (a_cell={rig.a:.6f})")
    print(f"Bonds: {rig.nb}; probe bonds: {len(rig.idx_probe_fwd)}; back-monitor "
          f"bonds: {len(rig.idx_bm_fwd)}; sentinel bonds: {len(rig.idx_sent_fwd)}")
    print(f"Launch: +x, comp-0 polarized; peak = {rig.launch()[:, :, 0].max():.4f}")

    sanity = pre_graded_gates(rig)
    gate_keys = ("CS1_pass", "CS2_pass", "CS3_pass", "CS4_pass", "CS6a_pass",
                 "CS6b_pass", "CS7_pass", "CT1_pass", "T1_pass")
    OUT["rawdir"].mkdir(parents=True, exist_ok=True)
    if not all(sanity[k] for k in gate_keys):
        _dump_sanity(sanity)
        banner("PRE-GRADED GATES FAILED -> RUN IS VOID (V1). STOPPING.")
        sys.exit(2)

    banner("GRADED SWEEPS (16 A-points x 2 loadings) — DATA COLLECTION ONLY")
    raw = {c: {} for c in CONFIGS}
    v2_fail, v5_fail = [], []
    for cfg, load in CONFIGS.items():
        for A in P["A_grid"]:
            Ab = rig.a_field(A)
            a_nodes, Y_port, sha0 = rig.build_scatter(Ab, load)
            run = rig.run(a_nodes, Y_port, P["T_run"])
            sha1 = hashlib.sha256(
                np.ascontiguousarray(a_nodes).tobytes()).hexdigest()
            run["sha_match"] = (sha0 == sha1)
            run["n_graded_bonds"] = int((Ab > 0).sum())
            run["max_c1_leak"] = float(run["c1_leak"].max())
            raw[cfg][A] = run
            if run["ey_drift"] >= P["v2_drift"] or not run["sha_match"]:
                v2_fail.append((cfg, A, run["ey_drift"], run["sha_match"]))
            if run["max_c1_leak"] > P["v5_leak"]:
                v5_fail.append((cfg, A, run["max_c1_leak"]))
            print(f"  {cfg} A={A:<7} graded_bonds={run['n_graded_bonds']:<5} "
                  f"E_Y drift={run['ey_drift']:.2e} sha_ok={run['sha_match']} "
                  f"c1_leak={run['max_c1_leak']:.1e}")
    if v2_fail:
        _dump_sanity(sanity)
        banner(f"V2 VOID: grading leaked into dynamics: {v2_fail}")
        sys.exit(2)
    if v5_fail:
        _dump_sanity(sanity)
        banner(f"V5 VOID: polarization leak: {v5_fail}")
        sys.exit(2)

    banner("WINDOW DERIVATION (pinned Class-C rule) + R-1")
    launch_peak = float(rig.launch()[:, :, 0].max())
    windows = {}
    for cfg in CONFIGS:
        cents = []
        n_dropped = 0
        for A in P["A_grid"]:
            if A == 0.0:
                continue
            Fb = raw[cfg][A]["Fb"]
            if float(np.abs(Fb).max()) < P["bm_measurable_frac"] * launch_peak:
                n_dropped += 1
                continue
            exp_bm = (P["back_monitor_x"] - P["x_s"]) * rig.a / sanity["c_meas"]
            c_bm, _ = pulse_moments(Fb, 0, min(len(Fb) - 1, int(1.8 * exp_bm)))
            cents.append(c_bm)
        t_back_min = min(cents) if cents else None
        w = derive_windows(rig, sanity, t_back_min)
        w["n_bm_runs_dropped_unmeasurable"] = n_dropped
        windows[cfg] = w
        print(f"  {cfg}: incident={w['w_inc']}, reflected={w['w_refl']}, "
              f"wrap-arrival={w['t_wrap_probe']:.3f}, back-return="
              f"{w['t_back_return']}, bm-dropped={n_dropped}, "
              f"constructible={w['constructible']}")
        # V4 constructional assert
        assert w["w_refl"][0] == w["w_inc"][1] + 1 and w["constructible"], \
            f"V4/V3: window sanity failed for {cfg}: {w}"
    banked = json.loads(OUT["banked"].read_text())
    bank_w = banked["windows"]["GJ"]
    r1_pass = (windows["TMAG"]["w_inc"] == list(bank_w["w_inc"])
               and windows["TMAG"]["w_refl"] == list(bank_w["w_refl"]))
    print(f"  R-1 (TMAG only): derived {windows['TMAG']['w_inc']}/"
          f"{windows['TMAG']['w_refl']} vs banked {bank_w['w_inc']}/"
          f"{bank_w['w_refl']} -> {'PASS' if r1_pass else 'FAIL'}")
    if not r1_pass:
        _dump_sanity(sanity)
        banner("R-1 FAILED -> machinery investigation, RUN IS VOID (V1).")
        sys.exit(2)
    if windows["TELEC"]["w_refl"] != windows["TMAG"]["w_refl"]:
        print(f"  NOTE: TELEC close differs from TMAG "
              f"({windows['TELEC']['w_refl']} vs {windows['TMAG']['w_refl']}); "
              f"E11 sets adjust per prereg R-1 clause (recorded as deviation)")

    banner("CS-5 NULL CALIBRATION (A=0 through the full pipeline)")
    eps_list = {}
    for cfg in CONFIGS:
        r0 = raw[cfg][0.0]
        ex = extract_gamma(r0["F"], r0["B"], tuple(windows[cfg]["w_inc"]),
                           tuple(windows[cfg]["w_refl"]))
        eps_list[cfg] = abs(ex["gamma"])
        print(f"  {cfg}: |Gamma(0)| = {abs(ex['gamma']):.5f} "
              f"(|G|_E = {ex['gammaE']:.5f}, tau*={ex['tau']}) gate < {P['cs5_cap']}")
    eps0 = max(eps_list.values())
    cs5_pass = all(e < P["cs5_cap"] for e in eps_list.values())
    theta = max(3 * eps0, P["theta_floor"])
    delta = max(eps0, P["delta_floor"])
    sanity.update(CS5_eps=eps_list, CS5_eps0=eps0, CS5_pass=cs5_pass,
                  theta=theta, delta=delta, R1_pass=bool(r1_pass))
    print(f"  eps0 = {eps0:.5f}; theta = {theta:.5f}; delta = {delta:.5f} "
          f"-> {'PASS' if cs5_pass else 'FAIL'}")
    _dump_sanity(sanity)
    if not cs5_pass:
        banner("CS-5 FAILED -> RUN IS VOID (V1). STOPPING.")
        sys.exit(2)

    banner("EXTRACTION + WINDOW-CONVERGENCE RECEIPTS [4.4]")
    table, sweep, tails, stab = {}, {}, {}, {}
    for cfg in CONFIGS:
        w_inc = tuple(windows[cfg]["w_inc"])
        close_f = windows[cfg]["w_refl"][1]
        t_open = windows[cfg]["w_refl"][0]
        rows, n_unrel_inf = [], 0
        sweep[cfg], tails[cfg] = {}, {}
        closes = sorted(set(list(P["sweep_closes_base"]) + [close_f]))
        for A in P["A_grid"]:
            r = raw[cfg][A]
            ex = extract_gamma(r["F"], r["B"], w_inc, (t_open, close_f))
            disc = abs(abs(ex["gamma"]) - ex["gammaE"]) / max(ex["gammaE"], theta)
            unreliable = bool(disc > P["discord_tol"])
            informative = bool(max(abs(ex["gamma"]), ex["gammaE"]) > theta)
            n_unrel_inf += int(unreliable and informative)
            e_refl = float((r["B"][t_open:close_f + 1] ** 2).sum())
            t0, t1 = close_f + 1, close_f + P["tail_span"]
            e_tail = float((r["B"][t0:min(t1, len(r["B"]) - 1) + 1] ** 2).sum())
            tail_frac = e_tail / e_refl if e_refl > 0 else 0.0
            rows.append(dict(A=A, gamma=ex["gamma"], gammaE=ex["gammaE"],
                             tau=ex["tau"], discordance=disc,
                             tmpl_contained=ex["tmpl_contained"],
                             tail_frac=tail_frac,
                             informative=informative,
                             unreliable=unreliable, valid=not unreliable))
            sweep[cfg][str(A)] = {
                str(c): extract_gamma(r["F"], r["B"], w_inc, (t_open, c))["gamma"]
                for c in closes}
            print(f"  {cfg} A={A:<7} G={ex['gamma']:+.5f} |G|_E={ex['gammaE']:.5f} "
                  f"tau*={str(ex['tau']):>4} disc={disc:.3f} tail={tail_frac:.3f} "
                  f"{'UNRELIABLE' if unreliable else ''}"
                  f"{'' if ex['tmpl_contained'] else ' TMPL-CLIPPED'}")
        table[cfg] = rows
        table[cfg + "_invalid_extraction"] = n_unrel_inf > P["discord_max_pts"]
        print(f"  {cfg}: informative-unreliable tally = {n_unrel_inf} "
              f"(INVALID if > {P['discord_max_pts']}) -> invalid="
              f"{table[cfg + '_invalid_extraction']}")
        # Stability rules S1-S3 on this config
        stab_closes = sorted(set(list(P["stability_closes"]) + [close_f]))
        cls_by_close = {}
        for c in stab_closes:
            rows_c = []
            for A in P["A_grid"]:
                r = raw[cfg][A]
                ex = extract_gamma(r["F"], r["B"], w_inc, (t_open, c))
                d = abs(abs(ex["gamma"]) - ex["gammaE"]) / max(ex["gammaE"], theta)
                rows_c.append(dict(A=A, gamma=ex["gamma"], valid=bool(d <= P["discord_tol"])))
            cc = classify(rows_c, theta, delta, P)
            cls_by_close[c] = {"SIGN_top": cc["SIGN_top"],
                               "n_crossings": len(cc["crossings"])}
        s1 = (len({str(v["SIGN_top"]) for v in cls_by_close.values()}) > 1
              or len({v["n_crossings"] for v in cls_by_close.values()}) > 1)
        valid_rows = [r for r in rows if r["valid"]]
        ws_pts = [r["A"] for r in valid_rows
                  if abs(sweep[cfg][str(r["A"])][str(close_f)]
                         - sweep[cfg][str(r["A"])]["70"]) > delta]
        ts_pts = [r["A"] for r in valid_rows if r["tail_frac"] > P["tail_frac"]]
        med_frac = float(np.median(
            [abs(sweep[cfg][str(r["A"])][str(close_f)]
                 - sweep[cfg][str(r["A"])]["70"])
             / max(abs(sweep[cfg][str(r["A"])][str(close_f)]), theta)
             for r in valid_rows])) if valid_rows else 0.0
        s3 = (len(ts_pts) >= P["trunc_count"]) or (med_frac > P["stab_median_frac"])
        stab[cfg] = dict(classifiers_by_close=cls_by_close, S1_fired=bool(s1),
                         window_sensitive_pts=ws_pts, truncation_suspect_pts=ts_pts,
                         median_delta_fraction=med_frac, S3_fired=bool(s3))
        print(f"  {cfg} stability: S1={s1}, WINDOW-SENSITIVE={ws_pts}, "
              f"TRUNCATION-SUSPECT={ts_pts}, median-frac={med_frac:.4f}, S3={s3}")
        if s3:
            probe_close = int(math.floor(windows[cfg]["t_wrap_probe"] - 1e-9))
            stab[cfg]["convergence_probe_close"] = probe_close
            stab[cfg]["convergence_probe"] = {
                str(A): extract_gamma(raw[cfg][A]["F"], raw[cfg][A]["B"],
                                      w_inc, (t_open, probe_close))["gamma"]
                for A in P["A_grid"]}
            print(f"  {cfg} S3 fired -> convergence probe at close {probe_close} "
                  f"(unguarded, NON-adjudicating) recorded")

    banner("CLASSIFIERS + R-2/R-3 + FROZEN VERDICTS [6.2/6.3/6.4]")
    cls = {}
    cls["TMAG"] = classify(table["TMAG"], theta, delta, P)
    cls["TELEC"] = classify(table["TELEC"], theta, delta, P, want_shape=True)
    for cfg in CONFIGS:
        print(f"  {cfg} classifiers: { {k: v for k, v in cls[cfg].items() if k != 'delta_sign_profile'} }")
        print(f"  {cfg} delta-sign profile: {cls[cfg]['delta_sign_profile']}")

    # R-2: reproduction vs the banked G-J matched-filter locus
    bank_rows = {r["A"]: r for r in banked["table"]["GJ"]}
    r2_devs = {A: abs(r["gamma"] - bank_rows[A]["gamma"])
               for A, r in ((row["A"], row) for row in table["TMAG"])}
    r2_max = max(r2_devs.values())
    r2_pass = r2_max < P["r2_tol"]
    print(f"  R-2: max |G_TMAG - G_GJ,banked| = {r2_max:.3e} "
          f"(gate < {P['r2_tol']:.0e}) -> {'PASS' if r2_pass else 'FAIL'}")
    # R-3: classifier concordance (this run's flags) vs banked
    bank_cls = banked["classifiers"]["GJ"]
    flag_diffs = [A for A, row in ((r["A"], r) for r in table["TMAG"])
                  if row["valid"] != bank_rows[A]["valid"]]
    tmag_win_stable = not (stab["TMAG"]["S1_fired"] or stab["TMAG"]["S3_fired"])
    r3_checks = dict(
        sign_top=(cls["TMAG"]["SIGN_top"] == bank_cls["SIGN_top"]),
        crossings=(len(cls["TMAG"]["crossings"]) == len(bank_cls["crossings"])),
        monotone_dir=(cls["TMAG"]["monotone_dir"] == bank_cls["monotone_dir"]),
        window_stable=tmag_win_stable,
        sign_top_defined=(cls["TMAG"]["SIGN_top"] is not None),
    )
    r3_pass = all(r3_checks.values())
    print(f"  R-3: {r3_checks} -> {'PASS' if r3_pass else 'FAIL'}; "
          f"per-point flag diffs vs banked (reported, not gated): {flag_diffs}")
    tmag_outcome = "REPRODUCED" if (r1_pass and r2_pass and r3_pass) else "R-FAIL"
    if tmag_outcome == "R-FAIL":
        _dump_sanity(sanity)
        banner("T-MAG R-FAIL -> machinery defect -> RUN IS VOID (V1). STOPPING.")
        # still persist what we have for the investigation
        _persist(raw, windows, sanity, table, sweep, cls, stab, {}, {},
                 tmag_outcome, ("VOID", "R-FAIL"), r2_devs, flag_diffs)
        sys.exit(2)

    mirror = mirror_diag(table["TMAG"], table["TELEC"], theta, P,
                         table["TMAG_invalid_extraction"],
                         table["TELEC_invalid_extraction"])
    print(f"  MIRROR: {mirror if mirror.get('status') != 'computed' else {k: mirror[k] for k in ('n_points', 'max', 'median')}}")

    v = telec_verdict(cls["TELEC"], table["TELEC_invalid_extraction"],
                      stab["TELEC"]["S1_fired"], stab["TELEC"]["S3_fired"])
    print(f"  VERDICT T-MAG: {tmag_outcome} (reproduction gate; machinery receipt only)")
    print(f"  VERDICT T-ELEC: {v[0]}  ({v[1]})")

    _persist(raw, windows, sanity, table, sweep, cls, stab, mirror,
             {"TMAG": tmag_outcome, "TELEC": list(v)}, tmag_outcome, v,
             r2_devs, flag_diffs)
    make_figure(table, theta, windows)
    return 0


def _np_default(o):
    if isinstance(o, np.bool_):
        return bool(o)
    if isinstance(o, np.integer):
        return int(o)
    if isinstance(o, np.floating):
        return float(o)
    if isinstance(o, np.ndarray):
        return o.tolist()
    raise TypeError(f"not JSON-serializable: {type(o)}")


def _jsonable(d):
    return json.loads(json.dumps(d, default=_np_default))


def _dump_sanity(sanity):
    s = {k: v for k, v in sanity.items() if k != "cold"}
    OUT["rawdir"].mkdir(parents=True, exist_ok=True)
    (OUT["rawdir"] / "cold_sanity.json").write_text(
        json.dumps(s, indent=1, default=_np_default))


def _persist(raw, windows, sanity, table, sweep, cls, stab, mirror, verdicts,
             tmag_outcome, telec_v, r2_devs, flag_diffs):
    for cfg in CONFIGS:
        out = {}
        for A in P["A_grid"]:
            r = raw[cfg][A]
            out[str(A)] = dict(F=r["F"].tolist(), B=r["B"].tolist(),
                               Fb=r["Fb"].tolist(),
                               sent_fwd=r["sent_fwd"].tolist(),
                               sent_bwd=r["sent_bwd"].tolist(),
                               c1_leak=r["c1_leak"].tolist(),
                               ey_drift=r["ey_drift"],
                               sha_match=bool(r["sha_match"]),
                               n_graded_bonds=r["n_graded_bonds"],
                               max_c1_leak=r["max_c1_leak"])
        (OUT["rawdir"] / f"raw_{cfg}.json").write_text(json.dumps(out))
    summary = dict(
        params={k: (list(v) if isinstance(v, tuple) else v) for k, v in P.items()},
        sanity={k: v for k, v in sanity.items() if k != "cold"},
        windows=windows,
        table={c: table[c] for c in CONFIGS},
        invalid_extraction={c: bool(table[c + "_invalid_extraction"])
                            for c in CONFIGS},
        classifiers={c: _jsonable(cls[c]) for c in CONFIGS} if cls else {},
        window_sweep=sweep,
        stability=_jsonable(stab),
        mirror=_jsonable(mirror),
        r2_max_dev=max(r2_devs.values()) if r2_devs else None,
        r2_devs={str(k): v for k, v in r2_devs.items()},
        r3_flag_diffs=flag_diffs,
        verdicts={"TMAG": tmag_outcome, "TELEC": list(telec_v)},
    )
    OUT["results"].write_text(json.dumps(summary, indent=1, default=_np_default))
    print(f"\nWrote {OUT['rawdir']}/raw_*.json and {OUT['results']}")


def make_figure(table, theta, windows):
    """Overlay: measured Gamma(A) per loading on the four SS2.2 forms.
    White house style via ave.viz.style; Okabe-Ito; no title; legend outside."""
    import matplotlib.pyplot as plt

    from ave.viz import ave_chart, style

    style.apply("print")
    fig, ax = plt.subplots(figsize=style.figsize("single"))
    Ad = np.linspace(0.0, 0.999, 400)
    core = ave_chart.gamma_of_A(Ad, "core").real
    ax.plot(Ad, core, color=style.COLORS["data"], lw=1.0,
            label="two-port MAG: $(\\sqrt{S}-1)/(\\sqrt{S}+1)$")
    ax.plot(Ad, -core, color=style.COLORS["data"], lw=1.0, ls="--",
            label="two-port ELEC (mirror): $(1-\\sqrt{S})/(1+\\sqrt{S})$")
    ax.plot(Ad, ave_chart.gamma_of_A(Ad, "J").real, color="#E69F00", lw=1.0,
            ls=":", label="MAG-VERTEX (Form-J algebra)")
    ax.plot(Ad, ave_chart.gamma_of_A(Ad, "B").real, color="#56B4E9", lw=1.0,
            ls=":", label="ELEC-VERTEX (Form-B algebra)")
    ax.axvline(ave_chart.A_MATCHED_B, color=style.COLORS["muted"], lw=0.7,
               ls=":", label="$A^*=\\sqrt{15}/4$ (report-against)")
    ax.axhline(0.0, color=style.COLORS["muted"], lw=0.5)
    marks = {"TMAG": ("o", "#0072B2", "measured T-MAG (reproduction config)"),
             "TELEC": ("s", "#D55E00", "measured T-ELEC (new measurement)")}
    for cfg, (m, col, lab) in marks.items():
        rows = table[cfg]
        Av = [r["A"] for r in rows if r["valid"]]
        Gv = [r["gamma"] for r in rows if r["valid"]]
        Au = [r["A"] for r in rows if not r["valid"]]
        Gu = [r["gamma"] for r in rows if not r["valid"]]
        ax.plot(Av, Gv, m, color=col, ms=5, ls="none", label=lab)
        if Au:
            ax.plot(Au, Gu, m, mfc="none", mec=col, ms=5, ls="none",
                    label=lab + " [unreliable pt]")
    ax.set_xlabel(style.axis_label("Grading amplitude", "A", ""))
    ax.set_ylabel(style.axis_label("Reflection coefficient", "\\Gamma", ""))
    ax.set_xlim(0, 1.0)
    ax.set_ylim(-1.05, 1.05)
    style.legend(ax, where="right", fontsize=6.5)
    OUT["figstem"].parent.mkdir(parents=True, exist_ok=True)
    paths = style.save(fig, OUT["figstem"])
    print(f"Figure written: {[str(x) for x in paths]}")


if __name__ == "__main__":
    log_path = OUT["rawdir"] / "run_log.txt"
    OUT["rawdir"].mkdir(parents=True, exist_ok=True)

    class Tee:
        def __init__(self, *streams):
            self.streams = streams

        def write(self, data):
            for s in self.streams:
                s.write(data)

        def flush(self):
            for s in self.streams:
                s.flush()

    with open(log_path, "w") as lf:
        sys.stdout = Tee(sys.__stdout__, lf)
        try:
            rc = main()
        finally:
            sys.stdout = sys.__stdout__
    sys.exit(rc or 0)
