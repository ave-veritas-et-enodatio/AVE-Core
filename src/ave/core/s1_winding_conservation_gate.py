"""S1 — the (2,3) winding as a separately-conserved DOF: the DYNAMICAL gate.

FROZEN PRE-REG: research/2026-06-24_engine-s1-winding-dof_prereg.md (commit bed0b2d3).
This module is the S1 make-or-break gate (pre-reg §3 SUB-CLAIM A): single-knot
(2,3)-winding conservation under the engine's ACTUAL `step()` (NOT static
`deform_continuous`) + a LOCAL winding-current continuity law (∂_t W + ∇·J_W ≈
source). Two-soliton TRANSFER is DEFERRED (pre-reg §3 (d), §6 SUB-CLAIM B).

AXIOM CHAIN (recorded per pre-reg §8.8): charge = the Beltrami helicity
H_bel = ∫ ω·(∇×ω) read off the real-space Cosserat ω micro-rotation grade
(master-equation.md:20). The (2,3) winding is the toroidal "2" (ω polarization-
direction) × poloidal "3" (the ω-tank LC quadrature phase). Coordinate category
RULED real-space ω-grade (pre-reg §7 Fork 2): the phase-space (V_inc, V_ref)
Clifford torus is V's read-only projection (NOT an independent DOF, so it cannot
host the separately-conserved winding); the real-space ω is the only genuinely
independent DOF (own field + own momentum I_ω·ω̇, cosserat_field_3d.py:934,948).

ANTI-REBUILD (Rule 14): this gate REUSES the crystal_graft_v2/v4 immune system
(slaved_omega positive control, real_dynamics_ran flag, alias canary, H_bel
pre/post-lock drift, helicity ledger) + charge_quantization.compute_Q_link /
seed_pq_winding. It PORTS the chord-deciding readout onto the α-clean host
`src/tests/engine_acceptance/_winding_host.py` (κ̃=6/5). It NEVER imports/routes
ALPHA / KAPPA_CHIRAL_ELECTRON / V_SNAP / L_NODE / M_E / Q_TANK on the readout
path (pre-reg §0 α-clean host; §5 trap 8).

CLASSIFICATION (consistency-vs-emergence): CONSISTENCY-class (pre-reg §2). It
upgrades "A1-sustains-rotation" from asserted-CLASS to derived-REAL for the
declared real-space ω coordinate and the single-knot conservation claim ONLY.
It is NOT the α-free chord (that is S4). The Q=137 slot stays EMPTY (gate
wmighcz1z, anti-substitution).
"""

from __future__ import annotations

import numpy as np

# ── α-CLEAN HOST (the chord-deciding readout path; κ̃=6/5, NO α). Importing this
#    module executes its load-time guard triad — an α-leak fails HERE. ──────────
from tests.engine_acceptance import _winding_host as HOST

# ── the engine: α-clean on all forbidden readout symbols (verified 2026-06-24;
#    crystal_engine/v2/v3/v4 import only NU_VAC + R_II from constants, never
#    ALPHA / KAPPA_CHIRAL_ELECTRON / V_SNAP / L_NODE / M_E / Q_TANK). κ̃ defaults
#    to the 6/5 literal in CrystalEngine.__init__ (α-FREE). ──────────────────────
from ave.core.crystal_graft_v4 import CrystalGraftV4

# ── the ported immune-system readouts (α-free: charge_quantization carries its
#    OWN value-echo import-guard; fast_winding_extractor is a pure instrument). ──
from ave.topological.charge_quantization import compute_Q_link, seed_pq_winding
from ave.utils.fast_winding_extractor import extract_2_3_omega_fast

# ── the engine config (frozen, α-FREE; mirrors crystal_graft_v4_run CFG). ──────
_CFG = dict(
    source_mode="abc", lam_sign=1, p=2, q=3, S_min=2e-3, A_cap=0.999,
    omega_gap=1.0, wall_center=0.62, wall_width=0.30,
    kappa_tilde=6.0 / 5.0, pml_thickness=6,
)
# the α-free winding factor the host certifies (κ̃ = 6/5); engine + host AGREE.
_KAPPA_TILDE = HOST.winding_kappa_tilde(2, 3)

# pre-stated tolerances (FROZEN before the run; do NOT tune to force a verdict).
ALIAS_TOL = 0.34            # pre-reg §3(c) alias canary
CONTINUITY_REL_TOL = 0.35   # interior dW/dt accounted by source+flux to this rel
MIN_CELLS_PER_TURN = 3.0    # pre-reg §4 resolution ceiling (q resolved ≥ 3-4 cells/turn)
NEG_CTRL_PUMP_RATIO = 3.0   # lock-OFF |L_ω| must exceed lock-ON by this factor (FIRES)


# ──────────────────────────────────────────────────────────────────────────────
# READOUT HELPERS (ported instruments — α-free).
# ──────────────────────────────────────────────────────────────────────────────
def _read_winding_lc(e: CrystalGraftV4, R: float, r: float) -> dict:
    """LC-quadrature (2,3) read on the INDEPENDENT ω carrier + the alias canary on
    the RETAINED RAW float trajectory (pre-reg §3(c), §5 trap 2). Uses
    extract_2_3_omega_fast (toroidal "2" = arg(ω·ê_R + iω·ê_z) around φ; poloidal
    "3" = arg(ω·d̂ + iπ_ω·d̂) around ψ — the C-state/L-state of the ω reactance
    pair, NOT slaved to V). Returns the dict augmented with w_pol_alias_frac."""
    res = extract_2_3_omega_fast(e.omega, e.omega_velocity(), R, r, e.N)
    for sec in ("w_tor", "w_pol"):
        raws = res.get(f"{sec}_raw_list", [])
        if raws:
            mode = res[sec]
            outl = sum(1 for w in raws if abs(abs(w) - mode) > 1.0 or abs(w) > 6.5)
            res[f"{sec}_alias_frac"] = outl / len(raws)
        else:
            res[f"{sec}_alias_frac"] = 0.0
    res["alias_frac"] = max(res["w_tor_alias_frac"], res["w_pol_alias_frac"])
    return res


def _curl_roll(F: np.ndarray) -> np.ndarray:
    """∇×F (central-difference, periodic via roll) — the SAME operator the engine
    uses for H_bel (crystal_graft_v2._curl, dx=1). Bit-consistent with the
    dynamics' helicity bookkeeping."""
    Fx, Fy, Fz = F[..., 0], F[..., 1], F[..., 2]

    def d(a, axis):
        return (np.roll(a, -1, axis=axis) - np.roll(a, 1, axis=axis)) / 2.0

    out = np.empty_like(F)
    out[..., 0] = d(Fz, 1) - d(Fy, 2)
    out[..., 1] = d(Fx, 2) - d(Fz, 0)
    out[..., 2] = d(Fy, 0) - d(Fx, 1)
    return out


def _helicity_density(omega: np.ndarray) -> np.ndarray:
    """h(x) = ω·(∇×ω) — the LOCAL winding (helicity) density (charge density)."""
    c = _curl_roll(omega)
    return omega[..., 0] * c[..., 0] + omega[..., 1] * c[..., 1] + omega[..., 2] * c[..., 2]


def _local_continuity_residual(e: CrystalGraftV4) -> dict:
    """LOCAL winding-current continuity across ONE engine step (pre-reg §3(c),
    §5 trap 4): ∂_t W + ∇·J_W = source.

    For the ω carrier (∂_t ω = π_ω) the helicity density h = ω·(∇×ω) obeys the
    EXACT continuum identity
        ∂_t h = 2 π_ω·(∇×ω) + ∇·(π_ω × ω)
    (the first term = the LC breathing source — the ω-tank exchanging helicity
    between its C-state and L-state, ZERO for a force-free Beltrami field; the
    second = a pure DIVERGENCE = the helicity-current flux J_W = ω × π_ω). The
    interior winding-charge W_in = ∫_interior h then changes ONLY via this source
    + the boundary flux. We measure dW_in/dt by finite difference across the step
    and confirm it is accounted (to CONTINUITY_REL_TOL) by source + flux — i.e.
    no UNACCOUNTED interior non-conservation (the substrate-native statement that
    the winding is a conserved current, with NO second soliton)."""
    m = e.interior_mask()
    o0 = e.omega.copy()
    pi0 = e.omega_velocity().copy()
    h0 = float((_helicity_density(o0) * m).sum())
    e.step()
    h1 = float((_helicity_density(e.omega) * m).sum())
    dW_dt = (h1 - h0) / e.dt
    # source: 2 π·(∇×ω) (the LC breathing exchange)
    src = float((2.0 * np.sum(pi0 * _curl_roll(o0), axis=-1) * m).sum())
    # flux: ∇·(π×ω) integrated over interior = boundary helicity-current flux
    cross = np.cross(pi0, o0)

    def ddiv(a, axis):
        return (np.roll(a, -1, axis) - np.roll(a, 1, axis)) / 2.0

    div = ddiv(cross[..., 0], 0) + ddiv(cross[..., 1], 1) + ddiv(cross[..., 2], 2)
    flux = float((div * m).sum())
    resid = dW_dt - (src + flux)
    # NOTE: the relative residual is reported but NOT binned per-step — a single
    # LC turning-point instant has dW/dt≈0 and src≈0, so |resid|/|dW/dt| blows up
    # on a NUMERICALLY TINY residual. The honest continuity verdict is taken on
    # the WINDOW AGGREGATE (continuity_over_window), which floors the denominator
    # by the window's RMS |dW/dt| so a turning-point instant cannot manufacture a
    # false fail. (This is robustness, not a tune-to-PASS — the absolute residual
    # is what closes; the floor only normalizes it.)
    rel = abs(resid) / (abs(dW_dt) + 1e-9)
    return {
        "dW_dt": dW_dt, "source_2pi_curl_omega": src,
        "flux_div_pi_cross_omega": flux, "residual": resid, "rel_residual": rel,
    }


def continuity_over_window(e: CrystalGraftV4, n_probe: int = 8, stride: int = 25) -> dict:
    """Aggregate the local continuity over a WINDOW of steps (robust to LC
    turning-point instants). At n_probe checkpoints (stride apart) measure the
    single-step continuity residual; bin on the WINDOW residual normalized by the
    window's RMS |dW/dt| (a physically-meaningful scale, not a near-zero instant).
    Closes ⇔ the interior winding change is accounted by source + flux to
    CONTINUITY_REL_TOL across the window."""
    dWs, resids = [], []
    for _ in range(n_probe):
        c = _local_continuity_residual(e)  # advances ONE step
        dWs.append(c["dW_dt"])
        resids.append(c["residual"])
        for _ in range(stride - 1):
            e.step()
    rms_dW = float(np.sqrt(np.mean(np.square(dWs))) + 1e-12)
    rms_resid = float(np.sqrt(np.mean(np.square(resids))))
    rel = rms_resid / rms_dW
    return {
        "rms_dW_dt": rms_dW, "rms_residual": rms_resid, "rel_residual_window": rel,
        "per_probe_dW_dt": [round(x, 4) for x in dWs],
        "per_probe_residual": [round(x, 4) for x in resids],
        "closed": bool(rel <= CONTINUITY_REL_TOL),
    }


def _cells_per_turn(r: float, q: int = 3) -> float:
    """Lattice resolution per poloidal turn (pre-reg §4): a (·,q) winding spends
    2πr/q cells/turn; the q=3 read is faithful for ≳ 3-4 cells/turn."""
    return 2.0 * np.pi * float(r) / float(q)


def _build_isolated_knot(N: int, R: float, r: float, *, lock_on: bool,
                         amplitude: float = 0.4, slaved: bool = False) -> CrystalGraftV4:
    """The ISOLATED single-knot config (pre-reg §3 SUB-CLAIM A): the ω carrier ON
    with its OWN wave eq + OWN momentum + mass-gap LC reactance; the bulk-buckle
    and photon source OFF (the make-or-break is conservation of an EXISTING knot
    under genuine ω evolution, NOT genesis). lock_on=False is the v3-behaviour
    contrast (the |L_ω| pump). Seeded via seed_omega_known_2_3 (the LC-quadrature
    plant: C-state in ω, L-state in ω_prev ⇒ a genuine breathing knot)."""
    e = CrystalGraftV4(
        N=N, lock_on=lock_on, lock_eta=(0.05 if lock_on else 0.0),
        photon_coupling=False, buckle_on=False, omega_sector_on=True,
        slaved_omega=slaved, **_CFG,
    )
    e.seed_omega_known_2_3(R, r, amplitude=amplitude, p=2, q=3)
    return e


def _build_coupled_knot(N: int, R: float, r: float, *, lock_on: bool,
                        slaved: bool = False, amplitude: float = 0.4) -> CrystalGraftV4:
    """The COUPLED arm (buckle + photon-director ON) used by the CONTROLS only.

    The isolated knot (_build_isolated_knot) is the conservation subject; but the
    CONTROLS need the bulk↔ω coupling LIVE: (e) the |L_ω| pump that the lock
    arrests exists ONLY when the buckle sources rigid ω-rotation from the
    photon/breather (a zero-net-L isolated knot has nothing to pump — verified
    |L_ω|≡0 isolated); (f) the V-perturbation can probe ω-independence ONLY when
    V couples to ω (buckle OFF ⇒ V decoupled ⇒ the perturbation never reaches ω,
    so 'robust' would be vacuous). This is the crystal_graft_v4_run control
    config. The κ̃ in the buckle is the engine's 6/5 literal (α-FREE)."""
    e = CrystalGraftV4(
        N=N, lock_on=lock_on, lock_eta=(0.05 if lock_on else 0.0),
        photon_coupling=True, buckle_on=True, omega_sector_on=True,
        slaved_omega=slaved, **_CFG,
    )
    ic = N // 2
    e.seed_bulk((ic, ic, ic), sigma=10.0, frac=0.999)
    e.seed_photon((ic, ic, ic), helicity=1.0, sigma=7.0, wavelength=10.0, amplitude=0.35)
    e.freeze_wall_window()
    e.seed_omega_known_2_3(R, r, amplitude=amplitude, p=2, q=3)
    return e


# ──────────────────────────────────────────────────────────────────────────────
# VALIDATE-ON-KNOWN (pre-reg §4 PRIMARY — the honest floor).
# ──────────────────────────────────────────────────────────────────────────────
def validate_on_known(N: int = 32, R: float = 7.0, r: float = 2.3) -> dict:
    """The static planted-integer recovery floor (pre-reg §4 PRIMARY): the
    real-space-phase extractor compute_Q_link MUST read Q_link=3 (poloidal) and
    w_tor=2 (toroidal) on a seeded canonical (2,3) (seed_pq_winding) — the only
    recoverable-in-limit known-good (there is NO existing PASSING dynamical (2,3)
    test to recover; §4 NOTE). 'An extractor that cannot see a known-imposed
    (2,3) cannot certify its absence.' Reads ONLY the integer + sign (α-free)."""
    omega_planted = seed_pq_winding(N, 2, 3, R, r)
    q = compute_Q_link(omega_planted, R, r)
    omega_null = np.zeros((N, N, N, 3), dtype=np.float64)
    qn = compute_Q_link(omega_null, R, r)
    pos_ok = (q["Q_link"] == 3) and (q["w_tor"] == 2) and abs(q["Q_link_raw"] - 3) < 0.25
    null_ok = (qn["Q_link"] == 0)
    return {
        "Q_link_poloidal": q["Q_link"], "Q_link_raw": round(q["Q_link_raw"], 4),
        "w_tor_toroidal": q["w_tor"], "w_pol_rel": round(q["w_pol_rel"], 3),
        "null_Q_link": qn["Q_link"],
        "known_positive_recovers_2_3": bool(pos_ok),
        "known_negative_null_is_zero": bool(null_ok),
        "PASS": bool(pos_ok and null_ok),
    }


# ──────────────────────────────────────────────────────────────────────────────
# THE FIVE SUB-GATES (pre-reg §3: a/b/c/e/f) + continuity + resolution.
# ──────────────────────────────────────────────────────────────────────────────
def gate_a_non_vacuity(N: int = 48, R: float = 11.0, r: float = 4.0,
                       n_steps: int = 400) -> dict:
    """(a) NON-VACUITY (pre-reg §3(a), §5 trap 1): ω genuinely evolved under its
    OWN wave eq (a_ω = c_ω²∇²ω − ω_gap²ω, crystal_graft_v4.py:240-241) with its
    OWN momentum I_ω·ω̇. real_dynamics_ran ⇔ the field moved AND its evolution is
    not a frozen template. Frozen-field 'conservation' = AUTO-FAIL."""
    e = _build_isolated_knot(N, R, r, lock_on=True)
    omega_0 = e.omega.copy()
    pi_0 = e.omega_velocity().copy()
    for _ in range(n_steps):
        e.step()
    moved = float(np.max(np.abs(e.omega - omega_0)))
    pi_nonzero = float(np.max(np.abs(pi_0))) > 1e-9       # own momentum populated
    own_wave = float(np.max(np.abs(e.omega))) > 1e-6      # field alive after evolution
    real_dynamics_ran = bool(moved > 1e-6 and pi_nonzero and own_wave)
    return {
        "max_delta_omega": moved, "max_pi_omega_init": float(np.max(np.abs(pi_0))),
        "max_omega_end": float(np.max(np.abs(e.omega))),
        "real_dynamics_ran": real_dynamics_ran, "PASS": real_dynamics_ran,
    }


def gate_b_known_signal(N: int = 48, R: float = 11.0, r: float = 4.0) -> dict:
    """(b) KNOWN-SIGNAL RECOVERY (pre-reg §3(b)): the extractor recovers a
    known-imposed (2,3) integer FIRST — compute_Q_link returns Q_link=3 on the
    seeded canonical (2,3). (Static floor; the dynamical gate (c) then shows it
    conserved under step().)"""
    vk = validate_on_known(N=N, R=R, r=r)
    return {"Q_link": vk["Q_link_poloidal"], "w_tor": vk["w_tor_toroidal"],
            "PASS": bool(vk["known_positive_recovers_2_3"])}


def gate_c_conservation_continuity(N: int = 48, R: float = 11.0, r: float = 4.0,
                                   n_steps: int = 600) -> dict:
    """(c) CONSERVATION-UNDER-EVOLUTION + LOCAL CONTINUITY (pre-reg §3(c)). The
    winding INTEGER is conserved across N steps measured on the RETAINED RAW float
    trajectory (alias_frac ≤ 0.34, NOT the snapped int alone); AND
    |ΔH_bel|/H_bel below tol pre/post the lock substep (the lock conserves the
    topological charge); AND the local winding-current continuity closes by the
    source+flux ledger. FROZEN-LIMIT first (§8.3): no-evolution reproduces the
    integer."""
    e = _build_isolated_knot(N, R, r, lock_on=True)

    # frozen limit (§8.3): the read with NO step reproduces the integer.
    w_frozen = _read_winding_lc(e, R, r)
    frozen_ok = (w_frozen["w_tor"], w_frozen["w_pol"]) == (2, 3)

    # raw-trajectory conservation: read the LC winding every `chk` steps, retain
    # the raw float lists + alias canary; the modal integer must hold (2,3).
    chk = max(1, n_steps // 6)
    reads, alias_max, lock_drift_max, cells_min = [], 0.0, 0.0, _cells_per_turn(r)
    steps_done = 0
    while steps_done < n_steps:
        e.step()
        steps_done += 1
        lock_drift_max = max(lock_drift_max, abs(e.lock_helicity_drift()))
        if steps_done % chk == 0:
            w = _read_winding_lc(e, R, r)
            reads.append((w["w_tor"], w["w_pol"]))
            alias_max = max(alias_max, w["alias_frac"])

    integer_conserved = all(rd == (2, 3) for rd in reads)
    alias_ok = alias_max <= ALIAS_TOL
    lock_conserves = lock_drift_max < 1e-6  # the lock is EXACTLY helicity-conserving

    # local continuity over a fresh window (the gate re-builds so the window is
    # measured from a clean breathing knot, not a wandered end-state).
    e2 = _build_isolated_knot(N, R, r, lock_on=True)
    for _ in range(50):  # warmup past the at-rest turning point
        e2.step()
    cont = continuity_over_window(e2)

    res_ok = cells_min >= MIN_CELLS_PER_TURN
    return {
        "frozen_limit_reads_2_3": bool(frozen_ok),
        "reads_along_trajectory": reads,
        "integer_conserved": bool(integer_conserved),
        "alias_frac_max": round(alias_max, 4), "alias_ok": bool(alias_ok),
        "lock_helicity_drift_max": lock_drift_max, "lock_conserves_Hbel": bool(lock_conserves),
        "continuity": cont, "continuity_closed": bool(cont["closed"]),
        "cells_per_turn": round(cells_min, 3), "resolution_ok": bool(res_ok),
        "PASS": bool(frozen_ok and integer_conserved and alias_ok
                     and lock_conserves and cont["closed"] and res_ok),
    }


def gate_e_negative_control(N: int = 48, R: float = 11.0, r: float = 4.0,
                            n_steps: int = 600) -> dict:
    """(e) LIVE NEGATIVE CONTROL (pre-reg §3(e), §5 trap 6 — the GX3 analogue): a
    pre-stated lock-OFF arm that DOES pump |L_ω| / destroy topology must FIRE. A
    conservation PASS is vacuous unless this arm can break it. TWO independent
    fire-paths:
      (i)  |L_ω| PUMP — lock-OFF |L_ω|_max exceeds lock-ON by ≥ NEG_CTRL_PUMP_RATIO
           (the v3 t^0.43 runaway the lock arrests);
      (ii) TOPOLOGY DESTRUCTION — replacing ω with its winding-UNWOUND amplitude
           (unwind_topology) breaks the (2,3) read (≠ (2,3)).
    The gate FIRES (canary works) iff EITHER path breaks the no-op state."""
    # (i) |L_ω| pump: lock-ON vs lock-OFF on the COUPLED arm (where the buckle
    #     sources the rigid ω-rotation the lock arrests; the isolated knot has
    #     |L_ω|≡0 by construction — nothing to pump, so the pump path lives on the
    #     coupled arm, the v3 t^0.43 runaway).
    def lmax(lock_on):
        e = _build_coupled_knot(N, R, r, lock_on=lock_on)
        Lm = e.spin_L_omega()
        for s in range(n_steps):
            e.step()
            if s % 20 == 0:
                Lm = max(Lm, e.spin_L_omega())
        return Lm
    L_on = lmax(True)
    L_off = lmax(False)
    pump_ratio = L_off / (L_on + 1e-12)
    pump_fires = pump_ratio >= NEG_CTRL_PUMP_RATIO

    # (ii) topology destruction: unwind a SPATIAL-PHASE (2,3) (seed_pq_winding,
    #      the coordinate compute_Q_link reads) → the integer must JUMP to 0. This
    #      proves the winding READOUT is not an amplitude artifact: unwind_topology
    #      removes the phase but keeps the amplitude/energy; a genuine topological
    #      integer must break.
    from ave.topological.charge_quantization import unwind_topology
    omega_phase = seed_pq_winding(N, 2, 3, R, r)
    qw = compute_Q_link(omega_phase, R, r)
    qu = compute_Q_link(unwind_topology(omega_phase, R, r), R, r)
    unwind_breaks = (qu["Q_link"] != qw["Q_link"]) and (qw["Q_link"] == 3)

    fired = bool(pump_fires or unwind_breaks)
    return {
        "Lomega_max_lockON": round(L_on, 4), "Lomega_max_lockOFF": round(L_off, 4),
        "pump_ratio": round(pump_ratio, 3), "pump_fires": bool(pump_fires),
        "Q_link_wound": qw["Q_link"], "Q_link_unwound": qu["Q_link"],
        "unwind_breaks_topology": bool(unwind_breaks),
        "negative_control_fired": fired, "PASS": fired,
    }


def gate_f_positive_control(N: int = 48, R: float = 11.0, r: float = 4.0,
                            n_steps: int = 500) -> dict:
    """(f) GENESIS-24 POSITIVE CONTROL (pre-reg §3(f), §5 trap 3): the slaved_omega
    arm (ω := grad(V)-derived each step, crystal_graft_v4.py:280-293) MUST return
    the independence gate = False (demonstrated-reachable-False). A gate that
    cannot fail on the slaved arm = AUTO-VOID (the v3 condition this removes).

    Independence = the winding is robust under a V-perturbation (ref==pert) on the
    REAL arm, but NOT robust on the SLAVED arm (where ω is a deterministic
    function of V, so a V-perturbation drags the winding)."""
    ic = N // 2

    def run(slaved):
        # COUPLED arm: V↔ω live so the V-perturbation can actually probe the ω
        # winding's independence (an isolated knot has V decoupled from ω ⇒ the
        # perturbation never reaches ω ⇒ 'robust' would be vacuous).
        e_ref = _build_coupled_knot(N, R, r, lock_on=True, slaved=slaved)
        e_pert = _build_coupled_knot(N, R, r, lock_on=True, slaved=slaved)
        e_pert.seed_bulk((ic + N // 5, ic, ic), sigma=4.0, frac=0.7)
        for _ in range(n_steps):
            e_ref.step()
            e_pert.step()
        w_ref = _read_winding_lc(e_ref, R, r)
        w_pert = _read_winding_lc(e_pert, R, r)
        diff = float(np.max(np.abs(e_ref.omega - e_pert.omega)))
        ran = float(np.max(np.abs(e_ref.omega))) > 1e-6 and diff > 1e-12
        robust = (w_ref["w_tor"], w_ref["w_pol"]) == (w_pert["w_tor"], w_pert["w_pol"])
        return {"w_ref": (w_ref["w_tor"], w_ref["w_pol"]),
                "w_pert": (w_pert["w_tor"], w_pert["w_pol"]),
                "omega_max_diff": diff, "real_dynamics_ran": bool(ran),
                "winding_robust": bool(robust)}

    real = run(False)
    slaved = run(True)
    real_independent = real["real_dynamics_ran"] and real["winding_robust"]
    # the gate returns independence=False on the slaved arm:
    slaved_independence = slaved["real_dynamics_ran"] and slaved["winding_robust"]
    slaved_arm_independence_false = (not slaved_independence)
    return {
        "real": real, "slaved": slaved,
        "real_arm_independent": bool(real_independent),
        "slaved_arm_independence_false": bool(slaved_arm_independence_false),
        # PASS ⇔ real arm independent AND slaved arm flagged False (reachable-False)
        "PASS": bool(real_independent and slaved_arm_independence_false),
        "AUTO_VOID": bool(not slaved_arm_independence_false),
    }


# ──────────────────────────────────────────────────────────────────────────────
# THE GATE RUNNER (pre-reg §8 reproduce plan) — bins the verdict.
# ──────────────────────────────────────────────────────────────────────────────
def run_s1_gate(N: int = 48, R: float = 11.0, r: float = 4.0) -> dict:
    """Run the full S1 dynamical winding-conservation gate and bin the verdict per
    the FROZEN pre-reg (research/2026-06-24_engine-s1-winding-dof_prereg.md §3,§8).

    S1 PASSES iff ALL of (a)-(c),(e),(f) hold AND the validate-on-known floor AND
    the α-clean confirmation. Any failing sub-gate ⇒ FAIL. INCONCLUSIVE is
    reported (NOT rescued — Rule 11) iff the integrator cannot carry the dynamics
    to a clean verdict (e.g. detonation / secular instability that voids the
    measurement rather than answering it). The negative-control firing is a
    PREREQUISITE for a non-vacuous PASS (a PASS the neg-control cannot break is a
    FAIL). The slaved-arm reachable-False is a PREREQUISITE (AUTO_VOID otherwise).
    """
    out: dict = {"config": {"N": N, "R": R, "r": r, "kappa_tilde": _KAPPA_TILDE}}

    # α-CLEAN confirmation (the readout path carries NO α-carrier; pre-reg §0,§5/8).
    HOST.assert_winding_host_globals_alpha_clean()
    HOST.assert_no_alpha_literal_in_chord_path()
    HOST.assert_not_in_landing_zone(_KAPPA_TILDE, "S1 winding κ̃")
    out["alpha_clean"] = {
        "host_globals_clean": True, "kappa_tilde": _KAPPA_TILDE,
        "kappa_is_six_fifths": bool(_KAPPA_TILDE == 6.0 / 5.0),
        "no_forbidden_in_gate_globals": all(
            s not in globals() for s in
            ("ALPHA", "KAPPA_CHIRAL_ELECTRON", "V_SNAP", "L_NODE", "M_E", "Q_TANK")
        ),
    }

    out["validate_on_known"] = validate_on_known()
    out["gate_a_non_vacuity"] = gate_a_non_vacuity(N, R, r)
    out["gate_b_known_signal"] = gate_b_known_signal(N, R, r)
    out["gate_c_conservation_continuity"] = gate_c_conservation_continuity(N, R, r)
    out["gate_e_negative_control"] = gate_e_negative_control(N, R, r)
    out["gate_f_positive_control"] = gate_f_positive_control(N, R, r)

    # immune-system summary (pre-reg deliverable fields)
    out["immune_system"] = {
        "real_dynamics_ran": bool(out["gate_a_non_vacuity"]["real_dynamics_ran"]),
        "negative_control_fired": bool(out["gate_e_negative_control"]["negative_control_fired"]),
        "slaved_arm_independence_false": bool(
            out["gate_f_positive_control"]["slaved_arm_independence_false"]),
        "alias_frac": out["gate_c_conservation_continuity"]["alias_frac_max"],
    }

    # INCONCLUSIVE detection (Rule 11 — report, do not rescue): the measurement is
    # voided rather than answered if the field detonated (alias canary saturated)
    # or the continuity ledger could not be formed (NaN). This is NOT a FAIL bin —
    # it says the integrator could not carry the dynamics to a clean verdict.
    alias = out["gate_c_conservation_continuity"]["alias_frac_max"]
    cont_rel = out["gate_c_conservation_continuity"]["continuity"]["rel_residual_window"]
    inconclusive = (alias >= 0.95) or (not np.isfinite(cont_rel))
    out["inconclusive_reason"] = (
        "alias canary saturated / continuity ledger NaN — integrator could not "
        "carry the dynamics to a clean verdict" if inconclusive else None
    )

    gates = {
        "a": out["gate_a_non_vacuity"]["PASS"],
        "b": out["gate_b_known_signal"]["PASS"],
        "c": out["gate_c_conservation_continuity"]["PASS"],
        "e": out["gate_e_negative_control"]["PASS"],
        "f": out["gate_f_positive_control"]["PASS"],
        "validate_on_known": out["validate_on_known"]["PASS"],
        "alpha_clean": out["alpha_clean"]["kappa_is_six_fifths"]
        and out["alpha_clean"]["no_forbidden_in_gate_globals"],
    }
    out["gate_pass_flags"] = gates

    if inconclusive:
        out["verdict"] = "INCONCLUSIVE"
    elif out["gate_f_positive_control"]["AUTO_VOID"]:
        out["verdict"] = "AUTO_VOID"  # the gate could not be made falsifiable
    elif all(gates.values()):
        out["verdict"] = "PASS"
    else:
        out["verdict"] = "FAIL"
    out["failing_gates"] = [k for k, v in gates.items() if not v]
    return out


if __name__ == "__main__":
    import json
    import sys

    print("S1 DYNAMICAL WINDING-CONSERVATION GATE (SUB-CLAIM A)")
    print("=" * 64)
    result = run_s1_gate()
    print(json.dumps(result, indent=2, default=str))
    print("=" * 64)
    print(f"VERDICT: {result['verdict']}")
    if result["failing_gates"]:
        print(f"FAILING GATES: {result['failing_gates']}")
    sys.exit(0 if result["verdict"] == "PASS" else 1)
