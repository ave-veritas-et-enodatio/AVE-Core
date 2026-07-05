"""HONEST NONLINEAR DYNAMICS MODULE — 2-DOF pump-probe chain (SKELETON).

Adjudicates the #526 T-slot scope fork (DC_ONLY vs EXTENDED) by running the FULL
NONLINEAR DYNAMICS of a 2-DOF-per-node chain and MEASURING what a slow transverse
probe sees through a traveling pump. NO slot bookkeeping. The dynamics do not know
how terms were divided between S and T; they just respond.

THE #531 TAUTOLOGY GUARD (binding): this module MUST NOT import
`pump_probe_predictions.py` (the slot-formula prediction module). The probe stiffness
is measured from the time-domain response ONLY. The #528 ReconcileGate compares this
module's measured output against the prediction module's frozen arms.

Construction (FROZEN prereg 2026-07-05_pump-probe-tslot_prereg_FROZEN.md):
  - N-node chain, 2 DOF/node: longitudinal u_i, transverse y_i, rest spacing a0=1.
  - Bond length L_i = √((a0 + u_{i+1} − u_i)² + (y_{i+1} − y_i)²)  ← the ONLY
    transverse↔axial coupling source (NOT a T/ℓ term inserted by hand).
  - Axial constitutive law = canonical kernel potential Φ, Φ''(a)=k0√(1−a²),
    Φ'(A)=k0(A√(1−A²)+arcsin A)/2 (integrate once).
  - H = Σ ½(u̇²+ẏ²)/m + Σ_bond Φ(A_bond); transverse stiffness inherited ENTIRELY
    from Φ through the geometry.
  - Symplectic velocity-Verlet integration; absorbing boundaries; SWR measured.
  - Slow weak transverse probe measures effective transverse stiffness / phase
    velocity in the measurement window.

STATUS: SKELETON. Bodies land in incremental commits (skeleton-first discipline).
"""
from __future__ import annotations

import numpy as np

# ── kernel-unit conventions (same as #526/#529/#531) ─────────────────────────
K0 = 1.0
ELL = 1.0     # rest bond spacing a0
K_A = 1.0     # axial spring scale (kernel units)
K_S = 1.0     # transverse (shear soft) spring scale


def bond_tension(amplitude):
    """Φ'(A) — canonical kernel potential's first derivative. Independent re-impl
    (the dynamics own their kernel; NOT imported from the prediction module)."""
    a = np.asarray(amplitude, dtype=float)
    return K0 * (a * np.sqrt(np.clip(1.0 - a**2, 0.0, 1.0)) + np.arcsin(np.clip(a, -1.0, 1.0))) / 2.0


def kernel_potential(amplitude):
    """Φ(A) = ∫₀^A Φ'(s) ds — the axial constitutive energy (Φ(0)=Φ'(0)=0)."""
    raise NotImplementedError("skeleton: Φ(A) double-integral lands in the dynamics commit")


def axial_force(amplitude):
    """dΦ/dA = Φ'(A) = bond_tension; the axial constitutive force magnitude."""
    return bond_tension(amplitude)


# ── the honest chain ─────────────────────────────────────────────────────────
class PumpProbeChain:
    """2-DOF-per-node nonlinear chain with symplectic integration + absorbing ends."""

    def __init__(self, n_nodes, mass=1.0, sponge_width=0, sponge_gamma=0.0):
        raise NotImplementedError("skeleton: chain construction lands in the dynamics commit")

    def bond_lengths(self, u, y):
        """L_i = √((a0 + Δu)² + Δy²) for every bond — the honest coupling source."""
        raise NotImplementedError("skeleton")

    def forces(self, u, y):
        """Per-node (F_u, F_y) from Σ_bond Φ(A_bond) via the bond-length gradient."""
        raise NotImplementedError("skeleton")

    def step_verlet(self, state, dt):
        """One symplectic velocity-Verlet step."""
        raise NotImplementedError("skeleton")

    def measure_swr(self, y_history, window):
        """Standing-wave ratio in the measurement window (hidden-reflection guard)."""
        raise NotImplementedError("skeleton")

    def measure_probe_stiffness(self, *, pump_amplitude, pump_omega, probe_amplitude,
                                probe_omega, window):
        """The CONSUMED observable: the effective transverse stiffness / phase
        velocity a slow weak probe sees in the measurement window. Measured from the
        time-domain response ONLY (no slot formulas)."""
        raise NotImplementedError("skeleton")


def run_three_states():
    """(a) COLD, (b) DC-BIAS held bow, (c) PUMP traveling wave — same measurement.
    Returns the measured probe-stiffness table."""
    raise NotImplementedError("skeleton: three-state driver lands in the dynamics commit")


def adjudicate():
    """Compare the measured (c) PUMP stiffness against the frozen arms via the #528
    ReconcileGate; select the bin (no fall-through else; DISCREPANT-HALT reachable)."""
    raise NotImplementedError("skeleton: bin selector + ReconcileGate lands in the gate commit")


if __name__ == "__main__":
    raise SystemExit("pump_probe_chain.py is a skeleton — bodies land in incremental commits")
