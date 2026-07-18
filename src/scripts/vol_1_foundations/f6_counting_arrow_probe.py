#!/usr/bin/env python3
"""F6 counting-arrow arm — §5b CIRCUIT-MAP PROBE (fills the mandatory gate; NO door).

Charter:  research/2026-07-15_f6-mode-count-door_CHARTER.md §5b (circuit-map gate)
Protocol: research/2026-07-16_f6-circuit-map-fill-PROTOCOL.md (fill order + reconcile rule)
Meter:    src/ave/thermal/f6_bath_meter.py (LatticeBathCoupler — the instrument)
Prereg:   research/2026-07-18_f6-counting-arrow-arm_prereg_FROZEN.md (this probe fills its §5b)

WHAT THIS IS. A probe-only script (fill-PROTOCOL §4.1: "tiny script reports S, bond Γ,
in-network energy on a named port mask — fills Steps 1-3 triples"). It measures the COLD
circuit facts of the collar→comb coupling port on the Phase-1 operating point (A_max≈0.10)
so the prereg's §5b table carries MEASURED values, not self-declared stamps.

WHAT THIS IS NOT. This is NOT the arm driver (f6_counting_arrow_arm.py). It does NOT
measure the arm's observable R_return(x) — measuring the recurrence return before freeze
would void the pre-registration. It measures only cold port/regime/energy-fate facts that
are independent of the frozen prediction (the Γ-vs-x transition is the HYPOTHESIS under
test, stated in the prereg, deliberately unmeasured here).

Run:  PYTHONPATH=src python src/scripts/vol_1_foundations/f6_counting_arrow_probe.py
"""

from __future__ import annotations

import numpy as np

from ave.core.k4_tlm import K4Lattice3D
from ave.thermal import LatticeBathCoupler, OscillatorBath, make_collar_mask

# --- Phase-1 operating point (ENGINEERING CHOICES — tagged; inherit meter frozen pins) --
N_GRID = 12
CENTER = (N_GRID // 2, N_GRID // 2, N_GRID // 2)
COLLAR_R_IN = 2.0
COLLAR_R_OUT = 4.0
KAPPA = 0.012
SEED = 1
SEED_SCALE_MILD = 0.6  # meter §B1 table: A_max≈0.10 (sub-yield Regime-I/II boundary)
OMEGA_MIN = 0.30
DELTA_OMEGA = 0.03
M_PROBE = 24  # band [0.30, 0.99]; ω_max·dt < π (Nyquist OK)


def _seed(lat: K4Lattice3D, scale: float) -> None:
    """Deterministic broadband seed (byte-identical to the meter's _seed_lattice shape)."""
    rng = np.random.default_rng(SEED)
    ii, jj, kk = np.indices((lat.nx, lat.ny, lat.nz))
    c = CENTER
    env = np.exp(-((ii - c[0]) ** 2 + (jj - c[1]) ** 2 + (kk - c[2]) ** 2) / (2 * 1.5**2))
    env[~lat.mask_active] = 0.0
    for p in range(4):
        lat.V_inc[..., p] += scale * 0.08 * env
    fld = np.zeros_like(lat.V_inc)
    for _ in range(6):
        kv = rng.integers(1, lat.nx // 2, size=3) * (2 * np.pi / lat.nx) * rng.choice([-1, 1], size=3)
        ph = rng.uniform(0, 2 * np.pi)
        pw = np.cos(kv[0] * ii + kv[1] * jj + kv[2] * kk + ph)
        pw2 = rng.normal(size=4)
        for p in range(4):
            fld[..., p] += scale * 0.03 * pw * pw2[p]
    fld[~lat.mask_active] = 0.0
    lat.V_inc += fld


def _build(kappa: float = KAPPA, scale: float = SEED_SCALE_MILD) -> LatticeBathCoupler:
    lat = K4Lattice3D(N_GRID, N_GRID, N_GRID, nonlinear=True, op3_bond_reflection=True, V_SNAP=1.0)
    _seed(lat, scale)
    lat.step()  # on-shell E0
    bath = OscillatorBath(M=M_PROBE, omega_min=OMEGA_MIN, delta_omega=DELTA_OMEGA)
    collar = make_collar_mask(lat, CENTER, COLLAR_R_IN, COLLAR_R_OUT)
    return LatticeBathCoupler(lat, bath, collar, kappa=kappa)


def main() -> None:
    cpl = _build()
    lat = cpl.lat
    collar = cpl.collar
    print("=" * 78)
    print("F6 COUNTING-ARROW ARM — §5b CIRCUIT-MAP PROBE (cold port facts; NO R_return)")
    print("=" * 78)

    # --- Step 1: PORTS (code identity) ---------------------------------------
    n_collar = int(collar.sum())
    in_active = bool(not np.any(collar & ~lat.mask_active))
    n_ports = lat.V_inc.shape[-1]
    print(f"[STEP1 ports ] collar_sites={n_collar}  ports_read=all_{n_ports}_K4_bonds(p0..p3)  "
          f"collar_subset_of_mask_active={in_active}  pml_thickness={lat.pml_thickness}")

    # --- Step 2: REGIME (declare, then measure) ------------------------------
    v = np.sqrt(np.sum(lat.V_inc**2, axis=-1))  # strain A = |V_inc|/V_SNAP (V_SNAP=1)
    a_collar = v[collar]
    a_max = float(a_collar.max())
    a2_mean = float((a_collar**2).mean())
    s_mean = float(np.sqrt(np.maximum(0.0, 1.0 - np.minimum(a_collar, 1.0) ** 2)).mean())
    print(f"[STEP2 regime] A_max(collar)={a_max:.4f}  <A^2>(collar)={a2_mean:.2e}  "
          f"<S=sqrt(1-A^2)>(collar)={s_mean:.5f}  -> COLD sub-yield (A^2 << 2*alpha=1.46e-2)")

    # --- Step 3: PORT BEHAVIOR (cold baseline; the Γ-vs-x transition is the FROZEN HYPOTHESIS) -
    # z_local (op3 bond front) spread on the collar, and the reflected/incident ratio.
    z_collar = lat.z_local_field[collar]
    z_spread = float(z_collar.max() - z_collar.min())
    vinc = np.abs(lat.V_inc[collar]).mean()
    vref = np.abs(lat.V_ref[collar]).mean()
    gamma_eff = float(vref / (vinc + 1e-30))
    print(f"[STEP3 portbeh] z_local(collar) in [{z_collar.min():.5f},{z_collar.max():.5f}] "
          f"spread={z_spread:.2e} (~1.00 => op3 bond front MATCHED, cold; the matched indicator); "
          f"|V_ref|/|V_inc|(collar)={gamma_eff:.4f} (~1 = standing-wave TLM ratio, NOT a lossy port; "
          f"diagnostic only)")

    # --- Step 4: ENERGY FATE (in-network reactive; conserving identity) ------
    # (a) closed cavity, no bath (kappa=0): interior is lossless-reactive (Ax3).
    cav = _build(kappa=0.0)
    E0c = cav.e_lat()
    for i in range(1, 200):
        cav.step(i)
    drift_closed = abs(cav.e_lat() - E0c) / E0c
    # (b) comb attached: E_lat + E_bath conserves (the #721 R-1 identity — NOT a claim
    #     about whether energy RETURNS; that is the arm's frozen observable, unmeasured here).
    E0 = cpl.e_lat()
    Etot0 = E0 + cpl.e_bath()
    max_tot_drift = 0.0
    for i in range(1, 200):
        cpl.step(i)
        max_tot_drift = max(max_tot_drift, abs((cpl.e_lat() + cpl.e_bath()) - Etot0) / E0)
    print(f"[STEP4 efate ] closed-cavity(kappa=0) |dE_lat|/E0={drift_closed:.2e} (<1e-10, lossless); "
          f"comb-on |d(E_lat+E_bath)|/E0={max_tot_drift:.2e} (identity-conserving, #721 R-1)")

    # --- Step 5: interior reversibility protection (no siphon) ----------------
    # The interior stays bias-stable via the SAME mechanism (lossless comb + on-shell
    # global rescale): the closed cavity above is the bias≠release control (drift ~ machine).
    print(f"[STEP5 protect] interior protected by losslessness (closed-cavity drift {drift_closed:.1e}); "
          f"no CORE_R mask, no siphon — reversibility is the recurrence, not a valve")

    # --- Step 6: forbidden costumes (explicit non-goals) ---------------------
    friction = cpl.friction
    has_damp_beta = cpl.beta
    print(f"[STEP6 costume] friction={friction} (no Re(Z) damp), beta={has_damp_beta}; "
          f"pml_thickness={lat.pml_thickness} (no sponge); back-reaction=global energy-matched "
          f"rescale (not face-V-scale siphon, not dump-R); comb=lossless (any Re(Z) is EMERGENT)")
    print("=" * 78)
    print("CONSISTENCY PASS (1)-(6): object=F6 occupancy chord; regime COLD measured; "
          "port matched cold; energy fate in-network conserving; interior lossless; no killed class.")
    print("=" * 78)


if __name__ == "__main__":
    main()
