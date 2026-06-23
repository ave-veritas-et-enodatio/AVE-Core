"""ave.bench — shared build-once-reuse bench infrastructure.

Every AVE bench repo (AVE-Bench-VacuumMirror, the cRIO EE bench, a future
laser-facility-birefringence repo, plus the AVE-Core vol_4 engineering drivers)
re-implements the same four load-bearing patterns by hand. Today the
VacuumMirror Born engine is copy-pasted across ~6 scripts and the FN/Paschen
breakdown ceilings are duplicated across qg42 + experimental_noise_floor. This
package factors those four patterns into ONE importable source so every driver
draws from the same contract.

Each module is FACTORED from a named, proven exemplar (a contract lifted, not
invented). The exemplars and the factoring discipline:

  sweep.py     — co-vary AVE-vs-SM/null divergence sweep.
                 FACTORED FROM AVE-Bench-VacuumMirror/scripts/
                 analytical_gamma_v_sweep.py (gamma_bragg_2d vs gamma_sm_eh_kerr
                 co-vary block). LOAD-BEARING INVARIANT (the no-strawman rule):
                 the SM/null callable is evaluated over the SAME x_grid and
                 through the same integral/profile as the AVE callable. There is
                 NO API path to pass a pre-baked independent SM curve.

  apparatus.py — geometry -> per-node saturation amplitude A_0, with a
                 Fowler-Nordheim field-emission breakdown CEILING.
                 FACTORED FROM AVE-Core src/scripts/vol_4_engineering/
                 qg42_vsign_deltaf.py (a_rms_local / G_geom = beta*Q_build block
                 + the FN-safe ceiling) cross-checked against
                 src/scripts/peer_review/experimental_noise_floor.py
                 (fowler_nordheim_current).

  snr.py       — shot-noise-limited SNR surface + time-to-Nsigma + signal-vs-floor.
                 FACTORED FROM AVE-Bench-VacuumMirror/scripts/apd_snr_sweep.py
                 (snr_direct + t_detection block) and AVE-Core
                 src/scripts/peer_review/experimental_noise_floor.py
                 (the breakdown-envelope floors).

  validate.py  — recover-a-known assertion gate (matches a computed value to a
                 labeled PDG/CODATA/known reference within tolerance).
                 FACTORED FROM the AVE-Core src/scripts/verify/*_anchor.py +
                 *_results.json pattern (muon_g2_fermilab_anchor,
                 baryon_ladder_pdg_2024_anchor): the deviation / deviation_pct /
                 n_sigma / PASS-or-FLAG verdict contract.

  birefringence.py — vacuum-birefringence bench physics: AVE retardance
                 (sqrt-S Axiom-4 index shift, E^2-leading), AVE parity-odd
                 optical-activity ROTATION (the clean zero-vs-nonzero QED
                 discriminator in FORM; the chiral-srs +-75.462 deg/unit magnitude
                 is an ETA_ROT_PER_WRITHE engineering decree, NOT a bankable
                 transport), and the QED Euler-Heisenberg
                 baseline (with the PVLAS A_e ~ 1.32e-24 T^-2 validate-on-known
                 anchor). FORWARD from ave.core.constants; the QED prefactor band
                 + PVLAS A_e are labeled non-AVE literature inputs. Grounded in
                 vacuum-birefringence-e4.md (clm-pp3qwf) + engine-capability-map.md
                 (#195 optical-activity) + the corrected coefficient-discriminator
                 driver birefringence_coefficient_discriminator.py.

DISCIPLINE: all physical constants are imported from ave.core.constants. There
are ZERO hardcoded SI literals in this package (the FN empirical coefficients
A_FN/B_FN/PHI_W are labeled experimental-input constants, lifted verbatim from
the canonical experimental chapter via the exemplars, NOT AVE-derived physics).
"""

from __future__ import annotations

from ave.bench.adopters import (
    birefringence_bench_spec,
    crio_validate_on_known_spec,
)
from ave.bench.apparatus import (
    ApparatusCoupling,
    fn_dark_current,
    fn_safe_max_amplitude,
    saturation_amplitude,
    v_yield_apparatus,
)
from ave.bench.birefringence import (
    A_EH_LITERATURE,
    BirefringencePoint,
    bench_point,
    coefficient_ratio,
    coefficient_ratio_differential,
    delta_n_ave_differential,
    delta_n_ave_differential_exact,
    delta_n_ave_exact,
    delta_n_ave_leading,
    delta_n_qed,
    delta_n_qed_magnetic,
    optical_activity_rate_deg_per_m,
    optical_activity_rotation_deg,
    optical_activity_rotation_qed,
    substrate_identity_holds,
    vacuum_magnetic_birefringence_constant,
)
from ave.bench.model import (
    AxisTag,
    BankabilityRecord,
    BenchSpec,
    BindingSpec,
    ChordEcho,
    CorpusState,
    DimensionalIngredient,
    DiscriminatorAxis,
    EvidenceFraming,
    GateStatus,
    LedgerAspect,
    LedgerRow,
    LedgerStatus,
    OutcomeKind,
    Prereg,
    SensitivitySpec,
    SharedWith,
    ValidateOnKnownSpec,
    Verdict,
    VerifiabilityClass,
    run_bench_model,
)
from ave.bench.snr import (
    SNRPoint,
    signal_vs_floor,
    snr_shot_noise,
    time_to_n_sigma,
)
from ave.bench.sweep import DivergenceSweepResult, run_divergence_sweep
from ave.bench.validate import KnownComparison, assert_recovers_known

__all__ = [
    # sweep
    "run_divergence_sweep",
    "DivergenceSweepResult",
    # apparatus
    "ApparatusCoupling",
    "saturation_amplitude",
    "v_yield_apparatus",
    "fn_dark_current",
    "fn_safe_max_amplitude",
    # snr
    "snr_shot_noise",
    "time_to_n_sigma",
    "signal_vs_floor",
    "SNRPoint",
    # validate
    "assert_recovers_known",
    "KnownComparison",
    # birefringence
    "delta_n_ave_exact",
    "delta_n_ave_leading",
    "delta_n_ave_differential",
    "delta_n_ave_differential_exact",
    "delta_n_qed",
    "delta_n_qed_magnetic",
    "vacuum_magnetic_birefringence_constant",
    "optical_activity_rate_deg_per_m",
    "optical_activity_rotation_deg",
    "optical_activity_rotation_qed",
    "coefficient_ratio",
    "coefficient_ratio_differential",
    "substrate_identity_holds",
    "bench_point",
    "BirefringencePoint",
    "A_EH_LITERATURE",
    # model — the channel-agnostic BenchModel spine + 8-gate bankability record
    "run_bench_model",
    "BenchSpec",
    "BankabilityRecord",
    "Verdict",
    "GateStatus",
    "ChordEcho",
    "DiscriminatorAxis",
    "SharedWith",
    "LedgerRow",
    "LedgerStatus",
    "LedgerAspect",
    "AxisTag",
    "Prereg",
    "DimensionalIngredient",
    "CorpusState",
    "OutcomeKind",
    "ValidateOnKnownSpec",
    "EvidenceFraming",
    "BindingSpec",
    "VerifiabilityClass",
    "SensitivitySpec",
    # adopters — reference BenchSpec builders (prove the spine shape)
    "birefringence_bench_spec",
    "crio_validate_on_known_spec",
]
