"""adopters.py — reference BenchSpec adopters for the BenchModel spine (GAP-1).

Two reference adopters prove the channel-agnostic spine shape against real
charter targets, by composing the spine (``ave.bench.model``) with channel
physics. They are the in-package analog of a satellite bench repo's driver
(AVE-Bench-Birefringence is the canonical out-of-repo example): a thin layer
that imports the contracts + the channel physics layer, declares the 8-gate
inputs, and hands a BenchSpec to ``run_bench_model``.

  1. ``birefringence_bench_spec()`` — the EM-photon vacuum-birefringence
     coefficient bench. Imports the canonical physics layer
     (``ave.bench.birefringence``) rather than re-deriving it, and headlines the
     MATCHED par-perp DIFFERENTIAL ratio 7.5/alpha^3 ~ 1.93e7 (NOT the demoted
     single-arm 4.14e6; FLAG-A 2026-06-21). Expected verdict:
     BANKABLE_AS_DISCRIMINATOR — a forced-given-alpha quantitative ratio + a
     tree-vs-loop FORM chord whose MAGNITUDE is a symmetric alpha-echo (the
     charter's intermediate Fork-2 tier; the 7.5-trace a94672de resolved input b).

  2. ``crio_validate_on_known_spec()`` — the cRIO C_eff(V) VALIDATE-ON-KNOWN
     pilot. NOT a physics test: the vacuum kernel is unreachable by ~18-24 OOM on
     a 10 V instrument (deep Regime I, per-node A0 ~ 1e-11). Its job is to learn
     the lock-in / drift-rejection / floor-attribution chain on a KNOWN nonlinear
     cap. Expected verdict: VALIDATE_ON_KNOWN_PASS. The G1 recovery numbers are
     MODELED representative datasheet values labeled as such — the real recovery
     happens at the bench; this spec encodes the chain logic and routes it to the
     validate-on-known tier. Its G3 honestly reports NON-discriminating (shared
     saturating FORM, GAP-6) and its G7 honestly reports the prereg is a DRAFT,
     not frozen — neither gates the pilot verdict, but both are recorded.

CITE-DON'T-DUPLICATE: canonical provenance is referenced by file:line; no physics
is copied. All AVE constants import from ave.core.constants; the QED prefactors
and the cRIO datasheet/charge-injection numbers are LABELED non-AVE inputs.
"""

from __future__ import annotations

import numpy as np

from ave.bench.birefringence import (
    delta_n_ave_differential,
    delta_n_qed,
    vacuum_magnetic_birefringence_constant,
)
from ave.bench.model import (
    AxisTag,
    BenchSpec,
    BindingSpec,
    ChordEcho,
    CorpusState,
    DimensionalIngredient,
    DiscriminatorAxis,
    EvidenceFraming,
    InterpretiveAlternative,
    LedgerAspect,
    LedgerRow,
    LedgerStatus,
    OutcomeKind,
    Prereg,
    SensitivitySpec,
    SharedWith,
    ValidateOnKnownSpec,
    VerifiabilityClass,
    run_bench_model,
)
from ave.core.constants import ALPHA, E_CRIT, E_YIELD

IA = InterpretiveAlternative

# QED matched par-perp differential coefficient (Euler-Heisenberg 7/45 parallel −
# 4/45 perp = 3/45). LABELED non-AVE literature input.
_A_EH_DIFFERENTIAL: float = 3.0 / 45.0

# Facility-class probe-field grid [V/m] — an ENGINEERING input (E-route / HIBEF
# class), well below E_YIELD ~ 1.13e17 so A = E/E_YIELD < 1. The differential
# ratio is field-INDEPENDENT, so the grid choice does not move the discriminator;
# it exists to DEMONSTRATE that field-independence across the reachable range.
_FACILITY_E_GRID = np.array([1e13, 1e14, 1e15, 1e16, 3e16])


def birefringence_bench_spec() -> BenchSpec:
    """The EM-photon vacuum-birefringence coefficient bench as a BenchSpec.

    Composes the canonical ``ave.bench.birefringence`` callables. The
    discriminator is the field-INDEPENDENT matched par-perp differential ratio
    delta_n_AVE / delta_n_QED = 7.5 / alpha^3 ~ 1.93e7 — a forced-given-alpha
    quantitative ratio (the 7.5 = lattice-1/2 / textbook-3/45 is FORCED; the
    alpha^-3 = alpha^-2 tree-vs-loop x alpha^-1 E_yield import) riding the
    substrate identity (E_CRIT/E_YIELD)^2 = 1/alpha. The FORM (tree-O(1)/2
    saturation vs QED alpha^2 loop) is the AVE-distinct chord; the MAGNITUDE is a
    symmetric alpha-echo (alpha imported on both sides) -> BANKABLE_AS_DISCRIMINATOR.
    """

    def ave_obs(E: float) -> float:
        # the par-perp birefringence falsifier observable, positive magnitude for
        # the divergence ratio (birefringence.py:215, delta_n_bir ~ -1/2 A^2).
        return float(abs(delta_n_ave_differential(E)))

    def sm_obs(E: float) -> float:
        # QED matched differential, driven over the SAME grid (no-strawman).
        return float(delta_n_qed(E, a_eh=_A_EH_DIFFERENTIAL))

    def ratio_at(E_field: float) -> float:
        # the physical field-independent discriminator ratio at a probe field.
        return ave_obs(E_field) / sm_obs(E_field)

    return BenchSpec(
        name="vacuum-birefringence-coefficient",
        channel="EM-photon (transverse retardance)",
        ave_observable=ave_obs,
        sm_observable=sm_obs,
        sweep_grid=_FACILITY_E_GRID,
        validate_on_known=ValidateOnKnownSpec(
            reference_label="PVLAS vacuum magnetic birefringence A_e [T^-2]",
            computed=vacuum_magnetic_birefringence_constant(),
            reference=1.32e-24,  # PVLAS/Rizzo textbook value (LABELED literature)
            tol=0.01,
            inconclusive_bin="recovery within 1% is required; a miss HALTS (model wrong)",
            through_identical_chain=True,
        ),
        ledger_rows=(
            LedgerRow(
                LedgerAspect.COUPLING,
                LedgerStatus.DERIVED,
                "A = E/E_YIELD (Axiom-4 per-node amplitude); E_YIELD constants.py:471",
                sm_also=True,  # QED equally keys on E/E_CRIT
            ),
            LedgerRow(
                LedgerAspect.PROBE,
                LedgerStatus.ENGINEERING_CHOICE,
                "polarimeter measures n_par - n_perp; field->cavity-phase->ellipticity "
                "coupling is FIRST-CUT (OQ-1, open derivation in AVE-Bench-Birefringence)",
                sm_also=True,
            ),
            LedgerRow(
                LedgerAspect.MAGNITUDE,
                LedgerStatus.ENGINEERING_CHOICE,
                "7.5/alpha^3 ~ 1.93e7 is a symmetric alpha-ECHO (alpha imported both "
                "sides); 7.5-trace a94672de; NOT an emergent number",
                sm_also=True,  # QED's coefficient is equally alpha-rooted (symmetric standard)
            ),
            LedgerRow(
                LedgerAspect.OBSERVABLE,
                LedgerStatus.DERIVED,
                "delta_n_bir = n_par - n_perp ~ -1/2 A^2 (birefringence.py:215; "
                "vacuum-birefringence-e4.md clm-pp3qwf)",
                sm_also=False,  # the E^2-leading FORM is shared, but the tree-vs-loop structure is AVE-only
            ),
        ),
        axis_tags=(
            AxisTag(
                name="par-perp coefficient ratio (7.5/alpha^3)",
                form_tag=ChordEcho.CHORD,  # tree-vs-loop FORM is forced
                value_tag=ChordEcho.ECHO,  # the magnitude is an alpha-echo
                discriminator_axis=DiscriminatorAxis.RATIO,
                shared_with=SharedWith.FORM,  # both AVE and QED are E^2-leading
                is_gating_axis=True,
                calibration_free=False,
                interpretive_alternatives=(
                    IA.APPROX_WITH_RESIDUAL,
                    IA.COINCIDENCE,
                    IA.STRATIFICATION,
                ),
                rationale="shared E^2-leading FORM; the discriminator is the coefficient ratio, "
                "rescued from non-discriminating by the tree-vs-loop FORM-within-form chord",
            ),
            AxisTag(
                name="tree-vs-loop structure (O(1)/2 saturation vs alpha^2 loop)",
                form_tag=ChordEcho.CHORD,
                value_tag=ChordEcho.CHORD,
                discriminator_axis=DiscriminatorAxis.SLOPE,  # the alpha-power structure
                shared_with=SharedWith.NONE,  # QED has no tree saturation term
                is_gating_axis=False,
                calibration_free=True,
                rationale="the independent structural FORM chord: AVE has a tree-level saturation "
                "the QED one-loop counterpart structurally lacks",
            ),
        ),
        prereg=Prereg(
            ref="research/2026-06-04_birefringence-coefficient-prereg.md (+ 7.5-trace a94672de)",
            frozen=True,
            corpus_state=CorpusState.PARTIAL,
            prior_work_refs=(
                "vacuum-birefringence-e4.md clm-pp3qwf",
                "birefringence.py:328 coefficient_ratio_differential",
            ),
            prediction="AVE sits ~10^7x QED (field-independent) on the matched par-perp "
            "differential, via a tree-level saturation the one-loop QED form lacks",
            rationale="tree-O(1)/2 saturation vs alpha^2 loop suppression; ratio rides " "(E_CRIT/E_YIELD)^2 = 1/alpha",
            discriminating_outcomes=(
                (OutcomeKind.POSITIVE, "ratio ~1.93e7, field-independent -> AVE-distinct tree-vs-loop"),
                (OutcomeKind.NEGATIVE, "ratio ~1 (alpha^2-suppressed) -> AVE form falsified"),
                (OutcomeKind.INCONCLUSIVE, "below facility floor / OQ-1 ellipticity model unresolved"),
            ),
            falsifier="a measured retardance consistent with the QED alpha^2 coefficient",
            expected_magnitude_eval=(
                DimensionalIngredient("alpha", ALPHA, "constants.py:154"),
                DimensionalIngredient("E_CRIT", E_CRIT, "constants.py:465"),
                DimensionalIngredient("E_YIELD", E_YIELD, "constants.py:471"),
            ),
        ),
        evidence_framing=EvidenceFraming(
            gating_axis="par-perp coefficient ratio (7.5/alpha^3)",
            non_gating_axes=("optical-activity rotation (separate channel)", "absolute delta_n magnitude"),
            binding_spec=BindingSpec.SINGLE_SHOT,  # the coefficient ratio is a directly-computed number
            verifiability_class=VerifiabilityClass.A_DIRECT,
            verification_artifact_ref="coefficient_ratio_differential() closed form == sweep ratio[0]",
            n_displayed=len(_FACILITY_E_GRID),
            n_total_run=len(_FACILITY_E_GRID),  # full grid reported; no selection-from-pool
        ),
        sensitivity=SensitivitySpec(
            observable_of=ratio_at,
            param_grids={"E_field": tuple(float(e) for e in _FACILITY_E_GRID)},
            verdict_fn=lambda r: r > 1e6,  # discriminator stays orders above the QED floor
            convergence_param=None,  # analytic closed form — no discretization to converge
            response_surface_ref="(field-independence is the response surface: ratio flat in E)",
        ),
        is_physics_test=True,
        magnitude_is_claimed=True,  # the 7.5/alpha^3 ratio is a quantitative claim
        result_is_numerical=False,  # closed-form analytic -> no convergence sweep required
        regime_note="weak-field probe (A = E/E_YIELD << 1); facility-gated (E-route/HIBEF); "
        "PVLAS resolved (static-B delta_n == 0 exactly)",
        snr_signal=None,
        snr_floor=None,
    )


def crio_validate_on_known_spec() -> BenchSpec:
    """The cRIO C_eff(V) VALIDATE-ON-KNOWN pilot as a BenchSpec (NOT a physics test).

    Routes to VALIDATE_ON_KNOWN_PASS by recovering a KNOWN nonlinear-cap datasheet
    point through the lock-in / drift-rejection / floor-attribution chain. The
    recovery numbers are MODELED representative datasheet values (X7R derating);
    the real recovery happens on hardware. The AVE-vs-SM co-sweep is illustrative
    only (a pilot does not gate on G3); G3 honestly reports the material analog is
    NON-discriminating (shared saturating FORM, GAP-6 sign tension). The prereg is
    a DRAFT (not frozen) -> G7 honestly FAILs; neither gates the pilot verdict.
    """

    # Illustrative normalized small-signal C(V)/C0 curves over a bias grid. For a
    # pilot these are NOT the gating step (the chain validation is). A standard
    # Class-2 X7R derating FALLS; the AVE small-signal differential-permittivity
    # form also FALLS (Branch-F), so they share the saturating FORM (GAP-6).
    bias = np.linspace(0.0, 0.9, 6)  # V/V_local (dimensionless), ENGINEERING grid

    def falling(x: float) -> float:
        # representative falling saturating curve (both AVE-F and standard fall)
        return float(np.sqrt(max(1.0 - x**2, 0.0)))

    return BenchSpec(
        name="cRIO-Ceff-V-validate-on-known-pilot",
        channel="EE-capacitance (small-signal C_eff(V), material analog)",
        ave_observable=falling,
        sm_observable=falling,  # illustrative; co-sweep is non-gating for a pilot
        sweep_grid=bias,
        validate_on_known=ValidateOnKnownSpec(
            reference_label="X7R/X5R Class-2 MLCC datasheet DC-bias derating (modeled recovery)",
            computed=0.52,  # MODELED recovered C/C0 at rated bias (illustrative)
            reference=0.50,  # representative datasheet derating point
            tol=0.20,  # X7R datasheet tolerance band (10-20%)
            inconclusive_bin="any C(V) feature within ~3x the Stage-C drift floor -> UNRESOLVED "
            "(BIN1); a known cap not recovered -> dead-instrument (Outcome D)",
            through_identical_chain=True,  # Stage A flat-cap -> Stage B datasheet -> Stage C drift floor
        ),
        ledger_rows=(
            LedgerRow(
                LedgerAspect.COUPLING,
                LedgerStatus.ENGINEERING_CHOICE,
                "lock-in quadrature C_eff = I_Q/(omega v_ac); ratiometric DUT/ref drift cancel",
                sm_also=True,
            ),
            LedgerRow(
                LedgerAspect.PROBE,
                LedgerStatus.ENGINEERING_CHOICE,
                "small-signal AC probe v_ac (linearity-gated over a decade); 4x4 NI-9263/9215",
                sm_also=True,
            ),
            LedgerRow(
                LedgerAspect.MAGNITUDE,
                LedgerStatus.ENGINEERING_CHOICE,
                "V_local is a FIT parameter for the material analog (consistency-class C); "
                "the vacuum scale is unreachable by ~18-24 OOM",
                sm_also=True,
            ),
            LedgerRow(
                LedgerAspect.OBSERVABLE,
                LedgerStatus.DERIVED,
                "saturating quarter-arc FORM S = sqrt(1-x^2) (Axiom-4; bench measures the "
                "Branch-F small-signal differential permittivity, INVARIANT-S2 sector split)",
                sm_also=True,  # standard saturating caps share the FORM -> shape-degenerate (GAP-6)
            ),
        ),
        axis_tags=(
            AxisTag(
                name="dC/dV sign (Branch-R rising vs Branch-F falling)",
                form_tag=ChordEcho.MIXED,  # GAP-6: sign un-adjudicated in the draft prereg
                value_tag=ChordEcho.ECHO,
                discriminator_axis=DiscriminatorAxis.MAGNITUDE,
                shared_with=SharedWith.FORM,  # shared saturating FORM with standard caps
                is_gating_axis=True,
                calibration_free=False,
                interpretive_alternatives=(IA.FLOOR, IA.COINCIDENCE, IA.STRATIFICATION),
                rationale="material analog shares the saturating FORM (shape-degenerate); GAP-6 "
                "sign tension blocks bin-pinning (but not this validate-on-known pilot)",
            ),
        ),
        prereg=Prereg(
            ref="research/2026-06-10_crio-ceff-saturation-onset_prereg-draft.md",
            frozen=False,  # DRAFT-FOR-GRANT-REVIEW, blocked on GAP-6 -> G7 honestly FAILs
            corpus_state=CorpusState.OPEN,
            prior_work_refs=(
                "cleave-01-requirements-boundary-conditions.md:42,157",
                "nonlinear-vacuum-capacitance.md:21 (Branch R)",
                "2026-06-03_yield-knee-map-prereg.md (Branch F)",
            ),
            prediction="the lock-in/drift/floor chain recovers a known nonlinear cap's "
            "datasheet C(V) before any DUT read is trusted",
            rationale="validate-on-known positive control on the instrument chain, not AVE physics",
            discriminating_outcomes=(
                (OutcomeKind.POSITIVE, "BIN2/3 AVE-FORM vs STANDARD-FORM decidable (needs x>=0.5 @ <0.1%)"),
                (OutcomeKind.NEGATIVE, "datasheet not recovered -> dead instrument (Outcome D)"),
                (OutcomeKind.INCONCLUSIVE, "BIN1 unresolved (within 3x drift floor) / BIN4 shape-degenerate"),
            ),
            falsifier="(material-analog) recovered C(V) inconsistent with the datasheet",
        ),
        evidence_framing=EvidenceFraming(
            gating_axis="known-cap datasheet recovery (chain validation)",
            non_gating_axes=("AVE-FORM vs STANDARD-FORM bin (blocked by GAP-6)",),
            binding_spec=BindingSpec.LEVEL_STABILITY_DRIFT,  # drift-floor-bound C(V)
            verifiability_class=VerifiabilityClass.B_CATEGORICAL,
            verification_artifact_ref="Stage-A flat-cap floor + Stage-B datasheet recovery + Stage-C Allan drift",
            n_displayed=len(bias),
            n_total_run=len(bias),
        ),
        sensitivity=None,  # validate-on-known pilot: bankability sensitivity N/A
        is_physics_test=False,
        magnitude_is_claimed=False,
        regime_note="deep Regime I, per-node A0 ~ 1e-11; vacuum kernel unreachable by ~18-24 OOM "
        "-> validate-on-known positive control, NOT a physics test. GAP-6 Branch-R/F sign "
        "tension open (candidate resolution: INVARIANT-S2 sector split, 2026-06-15).",
        snr_signal=None,
        snr_floor=None,
    )


def _main() -> dict:
    """Build both reference records and return a flat headline dict (CI contract)."""
    bire = run_bench_model(birefringence_bench_spec())
    crio = run_bench_model(crio_validate_on_known_spec())
    print(bire.summary())
    print()
    print(crio.summary())
    return {
        "birefringence_verdict": bire.verdict.value,
        "birefringence_ratio": bire.g3.ratio_value,
        "birefringence_field_independent": bire.g3.field_independent,
        "crio_verdict": crio.verdict.value,
        "crio_g1_passed": crio.g1.comparison.passed,
    }


if __name__ == "__main__":  # pragma: no cover
    _main()
