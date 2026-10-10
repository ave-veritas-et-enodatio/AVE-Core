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
K_HOPF = math.pi / 3.0  # engine default cf:1041 (self.k_hopf = float(np.pi/3.0))
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
# R2C_SIZE_RATIO is 6r_c-based (R2 primary, L=144): the A7.2 restoring barrier
# at R=13.0 → ratio 0.54 (ladder §3c.3, §7d.1). It is the R2-C size-collapse arm
# for the 288³ R2-primary run ONLY. v7.1: this number — and the 5.3 % barrier
# height and 61 % #14-edge margin — must NOT be applied to R2-PF (L=96 = 4r_c);
# R2-PF classifies its first bond with FIRST_BOND_BREAKUP_RATIO=0.85 instead.
R2C_SIZE_RATIO = 0.54      # 6r_c-based (R2 primary, L=144); period_collapse size arm

# First-bond classification: BREAKUP if r_eq(t_first)/r_eq0 ≥ 0.85, else INFALL
FIRST_BOND_BREAKUP_RATIO = 0.85

# Seed cutoffs (tanh profile parameter L = n_c × r_c)
SEED_L_PRIMARY = 144  # R2: rational(288,24), 6 r_c = 144
SEED_L_PII = 48       # P-ii: _hedgehog_at(128,12,...,L=48), 4 r_c
SEED_L_PF = 96        # R2-PF: rational(192,24,p=2,qq=3), cutoff L=96=4r_c=n/2, Math OK (v7.1)

# R2-PF #14 face-check pins (v7.1 §5 R2-PF, §7d.1) — LOG ONLY, 4r_c cutoff.
# At L=96 (4r_c) the predicted face tail (|q−1| units, fitted-D tail
# 3π r_c²(1+L/ℓ)e^{−L/ℓ}/L², ℓ=√2160; q0≈0.974 at the face) and the image
# shift δλ are larger than the R2-primary L=144 values. They exceed the
# R2-primary δλ ≤ 0.05 box rule; accepted for a T=0.25 pre-flight and logged.
R2PF_FACE_TAIL_L96 = 0.229   # R2-PF 4r_c face tail at L=96
R2PF_DLAMBDA_L96 = 0.176     # R2-PF 4r_c image shift δλ at L=96
# R2-primary (L=144, 6r_c) values, for contrast only — NOT applied to R2-PF.
R2_FACE_TAIL_L144 = 0.0484   # R2 primary 6r_c face tail at L=144
R2_DLAMBDA_L144 = 0.0136     # R2 primary 6r_c image shift δλ at L=144

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

    Seed is the axial (2,3) rational map (same as R2 primary, degree +6).
    rational(192,24) uses cutoff n/2 = 96 = SEED_L_PF (assert NX_PF/2 == SEED_L_PF).
    """
    assert NX_PF // 2 == SEED_L_PF, (
        f"R2-PF rational cutoff: NX_PF/2={NX_PF//2} != SEED_L_PF={SEED_L_PF}")
    k = K_OP10_PF_C if control else K_OP10
    n_steps_pf = math.ceil(T_PF / DT)
    # v7.1: the 6r_c barrier/height/margin numbers (R2C_SIZE_RATIO=0.54, 5.3 %,
    # 61 %) are R2-primary only and are NOT applied to R2-PF. The R2-PF first
    # bond is classified by FIRST_BOND_BREAKUP_RATIO (0.85) in preflight_verdict,
    # not by the 0.54 size arm. The face_check block below is LOG ONLY (4r_c).
    return {
        "nx": NX_PF, "ny": NY_PF, "nz": NZ_PF,
        "dt": DT, "n_steps": n_steps_pf, "t_end": T_PF,
        "gamma": GAMMA, "G": G, "G_c": G_C, "k_op10": k,
        "k_refl": K_REFL, "k_hopf": K_HOPF, "rotation_storage": ROTATION_STORAGE,
        "seed": {
            "constructor": "rational",
            "rc": SEED_RC, "p": SEED_P, "qq": SEED_QQ,
            "L": SEED_L_PF,   # rational cutoff is n/2; L stored for read-back
        },
        "face_check": {    # v7.1 §5 R2-PF / §7d.1 — LOG ONLY, 4r_c (L=96)
            "L": SEED_L_PF,
            "face_tail": R2PF_FACE_TAIL_L96,   # 0.229 at L=96
            "dlambda": R2PF_DLAMBDA_L96,       # 0.176 at L=96
            "r2_primary_face_tail_L144": R2_FACE_TAIL_L144,  # 0.0484 (contrast)
            "r2_primary_dlambda_L144": R2_DLAMBDA_L144,      # 0.0136 (contrast)
            "note": ("4r_c (L=96) face tail; the 6r_c barrier/height/margin "
                     "(0.54 / 5.3 % / 61 %) are R2-primary only, not applied here"),
        },
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
        "k_refl": K_REFL, "k_hopf": K_HOPF, "rotation_storage": ROTATION_STORAGE,
        "seed": {"constructor": "_hedgehog_at", "rc": 12, "L": SEED_L_PII},
        "checkpoints": pf_checkpoint_times(_T_PII),
    }


def build_pf_seed(cfg_dict: dict, n: int = None, rc: int = None) -> np.ndarray:
    """Build the initial quaternion array for a pre-flight config.

    When n and rc are given, constructs a stand-in seed at (n, rc) using the
    same L/rc ratio as the pinned config:
      L_standin = cfg['seed']['L'] * rc / cfg['seed']['rc']

    Dispatch on cfg['seed']['constructor']:
      "_hedgehog_at": calls _hedgehog_at(n, rc, (0,0,0), L=L_standin)
      "rational":     asserts n/2 == L_standin (rational has no L argument —
                      its cutoff is always n/2); then calls
                      rational(n, rc, p=..., qq=...).  Raises ValueError if
                      n/2 != L_standin, since the scale rule would violate the
                      hard cutoff invariant.

    When n and rc are None, uses the full config grid size and seed rc.
    """
    seed = cfg_dict['seed']
    constructor = seed['constructor']
    rc_cfg = seed['rc']
    n_use = n if n is not None else cfg_dict['nx']
    rc_use = rc if rc is not None else rc_cfg
    L_scaled = seed['L'] * rc_use / rc_cfg

    from ave.topological.charge_counters import _hedgehog_at, rational as _rational

    if constructor == '_hedgehog_at':
        return _hedgehog_at(n_use, rc_use, (0, 0, 0), L=L_scaled)
    elif constructor == 'rational':
        if n_use / 2.0 != L_scaled:
            raise ValueError(
                f"build_pf_seed: rational constructor requires n/2 == scaled L, "
                f"but n/2={n_use/2.0} != L_scaled={L_scaled} "
                f"(cfg L={seed['L']}, rc_cfg={rc_cfg}, rc_use={rc_use}). "
                "rational() cutoff is always n/2; adjust n or rc so n/2 == L.")
        return _rational(n_use, rc_use, p=seed['p'], qq=seed['qq'])
    else:
        raise ValueError(
            f"build_pf_seed: unknown seed constructor {constructor!r}; "
            "expected '_hedgehog_at' or 'rational'")


def preflight_setup(cfg: dict, n: int = None, rc: int = None) -> dict:
    """Build seed, alive mask, centre, and seed_sha1 for a pre-flight config.

    Returns dict with keys: q0, alive, centre, seed_sha1.  Used by both
    run_preflight and any test that needs the single seed-building path
    without running the solver.

    Centre = ((n-1)/2.0,)*3 in charge_counters.grid convention (F8 fix).
    """
    from ave.topological.charge_counters import bcc_alive_mask

    n_use = n if n is not None else cfg['nx']
    rc_use = rc if rc is not None else cfg['seed']['rc']

    q0 = build_pf_seed(cfg, n=n_use, rc=rc_use)
    alive = bcc_alive_mask((n_use, n_use, n_use))
    q0[~alive] = np.array([1.0, 0.0, 0.0, 0.0])
    seed_sha1 = hashlib.sha1(q0.tobytes()).hexdigest()
    ctr = (n_use - 1) / 2.0
    centre = (ctr, ctr, ctr)
    return {'q0': q0, 'alive': alive, 'centre': centre, 'seed_sha1': seed_sha1}


def preflight_initial_solver(cfg: dict, n: int = None, rc: int = None,
                              make_solver=None):
    """Build solver and apply initial state for a pre-flight config.

    Returns (cf, setup) where cf has cf.q set from preflight_setup's q0
    (dead-site reset already applied) and setup contains {'q0', 'alive',
    'centre', 'seed_sha1'}.

    This is the ONLY path from which opt-in pre-flight tests may obtain
    their initial solver + seed state.  No caller may read, copy, or assign
    the seed array directly — use cf.q or re-call preflight_initial_solver.
    """
    n_use = n if n is not None else cfg['nx']
    rc_use = rc if rc is not None else cfg['seed']['rc']
    gamma_cfg = cfg['gamma']
    k_op10_cfg = cfg['k_op10']
    k_refl_cfg = cfg['k_refl']
    k_hopf_cfg = cfg['k_hopf']   # v7.1: explicit key, not the engine default
    rot_cfg = cfg['rotation_storage']

    setup = preflight_setup(cfg, n=n_use, rc=rc_use)

    if make_solver is None:
        from ave.topological.cosserat_field_3d import CosseratField3D
        def make_solver(nn):
            cf_inner = CosseratField3D(
                nn, nn, nn,
                k_refl=k_refl_cfg,
                rotation_storage=rot_cfg,
            )
            cf_inner.gamma = gamma_cfg
            cf_inner.G = G
            cf_inner.G_c = G_C
            cf_inner.k_op10 = k_op10_cfg
            return cf_inner

    cf = make_solver(n_use)
    # Apply cfg physics params regardless of solver origin. k_hopf is set
    # explicitly from cfg (v7.1 §5): do NOT rely on the engine's π/3 default —
    # a supplied make_solver may default it differently (or to 0).
    cf.gamma = gamma_cfg
    cf.k_op10 = k_op10_cfg
    cf.k_refl = k_refl_cfg
    cf.k_hopf = k_hopf_cfg
    cf.q = setup['q0'].copy()
    return cf, setup


def run_preflight(cfg: dict, spec: dict, n: int = None, rc: int = None,
                  max_steps: int = None, make_solver=None) -> dict:
    """Shared pre-flight runner for P-ii, P-ii-C, R2-PF, R2-PF-C.

    Delegates solver + seed construction to preflight_initial_solver — the
    single initial-state path (single builder anchor).

    Checkpoint recording uses checkpoint_steps(ckpts, dt): each checkpoint
    t_k is recorded at the FIRST step s with s*dt >= t_k (F5 fix).

    Pre-bond dH measured vs H(0) (F6 fix).
    Post-bond dH measured vs H(0), not H_post (F7 fix).
    Centre = ((n_use-1)/2.0,)*3 — hedgehog zero in charge_counters.grid
    convention (F8 fix; avoids 0.87-unit offset from n//2).

    Returns trace dict with keys: rows, seed_sha1, H0, r_eq0, t_first,
    r_first, r_eq_at_first, n_antipodal_T, T.
    """
    from ave.topological.k4_quaternion import count_charge_k4

    n_use = n if n is not None else cfg['nx']
    rc_use = rc if rc is not None else cfg['seed']['rc']
    dt = float(cfg['dt'])
    T_end = float(cfg['t_end'])
    n_steps_full = int(cfg['n_steps'])
    n_steps = min(n_steps_full, max_steps) if max_steps is not None else n_steps_full

    # Build solver and seed via preflight_initial_solver — single initial-state path
    cf, setup = preflight_initial_solver(cfg, n=n_use, rc=rc_use, make_solver=make_solver)
    alive = setup['alive']
    centre = setup['centre']
    seed_sha1 = setup['seed_sha1']

    H0 = cf.total_energy_k4() + cf.kinetic_energy_k4()
    r_eq0 = r_eq_from_q(cf.q, alive)

    ckpts = cfg['checkpoints']
    hit_map = checkpoint_steps(ckpts, dt)  # {step: ckpt_idx}

    rows = []
    t_first = None
    r_first = None
    r_eq_at_first = None
    n_antipodal_T = 0

    for s in range(n_steps):
        cf.step(dt)
        step_1 = s + 1
        t = step_1 * dt

        bonds = antipodal_bonds(cf.q, alive, centre)
        n_antipodal_T = len(bonds)

        if t_first is None and bonds:
            t_first = t
            r_first = min(b[3] for b in bonds)
            r_eq_at_first = r_eq_from_q(cf.q, alive)

        if step_1 in hit_map:
            ckpt_t = float(ckpts[hit_map[step_1]])
            H_now = cf.total_energy_k4() + cf.kinetic_energy_k4()
            dH = abs(H_now - H0) / max(abs(H0), 1e-30)

            r_res = count_charge_k4(cf.q, alive)
            resolved = bool(r_res.get('resolved', False))
            N = r_res.get('value') if resolved else None
            r_eq_now = r_eq_from_q(cf.q, alive)

            rows.append({
                't': ckpt_t,
                'step': step_1,
                'N': N,
                'resolved': resolved,
                'dH': dH,
                'n_antipodal': n_antipodal_T,
                'r_eq': r_eq_now,
            })

    return {
        'rows': rows,
        'seed_sha1': seed_sha1,
        'H0': H0,
        'r_eq0': r_eq0,
        't_first': t_first,
        'r_first': r_first,
        'r_eq_at_first': r_eq_at_first,
        'n_antipodal_T': n_antipodal_T,
        'T': T_end,
        'centre': centre,
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

    R2-C (v7): if any period has collapse=True, verdict precedence is:
    FAIL(#14) > FAIL (pre-collapse wrong) > COLLAPSE. Exception: if
    r14_trip_period is not None and occurs before the first COLLAPSE period,
    the verdict is "FAIL(#14)"; a pre-collapse resolved period with value ≠ +6
    yields "FAIL", which outranks COLLAPSE.

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

    # R2-C verdict: any COLLAPSE → "COLLAPSE" (or "FAIL(#14)" or "FAIL" if higher
    # precedence applies). Precedence: FAIL(#14) > FAIL (pre-collapse wrong) > COLLAPSE.
    if first_collapse_idx is not None:
        if r14_trip_period is not None and r14_trip_period < first_collapse_idx:
            verdict = "FAIL(#14)"
            notes.append(
                f"#14 band trip at period {r14_trip_period} before first COLLAPSE "
                f"at period {first_collapse_idx} → FAIL(#14)")
        elif n_wrong > 0:
            verdict = "FAIL"
            notes.append(
                f"{n_wrong} pre-collapse resolved period(s) ≠ +6 → FAIL "
                f"(pre-collapse wrong value outranks COLLAPSE)")
        else:
            verdict = "COLLAPSE"
            notes.append(
                f"COLLAPSE at period {first_collapse_idx} → run verdict COLLAPSE")
        return {
            'verdict': verdict,
            'n_resolved': n_resolved,
            'n_unresolved': n_unresolved,
            'n_collapse': n_collapse,
            'n_wrong': n_wrong,
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


def checkpoint_steps(times, dt: float) -> dict:
    """Map checkpoint times to 1-indexed step numbers: first step s with s*dt >= t_k.

    Returns dict {step: ckpt_idx}.  Uses ceil(t_k/dt) with a small epsilon guard
    against floating-point overshoot so exact multiples don't bump to the next step.
    """
    result = {}
    for idx, t_k in enumerate(times):
        ratio = float(t_k) / float(dt)
        # Guard: if ratio is within 1e-9 of an integer, treat it as that integer.
        rounded = round(ratio)
        step = int(rounded) if abs(ratio - rounded) < 1e-9 else int(np.ceil(ratio))
        step = max(1, step)
        if step not in result:
            result[step] = idx
    return result


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
# Mirror-control energy offset (v7.1 "Mirror controls", HOPF-TERM-CHECK §5)
# ---------------------------------------------------------------------------
# The Hopf term is mirror-ODD: E_hopf(mirror) = −E_hopf(seed) (verified exactly
# by the Gate: +3.3437/−3.3437 on the 72³ hedgehog, +24.340/−24.340 on
# rational(192,24)). Every other energy term (strain, κ, op10, reflection) is
# bit-identical between a seed and its mirror. Therefore the total energies
# differ by exactly 2·k_hopf·E_hopf(seed) — a seed vs mirror comparison must
# NOT require exact ± symmetry of H. Count-sign symmetry N → −N stays EXACT
# (the integer charge flips sign with no energy-offset slack).

# Documented slack for the (nominally identical) non-Hopf terms: on a mirror
# (global q2 → −q2) the per-site non-Hopf densities are invariant, but JAX
# reduction ordering is not bit-identical, so H_seed − H_mirror carries a
# residual ~1e-15·|H| on top of the 2·k_hopf·E_hopf offset. 1e-9 is ~6 orders
# above that residual and ~6 orders below the physical offset (≤1e-3·|H|).
MIRROR_ENERGY_REL_SLACK = 1e-9


def mirror_energy_allowance(E_hopf, k_hopf=K_HOPF, rel_slack=MIRROR_ENERGY_REL_SLACK):
    """Allowed |ΔH| between a seed and its mirror given the seed's Hopf energy.

    Returns 2·|k_hopf·E_hopf| (the mirror-odd offset magnitude) plus a small
    documented slack. Nonzero whenever E_hopf ≠ 0.

    E_hopf is the Hopf energy WITHOUT the k_hopf prefactor — i.e.
    Σ_alive _hopf_density_q(q); the total-energy contribution is k_hopf·E_hopf.
    """
    base = 2.0 * abs(k_hopf) * abs(E_hopf)
    return base + rel_slack * max(base, 1.0)


def mirror_energy_consistent(H_seed, H_mirror, E_hopf_seed, k_hopf=K_HOPF,
                             rel_slack=MIRROR_ENERGY_REL_SLACK):
    """True iff (H_seed − H_mirror) matches the mirror-odd Hopf offset.

    Checks |(H_seed − H_mirror) − 2·k_hopf·E_hopf_seed| ≤ slack, where slack is
    rel_slack scaled by the energy magnitude. Exact ± symmetry is NOT required
    (the offset 2·k_hopf·E_hopf_seed is expected and allowed). Count-sign
    symmetry N → −N is a separate, exact relation and is not loosened here.

    E_hopf_seed is Σ_alive _hopf_density_q(q_seed) (no k_hopf prefactor).
    """
    expected = 2.0 * k_hopf * E_hopf_seed
    residual = abs((H_seed - H_mirror) - expected)
    scale = max(abs(H_seed), abs(H_mirror), abs(expected), 1.0)
    return residual <= rel_slack * scale


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
    """Gate and A8 verdict for a pre-flight run (rows-based trace, v7).

    Trace required keys:
      rows         list of per-checkpoint row dicts, each with:
                     t (float), step (int), N (int|None), resolved (bool),
                     dH (float, |ΔH|/H0 at this checkpoint), n_antipodal (int),
                     r_eq (float)
      H0           float   energy at t=0
      r_eq0        float   r_eq at t=0
      t_first      float|None  time of first antipodal bond (key MUST be present)
      r_first      float|None  distance to bond midpoint at t_first
      r_eq_at_first  float|None  r_eq at t_first
      n_antipodal_T  int  n_antipodal at end of run
      T            float  end time of run

    Gate verdicts (precedence top-down):
    1. INVALID: missing required key ('rows', 'H0', 't_first'); empty rows;
       r_eq(0) outside pin tolerance; spacing > 0.005 anywhere at t ≤ 0.1
       (derived from row times); any pre-bond row is UNRESOLVED, has N ≠
       N_expected, or has |dH| > 1e-3; STABLE but rows do not reach T.
    2. BREAKUP / INFALL: bond seen; class from classify_first_bond.
    3. STABLE: no bond through T, all rows valid.

    A8 verdict:
    - Non-control: CONFIRMED iff BREAKUP + all windows pass;
      MISS if BREAKUP or INFALL but some window fails; N/A if STABLE or INVALID.
    - Control: MISS if BREAKUP-class bond; N/A if INFALL, STABLE, or INVALID.

    Post-bond rows (t > t_first): |dH| > 1e-2 appends 'dH>1e-2 flag' to
    reasons (log only; does not change gate or a8).
    """
    reasons = []

    # 0. Required trace key presence
    for key in ('rows', 'H0', 'r_eq0', 't_first', 'T'):
        if key not in trace:
            reasons.append(f"missing required trace key '{key}'")
            return {'gate': 'INVALID', 'a8': 'N/A', 'reasons': reasons}

    rows = trace['rows']
    if not rows:
        reasons.append("empty rows — no checkpoint recorded (INVALID)")
        return {'gate': 'INVALID', 'a8': 'N/A', 'reasons': reasons}

    # 0b. Required per-row keys
    _ROW_KEYS = ('t', 'step', 'N', 'resolved', 'dH', 'n_antipodal', 'r_eq')
    for i, row in enumerate(rows):
        for rk in _ROW_KEYS:
            if rk not in row:
                reasons.append(
                    f"row {i} (t={row.get('t', '?')}): missing required row key '{rk}'")
                return {'gate': 'INVALID', 'a8': 'N/A', 'reasons': reasons}

    # 1a. r_eq0 pin check
    r_eq0 = trace['r_eq0']
    r_eq0_pin = spec.get('r_eq0_pin')
    r_eq0_tol = spec.get('r_eq0_tol', 0.005)
    if r_eq0_pin is not None and abs(r_eq0 - r_eq0_pin) > r_eq0_tol:
        reasons.append(
            f"r_eq0={r_eq0:.4f} outside pin {r_eq0_pin}±{r_eq0_tol}")
        return {'gate': 'INVALID', 'a8': 'N/A', 'reasons': reasons}

    # 1b. Spacing check: origin + all rows at t ≤ 0.1 (pre- and post-bond)
    t_first = trace['t_first']
    early_times = [0.0] + sorted(r['t'] for r in rows if r['t'] <= 0.1 + 1e-9)
    if len(early_times) >= 2:
        early_arr = np.array(early_times)
        max_early_sp = float(np.max(np.diff(early_arr)))
        if max_early_sp > 0.005 + 1e-9:
            reasons.append(
                f"checkpoint spacing {max_early_sp:.4f} > 0.005 at t ≤ 0.1 "
                f"(origin + row times; pre- and post-bond)")
            return {'gate': 'INVALID', 'a8': 'N/A', 'reasons': reasons}

    # 1c. Per-row pre-bond checks (N, resolved, dH)
    N_exp = spec.get('N_expected')
    pre_bond_rows = [r for r in rows
                     if t_first is None or r['t'] < t_first - 1e-9]
    for row in pre_bond_rows:
        rt = row['t']
        if not row['resolved']:
            reasons.append(
                f"checkpoint t={rt:.5f}: UNRESOLVED — "
                f"required resolved with N={N_exp} before any bond")
            return {'gate': 'INVALID', 'a8': 'N/A', 'reasons': reasons}
        if N_exp is not None and row['N'] != N_exp:
            reasons.append(
                f"checkpoint t={rt:.5f}: N={row['N']} ≠ N_expected={N_exp} "
                f"before any bond")
            return {'gate': 'INVALID', 'a8': 'N/A', 'reasons': reasons}
        row_dH = row['dH']
        if row_dH > 1e-3:
            reasons.append(
                f"checkpoint t={rt:.5f}: |dH|={row_dH:.2e} > 1e-3 before any bond")
            return {'gate': 'INVALID', 'a8': 'N/A', 'reasons': reasons}

    # 2 / 3. Gate verdict
    if t_first is None:
        # STABLE additionally requires rows to reach T
        T_end = trace['T']
        last_t = rows[-1]['t']
        if last_t < T_end - 1e-9:
            reasons.append(
                f"STABLE requires rows to reach T={T_end:.4f}; "
                f"last row at t={last_t:.4f}")
            return {'gate': 'INVALID', 'a8': 'N/A', 'reasons': reasons}
        return {'gate': 'STABLE', 'a8': 'N/A', 'reasons': reasons}

    # Bonded trace: require r_first, r_eq_at_first, n_antipodal_T non-None
    for key in ('r_first', 'r_eq_at_first', 'n_antipodal_T'):
        if key not in trace:
            reasons.append(f"bonded trace missing required key '{key}'")
            return {'gate': 'INVALID', 'a8': 'N/A', 'reasons': reasons}
        if trace[key] is None:
            reasons.append(
                f"bonded trace: '{key}' is None but t_first is not None")
            return {'gate': 'INVALID', 'a8': 'N/A', 'reasons': reasons}

    # Post-bond dH flag (log only; does not change gate or a8)
    for row in rows:
        if row['t'] > t_first + 1e-9 and row['dH'] > 1e-2:
            reasons.append("dH>1e-2 flag")
            break

    r_eq_at_first = trace['r_eq_at_first']
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
    r_first = trace['r_first']
    n_antipodal_T = trace['n_antipodal_T']
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
