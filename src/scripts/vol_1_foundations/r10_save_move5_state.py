"""r10_save_move5_state.py — Phase 0.1 per round_10_plan.md.

Captures Move 5 saturated attractor at end of selection window (t = 15 P) and
saves engine state via VacuumEngine3D.save(). Cached state amortizes the
pre-evolve (10 P) + selection (5 P) overhead across the ~5-8 Phase 1 observer
reruns (Direction 3 multi-operator signature observer + Direction 3' substrate-
(n,l,m_l) tests).

Setup IDENTICAL to path α v3 (and v1, v2) — same engine config, same seed,
same windows. Only the recording phase is omitted; the script saves engine
state at t=15 P instead of recording 185 P of post-selection trajectory.

Verification (round-trip smoke test):
1. Save engine A at t=15 P → .npz file
2. Load to engine B from .npz
3. Compare engine A and B state arrays element-wise (must match exactly)
4. Run 1 step on each; compare again (must match — engine evolution is
   deterministic from identical state)

If verification passes, the cached state is usable for downstream Phase 1
observer reruns: load → attach observers → run recording window.
"""
from __future__ import annotations

import sys
import time
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "src"))
sys.path.insert(0, str(Path(__file__).resolve().parent))

from ave.topological.vacuum_engine import VacuumEngine3D
from tlm_electron_soliton_eigenmode import initialize_2_3_voltage_ansatz


# ─── Constants (matching path α v1/v2/v3 + Move 5 exactly) ────────────────

PHI = 0.5 * (1.0 + np.sqrt(5.0))
PHI_SQ = PHI * PHI

N_LATTICE = 32
PML = 4
R_ANCHOR = 10.0
R_MINOR = R_ANCHOR / PHI_SQ

A26_AMP_SCALE = 0.3 / (np.sqrt(3.0) / 2.0)
GT_PEAK_OMEGA = 0.3 * np.pi
A26_GUARD_LOW = 0.85 * GT_PEAK_OMEGA
A26_GUARD_HIGH = 1.15 * GT_PEAK_OMEGA
V_AMP_INIT = 0.14

OMEGA_C = 1.0
COMPTON_PERIOD = 2.0 * np.pi / OMEGA_C
DT = 1.0 / np.sqrt(2.0)

PRE_EVOLVE_END_P = 10.0
SELECTION_END_P = 15.0
PRE_EVOLVE_END_STEP = int(PRE_EVOLVE_END_P * COMPTON_PERIOD / DT)
SELECTION_END_STEP = int(SELECTION_END_P * COMPTON_PERIOD / DT)

REPO_ROOT = Path(__file__).resolve().parents[3]
SAVE_PATH = REPO_ROOT / "data" / "move5_attractor_15p.npz"


def build_engine() -> VacuumEngine3D:
    return VacuumEngine3D.from_args(
        N=N_LATTICE, pml=PML, temperature=0.0,
        amplitude_convention="V_SNAP",
        disable_cosserat_lc_force=True,
        enable_cosserat_self_terms=True,
    )


def seed_corpus_2_3_joint(engine: VacuumEngine3D) -> None:
    engine.cos.initialize_electron_2_3_sector(
        R_target=R_ANCHOR, r_target=R_MINOR,
        use_hedgehog=True, amplitude_scale=A26_AMP_SCALE,
    )
    initialize_2_3_voltage_ansatz(
        engine.k4, R=R_ANCHOR, r=R_MINOR, amplitude=V_AMP_INIT,
    )


def pre_evolve_and_select(engine: VacuumEngine3D, label: str = "engine") -> None:
    """Pre-evolve through PRE_EVOLVE + SELECTION windows (15 P total)."""
    print(f"  [{label}] Pre-evolve + selection: 0 → 15 P "
          f"({SELECTION_END_STEP} steps)...", flush=True)
    t0 = time.time()
    last = t0
    for step in range(SELECTION_END_STEP):
        engine.step()
        if (time.time() - last) > 30.0:
            print(f"    [{label}] step {step}/{SELECTION_END_STEP}, "
                  f"elapsed {time.time()-t0:.1f}s", flush=True)
            last = time.time()
    print(f"    [{label}] done at {time.time()-t0:.1f}s", flush=True)


def assert_state_matches(a: VacuumEngine3D, b: VacuumEngine3D, tag: str) -> None:
    """Element-wise state comparison."""
    assert a.time == b.time, f"{tag}: time mismatch {a.time} vs {b.time}"
    fields_k4 = ["V_inc", "V_ref", "Phi_link", "S_field"]
    fields_cos = ["u", "omega", "u_dot", "omega_dot"]
    for fld in fields_k4:
        a_arr = getattr(a.k4, fld)
        b_arr = getattr(b.k4, fld)
        assert np.array_equal(a_arr, b_arr), f"{tag}: k4.{fld} mismatch"
    for fld in fields_cos:
        a_arr = getattr(a.cos, fld)
        b_arr = getattr(b.cos, fld)
        assert np.array_equal(a_arr, b_arr), f"{tag}: cos.{fld} mismatch"


def main() -> None:
    print("=" * 78, flush=True)
    print("  r10 Phase 0.1 — Move 5 saved-state caching")
    print("  (Engine save/load API + round-trip smoke test)")
    print("=" * 78, flush=True)
    print(f"  Lattice: N={N_LATTICE}, PML={PML} (interior {N_LATTICE - 2*PML}^3)")
    print(f"  Corpus GT: R={R_ANCHOR}, r={R_MINOR:.4f}")
    print(f"  Save target: t = {SELECTION_END_P} P "
          f"(pre-evolve {PRE_EVOLVE_END_P} P + selection "
          f"{SELECTION_END_P - PRE_EVOLVE_END_P} P)")
    print(f"  Save path: {SAVE_PATH.relative_to(REPO_ROOT)}")
    print()

    # ─── Phase 1: build engine A, evolve to 15 P ────────────────────────────
    print("Phase 1 — Build + evolve engine A to t=15 P", flush=True)
    engine_a = build_engine()
    seed_corpus_2_3_joint(engine_a)
    omega_peak_init = float(np.linalg.norm(engine_a.cos.omega, axis=-1).max())
    assert A26_GUARD_LOW <= omega_peak_init <= A26_GUARD_HIGH, \
        f"A26 init guard FAIL: peak |ω|={omega_peak_init:.4f} not in " \
        f"[{A26_GUARD_LOW:.4f}, {A26_GUARD_HIGH:.4f}]"
    print(f"  Initial peak |ω| = {omega_peak_init:.4f} (A26 guard OK)")

    pre_evolve_and_select(engine_a, "engine A")

    omega_peak_at_save = float(np.linalg.norm(engine_a.cos.omega, axis=-1).max())
    v_inc_l2_at_save = float(np.linalg.norm(engine_a.k4.V_inc))
    print(f"  At t=15 P: peak |ω| = {omega_peak_at_save:.4f}, "
          f"||V_inc||_2 = {v_inc_l2_at_save:.4e}")

    # ─── Phase 2: save engine A ─────────────────────────────────────────────
    print()
    print("Phase 2 — Save engine A state to disk", flush=True)
    saved_path = engine_a.save(SAVE_PATH)
    file_size_mb = saved_path.stat().st_size / 1024 / 1024
    print(f"  Saved: {saved_path} ({file_size_mb:.1f} MB compressed)")

    # ─── Phase 3: load engine B from disk ──────────────────────────────────
    print()
    print("Phase 3 — Load engine B from disk", flush=True)
    engine_b = VacuumEngine3D.load(SAVE_PATH)
    print(f"  Loaded: engine B at t={engine_b.time:.4f}, "
          f"N={engine_b.N}, config matches: "
          f"{engine_a.config == engine_b.config}")

    # ─── Phase 4: round-trip equivalence (state arrays exactly match) ──────
    print()
    print("Phase 4 — Round-trip equivalence (state arrays)", flush=True)
    assert_state_matches(engine_a, engine_b, "post-load")
    print("  ✓ engine_a.state == engine_b.state at t=15 P (exact match)")

    # ─── Phase 5: deterministic-evolution equivalence (1 step → still match) ─
    print()
    print("Phase 5 — Deterministic evolution (run 1 step on each)", flush=True)
    engine_a.step()
    engine_b.step()
    assert_state_matches(engine_a, engine_b, "post-step")
    print(f"  ✓ engine_a.state == engine_b.state at t={engine_a.time:.4f} "
          f"(deterministic evolution preserved)")

    # ─── Phase 6: report ────────────────────────────────────────────────────
    print()
    print("=" * 78, flush=True)
    print("  Phase 0.1 verification: PASS")
    print("=" * 78, flush=True)
    print(f"  Save path: {saved_path}")
    print(f"  Save size: {file_size_mb:.1f} MB (compressed npz)")
    print(f"  State at save: t={SELECTION_END_P} P, peak |ω|={omega_peak_at_save:.4f}, "
          f"||V_inc||_2={v_inc_l2_at_save:.4e}")
    print(f"  Round-trip: state arrays match element-wise post-load AND "
          f"after 1 step on both (deterministic evolution preserved)")
    print()
    print("Phase 1 observer reruns can now:")
    print("  engine = VacuumEngine3D.load('data/move5_attractor_15p.npz')")
    print("  engine.add_observer(YourPhase1Observer())")
    print("  engine.run(n_steps=N_RECORDING_STEPS)")
    print()


if __name__ == "__main__":
    main()
