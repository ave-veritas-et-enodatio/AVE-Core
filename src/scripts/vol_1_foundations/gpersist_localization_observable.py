#!/usr/bin/env python3
"""G-PERSIST localization observable + φ-channel plant — thin Rule-14 driver.

FROZEN prereg: research/2026-07-14_gpersist-localization-observable_prereg_FROZEN.md
(freeze-by-push BEFORE this driver; the freeze commit precedes this file in git
history on analysis/gpersist-localization-observable).

The two KEEP-BOTH follow-ons named in the #670 RESULT §8 (frozen #670 E/φ axes
UNTOUCHED):

  1. LOCALIZATION OBSERVABLE — a boundary-insensitive per-sector spatial-
     concentration meter (participation ratio + density-peak core fraction),
     A1/energy ⊥ T2/Φ_link (never summed), over the PML-excluded interior,
     recorded per quiet step. Discriminates the enclosure fork:
       CONCENTRATING (energy tightens)   -> Reading B genesis-under-confinement
       LOOP-FILLING  (energy stays flat  -> Reading A wake-feeding (Grant's lean)
                      while φ inflates)
  2. φ-CHANNEL PLANT — sustains φ via a distributed external K4 pump WITHOUT
     clobbering the Cosserat state (the #670 review's missing negative control).
     Frozen criterion: φ sustained (fools the retention floor) AND the meter reads
     LOOP-FILLING (externally-fed) => the two-meter combo is un-foolable.

Carrier = the EXISTING loop_gap_harness rank-4 probe, re-run through an
INSTRUMENTED MIRROR LOOP built from the SAME primitives (make_engine / apply_seed
/ apply_bulk_probe_ic / freeze_converter_wall / step / snapshot_op14). No new
engine, no new stepper, no retune. Byte-parity vs run_loop_gap_probe is asserted
on a live cell (--parity) — the meter is measured on the SAME trajectory.

States fork DATA; Grant rules the fork. Does NOT re-open G-PERSIST ★RULED (that
flip rests on the fork-independent PML φ-dispersion trend).

RULING-2 COMPLETION (2026-07-14, Grant): the frozen #689 meter read the POTENTIAL
register ONLY (finding #3 ESCALATED — it omitted the Cosserat KINETIC register,
~44% of H). Per Ruling 2, the circuit ontology is now completed and fully labelled:
the A1 energy blob is a two-register LC store (POTENTIAL = node-capacitor charge;
KINETIC = inductor currents), and the completed FULL-register meter (energy_full)
is the MANDATORY forward instrument; the frozen potential-only meter (energy_pot)
stays BANKED for the #689 run (KEEP-BOTH). See the addendum doc + the three
convention disclosures (register labels / bond-energy attribution / sponge
exclusion) at research/2026-07-14_gpersist-meter-circuit-ontology.md. The fork is
scored on the TORUS pair+graded_a0 cells (no sponge); both registers read
LOOP-FILLING there, so the RULED Reading A is UNCHANGED by the completion.

Usage:
  python gpersist_localization_observable.py --parity N PML MODE FID
  python gpersist_localization_observable.py --cell   N PML MODE FID
  python gpersist_localization_observable.py --plant  N PML MODE FID
  python gpersist_localization_observable.py --aggregate
"""

from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import numpy as np

from ave.core.constants import ALPHA
from ave.core.genesis_v18_coupled import (
    P11_A_PERSIST_MIN,
    P11_E_PERSIST_MIN,
    snapshot_op14,
    tau_steps_k4,
)
from ave.core.loop_gap_harness import (
    PHI_BASELINE_FLOOR,
    make_engine,
    run_loop_gap_probe,
)
from ave.core.loop_gap_seeds import A_LOCK_DEFAULT, A_YIELD, apply_seed

PREREG = "research/2026-07-14_gpersist-localization-observable_prereg_FROZEN.md"
ADDENDUM = "research/2026-07-14_gpersist-meter-circuit-ontology.md"
OUT_DIR = Path("assets/sim_outputs/gpersist_localization_observable")

LANDED_SEED_MODES = ("pair", "graded_a0", "photon_lock")
THETA = 0.10  # frozen meter-resolution floor (10% relative change)
CORE_RADII = (1.5, 2.0, 2.5)
PRIMARY_R = 2.0

# ---------------------------------------------------------------------------
# CIRCUIT-ONTOLOGY REGISTER MAP + sponge exclusion (Ruling 2, 2026-07-14 — the
# completion of the #689 escalated finding #3; addendum doc
# research/2026-07-14_gpersist-meter-circuit-ontology.md).
#
# The energy "blob" the enclosure fork asks about is a two-register LC store on
# the K4⊗Cosserat lattice (see the addendum for the full mapping + the three
# convention disclosures verbatim):
#
#   POTENTIAL register (capacitor / charge / displacement-storage):
#     E_pot[i] = k4.get_energy_density()[i]  +  cos.energy_density()[i]
#              = Σ_port(V_inc²+V_ref²)        +  (strain + curvature) potential
#       k4_tlm.py:528-530 (K4 V-sector node capacitance, per-port summed to the
#       home node) ; cosserat_field_3d.py:1427 (Cosserat elastic potential, per
#       node). This is the ONLY register the frozen #689 meter read (potential-
#       only) — banked, KEEP-BOTH.
#
#   KINETIC register (inductor / current / velocity-storage):
#     E_kin[i] = ½ρ Σ_c u̇_c[i]²  +  ½I_ω Σ_c ω̇_c[i]²
#       cosserat_field_3d.py:1789-1794 . Velocities u̇ (=cos.u_dot) and micro-
#       rotation rates ω̇ (=cos.omega_dot) — the inductor-current register in the
#       mechanical LC analogy (velocity↔current, displacement↔charge). ~44% of H
#       at the read step on the banked fork cells. OMITTED by the frozen #689
#       meter; ADDED here (the completion).
#
#   FULL-register A1 energy density (the completed forward instrument):
#     E_full[i] = E_pot[i] + E_kin[i]
#   (A1 ⊥ T2: the Φ_link/T2 winding channel is NEVER summed into A1 — recorded
#   separately, unchanged.)
# ---------------------------------------------------------------------------
SPONGE_GUARD = 1  # kinetic-transit guard rings excluded on the PML box (sponge
# exclusion, disclosed ENGINEERING-CHOICE); 0 on the torus (pml=0 = no sponge).

# KEEP-BOTH register roster (BANKED #689 vs COMPLETED forward + diagnostics).
SECTORS = (
    "energy_pot",      # BANKED #689 instrument: potential register, interior mask
    "energy_full",     # COMPLETED forward instrument: full register, sponge-excluded (SPONGE_GUARD)
    "energy_full_g0",  # diagnostic: full register, NO sponge guard (≡ #689 RESULT-ESCALATED composed)
    "energy_full_g2",  # diagnostic: full register, 2-ring guard (sponge-guard sensitivity)
    "energy_kin",      # diagnostic: kinetic register ONLY, sponge-excluded
    "energy_k4",       # diagnostic: K4 V-sector ONLY, interior mask
    "phi_link",        # T2 winding sector, interior mask (A1 ⊥ T2, never summed)
)
FORWARD_SECTOR = "energy_full"  # the MANDATORY forward instrument (Ruling 2)
BANKED_SECTOR = "energy_pot"    # the frozen #689 banked instrument (KEEP-BOTH)


# ---------------------------------------------------------------------------
# The localization meter (FROZEN definition, prereg §The localization meter)
# ---------------------------------------------------------------------------
def _axis_delta(coord, center: int, N: int, periodic: bool):
    """Per-axis distance from `center`. Minimum-image wrap on the periodic torus
    (pml=0, np.roll-periodic, k4_tlm.py:393); plain Euclidean on the PML box.

    REPAIR (2026-07-14, review finding #1 — torus-native CF stencil): the frozen
    "Euclidean ball" is not native to the pml=0 periodic lattice. A density peak
    near the array seam had part of its r-ball silently clipped, biasing CF low
    (toward LOOP-FILLING) by construction. Minimum-image `min(|d|, N−|d|)` is the
    substrate-native distance on the torus; the PML box keeps plain Euclidean.
    Sign is irrelevant (the caller squares it).
    """
    d = coord - center
    if periodic:
        ad = np.abs(d)
        return np.minimum(ad, N - ad)
    return d


def _cosserat_kinetic_density(cos) -> np.ndarray:
    """Per-NODE Cosserat KINETIC-register energy density: ½ρ|u̇|² + ½I_ω|ω̇|².

    CONVENTION DISCLOSURE (bond-energy attribution, ENGINEERING-CHOICE tag):
    the inductive/kinetic register is attributed with the ENGINE-NATIVE per-node
    register — NO synthetic bond-to-endpoint (half-to-each-endpoint) split is
    made. Rationale: the velocity u̇ (=cos.u_dot) and microrotation rate ω̇
    (=cos.omega_dot) are node-resident vector fields on the Cosserat continuum
    (cosserat_field_3d.py:910-918, shape (N,N,N,3)), so the kinetic energy is
    already node-local by construction — unlike the Φ_link/T2 flux, which is a
    genuine per-bond (4-port) quantity. This per-site density sums EXACTLY to the
    engine scalar cos.kinetic_energy() (cosserat_field_3d.py:1789-1794) at
    rel-diff 0.00e+00 (verified — see the addendum's attribution test); the same
    mask_alive gate the engine applies is used here.
    """
    m = np.asarray(cos.mask_alive, dtype=bool)[..., None]
    u_dot = np.asarray(cos.u_dot, dtype=float) * m
    w_dot = np.asarray(cos.omega_dot, dtype=float) * m
    k_u = 0.5 * float(cos.rho) * np.sum(u_dot**2, axis=-1)
    k_w = 0.5 * float(cos.I_omega) * np.sum(w_dot**2, axis=-1)
    return k_u + k_w


def _read_region(coupled, guard: int) -> np.ndarray:
    """Boolean read region = PML-excluded interior further eroded by `guard`
    kinetic-transit rings per face on the PML box.

    CONVENTION DISCLOSURE (sponge exclusion, ENGINEERING-CHOICE tag): the frozen
    #689 interior mask (_interior_mask, k4_cosserat_coupling.py:469) already
    excludes the absorbing region where cos_pml_mask<1 (d < pml_thickness,
    cosserat_field_3d.py:898-905). But the first interior rings ADJACENT to the
    sponge carry outbound kinetic TRANSIT current (velocity/rotation-rate heading
    into the absorber) that is NOT "the blob"; on the kinetic-inclusive read this
    swamps the interior signal (guard=0 → INCONCLUSIVE). This erodes `guard`
    additional rings per face. On the torus (pml=0) there is NO sponge, so the
    read region is the whole periodic lattice for every guard (the fork-scored
    torus cells are untouched by this choice). Shipped forward default:
    SPONGE_GUARD = 1 (the single transit ring adjacent to the sponge).
    """
    mask = np.asarray(coupled._interior_mask(), dtype=bool)
    if coupled.pml == 0 or guard <= 0:
        return mask
    N = coupled.N
    p = coupled.pml + guard
    guarded = np.zeros((N, N, N), dtype=bool)
    guarded[p : N - p, p : N - p, p : N - p] = True
    return mask & guarded


def _core_stats(d: np.ndarray, mask: np.ndarray, N: int, periodic: bool) -> dict:
    """PR + density-peak/geom core-fraction of density `d` over boolean `mask`.

    PR = raw participation ratio (effective participating sites); CF_r = fraction
    within radius r of the DENSITY PEAK (peak, not centroid) and of the geometric
    center. `periodic` selects the torus-native (minimum-image) core-ball on the
    pml=0 lattice vs the plain-Euclidean ball on the PML box (#689 finding #1).
    """
    ax = np.arange(N)
    xx, yy, zz = ax[:, None, None], ax[None, :, None], ax[None, None, :]
    geom = (N // 2, N // 2, N // 2)
    M = int(mask.sum())
    dv = d[mask]
    s1 = float(dv.sum())
    s2 = float((dv * dv).sum())
    pr = (s1 * s1) / s2 if s2 > 0 else 0.0
    dm = np.where(mask, d, -np.inf)
    pk = tuple(int(v) for v in np.unravel_index(int(np.argmax(dm)), d.shape))
    row: dict = {"PR": pr, "PR_frac": (pr / M if M > 0 else 0.0), "peak": list(pk), "M": M}
    rr_pk = np.sqrt(
        _axis_delta(xx, pk[0], N, periodic) ** 2
        + _axis_delta(yy, pk[1], N, periodic) ** 2
        + _axis_delta(zz, pk[2], N, periodic) ** 2
    )
    rr_gm = np.sqrt(
        _axis_delta(xx, geom[0], N, periodic) ** 2
        + _axis_delta(yy, geom[1], N, periodic) ** 2
        + _axis_delta(zz, geom[2], N, periodic) ** 2
    )
    for r in CORE_RADII:
        cp = mask & (rr_pk <= r)
        cg = mask & (rr_gm <= r)
        row[f"CF_peak_{r}"] = float(d[cp].sum()) / s1 if s1 > 0 else 0.0
        row[f"CF_geom_{r}"] = float(d[cg].sum()) / s1 if s1 > 0 else 0.0
    return row


def _meter_snapshot(coupled, periodic: bool) -> dict:
    """Two-REGISTER spatial-concentration meter at the current engine state.

    A1/energy is read in BOTH registers (KEEP-BOTH), never summed with T2/Φ_link:
      energy_pot     — POTENTIAL register (k4 voltage + Cosserat elastic), the
                       BANKED #689 instrument, over the interior mask.
      energy_full    — FULL register (potential + Cosserat KINETIC), the COMPLETED
                       forward instrument, over the SPONGE_GUARD-excluded region.
      energy_full_g0 — full register, NO sponge guard (≡ #689 RESULT-ESCALATED).
      energy_full_g2 — full register, 2-ring guard (sponge-guard sensitivity).
      energy_kin     — KINETIC register only (diagnostic), sponge-excluded.
      energy_k4      — K4 V-sector only (diagnostic), interior mask.
      phi_link       — T2/Φ_link winding sector = Σ_port Phi_link², interior mask.
    """
    N = coupled.N
    k4 = coupled.k4
    e_k4 = np.asarray(k4.get_energy_density(), dtype=float)
    e_cos_pot = np.asarray(coupled.cos.energy_density(), dtype=float)
    e_kin = _cosserat_kinetic_density(coupled.cos)
    e_pot = e_k4 + e_cos_pot
    e_full = e_pot + e_kin
    phi_dens = np.sum(np.asarray(k4.Phi_link, dtype=float) ** 2, axis=-1)

    m_int = _read_region(coupled, 0)
    m_ship = _read_region(coupled, SPONGE_GUARD)
    m_g2 = _read_region(coupled, 2)
    specs = (
        ("energy_pot", e_pot, m_int),
        ("energy_full", e_full, m_ship),
        ("energy_full_g0", e_full, m_int),
        ("energy_full_g2", e_full, m_g2),
        ("energy_kin", e_kin, m_ship),
        ("energy_k4", e_k4, m_int),
        ("phi_link", phi_dens, m_int),
    )
    out = {"M": int(m_int.sum()), "M_sponge": int(m_ship.sum())}
    for name, d, mask in specs:
        out[name] = _core_stats(d, mask, N, periodic)
    return out


def _trend(series: list[dict], sector: str, stat: str) -> dict:
    vals = [s[sector][stat] for s in series]
    start, end = vals[0], vals[-1]
    rel = (end - start) / abs(start) if abs(start) > 1e-30 else 0.0
    # REPAIR (2026-07-14, review finding #5): the frozen §Trend summary (prereg
    # line 113) declares "the least-squares slope normalized by window mean
    # (non-monotone guard)" — declared but never shipped. Add it. The endpoint-only
    # rel_trend hides strongly non-monotone series (e.g. a value that swings wide but
    # returns near its start); slope_norm + min/max are the non-monotone guard.
    n = len(vals)
    if n >= 2:
        xs = np.arange(n, dtype=float)
        slope = float(np.polyfit(xs, np.asarray(vals, dtype=float), 1)[0])
        wmean = float(np.mean(vals))
        slope_norm = slope / wmean if abs(wmean) > 1e-30 else 0.0
    else:
        slope_norm = 0.0
    return {
        "start": round(start, 6),
        "end": round(end, 6),
        "rel_trend": round(rel, 6),
        "min": round(min(vals), 6),
        "max": round(max(vals), 6),
        "slope_norm": round(slope_norm, 6),
    }


# ---------------------------------------------------------------------------
# Instrumented mirror loop — SAME primitives as run_loop_gap_probe (Rule-14),
# plus per-quiet-step meter recording, plus the optional φ-channel plant.
# ---------------------------------------------------------------------------
def _build_engine(N: int, pml: int, mode: str):
    """Reproduce run_loop_gap_probe's engine construction byte-for-byte."""
    engine = make_engine(
        4, N=N, bulk_density_on=True, pml=pml, use_memristive_saturation=True
    )
    apply_seed(engine, mode, amp=None, a_lock=A_LOCK_DEFAULT, front_target=A_YIELD)
    engine.apply_bulk_probe_ic(amp=0.08)
    engine.freeze_converter_wall()
    return engine


def run_instrumented(
    N: int, pml: int, mode: str, fast: bool, *, plant: bool = False
) -> dict:
    """Mirror the frozen #670 drive/quiet schedule; record the meter per quiet step.

    plant=True: during EVERY quiet step, add a distributed external K4 pump
    (V_inc[interior,:] += √ALPHA) BEFORE stepping — sustains Φ_link accumulation
    WITHOUT calling apply_seed (Cosserat u/ω NOT clobbered). Mirrors the #670
    sabotage plant's quiet-loop structure with the same primitives.
    """
    t0 = time.time()
    engine = _build_engine(N, pml, mode)
    coupled = engine._coupled
    mask = np.asarray(coupled._interior_mask(), dtype=bool)
    amp_pump = float(np.sqrt(ALPHA))

    tau = tau_steps_k4(coupled, fast=fast)
    n_drive = max(6 if fast else 10, int(round(0.5 * tau)))
    n_quiet = max(10 if fast else 20, int(round(1.5 * tau)))
    n_total = n_drive + n_quiet

    obs0 = snapshot_op14(coupled)
    phi_baseline = max(obs0["phi_link_sq"], PHI_BASELINE_FLOOR)
    obs_driveoff = obs0
    series: list[dict] = []
    for t in range(1, n_total + 1):
        if plant and t > n_drive:
            coupled.k4.V_inc[mask, :] += amp_pump  # distributed external sustenance
        engine.step()
        obs_t = snapshot_op14(coupled)
        if t == 1:
            phi_baseline = max(obs_t["phi_link_sq"], PHI_BASELINE_FLOOR)
        if t <= n_drive:
            obs_driveoff = obs_t
        if t >= n_drive:  # drive-off snapshot + every quiet step
            m = _meter_snapshot(coupled, periodic=(pml == 0))
            m["t"] = t
            m["phase"] = "drive_off" if t == n_drive else "quiet"
            m["H"] = float(obs_t["H"])
            m["phi_link_sq"] = float(obs_t["phi_link_sq"])
            series.append(m)
    obs_end = obs_t

    phi_drive = max(obs_driveoff["phi_link_sq"], phi_baseline)
    H_drive = max(obs_driveoff["H"], 1e-30)
    E_persist = obs_end["H"] / H_drive
    phi_persist = obs_end["phi_link_sq"] / phi_drive if phi_drive > 0 else 0.0

    trend = {}
    stats = ["PR", "PR_frac"] + [f"CF_peak_{r}" for r in CORE_RADII] + [
        f"CF_geom_{r}" for r in CORE_RADII
    ]
    for sec in SECTORS:
        trend[sec] = {stat: _trend(series, sec, stat) for stat in stats}

    return {
        "N": N,
        "pml": pml,
        "boundary": "torus" if pml == 0 else "PML",
        "seed_mode": mode,
        "fidelity": "smoke" if fast else "production",
        "plant": plant,
        "n_drive": n_drive,
        "n_quiet": n_quiet,
        "E_persist": float(E_persist),
        "phi_persist": float(phi_persist),
        "E_floor": P11_E_PERSIST_MIN,
        "phi_floor": P11_A_PERSIST_MIN,
        "M_interior": series[-1]["M"],
        "trend": trend,
        "series": series,
        "wall_seconds": round(time.time() - t0, 1),
        "prereg": PREREG,
    }


def _sector_signature(trend_sector: dict) -> str:
    """CONCENTRATING / LOOP-FILLING / MIXED / INCONCLUSIVE from ONE sector's PR/CF
    trend (the frozen bin leaves). Shared by the energy classifier and the aggregate
    gate's Φ_link cross-check (review finding #5 — all three MIXED routes)."""
    pr_rel = trend_sector["PR"]["rel_trend"]
    cf_rel = trend_sector[f"CF_peak_{PRIMARY_R}"]["rel_trend"]
    concentrating = (pr_rel <= -THETA) or (cf_rel >= THETA)
    loop_filling = (pr_rel >= -THETA) and (cf_rel <= THETA)
    resolvable = (abs(pr_rel) >= THETA) or (abs(cf_rel) >= THETA)
    if not resolvable:
        return "INCONCLUSIVE"
    if concentrating and not loop_filling:
        return "CONCENTRATING"
    if loop_filling and not concentrating:
        return "LOOP-FILLING"
    return "MIXED"


def _conjunction_signature(trend_sector: dict) -> str:
    """Two-statistic CONJUNCTION rule (#689 RESULT §4 forward hardening): the
    CONCENTRATING leaf requires PR falls AND CF rises (not the frozen CF-OR-PR
    disjunction that CF-alone false-positived). Reported alongside the frozen
    disjunctive `_sector_signature` for the completed forward instrument."""
    pr_rel = trend_sector["PR"]["rel_trend"]
    cf_rel = trend_sector[f"CF_peak_{PRIMARY_R}"]["rel_trend"]
    concentrating = (pr_rel <= -THETA) and (cf_rel >= THETA)
    loop_filling = (pr_rel >= -THETA) and (cf_rel <= THETA)
    resolvable = (abs(pr_rel) >= THETA) or (abs(cf_rel) >= THETA)
    if not resolvable:
        return "INCONCLUSIVE"
    if concentrating:
        return "CONCENTRATING"
    if loop_filling:
        return "LOOP-FILLING"
    return "MIXED"


def _classify_cell(res: dict) -> dict:
    """Per-cell signature on BOTH registers (KEEP-BOTH) — the before/after payload.

    signature        = the COMPLETED forward instrument (energy_full: potential +
                       Cosserat kinetic, sponge-excluded) under the frozen
                       disjunctive rule — the MANDATORY forward verdict (Ruling 2).
    signature_banked = the frozen #689 BANKED instrument (energy_pot: potential-
                       only, interior mask) — same rule, different register.
    signature_conj   = the forward instrument under the two-statistic conjunction
                       hardening (#689 RESULT §4).
    bin_move         = whether the register completion moved this cell's bin.
    sponge_sensitivity = full-register signature at guard 0 / 2 (the shipped guard
                       is SPONGE_GUARD; a guard-DEPENDENT bin flags a read-region
                       (PML-drain) artifact, not a boundary-clean physical signal).

    NOTE (#689 finding #4): φ_persist is carried as reported context ONLY, never
    gated — the ~10.5× inflation is the quarantined lap-counting gauge artifact
    (k4_tlm.py:400).
    """
    tr = res["trend"]
    fwd = tr[FORWARD_SECTOR]
    banked = tr[BANKED_SECTOR]
    sig_fwd = _sector_signature(fwd)
    sig_banked = _sector_signature(banked)
    guard_sigs = {
        "guard0": _sector_signature(tr["energy_full_g0"]),
        f"guard{SPONGE_GUARD}": sig_fwd,
        "guard2": _sector_signature(tr["energy_full_g2"]),
    }
    # A guard-DEPENDENT full-register bin is the fingerprint of a read-region
    # (PML-drain) artifact, NOT a boundary-clean physical signal; on the torus
    # the guard is a no-op so guard_sensitive is False by construction.
    guard_sensitive = len(set(guard_sigs.values())) > 1
    return {
        "PR_energy_rel_trend": fwd["PR"]["rel_trend"],
        "CF_energy_rel_trend": fwd[f"CF_peak_{PRIMARY_R}"]["rel_trend"],
        "phi_persist": round(res["phi_persist"], 4),
        "signature": sig_fwd,
        "signature_banked": sig_banked,
        "signature_conj": _conjunction_signature(fwd),
        "bin_move": None if sig_fwd == sig_banked else f"{sig_banked}->{sig_fwd}",
        "PR_banked_rel_trend": banked["PR"]["rel_trend"],
        "CF_banked_rel_trend": banked[f"CF_peak_{PRIMARY_R}"]["rel_trend"],
        "sponge_sensitivity": guard_sigs,
        "guard_sensitive": guard_sensitive,
    }


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------
def _cell_path(N, pml, mode, fast, plant=False) -> Path:
    fid = "smoke" if fast else "prod"
    tag = "plant" if plant else "cell"
    return OUT_DIR / f"{tag}_N{N}_pml{pml}_{mode}_{fid}.json"


def _write(path: Path, obj: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2, sort_keys=True))


def cmd_parity(argv) -> None:
    """Live-fire parity: mirror loop E/φ must match run_loop_gap_probe (≤1e-6 rel)."""
    N, pml, mode, fid = int(argv[0]), int(argv[1]), argv[2], argv[3]
    fast = fid == "smoke"
    ref = run_loop_gap_probe(
        f"parity_N{N}_pml{pml}_{mode}",
        rank_target=4,
        seed_mode=mode,
        N=N,
        pml=pml,
        bulk_density_on=True,
        front_target=A_YIELD,
        n_drive_mult=0.5,
        n_quiet_mult=1.5,
        fast=fast,
    )
    mine = run_instrumented(N, pml, mode, fast, plant=False)
    dE = abs(mine["E_persist"] - ref.E_persist_ratio) / max(abs(ref.E_persist_ratio), 1e-30)
    dP = abs(mine["phi_persist"] - ref.phi_persist_ratio) / max(
        abs(ref.phi_persist_ratio), 1e-30
    )
    ok = dE <= 1e-6 and dP <= 1e-6
    print(
        f"[parity] N={N} pml={pml} {mode} {fid}: "
        f"ref E={ref.E_persist_ratio:.6f} phi={ref.phi_persist_ratio:.6f} | "
        f"mirror E={mine['E_persist']:.6f} phi={mine['phi_persist']:.6f} | "
        f"relΔE={dE:.2e} relΔφ={dP:.2e} -> {'PASS' if ok else 'FAIL'}",
        flush=True,
    )
    _write(
        OUT_DIR / f"parity_N{N}_pml{pml}_{mode}_{fid}.json",
        {
            "ref_E": ref.E_persist_ratio,
            "ref_phi": ref.phi_persist_ratio,
            "mirror_E": mine["E_persist"],
            "mirror_phi": mine["phi_persist"],
            "rel_dE": dE,
            "rel_dphi": dP,
            "parity_pass": bool(ok),
            "prereg": PREREG,
        },
    )
    if not ok:
        raise SystemExit("PARITY FAILED — meter is on a different trajectory; run void")


def cmd_cell(argv) -> None:
    N, pml, mode, fid = int(argv[0]), int(argv[1]), argv[2], argv[3]
    assert mode in LANDED_SEED_MODES, mode
    fast = fid == "smoke"
    res = run_instrumented(N, pml, mode, fast, plant=False)
    res["classification"] = _classify_cell(res)
    _write(_cell_path(N, pml, mode, fast), res)
    c = res["classification"]
    move = c["bin_move"] or "no-move"
    print(
        f"[cell] N={N} pml={pml} {mode:10s} {fid:5s} "
        f"E={res['E_persist']:.4f} phi={res['phi_persist']:.4f} | "
        f"banked(pot-only)={c['signature_banked']} -> full={c['signature']} "
        f"[PR{c['PR_energy_rel_trend']:+.3f} CF{c['CF_energy_rel_trend']:+.3f}] "
        f"move={move} guardsens={c['sponge_sensitivity']} [{res['wall_seconds']}s]",
        flush=True,
    )


def cmd_plant(argv) -> None:
    N, pml, mode, fid = int(argv[0]), int(argv[1]), argv[2], argv[3]
    fast = fid == "smoke"
    free = run_instrumented(N, pml, mode, fast, plant=False)
    plant = run_instrumented(N, pml, mode, fast, plant=True)
    # Un-foolable check runs on the COMPLETED forward instrument (energy_full).
    e = plant["trend"][FORWARD_SECTOR]
    loop_filling = (e["PR"]["rel_trend"] >= -THETA) and (
        e[f"CF_peak_{PRIMARY_R}"]["rel_trend"] <= THETA
    )
    a = plant["phi_persist"] >= P11_A_PERSIST_MIN  # φ sustained (fools retention floor)
    b = loop_filling  # meter flags externally-fed
    if a and b:
        verdict = "UN-FOOLABLE_CONFIRMED"
    elif a and not b:
        verdict = "FOOLABLE_SURFACE"
    else:
        verdict = "INCONCLUSIVE_phi_not_sustained"
    out = {
        "N": N,
        "pml": pml,
        "boundary": "torus" if pml == 0 else "PML",
        "seed_mode": mode,
        "fidelity": "smoke" if fast else "production",
        "free_phi_persist": round(free["phi_persist"], 4),
        "free_E_persist": round(free["E_persist"], 4),
        "plant_phi_persist": round(plant["phi_persist"], 4),
        "plant_E_persist": round(plant["E_persist"], 4),
        "plant_phi_sustained": bool(a),
        "plant_meter_loop_filling": bool(b),
        "plant_PR_energy_rel_trend": e["PR"]["rel_trend"],
        "plant_CF_energy_rel_trend": e[f"CF_peak_{PRIMARY_R}"]["rel_trend"],
        "verdict": verdict,
        "free_classification": _classify_cell(free),
        "plant_trend_energy": plant["trend"][FORWARD_SECTOR],
        "prereg": PREREG,
    }
    _write(_cell_path(N, pml, mode, fast, plant=True), out)
    print(
        f"[plant] N={N} pml={pml} {mode} {fid}: "
        f"free_phi={out['free_phi_persist']:.3f} plant_phi={out['plant_phi_persist']:.3f} "
        f"sustained={a} loop_filling={b} -> {verdict}",
        flush=True,
    )


def cmd_aggregate() -> None:
    cells = [json.loads(p.read_text()) for p in sorted(OUT_DIR.glob("cell_*.json"))]
    plants = [json.loads(p.read_text()) for p in sorted(OUT_DIR.glob("plant_*.json"))]

    torus = [
        c
        for c in cells
        if c["pml"] == 0
        and c["seed_mode"] in ("pair", "graded_a0")
        and c["fidelity"] == "production"
    ]
    pml_twin = {
        c["seed_mode"]: c
        for c in cells
        if c["pml"] != 0
        and c["seed_mode"] in ("pair", "graded_a0")
        and c["fidelity"] == "production"
    }
    # KEEP-BOTH: fork bin scored on BOTH registers. forward (energy_full) is the
    # MANDATORY instrument (Ruling 2); banked (energy_pot) is the frozen #689 read.
    sigs = {c["seed_mode"]: c["classification"]["signature"] for c in torus}          # forward
    sigs_banked = {c["seed_mode"]: c["classification"]["signature_banked"] for c in torus}
    uniq = set(sigs.values())

    # #689 finding #5: all THREE bin-determining MIXED triggers, machine-evaluated:
    #   (1) pair vs graded_a0 energy signatures disagree;
    #   (2) energy meter and Φ_link meter disagree within a torus cell;
    #   (3) a torus cell CONCENTRATES while its PML twin does not.
    phi_sigs = {c["seed_mode"]: _sector_signature(c["trend"]["phi_link"]) for c in torus}
    twin_sigs = {m: t["classification"]["signature"] for m, t in pml_twin.items()}
    twin_sigs_banked = {m: t["classification"]["signature_banked"] for m, t in pml_twin.items()}
    mixed_reasons: list[str] = []
    if len(uniq) > 1:
        mixed_reasons.append(f"pair_vs_graded_disagree:{sigs}")
    for c in torus:
        m = c["seed_mode"]
        e_sig = c["classification"]["signature"]
        p_sig = phi_sigs[m]
        if e_sig != p_sig and "INCONCLUSIVE" not in (e_sig, p_sig):
            mixed_reasons.append(f"energy_vs_philink_disagree[{m}]:E={e_sig}/phi={p_sig}")
    for c in torus:
        m = c["seed_mode"]
        if c["classification"]["signature"] == "CONCENTRATING" and twin_sigs.get(m) != "CONCENTRATING":
            mixed_reasons.append(
                f"torus_concentrates_pml_twin_does_not[{m}]:twin={twin_sigs.get(m, 'NO-TWIN')}"
            )

    def _bin(sig_map: dict, reasons: list) -> str:
        u = set(sig_map.values())
        if not sig_map:
            return "NO-DATA"
        if u == {"INCONCLUSIVE"}:
            return "INCONCLUSIVE"
        if reasons or "MIXED" in u or "INCONCLUSIVE" in u:
            return "MIXED"
        return u.pop()

    fork_bin = _bin(sigs, mixed_reasons)                # forward (mandatory)
    fork_bin_banked = _bin(sigs_banked, [])             # frozen #689 banked
    # Boundary-insensitivity now register-explicit: torus vs PML-twin agreement.
    boundary_insensitive = {
        "forward": {m: (sigs.get(m) == twin_sigs.get(m)) for m in sigs},
        "banked": {m: (sigs_banked.get(m) == twin_sigs_banked.get(m)) for m in sigs_banked},
    }

    summary = {
        "battery": "gpersist_localization_observable",
        "prereg": PREREG,
        "addendum": ADDENDUM,
        "theta": THETA,
        "primary_core_radius": PRIMARY_R,
        "sponge_guard": SPONGE_GUARD,
        "forward_instrument": FORWARD_SECTOR,
        "banked_instrument": BANKED_SECTOR,
        "torus_signatures_forward": sigs,
        "torus_signatures_banked": sigs_banked,
        "torus_phi_link_signatures": phi_sigs,
        "pml_twin_signatures_forward": twin_sigs,
        "pml_twin_signatures_banked": twin_sigs_banked,
        "boundary_insensitive": boundary_insensitive,
        "mixed_triggers_evaluated": [
            "pair_vs_graded",
            "energy_vs_philink",
            "torus_concentrates_vs_pml_twin",
        ],
        "mixed_reasons": mixed_reasons,
        "fork_bin_forward": fork_bin,
        "fork_bin_banked": fork_bin_banked,
        "cells": [
            {
                "N": c["N"],
                "boundary": c["boundary"],
                "seed_mode": c["seed_mode"],
                "fidelity": c["fidelity"],
                "E_persist": round(c["E_persist"], 4),
                "phi_persist": round(c["phi_persist"], 4),
                "PR_energy_full": c["trend"][FORWARD_SECTOR]["PR"],
                "CF_energy_full_peak_2p0": c["trend"][FORWARD_SECTOR][f"CF_peak_{PRIMARY_R}"],
                "PR_energy_pot": c["trend"][BANKED_SECTOR]["PR"],
                "CF_energy_pot_peak_2p0": c["trend"][BANKED_SECTOR][f"CF_peak_{PRIMARY_R}"],
                "PR_phi_link": c["trend"]["phi_link"]["PR"],
                "classification": c["classification"],
            }
            for c in sorted(
                cells, key=lambda c: (c["N"], c["pml"], c["fidelity"], c["seed_mode"])
            )
        ],
        "plants": [
            {k: p[k] for k in p if k != "plant_trend_energy"} for p in plants
        ],
    }
    _write(OUT_DIR / "gpersist_localization_summary.json", summary)

    print("\n=== per-cell before/after (banked pot-only -> completed full-register) ===")
    for c in summary["cells"]:
        pr = c["PR_energy_full"]
        cf = c["CF_energy_full_peak_2p0"]
        cl = c["classification"]
        print(
            f"  N={c['N']} {c['boundary']:6s} {c['fidelity']:10s} {c['seed_mode']:10s} "
            f"E={c['E_persist']:.3f} phi={c['phi_persist']:.3f} | "
            f"{cl['signature_banked']:14s} -> {cl['signature']:14s} "
            f"(full PR {pr['rel_trend']:+.3f} CF {cf['rel_trend']:+.3f}) "
            f"move={cl['bin_move'] or 'no-move'}"
        )
    print(f"\ntorus forward signatures: {sigs}  | banked: {sigs_banked}")
    print(f"torus Φ_link signatures: {phi_sigs}")
    print(f"PML twin forward: {twin_sigs}  | banked: {twin_sigs_banked}")
    print(f"boundary-insensitive (forward): {boundary_insensitive['forward']}")
    print(f"MIXED triggers (all 3) reasons: {mixed_reasons or 'none — all clean'}")
    print(f"FORK BIN forward (energy_full, MANDATORY): {fork_bin}")
    print(f"FORK BIN banked  (energy_pot, #689 frozen): {fork_bin_banked}")
    print("\n=== φ-channel plants ===")
    for p in plants:
        print(
            f"  N={p['N']} {p['boundary']:6s} {p['seed_mode']:10s} {p['fidelity']:10s}: "
            f"free_phi={p['free_phi_persist']:.3f} plant_phi={p['plant_phi_persist']:.3f} "
            f"sustained={p['plant_phi_sustained']} loop_filling={p['plant_meter_loop_filling']} "
            f"-> {p['verdict']}"
        )
    print(f"\nsummary -> {OUT_DIR / 'gpersist_localization_summary.json'}")


def main(argv) -> None:
    if not argv:
        print(__doc__)
        return
    cmd, rest = argv[0], argv[1:]
    if cmd == "--parity":
        cmd_parity(rest)
    elif cmd == "--cell":
        cmd_cell(rest)
    elif cmd == "--plant":
        cmd_plant(rest)
    elif cmd == "--aggregate":
        cmd_aggregate()
    else:
        print(__doc__)


if __name__ == "__main__":
    main(sys.argv[1:])
