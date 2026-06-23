"""model.py — the channel-agnostic BenchModel spine (GAP-1).

The top-level pipeline that composes the four ave.bench contracts (sweep /
apparatus / snr / validate) plus the observable + sensitivity legs into ONE
"given a bench spec -> model AVE + SM, sweep, score" pipeline whose output
record IS the bankability schema.

    bench-spec -> (substrate engine + coupling) -> observable
                -> SM-baseline co-sweep -> 8-gate bankability record

CHANNEL-AGNOSTIC by construction: the spine never imports a channel's physics.
A BenchSpec supplies the AVE observable and the SM/null counterpart as CALLABLES
(driven over one shared grid by run_divergence_sweep — the no-strawman rule), so
the same spine models whatever prediction survives Fork-1 (EM-photon
birefringence / optical-activity today; a bulk/V-sector observable later if a
clever bench reaches one). The reference adopters that DO import channel physics
live in ``ave.bench.adopters``; this module wires only the bench-agnostic
contracts.

THE 8 GATES ARE MACHINE-CHECKABLE RECORD FIELDS, NOT PROSE (charter §4). Each
gate is a frozen dataclass with a computed ``GateStatus`` plus the concrete
fields that operationalize its grounding discipline. The whole record
serializes to a JSON-safe dict via ``as_dict()``.

  G1 validate-on-known   — every kill-verdict carries a modeled positive control
                           through the IDENTICAL chain (named known reference +
                           resolution-margin + explicit INCONCLUSIVE bin).
                           Grounding: cleave-01-requirements-boundary-conditions.md:42,157
                           + ave.bench.validate.assert_recovers_known.
  G2 forced-FORM-not-     — per-axis chord/echo tag; the infra REFUSES to label
     echoed-VALUE           an echo axis as the falsifiable discriminator (Fork-3);
                           >=3 interpretive alternatives per non-trivial axis.
                           Grounding: ave-discrimination-check Step 1.5/2.
  G3 SM co-computed,      — {AVE leg, SM leg, discriminator-axis MAGNITUDE|RATIO|
     same machinery         SLOPE|ZERO_VS_NONZERO, verdict}; a discriminator
                           claimed on the axis SHARED with the counterpart
                           auto-flags non-bankable. Grounding:
                           ave-discrimination-check Step 2/2.5 + run_divergence_sweep.
  G4 derived-vs-asserted  — 4 mandatory rows (coupling / probe / magnitude /
     ledger                 observable), each DERIVED(file:line) |
                           ENGINEERING-CHOICE(rationale) | ASSERTED(flag). Any
                           ASSERTED row -> FORK-status, not bankable. Grounding:
                           feedback_experiments_fully_lattice_derived.
  G5 sensitivity sweep,   — response surface over each load-bearing parameter;
     not single-point       in-window fraction; verdict-flip boundary; a
                           tuned-point-only positive books NEGATIVE. Grounding:
                           ave-engineering-program-rigor (the sweep IS the
                           rescue-fill discriminator).
  G6 symmetric standard   — per ledger row "does the counterpart also import /
                           fit / assert?" -> PEER not demote; a genuine AVE-only
                           shortfall STANDS. Grounding:
                           feedback_consensus_bias_symmetric_standard.
  G7 frozen prereg        — expected magnitude WITH canonical-primitive
                           dimensional eval; outcome bins incl. INCONCLUSIVE;
                           frozen before measurement. Grounding: ave-prereg
                           Step 3/3.5/3.6.
  G8 evidence-framing     — explicit gating-vs-non-gating axis; binding-spec
                           class (LEVEL-STABILITY/drift | SINGLE-SHOT | SNR-floor);
                           full sweep denominator (no selection-from-pool).
                           Grounding: ave-evidence-framing-discipline.

VERDICT (Fork-2 graded ladder, DEFAULT APPLIED per launch handoff §3): G1-G5
hard-gating + G6-G8 framing-discipline, with an intermediate tier
``BANKABLE_AS_DISCRIMINATOR`` for a prediction that passes the discriminator
gates with an open G4 sizing row (birefringence today: a forced-given-alpha
ratio + tree-vs-loop FORM chord whose MAGNITUDE is a symmetric alpha-echo). The
fully-``BANKABLE`` tier is reserved for a forced-FORM chord on an UNSHARED axis
(the zero-vs-nonzero optical-activity case: QED == 0, AVE != 0). A non-physics
validate-on-known pilot (cRIO) books ``VALIDATE_ON_KNOWN_PASS/FAIL`` — the
bankability tiers do not apply to a positive-control chain validation.

DISCIPLINE: this module imports ZERO physical constants (like sweep/snr/validate
it is pure orchestration + scoring logic). All physics lives in the
caller-supplied callables, which import from ave.core.constants.
"""

from __future__ import annotations

import itertools
from dataclasses import dataclass
from enum import Enum
from typing import Callable, Optional

import numpy as np

from ave.bench.snr import signal_vs_floor, time_to_n_sigma
from ave.bench.sweep import DivergenceSweepResult, run_divergence_sweep
from ave.bench.validate import KnownComparison, compare_to_known

# ============================================================================
# ENUMS — the machine-checkable vocabularies
# ============================================================================


class GateStatus(str, Enum):
    """Per-gate outcome.

    PASS / FAIL are the hard-gate (G1-G5) verdicts. FRAMING_FLAG is the
    framing-discipline (G6-G8) "recorded, advisory, does not hard-gate" state.
    HEDGED marks a gate that passes on its DERIVED core but rides a transparently
    first-cut leg (e.g. the birefringence OQ-1 sensitivity model). INCONCLUSIVE
    is the explicit no-result bin. NOT_APPLICABLE is for gates that do not bear
    on a given bench (e.g. the bankability gates of a validate-on-known pilot).
    """

    PASS = "PASS"
    FAIL = "FAIL"
    FRAMING_FLAG = "FRAMING_FLAG"
    HEDGED = "HEDGED"
    INCONCLUSIVE = "INCONCLUSIVE"
    NOT_APPLICABLE = "N/A"


class Verdict(str, Enum):
    """Overall bench-model verdict (Fork-2 graded ladder)."""

    BANKABLE = "BANKABLE"
    BANKABLE_AS_DISCRIMINATOR = "BANKABLE_AS_DISCRIMINATOR"
    NOT_BANKABLE = "NOT_BANKABLE"
    VALIDATE_ON_KNOWN_PASS = "VALIDATE_ON_KNOWN_PASS"
    VALIDATE_ON_KNOWN_FAIL = "VALIDATE_ON_KNOWN_FAIL"


class ChordEcho(str, Enum):
    """consistency-vs-emergence classification of an axis's FORM or VALUE.

    CHORD = forced FORM the substrate independently selects (AVE-distinct).
    ECHO  = imported VALUE / symmetric alpha-echo (a consistency match the
            substrate does not select; buys no discrimination).
    MIXED = form-derived / value-imported (the G-ruling 'mixed' tag).
    """

    CHORD = "chord"
    ECHO = "echo"
    MIXED = "mixed"


class DiscriminatorAxis(str, Enum):
    """The axis on which AVE is claimed to diverge from the counterpart.

    SLOPE / integer-exponent is the gold-standard (calibration-free, sharp).
    ZERO_VS_NONZERO is the strongest existence discriminator (counterpart
    identically zero). MAGNITUDE and RATIO carry calibration; a RATIO claimed on
    a SHARED FORM is non-discriminating (G3 Step 2.5 auto-flag).
    """

    MAGNITUDE = "MAGNITUDE"
    RATIO = "RATIO"
    SLOPE = "SLOPE"
    ZERO_VS_NONZERO = "ZERO_VS_NONZERO"
    EXISTENCE = "EXISTENCE"


class SharedWith(str, Enum):
    """What AVE shares with the counterpart on this axis (G3 Step 2.5)."""

    FORM = "FORM"  # shared functional form -> MAGNITUDE discriminates
    SCALE = "SCALE"  # shared scale -> RATIO/SLOPE discriminates
    NONE = "NONE"  # unshared (e.g. counterpart identically zero)


class LedgerStatus(str, Enum):
    """Derived-vs-asserted status of a G4 ledger row."""

    DERIVED = "DERIVED"  # carries a file:line provenance
    ENGINEERING_CHOICE = "ENGINEERING-CHOICE"  # a labeled apparatus/scale choice
    ASSERTED = "ASSERTED"  # an un-grounded flag -> FORK-status


class LedgerAspect(str, Enum):
    """The four mandatory G4 ledger aspects."""

    COUPLING = "coupling"
    PROBE = "probe"
    MAGNITUDE = "magnitude"
    OBSERVABLE = "observable"


class BindingSpec(str, Enum):
    """G8 binding-spec class — what kind of measurement binds the claim."""

    LEVEL_STABILITY_DRIFT = "LEVEL-STABILITY/drift"
    SINGLE_SHOT = "SINGLE-SHOT"
    SNR_FLOOR = "SNR-floor"


class VerifiabilityClass(str, Enum):
    """G8 verifiability class (ave-evidence-framing-discipline)."""

    A_DIRECT = "A_directly_verifiable"
    B_CATEGORICAL = "B_categorically_verifiable"
    C_SCOPE_BOUND = "C_scope_bound"
    D_SELECTION_FROM_POOL = "D_selection_from_pool"


class InterpretiveAlternative(str, Enum):
    """G2 interpretive-alternative kinds (ave-discrimination-check Step 1.5)."""

    EXACT = "exact"
    APPROX_WITH_RESIDUAL = "approx_with_residual"
    FLOOR = "floor"
    CEILING = "ceiling"
    COINCIDENCE = "coincidence"
    TAUTOLOGY = "tautology"
    STRATIFICATION = "stratification"


class CorpusState(str, Enum):
    """G7 prereg corpus-state (ave-prereg Step 3)."""

    CLOSED = "closed"
    PARTIAL = "partial"
    OPEN = "open"
    GREEN_FIELD = "green-field"


class OutcomeKind(str, Enum):
    """G7 discriminating-outcome kind; an INCONCLUSIVE bin is mandatory."""

    POSITIVE = "positive"
    NEGATIVE = "negative"
    NULL = "null"
    INCONCLUSIVE = "inconclusive"


# ============================================================================
# SPEC-SIDE DATACLASSES — the bench author's declaration surface
# ============================================================================


@dataclass(frozen=True)
class LedgerRow:
    """One row of the G4 derived-vs-asserted ledger (also feeds G6).

    Attributes
    ----------
    aspect : LedgerAspect
        One of the four mandatory aspects (coupling / probe / magnitude /
        observable).
    status : LedgerStatus
        DERIVED | ENGINEERING-CHOICE | ASSERTED.
    provenance : str
        file:line for DERIVED, the labeled rationale for ENGINEERING-CHOICE, the
        flag note for ASSERTED.
    sm_also : bool
        G6 symmetric-standard: does the SM/QED counterpart ALSO import / fit /
        assert this same aspect? If True the row is a PEER (not an AVE-only
        shortfall); if False and the AVE row is ENGINEERING-CHOICE/ASSERTED it is
        a genuine AVE-only shortfall that STANDS.
    """

    aspect: LedgerAspect
    status: LedgerStatus
    provenance: str
    sm_also: bool = False

    def as_dict(self) -> dict:
        return {
            "aspect": self.aspect.value,
            "status": self.status.value,
            "provenance": self.provenance,
            "sm_also": self.sm_also,
        }


@dataclass(frozen=True)
class AxisTag:
    """A per-discriminator-axis chord/echo + discrimination classification (G2/G3).

    Attributes
    ----------
    name : str
        Human-readable axis name (e.g. "birefringence par-perp coefficient ratio").
    form_tag : ChordEcho
        Is the FORM a chord (forced) or an echo (imported)?
    value_tag : ChordEcho
        Is the MAGNITUDE/VALUE a chord or an echo? (Birefringence: FORM chord,
        VALUE echo — alpha imported both sides.)
    discriminator_axis : DiscriminatorAxis
        MAGNITUDE | RATIO | SLOPE | ZERO_VS_NONZERO | EXISTENCE.
    shared_with : SharedWith
        FORM (shared functional form), SCALE (shared scale), or NONE.
    is_gating_axis : bool
        Is this the axis the bench's falsifiable verdict actually gates on? (G8
        gating-vs-non-gating; Fork-3 refusal triggers if a gating axis is an echo.)
    calibration_free : bool
        True for SLOPE/integer-exponent axes (gold standard); False when the axis
        carries an absolute-prefactor/gain calibration (a magnitude echo).
    interpretive_alternatives : tuple[InterpretiveAlternative, ...]
        >=3 enumerated alternatives for a non-trivial axis (G2 Step 1.5).
    rationale : str
        One-line justification of the tags.
    """

    name: str
    form_tag: ChordEcho
    value_tag: ChordEcho
    discriminator_axis: DiscriminatorAxis
    shared_with: SharedWith
    is_gating_axis: bool
    calibration_free: bool
    interpretive_alternatives: tuple[InterpretiveAlternative, ...] = ()
    rationale: str = ""

    def as_dict(self) -> dict:
        return {
            "name": self.name,
            "form_tag": self.form_tag.value,
            "value_tag": self.value_tag.value,
            "discriminator_axis": self.discriminator_axis.value,
            "shared_with": self.shared_with.value,
            "is_gating_axis": self.is_gating_axis,
            "calibration_free": self.calibration_free,
            "interpretive_alternatives": [a.value for a in self.interpretive_alternatives],
            "rationale": self.rationale,
        }


@dataclass(frozen=True)
class DimensionalIngredient:
    """One ingredient of a G7 expected-magnitude dimensional eval (Step 3.5)."""

    symbol: str
    canonical_value: float
    source_ref: str  # constants.py / INVARIANT file:line

    def as_dict(self) -> dict:
        return {
            "symbol": self.symbol,
            "canonical_value": self.canonical_value,
            "source_ref": self.source_ref,
        }


@dataclass(frozen=True)
class Prereg:
    """A frozen pre-registration (G7; ave-prereg Step 3/3.5/3.6).

    The spine does not author preregs; it RECORDS a reference to a frozen one and
    machine-checks the mandatory structure (an INCONCLUSIVE outcome bin must
    exist; a magnitude expectation must carry a dimensional eval).

    Attributes
    ----------
    ref : str
        Path (cite-don't-duplicate) to the frozen prereg doc.
    frozen : bool
        True once the prereg is frozen BEFORE measurement.
    corpus_state : CorpusState
    prior_work_refs : tuple[str, ...]
        file:line list of prior corpus work (Step 3).
    prediction : str
    rationale : str
    discriminating_outcomes : tuple[tuple[OutcomeKind, str], ...]
        (kind, text) pairs; MUST include an INCONCLUSIVE bin.
    falsifier : str
    expected_magnitude_eval : tuple[DimensionalIngredient, ...]
        Empty unless the expectation is a scaling-law/magnitude claim, in which
        case the canonical-primitive ingredients are listed (Step 3.5).
    """

    ref: str
    frozen: bool
    corpus_state: CorpusState
    prior_work_refs: tuple[str, ...]
    prediction: str
    rationale: str
    discriminating_outcomes: tuple[tuple[OutcomeKind, str], ...]
    falsifier: str
    expected_magnitude_eval: tuple[DimensionalIngredient, ...] = ()

    @property
    def has_inconclusive_bin(self) -> bool:
        return any(kind is OutcomeKind.INCONCLUSIVE for kind, _ in self.discriminating_outcomes)

    def as_dict(self) -> dict:
        return {
            "ref": self.ref,
            "frozen": self.frozen,
            "corpus_state": self.corpus_state.value,
            "prior_work_refs": list(self.prior_work_refs),
            "prediction": self.prediction,
            "rationale": self.rationale,
            "discriminating_outcomes": [{"kind": k.value, "text": t} for k, t in self.discriminating_outcomes],
            "falsifier": self.falsifier,
            "expected_magnitude_eval": [d.as_dict() for d in self.expected_magnitude_eval],
            "has_inconclusive_bin": self.has_inconclusive_bin,
        }


@dataclass(frozen=True)
class ValidateOnKnownSpec:
    """G1 validate-on-known positive control (cleave-01-requirements:42,157).

    Attributes
    ----------
    reference_label : str
        Named known reference (PDG/CODATA/datasheet) the control recovers.
    computed : float
        The value the IDENTICAL modeled chain produced for the known input.
    reference : float
        The labeled known target.
    tol : float
        Relative tolerance the recovery is adjudicated at.
    uncertainty : Optional[float]
        Reference uncertainty for an n_sigma report.
    inconclusive_bin : str
        The explicit INCONCLUSIVE/UNRESOLVED bin definition (e.g. "feature within
        3x the Stage-C drift floor -> UNRESOLVED, never a result").
    through_identical_chain : bool
        Attestation that the positive control rode the SAME modeling chain as the
        kill-verdict (not a separate shortcut path). Required True for G1 PASS.
    """

    reference_label: str
    computed: float
    reference: float
    tol: float
    uncertainty: Optional[float] = None
    inconclusive_bin: str = ""
    through_identical_chain: bool = True

    def as_dict(self) -> dict:
        return {
            "reference_label": self.reference_label,
            "computed": self.computed,
            "reference": self.reference,
            "tol": self.tol,
            "uncertainty": self.uncertainty,
            "inconclusive_bin": self.inconclusive_bin,
            "through_identical_chain": self.through_identical_chain,
        }


@dataclass(frozen=True)
class EvidenceFraming:
    """G8 evidence-framing declaration (ave-evidence-framing-discipline).

    Attributes
    ----------
    gating_axis : str
        The single axis the bankability verdict gates on.
    non_gating_axes : tuple[str, ...]
        Other reported axes that do NOT gate the verdict.
    binding_spec : BindingSpec
        LEVEL-STABILITY/drift | SINGLE-SHOT | SNR-floor.
    verifiability_class : VerifiabilityClass
        A/B/C/D; a gating claim must be verified, not asserted.
    verification_artifact_ref : str
        wc -l / git diff --stat / explicit-bounds / denominator artifact.
    n_displayed : int
        Number of instances displayed.
    n_total_run : int
        Full sweep denominator (every relevant instance, incl. nulls/failures).
    omitted_instances : tuple[str, ...]
        Enumerated omitted instances when n_displayed < n_total_run.
    """

    gating_axis: str
    non_gating_axes: tuple[str, ...]
    binding_spec: BindingSpec
    verifiability_class: VerifiabilityClass
    verification_artifact_ref: str
    n_displayed: int
    n_total_run: int
    omitted_instances: tuple[str, ...] = ()

    @property
    def selection_from_pool_clean(self) -> bool:
        """True if there is no undisclosed selection-from-pool."""
        if self.n_displayed >= self.n_total_run:
            return True
        # subset displayed -> the omitted instances must be enumerated
        return len(self.omitted_instances) >= (self.n_total_run - self.n_displayed)

    def as_dict(self) -> dict:
        return {
            "gating_axis": self.gating_axis,
            "non_gating_axes": list(self.non_gating_axes),
            "binding_spec": self.binding_spec.value,
            "verifiability_class": self.verifiability_class.value,
            "verification_artifact_ref": self.verification_artifact_ref,
            "n_displayed": self.n_displayed,
            "n_total_run": self.n_total_run,
            "omitted_instances": list(self.omitted_instances),
            "selection_from_pool_clean": self.selection_from_pool_clean,
        }


@dataclass(frozen=True)
class SensitivitySpec:
    """G5 sensitivity-sweep inputs (ave-engineering-program-rigor).

    The spine evaluates a verdict predicate over an N-D cube of load-bearing
    parameters and computes the in-window fraction + verdict-flip boundary that
    neither observable leg provides. ``verdict_fn`` maps an observable value to
    True (in-window / positive) or False.

    Attributes
    ----------
    observable_of : Callable[..., float]
        Maps a config dict of load-bearing params -> the observable scalar. Called
        as ``observable_of(**config)``.
    param_grids : dict[str, tuple[float, ...]]
        Each load-bearing parameter name -> its swept value list. The cube is the
        product of ALL axes (none privileged). Must be non-empty (single-point
        sweeps book the result NEGATIVE per the discipline).
    verdict_fn : Callable[[float], bool]
        Maps an observable value -> in-window (True) / out-of-window (False).
    convergence_param : Optional[str]
        The grid/resolution axis whose values are a convergence sweep (required
        for a magnitude claim; the spine flags BLOCKED if a magnitude claim lacks
        one). It is one of the param_grids keys.
    response_surface_ref : str
        Path to the plotted response surface (figure), if produced.
    """

    observable_of: Callable[..., float]
    param_grids: dict[str, tuple[float, ...]]
    verdict_fn: Callable[[float], bool]
    convergence_param: Optional[str] = None
    response_surface_ref: str = ""


@dataclass(frozen=True)
class BenchSpec:
    """The full input declaration the spine consumes.

    Attributes
    ----------
    name : str
        Bench name.
    channel : str
        The physical channel (e.g. "EM-photon", "shear", "bulk-V-sector",
        "EE-capacitance"). Free text — the spine is channel-agnostic.
    ave_observable : Callable[[float], float]
        AVE prediction as f(sweep-variable). POSITIVE magnitude (the caller wraps
        with abs() if the physical quantity is signed) so the divergence ratio is
        well-defined.
    sm_observable : Callable[[float], float]
        SM/QED/null counterpart as f(THE SAME sweep-variable). Driven over the
        same grid by run_divergence_sweep (the no-strawman contract).
    sweep_grid : np.ndarray
        The shared 1-D grid for the AVE-vs-SM co-sweep (G3).
    validate_on_known : ValidateOnKnownSpec
        The G1 positive control.
    ledger_rows : tuple[LedgerRow, ...]
        The G4 ledger; must cover all four mandatory aspects.
    axis_tags : tuple[AxisTag, ...]
        The G2/G3 per-axis chord/echo classification; exactly one is the gating
        axis.
    prereg : Prereg
        The G7 frozen prereg reference.
    evidence_framing : EvidenceFraming
        The G8 framing declaration.
    sensitivity : Optional[SensitivitySpec]
        The G5 sweep inputs. None only for a non-physics validate-on-known pilot.
    is_physics_test : bool
        True for a bankability candidate; False for a validate-on-known pilot
        (cRIO) whose verdict is VALIDATE_ON_KNOWN_*, not a bankability tier.
    magnitude_is_claimed : bool
        True if the bench HEADLINES a quantitative magnitude/ratio (forces a G7
        canonical-primitive dimensional eval). False if the headline is
        FORM/existence only.
    result_is_numerical : bool
        True if the headline magnitude comes from a DISCRETIZED simulation (a grid
        could introduce an artifact). A closed-form analytic result has no
        discretization to converge. NOTE: this flag alone does NOT earn the
        convergence-sweep exemption — see ``analytic_provenance`` (self-attestation
        cannot dodge the G5 requirement).
    analytic_provenance : str
        Positive provenance (a closed-form citation, e.g. "coefficient_ratio_
        differential() closed form, birefringence.py:328") that the headline
        magnitude is analytic. ONLY a magnitude claim that is non-numerical AND
        carries a non-empty analytic_provenance earns the G5 convergence-sweep
        exemption; a bare result_is_numerical=False with no provenance is BLOCKED
        (the gate refuses to take "it's analytic" on the author's word alone).
    regime_note : str
        Optional free-text physical-regime note (e.g. "deep Regime I, per-node
        A0 ~ 1e-11" for cRIO), surfaced in the record for context.
    snr_signal : Optional[float]
        Optional detected signal rate [Hz] for an SNR window read.
    snr_floor : Optional[float]
        Optional additive noise floor rate [Hz].
    """

    name: str
    channel: str
    ave_observable: Callable[[float], float]
    sm_observable: Callable[[float], float]
    sweep_grid: np.ndarray
    validate_on_known: ValidateOnKnownSpec
    ledger_rows: tuple[LedgerRow, ...]
    axis_tags: tuple[AxisTag, ...]
    prereg: Prereg
    evidence_framing: EvidenceFraming
    sensitivity: Optional[SensitivitySpec] = None
    is_physics_test: bool = True
    magnitude_is_claimed: bool = False
    result_is_numerical: bool = False
    analytic_provenance: str = ""
    regime_note: str = ""
    snr_signal: Optional[float] = None
    snr_floor: Optional[float] = None

    @property
    def gating_axis(self) -> Optional[AxisTag]:
        """The single axis the bankability verdict gates on (G8)."""
        gating = [a for a in self.axis_tags if a.is_gating_axis]
        return gating[0] if gating else None


# ============================================================================
# GATE-RESULT DATACLASSES — the machine-checkable record fields
# ============================================================================


@dataclass(frozen=True)
class G1ValidateOnKnown:
    """G1 — validate-on-known positive control through the IDENTICAL chain."""

    status: GateStatus
    comparison: KnownComparison
    resolution_margin: float  # tol - rel_error (positive => headroom)
    through_identical_chain: bool
    inconclusive_bin: str

    def as_dict(self) -> dict:
        return {
            "status": self.status.value,
            "label": self.comparison.label,
            "computed": self.comparison.value,
            "reference": self.comparison.reference,
            "tol": self.comparison.tol,
            "rel_error": self.comparison.rel_error,
            "n_sigma": self.comparison.n_sigma,
            "passed": self.comparison.passed,
            "resolution_margin": self.resolution_margin,
            "through_identical_chain": self.through_identical_chain,
            "inconclusive_bin": self.inconclusive_bin,
            "summary": self.comparison.summary(),
        }


@dataclass(frozen=True)
class G2FormVsValue:
    """G2 — forced FORM, not echoed VALUE (Fork-3 refusal of an echo gating axis)."""

    status: GateStatus
    axes: tuple[AxisTag, ...]
    gating_axis_form_is_echo: bool  # Fork-3 trigger
    fork3_refused: bool
    interpretive_alternatives_ok: bool  # >=3 on the gating axis
    note: str

    def as_dict(self) -> dict:
        return {
            "status": self.status.value,
            "axes": [a.as_dict() for a in self.axes],
            "gating_axis_form_is_echo": self.gating_axis_form_is_echo,
            "fork3_refused": self.fork3_refused,
            "interpretive_alternatives_ok": self.interpretive_alternatives_ok,
            "note": self.note,
        }


@dataclass(frozen=True)
class G3SMCoComputed:
    """G3 — SM co-computed on the same machinery; discriminator-axis classified."""

    status: GateStatus
    discriminator_axis: DiscriminatorAxis
    shared_with: SharedWith
    field_independent: bool
    sm_identically_zero: bool  # COMPUTED: counterpart structurally zero on the grid
    observables_diverge: bool  # COMPUTED: ratio departs from 1 somewhere on the grid
    ratio_value: float  # the constant ratio if field-independent, else max
    max_divergence: float
    non_discriminating_on_shared_axis: bool
    has_independent_form_chord: bool
    axis_contradicts_sweep: bool  # declared label inconsistent with the computed sweep
    n_grid: int
    note: str

    def as_dict(self) -> dict:
        return {
            "status": self.status.value,
            "discriminator_axis": self.discriminator_axis.value,
            "shared_with": self.shared_with.value,
            "field_independent": self.field_independent,
            "sm_identically_zero": self.sm_identically_zero,
            "observables_diverge": self.observables_diverge,
            "ratio_value": self.ratio_value,
            "max_divergence": self.max_divergence,
            "non_discriminating_on_shared_axis": self.non_discriminating_on_shared_axis,
            "has_independent_form_chord": self.has_independent_form_chord,
            "axis_contradicts_sweep": self.axis_contradicts_sweep,
            "n_grid": self.n_grid,
            "note": self.note,
        }


@dataclass(frozen=True)
class G4Ledger:
    """G4 — derived-vs-asserted ledger (4 mandatory rows)."""

    status: GateStatus
    rows: tuple[LedgerRow, ...]
    all_aspects_present: bool
    has_asserted_row: bool
    magnitude_row_status: Optional[LedgerStatus]
    note: str

    def as_dict(self) -> dict:
        return {
            "status": self.status.value,
            "rows": [r.as_dict() for r in self.rows],
            "all_aspects_present": self.all_aspects_present,
            "has_asserted_row": self.has_asserted_row,
            "magnitude_row_status": (self.magnitude_row_status.value if self.magnitude_row_status else None),
            "note": self.note,
        }


@dataclass(frozen=True)
class ParamSweepResult:
    """Per-parameter slice of the G5 sensitivity sweep."""

    param_name: str
    grid_min: float
    grid_max: float
    n_points: int
    flip_boundary: Optional[float]  # value where the marginal verdict crosses 0.5
    is_convergence_axis: bool

    def as_dict(self) -> dict:
        return {
            "param_name": self.param_name,
            "grid_min": self.grid_min,
            "grid_max": self.grid_max,
            "n_points": self.n_points,
            "flip_boundary": self.flip_boundary,
            "is_convergence_axis": self.is_convergence_axis,
        }


@dataclass(frozen=True)
class G5Sensitivity:
    """G5 — sensitivity sweep, not single-point (the rescue-fill discriminator)."""

    status: GateStatus
    n_configs: int
    n_in_window: int
    in_window_fraction: float
    tuned_point_only: bool
    verdict_flips_within_range: bool
    result_kind: str  # "robust_positive" | "tuned_positive" | "no_positive"
    per_param: tuple[ParamSweepResult, ...]
    convergence_sweep_present: bool
    magnitude_claim_blocked: bool  # magnitude claimed, no convergence sweep, no analytic provenance
    analytic_exemption_granted: bool  # non-numerical + positive provenance -> convergence N/A
    response_surface_ref: str
    note: str

    def as_dict(self) -> dict:
        return {
            "status": self.status.value,
            "n_configs": self.n_configs,
            "n_in_window": self.n_in_window,
            "in_window_fraction": self.in_window_fraction,
            "tuned_point_only": self.tuned_point_only,
            "verdict_flips_within_range": self.verdict_flips_within_range,
            "result_kind": self.result_kind,
            "per_param": [p.as_dict() for p in self.per_param],
            "convergence_sweep_present": self.convergence_sweep_present,
            "magnitude_claim_blocked": self.magnitude_claim_blocked,
            "analytic_exemption_granted": self.analytic_exemption_granted,
            "response_surface_ref": self.response_surface_ref,
            "note": self.note,
        }


@dataclass(frozen=True)
class G6SymmetricStandard:
    """G6 — symmetric standard: peer-with-counterpart vs genuine AVE-only shortfall."""

    status: GateStatus
    peer_rows: tuple[str, ...]  # aspects where SM also imports/fits/asserts
    ave_only_shortfalls: tuple[str, ...]  # aspects where ONLY AVE imports/fits
    note: str

    def as_dict(self) -> dict:
        return {
            "status": self.status.value,
            "peer_rows": list(self.peer_rows),
            "ave_only_shortfalls": list(self.ave_only_shortfalls),
            "note": self.note,
        }


@dataclass(frozen=True)
class G7FrozenPrereg:
    """G7 — frozen prereg before measurement (with dimensional eval if magnitude)."""

    status: GateStatus
    prereg_ref: str
    frozen: bool
    has_inconclusive_bin: bool
    dimensional_eval_present: bool
    dimensional_eval_required: bool
    note: str

    def as_dict(self) -> dict:
        return {
            "status": self.status.value,
            "prereg_ref": self.prereg_ref,
            "frozen": self.frozen,
            "has_inconclusive_bin": self.has_inconclusive_bin,
            "dimensional_eval_present": self.dimensional_eval_present,
            "dimensional_eval_required": self.dimensional_eval_required,
            "note": self.note,
        }


@dataclass(frozen=True)
class G8EvidenceFraming:
    """G8 — evidence-framing (gating axis, binding-spec class, full denominator)."""

    status: GateStatus
    gating_axis: str
    binding_spec: BindingSpec
    verifiability_class: VerifiabilityClass
    selection_from_pool_clean: bool
    n_displayed: int
    n_total_run: int
    note: str

    def as_dict(self) -> dict:
        return {
            "status": self.status.value,
            "gating_axis": self.gating_axis,
            "binding_spec": self.binding_spec.value,
            "verifiability_class": self.verifiability_class.value,
            "selection_from_pool_clean": self.selection_from_pool_clean,
            "n_displayed": self.n_displayed,
            "n_total_run": self.n_total_run,
            "note": self.note,
        }


@dataclass(frozen=True)
class BankabilityRecord:
    """The spine's output — the 8 gates + verdict as machine-checkable fields."""

    bench_name: str
    channel: str
    is_physics_test: bool
    verdict: Verdict
    verdict_rationale: str
    g1: G1ValidateOnKnown
    g2: G2FormVsValue
    g3: G3SMCoComputed
    g4: G4Ledger
    g5: Optional[G5Sensitivity]
    g6: G6SymmetricStandard
    g7: G7FrozenPrereg
    g8: G8EvidenceFraming
    regime_note: str = ""
    snr_time_to_5sigma_s: Optional[float] = None
    snr_signal_vs_floor: Optional[float] = None

    @property
    def hard_gates_pass(self) -> bool:
        """G1-G5 hard gates all PASS (G5 None counts as fail for a physics test)."""
        g5_ok = self.g5 is not None and self.g5.status is GateStatus.PASS
        return (
            self.g1.status is GateStatus.PASS
            and self.g2.status is GateStatus.PASS
            and self.g3.status is GateStatus.PASS
            and self.g4.status is GateStatus.PASS
            and (g5_ok or not self.is_physics_test)
        )

    def as_dict(self) -> dict:
        return {
            "bench_name": self.bench_name,
            "channel": self.channel,
            "is_physics_test": self.is_physics_test,
            "verdict": self.verdict.value,
            "verdict_rationale": self.verdict_rationale,
            "hard_gates_pass": self.hard_gates_pass,
            "regime_note": self.regime_note,
            "snr_time_to_5sigma_s": self.snr_time_to_5sigma_s,
            "snr_signal_vs_floor": self.snr_signal_vs_floor,
            "gates": {
                "G1_validate_on_known": self.g1.as_dict(),
                "G2_form_vs_value": self.g2.as_dict(),
                "G3_sm_co_computed": self.g3.as_dict(),
                "G4_derived_vs_asserted": self.g4.as_dict(),
                "G5_sensitivity": self.g5.as_dict() if self.g5 else None,
                "G6_symmetric_standard": self.g6.as_dict(),
                "G7_frozen_prereg": self.g7.as_dict(),
                "G8_evidence_framing": self.g8.as_dict(),
            },
        }

    def summary(self) -> str:
        """One-screen human-readable summary."""
        lines = [
            f"=== BenchModel bankability record: {self.bench_name} ({self.channel}) ===",
            f"VERDICT: {self.verdict.value}",
            f"  {self.verdict_rationale}",
            f"  physics-test: {self.is_physics_test}   hard-gates(G1-G5)-pass: {self.hard_gates_pass}",
        ]
        if self.regime_note:
            lines.append(f"  regime: {self.regime_note}")
        gate_objs = [
            ("G1 validate-on-known", self.g1.status),
            ("G2 form-not-value", self.g2.status),
            ("G3 SM co-computed", self.g3.status),
            ("G4 derived-vs-asserted", self.g4.status),
            ("G5 sensitivity", self.g5.status if self.g5 else GateStatus.NOT_APPLICABLE),
            ("G6 symmetric-standard", self.g6.status),
            ("G7 frozen-prereg", self.g7.status),
            ("G8 evidence-framing", self.g8.status),
        ]
        for label, status in gate_objs:
            lines.append(f"    {status.value:>13}  {label}")
        return "\n".join(lines)


# ============================================================================
# GATE EVALUATORS — populate each gate from the spec (machine checks)
# ============================================================================


def _eval_g1(spec: BenchSpec) -> G1ValidateOnKnown:
    """G1: recover-a-known through the identical chain (ave.bench.validate)."""
    v = spec.validate_on_known
    cmp = compare_to_known(v.computed, v.reference, v.tol, v.reference_label, uncertainty=v.uncertainty)
    margin = v.tol - cmp.rel_error
    if not v.through_identical_chain:
        status = GateStatus.FAIL
    elif not v.inconclusive_bin:
        # a kill-verdict with no explicit INCONCLUSIVE bin cannot pass G1
        status = GateStatus.FAIL
    elif cmp.passed:
        status = GateStatus.PASS
    else:
        status = GateStatus.FAIL
    return G1ValidateOnKnown(
        status=status,
        comparison=cmp,
        resolution_margin=margin,
        through_identical_chain=v.through_identical_chain,
        inconclusive_bin=v.inconclusive_bin,
    )


def _eval_g2(spec: BenchSpec) -> G2FormVsValue:
    """G2: refuse an echo gating axis (Fork-3); require >=3 interpretive alts."""
    gating = spec.gating_axis
    gating_form_echo = bool(gating is not None and gating.form_tag is ChordEcho.ECHO)
    fork3_refused = gating_form_echo
    alts_ok = bool(gating is not None and len(gating.interpretive_alternatives) >= 3)
    if fork3_refused:
        status = GateStatus.FAIL
        note = (
            "Fork-3 refusal: the declared falsifiable (gating) axis FORM is an "
            "echo — the infra refuses to model a prediction whose discriminator "
            "is an imported VALUE."
        )
    elif not alts_ok:
        status = GateStatus.FRAMING_FLAG
        note = "gating axis carries <3 interpretive alternatives (Step 1.5)."
    else:
        status = GateStatus.PASS
        note = "gating-axis FORM is a chord; >=3 interpretive alternatives enumerated."
    return G2FormVsValue(
        status=status,
        axes=spec.axis_tags,
        gating_axis_form_is_echo=gating_form_echo,
        fork3_refused=fork3_refused,
        interpretive_alternatives_ok=alts_ok,
        note=note,
    )


def _eval_g3(spec: BenchSpec, sweep: DivergenceSweepResult) -> G3SMCoComputed:
    """G3: classify the discriminator axis on the co-computed (same-grid) sweep."""
    gating = spec.gating_axis
    axis = gating.discriminator_axis if gating else DiscriminatorAxis.MAGNITUDE
    shared = gating.shared_with if gating else SharedWith.FORM

    # "identically zero" = a STRUCTURAL zero (the counterpart returns exactly 0,
    # e.g. QED parity-even -> zero optical rotation), NOT merely numerically small.
    # Physical observables can sit far below any absolute atol (a QED differential
    # delta_n ~ 1e-16) yet be structurally nonzero, so np.allclose(., 0, atol=1e-8)
    # would wrongly flag them zero and trigger the zero-vs-nonzero path. Use exact 0.
    sm_zero = bool(np.all(sweep.sm == 0.0))
    # field-independent ratio: constant across the grid (guard the inf/zero case)
    finite = np.isfinite(sweep.ratio)
    if sm_zero:
        field_independent = False
        ratio_value = float("inf")
    elif finite.any():
        r = sweep.ratio[finite]
        field_independent = bool(np.allclose(r, r[0], rtol=1e-6))
        ratio_value = float(r[0]) if field_independent else float(np.max(r))
    else:
        field_independent = False
        ratio_value = float("nan")

    # Do the co-computed observables actually diverge on the swept grid? (A
    # MAGNITUDE/RATIO discriminator where AVE == SM numerically is degenerate —
    # the observables are indistinguishable, so nothing is being discriminated.)
    if sm_zero:
        diverges = True
    elif finite.any():
        diverges = bool(np.any(np.abs(sweep.ratio[finite] - 1.0) > 1e-3))
    else:
        diverges = False

    # Step 2.5: discrimination claimed on the SHARED axis (a RATIO on a shared
    # FORM, or a MAGNITUDE on a shared SCALE) is non-discriminating.
    non_discriminating_shared = (shared is SharedWith.FORM and axis is DiscriminatorAxis.RATIO) or (
        shared is SharedWith.SCALE and axis is DiscriminatorAxis.MAGNITUDE
    )
    # an independent (NON-GATING) structural FORM chord can rescue a shared-axis
    # ratio to the discriminator tier (the birefringence tree-vs-loop case) — but
    # ONLY when the observables actually diverge (the degenerate branch below runs
    # first, so a rescue can never manufacture discrimination from a ratio ~ 1).
    # The gating axis cannot rescue its own shared-axis ratio.
    has_form_chord = any(
        (not a.is_gating_axis)
        and a.form_tag is ChordEcho.CHORD
        and a.discriminator_axis is not DiscriminatorAxis.MAGNITUDE
        for a in spec.axis_tags
    )

    # RECONCILE the declared label against the COMPUTED sweep — PASS is EARNED by
    # observed discrimination, never granted by a self-declared label (the gate
    # must be unriggable). A declared zero-vs-nonzero / existence axis requires a
    # computed structural zero; ANY discriminator requires the observables to
    # actually diverge (or the counterpart to be structurally zero).
    axis_claims_zero = axis in (DiscriminatorAxis.ZERO_VS_NONZERO, DiscriminatorAxis.EXISTENCE)
    axis_contradicts = axis_claims_zero and not sm_zero

    if not diverges and not sm_zero:
        # degenerate: AVE == SM on the grid (ratio ~ 1, counterpart NOT structurally
        # zero) — nothing is discriminated. UNCONDITIONAL, non-rescuable FAIL.
        status = GateStatus.FAIL
        note = (
            "degenerate: the co-computed observables do not diverge (ratio ~ 1) and the "
            "counterpart is not structurally zero — nothing is discriminated, NOT "
            "bankable (non-rescuable, no form chord can manufacture discrimination)."
        )
    elif axis_contradicts:
        # declared a zero-vs-nonzero / existence discriminator, but the COMPUTED
        # counterpart is not structurally zero — the label contradicts the sweep.
        status = GateStatus.FAIL
        note = (
            "declared a zero-vs-nonzero/existence discriminator, but the co-computed "
            "counterpart is NOT structurally zero (sm != 0) — the declared label "
            "contradicts the computed sweep, NOT bankable."
        )
    elif sm_zero:
        # genuine zero-vs-nonzero, COMPUTED (counterpart structurally zero on the grid).
        status = GateStatus.PASS
        note = "counterpart structurally zero on the grid (computed) — genuine zero-vs-nonzero discriminator."
    elif non_discriminating_shared and not has_form_chord:
        status = GateStatus.FAIL
        note = (
            "Step 2.5: discrimination claimed on the SHARED axis with no independent "
            "FORM chord — non-discriminating, NOT bankable."
        )
    elif non_discriminating_shared and has_form_chord:
        status = GateStatus.PASS
        note = (
            "shared-axis ratio rescued by an independent DIVERGING FORM-within-form "
            "chord (tree-vs-loop); discriminator tier (magnitude carries calibration)."
        )
    else:
        status = GateStatus.PASS
        note = "declared axis reconciled against a diverging co-computed sweep — AVE-distinct."

    return G3SMCoComputed(
        status=status,
        discriminator_axis=axis,
        shared_with=shared,
        field_independent=field_independent,
        sm_identically_zero=sm_zero,
        observables_diverge=diverges,
        ratio_value=ratio_value,
        max_divergence=float(sweep.max_divergence),
        non_discriminating_on_shared_axis=non_discriminating_shared,
        has_independent_form_chord=has_form_chord,
        axis_contradicts_sweep=axis_contradicts,
        n_grid=int(sweep.x.size),
        note=note,
    )


def _eval_g4(spec: BenchSpec) -> G4Ledger:
    """G4: 4 mandatory ledger aspects; any ASSERTED row -> FORK (FAIL)."""
    present = {row.aspect for row in spec.ledger_rows}
    all_present = present >= set(LedgerAspect)
    has_asserted = any(r.status is LedgerStatus.ASSERTED for r in spec.ledger_rows)
    mag_rows = [r for r in spec.ledger_rows if r.aspect is LedgerAspect.MAGNITUDE]
    mag_status = mag_rows[0].status if mag_rows else None

    if not all_present:
        missing = sorted(a.value for a in (set(LedgerAspect) - present))
        status = GateStatus.FAIL
        note = f"missing mandatory ledger aspect(s): {missing}"
    elif has_asserted:
        status = GateStatus.FAIL
        note = "an ASSERTED row -> FORK-status, not bankable."
    else:
        status = GateStatus.PASS
        note = "all 4 aspects present; none ASSERTED (DERIVED/ENGINEERING-CHOICE only)."
    return G4Ledger(
        status=status,
        rows=spec.ledger_rows,
        all_aspects_present=all_present,
        has_asserted_row=has_asserted,
        magnitude_row_status=mag_status,
        note=note,
    )


def _flip_boundary(values: np.ndarray, verdicts: np.ndarray) -> Optional[float]:
    """Marginal flip boundary along one axis: the value where in-window fraction
    crosses 0.5 (midpoint of the first crossing pair); None if no flip."""
    uniq = np.unique(values)
    if uniq.size < 2:
        return None
    fracs = np.array([float(np.mean(verdicts[values == u])) for u in uniq])
    for i in range(1, uniq.size):
        if (fracs[i - 1] >= 0.5) != (fracs[i] >= 0.5):
            return float(0.5 * (uniq[i - 1] + uniq[i]))
    return None


def _eval_g5(spec: BenchSpec, robust_threshold: float = 0.5) -> Optional[G5Sensitivity]:
    """G5: evaluate the verdict over the load-bearing cube; compute in-window
    fraction + verdict-flip boundary (which neither observable leg provides)."""
    sens = spec.sensitivity
    if sens is None:
        if spec.is_physics_test:
            # a physics bankability candidate with no sensitivity sweep is a
            # single-point result -> books NEGATIVE per the discipline.
            return G5Sensitivity(
                status=GateStatus.FAIL,
                n_configs=0,
                n_in_window=0,
                in_window_fraction=0.0,
                tuned_point_only=True,
                verdict_flips_within_range=False,
                result_kind="no_sweep",
                per_param=(),
                convergence_sweep_present=False,
                magnitude_claim_blocked=spec.magnitude_is_claimed,
                analytic_exemption_granted=False,
                response_surface_ref="",
                note="no sensitivity sweep supplied — single-point result books NEGATIVE.",
            )
        return None  # validate-on-known pilot: G5 N/A

    names = sorted(sens.param_grids.keys())
    grids = [np.asarray(sens.param_grids[n], dtype=float) for n in names]
    configs = list(itertools.product(*grids))
    n = len(configs)
    obs = np.array([float(sens.observable_of(**dict(zip(names, cfg)))) for cfg in configs], dtype=float)
    verdicts = np.array([bool(sens.verdict_fn(o)) for o in obs], dtype=bool)
    n_in = int(verdicts.sum())
    frac = float(n_in / n) if n else 0.0
    tuned = bool(n_in <= 1 and n > 1)
    flips = bool(0 < n_in < n)

    cfg_arr = np.array(configs, dtype=float)
    per_param = tuple(
        ParamSweepResult(
            param_name=names[j],
            grid_min=float(grids[j].min()),
            grid_max=float(grids[j].max()),
            n_points=int(grids[j].size),
            flip_boundary=_flip_boundary(cfg_arr[:, j], verdicts),
            is_convergence_axis=(names[j] == sens.convergence_param),
        )
        for j in range(len(names))
    )

    conv_present = sens.convergence_param is not None
    # A magnitude claim must be backed by EITHER a convergence (grid/resolution)
    # sweep OR a positive analytic-provenance citation (a closed-form has no
    # discretization to converge). The analytic exemption is earned ONLY by a
    # non-numerical result that ALSO carries a non-empty analytic_provenance — a
    # bare result_is_numerical=False with no provenance is self-attestation and is
    # BLOCKED (the gate refuses to dodge convergence on the author's word alone).
    analytic_exemption = (not spec.result_is_numerical) and bool(spec.analytic_provenance.strip())
    mag_blocked = bool(spec.magnitude_is_claimed and not conv_present and not analytic_exemption)

    if n_in == 0:
        status = GateStatus.FAIL
        result_kind = "no_positive"
        note = "no in-window config anywhere in the swept space — books NEGATIVE."
    elif tuned:
        status = GateStatus.FAIL
        result_kind = "tuned_positive"
        note = "positive only at a single swept point — tuned/rescue-fill, books NEGATIVE."
    elif mag_blocked:
        status = GateStatus.FAIL
        result_kind = "robust_positive"
        note = (
            "magnitude claimed but neither a convergence (grid/resolution) sweep nor a "
            "positive analytic_provenance citation — BLOCKED (self-attestation insufficient)."
        )
    elif frac >= robust_threshold:
        status = GateStatus.PASS
        result_kind = "robust_positive"
        note = f"robust across the swept range (in-window fraction {frac:.2f} >= {robust_threshold})."
    else:
        status = GateStatus.PASS
        result_kind = "robust_positive"
        note = (
            f"positive over a sub-range (in-window fraction {frac:.2f}); flip boundary "
            "recorded — robust but bounded."
        )
    return G5Sensitivity(
        status=status,
        n_configs=n,
        n_in_window=n_in,
        in_window_fraction=frac,
        tuned_point_only=tuned,
        verdict_flips_within_range=flips,
        result_kind=result_kind,
        per_param=per_param,
        convergence_sweep_present=conv_present,
        magnitude_claim_blocked=mag_blocked,
        analytic_exemption_granted=analytic_exemption,
        response_surface_ref=sens.response_surface_ref,
        note=note,
    )


def _eval_g6(spec: BenchSpec) -> G6SymmetricStandard:
    """G6: peer-with-counterpart vs genuine AVE-only shortfall (symmetric standard)."""
    peer, shortfall = [], []
    for r in spec.ledger_rows:
        if r.sm_also:
            peer.append(r.aspect.value)
        elif r.status is not LedgerStatus.DERIVED:
            # AVE imports/fits this and the counterpart does NOT -> a real shortfall
            shortfall.append(r.aspect.value)
    note = (
        f"{len(peer)} peer row(s) (counterpart also imports/fits/asserts -> PEER, not "
        f"demote); {len(shortfall)} genuine AVE-only shortfall(s) STAND."
    )
    return G6SymmetricStandard(
        status=GateStatus.FRAMING_FLAG,
        peer_rows=tuple(peer),
        ave_only_shortfalls=tuple(shortfall),
        note=note,
    )


def _eval_g7(spec: BenchSpec) -> G7FrozenPrereg:
    """G7: frozen prereg before measurement, INCONCLUSIVE bin, dimensional eval."""
    p = spec.prereg
    dim_required = spec.magnitude_is_claimed
    dim_present = len(p.expected_magnitude_eval) > 0
    if not p.frozen:
        status, note = GateStatus.FAIL, "prereg not frozen before measurement."
    elif not p.has_inconclusive_bin:
        status, note = GateStatus.FAIL, "prereg lacks an explicit INCONCLUSIVE outcome bin."
    elif dim_required and not dim_present:
        status, note = (
            GateStatus.FAIL,
            "magnitude claimed but prereg carries no canonical-primitive dimensional eval (Step 3.5).",
        )
    else:
        status, note = GateStatus.PASS, "frozen; INCONCLUSIVE bin present; dimensional eval as required."
    return G7FrozenPrereg(
        status=status,
        prereg_ref=p.ref,
        frozen=p.frozen,
        has_inconclusive_bin=p.has_inconclusive_bin,
        dimensional_eval_present=dim_present,
        dimensional_eval_required=dim_required,
        note=note,
    )


def _eval_g8(spec: BenchSpec) -> G8EvidenceFraming:
    """G8: gating-vs-non-gating axis, binding-spec class, full sweep denominator."""
    e = spec.evidence_framing
    if not e.selection_from_pool_clean:
        status = GateStatus.FAIL
        note = (
            f"selection-from-pool: {e.n_displayed} displayed of {e.n_total_run} run, "
            "omitted instances not enumerated."
        )
    elif not e.gating_axis:
        status = GateStatus.FRAMING_FLAG
        note = "no explicit gating axis declared."
    else:
        status = GateStatus.PASS
        note = (
            f"gating axis explicit; binding-spec={e.binding_spec.value}; full denominator "
            f"{e.n_total_run} disclosed."
        )
    return G8EvidenceFraming(
        status=status,
        gating_axis=e.gating_axis,
        binding_spec=e.binding_spec,
        verifiability_class=e.verifiability_class,
        selection_from_pool_clean=e.selection_from_pool_clean,
        n_displayed=e.n_displayed,
        n_total_run=e.n_total_run,
        note=note,
    )


# ============================================================================
# VERDICT — Fork-2 graded ladder
# ============================================================================


def _decide_verdict(
    spec: BenchSpec,
    g1: G1ValidateOnKnown,
    g2: G2FormVsValue,
    g3: G3SMCoComputed,
    g4: G4Ledger,
    g5: Optional[G5Sensitivity],
    g6: G6SymmetricStandard,
    g7: G7FrozenPrereg,
    g8: G8EvidenceFraming,
) -> tuple[Verdict, str]:
    """Apply the Fork-2 graded ladder: G1-G5 hard-gating + G6-G8 framing."""
    # --- non-physics validate-on-known pilot (cRIO) ---
    if not spec.is_physics_test:
        if g1.status is GateStatus.PASS:
            return (
                Verdict.VALIDATE_ON_KNOWN_PASS,
                "validate-on-known positive control recovered through the identical "
                "chain; the lock-in/drift-rejection/floor-attribution chain is "
                "validated. NOT a physics test (bankability tiers N/A).",
            )
        return (
            Verdict.VALIDATE_ON_KNOWN_FAIL,
            f"validate-on-known positive control FAILED ({g1.comparison.summary()}); "
            "the chain is not yet trustworthy.",
        )

    # --- physics bankability candidate ---
    # Fork-3: a declared echo gating axis is refused outright.
    if g2.fork3_refused:
        return (Verdict.NOT_BANKABLE, "Fork-3 refusal — declared falsifiable axis is an echo (G2).")
    # hard gates G1, G3, G4, G5
    if g1.status is not GateStatus.PASS:
        return (Verdict.NOT_BANKABLE, f"G1 validate-on-known did not pass ({g1.status.value}).")
    if g3.status is not GateStatus.PASS:
        return (Verdict.NOT_BANKABLE, f"G3 discriminator non-discriminating ({g3.note}).")
    if g4.status is not GateStatus.PASS:
        return (Verdict.NOT_BANKABLE, f"G4 ledger gate failed ({g4.note}).")
    if g5 is None or g5.status is not GateStatus.PASS:
        reason = g5.note if g5 else "no sensitivity sweep."
        return (Verdict.NOT_BANKABLE, f"G5 sensitivity gate failed ({reason}).")

    # passed all hard gates -> at least BANKABLE_AS_DISCRIMINATOR.
    gating = spec.gating_axis
    framing_ok = g7.status is not GateStatus.FAIL and g8.status is not GateStatus.FAIL
    # an open sizing row = magnitude claimed but the magnitude/value is an echo or
    # the ledger magnitude row is not DERIVED.
    mag_row_derived = g4.magnitude_row_status is LedgerStatus.DERIVED
    open_sizing_row = spec.magnitude_is_claimed and (
        (gating is not None and gating.value_tag is ChordEcho.ECHO) or not mag_row_derived
    )
    unshared_or_slope = gating is not None and (
        gating.shared_with is SharedWith.NONE
        or (gating.discriminator_axis is DiscriminatorAxis.SLOPE and gating.calibration_free)
        or gating.discriminator_axis in (DiscriminatorAxis.ZERO_VS_NONZERO, DiscriminatorAxis.EXISTENCE)
    )
    fully_bankable = (
        gating is not None
        and gating.form_tag is ChordEcho.CHORD
        and unshared_or_slope
        and not open_sizing_row
        and framing_ok
    )
    if fully_bankable:
        return (
            Verdict.BANKABLE,
            "G1-G5 pass; forced-FORM chord on an UNSHARED/slope axis with no open "
            "sizing row; framing (G6-G8) clean. Fully bankable.",
        )
    caveats = []
    if open_sizing_row:
        caveats.append("open G4 sizing row (magnitude is a calibration echo)")
    if gating is not None and gating.shared_with is SharedWith.FORM:
        caveats.append("discriminator rides a FORM shared with the counterpart (rescued by a tree-vs-loop chord)")
    if not framing_ok:
        caveats.append("a G6-G8 framing gate flags")
    return (
        Verdict.BANKABLE_AS_DISCRIMINATOR,
        "G1-G5 pass as a discriminator; "
        + ("; ".join(caveats) if caveats else "first-cut absolute sizing open")
        + ". Bankable AS DISCRIMINATOR / first-cut absolute sizing (Fork-2 intermediate tier).",
    )


# ============================================================================
# THE SPINE — bench-spec -> bankability record
# ============================================================================


def run_bench_model(spec: BenchSpec, *, robust_threshold: float = 0.5) -> BankabilityRecord:
    """Compose the legs into the bankability record (the GAP-1 spine).

    Pipeline: G1 validate-on-known (ave.bench.validate) -> G3 AVE-vs-SM co-sweep
    (ave.bench.sweep, no-strawman) -> G5 sensitivity cube (in-window fraction +
    flip boundary, computed here) -> G2/G4/G6/G7/G8 declaration checks -> Fork-2
    graded-ladder verdict. Optionally reads an SNR window (ave.bench.snr).

    Parameters
    ----------
    spec : BenchSpec
        The bench declaration (channel-agnostic).
    robust_threshold : float
        In-window-fraction threshold separating a robust positive from a bounded
        one in G5 (default 0.5; the raw fraction is always recorded so the
        auditor can re-judge).
    """
    g1 = _eval_g1(spec)
    sweep = run_divergence_sweep(spec.ave_observable, spec.sm_observable, spec.sweep_grid)
    g2 = _eval_g2(spec)
    g3 = _eval_g3(spec, sweep)
    g4 = _eval_g4(spec)
    g5 = _eval_g5(spec, robust_threshold=robust_threshold)
    g6 = _eval_g6(spec)
    g7 = _eval_g7(spec)
    g8 = _eval_g8(spec)

    verdict, rationale = _decide_verdict(spec, g1, g2, g3, g4, g5, g6, g7, g8)

    t5: Optional[float] = None
    svf: Optional[float] = None
    if spec.snr_signal is not None and spec.snr_floor is not None:
        t5 = time_to_n_sigma(spec.snr_signal, spec.snr_floor, sigma_target=5.0)
        svf = signal_vs_floor(spec.snr_signal, spec.snr_floor)

    return BankabilityRecord(
        bench_name=spec.name,
        channel=spec.channel,
        is_physics_test=spec.is_physics_test,
        verdict=verdict,
        verdict_rationale=rationale,
        g1=g1,
        g2=g2,
        g3=g3,
        g4=g4,
        g5=g5,
        g6=g6,
        g7=g7,
        g8=g8,
        regime_note=spec.regime_note,
        snr_time_to_5sigma_s=t5,
        snr_signal_vs_floor=svf,
    )
