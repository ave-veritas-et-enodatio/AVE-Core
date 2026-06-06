"""Observable-Battery infrastructure — the 14-channel physical readout for any
AVE simulation (PREREG ``research/2026-06-05_observable-battery-infrastructure-prereg.md``).

ONE reusable ``ObservableBattery`` instruments **every** AVE sim with the full
physical readout; a ``BatteryObserver(Observer)`` wraps it onto the
``VacuumEngine3D`` per-step / post-run hooks; ``ObservableReport`` is the
serializable per-sim record. The sweep harness lives in ``observable_sweep.py``.

Library discipline (``ave-module-library-discipline``): this module **composes**
the shipped diagnostics by import + call — it **redefines none** (KEEP-BOTH):

  * ``universal_reflection`` / ``universal_power_transmission`` /
    ``universal_spectral_analysis``  (``ave.core.universal_operators``)
  * ``compute_all_invariants``                       (``ave.core.boundary_invariants``)
  * ``EnergyBudgetObserver`` / ``TopologyObserver`` /
    ``RegimeClassifierObserver`` ``_capture`` bodies  (``ave.topological.vacuum_engine``)
  * ``_beltrami_helicity`` / ``extract_hopf_charge`` /
    ``find_soliton_centroids`` / ``extract_shell_radii`` /
    ``kinetic_energy``                                (``ave.topological.cosserat_field_3d``)
  * ``get_helicity_density`` / ``total_energy``        (``ave.core.k4_tlm``)
  * the coordinate-correct (2,3) extractor
    ``extract_2_3_spatial`` + ``shell_params_from_field`` +
    ``field_direction_nhat`` + ``fibre_phase_cell`` +
    ``knot_tangent_port_weights`` + ``is_2_3``
    (``src/scripts/vol_1_foundations/r10_2_3_winding_extractor_coordinate.py``)

NEW code only for the genuinely-missing reads: Γ reconstruction (the engine
never stores its in-flight Γ — ``k4_tlm.py``:410 is a local var), X_C/X_L
reactances, Θ_RP angle, the 7-mode energy split, ρ_Q charge density, and the
composing class + observer + sweep.

Honesty tags (``ave-driver-script-honesty`` / ``ave-evidence-framing``): every
channel carries a ``source`` ∈ {native-read, composed-diagnostic,
first-pass-proxy, engineering-input}. Mandatory: boundary Q/J = first-pass-proxy;
reactance ω = engineering-input. This is measurement infrastructure +
tool-validation (``consistency-vs-emergence``) — NOT an emergence or α claim;
forward reads only, no fits / no target-matching.

Constants come strictly from ``ave.core.constants`` (``ave-canonical-source``);
zero hardcoded physical literals.
"""

from __future__ import annotations

import enum
from dataclasses import dataclass, field, asdict
from typing import Any, Optional

import numpy as np

# ── Canonical constants (ave-canonical-source — zero hardcoded literals) ──────
from ave.core.constants import (
    ALPHA,      # fine-structure constant (dimensionless)
    Z_0,        # vacuum characteristic impedance [Ω]
    PHI,        # golden ratio (R/r torus aspect)
    V_SNAP,     # snap voltage = m_e c²/e [V]
    L_NODE,     # node length ℓ_NODE [m]
    C_0,        # speed of light [m/s]
    V_YIELD,    # yield voltage √α · V_SNAP [V]  (boundary-invariant strain ref)
)

# ── Shipped diagnostics COMPOSED by import (KEEP-BOTH — never redefined) ──────
# These two live in ave.core (pure-numpy, no JAX/Cosserat), so they are safe to
# import at module level even for a pure-FDTD run. The heavier topological
# readers (Cosserat / r10 (2,3) extractor) are lazy-imported inside extract_full.
from ave.core.universal_operators import (
    universal_reflection as _universal_reflection,           # Op3   (universal_operators:118)
    universal_power_transmission as _universal_power_transmission,  # Op17  (universal_operators:833)
    universal_spectral_analysis as _universal_spectral_analysis,    # Op7   (universal_operators:355)
)

# r10 coordinate-correct (2,3) extractor functions — lazy-imported + cached
# (the module needs the scripts path + its own JAX-stack dep). COMPOSED.
_R10_FUNCS: dict[str, Any] = {}


def _universal_power_transmission_from_gamma(gamma: float) -> float:
    """T² from a reflection coefficient, via the shipped Op17 reduction
    T² = 1 − Γ² (universal_operators:843). Kept as a thin adapter because the
    shipped operator takes impedances; here we already hold Γ from the rebuilt
    bond reflection, so T² = 1 − Γ² is the algebraic identity it computes."""
    return float(np.clip(1.0 - gamma ** 2, 0.0, 1.0))


# ── Lazy-imported topological diagnostics (KEEP-BOTH — composed, not copied) ──
# These live in ave.topological (need the Cosserat/JAX stack) so they are
# imported on FIRST USE inside the heavy reads — a pure-FDTD run never triggers
# them. Cached at module level after the first successful import.
_TOPO_OBSERVERS: dict[str, Any] = {}


def _lazy_topo_observers() -> dict[str, Any]:
    """Import + cache the three shipped Observers' classes (for ._capture
    composition) and return them. Redefines none — composes by import."""
    if not _TOPO_OBSERVERS:
        from ave.topological.vacuum_engine import (
            EnergyBudgetObserver,
            RegimeClassifierObserver,
            TopologyObserver,
        )
        _TOPO_OBSERVERS.update(
            EnergyBudgetObserver=EnergyBudgetObserver,
            RegimeClassifierObserver=RegimeClassifierObserver,
            TopologyObserver=TopologyObserver,
        )
    return _TOPO_OBSERVERS


def _EnergyBudgetObserver():
    """Shipped EnergyBudgetObserver (vacuum_engine:664) — composed by import."""
    return _lazy_topo_observers()["EnergyBudgetObserver"]()


def _RegimeClassifierObserver():
    """Shipped RegimeClassifierObserver (vacuum_engine:392) — composed."""
    return _lazy_topo_observers()["RegimeClassifierObserver"]()


def _TopologyObserver(**kw):
    """Shipped TopologyObserver (vacuum_engine:618) — composed."""
    return _lazy_topo_observers()["TopologyObserver"](**kw)


# ─────────────────────────────────────────────────────────────────────────────
# Honesty-tag enum (ave-evidence-framing): the provenance of every channel.
# ─────────────────────────────────────────────────────────────────────────────
class Source(str, enum.Enum):
    """Provenance tag for an observable channel. Carried on every read so a
    proxy is never silently read as rigorous (ave-evidence-framing)."""

    NATIVE = "native-read"           # direct engine native-state read
    COMPOSED = "composed-diagnostic"  # composed from a shipped diagnostic
    PROXY = "first-pass-proxy"        # geometric stand-in (e.g. Q/J component-count)
    ENGINEERING = "engineering-input"  # depends on an engineering choice (e.g. drive-ω)


# ─────────────────────────────────────────────────────────────────────────────
# Coordinate-class tag (phase-space-coordinate-check): the coordinate frame a
# channel measures in, so real-space reads are never compared against
# phase-space φ² predictions (A46).
# ─────────────────────────────────────────────────────────────────────────────
class Coord(str, enum.Enum):
    REAL = "real-space"          # lattice-Cartesian / physical-space read
    PHASE = "phase-space"        # impedance / C↔L / U(1)-fibre read
    SCALAR = "scalar"            # field-magnitude scalar (no coordinate frame)
    REAL_VS_PHASE = "real-vs-phase"  # an angle BETWEEN a real-space + phase-space axis


# ─────────────────────────────────────────────────────────────────────────────
# Per-channel tag table — the §1 prereg honesty + coordinate tags, frozen here
# so the report can self-describe its provenance without re-deriving it.
# ─────────────────────────────────────────────────────────────────────────────
CHANNEL_TAGS: dict[str, dict[str, str]] = {
    "reflection":   {"source": Source.NATIVE.value,      "coord": Coord.PHASE.value},          # 1 Γ (HEADLINE)
    "power_split":  {"source": Source.NATIVE.value,      "coord": Coord.PHASE.value},          # 2 R²/T²
    "reactance_XC": {"source": Source.ENGINEERING.value, "coord": Coord.PHASE.value},          # 3 X_C (ω engineering-input)
    "reactance_XL": {"source": Source.ENGINEERING.value, "coord": Coord.PHASE.value},          # 4 X_L (ω engineering-input)
    "theta_RP":     {"source": Source.NATIVE.value,      "coord": Coord.REAL_VS_PHASE.value},  # 5 real↔phase angle
    "winding_2_3":  {"source": Source.NATIVE.value,      "coord": Coord.REAL.value},           # 6 (2,3) winding (+confidence)
    "energy7":      {"source": Source.NATIVE.value,      "coord": Coord.REAL.value},           # 7 7-mode split
    "energy_budget": {"source": Source.COMPOSED.value,   "coord": Coord.SCALAR.value},         # 8 budget + retention
    "boundary_MQJ": {"source": Source.NATIVE.value,      "coord": Coord.SCALAR.value},         # 9 M native; Q/J proxy (see sub-tags)
    "helicity":     {"source": Source.NATIVE.value,      "coord": Coord.REAL.value},           # 10 Beltrami helicity
    "hopf":         {"source": Source.NATIVE.value,      "coord": Coord.REAL.value},           # 11 Hopf charge + R/r
    "regime":       {"source": Source.NATIVE.value,      "coord": Coord.SCALAR.value},         # 12 saturation / regime
    "charge_density": {"source": Source.NATIVE.value,    "coord": Coord.REAL.value},           # 13 ρ_Q density
    "dispersion":   {"source": Source.NATIVE.value,      "coord": Coord.SCALAR.value},         # 14 spectral dispersion (DSP)
}

# Mandatory sub-channel tags (prereg §5): boundary Q/J are first-pass-proxy even
# though channel 9's M is a native read; the C↔L diag winding is dynamics-gated.
SUBCHANNEL_TAGS: dict[str, str] = {
    "boundary_MQJ.M": Source.NATIVE.value,    # ∫(n−1)dV — mass = integrated strain (rigorous geometry)
    "boundary_MQJ.Q": Source.PROXY.value,     # component-count stand-in, NOT the winding (Axiom 2)
    "boundary_MQJ.J": Source.PROXY.value,     # MOI-anisotropy stand-in, NOT the (2,3) angular momentum
    "winding_2_3.diag_CL_w2": Source.PROXY.value,  # non-degenerate only once Φ_link develops quadrature
    "reactance.omega": Source.ENGINEERING.value,   # drive-ω, not the soliton's ω_C = c/ℓ_node
}


# ─────────────────────────────────────────────────────────────────────────────
# ObservableReport — the serializable per-sim record.
# ─────────────────────────────────────────────────────────────────────────────
@dataclass
class ObservableReport:
    """One simulation's full physical readout.

    ``scalar_history`` holds the per-step cheap-scalar channels (cadence-filtered)
    — mirrors the shipped Observer.history pattern. ``full`` holds the heavy
    post-run field-walks (run ONCE on the converged state). ``analysis`` holds
    the forward per-sim classification (OPEN/SHORT, eigenmode/trajectory, (2,3)-
    hosted, LC-matched, regime) — every verdict a forward read off native state.
    ``metadata`` records the engine flags (op3/nonlinear, op14 mode, N, PML, …),
    the honesty tags, and the coordinate tags so a Γ≈0 is never misread.
    """

    name: str = ""
    config: dict[str, Any] = field(default_factory=dict)
    # per-step cheap scalar channels, each a list of dicts {"t": …, …}
    scalar_history: dict[str, list] = field(default_factory=dict)
    # heavy post-run field-walk channels (run once on converged state)
    full: dict[str, Any] = field(default_factory=dict)
    # forward per-sim classification verdicts
    analysis: dict[str, Any] = field(default_factory=dict)
    # engine flags, honesty tags, coordinate tags
    metadata: dict[str, Any] = field(default_factory=dict)
    # honesty / coordinate tag table (frozen copy for self-description)
    tags: dict[str, Any] = field(default_factory=lambda: {
        "channels": CHANNEL_TAGS,
        "subchannels": SUBCHANNEL_TAGS,
    })
    # channels that came back honestly INCONCLUSIVE (cannot be computed)
    inconclusive: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        """JSON-serializable dict (numpy → python via the battery's _jsonify)."""
        return _jsonify(asdict(self))

    def latest_scalar(self, channel: str) -> Optional[dict]:
        """The most-recent cheap-scalar capture for a channel, or None."""
        h = self.scalar_history.get(channel)
        return h[-1] if h else None


# ─────────────────────────────────────────────────────────────────────────────
# JSON helper — numpy → python recursively (used by ObservableReport.to_dict
# and the sweep harness). Kept local to avoid a dependency.
# ─────────────────────────────────────────────────────────────────────────────
def _jsonify(obj: Any) -> Any:
    if isinstance(obj, dict):
        return {str(k): _jsonify(v) for k, v in obj.items()}
    if isinstance(obj, (list, tuple)):
        return [_jsonify(v) for v in obj]
    if isinstance(obj, (np.floating,)):
        return float(obj)
    if isinstance(obj, (np.integer,)):
        return int(obj)
    if isinstance(obj, (np.bool_,)):
        return bool(obj)
    if isinstance(obj, np.ndarray):
        return _jsonify(obj.tolist())
    if isinstance(obj, enum.Enum):
        return obj.value
    return obj


# ─────────────────────────────────────────────────────────────────────────────
# ObservableBattery — the 14-channel instrument. Steps 2-5 fill the channel
# methods; Step 6 wires BatteryObserver; this is the Step-1 skeleton shell.
# ─────────────────────────────────────────────────────────────────────────────
class ObservableBattery:
    """The 14-channel physical readout for an AVE simulation.

    Two read modes (prereg §3), mirroring the shipped cheap-scalar-history /
    heavy-topology-once pattern:

      * ``sample_cheap(engine)`` — O(N) scalar channels, called per-step by
        ``BatteryObserver`` (cadence-filtered): Γ reductions, reactances, E7,
        budget, regime, helicity, Q_hopf.
      * ``extract_full(engine)`` — the expensive field-walks, run ONCE on the
        converged state: (2,3) shell-walk, M/Q/J, R/r, ρ_Q, dispersion FFT.

    Engine-agnostic (lives in ``core/``); the topological readers are
    lazy-imported so a pure-FDTD run doesn't require the Cosserat/JAX stack.
    """

    def __init__(
        self,
        pml_thickness: int = 0,
        reactance_omega: float = 1.0,
        probe_history: Optional[list] = None,
    ):
        # PML cell exclusion (A-Rule 10 corollary): top-K field-density reads
        # must filter PML cells before argpartition — they return frozen-
        # absorbing artifact, not interior physics.
        self.pml_thickness = int(pml_thickness)
        # Reactance angular frequency — ENGINEERING-INPUT (prereg §5 mandatory
        # tag): the drive-ω, NOT the soliton's own ω_C = c/ℓ_node. Convergence
        # of a measured ring frequency to ω_C is itself an electron-check, but
        # v1 uses the config drive-ω and tags it.
        self.reactance_omega = float(reactance_omega)
        # Accumulated probe series for the post-run dispersion FFT (#14).
        self.probe_history: list = list(probe_history) if probe_history else []

    # ── canonical constants surfaced for downstream self-description ──────────
    CONSTANTS = {
        "ALPHA": ALPHA,
        "Z_0": Z_0,
        "PHI": PHI,
        "V_SNAP": V_SNAP,
        "L_NODE": L_NODE,
        "C_0": C_0,
        "V_YIELD": V_YIELD,
    }

    # K4 port shifts (A→B direction vectors per port) — MUST mirror the engine's
    # own convention so the rebuilt Γ matches the in-flight bond reflection.
    # Source: ave.core.k4_tlm.K4Lattice3D._connect_all port_shifts (k4_tlm:378).
    # Each entry rolls B's value to A's location: np.roll(field, shift, axes).
    _PORT_SHIFTS = (
        (-1, -1, -1),  # Port 0: B at (+1,+1,+1)
        (-1, +1, +1),  # Port 1: B at (+1,-1,-1)
        (+1, -1, +1),  # Port 2: B at (-1,+1,-1)
        (+1, +1, -1),  # Port 3: B at (-1,-1,+1)
    )

    # ─────────────────────────────────────────────────────────────────────────
    # CHANNEL 1 — Γ reflection coefficient (THE HEADLINE).
    # ─────────────────────────────────────────────────────────────────────────
    def _reflection(self, engine) -> dict:
        """Rebuild the in-flight reflection coefficient Γ per directed A→B bond.

        The engine NEVER stores its in-flight Γ — at ``k4_tlm.py``:410 it is a
        local variable inside ``_scatter_all`` (``gamma = (z_B_at_A − z_A_own) /
        (z_B_at_A + z_A_own + eps)``). We rebuild it from the PERSISTENT
        ``z_local_field`` (``k4_tlm.py``:294, ``Z_eff = 1/√S = 1/(1−A²)^¼``) via
        ``np.roll(port_shifts)`` + ``universal_reflection`` — COMPOSED, never
        redefined. To mirror the engine's A→B convention exactly we call
        ``universal_reflection(z_A_own, z_B_at_A)`` = ``(z_B − z_A)/(z_B + z_A)``.

        Physical reading (prereg §1 #1 / §2 #2): **the reflecting boundary IS
        matter.** Cold vacuum is a uniform Z₀ → Γ=0 (transparent); Γ≠0 only
        where saturation bends S(A). The reduction the substrate cares about is
        **Γ_at_max_A2_bond** — the boundary condition at the most-saturated bond:

            sign(Γ_at_max_A2) = +1  →  antinode / OPEN  (Z→∞, mass-closure)
            sign(Γ_at_max_A2) = −1  →  node     / SHORT (clamped, primer)

        Only meaningful with Op3/Op14 nonlinear ON (``op3_bond_reflection``);
        the metadata records the flag so a Γ≈0 reads "linear-vacuum-no-
        reflection," NOT "matched."  PML cells are excluded from the argmax
        (A-Rule 10 corollary) — they carry frozen-absorbing artifact.

        Returns the scalar reductions (cheap-scalar channel) plus a coarse
        Γ-vs-A² scatter (binned, O(N) to store).
        """
        k4 = engine.k4
        z = np.asarray(k4.z_local_field, dtype=float)            # (N,N,N) persistent Z_eff
        v_snap = float(getattr(engine, "V_SNAP", getattr(k4, "V_SNAP", 1.0)))

        # Per-site K4 strain A² = |V_inc|²/V_SNAP² — the SAME numerator the
        # engine uses in _update_z_local_field (strain = v_total/v_snap).
        v_total_sq = np.sum(np.asarray(k4.V_inc, dtype=float) ** 2, axis=-1)
        A2_site = v_total_sq / (v_snap ** 2)                     # (N,N,N)

        mask_A = np.asarray(k4.mask_A, dtype=bool)
        mask_active = np.asarray(k4.mask_active, dtype=bool)
        interior = self._interior_mask(z.shape)                  # PML-excluded

        op3 = bool(getattr(k4, "op3_bond_reflection", False))

        gamma_stack = []   # (4, N, N, N) per-port Γ at A-sites
        A2_bond_stack = []  # (4, N, N, N) per-bond strain (max of endpoints)
        for shift_to_B in self._PORT_SHIFTS:
            z_A_own = z
            z_B_at_A = np.roll(z, shift=shift_to_B, axis=(0, 1, 2))
            # COMPOSE the shipped operator — mirrors engine convention exactly.
            gamma = _universal_reflection(z_A_own, z_B_at_A)
            gamma_stack.append(gamma)
            # bond strain = max of the two endpoints' A² (the saturated-wall side)
            A2_B_at_A = np.roll(A2_site, shift=shift_to_B, axis=(0, 1, 2))
            A2_bond_stack.append(np.maximum(A2_site, A2_B_at_A))

        gamma_arr = np.stack(gamma_stack, axis=0)    # (4,N,N,N)
        A2_bond_arr = np.stack(A2_bond_stack, axis=0)

        # Restrict to live, interior A-site bonds (canonical A→B direction).
        bond_valid = mask_A & mask_active & interior          # (N,N,N)
        valid4 = np.broadcast_to(bond_valid, gamma_arr.shape)  # (4,N,N,N)

        if not valid4.any():
            return self._empty_reflection(op3)

        g_valid = gamma_arr[valid4]
        a2_valid = A2_bond_arr[valid4]

        # THE ADJUDICATOR: Γ at the most-saturated valid bond.
        i_max = int(np.argmax(a2_valid))
        gamma_at_max_A2 = float(g_valid[i_max])
        A2_at_max = float(a2_valid[i_max])

        # R² / T² per bond (COMPOSE Op17). R² = Γ², T² = 1 − Γ².
        R2 = float(gamma_at_max_A2 ** 2)
        T2 = float(_universal_power_transmission_from_gamma(gamma_at_max_A2))

        # Coarse Γ-vs-A² scatter (binned) — forward read, no fit. 12 A²-bins.
        scatter = self._gamma_vs_A2_scatter(g_valid, a2_valid)

        return {
            "t": float(getattr(engine, "time", 0.0)),
            "gamma_at_max_A2": gamma_at_max_A2,
            "sign_gamma_at_max_A2": int(np.sign(gamma_at_max_A2)) if gamma_at_max_A2 != 0.0 else 0,
            "A2_at_max_bond": A2_at_max,
            "gamma_max": float(g_valid.max()),
            "gamma_min": float(g_valid.min()),
            "gamma_abs_max": float(np.abs(g_valid).max()),
            "gamma_rms": float(np.sqrt(np.mean(g_valid ** 2))),
            "R2_at_max_A2": R2,
            "T2_at_max_A2": T2,
            "n_valid_bonds": int(g_valid.size),
            "op3_bond_reflection": op3,
            "gamma_vs_A2_scatter": scatter,
        }

    def _empty_reflection(self, op3: bool) -> dict:
        """Degenerate Γ record (no valid interior bonds)."""
        return {
            "t": 0.0, "gamma_at_max_A2": 0.0, "sign_gamma_at_max_A2": 0,
            "A2_at_max_bond": 0.0, "gamma_max": 0.0, "gamma_min": 0.0,
            "gamma_abs_max": 0.0, "gamma_rms": 0.0, "R2_at_max_A2": 0.0,
            "T2_at_max_A2": 1.0, "n_valid_bonds": 0, "op3_bond_reflection": op3,
            "gamma_vs_A2_scatter": {"A2_bin_centers": [], "gamma_mean": [],
                                    "gamma_std": [], "counts": []},
        }

    @staticmethod
    def _gamma_vs_A2_scatter(gamma: np.ndarray, A2: np.ndarray,
                             n_bins: int = 12) -> dict:
        """Binned Γ-vs-A² scatter — the forward read of how the boundary
        condition tracks saturation (no fit, no target). Bins over [0, A²_max]."""
        a2_max = float(A2.max())
        if a2_max <= 0.0:
            return {"A2_bin_centers": [], "gamma_mean": [], "gamma_std": [], "counts": []}
        edges = np.linspace(0.0, a2_max, n_bins + 1)
        idx = np.clip(np.digitize(A2, edges) - 1, 0, n_bins - 1)
        centers, means, stds, counts = [], [], [], []
        for b in range(n_bins):
            sel = idx == b
            c = int(sel.sum())
            centers.append(float(0.5 * (edges[b] + edges[b + 1])))
            counts.append(c)
            if c > 0:
                means.append(float(gamma[sel].mean()))
                stds.append(float(gamma[sel].std()))
            else:
                means.append(0.0)
                stds.append(0.0)
        return {"A2_bin_centers": centers, "gamma_mean": means,
                "gamma_std": stds, "counts": counts}

    def _interior_mask(self, shape: tuple[int, int, int]) -> np.ndarray:
        """Boolean interior mask excluding PML cells (A-Rule 10 corollary):
        pml ≤ {i,j,k} ≤ N − pml − 1. PML cells return frozen-absorbing
        artifact, not interior physics, so they are filtered before any
        top-K / argmax field-density extraction."""
        nx, ny, nz = shape
        p = self.pml_thickness
        m = np.zeros(shape, dtype=bool)
        if p <= 0:
            m[:] = True
            return m
        m[p:nx - p, p:ny - p, p:nz - p] = True
        return m

    # ─────────────────────────────────────────────────────────────────────────
    # CHANNELS 3 & 4 — Capacitive / inductive reactance X_C, X_L.
    # ─────────────────────────────────────────────────────────────────────────
    def _reactances(self, engine) -> dict:
        """C-state (V_inc, voltage store) vs L-state (Φ_link, flux store) ratio.

            X_C = |V_inc| / (ω·|Φ_link|)        (capacitive)
            X_L =  ω·|Φ_link| / |V_inc|         (inductive)
            X_L/X_C → 1  ⇒  LC-matched standing mode (bond-pair resonance)

        ω = ``self.reactance_omega`` — ENGINEERING-INPUT (prereg §5 mandatory
        tag): the config drive-ω, NOT the soliton's own ω_C = c/ℓ_node. A formed
        electron rings at ω_C; v1 uses drive-ω and tags it. Convergence of a
        measured ring frequency to ω_C is itself an electron-check (#14), but is
        NOT asserted here. Read off live, interior, A-site bonds (PML-excluded).
        """
        k4 = engine.k4
        omega = float(self.reactance_omega)
        V_inc = np.asarray(k4.V_inc, dtype=float)       # (N,N,N,4)  C-state per port
        Phi = np.asarray(k4.Phi_link, dtype=float)      # (N,N,N,4)  L-state per port
        mask_A = np.asarray(k4.mask_A, dtype=bool)
        mask_active = np.asarray(k4.mask_active, dtype=bool)
        interior = self._interior_mask(V_inc.shape[:3])
        valid = mask_A & mask_active & interior          # (N,N,N)

        eps = 1e-30
        absV = np.abs(V_inc)                              # (N,N,N,4)
        absPhi = np.abs(Phi)
        # per-bond magnitudes at valid A-sites
        valid4 = np.broadcast_to(valid[..., None], absV.shape)
        absV_v = absV[valid4]
        absPhi_v = absPhi[valid4]
        if absV_v.size == 0:
            return {"t": float(getattr(engine, "time", 0.0)), "omega": omega,
                    "XC_median": 0.0, "XL_median": 0.0, "XL_over_XC_median": 0.0,
                    "XL_over_XC_min": 0.0, "n_valid_bonds": 0,
                    "omega_source": Source.ENGINEERING.value}

        XC = absV_v / (omega * absPhi_v + eps)
        XL = (omega * absPhi_v) / (absV_v + eps)
        ratio = XL / (XC + eps)   # = (ω·|Φ|/|V|) / (|V|/(ω·|Φ|)) = (ω|Φ|/|V|)²

        return {
            "t": float(getattr(engine, "time", 0.0)),
            "omega": omega,
            "omega_source": Source.ENGINEERING.value,  # mandatory engineering-input tag
            "XC_median": float(np.median(XC)),
            "XL_median": float(np.median(XL)),
            "XL_over_XC_median": float(np.median(ratio)),
            "XL_over_XC_min": float(ratio.min()),
            "XL_over_XC_closest_to_1": float(ratio.flat[int(np.argmin(np.abs(ratio - 1.0)))]),
            "n_valid_bonds": int(absV_v.size),
        }

    # ─────────────────────────────────────────────────────────────────────────
    # CHANNEL 7 — 7-mode energy split (the substrate's 7 micropolar DOF).
    # ─────────────────────────────────────────────────────────────────────────
    def _energy7(self, engine) -> dict:
        """Energy partition across the 7 micropolar DOF, mechanically:

            3 translational / C-sector :  ½·ρ·u̇ᵢ²        (per axis i)
            3 rotational     / L-sector :  ½·I_ω·ω̇ᵢ²      (per axis i)
            1 volumetric                 :  ½·λ·(∇·u)²      (λ = K − ⅔G = (4/3)G)
            + E_K4 (the K4-TLM sector)

        Composes the SAME ½ρ|u̇|²+½I_ω|ω̇|² kernel as ``CosseratField3D.
        kinetic_energy`` (cosserat:1504) but split per-axis (the aggregate sum is
        cross-checked). The volumetric term is NEW (the divergence of u), with
        the Lamé λ DERIVED from the field's own shear modulus self.G via the
        engine's K=2G convention (cfl_dt:1491) — no planted modulus.

        C-sector (3 trans + volumetric) vs L-sector (3 rot) balance is the
        mechanical reading of the C↔L reactance state (real-space complement to
        channels 3/4).
        """
        cos = engine.cos
        mask = np.asarray(cos.mask_alive, dtype=bool)
        u_dot = np.asarray(cos.u_dot, dtype=float)       # (N,N,N,3)
        omega_dot = np.asarray(cos.omega_dot, dtype=float)
        u = np.asarray(cos.u, dtype=float)
        dx = float(cos.dx)
        rho = float(cos.rho)
        I_omega = float(cos.I_omega)
        G = float(getattr(cos, "G", 1.0))
        lam = (4.0 / 3.0) * G   # λ = K − ⅔G, with K = 2G (cfl_dt convention) → (4/3)G

        m3 = mask[..., None].astype(float)
        # 3 translational (C-sector), per axis
        E_trans = [float(0.5 * rho * np.sum((u_dot[..., i] * mask) ** 2)) for i in range(3)]
        # 3 rotational (L-sector), per axis
        E_rot = [float(0.5 * I_omega * np.sum((omega_dot[..., i] * mask) ** 2)) for i in range(3)]
        # 1 volumetric — ½λ(∇·u)² (NEW). Central-difference divergence on the
        # lattice (dx spacing); masked to alive sites.
        div_u = self._divergence(u, dx) * mask
        E_vol = float(0.5 * lam * np.sum(div_u ** 2) * (dx ** 3))

        E_K4 = float(engine.k4.total_energy())
        E_C = sum(E_trans) + E_vol     # C-sector: translation + volumetric
        E_L = sum(E_rot)               # L-sector: rotation
        total7 = E_C + E_L

        return {
            "t": float(getattr(engine, "time", 0.0)),
            "E_trans_x": E_trans[0], "E_trans_y": E_trans[1], "E_trans_z": E_trans[2],
            "E_rot_x": E_rot[0], "E_rot_y": E_rot[1], "E_rot_z": E_rot[2],
            "E_volumetric": E_vol,
            "E_C_sector": E_C, "E_L_sector": E_L,
            "C_over_L": float(E_C / (E_L + 1e-30)),
            "E_7mode_total": total7,
            "E_K4": E_K4,
            "lambda_lame": lam,
        }

    @staticmethod
    def _divergence(u: np.ndarray, dx: float) -> np.ndarray:
        """∇·u via central differences on the lattice (NEW). u is (N,N,N,3)."""
        du_dx = np.gradient(u[..., 0], dx, axis=0)
        dv_dy = np.gradient(u[..., 1], dx, axis=1)
        dw_dz = np.gradient(u[..., 2], dx, axis=2)
        return du_dx + dv_dy + dw_dz

    # ─────────────────────────────────────────────────────────────────────────
    # CHANNEL 8 — Energy budget + retention (COMPOSE EnergyBudgetObserver).
    # ─────────────────────────────────────────────────────────────────────────
    def _energy_budget(self, engine) -> dict:
        """E_K4, E_cos, T_cos, E_coupling, H_total — composed from the shipped
        ``EnergyBudgetObserver._capture`` (vacuum_engine:667), redefined never.
        ``retention = H(t)/H(t_drive_off)`` is added downstream once the drive-
        off step is known (the per-sim analysis fills it). Conservation→1 = bound
        standing wave (mass = trapped reactance); →0 = dispersal."""
        cap = _EnergyBudgetObserver()._capture(engine)   # COMPOSED
        return cap

    # ─────────────────────────────────────────────────────────────────────────
    # CHANNEL 12 — Saturation / regime (COMPOSE RegimeClassifierObserver).
    # ─────────────────────────────────────────────────────────────────────────
    def _regime(self, engine) -> dict:
        """Where on the Axiom-4 kernel the substrate sits — how close to making
        a boundary (A²→1 = the wall forms = matter). COMPOSES the shipped
        ``RegimeClassifierObserver._capture`` (vacuum_engine:395): per-regime
        cell counts (Pythagorean A²_k4+A²_cos), max_A2_total. Redefined never."""
        return _RegimeClassifierObserver()._capture(engine)   # COMPOSED

    # ─────────────────────────────────────────────────────────────────────────
    # CHANNELS 10 — Beltrami helicity (COMPOSE _beltrami_helicity + get_helicity).
    # ─────────────────────────────────────────────────────────────────────────
    def _helicity(self, engine) -> dict:
        """The chirality signature — the handedness frozen at genesis.

        h_K4 = ``K4Lattice3D.get_helicity_density`` (k4_tlm:535, A·B bipartite,
        native) reduced to mean/abs-mean over interior live sites; and the
        Cosserat Beltrami helicity h = ω·(∇×ω)/(|ω||∇×ω|) via the shipped
        ``_beltrami_helicity`` (cosserat:445). COMPOSED — redefines neither."""
        k4 = engine.k4
        interior = self._interior_mask(np.asarray(k4.z_local_field).shape)
        live = np.asarray(k4.mask_active, dtype=bool) & interior
        h_k4 = np.asarray(k4.get_helicity_density(), dtype=float)        # COMPOSED
        h_k4_live = h_k4[live] if live.any() else np.array([0.0])
        out = {
            "t": float(getattr(engine, "time", 0.0)),
            "h_K4_mean": float(h_k4_live.mean()),
            "h_K4_abs_mean": float(np.abs(h_k4_live).mean()),
            "h_K4_signed_sum": float(h_k4_live.sum()),
        }
        # Cosserat Beltrami helicity (lazy — only if the cos sector is alive).
        try:
            from ave.topological.cosserat_field_3d import _beltrami_helicity  # COMPOSED
            cos = engine.cos
            omega = np.asarray(cos.omega, dtype=float)
            if np.any(np.abs(omega) > 1e-30):
                h_bel = np.asarray(_beltrami_helicity(omega, float(cos.dx)))
                cos_live = np.asarray(cos.mask_alive, dtype=bool)
                h_bel_live = h_bel[cos_live] if cos_live.any() else np.array([0.0])
                out["h_beltrami_mean"] = float(h_bel_live.mean())
                out["h_beltrami_abs_mean"] = float(np.abs(h_bel_live).mean())
            else:
                out["h_beltrami_mean"] = 0.0
                out["h_beltrami_abs_mean"] = 0.0
                out["h_beltrami_note"] = "cosserat-omega-cold"
        except Exception as exc:   # pragma: no cover — pure-FDTD / import guard
            out["h_beltrami_note"] = f"unavailable: {type(exc).__name__}"
        return out

    # ─────────────────────────────────────────────────────────────────────────
    # CHANNEL 11 (cheap part) — Hopf charge + centroids (COMPOSE TopologyObserver).
    # ─────────────────────────────────────────────────────────────────────────
    def _hopf_cheap(self, engine) -> dict:
        """Q_hopf (Chern-Simons) + centroids — the topological sector (→6 for a
        (2,3) electron, 0 vacuum) and where matter sits. COMPOSES the shipped
        ``TopologyObserver._capture`` (vacuum_engine:644, which calls
        ``extract_hopf_charge`` + ``find_soliton_centroids``). Redefined never.
        Shell radii R/r (``extract_shell_radii``) are added in extract_full
        (heavier). Cheap because Q_hopf + centroids are O(N) on the cos field."""
        cap = _TopologyObserver(cadence=1)._capture(engine)   # COMPOSED
        return cap

    # ── Step-2 + Step-3 + Step-4 cheap channels ──────────────────────────────
    def sample_cheap(self, engine) -> dict:  # noqa: D401 — extended Step 6
        """O(N) per-step scalar channels (Γ, reactances, E7, budget, regime,
        helicity, Q_hopf). Heavy field-walks live in extract_full (Step 5)."""
        return {
            "reflection": self._reflection(engine),
            "reactances": self._reactances(engine),
            "energy7": self._energy7(engine),
            "energy_budget": self._energy_budget(engine),
            "regime": self._regime(engine),
            "helicity": self._helicity(engine),
            "hopf": self._hopf_cheap(engine),
        }

    # ─────────────────────────────────────────────────────────────────────────
    # CHANNEL 9 — Boundary invariants M, Q, J (COMPOSE compute_all_invariants).
    # ─────────────────────────────────────────────────────────────────────────
    def _boundary_MQJ(self, engine) -> dict:
        """The three things visible outside a Γ-wall (A-026), on A = √(V_inc²):

            M = ∫(n−1)dV   — RIGOROUS (mass = integrated strain, geometry).
            Q              — first-pass-proxy (component-count stand-in, NOT the
                             Axiom-2 winding/linking).
            J              — first-pass-proxy (MOI-anisotropy stand-in, NOT the
                             (2,3) angular momentum).

        COMPOSES the shipped ``compute_all_invariants`` (boundary_invariants:268)
        — whose own dataclass docstring labels Q "linking number proxy" and J
        "winding number proxy" (lines 77/80). V_yield is passed as the engine's
        natural-unit V_SNAP (=1.0) to match the field normalization; tagged. The
        proxy tags are MANDATORY (prereg §5) and surfaced verbatim so Q/J are
        never read as the rigorous winding (ave-evidence-framing). Heavy: a
        full-field walk → lives in extract_full."""
        from ave.core.boundary_invariants import compute_all_invariants  # COMPOSED
        k4 = engine.k4
        V_inc = np.asarray(k4.V_inc, dtype=float)
        # Scalar substrate field A = √(Σ_port V_inc²) — the prereg's channel-9 input.
        A_scalar = np.sqrt(np.sum(V_inc ** 2, axis=-1))     # (N,N,N)
        v_snap = float(getattr(engine, "V_SNAP", getattr(k4, "V_SNAP", 1.0)))
        dx = float(getattr(k4, "dx", 1.0))
        inv = compute_all_invariants(
            A_scalar, dx=dx, V_yield=v_snap,
            l_node=float(L_NODE),
        )
        return {
            "M": float(inv.M),
            "Q": float(inv.Q),
            "J": float(inv.J),
            "M_unit_normalized": (float(inv.M_unit_normalized)
                                  if inv.M_unit_normalized is not None else None),
            "M_source": Source.NATIVE.value,    # rigorous: mass = integrated strain
            "Q_source": Source.PROXY.value,     # MANDATORY proxy tag (Axiom-2 stand-in)
            "J_source": Source.PROXY.value,     # MANDATORY proxy tag
            "V_yield_used": v_snap,
            "V_yield_source": Source.ENGINEERING.value,  # natural-unit V_SNAP normalization
            "note": "Q,J are geometric proxies (component-count / MOI-anisotropy), "
                    "NOT the Axiom-2 winding/linking; M = integrated strain (rigorous).",
        }

    # ─────────────────────────────────────────────────────────────────────────
    # Heavy post-run field-walks — run ONCE on the converged state (extract_full).
    # ─────────────────────────────────────────────────────────────────────────
    def extract_full(self, engine) -> dict:
        """The expensive field-walks, run once on the converged state (prereg
        §3): (2,3) shell-walk (#6), Θ_RP (#5), M/Q/J (#9 heavy), R/r (#11
        heavy), ρ_Q density (#13), dispersion FFT (#14). Each channel that
        cannot be honestly computed is returned with an ``inconclusive`` flag
        rather than a null (so a missing read is never a false negative)."""
        full: dict[str, Any] = {}
        inconclusive: list[str] = []

        full["winding_2_3"] = self._winding_2_3(engine, inconclusive)
        full["theta_RP"] = self._theta_RP(engine, inconclusive)
        full["boundary_MQJ"] = self._boundary_MQJ(engine)        # heavy full-field
        full["hopf_full"] = self._hopf_full(engine, inconclusive)  # + R/r shell radii
        full["charge_density"] = self._charge_density(engine, inconclusive)
        full["dispersion"] = self._dispersion(engine, inconclusive)

        full["_inconclusive"] = inconclusive
        return full

    # ── CHANNEL 6 — (2,3) winding (COMPOSE the r10 coordinate-correct extractor)
    def _winding_2_3(self, engine, inconclusive: list) -> dict:
        """The soliton's topological charge W via the coordinate-correct (2,3)
        extractor. COMPOSES ``shell_params_from_field`` + ``extract_2_3_spatial``
        + ``is_2_3`` from r10 (the clean-validated extractor). Redefines none.

        Reads the K4 V_inc/Phi_link full field (NOT the Cosserat sector), so it
        populates on the K4-hosted imposed-(2,3) control. modal_count / n_walks
        confidence fields are carried through so a weak read is visible (the V0
        degradation-vs-contamination fork: a conserved (2,3) cannot fade
        gradually, so a weak read = thermal dressing, not lost charge)."""
        r10 = self._lazy_r10(inconclusive, "winding_2_3")
        if r10 is None:
            return {"inconclusive": True, "reason": "r10-extractor-unavailable"}
        try:
            k4 = engine.k4
            V_inc = np.asarray(k4.V_inc, dtype=float)
            Phi = np.asarray(k4.Phi_link, dtype=float)
            mA = np.asarray(k4.mask_A, dtype=bool)
            N = int(engine.N)
            PML = int(self.pml_thickness)
            R, r, cx, cy, cz, kz = r10["shell_params_from_field"](V_inc, mA, N)
            res = r10["extract_2_3_spatial"](V_inc, Phi, mA, N, PML, R, r,
                                             (cx, cy, cz), kz)
            res.pop("_curve", None)   # drop figure samples from the record
            res["is_2_3"] = bool(r10["is_2_3"](res))
            res["a2_max"] = float(np.sum(V_inc ** 2, axis=-1).max())
            return res
        except Exception as exc:   # pragma: no cover
            inconclusive.append("winding_2_3")
            return {"inconclusive": True, "reason": f"{type(exc).__name__}: {exc}"}

    # ── CHANNEL 5 — Real↔phase angle Θ_RP (COMPOSE r10 nhat + fibre-phase) ─────
    def _theta_RP(self, engine, inconclusive: list) -> dict:
        """Angle between the real-space field direction n̂ (Cosserat-analog,
        from K4 port-weighted direction) and the phase-space C↔L/U(1)-fibre
        phase. COMPOSES ``field_direction_nhat`` + ``fibre_phase_cell`` +
        ``knot_tangent_port_weights`` (r10). Redefines none.

        Eigenmode-vs-trajectory discriminator (phase-space-coordinate-check —
        this is the one channel that is explicitly an angle BETWEEN a real-space
        and a phase-space axis): n̂ locked in quadrature to the C↔L fibre =
        phase-coherent eigenmode; the angle drifting = dissipative trajectory.
        Read at the energy-density-peak A-sites (density-peak sampling, A-Rule
        10 — NOT centroid+offset, since a shell's centroid is the empty middle)."""
        r10 = self._lazy_r10(inconclusive, "theta_RP")
        if r10 is None:
            return {"inconclusive": True, "reason": "r10-extractor-unavailable"}
        try:
            k4 = engine.k4
            V_inc = np.asarray(k4.V_inc, dtype=float)
            Phi = np.asarray(k4.Phi_link, dtype=float)
            mA = np.asarray(k4.mask_A, dtype=bool)
            N = int(engine.N)
            interior = self._interior_mask(V_inc.shape[:3])
            valid = mA & np.asarray(k4.mask_active, dtype=bool) & interior

            # locate the hosted shell to get the knot-tangent coherent weight
            R, r, cx, cy, cz, kz = r10["shell_params_from_field"](V_inc, mA, N)

            # Density-peak sampling: top-K |V_inc|² A-sites (PML-excluded).
            a2 = np.sum(V_inc ** 2, axis=-1)
            a2_valid = np.where(valid, a2, -1.0)
            K = min(64, int(valid.sum()))
            if K <= 0:
                inconclusive.append("theta_RP")
                return {"inconclusive": True, "reason": "no-valid-interior-A-sites"}
            flat_idx = np.argpartition(a2_valid.ravel(), -K)[-K:]
            ijk = np.array(np.unravel_index(flat_idx, a2.shape)).T  # (K,3)

            angles = []
            for (i, j, k) in ijk:
                V_cell = V_inc[i, j, k]            # (4,) port voltages
                Phi_cell = Phi[i, j, k]            # (4,) port flux
                # real-space field direction n̂ (S² "2" base) → its azimuth
                nhat, nmag = r10["field_direction_nhat"](V_cell)
                if nmag < 1e-12:
                    continue
                nhat_az = float(np.arctan2(nhat[1], nhat[0]))
                # phase-space C↔L fibre phase at the cell's (φ,ψ) coherent weight
                phi_ang = float(np.arctan2(j - cy, i - cx))
                psi_ang = 0.0  # outer-equator crest (minor angle ~0 at the slice)
                w_port = r10["knot_tangent_port_weights"](phi_ang, psi_ang, R, r)
                fibre_phase, fmag = r10["fibre_phase_cell"](V_cell, Phi_cell, w_port)
                if fmag < 1e-15:
                    continue
                # Θ_RP = angle between the real-space n̂-azimuth and the phase
                # fibre angle, wrapped to (−π, π].
                dtheta = np.arctan2(np.sin(nhat_az - fibre_phase),
                                    np.cos(nhat_az - fibre_phase))
                angles.append(float(dtheta))

            if not angles:
                inconclusive.append("theta_RP")
                return {"inconclusive": True, "reason": "no-coherent-fibre-phase"}
            angles = np.array(angles)
            # circular stats: mean resultant length R_bar ∈ [0,1]; R_bar→1 =
            # locked (coherent eigenmode), R_bar→0 = drifting (trajectory).
            C = float(np.mean(np.cos(angles)))
            S = float(np.mean(np.sin(angles)))
            R_bar = float(np.hypot(C, S))
            theta_mean = float(np.arctan2(S, C))
            # quadrature check: |Θ_RP| near π/2 = locked-in-quadrature.
            quad_frac = float(np.mean(np.abs(np.abs(angles) - np.pi / 2.0) < (np.pi / 8.0)))
            return {
                "theta_RP_mean_rad": theta_mean,
                "theta_RP_circular_R": R_bar,    # coherence: →1 locked, →0 drifting
                "quadrature_fraction": quad_frac,  # frac within ±π/8 of ±π/2
                "n_samples": int(len(angles)),
                "coord": Coord.REAL_VS_PHASE.value,
            }
        except Exception as exc:   # pragma: no cover
            inconclusive.append("theta_RP")
            return {"inconclusive": True, "reason": f"{type(exc).__name__}: {exc}"}

    # ── CHANNEL 11 heavy — Hopf + centroids + R/r shell radii ─────────────────
    def _hopf_full(self, engine, inconclusive: list) -> dict:
        """Q_hopf + centroids (COMPOSE TopologyObserver) PLUS shell radii R/r
        via ``CosseratField3D.extract_shell_radii`` (cosserat:1737). R/r vs φ²
        golden-torus aspect. Feeds the rigorous Q/J. Reads the Cosserat sector;
        on a K4-only control the centroids/Q_hopf read 0 (flagged, not nulled)."""
        try:
            cap = _TopologyObserver(cadence=1)._capture(engine)     # COMPOSED
            cap["phi_squared"] = float(PHI ** 2)   # golden-torus aspect reference
            # R/r reads the Cosserat ω field; it is ONLY meaningful when that
            # sector is alive. On a K4-only control the read picks up noise — so
            # gate it + flag rather than report a meaningless R/r (flag-don't-fix).
            cos = engine.cos
            cos_alive = bool(np.any(np.abs(np.asarray(cos.omega)) > 1e-30))
            if cos_alive:
                R, r = cos.extract_shell_radii()                     # COMPOSED
                cap["R_major"] = float(R)
                cap["r_minor"] = float(r)
                cap["R_over_r"] = float(R / r) if r > 1e-12 else 0.0
            else:
                cap["R_major"] = None
                cap["r_minor"] = None
                cap["R_over_r"] = None
                cap["R_r_note"] = ("Cosserat ω cold (K4-only control): R/r shell "
                                   "radii not meaningful; the (2,3) winding (#6) "
                                   "reads the K4-hosted shell instead.")
            if cap.get("n_centroids", 0) == 0:
                cap["note"] = ("Q_hopf/centroids read the Cosserat ω field; "
                               "0 on a K4-only control (not a null result).")
            return cap
        except Exception as exc:   # pragma: no cover
            inconclusive.append("hopf_full")
            return {"inconclusive": True, "reason": f"{type(exc).__name__}: {exc}"}

    # ── CHANNEL 13 — Per-site charge density ρ_Q (reuse the Q_hopf kernel) ─────
    def _charge_density(self, engine, inconclusive: list) -> dict:
        """Pre-integration Chern-Simons/Beltrami integrand per site — the
        virtual-soliton / pair-nucleation precursor map (where the substrate is
        about to seed topology). REUSES the shipped ``_hopf_density`` kernel
        (cosserat:240, A·B/2) that ``extract_hopf_charge`` integrates — same
        kernel, un-integrated. Redefines none. Reduced to interior peak / RMS /
        signed-sum (the full field is too large for the JSON record)."""
        try:
            from ave.topological.cosserat_field_3d import _hopf_density  # COMPOSED kernel
            cos = engine.cos
            omega = np.asarray(cos.omega, dtype=float)
            if not np.any(np.abs(omega) > 1e-30):
                return {"rho_Q_peak": 0.0, "rho_Q_rms": 0.0, "rho_Q_signed_sum": 0.0,
                        "note": "cosserat-omega-cold (K4-only control)"}
            rho = np.asarray(_hopf_density(omega, float(cos.dx)), dtype=float)
            live = np.asarray(cos.mask_alive, dtype=bool)
            interior = self._interior_mask(rho.shape)
            sel = live & interior
            rho_sel = rho[sel] if sel.any() else np.array([0.0])
            return {
                "rho_Q_peak": float(np.abs(rho_sel).max()),
                "rho_Q_rms": float(np.sqrt(np.mean(rho_sel ** 2))),
                "rho_Q_signed_sum": float(rho_sel.sum() * (float(cos.dx) ** 3)),
                "rho_Q_positive_frac": float(np.mean(rho_sel > 0)),
            }
        except Exception as exc:   # pragma: no cover
            inconclusive.append("charge_density")
            return {"inconclusive": True, "reason": f"{type(exc).__name__}: {exc}"}

    # ── CHANNEL 14 — Spectral dispersion (COMPOSE universal_spectral_analysis) ─
    def _dispersion(self, engine, inconclusive: list) -> dict:
        """FFT of the accumulated probe series → spectrum, dominant frequencies.
        COMPOSES the shipped ``universal_spectral_analysis`` (universal_operators:
        355). Does the soliton ring at ω_C? POST-RUN only. Honest INCONCLUSIVE
        if too few probe samples accumulated (DSP needs a series)."""
        if len(self.probe_history) < 8:
            inconclusive.append("dispersion")
            return {"inconclusive": True,
                    "reason": f"probe_history too short ({len(self.probe_history)}<8 samples)",
                    "n_probe_samples": len(self.probe_history)}
        try:
            series = np.asarray(self.probe_history, dtype=float)
            spec = _universal_spectral_analysis(series)             # COMPOSED
            dom_k = spec.get("dominant_k")
            power = spec.get("power")
            out = {
                "n_probe_samples": int(series.size),
                "dominant_k": [int(x) for x in np.atleast_1d(dom_k)][:5]
                              if dom_k is not None else [],
                "dc_level": float(np.real(spec["spectrum"][0]) / series.size)
                            if "spectrum" in spec else 0.0,
            }
            if power is not None and len(power) > 1:
                # peak-spatial-frequency reading (DSP) — phase/group velocity
                # would require a (k, ω) 2D probe; v1 reports the 1D peak only.
                out["peak_freq_index"] = int(np.argmax(power[1:]) + 1)
            return out
        except Exception as exc:   # pragma: no cover
            inconclusive.append("dispersion")
            return {"inconclusive": True, "reason": f"{type(exc).__name__}: {exc}"}

    # ── Lazy r10 (2,3) extractor import (scripts path) — composed, not copied ──
    def _lazy_r10(self, inconclusive: list, channel: str) -> Optional[dict]:
        """Import + cache the r10 coordinate-correct (2,3) extractor functions
        (COMPOSED). Returns None + flags inconclusive if the scripts path / its
        own dep (tlm_electron_soliton_eigenmode) is unavailable."""
        if _R10_FUNCS:
            return _R10_FUNCS
        try:
            import sys as _sys
            from pathlib import Path as _Path
            # the r10 module lives in src/scripts/vol_1_foundations; add to path
            here = _Path(__file__).resolve()
            # …/src/ave/core/observable_battery.py → …/src
            src_root = here.parents[2]
            scripts_dir = src_root / "scripts" / "vol_1_foundations"
            for p in (str(scripts_dir),):
                if p not in _sys.path:
                    _sys.path.insert(0, p)
            from r10_2_3_winding_extractor_coordinate import (   # COMPOSED
                extract_2_3_spatial,
                shell_params_from_field,
                field_direction_nhat,
                fibre_phase_cell,
                knot_tangent_port_weights,
                is_2_3,
            )
            _R10_FUNCS.update(
                extract_2_3_spatial=extract_2_3_spatial,
                shell_params_from_field=shell_params_from_field,
                field_direction_nhat=field_direction_nhat,
                fibre_phase_cell=fibre_phase_cell,
                knot_tangent_port_weights=knot_tangent_port_weights,
                is_2_3=is_2_3,
            )
            return _R10_FUNCS
        except Exception as exc:   # pragma: no cover
            if channel not in inconclusive:
                inconclusive.append(channel)
            return None


# ─────────────────────────────────────────────────────────────────────────────
# BatteryObserver — the thin Observer wrapper for the VacuumEngine3D hook.
# ─────────────────────────────────────────────────────────────────────────────
# Lazy base so a pure-numpy import of this module (FDTD-only) doesn't pull the
# Cosserat/JAX stack. The real base is ave.topological.vacuum_engine.Observer.
def _make_battery_observer_class():
    from ave.topological.vacuum_engine import Observer as _Observer

    class BatteryObserver(_Observer):
        """Drives an ``ObservableBattery`` off the per-step engine hook
        (vacuum_engine:1851). Each cadence-filtered step calls
        ``battery.sample_cheap(engine)`` (O(N) scalar channels) and appends a
        scalar probe value for the post-run dispersion FFT (#14). Heavy field-
        walks (``extract_full``) are NOT run per-step — the harness calls them
        once on the converged state, mirroring the shipped cheap-scalar-history
        / heavy-once pattern.

        ``probe_fn`` extracts one scalar per step for the dispersion series
        (default: max |V_inc| at the lattice center — a native ring probe)."""

        def __init__(self, battery: "ObservableBattery", cadence: int = 1,
                     probe_fn=None):
            super().__init__(cadence=cadence)
            self.battery = battery
            self.probe_fn = probe_fn or _default_probe_fn

        def _capture(self, engine):
            rec = self.battery.sample_cheap(engine)
            # accumulate the dispersion probe (cheap scalar per step)
            try:
                self.battery.probe_history.append(float(self.probe_fn(engine)))
            except Exception:   # pragma: no cover — probe is best-effort
                pass
            rec["t"] = float(getattr(engine, "time", 0.0))
            rec["step_count"] = int(getattr(engine, "step_count", 0))
            return rec

    return BatteryObserver


def _default_probe_fn(engine) -> float:
    """Default dispersion probe: |V_inc| magnitude at the lattice center node
    (a native ring probe). Reads off the K4 V_inc field."""
    k4 = engine.k4
    V = np.asarray(k4.V_inc, dtype=float)
    nx, ny, nz = V.shape[:3]
    c = (nx // 2, ny // 2, nz // 2)
    return float(np.sqrt(np.sum(V[c] ** 2)))


# Module-level cache so the class is built once (after the first lazy import).
_BATTERY_OBSERVER_CLS: list = []


def make_battery_observer(battery: "ObservableBattery", cadence: int = 1,
                          probe_fn=None):
    """Construct a ``BatteryObserver`` bound to ``battery`` (lazy base import).
    Attach via ``engine.add_observer(make_battery_observer(battery))``."""
    if not _BATTERY_OBSERVER_CLS:
        _BATTERY_OBSERVER_CLS.append(_make_battery_observer_class())
    return _BATTERY_OBSERVER_CLS[0](battery, cadence=cadence, probe_fn=probe_fn)


# ─────────────────────────────────────────────────────────────────────────────
# Forward per-sim analysis (prereg §4) — forward classification off native
# state. Every verdict a forward read; every threshold honesty-tagged. NO fits,
# NO target-matching (ave-driver-script-honesty).
# ─────────────────────────────────────────────────────────────────────────────
# Classification thresholds — engineering choices, tagged. NOT physics targets;
# they are read-off discriminators (which axis discriminates is read OFF the
# cube, not decided here).
_ANALYSIS_THRESHOLDS = {
    "eigenmode_circular_R": 0.5,   # Θ_RP circular-R above ⇒ phase-coherent eigenmode
    "retention_bound": 0.5,        # H(t)/H(t_drive_off) above ⇒ bound standing wave
    "lc_matched_tol": 0.2,         # |X_L/X_C − 1| below ⇒ LC-matched standing mode
    "saturated_A2": 1.0,           # max_A2_total ≥ ⇒ a boundary has formed (matter)
}


def analyze_report(report: "ObservableReport",
                   drive_off_step: Optional[int] = None) -> dict:
    """Run the forward per-sim classification on a populated ObservableReport.

    Verdicts (each a forward read off native state, prereg §4):
      * OPEN / SHORT          via sign(Γ_at_max_A2)         (the boundary condition)
      * eigenmode / trajectory via Θ_RP circular-R + retention
      * (2,3)-hosted           via is_2_3 (+ confidence)     (the topological charge)
      * LC-matched             via |X_L/X_C − 1|             (the bond-pair resonance)
      * regime                 via max_A2_total              (where on the Ax-4 kernel)
      * retention              via H(t)/H(t_drive_off)       (conservation vs dispersal)

    All thresholds are engineering discriminators (tagged), NOT physics targets.
    """
    th = _ANALYSIS_THRESHOLDS
    out: dict[str, Any] = {"thresholds": dict(th),
                           "thresholds_source": Source.ENGINEERING.value}

    # ── OPEN / SHORT (the headline boundary condition) ────────────────────────
    refl_last = report.latest_scalar("reflection")
    if refl_last and refl_last.get("n_valid_bonds", 0) > 0:
        sgn = int(refl_last.get("sign_gamma_at_max_A2", 0))
        op3 = bool(refl_last.get("op3_bond_reflection", False))
        gam = float(refl_last.get("gamma_at_max_A2", 0.0))
        if not op3:
            verdict = "LINEAR-VACUUM-NO-REFLECTION"   # prereg §2 #1: NOT "matched"
        elif sgn > 0:
            verdict = "OPEN"     # antinode, Z→∞, mass-closure
        elif sgn < 0:
            verdict = "SHORT"    # node, primer
        else:
            verdict = "MATCHED-OR-ZERO"
        out["boundary_condition"] = {
            "verdict": verdict, "sign_gamma_at_max_A2": sgn,
            "gamma_at_max_A2": gam, "op3_bond_reflection": op3,
            "evidence": "sign of Γ at the most-saturated interior bond",
        }
    else:
        out["boundary_condition"] = {"verdict": "INCONCLUSIVE",
                                     "reason": "no valid interior bonds"}

    # ── eigenmode / trajectory ────────────────────────────────────────────────
    theta = report.full.get("theta_RP", {})
    retention = _compute_retention(report, drive_off_step)
    if theta and not theta.get("inconclusive"):
        Rbar = float(theta.get("theta_RP_circular_R", 0.0))
        coherent = Rbar >= th["eigenmode_circular_R"]
        bound = (retention is not None) and (retention >= th["retention_bound"])
        if coherent and bound:
            verdict = "EIGENMODE"        # phase-coherent + retained
        elif coherent:
            verdict = "EIGENMODE-CANDIDATE"  # coherent but retention unknown/low
        else:
            verdict = "TRAJECTORY"       # drifting / dissipative
        out["mode_class"] = {"verdict": verdict, "theta_RP_circular_R": Rbar,
                             "retention": retention}
    else:
        out["mode_class"] = {"verdict": "INCONCLUSIVE",
                             "reason": "theta_RP not computed"}

    # ── (2,3)-hosted (the topological charge) ─────────────────────────────────
    w = report.full.get("winding_2_3", {})
    if w and not w.get("inconclusive"):
        is23 = bool(w.get("is_2_3", False))
        out["topology_class"] = {
            "verdict": "TWO-THREE-HOSTED" if is23 else "WEAK-OR-ABSENT",
            "is_2_3": is23,
            "w1_base": w.get("w1_base"), "w2_fibre": w.get("w2_fibre"),
            "crossing_count_c": w.get("crossing_count_c"),
            "w1_modal_count": w.get("w1_base_modal_count"),
            "w2_modal_count": w.get("w2_fibre_modal_count"),
            "n_walks": w.get("w1_base_n_walks"),
            # prereg §2 #3: a conserved (2,3) can't fade — a WEAK read is thermal
            # dressing around a conserved core, NOT lost charge. Confidence
            # fields make the weak read visible.
            "note": ("conserved-(2,3) cannot fade gradually; a weak read = "
                     "thermal dressing / under-converged shell, not lost charge"),
        }
    else:
        out["topology_class"] = {"verdict": "INCONCLUSIVE",
                                 "reason": w.get("reason", "winding not computed")}

    # ── LC-matched (the bond-pair resonance) ──────────────────────────────────
    rx = report.latest_scalar("reactances")
    if rx and rx.get("n_valid_bonds", 0) > 0:
        ratio_med = float(rx.get("XL_over_XC_median", 0.0))
        closest = float(rx.get("XL_over_XC_closest_to_1", 0.0))
        matched = abs(ratio_med - 1.0) <= th["lc_matched_tol"]
        out["lc_class"] = {
            "verdict": "LC-MATCHED" if matched else "LC-DETUNED",
            "XL_over_XC_median": ratio_med,
            "XL_over_XC_closest_to_1": closest,
            "omega_source": rx.get("omega_source", Source.ENGINEERING.value),
            "caveat": "ω = drive-ω (engineering-input), not the soliton ω_C",
        }
    else:
        out["lc_class"] = {"verdict": "INCONCLUSIVE", "reason": "no reactance bonds"}

    # ── regime (where on the Ax-4 kernel) ─────────────────────────────────────
    reg = report.latest_scalar("regime")
    if reg:
        a2 = float(reg.get("max_A2_total", 0.0))
        out["regime_class"] = {
            "verdict": "SATURATED-WALL" if a2 >= th["saturated_A2"]
                       else ("TRANSITION" if a2 >= 2.0 * ALPHA else "PASSBAND"),
            "max_A2_total": a2,
            "rupture_cells": int(reg.get("rupture", 0)),
            "rg_III_cells": int(reg.get("rg_III", 0)),
        }
    else:
        out["regime_class"] = {"verdict": "INCONCLUSIVE"}

    return out


def _compute_retention(report: "ObservableReport",
                       drive_off_step: Optional[int]) -> Optional[float]:
    """retention = H(t_final)/H(t_drive_off) from the energy-budget history. If
    no drive-off step is known, falls back to H(t_final)/H(t_initial)."""
    hist = report.scalar_history.get("energy_budget", [])
    if len(hist) < 2:
        return None
    H = [float(r.get("H_total", 0.0)) for r in hist]
    H_final = H[-1]
    if drive_off_step is not None:
        # find the history record nearest the drive-off step
        steps = [int(r.get("step_count", i)) for i, r in enumerate(hist)]
        idx = int(np.argmin([abs(s - drive_off_step) for s in steps]))
        H_ref = H[idx]
    else:
        H_ref = H[0]
    if abs(H_ref) < 1e-30:
        return None
    return float(H_final / H_ref)


# ─────────────────────────────────────────────────────────────────────────────
# Non-VacuumEngine3D (FDTD-scalar) branch — the harness wraps a scalar-field
# engine's run() loop; channels that are undefined for a scalar field (Γ needs
# the K4 z_local_field; (2,3)/helicity/Q_hopf need the topological state) are
# marked N/A so a missing read is never a false null result (prereg §3).
# ─────────────────────────────────────────────────────────────────────────────
def fdtd_scalar_report(engine, name: str = "", config: Optional[dict] = None) -> "ObservableReport":
    """Build an ObservableReport for a non-VacuumEngine3D scalar-field engine
    (e.g. MasterEquationFDTD). Marks the topological / Γ channels N/A (they are
    undefined for a scalar field) and reads whatever scalar diagnostics the
    engine does expose. Honest N/A, not a null."""
    report = ObservableReport(name=name, config=dict(config or {}))
    na_channels = ["reflection", "power_split", "reactance_XC", "reactance_XL",
                   "theta_RP", "winding_2_3", "energy7", "boundary_MQJ",
                   "helicity", "hopf", "charge_density"]
    report.full["_not_applicable"] = {
        ch: "undefined for a scalar field (no K4 z_local_field / topological state)"
        for ch in na_channels
    }
    report.inconclusive = list(na_channels)
    report.metadata.update({
        "engine_class": type(engine).__name__,
        "engine_kind": "fdtd-scalar",
        "note": "scalar-field engine — topological + Γ channels N/A by construction",
    })
    # best-effort scalar reads (energy / spectral) if the engine exposes them
    for attr in ("total_energy", "energy"):
        fn = getattr(engine, attr, None)
        if callable(fn):
            try:
                report.full["scalar_energy"] = float(fn())
                break
            except Exception:   # pragma: no cover
                pass
    return report
