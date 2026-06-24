"""STAGE 1 — the 2 TRANSVERSE DOF: wave-typed constitutive helpers + α-guard.

Epic `_orchestration/2026-06-23_full-engine-pathway.md` Stage 1.
Prereg: `research/2026-06-23_engine-stage1-transverse-modes_prereg.md`.

═══════════════════════════════════════════════════════════════════════════════
WHAT THIS MODULE IS (and is NOT)
═══════════════════════════════════════════════════════════════════════════════
The 2 transverse DOF (the srs vector field's 2 polarizations) carry BOTH the
EM-transverse PHOTON (ε,μ modulus → c_EM=c₀/S) AND the transverse SHEAR/GW
(G modulus → c_shear=c₀·√S). At S=1 (cold) these are DEGENERATE at c₀; the split
is DRIVEN-only. This module provides the WAVE-TYPED constitutive speeds — each
keyed by WHICH MODULUS responds — so the twice-conflated c_EM↔c_shear category
error (`ave-kb/CLAUDE.md:71`) cannot recur.

THE THREE LIVE INDICES (canonical taxonomy, ave-kb/CLAUDE.md:79-80, clm-8nkvwy):
  * n_EM PHASE  = S       → c_EM   = c₀/S    (Maxwell phase velocity; the α-speed)
  * n_EM GROUP  = √S      → c_group= c₀·√S   (optical/birefringence SIGNAL index)
  * n_shear     = 1/√S    → c_shear= c₀·√S   (Shapiro/gravitational; reciprocal of n_EM_group)
A single scalar CANNOT serve all three. The driven smoke-check reads the PHASE
constitutive for c_EM (ε,μ) and the canonical √S identity for c_shear (G) — NEVER
one substituted for the other.

α-CLEAN: this module + the Stage-1 code path import ONLY α-free constants
(EPSILON_0, MU_0, Z_0, C_0). The driven c_EM split routes through the α-clean
`_em_media.em_params` (imports only those four), NOT `chiral_lattice_vector_sat`
(which imports ALPHA :15 — the genesis self-lock engine, NAMED out-of-scope; see
the guard-triad extension below + the prereg S1.3 flag).
"""

from __future__ import annotations

import numpy as np

# α-FREE constants ONLY (ave-canonical-source). NEVER import ALPHA into the engine.
from ave.core.constants import EPSILON_0, MU_0, Z_0, C_0  # noqa: F401  (Z_0 used by callers/gate)

# the α-clean EM varactor (imports only EPSILON_0/MU_0/Z_0/C_0) — the matching
# IMPEDANCE-PLANE substrate for the driven c_EM PHASE constitutive.
from . import _em_media as EM


# ─────────────────────────────────────────────────────────────────────────────
# GUARD TRIAD EXTENSION (import-time) — the SAME triad as the Stage-0 spine
# (_spine.py:76-80) and graded_vacuum_network.py:111-114, now covering the
# transverse/srs code path. A leak trips AT LOAD.
# ─────────────────────────────────────────────────────────────────────────────
assert "ALPHA" not in globals(), "α-leak: ALPHA must NOT be imported into the transverse module"
assert "ALPHA_COLD_INV" not in globals(), "α-leak: ALPHA_COLD_INV (≈137) must NOT be imported"
assert "Q_TANK" not in globals(), "α-leak: Q_TANK (=1/α) must NOT be imported into the transverse module"
assert "ELECTRON" not in globals(), "α-leak: the ELECTRON instance must NOT be imported"
assert "RHO_BULK" not in globals(), "second-leak: the bare RHO_BULK magnitude must NOT be imported"


# ─────────────────────────────────────────────────────────────────────────────
# WAVE-TYPED constitutive speeds (each keyed by WHICH MODULUS responds)
# ─────────────────────────────────────────────────────────────────────────────
def S_of_A(A) -> np.ndarray:
    """Canonical Axiom-4 kernel S(A) = √(1 − A²) (constants.py:46). Sub-yield only
    (A < 1, Regime I/II); floored for numerical safety near the wall."""
    A = np.asarray(A, dtype=float)
    return np.sqrt(np.maximum(1e-12, 1.0 - A * A))


def c_em_phase_over_c0(A):
    """EM-transverse PHOTON phase velocity ratio c_EM/c₀ = 1/S (RISES above 1 as
    A→1). Keyed by the ε,μ moduli (the SYM varactor): the α-bearing optical
    channel. Read via the α-clean impedance-plane varactor `em_params` at SYM
    loading (S_eps = S_mu = S) so the wave-typing is the REAL constitutive, not a
    bare algebraic restatement.

    c_EM = 1/√(μ_eff·ε_eff) = c₀/√(S_μ·S_eps) = c₀/S at SYM. n_EM_phase = c₀/c_EM = S."""
    A = np.asarray(A, dtype=float)
    p = EM.em_params(A, A)  # SYM loading: both ε and μ sectors scale by S(A)
    return p["c_EM"] / C_0  # = 1/S


def c_shear_over_c0(A):
    """Transverse SHEAR / GW phase velocity ratio c_shear/c₀ = √S (FALLS below 1 as
    A→1; freezes the matter/gravitational clock). Keyed by the G (deviatoric)
    modulus — the canonical matter-clock identity c_shear = c₀·√S = c₀·(1−A²)^(1/4)
    (invariant-gravitational-impedance.md:30; the same curve in kernel-base √S vs
    amplitude-base (1−A²)^(1/4)). This is the CONSTITUTIVE IDENTITY at the operating
    point; the saturated G-modulus DYNAMICAL engine that propagates it is Stage 4."""
    return S_of_A(A) ** 0.5  # = √S


def n_em_phase(A):
    """n_EM PHASE = c₀/c_EM = S (the Maxwell phase index; the α-speed). DISTINCT
    from the GROUP index √S off S=1."""
    return C_0 / EM.em_params(np.asarray(A, dtype=float), np.asarray(A, dtype=float))["c_EM"]


def n_em_group(A):
    """n_EM GROUP = √S (the optical/birefringence SIGNAL index; master_equation_fdtd
    .n_em_index). The ray/bending observable, NOT the phase index."""
    return S_of_A(A) ** 0.5


def n_shear(A):
    """n_shear = 1/√S (the Shapiro/gravitational ray-bending index; the RECIPROCAL
    of n_EM_group). master_equation_fdtd.n_shear_index."""
    return S_of_A(A) ** (-0.5)


# ─────────────────────────────────────────────────────────────────────────────
# canonical-source verification (ave-canonical-source Step 4)
# ─────────────────────────────────────────────────────────────────────────────
def assert_canonical_constants() -> None:
    """Fail loudly if ave.core.constants is not the worktree's canonical source."""
    import ave.core.constants as _avc

    assert _avc.__file__.endswith("ave/core/constants.py"), (
        f"ave.core.constants is not the AVE-Core canonical source: {_avc.__file__}"
    )


def assert_transverse_path_alpha_clean() -> None:
    """Runtime re-assert of the guard triad over the Stage-1 transverse code path.

    Asserts no α-carrier (ALPHA / ALPHA_COLD_INV / Q_TANK / ELECTRON / RHO_BULK) is
    reachable in THIS module's globals, in `_em_media`'s globals (the driven-split
    substrate), or in `chiral_lattice_vector`'s globals (the srs vector engine).

    ⚑ NAMED out-of-scope contaminant (flag-don't-fix; prereg S1.3): the SATURATED
    genesis engine `chiral_lattice_vector_sat` imports ALPHA (:15). It is NOT in
    the Stage-1 transverse wave-typing path (the driven smoke-check uses the α-clean
    `_em_media.em_params`). This function records the `_sat` α-import as a named
    Stage-4-blocking contaminant WITHOUT failing Stage 1 — Stage 4 (the saturated
    c_shear dynamics) must clean it before hosting the dynamical shear mode. The
    Stage-1 path is verified α-clean here.
    """
    from . import _em_media as _emm
    from . import _transverse as _self
    import ave.core.chiral_lattice_vector as _clv

    forbidden = ("ALPHA", "ALPHA_COLD_INV", "Q_TANK", "ELECTRON", "RHO_BULK")
    for mod, name in (
        (_self, "_transverse"),
        (_emm, "_em_media"),
        (_clv, "chiral_lattice_vector"),
    ):
        for sym in forbidden:
            assert sym not in vars(mod), (
                f"α-leak: forbidden symbol '{sym}' reachable in {name} globals — "
                f"the Stage-1 transverse wave-typing path must carry NO α-carrier."
            )


def sat_engine_alpha_import_is_out_of_scope() -> dict:
    """Record (NOT assert away) the KNOWN α-import in the saturated genesis engine.

    `chiral_lattice_vector_sat.py:15` does `from ave.core.constants import ALPHA,
    R_I`. This is the Phase-2 self-lock engine, NOT the Stage-1 transverse path.
    Returns the named contaminant record so the gate can SURFACE it (flag-don't-fix)
    as a Stage-4-blocking item, without rewriting `_sat` (out of Stage-1 scope)."""
    import ave.core.chiral_lattice_vector_sat as _sat

    has_alpha = "ALPHA" in vars(_sat)
    return {
        "module": "ave.core.chiral_lattice_vector_sat",
        "imports_alpha": bool(has_alpha),
        "in_stage1_path": False,  # the driven smoke-check does NOT use _sat
        "blocks_stage": 4,        # Stage 4 (saturated c_shear dynamics) must clean it
        "note": (
            "genesis self-lock engine imports ALPHA :15; out of Stage-1 scope "
            "(Stage-1 driven split uses the α-clean _em_media.em_params); "
            "Stage 4 must clean before hosting the dynamical shear mode."
        ),
    }
