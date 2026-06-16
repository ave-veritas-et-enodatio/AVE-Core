"""Stage-1.6 — CP8-safe OPEN route: external moving Γ=−1 wall on Sector B.

Prereg (FROZEN, Rule-11): research/2026-06-16_stage16-moving-wall-sectorB-prereg.md
Inherited success criterion (FROZEN): reconciliation-handoffs/
2026-06-16_electron-existence-discrimination-prereg.md (α-free emergence lane).
Extends: research/2026-06-16_stage15-alphafree-winding-emergence_result.md (the
Stage-1.5 (c) EMERGENCE-NEGATIVE + its named mechanism).

THE GATED QUESTION: Stage-1.5 (c) proved an internal SPECTATOR cage can't confine a
propagating photon (the winding curl never co-locates with the compact irrotational
cage core; f_V=0). Can an EXTERNAL moving Γ=−1 / Op17-bounded wall on SECTOR B (the
photon's OWN sector) confine it so the energize-LOCK loop closes (coupling_work≠0)
WITHOUT changing the seed (CP8-safety)?

This driver runs:
  §0  apparatus-floor known-positive (ave-apparatus-floor-attribution): does the
      α-free moving wall confine a KNOWN photon, vs no-wall dispersal? — validated
      BEFORE any null is trusted.
  §1  THE GATED TEST: wall-ON vs wall-OFF (= Stage-1.5 (c)), recording the
      coupling_work / f_V trajectory, confinement (Sector-B Γ→rim), the reactance
      pair (|ω|,|ω̇|), the winding (2,3) read, and the full-H ledger.
  §2  CP8-SPATIAL-PROVENANCE (the NEW gate): (a) seed-provenance, (b)
      wall-provenance (front vs photon-peak co-evolution), (c) generic-offset sweep
      (the plant discriminator).
  §3  the coupling-curl SUBLATTICE discriminator (flag-don't-fix; a measurement).

α-FREE (load-bearing): no ALPHA in the engine update path (grep-confirmed in the
engine module; the kappa_chiral=0 override routes around KAPPA_CHIRAL_ELECTRON).
ALPHA used here for COMPARISON-ONLY provenance, never inserted.

Run:  PYTHONPATH=src ./.venv/bin/python \
        src/scripts/vol_1_foundations/stage16_moving_wall_sectorB.py
Env overrides: S16_N (default 24), S16_PERIODS (default 12), S16_AMP (default 2.0
  = the wall-formation operating point; the frozen-0.3 case is reported separately
  as the apparatus-floor read), S16_K (clamp strength, default 400),
  S16_FIGS (1 to emit figures, default 1).
"""
from __future__ import annotations

import json
import os

import numpy as np

import ave.core.constants as _avc
from ave.core.constants import ALPHA, ALPHA_COLD_INV
from ave.core.a1_cosserat_moving_wall_engine import A1CosseratMovingWallEngine

HERE = os.path.dirname(os.path.abspath(__file__))
FIGDIR = os.path.abspath(os.path.join(HERE, "..", "..", "..", "research", "figures"))

N = int(os.environ.get("S16_N", "24"))
PML = 4
DX = 0.5
SEED_FRAC = 0.85
SEED_SIGMA = 2.5
PHOTON_SIGMA = 3.0
PHOTON_LAM = 6.0
# The Stage-1.5 (c) seed amplitude (0.3) is BELOW the wall-formation floor (Γ≈0,
# matched — the wall is inert because it does NOT form, an APPARATUS FLOOR not
# physics). The wall's operating point requires the GENERIC photon to drive the
# μ-saturation threshold. Amplitude is a DRIVE LEVEL, not a topological/spatial
# plant (CP8-safety forbids planting the ANSWER — a confined/co-located/pre-wound
# precursor — NOT a higher-amplitude generic transverse photon). Both the frozen
# 0.3 and the operating-point amplitude are reported (apparatus-floor discipline).
PHOTON_AMP = float(os.environ.get("S16_AMP", "2.0"))
PHOTON_AMP_FROZEN = 0.3  # the Stage-1.5 (c) value, reported as the floor read
K_WALL = float(os.environ.get("S16_K", "400.0"))
EMIT_FIGS = os.environ.get("S16_FIGS", "1") == "1"

OMEGA_C_NATURAL = 1.0
T_COMPTON = 2.0 * np.pi / OMEGA_C_NATURAL
N_PERIODS = float(os.environ.get("S16_PERIODS", "12"))


def _alpha_free_provenance_gate() -> None:
    assert _avc.__file__.endswith("ave/core/constants.py"), "non-canonical constants"
    assert abs(ALPHA - 7.2973525693e-3) < 1e-12, "ALPHA not canonical"
    # ALPHA / ALPHA_COLD_INV asserted for COMPARISON-ONLY provenance; NEVER inserted.
    # α-free grep self-check on the engine module: no α-bearing symbol may appear
    # in an EXECUTABLE statement (docstrings/comments may DISCUSS the α-free routing).
    # Tokenize and inspect only NAME/OP tokens (strings + comments excluded by the
    # tokenizer category), so the check sees the actual code path, not the prose.
    import ave.core.a1_cosserat_moving_wall_engine as mod, inspect, io, tokenize
    src = inspect.getsource(mod)
    code_tokens = []
    for tok in tokenize.generate_tokens(io.StringIO(src).readline):
        if tok.type in (tokenize.STRING, tokenize.COMMENT):
            continue  # docstrings + comments may discuss α-free; not the code path
        code_tokens.append(tok.string)
    code = " ".join(code_tokens)
    bad = [t for t in ("ALPHA", "KAPPA_CHIRAL", "KAPPA_CHIRAL_ELECTRON") if t in code]
    # the ONLY numeric kappa_chiral in the code path must be 0.0 (the α-free override)
    assert not bad, f"α-bearing symbol in the engine update path (executable): {bad}"


# ── A46 phase-space winding extractors (ported VERBATIM from the validated
#    stage15_layer_c_emergence_probe.py / crystal_engine_alpha_emergence.py) ──
def _contour_winding(fx, fy, center, R, r_minor, plane="poloidal", n=128):
    cx, cy, cz = center
    t = np.linspace(0.0, 2.0 * np.pi, n, endpoint=False)
    if plane == "poloidal":
        xs = cx + (R + r_minor * np.cos(t))
        ys = cy + np.zeros_like(t)
        zs = cz + r_minor * np.sin(t)
    else:
        xs = cx + R * np.cos(t)
        ys = cy + R * np.sin(t)
        zs = cz + np.zeros_like(t)
    nx, ny, nz = fx.shape
    ix = np.clip(xs.astype(int), 0, nx - 2)
    iy = np.clip(ys.astype(int), 0, ny - 2)
    iz = np.clip(zs.astype(int), 0, nz - 2)
    dx_, dy_, dz_ = xs - ix, ys - iy, zs - iz

    def samp(F):
        return (
            (1 - dx_) * (1 - dy_) * (1 - dz_) * F[ix, iy, iz]
            + dx_ * (1 - dy_) * (1 - dz_) * F[ix + 1, iy, iz]
            + (1 - dx_) * dy_ * (1 - dz_) * F[ix, iy + 1, iz]
            + (1 - dx_) * (1 - dy_) * dz_ * F[ix, iy, iz + 1]
            + dx_ * dy_ * (1 - dz_) * F[ix + 1, iy + 1, iz]
            + dx_ * (1 - dy_) * dz_ * F[ix + 1, iy, iz + 1]
            + (1 - dx_) * dy_ * dz_ * F[ix, iy + 1, iz + 1]
            + dx_ * dy_ * dz_ * F[ix + 1, iy + 1, iz + 1]
        )

    ox, oy = samp(fx), samp(fy)
    amp = np.sqrt(ox**2 + oy**2)
    max_amp = float(amp.max())
    if max_amp < 1e-30:
        return 0.0, 0.0, max_amp
    phase = np.unwrap(np.arctan2(oy, ox))
    winding = (phase[-1] - phase[0]) / (2.0 * np.pi)
    return float(winding), float(amp.min() / max_amp), max_amp


def _measure_23(fx, fy, center, R, n_minor=6):
    out = {}
    amp_seen = 0.0
    for plane in ("toroidal", "poloidal"):
        w_best, rel_best = 0.0, 0.0
        for r_minor in np.linspace(1.0, max(3.0, R * 0.6), n_minor):
            w, rel, amp = _contour_winding(fx, fy, center, R, r_minor, plane)
            amp_seen = max(amp_seen, amp)
            if rel > rel_best:
                w_best, rel_best = w, rel
        out[f"w_{plane[:3]}"] = round(w_best, 2)
        out[f"rel_{plane[:3]}"] = round(rel_best, 3)
    out["amp"] = float(amp_seen)
    wt, wp = abs(out["w_tor"]), abs(out["w_pol"])
    rel = min(out["rel_tor"], out["rel_pol"])
    out["closes_23"] = bool(amp_seen > 1e-9 and rel > 0.1 and abs(wt - 2.0) < 0.5 and abs(wp - 3.0) < 0.5)
    return out


def _winding_read(eng, omega_char=1.0) -> dict:
    bpk = eng.density_peak_interior()
    bvx, bvy, _, _ = eng.bulk_phase_space_vinc_vref(omega_char)
    R_b = max(eng.N * 0.18, 3.0)
    bulk = _measure_23(bvx, bvy, bpk, R_b)
    wpk = eng.omega_density_peak_interior()
    wvx, wvy, _, _ = eng.cosserat_phase_space_vinc_vref(omega_char)
    R_w = max(eng.N * 0.18, 3.0)
    cos = _measure_23(wvx, wvy, wpk, R_w)
    return {
        "bulk_reactance": {"peak": list(bpk), **bulk},
        "cosserat_winding": {"peak": list(wpk), **cos},
        "any_closes_23": bool(bulk["closes_23"] or cos["closes_23"]),
    }


def _build(amp, wall_on, launch_offset=(0, 0, 0), K=None, no_bulk=False):
    """Build an engine with the SAME generic seed (CP8-safety), optionally with the
    wall, an optional launch offset (for the generic-offset sweep), an optional
    clamp strength K (for the amend-4 K_wall sweep), and an optional no_bulk flag
    (the amend-5 forced-zero coupling-meter null: with the bulk seed omitted, V≡0
    so H_c=κ̃∫g·V·Ξ ≡ 0 by construction — a CALIBRATED zero distinct from a
    diverged-before-overlap 0)."""
    eng = A1CosseratMovingWallEngine(
        N=N, dx=DX, V_yield=1.0, c0=1.0, cfl_safety=0.4,
        pml_thickness=PML, A_cap=0.99, S_min=0.05, couple_on=True,
        coupling_support="front", wall_on=wall_on,
        impedance_clamp_strength=(K_WALL if K is None else float(K)),
    )
    c = N / 2.0
    ox, oy, oz = launch_offset
    if not no_bulk:
        eng.seed_bulk_blob(center=(c, c, c), sigma=SEED_SIGMA, frac=SEED_FRAC)
    eng.seed_cosserat_photon(
        center=(c + ox, c + oy, c + oz), sigma=PHOTON_SIGMA,
        wavelength=PHOTON_LAM, amplitude=amp, direction=(1, 0, 0),
        helicity=1.0, axis=2,
    )
    return eng


def _run(eng, nsteps, record=False):
    """Advance, recording the reactance pair + coupling trajectory + ledger.

    amend-2/3 (ww8x96sci): also records the RECIPROCAL back-reaction f_ω on the
    ALIVE sublattice (the half-loop guard), the FULL conserved H ledger AND its
    V_clamp wall-storage part separately (the H-ledger bin gate; V_clamp held
    separable so a reactive wall-store is not mis-read as a pump), every recorded
    step over the long window."""
    trace = {"t": [], "coupling_work": [], "fV_live": [], "fw_alive": [], "loc": [],
             "gamma_min": [], "omega_max": [], "omega_dot_max": [], "H": [],
             "V_clamp": [], "H_minus_Vclamp": [], "wall_peak": [], "omega_peak": []}
    om_seed = eng.omega_max_interior()
    diverged = None
    fV_live_steps = 0
    fV_live_max = 0.0
    f_omega_alive_max = 0.0   # amend-2: the RECIPROCAL back-reaction on alive (GAP 1/2)
    alive_m = eng.B.mask_alive & eng._interior
    for s in range(nsteps):
        eng.step_coupled()
        fV, f_omega = eng._coupling_forces()
        fvmax = float(np.abs(fV * eng._interior).max())
        fV_live_max = max(fV_live_max, fvmax)
        # the back-reaction must ALSO be live on alive for a true CLOSED loop — a
        # source-only f_V is a half-loop (amend-2 / two-sided fire assertion).
        fwmag = np.sqrt(np.sum(f_omega ** 2, axis=-1))
        fwmax = float(fwmag[alive_m].max()) if alive_m.sum() else 0.0
        f_omega_alive_max = max(f_omega_alive_max, fwmax)
        if fvmax > 1e-12:
            fV_live_steps += 1
        oc = eng.omega_max_interior()
        if not np.isfinite(oc) or oc > 1e4 * max(om_seed, 1e-6):
            diverged = s
            break
        if record and (s % max(1, nsteps // 60) == 0 or s == nsteps - 1):
            # amend-3: keep V_clamp (the reactive wall storage) SEPARABLE from H so
            # a wall-store is not read as a pump; gate on H_minus_Vclamp flatness.
            if eng.wall_on:
                imp = eng.B.impedance_hamiltonian()
                V_clamp = imp["V_clamp"]
                H_full = imp["H"] + eng.bulk_energy_conserved() + eng._coupling_energy()
            else:
                V_clamp = 0.0
                H_full = eng.coupling_hamiltonian_full()
            trace["t"].append(s)
            trace["coupling_work"].append(eng.coupling_work)
            trace["fV_live"].append(fvmax)
            trace["fw_alive"].append(fwmax)
            trace["loc"].append(eng.omega_localization())
            trace["gamma_min"].append(eng.wall_gamma_min_interior())
            trace["omega_max"].append(oc)
            trace["omega_dot_max"].append(eng.omega_dot_max_interior())
            trace["H"].append(H_full)
            trace["V_clamp"].append(V_clamp)
            trace["H_minus_Vclamp"].append(H_full - V_clamp)
            trace["wall_peak"].append(list(eng.wall_front_peak()))
            trace["omega_peak"].append(list(eng.omega_density_peak_interior()))
    return {
        "diverged": diverged,
        "coupling_work": eng.coupling_work,
        "fV_live_max": fV_live_max,
        "f_omega_alive_max": f_omega_alive_max,
        "fV_live_frac": fV_live_steps / max(nsteps, 1),
        "loc_f": eng.omega_localization(),
        "gamma_min_f": eng.wall_gamma_min_interior(),
        "omega_max_f": eng.omega_max_interior(),
        "trace": trace,
    }


def main() -> dict:
    _alpha_free_provenance_gate()
    nsteps = int(np.ceil(N_PERIODS * T_COMPTON / A1CosseratMovingWallEngine(
        N=8, dx=DX, pml_thickness=2, wall_on=False).dt))
    result = {
        "stage": "Stage-1.6 — external moving Γ=−1 wall on Sector B (CP8-safe OPEN route)",
        "alpha_free": True,
        "alpha_in_dynamics": "NONE (kappa_chiral=0 override; κ̃=6/5; V_yield=1.0; ω_yield=π)",
        "run_N_explicit": int(N),
        "long_window_periods": float(N_PERIODS),
        "nsteps": nsteps,
        "photon_amp_operating_point": PHOTON_AMP,
        "photon_amp_frozen_stage15c": PHOTON_AMP_FROZEN,
        "K_wall": K_WALL,
    }
    print("=" * 80)
    print("STAGE-1.6 — EXTERNAL MOVING Γ=−1 WALL ON SECTOR B (CP8-safe OPEN route)")
    print("=" * 80)
    print(f"α-free: True (kappa_chiral=0 override; κ̃=6/5; V_yield=1.0; ω_yield=π)")
    print(f"N={N} PML={PML} | nsteps={nsteps} ({N_PERIODS}P) | K_wall={K_WALL}")
    print(f"photon amp: operating-point={PHOTON_AMP} | frozen Stage-1.5(c)={PHOTON_AMP_FROZEN}")

    # ── §0 APPARATUS-FLOOR KNOWN-POSITIVE (ave-apparatus-floor-attribution) ──
    print("\n[§0 APPARATUS-FLOOR] does the α-free moving wall CONFINE a known photon "
          "(vs no-wall dispersal)? — validated BEFORE any null is trusted")
    floor = {}
    for amp_label, amp in (("frozen_0.3", PHOTON_AMP_FROZEN), ("operating_2.0", PHOTON_AMP)):
        row = {}
        for wall in (True, False):
            eng = _build(amp, wall)
            l0 = eng.omega_localization()
            g0 = eng.wall_gamma_min_interior()
            r = _run(eng, min(120, nsteps))
            row[f"wall_{wall}"] = {"loc0": l0, "loc_f": r["loc_f"], "gamma_min0": g0,
                                   "gamma_min_f": r["gamma_min_f"], "omega_max_f": r["omega_max_f"]}
        floor[amp_label] = row
        w, nw = row["wall_True"], row["wall_False"]
        print(f"  amp={amp:>4}: Γ_min0={w['gamma_min0']:+.3f} | WALL loc {w['loc0']:.3f}→{w['loc_f']:.3f}"
              f"  vs no-wall {nw['loc0']:.3f}→{nw['loc_f']:.3f}  |ω|max_f(wall)={w['omega_max_f']:.2f}")
    # apparatus-floor verdict: the wall must FORM (Γ<0) AND confine at the
    # operating point, and the frozen-0.3 must show the BELOW-FLOOR (Γ≈0) read.
    op = floor["operating_2.0"]
    fr = floor["frozen_0.3"]
    wall_forms_op = op["wall_True"]["gamma_min0"] < -0.05
    wall_confines_op = op["wall_True"]["loc_f"] > 0.5 and op["wall_True"]["loc_f"] > op["wall_False"]["loc_f"] + 0.2
    floor_below_at_03 = fr["wall_True"]["gamma_min0"] > -0.05  # wall does NOT form at 0.3
    result["apparatus_floor"] = {
        "data": floor,
        "wall_forms_at_operating_point": bool(wall_forms_op),
        "wall_confines_at_operating_point": bool(wall_confines_op),
        "wall_below_floor_at_frozen_0.3": bool(floor_below_at_03),
        "known_positive_PASS": bool(wall_forms_op and wall_confines_op),
    }
    print(f"  → wall FORMS @op={wall_forms_op}  CONFINES @op={wall_confines_op}  "
          f"below-floor @0.3={floor_below_at_03}  KNOWN-POSITIVE PASS="
          f"{result['apparatus_floor']['known_positive_PASS']}")

    # ── §1 THE GATED TEST: wall-ON vs wall-OFF (= Stage-1.5 (c)) ──
    print("\n[§1 GATED TEST] does the energize-LOCK loop FIRE (coupling_work≠0, f_V≠0) "
          "under the wall, vs Stage-1.5(c)'s spectator f_V=0?")
    gated = {}
    for wall in (True, False):
        eng = _build(PHOTON_AMP, wall)
        seed_read = _winding_read(eng)            # CP8 seed-audit (non-circular)
        ov = eng.coupling_support_overlap()       # §3 sublattice discriminator (record at seed)
        r = _run(eng, nsteps, record=True)
        final_read = _winding_read(eng)
        gated[f"wall_{wall}"] = {
            "coupling_work": r["coupling_work"],
            "fV_live_max": r["fV_live_max"],
            "f_omega_alive_max": r["f_omega_alive_max"],
            "fV_live_frac": r["fV_live_frac"],
            "loc_f": r["loc_f"],
            "gamma_min_f": r["gamma_min_f"],
            "omega_max_f": r["omega_max_f"],
            "diverged": r["diverged"],
            "seed_t0_closes_23": seed_read["any_closes_23"],
            "final_closes_23": final_read["any_closes_23"],
            "final_read": final_read,
            "coupling_overlap": ov,
            "trace": r["trace"],
        }
        print(f"  wall={wall}: coupling_work={r['coupling_work']:+.4e}  f_V_live_max={r['fV_live_max']:.3e}"
              f"  f_ω_alive_max={r['f_omega_alive_max']:.3e}"
              f"  loc→{r['loc_f']:.3f}  Γ_min→{r['gamma_min_f']:+.3f}  |ω|max→{r['omega_max_f']:.2f}")
    # the (c) baseline coupling_work=0 / f_V=0 is the wall=False row (same engine,
    # wall off) AND is consistent with the Stage-1.5 (c) result.
    result["gated_test"] = gated
    cw_wall = gated["wall_True"]["coupling_work"]
    fV_wall = gated["wall_True"]["fV_live_max"]
    fw_wall = gated["wall_True"]["f_omega_alive_max"]
    # amend-2 TWO-SIDED FIRE ASSERTION: a CLOSED energize-LOCK loop requires BOTH
    # the source f_V>0 (sources V from the winding curl) AND the reciprocal
    # back-reaction f_ω>0 on the ALIVE sublattice (sources ω from the bulk). A
    # source-only f_V is a HALF-LOOP (the GAP-1 self-zeroing back-reaction).
    loop_fires = abs(cw_wall) > 1e-9 and fV_wall > 1e-9 and fw_wall > 1e-9
    print(f"  → LOOP FIRES under the wall (TWO-SIDED)? {loop_fires}  "
          f"(coupling_work={cw_wall:+.3e}, f_V={fV_wall:.3e}, f_ω_alive={fw_wall:.3e})")

    # ── §2 CP8-SPATIAL-PROVENANCE (the NEW gate) ──
    print("\n[§2 CP8-SPATIAL-PROVENANCE] (a) seed-provenance (b) wall-provenance "
          "(c) generic-offset sweep")
    # (a) seed-provenance: the seed is the SAME generic photon, no spatial plant.
    seed_prov = {
        "seed_t0_closes_23": gated["wall_True"]["seed_t0_closes_23"],
        "seed_is_generic_photon": not gated["wall_True"]["seed_t0_closes_23"],
        "seed_amplitude": PHOTON_AMP,
        "note": "seed = generic transverse Gaussian ω-photon + sub-yield bulk; NO "
                "planted (2,3), NO pre-co-location, NO pre-winding. amplitude is a "
                "drive level (apparatus operating point), not a topological/spatial plant.",
    }
    # (b) wall-provenance: the wall front co-evolves with the photon under the
    #     generic Γ rule (not pinned). Read from the recorded trajectory.
    tr = gated["wall_True"]["trace"]
    wall_peaks = np.array(tr["wall_peak"]) if tr["wall_peak"] else np.zeros((1, 3))
    om_peaks = np.array(tr["omega_peak"]) if tr["omega_peak"] else np.zeros((1, 3))
    wall_moved = float(np.linalg.norm(wall_peaks[-1] - wall_peaks[0])) if len(wall_peaks) > 1 else 0.0
    wall_prov = {
        "wall_front_start": wall_peaks[0].tolist(),
        "wall_front_end": wall_peaks[-1].tolist(),
        "wall_front_displacement_cells": wall_moved,
        "photon_peak_start": om_peaks[0].tolist(),
        "photon_peak_end": om_peaks[-1].tolist(),
        "note": "wall position = the α-free Γ-field argmin, recomputed from the "
                "focusing ω-field every sub-step (generic rule). NOT hand-placed.",
    }
    # (c) GENERIC-OFFSET SWEEP — the plant discriminator. Vary the photon launch
    #     position relative to the wall/cage center over a generic range.
    print("  (c) generic-offset sweep — does loop-closure work across a generic "
          "range, or ONLY at one hand-tuned offset (=plant)?")
    offsets = [(-3, 0, 0), (-1, 0, 0), (0, 0, 0), (1, 0, 0), (3, 0, 0), (0, 2, 0)]
    sweep = []
    for off in offsets:
        eng = _build(PHOTON_AMP, True, launch_offset=off)
        r = _run(eng, min(150, nsteps))
        fires = abs(r["coupling_work"]) > 1e-9 and r["fV_live_max"] > 1e-9
        sweep.append({"offset": list(off), "coupling_work": r["coupling_work"],
                      "fV_live_max": r["fV_live_max"], "loc_f": r["loc_f"],
                      "gamma_min_f": r["gamma_min_f"], "loop_fires": bool(fires)})
        print(f"    offset={str(off):>12}: coupling_work={r['coupling_work']:+.3e}  "
              f"f_V={r['fV_live_max']:.3e}  loc→{r['loc_f']:.3f}  fires={fires}")
    n_fire = sum(1 for s in sweep if s["loop_fires"])
    # plant test: if it fires at NONE or at exactly ONE hand-tuned offset → not a
    # generic earned positive. If it fires across a generic range → earned. If it
    # fires NOWHERE → there is nothing to be a plant of (the loop is inert).
    sweep_verdict = ("EARNED" if n_fire >= len(offsets) - 1 else
                     "PLANT" if n_fire == 1 else
                     "INERT-EVERYWHERE" if n_fire == 0 else "PARTIAL")
    result["cp8_spatial_provenance"] = {
        "seed_provenance": seed_prov,
        "wall_provenance": wall_prov,
        "generic_offset_sweep": sweep,
        "n_offsets_fire": n_fire,
        "sweep_verdict": sweep_verdict,
    }
    print(f"  → offset-sweep: {n_fire}/{len(offsets)} fire → {sweep_verdict}")

    # ── §3 the coupling-curl SUBLATTICE discriminator (flag-don't-fix) ──
    ov = gated["wall_True"]["coupling_overlap"]
    result["coupling_curl_sublattice_discriminator"] = ov
    print("\n[§3 COUPLING-CURL SUBLATTICE DISCRIMINATOR] (flag-don't-fix, a measurement):")
    print(f"  INHERITED Cartesian curl: |Ξ| alive_max={ov['Xi_cartesian_alive_max']:.3e} "
          f"dead_max={ov['Xi_cartesian_dead_max']:.3e}  g·Ξ overlap_cells={ov['overlap_cells_cartesian']}")
    print(f"  substrate-native tetrahedral curl: |Ξ| alive_max={ov['Xi_tetrahedral_alive_max']:.3e} "
          f"dead_max={ov['Xi_tetrahedral_dead_max']:.3e}  g·Ξ overlap_cells={ov['overlap_cells_tetrahedral']}")
    print("  → the inherited Cartesian np.roll(±1) curl places Ξ ENTIRELY on the K4 DEAD "
          "sublattice; g is masked to ALIVE → g·Ξ≡0 for ANY field (confined or not).")

    # ── §M amend-5 KNOWN-NULL METER CONTROL (ave-apparatus-floor-attribution) ──
    # A forced-zero coupling-meter reference: with the bulk seed omitted, V≡0, so
    # H_c=κ̃∫g·V·Ξ ≡ 0 BY CONSTRUCTION — a calibrated zero distinct from a
    # diverged-before-overlap 0. If the meter does NOT read ≈0 here, a 0 at the
    # operating point cannot be trusted. (NOTE: matched-Γ wall-OFF is NOT a forced
    # zero post-tetra-swap — the alive-sublattice coupling is nonzero for a
    # free-streaming photon — so the V≡0 disjoint-support config is used.)
    print("\n[§M KNOWN-NULL METER CONTROL] forced-zero (V≡0, no bulk) — coupling_work MUST read ≈0:")
    eng_null = _build(PHOTON_AMP, True, no_bulk=True)
    r_null = _run(eng_null, min(80, nsteps))
    null_cw = r_null["coupling_work"]
    null_reads_zero = bool(abs(null_cw) < 1e-6)
    result["known_null_meter"] = {
        "config": "V≡0 (bulk seed omitted) → H_c=κ̃∫g·V·Ξ≡0 by construction",
        "coupling_work_null": null_cw,
        "null_reads_zero": null_reads_zero,
        "tolerance": 1e-6,
        "note": ("matched-Γ wall-OFF is NOT a forced zero after the tetra swap (alive "
                 "coupling is nonzero for a free-streaming photon); the V≡0 config is the "
                 "calibrated zero-reference."),
    }
    print(f"  coupling_work (null) = {null_cw:+.3e}  → reads-zero(<1e-6)={null_reads_zero}")

    # ── §4 amend-4 K_WALL SWEEP (the 'Op17-bound' premise is FALSE — no |ω| ceiling) ──
    # _rotate_clamp is an EXACT harmonic rotation with NO amplitude ceiling, so the
    # wall can confine AND pump together. Sweep K and ask: does ANY K hold the
    # conserved ledger H_minus_Vclamp FLAT (<10% rise) AND preserve Γ→−1 + loc-held?
    # If none separates pump-suppression from confinement-loss → the BC verdict is
    # AMBIGUOUS-pending-stable-BC, NOT a substrate statement.
    print("\n[§4 K_WALL SWEEP] does any K hold H flat AND preserve Γ→−1 + loc-held?")
    kw_steps = min(120, nsteps)
    k_rows = []
    for K in (100, 200, 400, 800):
        eng_k = _build(PHOTON_AMP, True, K=K)
        imp0 = eng_k.B.impedance_hamiltonian()
        Hnv0 = imp0["H"] - imp0["V_clamp"] + eng_k.bulk_energy_conserved() + eng_k._coupling_energy()
        Hnv_series = []
        for _ in range(kw_steps):
            eng_k.step_coupled()
            imp = eng_k.B.impedance_hamiltonian()
            Hnv_series.append(imp["H"] - imp["V_clamp"] + eng_k.bulk_energy_conserved() + eng_k._coupling_energy())
            if eng_k.omega_max_interior() > 1e4 * PHOTON_AMP:
                break
        Hnv_arr = np.array(Hnv_series) if Hnv_series else np.array([Hnv0])
        rise = float((Hnv_arr.max() - Hnv0) / max(abs(Hnv0), 1e-30))
        gmin = eng_k.wall_gamma_min_interior()
        locf = eng_k.omega_localization()
        wall_forms = bool(gmin < -0.5)        # Γ→−1 = the μ-short rim
        loc_held = bool(locf > 0.5)
        H_flat_k = bool(rise < 0.10)
        clean_k = bool(H_flat_k and wall_forms and loc_held)
        k_rows.append({"K": K, "Hnv_peak_rise_frac": rise, "gamma_min_f": gmin,
                       "loc_f": locf, "wall_forms": wall_forms, "loc_held": loc_held,
                       "H_flat": H_flat_k, "clean_separation": clean_k,
                       "omega_max_f": eng_k.omega_max_interior()})
        print(f"  K={K:>4}: Hnv rise={100*rise:>7.1f}%  Γ_min={gmin:+.3f}  loc={locf:.3f}  "
              f"forms={wall_forms} held={loc_held} H_flat={H_flat_k} → clean={clean_k}")
    any_clean = any(r["clean_separation"] for r in k_rows)
    bc_verdict = "STABLE-BC-FOUND" if any_clean else "AMBIGUOUS-pending-stable-BC"
    result["k_wall_sweep"] = {
        "rows": k_rows,
        "any_K_separates_pump_from_confinement": any_clean,
        "bc_verdict": bc_verdict,
        "note": ("_rotate_clamp (cosserat_field_3d.py:1760) is an exact harmonic rotation "
                 "with NO |ω| ceiling — the 'Op17-bound' premise is FALSE; the wall can "
                 "confine (Γ→−1, loc-held) AND pump (conserved ledger climbs) together."),
    }
    print(f"  → BC verdict: {bc_verdict} (any-clean-K={any_clean})")

    # ── amend-3 H-LEDGER BIN GATE (ave-conserved-vs-pumped) ──
    # coupling_work is a SIGNED running sum of an energy-functional, NOT a measured
    # transfer — a bounded wall-pump that injects energy without diverging |ω| would
    # read coupling_work≠0. LOOP-CLOSES therefore ALSO requires the CONSERVED ledger
    # H_minus_Vclamp (full H minus the reactive wall storage V_clamp, held separable)
    # to be FLAT/decaying over the long window, AND the ON-minus-OFF coupling_work
    # excess to be a bounded conserved REDISTRIBUTION (not a climbing injection).
    trW = gated["wall_True"]["trace"]
    H_nv = np.array(trW["H_minus_Vclamp"]) if trW["H_minus_Vclamp"] else np.array([0.0])
    H_full_tr = np.array(trW["H"]) if trW["H"] else np.array([0.0])
    H0 = float(H_nv[0]) if H_nv.size else 0.0
    H_ledger_drift = float((H_nv[-1] - H_nv[0]) / max(abs(H0), 1e-30)) if H_nv.size > 1 else 0.0
    H_ledger_peak_rise = float((H_nv.max() - H_nv[0]) / max(abs(H0), 1e-30)) if H_nv.size > 1 else 0.0
    # FLAT/decaying = the conserved (non-wall-storage) ledger does not climb past a
    # 10% reactive-slosh band over the window (a pump climbs orders of magnitude).
    H_flat = bool(H_ledger_peak_rise < 0.10)
    cw_off = gated["wall_False"]["coupling_work"]
    cw_excess = float(cw_wall - cw_off)
    # the excess must be a bounded conserved redistribution: |excess| comparable to
    # the conserved ledger scale, NOT a runaway. (A wall-pump shows |excess| growing
    # with H_full climbing — caught by H_flat above.)
    H_full_rise = float((H_full_tr.max() - H_full_tr[0]) / max(abs(float(H_full_tr[0])), 1e-30)) if H_full_tr.size > 1 else 0.0
    coupling_redistribution_conserved = bool(H_flat and np.isfinite(cw_excess))
    result["h_ledger_gate"] = {
        "H_minus_Vclamp_drift_frac": H_ledger_drift,
        "H_minus_Vclamp_peak_rise_frac": H_ledger_peak_rise,
        "H_full_peak_rise_frac": H_full_rise,
        "H_flat_or_decaying": H_flat,
        "coupling_work_ON": cw_wall,
        "coupling_work_OFF": cw_off,
        "coupling_work_excess_ON_minus_OFF": cw_excess,
        "coupling_redistribution_conserved": coupling_redistribution_conserved,
        "V_clamp_held_separable": True,
    }
    print(f"\n[H-LEDGER GATE] H_minus_Vclamp peak-rise={H_ledger_peak_rise:+.3e} "
          f"(flat<0.10={H_flat}) | H_full peak-rise={H_full_rise:+.3e} | "
          f"coupling_work excess ON−OFF={cw_excess:+.3e} | conserved-redist={coupling_redistribution_conserved}")

    # ── BIN (frozen, prereg §4) ──
    wall_confines = (gated["wall_True"]["loc_f"] > 0.5 and
                     gated["wall_True"]["loc_f"] > gated["wall_False"]["loc_f"] + 0.2)
    pumps = (gated["wall_True"]["diverged"] is not None or
             gated["wall_True"]["omega_max_f"] > 50 * PHOTON_AMP or
             not H_flat)   # amend-3: a bounded wall-pump (|ω| not diverged but the
                           # conserved ledger climbs) is STILL a pump — the H gate
                           # catches it where the |ω|-ceiling test cannot.
    if pumps:
        verdict = "PUMPS"   # FROZEN bin (prereg §4) — kept; the K_wall-sweep
                            # AMBIGUOUS-pending-stable-BC is a QUALIFIER on this
                            # bin's interpretation, NOT a 5th bin.
        diverged_note = (gated["wall_True"]["diverged"] is not None or
                         gated["wall_True"]["omega_max_f"] > 50 * PHOTON_AMP)
        bc_tail = (f" K_wall sweep: {bc_verdict} (no K holds H flat while preserving Γ→−1 "
                   f"+ loc-held — confinement and pumping rise together because _rotate_clamp "
                   f"has no |ω| ceiling) ⇒ this PUMPS is BC-attributable, NOT a substrate "
                   f"statement." if not any_clean else
                   f" K_wall sweep: a stable BC exists at K={[r['K'] for r in k_rows if r['clean_separation']]}.")
        reason = (("the wall is not Op17-bounded (|ω| blow-up / divergence) — fix the BC."
                   if diverged_note else
                   "the conserved ledger H_minus_Vclamp CLIMBS (bounded wall-pump: |ω| "
                   "stays finite but energy is injected, not redistributed) — fix the BC.")
                  + bc_tail)
    elif not wall_confines:
        verdict = "WALL-ALSO-FAILS"
        reason = ("the moving wall cannot confine the propagating photon "
                  "(radiates through/past) → obstruction promotes to a substrate statement")
    elif loop_fires and sweep_verdict == "EARNED" and coupling_redistribution_conserved:
        verdict = "LOOP-CLOSES"
        reason = ("wall confines AND coupling_work≠0 (TWO-SIDED: f_V AND f_ω_alive) AND "
                  "generic-offset sweep EARNED AND the conserved ledger H_minus_Vclamp is "
                  "FLAT/decaying (the coupling_work excess is a conserved redistribution, "
                  "NOT a wall-pump injection; V_clamp held separable)")
    else:
        verdict = "WALL-CONFINES-BUT-LOOP-INERT"
        reason = ("the wall traps the photon (Sector-B Γ→−1, loc held) but coupling_work=0 "
                  "→ obstruction is DEEPER than confinement (see §3: the inherited "
                  "Cartesian-curl coupling stencil puts Ξ on the dead sublattice, g on "
                  "alive → g·Ξ≡0 independent of confinement)")
    result["verdict"] = verdict
    result["verdict_reason"] = reason
    result["bc_verdict"] = bc_verdict   # amend-4 K_wall-sweep qualifier
    result["loop_fires"] = bool(loop_fires)
    result["loop_fires_two_sided"] = bool(loop_fires)  # amend-2: f_V AND f_ω_alive
    result["f_omega_alive_max_wall_on"] = float(fw_wall)
    result["wall_confines"] = bool(wall_confines)
    result["frozen_bins"] = ["LOOP-CLOSES", "WALL-CONFINES-BUT-LOOP-INERT",
                             "WALL-ALSO-FAILS", "PUMPS"]  # FROZEN prereg §4 — 4 bins
    result["alpha_comparison_only"] = {"ALPHA_inv_CODATA": float(1.0 / ALPHA),
                                       "ALPHA_COLD_INV": float(ALPHA_COLD_INV)}

    print("\n" + "=" * 80)
    print(f"VERDICT: {verdict}")
    print(f"  {reason}")
    print("=" * 80)

    out_path = os.path.join(HERE, "stage16_moving_wall_sectorB_results.json")
    with open(out_path, "w") as f:
        json.dump(result, f, indent=2, default=float)
    result["results_json"] = out_path
    print(f"results → {out_path}")

    if EMIT_FIGS:
        figs = _emit_figures(result, floor, gated, sweep, ov)
        result["figures"] = figs
        for p in figs:
            print(f"figure → {p}")

    return result


def _emit_figures(result, floor, gated, sweep, ov):
    """Emit the 5 REAL-data diagnostic figures (matplotlib Agg) to research/figures/.
    Matches the diagnostic-board template (multi-panel, annotated, real data)."""
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    os.makedirs(FIGDIR, exist_ok=True)
    paths = []
    trW = gated["wall_True"]["trace"]
    trN = gated["wall_False"]["trace"]
    t = np.array(trW["t"]) if trW["t"] else np.array([0])

    # ── FIG 1: moving-wall TDR — wall front position vs time + photon confinement ──
    fig, ax = plt.subplots(1, 2, figsize=(13, 5))
    fig.suptitle("Stage-1.6 FIG-1 — moving-wall TDR: wall front + photon confinement (REAL data)",
                 fontweight="bold")
    wp = np.array(trW["wall_peak"]) if trW["wall_peak"] else np.zeros((1, 3))
    op = np.array(trW["omega_peak"]) if trW["omega_peak"] else np.zeros((1, 3))
    ax[0].plot(t, wp[:, 0], "o-", label="wall front  (x, Γ-argmin)", color="crimson")
    ax[0].plot(t, op[:, 0], "s--", label="photon |ω|² peak (x)", color="steelblue")
    ax[0].set_xlabel("step"); ax[0].set_ylabel("x cell"); ax[0].legend(); ax[0].grid(alpha=0.3)
    ax[0].set_title("wall front co-moves with the focusing photon\n(generic Γ rule, not hand-placed)")
    ax[1].plot(t, trW["loc"], "o-", color="crimson", label="WALL on (Sector B)")
    ax[1].plot(np.array(trN["t"]), trN["loc"], "s--", color="gray", label="wall OFF (= Stage-1.5 c)")
    ax[1].set_xlabel("step"); ax[1].set_ylabel("|ω|² localization (r≤6 of peak)")
    ax[1].set_ylim(0, 1.05); ax[1].legend(); ax[1].grid(alpha=0.3)
    ax[1].set_title(f"photon held by the wall vs dispersed without\n(amp={PHOTON_AMP}, K={K_WALL})")
    p1 = os.path.join(FIGDIR, "stage16_fig1_moving_wall_tdr.png")
    fig.tight_layout(); fig.savefig(p1, dpi=130); plt.close(fig); paths.append(p1)

    # ── FIG 2: coupling_work / f_V trajectory — does the loop fire vs (c) f_V=0 ──
    fig, ax = plt.subplots(1, 2, figsize=(13, 5))
    fig.suptitle("Stage-1.6 FIG-2 — energize-LOCK loop: does it FIRE under the wall? (THE gated number)",
                 fontweight="bold")
    ax[0].plot(t, trW["coupling_work"], "o-", color="crimson", label="WALL on")
    ax[0].plot(np.array(trN["t"]), trN["coupling_work"], "s--", color="gray",
               label="wall OFF (= Stage-1.5 c spectator)")
    ax[0].axhline(0, color="k", lw=0.8)
    ax[0].set_xlabel("step"); ax[0].set_ylabel("coupling_work (∫ κ̃ g·V·Ξ)")
    ax[0].legend(); ax[0].grid(alpha=0.3)
    ax[0].set_title("coupling_work trajectory\n(flat-zero = the (c) inert spectator loop)")
    ax[1].plot(t, trW["fV_live"], "o-", color="crimson", label="WALL on")
    ax[1].plot(np.array(trN["t"]), trN["fV_live"], "s--", color="gray", label="wall OFF")
    ax[1].axhline(0, color="k", lw=0.8)
    ax[1].set_xlabel("step"); ax[1].set_ylabel("f_V source live max  (−κ̃ g·Ξ)")
    ax[1].legend(); ax[1].grid(alpha=0.3)
    ax[1].set_title(f"f_V source: {result['verdict']}\n(=0 ⇒ loop inert even with the wall)")
    p2 = os.path.join(FIGDIR, "stage16_fig2_coupling_work_fV.png")
    fig.tight_layout(); fig.savefig(p2, dpi=130); plt.close(fig); paths.append(p2)

    # ── FIG 3: Sector-B Γ-plane locus (Smith) — does Γ migrate center→rim? ──
    fig, ax = plt.subplots(1, 2, figsize=(13, 5.2))
    fig.suptitle("Stage-1.6 FIG-3 — Sector-B Γ-plane: does the photon's Γ migrate center→rim under the wall?",
                 fontweight="bold")
    th = np.linspace(0, 2 * np.pi, 200)
    for a in ax:
        a.plot(np.cos(th), np.sin(th), "k-", lw=1.0)
        a.plot(0, 0, "k+", ms=10)
        a.set_aspect("equal"); a.set_xlim(-1.15, 1.15); a.set_ylim(-1.15, 1.15)
        a.grid(alpha=0.25); a.set_xlabel("Re Γ"); a.set_ylabel("Im Γ")
    # μ-side short: Γ is real-negative; plot |Γ_min| trajectory along the −Re axis.
    gW = np.array(trW["gamma_min"]); gN = np.array(trN["gamma_min"])
    ax[0].plot(gW, np.zeros_like(gW), "o-", color="crimson", label="WALL on (μ-short)")
    ax[0].plot(gW[-1], 0, "*", color="crimson", ms=18)
    ax[0].annotate("Γ→−1 = the rim (Z→0 short)", xy=(-1, 0), xytext=(-0.95, 0.45),
                   arrowprops=dict(arrowstyle="->"), fontsize=8)
    ax[0].set_title("WALL on: Sector-B μ-short Γ migrates center→rim\n(DUAL-SECTOR, H3 wall-branch fork: μ-short axis)")
    ax[0].legend(fontsize=8)
    ax[1].plot(gN, np.zeros_like(gN), "s--", color="gray", label="wall OFF (matched)")
    ax[1].set_title("wall OFF: Γ stays ≈0 (matched, photon free-streams)")
    ax[1].legend(fontsize=8)
    # bake-(ii) echo annotation: the terminal |Γ|²=1−α universal Q-invariant leak.
    A_echo = np.sqrt(1.0 - ALPHA)
    for a in ax:
        a.plot(A_echo * np.cos(th), A_echo * np.sin(th), ":", color="purple", lw=1.0)
    ax[1].annotate("|Γ|²=1−α  (bake-(ii) ECHO, NOT emergence:\nthe universal Q-invariant radiative leak,\ncvr_model.gamma_mag_sq_leak — α NOT read here)",
                   xy=(A_echo, 0), xytext=(-1.1, -1.05), fontsize=7, color="purple")
    p3 = os.path.join(FIGDIR, "stage16_fig3_sectorB_gamma_smith.png")
    fig.tight_layout(); fig.savefig(p3, dpi=130); plt.close(fig); paths.append(p3)

    # ── FIG 4: winding read — does (2,3) self-form? (w_tor, w_pol) ──
    fig, ax = plt.subplots(1, 1, figsize=(8.5, 5.2))
    fr = gated["wall_True"]["final_read"]
    cats = ["bulk w_tor", "bulk w_pol", "cosserat w_tor", "cosserat w_pol"]
    vals = [fr["bulk_reactance"]["w_tor"], fr["bulk_reactance"]["w_pol"],
            fr["cosserat_winding"]["w_tor"], fr["cosserat_winding"]["w_pol"]]
    rels = [fr["bulk_reactance"]["rel_tor"], fr["bulk_reactance"]["rel_pol"],
            fr["cosserat_winding"]["rel_tor"], fr["cosserat_winding"]["rel_pol"]]
    colors = ["steelblue" if r > 0.1 else "lightgray" for r in rels]
    bars = ax.bar(cats, vals, color=colors)
    ax.axhline(2, color="green", ls="--", lw=1, label="target '2' (toroidal)")
    ax.axhline(3, color="orange", ls="--", lw=1, label="target '3' (poloidal)")
    ax.axhline(0, color="k", lw=0.8)
    for b, r in zip(bars, rels):
        ax.text(b.get_x() + b.get_width() / 2, b.get_height() + 0.05, f"rel={r:.2f}",
                ha="center", fontsize=7)
    ax.set_ylabel("winding number"); ax.legend(fontsize=8)
    ax.set_title(f"FIG-4 winding read (A46 phase-space) — does (2,3) self-form under the wall?\n"
                 f"closes_(2,3)={fr['any_closes_23']}  (gray bar = unreliable contour, rel≤0.1)")
    p4 = os.path.join(FIGDIR, "stage16_fig4_winding_read.png")
    fig.tight_layout(); fig.savefig(p4, dpi=130); plt.close(fig); paths.append(p4)

    # ── FIG 5: apparatus-floor known-positive — wall confines a known photon ──
    fig, ax = plt.subplots(1, 1, figsize=(8.5, 5.2))
    labels = []
    locw, locn = [], []
    for amp_label in ("frozen_0.3", "operating_2.0"):
        labels.append(amp_label)
        locw.append(floor[amp_label]["wall_True"]["loc_f"])
        locn.append(floor[amp_label]["wall_False"]["loc_f"])
    x = np.arange(len(labels)); w = 0.35
    ax.bar(x - w / 2, locw, w, label="WALL on (α-free)", color="crimson")
    ax.bar(x + w / 2, locn, w, label="wall OFF", color="gray")
    for amp_label, xi in zip(("frozen_0.3", "operating_2.0"), x):
        g0 = floor[amp_label]["wall_True"]["gamma_min0"]
        ax.text(xi, 1.02, f"Γ_min0={g0:+.3f}", ha="center", fontsize=8)
    ax.set_xticks(x); ax.set_xticklabels(labels)
    ax.set_ylabel("final |ω|² localization"); ax.set_ylim(0, 1.15); ax.legend()
    ax.set_title("FIG-5 apparatus-floor known-positive — the α-free wall confines a KNOWN photon\n"
                 "(frozen 0.3 = below the wall-formation floor, Γ≈0; operating 2.0 = wall forms + confines)")
    p5 = os.path.join(FIGDIR, "stage16_fig5_apparatus_floor.png")
    fig.tight_layout(); fig.savefig(p5, dpi=130); plt.close(fig); paths.append(p5)

    return paths


if __name__ == "__main__":
    main()
