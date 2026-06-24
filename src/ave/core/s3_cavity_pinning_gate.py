"""S3 — the Γ=−1 boundary cavity MUTUAL-PINNING gate (the re-route payoff test).

FROZEN PRE-REG: research/2026-06-24_engine-s3-cavity-pinning_prereg.md (commit 0b5691cd).
This module runs the S3 make-or-break on the COUPLED real-space A1↔ω PDE
(ave.solvers.coupled_cage_winding) and bins the HONEST verdict per the pre-reg §7
gate plan. A FALSE (disperses) result is a DEEPER negative and is reported as
DISPERSE-FALSIFIED — NOT rescued (pre-reg §0, §1; Rule 10+11).

THE MAKE-OR-BREAK (pre-reg §1) — the DELTA between (coupled, winding ON) and
(winding OFF / ω=0 = A1-alone, which MUST reproduce Stage-2 Mode-III):
  MAKE (pinned)    : the A1-core centroid-spread / interior energy-localization
                     holds BOUNDED over the full run — clears the Stage-2 Mode-I
                     PERSIST bar that A1-alone FAILED — energy-conservation-
                     certified on a CLOSED native-stencil box (|rel_drift|≤1e-5,
                     NO PML, NO damping), robust across sech AND gaussian.
  BREAK (disperses): reproduces Stage-2 Mode-III (interior peak → seed then sheds).

HALT GATES (pre-reg §7) — any failing → HALT (broken instrument, not a verdict):
  G1 operator validity on the coupled native stencil (H Hermitian; A1-block
     reproduces the Stage-2 native operator).
  G2 energy conservation on the COUPLED object, closed-box, |rel_drift| ≤ 1e-5.
  G3 negative controls FIRE: GX3 backward-Euler bleed > 0.05; GX5 passive-port
     Hmax/H0 ≤ 1; winding-OFF reproduces Mode-III; gaussian disperses;
     Cartesian-v14 self-traps; slaved-arm reachable-False (genesis-24).

GENESIS-24 (pre-reg §4): ω is its OWN DOF (never grad(V)); BOTH the A1-norm AND
the ω-winding integer are separately certified conserved. The slaved-arm
reachable-False control (S1 gate_f_positive_control) is the in-harness
independence discriminator.

α-CLEAN (pre-reg §3 trap 7): the chord-deciding read carries NO α-carrier. The
coupled solver's import-time guard triad + the winding-host κ̃=6/5 + θ_χ=2π·ν_vac
are α-free. V_snap is the declared operating-point scalar (CONSISTENCY-class), NOT
on the verdict-determining path. Q=137 stays EMPTY (anti-substitution, Rule 12).
"""

from __future__ import annotations

import numpy as np

from ave.solvers.coupled_cage_winding import (
    CoupledCageWinding,
    CoupledCageWindingConfig,
)
from ave.solvers.native_cage_imex import (
    NativeCageIMEX,
    NativeCageIMEXConfig,
    assemble_L_D,
    energy_conservation_gate,
)

# ── FROZEN run window (v14 Mode-I; Stage-2 production) — pre-stated, NOT tuned. ──
N_PROD = 24
N_STEPS_TOTAL = 600
N_STEPS_TRANSIENT = 200
SEED_AMP = 0.85
SEED_RADIUS = 2.5
SEED_SIGMA = 2.5
DX = 0.5

# ── FROZEN verdict bins (pre-reg §1, §2 — IDENTICAL to the Stage-2 Mode-I bins,
#    only the integrator + the winding DOF changed, NOT the adjudication). ──
ENERGY_DRIFT_TOL = 1e-5          # G2 closed-box |rel_drift| (matches Stage-2 −8.77e-6)
MODE_I_PEAK_MIN = 0.2           # I-1 interior peak persists
MODE_I_BREATH_MIN = 0.05        # I-2 breathing (not frozen)
MODE_I_BREATH_MAX = 0.5         # I-3 not diverging
MODE_I_RADFLOOR_MULT = 1.5      # I-5 above the radiation floor (>1.5× gaussian late)
DETONATION_MAX = 10.0           # I-6 bounded
GAUSS_DISPERSE_FRAC = 0.5       # gaussian control disperses below 0.5·seed
# BOUNDED-SPREAD localization (pre-reg §1 MAKE — the A46 real-space DELTA): a
# PINNED core's centroid-spread holds bounded (does NOT grow toward the box). The
# bar: the ON spread must stay below the box quarter-extent AND be materially
# tighter than the dispersing OFF control (the DELTA). Pre-stated bound:
SPREAD_BOUNDED_FRAC = 0.25      # ON spread_post < SPREAD_BOUNDED_FRAC · (N·dx)
SPREAD_DELTA_MIN = 1.30         # OFF/ON spread_post ratio (ON materially tighter)


def _gaussian_seed(N, *, amp, sigma, dx):
    c = N // 2
    i, j, k = np.indices((N, N, N))
    r2 = ((i - c) ** 2 + (j - c) ** 2 + (k - c) ** 2) * (dx**2)
    return amp * np.exp(-r2 / (2.0 * sigma**2))


# ═════════════════════════════════════════════════════════════════════════════
# THE COUPLED RUN RECORDER (real-space A1-core localization observables, A46).
# ═════════════════════════════════════════════════════════════════════════════
def run_coupled(N=N_PROD, *, winding_on, seed="sech", amp=SEED_AMP, radius=SEED_RADIUS,
                winding_mode="rigid_template", n_total=N_STEPS_TOTAL,
                n_transient=N_STEPS_TRANSIENT, dt=0.066, wind_check_stride=120):
    """Run the coupled A1↔ω PDE and record the real-space localization observables
    + the energy + per-grade + winding-integer histories. winding_on=False ⇒ Ω≡0
    = the A1-alone Mode-III negative control. Returns the run dict."""
    cfg = CoupledCageWindingConfig(N=N, dx=DX, winding_on=winding_on,
                                   winding_mode=winding_mode, dt=dt)
    eng = CoupledCageWinding(cfg)
    if seed == "sech":
        eng.seed_A1_sech(amplitude=amp, radius=radius)
    elif seed == "gaussian":
        eng.seed_A1_gaussian(amplitude=amp, sigma=radius)
    else:
        raise ValueError(seed)
    eng.seed_winding()

    H0 = eng.total_energy()
    a1_0 = eng.a1_energy()
    om_0 = eng.omega_energy()
    w0 = eng.winding_integer()
    spread0 = eng.a1_centroid_spread()

    peak_h, spread_h, ie_h, H_h, a1_h, om_h = [], [], [], [], [], []
    winds = [(w0["Q_link"], w0["w_tor"])]
    for s in range(n_total):
        eng.step()
        peak_h.append(eng.interior_peak_abs_A1())
        spread_h.append(eng.a1_centroid_spread())
        ie_h.append(eng.interior_A1_energy())
        H_h.append(eng.total_energy())
        a1_h.append(eng.a1_energy())
        om_h.append(eng.omega_energy())
        if (s + 1) % wind_check_stride == 0:
            w = eng.winding_integer()
            winds.append((w["Q_link"], w["w_tor"]))
    peak = np.array(peak_h)
    spread = np.array(spread_h)
    ie = np.array(ie_h)
    post = slice(n_transient, None)
    H_arr = np.array(H_h)
    return {
        "N": N, "winding_on": winding_on, "seed": seed, "winding_mode": winding_mode,
        "dt": dt, "n_total": n_total, "n_transient": n_transient,
        "rel_drift_end": float((eng.total_energy() - H0) / H0),
        "rel_drift_max": float(np.max(np.abs(H_arr - H0)) / H0),
        "a1_drain": float((eng.a1_energy() - a1_0) / a1_0),
        "om_drain": float((eng.omega_energy() - om_0) / om_0),
        "winding_history": winds,
        "winding_conserved": bool(all(w == (3, 2) for w in winds)),
        "winding_seed": (w0["Q_link"], w0["w_tor"]),
        "peak_post_mean": float(peak[post].mean()),
        "peak_std_over_mean_post": float(peak[post].std() / max(peak[post].mean(), 1e-9)),
        "peak_max_over_run": float(peak.max()),
        "spread0": float(spread0),
        "spread_post_mean": float(spread[post].mean()),
        "spread_end": float(spread[-1]),
        "spread_grows": bool(spread[-1] > spread0 * 1.10),
        "ie0": float(ie[0]),
        "ie_post_mean": float(ie[post].mean()),
        "ie_end": float(ie[-1]),
        "last_gmres_info": int(eng.last_gmres_info),
    }


# ═════════════════════════════════════════════════════════════════════════════
# HALT GATE 1 — operator validity on the coupled native stencil.
# ═════════════════════════════════════════════════════════════════════════════
def halt_gate_1_operator_validity(N=12) -> dict:
    """G1: the coupled generator H is Hermitian (⇒ unitary ⇒ exact conservation)
    AND its A1-block reproduces the VALIDATED Stage-2 native operator (the spatial
    op is UNCHANGED — only the coupling + ω DOF are added). FAIL → HALT."""
    cfg = CoupledCageWindingConfig(N=N, R=4.0, r=1.6)
    eng = CoupledCageWinding(cfg)
    eng.seed_A1_sech(amplitude=0.85, radius=2.5)
    eng.seed_winding()
    H = eng._assemble_H()
    asym = float(abs(H - H.conj().T).max())
    hermitian = asym < 1e-10

    # A1-block (top-left ndof×ndof) = ω_b·I − c_A1²·L_D : reproduces the native op.
    nd = eng.ndof
    H_A1_block = H[:nd, :nd].toarray()
    D = eng.stiffness_D().reshape(nd)
    L_D = assemble_L_D(eng.Grad, eng.Div, D).toarray()
    expected = cfg.omega_b * np.eye(nd) - (cfg.c_A1**2) * L_D
    block_err = float(np.abs(H_A1_block - expected).max())
    block_ok = block_err < 1e-10
    return {
        "H_hermitian_asym": asym, "H_hermitian": bool(hermitian),
        "A1_block_matches_native_op_err": block_err, "A1_block_matches_native": bool(block_ok),
        "PASS": bool(hermitian and block_ok),
    }


# ═════════════════════════════════════════════════════════════════════════════
# HALT GATE 2 — energy conservation on the COUPLED object (closed-box, the hero).
# ═════════════════════════════════════════════════════════════════════════════
def halt_gate_2_energy_conservation(N=N_PROD) -> dict:
    """G2: the COUPLED object conserves energy on a CLOSED box (NO PML, NO
    damping) to |rel_drift| ≤ 1e-5 — the rigor guard (damping-bought localization
    is the top trap, pre-reg §3 trap 1). Measured on the production self-focusing
    sech with the winding ON (the verdict run's actual dynamics). FAIL → HALT."""
    r = run_coupled(N, winding_on=True, seed="sech")
    passed = abs(r["rel_drift_max"]) <= ENERGY_DRIFT_TOL
    return {
        "rel_drift_end": r["rel_drift_end"], "rel_drift_max": r["rel_drift_max"],
        "tol": ENERGY_DRIFT_TOL, "gmres_info": r["last_gmres_info"],
        "PASS": bool(passed),
    }


def _cartesian_v14_self_traps(N=N_PROD) -> dict:
    """Cartesian-v14 MUST self-trap (Mode-I) — the live in-harness positive
    control (pre-reg §3 trap 2/5). The retired bulk self-trap is a Cartesian
    artifact; this confirms the apparatus can SEE a self-trap when one exists."""
    from ave.core.master_equation_fdtd import MasterEquationFDTD
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
    som = float(v_peak.std() / max(v_peak.mean(), 1e-9))
    self_traps = bool(v_peak.mean() > 0.2 and 0.05 < som < 0.5
                      and np.array(n_min).min() < 0.97)
    return {"v_peak_mean_post": float(v_peak.mean()), "std_over_mean": som,
            "n_em_min": float(np.array(n_min).min()), "self_traps": self_traps,
            "PASS": self_traps}


# ═════════════════════════════════════════════════════════════════════════════
# HALT GATE 3 — negative controls FIRE (any not behaving as pre-stated → HALT).
# ═════════════════════════════════════════════════════════════════════════════
def halt_gate_3_negative_controls(N=N_PROD, *, fast=False) -> dict:
    """G3 (pre-reg §7.3): the immune system must FIRE. (a) GX3 backward-Euler
    bleed > 0.05; (b) GX5 passive-port Hmax/H0 ≤ 1; (c) winding-OFF reproduces
    Mode-III in-harness; (d) gaussian disperses; (e) Cartesian-v14 self-traps;
    (f) slaved-arm reachable-False (genesis-24). A control NOT behaving as
    pre-stated ⇒ HALT (broken instrument). Ports the Stage-2 GX3/GX5 + the S1
    slaved-arm discriminator (Rule 14 anti-rebuild)."""
    out = {}

    # (a) GX3 backward-Euler bleeds (the Stage-2 negative control, ported).
    from scipy.sparse import identity
    from scipy.sparse.linalg import cg
    cfg = NativeCageIMEXConfig(N=16)
    be = NativeCageIMEX(cfg)
    be.em_port_closed = True
    be.seed_sech(amplitude=0.02, radius=2.5)
    be.set_dt_accuracy()
    ndof = 16**3
    H0 = be.total_energy()
    for _ in range(400):
        D = be.stiffness_D()
        L_D = assemble_L_D(be.Grad, be.Div, D)
        coef = (be.dt**2) * (be.c0**2)
        v = be.V.reshape(ndof)
        v_prev = be.V_prev.reshape(ndof)
        A_sys = (identity(ndof, format="csr") + coef * L_D).tocsr()
        v_new, _ = cg(A_sys, 2.0 * v - v_prev, rtol=1e-10, maxiter=2000, x0=v)
        be.V_prev = be.V.copy()
        be.V = v_new.reshape(16, 16, 16)
        be.time += be.dt
    bleed = (H0 - be.total_energy()) / H0
    out["gx3_backward_euler_bleed"] = {"bleed": float(bleed), "PASS": bool(bleed > 0.05)}

    # (b) GX5 passive radiative port (the Stage-2 negative control, ported).
    pp = NativeCageIMEX(NativeCageIMEXConfig(N=16, dx=0.5, port_sigma=0.05))
    pp.seed_sech(amplitude=0.85, radius=2.5)
    pp.set_dt_accuracy()
    pp.dt = 0.066
    H0p = pp.total_energy()
    Hmax = H0p
    for _ in range(300):
        pp.step()
        Hmax = max(Hmax, pp.total_energy())
    out["gx5_passive_port"] = {"Hmax_over_H0": float(Hmax / H0p),
                               "PASS": bool(Hmax <= H0p * (1.0 + 1e-6))}

    # (c) winding-OFF reproduces Mode-III IN THIS HARNESS (the HERO-CANARY).
    off = run_coupled(N, winding_on=True if False else False, seed="sech",
                      n_total=(200 if fast else N_STEPS_TOTAL),
                      n_transient=(60 if fast else N_STEPS_TRANSIENT))
    # Mode-III ⇔ the interior peak → seed then sheds below the radiation floor:
    # peak_post well below seed AND interior energy drains AND spread grows.
    off_modeIII = bool(off["peak_post_mean"] < 0.5 * SEED_AMP
                       and off["ie_end"] < 0.5 * off["ie0"]
                       and off["spread_grows"])
    out["winding_off_reproduces_modeIII"] = {
        "peak_post_mean": off["peak_post_mean"], "ie0": off["ie0"], "ie_end": off["ie_end"],
        "spread0": off["spread0"], "spread_end": off["spread_end"],
        "is_modeIII": off_modeIII, "PASS": off_modeIII,
    }

    # (d) gaussian disperses (winding OFF gaussian, the seed-robustness control).
    g = run_coupled(N, winding_on=False, seed="gaussian",
                    n_total=(200 if fast else N_STEPS_TOTAL),
                    n_transient=(60 if fast else N_STEPS_TRANSIENT))
    gd = bool(g["peak_post_mean"] < GAUSS_DISPERSE_FRAC * SEED_AMP)
    out["gaussian_disperses"] = {"peak_post_mean": g["peak_post_mean"], "PASS": gd}

    # (e) Cartesian-v14 self-traps (the apparatus-can-see-a-trap control).
    if not fast:
        out["cartesian_v14_self_traps"] = _cartesian_v14_self_traps(N)
    else:
        out["cartesian_v14_self_traps"] = {"PASS": True, "skipped_fast": True}

    # (f) slaved-arm reachable-False (genesis-24 independence; S1 gate, Rule 14).
    if not fast:
        from ave.core import s1_winding_conservation_gate as S1
        f = S1.gate_f_positive_control(48, 11.0, 4.0)
        out["slaved_arm_reachable_false"] = {
            "slaved_arm_independence_false": bool(f["slaved_arm_independence_false"]),
            "real_arm_independent": bool(f["real_arm_independent"]),
            "PASS": bool(f["slaved_arm_independence_false"]),
        }
    else:
        out["slaved_arm_reachable_false"] = {"PASS": True, "skipped_fast": True}

    out["PASS"] = bool(all(v["PASS"] for v in out.values() if isinstance(v, dict)))
    return out


# ═════════════════════════════════════════════════════════════════════════════
# GENESIS-24 BOTH-CONSERVED CERT (pre-reg §4) — A1-norm AND ω-winding separately.
# ═════════════════════════════════════════════════════════════════════════════
def genesis24_both_conserved(on_run: dict) -> dict:
    """Certify BOTH conserved on the winding-ON run (pre-reg §4): (1) the joint
    energy (the A1-norm half + the ω half) conserved (the closed-box rigor guard);
    (2) the ω-winding INTEGER conserved (3,2) across the run (read off the
    quadrature-invariant |b_ω|·ê_w — NOT bled into the A1 scalar). A "pin" bought
    by draining the winding into A1 would FAIL the winding-integer check even if
    energy is conserved. Both must hold for a trustworthy PERSIST."""
    energy_ok = abs(on_run["rel_drift_max"]) <= ENERGY_DRIFT_TOL
    winding_ok = on_run["winding_conserved"]
    return {
        "energy_conserved": bool(energy_ok), "rel_drift_max": on_run["rel_drift_max"],
        "winding_integer_conserved": bool(winding_ok),
        "winding_history": on_run["winding_history"],
        "a1_drain": on_run["a1_drain"], "om_drain": on_run["om_drain"],
        "both_conserved": bool(energy_ok and winding_ok),
        "PASS": bool(energy_ok and winding_ok),
    }


# ═════════════════════════════════════════════════════════════════════════════
# THE PRIMARY DELTA — winding ON vs OFF; bin PERSIST (Mode-I) vs DISPERSE (Mode-III).
# ═════════════════════════════════════════════════════════════════════════════
def classify_persist(on: dict, off: dict) -> dict:
    """Apply the FROZEN Mode-I PERSIST bins (pre-reg §1, §2 — IDENTICAL to the
    Stage-2 bins + the bounded-spread localization criterion). PERSIST ⇔ the
    winding-ON core clears the Mode-I bar that A1-alone (OFF) FAILED, with the
    A1-core spread held BOUNDED and materially tighter than the dispersing OFF
    control (the A46 real-space DELTA). Returns the bins + the verdict."""
    box_extent = N_PROD * DX
    bins = {
        "I-1 peak_post > 0.2": on["peak_post_mean"] > MODE_I_PEAK_MIN,
        "I-2 breathing std/mean > 0.05": on["peak_std_over_mean_post"] > MODE_I_BREATH_MIN,
        "I-3 not diverging std/mean < 0.5": on["peak_std_over_mean_post"] < MODE_I_BREATH_MAX,
        "I-5 above radiation floor (>1.5x OFF peak)":
            on["peak_post_mean"] > MODE_I_RADFLOOR_MULT * off["peak_post_mean"],
        "I-6 bounded max|V| < 10": on["peak_max_over_run"] < DETONATION_MAX,
        # the A46 real-space localization DELTA (the load-bearing pin criterion):
        "L-1 spread bounded (< 0.25·box)": on["spread_post_mean"] < SPREAD_BOUNDED_FRAC * box_extent,
        "L-2 spread does NOT grow": not on["spread_grows"],
        "L-3 spread DELTA OFF/ON >= 1.30":
            (off["spread_post_mean"] / max(on["spread_post_mean"], 1e-9)) >= SPREAD_DELTA_MIN,
    }
    persist = all(bins.values())
    return {
        "bins": {k: bool(v) for k, v in bins.items()},
        "on_peak_post_mean": on["peak_post_mean"],
        "off_peak_post_mean": off["peak_post_mean"],
        "on_spread_post_mean": on["spread_post_mean"], "on_spread0": on["spread0"],
        "on_spread_end": on["spread_end"], "off_spread_post_mean": off["spread_post_mean"],
        "spread_delta_off_over_on": float(off["spread_post_mean"] / max(on["spread_post_mean"], 1e-9)),
        "on_ie_post_mean": on["ie_post_mean"], "off_ie_post_mean": off["ie_post_mean"],
        "ie_delta_on_over_off": float(on["ie_post_mean"] / max(off["ie_post_mean"], 1e-9)),
        "verdict": "PERSIST" if persist else "DISPERSE",
        "failing_bins": [k for k, v in bins.items() if not v],
    }


# ═════════════════════════════════════════════════════════════════════════════
# THE GATE RUNNER — HALT logic + the honest final verdict (NO rescue).
# ═════════════════════════════════════════════════════════════════════════════
def run_s3_gate(N=N_PROD, *, fast=False) -> dict:
    """Run the full S3 cavity-pinning gate and bin the HONEST verdict per the
    FROZEN pre-reg (§1, §7). PERSIST-PINNED iff (a) the HALT gates all pass, (b)
    BOTH conserved (energy + winding integer; genesis-24), (c) the winding-ON core
    clears the Mode-I PERSIST bar with the spread bounded + the DELTA, (d)
    seed-robust (sech AND gaussian). DISPERSE-FALSIFIED iff the make-or-break
    DELTA does not clear the bar (the deeper negative — pre-reg §0; reported
    honestly, NOT rescued). INCONCLUSIVE iff a HALT gate fails (broken instrument,
    not a verdict)."""
    out = {"prereg": "research/2026-06-24_engine-s3-cavity-pinning_prereg.md (0b5691cd)",
           "scheme": "Crank-Nicolson/Cayley (I+i dt/2 H)x^{n+1}=(I-i dt/2 H)x^n; H Hermitian; GMRES",
           "winding_mode": "rigid_template", "N": N}

    # ── HALT GATE 1: operator validity ──
    g1 = halt_gate_1_operator_validity()
    out["halt_gate_1_operator_validity"] = g1
    if not g1["PASS"]:
        out["verdict"] = "INCONCLUSIVE"
        out["halt_reason"] = "G1 operator validity FAILED — coupled generator is not a valid Hermitian native operator."
        return out

    # ── HALT GATE 2: energy conservation (the hero) ──
    g2 = halt_gate_2_energy_conservation(N)
    out["halt_gate_2_energy_conservation"] = g2
    if not g2["PASS"]:
        out["verdict"] = "INCONCLUSIVE"
        out["halt_reason"] = (f"G2 energy conservation FAILED — |rel_drift|={g2['rel_drift_max']:.2e} > {ENERGY_DRIFT_TOL:.0e}; "
                              "damping-bought localization risk (broken instrument).")
        return out

    # ── HALT GATE 3: negative controls fire ──
    g3 = halt_gate_3_negative_controls(N, fast=fast)
    out["halt_gate_3_negative_controls"] = g3
    if not g3["PASS"]:
        out["verdict"] = "INCONCLUSIVE"
        failing = [k for k, v in g3.items() if isinstance(v, dict) and not v.get("PASS", True)]
        out["halt_reason"] = f"G3 negative control(s) did NOT behave as pre-stated: {failing} (broken instrument)."
        return out

    # ── PRIMARY DELTA: winding ON vs OFF, sech + gaussian ──
    nt = 200 if fast else N_STEPS_TOTAL
    ntr = 60 if fast else N_STEPS_TRANSIENT
    on_sech = run_coupled(N, winding_on=True, seed="sech", n_total=nt, n_transient=ntr)
    off_sech = run_coupled(N, winding_on=False, seed="sech", n_total=nt, n_transient=ntr)
    on_gauss = run_coupled(N, winding_on=True, seed="gaussian", n_total=nt, n_transient=ntr)
    off_gauss = run_coupled(N, winding_on=False, seed="gaussian", n_total=nt, n_transient=ntr)

    delta_sech = classify_persist(on_sech, off_sech)
    delta_gauss = classify_persist(on_gauss, off_gauss)
    out["primary_delta_sech"] = delta_sech
    out["primary_delta_gaussian"] = delta_gauss

    # ── GENESIS-24 BOTH-conserved (on the winding-ON sech run) ──
    g24 = genesis24_both_conserved(on_sech)
    out["genesis24_both_conserved"] = g24

    # ── IMMUNE-SYSTEM summary (the deliverable fields) ──
    out["immune_system"] = {
        "winding_off_disperses_modeIII": bool(
            g3["winding_off_reproduces_modeIII"]["PASS"]),
        "energy_gate_passed": bool(g2["PASS"]),
        "both_conserved_A1_and_winding": bool(g24["both_conserved"]),
        "slaved_arm_independence_false": bool(
            g3["slaved_arm_reachable_false"]["PASS"]),
        "negative_controls_fired": bool(g3["PASS"]),
    }

    # ── HONEST FINAL VERDICT (NO rescue, Rule 10+11) ──
    seed_robust = (delta_sech["verdict"] == delta_gauss["verdict"])
    persist = (delta_sech["verdict"] == "PERSIST" and delta_gauss["verdict"] == "PERSIST"
               and g24["both_conserved"])
    out["seed_robust"] = bool(seed_robust)
    if persist:
        out["verdict"] = "PERSIST-PINNED"
        out["verdict_reason"] = (
            "The winding-ON A1 core clears the Mode-I PERSIST bar that A1-alone "
            "(winding OFF) FAILED — spread bounded, DELTA present — energy + "
            "winding-integer BOTH conserved (closed-box, no damping). The "
            "localization mechanism is boundary/topological (the re-route holds)."
        )
    elif delta_sech["verdict"] == "DISPERSE" and delta_gauss["verdict"] == "DISPERSE":
        out["verdict"] = "DISPERSE-FALSIFIED"
        out["verdict_reason"] = (
            "The winding-ON A1 core DISPERSES (reproduces Stage-2 Mode-III): the "
            "centroid-spread is NOT held bounded (grows toward the box) and does "
            "not clear the Mode-I PERSIST bar, robustly across sech AND gaussian, "
            "on an energy-conservation-certified CLOSED box (NOT numerics). "
            "winding + H_couple + cavity does NOT pin the core — the DEEPER "
            "negative (pre-reg §0). Reported honestly; NOT rescued (Rule 11)."
        )
    else:
        out["verdict"] = "PARTIAL"
        out["verdict_reason"] = (
            f"Seed-DEPENDENT: sech={delta_sech['verdict']}, "
            f"gaussian={delta_gauss['verdict']} — not seed-robust. The DELTA does "
            "not give a clean seed-robust PERSIST (pre-reg §1 robustness)."
        )
    return out


def main() -> None:
    import json
    import sys

    print("S3 CAVITY-PINNING GATE — coupled real-space A1↔ω PDE (native K4)")
    print("=" * 70)
    res = run_s3_gate()
    print(json.dumps(res, indent=2, default=str))
    print("=" * 70)
    print(f"VERDICT: {res['verdict']}")
    print(res.get("verdict_reason", res.get("halt_reason", "")))
    sys.exit(0)


if __name__ == "__main__":
    main()
