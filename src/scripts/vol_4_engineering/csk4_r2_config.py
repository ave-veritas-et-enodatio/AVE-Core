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
  steps = 144 643  32.4 time-units / 2.24e-4 dt (20 breathing periods,
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
N_STEPS = 144_643       # 32.4 tu / DT  (20 breathing periods)

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


def aggregate_r2_periods(period_results):
    """Aggregate per-period count_charge_k4 results for the R2 breathing check.

    F4 (v5): this consumes count_charge_k4 RESULT DICTS directly — the adapter is
    the single source of truth for whether a period resolved. A period is counted
    RESOLVED iff the adapter returned resolved=True (which already requires c_exact
    AND c_link to agree). Any resolved=False — for ANY reason (NONUNIT, NONFINITE,
    boundary margin, c_exact/c_link DISAGREEMENT) — is UNRESOLVED, never a FAIL.
    This closes the agg_clink_ignored mutant: a c_link-only disagreement is handled
    by the adapter (→ resolved=False → UNRESOLVED), not by a `ce!=6 or cl!=6` FAIL.

    Ladder §5 R2 #7 verdict logic:
      - A RESOLVED value ≠ +6 is the only COUNT FAIL.
      - PASS needs ≥ 90% resolved AND all resolved values = +6.
      - < 90% resolved (too many UNRESOLVED) → INCONCLUSIVE.
      - Nit N3: on an UNRESOLVED period, log the C-link value alone.

    Args:
        period_results: list of count_charge_k4 result dicts with keys
            'resolved' (bool), 'value' (int or None), 'reason' (str or None),
            'c_link_result' (dict or None, for the N3 c_link log).
            Legacy {'c_exact','c_link'} dicts are also accepted for back-compat.

    Returns:
        dict with 'verdict' (PASS/FAIL/INCONCLUSIVE), 'n_resolved',
        'n_unresolved', 'n_wrong', 'n_periods', 'notes' (list[str]).
    """
    n_periods = len(period_results)
    n_resolved = 0
    n_wrong = 0
    n_unresolved = 0
    notes = []

    for i, pr in enumerate(period_results):
        if 'resolved' in pr:
            # count_charge_k4 result dict (canonical path).
            resolved = bool(pr.get('resolved'))
            value = pr.get('value')
            reason = pr.get('reason') or ''
            clk = pr.get('c_link_result')
            c_link_val = clk.get('value') if isinstance(clk, dict) else None
        else:
            # Legacy {'c_exact','c_link'} dict: resolved iff both present AND agree
            # (so a c_link-only disagreement is UNRESOLVED, not FAIL).
            ce = pr.get('c_exact')
            cl = pr.get('c_link')
            c_link_val = cl if cl is not None else pr.get('c_link_raw')
            resolved = (ce is not None and cl is not None and ce == cl)
            value = ce if resolved else None
            reason = '' if resolved else 'UNRESOLVED (legacy: c_exact/c_link absent or disagree)'

        if not resolved:
            n_unresolved += 1
            # Nit N3: log the C-link value alone on UNRESOLVED.
            notes.append(f"Period {i}: UNRESOLVED ({reason}); c_link={c_link_val!r}")
        else:
            n_resolved += 1
            if value != 6:
                n_wrong += 1
                notes.append(
                    f"Period {i}: RESOLVED but wrong: value={value}")

    # A resolved wrong value is the only COUNT FAIL — it dominates the verdict.
    if n_wrong > 0:
        verdict = "FAIL"
        notes.append(
            f"{n_wrong}/{n_periods} resolved periods ≠ +6 → COUNT FAIL")
    elif n_periods > 0 and n_resolved >= 0.9 * n_periods:
        verdict = "PASS"
        notes.append(f"{n_resolved}/{n_periods} resolved, all +6 → PASS")
    else:
        verdict = "INCONCLUSIVE"
        notes.append(
            f"only {n_resolved}/{n_periods} resolved (< 90%) "
            f"({n_unresolved} UNRESOLVED) → RESOLUTION-INCONCLUSIVE")

    return {
        'verdict': verdict,
        'n_resolved': n_resolved,
        'n_unresolved': n_unresolved,
        'n_wrong': n_wrong,
        'n_periods': n_periods,
        'notes': notes,
    }


if __name__ == "__main__":
    run_r2()
