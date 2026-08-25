#!/usr/bin/env python
"""Graded-region pulse reflection Gamma(A) on the srs scalar TLM engine.

Executes research/2026-08-24_engine-gamma-meanstest_prereg_FROZEN.md verbatim
(`prereg_FROZEN.md` in the run workspace). Driver-script honesty: every
parameter actually used is printed at run start; no silent defaults.

Engine: READ-ONLY import from AVE-Core src (verified byte-identical to the
avechart worktree's copies of chiral_lattice.py / chiral_lattice_dynamics.py /
viz/style.py). Chart forms: loaded by file path from the avechart worktree
(branch infra/2026-08-24-ave-chart-instrument).

Graded extension (prereg 4.1, NEW code here, engine untouched):
  per-port admittances Y_p  =>  V = 2*(sum_j Y_j V_j^inc)/(sum_k Y_k)
  =>  S_ij = 2*Y_j/(sum_k Y_k) - delta_ij   (per node)
applied as V_ref[u] = S_u @ V_inc[u]; CONNECT untouched. Lossless under
E_Y = sum_{u,p} Y_{b(u,p)} V_inc[u,p]^2 (gated V2, not assumed).

POST-VERIFY AMENDMENT (2026-08-24, after the 3-lens adversarial verify)
----------------------------------------------------------------------
The FROZEN path below (cold gate -> 48 graded runs -> windows -> extraction ->
classifiers -> verdicts) is UNCHANGED: same parameters, same windows, same
numbers, same verdicts.  Added, strictly downstream of the frozen verdicts and
never feeding them:

  * `post_verify_amendment()` — re-extracts Gamma over a SWEEP of reflected-
    window closes from the already-computed raw series (no new lattice runs),
    banking (a) the converged G-T locus at the extended close AMEND_CLOSE, the
    window-truncation repair of the vnum MAJOR finding, (b) the G-B
    matched-filter sign's window-dependence, (c) post-window tail energies as
    the convergence receipt, (d) the corrected slab-back close bounds.
  * `make_figure()` additionally plots the converged G-T points.
  * Path resolution (engine src / chart module / outputs) now prefers the
    ENCLOSING CHECKOUT so the landed artifact re-runs in place; the run of
    record used the run-workspace fallbacks (printed at run start either way).
    The three engine files were verified byte-identical (cmp) between the two
    checkouts at run time, so this is a path change, not an engine change.

The per-run V3 sentinel gate that the result doc DECLARED is implemented in the
companion script `engine_gamma_meanstest_check_sentinels.py` (beside this file;
`check_sentinels.py` in the run workspace), not here: it consumes the shipped
sentinel series and is re-runnable without a lattice run.
"""
from __future__ import annotations

import hashlib
import json
import math
import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent

# Run-of-record fallbacks (the run workspace this driver was executed from).
ENGINE_SRC_RUN = Path("/Users/grantlindblom/AVE-staging/AVE-Core/src")
AVECHART_FILE_RUN = Path(
    "/private/tmp/claude-501/-Users-grantlindblom-AVE-staging/"
    "91b867e5-bc0e-42d5-9d27-3ec2573c4b62/scratchpad/avechart/src/ave/viz/ave_chart.py"
)


def _resolve_engine_src() -> Path:
    """Enclosing checkout's src/ if this file sits in one, else the run path."""
    for parent in (HERE, *HERE.parents):
        if (parent / "src" / "ave" / "core" / "chiral_lattice.py").is_file():
            return parent / "src"
    return ENGINE_SRC_RUN


def _resolve_chart_file() -> Path:
    """In-tree ave_chart.py (branch infra/2026-08-24-ave-chart-instrument)."""
    cand = _resolve_engine_src() / "ave" / "viz" / "ave_chart.py"
    return cand if cand.is_file() else AVECHART_FILE_RUN


def _resolve_outputs() -> dict:
    """Landed layout (research/drivers/...) vs run-workspace layout."""
    if HERE.name == "drivers" and HERE.parent.name == "research":
        repo = HERE.parent.parent
        return dict(
            results=HERE / "engine_gamma_meanstest_results.json",
            rawdir=HERE / "data" / "engine_gamma_meanstest",
            figstem=(repo / "research" / "figures"
                     / "2026-08-24-engine-gamma-meanstest" / "fig1_gamma_overlay"),
        )
    return dict(results=HERE / "data" / "results.json", rawdir=HERE / "data",
                figstem=HERE / "gamma_overlay")


ENGINE_SRC = _resolve_engine_src()
AVECHART_FILE = _resolve_chart_file()
OUT = _resolve_outputs()
sys.path.insert(0, str(ENGINE_SRC))

from ave.core import chiral_lattice as cl  # noqa: E402
from ave.core import chiral_lattice_dynamics as cld  # noqa: E402
from ave.viz import style  # noqa: E402


def load_ave_chart():
    """Load ave_chart.py by file path (in-tree if present, else run path)."""
    import importlib.util

    spec = importlib.util.spec_from_file_location("ave_chart_worktree", AVECHART_FILE)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


# ---------------------------------------------------------------------------
# FROZEN parameters (prereg sections in brackets); ALL printed at run start
# ---------------------------------------------------------------------------
P = dict(
    # DEVIATION D1 (recorded, within E1's own latitude "any L >= 12 satisfying
    # the V3 timing budget is acceptable, recorded if changed"): L=16 does NOT
    # satisfy the V3 timing budget — the measured ~9%-amplitude backward-launch
    # residual wraps the 3-cell margin (12-cell path, arrival t~48-68 at the
    # probe) and lands INSIDE the reflected window (echo centroid t~49), making
    # the window non-constructible. L=24 (wrap margin 11 cells) moves the wrap
    # contaminant to t~98, cleanly after the echo.
    L=24,                      # [4.1 E1, deviation D1 above] cells per side
    enantiomorph="right",      # [E8]
    # geometry, units of a_cell [4.3 E2]: x_s = x_I-7, x_p = x_I-3, x_B = x_I+6
    x_s=2.0, x_p=6.0, x_I=9.0, x_B=15.0, W_slab=6.0, N_taper=3.0,
    wrap_margin_cells=11.0,    # 24 - (15 - 2) = 11 >= 3 [4.3]
    sigma_x_cells=1.5,         # [E3] baseband Gaussian, directional weighting
    back_monitor_x=15.5,       # DRIVER-DECLARED (deviation D10): transmitted-
                               # pulse monitor plane (cells), half a cell past
                               # the slab back x_B=15 — this is the plane that
                               # operationalizes prereg 4.4's "measured graded
                               # transit times" for the window close
    sentinel_x=19.5,           # wrap-margin plane opposite the source (cells);
                               # mid-margin, 6.5 cells min-image from the source
                               # so the launch tail (~8e-5) cannot false-trigger
    sentinel_thresh=0.01,      # DRIVER-DECLARED: contaminant front = 1% of the
                               # unit launch envelope (actual peak ~0.705)
    A_grid=[0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.85,
            0.9, 0.925, 0.95, 0.9682, 0.98, 0.99],  # [E4]
    T_cold=200, T_run=170, hard_cap=6000,           # [E5]
    guard_sigmas=2.0,          # [E6] window guard margin = 2*sigma_t per edge
    discord_tol=0.2, discord_max_pts=4,             # [E6]
    cs2_tol=0.02, cs2_band_dev=0.05, cs2_band_frac=0.95, cs3_tol=0.05,  # [E7]
    cs1_drift=1e-10, cs4_dev=1e-12, v2_drift=1e-8, cs5_cap=0.02,        # [E7]
    theta_floor=0.05, delta_floor=0.01,             # [E7] theta=max(3eps0,.05)
    taper_factor=0.5, taper_band=(0.5, 0.9),        # [E7]
    dispersion_axis=0,         # DRIVER-DECLARED (deviation D9): dispersion
                               # measured along the propagation axis x; the
                               # engine default is axis=2 (z)
    m_values=(1, 2, 3, 4), n_steps_disp=800,        # [5 CS-2]
)

# POST-VERIFY AMENDMENT parameters — NOT part of P (the frozen block), and
# never consumed by the frozen extraction/classifier/verdict path.  They
# parameterize the downstream convergence re-extraction only.
AMEND = dict(
    # Extended reflected-window close for the G-T convergence re-extraction.
    # 85 is the largest close still strictly BEFORE the earliest projected
    # contaminant arrival (87.78 steps, all 48 runs -> check_sentinels.py); it
    # is NOT guard-protected (the 2*sigma_t = 9.61-step guard needs close<=78),
    # which is exactly why it is a convergence PROBE and not a re-adjudication:
    # the frozen extraction keeps the guarded close.
    close_extended=85,
    # Window-close sweep: 60/64/70 (truncating), 78 (frozen), 85 (converged),
    # 95 (past the 87.78 contaminant front -> contaminated, shown to be so).
    close_sweep=(60, 64, 70, 78, 85, 95),
    # Post-window tail-energy diagnostic ranges (inclusive step bounds).
    tail_frozen=(79, 86), tail_extended=(86, 87),
)


def banner(msg):
    print("\n" + "=" * 78 + f"\n{msg}\n" + "=" * 78, flush=True)


def kernel_S(A):
    """Axiom-4 kernel S(A) = sqrt(1 - A^2), exact/unclipped on [0,1]."""
    A = np.asarray(A, dtype=float)
    return np.sqrt(np.clip(1.0 - A * A, 0.0, 1.0))


def z_of_A(A):
    """Canonical impedance map z = sqrt(S(A)) [4.2, shared with chart forms]."""
    return np.sqrt(kernel_S(A))


# ---------------------------------------------------------------------------
# Net + bond bookkeeping
# ---------------------------------------------------------------------------
class Rig:
    """Net + bond tables + geometry index sets, all in CELL units for planes."""

    def __init__(self, p):
        self.p = p
        self.net = cl.build_srs_net(L=p["L"], enantiomorph=p["enantiomorph"])
        net = self.net
        self.a = net.a_cell                       # 2*sqrt(2); bond length = 1.0
        self.N = net.n_nodes
        self.deg = net.degree
        self.conn = net.connect_index()
        self.box_cells = net.box / self.a         # = L
        # node x in cell units
        self.xu = net.pos[:, 0] / self.a
        # bonds: canonical (min,max) pairs; per-directed-port bond id
        bond_id = {}
        b_x0, b_dx = [], []                       # unwrapped endpoint / span (cells)
        self.port_bond = np.zeros((self.N, self.deg), dtype=np.int64)
        for u in range(self.N):
            for pp, v in enumerate(net.neighbors[u]):
                key = (min(u, v), max(u, v))
                if key not in bond_id:
                    bond_id[key] = len(b_x0)
                    u0, u1 = key
                    dx = net.pos[u1, 0] - net.pos[u0, 0]
                    dx -= net.box * np.round(dx / net.box)   # minimum image
                    b_x0.append(net.pos[u0, 0] / self.a)
                    b_dx.append(dx / self.a)
                self.port_bond[u, pp] = bond_id[key]
        self.bonds = np.array(sorted(bond_id, key=bond_id.get), dtype=np.int64)
        self.b_x0 = np.array(b_x0)
        self.b_dx = np.array(b_dx)
        self.b_mid = np.mod(self.b_x0 + 0.5 * self.b_dx, self.box_cells)
        self.nb = len(self.bonds)
        # Directional port weights for a +x-propagating launch.
        # DEVIATION D2 (recorded): the prereg 4.3 formula max(0, +x.b_hat)
        # weights the ports whose bond vector points +x — but V_inc[u,p] is the
        # wave ARRIVING at u along bond p, so that literal weighting launches a
        # -x-traveling pulse (verified empirically: the pulse arrived at the
        # probe via the wrap path on the backward ports). The frozen GEOMETRY
        # (source at x_I-7 firing INTO the interface, 4.3) requires the
        # +x-propagating pulse, i.e. weight = max(0, -x.b_hat): incident from
        # the -x-side neighbours = traveling +x. Geometry controls; sign fixed.
        self.wport = np.zeros((self.N, self.deg))
        for u in range(self.N):
            for pp in range(self.deg):
                self.wport[u, pp] = max(0.0, -net.bond_unit[u][pp][0])
        # probe / monitor bond port index sets
        self.idx_probe_fwd, self.idx_probe_bwd = self._crossing_ports(p["x_p"])
        self.idx_bm_fwd, _ = self._crossing_ports(p["back_monitor_x"])
        # wrap sentinel: direction-resolved port sets on bonds crossing the
        # mid-margin plane opposite the source [V3]
        self.idx_sent_fwd, self.idx_sent_bwd = self._crossing_ports(p["sentinel_x"])

    def _crossing_ports(self, plane):
        """Flat V-indices for (u_plus, port from u_minus) [forward] and
        (u_minus, port from u_plus) [backward] over bonds crossing `plane`."""
        net = self.net
        fwd, bwd = [], []
        x0, x1 = self.b_x0, self.b_x0 + self.b_dx
        crossing = np.where((x0 - plane) * (x1 - plane) < 0.0)[0]
        for bi in crossing:
            u0, u1 = self.bonds[bi]
            # source-side endpoint = smaller unwrapped x
            if x0[bi] < x1[bi]:
                um, up = u0, u1
            else:
                um, up = u1, u0
            p_up = net.neighbors[up].index(um)    # port on u_plus facing u_minus
            p_um = net.neighbors[um].index(up)    # port on u_minus facing u_plus
            fwd.append(up * self.deg + p_up)
            bwd.append(um * self.deg + p_um)
        return np.array(fwd, dtype=np.int64), np.array(bwd, dtype=np.int64)

    # -- imposed grading [4.3] ------------------------------------------------
    def a_field(self, config, A):
        """Per-bond A_b for config in {GJ, GB, GT} at grid amplitude A."""
        p = self.p
        Ab = np.zeros(self.nb)
        x0, x1 = self.b_x0, self.b_x0 + self.b_dx
        lo, hi = np.minimum(x0, x1), np.maximum(x0, x1)
        if config == "GJ":
            inside = (lo > p["x_I"]) & (hi < p["x_B"])
            Ab[inside] = A
        elif config == "GB":
            crossing = (x0 - p["x_I"]) * (x1 - p["x_I"]) < 0.0
            Ab[crossing] = A
        elif config == "GT":
            xm = self.b_mid
            r = np.clip((xm - p["x_I"]) / p["N_taper"], 0.0, 1.0)
            r[xm >= p["x_B"]] = 0.0
            r[xm <= p["x_I"]] = 0.0
            Ab = A * r
        else:
            raise ValueError(config)
        return Ab

    # -- graded step machinery [4.1] -----------------------------------------
    def build_scatter(self, Ab):
        """Per-node scatter coefficients from the per-bond grading.

        Returns (a_nodes, Yp, sha) with S_ij = a_j - delta_ij, a_j = 2 Y_j/sum Y.
        sha = SHA-256 of the stacked explicit S_u array [4.2 / V2].
        """
        Yb = 1.0 / z_of_A(Ab)                     # Y_b = Y0/z_b, Y0 = 1
        Yp = Yb[self.port_bond]                   # (N, 3): both end-ports share Y_b
        a_nodes = 2.0 * Yp / Yp.sum(axis=1, keepdims=True)
        S_nodes = a_nodes[:, None, :] - np.eye(self.deg)[None, :, :]
        sha = hashlib.sha256(np.ascontiguousarray(S_nodes).tobytes()).hexdigest()
        return a_nodes, Yp, sha

    def step_graded(self, V, a_nodes):
        """V_ref[u] = S_u @ V_inc[u] with S_ij = a_j - delta_ij, then CONNECT."""
        w = (a_nodes * V).sum(axis=1)
        V_ref = w[:, None] - V
        V_new = np.zeros_like(V)
        V_new.flat[self.conn[1]] = V_ref.flat[self.conn[0]]
        return V_new

    def launch(self):
        """Baseband Gaussian plane pulse, directionally weighted [4.3 E3]."""
        p = self.p
        g = np.exp(-((self.xu - p["x_s"]) ** 2) / (2.0 * p["sigma_x_cells"] ** 2))
        return g[:, None] * self.wport

    def run(self, a_nodes, Yp, T):
        """Time-step T steps from the launch; record all observables per step."""
        V = self.launch()
        EY0 = float((Yp * V * V).sum())
        F = np.zeros(T + 1)
        B = np.zeros(T + 1)
        Fb = np.zeros(T + 1)
        s_fwd = np.zeros(T + 1)
        s_bwd = np.zeros(T + 1)
        eydrift = 0.0
        for t in range(1, T + 1):
            V = self.step_graded(V, a_nodes)
            F[t] = V.flat[self.idx_probe_fwd].sum()
            B[t] = V.flat[self.idx_probe_bwd].sum()
            Fb[t] = V.flat[self.idx_bm_fwd].sum()
            s_fwd[t] = np.abs(V.flat[self.idx_sent_fwd]).max()
            s_bwd[t] = np.abs(V.flat[self.idx_sent_bwd]).max()
            eydrift = max(eydrift, abs((Yp * V * V).sum() - EY0) / EY0)
        return dict(F=F, B=B, Fb=Fb, sent_fwd=s_fwd, sent_bwd=s_bwd,
                    ey_drift=eydrift)


# ---------------------------------------------------------------------------
# Pulse moments, windows, extraction [4.4]
# ---------------------------------------------------------------------------
def pulse_moments(F, t_lo=0, t_hi=None):
    """(centroid, sigma_t) of F^2 within [t_lo, t_hi], iterated once."""
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
    """Matched-filter signed Gamma + unsigned energy cross-check [4.4].

    w_inc, w_refl = (start, stop) inclusive step windows.
    Gamma_meas = sum_{t in refl} B(t) T(t - tau*) / sum_{t in refl} T(t-tau*)^2,
    T = F restricted to the incident window, tau* = argmax |xcorr| over lags
    whose shifted template carries >= 25% of its energy inside w_refl.

    TWO OPERATIONALIZATIONS of the prereg 4.4 estimator live here, both logged
    as deviation D7 in the result doc (they were disclosed in this docstring
    but not in the deviation register until the post-verify repair):
      (a) the 25%-of-template-energy-in-window lag admissibility cutoff, which
          regularizes den -> 0 at extreme lags (line `if den < 0.25*E_tmpl`);
      (b) the denominator is the shifted template's energy RESTRICTED to the
          reflected window (`den = (sh[mask]**2).sum()`), not the full template
          energy E_tmpl.  For every reported valid point the locked-lag template
          lies fully inside the window, so (b) is numerically inert there; for
          near-edge lags it can inflate |Gamma| by up to 1/0.25 = 4x, which is
          what the (a) floor caps.
    """
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
        return dict(gamma=0.0, gammaE=0.0, tau=None, EF=E_tmpl, EB=0.0)
    num, den, tau = best
    E_F = float((F[i0:i1 + 1] ** 2).sum())
    E_B = float((B[r0:r1 + 1] ** 2).sum())
    return dict(gamma=num / den, gammaE=math.sqrt(E_B / E_F), tau=tau,
                EF=E_F, EB=E_B)


# ---------------------------------------------------------------------------
# Cold sanity gate [5] — the run is VOID if any CS fails
# ---------------------------------------------------------------------------
def cold_sanity(rig):
    p = rig.p
    out = {}
    banner("COLD SANITY GATE (prereg 5) — run first; VOID on any failure")

    # CS-1: closed-system conservation, uniform scatter, the actual launch pulse
    S_uni = cl.scatter_matrix(rig.deg)
    V = rig.launch()
    E0 = cl.lattice_energy(V)
    drift = 0.0
    traj_uni = []
    for _ in range(200):
        V = cl.scalar_tlm_step(rig.net, V, S_uni, rig.conn)
        traj_uni.append(V.copy())
        drift = max(drift, abs(cl.lattice_energy(V) - E0) / E0)
    out["CS1_drift"] = drift
    out["CS1_pass"] = drift < p["cs1_drift"]
    print(f"CS-1 energy drift (uniform, 200 steps): {drift:.3e} "
          f"(gate < {p['cs1_drift']:.0e}) -> {'PASS' if out['CS1_pass'] else 'FAIL'}")

    # CS-4: per-node-S machinery, all bonds cold, vs uniform trajectory
    a_nodes, Yp, _ = rig.build_scatter(np.zeros(rig.nb))
    V = rig.launch()
    dev = 0.0
    for t in range(200):
        V = rig.step_graded(V, a_nodes)
        dev = max(dev, float(np.abs(V - traj_uni[t]).max()))
    out["CS4_dev"] = dev
    out["CS4_pass"] = dev <= p["cs4_dev"]
    print(f"CS-4 graded-path regression (all-cold, 200 steps): max|dV| = {dev:.3e} "
          f"(gate <= {p['cs4_dev']:.0e}) -> {'PASS' if out['CS4_pass'] else 'FAIL'}")

    # CS-2: dispersion vs ANALYTIC_NETWORK_FACTOR + band edge.
    # DEVIATION D8: network_velocity_factor WRAPS the prereg-named
    # measure_dispersion (same measurement) and returns c0 = the k->0
    # extrapolation of a linear fit in k^2; the prereg wording is "at the
    # smallest k".  The gate is applied to the extrapolated c0; the smallest-k
    # reading is the shipped CS2_c[0] and is recomputed against the 2% gate in
    # post_verify_amendment() (both pass) — no second measurement is involved.
    nv = cld.network_velocity_factor(
        rig.net, axis=p["dispersion_axis"], m_values=p["m_values"],
        n_steps=p["n_steps_disp"])
    fac, target = nv["factor"], cld.ANALYTIC_NETWORK_FACTOR
    rel = abs(fac - target) / target
    ks, cs = np.array(nv["k"]), np.array(nv["c_of_k"])
    devs = np.abs(cs - nv["c0"]) / nv["c0"]
    good = devs < p["cs2_band_dev"]
    k_edge = float(ks[good].max()) if good.any() else 0.0
    sigma_x = p["sigma_x_cells"] * rig.a
    frac_analytic = math.erf(k_edge * sigma_x)     # energy ~ exp(-k^2 sigma_x^2)
    # discrete cross-check: rfft of the launched envelope binned PER CELL
    # (one bin per cell averages out the srs motif's intra-cell granularity,
    # which is lattice structure, not propagating pulse content; Nyquist
    # pi/a_cell = 1.11 comfortably above k_edge)
    nbins = p["L"]
    prof, _ = np.histogram(rig.xu * rig.a, bins=nbins,
                           range=(0, rig.net.box),
                           weights=rig.launch().sum(axis=1))
    cnt, _ = np.histogram(rig.xu * rig.a, bins=nbins, range=(0, rig.net.box))
    prof = prof / np.maximum(cnt, 1)
    Fk = np.abs(np.fft.rfft(prof - prof.mean())) ** 2
    kf = 2 * np.pi * np.fft.rfftfreq(nbins, d=rig.net.box / nbins)
    frac_disc = float(Fk[kf <= k_edge].sum() / Fk.sum()) if Fk.sum() > 0 else 0.0
    out.update(CS2_factor=fac, CS2_target=target, CS2_rel=rel,
               CS2_k=ks.tolist(), CS2_c=cs.tolist(), CS2_k_edge=k_edge,
               CS2_band_frac_analytic=frac_analytic,
               CS2_band_frac_discrete=frac_disc)
    out["CS2_pass"] = (rel < p["cs2_tol"]) and \
        (min(frac_analytic, frac_disc) >= p["cs2_band_frac"])
    print(f"CS-2 network factor: measured {fac:.6f} vs analytic {target:.6f} "
          f"(rel dev {rel:.4%}, gate < {p['cs2_tol']:.0%})")
    print(f"CS-2 c(k): {[f'{c:.4f}' for c in cs]} at k = "
          f"{[f'{k:.4f}' for k in ks]}; band edge k <= {k_edge:.4f}")
    print(f"CS-2 pulse band fraction below edge: analytic {frac_analytic:.5f}, "
          f"discrete-FFT {frac_disc:.5f} (gate >= {p['cs2_band_frac']:.2f}) "
          f"-> {'PASS' if out['CS2_pass'] else 'FAIL'}")

    # Cold reference run on the per-node machinery (defines timing + windows)
    cold = rig.run(a_nodes, Yp, p["T_cold"])
    out["cold_ey_drift"] = cold["ey_drift"]
    t_cF, sigma_t = pulse_moments(cold["F"], 0, 3 * int(
        (p["x_p"] - p["x_s"]) * rig.a / (cld.ANALYTIC_NETWORK_FACTOR)))
    out["t_cF"], out["sigma_t"] = t_cF, sigma_t

    # CS-3: time-of-flight vs CS-2 small-k velocity
    v_tof = (p["x_p"] - p["x_s"]) * rig.a / t_cF
    rel3 = abs(v_tof - nv["c0"]) / nv["c0"]
    out.update(CS3_v_tof=v_tof, CS3_c0=nv["c0"], CS3_rel=rel3)
    out["CS3_pass"] = rel3 < p["cs3_tol"]
    print(f"CS-3 TOF velocity source->probe: {v_tof:.5f} vs c0 {nv['c0']:.5f} "
          f"(rel dev {rel3:.4%}, gate < {p['cs3_tol']:.0%}) "
          f"-> {'PASS' if out['CS3_pass'] else 'FAIL'}; "
          f"t_centroid = {t_cF:.2f}, sigma_t = {sigma_t:.2f} steps")
    out["cold"] = cold
    out["c_meas"] = nv["c0"]
    return out


def derive_windows(rig, sanity, config, t_back_centroid_min=None):
    """Windows per prereg 4.4, derived from cold measurements + timing budget.

    incident  = [t_cF - 2 sigma_t, t_cF + 2 sigma_t]  (brackets the transit)
    reflected = opens at incident close; closes at the earliest of
      (a) slab-back first return front (G-J/G-T): t_back_front - guard,
          t_back_front = (t_back_centroid) - 2 sigma_t, back-face return
          centroid computed from measured transit at the back monitor,
      (b) wrap contaminant: sentinel crossing projected to the probe
          (t_cross + (box - x_p) cells / c_meas) - guard, guard = 2 sigma_t.
    """
    p = rig.p
    t_cF, s_t, c = sanity["t_cF"], sanity["sigma_t"], sanity["c_meas"]
    g = p["guard_sigmas"] * s_t
    w_inc = (max(1, int(round(t_cF - g))), int(round(t_cF + g)))
    t_open = w_inc[1] + 1
    closes = []
    # (b) wrap budget from the cold run's direction-resolved sentinel:
    #   backward (-x) crossing at x_sent continues -x, wraps to the probe over
    #     (x_sent - x_p) cells; forward (+x) crossing continues +x over
    #     (box - x_sent + x_p) cells. Earliest projected probe arrival binds.
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
    # (a) slab-back return for G-J / G-T
    t_back = None
    if config in ("GJ", "GT") and t_back_centroid_min is not None:
        # back-monitor centroid -> return to probe at cold interior speed
        t_back = t_back_centroid_min + (p["back_monitor_x"] - p["x_p"]) * rig.a / c
        closes.append((t_back - 2 * s_t) - g)
    t_close = int(math.floor(min(closes))) if closes else sanity["cold"]["F"].size - 2
    return dict(w_inc=w_inc, w_refl=(t_open, t_close),
                t_wrap_probe=t_wrap_probe, t_back_return=t_back,
                constructible=t_close > t_open)

# === PART 2 END ===

# ---------------------------------------------------------------------------
# Classifiers [6.2] and per-config verdicts [6.3]
# ---------------------------------------------------------------------------
def classify(rows, theta, delta):
    """rows: list of dicts (A, gamma, valid) sorted by A."""
    v = [r for r in rows if r["valid"]]
    out = {"n_valid": len(v)}
    if not v:
        return out
    out["SIGN_top_A"] = v[-1]["A"]
    out["SIGN_top"] = float(np.sign(v[-1]["gamma"]))
    crossings = []
    for a, b in zip(v[:-1], v[1:]):
        if (np.sign(a["gamma"]) != np.sign(b["gamma"])
                and abs(a["gamma"]) > theta and abs(b["gamma"]) > theta):
            crossings.append((a["A"], b["A"],
                              "-+" if a["gamma"] < 0 else "+-"))
    out["crossings"] = crossings
    fitpts = [r for r in v if 0.0 < r["A"] <= 0.5]
    if len(fitpts) >= 2:
        Aarr = np.array([r["A"] for r in fitpts])
        Garr = np.array([r["gamma"] for r in fitpts])
        slope, intercept = np.polyfit(Aarr, Garr, 1)
        out["floor_intercept"] = float(intercept)
        out["FLOOR"] = abs(intercept) > theta
    else:
        out["floor_intercept"] = None
        out["FLOOR"] = False
    g = [r["gamma"] for r in v]
    dec = all(g[i + 1] <= g[i] + delta for i in range(len(g) - 1))
    inc = all(g[i + 1] >= g[i] - delta for i in range(len(g) - 1))
    out["MONOTONE"] = dec or inc
    out["monotone_dir"] = "dec" if dec else ("inc" if inc else "none")
    out["pos_at_low_A"] = any(r["gamma"] > theta for r in v if r["A"] <= 0.5)
    return out


def verdict_config(config, cls, rows_by_A, theta, gj_rows=None,
                   taper_band=(0.5, 0.9), taper_factor=0.5):
    """Frozen 6.3 rules only. Returns (label, notes)."""
    notes = []
    c = cls
    none_hits = []
    if any(d == "+-" for *_, d in c.get("crossings", [])):
        none_hits.append("+-to-minus crossing")
    if len(c.get("crossings", [])) > 1:
        none_hits.append("multiple crossings")
    if c.get("SIGN_top") == 1.0 and not c.get("crossings"):
        none_hits.append("SIGN_top=+ without crossing")
    if c.get("pos_at_low_A"):
        none_hits.append("positive Gamma>theta at A<=0.5")
    if config in ("GJ", "GB") and not c.get("MONOTONE", False):
        none_hits.append("non-monotone beyond +/-delta")
    if config == "GT" and gj_rows is not None:
        for A, r in rows_by_A.items():
            if taper_band[0] <= A <= taper_band[1] and A in gj_rows:
                gj = gj_rows[A]
                if (r["valid"] and gj["valid"]
                        and abs(r["gamma"]) >= abs(gj["gamma"]) > theta):
                    none_hits.append(f"|G_GT|>=|G_GJ|>theta at A={A}")
    if none_hits:
        return "NONE", none_hits
    if config == "GJ":
        if not c.get("crossings") and c.get("SIGN_top") == -1.0 \
                and c.get("MONOTONE"):
            if c.get("FLOOR"):
                return "J-class (full, with floor)", notes
            return "J-class (floorless negative, core/J-class locus)", notes
        return "UNCLASSIFIED", ["fails J-class conjunction without a NONE tell"]
    if config == "GB":
        cr = c.get("crossings", [])
        if len(cr) == 1 and cr[0][2] == "-+" and c.get("SIGN_top") == 1.0:
            return "B-class", notes
        # not B, not NONE: shape drawn matches the J-class conjunction?
        if not cr and c.get("SIGN_top") == -1.0 and c.get("MONOTONE"):
            return "J-class-shaped (degenerate with G-J)", notes
        return "UNCLASSIFIED", ["fails B-class conjunction without a NONE tell"]
    if config == "GT":
        # TAPER-SUPPRESSED computed by caller; placeholder replaced there
        return "TAPER-PENDING", notes
    return "UNCLASSIFIED", notes


# ---------------------------------------------------------------------------
# POST-VERIFY AMENDMENT (downstream of the frozen verdicts; never feeds them)
# ---------------------------------------------------------------------------
def post_verify_amendment(rig, raw, windows, sanity, table, verd):
    """Window-convergence re-extraction over the ALREADY-COMPUTED raw series.

    Repairs the quantitative record flagged by the numerical-verify lens: the
    G-T echo is delayed (tau* ~ 48-55) and time-stretched, so the frozen
    wrap-bound close at t=78 clips its tail and biases |Gamma_GT| LOW.  Nothing
    here re-adjudicates: the frozen verdicts are passed in and re-asserted
    against the CONVERGED numbers so the a-fortiori claim is computed, not
    declared.
    """
    configs = ("GJ", "GB", "GT")
    theta, delta = sanity["theta"], sanity["delta"]
    w_inc = windows["GJ"]["w_inc"]
    c_ext = AMEND["close_extended"]
    out = {"close_extended": c_ext, "close_sweep": list(AMEND["close_sweep"]),
           "w_inc": list(w_inc)}

    # (a) window-close sweep, every config, every A
    sweep = {}
    for cfg in configs:
        sweep[cfg] = {}
        for A in P["A_grid"]:
            r = raw[cfg][A]
            sweep[cfg][str(A)] = {
                str(cl_): extract_gamma(r["F"], r["B"], w_inc, (30, cl_))["gamma"]
                for cl_ in AMEND["close_sweep"]}
    out["window_sweep"] = sweep

    # (b) converged tables at the extended close + reused frozen classifiers
    ext_rows, ext_by_A = {}, {}
    for cfg in configs:
        rows = []
        for A in P["A_grid"]:
            r = raw[cfg][A]
            ex = extract_gamma(r["F"], r["B"], w_inc, (30, c_ext))
            disc = abs(abs(ex["gamma"]) - ex["gammaE"]) / max(ex["gammaE"], theta)
            unrel = bool(disc > P["discord_tol"])
            rows.append(dict(A=A, gamma=ex["gamma"], gammaE=ex["gammaE"],
                             tau=ex["tau"], discordance=disc,
                             tmpl_span=[w_inc[0] + ex["tau"], w_inc[1] + ex["tau"]],
                             tmpl_contained=bool(w_inc[1] + ex["tau"] <= c_ext),
                             unreliable=unrel, valid=not unrel))
        ext_rows[cfg] = rows
        ext_by_A[cfg] = {r["A"]: r for r in rows}
    out["table_extended"] = ext_rows
    out["n_unreliable_extended"] = {c: sum(r["unreliable"] for r in ext_rows[c])
                                    for c in configs}
    out["invalid_extraction_extended"] = {
        c: bool(out["n_unreliable_extended"][c] > P["discord_max_pts"])
        for c in configs}
    out["classifiers_extended"] = {c: _jsonable(classify(ext_rows[c], theta, delta))
                                   for c in configs}

    # (c) taper suppression ratio, frozen window vs converged window
    frozen_by_A = {c: {r["A"]: r for r in table[c]} for c in configs}
    band, ratios = P["taper_band"], []
    for A in P["A_grid"]:
        gj = frozen_by_A["GJ"].get(A)
        if gj is None or not gj["valid"]:
            continue
        in_band = bool(band[0] <= A <= band[1] and abs(gj["gamma"]) > theta)
        gt_f, gt_x = frozen_by_A["GT"][A], ext_by_A["GT"][A]
        ratios.append(dict(A=A, gj=abs(gj["gamma"]),
                           gt_frozen=abs(gt_f["gamma"]),
                           gt_extended=abs(gt_x["gamma"]),
                           ratio_frozen=abs(gt_f["gamma"]) / abs(gj["gamma"]),
                           ratio_extended=abs(gt_x["gamma"]) / abs(gj["gamma"]),
                           in_taper_band=in_band,
                           gt_valid_frozen=bool(gt_f["valid"]),
                           gt_valid_extended=bool(gt_x["valid"])))
    out["taper_ratios"] = ratios
    inband = [r for r in ratios if r["in_taper_band"] and r["gt_valid_extended"]]
    if not inband:                      # fail loud, never silently "suppressed"
        raise RuntimeError("amendment: taper band empty — cannot recompute the "
                           "suppression criterion on converged numbers")
    out["taper_band_ratio_extended"] = [min(r["ratio_extended"] for r in inband),
                                        max(r["ratio_extended"] for r in inband)]
    out["taper_band_ratio_frozen"] = [min(r["ratio_frozen"] for r in inband),
                                      max(r["ratio_frozen"] for r in inband)]
    # the frozen criterion, recomputed on the CONVERGED numbers (a fortiori)
    out["TAPER_SUPPRESSED_extended"] = all(
        r["ratio_extended"] < P["taper_factor"] for r in inband)
    out["verdicts_frozen"] = {c: list(verd[c]) for c in configs}
    out["verdict_survival"] = {
        "GT_taper_suppressed_frozen_window": bool(
            all(r["ratio_frozen"] < P["taper_factor"] for r in inband)),
        "GT_taper_suppressed_converged_window": out["TAPER_SUPPRESSED_extended"],
        "GT_sign_top_converged": out["classifiers_extended"]["GT"].get("SIGN_top"),
        "GT_crossings_converged": out["classifiers_extended"]["GT"].get("crossings"),
        "GT_floor_converged": out["classifiers_extended"]["GT"].get("FLOOR"),
        "GT_monotone_converged": out["classifiers_extended"]["GT"].get("MONOTONE"),
        "GJ_unchanged_at_extended_close": bool(all(
            abs(ext_by_A["GJ"][A]["gamma"] - frozen_by_A["GJ"][A]["gamma"]) < 1e-9
            for A in P["A_grid"])),
    }

    # (d) convergence receipt: post-window tail energy of the reflected trace
    t0f, t1f = AMEND["tail_frozen"]
    t0x, t1x = AMEND["tail_extended"]
    tails = {}
    for cfg in ("GJ", "GT"):
        tails[cfg] = {}
        for A in P["A_grid"]:
            B = raw[cfg][A]["B"]
            e_fro = float((B[30:79] ** 2).sum())
            e_ext = float((B[30:c_ext + 1] ** 2).sum())
            tails[cfg][str(A)] = dict(
                tail_frozen_frac=float((B[t0f:t1f + 1] ** 2).sum()) / e_fro,
                tail_extended_frac=float((B[t0x:t1x + 1] ** 2).sum()) / e_ext)
    out["tail_energy"] = tails

    # (e) corrected slab-back close bounds (the doc's 93.1/92.8 narrative pair)
    s_t = sanity["sigma_t"]
    out["back_path_close_bound"] = {
        cfg: (windows[cfg]["t_back_return"] - 2 * s_t - P["guard_sigmas"] * s_t)
        for cfg in ("GJ", "GT")}

    # (e2) CS-2 read BOTH ways (deviation D8): the gated k->0 polyfit
    # extrapolation vs the prereg's literal "at the smallest k" reading.  Same
    # shipped measurement, two readings; c_link = mean_bond_length = 1.0 so the
    # smallest-k factor IS c(k_1).
    c_link = cld.mean_bond_length(rig.net)
    tgt = sanity["CS2_target"]
    k1 = sanity["CS2_c"][0] / c_link
    out["cs2_readings"] = {
        "c_link": c_link,
        "polyfit_extrapolation": {"factor": sanity["CS2_factor"],
                                  "rel_dev": sanity["CS2_rel"],
                                  "passes_2pct": bool(sanity["CS2_rel"] < P["cs2_tol"])},
        "smallest_k": {"factor": k1, "rel_dev": abs(k1 - tgt) / tgt,
                       "passes_2pct": bool(abs(k1 - tgt) / tgt < P["cs2_tol"])},
    }

    # (f) G-B matched-filter sign vs window close (the struck "hint")
    out["gb_sign_vs_close"] = {
        str(A): {str(cl_): float(np.sign(sweep["GB"][str(A)][str(cl_)]))
                 for cl_ in AMEND["close_sweep"]} for A in P["A_grid"]}
    out["gb_sign_stable"] = bool(all(
        len({v for v in row.values()}) == 1
        for row in out["gb_sign_vs_close"].values()))
    out["contaminant_front"] = windows["GJ"]["t_wrap_probe"]

    banner("POST-VERIFY AMENDMENT — window-convergence re-extraction [downstream]")
    print(f"  extended close = {c_ext} (contaminant front "
          f"{out['contaminant_front']:.2f}; guard {P['guard_sigmas']}*sigma_t = "
          f"{P['guard_sigmas'] * s_t:.2f} -> NOT guard-protected: probe only)")
    print(f"  G-J at extended close identical to frozen: "
          f"{out['verdict_survival']['GJ_unchanged_at_extended_close']}")
    print("  G-T converged locus (A, Gamma_frozen, Gamma_converged, tau*, "
          "ratio_frozen, ratio_converged):")
    for r in ratios:
        print(f"    A={r['A']:<7}{frozen_by_A['GT'][r['A']]['gamma']:+.5f} "
              f"{ext_by_A['GT'][r['A']]['gamma']:+.5f} "
              f"tau*={ext_by_A['GT'][r['A']]['tau']:<3} "
              f"{r['ratio_frozen']:.3f} {r['ratio_extended']:.3f}"
              f"{'  [taper band]' if r['in_taper_band'] else ''}")
    print(f"  in-band ratio: frozen {out['taper_band_ratio_frozen'][0]:.3f}-"
          f"{out['taper_band_ratio_frozen'][1]:.3f}  converged "
          f"{out['taper_band_ratio_extended'][0]:.3f}-"
          f"{out['taper_band_ratio_extended'][1]:.3f}  "
          f"(frozen criterion: < {P['taper_factor']})")
    print(f"  TAPER-SUPPRESSED on converged numbers: "
          f"{out['TAPER_SUPPRESSED_extended']} (frozen-window: "
          f"{out['verdict_survival']['GT_taper_suppressed_frozen_window']}) -> "
          f"the frozen G-T verdict survives a fortiori")
    print(f"  G-T extraction validity at extended close: "
          f"{out['n_unreliable_extended']['GT']} unreliable "
          f"(gate > {P['discord_max_pts']}) -> INVALID-EXTRACTION="
          f"{out['invalid_extraction_extended']['GT']}")
    print(f"  G-B matched-filter sign stable across the close sweep: "
          f"{out['gb_sign_stable']}")
    for A in (0.5, 0.9):
        row = out["gb_sign_vs_close"][str(A)]
        print(f"    A={A}: " + " ".join(
            f"close{k}:{'+' if v > 0 else '-'}" for k, v in row.items()))
    print(f"  corrected slab-back close bounds: "
          f"GJ {out['back_path_close_bound']['GJ']:.2f}, "
          f"GT {out['back_path_close_bound']['GT']:.2f} "
          f"(the result doc's narrative pair, recomputed)")
    r2 = out["cs2_readings"]
    print(f"  CS-2 read both ways (D8): polyfit-extrapolated "
          f"{r2['polyfit_extrapolation']['factor']:.6f} "
          f"(rel dev {r2['polyfit_extrapolation']['rel_dev']:.4%}, pass="
          f"{r2['polyfit_extrapolation']['passes_2pct']}); at smallest k "
          f"{r2['smallest_k']['factor']:.6f} "
          f"(rel dev {r2['smallest_k']['rel_dev']:.4%}, pass="
          f"{r2['smallest_k']['passes_2pct']}); c_link={r2['c_link']:.6f}")
    return out


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    np.random.seed(0)
    banner("DRIVER PARAMETERS (all values actually used; no silent defaults)")
    for k, v in P.items():
        print(f"  {k} = {v}")
    for k, v in AMEND.items():
        print(f"  [amendment] {k} = {v}")
    print(f"  engine src   = {ENGINE_SRC}")
    print(f"  chart module = {AVECHART_FILE}")
    print(f"  results out  = {OUT['results']}")
    print(f"  raw dir      = {OUT['rawdir']}")
    print(f"  figure stem  = {OUT['figstem']}")

    rig = Rig(P)
    net = rig.net
    print(f"\nNet: {net.name}, carrier={net.carrier}, N={rig.N} nodes, "
          f"degree={rig.deg}, box={rig.box_cells:.0f} cells "
          f"(a_cell={rig.a:.6f}, bond length=1.0 Cartesian)")
    print(f"Bonds: {rig.nb}; probe bonds crossing x_p={P['x_p']}: "
          f"{len(rig.idx_probe_fwd)}; back-monitor bonds: {len(rig.idx_bm_fwd)}; "
          f"sentinel bonds crossing x={P['sentinel_x']}: {len(rig.idx_sent_fwd)}")
    print(f"Launch: +x-propagating (weight max(0, -x.b_hat), deviation D2); "
          f"peak amplitude = {rig.launch().max():.4f}")

    sanity = cold_sanity(rig)
    gates14 = {k: sanity[k] for k in ("CS1_pass", "CS2_pass", "CS3_pass", "CS4_pass")}
    OUT["rawdir"].mkdir(parents=True, exist_ok=True)
    OUT["results"].parent.mkdir(parents=True, exist_ok=True)
    if not all(gates14.values()):
        _dump_sanity(sanity)
        banner("COLD SANITY FAILED (CS-1..CS-4) -> RUN IS VOID (V1). STOPPING.")
        sys.exit(2)

    banner("GRADED SWEEPS (16 A-points x 3 configs) — data collection")
    configs = ("GJ", "GB", "GT")
    raw = {c: {} for c in configs}
    v2_fail = []
    for config in configs:
        for A in P["A_grid"]:
            Ab = rig.a_field(config, A)
            a_nodes, Yp, sha0 = rig.build_scatter(Ab)
            run = rig.run(a_nodes, Yp, P["T_run"])
            # V2 checksum, SCOPE-HONEST: sha0 (build_scatter) and sha1 below are
            # both computed from the SAME in-memory `a_nodes`, so this gate can
            # fire only on IN-PLACE MUTATION of that array during the run — the
            # relevant leak channel for this code shape, but NOT a proof that
            # the stepper read S from here.  The freeze is over-determined by
            # the E_Y drift gate, CS-4, and step_graded's structure (no
            # A-update, no V-dependence of S).  Stated identically in the
            # result doc's V2 row so the two cannot drift apart.
            S_re = a_nodes[:, None, :] - np.eye(rig.deg)[None, :, :]
            sha1 = hashlib.sha256(np.ascontiguousarray(S_re).tobytes()).hexdigest()
            run["sha_match"] = (sha0 == sha1)
            run["n_graded_bonds"] = int((Ab > 0).sum())
            raw[config][A] = run
            if run["ey_drift"] >= P["v2_drift"] or not run["sha_match"]:
                v2_fail.append((config, A, run["ey_drift"], run["sha_match"]))
            print(f"  {config} A={A:<7} graded_bonds={run['n_graded_bonds']:<5} "
                  f"E_Y drift={run['ey_drift']:.2e} sha_ok={run['sha_match']}")
    if v2_fail:
        _dump_sanity(sanity)
        banner(f"V2 VOID: grading leaked into dynamics: {v2_fail}")
        sys.exit(2)

    banner("WINDOW DERIVATION (from cold measurements + measured graded transit)")
    t_back_min = {}
    for config in ("GJ", "GT"):
        cents = []
        for A in P["A_grid"]:
            if A == 0.0:
                continue
            Fb = raw[config][A]["Fb"]
            exp_bm = (P["back_monitor_x"] - P["x_s"]) * rig.a / sanity["c_meas"]
            c_bm, _ = pulse_moments(Fb, 0, min(len(Fb) - 1, int(1.8 * exp_bm)))
            cents.append(c_bm)
        t_back_min[config] = min(cents)
        print(f"  {config}: earliest transmitted centroid at back monitor = "
              f"{t_back_min[config]:.1f} steps")
    windows = {}
    for config in configs:
        w = derive_windows(rig, sanity, config, t_back_min.get(config))
        windows[config] = w
        t_echo = sanity["t_cF"] + 2 * (P["x_I"] - P["x_p"]) * rig.a / sanity["c_meas"]
        print(f"  {config}: incident={w['w_inc']}, reflected={w['w_refl']}, "
              f"wrap-projected probe arrival={w['t_wrap_probe']}, "
              f"slab-back return={w['t_back_return']}, "
              f"expected front-echo centroid={t_echo:.1f}, "
              f"constructible={w['constructible']}")
        if not w["constructible"]:
            _dump_sanity(sanity)
            banner(f"V3 VOID: reflected window not constructible for {config}")
            sys.exit(2)

    banner("CS-5 NULL CALIBRATION (A=0 through the full extraction pipeline)")
    eps_list = {}
    for config in configs:
        r0 = raw[config][0.0]
        ex = extract_gamma(r0["F"], r0["B"], windows[config]["w_inc"],
                           windows[config]["w_refl"])
        eps_list[config] = abs(ex["gamma"])
        print(f"  {config}: |Gamma(A=0)| = {abs(ex['gamma']):.5f} "
              f"(|Gamma|_E = {ex['gammaE']:.5f}, tau*={ex['tau']}) "
              f"gate < {P['cs5_cap']}")
    eps0 = max(eps_list.values())
    cs5_pass = all(e < P["cs5_cap"] for e in eps_list.values())
    theta = max(3 * eps0, P["theta_floor"])
    delta = max(eps0, P["delta_floor"])
    sanity.update(CS5_eps=eps_list, CS5_eps0=eps0, CS5_pass=cs5_pass,
                  theta=theta, delta=delta)
    print(f"  eps0 = {eps0:.5f}; theta = {theta:.5f}; delta = {delta:.5f} "
          f"-> {'PASS' if cs5_pass else 'FAIL'}")
    _dump_sanity(sanity)
    if not cs5_pass:
        banner("COLD SANITY FAILED (CS-5) -> RUN IS VOID (V1). STOPPING.")
        sys.exit(2)

    banner("EXTRACTION (matched filter + energy cross-check) [4.4]")
    table = {c: [] for c in configs}
    for config in configs:
        n_unrel = 0
        for A in P["A_grid"]:
            r = raw[config][A]
            ex = extract_gamma(r["F"], r["B"], windows[config]["w_inc"],
                               windows[config]["w_refl"])
            disc = abs(abs(ex["gamma"]) - ex["gammaE"]) / max(ex["gammaE"], theta)
            unreliable = disc > P["discord_tol"]
            n_unrel += int(unreliable)
            table[config].append(dict(A=A, gamma=ex["gamma"], gammaE=ex["gammaE"],
                                      tau=ex["tau"], discordance=disc,
                                      unreliable=bool(unreliable),
                                      valid=bool(not unreliable)))
            print(f"  {config} A={A:<7} Gamma={ex['gamma']:+.5f} "
                  f"|G|_E={ex['gammaE']:.5f} tau*={str(ex['tau']):>4} "
                  f"disc={disc:.3f} {'UNRELIABLE' if unreliable else ''}")
        table[config + "_invalid_extraction"] = n_unrel > P["discord_max_pts"]
        if table[config + "_invalid_extraction"]:
            print(f"  {config}: INVALID-EXTRACTION ({n_unrel} unreliable points "
                  f"> {P['discord_max_pts']})")

    banner("CLASSIFIERS + FROZEN VERDICTS [6.2/6.3/6.4]")
    cls, verd = {}, {}
    rows_by_A = {c: {r["A"]: r for r in table[c]} for c in configs}
    for config in configs:
        cls[config] = classify(table[config], theta, delta)
        print(f"  {config} classifiers: {cls[config]}")
    # TAPER-SUPPRESSED
    band = P["taper_band"]
    band_checks, suppressed = [], True
    for A in P["A_grid"]:
        if band[0] <= A <= band[1]:
            gj, gt = rows_by_A["GJ"].get(A), rows_by_A["GT"].get(A)
            if gj and gj["valid"] and abs(gj["gamma"]) > theta:
                ok = gt is not None and gt["valid"] and \
                    abs(gt["gamma"]) < P["taper_factor"] * abs(gj["gamma"])
                band_checks.append((A, abs(gj["gamma"]),
                                    abs(gt["gamma"]) if gt else None, ok))
                suppressed = suppressed and ok
    cls["GT"]["TAPER_SUPPRESSED"] = suppressed and len(band_checks) > 0
    print(f"  TAPER-SUPPRESSED band checks (A, |G_GJ|, |G_GT|, ok): {band_checks}")
    for config in configs:
        if table[config + "_invalid_extraction"]:
            verd[config] = ("INVALID-EXTRACTION", ["discordance gate [4.4]"])
            continue
        v = verdict_config(config, cls[config], rows_by_A[config], theta,
                           gj_rows=rows_by_A["GJ"],
                           taper_band=band, taper_factor=P["taper_factor"])
        if config == "GT" and v[0] == "TAPER-PENDING":
            gtc = cls["GT"]
            if gtc["TAPER_SUPPRESSED"] and not gtc.get("FLOOR") \
                    and not gtc.get("crossings"):
                v = ("TAPER (suppressed, no floor, no crossing)", [])
            else:
                why = []
                if not gtc["TAPER_SUPPRESSED"]:
                    why.append("fails TAPER-SUPPRESSED")
                if gtc.get("FLOOR"):
                    why.append("has FLOOR")
                if gtc.get("crossings"):
                    why.append("has CROSSING")
                v = ("TAPER-EXPECTATION NOT DRAWN", why)
        verd[config] = v
        print(f"  VERDICT {config}: {v[0]}  {v[1] if v[1] else ''}")

    # POST-VERIFY AMENDMENT — strictly downstream of the frozen verdicts above
    amend = post_verify_amendment(rig, raw, windows, sanity, table, verd)

    # persist
    for config in configs:
        out = {}
        for A in P["A_grid"]:
            r = raw[config][A]
            out[str(A)] = dict(F=r["F"].tolist(), B=r["B"].tolist(),
                               Fb=r["Fb"].tolist(),
                               sent_fwd=r["sent_fwd"].tolist(),
                               sent_bwd=r["sent_bwd"].tolist(),
                               ey_drift=r["ey_drift"],
                               sha_match=bool(r["sha_match"]),
                               n_graded_bonds=r["n_graded_bonds"])
        (OUT["rawdir"] / f"raw_{config}.json").write_text(json.dumps(out))
    summary = dict(
        params={k: (list(v) if isinstance(v, tuple) else v) for k, v in P.items()},
        sanity={k: v for k, v in sanity.items() if k != "cold"},
        windows={c: {k: v for k, v in windows[c].items()} for c in configs},
        table={c: table[c] for c in configs},
        invalid_extraction={c: bool(table[c + "_invalid_extraction"])
                            for c in configs},
        classifiers={c: _jsonable(cls[c]) for c in configs},
        verdicts={c: list(verd[c]) for c in configs},
        # everything above this line is the FROZEN record (byte-stable across
        # the post-verify repair); everything below is the amendment.
        post_verify_amendment=_jsonable(amend),
    )
    OUT["results"].write_text(
        json.dumps(summary, indent=1, default=_np_default))
    print(f"\nWrote {OUT['rawdir']}/raw_*.json and {OUT['results']}")

    make_figure(rig, table, theta, amend)
    return summary


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


def make_figure(rig, table, theta, amend=None):
    """Overlay: measured Gamma(A) per config on the three lumped forms.

    House style: white (style.apply print profile), Okabe-Ito, no title,
    legend outside the data, honest axes with units.

    POST-VERIFY AMENDMENT: G-T is plotted at the CONVERGED window close
    (amend['close_extended']); its frozen-window (tail-truncated) points are
    kept on the figure as small muted markers so the plot and the frozen table
    can be read against each other instead of silently disagreeing."""
    import matplotlib.pyplot as plt

    chart = load_ave_chart()
    style.apply("print")
    fig, ax = plt.subplots(figsize=style.figsize("single"))
    Ad = np.linspace(0.0, 0.999, 400)
    ax.plot(Ad, chart.gamma_of_A(Ad, "core").real, color=style.COLORS["data"],
            lw=1.0, ls="-", label="lumped core: $(\\sqrt{S}-1)/(\\sqrt{S}+1)$")
    ax.plot(Ad, chart.gamma_of_A(Ad, "J").real, color="#E69F00", lw=1.2,
            label="lumped J (junction-side): $(\\sqrt{S}/2-1)/(\\sqrt{S}/2+1)$")
    ax.plot(Ad, chart.gamma_of_A(Ad, "B").real, color="#56B4E9", lw=1.2,
            label="lumped B (bond-side): $(1/2-\\sqrt{S})/(1/2+\\sqrt{S})$")
    ax.axvline(chart.A_MATCHED_B, color=style.COLORS["muted"], lw=0.7, ls=":",
               label="$A^*=\\sqrt{15}/4$ (report-against, non-binding)")
    ax.axhline(0.0, color=style.COLORS["muted"], lw=0.5)
    marks = {"GJ": ("o", "#0072B2", "measured G-J (far-side slab)"),
             "GB": ("s", "#D55E00", "measured G-B (single crossing bond)"),
             "GT": ("^", "#009E73", "measured G-T (3-cell taper)")}
    # G-T's plotted series is the converged one when the amendment is present.
    plotted = {c: table[c] for c in marks}
    if amend is not None:
        c_ext = amend["close_extended"]
        plotted["GT"] = amend["table_extended"]["GT"]
        marks["GT"] = ("^", "#009E73",
                       f"measured G-T (3-cell taper), window close {c_ext}")
        gt_fro = table["GT"]
        ax.plot([r["A"] for r in gt_fro], [r["gamma"] for r in gt_fro], "x",
                color=style.COLORS["muted"], ms=4, mew=0.8, ls="none",
                label="G-T at frozen close 78 (tail-truncated)")
    for config, (m, col, lab) in marks.items():
        rows = plotted[config]
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
    main()
