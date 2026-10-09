"""R2 primary run configuration — charged-seed K4 trade (b).

Grant decision T-A4b (2026-10-08 22:01 PT):
  k_refl = 0, r_c = 24, k_op10 = 1.415e6, γ = 4320, dt = 2.24e-4, 288³ periodic.

Source documents (SHA-1 from ~/AVE-staging/runs/csk4/inputs/SHA1SUMS):
  Brief           2026-10-08-charged-seed-K4-BRIEF.md          0de2f577279f
  Spec (A6)       2026-10-08-charged-seed-K4-change-SPEC_CANDIDATE.md  a4ae89f69f2e
  Setup sheet     2026-10-08-charged-seed-SETUP-SHEET_CANDIDATE.md     cd5bb927d128
  Gate ladder v5  LADDER-charged-seed-K4-2026-10-08.md                 1ae8604b19c6

NOT RUN without Grant's GO.  Runs needing GO:
  R2 primary:  288³, dt=2.24e-4, 144 643 steps  (3.44e12 point-steps)
  #16 partner: 192³, same dt/steps               (1.02e12 point-steps)
  dt/2 rung:   192³, dt/2, 289 286 steps         (2.04e12 point-steps)
  C0-cold:     192³, same dt/steps               (1.02e12 point-steps)

Pinned-value provenance (ladder §2):
  dt = 2.24e-4   The guard 2.2446e-4 from max|∂n|²=0.20736 on the alive
                 stencil at r_c=24; 0.25/Ω_max≤2.745e-4; pin 2.24e-4
                 (2.25e-4 is 0.2% above guard — see ladder §2 "dt HOLDS").
  steps = 144 643  32.4 time-units / 2.24e-4 dt (9.5 breathing periods (T_b 3.40),
                  period ∝ R, measured at r_c≈12 → 1.62 tu → scaled).
  k_op10 = 1.415e6  Gate engine-stencil 3-pt at r_c=24: k*=1.41487e6,
                  s=0.99991, d²E/dλ²=+4.76e7 (true minimum).  Math smooth
                  fit 1.415e6 (fit24_b).  Trade (b): k_refl=0 → no reflection
                  term; k_op10 set by γ/op10 balance alone.
  γ = 4320  = 30·G_c·r_c²|_{r_c=24} = 30·1·576 (ensures mass term ≤10% of
             γ-term push at R=r_c; r_c=24 per T-A4b trade).
  k_refl = 0  Trade (b); reflection off for a clean pin (Rule-10 row 3,
             ladder §7: cf:497–500 / cf:1038).

Rule-10 flag (ladder §7, spec §6):
  Row 1  cf:1290–1292  ω "has SO(3) period 2π by construction" — retracted
                       for quaternion storage; K-R5.
  Row 3  cf:1038       k_refl hard-coded 1.0; now a constructor kwarg.
  Row 4  cf:493–494    eps_reg "not a fit parameter"; its value sets k_refl=1
                       reflection energy when not turned off.
"""

import hashlib
import json
import math
import os

import numpy as np

# ---------------------------------------------------------------------------
# D1: charge_counters_pin.json path (Gate C1)
# ---------------------------------------------------------------------------

_PIN_FILE = os.path.normpath(os.path.join(
    os.path.dirname(__file__), '..', '..', 'ave', 'topological',
    'charge_counters_pin.json',
))


def _check_charge_counters_pin() -> None:
    """Load charge_counters_pin.json and verify blob sha1 of charge_counters.py.

    Raises RuntimeError if the file has been modified since the Gate
    CONDITIONAL PASS at d2c7da09 (blob b0384af0ca7e…). Called from
    make_r2_solver() so the R2 run cannot proceed with a mutated file.
    """
    with open(_PIN_FILE) as fpin:
        pin = json.load(fpin)
    cc_path = os.path.normpath(os.path.join(
        os.path.dirname(__file__), '..', '..', 'ave', 'topological',
        'charge_counters.py',
    ))
    with open(cc_path, 'rb') as f:
        data = f.read()
    header = b"blob %d\0" % len(data)
    actual = hashlib.sha1(header + data).hexdigest()
    expected = pin['blob_sha1']
    if actual != expected:
        raise RuntimeError(
            f"charge_counters.py has been modified since the Gate pin "
            f"(expected blob_sha1={expected}, got {actual}). "
            "Update charge_counters_pin.json and re-run the Gate audit "
            "before running the R2 simulation.")


# ---------------------------------------------------------------------------
# Pinned parameters — do NOT edit without updating the ladder document.
# ---------------------------------------------------------------------------

GAMMA = 4320.0
G = 1.0
G_C = 1.0
RHO = 1.0
I_OMEGA = 1.0
K_OP10 = 1.415e6
K_REFL = 0.0            # trade (b): reflection off
K_HOPF = math.pi / 3.0  # engine default cf:1311
ROTATION_STORAGE = "quaternion"

DT = 2.24e-4            # pinned (guard 2.2446e-4; 0.25/Ω_max ≤ 2.745e-4)
N_STEPS = 144_643       # 32.4 tu / DT  (9.5 breathing periods (T_b 3.40))

# Seed parameters
SEED_P = 2              # torus-knot exponent p
SEED_QQ = 3             # torus-knot exponent q (named qq to avoid shadowing)
SEED_RC = 24            # core radius in cells

# Primary box
NX_PRIMARY = NY_PRIMARY = NZ_PRIMARY = 288   # periodic, PML=0
PML_WIDTH = 0
DAMPING = 0.0

# #16 partner box
NX_PARTNER = NY_PARTNER = NZ_PARTNER = 192

# R2-PF pre-flight box (192³, T=0.25 tu; config only — run needs GO)
NX_PF = NY_PF = NZ_PF = 192
T_PF = 0.25  # time units

# ---------------------------------------------------------------------------
# v7 constants (ladder bdb5c32b8e87)
# ---------------------------------------------------------------------------

# Breathing period and run length
T_B = 3.40           # breathing period (tu) at r_c=12
N_FULL_PERIODS = 9   # 32.4 tu / T_b=3.40 → 9.5 periods → 9 full

# r_eq(0) pins (±0.005 for hedgehogs, ±0.05 for R2); formula: (3·4·n_neg/4π)^{1/3}
R_EQ0_HH48 = 6.016   # hedgehog(48,6): 228 sites with q0<0
R_EQ0_PII = 11.983   # _hedgehog_at(128,12,(0,0,0),L=48): 1802 sites
R_EQ0_R2 = 38.92     # rational(288,24) L=144 (A8 §8.1)

# R2 band and size-collapse threshold
R14_BAND = (27.2, 54.5)    # #14 band: 0.7–1.4 × R_EQ0_R2
R2C_SIZE_RATIO = 0.54      # period_collapse size arm threshold (unchanged)

# First-bond classification: BREAKUP if r_eq(t_first)/r_eq0 ≥ 0.85, else INFALL
FIRST_BOND_BREAKUP_RATIO = 0.85

# Seed cutoffs (tanh profile parameter L = n_c × r_c)
SEED_L_PRIMARY = 144  # R2: rational(288,24), 6 r_c = 144
SEED_L_PII = 48       # P-ii: _hedgehog_at(128,12,...,L=48), 4 r_c
SEED_L_PF = 96        # R2-PF: _hedgehog_at(192,24,...,L=96), 4 r_c (OPEN §6.3)

# Control k_op10 values. Formula: k = 8·γ/max|Δn|², with γ=4320.
# max|Δn|²=0.6183 (rc=12), max|Δn|²=0.88 (R2, rc=24).
K_OP10_PII = 8.88e5    # P-ii: 8·4320/0.6183 ≈ 8.88e5 (rc=12)
K_OP10_PII_C = 5.59e4  # P-ii-C: Λ=8 control k at rc=12
K_OP10_PF_C = 3.93e4   # R2-PF-C: Λ=8 control k at rc=24


def assert_r2_config(cf) -> None:
    """Read-back assert: verify all pinned R2 values on a constructed solver.

    Call with any CosseratField3D returned by make_r2_solver() — the grid can
    be tiny (do NOT allocate 288³ in tests).  Raises AssertionError on mismatch.
    """
    assert cf.gamma == GAMMA,       f"gamma mismatch: {cf.gamma!r} != {GAMMA!r}"
    assert cf.G == G,               f"G mismatch: {cf.G!r} != {G!r}"
    assert cf.G_c == G_C,           f"G_c mismatch: {cf.G_c!r} != {G_C!r}"
    assert cf.k_op10 == K_OP10,     f"k_op10 mismatch: {cf.k_op10!r} != {K_OP10!r}"
    assert cf.k_refl == K_REFL,     f"k_refl mismatch: {cf.k_refl!r} != {K_REFL!r}"
    assert abs(cf.k_hopf - K_HOPF) < 1e-14, (
        f"k_hopf mismatch: {cf.k_hopf!r} != {K_HOPF!r}")
    assert cf.rotation_storage == ROTATION_STORAGE, (
        f"rotation_storage mismatch: {cf.rotation_storage!r} != {ROTATION_STORAGE!r}")


def make_r2_solver(nx=None, ny=None, nz=None, _skip_pin_check=False):
    """Construct a CosseratField3D with R2 pinned parameters.

    Verifies charge_counters_pin.json before construction (Gate C1 D1).
    Pass _skip_pin_check=True ONLY in pin-mismatch test to exercise refusal.

    Note: gamma, G, G_c, k_op10 are post-construction attributes (the
    constructor only accepts k_refl and rotation_storage for physics knobs).
    Pass nx/ny/nz to override the default 288³ (e.g. a tiny test grid).

    Keyword-only nit (v5): k_refl / rotation_storage are passed BY NAME here and
    everywhere in the test suite. cf.py's constructor signature is NOT changed to
    make them keyword-only (that would be a net line edit to cosserat_field_3d.py,
    breaking the inbound cite-shift pin); by-name passing is the enforced
    convention instead.
    """
    if not _skip_pin_check:
        _check_charge_counters_pin()
    from ave.topological.cosserat_field_3d import CosseratField3D
    nx = nx or NX_PRIMARY
    ny = ny or NY_PRIMARY
    nz = nz or NZ_PRIMARY
    cf = CosseratField3D(
        nx, ny, nz,
        k_refl=K_REFL,
        rotation_storage=ROTATION_STORAGE,
    )
    cf.gamma = GAMMA
    cf.G = G
    cf.G_c = G_C
    cf.k_op10 = K_OP10
    assert_r2_config(cf)
    return cf


def make_r2_pf_config(control: bool = False) -> dict:
    """R2-PF 192³ pre-flight config (config only; run needs GO).

    control=True: uses Λ-8 k_op10 (K_OP10_PF_C=3.93e4) instead of the primary k_op10.
    Returns parameter dict with grid, seed, γ, k_op10, k_refl, dt, T, n_steps,
    and checkpoint times from pf_checkpoint_times(T_PF).
    """
    k = K_OP10_PF_C if control else K_OP10
    n_steps_pf = math.ceil(T_PF / DT)
    return {
        "nx": NX_PF, "ny": NY_PF, "nz": NZ_PF,
        "dt": DT, "n_steps": n_steps_pf, "t_end": T_PF,
        "gamma": GAMMA, "G": G, "G_c": G_C, "k_op10": k,
        "k_refl": K_REFL, "rotation_storage": ROTATION_STORAGE,
        "seed": {"constructor": "_hedgehog_at", "rc": SEED_RC, "L": SEED_L_PF},
        "checkpoints": pf_checkpoint_times(T_PF),
    }


def make_pii_config(control: bool = False) -> dict:
    """P-ii 128³ pre-flight config (config only; run needs Grant GO, STOPPED).

    control=True: uses Λ-8 k_op10 (K_OP10_PII_C=5.59e4) instead of K_OP10_PII.
    Returns parameter dict with grid, seed, γ, k_op10, k_refl, dt, T, n_steps,
    and checkpoint times from pf_checkpoint_times(0.25).

    P-ii spec: 128³, rc=12, _hedgehog_at(128,12,(0,0,0),L=48), γ=4320,
               k_op10=8.88e5, k_refl=0, dt=1.65e-4, T=0.25 (1,516 steps).
    """
    _DT_PII = 1.65e-4
    _T_PII = 0.25
    k = K_OP10_PII_C if control else K_OP10_PII
    n_steps = math.ceil(_T_PII / _DT_PII)
    return {
        "nx": 128, "ny": 128, "nz": 128,
        "dt": _DT_PII, "n_steps": n_steps, "t_end": _T_PII,
        "gamma": GAMMA, "G": G, "G_c": G_C, "k_op10": k,
        "k_refl": K_REFL, "rotation_storage": ROTATION_STORAGE,
        "seed": {"constructor": "_hedgehog_at", "rc": 12, "L": SEED_L_PII},
        "checkpoints": pf_checkpoint_times(_T_PII),
    }


def r_eq_from_q(q: np.ndarray, mask_alive: np.ndarray) -> float:
    """Equivalent radius of the q0<0 core (BCC density ¼, dx=1).

    V = 4 · #{alive sites with q[...,0] < 0}  (BCC alive density ¼ → V = 4·n_neg·dx³, dx=1)
    r_eq = (3V/4π)^{1/3}

    Pins (±0.005 hedgehogs, ±0.05 R2):
      hedgehog(48,6)                          n_neg=228  r_eq(0)=6.016
      _hedgehog_at(128,12,(0,0,0),L=48)       n_neg=1802 r_eq(0)=11.983
      rational(288,24) L=144 (R2, A8 §8.1)   —          r_eq(0)=38.92
    """
    n_neg = int(np.sum(q[mask_alive, 0] < 0))
    return float((3.0 * 4.0 * n_neg / (4.0 * np.pi)) ** (1.0 / 3.0))


def period_collapse(q: np.ndarray, mask_alive: np.ndarray,
                    r_eq0: float) -> bool:
    """R2-C collapse criterion: Re≤0 on any alive bond OR r_eq/r_eq0 < 0.54.

    Used by the R2 harness (shared with R1-2e via r_eq_from_q).  Returns True
    if the current field state counts as a collapse event.

    Args:
        q: quaternion field (n,n,n,4)
        mask_alive: bool mask of alive BCC sites
        r_eq0: initial equivalent radius from r_eq_from_q at t=0

    Mutant anchor: replacing `< 0.54` with `< 0` disables the size-ratio arm.
    """
    from ave.topological.k4_quaternion import collapse_check
    if collapse_check(q, mask_alive)["collapse"]:
        return True
    if r_eq0 > 0.0:
        if r_eq_from_q(q, mask_alive) / r_eq0 < 0.54:
            return True
    return False


def classify_checkpoint(q: np.ndarray, mask_alive: np.ndarray,
                        collapse_flagged: bool) -> dict:
    """Classify a K4 checkpoint as RESOLVED(N), UNRESOLVED, or COLLAPSE.

    Consults C-exact first; C-link is NEVER a fallback (M2 guard).
    COLLAPSE wins whenever collapse_flagged is True.

    M2 mutant anchor: inside the `if not c_exact_resolved:` block, replace
    `return {"outcome": "UNRESOLVED", "value": None}` with a c_link lookup.
    R1-2e assertion (b) kills it — post-collapse COLLAPSE checkpoints must
    never become RESOLVED via a C-link fallback.
    """
    if collapse_flagged:
        return {"outcome": "COLLAPSE", "value": None}
    from ave.topological.k4_quaternion import count_charge_k4
    r = count_charge_k4(q, mask_alive)
    c_exact = r.get("c_exact_result")
    c_exact_resolved = c_exact is not None and bool(c_exact.get("resolved"))
    if not c_exact_resolved:
        # M2 anchor: do NOT fall back to c_link here
        return {"outcome": "UNRESOLVED", "value": None}
    if r["resolved"]:
        return {"outcome": f"RESOLVED({r['value']})", "value": r["value"]}
    return {"outcome": "UNRESOLVED", "value": None}


def get_charge_verdict(q, mask_alive):
    """R2 charge verdict using the count_charge_k4 adapter (Gate §11, D2).

    Single call site for all integer-charge verdicts in the R2 harness.
    Returns the count_charge_k4 result dict (resolved, value, reason, ...).
    """
    from ave.topological.k4_quaternion import count_charge_k4
    return count_charge_k4(q, mask_alive)


def make_r2_seed(nx=NX_PRIMARY, ny=NY_PRIMARY, nz=NZ_PRIMARY, rc=SEED_RC):
    """Return the axial (2,3) KTL seed quaternion array for the given grid."""
    from ave.topological.charge_counters import rational
    return rational(nx, rc, p=SEED_P, qq=SEED_QQ)


def run_r2():  # pragma: no cover
    """R2 primary run — NOT called without Grant's GO.

    Usage (after GO):
        PYTHONPATH=src python src/scripts/vol_4_engineering/csk4_r2_config.py \
            ~/AVE-runs/csk4-r2-<date>
    """
    import sys
    import time

    outdir = sys.argv[1] if len(sys.argv) > 1 else None
    if outdir is None:
        raise SystemExit("Usage: csk4_r2_config.py <outdir>  (needs Grant GO first)")
    if not os.environ.get("AVE_R2_GO"):
        raise RuntimeError(
            "Set AVE_R2_GO=1 to confirm Grant GO before running the 288³ R2 simulation."
        )
    os.makedirs(outdir, exist_ok=True)

    print(f"R2 primary: 288³ periodic, dt={DT}, {N_STEPS} steps, k_refl={K_REFL}")
    print(f"  γ={GAMMA}, k_op10={K_OP10}, rotation_storage={ROTATION_STORAGE!r}")
    print(f"  Seed: axial ({SEED_P},{SEED_QQ}) r_c={SEED_RC}")
    print(f"  Output: {outdir}")

    cf = make_r2_solver()

    # R2-1 read-backs (ladder §5): the running dt, strain form, and #16 partner
    # box must match the pinned trade before the 3.4e12 point-step run proceeds.
    assert DT == 2.24e-4, f"R2-1 dt read-back: {DT!r} != 2.24e-4"
    assert cf.rotation_storage == "quaternion", (
        f"R2-1 strain-form read-back: rotation_storage={cf.rotation_storage!r} "
        "(K4 finite-rotation strain ε=Rᵀ(q)F−I required)")
    assert NX_PARTNER != NX_PRIMARY, (
        f"R2-1 partner read-back: #16 partner box {NX_PARTNER}³ must differ from "
        f"primary {NX_PRIMARY}³")

    seed = make_r2_seed()
    cf.q = seed.copy()
    cf.q[~cf.mask_alive] = np.array([1.0, 0.0, 0.0, 0.0])

    t0 = time.time()
    for step in range(N_STEPS):
        cf.step(DT)
        if step % 10000 == 0:
            print(f"  step {step}/{N_STEPS}  t={step*DT:.4f}  "
                  f"elapsed={time.time()-t0:.1f}s")
    print(f"Done. Total elapsed: {time.time()-t0:.1f}s")


# ---------------------------------------------------------------------------
# B9: R2 breathing-period aggregator (ladder §5 R2 #7)
# ---------------------------------------------------------------------------


def aggregate_r2_periods(period_results, expected_periods=N_FULL_PERIODS,
                         r14_trip_period=None):
    """Aggregate per-period count_charge_k4 results for the R2 breathing check.

    F4 (v5): consumes count_charge_k4 RESULT DICTS directly. Non-adapter dicts
    (those without 'resolved' key) raise TypeError — no legacy path.

    R2-C (v7): if any period has collapse=True, the run verdict is "COLLAPSE"
    (never PASS, never a count FAIL). Exception: if r14_trip_period is not None
    and occurs before the first COLLAPSE period, the verdict is "FAIL(#14)".

    Verdict logic (non-COLLAPSE runs, applied to all expected_periods):
      - A RESOLVED value ≠ +6 → FAIL.
      - PASS iff 10·n_resolved ≥ 9·expected_periods (integer arithmetic).
        9/9 → PASS; 8/9 → INCONCLUSIVE.
      - Otherwise INCONCLUSIVE.
      - Nit N3: on UNRESOLVED, log the C-link value.

    Args:
        period_results: list of count_charge_k4 result dicts with keys
            'resolved' (bool), 'value' (int or None), 'reason' (str or None),
            'c_link_result' (dict or None). Optional 'collapse' (bool) → R2-C.
        expected_periods: expected list length (raises ValueError on mismatch).
            Defaults to N_FULL_PERIODS=9; pass 20 for a 68 tu extended run.
        r14_trip_period: index of the #14-band trip (if any); if not None and
            earlier than the first COLLAPSE period, verdict → "FAIL(#14)".

    Returns:
        dict with 'verdict', 'n_resolved', 'n_unresolved', 'n_collapse',
        'n_wrong', 'n_periods', 'notes'.
    """
    n_periods = len(period_results)
    if n_periods != expected_periods:
        raise ValueError(
            f"aggregate_r2_periods: expected {expected_periods} periods, "
            f"got {n_periods} (period-count read-back)")

    n_resolved = 0
    n_wrong = 0
    n_unresolved = 0
    n_collapse = 0
    notes = []
    first_collapse_idx = None

    for i, pr in enumerate(period_results):
        if not isinstance(pr, dict) or 'resolved' not in pr:
            raise TypeError(
                f"Period {i}: expected count_charge_k4 result dict with 'resolved' "
                f"key, got {type(pr).__name__!r}. Legacy dicts are not accepted.")
        if pr.get('collapse'):
            if first_collapse_idx is None:
                first_collapse_idx = i
            n_collapse += 1
            notes.append(f"Period {i}: COLLAPSE (Re≤0 or size ratio <0.54); excluded from #7")
            continue
        if first_collapse_idx is not None:
            # Post-COLLAPSE periods excluded from #7, never a count FAIL.
            n_collapse += 1
            notes.append(f"Period {i}: post-COLLAPSE excluded from #7")
            continue
        resolved = bool(pr.get('resolved'))
        value = pr.get('value')
        reason = pr.get('reason') or ''
        clk = pr.get('c_link_result')
        c_link_val = clk.get('value') if isinstance(clk, dict) else None

        if not resolved:
            n_unresolved += 1
            notes.append(f"Period {i}: UNRESOLVED ({reason}); c_link={c_link_val!r}")
        else:
            n_resolved += 1
            if value != 6:
                n_wrong += 1
                notes.append(f"Period {i}: RESOLVED but wrong: value={value}")

    # R2-C verdict: any COLLAPSE → "COLLAPSE" (or "FAIL(#14)" if r14 earlier)
    if first_collapse_idx is not None:
        if r14_trip_period is not None and r14_trip_period < first_collapse_idx:
            verdict = "FAIL(#14)"
            notes.append(
                f"#14 band trip at period {r14_trip_period} before first COLLAPSE "
                f"at period {first_collapse_idx} → FAIL(#14)")
        else:
            verdict = "COLLAPSE"
            notes.append(
                f"COLLAPSE at period {first_collapse_idx} → run verdict COLLAPSE")
        return {
            'verdict': verdict,
            'n_resolved': n_resolved,
            'n_unresolved': n_unresolved,
            'n_collapse': n_collapse,
            'n_wrong': 0,
            'n_periods': n_periods,
            'notes': notes,
        }

    # Non-COLLAPSE verdict (integer 90% rule).
    if n_wrong > 0:
        verdict = "FAIL"
        n_active = n_periods - n_collapse
        notes.append(f"{n_wrong}/{n_active} resolved periods ≠ +6 → COUNT FAIL")
    elif 10 * n_resolved >= 9 * expected_periods:
        verdict = "PASS"
        notes.append(f"{n_resolved}/{expected_periods} resolved, all +6 → PASS")
    else:
        verdict = "INCONCLUSIVE"
        notes.append(
            f"only {n_resolved}/{expected_periods} resolved (< 90%) "
            f"({n_unresolved} UNRESOLVED) → RESOLUTION-INCONCLUSIVE")

    return {
        'verdict': verdict,
        'n_resolved': n_resolved,
        'n_unresolved': n_unresolved,
        'n_collapse': n_collapse,
        'n_wrong': n_wrong,
        'n_periods': n_periods,
        'notes': notes,
    }


# ---------------------------------------------------------------------------
# v7 pre-flight helpers (pf_checkpoint_times, antipodal_bonds,
#   classify_first_bond, preflight_verdict) and frozen specs
# ---------------------------------------------------------------------------


def pf_checkpoint_times(T: float) -> np.ndarray:
    """Checkpoint times for a pre-flight run to T.

    Spacing ≤ 0.005 for t ≤ 0.1; ≤ 0.025 after 0.1; always includes T.
    """
    fine = np.arange(0.005, min(T, 0.1) + 1e-10, 0.005)
    if T > 0.1:
        coarse = np.arange(0.125, T + 1e-10, 0.025)
    else:
        coarse = np.array([], dtype=float)
    times = np.concatenate([fine, coarse])
    if len(times) == 0 or abs(times[-1] - T) > 1e-10:
        times = np.append(times, T)
    return np.sort(np.unique(np.round(times, 10)))


_TETRA_OFFSETS = ((1, 1, 1), (1, -1, -1), (-1, 1, -1), (-1, -1, 1))


def antipodal_bonds(q: np.ndarray, mask_alive: np.ndarray,
                    centre) -> list:
    """Find alive tetra bonds with Re(q̄(x)q(x+p)) ≤ 0.

    Shares the bond loop with collapse_check. Returns list of
    (site, p, re, r) where r = distance from seed centre to bond midpoint.
    """
    bonds = []
    q_conj = q * np.array([1.0, -1.0, -1.0, -1.0])
    c = np.array(centre, dtype=float)
    for (di, dj, dk) in _TETRA_OFFSETS:
        qs = np.roll(np.roll(np.roll(q, -di, axis=0), -dj, axis=1), -dk, axis=2)
        prod_re = (q_conj[..., 0] * qs[..., 0]
                   - q_conj[..., 1] * qs[..., 1]
                   - q_conj[..., 2] * qs[..., 2]
                   - q_conj[..., 3] * qs[..., 3])
        hit = mask_alive & (prod_re <= 0)
        for site in np.argwhere(hit):
            i, j, k = site
            mid = np.array([i + di / 2.0, j + dj / 2.0, k + dk / 2.0])
            r = float(np.linalg.norm(mid - c))
            bonds.append((tuple(site.tolist()), (di, dj, dk), float(prod_re[i, j, k]), r))
    return bonds


def classify_first_bond(r_eq_t: float, r_eq0: float) -> str:
    """Classify the first antipodal bond as 'BREAKUP' or 'INFALL'.

    BREAKUP if r_eq(t_first)/r_eq(0) ≥ FIRST_BOND_BREAKUP_RATIO (0.85).
    """
    if r_eq0 <= 0.0:
        return 'INFALL'
    return 'BREAKUP' if (r_eq_t / r_eq0) >= FIRST_BOND_BREAKUP_RATIO else 'INFALL'


# ---------------------------------------------------------------------------
# Frozen preflight specs (v7, ladder bdb5c32b8e87)
# ---------------------------------------------------------------------------
# trace keys: r_eq0, t_first, r_first, r_eq_at_first, n_antipodal_T,
#             pre_bond_dH_max, pre_bond_N, ckpt_spacings_early (list[float])

PII_SPEC = {
    'name': 'PII',
    'N_expected': 1,
    'r_eq0_pin': R_EQ0_PII,
    'r_eq0_tol': 0.005,
    'is_control': False,
    'windows': [
        {'name': 't_first',      'lo': 0.025, 'hi': 0.09},
        {'name': 'r_first',      'lo': 4.0,   'hi': 11.0},
        {'name': 'r_eq_ratio',   'lo': 0.80,  'hi': 1.02},
        {'name': 'n_antipodal_T', 'min': 5},
    ],
}

PII_C_SPEC = {
    'name': 'PII_C',
    'N_expected': 1,
    'r_eq0_pin': R_EQ0_PII,
    'r_eq0_tol': 0.005,
    'is_control': True,
    'windows': [],
}

R2PF_SPEC = {
    'name': 'R2PF',
    'N_expected': 6,
    'r_eq0_pin': R_EQ0_R2,
    'r_eq0_tol': 0.05,
    'is_control': False,
    'windows': [
        {'name': 't_first',      'lo': 0.012, 'hi': 0.06},
        {'name': 'r_first',      'lo': 8.0,   'hi': 24.0},
        {'name': 'r_eq_ratio',   'lo': 0.85,  'hi': 1.02},
        {'name': 'n_antipodal_T', 'min': 5},
    ],
}

R2PF_C_SPEC = {
    'name': 'R2PF_C',
    'N_expected': 6,
    'r_eq0_pin': R_EQ0_R2,
    'r_eq0_tol': 0.05,
    'is_control': True,
    'windows': [],
}


def preflight_verdict(trace: dict, spec: dict) -> dict:
    """Gate and A8 verdict for a pre-flight run.

    Gate verdicts (precedence top-down):
    1. INVALID: checkpoint spacing > 0.005 at t ≤ 0.1; |dH| > 1e-3 before any
       bond; resolved N ≠ N_expected before any bond; r_eq(0) outside pin tol.
    2. BREAKUP / INFALL: bond seen; class from classify_first_bond.
    3. STABLE: no bond through T.

    A8 verdict:
    - Non-control: CONFIRMED iff BREAKUP + all windows pass;
      MISS if BREAKUP or INFALL but some window fails; N/A if STABLE or INVALID.
    - Control: MISS if BREAKUP-class bond (control should have none);
      N/A if INFALL or STABLE or INVALID.

    Trace keys (all optional — missing → treated as safe):
      r_eq0             float    r_eq at t=0
      t_first           float    time of first antipodal bond (None → no bond)
      r_first           float    distance to bond midpoint at t_first
      r_eq_at_first     float    r_eq at t_first
      n_antipodal_T     int      n_antipodal at end of run
      pre_bond_dH_max   float    max |dH/H0| before t_first
      pre_bond_N        int      resolved adapter value before t_first (None → skip check)
      ckpt_spacings_early list[float]  spacing of each checkpoint at t ≤ 0.1
    """
    reasons = []

    # 1. INVALID checks (precedence order)
    r_eq0 = trace.get('r_eq0', 0.0)
    r_eq0_pin = spec.get('r_eq0_pin')
    r_eq0_tol = spec.get('r_eq0_tol', 0.005)
    if r_eq0_pin is not None and abs(r_eq0 - r_eq0_pin) > r_eq0_tol:
        reasons.append(
            f"r_eq0={r_eq0:.4f} outside pin {r_eq0_pin}±{r_eq0_tol}")
        return {'gate': 'INVALID', 'a8': 'N/A', 'reasons': reasons}

    early_spacings = trace.get('ckpt_spacings_early', [])
    if early_spacings:
        max_early = max(early_spacings)
        if max_early > 0.005:
            reasons.append(
                f"checkpoint spacing {max_early:.4f} > 0.005 at t ≤ 0.1")
            return {'gate': 'INVALID', 'a8': 'N/A', 'reasons': reasons}

    pre_dH = trace.get('pre_bond_dH_max', 0.0)
    if pre_dH > 1e-3:
        reasons.append(f"|dH| = {pre_dH:.2e} > 1e-3 before any antipodal bond")
        return {'gate': 'INVALID', 'a8': 'N/A', 'reasons': reasons}

    N_exp = spec.get('N_expected')
    pre_N = trace.get('pre_bond_N')
    if pre_N is not None and N_exp is not None and pre_N != N_exp:
        reasons.append(
            f"adapter N={pre_N} ≠ N_expected={N_exp} before any antipodal bond")
        return {'gate': 'INVALID', 'a8': 'N/A', 'reasons': reasons}

    # 2 / 3. Gate verdict
    t_first = trace.get('t_first')
    if t_first is None:
        return {'gate': 'STABLE', 'a8': 'N/A', 'reasons': reasons}

    r_eq_at_first = trace.get('r_eq_at_first', 0.0)
    gate = classify_first_bond(r_eq_at_first, r_eq0)

    is_control = spec.get('is_control', False)
    if is_control:
        if gate == 'BREAKUP':
            r_ratio = r_eq_at_first / r_eq0 if r_eq0 > 0 else 0.0
            reasons.append(
                f"control: BREAKUP-class bond at t_first={t_first:.4f} "
                f"(ratio={r_ratio:.3f} ≥ {FIRST_BOND_BREAKUP_RATIO})")
            return {'gate': gate, 'a8': 'MISS', 'reasons': reasons}
        else:
            r_ratio = r_eq_at_first / r_eq0 if r_eq0 > 0 else 0.0
            reasons.append(
                f"control: INFALL at t_first={t_first:.4f} "
                f"(ratio={r_ratio:.3f} < {FIRST_BOND_BREAKUP_RATIO}) — logged")
            return {'gate': gate, 'a8': 'N/A', 'reasons': reasons}

    # Non-control: check A8 windows
    r_eq_ratio = r_eq_at_first / r_eq0 if r_eq0 > 0 else 0.0
    r_first = trace.get('r_first')
    n_antipodal_T = trace.get('n_antipodal_T', 0)
    failed = []
    for w in spec.get('windows', []):
        wn = w['name']
        if wn == 't_first':
            if not (w['lo'] <= t_first <= w['hi']):
                failed.append(
                    f"t_first={t_first:.4f} ∉ [{w['lo']}, {w['hi']}]")
        elif wn == 'r_first':
            if r_first is not None and not (w['lo'] <= r_first <= w['hi']):
                failed.append(
                    f"r_first={r_first:.3f} ∉ [{w['lo']}, {w['hi']}]")
        elif wn == 'r_eq_ratio':
            if not (w['lo'] <= r_eq_ratio <= w['hi']):
                failed.append(
                    f"r_eq_ratio={r_eq_ratio:.4f} ∉ [{w['lo']}, {w['hi']}]")
        elif wn == 'n_antipodal_T':
            if n_antipodal_T < w.get('min', 0):
                failed.append(
                    f"n_antipodal_T={n_antipodal_T} < {w['min']}")
    reasons.extend(failed)

    if gate == 'BREAKUP' and not failed:
        a8 = 'CONFIRMED'
    elif gate == 'INFALL':
        reasons.append(
            f"gate=INFALL (ratio={r_eq_ratio:.3f} < {FIRST_BOND_BREAKUP_RATIO}): "
            f"CONFIRMED requires BREAKUP")
        a8 = 'MISS'
    else:
        a8 = 'MISS'

    return {'gate': gate, 'a8': a8, 'reasons': reasons}


if __name__ == "__main__":
    run_r2()
