"""
WRITHE ARC — GATE-0: PAIR FEASIBILITY (the cheap-decisive gate, runs FIRST)
==========================================================================

FROZEN PRE-REG: research/2026-07-03_writhe-gate0-pair-feasibility_prereg.md.
Arc charter: _orchestration/2026-07-02_writhe-force-ratio-build-brief.md (§3 step 0).

THE QUESTION (prereg §1): can the engine host TWO winding solitons at controlled
real-space separation d, such that each individually conserves its S1 (2,3) DOF and
the pair neither merges nor disperses over a measurement window?

SCOPE CAP (prereg §6): Gate-0 ONLY. NO |F| ratio claim of any kind. This driver
measures pair feasibility + per-knot winding conservation + (if stable) a mid-plane
ω-sector T^{0i} transmission PRESENCE/floor probe. It does NOT measure R=|F|_co/|F|_anti,
does NOT compare RR vs RL/LR forces. That is the HELD four-configuration campaign.

CLASSIFICATION (consistency-vs-emergence): CONSISTENCY-class. Engine-capability check.

SECTOR / REGIME (prereg §0):
  SECTOR  = T2 / Cosserat micro-rotation ω-sector (charge = Beltrami helicity on ω-grade).
  HOST    = S1 isolated-knot host (CrystalGraftV4, buckle OFF, photon OFF, lock ON) —
            reused verbatim from s1_winding_conservation_gate._build_isolated_knot; NOT
            reinvented (mission spec). κ̃=6/5 literal, α-CLEAN readout path.
  MEDIUM  = cold / parity-even inter-knot region. The knots' own T2 walls are the only
            saturated (Γ=−1) regions. NOTE: the κ_chiral saturation-bias term lives in the
            JAX CosseratField3D engine (src/ave/topological/cosserat_field_3d.py), NOT in
            this buckle-OFF host — so this host runs NO κ_chiral term (prereg §5.1).

COORDINATES (phase-space-coordinate-check, A46; prereg §0.1):
  The (2,3) winding label is PHASE-SPACE (ω-tank LC quadrature + toroidal ω-polarization),
  read by extract_2_3_omega_fast in its native phase-space coords. The pair separation d
  is REAL-SPACE (lattice-x, cells). NEVER cross-compared. Each knot read in its LOCAL frame
  (roll-to-center), since both readers hard-center the readout torus at grid center.

SAMPLING DISCIPLINE (Rule 10): PML cells excluded from every integral (interior_mask()).
Density-PEAK sampling (top-2 |ω|² peaks), NOT centroid — the knots are shell-like tori.

DRIVER HONESTY (ave-driver-script-honesty): every printed number computed in-run;
validate-on-known (single knot in THIS setup) runs FIRST and gates the pair verdict.

Run:
    PYTHONPATH=src <venv>/bin/python \
        src/scripts/vol_4_engineering/writhe_gate0_pair_feasibility.py
"""

from __future__ import annotations

import json

import numpy as np

# ── the S1 host + its frozen config (REUSED verbatim — mission spec). The isolated
#    knot builder gives the buckle-OFF, lock-ON, ω-carrier-ON host that S1 PASSED on.
from ave.core.s1_winding_conservation_gate import (
    _CFG,                       # frozen α-clean engine config (κ̃=6/5)
    _build_isolated_knot,       # the S1 isolated-knot host builder
    validate_on_known,          # the S1 static planted-integer floor (Q_link=3, w_tor=2)
    ALIAS_TOL,                  # frozen S1 alias tolerance = 0.34
)
from ave.core.crystal_graft_v4 import CrystalGraftV4
# ── the S1 LIVE winding reader (phase-space (2,3) on the ω carrier). This is the reader
#    the S1 gate uses on the evolving CrystalGraftV4 field (compute_Q_link reads the STATIC
#    seed_pq_winding, a DIFFERENT construction — prereg §1.1 note).
from ave.utils.fast_winding_extractor import extract_2_3_omega_fast

# ── canonical-source note (ave-canonical-source): the S1 host is DELIBERATELY α-clean —
#    it imports NO α-carrier on the readout path (s1_winding_conservation_gate.py:41-44),
#    and Gate-0 stays α-clean (the verdict is winding INTEGERS + real-space SEPARATION +
#    an energy RATIO — no physical-constant magnitude is pinned). All engine constants
#    (c_ω, ω_gap, dt via CFL) are set by _CFG and the engine's own CFL, imported through
#    _build_isolated_knot; no physics constant is hard-coded in this driver.

# ── FROZEN GATE-0 CONFIG (prereg §2) ──────────────────────────────────────────────────
N = 96                       # domain: two R=11 knots + cold gap + pml=6 each side
R = 11.0                     # torus major radius (S1 default)
r = 4.0                      # torus tube radius (S1 default)
L_CORE = 2.0 * R             # knot core scale = toroidal diameter = 22 cells (prereg §2.1)
XC = (N - 1) / 2.0           # true grid center 47.5 (T^{0i} true-center discipline)
SEPARATIONS = [24, 34, 44]   # cells = {1.09, 1.55, 2.00}·L_core (SMALL/MEDIUM/LARGE), EVEN
WARMUP = 50                  # steps past the at-rest LC turning point (matches S1 gate_c)
WINDOW = 600                 # recording steps — the S1-certified conservation window
N_READS = 7                  # winding+separation readouts over the window (S1 chk cadence)
AMPLITUDE = 0.4              # S1 isolated-knot seed amplitude (crystal_graft default)

# ── FROZEN STABILITY THRESHOLDS (prereg §3 — NO post-hoc tuning) ───────────────────────
WINDING_TARGET = (2, 3)          # (w_tor, w_pol) each knot must hold at every read
ENERGY_RETAIN_MIN = 0.50         # >=50% post-warmup interior ω-energy retained (no dispersal)
SEP_DRIFT_MAX = 0.30             # |Δd|/d <= 30% over the window (controlled-separation premise)
PEAK_MERGE_FRAC = 0.50           # peaks must stay separated by >= 0.5·d_initial (no merger)
ALIAS_DETONATE = 0.95            # alias >= 0.95 => INCONCLUSIVE (detonation, Rule 11)
TRANSMISSION_FLOOR_MULT = 3.0    # |Φ_mid| must exceed 3× single-knot floor for T-IMPRINTED


# ──────────────────────────────────────────────────────────────────────────────────────
# SEED HELPERS — reuse the S1 seed verbatim + lossless np.roll translation (prereg §1.1).
# ──────────────────────────────────────────────────────────────────────────────────────
def _single_knot_fields(mirror: bool = False):
    """Build ONE canonical S1 (2,3) breathing knot centered at grid center; return its
    (ω, ω_prev) arrays. The S1 seed hard-centers the torus at c=(N-1)/2; we take its
    seeded fields and translate them (below). mirror=True gives the ENANTIOMORPH (a
    z-reflection of the seed) — used for the optional LL pair (prereg §1.2).

    REUSE, not reinvention: _build_isolated_knot is the S1 host builder; we read its
    seeded ω/ω_prev, then discard the engine (we re-seed a fresh pair engine below)."""
    e = _build_isolated_knot(N, R, r, lock_on=True, amplitude=AMPLITUDE)
    om = e.omega.copy()
    omp = e.omega_prev.copy()
    if mirror:
        # enantiomorph = z-reflection (mirror). Reflect the z-axis AND flip ω_z so the
        # winding SIGN inverts (the R->L map). VERIFIED: magnitude read stays (2,3).
        om = om[:, :, ::-1, :].copy()
        om[..., 2] *= -1.0
        omp = omp[:, :, ::-1, :].copy()
        omp[..., 2] *= -1.0
    return om, omp


def _roll_x(field: np.ndarray, shift: int) -> np.ndarray:
    """Rigid translation of a (N,N,N,3) field along x by `shift` cells (lossless for the
    winding integer — VERIFIED prereg §1.1). np.roll is periodic; the PML-excluded
    interior guarantees the wrapped tail lands in the absorbing shell, not the interior."""
    return np.roll(field, shift, axis=0)


def _seed_pair(d: int, *, mirror_A: bool = False, mirror_B: bool = False) -> CrystalGraftV4:
    """Seed a PAIR of (2,3) knots at centers XC∓d/2 on the x-axis (prereg §1.1, §1.2).

    Builds a fresh isolated-knot host, ZEROS its ω fields, then superposes the two
    translated single-knot (ω, ω_prev) contributions. Superposition (not sequential
    seed_omega_known_2_3 calls) is REQUIRED because the canonical seed OVERWRITES
    ω_prev (`=`, not `+=`) — so each knot's LC partner is assembled independently and
    summed (prereg §1.1 note). Both centers land on integer cells (even d, XC=47.5)."""
    e = _build_isolated_knot(N, R, r, lock_on=True, amplitude=AMPLITUDE)
    e.omega[...] = 0.0
    e.omega_prev[...] = 0.0
    shift = d // 2  # XC∓d/2: knot-A at XC−d/2, knot-B at XC+d/2 (even d -> integer shift)
    omA, ompA = _single_knot_fields(mirror=mirror_A)
    omB, ompB = _single_knot_fields(mirror=mirror_B)
    e.omega += _roll_x(omA, -shift) + _roll_x(omB, +shift)
    e.omega_prev += _roll_x(ompA, -shift) + _roll_x(ompB, +shift)
    return e


# ──────────────────────────────────────────────────────────────────────────────────────
# READOUT HELPERS — per-knot local-frame winding + separation + energy (prereg §3).
# ──────────────────────────────────────────────────────────────────────────────────────
def _read_knot_local(e: CrystalGraftV4, center_x: float) -> dict:
    """Read the (2,3) winding of the knot whose torus center sits at x=center_x, in its
    LOCAL frame: rigidly roll the ω (and ω_velocity) field so that knot lands at grid
    center, then use the S1 live reader extract_2_3_omega_fast (which hard-centers at
    c=(N-1)/2). Roll is lossless (prereg §3.3). Returns w_tor/w_pol + the alias fraction."""
    shift = int(round(XC - center_x))  # bring center_x -> grid center
    om = _roll_x(e.omega, shift)
    piw = _roll_x(e.omega_velocity(), shift)
    res = extract_2_3_omega_fast(om, piw, R, r, N)
    # alias canary on the raw winding lists (S1 pattern, s1_winding_conservation_gate.py:78)
    alias = 0.0
    for sec in ("w_tor", "w_pol"):
        raws = res.get(f"{sec}_raw_list", [])
        if raws:
            mode = res[sec]
            outl = sum(1 for w in raws if abs(abs(w) - mode) > 1.0 or abs(w) > 6.5)
            alias = max(alias, outl / len(raws))
    return {"w_tor": int(res["w_tor"]), "w_pol": int(res["w_pol"]), "alias_frac": float(alias)}


def _omega_energy_density(e: CrystalGraftV4) -> np.ndarray:
    """|ω|² energy density (N,N,N), for peak-finding + the dispersal ledger."""
    return np.sum(e.omega * e.omega, axis=-1)


def _interior(e: CrystalGraftV4) -> np.ndarray:
    """PML-excluded interior boolean mask (Rule 10)."""
    return e.interior_mask()


def _interior_omega_energy(e: CrystalGraftV4) -> float:
    """Total PML-excluded interior ω-energy ∫|ω|² (the dispersal criterion, prereg §3.2 D)."""
    return float(np.sum(_omega_energy_density(e) * _interior(e)))


def _knot_centers_x(e: CrystalGraftV4) -> tuple[float, float]:
    """The x-positions of the two knot ENERGY CENTROIDS, one per half-region (split at XC).

    DRIVER-TIME CORRECTION (Rule 10, flag-don't-fix): the naive top-2 ω-energy-density
    PEAK finder does NOT locate a torus CENTER — a torus of major radius R peaks on its
    TUBE at x=center±R (the tube crossings), so the global top-2 peaks of a pair land on
    the two INNER tube crossings and read an apparent separation of ~(d−2R), not d, and
    rolling those to grid center MIS-CENTERS the readout torus (verified: reads (0,1) not
    (2,3)). The knot CENTER is the ω-energy CENTROID of its half-region — the torus tube
    is symmetric about its own center, so the centroid recovers the center exactly
    (verified: half-region centroids recover the seeded XC∓d/2 to <0.01 cell, and reading
    at those centers reads (2,3)). Split at XC (the pair straddles it symmetrically). This
    IS a density-weighted read (not a bare geometric centroid of an empty middle) — the
    shell-centroid caveat is handled by the half-region split isolating one torus each."""
    dens = _omega_energy_density(e) * _interior(e)
    _I = np.indices((N, N, N))[0]
    xax = np.arange(N)
    prof_L = (dens * (_I < XC)).sum(axis=(1, 2))   # (N,) x-profile, left half
    prof_R = (dens * (_I >= XC)).sum(axis=(1, 2))  # right half
    cxL = float((xax * prof_L).sum() / (prof_L.sum() + 1e-30))
    cxR = float((xax * prof_R).sum() / (prof_R.sum() + 1e-30))
    return cxL, cxR


# ──────────────────────────────────────────────────────────────────────────────────────
# ω-SECTOR T^{0i} — the transmission probe observable (prereg §5). The ω-sector analogue
# of the mass-sector scalar T^{0x}=(∂_t V)(∂_x V) (mass_sector_field_momentum_T0i.py:137):
#   T^{0x}_ω = (∂_t ω)·(∂_x ω)   (dot over the 3 ω-components — the winding carrier's own
#              momentum-flux density along x). ∂_t ω = omega_velocity(); ∂_x ω = central diff.
# ──────────────────────────────────────────────────────────────────────────────────────
def _T0x_omega_density(e: CrystalGraftV4) -> np.ndarray:
    """T^{0x}_ω = (∂_t ω)·(∂_x ω) field-momentum density (N,N,N), summed over ω-components.
    ∂_t ω = (ω − ω_prev)/dt (the engine's two stored leapfrog ω states, omega_velocity()).
    ∂_x ω central-difference along x (matches the engine's own central-difference stencil).
    Edge planes left 0 (they sit inside the PML and are excluded from every integral)."""
    dt_omega = e.omega_velocity()                 # (N,N,N,3)
    dx_omega = np.zeros_like(e.omega)
    dx_omega[1:-1, :, :, :] = (e.omega[2:, :, :, :] - e.omega[:-2, :, :, :]) / 2.0
    return np.sum(dt_omega * dx_omega, axis=-1)    # (N,N,N)


def _midplane_flux(e: CrystalGraftV4) -> float:
    """Mid-plane ω-momentum flux Φ_mid across the XC=47.5 face (mean of the i=47 and i=48
    planes, PML-excluded) — the momentum the ω field transports left↔right through the gap
    (prereg §5.2). Reuses the mass-sector face-flux construction (…T0i.py:169), ported to
    the ω vector field. SYMMETRY-CAVEAT (prereg §5.2): for a mirror-symmetric pair this is
    symmetry-forced to zero — a nonzero Φ_mid is a mirror-symmetry-BREAKING (handedness) flux."""
    t0x = _T0x_omega_density(e)
    interior = _interior(e)
    i_lo = int(np.floor(XC))   # 47
    i_hi = i_lo + 1            # 48
    _I = np.indices((N, N, N))[0]
    face_lo = interior & (_I == i_lo)
    face_hi = interior & (_I == i_hi)
    return 0.5 * (float(np.sum(t0x[face_lo])) + float(np.sum(t0x[face_hi])))


def _mirror_symmetry_residual(e: CrystalGraftV4) -> float:
    """max|ω(x) − ω(N−1−x)| over the interior — 0 ⇒ exactly mirror-symmetric about XC (so
    a zero Φ_mid is symmetry-forced, prereg §5.2). Reuses the mass-sector symmetry check
    (…T0i.py:42)."""
    omega = e.omega
    mirror = omega[::-1, :, :, :]
    interior = _interior(e)[..., None]
    return float(np.max(np.abs((omega - mirror) * interior)))


# ──────────────────────────────────────────────────────────────────────────────────────
# VALIDATE-ON-KNOWN (prereg §3.4) — the honest floor, runs FIRST, gates the pair verdict.
# ──────────────────────────────────────────────────────────────────────────────────────
def validate_on_known_gate0() -> dict:
    """A SINGLE seeded (2,3) knot must reproduce the S1 result IN THE GATE-0 SETUP before
    any pair verdict counts (prereg §3.4). Two checks: (1) the S1 static planted-integer
    floor (validate_on_known: Q_link=3, w_tor=2, null=0) — the extractor floor; (2) a
    single LIVE breathing knot centered in the N=96 domain reads (2,3) via the same
    per-knot local-frame reader the pair uses. If either fails, the pair result is VOID."""
    vk = validate_on_known()  # S1 static floor (its own N=32/R=7/r=2.3 defaults)
    e = _build_isolated_knot(N, R, r, lock_on=True, amplitude=AMPLITUDE)  # centered in N=96
    live = _read_knot_local(e, XC)  # read at grid center (shift 0)
    live_ok = (live["w_tor"], live["w_pol"]) == WINDING_TARGET
    return {
        "s1_static_floor": {
            "Q_link": vk["Q_link_poloidal"], "w_tor": vk["w_tor_toroidal"],
            "null_Q_link": vk["null_Q_link"], "PASS": vk["PASS"],
        },
        "live_single_knot_N96": {
            "w_tor": live["w_tor"], "w_pol": live["w_pol"],
            "alias_frac": round(live["alias_frac"], 4),
            "reads_2_3": bool(live_ok),
        },
        "PASS": bool(vk["PASS"] and live_ok),
    }


# ──────────────────────────────────────────────────────────────────────────────────────
# THE PER-d STABILITY RUN (prereg §3 — every threshold frozen) + single-knot floor.
# ──────────────────────────────────────────────────────────────────────────────────────
def run_single_knot_floor(d: int) -> dict:
    """The single-knot ω-T^{0i} mid-plane FLOOR (prereg §5.2): one knot at blob-A's
    position (XC−d/2, off-center like the pair) — its own breathing radiation drives a
    nonzero Φ_mid that is NOT an inter-knot transmission. The two-knot |Φ_mid| must EXCEED
    this to count as a real transmission signal. Records the max |Φ_mid| over the window."""
    e = _seed_single_offset(d)
    for _ in range(WARMUP):
        e.step()
    phi_abs = []
    for _ in range(WINDOW):
        e.step()
        phi_abs.append(abs(_midplane_flux(e)))
    return {
        "phi_mid_floor_max": float(np.max(phi_abs)) if phi_abs else float("nan"),
        "phi_mid_floor_mean": float(np.mean(phi_abs)) if phi_abs else float("nan"),
    }


def _seed_single_offset(d: int) -> CrystalGraftV4:
    """One knot at XC−d/2 (blob-A's off-center position) — the transmission-floor control."""
    e = _build_isolated_knot(N, R, r, lock_on=True, amplitude=AMPLITUDE)
    e.omega[...] = 0.0
    e.omega_prev[...] = 0.0
    om, omp = _single_knot_fields(mirror=False)
    e.omega += _roll_x(om, -(d // 2))
    e.omega_prev += _roll_x(omp, -(d // 2))
    return e


def run_pair_stability(d: int, *, mirror_A: bool = False, mirror_B: bool = False,
                       label: str = "RR") -> dict:
    """Evolve a knot pair at separation d and evaluate ALL frozen stability criteria over
    the window (prereg §3). Reads per-knot winding (local frame), separation (top-2 peaks),
    interior ω-energy, and the alias canary at N_READS checkpoints. Returns the full ledger
    + the per-criterion booleans + the STABLE/UNSTABLE/INCONCLUSIVE verdict for THIS d."""
    e = _seed_pair(d, mirror_A=mirror_A, mirror_B=mirror_B)
    for _ in range(WARMUP):
        e.step()

    E0 = _interior_omega_energy(e)                 # post-warmup interior ω-energy (baseline)
    pA0, pB0 = _knot_centers_x(e)
    d0 = abs(pB0 - pA0)                             # measured initial separation (centroids)
    stride = max(1, WINDOW // N_READS)

    reads = []          # per-checkpoint (wA, wB, sep, E_frac, alias)
    alias_max = 0.0
    steps = 0
    while steps < WINDOW:
        e.step()
        steps += 1
        if steps % stride == 0 or steps == WINDOW:
            cxA, cxB = _knot_centers_x(e)
            sep = abs(cxB - cxA)
            # read each knot at its CURRENT half-region energy-centroid (local frame)
            wA = _read_knot_local(e, cxA)
            wB = _read_knot_local(e, cxB)
            Efrac = _interior_omega_energy(e) / (E0 + 1e-30)
            al = max(wA["alias_frac"], wB["alias_frac"])
            alias_max = max(alias_max, al)
            reads.append({
                "step": steps,
                "wA": (wA["w_tor"], wA["w_pol"]), "wB": (wB["w_tor"], wB["w_pol"]),
                "sep": round(sep, 2), "E_frac": round(Efrac, 4), "alias": round(al, 3),
            })

    # ── evaluate the frozen criteria (prereg §3) ──
    winding_ok = all(tuple(rd["wA"]) == WINDING_TARGET and tuple(rd["wB"]) == WINDING_TARGET
                     for rd in reads)
    alias_ok = alias_max <= ALIAS_TOL
    E_end = reads[-1]["E_frac"] if reads else 0.0
    no_dispersal = E_end >= ENERGY_RETAIN_MIN
    sep_end = reads[-1]["sep"] if reads else 0.0
    no_merger = (d0 > 0) and all(rd["sep"] >= PEAK_MERGE_FRAC * d0 for rd in reads)
    sep_drift = abs(sep_end - d0) / (d0 + 1e-30)
    sep_bounded = sep_drift <= SEP_DRIFT_MAX

    detonated = alias_max >= ALIAS_DETONATE or not np.isfinite(E_end)

    if detonated:
        verdict = "INCONCLUSIVE"
    elif winding_ok and alias_ok and no_dispersal and no_merger and sep_bounded:
        verdict = "STABLE"
    else:
        verdict = "UNSTABLE"

    failing = [k for k, v in {
        "winding_conserved": winding_ok, "alias_ok": alias_ok,
        "no_dispersal": no_dispersal, "no_merger": no_merger,
        "sep_bounded": sep_bounded,
    }.items() if not v]

    return {
        "label": label, "d": d, "d_over_Lcore": round(d / L_CORE, 3),
        "d0_measured": round(d0, 2), "sep_end": round(sep_end, 2),
        "sep_drift": round(sep_drift, 4), "E_frac_end": round(E_end, 4),
        "alias_max": round(alias_max, 4),
        "reads": reads,
        "criteria": {
            "winding_conserved": bool(winding_ok), "alias_ok": bool(alias_ok),
            "no_dispersal": bool(no_dispersal), "no_merger": bool(no_merger),
            "sep_bounded": bool(sep_bounded),
        },
        "verdict": verdict, "failing_criteria": failing,
    }


# ──────────────────────────────────────────────────────────────────────────────────────
# TRANSMISSION PROBE (prereg §5.2) — fires ONLY on a STABLE RR pair. Reuses the evolved
# stable-pair state; reads the mid-plane ω-T^{0i} and bins {T-IMPRINTED / T-SYMMETRY-ZEROED
# / T-DOCUMENTED-OPEN}. Cold-medium null is NEVER booked as wrong-regime (brief forbids).
# ──────────────────────────────────────────────────────────────────────────────────────
def run_transmission_probe(d: int, floor: dict) -> dict:
    """Read the mid-plane ω-T^{0i} Φ_mid on the stable RR pair over the window; compare to
    the single-knot floor; check whether any zero is symmetry-forced (prereg §5.2)."""
    e = _seed_pair(d, mirror_A=False, mirror_B=False)  # RR
    for _ in range(WARMUP):
        e.step()
    phi_series, sym_resid, midamp_series = [], [], []
    _I = np.indices((N, N, N))[0]
    i_lo = int(np.floor(XC))
    midface = _interior(e) & ((_I == i_lo) | (_I == i_lo + 1))
    for _ in range(WINDOW):
        e.step()
        phi_series.append(_midplane_flux(e))
        # mid-plane ω amplitude: does the pair even have FIELD OVERLAP at XC? (a
        # well-separated cold-gap pair has ~0 field there -> Φ=0 is no-overlap, NOT
        # symmetry-forced NOR transmission. Distinguishing this is honest — Rule 10.)
        midamp_series.append(float(np.max(np.abs(e.omega[midface]))))
        if len(sym_resid) < 5:  # sample the mirror-symmetry residual a few times
            sym_resid.append(_mirror_symmetry_residual(e))
    phi_abs_max = float(np.max(np.abs(phi_series)))
    phi_net = float(np.mean(phi_series))
    floor_max = floor["phi_mid_floor_max"]
    sym_res = float(np.mean(sym_resid)) if sym_resid else float("nan")
    midamp_max = float(np.max(midamp_series)) if midamp_series else 0.0
    interior_amp = float(np.max(np.abs(e.omega * _interior(e)[..., None])))
    # is the field mirror-symmetric about XC (so a zero Φ_mid is symmetry-forced)?
    mirror_symmetric = bool(np.isfinite(sym_res) and interior_amp > 0
                            and sym_res < 0.05 * interior_amp)
    # is there ANY appreciable field at the midplane? (>1% of the interior ω amp)
    has_midplane_overlap = bool(interior_amp > 0 and midamp_max > 0.01 * interior_amp)

    above_floor = bool(np.isfinite(phi_abs_max) and np.isfinite(floor_max)
                       and phi_abs_max > TRANSMISSION_FLOOR_MULT * floor_max)

    if above_floor:
        tbin = "T-IMPRINTED"
        rationale = (
            f"|Φ_mid|_max={phi_abs_max:.3e} > {TRANSMISSION_FLOOR_MULT}× single-knot "
            f"floor ({floor_max:.3e}) -> a handedness-carrying ω-momentum-flux reaches "
            "the cold mid-plane; wall-supplied saturation SUFFICES (the cold medium need "
            "NOT be driven near-yield). NOTE: this is a PRESENCE/floor check on the RR "
            "pair only — NOT a co-vs-anti force ratio (that is the HELD campaign).")
    elif mirror_symmetric:
        tbin = "T-SYMMETRY-ZEROED"
        rationale = (
            f"|Φ_mid|_max={phi_abs_max:.3e} ~ floor ({floor_max:.3e}) AND the field is "
            f"mirror-symmetric about XC (residual {sym_res:.2e} < 5% of interior ω amp "
            f"{interior_amp:.2e}) -> the parity-EVEN mid-plane flux is SYMMETRY-FORCED to "
            "zero (mass-sector M2 caveat). This is NOT a transmission null and NOT a "
            "cold-medium wrong-regime null: the handedness signal is parity-ODD and needs "
            "the RL/LR configs (HELD campaign). Documented-open.")
    elif not has_midplane_overlap:
        tbin = "T-DOCUMENTED-OPEN"
        rationale = (
            f"|Φ_mid|_max={phi_abs_max:.3e} ~ floor ({floor_max:.3e}), and the mid-plane "
            f"ω amplitude ({midamp_max:.3e}) is < 1% of the interior ω amp ({interior_amp:.3e}) "
            "-> the two knots have NO appreciable FIELD OVERLAP at XC (a well-separated "
            "cold-gap pair): Φ=0 is NO-OVERLAP, not symmetry-forced and not a transmission "
            "null. This is NOT a cold-medium wrong-regime null (brief forbids booking one). "
            "Transmission answered ANALYTICALLY only (prereg §5.1); a smaller-d overlapping "
            "pair + the RL/LR four-config set (HELD) is needed to resolve numerically.")
    else:
        tbin = "T-DOCUMENTED-OPEN"
        rationale = (
            f"|Φ_mid|_max={phi_abs_max:.3e} vs floor {floor_max:.3e}: the knots DO overlap "
            f"at XC (mid ω amp {midamp_max:.3e}) but the flux is at floor and no clean "
            "symmetry-zero -> transmission answered ANALYTICALLY only (prereg §5.1); the "
            "full RL/LR four-config set (HELD) is needed to resolve.")
    return {
        "d": d, "phi_mid_abs_max": phi_abs_max, "phi_mid_net": phi_net,
        "floor_max": floor_max, "mirror_symmetry_residual": sym_res,
        "interior_omega_amp": interior_amp, "midplane_omega_amp_max": midamp_max,
        "has_midplane_overlap": has_midplane_overlap,
        "mirror_symmetric": mirror_symmetric,
        "above_floor": above_floor, "transmission_bin": tbin, "rationale": rationale,
    }


# ──────────────────────────────────────────────────────────────────────────────────────
# MINI-BIN CLASSIFIER (prereg §4) — bins the pair-feasibility verdict.
# ──────────────────────────────────────────────────────────────────────────────────────
def classify_pair_feasibility(per_d: list[dict]) -> tuple[str, str]:
    """Bin the RR d-sweep into the frozen mini-bins (prereg §4)."""
    verdicts = {rd["d"]: rd["verdict"] for rd in per_d}
    stable_d = [d for d, v in verdicts.items() if v == "STABLE"]
    inconclusive = [d for d, v in verdicts.items() if v == "INCONCLUSIVE"]

    if inconclusive and not stable_d:
        return ("INCONCLUSIVE",
                f"the integrator could not carry the dynamics to a clean verdict at "
                f"d={inconclusive} (alias >= {ALIAS_DETONATE} / NaN energy). Reported, "
                "not rescued (Rule 11).")
    if len(stable_d) == len(per_d):
        return ("PAIRS-STABLE",
                f"all tested d ({stable_d}) STABLE -> the arc proceeds to steps 1–5 "
                "(HELD for Grant's review). Pair-force observable is WELL-DEFINED at "
                "current engine capability.")
    if stable_d:
        unstable_d = [d for d, v in verdicts.items() if v == "UNSTABLE"]
        return ("STABLE-IN-A-WINDOW",
                f"STABLE at d={stable_d}, UNSTABLE at d={unstable_d} -> the stable-d "
                "window IS the measurement domain for the HELD campaign; recorded.")
    return ("UNSTABLE-ALL-d",
            f"UNSTABLE at every tested d ({list(verdicts.keys())}) -> the pair-force "
            "observable is ILL-DEFINED at current engine capability. Named blocker; arc "
            "stops (~10–15% cost); register §2.4 gets the honest status (Rule 11).")


def main() -> None:
    import sys
    optional_LL = "--with-LL" in sys.argv  # optional enantiomorph symmetry check (labeled)

    print("=" * 84)
    print("WRITHE ARC — GATE-0: PAIR FEASIBILITY (RR pair; NO |F| ratio claim)")
    print(f"  host=CrystalGraftV4 buckle-OFF lock-ON  N={N} R={R} r={r}  L_core={L_CORE:.0f}")
    print(f"  d-sweep={SEPARATIONS} cells  window={WINDOW} steps (warmup {WARMUP})")
    print("=" * 84)

    results: dict = {
        "config": {
            "N": N, "R": R, "r": r, "L_core": L_CORE, "XC": XC,
            "separations": SEPARATIONS, "warmup": WARMUP, "window": WINDOW,
            "kappa_tilde": _CFG["kappa_tilde"], "alias_tol": ALIAS_TOL,
            "thresholds": {
                "energy_retain_min": ENERGY_RETAIN_MIN, "sep_drift_max": SEP_DRIFT_MAX,
                "peak_merge_frac": PEAK_MERGE_FRAC, "alias_detonate": ALIAS_DETONATE,
                "transmission_floor_mult": TRANSMISSION_FLOOR_MULT,
            },
        }
    }

    # (1) VALIDATE-ON-KNOWN FIRST (prereg §3.4) — gates everything.
    print("\n--- VALIDATE-ON-KNOWN (single knot in the Gate-0 N=96 setup) ---")
    vok = validate_on_known_gate0()
    results["validate_on_known"] = vok
    print(f"  S1 static floor: Q_link={vok['s1_static_floor']['Q_link']} "
          f"w_tor={vok['s1_static_floor']['w_tor']} null={vok['s1_static_floor']['null_Q_link']} "
          f"PASS={vok['s1_static_floor']['PASS']}")
    print(f"  live single knot N=96: (w_tor,w_pol)="
          f"({vok['live_single_knot_N96']['w_tor']},{vok['live_single_knot_N96']['w_pol']}) "
          f"alias={vok['live_single_knot_N96']['alias_frac']} "
          f"reads_2_3={vok['live_single_knot_N96']['reads_2_3']}")
    if not vok["PASS"]:
        print("  VALIDATE-ON-KNOWN FAILED -> pair result VOID (setup broken). Reported, not rescued.")
        results["overall_verdict"] = "VOID (validate-on-known failed)"
        _dump(results)
        sys.exit(1)
    print("  validate-on-known PASS -> pair verdicts count.")

    # (2) RR pair d-sweep (prereg §3, §4).
    print("\n--- RR PAIR d-SWEEP ---")
    per_d = []
    for d in SEPARATIONS:
        rd = run_pair_stability(d, label="RR")
        per_d.append(rd)
        print(f"  d={d:2d} ({rd['d_over_Lcore']}·L_core): verdict={rd['verdict']:12s}  "
              f"E_frac_end={rd['E_frac_end']}  sep {rd['d0_measured']}->{rd['sep_end']} "
              f"(drift {rd['sep_drift']})  alias={rd['alias_max']}  "
              f"fail={rd['failing_criteria']}")
    results["RR_pair_sweep"] = per_d
    bin_name, rationale = classify_pair_feasibility(per_d)
    results["pair_feasibility_bin"] = bin_name
    results["pair_feasibility_rationale"] = rationale
    print(f"\n  PAIR-FEASIBILITY BIN: {bin_name}")
    print(f"    {rationale}")

    # (3) TRANSMISSION PROBE — fires only on stable RR (prereg §5.2).
    stable_d = [rd["d"] for rd in per_d if rd["verdict"] == "STABLE"]
    if stable_d:
        d_probe = stable_d[0]  # the first (smallest) stable d — most overlap
        print(f"\n--- TRANSMISSION PROBE (mid-plane ω-T^{{0i}} on stable RR d={d_probe}) ---")
        floor = run_single_knot_floor(d_probe)
        tprobe = run_transmission_probe(d_probe, floor)
        results["transmission_probe"] = tprobe
        print(f"  |Φ_mid|_max={tprobe['phi_mid_abs_max']:.4e}  floor={tprobe['floor_max']:.4e}  "
              f"mirror-symmetric={tprobe['mirror_symmetric']} (resid {tprobe['mirror_symmetry_residual']:.2e})")
        print(f"  TRANSMISSION BIN: {tprobe['transmission_bin']}")
        print(f"    {tprobe['rationale']}")
    else:
        results["transmission_probe"] = {
            "status": "NOT-RUN (no stable RR pair)",
            "transmission_bin": "T-DOCUMENTED-OPEN",
            "rationale": "no stable RR pair -> transmission answered ANALYTICALLY only "
                         "(prereg §5.1); numerical probe not applicable.",
        }
        print("\n  TRANSMISSION PROBE: NOT-RUN (no stable RR pair) -> answered analytically only.")

    # (4) OPTIONAL LL enantiomorph symmetry check (labeled; prereg §1.2).
    if optional_LL:
        print("\n--- OPTIONAL: LL enantiomorph pair (symmetry cross-check) ---")
        ll = []
        for d in SEPARATIONS:
            rd = run_pair_stability(d, mirror_A=True, mirror_B=True, label="LL")
            ll.append(rd)
            print(f"  d={d:2d}: verdict={rd['verdict']:12s}  E_frac_end={rd['E_frac_end']}  "
                  f"alias={rd['alias_max']}  fail={rd['failing_criteria']}")
        results["LL_pair_sweep"] = ll
        ll_bin, _ = classify_pair_feasibility(ll)
        results["LL_feasibility_bin"] = ll_bin
        mismatch = ll_bin != bin_name
        results["LL_matches_RR"] = not mismatch
        print(f"  LL bin={ll_bin}  (RR bin={bin_name})  match={not mismatch}")
        if mismatch:
            print("  FLAG (flag-don't-fix): LL feasibility DIVERGES from RR -> surface to Grant.")

    results["overall_verdict"] = bin_name
    _dump(results)
    print("\n" + "=" * 84)
    print(f"  GATE-0 VERDICT: {bin_name}")
    print("=" * 84)


def _dump(results: dict) -> None:
    out_path = ("src/scripts/vol_4_engineering/writhe_gate0_pair_feasibility_results.json")
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2, default=str)
    print(f"\n  wrote {out_path}")


if __name__ == "__main__":
    main()
