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


def main() -> dict:
    raise NotImplementedError("skeleton — sections land incrementally")


if __name__ == "__main__":
    main()
