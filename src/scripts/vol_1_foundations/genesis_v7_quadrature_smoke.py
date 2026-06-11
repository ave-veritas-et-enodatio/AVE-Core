"""
genesis-v7 PHASE-2 — THE D13 QUADRATURE-DEPOSIT SMOKE (THE GATE)
================================================================

The centerpiece (prereg `research/2026-06-10_genesis-v7-quadrature_prereg.md`,
FROZEN before this run). D13 = the wall's extracted photon spin is deposited NOT
as a rigid-azimuthal δπ_ω (v6, which `_lock_relax` drains) but as a POLOIDAL-
PROJECTING LC quadrature (δω cos(qψ) + δπ_ω sin(qψ)) on the g_wall shell — a
zero-net-axial-AM winding the lock's net-L removal cannot drain. D14 = the
lock-survival discriminator.

THE SMOKE measures, FROM the evolved field (ave-driver-script-honesty), the
mini-prereg (§ headers below):
  (i)   NET FIELD poloidal deposit (MAIN − transducer-OFF, same handedness) vs the
        un-drained (lock-OFF) field reference vs the F-EXCHANGE floor — THE
        GROSS-VS-FIELD RULE (the headline is the FIELD, never the accumulator).
  (ii)  D14 lock-ON vs lock-OFF survival of the poloidal field + the v6 RIGID
        deposit control reproduced as the KNOWN-DRAIN (axial AM, lock-ON/OFF).
  (iii) helicity-odd (RH ↔ LH sign reversal; achiral structural null).
  (iv)  the AM ledger closes 1:1 (the rigid transfer untouched) + passive (E_abs≥0).
  (v)   the achiral + transducer-OFF nulls (structural zeros).
  (vi)  knob sweeps (alpha_pol, q_dep, chi_exch, lock_eta, omega_recipient_frac,
        wall_width — §210-COMPLIANCE).

GATE BINS (FROZEN): QUADRATURE-LIVE / DRAINED-AGAIN (name the sink) / UNRESOLVED /
BUILD-BLOCKED. Rule 11: the bins are frozen; no post-hoc criterion drop.

GROSS-VS-FIELD NOTE: the per-step bookkeeping accumulator `pol_deposit_accum` is in
amplitude×volume units, NOT field-comparable to the LC-quadrature content C_pol.
The field-comparable UN-DRAINED reference is the lock-OFF field (the deposit
accumulated with no drain). Survival = C_pol(lock-ON)/C_pol(lock-OFF); v6's rigid
analog L_om(ON)/L_om(OFF) is the known 4-OOM drain. Field-to-field, per the rule.
"""

from __future__ import annotations

import json
import os
import sys
import time

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from ave.core.unified_genesis_engine import UnifiedGenesisEngine  # noqa: E402

N_MAIN = 28
N_STEPS = 200
FRAC, DRIVE_AMP, WAVELEN, SIGMA_PH, SIGMA_SEED = 0.95, 0.10, 8.0, 5.0, 5.0
CHI_DEFAULT, ETA_DEFAULT, AXIS = 0.02, 0.08, 2
PHI2 = ((1.0 + np.sqrt(5.0)) / 2.0) ** 2

# FROZEN gate thresholds (mini-prereg)
SURVIVE_MIN = 0.1        # poloidal SURVIVES if C_pol(ON)/C_pol(OFF) ≥ 0.1 (gap ≲1 OOM)
RIGID_DRAIN_MAX = 0.5    # the v6 rigid control must DRAIN: L_om(ON)/L_om(OFF) ≤ 0.5 at 200 steps
FLOOR_MULT = 100.0       # net field MAIN−OFF ≥ 100× F-EXCHANGE
ODD_FRAC_MIN = 0.9       # helicity-odd: |RH−LH|/(|RH|+|LH|) > 0.9
ALPHA0_FLOOR_MULT = 100.0  # the α_pol=0 (rigid) control: C_pol ≤ 1/100 of α_pol=1


def build(helicity, chi, alpha_pol, *, lock, quad, q=3, eta=ETA_DEFAULT,
          wall_width=0.12, frac_om=1.0, N=N_MAIN):
    """Transducer-ISOLATED (buckle OFF; ω the only transducer recipient) — the
    clean reference for the poloidal channel + the v6 rigid control."""
    e = UnifiedGenesisEngine(
        N, bulk_density_on=True, snap_on=False, omega_sector_on=True,
        buckle_on=False, lock_on=lock, lock_eta=eta, transducer_on=(chi > 0.0),
        chi_exch=chi, omega_recipient_frac=frac_om, quadrature_deposit=quad,
        alpha_pol=alpha_pol, q_dep=q, p_dep=2, wall_width=wall_width,
        pol_R=0.30 * N, pol_r=0.30 * N / PHI2)
    c = (N - 1) / 2.0
    e.seed_bulk((c, c, c), sigma=SIGMA_SEED, frac=FRAC, helical=False)
    e.freeze_wall_window()
    e.drive_chiral_photon(helicity=helicity, sigma=SIGMA_PH, wavelength=WAVELEN,
                          amplitude=DRIVE_AMP, axis=AXIS)
    for _ in range(N_STEPS):
        e.step()
    return e


def main():
    t0 = time.time()
    R = {}

    # ── (v) FLOOR: transducer-OFF (chi=0), same handedness — the F-EXCHANGE floor ──
    e_floor = build(+1, 0.0, 1.0, lock=True, quad=True)
    C_floor = e_floor.poloidal_quadrature_content()
    R["F_EXCHANGE_C_pol_off"] = C_floor

    # ── (i) NET FIELD poloidal deposit (MAIN − OFF) + (ii) D14 survival ──
    e_on = build(+1, CHI_DEFAULT, 1.0, lock=True, quad=True)
    e_off = build(+1, CHI_DEFAULT, 1.0, lock=False, quad=True)
    C_on, C_off = e_on.poloidal_quadrature_content(), e_off.poloidal_quadrature_content()
    netfield = C_on - C_floor
    survive_ratio = abs(C_on) / (abs(C_off) + 1e-30)
    led = e_on.transducer_ledger()
    R["poloidal"] = {
        "C_pol_lock_on": C_on, "C_pol_lock_off": C_off,
        "net_field_main_minus_off": netfield,
        "accumulator_bookkeeping": led["pol_deposit_accum"],
        "survive_ratio_on_over_off": survive_ratio,
        "above_floor_mult": abs(netfield) / (abs(C_floor) + 1e-30),
        "E_pol_deposit": led["E_pol_deposit"], "pol_events": led["pol_deposit_events"],
    }

    # ── (ii) the v6 RIGID deposit control: the KNOWN axial-AM lock-drain ──
    r_on = build(+1, CHI_DEFAULT, 0.0, lock=True, quad=False)
    r_off = build(+1, CHI_DEFAULT, 0.0, lock=False, quad=False)
    Lr_on = r_on.angular_momentum_omega_axial()
    Lr_off = r_off.angular_momentum_omega_axial()
    rigid_ratio = abs(Lr_on) / (abs(Lr_off) + 1e-30)
    R["rigid_control_v6"] = {
        "L_om_axial_lock_on": Lr_on, "L_om_axial_lock_off": Lr_off,
        "drain_ratio_on_over_off": rigid_ratio,
        "accumulator_L_transferred_omega": r_on.L_transferred_omega,
    }

    # ── (iii) helicity-odd + achiral null ──
    c_rh = e_on.poloidal_quadrature_content()
    c_lh = build(-1, CHI_DEFAULT, 1.0, lock=True, quad=True).poloidal_quadrature_content()
    c_ac = build(0, CHI_DEFAULT, 1.0, lock=True, quad=True).poloidal_quadrature_content()
    odd_frac = abs(c_rh - c_lh) / (abs(c_rh) + abs(c_lh) + 1e-30)
    R["helicity"] = {"RH": c_rh, "LH": c_lh, "achiral": c_ac, "odd_frac": odd_frac}

    # ── (iv) AM ledger 1:1 + passive ──
    R["ledger"] = {
        "ratio_removed_over_transferred": led["ledger_ratio_removed_over_transferred"],
        "L_eq_Lu_plus_Lom": abs(led["L_transferred"]
                                - (led["L_transferred_u"] + led["L_transferred_omega"])),
        "passive_no_pump": led["passive_no_pump"], "E_absorbed": led["E_absorbed_sink"],
    }

    # ── (vi) MANDATED knob sweeps (§210) ──
    sweeps = {}
    sweeps["alpha_pol"] = {f"{a:.2f}": build(+1, CHI_DEFAULT, a, lock=True, quad=True)
                           .poloidal_quadrature_content() for a in (0.0, 0.25, 0.5, 0.75, 1.0)}
    sweeps["q_dep"] = {str(q): build(+1, CHI_DEFAULT, 1.0, lock=True, quad=True, q=q)
                       .poloidal_quadrature_content(q=q) for q in (2, 3, 4)}
    sweeps["chi_exch"] = {f"{chi:.0e}": build(+1, chi, 1.0, lock=True, quad=True)
                          .poloidal_quadrature_content() for chi in (9e-4, 0.005, 0.02, 0.08)}
    sweeps["lock_eta"] = {f"{eta:.2f}": build(+1, CHI_DEFAULT, 1.0, lock=True, quad=True, eta=eta)
                          .poloidal_quadrature_content() for eta in (0.0, 0.05, 0.08, 0.12)}
    sweeps["omega_recipient_frac"] = {
        f"{fr:.1f}": build(+1, CHI_DEFAULT, 1.0, lock=True, quad=True, frac_om=fr)
        .poloidal_quadrature_content() for fr in (0.0, 0.5, 1.0)}
    sweeps["wall_width"] = {f"{ww:.2f}": build(+1, CHI_DEFAULT, 1.0, lock=True, quad=True, wall_width=ww)
                            .poloidal_quadrature_content() for ww in (0.06, 0.12, 0.20)}
    R["sweeps"] = sweeps

    # ──────────────────────────── BINNING (FROZEN) ────────────────────────────
    a0 = abs(sweeps["alpha_pol"]["0.00"])
    a1 = abs(sweeps["alpha_pol"]["1.00"])
    eta_vals = [abs(v) for v in sweeps["lock_eta"].values()]
    eta_flat = (max(eta_vals) - min(eta_vals)) / (max(eta_vals) + 1e-30) < 0.05
    checks = {
        "net_field_above_floor": abs(netfield) >= FLOOR_MULT * abs(C_floor) or C_floor == 0.0,
        "poloidal_survives_lock": survive_ratio >= SURVIVE_MIN,
        "rigid_control_drains": rigid_ratio <= RIGID_DRAIN_MAX,
        "helicity_odd": odd_frac > ODD_FRAC_MIN and c_rh * c_lh < 0.0,
        "achiral_null": c_ac == 0.0,
        "ledger_1to1": abs(R["ledger"]["ratio_removed_over_transferred"] - 1.0) < 1e-9,
        "passive": led["passive_no_pump"],
        "alpha0_is_rigid_control": a0 <= a1 / ALPHA0_FLOOR_MULT,
        "survival_eta_independent": eta_flat,
    }
    R["checks"] = checks

    if not all(checks.values()):
        if checks["net_field_above_floor"] and checks["poloidal_survives_lock"] is False \
           and checks["rigid_control_drains"]:
            verdict = "DRAINED-AGAIN"  # poloidal above floor but drained like the rigid
        elif not checks["net_field_above_floor"]:
            verdict = "UNRESOLVED"
        else:
            verdict = "UNRESOLVED"
    else:
        verdict = "QUADRATURE-LIVE"
    R["verdict"] = verdict
    R["wall_time_s"] = round(time.time() - t0, 1)

    # ──────────────────────────────── REPORT ──────────────────────────────────
    print("=" * 74)
    print("genesis-v7 D13 QUADRATURE-DEPOSIT SMOKE")
    print("=" * 74)
    print(f"\n(i) NET FIELD (gross-vs-field): C_pol MAIN(lock-on)={C_on:+.4e}")
    print(f"    transducer-OFF floor C_pol={C_floor:+.3e}  ⇒  MAIN−OFF={netfield:+.4e}"
          f"  ({R['poloidal']['above_floor_mult']:.1e}× floor)")
    print(f"    [bookkeeping accumulator (NOT headline)={led['pol_deposit_accum']:+.3e}]")
    print(f"\n(ii) D14 SURVIVAL  poloidal C_pol(on)/C_pol(off) = {survive_ratio:.4f}"
          f"   {'SURVIVES' if survive_ratio>=SURVIVE_MIN else 'DRAINED'}")
    print(f"     v6 RIGID control L_om(on)/L_om(off)        = {rigid_ratio:.4f}"
          f"   {'DRAINS (v6 reproduced)' if rigid_ratio<=RIGID_DRAIN_MAX else 'NOT-DRAINED'}")
    print(f"     (rigid lock-off L_om={Lr_off:+.3e} → lock-on {Lr_on:+.3e})")
    print(f"\n(iii) HELICITY-ODD  RH={c_rh:+.3e} LH={c_lh:+.3e} achiral={c_ac:+.1e}"
          f"  odd_frac={odd_frac:.4f}")
    print(f"(iv) LEDGER 1:1 ratio={R['ledger']['ratio_removed_over_transferred']:.9f}"
          f"  passive={led['passive_no_pump']}  E_abs={led['E_absorbed_sink']:.3e}")
    print("\n(vi) SWEEPS:")
    for k, v in sweeps.items():
        print(f"  {k:22s} " + "  ".join(f"{kk}:{vv:+.2e}" for kk, vv in v.items()))
    print("\nCHECKS:")
    for k, v in checks.items():
        print(f"  [{'PASS' if v else 'FAIL'}] {k}")
    print("\n" + "=" * 74)
    print(f"GATE VERDICT: {verdict}   ({R['wall_time_s']}s)")
    print("=" * 74)

    out = os.path.join(os.path.dirname(__file__), "..", "..", "..", "research",
                       "2026-06-10_genesis-v7-quadrature-smoke_results.json")
    with open(os.path.abspath(out), "w") as f:
        json.dump(R, f, indent=2, default=float)
    print(f"results → {os.path.abspath(out)}")
    return verdict


if __name__ == "__main__":
    v = main()
    sys.exit(0 if v in ("QUADRATURE-LIVE", "DRAINED-AGAIN") else 1)
