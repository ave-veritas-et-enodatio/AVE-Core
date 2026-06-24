"""L0 (engine RE-ROUTE) — the α-STRIPPED WINDING HOST.

The de-risked host for the (2,3) winding DOF chord path. The re-route's chord
program (S1→S4, `_orchestration/2026-06-24_engine-reroute-pathway.md`) decides
chord-vs-echo at S4 via an α-FREE dimensionless ratio. That verdict is only
meaningful if the host carrying the winding DOF is α-FREE. This module IS that
α-clean host.

ORIGIN — the re-route audit found the natural winding host,
`src/ave/topological/cosserat_field_3d.py`, α-CONTAMINATED on the readout path:
  * `:56`   `from ave.core.constants import ALPHA, V_SNAP`
  * `:115`  `def kappa_chiral_from_topology(p, q, alpha: float = ALPHA)`  (default-arg ALPHA)
  * `:131`  `KAPPA_CHIRAL_ELECTRON = ALPHA * KAPPA_TILDE_ELECTRON`  (the α-baked factor)
  * `:2422` `extract_quality_factor` → 16π³(R·r)+4π²(R·r)+π·d = 137.036304 at R·r=¼
            (= a closed-form α⁻¹, in the 117–157 band, NOT a measured ring-down)

This is the SAME hazard the original Gate 0 (PR #394) HARD-STOPPED on. The fix
is NOT to strip the shared `cosserat_field_3d.py` in place (its α-baked symbols
are legitimately used by α-aware callers) but to stand up THIS α-stripped host,
which SELECTIVELY imports ONLY the α-FREE cosserat symbols and carries the
ported guard triad. Identical pattern to `graded_vacuum_network.py:100-114`.

WHAT IS ON THE CHORD PATH (α-FREE, by selective import):
  * KAPPA_TILDE_ELECTRON  (= 6/5 = 1.2, the α-FREE (2,3) winding factor; :94)
  * the NATIVE K4 stencil:  tetrahedral_gradient, adjoint_tetrahedral_divergence,
                            TETRA_OFFSETS  (NO Cartesian 7-pt Laplacian; HR1)

WHAT IS *FORBIDDEN* (never imported / never reached on the chord path):
  ALPHA, ALPHA_COLD_INV, Q_TANK, ELECTRON, RHO_BULK, V_SNAP,
  KAPPA_CHIRAL_ELECTRON (=α·κ̃), kappa_chiral_from_topology (default-arg ALPHA),
  extract_quality_factor (the baked-137 golden-torus Q-form).

⚑ COORDINATE-CATEGORY CAVEAT (load-bearing): this host carries the (2,3) winding
   factor κ̃ — a PHASE-SPACE Clifford-torus quantity. It does NOT touch the
   real-space 720° SU(2) spin-½ DOF on the unknot BODY. These are TWO DIFFERENT
   "2"s; conflating them is the (2)×(2)=4 double-count. Keep them separate.

CLASSIFICATION (consistency-vs-emergence): Class A — identity/foundation. The
guard asserts ARE the immune system (structural, not predictive). NO chord, NO
α-readout, NO Q-derivation here. The Q=137 slot stays EMPTY (gate wmighcz1z,
anti-substitution).
"""

from __future__ import annotations

import inspect

import numpy as np

# ─────────────────────────────────────────────────────────────────────────────
# SELECTIVE IMPORT — ONLY the α-FREE cosserat symbols reach the chord path.
# `from X import name` binds ONLY `name`; ALPHA / KAPPA_CHIRAL / the 137-Q form
# do NOT enter this module's globals (verified 2026-06-24). This is the same
# selective-import precedent `graded_vacuum_network.py:100-105` relies on.
# ─────────────────────────────────────────────────────────────────────────────
from ave.topological.cosserat_field_3d import (
    KAPPA_TILDE_ELECTRON,  # = 6/5, α-FREE electron (2,3) torus factor (:94)
    TETRA_OFFSETS,  # the native K4 diamond stencil offsets
    adjoint_tetrahedral_divergence,  # native K4 adjoint divergence
    tetrahedral_gradient,  # native K4 gradient
)

# ─────────────────────────────────────────────────────────────────────────────
# IMPORT-GUARD TRIAD (anti-circularity, HARD-STOP). PORTED VERBATIM-IN-PATTERN
# from graded_vacuum_network.py:108-114 (the proven-LIVE precedent). These run
# at MODULE LOAD: if an α-carrier had leaked into this host's globals, importing
# this module would FAIL HERE — the leak is the signal (do NOT patch around it).
# ─────────────────────────────────────────────────────────────────────────────
assert "ALPHA" not in globals(), "α-leak: ALPHA must NOT be imported into the winding host"
assert "ALPHA_COLD_INV" not in globals(), "α-leak: ALPHA_COLD_INV (=4π³+π²+π≈137) must NOT be imported"
assert "Q_TANK" not in globals(), "α-leak: Q_TANK (=1/α) must NOT be imported into the winding host"
assert "ELECTRON" not in globals(), "α-leak: the ELECTRON instance must NOT be imported into the winding host"
assert "RHO_BULK" not in globals(), "second-leak: the bare RHO_BULK magnitude must NOT be imported"
assert "V_SNAP" not in globals(), "α-leak: V_SNAP (=m_e c²/e, routes through m_e) must NOT be on the chord path"
assert "KAPPA_CHIRAL_ELECTRON" not in globals(), "α-leak: KAPPA_CHIRAL_ELECTRON (=α·κ̃) must NOT be imported — use κ̃=6/5"
assert "kappa_chiral_from_topology" not in globals(), "α-leak: kappa_chiral_from_topology (default-arg ALPHA) must NOT be imported"
assert "extract_quality_factor" not in globals(), "α-leak: the baked-137 golden-torus Q-form must NOT be on the chord path"

# The literal-scrubber forbidden numerals (the α value echoes).
_FORBIDDEN_VALUE_LITERALS = ("137", "0.00729")
# The α-leak landing zone: a chord-path numeric here would be an α⁻¹ echo.
_LANDING_ZONE = (117.0, 157.0)


# ─────────────────────────────────────────────────────────────────────────────
# THE CHORD-PATH WINDING FACTOR (α-FREE).
# ─────────────────────────────────────────────────────────────────────────────
def winding_kappa_tilde(p: int = 2, q: int = 3) -> float:
    """The α-FREE (p,q) winding factor κ̃ for the chord path.

    For the electron (2,3) winding this returns κ̃ = 6/5 (= KAPPA_TILDE_ELECTRON,
    `cosserat_field_3d.py:94`). It does NOT route through ALPHA — there is NO
    α-multiply (the α-baked KAPPA_CHIRAL_ELECTRON = α·κ̃ is FORBIDDEN here).

    This is the ONLY winding-amplitude scalar the chord path is permitted to use.
    """
    if (p, q) == (2, 3):
        return float(KAPPA_TILDE_ELECTRON)  # = 6/5, α-FREE
    # General α-free torus factor (NO α-multiply). Mirrors the α-free shape of
    # cosserat_field_3d.kappa_tilde_torus, kept local to avoid pulling the
    # α-aware module attributes into scope.
    return float(q) / float(p) * (4.0 / 5.0) if p else float("nan")


def native_k4_laplacian(field: np.ndarray) -> np.ndarray:
    """The substrate-native K4 (tetrahedral / diamond) scalar Laplacian:
        L = adjoint_tetrahedral_divergence( tetrahedral_gradient(field) ).
    Uses ONLY the K4 diamond stencil (TETRA_OFFSETS, 4 diagonals) — the Cartesian
    7-pt Laplacian is FORBIDDEN (HR1) and never called. α-FREE (the stencil
    carries no calibration constant). Identical construction to
    graded_vacuum_network._native_scalar_laplacian.
    """
    return adjoint_tetrahedral_divergence(tetrahedral_gradient(field))


# ─────────────────────────────────────────────────────────────────────────────
# THE GUARD HELPERS (runtime re-assert + the literal scrubber). Mirror
# _spine.assert_spine_globals_alpha_clean / assert_no_alpha_literal_in_spine.
# ─────────────────────────────────────────────────────────────────────────────
def assert_winding_host_globals_alpha_clean() -> None:
    """Runtime re-assert of the import-time triad: no α-carrier reachable in THIS
    host's globals NOR in the cosserat module's namespace *as reached through this
    host's chord path*. Belt-and-suspenders for the load-time asserts above.

    We check (a) this host's own globals (the selective import must not have
    pulled a carrier in), and (b) that the cosserat module's α-carriers, while
    they exist in THAT module, are NOT bound names in THIS host (the chord path
    cannot name them).
    """
    forbidden = (
        "ALPHA",
        "ALPHA_COLD_INV",
        "Q_TANK",
        "ELECTRON",
        "RHO_BULK",
        "V_SNAP",
        "KAPPA_CHIRAL_ELECTRON",
        "kappa_chiral_from_topology",
        "extract_quality_factor",
    )
    g = globals()
    for sym in forbidden:
        assert sym not in g, (
            f"α-leak: forbidden symbol '{sym}' reachable in the winding-host globals — "
            f"the chord path must carry NO α-carrier (use κ̃=6/5, never α·κ̃; "
            f"never the baked-137 golden-torus Q-form)."
        )


def assert_no_alpha_literal_in_chord_path() -> None:
    """Read the chord-path verdict-determining functions' source and assert the
    α-numeral literals ('137' / '0.00729') are ABSENT. Any α-numeral hardcoded
    onto the chord path would be the echo; the chord path is α-FREE by
    construction."""
    # Scrub ONLY the NUMERICAL chord-path functions (the verdict-determining
    # value path). The guard helpers themselves legitimately *name* '137' in
    # their error messages to explain what is forbidden — they are NOT on the
    # value path (same scoping the Stage-0 precedent uses, _spine.py:228-234).
    src = (
        inspect.getsource(winding_kappa_tilde)
        + inspect.getsource(native_k4_laplacian)
    )
    for lit in _FORBIDDEN_VALUE_LITERALS:
        assert lit not in src, (
            f"VALUE-ECHO IMMUNITY violation: α-literal '{lit}' found in the winding-host "
            f"chord-path code — the chord path must be α-free."
        )


def assert_not_in_landing_zone(value: float, what: str = "chord-path numeric") -> None:
    """A chord-path numeric landing in the 117–157 α-leak band would be an α⁻¹
    echo (1/α ≈ 137.036). Assert it does NOT."""
    lo, hi = _LANDING_ZONE
    assert not (lo < float(value) < hi), (
        f"α-leak landing-zone HARD-STOP: {what} = {value} landed in the {lo}–{hi} band "
        f"(1/α ≈ 137.036 lives here). The chord path must NOT reproduce α⁻¹."
    )
