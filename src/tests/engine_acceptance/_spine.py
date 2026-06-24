"""STAGE 0 — the α-clean spine: the immune-system foundation everything stands on.

Re-scoped Gate 0 (epic `_orchestration/2026-06-23_full-engine-pathway.md`).
Prereg: `research/2026-06-23_engine-stage0-alpha-clean-spine_prereg.md`.

═══════════════════════════════════════════════════════════════════════════════
WHAT THIS MODULE IS (and is NOT)
═══════════════════════════════════════════════════════════════════════════════
The α-CLEAN SPINE = the cold `CrystalEngine` (A1 SCALAR BULK branch ONLY,
`converter_on=False` ⇒ NO (2,3) micro-rotation winding) + the c_eff(V) cage
kernel (`c_eff²=c₀²/S`, `S(A)=√(1−A²)`), in engine-natural (α-FREE) units. It is
the foundation Stages 1–7 extend. Stage 0 erects the foundation + the grid
scaffold ONLY — NO winding, NO cross-sector coupling.

THE ARMED α-LEAK IMMUNE SYSTEM (the reason this stage exists):
  * GUARD TRIAD (import-time): assert ALPHA / Q_TANK / ELECTRON / RHO_BULK are
    NOT reachable in this module's globals — the same triad as
    `graded_vacuum_network.py:111-114`. A leak trips the assert AT LOAD.
  * LITERAL SCRUBBER (source-level): the verdict-determining code path carries
    NO '137' / '0.00729' literal — the same pattern as
    `charge_quantization.py:104`.
  * Q IS MEASURED, NEVER BAKED: the SOLE Q-extractor is `ringdown_Q`
    (`_bulk.py:466`) — a Hilbert-envelope decay fit, Q=ω₀·τ/2, α-FREE by
    construction. The golden-torus α-echo Q=4π³+π²+π≈137
    (`cosserat_field_3d.py:2425`) is EXCLUDED from the dynamical spine: this
    module never imports the cosserat host.

VCA FRAMING (Grant directive — circuit-native):
  The Γ=−1 wall = the impedance short (Z_core→0 as A→1; α-free Z_eff=√S route,
  `resonant-lc-solitons.md:38`). The cage is a BOUNDARY CONDITION (a reflecting
  short), NOT a bulk confining well (substrate-native-check CP10). The resonator
  Q is read by RING-DOWN (envelope decay), never from a closed form.

SUBSTRATE-NATIVE (walked before any code, prereg §):
  * Dynamics : the leapfrog scatter+connect (∂²V/∂t²=c_eff²∇²V) — wave
               propagation, NOT Lagrangian/gradient-descent/energy-min.
  * Sector   : the A1 longitudinal-dilatation SCALAR V-sector (the "mass-3").
               ORTHOGONAL to the transverse photon; the winding is NEVER wired
               into the (V_inc, V_ref) phasor (master-equation.md:20).
  * Coords   : the Q observable is time-domain / spectral (Hilbert envelope of
               ∂_t V, FFT cutoff ω) in real-space — MATCHING the cold-cage
               ring-down corpus claim. NO phase-space φ²/Clifford-torus claim is
               at issue at Stage 0.
  * CP8      : the cold cage is a consistency-class POSIT (not an
               emergence/self-formation test). NO precursor-vs-baseline at
               Stage 0 — that is the genesis track, not the spine.

THE SHARED GRID (named here; the COLLAPSE is Stage 3):
  The K4 node set is the single shared grid TARGET for the full engine. Stage 0
  NAMES it (see `shared_grid_descriptor`) but the Cartesian-∇²V → K4-graph-
  Laplacian (z=3) collapse is the Stage-3 two-grid bridge (the FIRST
  RECONCILIATION MILESTONE), explicitly NOT Stage 0. The cold spine runs on the
  Cartesian leapfrog grid the validated Master-Equation engine already uses.
"""

from __future__ import annotations

import numpy as np

# α-FREE engine-natural inputs ONLY. The spine host (`CrystalEngine`) itself
# imports only NU_VAC, R_II (verified α-free, crystal_engine.py:48); the
# Master-Equation engine imports only numpy. We import the cold cage host + the
# SOLE Q-extractor + the canonical-source check.
from ave.core.crystal_engine import CrystalEngine

from . import _bulk as B

# ─────────────────────────────────────────────────────────────────────────────
# GUARD TRIAD (anti-circularity, import-time) — the SAME triad as
# graded_vacuum_network.py:111-114. A leak trips AT LOAD, not at run.
# ALPHA (=1/Q_TANK) and the ELECTRON instance and the bare RHO_BULK magnitude
# must NOT be reachable in this module's globals.
# ─────────────────────────────────────────────────────────────────────────────
assert "ALPHA" not in globals(), "α-leak: ALPHA must NOT be imported into the spine"
assert "ALPHA_COLD_INV" not in globals(), "α-leak: ALPHA_COLD_INV (=4π³+π²+π≈137) must NOT be imported"
assert "Q_TANK" not in globals(), "α-leak: Q_TANK (=1/α) must NOT be imported into the spine"
assert "ELECTRON" not in globals(), "α-leak: the ELECTRON instance must NOT be imported into the spine"
assert "RHO_BULK" not in globals(), "second-leak: the bare RHO_BULK magnitude must NOT be imported"


# ─────────────────────────────────────────────────────────────────────────────
# THE SHARED GRID (named; the COLLAPSE is Stage 3)
# ─────────────────────────────────────────────────────────────────────────────
def shared_grid_descriptor() -> dict:
    """The single shared grid TARGET for the full engine: the K4 node set.

    Stage 0 NAMES the target and records the present (Stage-0) carrier — the
    Cartesian leapfrog grid the validated Master-Equation engine uses. The
    Cartesian-∇²V → K4-graph-Laplacian (connectivity z=3) COLLAPSE is the
    Stage-3 two-grid bridge (the FIRST RECONCILIATION MILESTONE), NOT Stage 0.
    Returned descriptor is a SCAFFOLD record (no physics is run on it here)."""
    return {
        "target_grid": "K4 node set (single shared grid)",
        "k4_connectivity_z": 3,  # K4 strut count (don't flip 3->4; per-volume cleanup)
        "stage0_carrier": "Cartesian leapfrog (MasterEquation / CrystalEngine bulk)",
        "collapse_milestone": "Stage 3 (two-grid bridge; Cartesian ∇²V -> K4 graph-Laplacian)",
        "stage0_scope": "foundation + grid scaffold ONLY; NO winding, NO coupling",
    }


# ─────────────────────────────────────────────────────────────────────────────
# THE COLD α-CLEAN CAGE on the spine (CrystalEngine BULK branch, converter OFF)
# ─────────────────────────────────────────────────────────────────────────────
def make_lossless_cage(N: int = 32, *, S_min: float = 1e-3, A_cap: float = 0.999) -> CrystalEngine:
    """The genuinely-LOSSLESS cold cage: a CrystalEngine on its A1 SCALAR BULK
    branch ONLY (`converter_on=False` ⇒ NO (2,3) winding — the two-3s guard),
    with NO absorbing channel (`pml_thickness=0` ⇒ energy-conserving reflecting
    boundaries; the damping mask is all-ones). Driven in the LINEAR regime
    (A≪1 ⇒ S=1 ⇒ uniform c₀) as a standing-wave eigenmode, this is a Hermitian
    reactive resonator — no dissipative port ⇒ the ring-down envelope is FLAT
    ⇒ Q=∞ (read honestly by `ringdown_Q`, NEVER baked).

    α-FREE: CrystalEngine imports only NU_VAC, R_II (crystal_engine.py:48); the
    kernel + speeds are α-free dimensionless ratios (ν_vac=2/7, K=2G)."""
    return CrystalEngine(
        N=N, S_min=S_min, A_cap=A_cap, pml_thickness=0, converter_on=False
    )


def seed_linear_standing_eigenmode(
    eng: CrystalEngine, *, mode: int = 2, amp: float = 1e-3
) -> None:
    """Seed a pure standing-wave eigenmode of the box on the BULK V field, in the
    LINEAR regime (amp≪V_yield ⇒ A≪1 ⇒ S=1 ⇒ uniform c₀, NO nonlinear dispersion).
    `V_prev = V` ⇒ the field is at rest at its spatial peak ⇒ a pure
    cosine-in-time standing oscillation. This is the lossless reactive standing
    mode: a perfect LC short, no radiating channel, no dispersion ⇒ flat envelope.

    DISTINCT from the SATURATED cage (A→1): a saturated `pml=0` cage DISPERSES
    (the c_eff(V) gradient spreads the breathing wavepacket) and dephases to a
    FINITE Q — a finite-grid artifact, NOT a leak (see the result doc)."""
    N = eng.N
    i, j, k = np.indices((N, N, N))
    m = int(mode)
    shape = (
        np.sin(np.pi * m * (i + 0.5) / N)
        * np.sin(np.pi * m * (j + 0.5) / N)
        * np.sin(np.pi * m * (k + 0.5) / N)
    )
    eng.V = (amp * shape).astype(np.float64)
    eng.V_prev = eng.V.copy()  # at rest at peak ⇒ pure standing oscillation


def lossless_ringdown_Q(eng: CrystalEngine, *, n_steps: int = 3000, probe=(8, 8, 8)) -> dict:
    """Evolve the seeded lossless cage and read its ring-down Q via the SOLE
    extractor `ringdown_Q` (`_bulk.py:466`). Records ∂_t V (the L-state of the
    bulk reactance pair, CP6) at an antinode probe, extracts the FFT cutoff ω₀,
    then the Hilbert-envelope decay → Q. α-FREE: no Q_TANK, no ELECTRON, no
    closed-form; Q is MEASURED.

    ⚑ HONEST FINDING (flag-don't-fix; recorded in the result doc): on a FINITE
    leapfrog grid the time-domain ring-down of a *standing* cage is NOT exactly
    flat — the continuum-seeded mode is not the exact DISCRETE eigenmode, so it
    beats/disperses slightly, and `ringdown_Q`'s slope-sign branch is knife-edge
    near zero slope. So this read returns a LARGE-but-window-sensitive Q (∞ in
    the flat limit, O(50) at longer windows). It is the CORROBORATING witness; the
    RIGOROUS, tuning-independent lossless Q=∞ lives in the EIGENFRAME
    (`eigenframe_lossless_Q`, the closed-port Hermitian Im(ω)=0 ⇒ Q=∞ property,
    corpus GATE2). The finite-grid time-domain ring-down giving a FINITE Q is
    corpus-named, NOT a leak (`test_graded_vacuum_network_isolation.py:21`)."""
    p = tuple(int(x) for x in probe)
    dV = np.empty(n_steps, dtype=np.float64)
    for n in range(n_steps):
        v0 = float(eng.V[p])
        eng.step()
        dV[n] = (float(eng.V[p]) - v0) / eng.dt
    ev = B.cutoff_eigenfrequency(eng, dV)
    omega0 = ev["omega_cutoff"]
    rd = B.ringdown_Q(eng, dV, omega0)
    Q = rd["Q_ringdown"]
    # robust loss-floor: 1/Q is the per-radian amplitude-loss; ≈0 ⇒ lossless.
    inv_Q = 0.0 if not np.isfinite(Q) else (1.0 / Q if Q != 0 else float("inf"))
    return {
        "omega_cutoff": float(omega0),
        "tau": rd["tau"],
        "Q_ringdown": Q,
        "inv_Q": float(inv_Q),
        "is_lossless_inf": (not np.isfinite(Q)),
        "zero_crossings": int(ev["zero_crossings"]),
    }


def eigenframe_lossless_Q(N: int = 24, *, frac: float = 0.9, S_min: float = 1e-3) -> dict:
    """The RIGOROUS, tuning-independent lossless witness: the closed-port
    Hermitian eigenframe. With the EM port CLOSED (Γ_EM=−1, fully confined) the
    isolation operator is Hermitian ⇒ Im(ω)=0 ⇒ Q=∞ — the lossless reactive
    standing-mode limit (corpus GATE2, `test_graded_vacuum_network_isolation.py:92`).
    α-FREE: `solve_isolation_Q_sparse` reads no Q_TANK / ELECTRON.

    This is the substrate-native statement of 'lossless': a perfectly reflecting
    Γ=−1 boundary stores energy and dissipates none ⇒ the resonator Q is infinite.
    It is the EIGENFRAME complement to the time-domain ring-down — the two are
    DIFFERENT observables (the corpus is explicit, :16-24), and the eigenframe is
    the one that carries the intrinsic lossless Q=∞ without finite-grid dephasing."""
    # Imported HERE (function-local) so the closed-port eigensolver — which is
    # itself α-guarded at its own module load (graded_vacuum_network.py:111-114) —
    # is reachable for the witness WITHOUT putting any α-carrier in the spine.
    from ave.solvers.graded_vacuum_network import IsolationConfig, solve_isolation_Q_sparse

    cfg = IsolationConfig(
        N=N, sigma=N / 9.0, exponent=0.5, port_thickness=max(3, N // 12),
        em_port_closed=True, frac=frac, S_min=S_min, sigma_port=2.0,
    )
    r = solve_isolation_Q_sparse(cfg, omega_guess=2.87)
    return {
        "Q": float(r["Q"]),
        "omega_im": float(r["omega_im"]),
        "omega_re": float(r["omega_re"]),
        "is_lossless": (r["omega_im"] < 1e-10 and r["Q"] > 1e9),
    }


# ─────────────────────────────────────────────────────────────────────────────
# LITERAL SCRUBBER (source-level) — the SAME pattern as charge_quantization.py:104.
# The verdict-determining spine code path carries NO α-numeral literal.
# ─────────────────────────────────────────────────────────────────────────────
_FORBIDDEN_VALUE_LITERALS = ("137", "0.00729")


def assert_no_alpha_literal_in_spine() -> None:
    """Read this module's verdict-determining functions' source and assert the
    α-numeral literals ('137' / '0.00729') are ABSENT. Any α-numeral hardcoded
    into the Q-read would be the echo; the spine is α-FREE by construction."""
    import inspect

    src = (
        inspect.getsource(make_lossless_cage)
        + inspect.getsource(seed_linear_standing_eigenmode)
        + inspect.getsource(lossless_ringdown_Q)
        + inspect.getsource(shared_grid_descriptor)
    )
    for lit in _FORBIDDEN_VALUE_LITERALS:
        assert lit not in src, (
            f"VALUE-ECHO IMMUNITY violation: α-literal '{lit}' found in the spine "
            f"verdict-determining code path — the Q-read must be α-free."
        )


def assert_spine_globals_alpha_clean() -> None:
    """Runtime re-assert of the import-time guard triad: confirm no α-carrier
    leaked into the spine engine modules' globals OR this module's globals.
    Belt-and-suspenders for the load-time asserts above."""
    import ave.core.crystal_engine as _ce
    import ave.core.master_equation_fdtd as _me

    forbidden = ("ALPHA", "ALPHA_COLD_INV", "Q_TANK", "ELECTRON", "RHO_BULK")
    for mod, name in ((_ce, "crystal_engine"), (_me, "master_equation_fdtd"), (None, "_spine")):
        ns = globals() if mod is None else vars(mod)
        for sym in forbidden:
            assert sym not in ns, (
                f"α-leak: forbidden symbol '{sym}' reachable in {name} globals — "
                f"the dynamical spine must carry NO α-carrier."
            )

