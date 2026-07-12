"""Engine categorization guards — ledger pairing, claim class, wave-speed slots.

Closes the failure mode where agents (and tests) bank an *entailed* identity
(e.g. Gauss flux ≡ ∫T₀₀^src) as a *reconciliation* of two different functionals
(e.g. flux vs M_eff), or plug ``c_shear`` into the α formula / ``c_EM`` into a
Schwarzschild reduction (INVARIANT-S2 Pitfall #5).

This module is **tooling**, not a new chord. It encodes taxonomy already named
in the KB / skills (consistency-vs-emergence; translation-circuit parity and
3-port theorems; gravity ADD vs SUBTRACT ledger split from #651 / X44).

Public entry points raise :class:`CategorizationError` on illegal pairings /
slots so misuse fails loudly at call time.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Iterable

import numpy as np

# ══════════════════════════════════════════════════════════════════════════════
# Claim / gate class (A47 consistency-vs-emergence + certification entailment)
# ══════════════════════════════════════════════════════════════════════════════


class ClaimClass(str, Enum):
    """What a numeric agreement means (skill ``consistency-vs-emergence``)."""

    IDENTITY = "A_identity"
    AXIOM_MANIFESTATION = "B_axiom_manifestation"
    CONSISTENCY = "C_consistency"
    EMERGENCE = "D_emergence"
    OPERATING_POINT = "E_operating_point"
    # Certification of an install-tautology (Gauss ≡ source). Not Class D.
    CERTIFICATION_ENTAILED = "certification_entailed"
    # Cross-functional agreement that is fireable and may miss (X44).
    RECONCILIATION_FIREABLE = "reconciliation_fireable"


# ══════════════════════════════════════════════════════════════════════════════
# Gravity / energy ledger taxonomy (#651 / X44)
# ══════════════════════════════════════════════════════════════════════════════


class LedgerKind(str, Enum):
    """Named energy / charge registers on the gravity back-reaction solve."""

    MATTER = "matter"  # ∫ T₀₀^matter
    FIELD_STRAIN = "field_strain"  # U_bind = ∫ ½ g |∇ε|²
    TOTAL_ENERGY_ADD = "total_energy_add"  # M + U  (ADD-side inertial ledger)
    ADM_DEFICIT = "adm_deficit"  # M − U  (engine-labeled M_eff)
    CLOCK_WEIGHT_DEFICIT = "clock_weight_deficit"  # Δ_clock = ∫ T(1−√S)
    FAR_FIELD_FLUX = "far_field_flux"  # Σ_interior (L @ ε) ≡ ∫ T₀₀^src
    PICARD_SOURCE = "picard_source"  # T₀₀^src as installed


class PairingKind(str, Enum):
    """Whether comparing two ledgers is entailed or fireable."""

    ENTAILED = "entailed"  # same install / discrete Gauss identity
    FIREABLE = "fireable"  # different functionals; may miss
    FORBIDDEN = "forbidden"  # category error; do not form η from this pair


# Allowed (numerator, denominator) → pairing kind for Nordtvedt-style ratios.
# Far-field flux is always ≡ Picard source (Gauss). Under legacy ADD the Picard
# source is M+U, so flux vs TOTAL_ENERGY_ADD is ENTAILED. Flux vs ADM_DEFICIT is
# FIREABLE (the #651 / X44 mixed register).
_LEDGER_PAIRINGS: dict[tuple[LedgerKind, LedgerKind], PairingKind] = {
    (LedgerKind.FAR_FIELD_FLUX, LedgerKind.PICARD_SOURCE): PairingKind.ENTAILED,
    (LedgerKind.FAR_FIELD_FLUX, LedgerKind.TOTAL_ENERGY_ADD): PairingKind.ENTAILED,
    (LedgerKind.FAR_FIELD_FLUX, LedgerKind.ADM_DEFICIT): PairingKind.FIREABLE,
    (LedgerKind.FAR_FIELD_FLUX, LedgerKind.CLOCK_WEIGHT_DEFICIT): PairingKind.FORBIDDEN,
    (LedgerKind.ADM_DEFICIT, LedgerKind.CLOCK_WEIGHT_DEFICIT): PairingKind.FIREABLE,
    (LedgerKind.TOTAL_ENERGY_ADD, LedgerKind.ADM_DEFICIT): PairingKind.FORBIDDEN,
}


@dataclass(frozen=True)
class LedgerPairing:
    numerator: LedgerKind
    denominator: LedgerKind
    kind: PairingKind
    claim_class: ClaimClass

    @property
    def is_certification(self) -> bool:
        return self.kind is PairingKind.ENTAILED

    @property
    def is_reconciliation(self) -> bool:
        return self.kind is PairingKind.FIREABLE


class CategorizationError(ValueError):
    """Illegal ledger pairing, wave-speed slot, or load-class use."""


def classify_ledger_pairing(
    numerator: LedgerKind | str,
    denominator: LedgerKind | str,
) -> LedgerPairing:
    """Classify a Nordtvedt-style register pairing.

    Raises :class:`CategorizationError` if the pair is FORBIDDEN or unknown.
    """
    num = LedgerKind(numerator)
    den = LedgerKind(denominator)
    kind = _LEDGER_PAIRINGS.get((num, den))
    if kind is None:
        raise CategorizationError(
            f"unknown ledger pairing {num.value!r} vs {den.value!r}; "
            f"register it explicitly in ave.core.categorization._LEDGER_PAIRINGS"
        )
    if kind is PairingKind.FORBIDDEN:
        raise CategorizationError(
            f"FORBIDDEN ledger pairing: {num.value} vs {den.value} — "
            f"category error (do not form η / bank agreement from this pair)"
        )
    claim = (
        ClaimClass.CERTIFICATION_ENTAILED
        if kind is PairingKind.ENTAILED
        else ClaimClass.RECONCILIATION_FIREABLE
    )
    return LedgerPairing(numerator=num, denominator=den, kind=kind, claim_class=claim)


def require_ledger_pairing(
    numerator: LedgerKind | str,
    denominator: LedgerKind | str,
    *,
    expect: PairingKind | Iterable[PairingKind] | None = None,
) -> LedgerPairing:
    """Classify and optionally assert the expected pairing kind."""
    pairing = classify_ledger_pairing(numerator, denominator)
    if expect is not None:
        allowed = {expect} if isinstance(expect, PairingKind) else set(expect)
        if pairing.kind not in allowed:
            raise CategorizationError(
                f"ledger pairing {pairing.numerator.value} vs "
                f"{pairing.denominator.value} is {pairing.kind.value}, "
                f"expected one of {[k.value for k in allowed]}"
            )
    return pairing


def backreaction_ledger_tags(*, source_convention: str = "add_field") -> dict:
    """Metadata stamped onto ``solve_backreaction`` results.

    ``source_convention``:
      * ``"add_field"`` — legacy Picard ``T = matter + u_field`` (main / pre-X44).
      * ``"komar"`` — ruled ``T = matter · √S`` (X44; when installed).
    """
    if source_convention == "add_field":
        picard = LedgerKind.TOTAL_ENERGY_ADD
        far_vs_adm = PairingKind.FIREABLE
        far_vs_inertial = PairingKind.ENTAILED
    elif source_convention == "komar":
        picard = LedgerKind.PICARD_SOURCE  # weighted matter; not M±U
        far_vs_adm = PairingKind.FIREABLE
        far_vs_inertial = PairingKind.FIREABLE  # M+U is no longer the source
    else:
        raise CategorizationError(
            f"unknown source_convention={source_convention!r}; "
            f"expected 'add_field' or 'komar'"
        )
    return {
        "source_convention": source_convention,
        "picard_source_ledger": picard.value,
        "adm_label_ledger": LedgerKind.ADM_DEFICIT.value,
        "far_field_vs_adm": far_vs_adm.value,
        "far_field_vs_add_inertial": far_vs_inertial.value,
        "claim_note": (
            "Gauss flux ≡ Picard source is CERTIFICATION_ENTAILED; "
            "flux vs M_eff is RECONCILIATION_FIREABLE (may miss — see X44)."
        ),
    }


# ══════════════════════════════════════════════════════════════════════════════
# Wave-speed slots + SYM / ASYM load class (INVARIANT-S2)
# ══════════════════════════════════════════════════════════════════════════════


class WaveSpeedSlot(str, Enum):
    """Which effective speed is legal in a derivation slot."""

    C_EM = "c_EM"  # Maxwell phase velocity c₀/S (SYM) or c₀/√S_ε (ASYM)
    C_SHEAR = "c_shear"  # mechanical / group / rest-mass velocity c₀√S


class LoadClass(str, Enum):
    """How the saturation kernel loads the ε / μ sectors."""

    SYM = "sym"  # both sectors scale → Z = Z₀, reflectionless
    ASYM_EPS = "asym_eps"  # static-E / ε-only → Z = Z₀√(S_μ/S_ε) with S_μ=1
    ASYM_MU = "asym_mu"  # μ-only (rare; reserved)


# Derivation slots → required wave-speed
_SLOT_SPEED: dict[str, WaveSpeedSlot] = {
    "fine_structure_alpha": WaveSpeedSlot.C_EM,
    "maxwell_phase_velocity": WaveSpeedSlot.C_EM,
    "schwarzschild_redshift": WaveSpeedSlot.C_SHEAR,
    "gravitational_time_dilation": WaveSpeedSlot.C_SHEAR,
    "rest_mass_transport": WaveSpeedSlot.C_SHEAR,
}


def require_wave_speed_slot(derivation: str, slot: WaveSpeedSlot | str) -> WaveSpeedSlot:
    """Refuse the Pitfall #5 substitution (c_shear in α, c_EM in Schwarzschild)."""
    want = _SLOT_SPEED.get(derivation)
    if want is None:
        raise CategorizationError(
            f"unknown derivation slot {derivation!r}; register in "
            f"ave.core.categorization._SLOT_SPEED"
        )
    got = WaveSpeedSlot(slot)
    if got is not want:
        raise CategorizationError(
            f"slot refusal: derivation {derivation!r} requires {want.value}, "
            f"got {got.value} (INVARIANT-S2 Pitfall #5)"
        )
    return got


def effective_speeds(S: float, *, load: LoadClass | str) -> dict[str, float]:
    """Return ``{c_EM, c_shear, Z_over_Z0}`` for a load class at saturation S.

    Cold lattice: pass ``S=1``. Speeds are normalized to ``c₀ = 1``.
    """
    load = LoadClass(load)
    S = float(S)
    if not (0.0 < S <= 1.0):
        raise CategorizationError(f"S must be in (0, 1], got {S}")
    c_shear = float(np.sqrt(S))
    if load is LoadClass.SYM:
        c_em = 1.0 / S
        z_ratio = 1.0
    elif load is LoadClass.ASYM_EPS:
        # S_ε = S, S_μ = 1 → c_EM = 1/√(μ ε) = 1/√S ; Z/Z0 = √(S_μ/S_ε) = 1/√S
        c_em = 1.0 / np.sqrt(S)
        z_ratio = 1.0 / np.sqrt(S)
    elif load is LoadClass.ASYM_MU:
        c_em = 1.0 / np.sqrt(S)
        z_ratio = float(np.sqrt(S))
    else:
        raise CategorizationError(f"unhandled load class {load}")
    return {
        "load": load.value,
        "S": S,
        "c_EM": float(c_em),
        "c_shear": c_shear,
        "Z_over_Z0": float(z_ratio),
    }


def require_load_class_for_alpha_invariance(load: LoadClass | str) -> LoadClass:
    """α invariance under operating-point bias holds for SYM loading only."""
    load = LoadClass(load)
    if load is not LoadClass.SYM:
        raise CategorizationError(
            f"α invariance (clm-3zz0f6) requires LoadClass.SYM; got {load.value}. "
            f"ASYM loads modulate α (separate claim surface)."
        )
    return load


# ══════════════════════════════════════════════════════════════════════════════
# Theorem keepers (parity / 3-port) — pure identities, no solve
# ══════════════════════════════════════════════════════════════════════════════


def combination_tone_parity_allowed(m: int, n: int) -> bool:
    """Even Ax-4 kernel ⇒ odd restoring force ⇒ tone m·ω_lo + n·ω_hi allowed iff m+n odd.

    Canonical: ``clm-invmtr`` (inversion-symmetry / difference-tone meter).
    """
    return ((int(m) + int(n)) % 2) == 1


def difference_tone_allowed_subyield() -> bool:
    """Literal difference tone ω_hi − ω_lo is FORBIDDEN sub-yield (m=+1, n=−1)."""
    return combination_tone_parity_allowed(1, -1)


def bare_junction_gamma(z: int = 3) -> float:
    """Matched-arm star junction: Γ = (2 − z)/z. For srs z=3 → −1/3.

    Canonical: matched-lossless-reciprocal-3-port floor (``clm-v3port``).
    """
    z = int(z)
    if z < 2:
        raise CategorizationError(f"coordination z must be ≥ 2, got {z}")
    return (2.0 - z) / float(z)


def reciprocal_3port_s11_floor(z: int = 3) -> float:
    """Lossless reciprocal matched 3-port: |S₁₁| ≥ |(2−z)/z| (= 1/3 at z=3)."""
    return abs(bare_junction_gamma(z))
