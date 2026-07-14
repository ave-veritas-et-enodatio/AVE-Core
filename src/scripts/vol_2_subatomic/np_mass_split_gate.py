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

import math
from dataclasses import dataclass, field

from ave.core import constants

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


def reference_from_constants(source: object = constants) -> dict[str, float]:
    """A snapshot of the consumed constants from the live module (the default no-refit reference)."""
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
    mutated attribute (a refit plant) to prove the audit trips. `reference` defaults to a snapshot
    of the live module; the exempt regression test passes the frozen HEAD literals so a DELTA_THERMAL
    refit (upstream of the reproduction path) is also caught.
    """
    if reference is None:
        reference = reference_from_constants()

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


def sign_leg() -> SignResult:
    """Both named neutron contributions are positive-definite -> sign(Delta m) = + .

    n = bare proton + threaded 0_1 electron (rest mass = +1.000 m_e, the electron IS the m_e unit)
                    + Ax1-forced Borromean expansion (elastic strain energy >= 0: Ax1 forbids the
                    flux tube shrinking below l_node, so the ring is STRETCHED, strain energy >= 0).
    Sum of two non-negative additions to the bare-proton energy -> Delta m > 0 (neutron heavier),
    structurally FORCED, with NO delta_th and NO new assumption. Robust to the mass-accounting
    ambiguity (Reading X vs Y): under both, every contribution is >= 0.
    """
    m_e_threaded = 1.0  # the 0_1 unknot's rest mass, in m_e units (definitional, canonical)
    return SignResult(
        threaded_electron_rest_mass_me=m_e_threaded,
        elastic_strain_sign=">= 0 (Ax1: ring stretched, not relaxed)",
        sign_delta_m="+",
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
    "C5 -- whether delta_th (or a threaded analog) softens the composite's coupling: the neutron "
    "construction never invokes a kappa_FS softening for the split; adopting one would be a new "
    "assumption, not a canonical carry-over.",
]


def magnitude_computability_leg() -> MagnitudeResult:
    """Enumerate the frozen-chain quantities that map to a split component.

    Frozen chain fixes m_p (the bulk mass that CANCELS in the difference) and the electron rest
    mass (+1.000 m_e). The neutron surplus over the BARE proton has two named parts
    (neutron-identification.md:25,36; proton-neutron-mass-split.md:10):
      (a) threaded electron rest mass  -> frozen-chain value = +1.000 m_e (Reading X only)
      (b) elastic-expansion tension    -> NO frozen-chain value (mechanism named, magnitude TBD)

    The target split +2.531 m_e = (a)+1.000 + (b)+1.531. Component (b) -- the DOMINANT part, and
    the WHOLE surplus under Reading Y -- has no literal, no code path, no solver output anywhere in
    the corpus (M_N is a CODATA anchor: constants.py:1104 'no framework derivation has yet been
    adopted for the neutron mass'). Computing it requires >=1 of the MISSING_CHOICES -> STOP.
    """
    fixed = {
        "threaded_electron_rest_mass (Reading X)": 1.000,  # +1.000 m_e, frozen-chain-fixed
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
        return (
            "ii",
            "WRONG-SIGN: the ppm precision of the m_p/m_e chain is confirmed a proton-specific "
            "coincidence -- a delta_th tuned to land the proton on CODATA has no reason to produce "
            "the correct sign of a difference measurement, and it did not.",
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
    print("  threaded electron rest mass: +1.000 m_e (>= 0)")
    print("  elastic strain energy:       >= 0 (Ax1: ring stretched, not relaxed)")
    print(f"  => sign(Delta m) = {r['sign_delta_m']}  (neutron heavier -- structurally FORCED)")
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
    print("  delta_th-free. NOTE: the canonical neutron is a composite additive mechanism, NOT a")
    print("  (2,q) delta_th-modulated eigenvalue -- so the difference measurement does not actually")
    print("  load delta_th (the split's dominant term is elastic strain, not a kappa_FS softening).")


if __name__ == "__main__":
    main()
