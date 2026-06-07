"""Option-D (2,3) pair IMPOSE re-tested under the (II) moving-Γ=−1 reflective wall.

Re-runs the EXISTING `phase5_topological_pair_injection` impose — the (2,3)
torus-knot LH@A / RH@B pair hand-placed at an A→B bond, driven by the
autoresonant collision, observed for persistence — which under the engine's
NATIVE energy-saturation confinement gave **MODE III** (the pair AND its (2,3)
dissolved at step ~11; verdict *"coupling-depth issue, not injection-profile
issue"*, `phase5_topological_pair_injection_results.json`).

The ONE new variable: **swap the confinement**. Arm C proved the native
energy-saturation term `γ(κ²−κ⁴/ω_yield²)` COLLAPSES; the (II) build proved a
moving `Γ=−1` impedance boundary CONFINES the same field the energy term blows
up. This driver asks: **does the imposed pair PERSIST past step ~11 when
confined by the (II) reflective wall instead of the collapsing energy term?**

Three configs isolate which ingredient (if any) matters (forward, no fit):
  - **native**       (`use_impedance_boundary=False`) — reproduce MODE III (control).
  - **wall_only**    (`use_impedance_boundary=True, couple_v_sector=False`) —
                     the (II) moving wall, but the Cosserat-ω "2" wall sees
                     V_sq=0 (decoupled from the K4 V-sector "3").
  - **wall_sector**  (`use_impedance_boundary=True, couple_v_sector=True`) —
                     the moving wall co-determined by the live K4 V_sq (the §9
                     sector-coupling fix: the "3"=U(1) fibre feeds the shared front).

`consistency-vs-emergence`: this is an **IMPOSE / Option-D STABILITY test** — we
hand-place the (2,3) pair and ask whether the confinement makes the *imposed*
object PERSIST. It is **NOT an emergence test**; no claim the electron emerges
from the drive. The class is `consistency` (does the (II) confinement render the
Option-D impose self-consistent / stable), per `consistency-vs-emergence`.

`phase-space-coordinate-check`: the imposed pair lives in the **Cosserat-ω**
sector (real-space winding, the "2"); the K4 V-sector (the "3"=U(1) fibre) is
read in its own coordinate (V_sq, Φ_link at the bond) — NOT conflated. The
reactance pair is tracked at every recorded step: C-state |ω| AND L-state |ω̇|
at each endpoint (A-Rule 10 reactance-pair discipline).

REUSE (`ave-prereg`, cite the MODE-III prior):
  - `PairNucleationGate` (pre-marked nucleated → never re-fires; Option-D impose).
  - `AutoresonantCWSource` (the C2 drive), exactly as the prior phase5 run.
  - `find_central_bond` + `seed_2_3_torus_knot_at_bond` imported from
    `phase5_topological_pair_injection` (the (2,3) impose profile, unchanged).
  - the (II) `use_impedance_boundary` moving-Γ=−1 confinement (committed 688cc14d),
    ported to the coupled engine + implicit reactance-rotation integrator.

References:
  - phase5_topological_pair_injection.py / _results.json (MODE III, frozen 1c89fa1)
  - research/2026-06-06_saturation-tir-moving-boundary-result.md (the (II) verdict)
  - research/2026-06-06_optionD-impose-under-reflective-confinement-result.md (this)
"""

from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "src"))

import jax.numpy as jnp

from ave.topological.cosserat_field_3d import _beltrami_helicity
from ave.topological.vacuum_engine import (
    AutoresonantCWSource,
    PairNucleationGate,
    VacuumEngine3D,
)

# Reuse the (2,3) impose profile + bond finder from the MODE-III driver verbatim.
from phase5_topological_pair_injection import (  # noqa: E402
    find_central_bond,
    seed_2_3_torus_knot_at_bond,
)

# ─── Pre-registered persistence criterion (frozen, P_phase5_nucleation) ───────
PERSIST_FRAC_THRESH = 0.5    # peak |ω| ≥ 0.5·seed counts as "held"
PERSIST_PERIODS_REQ = 10.0   # ≥ 10 Compton periods post-drive
TOPOLOGY_TARGET_C = 3        # (2,3) winding target

PRIOR_JSON = Path(__file__).parent / "phase5_topological_pair_injection_results.json"
OUTPUT_JSON = Path(__file__).parent / "phase5_optionD_under_reflective_confinement_results.json"


def _localization(cos, pml) -> float:
    """Fraction of |ω|² within r≤6 of the energy-density PEAK (PML-excluded).

    Position-INDEPENDENT (CP7: density-peak, not fixed-site/centroid) — so a pair
    that MOVES off the seed bond but stays trapped still reads high; only genuine
    dispersal/dissolution drives it → 0. The new axis alongside the legacy
    fixed-site |ω|_A/B (which cannot tell "moved" from "dissolved")."""
    N = cos.nx
    ii, jj, kk = cos._i, cos._j, cos._k
    interior = (
        (ii >= pml) & (ii < N - pml) & (jj >= pml) & (jj < N - pml) & (kk >= pml) & (kk < N - pml)
    )
    w2 = np.sum(np.asarray(cos.omega) ** 2, axis=-1) * cos.mask_alive * interior
    tot = w2.sum()
    if tot < 1e-30:
        return 0.0
    pk = np.unravel_index(np.argmax(w2), w2.shape)
    r2 = (ii - pk[0]) ** 2 + (jj - pk[1]) ** 2 + (kk - pk[2]) ** 2
    return float((w2 * (r2 <= 36)).sum() / tot)


def _wall_gamma_min(engine) -> float | None:
    """Most-negative Op3 Γ over the lattice = wall-engagement diagnostic.
    g_min→−1 ⇒ a hard reflective short formed; g_min≈0 ⇒ the wall never engaged
    at this amplitude (so a null result is 'wall absent', NOT 'wall failed').
    None for the native (no-wall) config."""
    coupled = engine._coupled
    if not getattr(coupled, "use_impedance_boundary", False):
        return None
    g = coupled._impedance_gamma_shared()
    alive = engine.cos.mask_alive
    return float(g[alive].min())


def _local_helicity(engine, idx, half=2) -> float:
    """Integrated Beltrami helicity h=ω·(∇×ω) in a ±half box around `idx`.

    The sign is the local handedness (LH@A vs RH@B); retention of the
    sign-split is the charge-neutral-pair / handedness check (Cosserat-ω sector).
    """
    h = np.asarray(_beltrami_helicity(jnp.asarray(engine.cos.omega), engine.cos.dx))
    N = engine.cos.nx
    i0, j0, k0 = idx
    sl = tuple(slice(max(0, c - half), min(N, c + half + 1)) for c in (i0, j0, k0))
    return float(np.sum(h[sl]))


def measure_state(engine, A_idx, B_idx, port) -> dict:
    """Persistence snapshot — directly comparable to the MODE-III prior, plus
    the reactance pair (C-state ω AND L-state ω̇) and the K4 V-sector ("3")."""
    cos = engine.cos
    omega_A = cos.omega[A_idx[0], A_idx[1], A_idx[2], :]
    omega_B = cos.omega[B_idx[0], B_idx[1], B_idx[2], :]
    wdot_A = cos.omega_dot[A_idx[0], A_idx[1], A_idx[2], :]
    wdot_B = cos.omega_dot[B_idx[0], B_idx[1], B_idx[2], :]
    V_sq = np.asarray(engine.k4.V_inc) ** 2
    V_sq = np.sum(V_sq, axis=-1)  # per-site Σ_k V_inc[k]²
    alive = engine.k4.mask_active
    phi_bond = float(engine.k4.Phi_link[A_idx[0], A_idx[1], A_idx[2], port])
    return {
        "t": float(engine.time),
        "step": int(engine.step_count),
        # Cosserat-ω "2" sector — the imposed pair (reactance pair C + L state)
        "|w|_A": float(np.linalg.norm(omega_A)),
        "|w|_B": float(np.linalg.norm(omega_B)),
        "|wdot|_A": float(np.linalg.norm(wdot_A)),
        "|wdot|_B": float(np.linalg.norm(wdot_B)),
        "peak|w|_global": float(np.max(np.linalg.norm(np.asarray(cos.omega), axis=-1))),
        # Position-independent localization (density-peak, PML-excluded) — the
        # honest "did the imposed structure survive ANYWHERE" axis.
        "loc": _localization(cos, cos.pml_thickness),
        "c_cos_global": int(cos.extract_crossing_count()),
        "E_cos": float(cos.total_energy()),
        "h_A": _local_helicity(engine, A_idx),
        "h_B": _local_helicity(engine, B_idx),
        # Wall-engagement diagnostic (None for native) — separates a clean (III)
        # ("wall formed, pair still dissolves") from "wall never engaged".
        "g_min": _wall_gamma_min(engine),
        # K4 V-sector "3" (U(1) fibre) — read in its own coordinate (CP4)
        "max_V_sq": float(V_sq[alive].max()) if alive.any() else 0.0,
        "|Phi_link|_bond": abs(phi_bond),
    }


# ─── One config: seed the (2,3) impose, drive, observe persistence ────────────


def run_config(
    name: str,
    engine_kwargs: dict,
    *,
    N=24,
    pml=4,
    amplitude=0.5,
    wavelength=3.5,
    t_ramp_periods=3.0,
    t_sustain_periods=10.0,
    t_post_drive_periods=12.0,
    record_cadence=2,
    seed_amp_scale=1.0,
    drive=True,
) -> dict:
    omega_carrier = 2.0 * np.pi / wavelength
    period = 2.0 * np.pi / omega_carrier
    t_ramp = t_ramp_periods * period
    t_sustain = t_sustain_periods * period
    drive_end_time = (t_ramp_periods + t_sustain_periods + 1.0) * period
    total_time = drive_end_time + t_post_drive_periods * period
    n_outer_steps = int(total_time * np.sqrt(2.0)) + 1

    # Base config = the MODE-III phase5 config; the impedance flags are the swap.
    engine = VacuumEngine3D.from_args(
        N=N,
        pml=pml,
        temperature=0.0,
        amplitude_convention="V_SNAP",
        disable_cosserat_lc_force=True,
        enable_cosserat_self_terms=True,
        **engine_kwargs,
    )

    A_idx, port, B_idx = find_central_bond(engine)
    seed_2_3_torus_knot_at_bond(engine, A_idx, port, B_idx)
    # seed_amp_scale > 1 lifts the imposed pair above the wall-engagement
    # threshold (the diagnostic separating "wall never engaged at the m_ec²-
    # calibrated impose amplitude" from "wall engaged, pair still dissolves").
    if seed_amp_scale != 1.0:
        engine.cos.omega *= float(seed_amp_scale)
    state_seed = measure_state(engine, A_idx, B_idx, port)

    # Option-D gate: pre-mark this bond nucleated so the gate never re-fires —
    # the pair is IMPOSED (hand-placed), not nucleated by the drive (Option-D).
    gate = PairNucleationGate(cadence=record_cadence)
    gate._nucleated_bonds.add((A_idx[0], A_idx[1], A_idx[2], port))
    engine.add_observer(gate)

    # drive=False isolates whether the hard-wall parametric pumping is
    # drive-induced (the moving front tracking the K4-fed focusing field) or
    # wall-intrinsic (the (II) §6 instability of the stiff clamp itself).
    src_offset = pml + 3
    if drive:
        for x0, d in ((src_offset, 1.0), (N - src_offset, -1.0)):
            engine.add_source(
                AutoresonantCWSource(
                    x0=x0,
                    direction=(d, 0.0, 0.0),
                    amplitude=amplitude,
                    omega=omega_carrier,
                    sigma_yz=3.0,
                    t_ramp=t_ramp,
                    t_sustain=t_sustain,
                    t_decay=period,
                )
            )

    trajectory = [state_seed]
    blew_up = False
    t0 = time.time()
    for _ in range(n_outer_steps):
        engine.step()
        # Early-stop on a blown-up field (the native energy-saturation collapse
        # at the diagnostic amplitude — Arm C / (II) §3 — would otherwise NaN the
        # observers and waste compute). The blowup IS the result; record + stop.
        if not np.all(np.isfinite(engine.cos.omega)):
            blew_up = True
            break
        if engine.step_count % record_cadence == 0:
            trajectory.append(measure_state(engine, A_idx, B_idx, port))
    elapsed = time.time() - t0

    return {
        "name": name,
        "engine_kwargs": engine_kwargs,
        "A_idx": list(A_idx),
        "port": int(port),
        "B_idx": list(B_idx),
        "period": period,
        "drive_end_time": drive_end_time,
        "drive_end_step": int(drive_end_time * np.sqrt(2.0)),
        "n_sub": int(engine._coupled._n_sub),
        "trajectory": trajectory,
        "elapsed_s": elapsed,
        "blew_up": blew_up,
        "seed_amp_scale": float(seed_amp_scale),
    }


# ─── Per-config adjudication (forward, no fit) ────────────────────────────────


def adjudicate(run: dict) -> dict:
    traj = run["trajectory"]
    period = run["period"]
    drive_end_step = run["drive_end_step"]
    seed = traj[0]
    omega_seed = seed["|w|_A"]
    threshold = PERSIST_FRAC_THRESH * omega_seed

    # Dissolution step — first recorded step (after seed) where |ω|_A < 0.5·seed.
    # This is the direct "past step ~11?" comparison vs the MODE-III prior.
    dissolution_step = None
    dissolution_t = None
    for s in traj[1:]:
        if s["|w|_A"] < threshold:
            dissolution_step = s["step"]
            dissolution_t = s["t"]
            break

    # Post-drive persistence (formal P_phase5_nucleation).
    post = [s for s in traj if s["step"] >= drive_end_step]
    if len(post) > 1:
        wa = [s["|w|_A"] for s in post]
        wb = [s["|w|_B"] for s in post]
        freq_pass_A = all(w >= threshold for w in wa)
        freq_pass_B = all(w >= threshold for w in wb)
        compton_post = (post[-1]["t"] - post[0]["t"]) / period
        min_wa_post = min(wa)
        min_wb_post = min(wb)
    else:
        freq_pass_A = freq_pass_B = False
        compton_post = 0.0
        min_wa_post = min_wb_post = 0.0
    period_check = compton_post >= PERSIST_PERIODS_REQ
    frequency_pass = bool(freq_pass_A and freq_pass_B and period_check)

    # NEW AXIS — position-independent localization (density-peak, honest "held
    # anywhere"). loc held ≥0.5·seed through ≥10 Compton post-drive = the brief's
    # "localization/winding/energy held" persistence (KEEP-BOTH vs fixed-site).
    loc_seed = seed["loc"]
    loc_thresh = PERSIST_FRAC_THRESH * loc_seed
    loc_dissolution_step = None
    for s in traj[1:]:
        if s["loc"] < loc_thresh:
            loc_dissolution_step = s["step"]
            break
    loc_post = [s["loc"] for s in post] if len(post) > 1 else []
    loc_held = bool(loc_post and all(l >= loc_thresh for l in loc_post) and period_check)
    loc_min_post = min(loc_post) if loc_post else 0.0
    loc_survives_past_11 = (loc_dissolution_step is None) or (loc_dissolution_step > 11)

    # Wall-engagement diagnostic — deepest (most-negative) Γ over the trajectory.
    # Separates a clean (III) (wall formed, pair still dissolves) from "wall never
    # engaged at the imposed-pair amplitude" (g_min≈0 → inconclusive for the wall).
    g_mins = [s["g_min"] for s in traj if s["g_min"] is not None]
    g_min_deepest = min(g_mins) if g_mins else None
    wall_engaged = (g_min_deepest is not None) and (g_min_deepest < -0.1)

    # Topology (the "2" winding) trajectory.
    c_vals = [s["c_cos_global"] for s in traj]
    topology_preserved = all(c == TOPOLOGY_TARGET_C for c in c_vals)

    # Handedness retention (LH@A / RH@B sign-split, charge-neutral pair).
    hand_ok_seed = (seed["h_A"] * seed["h_B"]) <= 0  # opposite sign at seed
    hand_A_sign = np.sign(traj[-1]["h_A"])
    hand_B_sign = np.sign(traj[-1]["h_B"])
    hand_retained_end = (traj[-1]["h_A"] * traj[-1]["h_B"]) <= 0

    # Energy bounded (no parametric pumping): E_cos_end / E_cos_seed.
    E_seed = seed["E_cos"] if abs(seed["E_cos"]) > 1e-12 else 1.0
    E_ratio_end = traj[-1]["E_cos"] / E_seed
    peak_w_max = max(s["peak|w|_global"] for s in traj)
    blew_up = bool(run.get("blew_up", False))
    energy_bounded = (not blew_up) and peak_w_max < 1e3  # MODE-III/Arm-C blowup → |ω|→2e5

    # Survives past the step-~11 MODE-III dissolution?
    survives_past_11 = (dissolution_step is None) or (dissolution_step > 11)

    return {
        "name": run["name"],
        "omega_seed": omega_seed,
        "threshold": threshold,
        "dissolution_step": dissolution_step,
        "dissolution_t": dissolution_t,
        "dissolution_compton": (dissolution_t / period) if dissolution_t else None,
        "survives_past_step11": bool(survives_past_11),
        # New honest axis — localization (density-peak, position-independent)
        "loc_seed": loc_seed,
        "loc_end": traj[-1]["loc"],
        "loc_min_post": loc_min_post,
        "loc_dissolution_step": loc_dissolution_step,
        "loc_survives_past_step11": bool(loc_survives_past_11),
        "loc_held": loc_held,
        # Wall-engagement gate
        "g_min_deepest": g_min_deepest,
        "wall_engaged": bool(wall_engaged),
        "frequency_pass_A": bool(freq_pass_A),
        "frequency_pass_B": bool(freq_pass_B),
        "frequency_pass": frequency_pass,
        "compton_periods_post": compton_post,
        "min_wA_post": min_wa_post,
        "min_wB_post": min_wb_post,
        "c_cos_min": min(c_vals),
        "c_cos_max": max(c_vals),
        "c_cos_end": c_vals[-1],
        "topology_preserved": bool(topology_preserved),
        "hand_opposite_at_seed": bool(hand_ok_seed),
        "hand_A_sign_end": float(hand_A_sign),
        "hand_B_sign_end": float(hand_B_sign),
        "hand_retained_end": bool(hand_retained_end),
        "E_ratio_end": E_ratio_end,
        "peak_w_max": peak_w_max,
        "energy_bounded": bool(energy_bounded),
        "blew_up": blew_up,
        "seed_amp_scale": float(run.get("seed_amp_scale", 1.0)),
        "n_sub": run["n_sub"],
        "elapsed_s": run["elapsed_s"],
    }


# ─── Main: three configs, cross-compare vs MODE-III prior, adjudicate ─────────

CONFIGS = {
    "native": dict(use_impedance_boundary=False),
    "wall_only": dict(use_impedance_boundary=True, couple_v_sector=False),
    "wall_sector": dict(use_impedance_boundary=True, couple_v_sector=True),
}


def _fmt(a):
    return "—" if a is None else (f"{a}" if isinstance(a, int) else f"{a:.3f}")


def main(tag: str = "", **run_kwargs) -> dict:
    out_json = OUTPUT_JSON if not tag else OUTPUT_JSON.with_name(
        OUTPUT_JSON.stem + tag + OUTPUT_JSON.suffix
    )
    print("=" * 78, flush=True)
    print("  Option-D (2,3) pair IMPOSE under the (II) moving-Γ=−1 reflective wall")
    print("  consistency-vs-emergence: IMPOSE/STABILITY test (NOT emergence)")
    print(f"  Compare vs MODE-III prior (phase5_topological_pair_injection)  tag={tag or '(primary)'}")
    print("=" * 78, flush=True)

    prior = json.loads(PRIOR_JSON.read_text()) if PRIOR_JSON.exists() else {}
    print(f"  MODE-III prior: mode={prior.get('mode')} freq_pass={prior.get('frequency_pass')} "
          f"c_end={prior.get('c_cos_at_end')} (frozen {prior.get('frozen_at_commit')})\n")

    results = {}
    for name, kw in CONFIGS.items():
        print(f"  [{name}] {kw} ...", flush=True)
        run = run_config(name, kw, **run_kwargs)
        adj = adjudicate(run)
        results[name] = {"adjudication": adj, "trajectory": run["trajectory"],
                         "drive_end_step": run["drive_end_step"], "period": run["period"]}
        print(f"     n_sub={adj['n_sub']:>4d}  {adj['elapsed_s']:6.1f}s  "
              f"seed|ω|_A={adj['omega_seed']:.4f}  fixed-site dissolve@{_fmt(adj['dissolution_step'])}  "
              f"| loc {adj['loc_seed']:.3f}→{adj['loc_end']:.3f} (min_post {adj['loc_min_post']:.3f}) "
              f"loc_dissolve@{_fmt(adj['loc_dissolution_step'])} held={adj['loc_held']}  "
              f"| g_min={_fmt(adj['g_min_deepest'])} engaged={adj['wall_engaged']}  "
              f"c_end={adj['c_cos_end']} peak|ω|={adj['peak_w_max']:.2f} E_end/seed={adj['E_ratio_end']:.2f}",
              flush=True)

    nat = results["native"]["adjudication"]
    wo = results["wall_only"]["adjudication"]
    ws = results["wall_sector"]["adjudication"]

    def loc_dstep(a):
        return a["loc_dissolution_step"] if a["loc_dissolution_step"] is not None else 10**9

    # CRITICAL GATE — a wall config only "helps"/"persists" if its energy is
    # BOUNDED. A blown-up field (parametric pumping of the hard Γ=−1 wall, the
    # (II) §6 instability) concentrates energy into a UV spike, which reads as
    # HIGH localization — a confinement IMPOSTER. Gate every help/persist claim
    # on energy_bounded so the pumping cannot masquerade as the pair surviving.
    any_wall_engaged = bool(wo["wall_engaged"] or ws["wall_engaged"])
    any_wall_pumped = bool(
        (wo["wall_engaged"] and not wo["energy_bounded"])
        or (ws["wall_engaged"] and not ws["energy_bounded"])
    )
    viable = [a for a in (wo, ws) if a["energy_bounded"]]  # bounded wall configs only

    # "best" = the bounded wall config with the highest post-drive localization;
    # if none is bounded, fall back to the least-pumped (lowest peak|ω|) for the report.
    if viable:
        best_adj = max(viable, key=lambda a: a["loc_min_post"])
    else:
        best_adj = min((wo, ws), key=lambda a: a["peak_w_max"])
    best = best_adj["name"]

    # wall_helps = a BOUNDED wall config holds localization meaningfully better
    # than native (blown-up configs are excluded — they do not "help").
    wall_helps = any(
        a["loc_min_post"] > 1.2 * max(nat["loc_min_post"], 1e-6)
        or loc_dstep(a) > loc_dstep(nat) + 4
        for a in viable
    )
    # sector_adds = wall_sector holds better than wall_only, BOTH bounded.
    sector_adds = bool(
        ws["energy_bounded"] and wo["energy_bounded"]
        and (ws["loc_min_post"] > 1.1 * max(wo["loc_min_post"], 1e-6)
             or loc_dstep(ws) > loc_dstep(wo) + 2)
    )

    # Verdict (pre-committed I/II/III), on the localization axis + energy gate.
    persists = bool(
        best_adj["energy_bounded"]
        and best_adj["loc_held"]
        and best_adj["loc_survives_past_step11"]
        and best_adj["wall_engaged"]
        and not nat["loc_held"]
    )
    if persists:
        mode = "I"
        verdict = (
            f"(I) The imposed (2,3) pair PERSISTS under the (II) reflective wall "
            f"({best}: loc held {best_adj['loc_seed']:.3f}→{best_adj['loc_end']:.3f}, "
            f"min_post {best_adj['loc_min_post']:.3f}, ≥{best_adj['compton_periods_post']:.1f} "
            f"Compton post-drive, g_min={_fmt(best_adj['g_min_deepest'])}, energy bounded) where "
            f"native dissolves (loc_min_post {nat['loc_min_post']:.3f}). The confinement WAS the "
            f"missing coupling depth: Option-D impose + reflective confinement = a stable "
            f"lattice-scale pair (Kelvin protection). Fix attributed to: "
            f"{'sector-coupling (3↔2)' if sector_adds else 'the moving boundary alone'}."
        )
    elif wall_helps:
        mode = "II"
        verdict = (
            f"(II) A BOUNDED wall config HELPS but the imposed pair is not stable. Native "
            f"loc_min_post={nat['loc_min_post']:.3f}; best bounded wall ({best}) "
            f"loc_min_post={best_adj['loc_min_post']:.3f}, loc_dissolve@"
            f"{_fmt(best_adj['loc_dissolution_step'])} (native @{_fmt(nat['loc_dissolution_step'])}) "
            f"— but fails the ≥10-Compton hold (loc_held={best_adj['loc_held']}). Residual "
            f"coupling-depth gap. sector-coupling adds over wall-only: {sector_adds}."
        )
    else:
        mode = "III"
        if any_wall_pumped:
            wall_caveat = (
                f"the hard Γ=−1 wall ENGAGES (g_min→{_fmt(min(a['g_min_deepest'] for a in (wo, ws) if a['g_min_deepest'] is not None))}) "
                f"but PARAMETRIC-PUMPS in the coupled+driven engine (peak|ω| wall_only="
                f"{wo['peak_w_max']:.0f}, wall_sector={ws['peak_w_max']:.0f}; E_end/seed "
                f"{wo['E_ratio_end']:.0f}/{ws['E_ratio_end']:.0f}×) — the (II) §6 hard-wall "
                f"instability is NOT tamed by the ported implicit reactance-rotation integrator "
                f"in the coupled+driven configuration. No STABLE confinement of the imposed pair "
                f"was reached at any amplitude (sub-threshold soft at impose amplitude; pumping "
                f"when engaged) → the reflective wall is not the missing ingredient as realized"
            )
        elif any_wall_engaged:
            wall_caveat = (
                "the wall forms a reflective short (g_min<−0.1), stays bounded, yet the pair "
                "still disperses → a clean (III): the coupling-depth issue is independent of "
                "confinement"
            )
        else:
            wall_caveat = (
                "the wall NEVER engaged at the imposed-pair amplitude (g_min≈0, soft) → "
                "INCONCLUSIVE for the wall mechanism: the m_ec²-calibrated (2,3) impose "
                "under-drives its own saturation front, so the wall never forms (distinct from "
                "a clean (III) — see the scale-up diagnostic)"
            )
        verdict = (
            f"(III) The imposed pair does NOT persist as a stable bound state under the wall: "
            f"native loc_min_post={nat['loc_min_post']:.3f}, wall_only={wo['loc_min_post']:.3f} "
            f"(bounded={wo['energy_bounded']}), wall_sector={ws['loc_min_post']:.3f} "
            f"(bounded={ws['energy_bounded']}). Diagnosis: {wall_caveat}."
        )

    print("\n" + "=" * 78)
    print(f"  VERDICT: MODE {mode}")
    print("=" * 78)
    print(f"  {verdict}\n")
    print(f"  Which fix mattered: wall_helps={wall_helps}  sector_adds={sector_adds}  "
          f"best={best}  any_wall_engaged={any_wall_engaged}  any_wall_pumped={any_wall_pumped}")

    payload = {
        "test": "P_phase5_nucleation under (II) moving-Γ=−1 reflective confinement",
        "class": "consistency (Option-D IMPOSE stability test, NOT emergence)",
        "mode": mode,
        "verdict": verdict,
        "wall_helps": bool(wall_helps),
        "sector_coupling_adds": bool(sector_adds),
        "any_wall_engaged": any_wall_engaged,
        "any_wall_pumped": any_wall_pumped,
        "best_config": best,
        "prior_mode_iii": {
            "mode": prior.get("mode"),
            "frequency_pass": prior.get("frequency_pass"),
            "c_cos_at_end": prior.get("c_cos_at_end"),
            "frozen_at_commit": prior.get("frozen_at_commit"),
        },
        "configs": {
            name: {k: v for k, v in r["adjudication"].items()}
            for name, r in results.items()
        },
        "run_kwargs": run_kwargs,
    }
    out_json.write_text(json.dumps(payload, indent=2, default=str), encoding="utf-8")
    print(f"\n  Result JSON: {out_json}")
    # Stash full trajectories for the (optional) animation / result-doc plots.
    def _col(traj, key):
        return np.array([np.nan if s[key] is None else s[key] for s in traj], dtype=float)

    np.savez(
        out_json.with_suffix(".npz"),
        **{
            f"{name}_{key}": _col(r["trajectory"], key)
            for name, r in results.items()
            for key in ("step", "t", "|w|_A", "|w|_B", "|wdot|_A", "|wdot|_B",
                        "peak|w|_global", "loc", "c_cos_global", "E_cos", "h_A", "h_B",
                        "g_min", "max_V_sq", "|Phi_link|_bond")
        },
    )
    print(f"  Trajectories: {out_json.with_suffix('.npz')}")
    return payload


if __name__ == "__main__":
    main()

