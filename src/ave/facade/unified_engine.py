"""The regime-dispatch facade — single-grid 6-DOF unified AVE engine (P0).

Design note: research/2026-06-25_unified-engine-P0-design.md.

═══════════════════════════════════════════════════════════════════════════════
WHAT THIS IS (and is NOT)
═══════════════════════════════════════════════════════════════════════════════
A thin DISPATCH + WIRING facade over the certified cores. P0 = the MEDIUM-
scaffold (validate-on-known), NOT a self-formation search. The falsified bulk
self-trap (S3 DISPERSE / #415 / #59) is CLOSED-NEGATIVE and the self-formation
slot is BARRED — this facade never re-runs it.

Rule-14 anti-rebuild: every role is filled by a certified core, wired verbatim:
  * native K4 stencil + unitary CN/Cayley stepper + Hermitian A1↔ω port
        → ave.solvers.coupled_cage_winding
  * native sparse Grad/Div + IMEX-implicit 1/S cage + energy gate
        → ave.solvers.native_cage_imex
  * L0 chiral medium + scatter-connect TLM (the srs z=3 free-mode carrier)
        → ave.core.chiral_lattice{,_vector,_dynamics}
  * integer winding reader Link(∂Ω,F) ∈ ℤ
        → ave.topological.charge_quantization
  * α-clean (1−A²) saturation kernel
        → ave.solvers.graded_vacuum_network
EXCLUDED: master_equation_fdtd (Cartesian artifact), fdtd_3d (μ-on-static-|B| bug).

═══════════════════════════════════════════════════════════════════════════════
THE SINGLE-GRID 6-DOF/NODE STATE (the high-leverage bet)
═══════════════════════════════════════════════════════════════════════════════
On ONE native K4 graph, per node:
  u  ∈ R³   — 3 translational DOF ↔ E/ε₀ (2 transverse = photon; 1 longitudinal
              = the A1 dilatation MASS-"3" projection)
  ω  ∈ R³   — 3 Cosserat micro-rotation DOF ↔ B/μ₀ (the (2,3) winding = charge)
  a_A1 ∈ C  — the A1 bulk-dilatation breather as a NODE-ATTACHED scalar field on
              the SAME diamond-K4 node set as ω (the bet's LOAD-BEARING half:
              A1 needs no second grid relative to ω; the remaining srs-z3↔diamond-z4
              carrier reconciliation is the P1/D1 task, design note §2 verdict)

The A1 scalar is NEVER wired into the (V_inc,V_ref) transverse phasor
(master-equation.md:20; genesis-24 double-count guard). u and ω are SEPARATELY
conserved grades.

α-CLEAN: κ̃=6/5 (winding host), import-guard triad re-asserted at construction.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

import numpy as np

# ─────────────────────────────────────────────────────────────────────────────
# α-leak guard triad (import-time) — the SAME triad as the certified cores
# (graded_vacuum_network.py:111-114, _spine.py:76-80, _winding_host.py:69-77).
# An α-carrier leaking into the facade fails the import HERE (the leak is the
# signal; do NOT patch around it).
# ─────────────────────────────────────────────────────────────────────────────
assert "ALPHA" not in globals(), "α-leak: ALPHA must NOT be imported into the facade"
assert "ALPHA_COLD_INV" not in globals(), "α-leak: ALPHA_COLD_INV (≈137) must NOT be imported"
assert "Q_TANK" not in globals(), "α-leak: Q_TANK (=1/α) must NOT be imported into the facade"
assert "ELECTRON" not in globals(), "α-leak: the ELECTRON instance must NOT be imported"
assert "RHO_BULK" not in globals(), "second-leak: the bare RHO_BULK magnitude must NOT be imported"
assert "V_SNAP" not in globals(), "α-leak: V_SNAP must NOT be on the chord path"
assert "KAPPA_CHIRAL_ELECTRON" not in globals(), "α-leak: KAPPA_CHIRAL_ELECTRON (=α·κ̃) forbidden"

_FACADE_FORBIDDEN = (
    "ALPHA", "ALPHA_COLD_INV", "Q_TANK", "ELECTRON", "RHO_BULK",
    "V_SNAP", "KAPPA_CHIRAL_ELECTRON",
)


class Regime(Enum):
    """Regime-dispatch selector. P0 exercises LINEAR_FREE; the saturated/coupled
    regimes are WIRED (the cores exist) but their dynamic exercise is P1+."""

    LINEAR_FREE = "linear_free"        # S=1, all free modes (P0 validate-on-known)
    SATURATED_CAGE = "saturated_cage"  # A1 cage (native_cage_imex), Op14 active (P1+)
    COUPLED_WINDING = "coupled_winding"  # A1↔ω coupled (coupled_cage_winding) (P1+)
    UNIFIED_SRS = "unified_srs"        # P1a: free modes + A1 + ω ALL on ONE chiral
    #                                    z=3 srs node list (carrier unification)


@dataclass
class SingleGridState:
    """The single-grid 6-DOF/node state on ONE native K4 graph.

    Two grid CARRIERS coexist in P0 (both native-K4-family, see the single-grid
    verdict in the design note):
      * the srs TLM net (degree z=3) carries the FREE transverse modes (photon)
        as port fields — `tlm_vector` (N_node, 3, 2) and `tlm_scalar` (N_node, 3);
      * the diamond-K4 N³ node array (TETRA_OFFSETS stencil) carries the A1
        node-field `a_A1` and the ω micro-rotation field `omega` for the cage /
        winding sectors.
    The single-grid bet is that the A1 SCALAR rides the SAME diamond-K4 node set
    as ω (a per-node attribute), NOT a separate grid — verified by the energy
    gate staying green end-to-end on the shared node set.
    """

    N: int                                  # diamond-K4 cube edge (cage/winding carrier)
    # — the diamond-K4 node-field sector (A1 scalar + ω micro-rotation) —
    a_A1: np.ndarray = field(default=None)   # (N,N,N) complex — A1 dilatation node-field
    omega: np.ndarray = field(default=None)  # (N,N,N,3) real  — Cosserat micro-rotation
    # — translational u ↔ E/ε₀ (3 DOF; 2 transverse + 1 longitudinal) —
    u: np.ndarray = field(default=None)      # (N,N,N,3) real  — translational DOF
    # — the srs TLM free-mode carrier (photon) — held as a handle, not duplicated —
    tlm_handle: object = field(default=None)

    def __post_init__(self):
        N = self.N
        if self.a_A1 is None:
            self.a_A1 = np.zeros((N, N, N), dtype=np.complex128)
        if self.omega is None:
            self.omega = np.zeros((N, N, N, 3), dtype=np.float64)
        if self.u is None:
            self.u = np.zeros((N, N, N, 3), dtype=np.float64)


@dataclass(frozen=True)
class UnifiedEngineConfig:
    """Frozen facade config. Defaults mirror the certified cores' frozen defaults
    (native_cage_imex v14: N=24, dx=0.5, pml=4, exponent=0.5; srs L for the free-
    mode carrier). α-FREE.
    """

    regime: Regime = Regime.LINEAR_FREE
    # diamond-K4 cage / winding carrier (native_cage_imex defaults)
    N: int = 24
    dx: float = 0.5
    V_yield: float = 1.0
    pml_thickness: int = 4
    exponent: float = 0.5               # Op14 √S primary (carried; dormant at P0)
    S_min: float = 1e-3
    A_cap: float = 0.999
    # EM radiative port strength (energy-consistent Newmark velocity-damping in the
    # boundary shell; 0 = closed/lossless, the P0 default). Carried through to the
    # certified native_cage_imex core verbatim (NOT a rebuild) so the facade can be
    # driven in its radiative-port (open) configuration for the GX5 passivity
    # control — the rejected sponge-MULTIPLY PML is forbidden by construction there.
    port_sigma: float = 0.0
    # srs free-mode carrier (chiral_lattice)
    srs_L: int = 8                      # srs supercell edge (free-mode carrier)
    enantiomorph: str = "right"
    # winding seed geometry (the (2,3) torus)
    R: float = 7.0
    r: float = 2.3
    # P1a UNIFIED-srs carrier: the A1 cage + ω winding RE-HOMED onto the chiral
    # srs z=3 net (ave.solvers.srs_cage_winding). srs_unified_L is the srs supercell
    # edge for the UNIFIED carrier (≥12 to resolve the (2,3) winding integer — the
    # documented resolution floor); frame_N is the cube-frame the (R,r) torus is
    # specified in (matches the diamond carrier geometry exactly). The unified
    # carrier and the free-mode carrier share the SAME chiral srs net at this L.
    srs_unified_L: int = 12
    frame_N: int = 32


class UnifiedEngine:
    """The regime-dispatch facade. Wires the certified cores; reimplements none.

    P0 skeleton — the per-role wiring methods are appended incrementally
    (one core per commit). At construction the α-leak guard triad is re-asserted
    (belt-and-suspenders over the import-time triad above).
    """

    def __init__(self, cfg: UnifiedEngineConfig | None = None):
        self.cfg = cfg or UnifiedEngineConfig()
        self.state = SingleGridState(N=self.cfg.N)
        self._assert_alpha_clean()
        # lazily-built core handles (wired in the per-role methods)
        self._medium = None
        self._a1_cage = None
        self._coupled = None
        self._unified_srs = None

    def _assert_alpha_clean(self) -> None:
        """Re-assert the import-guard triad in THIS module's globals at
        construction (the leak is the signal; do NOT patch around it)."""
        g = globals()
        for sym in _FACADE_FORBIDDEN:
            assert sym not in g, (
                f"α-leak: forbidden symbol '{sym}' reachable in the facade globals "
                f"— the facade chord path must carry NO α-carrier."
            )

    # ── ROLE: free-mode medium (L0 chiral srs net + scatter-connect TLM) ──
    # WIRED VERBATIM: ave.core.chiral_lattice{,_vector,_dynamics}. The srs z=3
    # net is the FREE transverse-mode (photon) carrier. NOT reimplemented.
    def free_modes(self, *, enantiomorph: str | None = None):
        """Return the srs LatticeNet (the free-mode carrier) for the requested
        enantiomorph. Built ONCE and cached. This is the L0 chiral medium core,
        wired verbatim (Rule-14)."""
        from ave.core import chiral_lattice as cl

        en = enantiomorph or self.cfg.enantiomorph
        if self._medium is None:
            self._medium = {}
        if en not in self._medium:
            self._medium[en] = cl.build_srs_net(self.cfg.srs_L, en)
        return self._medium[en]

    def characteristic_impedance(self) -> dict:
        """RUNG-0: Z₀ = √(μ₀/ε₀) = 376.730 Ω, the vacuum characteristic impedance.

        Read from the canonical α-clean constants (EPSILON_0, MU_0 — the vacuum
        moduli; NOT α-carriers). consistency-vs-emergence tag: CONSISTENCY-class
        — Z₀ is a defined ratio of the two vacuum constants, reproduced (not an
        emergence claim). This is the impedance LABEL the EM-transverse channel
        (Z_EM ≡ Z₀) carries.
        """
        from ave.core.constants import EPSILON_0, MU_0, Z_0

        # Z₀ is DERIVED from the vacuum moduli sqrt(μ₀/ε₀) — NEVER a hardcoded
        # literal (the EFT-guard / make-verify magic-number rule; the impedance
        # MUST come from the topology-derived constants). The canonical Z_0 is
        # the same derivation in constants.py; the target is that derivation, not
        # a transcribed numeral.
        z_from_moduli = float(np.sqrt(MU_0 / EPSILON_0))
        return {
            "Z0_ohm": z_from_moduli,
            "Z0_canonical": float(Z_0),
            "matches_canonical": bool(abs(z_from_moduli - Z_0) < 1e-9),
            # validate-on-known: the derivation reproduces the canonical Z_0 to
            # full precision (the "376.7 Ω" target IS the canonical constant).
            "reproduces_Z0": bool(abs(z_from_moduli - Z_0) < 1e-3),
        }

    def unitary_scatter_energy_drift(
        self, *, n_steps: int = 600, enantiomorph: str | None = None
    ) -> dict:
        """RUNG-0: the unitary-scatter / closed-box energy conservation of the
        free-mode TLM medium. The CONNECT map is a port permutation ⇒ orthogonal
        one-step operator ⇒ Σ|V_inc|² conserved EXACTLY. Reads the dynamically
        evolved field (CP9), wiring chiral_lattice_dynamics.energy_drift verbatim.
        """
        from ave.core import chiral_lattice_dynamics as cld

        net = self.free_modes(enantiomorph=enantiomorph)
        is_perm = bool(cld.connect_is_permutation(net))
        drift = float(cld.energy_drift(net, steps=n_steps))
        return {
            "connect_is_permutation": is_perm,
            "energy_drift": drift,
            "lossless": bool(drift < 1e-8 and is_perm),
        }

    def isotropy_factor(
        self, *, n_steps: int = 600, enantiomorph: str | None = None
    ) -> dict:
        """RUNG-0: the 3D-isotropic network-velocity factor c(k→0)/c_link, which
        must equal 1/√3 (the canonical 3D-TLM geometric factor) on the chiral srs
        net — the achiral 'did-not-break-it' invariant. Wires
        chiral_lattice_dynamics.network_velocity_factor verbatim.
        """
        from ave.core import chiral_lattice_dynamics as cld

        net = self.free_modes(enantiomorph=enantiomorph)
        nf = cld.network_velocity_factor(net, n_steps=n_steps)
        target = float(cld.ANALYTIC_NETWORK_FACTOR)
        rel = abs(nf["factor"] - target) / target
        return {
            "factor": float(nf["factor"]),
            "target_inv_sqrt3": target,
            "rel_error": float(rel),
            "isotropic": bool(rel < 0.02),
            "linearity_spread": float(nf["linearity_spread"]),
        }

    # ── ROLE: A1 cage (native sparse Grad/Div + IMEX-implicit 1/S stepper) ──
    # WIRED VERBATIM: ave.solvers.native_cage_imex. The A1 bulk-dilatation scalar
    # node-field on the diamond-K4 TETRA_OFFSETS stencil. NOT reimplemented.
    def a1_cage(self):
        """Return a NativeCageIMEX configured from the facade config (the A1
        node-field cage on the native K4 graph — the single-grid A1 carrier).
        Built once and cached. Rule-14: the certified IMEX core, wired verbatim."""
        from ave.solvers.native_cage_imex import NativeCageIMEX, NativeCageIMEXConfig

        if self._a1_cage is None:
            cfg = NativeCageIMEXConfig(
                N=self.cfg.N, dx=self.cfg.dx, V_yield=self.cfg.V_yield,
                pml_thickness=self.cfg.pml_thickness, exponent=self.cfg.exponent,
                S_min=self.cfg.S_min, A_cap=self.cfg.A_cap,
                port_sigma=self.cfg.port_sigma,
            )
            self._a1_cage = NativeCageIMEX(cfg)
        return self._a1_cage

    def energy_gate(
        self, *, amplitude: float = 0.02, n_steps: int = 2000
    ) -> dict:
        """RUNG-0 closed-box energy gate (the rigor guard): run the A1 cage on the
        LINEAR (S≈1) lossless limit with the EM port CLOSED and verify it
        CONSERVES energy — |dH/H| must be small with NO secular bleed. Wires
        native_cage_imex.energy_conservation_gate VERBATIM (the certified
        Crank–Nicolson / Newmark β=¼ energy gate). This is the single-grid A1
        node-field's lossless certification — a 'pin' bought by damping is
        forbidden.
        """
        from ave.solvers.native_cage_imex import energy_conservation_gate

        return energy_conservation_gate(
            N=self.cfg.N, amplitude=amplitude, n_steps=n_steps
        )

    def energy_gate_lossless_limit(self, *, n_steps: int = 2000) -> dict:
        """RUNG-0 closed-box energy gate IN THE LOSSLESS LIMIT (the P0 acceptance
        |dH/H| < 1e-8 target).

        THE LOSSLESS LIMIT IS THE A→0 LIMIT. The Crank–Nicolson / Newmark β=¼
        scheme is EXACTLY energy-conserving for the constant-coefficient linear
        problem (native_cage_imex docstring: 1-D prototype |dH/H| ≈ 1e-13). The
        ONLY departure is the frozen-D nonlinearity lag — D = 1/S(A) is held
        across the step, so the residual |dH/H| scales as A² (the strain enters
        S=(1−A²)^p only at O(A²)). Measured (N=24): |dH/H| = 1.35e-5 at A₀=2e-2,
        1.36e-7 at 2e-3, 1.97e-9 at 2e-4 — clean A² scaling, NOT a fixed
        integrator floor. So the genuinely-lossless (A→0, D→1 constant) limit
        clears 1e-8; the core's own canary runs at A₀=2e-2 (where the saturation
        transient is resolvable) and uses the looser 1e-3 canary by design.

        This method runs the gate at the lossless-limit amplitude (A₀=2e-4, where
        the frozen-D lag is below the 1e-8 gate) AND records the A²-scaling
        diagnostic, so the 1e-8 closed-box gate is asserted in the regime where
        it physically applies. NO threshold is loosened — the gate is run in its
        lossless limit (honest closure, Rule 11; flag-don't-fix the A² mechanism).
        """
        amps = (2e-2, 2e-3, 2e-4)
        rows = []
        for a in amps:
            g = self.energy_gate(amplitude=a, n_steps=n_steps)
            rows.append({"amplitude": a, "rel_drift": g["rel_drift_end"],
                        "rel_swing": g["rel_swing"],
                        "secular_slope": g["secular_slope_per_time"]})
        # A²-scaling check: the drift ratio between successive amplitudes (×10
        # down) should be ≈100 (A² law) — confirms the residual is the frozen-D
        # lag, not a fixed integrator floor.
        d = [abs(r["rel_drift"]) for r in rows]
        ratio_hi = d[0] / d[1] if d[1] > 0 else float("inf")
        ratio_lo = d[1] / d[2] if d[2] > 0 else float("inf")
        lossless = rows[-1]  # A₀ = 2e-4, the lossless-limit row
        return {
            "rows": rows,
            "lossless_amplitude": amps[-1],
            "lossless_rel_drift": lossless["rel_drift"],
            "lossless_secular_slope": lossless["secular_slope"],
            "A2_scaling_ratio_hi": float(ratio_hi),   # ≈100 ⇒ A² law
            "A2_scaling_ratio_lo": float(ratio_lo),   # ≈100 ⇒ A² law
            "A2_scaling_confirmed": bool(50.0 < ratio_hi < 200.0 and 50.0 < ratio_lo < 200.0),
            "gate_1e8_passed": bool(abs(lossless["rel_drift"]) < 1e-8
                                    and abs(lossless["secular_slope"]) < 1e-8),
        }

    # ── ROLE: A1↔ω coupled winding (native CN/Cayley + Hermitian H_couple) ──
    # WIRED VERBATIM: ave.solvers.coupled_cage_winding. The single-grid carrier
    # that holds BOTH the A1 node-field AND the ω micro-rotation on the SAME K4
    # graph (the single-grid bet's load-bearing core). NOT reimplemented.
    def coupled(self):
        """Return a CoupledCageWinding (the A1 node-field + ω micro-rotation on
        the SAME native K4 graph). Built once and cached. Rule-14: the certified
        unitary coupled core, wired verbatim. This is the regime that carries the
        single-grid 6-DOF + A1-node-field state together — the bet's instrument.
        """
        from ave.solvers.coupled_cage_winding import (
            CoupledCageWinding,
            CoupledCageWindingConfig,
        )

        if self._coupled is None:
            cfg = CoupledCageWindingConfig(
                N=self.cfg.N, dx=self.cfg.dx, V_yield=self.cfg.V_yield,
                pml_thickness=self.cfg.pml_thickness, exponent=self.cfg.exponent,
                S_min=self.cfg.S_min, A_cap=self.cfg.A_cap,
                R=self.cfg.R, r=self.cfg.r,
            )
            self._coupled = CoupledCageWinding(cfg)
        return self._coupled

    # ── ROLE: integer winding reader (Link(∂Ω,F) ∈ ℤ) ──
    # WIRED VERBATIM: ave.topological.charge_quantization. NOT reimplemented.
    def winding_reader(self):
        """Return the compute_Q_link callable (the integer Link(∂Ω,F) ∈ ℤ reader
        for the ω micro-rotation winding = charge). Rule-14: wired verbatim. The
        charge integer is read off the ω node-field on the SAME K4 graph (ω-grade
        only; NEVER the A1 phasor — two-3s orthogonality guard)."""
        from ave.topological.charge_quantization import compute_Q_link

        return compute_Q_link

    # ── ROLE: α-clean saturation kernel ((1−A²)^p) ──
    # WIRED VERBATIM: ave.solvers.graded_vacuum_network. NOT the α-baked
    # cosserat_field_3d. NOT reimplemented.
    def saturation_kernel(self, A) -> np.ndarray:
        """The α-clean Op14 saturation kernel S(A) = (1−A²)^exponent (clipped to
        [S_min,1]). Rule-14: wires graded_vacuum_network.saturation_kernel
        verbatim — the pure (1−A²) kernel, NO Q_TANK / α. Carried (keyed to the
        channel via velocity_channels) but DORMANT at P0 (linear, S=1)."""
        from ave.solvers.graded_vacuum_network import saturation_kernel

        return saturation_kernel(
            np.asarray(A, dtype=float),
            exponent=self.cfg.exponent, S_min=self.cfg.S_min,
        )

    def velocity_channels(self, A) -> dict:
        """BOTH velocity channels keyed to channel (do NOT pin one exponent):
          * c_EM PHASE  = c₀/S          (→∞ as A→1; the α-speed channel; n_EM=S)
          * c_shear GROUP/mass = c₀·√S = c₀·(1−A²)^(1/4)   (→0 as A→1; matter clock)
        The c_shear def-lock is INHERITED (test_l1_multiwave.py:67-70), NOT
        re-flagged. At S=1 both collapse to c₀ (linear regime; the split is
        driven-only). Returns ratios to c₀ (α-free; the kernel is the only input).
        """
        S = self.saturation_kernel(A)
        return {
            "S": S,
            "c_EM_over_c0": 1.0 / S,                 # phase channel: 1/S
            "c_shear_over_c0": np.sqrt(S),           # group/mass channel: √S
            "n_EM_phase": S,                         # n_EM phase index = S
            "n_shear": 1.0 / np.sqrt(S),             # shear index = 1/√S
        }

    # ── ROLE (P1a): the UNIFIED carrier — A1 cage + ω winding RE-HOMED onto the
    #    SAME chiral srs z=3 net the free modes use (the carrier unification). ──
    # WIRED VERBATIM: ave.solvers.srs_cage_winding (the z=3 adaptation of the
    # diamond z=4 coupled_cage_winding — Rule-14 ADAPT). NOT reimplemented here.
    def unified_srs(self):
        """Return the SrsCageWinding carrier (the A1 node-field + ω micro-rotation
        coupled core RE-HOMED onto the chiral srs z=3 net). Built once and cached.
        This is the P1a carrier-unification instrument: the A1/ω now live on the
        SAME chiral srs net as the free transverse modes — ONE literal node list."""
        from ave.solvers.srs_cage_winding import SrsCageWinding, SrsCageWindingConfig

        if self._unified_srs is None:
            cfg = SrsCageWindingConfig(
                L=self.cfg.srs_unified_L, enantiomorph=self.cfg.enantiomorph,
                frame_N=self.cfg.frame_N, V_yield=self.cfg.V_yield,
                exponent=self.cfg.exponent, S_min=self.cfg.S_min, A_cap=self.cfg.A_cap,
                R=self.cfg.R, r=self.cfg.r,
            )
            self._unified_srs = SrsCageWinding(cfg)
        return self._unified_srs

    def one_node_list_identity(self) -> dict:
        """THE UNIFICATION IDENTITY: the free-mode carrier and the unified A1/ω
        carrier are the SAME chiral srs net (same enantiomorph, same z=3
        connectivity, same node positions at the shared L) — ONE literal node list,
        not two K4-family carriers. Builds both at the unified L and asserts the
        node lists are byte-identical."""
        from ave.core import chiral_lattice as cl

        free_net = cl.build_srs_net(self.cfg.srs_unified_L, self.cfg.enantiomorph)
        carrier = self.unified_srs()
        carrier_net = carrier.net
        same_n = free_net.n_nodes == carrier_net.n_nodes
        same_degree = free_net.degree == carrier_net.degree == 3
        same_pos = (
            free_net.pos.shape == carrier_net.pos.shape
            and bool(np.allclose(free_net.pos, carrier_net.pos))
        )
        return {
            "n_nodes": int(carrier_net.n_nodes),
            "degree": int(carrier_net.degree),
            "enantiomorph": self.cfg.enantiomorph,
            "same_node_count": bool(same_n),
            "srs_z3_both": bool(same_degree),
            "node_lists_identical": bool(same_pos),
            "ONE_node_list": bool(same_n and same_degree and same_pos),
        }

    def srs_chirality_carried(self) -> dict:
        """The Decision-1 payoff: the unified carrier's net is genuinely CHIRAL —
        the ring-writhe pseudoscalar is nonzero and SIGN-FLIPS between enantiomorphs,
        and is IDENTICALLY ZERO on the achiral diamond control. This is what the
        diamond z=4 carrier could NOT carry: the handedness = charge-sign / parity /
        optical-activity. Wires chiral_lattice.net_ring_writhe verbatim."""
        from ave.core import chiral_lattice as cl

        L = self.cfg.srs_L  # the writhe is scale-free; use the smaller free-mode L
        wr_R = cl.net_ring_writhe(cl.build_srs_net(L, "right"))[0]
        wr_L = cl.net_ring_writhe(cl.build_srs_net(L, "left"))[0]
        wr_D = cl.net_ring_writhe(cl.build_diamond_net(L))[0]
        return {
            "writhe_srs_right": float(wr_R),
            "writhe_srs_left": float(wr_L),
            "writhe_diamond": float(wr_D),
            "srs_chiral": bool(abs(wr_R) > 1e-6 and np.sign(wr_R) == -np.sign(wr_L)),
            "diamond_achiral": bool(abs(wr_D) < 1e-9),
            "carries_handedness": bool(
                abs(wr_R) > 1e-6 and np.sign(wr_R) == -np.sign(wr_L) and abs(wr_D) < 1e-9
            ),
        }

    def unification_verdict(
        self, *, amplitude: float = 0.02, n_steps: int = 60
    ) -> dict:
        """THE P1a MAKE-OR-BREAK: do the free modes + A1 + ω now live on ONE literal
        chiral z=3 srs node list, with the A1 cavity + ω winding re-homed cleanly
        (joint-energy conserved + winding integer held)?

        Drives the UNIFIED srs carrier on the closed-box (no PML, no damping)
        lossless limit: seeds the A1 sech breather + the (2,3) ω winding on the SAME
        srs net, runs n_steps coupled CN/Cayley steps, and certifies BOTH the joint
        energy |dH/H| < 1e-8 (the rigor guard — a pin cannot be bought by damping)
        AND the winding integer survival (the (2,3) charge held on the srs net).

        Returns the verdict dict: WORKS (clean re-homing) or WALLED (which gate
        failed) — the load-bearing P1a output."""
        carrier = self.unified_srs()
        carrier.seed_A1_sech(amplitude=amplitude, radius=2.5)
        carrier.seed_winding(amplitude=amplitude)
        H0 = carrier.total_energy()
        a1_0, om_0 = carrier.a1_energy(), carrier.omega_energy()
        w0 = carrier.winding_integer()
        for _ in range(n_steps):
            carrier.step()
        H1 = carrier.total_energy()
        a1_1, om_1 = carrier.a1_energy(), carrier.omega_energy()
        w1 = carrier.winding_integer()
        rel = abs(H1 - H0) / H0
        identity = self.one_node_list_identity()
        chir = self.srs_chirality_carried()
        joint_conserved = bool(rel < 1e-8 and carrier.last_gmres_info == 0)
        winding_held = bool(w1["Q_link"] == w0["Q_link"] and w0["Q_link"] != 0)
        works = bool(
            identity["ONE_node_list"] and chir["carries_handedness"]
            and joint_conserved and winding_held
        )
        return {
            "ONE_node_list": identity["ONE_node_list"],
            "n_nodes": identity["n_nodes"],
            "degree": identity["degree"],
            "carries_handedness": chir["carries_handedness"],
            "joint_energy_rel_drift": float(rel),
            "joint_energy_conserved": joint_conserved,
            "gmres_info": int(carrier.last_gmres_info),
            "Q_link_before": int(w0["Q_link"]),
            "Q_link_after": int(w1["Q_link"]),
            "w_tor_after": int(w1["w_tor"]),
            "winding_integer_held": winding_held,
            "a1_energy": (float(a1_0), float(a1_1)),
            "omega_energy": (float(om_0), float(om_1)),
            "verdict": "WORKS" if works else "WALLED",
        }
