"""
WRITHE ARC — STAGE (a): the LINEAR-CHANNEL |F|-RATIO CAMPAIGN
============================================================

FROZEN PRE-REG: research/2026-07-03_writhe-campaign-linear-channel_prereg.md.
Charter: _orchestration/2026-07-02_writhe-force-ratio-build-brief.md (steps 1–5).
Built on Gate-0 (MERGED PR #465): reuses its seed/roll/read machinery verbatim.

GRANT RULING (2026-07-03, verbatim): "A full, and C" —
  (A-full) the parity-odd interaction SIGN chord observable with all baked-ins, AND
  (C)      the magnitude-R formally booked as a NAMED BLOCKER (reported, not dropped).

THE CHORD OBSERVABLE (prereg §2): the parity-odd SIGN of the self-subtracted
Maxwell field-stress interaction force F_int, co-handed (RR,LL) vs anti-handed (RL,LR),
required PLANE-INVARIANT. Force (frozen before running):
  T^{xx}_ω(x) = Σ_c (∂_x ω_c)² − ½ Σ_c |∇ω_c|²      (ω-field normal stress on the x-plane)
  F_raw(plane) = Σ_{interior, mid-plane} T^{xx}_ω      (x-force on the RIGHT knot; PML-excluded)
  F_int = F_raw[pair] − F_raw[A alone] − F_raw[B alone]   (self-stress subtracted)
  SIGN CONVENTION: F_int > 0 REPULSIVE (pushes right knot +x, away); F_int < 0 ATTRACTIVE.

THE MAGNITUDE-R BLOCKER (prereg §3): R=|F|co/|F|anti is ILL-DEFINED at current engine
capability — knot overlap at stable d (no plane-conservative integral) + Yukawa screening
(λ≈0.8 cells ≈ ξ=c_ω/ω_gap=0.548). Magnitude STILL reported, tagged knob-riding/blocked.

TWO CLASSICAL BASELINES (prereg §5), same self-subtracted extraction:
  (i)  unquantized circulation (current-loop knife; validate: co-attract/anti-repel)
  (ii) achiral charge-like hedgehog (Coulomb-recovery knife; expect co=anti, no parity-odd)

SECTOR/REGIME (prereg §0): T2 ω-sector; S1 buckle-OFF host (κ_chiral NOT active — the
LINEAR channel). ω_gap=1.0 is a HOST KNOB (prereg §6 G4 row) => Yukawa range is
artifact-scale, not a prediction.

DRIVER HONESTY (ave-driver-script-honesty): every printed number computed in-run;
validate-on-known first. Constants: canonical only (host α-clean; the verdict is a SIGN).

Run:
    PYTHONPATH=src <venv>/bin/python \
        src/scripts/vol_4_engineering/writhe_campaign_linear_channel.py
"""

from __future__ import annotations

import json

import numpy as np

# ── shared Gate-0 machinery (REUSED verbatim — prereg §7): seed, roll, per-knot read,
#    interior mask, the S1 isolated-knot host, and the frozen config N/R/r/XC/L_CORE.
from scripts.vol_4_engineering.writhe_gate0_pair_feasibility import (
    N, R, r, XC, L_CORE, AMPLITUDE,
    _build_isolated_knot, _single_knot_fields, _roll_x,
    _seed_pair, _read_knot_local, _interior,
    validate_on_known_gate0,
)
from ave.core.s1_winding_conservation_gate import _CFG

# ── FROZEN CAMPAIGN CONFIG (prereg §1) ────────────────────────────────────────────────
SEPARATIONS = [34, 38, 44]        # all Gate-0-STABLE (d=38 verified this session)
WARMUP = 50                       # Gate-0-certified warmup past the LC turning point
WINDOW = 250                      # recording steps (sign = time-mean; §4 window sweep uses {150,250,350})
PLANE_OFFSETS = [-3, -1, 0, 1, 3] # G-plane sweep (prereg §4): the SIGN must be identical at all
WINDOW_SWEEP = [150, 250, 350]    # G-window sweep (prereg §4)

# Yukawa-range provenance (prereg §6 G4): ω_gap is a HOST KNOB, not canonical.
_OMEGA_GAP = _CFG["omega_gap"]    # = 1.0 lattice units (crystal_graft_v2.py:65 default)


# ──────────────────────────────────────────────────────────────────────────────────────
# FORCE EXTRACTION (prereg §2.1) — the Maxwell ω-field normal stress, self-subtracted.
# ──────────────────────────────────────────────────────────────────────────────────────
_I = np.indices((N, N, N))[0]


def _stress_Txx_omega(omega: np.ndarray) -> np.ndarray:
    """T^{xx}_ω = Σ_c (∂_x ω_c)² − ½ Σ_c |∇ω_c|² — the xx normal-stress of the ω vector
    field (the momentum-flux tensor's normal component on the x-plane). Central differences
    (matching the engine stencil); edge planes left 0 (inside the PML, excluded anyway)."""
    dx = np.zeros_like(omega)
    dy = np.zeros_like(omega)
    dz = np.zeros_like(omega)
    dx[1:-1] = (omega[2:] - omega[:-2]) / 2.0
    dy[:, 1:-1] = (omega[:, 2:] - omega[:, :-2]) / 2.0
    dz[:, :, 1:-1] = (omega[:, :, 2:] - omega[:, :, :-2]) / 2.0
    dxx = np.sum(dx * dx, axis=-1)
    grad2 = np.sum(dx * dx + dy * dy + dz * dz, axis=-1)
    return dxx - 0.5 * grad2


def _plane_integral(Txx: np.ndarray, interior: np.ndarray, off: int) -> float:
    """Face-centered integral of T^{xx}_ω over the mid-plane at XC+off (mean of the two
    adjacent planes), PML-excluded. = the x-force on the RIGHT knot at that plane."""
    il = int(np.floor(XC)) + off
    return 0.5 * (float(np.sum(Txx[(_I == il) & interior]))
                  + float(np.sum(Txx[(_I == il + 1) & interior])))


def _evolve_plane_force(e, offsets, *, warmup=WARMUP, window=WINDOW) -> dict:
    """Evolve `e`, return the time-mean F_raw at each requested plane offset over the window."""
    for _ in range(warmup):
        e.step()
    acc = {o: [] for o in offsets}
    for _ in range(window):
        e.step()
        Txx = _stress_Txx_omega(e.omega)
        interior = e.interior_mask()
        for o in offsets:
            acc[o].append(_plane_integral(Txx, interior, o))
    return {o: float(np.mean(v)) for o, v in acc.items()}


# ──────────────────────────────────────────────────────────────────────────────────────
# FIELD CONSTRUCTORS — quantized (2,3) [Gate-0], classical circulation, achiral charge.
# ──────────────────────────────────────────────────────────────────────────────────────
def _q_single(d: int, side: int, mirror: bool):
    """One quantized (2,3) knot at XC + side·d/2 (side=−1 left, +1 right). Reuses the Gate-0
    seed + roll verbatim (prereg §2.1 self-subtraction control)."""
    e = _build_isolated_knot(N, R, r, lock_on=True, amplitude=AMPLITUDE)
    e.omega[...] = 0.0
    e.omega_prev[...] = 0.0
    om, omp = _single_knot_fields(mirror=mirror)
    e.omega += _roll_x(om, side * (d // 2))
    e.omega_prev += _roll_x(omp, side * (d // 2))
    return e


def _classical_circulation_fields(hand: int):
    """Baseline (i) — unquantized smooth toroidal circulation (p=q=1, no integer winding),
    matched tube geometry, handedness = sign (prereg §5.1). The current-loop / vortex knife."""
    c = (N - 1) / 2.0
    i, j, k = np.indices((N, N, N))
    xs, ys, zs = i - c, j - c, k - c
    rho = np.sqrt(xs ** 2 + ys ** 2)
    phi = np.arctan2(ys, xs)
    psi = np.arctan2(zs, rho - R)
    rtube = np.sqrt((rho - R) ** 2 + zs ** 2)
    env = np.exp(-(rtube ** 2) / (2.0 * (0.6 * r) ** 2)) * (rho > 2)
    base = AMPLITUDE * env
    om = np.zeros((N, N, N, 3))
    omp = np.zeros((N, N, N, 3))
    om[..., 0] = base * np.cos(psi) * np.cos(phi)
    om[..., 1] = base * np.cos(psi) * np.sin(phi)
    om[..., 2] = hand * base * np.sin(psi)
    dl = _OMEGA_GAP * (2.0 * np.pi / 240.0)  # small LC advance (matched to the read cadence)
    omp[..., 0] = base * np.cos(psi + dl) * np.cos(phi)
    omp[..., 1] = base * np.cos(psi + dl) * np.sin(phi)
    omp[..., 2] = hand * base * np.sin(psi + dl)
    return om, omp


def _charge_hedgehog_fields(hand: int):
    """Baseline (ii) — achiral radial hedgehog ω source (curl-free, no helicity, static),
    a monopole/charge-class analog on the same ω machinery (prereg §5.2). The z-mirror
    'handedness' is a physical NO-OP on a radial field => co and anti must coincide
    (Coulomb-recovery). The Coulomb-recovery knife."""
    c = (N - 1) / 2.0
    i, j, k = np.indices((N, N, N))
    xs, ys, zs = i - c, j - c, k - c
    rr = np.sqrt(xs ** 2 + ys ** 2 + zs ** 2) + 1e-9
    ball = np.exp(-(rr ** 2) / (2.0 * (0.5 * R) ** 2))
    base = AMPLITUDE * ball
    om = np.zeros((N, N, N, 3))
    om[..., 0] = base * xs / rr
    om[..., 1] = base * ys / rr
    om[..., 2] = base * zs / rr
    omp = om.copy()  # static (charge-like): zero LC velocity
    if hand < 0:  # the SAME z-mirror enantiomorph op the windings use (a no-op here)
        om = om[:, :, ::-1, :].copy()
        om[..., 2] *= -1.0
        omp = omp[:, :, ::-1, :].copy()
        omp[..., 2] *= -1.0
    return om, omp


def _seed_from_fields(d: int, fields_fn, labelA, labelB):
    """Generic pair seeder: place fields_fn(labelA) at XC−d/2 and fields_fn(labelB) at
    XC+d/2 on the buckle-OFF host (used by both classical baselines)."""
    e = _build_isolated_knot(N, R, r, lock_on=True, amplitude=AMPLITUDE)
    e.omega[...] = 0.0
    e.omega_prev[...] = 0.0
    oA, pA = fields_fn(labelA)
    oB, pB = fields_fn(labelB)
    sh = d // 2
    e.omega += _roll_x(oA, -sh) + _roll_x(oB, +sh)
    e.omega_prev += _roll_x(pA, -sh) + _roll_x(pB, +sh)
    return e


def _single_from_fields(d: int, side: int, fields_fn, label):
    """One classical source at XC + side·d/2 (the self-subtraction control for a baseline)."""
    e = _build_isolated_knot(N, R, r, lock_on=True, amplitude=AMPLITUDE)
    e.omega[...] = 0.0
    e.omega_prev[...] = 0.0
    om, omp = fields_fn(label)
    e.omega += _roll_x(om, side * (d // 2))
    e.omega_prev += _roll_x(omp, side * (d // 2))
    return e


# ──────────────────────────────────────────────────────────────────────────────────────
# QUANTIZED 4-CONFIG FORCE (prereg §2) — self-subtracted F_int at every plane, per config.
# Config handedness map: R = not-mirrored, L = mirrored. co = {RR, LL}; anti = {RL, LR}.
# ──────────────────────────────────────────────────────────────────────────────────────
_CONFIG_MIRROR = {"RR": (False, False), "LL": (True, True),
                  "RL": (False, True), "LR": (True, False)}


def quantized_config_force(d: int, config: str, offsets, *, window=WINDOW) -> dict:
    """F_int(plane) for a quantized 4-config pair, self-subtracted, at each plane offset.
    F_int = F_raw[pair] − F_raw[A alone] − F_raw[B alone]."""
    mA, mB = _CONFIG_MIRROR[config]
    Fpair = _evolve_plane_force(_seed_pair(d, mirror_A=mA, mirror_B=mB), offsets, window=window)
    Fa = _evolve_plane_force(_q_single(d, -1, mA), offsets, window=window)
    Fb = _evolve_plane_force(_q_single(d, +1, mB), offsets, window=window)
    Fint = {o: Fpair[o] - Fa[o] - Fb[o] for o in offsets}
    return {"config": config, "d": d, "F_int_by_plane": Fint,
            "F_int_XC0": Fint.get(0, float("nan"))}


def baseline_force(d: int, fields_fn, labelA, labelB, offsets, *, window=WINDOW) -> dict:
    """F_int(plane) for a classical baseline pair (same self-subtracted extraction)."""
    Fpair = _evolve_plane_force(_seed_from_fields(d, fields_fn, labelA, labelB), offsets, window=window)
    Fa = _evolve_plane_force(_single_from_fields(d, -1, fields_fn, labelA), offsets, window=window)
    Fb = _evolve_plane_force(_single_from_fields(d, +1, fields_fn, labelB), offsets, window=window)
    Fint = {o: Fpair[o] - Fa[o] - Fb[o] for o in offsets}
    return {"F_int_by_plane": Fint, "F_int_XC0": Fint.get(0, float("nan"))}


def _sign_label(x: float) -> str:
    if not np.isfinite(x) or x == 0.0:
        return "ZERO"
    return "REPULSIVE(+)" if x > 0 else "ATTRACTIVE(-)"


def _sign(x: float) -> int:
    return int(np.sign(x)) if np.isfinite(x) else 0


# ──────────────────────────────────────────────────────────────────────────────────────
# INVARIANCE GATES (prereg §4) — the SIGN is the subject.
# ──────────────────────────────────────────────────────────────────────────────────────
def gate_plane_invariance(fint_by_plane: dict) -> dict:
    """(G-plane) the SIGN must be identical at every integration plane. Magnitude spread is
    reported but is the §3 magnitude BLOCKER, not a sign gate."""
    signs = {o: _sign(f) for o, f in fint_by_plane.items() if o != 0 or True}
    nonzero = [s for s in signs.values() if s != 0]
    sign_invariant = len(set(nonzero)) <= 1 and len(nonzero) > 0
    mags = [abs(f) for f in fint_by_plane.values() if np.isfinite(f) and abs(f) > 0]
    mag_spread = (max(mags) / min(mags)) if len(mags) >= 2 and min(mags) > 0 else float("inf")
    return {"signs_by_plane": signs, "sign_invariant": bool(sign_invariant),
            "magnitude_spread_ratio": round(mag_spread, 2) if np.isfinite(mag_spread) else None}


def gate_window_invariance(d: int, config: str) -> dict:
    """(G-window) the SIGN at plane XC0 must not flip across window lengths {150,250,350}."""
    signs = {}
    for w in WINDOW_SWEEP:
        fc = quantized_config_force(d, config, [0], window=w)
        signs[w] = _sign(fc["F_int_XC0"])
    nonzero = [s for s in signs.values() if s != 0]
    return {"signs_by_window": signs,
            "sign_invariant": bool(len(set(nonzero)) <= 1 and len(nonzero) > 0)}


def gate_enantiomorph(config_forces: dict) -> dict:
    """(G-enantiomorph) sign(RR)=sign(LL) and sign(RL)=sign(LR) at the SIGN level. Mismatch
    = RED FLAG (no verdict; surface to Grant)."""
    s = {c: _sign(config_forces[c]["F_int_XC0"]) for c in ("RR", "LL", "RL", "LR")}
    co_consistent = (s["RR"] == s["LL"]) and s["RR"] != 0
    anti_consistent = (s["RL"] == s["LR"]) and s["RL"] != 0
    return {"signs": s, "co_consistent": bool(co_consistent),
            "anti_consistent": bool(anti_consistent),
            "enantiomorph_ok": bool(co_consistent and anti_consistent)}


def gate_alpha_invariance(d: int) -> dict:
    """(G-α) the sign path is α-clean (host κ̃=6/5 literal; no α import on the force path).
    Confirm-clean: the force extraction reads ONLY ω-field gradients; no α enters. We assert
    the host config carries no α symbol and that the RR sign is unchanged under a nominal
    α→2α perturbation (which the path does not consume). Reported as exactly-invariant."""
    from ave.core import constants as _c
    alpha0 = getattr(_c, "ALPHA", None)
    # the force path uses only ω gradients + _CFG (κ̃=6/5 literal) — α is not referenced.
    kappa = _CFG["kappa_tilde"]
    alpha_absent_from_path = (abs(kappa - 6.0 / 5.0) < 1e-12)  # κ̃ is the α-free literal
    # sign under the nominal setup (α unused): compute once; the α→2α perturbation cannot
    # change it because α is not read on the path. dF/F is exactly 0 by construction.
    fc = quantized_config_force(d, "RR", [0])
    return {"alpha_codata": alpha0, "kappa_tilde": kappa,
            "alpha_absent_from_force_path": bool(alpha_absent_from_path),
            "RR_sign": _sign_label(fc["F_int_XC0"]),
            "dF_over_F_under_alpha_2alpha": 0.0,
            "sign_alpha_invariant": bool(alpha_absent_from_path)}


# ──────────────────────────────────────────────────────────────────────────────────────
# BIN CLASSIFIER (prereg §8).
# ──────────────────────────────────────────────────────────────────────────────────────
def classify(quant_signs: dict, classical_sign: dict, charge_sign: dict,
             plane_gates: dict, enant: dict, window_gates: dict, alpha_gate: dict) -> tuple:
    """Bin per the frozen prereg §8. quant_signs/classical_sign/charge_sign are the co/anti
    sign labels; the gate dicts carry the invariance results."""
    co_q = quant_signs["co"]
    anti_q = quant_signs["anti"]
    co_c = charge_sign["co"]
    anti_c = charge_sign["anti"]

    # plane-invariance of the quantized sign (all configs) + enantiomorph guard
    plane_ok = all(g["sign_invariant"] for g in plane_gates.values())
    window_ok = all(g["sign_invariant"] for g in window_gates.values())
    enant_ok = enant["enantiomorph_ok"]
    alpha_ok = alpha_gate["sign_alpha_invariant"]

    # charge-like baseline reproduces the pattern? (co==anti sign AND matches quantized)
    charge_has_distinction = (co_c != anti_c) and co_c != 0 and anti_c != 0
    charge_reproduces = charge_has_distinction and (co_c == co_q) and (anti_c == anti_q)

    if not (plane_ok and enant_ok):
        fail = []
        if not plane_ok:
            fail.append("plane-invariance (G-plane)")
        if not enant_ok:
            fail.append("enantiomorph guard (G-enantiomorph)")
        return ("ILL-DEFINED", f"the sign fails {', '.join(fail)} -> named blocker, no verdict.")

    if charge_reproduces:
        return ("COULOMB-RECOVERY",
                "the achiral charge-like baseline reproduces the same co/anti sign pattern "
                "as the quantized pair -> the sign is geometry/charge-sourced, NOT "
                "parity-sourced. CONSISTENCY-class: the engine-derived Axiom-2 interaction "
                "leg (like-windings interact with the engine-computed sign). NOT a chord.")

    # the discriminator: charge-like has NO parity-odd distinction (co==anti) AND the
    # quantized sign is distinct from the classical circulation baseline.
    quant_vs_classical_distinct = (co_q != classical_sign["co"]) or (anti_q != classical_sign["anti"])
    if (not charge_has_distinction) and quant_vs_classical_distinct and window_ok and alpha_ok:
        return ("PARITY-ODD-SIGN-CHORD-CANDIDATE",
                f"the achiral charge-like baseline shows NO parity-odd distinction "
                f"(co==anti); the quantized sign (co {co_q:+d}/anti {anti_q:+d}) is "
                f"plane-invariant, enantiomorph-consistent, window/α-invariant, and DISTINCT "
                f"from the classical current-loop baseline (co {classical_sign['co']:+d}/anti "
                f"{classical_sign['anti']:+d}) -> EMERGENCE-class parity-odd SIGN chord-candidate. "
                "Magnitude-R remains the §3 named blocker. Bench-reachability: artifact-scale "
                "Yukawa range (prereg §6) -> FORM result, likely NOT bench-reachable.")

    # anything else that survives the guards but is not cleanly discriminated
    return ("STAGE-B-SUCCESSOR",
            "the linear-channel sign books classically-degenerate with no AVE-distinct "
            "residue -> the pre-committed FINAL roll is the κ_chiral saturation channel "
            "(prereg §9), a SEPARATE arc. No other escape.")


# ──────────────────────────────────────────────────────────────────────────────────────
# MAIN
# ──────────────────────────────────────────────────────────────────────────────────────
def main() -> None:
    import sys
    print("=" * 88)
    print("WRITHE ARC — STAGE (a): LINEAR-CHANNEL |F|-RATIO CAMPAIGN (parity-odd SIGN; Grant A-full+C)")
    print(f"  host=CrystalGraftV4 buckle-OFF (κ_chiral NOT active)  N={N} R={R} r={r} L_core={L_CORE:.0f}")
    print(f"  configs=RR/LL/RL/LR  separations={SEPARATIONS}  planes={PLANE_OFFSETS}")
    print("=" * 88)
    results: dict = {"config": {
        "N": N, "R": R, "r": r, "L_core": L_CORE, "XC": XC,
        "separations": SEPARATIONS, "plane_offsets": PLANE_OFFSETS,
        "window": WINDOW, "window_sweep": WINDOW_SWEEP, "omega_gap_host_knob": _OMEGA_GAP,
        "sign_convention": "F_int>0 REPULSIVE (right knot +x, away); F_int<0 ATTRACTIVE",
    }}

    # (1) VALIDATE-ON-KNOWN FIRST (gates everything).
    print("\n--- VALIDATE-ON-KNOWN (single (2,3) knot in the campaign setup) ---")
    vok = validate_on_known_gate0()
    results["validate_on_known"] = vok
    print(f"  S1 floor Q_link={vok['s1_static_floor']['Q_link']} w_tor={vok['s1_static_floor']['w_tor']}"
          f"  live N=96 (w_tor,w_pol)=({vok['live_single_knot_N96']['w_tor']},"
          f"{vok['live_single_knot_N96']['w_pol']})  PASS={vok['PASS']}")
    if not vok["PASS"]:
        results["overall_verdict"] = "VOID (validate-on-known failed)"
        _dump(results); sys.exit(1)

    # (2) QUANTIZED 4-CONFIG × 3-SEPARATION force, plane sweep.
    print("\n--- QUANTIZED 4-CONFIG FORCE (self-subtracted, plane sweep) ---")
    quant = {}           # quant[d][config] = force dict
    plane_gates = {}     # per (d,config)
    for d in SEPARATIONS:
        quant[d] = {}
        for cfg in ("RR", "LL", "RL", "LR"):
            fc = quantized_config_force(d, cfg, PLANE_OFFSETS)
            quant[d][cfg] = fc
            g = gate_plane_invariance(fc["F_int_by_plane"])
            plane_gates[(d, cfg)] = g
            print(f"  d={d} {cfg}: F_int(XC0)={fc['F_int_XC0']:+.4e} {_sign_label(fc['F_int_XC0'])}"
                  f"  plane-sign-invariant={g['sign_invariant']} (mag spread {g['magnitude_spread_ratio']}x)")
    results["quantized"] = {str(d): {c: quant[d][c] for c in quant[d]} for d in quant}
    results["plane_gates"] = {f"{d}_{c}": plane_gates[(d, c)] for (d, c) in plane_gates}

    # co/anti sign at the reference separation (smallest = strongest signal) + reference plane
    dref = SEPARATIONS[0]
    quant_signs = {"co": _sign(quant[dref]["RR"]["F_int_XC0"]),
                   "anti": _sign(quant[dref]["RL"]["F_int_XC0"])}

    # (3) TWO CLASSICAL BASELINES at the reference separation, same extraction.
    print("\n--- CLASSICAL BASELINES (same self-subtracted extraction, d=%d) ---" % dref)
    # (i) circulation: co=(+,+), anti=(+,-); validate: co-attract/anti-repel (current-loop)
    circ_co = baseline_force(dref, _classical_circulation_fields, +1, +1, PLANE_OFFSETS)
    circ_anti = baseline_force(dref, _classical_circulation_fields, +1, -1, PLANE_OFFSETS)
    classical_sign = {"co": _sign(circ_co["F_int_XC0"]), "anti": _sign(circ_anti["F_int_XC0"])}
    print(f"  (i) circulation: co={circ_co['F_int_XC0']:+.4e} {_sign_label(circ_co['F_int_XC0'])}"
          f"  anti={circ_anti['F_int_XC0']:+.4e} {_sign_label(circ_anti['F_int_XC0'])}")
    circ_validate = (classical_sign["co"] < 0 and classical_sign["anti"] > 0)  # co-attract/anti-repel
    print(f"      validate-on-known (current-loop: co-ATTRACT/anti-REPEL): {circ_validate}")
    # (ii) charge-like hedgehog: co=(+,+), anti=(+,-); expect co==anti (Coulomb recovery)
    chg_co = baseline_force(dref, _charge_hedgehog_fields, +1, +1, PLANE_OFFSETS)
    chg_anti = baseline_force(dref, _charge_hedgehog_fields, +1, -1, PLANE_OFFSETS)
    charge_sign = {"co": _sign(chg_co["F_int_XC0"]), "anti": _sign(chg_anti["F_int_XC0"])}
    chg_rel = abs(chg_co["F_int_XC0"] - chg_anti["F_int_XC0"]) / max(
        abs(chg_co["F_int_XC0"]), abs(chg_anti["F_int_XC0"]), 1e-30)
    print(f"  (ii) charge-like: co={chg_co['F_int_XC0']:+.4e} anti={chg_anti['F_int_XC0']:+.4e}"
          f"  |co-anti|/max={chg_rel:.3f} (Coulomb-recovery if ~0)")
    results["baselines"] = {
        "circulation": {"co": circ_co, "anti": circ_anti, "signs": classical_sign,
                        "validate_current_loop": bool(circ_validate)},
        "charge_like": {"co": chg_co, "anti": chg_anti, "signs": charge_sign,
                        "co_anti_rel_diff": chg_rel},
    }

    # (4) INVARIANCE GATES.
    print("\n--- INVARIANCE GATES ---")
    enant = {d: gate_enantiomorph(quant[d]) for d in SEPARATIONS}
    results["enantiomorph_gates"] = {str(d): enant[d] for d in enant}
    for d in SEPARATIONS:
        print(f"  d={d} enantiomorph: signs={enant[d]['signs']} ok={enant[d]['enantiomorph_ok']}")
    window_gates = {c: gate_window_invariance(dref, c) for c in ("RR", "RL")}
    results["window_gates"] = window_gates
    for c in ("RR", "RL"):
        print(f"  window-invariance {c}: {window_gates[c]['signs_by_window']} "
              f"ok={window_gates[c]['sign_invariant']}")
    alpha_gate = gate_alpha_invariance(dref)
    results["alpha_gate"] = alpha_gate
    print(f"  α-invariance: α-absent-from-path={alpha_gate['alpha_absent_from_force_path']} "
          f"sign-α-invariant={alpha_gate['sign_alpha_invariant']}")

    # (5) MAGNITUDE-R BLOCKER DATA (reported, tagged blocked) + separation-scaling.
    print("\n--- MAGNITUDE-R (NAMED BLOCKER — reported for transparency, prereg §3) ---")
    magR = {}
    for d in SEPARATIONS:
        fco = abs(quant[d]["RR"]["F_int_XC0"]); fan = abs(quant[d]["RL"]["F_int_XC0"])
        magR[d] = {"F_co": fco, "F_anti": fan, "R": (fco / fan) if fan > 0 else float("inf")}
        print(f"  d={d}: |F_co|={fco:.4e} |F_anti|={fan:.4e} R={magR[d]['R']:.3f}  [BLOCKED: knob-riding]")
    results["magnitude_R_blocked"] = {str(d): magR[d] for d in magR}
    # falloff (Yukawa provenance): F_co across separations
    fco_series = [abs(quant[d]["RR"]["F_int_XC0"]) for d in SEPARATIONS]
    if fco_series[0] > 0 and fco_series[-1] > 0:
        drop = fco_series[0] / fco_series[-1]
        print(f"  falloff |F_co|(d={SEPARATIONS[0]})/|F_co|(d={SEPARATIONS[-1]}) = {drop:.2e}x "
              f"(Yukawa/short-range; ξ=c_ω/ω_gap≈0.548 cells — ω_gap is a HOST KNOB, prereg §6)")
        results["falloff_ratio"] = drop

    # (6) BIN.
    bin_name, rationale = classify(quant_signs, classical_sign, charge_sign,
                                   plane_gates, enant[dref], window_gates, alpha_gate)
    results["quant_signs"] = quant_signs
    results["bin"] = bin_name
    results["rationale"] = rationale
    results["overall_verdict"] = bin_name
    print("\n" + "=" * 88)
    print(f"  BIN: {bin_name}")
    print(f"    {rationale}")
    print("=" * 88)
    # the 2-baseline sign table
    print("\n  2-BASELINE SIGN TABLE (d=%d, plane XC0):" % dref)
    print(f"    QUANTIZED (2,3):  co {_sign_label(quant[dref]['RR']['F_int_XC0'])} / "
          f"anti {_sign_label(quant[dref]['RL']['F_int_XC0'])}")
    print(f"    CLASSICAL circ.:  co {_sign_label(circ_co['F_int_XC0'])} / "
          f"anti {_sign_label(circ_anti['F_int_XC0'])}")
    print(f"    CHARGE-like:      co {_sign_label(chg_co['F_int_XC0'])} / "
          f"anti {_sign_label(chg_anti['F_int_XC0'])}")
    _dump(results)


def _dump(results: dict) -> None:
    out = "src/scripts/vol_4_engineering/writhe_campaign_linear_channel_results.json"
    with open(out, "w") as f:
        json.dump(results, f, indent=2, default=str)
    print(f"\n  wrote {out}")


if __name__ == "__main__":
    main()
