#!/usr/bin/env python3
"""F6 NO-FULL-DISCHARGE calibration scan — PHASE 0 (pre-prereg; DISCLOSED as
instrument calibration).

Goal (the follow-on SPEC'd in PR #726 result §6, route-1): can the counting-arrow
cross-comb collapse be measured on the EXISTING certified instrument with the two
artifacts that ate #726's signal engineered out — (1) the argmax observable (fixed
by the first-plateau reading, reimplemented in the fire driver) and (2) the scale=0
back-reaction ABSORBING clamp (fixed by a NO-FULL-DISCHARGE operating point where the
clamp NEVER fires)? This scan searches the instrument-configuration knobs WITHIN the
certificate's scope for a cell family satisfying BOTH regime-live transfer AND no full
discharge, at >=4 comb densities spanning >= a decade of dw.

★ HARD FENCE (stated and honored): this scan measures TRANSFER quantities ONLY —
  peak_frac, t63/T_rec, clamp-fire, and the regime-side N_occ (the prereg's own regime
  gate, a spectral occupancy read). It NEVER computes R_return, return-timing, x_50,
  R_cum, or the cross-comb collapse. The collapse observable is frozen in the prereg
  AFTER this scan, never tuned on it. (N_occ is a regime-characterization quantity like
  t63/peak_frac — the "is the regime reached" side — NOT the return/collapse answer;
  recording it does not peek at the signal.)

★ THE CENTRAL SCOPE FINDING (measured, not asserted — see degeneracy_check()): in the
  meter the coupling enters ONLY as the product kappa*g (f6_bath_meter.py:198,
  `self.p += dt * kappa * self.g * q`). So a uniform per-mode weight g0 and the coupling
  kappa are EXACTLY degenerate: (kappa=0.030, g0=s) is BIT-IDENTICAL to (kappa=0.030*s,
  g0=1.0). Scaling g0 down to soften the discharge is therefore NOT "gentler at fixed
  kappa" — it is a reduction of the EFFECTIVE coupling kappa_eff = kappa*g0 BELOW the
  certified single-point band METER-VALID-KAPPA-BAND[0.030,0.030]. This is flagged for
  the review to adjudicate (task RAILS: "flag for the review"). The scan reports kappa_eff
  alongside g0 so the scope-exit is explicit at every cell.

CERTIFICATE / SCOPE:
  Instrument : src/ave/thermal/f6_bath_meter.py (LatticeBathCoupler, OscillatorBath) —
               BYTE-UNTOUCHED (only constructor args passed; no meter/engine edit).
  Certificate: METER-VALID-KAPPA-BAND[0.030,0.030] @ MILD (PR #724, standalone-K4).
  Reused BYTE-UNTOUCHED: f6_counting_arrow_arm.py (#722 _seed_lattice / grid / _m_for).
  Observable algorithm (first-plateau): reimplemented here + in the fire driver, citing
               the PR #726 branch feat/f6-certified-kappa-sweep _first_plateau_idx (NOT
               cherry-picked; reimplemented per the task RAILS).

SECTOR / REGIME:
  Sector : E-sector eps-store (F6 eps->T2 candidate). NOT A1 mass, NOT Cosserat (2,3).
  Mode   : reactive K4 TLM lattice + external Foster comb (Caldeira-Leggett).
  Regime : Regime I sub-yield, A_max~0.10 MILD, kappa=0.030 (g0 varied => kappa_eff).
  Phase  : driven-then-source-off, closed cavity (pml=0, energy-conserving).

Run: PYTHONPATH=src python src/scripts/vol_1_foundations/f6_no_discharge_scan.py [--json]
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass

import numpy as np

from ave.core.k4_tlm import K4Lattice3D
from ave.thermal import LatticeBathCoupler, OscillatorBath, make_collar_mask

# ── BYTE-UNTOUCHED plant constants (mirrors f6_counting_arrow_arm.py) ─────────
from scripts.vol_1_foundations.f6_counting_arrow_arm import (
    CENTER,
    COLLAR_R_IN,
    COLLAR_R_OUT,
    N_GRID,
    OMEGA_MIN,
    _m_for,
    _seed_lattice,
)

# ── the certified cell (fixed) ───────────────────────────────────────────────
KAPPA = 0.030            # the certified point [0.030,0.030] — NEVER changed here
SEED_SCALE_MILD = 0.6    # MILD, A_max~0.10 — the certified operating point

# ── scan grids (ENGINEERING CHOICES — tagged) ────────────────────────────────
# Uniform per-mode coupling weight g0 (OscillatorBath.g0). kappa_eff = KAPPA*g0.
G0_GRID = (1.0, 0.7, 0.5, 0.35, 0.25)
# Comb density grid spanning >= a decade (0.008 -> 0.080). >=3 pts/decade.
DW_GRID = (0.008, 0.010, 0.013, 0.016, 0.020, 0.030, 0.050, 0.080)
HORIZON_RECURRENCES = 11  # the full prereg window (clamp must NEVER fire over ALL of it)

# ── the three scan conditions (frozen for the scan; NOT the prereg verdict tree) ──
T63_GATE = 0.5          # regime gate: transfer >=63%-done by the half-recurrence
PEAK_FRAC_MAX = 0.85    # NO-FULL-DISCHARGE: first-plateau transfer stays <= 0.85
NOCC_GATE = 10          # regime gate (reported; the prereg's floor)
EPS_CLAMP = 1e-12       # E_lat <= this => the scale=0 clamp has hard-zeroed the lattice
PLATEAU_PROM = 0.05     # transfer-complete prominence tol (frac of E0) — #726 R-1 value
INV_E = 1.0 - 1.0 / np.e


def _build_scan(delta_omega: float, m: int, g0: float,
                kappa: float = KAPPA, scale: float = SEED_SCALE_MILD) -> LatticeBathCoupler:
    """Coupled meter on a standalone-K4 plant with a uniform per-mode weight g0.

    IDENTICAL to f6_counting_arrow_arm._build except (a) kappa=0.030 (certified) and
    (b) the bath is built with g0 (default 1.0 in the arm). The meter module is
    BYTE-UNTOUCHED — g0 is an OscillatorBath constructor arg (f6_bath_meter.py:102).
    """
    lat = K4Lattice3D(N_GRID, N_GRID, N_GRID, nonlinear=True, op3_bond_reflection=True, V_SNAP=1.0)
    _seed_lattice(lat, scale)
    lat.step()  # on-shell baseline
    bath = OscillatorBath(M=m, omega_min=OMEGA_MIN, delta_omega=delta_omega, g0=g0)
    collar = make_collar_mask(lat, CENTER, COLLAR_R_IN, COLLAR_R_OUT)
    return LatticeBathCoupler(lat, bath, collar, kappa=kappa)


def _clamp_onset(e_lat: np.ndarray) -> int:
    """First step where the scale=0 back-reaction clamp has hard-zeroed the lattice
    (E_lat <= EPS_CLAMP). Returns len(e_lat) if it never fires (window is the whole run).
    Reimplements PR #726 branch feat/f6-certified-kappa-sweep `_clamp_onset` (R-2)."""
    hit = np.nonzero(e_lat <= EPS_CLAMP)[0]
    return int(hit[0]) if hit.size else len(e_lat)


def _first_plateau_idx(e_bath: np.ndarray, e0: float, phys_end: int) -> int:
    """First-plateau / transfer-complete peak: the first local E_bath max in the
    PHYSICAL (pre-clamp) window whose following dip exceeds PLATEAU_PROM*E0 before
    recovery. Falls back to the pre-clamp argmax. Reimplements PR #726 branch
    feat/f6-certified-kappa-sweep `_first_plateau_idx` (R-1 — the argmax fix)."""
    prom = PLATEAU_PROM * e0
    for i in range(1, max(phys_end - 1, 1)):
        if e_bath[i] >= e_bath[i - 1] and e_bath[i] > e_bath[i + 1]:
            for j in range(i + 1, phys_end):
                if e_bath[j] >= e_bath[i]:
                    break
                if e_bath[i] - e_bath[j] >= prom:
                    return i
    return int(np.argmax(e_bath[:phys_end])) if phys_end > 0 else 0


@dataclass
class ScanCell:
    delta_omega: float
    M: int
    g0: float
    kappa_eff: float          # KAPPA * g0 — the effective coupling (degeneracy, scope)
    t_rec: float
    n_steps_run: int          # may be < 11*T_rec if the clamp fired (early stop)
    n_steps_full: int         # the full 11*T_rec window
    e0: float
    # ── TRANSFER quantities ONLY (the fence) ──
    peak_frac: float          # first-plateau E_bath/E0 (honest transfer health)
    first_plateau_x: float
    t63_over_trec: float
    n_occ: int                # spectral occupancy (regime side)
    min_elat_frac: float      # min E_lat/E0 over the physical window (discharge depth)
    clamp_fires: bool
    clamp_x: float
    frac_dead: float
    max_cons_drift: float
    # ── the three scan conditions ──
    transfer_live: bool       # t63/T_rec <= T63_GATE
    no_full_discharge: bool   # peak_frac <= PEAK_FRAC_MAX
    clamp_never: bool         # not clamp_fires
    nocc_ok: bool             # n_occ >= NOCC_GATE (reported; the prereg regime floor)
    satisfies_scan: bool      # transfer_live AND no_full_discharge AND clamp_never


def scan_cell(delta_omega: float, g0: float, kappa: float = KAPPA) -> ScanCell:
    """Run one (dw, g0) comb over the full 11*T_rec window (early-stop on clamp) and
    record the TRANSFER quantities. FENCE: no R_return / x_50 / collapse computed."""
    m = _m_for(delta_omega)
    t_rec = 2 * np.pi / delta_omega
    n_full = int(round(HORIZON_RECURRENCES * t_rec))
    cpl = _build_scan(delta_omega, m, g0, kappa=kappa)
    e0 = cpl.e_lat()
    etot0 = e0 + cpl.e_bath()
    e_lat = np.empty(n_full)
    e_bath = np.empty(n_full)
    max_drift = 0.0
    ran = n_full
    for k in range(n_full):
        cpl.step(k + 1)
        e_lat[k] = cpl.e_lat()
        e_bath[k] = cpl.e_bath()
        max_drift = max(max_drift, abs((e_lat[k] + e_bath[k]) - etot0) / e0)
        if e_lat[k] <= EPS_CLAMP:  # clamp fired — physical info ends; stop (still full window known)
            ran = k + 1
            break
    e_lat = e_lat[:ran]
    e_bath = e_bath[:ran]
    steps = np.arange(1, ran + 1)
    x = steps * delta_omega / (2 * np.pi)

    phys_end = _clamp_onset(e_lat)
    clamp_fires = phys_end < ran or ran < n_full  # clamp within full window
    clamp_x = float(x[phys_end]) if phys_end < ran else float("nan")
    frac_dead = (n_full - phys_end) / n_full if phys_end < ran else 0.0

    t_fp = _first_plateau_idx(e_bath, e0, phys_end)
    e_bath_peak = float(e_bath[t_fp])
    peak_frac = e_bath_peak / e0
    hit63 = np.nonzero(e_bath >= INV_E * e_bath_peak)[0]
    t63 = int(steps[hit63[0]]) if hit63.size else n_full
    n_occ = cpl.bath.n_occ()
    min_elat_frac = float(e_lat[:phys_end].min()) / e0 if phys_end > 0 else 0.0

    transfer_live = bool(t63 / t_rec <= T63_GATE)
    no_full_discharge = bool(peak_frac <= PEAK_FRAC_MAX)
    clamp_never = bool(not clamp_fires)
    return ScanCell(
        delta_omega=delta_omega, M=m, g0=g0, kappa_eff=kappa * g0, t_rec=t_rec,
        n_steps_run=ran, n_steps_full=n_full, e0=e0,
        peak_frac=peak_frac, first_plateau_x=float(x[t_fp]),
        t63_over_trec=t63 / t_rec, n_occ=n_occ, min_elat_frac=min_elat_frac,
        clamp_fires=clamp_fires, clamp_x=clamp_x, frac_dead=frac_dead,
        max_cons_drift=max_drift,
        transfer_live=transfer_live, no_full_discharge=no_full_discharge,
        clamp_never=clamp_never, nocc_ok=bool(n_occ >= NOCC_GATE),
        satisfies_scan=bool(transfer_live and no_full_discharge and clamp_never),
    )


def degeneracy_check() -> dict:
    """The CENTRAL SCOPE FINDING, measured: (kappa=0.030, g0=0.5) is BIT-IDENTICAL to
    (kappa=0.015, g0=1.0). Proves kappa and g0 enter only as kappa*g0, so a g0-scaled
    'no-discharge' cell runs at kappa_eff < 0.030 — OUTSIDE the certified band. Records
    the max abs diff of the two E_bath / E_lat trajectories over a short window."""
    dw = 0.020
    m = _m_for(dw)
    nsteps = 400

    def _traj(kappa, g0):
        cpl = _build_scan(dw, m, g0, kappa=kappa)
        e0 = cpl.e_lat()
        eb = np.empty(nsteps)
        el = np.empty(nsteps)
        for k in range(nsteps):
            cpl.step(k + 1)
            eb[k] = cpl.e_bath()
            el[k] = cpl.e_lat()
        return e0, eb, el, cpl.bath.n_occ()

    e0a, eba, ela, na = _traj(0.030, 0.5)   # certified kappa, g0=0.5
    e0b, ebb, elb, nb = _traj(0.015, 1.0)   # half kappa, g0=1.0
    return {
        "note": "kappa and g0 enter the meter ONLY as kappa*g0 (f6_bath_meter.py:198). "
                "(kappa=0.030,g0=0.5) vs (kappa=0.015,g0=1.0) => kappa_eff=0.015 both.",
        "dw": dw, "nsteps": nsteps,
        "e0_match": bool(e0a == e0b),
        "max_ebath_absdiff": float(np.max(np.abs(eba - ebb))),
        "max_elat_absdiff": float(np.max(np.abs(ela - elb))),
        "n_occ_a": na, "n_occ_b": nb, "n_occ_match": bool(na == nb),
        "bit_identical": bool(e0a == e0b
                              and np.max(np.abs(eba - ebb)) == 0.0
                              and np.max(np.abs(ela - elb)) == 0.0
                              and na == nb),
    }


def _in_scope(c: ScanCell) -> bool:
    """A cell is on the CERTIFIED instrument iff kappa_eff == KAPPA exactly, i.e. g0==1.0.
    The (kappa,g0) degeneracy (degeneracy_check) makes any g0<1.0 bit-identical to a run
    at kappa<0.030 — OUTSIDE the certified single-point band [0.030,0.030] and inside the
    region the task fenced out ('NOT kappa != 0.030')."""
    return abs(c.kappa_eff - KAPPA) < 1e-12


def run_scan() -> dict:
    cells = [scan_cell(dw, g0) for g0 in G0_GRID for dw in DW_GRID]
    # per-g0: raw satisfying (three transfer conditions) AND usable (also in-scope + N_occ).
    # A cell is USABLE for the counting-arrow collapse only if it ALSO (i) stays on the
    # certified instrument (kappa_eff==0.030 => g0==1.0; the degeneracy) AND (ii) reaches
    # the quasi-continuum (N_occ>=10; the prereg's OWN frozen regime gate — a cell below it
    # returns REGIME-NOT-REACHED, question UNASKED). Both are PRE-EXISTING hard constraints,
    # not post-hoc goalposts: (i) is the task's kappa fence, (ii) is the inherited #726 tree.
    per_g0 = {}
    for g0 in G0_GRID:
        rows = [c for c in cells if c.g0 == g0]
        sat = [c for c in rows if c.satisfies_scan]                       # raw 3 conditions
        usable = [c for c in sat if _in_scope(c) and c.nocc_ok]           # + scope + regime
        dws = sorted(c.delta_omega for c in sat)
        udws = sorted(c.delta_omega for c in usable)
        decade = (max(udws) / min(udws) >= 10.0) if len(udws) >= 2 else False
        per_g0[g0] = {
            "kappa_eff": KAPPA * g0,
            "in_scope": bool(_in_scope(rows[0])),
            "n_satisfying_raw": len(sat),
            "satisfying_dws_raw": dws,
            "n_usable": len(usable),                # in-scope + N_occ>=10 + the 3 conditions
            "usable_dws": udws,
            "spans_decade": bool(decade),
        }
    # OUTCOME (folds in the two pre-existing constraints — honest, not the raw flag):
    #   (a) a g0 (necessarily g0==1.0, in scope) with >=4 USABLE densities spanning a decade
    #   (b) >=1 USABLE cell exists but not a full decade-family (freeze on what exists)
    #   (c) NO USABLE cell exists in scope => INSTRUMENT-INCOMPATIBLE (DO NOT FIRE)
    total_usable = sum(v["n_usable"] for v in per_g0.values())
    any_full_family = any(v["n_usable"] >= 4 and v["spans_decade"] for v in per_g0.values())
    total_raw = sum(v["n_satisfying_raw"] for v in per_g0.values())
    if any_full_family:
        outcome = "A_SATISFYING_FAMILY"
    elif total_usable >= 1:
        outcome = "B_PARTIAL"
    else:
        outcome = "C_INSTRUMENT_INCOMPATIBLE"
    best = max(per_g0.values(), key=lambda v: (v["n_usable"], v["n_satisfying_raw"]))
    return {
        "meta": {
            "lane": "F6 NO-FULL-DISCHARGE calibration scan (PHASE 0; pre-prereg)",
            "fence": "TRANSFER quantities ONLY (peak_frac, t63/T_rec, clamp-fire, N_occ). "
                     "NEVER R_return/return-timing/x_50/collapse.",
            "kappa": KAPPA, "operating_point": "MILD (scale=0.6)",
            "instrument": "f6_bath_meter.py (BYTE-UNTOUCHED; g0 = constructor arg)",
            "conditions": {
                "transfer_live": f"t63/T_rec <= {T63_GATE}",
                "no_full_discharge": f"peak_frac(first-plateau) <= {PEAK_FRAC_MAX}",
                "clamp_never": "E_lat never <= EPS over the full 11*T_rec window",
                "nocc_reported": f"N_occ >= {NOCC_GATE} (prereg regime floor; reported)",
            },
        },
        "degeneracy": degeneracy_check(),
        "outcome": outcome,
        "totals": {
            "n_satisfying_raw": total_raw,   # cells tripping the 3 transfer conditions
            "n_usable": total_usable,        # + in-scope (kappa_eff==0.030) + N_occ>=10
        },
        # transparency: the raw-satisfying cells that are DISQUALIFIED and why
        "disqualified_raw_satisfiers": [
            {
                "g0": c.g0, "kappa_eff": c.kappa_eff, "delta_omega": c.delta_omega,
                "n_occ": c.n_occ, "peak_frac": c.peak_frac, "t63_over_trec": c.t63_over_trec,
                "out_of_scope": bool(not _in_scope(c)),
                "regime_not_reached_nocc": bool(not c.nocc_ok),
            }
            for g0 in G0_GRID for c in [x for x in cells if x.g0 == g0]
            if c.satisfies_scan and not (_in_scope(c) and c.nocc_ok)
        ],
        # the in-scope (g0=1.0, kappa_eff=0.030) reality: does ANY N_occ>=10 comb avoid the clamp?
        "in_scope_quasicontinuum_all_clamp": bool(
            all(c.clamp_fires for c in cells if _in_scope(c) and c.nocc_ok)
            and any(_in_scope(c) and c.nocc_ok for c in cells)
        ),
        "per_g0": {str(k): v for k, v in per_g0.items()},
        "best_g0_summary": best,
        "cells": [asdict(c) for c in cells],
    }


def _fmt(c: dict) -> str:
    flags = "".join([
        "T" if c["transfer_live"] else "-",
        "P" if c["no_full_discharge"] else "-",
        "C" if c["clamp_never"] else "-",
        "N" if c["nocc_ok"] else "-",
    ])
    star = " <== SAT" if c["satisfies_scan"] else ""
    cx = f"{c['clamp_x']:.2f}" if c["clamp_fires"] else " -- "
    return (f"g0={c['g0']:.2f} keff={c['kappa_eff']:.4f} dw={c['delta_omega']:.3f} "
            f"M={c['M']:>3d} peak={c['peak_frac']:.3f} t63/Trec={c['t63_over_trec']:.3f} "
            f"Nocc={c['n_occ']:>2d} minElat={c['min_elat_frac']:.2e} clampx={cx} "
            f"[{flags}]{star}")


def main() -> None:
    ap = argparse.ArgumentParser(description="F6 NO-FULL-DISCHARGE calibration scan (Phase 0)")
    ap.add_argument("--json", action="store_true", help="emit JSON")
    args = ap.parse_args()

    out = run_scan()
    if args.json:
        print(json.dumps(out, indent=2, default=lambda o: None))
        return

    print("=" * 100)
    print("F6 NO-FULL-DISCHARGE CALIBRATION SCAN (PHASE 0) — FENCE: transfer quantities only")
    print("=" * 100)
    d = out["degeneracy"]
    print(f"DEGENERACY (scope): (k=0.030,g0=0.5) vs (k=0.015,g0=1.0) bit_identical={d['bit_identical']} "
          f"(max|dE_bath|={d['max_ebath_absdiff']:.1e}, N_occ {d['n_occ_a']}=={d['n_occ_b']})")
    print("  => g0-scaling IS kappa-scaling; kappa_eff=KAPPA*g0 EXITS the certified [0.030,0.030] band.")
    print("-" * 100)
    print("Flags: [T]ransfer-live(t63/Trec<=0.5) [P]artial(peak<=0.85) [C]lamp-never [N]occ>=10")
    for c in out["cells"]:
        print("  " + _fmt(c))
    print("-" * 100)
    for g0, v in out["per_g0"].items():
        scope = "IN-SCOPE" if v["in_scope"] else "OUT-OF-SCOPE(kappa_eff<0.030)"
        print(f"  g0={g0} keff={v['kappa_eff']:.4f} [{scope}]: raw-satisfying={v['n_satisfying_raw']} "
              f"{v['satisfying_dws_raw']}; USABLE(+scope+Nocc>=10)={v['n_usable']} {v['usable_dws']} "
              f"decade={v['spans_decade']}")
    print("-" * 100)
    if out["disqualified_raw_satisfiers"]:
        print("  RAW-satisfying cells that are DISQUALIFIED (reported for transparency):")
        for d in out["disqualified_raw_satisfiers"]:
            why = []
            if d["out_of_scope"]:
                why.append(f"OUT-OF-SCOPE(kappa_eff={d['kappa_eff']:.4f}<0.030)")
            if d["regime_not_reached_nocc"]:
                why.append(f"REGIME-NOT-REACHED(N_occ={d['n_occ']}<{NOCC_GATE})")
            print(f"    g0={d['g0']} dw={d['delta_omega']:.3f}: {' + '.join(why)}")
    print(f"  in-scope quasi-continuum (N_occ>=10) cells ALL clamp: "
          f"{out['in_scope_quasicontinuum_all_clamp']}")
    print(f"  totals: raw-satisfying={out['totals']['n_satisfying_raw']}  "
          f"USABLE(in-scope+regime)={out['totals']['n_usable']}")
    print("-" * 100)
    print(f"OUTCOME: {out['outcome']}")
    print("=" * 100)


if __name__ == "__main__":
    main()
