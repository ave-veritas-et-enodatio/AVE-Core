"""
Motion-stability via back-EMF — native Cosserat/dark-wake τ_zx on VacuumEngine3D.

Grant's hypothesis (stability FROM motion): the native τ_zx back-EMF of a MOVING
self-trap STABILIZES it — retention(v) slope > 0, stability gain tracking the
native τ_zx (positive), MORE than a linear (SM-counterfactual) control at matched
amplitude/saturation.

Canonical default CONTRADICTS: the saturated (2,3) self-trap is a static Γ=−1 knot;
at A²≈8.9 the core saturation S=√(1−A²) clamps to 0 ⇒ z_local at the rupture floor
⇒ c_eff = c·√S → 0 (frozen local clock). A frozen-core trap is PINNED: stable
because static, not via motion.

THIS engine is the real adjudication: the prior Maxwell-engine version (per brief)
saw only the E/H PROJECTION of τ_zx (anti-correlated −0.81); VacuumEngine3D's
DarkWakeObserver carries the NATIVE back-EMF stress τ_zx = z_local·∂_x(A²) directly
(K4 saturation-modulated impedance × strain gradient, vacuum_engine.py:1533).

Brief / prereg: _orchestration/motion-stability-bemf-cosserat.md
Result:        research/2026-06-04_motion-stability-bemf-cosserat-result.md

THE BOOST (the fix — replaces the failed port-pairing of the stalled run):
  The winding-extractor reads the quadrature phasor (ox, oy) = (V0+V1, V2+V3); the
  ansatz plants exactly this (ports {0,1}=cos(2φ+3ψ), {2,3}=sin(2φ+3ψ)). The boost
  rotates ox+i·oy by exp(i k_x x) — a +x spatial phase gradient applied COHERENTLY
  to the full phasor, redistributed onto the ports preserving intra-pair ratios.
  A genuine traveling-wave boost on the channel the winding lives in.

ANTI-STALL: validate the boost on a LINEAR (sub-saturation) pulse FIRST (≤2 boost
  variants). LINEAR moves → proceed; LINEAR does NOT move after 2 variants →
  BLOCKED-boost, write diagnosis, return.

FORWARD-PREDICTED SIGN (pre-run, no fit — ave-driver-script-honesty):
  substrate-default = PIN. LINEAR advects (c_eff≈c); SELF-TRAP does NOT
  (v_knot/v_linear ≪ 1); retention(v) flat-or-falling; native-τ_zx-vs-stability
  correlation ≤ 0. Predicted verdict: CONTRADICTS-via-PIN. A SUPPORTS overturns
  the static-trap canon and triggers full ave-discrimination-check.
"""

import json
import sys
import time
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "src"))
sys.path.insert(0, str(Path(__file__).resolve().parent))

from ave.core.constants import ALPHA  # noqa: E402
from ave.topological.vacuum_engine import (  # noqa: E402
    DarkWakeObserver,
    VacuumEngine3D,
)
from tlm_electron_soliton_eigenmode import (  # noqa: E402
    initialize_2_3_voltage_ansatz,
)

# ── Substrate-derived constants (ave-canonical-source: NO hardcoded literals) ──
A2_OP14 = float(np.sqrt(2.0 * ALPHA))   # √(2α) ≈ 0.1208 — Op14 engagement (self-trap bar)
PHI = (1.0 + np.sqrt(5.0)) / 2.0
COMPTON_PERIOD = 2.0 * np.pi
DT = 1.0 / np.sqrt(2.0)                  # K4-TLM 4-port junction timestep

# Host (Arm-C) geometry — the confirmed durable host (retention ~0.88–0.91, peak A²≈8.9)
HOST_R_FRAC = 0.22                       # R_shell = 0.22·N
HOST_AMP = 0.40                          # peak A²_interior ≈ 8.9 during evolution

# FORWARD-PREDICTED SIGN (no fit). The substrate default at A²≈8.9 (S=0, c_eff→0).
FORWARD_PREDICTED_VERDICT = "CONTRADICTS-via-PIN"
FORWARD_PREDICTED_SIGN = {
    "linear_moves": True,
    "knot_moves": False,
    "retention_slope_sign": "<= 0 (flat or falling)",
    "tau_zx_vs_stability_corr_sign": "<= 0",
}


# ══════════════════════════════════════════════════════════════════════════════
# Engine + host (confirmed config — reused verbatim from
# r10_vacuumengine3d_transverse_2_3_emergence.py:setup_engine / Arm-C)
# ══════════════════════════════════════════════════════════════════════════════
def setup_engine(N, PML):
    """A28-corrected coupled VacuumEngine3D (doc 67 §15 + r10_v8 config)."""
    return VacuumEngine3D.from_args(
        N=N,
        pml=PML,
        temperature=0.0,
        amplitude_convention="V_SNAP",
        disable_cosserat_lc_force=True,
        enable_cosserat_self_terms=True,
        use_asymmetric_saturation=True,
        axiom_4_enabled=True,
    )


def seed_host(engine, N, amplitude=HOST_AMP):
    """Plant the durable (2,3) host (Arm-C config): the confirmed self-trap that
    holds retention ~0.88–0.91 at peak A²≈8.9. R = 0.22·N, r = R/φ²."""
    R = HOST_R_FRAC * N
    r = R / (PHI**2)
    initialize_2_3_voltage_ansatz(engine.k4, R=R, r=r, amplitude=amplitude)
    return R, r


def _interior_mask(N, PML):
    m = np.zeros((N, N, N), dtype=bool)
    m[PML : N - PML, PML : N - PML, PML : N - PML] = True
    return m


# ══════════════════════════════════════════════════════════════════════════════
# THE BOOST — coherent phasor traveling wave on (ox, oy) = (V0+V1, V2+V3)
# ══════════════════════════════════════════════════════════════════════════════
def apply_coherent_phasor_boost(engine, k_x, x_c=None):
    """Rotate the winding phasor ox+i·oy by exp(i k_x x) at every active site,
    ENERGY-CONSERVINGLY, where ox = V0+V1 (ports {0,1}, +x hemisphere) and
    oy = V2+V3 (ports {2,3}, −x hemisphere) — the channel the (2,3) winding lives
    in (ansatz: {0,1}=cos θ_wind, {2,3}=sin θ_wind). A +x spatial phase gradient =
    a genuine +x traveling-wave boost.

    Construction (exact energy conservation — verified max|dE/E|=6e-16 vs the prior
    multiplicative-redistribution form that injected O(10⁶) energy at phasor zeros
    on the saturated shell): decompose each site's 4 ports into a COMMON mode
    (a,b) = (V0+V1, V2+V3) = (ox, oy) and a DIFFERENTIAL mode (c,d) = (V0−V1, V2−V3).
    Rotate ONLY the common mode by R(α) (orthogonal → preserves a²+b², hence total
    port energy exactly); leave the differential mode fixed. Invert:
      V0=(a'+c)/2, V1=(a'−c)/2, V2=(b'+d)/2, V3=(b'−d)/2.
    No division → no blow-up at ox≈0 or oy≈0 (which occur all over the winding shell).
    NOT the port-pairs (the stalled run showed port-pairing is not a clean traveling
    wave).

    k_x: +x phase gradient (rad/cell). 0 → identity (no boost).
    x_c: phase reference plane (defaults to lattice center).
    """
    if k_x == 0.0:
        return
    N = engine.N
    if x_c is None:
        x_c = (N - 1) / 2.0
    V = engine.k4.V_inc
    xi = np.arange(N, dtype=float)[:, None, None]
    alpha = k_x * (xi - x_c)                      # (N,1,1) per-x rotation angle
    ca = np.cos(alpha)
    sa = np.sin(alpha)
    a = V[..., 0] + V[..., 1]   # common mode = (ox, oy) — the winding phasor
    b = V[..., 2] + V[..., 3]
    c = V[..., 0] - V[..., 1]   # differential mode (untouched)
    d = V[..., 2] - V[..., 3]
    a2 = ca * a - sa * b        # rotate common mode by exp(i k_x x)
    b2 = sa * a + ca * b
    V[..., 0] = 0.5 * (a2 + c)
    V[..., 1] = 0.5 * (a2 - c)
    V[..., 2] = 0.5 * (b2 + d)
    V[..., 3] = 0.5 * (b2 - d)
    V[~engine.k4.mask_active] = 0.0


# ══════════════════════════════════════════════════════════════════════════════
# LINEAR (sub-saturation) pulse — the SM-counterfactual + the boost smoke test
# ══════════════════════════════════════════════════════════════════════════════
def seed_linear_pulse(engine, N, PML, peak_A2_target=0.5 * A2_OP14):
    """Sub-saturation, ZERO-CARRIER phasor blob with the (ox,oy)=(V0+V1,V2+V3)
    quadrature structure of the host winding, localized and BELOW A²_op14 (no
    self-trap). ZERO carrier (ox=env real, oy=0) so the one-shot coherent boost
    `exp(i k_x x)` imprints a CLEAN momentum (group velocity) with v=0 at k=0 — the
    SM-counterfactual + the boost smoke test. (A pre-existing standing carrier
    washes out the imprinted momentum; verified — the zero-carrier blob advects
    cleanly and sign-symmetrically.) Amplitude scaled so peak A² ≈ peak_A2_target
    (sub-saturation; default = ½·A²_op14)."""
    cx = (N - 1) / 2.0
    i, j, k = np.indices((N, N, N), dtype=float)
    r2 = (i - cx) ** 2 + (j - cx) ** 2 + (k - cx) ** 2
    sigma = max(2.5, 0.10 * N)
    env = np.exp(-r2 / (2.0 * sigma**2))
    V = engine.k4.V_inc
    V[..., 0] = env       # zero-carrier: ox = V0+V1 = 2·env (real), oy = V2+V3 = 0
    V[..., 1] = env
    V[..., 2] = 0.0
    V[..., 3] = 0.0
    V[~engine.k4.mask_active] = 0.0
    # scale to the sub-saturation target peak A²
    A2 = np.sum(V**2, axis=-1) / engine.V_SNAP**2
    m = _interior_mask(N, PML)
    cur = float(A2[m].max())
    if cur > 0:
        scale = np.sqrt(peak_A2_target / cur)
        V *= scale
    return float(np.sum((np.sum(V**2, axis=-1) / engine.V_SNAP**2)[m]))


# ══════════════════════════════════════════════════════════════════════════════
# Observables
# ══════════════════════════════════════════════════════════════════════════════
def a2_field(engine):
    return np.sum(engine.k4.V_inc**2, axis=-1) / engine.V_SNAP**2


def x_centroid(engine, PML, weight_floor=0.0):
    """Energy-weighted x-centroid over the interior (A² weighting). The motion
    observable. Returns (centroid_x, total_interior_energy)."""
    N = engine.N
    A2 = a2_field(engine)
    m = _interior_mask(N, PML) & engine.k4.mask_active
    w = np.where(m, A2, 0.0)
    if weight_floor > 0:
        w = np.where(w >= weight_floor * w.max(), w, 0.0)
    tot = float(w.sum())
    if tot <= 0:
        return float("nan"), 0.0
    xi = np.arange(N, dtype=float)[:, None, None]
    cx = float((w * xi).sum() / tot)
    return cx, tot


def x_fwhm(engine, PML):
    """FWHM of the interior A² profile projected onto x (localization width)."""
    N = engine.N
    A2 = a2_field(engine)
    m = _interior_mask(N, PML) & engine.k4.mask_active
    prof = np.where(m, A2, 0.0).sum(axis=(1, 2))
    if prof.max() <= 0:
        return float("nan")
    half = 0.5 * prof.max()
    idx = np.where(prof >= half)[0]
    if len(idx) < 2:
        return float(DT)  # sub-cell
    return float(idx[-1] - idx[0] + 1)


def smoke_test_boost(N=40, PML=4, n_steps=60, k_list=(0.0, 0.15, 0.30)):
    """ANTI-STALL smoke test: seed a zero-carrier LINEAR sub-saturation pulse,
    apply the ONE-SHOT coherent boost exp(i k_x x), confirm the centroid MOVES
    (monotone, sign-symmetric, v=0 at k=0). Returns per-k_x velocity.

    The boost is a ONE-SHOT momentum imprint (the physical traveling-wave boost);
    a re-imposed-every-step variant is a sustained PUMP (injects energy → blows up
    the field) and is NOT a clean boost — rejected (verified: overflow). The
    one-shot phasor rotation is the genuine `rotate ox+i·oy by exp(i k_x x)` boost.
    """
    out = {"per_kx": []}
    for k_x in k_list:
        engine = setup_engine(N, PML)
        seed_linear_pulse(engine, N, PML)
        apply_coherent_phasor_boost(engine, k_x)   # one-shot momentum imprint
        cx0, e0 = x_centroid(engine, PML)
        traj = [(0.0, cx0, e0)]
        for s in range(n_steps):
            engine.step()
            if (s + 1) % 5 == 0:
                cx, e = x_centroid(engine, PML)
                traj.append(((s + 1) * DT, cx, e))
        ts = np.array([t for (t, c, e) in traj if not np.isnan(c)])
        cs = np.array([c for (t, c, e) in traj if not np.isnan(c)])
        v = float(np.polyfit(ts, cs, 1)[0]) if len(ts) >= 2 else float("nan")
        out["per_kx"].append({
            "k_x": k_x, "v_centroid": v,
            "cx_start": float(cs[0]) if len(cs) else float("nan"),
            "cx_end": float(cs[-1]) if len(cs) else float("nan"),
            "dx_total": float(cs[-1] - cs[0]) if len(cs) >= 2 else float("nan"),
        })
    vs = [abs(d["v_centroid"]) for d in out["per_kx"]]
    # MOVES: v at largest k meaningfully exceeds the k=0 (≈static) value
    out["moves"] = bool(vs[-1] > 5.0 * (vs[0] + 1e-6) and vs[-1] > 1e-3)
    out["monotone"] = bool(vs[-1] >= vs[1] - 1e-9 >= vs[0] - 1e-9)
    out["v0_is_zero"] = bool(vs[0] < 1e-3)
    return out


# ══════════════════════════════════════════════════════════════════════════════
# BASELINE — matched energy + A-trajectory, NET-ZERO momentum (opposite-v superpose)
# ══════════════════════════════════════════════════════════════════════════════
def apply_opposite_v_baseline_boost(engine, k_x, x_c=None):
    """BASELINE(v) boost (ave-discrimination-check matched control): superpose a
    +k_x and −k_x phase gradient on the SAME host, giving a standing (net-zero
    momentum) modulation at the SAME interior energy + SAME saturation depth +
    SAME A-trajectory as SELF-TRAP(v) — but NO net translation. This is the
    genuinely-matched baseline the brief requires (NOT a phase-scramble, which
    would change energy/saturation). cos(k_x x) common-mode amplitude modulation:
    the even part of exp(±i k_x x), so it carries the boost's |k_x| spectral
    content with zero first moment.

    Energy-conserving: rotates the common mode (ox,oy) by ±α and averages → a real
    amplitude scaling cos(α); to keep energy matched we re-normalize the common
    mode magnitude back to its pre-boost value per site."""
    if k_x == 0.0:
        return
    N = engine.N
    if x_c is None:
        x_c = (N - 1) / 2.0
    V = engine.k4.V_inc
    xi = np.arange(N, dtype=float)[:, None, None]
    alpha = k_x * (xi - x_c)
    ca = np.cos(alpha)
    a = V[..., 0] + V[..., 1]
    b = V[..., 2] + V[..., 3]
    c = V[..., 0] - V[..., 1]
    d = V[..., 2] - V[..., 3]
    mag0 = np.sqrt(a * a + b * b)
    # symmetric (even) part of the rotation: ½[R(α)+R(−α)] = diag(cos α) → standing
    a2 = ca * a
    b2 = ca * b
    mag1 = np.sqrt(a2 * a2 + b2 * b2)
    # renormalize common-mode magnitude back to mag0 (match energy exactly)
    scale = np.where(mag1 > 1e-12, mag0 / np.where(mag1 > 1e-12, mag1, 1.0), 1.0)
    a2 *= scale
    b2 *= scale
    V[..., 0] = 0.5 * (a2 + c)
    V[..., 1] = 0.5 * (a2 - c)
    V[..., 2] = 0.5 * (b2 + d)
    V[..., 3] = 0.5 * (b2 - d)
    V[~engine.k4.mask_active] = 0.0


# ══════════════════════════════════════════════════════════════════════════════
# Instrumented arm runner (the full decisive test)
# ══════════════════════════════════════════════════════════════════════════════
def run_arm(kind, k_x, N, PML, settle=10, n_steps=70, rec_every=5):
    """Run one (arm, v) cell and record the full trajectory.

    kind:
      'selftrap' — durable (2,3) host (A²≈3.07 steady, S=0 frozen core), boosted by
                   the coherent phasor traveling wave (the object under test).
      'linear'   — zero-carrier sub-saturation pulse, same boost (SM-counterfactual).
      'baseline' — host + opposite-v (standing) boost: matched energy + A-trajectory,
                   net-zero momentum (the genuinely-matched control).

    Records: x-centroid trajectory (→ velocity), interior energy (→ retention),
    FWHM (localization), native max|τ_zx| (DarkWakeObserver), peak interior A²
    (saturated-while-moving check)."""
    engine = setup_engine(N, PML)
    obs = DarkWakeObserver(cadence=1, propagation_axis=0)
    if kind == "linear":
        seed_linear_pulse(engine, N, PML)
    else:
        seed_host(engine, N)
    engine.add_observer(obs)
    # settle (let the host self-trap into the frozen-core (2,3); harmless for linear)
    for _ in range(settle):
        engine.step()
    # apply the boost at t=0 of the recording window
    if kind == "baseline":
        apply_opposite_v_baseline_boost(engine, k_x)
    else:
        apply_coherent_phasor_boost(engine, k_x)

    traj = []   # (t, cx, E_int, fwhm, max_tau_zx, peakA2)
    cx0, e0 = x_centroid(engine, PML)
    d0 = obs._capture(engine)
    A2_0 = a2_field(engine)
    m = _interior_mask(N, PML)
    traj.append((0.0, cx0, e0, x_fwhm(engine, PML), d0["max_tau_zx"], float(A2_0[m].max())))
    for s in range(n_steps):
        engine.step()
        if (s + 1) % rec_every == 0:
            cx, e = x_centroid(engine, PML)
            d = obs._capture(engine)
            A2 = a2_field(engine)
            traj.append(((s + 1) * DT, cx, e, x_fwhm(engine, PML),
                         d["max_tau_zx"], float(A2[m].max())))
    arr = np.array(traj, dtype=float)
    ts, cxs, es, fwhms, taus, peakA2s = arr.T
    good = ~np.isnan(cxs)
    v = float(np.polyfit(ts[good], cxs[good], 1)[0]) if good.sum() >= 2 else float("nan")
    # retention = last/first interior energy over the recorded (post-boost) window
    retention = float(es[-1] / es[0]) if es[0] > 0 else float("nan")
    return {
        "kind": kind, "k_x": k_x,
        "v_centroid": v,
        "cx_start": float(cxs[0]), "cx_end": float(cxs[-1]),
        "dx_total": float(cxs[-1] - cxs[0]),
        "E_start": float(es[0]), "E_end": float(es[-1]),
        "retention": retention,
        "fwhm_start": float(fwhms[0]), "fwhm_end": float(fwhms[-1]),
        "max_tau_zx_mean": float(np.mean(taus)),
        "max_tau_zx_start": float(taus[0]), "max_tau_zx_end": float(taus[-1]),
        "peakA2_mean": float(np.mean(peakA2s)), "peakA2_min": float(np.min(peakA2s)),
        "_traj": arr,
    }


def adjudicate_motion_stability(sweep):
    """Apply the decisive disambiguation + Grant-vs-canon verdict.

    sweep: {arm: {k_x: result}} for arm in {selftrap, linear, baseline}, k_x in K_SWEEP.
    """
    K = sorted({r["k_x"] for r in sweep["linear"].values()})
    k_max = max(K)

    def v_of(arm, k):
        return sweep[arm][k]["v_centroid"]

    # boost-RESPONSE = v(k_max) corrected for the k=0 self-drift, and the
    # sign-symmetry (a real momentum kick flips sign with k). We probe ±k_max.
    lin_resp = abs(v_of("linear", k_max) - v_of("linear", 0.0))
    st_resp = abs(v_of("selftrap", k_max) - v_of("selftrap", 0.0))
    # sign-flip test (the robust pin tell): does v flip sign between +k and −k?
    # (cast to Python bool — numpy bool_ fails `is False` identity checks.)
    has_neg = (-k_max) in sweep["linear"]
    lin_signflip = bool(np.sign(v_of("linear", k_max)) != np.sign(v_of("linear", -k_max))) if has_neg else None
    st_signflip = bool(np.sign(v_of("selftrap", k_max)) != np.sign(v_of("selftrap", -k_max))) if has_neg else None

    linear_moves = bool(lin_resp > 1e-3)
    # PIN: linear responds to the boost, self-trap does NOT (response ≪ linear AND
    # no sign-flip with boost direction → motion is boost-independent self-drift).
    knot_pinned = bool(linear_moves and (st_resp < 0.25 * lin_resp))
    if has_neg:
        knot_pinned = bool(knot_pinned and (st_signflip is False))  # st_signflip now Python bool

    # retention(v) slope on the SELF-TRAP arm (Grant: should be >0 if motion stabilizes)
    st_ret = [sweep["selftrap"][k]["retention"] for k in K]
    st_v_abs = [abs(sweep["selftrap"][k]["v_centroid"]) for k in K]
    ret_slope = float(np.polyfit(st_v_abs, st_ret, 1)[0]) if len(K) >= 2 and np.ptp(st_v_abs) > 1e-9 else float("nan")

    # native-τ_zx-vs-stability correlation: across the v-sweep, does the stability
    # gain (Δretention vs k=0) track max|τ_zx|? Grant: positive. Canon: ≤0.
    tau = [sweep["selftrap"][k]["max_tau_zx_mean"] for k in K]
    ret = st_ret
    if len(K) >= 3 and np.std(tau) > 1e-30 and np.std(ret) > 1e-30:
        tau_ret_corr = float(np.corrcoef(tau, ret)[0, 1])
    else:
        tau_ret_corr = float("nan")

    # saturated-while-moving check (peak A² stays ≫1 → frozen core throughout)
    peakA2_min = min(sweep["selftrap"][k]["peakA2_min"] for k in K)
    saturated_throughout = bool(peakA2_min > 1.0)

    # VERDICT
    if not linear_moves:
        verdict = "BLOCKED-boost"
        text = ("The LINEAR control does NOT move under the boost — the boost mechanism is the "
                "blocker, not the physics. (Should not occur: smoke test passed.)")
    elif knot_pinned:
        verdict = "CONTRADICTS-via-PIN"
        text = ("LINEAR moves but the SELF-TRAP knot does NOT (boost-independent residual drift, "
                "no sign-flip with boost direction). The saturated (2,3) core (A²≫1 ⇒ S=0 ⇒ "
                "c_eff→0) is GENUINELY PINNED — stable because static (frozen local clock), NOT "
                "via motion. Grant's stability-FROM-motion hypothesis is CONTRADICTED cleanly on "
                "the native-τ_zx engine. The knot is a frozen-clock soliton; motion needs an "
                "external drive the boost cannot supply to a c_eff→0 core.")
    else:
        # the knot DID respond to the boost → SUPPORTS pathway (gated by discipline)
        supports = bool(ret_slope > 0 and tau_ret_corr > 0)
        if supports:
            verdict = "SUPPORTS-pending-discrimination-check"
            text = ("The SELF-TRAP knot MOVES under the boost AND retention rises with v AND the "
                    "stability gain tracks native τ_zx (positive) — SUPPORTS Grant. MANDATORY: "
                    "apply ave-discrimination-check (LINEAR-control SM-counterfactual already in; "
                    "verify saturated-while-moving + baseline-fairness + interpretive-alternatives) "
                    "BEFORE any positive framing. A positive overturns the static-trap canon.")
        else:
            verdict = "NULL"
            text = ("The SELF-TRAP knot responds to the boost but retention does NOT rise with v "
                    "(slope≤0) and/or stability does NOT track native τ_zx (corr≤0). Neither a "
                    "clean PIN nor a motion-stabilization signal — NULL on the stability-from-motion "
                    "axis.")

    return {
        "verdict": verdict, "text": text,
        "linear_moves": linear_moves,
        "linear_boost_response": lin_resp, "selftrap_boost_response": st_resp,
        "selftrap_resp_over_linear": float(st_resp / lin_resp) if lin_resp > 0 else float("nan"),
        "linear_signflips_with_boost": (bool(lin_signflip) if lin_signflip is not None else None),
        "selftrap_signflips_with_boost": (bool(st_signflip) if st_signflip is not None else None),
        "knot_pinned": knot_pinned,
        "retention_v_slope_selftrap": ret_slope,
        "native_tau_zx_vs_retention_corr": tau_ret_corr,
        "saturated_throughout": saturated_throughout,
        "peakA2_min_selftrap": peakA2_min,
        "forward_predicted_verdict": FORWARD_PREDICTED_VERDICT,
        "forward_predicted_sign": FORWARD_PREDICTED_SIGN,
        "v_by_arm_k": {arm: {str(k): sweep[arm][k]["v_centroid"] for k in sorted(sweep[arm])}
                       for arm in sweep},
        "retention_by_arm_k": {arm: {str(k): sweep[arm][k]["retention"] for k in sorted(sweep[arm])}
                               for arm in sweep},
    }


def run_full_sweep(N=48, PML=4, settle=10, n_steps=70):
    """The decisive test: SELF-TRAP / LINEAR / BASELINE × v∈{0, low, mid} (+ −mid for
    the sign-flip pin tell). Fixed host config (peak A²≈8.9-run / ≈3.07-steady) across
    the sweep — no saturation-depth confound (same seed amplitude every cell)."""
    K_SWEEP = [0.0, 0.15, 0.30, -0.30]   # 0, low, mid, −mid (sign-flip control)
    arms = ["selftrap", "linear", "baseline"]
    sweep = {a: {} for a in arms}
    for arm in arms:
        for k in K_SWEEP:
            print(f"    [{arm:9s} k={k:+.2f}] ...", flush=True, end=" ")
            t0 = time.time()
            r = run_arm(arm, k, N, PML, settle=settle, n_steps=n_steps)
            sweep[arm][k] = r
            print(f"v={r['v_centroid']:+.5f} ret={r['retention']:.3f} "
                  f"τ_zx={r['max_tau_zx_mean']:.3e} peakA²={r['peakA2_mean']:.2f} "
                  f"({time.time()-t0:.0f}s)", flush=True)
    return sweep, K_SWEEP


def main():
    print("=" * 80, flush=True)
    print("  MOTION-STABILITY via back-EMF — native Cosserat/dark-wake τ_zx on VacuumEngine3D")
    print("  Grant: stability FROM motion (retention(v) slope>0, tracks native τ_zx).")
    print("  Canon: saturated knot PINNED (S=0 frozen core, c_eff→0). Maxwell saw only E/H proj.")
    print("=" * 80, flush=True)
    print(f"  ALPHA={ALPHA} A²_op14={A2_OP14:.4f} (ave-canonical-source) | dt={DT:.4f}")
    print(f"  FORWARD-PREDICTED (no fit): {FORWARD_PREDICTED_VERDICT} | {FORWARD_PREDICTED_SIGN}")

    print("\n  ── ANTI-STALL smoke test (does the boost advect a LINEAR pulse?) ──", flush=True)
    ts0 = time.time()
    smoke = smoke_test_boost(k_list=(0.0, 0.15, 0.30, -0.30))
    for d in smoke["per_kx"]:
        print(f"    k_x={d['k_x']:+.2f}: v={d['v_centroid']:+.4f} cell/τ dx={d['dx_total']:+.3f}")
    print(f"    LINEAR MOVES={smoke['moves']} v0≈0={smoke['v0_is_zero']} ({time.time()-ts0:.0f}s)")
    if not smoke["moves"]:
        print("\n  BLOCKED-boost: LINEAR pulse does not move. STOP (see _orchestration brief).")
        return {"verdict": "BLOCKED-boost", "smoke": smoke}

    print("\n  ── FULL SWEEP: SELF-TRAP / LINEAR / BASELINE × v ──", flush=True)
    sweep, K = run_full_sweep()
    verdict = adjudicate_motion_stability(sweep)

    print("\n" + "=" * 80)
    print("  VERDICT:", verdict["verdict"])
    print("=" * 80)
    print(f"  LINEAR moves: {verdict['linear_moves']} (response {verdict['linear_boost_response']:.4f}); "
          f"SELF-TRAP response {verdict['selftrap_boost_response']:.4f} "
          f"(= {verdict['selftrap_resp_over_linear']:.3f}× linear)")
    print(f"  sign-flips with boost dir — linear: {verdict['linear_signflips_with_boost']}, "
          f"self-trap: {verdict['selftrap_signflips_with_boost']}")
    print(f"  knot PINNED: {verdict['knot_pinned']}")
    print(f"  retention(v) slope (self-trap): {verdict['retention_v_slope_selftrap']:.4e}")
    print(f"  native τ_zx vs retention corr: {verdict['native_tau_zx_vs_retention_corr']:.3f}")
    print(f"  saturated throughout (peakA²_min={verdict['peakA2_min_selftrap']:.2f}): "
          f"{verdict['saturated_throughout']}")
    print(f"\n  {verdict['text']}")
    print(f"\n  Forward-predicted: {verdict['forward_predicted_verdict']} | "
          f"observed: {verdict['verdict']}")

    # save (strip raw traj arrays from JSON; keep in npz)
    out_json = {
        "verdict": verdict,
        "smoke": smoke,
        "config": {"N": 48, "PML": 4, "settle": 10, "n_steps": 70,
                   "host_R_frac": HOST_R_FRAC, "host_amp": HOST_AMP,
                   "A2_op14": A2_OP14, "ALPHA": ALPHA, "dt": DT,
                   "K_sweep": K},
        "arms": {arm: {str(k): {kk: vv for kk, vv in sweep[arm][k].items() if kk != "_traj"}
                       for k in sweep[arm]} for arm in sweep},
    }
    out_path = Path(__file__).parent / "motion_stability_bemf_cosserat_probe_results.json"
    out_path.write_text(json.dumps(out_json, indent=2, default=str), encoding="utf-8")
    print(f"\n  Saved {out_path.name}")
    npz_path = Path(__file__).parent / "motion_stability_bemf_cosserat_probe_capture.npz"
    np.savez_compressed(
        npz_path,
        **{f"{arm}_k{str(k).replace('-','m').replace('.','p')}": sweep[arm][k]["_traj"]
           for arm in sweep for k in sweep[arm]},
        dt=DT, N=48, PML=4,
    )
    print(f"  Saved {npz_path.name}")
    return verdict


if __name__ == "__main__":
    main()
