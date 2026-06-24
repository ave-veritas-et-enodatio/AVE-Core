"""S2 — a conservative skew-Hermitian H_couple locking A1↔ω (winding stays independent).

FROZEN PRE-REG: research/2026-06-24_engine-s2-hcouple_prereg.md (commit 38066fd2).
This module is the S2 make-or-break gate (pre-reg §Make-or-break): a FIELD-RESOLVED
skew-Hermitian (anti-Hermitian-by-construction) H_couple in the A1↔ω SECTOR PAIR
(A1 bulk-dilatation breather = mass ↔ Cosserat micro-rotation ω = charge winding),
S(A)-gated (saturation front, FORK A=(a) intra-mechanical — NO TKI transducer),
on the α-clean host. PASSES iff ALL FOUR criteria hold; FAIL on any one; Rule-11
INCONCLUSIVE is a legit landing (no rescue).

    (1) CONSERVATION  — |dH/H| < 1e-8 over a long closed-system window
                        (precedent test_l1_photon.py:285; PR#321 reduced gen ≈1.1e-12).
    (2) NON-VACUITY   — transfer MEASURED (a_shear/ω starts EMPTY, fills) AND the
                        |L_ω| pump canary stays BOUNDED (spin_L_omega, graft_v2:300).
    (3) INDEPENDENCE  — ω keeps its OWN conserved winding integer robust under a
                        V-perturbation on the REAL arm, while the SLAVED arm
                        (ω:=F(V)) returns independence=False (reachable-False /
                        AUTO_VOID, s1_winding_conservation_gate.py:439). Normal-mode
                        SPLITTING is DECLARED EXPECTED + bounded (FORK B=(b)) — NOT
                        a violation.
    (4) REDUCED-LIMIT — H_couple recovers the 2-mode circulator generator
                        (node_circulator_coupling.py:124-157) in its 2-mode limit.

ANTI-REBUILD (Rule 14). This gate REUSES the existing immune system:
  * node_circulator_coupling.circulator_generator — the PR#321 2-mode generator,
    the VALIDATE-ON-KNOWN to RECOVER (criterion 4), NOT re-skinned as deliverable.
  * crystal_graft_v2.spin_L_omega — the |L_ω| pump canary (criterion 2 + neg-ctrl).
  * s1_winding_conservation_gate.gate_f_positive_control — the slaved-arm
    reachable-False INDEPENDENCE discriminator (criterion 3).
  * test_l1_photon.py:285 — the |dH/H| < 1e-8 conservation precedent.

GENUINE NEW WORK: there is NO existing field-resolved coupling in the A1↔ω pair.
ADD-2 (crystal_engine.py:222) is bulk↔shear-DISPLACEMENT (V↔w) — the WRONG pair;
recovering it does NOT count (pre-reg WRONG-SECTOR-PAIR guard). S2 BUILDS the
field-resolved A1↔Cosserat-ω skew generator and recovers the 2-mode ODE in limit.

α-CLEAN (pre-reg §α-clean discipline). The chord-deciding readout routes through
the α-clean host _winding_host.py (κ̃=6/5). NEVER ALPHA / KAPPA_CHIRAL_ELECTRON /
V_SNAP / L_NODE / M_E / Q_TANK on the chord path. The chirality PHASE uses the
α-free θ_χ=2π·ν_vac (ν_vac=2/7); the rate scale uses κ̃=6/5. Q=137 slot stays EMPTY.

CLASSIFICATION (consistency-vs-emergence): CONSISTENCY-class (pre-reg §Class). A
green S2 demonstrates a substrate-consistent conservative lock; it is NOT the
α-free chord (the chord-decider is S4). No emergence headline.
"""

from __future__ import annotations

import importlib.util as _ilu
from pathlib import Path as _Path

import numpy as np

# ── α-CLEAN HOST (the chord-deciding readout path; κ̃=6/5, NO α). Importing this
#    module executes its load-time guard triad — an α-leak fails HERE. ──────────
from tests.engine_acceptance import _winding_host as HOST

# ── VALIDATE-ON-KNOWN target to RECOVER (criterion 4): the PR#321 2-mode skew
#    generator. node_circulator_coupling.py lives in src/scripts/vol_9_device/
#    (no package __init__), so we load it BY FILE — importing the EXACT PR#321
#    functions (anti-rebuild, Rule 14), NOT a re-skin. The module's own α-free
#    guard (assert_alpha_free) is NOT run at module load (only in its main()), so
#    importing it cannot pull α onto our chord path; the S2 chord readout still
#    routes through HOST. We use ONLY circulator_generator/evolve/mode_energies. ─
def _load_node_circulator():
    p = (
        _Path(__file__).resolve().parents[2]
        / "scripts"
        / "vol_9_device"
        / "node_circulator_coupling.py"
    )
    spec = _ilu.spec_from_file_location("_ave_node_circulator_coupling", p)
    mod = _ilu.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


_NCC = _load_node_circulator()
ncc_circulator_generator = _NCC.circulator_generator  # the 2-mode skew generator
ncc_evolve = _NCC.evolve  # exact unitary trajectory a_k = U^k a0
ncc_mode_energies = _NCC.mode_energies  # |a_bulk|², |a_shear|²
