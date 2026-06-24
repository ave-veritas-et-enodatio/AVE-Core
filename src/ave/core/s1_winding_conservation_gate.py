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
