"""THE N-P MASS-SPLIT GATE: does the same frozen chain produce the n-p split, sign included?

FROZEN prereg (gated on): research/2026-07-13_np-mass-split-gate_prereg.md
(freeze commit pushed BEFORE this file -- git ordering = freeze proof).

THE GATE (one sentence). Same frozen chain, same delta_th, NO refit: does the corpus's
CANONICAL neutron construction (n = 6_2^3 cup 0_1) produce the n-p mass split +1.293 MeV
(+2.531 m_e), SIGN INCLUDED (neutron heavier)? A coincidence-tuned delta_th has no reason to
survive a DIFFERENCE measurement where the bulk proton mass cancels and only chain structure
remains -- the discriminating second shot on the m_p/m_e claim.

MODE: derivation-from-canon + NO-REFIT arithmetic consistency driver. NOT engine-fire. NO new
primitive. The instrument re-derives the EXISTING proton eigenvalue chain from live constants,
and asks whether the EXISTING neutron construction defines a computable mass split at all.

SECTOR: A1 (dilatation/mass) is what this measures. The split is a rest-energy A1 question
(rest mass + elastic strain), NOT a charge-sector question. Charge = Cosserat (2,3) winding,
untouched. A1 _|_ charge.

HARD RAILS (from the prereg, binding):
  1. No new parameters minted.
  2. No refit -- every consumed constant is imported LIVE from ave.core.constants and reproduced
     from its own definition; the exempt regression test (test_np_mass_split_gate.py) holds the
     frozen HEAD literals and asserts live == frozen (the prereg-vs-HEAD no-refit assertion).
  3. If the computation needs ANY non-canonical choice -> STOP at bin (iv), ENUMERATE, do NOT make it.
  4. Never seed from the answer (proton ratio / 1.293 MeV / 2.531 m_e / neutron mass) inside the
     derivation. The forbidden-seed set is DERIVED from the canonical CODATA anchors (never a
     hard-coded magic float), so it auto-tracks the anchors.

SUBSTRATE-NATIVE: zero hard-coded physics numbers in this driver. Every quantity is imported from
ave.core.constants or derived from it; the EFT magic-number gate (verify_universe.py) passes.

Legs:
  A  no_refit_audit         -- reproduce PROTON_ELECTRON_RATIO live from I_scalar/(1 - V*p_c) + 1
                               and diff a source's consumed constants against a reference. The
                               positive control that CAN fail: a refit-plant trips the abort.
  B  sign_leg               -- both named neutron contributions (rest mass, elastic strain) are
                               positive-definite (rest mass >= 0; Ax1 forbids ring shrink ->
                               strain >= 0) -> sign(Delta m) = + . delta_th-free, alpha-free.
  C  magnitude_computability-- enumerate every frozen-chain quantity that maps to a split
                               component; the only one available is the threaded electron rest
                               mass (+1.000 m_e, Reading X) or nothing (Reading Y); the elastic-
                               expansion tension has NO frozen-chain value. -> bin (iv) unless a
                               frozen-chain magnitude path exists.
"""

from __future__ import annotations

import json
import math
from dataclasses import dataclass, field
from pathlib import Path

from ave.core import constants

# Independent frozen HEAD reference (constants.py @ 9bfc50ef), stored as a NON-.py sidecar so it
# (a) is exempt from the EFT magic-number gate (which scans *.py only) yet (b) is an operative,
# not self-snapshot, no-refit anchor in the driver's live path: once committed it does NOT track a
# future source-level refit of constants.py, so run_gate()'s own audit trips on drift of ANY
# consumed constant -- including KAPPA_FS_COLD and DELTA_THERMAL (the audit's focal constant),
# which the old self-snapshot default could not catch.
_FROZEN_HEAD_PATH = Path(__file__).with_name("np_mass_split_gate_frozen_head.json")

# The names the frozen chain consumes (hard rail 2). Values are pulled LIVE -- no literals here.
CONSUMED_CONSTANTS: tuple[str, ...] = (
    "I_SCALAR_1D",
    "V_TOROIDAL_HALO",
    "ALPHA",
    "KAPPA_FS_COLD",
    "DELTA_THERMAL",
    "PROTON_ELECTRON_RATIO",
)

RTOL = 1e-12  # matches tests/test_constants_literals.py -- literal<->live pin


def _me_c2_mev(source: object = constants) -> float:
    """Electron rest energy in MeV, from the module's SI anchors (not a hard-coded value)."""
    return float(source.M_E) * float(source.C_0) ** 2 / float(source.e_charge) * 1e-6


def frozen_head_reference() -> dict[str, float]:
    """The INDEPENDENT frozen HEAD literal table (the operative no-refit anchor, hard rail 2).

    Loaded from the committed JSON sidecar -- a fixed copy of constants.py @ 9bfc50ef that does
    NOT move when the live module is refit, so diffing the live module against it catches a
    source-level refit of ANY consumed constant (incl. KAPPA_FS_COLD / DELTA_THERMAL).
    """
    raw = json.loads(_FROZEN_HEAD_PATH.read_text())
    return {k: float(v) for k, v in raw.items() if not k.startswith("_")}


def reference_from_constants(source: object = constants) -> dict[str, float]:
    """A snapshot of the consumed constants from the live module (a WEAK reference; kept for tests).

    NOTE: this is self-referential on the live path (live == live), so it is NOT used as the
    run_gate() default anymore -- frozen_head_reference() is. Retained so a caller can explicitly
    request a snapshot comparison.
    """
    return {name: float(getattr(source, name)) for name in CONSUMED_CONSTANTS}


def forbidden_seeds(source: object = constants) -> tuple[float, ...]:
    """The forbidden derivation seeds (hard rail 4), DERIVED from canonical anchors.

    No hard-coded magic float appears; the seeds auto-track the module's CODATA anchors.
    """
    me = _me_c2_mev(source)
    split_mev = float(source.M_N_MEV_TARGET) - float(source.M_P_MEV_CODATA)  # ~1.293 MeV
    return (
        float(source.PROTON_ELECTRON_RATIO),                       # AVE proton ratio ~1836.117
        float(source.M_P_MEV_CODATA) / me,                         # CODATA proton ratio ~1836.15
        split_mev,                                                 # split ~1.293 MeV
        split_mev / me,                                            # split ~2.531 m_e
        float(source.M_N_MEV_TARGET),                              # neutron mass ~939.565 MeV
    )


# ===========================================================================
# LEG A -- no-refit audit (the gate that fires on a refit plant)
# ===========================================================================
@dataclass
class NoRefitResult:
    ok: bool
    mismatches: list[tuple[str, float, float]] = field(default_factory=list)
    proton_ratio_live: float = 0.0
    proton_ratio_reproduced: float = 0.0


def no_refit_audit(source: object = constants, reference: dict[str, float] | None = None) -> NoRefitResult:
    """Diff a source's consumed constants against a reference and reproduce the proton ratio.

    `source` defaults to the live `ave.core.constants` module; a test may pass a stand-in with a
    mutated attribute (a refit plant) to prove the audit trips. `reference` defaults to the
    INDEPENDENT frozen HEAD table (JSON sidecar) -- so a source-level refit of ANY consumed
    constant, including KAPPA_FS_COLD / DELTA_THERMAL (which do not feed the reproduction identity),
    is caught on the driver's own live path, per prereg hard rail 2.
    """
    if reference is None:
        reference = frozen_head_reference()

    mismatches: list[tuple[str, float, float]] = []
    for name in CONSUMED_CONSTANTS:
        live = float(getattr(source, name))
        ref = reference[name]
        if not math.isclose(live, ref, rel_tol=RTOL, abs_tol=0.0):
            mismatches.append((name, ref, live))

    # P_C consistency: the module literal must equal 8*pi*ALPHA at the audited ALPHA.
    alpha_live = float(getattr(source, "ALPHA"))
    p_c_live = float(getattr(source, "P_C"))
    if not math.isclose(p_c_live, 8.0 * math.pi * alpha_live, rel_tol=RTOL, abs_tol=0.0):
        mismatches.append(("P_C", 8.0 * math.pi * alpha_live, p_c_live))

    # KAPPA_FS consistency: the delta_th-softened coupling that the FS solver consumes must equal
    # KAPPA_FS_COLD*(1-DELTA_THERMAL) AND the frozen HEAD value (catches a source-level DELTA_THERMAL
    # or KAPPA_FS_COLD refit -- the audit's focal constant, vacuous under the old self-snapshot).
    kfs_cold = float(getattr(source, "KAPPA_FS_COLD"))
    dth = float(getattr(source, "DELTA_THERMAL"))
    kfs_live = float(getattr(source, "KAPPA_FS"))
    if not math.isclose(kfs_live, kfs_cold * (1.0 - dth), rel_tol=RTOL, abs_tol=0.0):
        mismatches.append(("KAPPA_FS(consistency)", kfs_cold * (1.0 - dth), kfs_live))
    if "KAPPA_FS" in reference and not math.isclose(kfs_live, reference["KAPPA_FS"], rel_tol=RTOL, abs_tol=0.0):
        mismatches.append(("KAPPA_FS", reference["KAPPA_FS"], kfs_live))

    # Reproduce the proton eigenvalue live from the audited pieces (constants.py:955-956).
    i_scalar = float(getattr(source, "I_SCALAR_1D"))
    v_total = float(getattr(source, "V_TOROIDAL_HALO"))
    x_core = i_scalar / (1.0 - v_total * p_c_live)
    reproduced = x_core + 1.0
    ratio_live = float(getattr(source, "PROTON_ELECTRON_RATIO"))
    if not math.isclose(reproduced, ratio_live, rel_tol=RTOL, abs_tol=0.0):
        mismatches.append(("PROTON_ELECTRON_RATIO(reproduce)", ratio_live, reproduced))

    return NoRefitResult(
        ok=(len(mismatches) == 0),
        mismatches=mismatches,
        proton_ratio_live=ratio_live,
        proton_ratio_reproduced=reproduced,
    )


def assert_no_seed(value: float, label: str, source: object = constants) -> float:
    """Hard rail 4: refuse any derivation input that equals a forbidden (answer-derived) seed."""
    for seed in forbidden_seeds(source):
        if math.isclose(value, seed, rel_tol=1e-6, abs_tol=1e-6):
            raise ValueError(
                f"SEED VIOLATION: derivation input {label}={value!r} matches forbidden target "
                f"seed {seed!r}. The gate must not read the answer as an input (hard rail 4)."
            )
    return value


# ===========================================================================
# LEG B -- the sign sub-finding (delta_th-free, alpha-free)
# ===========================================================================
@dataclass
class SignResult:
    threaded_electron_rest_mass_me: float  # >= 0
    elastic_strain_sign: str  # ">= 0" by Ax1 (ring is stretched, not relaxed)
    sign_delta_m: str  # "+" (neutron heavier), forced
    conditionality: str  # the exhaustiveness qualifier (C2 coupling-term caveat)
    beta_decay_lower_bound_me: float  # the STRONGER, C2-immune bound: Delta m > this
    beta_decay_bound_basis: str  # the canonical mechanism grounding the stronger bound


def sign_leg() -> SignResult:
    """The sign is forced positive -- two justifications, the second STRONGER and C2-immune.

    (1) POSITIVITY of the two CANONICAL named terms: n = bare proton + threaded 0_1 electron
        (rest mass = +1.000 m_e, the electron IS the m_e unit) + Ax1-forced Borromean expansion
        (elastic strain energy >= 0: Ax1 forbids the flux tube shrinking below l_node, so the ring
        is STRETCHED, strain energy >= 0). Sum of two non-negative additions -> Delta m > 0.
        CONDITIONALITY (review R2): this rides on the two NAMED terms being exhaustive; the driver's
        own C2 (threading-lock / boundary coupling energy) is enumerated missing with UNDETERMINED
        sign, and composite binding CAN reduce mass in this leaf family (He-4 is 28.3 MeV bound
        below its constituents, proton-neutron-mass-split.md:28). So (1) forces Delta m > 0 only if
        the C2 coupling term is not large-and-negative. Hence "no assumption BEYOND the two named
        terms", not "NO new assumption" flatly.
    (2) BETA-DECAY-DOWNHILL energetics (canonical, C2-immune, STRONGER): neutron-identification.md:26
        property 4 makes free-neutron beta-decay spontaneous (n -> p + e + nu-bar; the tensioned
        electron slips its lock and is ejected). A spontaneous decay is exothermic, so
        m_n c^2 > (m_p + m_e) c^2 + KE + E_nu-bar >= (m_p + m_e) c^2, i.e. Delta m > 1.000 m_e.
        This is a GLOBAL energetics bound on the final-state rest masses -- it subsumes any C2
        coupling term and does NOT read the measured 1.293 MeV (it uses only the canonical fact
        that decay occurs, property 4, not its Q-value). delta_th-free and alpha-free (sign_leg
        consumes zero module constants).
    """
    m_e_threaded = 1.0  # the 0_1 unknot's rest mass, in m_e units (definitional, canonical)
    return SignResult(
        threaded_electron_rest_mass_me=m_e_threaded,
        elastic_strain_sign=">= 0 (Ax1: ring stretched, not relaxed)",
        sign_delta_m="+",
        conditionality="forced by the two CANONICAL terms; conditional on C2 (coupling energy, "
        "sign undetermined) not being large-and-negative -- see the stronger beta-decay bound",
        beta_decay_lower_bound_me=1.000,
        beta_decay_bound_basis="free-neutron beta-decay is spontaneous (neutron-identification.md:26 "
        "property 4) => exothermic => m_n > m_p + m_e => Delta m > 1.000 m_e; C2-immune, uses "
        "decay-occurs not the measured Q-value",
    )


# ===========================================================================
# LEG C -- magnitude computability (the gate)
# ===========================================================================
@dataclass
class MagnitudeResult:
    computable: bool
    fixed_components_me: dict[str, float]  # frozen-chain-fixed split components
    underived_components: list[str]  # named-but-not-computable components
    computed_split_me: float | None  # a NUMBER only if computable is True
    missing_choices: list[str]  # verbatim, for bin (iv)


# The verbatim missing-choice enumeration for bin (iv) (prereg hard rail 3).
MISSING_CHOICES: list[str] = [
    "C1 -- FS field ansatz for the threaded 0_1 unknot inside the 6_2^3 cage: no composite "
    "configuration exists in the corpus (neutron-identification.md:77).",
    "C2 -- the threading-lock / boundary coupling energy term (how the 0_1 tube couples to the "
    "Borromean cage): no energy functional term in the corpus.",
    "C3 -- the Borromean cage elastic stiffness that converts the forced radial expansion into "
    "strain energy: not derived; neutron-identification.md:54 FLAGS even the l_node-radial-"
    "expansion premise as 'not established'.",
    "C4 -- the mass-accounting convention: is the threaded electron's rest mass additively "
    "counted (Reading X) or absorbed into the surplus (Reading Y)? proton-neutron-mass-split.md:10 "
    "leaves this open (attributes the WHOLE surplus to elastic tension, no separate m_e term).",
    "C5 -- whether delta_th softens the composite's coupling is UNDETERMINED (review R1, 2026-07-14): "
    "the corpus's OWN named completion route -- neutron-identification.md:36/:77 TBD-pin, "
    "'Same shape as proton mass eigenvalue derivation ... adding to the FS energy integral' -- "
    "instructs a proton-shaped FS derivation, and that solver consumes the delta_th-softened "
    "KAPPA_FS = 8pi(1-delta_th) (constants.py:896). So kappa_FS carry-over is arguably the CANONICAL "
    "DEFAULT, not a new assumption. FORK: the linear-elastic-stiffness bound route "
    "(neutron-identification.md:54) may instead be delta_th-free. Unresolved until C1-C3 are built. "
    "[KEEP-BOTH -- superseded framing: 'the neutron construction never invokes a kappa_FS softening; "
    "adopting one would be a new assumption, not a canonical carry-over' (2026-07-13 pre-review).]",
]


def corpus_has_derived_neutron_mass(source: object = constants) -> bool:
    """DETECTOR (review R6c): does the module now carry a DERIVED neutron mass (not a CODATA anchor)?

    The bin-(iv) 'no computable split' claim is a global-negative established by corpus reading at
    prereg time (it cannot be proven by a runtime scan). But the ONE mechanically-checkable
    corpus-state signal IS scannable: today M_N_MEV_TARGET is a bare CODATA literal
    (constants.py:1107) and there is no derived neutron-mass symbol. If a future commit adds one
    (M_N_MEV_AVE / NEUTRON_ELECTRON_RATIO / a derived M_N), the split may have become computable and
    the adjudication MUST be re-run -- so this detector flips the leg off the hard-coded (iv).
    """
    derived_symbols = ("M_N_MEV_AVE", "NEUTRON_ELECTRON_RATIO", "M_N_ELECTRON_RATIO", "N_ELECTRON_RATIO")
    return any(hasattr(source, s) for s in derived_symbols)


def magnitude_computability_leg(source: object = constants) -> MagnitudeResult:
    """Adjudicate whether the frozen chain yields a computable split magnitude.

    ADJUDICATION CONSTANT (review R6c): `computable=False` is NOT a runtime numeric detector output
    -- it is a prereg-time corpus-completeness adjudication (a global-negative 'no composite-FS
    neutron derivation exists in the corpus') codified as a literal, with receipts
    neutron-identification.md:25,36,77 + constants.py:1104 + the odd-c-only BARYON_LADDER {5,7,9,11,13}
    (the neutron is 'NOT a (2,q) family entry', neutron-identification.md:23). The ONE
    mechanically-checkable corpus-state signal is wired as a live DETECTOR: `corpus_has_derived_
    neutron_mass()` -- if a derived neutron mass ever appears in the module, this leg raises so the
    adjudication is re-run (it is not a frozen verdict that cannot fire).

    Frozen chain fixes m_p (the bulk mass that CANCELS in the difference) and the electron rest
    mass (+1.000 m_e). The neutron surplus over the BARE proton has two named parts
    (neutron-identification.md:25,36; proton-neutron-mass-split.md:10):
      (a) threaded electron rest mass  -> frozen-chain value = +1.000 m_e (Reading X only)
      (b) elastic-expansion tension    -> NO frozen-chain value (mechanism named, magnitude TBD)

    The target split +2.531 m_e = (a)+1.000 + (b)+1.531. Component (b) -- the DOMINANT part, and
    the WHOLE surplus under Reading Y -- has no literal, no code path, no solver output anywhere in
    the corpus. Computing it requires >=1 of the MISSING_CHOICES -> STOP.
    """
    if corpus_has_derived_neutron_mass(source):
        raise RuntimeError(
            "CORPUS-STATE CHANGE: a derived neutron-mass symbol now exists in ave.core.constants; "
            "the bin-(iv) 'no computable split' adjudication is STALE and must be re-run "
            "(the split may now be computable -- re-adjudicate against the new derivation)."
        )
    # Every emitted split component is routed through the mint + seed guards (review R3/R6b): the
    # guards are now LIVE on the actual output, not plant-only. A future computed_split_me MUST use
    # the same gateway (_guarded_component) or it cannot enter the result.
    fixed = {
        "threaded_electron_rest_mass (Reading X)": _guarded_component(
            "threaded_electron_rest_mass", 1.000, provenance="electron_rest_mass_0_1_unknot"
        ),  # +1.000 m_e, frozen-chain-fixed
    }
    underived = [
        "elastic_expansion_tension -- mechanism named (Ax1 stretch), MAGNITUDE not derived; "
        "= +1.531 m_e (=0.782 MeV, the beta-decay Q-value) under Reading X, or the whole "
        "+2.531 m_e under Reading Y. No frozen-chain value.",
    ]
    # The split is NOT computable: the dominant/whole component has no frozen-chain value, and
    # obtaining it needs a non-canonical choice. We do NOT emit a number for the split.
    return MagnitudeResult(
        computable=False,
        fixed_components_me=fixed,
        underived_components=underived,
        computed_split_me=None,
        missing_choices=list(MISSING_CHOICES),
    )


def _guarded_component(name: str, value: float, provenance: str) -> float:
    """The single gateway every emitted split component passes: mint guard THEN seed guard.

    Wires assert_no_seed + provenance_guarded_magnitude into the LIVE path (review R3/R6b) so the
    hard rails are structural, not convention: a component from non-canonical provenance is rejected
    (mint), and a component whose VALUE equals the answer (proton ratio / 1.293 / 2.531 / 939.565)
    is rejected (seed). Any future magnitude path MUST route through here.
    """
    provenance_guarded_magnitude(name, value, provenance)
    assert_no_seed(value, label=name)
    return value


def provenance_guarded_magnitude(component: str, value: float, provenance: str) -> float:
    """Hard rail 1+3: refuse to emit a split magnitude from a constant not in the frozen chain.

    A mint plant (a fabricated E_elastic with provenance 'invented') is rejected here.
    """
    allowed = set(CONSUMED_CONSTANTS) | {"P_C", "M_E", "electron_rest_mass_0_1_unknot"}
    if provenance not in allowed:
        raise ValueError(
            f"MINT VIOLATION: refusing to emit split component {component}={value!r} from "
            f"non-canonical provenance {provenance!r}. Allowed provenance: {sorted(allowed)}. "
            f"The elastic-expansion tension has NO such provenance (hard rail 1+3)."
        )
    return value


# ===========================================================================
# BIN CLASSIFIER (the frozen bins; fireable off bin (iv) by a plant)
# ===========================================================================
def target_split_me(source: object = constants) -> float:
    """Frozen target band centre, DERIVED from CODATA anchors (band-NAMING only, not an input)."""
    return (float(source.M_N_MEV_TARGET) - float(source.M_P_MEV_CODATA)) / _me_c2_mev(source)


def classify_bin(mag: MagnitudeResult, target: float | None = None) -> tuple[str, str]:
    """Return (bin_id, one-line consequence). Bin (iv) unless a computable split exists."""
    if target is None:
        target = target_split_me()
    lo, hi = target / 2.0, target * 2.0  # 2x band, same sign
    if not mag.computable or mag.computed_split_me is None:
        return (
            "iv",
            "CHAIN-INSUFFICIENT: the canonical neutron construction does not define a computable "
            "mass without new assumptions. Honest instrument gap, NOT a physics verdict.",
        )
    dm = mag.computed_split_me
    if dm < 0:
        # Prereg bin (ii) consequence, FROZEN VERBATIM (review R7: full text restored, incl. the
        # epic-40 corroboration sentence dropped in the pre-review driver).
        return (
            "ii",
            "WRONG-SIGN: the ppm precision of the m_p/m_e chain is confirmed a proton-specific "
            "coincidence -- a delta_th tuned to land the proton on CODATA has no reason to produce "
            "the correct sign of a difference measurement, and it did not. This corroborates the "
            "epic-40 Delta(1232) +2.35% miss ('proton-specific tightness = COINCIDENCE').",
        )
    if lo <= dm <= hi:
        return ("i", "STRUCTURE-SIGNAL: correct sign AND within 2x -- tuning hypothesis harder to hold.")
    return ("iii", "RIGHT-SIGN-WRONG-MAGNITUDE: structure carries the sign but not the scale.")


# ===========================================================================
# HONEST-COMPARISON (CODATA anchors -- NAMING ONLY, never a derivation input)
# ===========================================================================
def codata_target() -> dict[str, float]:
    """The experimental target, from module CODATA anchors -- for reporting, not derivation."""
    m_e_mev = _me_c2_mev()
    dm_mev = float(constants.M_N_MEV_TARGET) - float(constants.M_P_MEV_CODATA)
    return {
        "m_e_c2_MeV": m_e_mev,
        "m_n_minus_m_p_MeV": dm_mev,
        "m_n_minus_m_p_me": dm_mev / m_e_mev,
    }


def run_gate() -> dict:
    """Run all legs and return the structured verdict."""
    refit = no_refit_audit()
    if not refit.ok:
        raise RuntimeError(f"NO-REFIT ABORT: {refit.mismatches}")
    sign = sign_leg()
    mag = magnitude_computability_leg()
    bin_id, consequence = classify_bin(mag)
    target = codata_target()
    return {
        "no_refit_ok": refit.ok,
        "proton_ratio": refit.proton_ratio_reproduced,
        "sign_delta_m": sign.sign_delta_m,
        "sign_conditionality": sign.conditionality,
        "beta_decay_lower_bound_me": sign.beta_decay_lower_bound_me,
        "beta_decay_bound_basis": sign.beta_decay_bound_basis,
        "computable": mag.computable,
        "computed_split_me": mag.computed_split_me,
        "fixed_components_me": mag.fixed_components_me,
        "underived_components": mag.underived_components,
        "bin": bin_id,
        "consequence": consequence,
        "missing_choices": mag.missing_choices,
        "codata_target": target,
    }


def main() -> None:
    r = run_gate()
    t = r["codata_target"]
    print("=" * 78)
    print("THE N-P MASS-SPLIT GATE -- same frozen chain, same delta_th, NO refit")
    print("=" * 78)
    print("\n[LEG A] no-refit audit")
    print(f"  frozen chain reproduced OK: {r['no_refit_ok']}")
    print(f"  PROTON_ELECTRON_RATIO (live-reproduced): {r['proton_ratio']!r}")
    print("\n[LEG B] sign sub-finding (delta_th-free, alpha-free)")
    print("  (1) two CANONICAL positive-definite terms: rest mass +1.000 m_e (>= 0) + Ax1 strain (>= 0)")
    print(f"      => sign(Delta m) = {r['sign_delta_m']}  (conditional on C2 coupling not large-negative)")
    print(f"  (2) STRONGER, C2-immune: beta-decay downhill => Delta m > {r['beta_decay_lower_bound_me']:.3f} m_e")
    print(f"      basis: {r['beta_decay_bound_basis']}")
    print("\n[LEG C] magnitude computability")
    print(f"  frozen-chain-fixed components (m_e): {r['fixed_components_me']}")
    for u in r["underived_components"]:
        print(f"  UNDERIVED: {u}")
    print(f"  computable split from frozen chain: {r['computable']}")
    print("\n[TARGET -- CODATA anchors, naming only, NOT a derivation input]")
    print(f"  m_n - m_p = {t['m_n_minus_m_p_MeV']:.6f} MeV = +{t['m_n_minus_m_p_me']:.4f} m_e")
    print(f"\n[VERDICT] bin ({r['bin']})")
    print(f"  {r['consequence']}")
    if r["bin"] == "iv":
        print("\n  MISSING CHOICES (verbatim -- required to make the split computable; NOT made):")
        for c in r["missing_choices"]:
            print(f"    - {c}")
    print("\n[INTERPRETATION-CARE] a bin-(iv) is an instrument gap, NOT a falsification: it does")
    print("  NOT falsify the +0.74% bare-topology result (stands independently of delta_th), and")
    print("  does NOT confirm the proton-specific-coincidence hypothesis. The sign (+) IS forced,")
    print("  delta_th-free. NOTE (review R1): delta_th-loading of the split is C5-UNDETERMINED, not")
    print("  'never' -- the corpus's own TBD-pin (neutron-identification.md:36/:77) instructs a")
    print("  proton-shaped FS derivation that DOES consume delta_th-softened kappa_FS, so Route A")
    print("  (that TBD-pin, built value-blind) IS the delta_th second shot against the CANONICAL")
    print("  neutron; a competing linear-elastic route (:54) may be delta_th-free -- FORK-OPEN.")


if __name__ == "__main__":
    main()
