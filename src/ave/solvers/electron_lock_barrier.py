"""ELECTRON-LOCK RECONNECTION-BARRIER TEST — does GENUINE confinement rescue the
(2,3) winding from being a carrier-ratio ECHO?

FROZEN PRE-REG: research/2026-07-08_electron-lock-barrier_prereg.md.

═══════════════════════════════════════════════════════════════════════════════
WHAT THIS IS (the last-swing of the electron-lock effort)
═══════════════════════════════════════════════════════════════════════════════
The PINCER (both loci already read AGAINST Reading B, grep-confirmed):
  • REAL-SPACE winding HOLDS but is INERT (research/2026-06-24_engine-s1-winding-
    dof_result.md:25) — same arc's S3 is DISPERSE-FALSIFIED (research/2026-06-24_
    engine-s3-cavity-pinning_result.md:4,50): "even with the winding demonstrably
    conserved, the coupling does not pin the core."
  • PHASE-SPACE winding reads as the LC CARRIER FREQUENCY RATIO, not topology
    (#417 BREAK, research/2026-06-24_engine-phase-space-winding_result.md:29). The
    load-bearing discriminator was CARRIER-RATIO DETUNING: detune ω_b:ω_s and the
    "(2,3)" tracks CONTINUOUSLY (1:1→0.93, 2:3→0.65, 3:2→1.54, 1:2→0.48). A
    topological integer CANNOT slide; a carrier ratio does exactly that.
  • Production `coupled_cage_winding` `rigid_template` mode CANNOT unwind (frozen
    ê_w, conserved BY CONSTRUCTION); a "held" there is a data-structure artifact.

The ONE un-run version is the BARRIER: every prior run measured whether a LABEL
stayed constant; NONE measured whether there is an ENERGY BARRIER against a REAL
reconnection. Pre-test physics (walked with Grant, ruled): "a knot holds because
untying it COSTS energy, losslessly — not because a bookkeeping integer is
conserved."

═══════════════════════════════════════════════════════════════════════════════
THE ASSEMBLY (reuse, anti-rebuild Rule 14)
═══════════════════════════════════════════════════════════════════════════════
Evolve a reconnection-capable (FREE / dispersive-vector-class) director — so
unwinding is physically POSSIBLE — WITH a moving-Γ=−1 confinement wall ON.
ENERGY-CONSERVING integrator only (UNITARY Crank–Nicolson/Cayley), so NO
numerical damping can fake a hold (Ax3-lossless; "no damping fakes a pin"). Read
winding in PHASE-SPACE (the Clifford torus, where the claim lives and where #417
bit) AND in real-space (compute_Q_link, the reconnection observable).

  • Spine: `CoupledCageWinding` in `winding_mode="dispersive_vector"` — the free ω
    director that CAN reconnect (the honest arm; rigid_template is frozen-by-
    construction and is used ONLY as a PROTECTED-reachable bin-liveness control).
  • Wall: `ConfinedCageWinding` (below) adds the moving-Γ=−1 confinement wall as a
    HERMITIAN reactive on-site potential U_conf(x) = K·g(x) on the ω-block
    diagonal. This is the UNITARY-scheme faithful analog of
    `cosserat_field_3d.py`'s `use_impedance_boundary` reactive clamp
    V_clamp = ½K·relu(−Γ)·|ω|² (`cosserat_field_3d.py:1920`) — a LOSSLESS,
    energy-STORING reflective short keyed on the MOVING saturation front, NOT the
    singular bulk `_reflection_density` term (the genesis-24 detonation, CP10).
    Being a REAL diagonal it keeps the CN/Cayley propagator EXACTLY UNITARY ⇒
    joint energy conserved to GMRES tolerance (~1e-10) — the rigor guard.

  ⚑ HONEST FLAG (BC-not-bulk / substrate-native): the literal
    `CosseratField3D.use_impedance_boundary` is a velocity-Verlet clamp on a
    DIFFERENT field representation (the JAX Cosserat u/ω) and its Meissner Γ=−1
    comes from the asymmetric (S_μ,S_ε) split, which the scalar unitary spine does
    not carry. On the spine the wall is realized as the reactive Op17-bounded
    moving-front confinement POTENTIAL (the Hermitian analog of the V_clamp term),
    keyed on the ω-sector's own saturation front. This preserves the brief's HARD
    requirement — "energy-conserving integrator only (unitary)", which the
    velocity-Verlet hard-clamp CANNOT pass (its own docstring reports ~1e4–1e5×
    runaway at default dt). The correspondence is V_clamp; the μ/ε provenance is
    replaced by the |ω|-front proxy — stated, not smoothed.

═══════════════════════════════════════════════════════════════════════════════
α-CLEAN / PHASE-ONLY
═══════════════════════════════════════════════════════════════════════════════
The phase-space observable is a pure arg() (dimensionless). No ALPHA / Q_TANK /
V_SNAP / KAPPA_CHIRAL_ELECTRON on the verdict path. Constants may enter ONLY as
off-path scale anchors (the scale-invariance gate proves the α-echo magnitude in
V_yield does NOT reach the verdict). An AST firewall scan asserts no ALPHA/M_E
NAME token in any verdict-path function.
"""

from __future__ import annotations

from dataclasses import dataclass, field

import numpy as np
from scipy import sparse

# REUSE (anti-rebuild, Rule 14): the S3 conservative unitary evolver + the α-free
# saturation-front gate + the electron seed; the real-space winding reader.
from ave.solvers.coupled_cage_winding import (
    CoupledCageWinding,
    CoupledCageWindingConfig,
    front_gate,
)
from ave.topological.charge_quantization import compute_Q_link

# ─────────────────────────────────────────────────────────────────────────────
# α-leak guard triad (import-time). An α-carrier leaking here fails the import.
# The verdict observable is a pure arg(); no α-carrier may reach the verdict path.
# ─────────────────────────────────────────────────────────────────────────────
assert "ALPHA" not in globals(), "α-leak: ALPHA must NOT be imported"
assert "Q_TANK" not in globals(), "α-leak: Q_TANK (=1/alpha) must NOT be imported"
assert "V_SNAP" not in globals(), "α-leak: V_SNAP must NOT be on the chord path"
assert "M_E" not in globals(), "α-leak: M_E must NOT be on the verdict path"
assert "KAPPA_CHIRAL_ELECTRON" not in globals(), "α-leak: KAPPA_CHIRAL_ELECTRON forbidden"


# ═════════════════════════════════════════════════════════════════════════════
# THE WALL — the moving-Γ=−1 reactive confinement, as a Hermitian on-site
# potential on the unitary spine (keeps CN/Cayley EXACTLY unitary).
# ═════════════════════════════════════════════════════════════════════════════
class ConfinedCageWinding(CoupledCageWinding):
    """`CoupledCageWinding` + a moving-Γ=−1 reactive confinement wall.

    The wall is a Hermitian on-site potential U_conf(x) = clamp_strength·g(x) added
    to the ω-sector diagonal block, where g(x) is a MOVING saturation-front weight
    ∈ [0,1]. Because U_conf is a REAL diagonal, the generator H stays Hermitian ⇒
    the Crank–Nicolson/Cayley propagator stays EXACTLY UNITARY ⇒ the joint energy
    ‖a_A1‖²+‖ω‖² is conserved to GMRES tolerance. This is the unitary-scheme analog
    of `cosserat_field_3d.py:1920`'s reactive V_clamp = ½K·relu(−Γ)·|ω|² — a
    lossless, energy-storing reflective short, NOT damping (Ax3: no damping fakes a
    pin) and NOT the singular bulk `_reflection_density` term (BC-not-bulk).

    `wall_form` selects the moving-front weight g(x):
      • "off"          — U_conf ≡ 0 (the wall-OFF control; Arm 1 / negative bin).
      • "omega_front"  — g = front_gate(|ω|/ω_yield): a reflective SHELL at the
                         ω-sector saturation front (the μ-side short locus, where
                         the ω-photon focuses); drives ω→node there. DEFAULT.
      • "a1_front"     — g = front_gate(|a_A1|/V_yield): the A1-core saturation
                         front (the same R_II=4/7 shell the coupling port uses).
      • "seed_cavity"  — g = 1 − w_amp0/max(w_amp0): a STATIC reflective box around
                         the seeded winding torus (a strong-confinement stress arm).
    """

    def __init__(self, cfg: CoupledCageWindingConfig, *, clamp_strength: float = 0.0,
                 wall_form: str = "omega_front", omega_yield: float = 1.0):
        super().__init__(cfg)
        self.clamp_strength = float(clamp_strength)
        self.wall_form = str(wall_form)
        self.omega_yield = float(omega_yield)
        self._wmax = 1.0  # set by seed_winding

    def seed_winding(self, *, amplitude: float = 1.0):
        super().seed_winding(amplitude=amplitude)
        self._wmax = max(1e-9, float(self.w_amp0.max()))

    def _omega_amp(self) -> np.ndarray:
        """|ω|(x) from the evolving field (dispersive_vector: a_w; rigid: b_w·ê_w)."""
        if self.winding_mode == "rigid_template":
            return np.abs(self.b_w)
        return np.sqrt(np.sum(np.abs(self.a_w) ** 2, axis=-1))

    def wall_weight(self) -> np.ndarray:
        """g(x) ∈ [0,1] — the MOVING confinement-front weight (α-free; pure ratio)."""
        if self.wall_form == "off" or self.clamp_strength == 0.0:
            return np.zeros((self.N, self.N, self.N), dtype=np.float64)
        if self.wall_form == "omega_front":
            A_omega = self._omega_amp() / max(self._wmax, 1e-9)
            return front_gate(A_omega)
        if self.wall_form == "a1_front":
            return front_gate(self.strain())
        if self.wall_form == "seed_cavity":
            return 1.0 - (self.w_amp0 / max(self._wmax, 1e-9))
        raise ValueError(f"unknown wall_form '{self.wall_form}'")

    def _conf_diag(self) -> np.ndarray:
        """U_conf(x) = clamp_strength·g(x), flattened to the ω-block ordering."""
        return (self.clamp_strength * self.wall_weight()).reshape(self.ndof)

    def _assemble_H(self):
        """Parent H (native-Laplacian blocks + on-site A1↔ω coupling) + the reactive
        confinement potential on the ω-block diagonal. Real diagonal ⇒ Hermitian ⇒
        unitary ⇒ energy conserved exactly."""
        H = super()._assemble_H()
        if self.clamp_strength == 0.0 or self.wall_form == "off":
            return H
        nd = self.ndof
        U = self._conf_diag()
        if self.winding_mode == "rigid_template":
            full = np.concatenate([np.zeros(nd), U])
        else:  # dispersive_vector: 4·nd state, ω = blocks 1,2,3
            full = np.concatenate([np.zeros(nd), U, U, U])
        return (H + sparse.diags(full, format="csr")).tocsr()

    def wall_energy(self) -> float:
        """V_clamp = ½·clamp_strength·Σ g(x)·|ω(x)|² — the reactive wall storage (the
        energy the winding must pay INTO the wall). The unitary-scheme analog of
        `cosserat_field_3d.py:1944` (impedance_hamiltonian V_clamp)."""
        g = self.wall_weight()
        return 0.5 * self.clamp_strength * float(np.sum(g * self._omega_amp() ** 2))
