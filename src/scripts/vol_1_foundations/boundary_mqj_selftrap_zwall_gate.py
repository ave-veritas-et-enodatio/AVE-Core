"""Stage 1 GATE — boundary-observable (𝓜/𝓠/𝓙) self-trap integrator + Z-at-wall.

Keystone reframe (canonical: manuscript/ave-kb/common/boundary-observables-m-q-j.md):
the substrate-correct electron test reads the three boundary observables 𝓜 (mass),
𝓠 (charge), 𝓙 (spin) at the boundary ∂Ω of a self-trapped Γ=−1 region. Prior arc
negatives measured INTERIOR plumbing (a category error: interior eigenmodes are
causally disconnected per clm-sjjvhf). The boundary test never ran.

THIS STAGE is the GATE and computes NO M/Q/J (that is Stage 2/3). It answers ONE
gating question with a FOUR-WAY (NOT binary) verdict:
  Does a self-trapped Γ=−1 region port to the COUPLED engine and remain stable as
  a TRUE STIFFENING confinement (C_eff→∞ ⇒ Z→0 ⇒ |Γ|=1), long enough to later read
  its boundary?

THE LOAD-BEARING TENSION (why the gate is 4-way, not binary):
  The electron self-trap is the STIFFENING route: C_eff→∞ ⇒ Z→0 ⇒ |Γ|=1 — the A1
  longitudinal matter-wall (INVARIANT-S2 Q1=B, Grant-ratified). BUT the
  capability-map (engine-capability-map.md:45,79) says VacuumEngine3D is
  "softening-only ... structurally cannot host the stiffening cage": its scalar is
  a PROJECTION v_scalar_from_v_inc(V_inc), NO independent A1 field. So the
  vacuum_engine Γ=−1 saturated-bond wall is EITHER (a) a true Z→0 stiffening
  confinement OR (b) a softening-route proxy (transverse Meissner Z_eff=√(S_μ/S_ε),
  bulk ρ̄ reflection). WE DETERMINE WHICH BY MEASURING Z AT THE SATURATED WALL.

FOUR-WAY VERDICT (auditor-mandated buckets — NOT collapsed to binary):
  PORTS-STABLE        — known-positive held + Z→0 at wall (TRUE stiffening) + |ω|
                        bounded + full-Hamiltonian flat/decaying + saturated channel
                        persists ≥10 Compton periods while unsaturated decays.
  c_eff(V)-STRUCTURAL-GAP (🔧, NOT echo; a bounded build) — wall forms but Z does
                        NOT →0 (softening proxy, not C_eff→∞). Confirms cap-map
                        :45/:79. → coupled engine needs a true c_eff(V)/independent-A1
                        field (a BOUNDED build: couple the master-equation cage's
                        c_eff(V) in). Report the measured Z behavior as evidence.
  PHYSICAL-NO-TRAP    (🔴, ECHO candidate) — known-positive held AND Z→0 stiffening
                        present, but STILL no stable bounded trap (disperses /
                        destabilizes). Only THIS bucket bears on echo.
  PUMPS               — full-Hamiltonian ledger climbs → trap not passive (ontology).
  (INTEGRATOR-INADEQUATE — bucket 1: if the known-positive standalone cage CANNOT
   be held, any coupled blow-up is numerical, not physics.)

A naive "BLOW-UP" must NOT be reported — it is resolved into (1) numerical,
(2) needs-the-cage, or (3) echo, via the known-positive validation (step 1) + the
Z-at-wall measurement (step 2).

DISCIPLINE (applied, not just named):
  ave-apparatus-floor-attribution — KNOWN-POSITIVE FIRST: run the standalone
    MasterEquationFDTD v14 verdict-II cage (the engine that DOES have c_eff(V));
    confirm the solver holds it. Then dx/dt(cfl) sweep. Bucket-1 gate.
  substrate-native-check CP8 — seed the GENERATIVE PRECURSOR (helical ω-photon);
    let the moving Γ=−1 wall form. A planted-Γ run is LABELED instrumentation-only.
  substrate-native-check CP10 — trap rendered as Op17-bounded BOUNDARY CONDITION
    (use_impedance_boundary=True; _rotate_clamp exact reactance rotation), NOT a
    bulk energy/force term. The bulk V→ω W_refl gradient force (the documented
    runaway channel) is OFF on this path.
  ave-conserved-vs-pumped — full-Hamiltonian witness total_hamiltonian()
    (kinetic+gradient potential), NOT sum(ω²); KEEP-BOTH the engine's own
    impedance_hamiltonian().
  ave-canonical-source — V_SNAP, ALPHA from ave.core.constants; ZERO new free params.

Run:  PYTHONPATH=src ./.venv/bin/python \
        src/scripts/vol_1_foundations/boundary_mqj_selftrap_zwall_gate.py
Env overrides for fast smoke: MQJ_N, MQJ_PERIODS.
"""
from __future__ import annotations

import json
import os

import numpy as np

# ── Canonical-source imports (ave-canonical-source — zero new free params) ────
from ave.core.constants import ALPHA, C_0, V_SNAP
from ave.core.master_equation_fdtd import MasterEquationFDTD
from ave.topological.vacuum_engine import (
    BondObserver,
    EnergyBudgetObserver,
    EngineConfig,
    VacuumEngine3D,
)

import ave.core.constants as _avc  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))


def _canonical_source_gate() -> None:
    """ave-canonical-source — assert the constants are the canonical ones."""
    assert _avc.__file__.endswith("ave/core/constants.py"), "non-canonical constants source"
    assert abs(ALPHA - 7.2973525693e-3) < 1e-12, "ALPHA not canonical"
    _ = (C_0, V_SNAP)  # referenced for provenance


# ──────────────────────────────────────────────────────────────────────────
# Geometry + units (natural units: dx = ℓ_node, c₀ = 1)
# ──────────────────────────────────────────────────────────────────────────
N = int(os.environ.get("MQJ_N", "24"))
PML = 4
SIGMA, LAM = 3.0, 6.0
A_LOCK = 3.0          # peak |ω| seed for the LOCK regime (engages a soft Γ=−1 wall)
A_PUMP = 6.0          # peak |ω| seed for the PUMP control (hard wall, parametric pump)
K_WALL = 60.0         # soft clamp → engaged + stable + few sub-steps
CFL_SAFE = 0.25       # anti-pump margin on the implicit reactance-rotation
CENTER = (N / 2.0, N / 2.0, N / 2.0)

OMEGA_C_NATURAL = 1.0                        # = c_R/dx ring scale
T_COMPTON = 2.0 * np.pi / OMEGA_C_NATURAL    # one Compton period in natural-time
N_PERIODS = float(os.environ.get("MQJ_PERIODS", "12"))   # ≥10P persistence target + margin


def _steps_for_periods(eng, n_periods: float) -> int:
    """# outer steps to evolve `n_periods` Compton periods (apparatus-floor honest:
    derived from the engine's own outer_dt, not a hard-coded step count)."""
    return int(np.ceil(n_periods * T_COMPTON / eng.outer_dt))


# ══════════════════════════════════════════════════════════════════════════
# STEP 1 — KNOWN-POSITIVE VALIDATION (ave-apparatus-floor-attribution).
# Run the STANDALONE verdict-II self-trap that DOES have c_eff(V): the
# MasterEquationFDTD v14 breathing soliton (master_equation_fdtd.py:13 —
# c_eff(V)=c0·(1−A²)^(−1/4)→∞; v14 Mode I PASS, test_master_equation_v14_mode_i.py).
# This is the cap-map's "the only engine with the A1 cage" (engine-capability-map.md:42).
#
# If the solver CANNOT hold this known-stable standalone trap → bucket (1)
# INTEGRATOR-INADEQUATE: any coupled blow-up downstream is numerical, not physics.
# Validate the INSTRUMENT on a known-positive before trusting any coupled null.
#
# Z-at-wall on the cage: the A1 longitudinal tank has C_eff = C_0/S, so
# Z_long = √(L/C_eff) = √(L·S/C_0) ∝ √S → 0 as S→0 (A→1). The engine exposes
# refractive_index() = S^(1/4), so Z_long/Z_0 = √S = refractive_index()². The
# MIN over the lattice is the deepest saturation (cage core). Z_long→0 there IS
# the stiffening-confinement signature this gate looks for.
# ══════════════════════════════════════════════════════════════════════════
KP_DX = 0.5
KP_SEED_AMP = 0.85     # v14 canonical seed (test_master_equation_v14_mode_i.py:35)
KP_SEED_RADIUS = 2.5
KP_STEPS = 600
KP_TRANSIENT = 200


def _run_known_positive(amplitude=KP_SEED_AMP, cfl=0.4, N_kp=24, nsteps=KP_STEPS):
    """Run the standalone MasterEquationFDTD v14 verdict-II cage and report
    whether the solver HELDS it (bucket-1 gate) + its longitudinal Z-at-core."""
    eng = MasterEquationFDTD(
        N=N_kp, dx=KP_DX, V_yield=1.0, c0=1.0, cfl_safety=cfl, pml_thickness=4
    )
    c = N_kp // 2
    coords = np.arange(N_kp) - c
    X, Y, Z = np.meshgrid(coords, coords, coords, indexing="ij")
    r = np.sqrt(X**2 + Y**2 + Z**2) * KP_DX
    seed = amplitude * (1.0 / np.cosh(r / KP_SEED_RADIUS))
    eng.V[:] = seed
    eng.V_prev[:] = seed.copy()

    v_peak, n_min, diverged = [], [], None
    for s in range(nsteps):
        eng.step()
        vmax = float(np.abs(eng.V).max())
        if not np.isfinite(vmax) or vmax > 1e3:
            diverged = s
            break
        if s >= nsteps // 3:
            v_peak.append(vmax)
            n_min.append(float(eng.refractive_index().min()))
    if diverged is not None or not v_peak:
        return {
            "held": False, "diverged_at": diverged, "cfl": float(cfl), "N": int(N_kp),
            "v_peak_mean": float("nan"), "std_over_mean": float("nan"),
            "S_core": float("nan"), "Z_long_core": float("nan"),
        }
    vp = np.asarray(v_peak)
    nm = np.asarray(n_min)
    som = float(vp.std() / max(vp.mean(), 1e-9))
    S_core = float(nm.min() ** 4)          # refractive_index = S^(1/4)
    Z_long = float(np.sqrt(max(S_core, 0.0)))  # Z_long/Z_0 = √S
    held = bool(vp.mean() > 0.2 and 0.05 < som < 0.5 and nm.min() < 0.97)
    return {
        "held": held, "diverged_at": diverged, "cfl": float(cfl), "N": int(N_kp),
        "v_peak_mean": float(vp.mean()), "std_over_mean": som,
        "S_core": S_core, "Z_long_core": Z_long,
    }


def _known_positive_gate() -> dict:
    """Bucket-1 gate + apparatus-floor sweep on the KNOWN-POSITIVE cage.
    Held across amplitude × cfl → the instrument is adequate; a coupled failure
    cannot then be blamed on the integrator."""
    base = _run_known_positive(amplitude=KP_SEED_AMP, cfl=0.4)
    sweep = []
    for amp in (0.85, 0.97):
        for cfl in (0.4, 0.2):
            sweep.append(_run_known_positive(amplitude=amp, cfl=cfl))
    held_all = base["held"] and all(p["held"] for p in sweep)
    Z_trend = [p["Z_long_core"] for p in sweep if np.isfinite(p["Z_long_core"])]
    return {
        "instrument_adequate": bool(held_all),
        "base": base,
        "sweep": sweep,
        "Z_long_core_min": float(min(Z_trend)) if Z_trend else float("nan"),
        "note": (
            "KNOWN-POSITIVE = standalone MasterEquationFDTD v14 cage (the engine "
            "with c_eff(V); master_equation_fdtd.py:13). Z_long/Z_0=√S→0 at core IS "
            "the stiffening-confinement signature. If instrument_adequate is True, "
            "any coupled-engine blow-up is NOT numerical (bucket-1 cleared)."
        ),
    }


def main() -> dict:
    raise NotImplementedError("skeleton — sections land incrementally")


if __name__ == "__main__":
    main()
