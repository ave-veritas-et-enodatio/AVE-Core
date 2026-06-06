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

    # Steps 2-5 implement these; declared here so the contract is visible.
    def sample_cheap(self, engine) -> dict:  # noqa: D401 — filled Step 2-4/6
        """O(N) per-step scalar channels. Implemented incrementally per §6."""
        raise NotImplementedError("ObservableBattery.sample_cheap — filled Step 2-4/6")

    def extract_full(self, engine) -> dict:  # noqa: D401 — filled Step 5
        """Heavy post-run field-walks (run once). Implemented Step 5."""
        raise NotImplementedError("ObservableBattery.extract_full — filled Step 5")
