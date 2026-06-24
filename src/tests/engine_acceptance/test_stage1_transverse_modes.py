"""STAGE 1 — the 2 TRANSVERSE DOF: photon (c_EM=c₀/S) + shear (c_shear=c₀·√S)
on the chiral srs grid. The 2 transverse modes wave-typed; the foundation Stage 4
(saturated G-modulus dynamics) inherits.

Epic:  `_orchestration/2026-06-23_full-engine-pathway.md` Stage 1
Prereg: `research/2026-06-23_engine-stage1-transverse-modes_prereg.md` (FROZEN pre-run)
Result: `research/2026-06-23_engine-stage1-transverse-modes_result.md`
Stacks on: Stage 0 (`analysis/engine-stage0-alpha-clean-spine`, PR #399 — not yet on main).

════════════════════════════════════════════════════════════════════════════════
STAGE 1 FROZEN-BIN OUTCOMES (BRUTAL HONESTY — Rule 11)
════════════════════════════════════════════════════════════════════════════════
  T1.6  the 2-DOF transverse field is LOSSLESS on the spine (cold, S=1):  RE-CONFIRM.
        Inherited gate (test_l1_multiwave.py:154); re-run here to confirm green on
        the Stage-1 worktree. At S=1 c_EM=c_shear=c₀ (DEGENERATE) — the foundation
        property; the split is DRIVEN-only.
  S1.1  the 2 modes SPLIT the RIGHT way off S=1 (driven smoke-check):  the substance.
        As A rises (S falls below 1): c_EM/c₀=1/S RISES > 1; c_shear/c₀=√S FALLS < 1.
        Opposite directions, monotonic — they diverge from the c₀ degeneracy. The
        wave-typing is wired: c_EM reads the ε,μ PHASE constitutive, c_shear reads
        the G √S identity (DIFFERENT moduli). NOT the full near-yield validation
        (Stage 4) — the sub-yield sanity check that the 2 modes are genuinely
        distinct + wave-typed. STOP-and-report if they don't split or split wrong.
  S1.2  the THREE indices are PINNED, the legacy alias is HARD-SCOPED:  CONSISTENCY.
        n_EM_group=√S, n_shear=1/√S (exact reciprocals); refractive_index() is
        n_em_index() on BOTH engines (the alias holds); n_EM_phase=S is DISTINCT
        from √S off S=1. The wave-typing cannot silently swap → Stage 4 cannot
        re-conflate c_EM/c_shear.
  S1.3  the α-GUARD TRIAD covers the transverse/srs modules:  PASS.
        ALPHA/ALPHA_COLD_INV/Q_TANK/ELECTRON/RHO_BULK absent from the Stage-1 code
        path (_transverse / _em_media / chiral_lattice_vector). STRUCTURAL chirality
        ON (lossless optical-activity rotation, Axiom-3); the α-dressed
        ETA_ROT_PER_WRITHE NOT inherited as a bankable scale. ⚑ the saturated
        genesis engine `_sat` imports ALPHA (:15) — NAMED out-of-scope Stage-4
        contaminant, recorded not silently fixed.

PASS  = T1.6 green + the 2 modes split the right way + indices pinned + guards extended.
STOP  = the modes don't split / split the WRONG way (wave-typing broken) OR any
        α re-leak in the Stage-1 path. Report it — do NOT patch around it.

CLASSIFICATION (consistency-vs-emergence — Stage 1 is CONSISTENCY, NO chord):
  T1.6/S1.1 = Class-C consistency (lossless propagation + the canonical wave-speed
  identities reproduced). S1.2/S1.3 = Class-A identity/foundation (structural pins;
  the guard asserts ARE the immune system). NO Class-D emergence / chord anywhere.

CI partition: this file is a fast keeper (T1.6 ~2s; S1.1/S1.2 desk-calc on the
α-clean varactor + index identities; S1.3 import-time asserts). No heavy eigensolve
/ genesis driver ⇒ stays in the GATING lane (NOT engine_sim).
"""

from __future__ import annotations

import numpy as np
import pytest

# Importing `_transverse` EXECUTES its load-time guard triad (the asserts at module
# body). If an α-carrier had leaked into the transverse path, THIS IMPORT would fail.
from . import _transverse as TX
from .test_l1_multiwave import test_t1_6_transverse_shear_wave as _t1_6


# ─────────────────────────────────────────────────────────────────────────────
# T1.6 — RE-CONFIRM the inherited cold (S=1) lossless 2-DOF gate on the spine.
# ─────────────────────────────────────────────────────────────────────────────
def test_T1_6_lossless_two_dof_transverse_on_spine():
    """RE-CONFIRM (pinned): the 2-DOF transverse field propagates LOSSLESSLY on
    the Stage-1 worktree spine (drift<1e-8, dispersion<0.05, |c|/c_net±5%,
    transverse_dof==2). Delegates to the frozen T1.6 gate (test_l1_multiwave.py).
    At S=1 the photon and shear are DEGENERATE at c₀ — the foundation property the
    driven split (S1.1) then breaks."""
    _t1_6()  # the frozen gate; raises on any regression


# ─────────────────────────────────────────────────────────────────────────────
# S1.1 — DRIVEN SMOKE-CHECK: do the 2 modes split the RIGHT way off S=1?
# ─────────────────────────────────────────────────────────────────────────────
def test_S1_1_driven_split_em_rises_shear_falls():
    """S1.1 [consistency — the substance]: as the medium is driven below S=1, the
    EM-transverse PHOTON (c_EM=c₀/S) RISES above c₀ while the transverse SHEAR
    (c_shear=c₀·√S) FALLS below c₀ — they diverge from the cold c₀ degeneracy in
    OPPOSITE directions. This confirms the 2 modes are genuinely DISTINCT and the
    wave-typing is wired (c_EM ← ε,μ PHASE constitutive; c_shear ← G √S identity;
    DIFFERENT moduli, never substituted).

    REGIME (ave-regime-phase-state-check): MODE = 2 transverse DOF (BOTH channels);
    REGIME = sub-yield linear→weak (A ≤ 0.6, below near-yield r₂=0.866); PHASE-STATE
    = weakly-loaded. The observable is a SCALAR ⟨S⟩-deficit propagation-speed shift
    → achromatic-compatible, EXISTS in every regime (NOT the rate-asymmetry/∮≠0
    near-yield trap). Well-posed as a sub-yield sanity check.

    SCOPE: NOT the full near-yield √S-shear validation (Stage 4 — the saturated
    G-modulus dynamical engine). c_shear here is the CONSTITUTIVE IDENTITY c₀·√S at
    the operating point; Stage 4's dynamical engine must reproduce it.

    PRE-REGISTERED BINS (frozen): PASS = at A=0 degenerate (within 1e-9); c_EM
    monotonic-up, c_shear monotonic-down as A rises; split opposite-direction.
    STOP = no split / wrong direction / both read the same form (wave-typing broken).
    """
    TX.assert_canonical_constants()
    A = np.array([0.0, 0.2, 0.4, 0.6])
    c_em = np.asarray(TX.c_em_phase_over_c0(A), dtype=float)      # ε,μ PHASE constitutive
    c_sh = np.asarray(TX.c_shear_over_c0(A), dtype=float)         # G √S identity
    S = TX.S_of_A(A)

    print("\n--- S1.1 driven split (sub-yield smoke-check; NOT the Stage-4 validation) ---")
    print("   A      S       c_EM/c₀=1/S (ε,μ; RISES)   c_shear/c₀=√S (G; FALLS)")
    for a, s, ce, cs in zip(A, S, c_em, c_sh):
        print(f"  {a:.2f}   {s:.4f}        {ce:.5f}                  {cs:.5f}")

    # (a) cold degeneracy: at A=0 (S=1) both modes are c₀.
    assert abs(c_em[0] - 1.0) < 1e-9 and abs(c_sh[0] - 1.0) < 1e-9, (
        f"S1.1 STOP: not degenerate at S=1 — c_EM={c_em[0]}, c_shear={c_sh[0]}"
    )
    # (b) the split: c_EM RISES strictly above 1, c_shear FALLS strictly below 1.
    assert np.all(np.diff(c_em[1:]) > 0) and c_em[-1] > 1.0 + 1e-6, (
        f"S1.1 STOP: c_EM did NOT rise (wave-typing broken) — c_EM/c₀={c_em}"
    )
    assert np.all(np.diff(c_sh[1:]) < 0) and c_sh[-1] < 1.0 - 1e-6, (
        f"S1.1 STOP: c_shear did NOT fall (wave-typing broken) — c_shear/c₀={c_sh}"
    )
    # (c) opposite directions: they diverge from c₀ (the product of the deviations
    #     from 1 is negative everywhere off S=1).
    off = A > 0
    assert np.all((c_em[off] - 1.0) * (c_sh[off] - 1.0) < 0), (
        f"S1.1 STOP: modes did NOT split in OPPOSITE directions — "
        f"c_EM/c₀={c_em}, c_shear/c₀={c_sh}"
    )
    # (d) wave-typing wired: the two speeds read DIFFERENT moduli — c_EM=1/S and
    #     c_shear=√S are NOT equal off S=1 (the conflation would make them equal).
    assert np.all(np.abs(c_em[off] - c_sh[off]) > 1e-3), (
        f"S1.1 STOP: c_EM and c_shear read the SAME form off S=1 — the c_EM↔c_shear "
        f"category error (ave-kb/CLAUDE.md:71). c_EM={c_em}, c_shear={c_sh}"
    )
    # (e) numeric anchor: c_EM=1/S and c_shear=√S to the canonical forms.
    assert np.allclose(c_em, 1.0 / S, rtol=1e-9), "c_EM must equal 1/S (PHASE constitutive)"
    assert np.allclose(c_sh, np.sqrt(S), rtol=1e-9), "c_shear must equal √S (G identity)"
    print("  → c_EM RISES (ε,μ; 1/S), c_shear FALLS (G; √S): the modes SPLIT the RIGHT way. ✓")
    print("  → SCOPE: sub-yield sanity check; the full near-yield √S dynamics is Stage 4.")


# ─────────────────────────────────────────────────────────────────────────────
# S1.2 — WAVE-TYPING / ALIAS GATE: the three indices pinned, the legacy alias scoped.
# ─────────────────────────────────────────────────────────────────────────────
def test_S1_2_three_indices_pinned_and_alias_hard_scoped():
    """S1.2 [identity — the load-bearing pin]: the three live refractive indices
    on the transverse field are PINNED to their canonical forms and the legacy
    `refractive_index()` alias is HARD-SCOPED to the EM GROUP index, so Stage 4
    (which inherits this) CANNOT silently re-conflate c_EM and c_shear.

    THE THREE (ave-kb/CLAUDE.md:79-80; gravity_sign_freq_modulation.py:92-97):
      n_EM PHASE = S      (c_EM=c₀/S; the α-speed)
      n_EM GROUP = √S     (master_equation_fdtd.n_em_index; the SIGNAL index)
      n_shear    = 1/√S   (master_equation_fdtd.n_shear_index; reciprocal of GROUP)

    PRE-REGISTERED BINS (frozen): PASS = all three identities hold at every swept A;
    the alias points at n_em_index() on BOTH engines; phase≠group off S=1.
    FAIL = any index drifts off canonical form / alias points elsewhere / phase==group.
    """
    from ave.core.master_equation_fdtd import MasterEquationFDTD
    from ave.core.crystal_engine import CrystalEngine

    A = np.array([0.0, 0.2, 0.4, 0.6])
    S = TX.S_of_A(A)

    # (1) the desk-calc taxonomy: the three forms are correct + reciprocal.
    assert np.allclose(TX.n_em_group(A), np.sqrt(S), rtol=1e-9), "n_EM_group must be √S"
    assert np.allclose(TX.n_shear(A), 1.0 / np.sqrt(S), rtol=1e-9), "n_shear must be 1/√S"
    assert np.allclose(TX.n_em_group(A) * TX.n_shear(A), 1.0, rtol=1e-9), (
        "n_EM_group and n_shear must be EXACT reciprocals (RECIPROCAL channels)"
    )
    assert np.allclose(TX.n_em_phase(A), S, rtol=1e-9), "n_EM_phase must be S"
    # phase ≠ group off S=1 (the conflation would make them equal):
    off = A > 0
    assert np.all(np.abs(TX.n_em_phase(A)[off] - TX.n_em_group(A)[off]) > 1e-3), (
        "n_EM_phase (S) and n_EM_group (√S) must be DISTINCT off S=1 — conflating "
        "them is the phase/group category error"
    )

    # (2) the ENGINE methods carry the wave-typed forms + the alias holds on BOTH.
    print("\n--- S1.2 three-index pin + alias hard-scope (both engines) ---")
    for Engine, kw in (
        (MasterEquationFDTD, dict(N=16)),
        (CrystalEngine, dict(N=16)),
    ):
        e = Engine(**kw)
        # seed a sub-yield field so S<1 somewhere (the index forms are nontrivial)
        if hasattr(e, "inject_gaussian"):
            e.inject_gaussian((8, 8, 8), 2.0, 0.5 * e.V_yield)
        n_em = np.asarray(e.n_em_index())
        n_sh = np.asarray(e.n_shear_index())
        n_alias = np.asarray(e.refractive_index())
        # the engine n_em_index is the GROUP index √S; n_shear is its reciprocal 1/√S
        assert np.allclose(n_em * n_sh, 1.0, rtol=1e-9), (
            f"{Engine.__name__}: n_em_index·n_shear_index must be 1 (reciprocal)"
        )
        # the alias is HARD-SCOPED to n_em_index (the GROUP index) — NOT n_shear.
        assert np.allclose(n_alias, n_em, rtol=1e-12), (
            f"{Engine.__name__}: refractive_index() must alias n_em_index() (the "
            f"hard-scoped EM GROUP index), NOT n_shear_index — wave-typing broken"
        )
        assert not np.allclose(n_alias, n_sh, rtol=1e-3) or np.allclose(n_em, n_sh), (
            f"{Engine.__name__}: the alias must NOT silently read n_shear"
        )
        print(f"  {Engine.__name__}: n_em·n_shear=1 (reciprocal) ✓; "
              f"refractive_index() is n_em_index() (GROUP √S) ✓")
    print("  → the three indices are PINNED; the alias is HARD-SCOPED to the EM GROUP")
    print("    index → Stage 4 cannot silently re-conflate c_EM and c_shear.")


# ─────────────────────────────────────────────────────────────────────────────
# S1.3 — GUARD-TRIAD EXTENSION: the α-clean immune system covers transverse/srs.
# ─────────────────────────────────────────────────────────────────────────────
def test_S1_3_guard_triad_extends_to_transverse_modules():
    """S1.3 [identity/foundation — the immune system]: the Stage-0 guard triad
    (no ALPHA/ALPHA_COLD_INV/Q_TANK/ELECTRON/RHO_BULK reachable) is EXTENDED to the
    Stage-1 transverse code path (_transverse / _em_media / chiral_lattice_vector).
    STRUCTURAL chirality is ON (lossless optical-activity rotation, Axiom-3) but
    the α-dressed ETA_ROT_PER_WRITHE is NOT inherited as a bankable scale.

    ⚑ NAMED out-of-scope contaminant (flag-don't-fix; prereg S1.3): the SATURATED
    genesis engine `chiral_lattice_vector_sat` imports ALPHA (:15). It is NOT in the
    Stage-1 transverse path (the driven split uses the α-clean _em_media.em_params).
    Recorded as a Stage-4-blocking item, NOT silently rewritten (out of Stage-1 scope).

    PRE-REGISTERED BINS (frozen): PASS = no α-carrier in the Stage-1 path AND the
    guard is LIVE (a deliberate leak trips it) AND ETA_ROT_PER_WRITHE is the tagged
    engineering scale (=1.0, not a bankable magnitude) AND the _sat α-import is
    recorded as a named out-of-scope contaminant. HARD-STOP = any α-carrier reachable
    in the Stage-1 path.
    """
    import ave.core.chiral_lattice_vector as clv

    # (a) the Stage-1 transverse path is α-clean.
    TX.assert_transverse_path_alpha_clean()
    print("\n--- S1.3 guard-triad extension to the transverse/srs modules ---")
    print("  ALPHA/ALPHA_COLD_INV/Q_TANK/ELECTRON/RHO_BULK absent from")
    print("  _transverse / _em_media / chiral_lattice_vector globals?  YES (load-time + runtime).")

    # (b) the guard is LIVE, not vacuous: a deliberately-injected leak trips it.
    import ave.core.chiral_lattice_vector as _clv_mod
    _clv_mod.ALPHA = 7.2973525693e-3  # inject a leak into the srs vector engine
    try:
        with pytest.raises(AssertionError, match="α-leak|ALPHA"):
            TX.assert_transverse_path_alpha_clean()
        print("  guard is LIVE: a deliberately-injected ALPHA into chiral_lattice_vector TRIPS it. ✓")
    finally:
        del _clv_mod.ALPHA  # restore cleanliness
    TX.assert_transverse_path_alpha_clean()  # confirm restored

    # (c) STRUCTURAL chirality ON, but ETA_ROT_PER_WRITHE is the TAGGED engineering
    #     scale — not a bankable α-dressed magnitude. (The Stage-0 spine excludes the
    #     α-echo; the transverse rotation is the lossless geometry channel κ=0.)
    assert clv.ETA_ROT_PER_WRITHE == 1.0, (
        "ETA_ROT_PER_WRITHE must be the tagged engineering scale (1.0), not a "
        "bankable α-dressed magnitude"
    )
    print(f"  ETA_ROT_PER_WRITHE = {clv.ETA_ROT_PER_WRITHE} (tagged engineering scale; "
          f"structural chirality ON, not a bankable α-dressed magnitude). ✓")

    # (d) the saturated genesis engine's α-import is NAMED out-of-scope (recorded,
    #     not silently fixed) — a Stage-4-blocking contaminant.
    rec = TX.sat_engine_alpha_import_is_out_of_scope()
    print(f"  ⚑ FLAG (out-of-scope, Stage-4-blocking): {rec['module']} imports ALPHA "
          f"({rec['imports_alpha']}); in Stage-1 path? {rec['in_stage1_path']}.")
    assert rec["in_stage1_path"] is False, (
        "the _sat α-import must be OUT of the Stage-1 path (the driven split must "
        "route through the α-clean _em_media.em_params, not _sat)"
    )
    assert rec["blocks_stage"] == 4, "the _sat α-import is a Stage-4-blocking contaminant"
    print("  → the guard triad now covers the transverse/srs modules; the _sat α-import")
    print("    is a NAMED Stage-4 contaminant (flag-don't-fix), out of Stage-1 scope.")
