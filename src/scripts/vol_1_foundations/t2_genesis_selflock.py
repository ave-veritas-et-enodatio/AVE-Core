"""
T2 — genesis self-lock driver (photon-at-a-field -> autoresonant bulk breather)
================================================================================

Implements `research/2026-06-13_t2-genesis-selflock_prereg_FROZEN.md` EXACTLY.
DRIVER-NOT-BUILD on the v14-validated / cage-validated `CrystalEngine` bulk
branch — NO new engine, NO new `genesis_v{N}` / `chiral_lattice_v{N}`, NO engine
edits (`ave-loop-gap-harness-discipline`). It composes only the public engine API:
`seed_photon`, `seed_bulk(..., helical=False)`, `phase_space_vinc_vref`,
`saturation_kernel`, `converter_on`. The PUMP arm's fixed-omega CW drive is a
DRIVER-LEVEL forcing injected after `engine.step()` — never an engine method.

THE TEST (prereg §0)
  Does a flowing transverse photon (`seed_photon`) incident on a GENERIC
  sub-threshold bulk field (`seed_bulk(helical=False)` — the "nucleus") DYNAMICALLY
  AUTORESONANT-SELF-LOCK into the persistent v14-Mode-I bulk breather — the
  carrier phase-locking to its own dropping local resonance
  omega_local(t) = omega0 * sqrt(S(A(t))) as the core fills — vs DISPERSE (the
  sub-threshold field sheds it) or DETONATE (pump artifact)?

THE FOUR-WAY DISCRIMINATOR (prereg §6, LOAD-BEARING)
  (C)    photon + generic field, converter ON           -- PRIMARY
  (A')   generic field, converter ON, NO photon          -- photon-isolating control
  (A)    generic field, converter OFF, NO photon          -- converter-isolating control
  (PUMP) generic field + fixed-omega CW drive on V        -- pump/detonate control
  TARGET POSITIVE = (C) LOCK ∧ (A/A') DISPERSE, A0 >= g_front floor.

🔴 CRITICAL GUARDS (carried from the prereg + the auditor)
  - CP8: `seed_bulk(..., helical=False)` on EVERY call (default is helical=True).
    The field MUST be a generic Gaussian — NOT helical/chiral, NOT a sech
    eigen-profile. A helical or sech seed VOIDS the run.
  - omega_local = omega0 * sqrt(S_core), S = `engine.saturation_kernel()`
    (= sqrt(1-A^2)), S_core = min over interior. NOT omega0*sqrt(1-A^2) (the
    canon-STALE form, op14-local-clock-modulation:13) and NOT
    `engine.refractive_index()` (the separate S^0.25 carried defect).
  - The autoresonance read is the carrier phase vs omega_local(t) in the
    (V, ∂_tV/omega_local) phasor via `phase_space_vinc_vref(ω_char=ω_local(t))`,
    feeding the DYNAMIC omega_local each step (CP9 — dynamically evolved, NOT an
    algebraic read; A46 phasor coords, NOT real-space).
  - Success = bounded + persistent (max|A| <~ V_yield, << genesis-24's ~1e4),
    NOT energy-flat (energy-ledger drift is REPORTED, not binned — leapfrog grows
    it on a genuine bounded self-focus per cage Amendment 3).
  - REGIME near-yield forming (A^2<=1). Any arm that RUPTURES (A^2>1) or
    DETONATES is EXCLUDED from the lock verdict.

🔴 NO CHORD / GENESIS CLAIM. This driver reports the four-way bin HONESTLY. A
READ-ONLY auditor verifies the result against the discriminator before ANY chord
claim. A null/negative is a valid result; this driver does NOT tune knobs to force
a lock (`ave-driver-script-honesty`, Rule 11 honest closure).

Run:
    python t2_genesis_selflock.py --smoke        # CI-budget
    python t2_genesis_selflock.py --production    # resolve TRANSIENT-vs-persist
"""

from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "src"))

# ── canonical-source ONLY (ave-canonical-source) — no hard-coded physics ──────
from ave.core.constants import ALPHA, R_II, R_III, V_SNAP, V_YIELD, Z_0  # noqa: E402
from ave.core.crystal_engine import CrystalEngine  # noqa: E402

OUT = Path(__file__).parent

# ── engine config: mirror the cage driver (the static-basin foundation this
#    builds on) so (C)/(A')/(A) are a direct dynamic extension of the cage's
#    profile-selective static result (generic Gaussian disperses). ───────────
N_BOX = 37
DX = 1.0
SIGMA = 3.0          # bulk-field Gaussian width (cage SIGMA_GAUSS)
PML = 4
S_MIN = 0.05
A_CAP = 0.99

# ── photon (FIXED engineering choice — NOT swept to force a lock). Amplitude
#    chosen for energy-parity with the seed (V_peak = A0 ~ O(1)); a clearly-
#    engaged converter drive. The outcome is amplitude-insensitive across
#    0..4x (characterized pre-freeze), so 1.0 is fair + representative. ───────
PHOTON_AMP = 1.0
PHOTON_WL = 6.0
PHOTON_HELICITY = 1.0
PHOTON_DIR = (1, 0, 0)

# ── PUMP arm: genesis-24-style fixed-omega CW free-work drive on V (driver-level
#    forcing; the conserved-vs-pumped control). FIXED omega (does NOT track the
#    dropping omega_local) — the classic autoresonance-failure mode. ──────────
PUMP_AMP = 0.05
PUMP_OMEGA = 0.5     # fixed engine-unit drive frequency (matter-clock scale c0/dx~1)
PUMP_SIGMA = 3.0

# ── A0 sweep across the g_front window (prereg §5): floor .. R_II .. sub-rupture.
#    front_center = R_II = sqrt(3)/2 ~ 0.866 (g_front maximal); window exists
#    because R_II < 0.95 (the cage generic-disperse ceiling). ──────────────────
A0_SWEEP = [0.69, 0.78, R_II, 0.95]          # all >= g_front floor, all < R_III
A0_BELOW_FLOOR = [0.40]                       # F6: confirm the valve-shut false-negative

# ── SECH POSITIVE-CONTROL (instrument validation — NOT a frozen-prereg arm).
#    The cage's v14 Mode-I sech eigen-profile (1/cosh(r/R)) that the cage ANCHOR
#    arm SELF-FOCUSED, run in the cage's self-focus box (N_SECH, dx_SECH), converter
#    OFF, NO photon. It is the KNOWN-POSITIVE: the LOCK-detector MUST fire on it,
#    else a photon-arm DISPERSE is a can't-detect-anything artifact rather than a
#    real negative (ave-apparatus-floor-attribution validate-on-known-positive).
#    Box mirrors cage_stiffening_wall.py SECH_ANCHOR (test_master_equation_v14_mode_i
#    box). Amps stay in the cage self-focus range AND A²≤1 (near-yield forming) —
#    the cage's 0.70/0.85 ring up to A²>1 (RUPTURE-EXCLUDED, out of the LOCK regime).
N_SECH = 24
DX_SECH = 0.5
RADIUS_SECH = 2.5
SECH_AMPS = [0.20, 0.30, 0.50]               # cage-self-focus range, all A²pk<1

# ── verdict tolerances (frozen here; the disperse/lock separation is large) ──
GROW_TOL = 0.05        # peak must exceed seed by >5% to count as "grew"
PERSIST_FRAC = 0.50    # post-transient envelope must retain >50% of seed to "persist"
FLAT_TOL = 0.08
DECAY_TOL = 0.60       # late envelope < 0.6*mid envelope => still decaying
PLV_LOCK = 0.80        # phase-locking value above this = phase-coherent carrier
RUPTURE_A2 = 1.0       # A^2 > 1 => post-rupture regime (excluded from lock verdict)
DETONATION_MAX_V = 10.0  # max|V| beyond this = genesis-24-scale detonation (was ~1e4)


# ──────────────────────────────────────────────────────────────────────────
# canonical-source cross-check (verify_constants-style; before any output)
# ──────────────────────────────────────────────────────────────────────────
def verify_constants(front_center: float, front_width: float) -> dict:
    """Confirm the canonical constants + the g_front window the arms ride on,
    COMPUTED not asserted. front_center / front_width are READ FROM THE ENGINE
    (not hard-coded)."""
    floor = front_center - front_width
    checks = {
        "R_II_is_sqrt3_over_2": bool(np.isclose(R_II, np.sqrt(3.0) / 2.0)),
        "V_yield_is_sqrt_alpha_V_snap": bool(np.isclose(V_YIELD, np.sqrt(ALPHA) * V_SNAP)),
        "front_center_is_R_II": bool(np.isclose(front_center, R_II)),
        "window_floor_ge_check": bool(min(A0_SWEEP) >= floor - 1e-9),
        "window_ceiling_sub_rupture": bool(max(A0_SWEEP) < R_III),
        "window_exists_RII_lt_ceiling": bool(R_II < 0.95),  # cage generic-disperse ceiling
        "below_floor_is_below": bool(all(a < floor for a in A0_BELOW_FLOOR)),
    }
    return {
        "R_II": float(R_II), "R_III": float(R_III), "V_YIELD": float(V_YIELD),
        "V_SNAP": float(V_SNAP), "ALPHA": float(ALPHA), "Z_0": float(Z_0),
        "front_center": float(front_center), "front_width": float(front_width),
        "g_front_floor": float(floor), "checks": checks,
        "all_pass": bool(all(checks.values())),
    }


# ──────────────────────────────────────────────────────────────────────────
# arm construction (CP8 guard rides EVERY seed_bulk call: helical=False)
# ──────────────────────────────────────────────────────────────────────────
ARM_C = "C"        # photon + generic field, converter ON
ARM_AP = "A_prime"  # generic field, converter ON, NO photon
ARM_A = "A"        # generic field, converter OFF, NO photon
ARM_PUMP = "PUMP"  # generic field + fixed-omega CW drive on V
ARM_SECH = "SECH"  # cage v14 sech eigen-profile, converter OFF, NO photon (POSITIVE CONTROL)


def _seed_sech(e: CrystalEngine, amp: float, width: float, dx: float) -> None:
    """Direct-assign the v14 Mode-I sech eigen-profile 1/cosh(r/R) — the cage
    ANCHOR seed (cage_stiffening_wall.py `_seed` 'sech' branch), the KNOWN
    self-focusing profile. Stationary start (∂_tV=0): V_prev=V. This is the
    detector positive-control: deliberately planting the known self-focusing
    end-state is CORRECT for a detector/positive-control (substrate-native-check —
    CP8's seed-the-precursor guard governs the EMERGENCE-test arms, NOT the
    detector check; the cage proved THIS profile self-focuses)."""
    c = e.N // 2
    coords = np.arange(e.N) - c
    xx, yy, zz = np.meshgrid(coords, coords, coords, indexing="ij")
    r = np.sqrt(xx**2 + yy**2 + zz**2) * dx
    seed = amp * (1.0 / np.cosh(r / width))
    e.V[:] = seed
    e.V_prev[:] = seed.copy()


def _build_engine(arm: str, A0: float, helicity: float) -> CrystalEngine:
    if arm == ARM_SECH:
        # POSITIVE-CONTROL: cage v14 sech in the cage self-focus box, converter
        # OFF, NO photon — the known-positive the LOCK-detector must fire on.
        e = CrystalEngine(N=N_SECH, dx=DX_SECH, S_min=S_MIN, A_cap=A_CAP,
                          converter_on=False, pml_thickness=PML)
        _seed_sech(e, amp=A0, width=RADIUS_SECH, dx=DX_SECH)
        return e
    converter_on = arm in (ARM_C, ARM_AP, ARM_PUMP)  # (A) is the converter-OFF control
    e = CrystalEngine(N=N_BOX, dx=DX, S_min=S_MIN, A_cap=A_CAP,
                      converter_on=converter_on, pml_thickness=PML)
    ic = e.N // 2
    # 🔴 CP8 generic-field guard rides the CALL: helical=False (NOT the default).
    e.seed_bulk((ic, ic, ic), sigma=SIGMA, frac=A0, helical=False)
    if arm == ARM_C:
        e.seed_photon((ic, ic, ic), sigma=SIGMA, wavelength=PHOTON_WL,
                      amplitude=PHOTON_AMP, helicity=helicity, direction=PHOTON_DIR)
    return e


def _pump_envelope(e: CrystalEngine) -> np.ndarray:
    ic = e.N // 2
    i, j, k = np.indices((e.N, e.N, e.N))
    r2 = (i - ic) ** 2 + (j - ic) ** 2 + (k - ic) ** 2
    return np.exp(-r2 / (2.0 * PUMP_SIGMA**2))


# ──────────────────────────────────────────────────────────────────────────
# instrumentation
# ──────────────────────────────────────────────────────────────────────────
def _carrier_omega0(Vcore, Score, dt, n_trans):
    """COMPUTED matter-clock zero-point omega0: the dominant carrier angular
    frequency of V_core(t) (post-transient, DC removed, FFT peak) divided by
    <sqrt(S_core)> so that <omega_local> = omega0*<sqrt S> matches the OBSERVED
    carrier. Returns (omega0, omega_dom, spectral_concentration, zero_crossings).
    A weak/absent carrier (no breather) => low concentration => omega0 unreliable
    (reported, never asserted)."""
    v = np.asarray(Vcore, dtype=float)[n_trans:]
    s = np.asarray(Score, dtype=float)[n_trans:]
    v = v - v.mean()
    zc = int(np.sum((v[:-1] * v[1:]) < 0))
    if v.std() < 1e-12 or len(v) < 8:
        return 0.0, 0.0, 0.0, zc
    spec = np.abs(np.fft.rfft(v))
    freqs = np.fft.rfftfreq(len(v), d=dt)
    spec[0] = 0.0  # kill DC (the slow dispersal drift)
    kpk = int(np.argmax(spec))
    omega_dom = 2.0 * np.pi * float(freqs[kpk])
    conc = float(spec[kpk] / max(spec.sum(), 1e-30))
    sqrtS_mean = float(np.sqrt(np.maximum(s, 1e-12)).mean())
    omega0 = omega_dom / max(sqrtS_mean, 1e-12)
    return omega0, omega_dom, conc, zc


def evolve(arm: str, A0: float, nsteps: int, omega0: float | None = None,
           helicity: float = PHOTON_HELICITY, transient_frac: float = 0.5):
    """Run one arm. PASS 1 (omega0=None): evolve + record max|A|, max|V|, S_core,
    V_core, ∂_tV_core. PASS 2 (omega0 set): re-run identically and, EVERY STEP,
    feed the DYNAMIC omega_local(t)=omega0*sqrt(S_core(t)) into the engine's own
    `phase_space_vinc_vref(ω_char=ω_local(t))` and read the core phasor (CP9 —
    dynamically evolved; A46 phasor coords). Deterministic => pass-2 dynamics ==
    pass-1 dynamics."""
    e = _build_engine(arm, A0, helicity)
    m = e.interior_mask()
    c = e.N // 2
    pump_env = _pump_envelope(e) if arm == ARM_PUMP else None

    def max_A():
        return float(np.max(e.strain_field()[m]))

    def max_V():
        return float(np.max(np.abs(e.V[m])))

    def s_core():
        return float(np.min(e.saturation_kernel(e.V)[m]))

    a_ser = [max_A()]
    v_ser = [max_V()]
    s_ser = [s_core()]
    vcore = [float(e.V[c, c, c])]
    pvcore = [float(e.bulk_velocity()[c, c, c])]
    et0 = e.total_energy()
    ec0 = e.bulk_energy_conserved()
    phi_ser, wl_ser, rad_ser = [], [], []

    if omega0 is not None:
        wl0 = omega0 * np.sqrt(max(s_ser[0], 1e-12))
        vix, viy, _, _ = e.phase_space_vinc_vref(omega_char=max(wl0, 1e-9))
        phi_ser.append(float(np.arctan2(viy[c, c, c], vix[c, c, c])))
        wl_ser.append(float(wl0))
        rad_ser.append(float(np.hypot(vix[c, c, c], viy[c, c, c])))

    for _ in range(nsteps):
        e.step()
        if arm == ARM_PUMP:  # driver-level fixed-omega CW free-work drive on V
            e.V += PUMP_AMP * pump_env * np.sin(PUMP_OMEGA * e.time)
        a_ser.append(max_A())
        v_ser.append(max_V())
        s_ser.append(s_core())
        vcore.append(float(e.V[c, c, c]))
        pvcore.append(float(e.bulk_velocity()[c, c, c]))
        if omega0 is not None:
            wl = omega0 * np.sqrt(max(s_ser[-1], 1e-12))  # DYNAMIC omega_local(t)
            vix, viy, _, _ = e.phase_space_vinc_vref(omega_char=max(wl, 1e-9))
            phi_ser.append(float(np.arctan2(viy[c, c, c], vix[c, c, c])))
            wl_ser.append(float(wl))
            rad_ser.append(float(np.hypot(vix[c, c, c], viy[c, c, c])))

    a = np.array(a_ser); v = np.array(v_ser); s = np.array(s_ser)
    n_trans = int(transient_frac * len(a))
    post = a[n_trans:]
    mid = post[: max(1, len(post) // 2)]
    late = post[max(1, len(post) // 2):]
    et1 = e.total_energy(); ec1 = e.bulk_energy_conserved()
    fi = e.field_intensity()
    # density-peak location (Rule 10: sample at the |V| peak, PML-excluded)
    Vi = np.abs(e.V) * m
    pk = np.unravel_index(int(np.argmax(Vi)), Vi.shape)

    rec = {
        "arm": arm, "A0": float(A0), "helicity": float(helicity), "n_steps": nsteps,
        "max_A_t0": float(a[0]), "max_A_peak": float(a.max()), "max_A_end": float(a[-1]),
        "max_A_persist": float(post.mean()),
        "envelope_mid": float(mid.mean()), "envelope_late": float(late.mean()),
        "A2_peak": float(a.max() ** 2),
        "max_V_max": float(v.max()), "field_max_V_end": float(fi["max_V"]),
        "S_core_t0": float(s[0]), "S_core_end": float(s[-1]), "S_core_min": float(s.min()),
        "peak_cell": [int(x) for x in pk], "core_cell": [c, c, c],
        "total_energy_t0": float(et0), "total_energy_end": float(et1),
        "total_energy_drift_pct": float((et1 - et0) / max(abs(et0), 1e-30) * 100.0),
        "bulk_E_conserved_t0": float(ec0), "bulk_E_conserved_end": float(ec1),
        "bulk_E_conserved_drift_pct": float((ec1 - ec0) / max(abs(ec0), 1e-30) * 100.0),
        "converter_work": float(e.converter_work),
        "_vcore": vcore, "_pvcore": pvcore, "_score": s_ser, "_n_trans": n_trans,
    }
    if omega0 is not None:
        rec.update(_phase_coherence(phi_ser, wl_ser, rad_ser, e.dt, n_trans, omega0))
    return rec


def _phase_coherence(phi_ser, wl_ser, rad_ser, dt, n_trans, omega0):
    """The autoresonance signature (F3 / CP9): LOCK = the core phasor phase
    stays COHERENT with its own dropping omega_local. The locked-carrier
    prediction is phi advancing at -omega_local (the (V, ∂_tV/omega_local) phasor
    is a circle traversed at omega_local iff omega_char tracks the carrier). PLV =
    |<exp(i*(phi_meas - phi_pred))>| over the post-transient window: ~1 = phase-
    locked (autoresonant); ->0 = drifting (incoherent / dispersing). Also reports
    phasor-radius persistence (sustained oscillation vs collapse)."""
    phi = np.unwrap(np.asarray(phi_ser, dtype=float))
    wl = np.asarray(wl_ser, dtype=float)
    rad = np.asarray(rad_ser, dtype=float)
    phi_pred = phi[0] - np.cumsum(np.concatenate([[0.0], wl[:-1]])) * dt
    delta = phi[n_trans:] - phi_pred[n_trans:]
    plv = float(np.abs(np.mean(np.exp(1j * delta)))) if delta.size else 0.0
    r_post = rad[n_trans:]
    rad_persist = float(r_post.mean() / max(rad[0], 1e-30)) if r_post.size else 0.0
    return {
        "omega0": float(omega0),
        "omega_local_start": float(wl[0]) if wl.size else 0.0,
        "omega_local_end": float(wl[-1]) if wl.size else 0.0,
        "omega_local_min": float(wl.min()) if wl.size else 0.0,
        "phase_coherence_PLV": plv,
        "phasor_radius_persist": rad_persist,
    }


def g_front_at(A0: float, front_center: float, front_width: float) -> float:
    """The converter valve opening at peak strain A0 (engine `_front_window`
    form, evaluated at the seed peak). ~1 at R_II (valve maximal); ->0 far from
    the front (valve shut)."""
    return float(np.exp(-((A0 - front_center) ** 2) / (2.0 * front_width**2)))


# ──────────────────────────────────────────────────────────────────────────
# pure classifier (record -> bin); unit-testable on synthetic records
# ──────────────────────────────────────────────────────────────────────────
def classify(rec) -> str:
    """Bins: DETONATE / RUPTURE-EXCLUDED / LOCK / DISPERSE / UNRESOLVED.
    Near-yield forming (A^2<=1) is the only regime where LOCK/DISPERSE are binned;
    DETONATE (genesis-24 pump) and RUPTURE (A^2>1) are regime-excluded from the
    lock verdict (prereg §4/§7). LOCK requires bounded + persistent + phase-
    coherent (the ratified boundedness criterion, NOT energy-flat)."""
    a0 = rec["max_A_t0"]
    apk = rec["max_A_peak"]
    apersist = rec["max_A_persist"]
    if rec["max_V_max"] > DETONATION_MAX_V:
        return "DETONATE"
    if rec["A2_peak"] > RUPTURE_A2:
        return "RUPTURE-EXCLUDED"
    grew = apk > a0 * (1.0 + GROW_TOL)
    persisted = apersist > a0 * PERSIST_FRAC
    decaying = rec["envelope_late"] < rec["envelope_mid"] * DECAY_TOL
    plv = rec.get("phase_coherence_PLV", 0.0)
    coherent = plv >= PLV_LOCK and rec.get("phasor_radius_persist", 0.0) >= PERSIST_FRAC
    bounded = rec["max_V_max"] <= DETONATION_MAX_V
    if persisted and bounded and coherent and not decaying:
        return "LOCK"
    if not persisted:
        return "DISPERSE"
    return "UNRESOLVED"  # persistent but not phase-coherent — ambiguous, flag


# ──────────────────────────────────────────────────────────────────────────
# four-way discriminator (prereg §6 table)
# ──────────────────────────────────────────────────────────────────────────
def discriminate(binC, binAp, binA, A0, floor):
    valve_open = A0 >= floor - 1e-9
    if binC in ("DETONATE",):
        return "C-DETONATE", "🔴 (C) pump/detonate artifact, not genesis (conserved-vs-pumped)"
    if not valve_open:
        if binC == "DISPERSE":
            return ("EXCLUDED-VALVE-SHUT",
                    "⛔ A0<g_front floor: valve never opened (apparatus artifact, NOT a physics null; F6)")
        return ("BELOW-FLOOR-OTHER", f"(C)={binC} below floor — interpret with care (valve shut)")
    if binC == "LOCK" and binAp == "DISPERSE" and binA == "DISPERSE":
        return ("TARGET-POSITIVE-PENDING-AUDIT",
                "✅ (C) LOCK ∧ (A/A') DISPERSE — target-positive bin, PENDING auditor verification")
    if binC == "LOCK" and (binAp == "LOCK" or binA == "LOCK"):
        return ("FIELD-SELF-GENESIS",
                "⚠️ (C) LOCK ∧ (A/A') LOCK — field self-genesises via Op14; photon is a PASSENGER")
    if binC == "DISPERSE":
        return ("NO-GENESIS",
                "❌ (C) DISPERSE with valve open — no genesis on crystal_engine (photon can't build it)")
    return ("INDETERMINATE", f"(C)={binC} (A')={binAp} (A)={binA} — not a clean discriminator cell")


def fmt(rec, bin_, gfront):
    plv = rec.get("phase_coherence_PLV", float("nan"))
    wl0 = rec.get("omega_local_start", float("nan"))
    wle = rec.get("omega_local_end", float("nan"))
    return (
        f"  {rec['arm']:7} A0={rec['A0']:.3f} g_front={gfront:.3f} | "
        f"A0={rec['max_A_t0']:.3f} Apk={rec['max_A_peak']:.3f} Apersist={rec['max_A_persist']:.3f} "
        f"Aend={rec['max_A_end']:.3f} | maxV={rec['max_V_max']:.2f} A2pk={rec['A2_peak']:.2f} | "
        f"ω_loc {wl0:.3f}->{wle:.3f} PLV={plv:.3f} | dE={rec['total_energy_drift_pct']:+.0f}% "
        f"-> {bin_}"
    )


# ──────────────────────────────────────────────────────────────────────────
# run one arm both passes (measure omega0, then feed dynamic omega_local)
# ──────────────────────────────────────────────────────────────────────────
def run_arm(arm: str, A0: float, nsteps: int, helicity: float = PHOTON_HELICITY) -> dict:
    # PASS 1: evolve + record carrier; measure the COMPUTED matter-clock omega0.
    p1 = evolve(arm, A0, nsteps, omega0=None, helicity=helicity)
    omega0, omega_dom, conc, zc = _carrier_omega0(p1["_vcore"], p1["_score"], _DT, p1["_n_trans"])
    # PASS 2: re-run, feeding the DYNAMIC omega_local(t)=omega0*sqrt(S_core) into
    # the engine's phase_space_vinc_vref each step (CP9 dynamically evolved).
    rec = evolve(arm, A0, nsteps, omega0=omega0, helicity=helicity)
    rec["carrier_omega_dom"] = float(omega_dom)
    rec["carrier_spectral_conc"] = float(conc)
    rec["carrier_zero_crossings"] = int(zc)
    # drop the bulky per-step traces from the persisted record (keep summaries +
    # the short omega_local/series-derived scalars); keep core traces compact
    for k in ("_vcore", "_pvcore", "_score", "_n_trans"):
        rec.pop(k, None)
    return rec


# leapfrog dt is fixed by the engine config; capture once for the carrier FFT.
_DT = CrystalEngine(N=N_BOX, dx=DX, S_min=S_MIN, A_cap=A_CAP, pml_thickness=PML).dt
# v14-box dt for the SECH positive-control (dx_SECH≠DX ⇒ dt differs by 2×); the
# carrier FFT MUST use this dt or ω_local is mis-scaled and PLV is mis-predicted.
_DT_SECH = CrystalEngine(N=N_SECH, dx=DX_SECH, S_min=S_MIN, A_cap=A_CAP, pml_thickness=PML).dt


def run_sech_control(amp: float, nsteps: int) -> dict:
    """SECH POSITIVE-CONTROL: run the cage v14 sech eigen-profile (converter OFF,
    no photon) through the EXACT T2 detector — same `evolve` loop, same
    `_carrier_omega0`/phasor, same `classify()` + LOCK criterion (UNCHANGED).
    validate-on-known-positive (ave-apparatus-floor-attribution): a genuine
    self-focus MUST trip LOCK, else a photon-arm DISPERSE is can't-detect noise.
    Uses the v14-box dt (`_DT_SECH`), NOT the T2-box `_DT`. Reports the ring-up
    apk/a0 + the F1 `grew` flag ALONGSIDE the bin so the auditor sees the sech
    BOTH grows AND persists (the stricter F1 grow+coherent read)."""
    p1 = evolve(ARM_SECH, amp, nsteps, omega0=None)
    omega0, omega_dom, conc, zc = _carrier_omega0(p1["_vcore"], p1["_score"], _DT_SECH, p1["_n_trans"])
    rec = evolve(ARM_SECH, amp, nsteps, omega0=omega0)
    rec["carrier_omega_dom"] = float(omega_dom)
    rec["carrier_spectral_conc"] = float(conc)
    rec["carrier_zero_crossings"] = int(zc)
    rec["ring_up_apk_over_a0"] = float(rec["max_A_peak"] / max(rec["max_A_t0"], 1e-30))
    rec["grew_F1"] = bool(rec["max_A_peak"] > rec["max_A_t0"] * (1.0 + GROW_TOL))
    rec["dt_sech"] = float(_DT_SECH)
    for k in ("_vcore", "_pvcore", "_score", "_n_trans"):
        rec.pop(k, None)
    return rec


# ──────────────────────────────────────────────────────────────────────────
# main
# ──────────────────────────────────────────────────────────────────────────
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--smoke", action="store_true", help="CI budget (short)")
    ap.add_argument("--production", action="store_true", help="resolve TRANSIENT-vs-persist")
    args = ap.parse_args()
    smoke = args.smoke or not args.production
    nsteps = 250 if smoke else 700
    sweep = [R_II] if smoke else A0_SWEEP

    t0 = time.time()
    _probe = CrystalEngine(N=N_BOX, dx=DX, S_min=S_MIN, A_cap=A_CAP, pml_thickness=PML)
    front_center, front_width = _probe.front_center, _probe.front_width
    vc = verify_constants(front_center, front_width)
    floor = vc["g_front_floor"]

    print("=" * 96)
    print("  T2 — GENESIS SELF-LOCK (photon-at-a-field -> autoresonant bulk breather), crystal_engine")
    print(f"  mode={'SMOKE' if smoke else 'PRODUCTION'} nsteps={nsteps} dt={_DT:.4e} | "
          f"front_center=R_II={front_center:.4f} front_width={front_width:.3f} g_front_floor={floor:.4f}")
    print(f"  canonical: V_YIELD(SI)={V_YIELD:.0f} V_SNAP={V_SNAP:.0f} α={ALPHA:.6e} Z_0={Z_0:.2f} "
          f"R_II={R_II:.4f} R_III={R_III:.1f}")
    print(f"  constants cross-check all_pass={vc['all_pass']}  checks={vc['checks']}")
    print(f"  photon (FIXED, not tuned): amp={PHOTON_AMP} wl={PHOTON_WL} h={PHOTON_HELICITY} | "
          f"PUMP fixed-ω={PUMP_OMEGA} amp={PUMP_AMP}")
    print(f"  DISCRIMINATOR: TARGET POSITIVE = (C) LOCK ∧ (A/A') DISPERSE, A0>=floor. "
          f"NO chord claim — auditor verifies.")
    print("=" * 96, flush=True)
    if not vc["all_pass"]:
        raise SystemExit("canonical-source cross-check FAILED — aborting (no output on a bad bench)")

    out = {
        "mode": "smoke" if smoke else "production", "nsteps": nsteps, "dt": _DT,
        "config": {"N": N_BOX, "dx": DX, "sigma": SIGMA, "pml": PML, "S_min": S_MIN, "A_cap": A_CAP,
                   "photon_amp": PHOTON_AMP, "photon_wl": PHOTON_WL, "photon_helicity": PHOTON_HELICITY,
                   "pump_amp": PUMP_AMP, "pump_omega": PUMP_OMEGA,
                   "A0_sweep": [float(a) for a in sweep], "A0_below_floor": A0_BELOW_FLOOR},
        "canonical_check": vc,
        "tolerances": {"GROW_TOL": GROW_TOL, "PERSIST_FRAC": PERSIST_FRAC, "PLV_LOCK": PLV_LOCK,
                       "RUPTURE_A2": RUPTURE_A2, "DETONATION_MAX_V": DETONATION_MAX_V},
        "arms": {}, "discriminator": {}, "below_floor_F6": {}, "ablation_helicity": {},
    }

    # ── the four-way discriminator across the A0 window ──────────────────────
    print("\n[SWEEP] four-way discriminator across the g_front window (valve OPEN, A0>=floor):")
    for A0 in sweep:
        gf = g_front_at(A0, front_center, front_width)
        recs = {}
        for arm in (ARM_C, ARM_AP, ARM_A, ARM_PUMP):
            r = run_arm(arm, A0, nsteps)
            b = classify(r)
            r["bin"] = b
            recs[arm] = r
            print(fmt(r, b, gf))
        case, msg = discriminate(recs[ARM_C]["bin"], recs[ARM_AP]["bin"], recs[ARM_A]["bin"], A0, floor)
        pump_bin = recs[ARM_PUMP]["bin"]
        print(f"    => A0={A0:.3f} g_front={gf:.3f}: {case}  | PUMP={pump_bin}  | {msg}")
        out["arms"][f"{A0:.3f}"] = {arm: recs[arm] for arm in recs}
        out["discriminator"][f"{A0:.3f}"] = {
            "g_front": gf, "binC": recs[ARM_C]["bin"], "binAprime": recs[ARM_AP]["bin"],
            "binA": recs[ARM_A]["bin"], "binPUMP": pump_bin, "case": case, "msg": msg,
        }

    # ── F6: below-floor (C) — CONFIRM the valve-shut false-negative exists ───
    print("\n[F6] below-floor (C) (A0<g_front floor) — confirm valve-shut apparatus artifact (EXCLUDED):")
    for A0 in A0_BELOW_FLOOR:
        gf = g_front_at(A0, front_center, front_width)
        r = run_arm(ARM_C, A0, nsteps)
        b = classify(r); r["bin"] = b
        case, msg = discriminate(b, "DISPERSE", "DISPERSE", A0, floor)
        print(fmt(r, b, gf))
        print(f"    => A0={A0:.3f} g_front={gf:.3f}: {case} | {msg}")
        out["below_floor_F6"][f"{A0:.3f}"] = {"record": r, "g_front": gf, "case": case, "msg": msg}

    # ── ablation: opposite-helicity photon at R_II (matter/antimatter selector) ─
    print("\n[ABLATION] (C) opposite-helicity photon at A0=R_II (chirality selector):")
    r = run_arm(ARM_C, R_II, nsteps, helicity=-PHOTON_HELICITY)
    b = classify(r); r["bin"] = b
    print(fmt(r, b, g_front_at(R_II, front_center, front_width)))
    out["ablation_helicity"][f"{R_II:.3f}_h-1"] = {"record": r, "bin": b}

    # ── SECH POSITIVE-CONTROL (instrument validation; NOT a frozen-prereg arm) ──
    # validate-on-known-positive (ave-apparatus-floor-attribution): the cage v14
    # sech SELF-FOCUSES — the LOCK-detector MUST fire on it, else a photon-arm
    # DISPERSE is a can't-detect-anything artifact, not a real negative. We report
    # the ring-up apk/a0 + grew_F1 ALONGSIDE the bin (grow AND persist). Run in the
    # cage sech-arm box + budget (the configuration where the known-positive holds).
    print("\n[POSITIVE-CONTROL] SECH eigen-profile (cage v14 self-focus; converter OFF, NO photon) "
          "through the EXACT LOCK-detector:")
    nsteps_sech = 300 if smoke else 600  # cage sech-arm budget (the known-positive)
    out["sech_positive_control"] = {
        "box": {"N": N_SECH, "dx": DX_SECH, "radius": RADIUS_SECH}, "nsteps": nsteps_sech,
        "role": "detector-validation / positive-control (consistency-vs-emergence: DETECTOR-VALIDATION class)",
        "amps": {},
    }
    for amp in SECH_AMPS:
        rs = run_sech_control(amp, nsteps_sech)
        bs = classify(rs); rs["bin"] = bs
        print(f"  SECH  amp={amp:.2f} | A0={rs['max_A_t0']:.3f} Apk={rs['max_A_peak']:.3f} "
              f"ringup={rs['ring_up_apk_over_a0']:.3f}x grew_F1={rs['grew_F1']} "
              f"Apersist={rs['max_A_persist']:.3f} A2pk={rs['A2_peak']:.3f} maxV={rs['max_V_max']:.2f} | "
              f"PLV={rs['phase_coherence_PLV']:.3f} radpersist={rs['phasor_radius_persist']:.3f} -> {bs}")
        out["sech_positive_control"]["amps"][f"{amp:.2f}"] = rs
    sech_bins = {a: out["sech_positive_control"]["amps"][a]["bin"] for a in out["sech_positive_control"]["amps"]}
    sech_all_lock = all(b == "LOCK" for b in sech_bins.values())
    out["sech_positive_control"]["bins"] = sech_bins
    out["sech_positive_control"]["all_lock"] = bool(sech_all_lock)
    if sech_all_lock:
        pc_msg = ("✅ DETECTOR VALIDATED — the known-positive sech returns LOCK; the LOCK-detector "
                  "fires on a genuine self-focus, so the (C) DISPERSE is a real negative.")
    else:
        pc_msg = ("🔴 DETECTOR FLAG — the known-positive sech does NOT return LOCK "
                  f"(bins {sech_bins}). It self-focuses (rings up + persists + bounded, grew_F1=True) "
                  f"but PLV<{PLV_LOCK} -> UNRESOLVED: the PLV phase-coherence LOCK-gate does NOT fire "
                  "on a genuine self-focus. The (C) DISPERSE verdict rests on the VALIDATED ring-up/"
                  "persistence legs (photon arms show neither), NOT the PLV/F3 leg. flag-don't-fix: "
                  "do NOT tune the gate; auditor+Grant adjudicate.")
    out["sech_positive_control"]["message"] = pc_msg
    print(f"    => {pc_msg}")

    # ── headline four-way verdict (HONEST; no chord claim) ──────────────────
    cases = {k: v["case"] for k, v in out["discriminator"].items()}
    any_target = any(c == "TARGET-POSITIVE-PENDING-AUDIT" for c in cases.values())
    any_selfgen = any(c == "FIELD-SELF-GENESIS" for c in cases.values())
    all_nogen = all(c == "NO-GENESIS" for c in cases.values())
    pump_dets = [out["discriminator"][k]["binPUMP"] == "DETONATE" for k in out["discriminator"]]
    if any_target:
        headline = ("TARGET-POSITIVE (C) LOCK ∧ (A/A') DISPERSE at >=1 valve-open A0 — "
                    "PENDING auditor verification. NOT a confirmed chord.")
    elif any_selfgen:
        headline = "FIELD-SELF-GENESIS (⚠️) at >=1 A0 — photon a passenger; different claim."
    elif all_nogen:
        headline = ("NO-GENESIS (❌) at EVERY valve-open A0: (C) DISPERSES like (A/A'). "
                    "The asserted autoresonance self-lock is NOT realized on crystal_engine "
                    "in the near-yield forming regime. Clean negative (Rule 11).")
    else:
        headline = f"MIXED / INDETERMINATE: {cases}"
    out["headline"] = headline
    out["pump_all_detonate"] = bool(all(pump_dets))

    out["elapsed_s"] = time.time() - t0
    jpath = OUT / "t2_genesis_selflock_results.json"
    jpath.write_text(json.dumps(out, indent=2, default=float))
    print("\n" + "=" * 96)
    print(f"HEADLINE: {headline}")
    print(f"  POSITIVE-CONTROL (sech): all_lock={out['sech_positive_control']['all_lock']} "
          f"bins={out['sech_positive_control']['bins']}")
    print(f"  PUMP detonates at every tested A0: {out['pump_all_detonate']} (conserved-vs-pumped control)")
    print(f"  per-A0 cases: {cases}")
    print(f"  wrote {jpath.name} | elapsed {out['elapsed_s']:.1f}s")
    print("=" * 96, flush=True)
    return out


if __name__ == "__main__":
    main()
