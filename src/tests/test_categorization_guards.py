"""Categorization guards — ledger pairing, wave-speed slots, theorem keepers.

Test-fires ``ave.core.categorization`` (tooling for entailment vs reconciliation,
INVARIANT-S2 c_EM/c_shear slot refusal, SYM/ASYM load class, parity + 3-port
theorem identities).
"""

from __future__ import annotations

import pytest

from ave.core.categorization import (
    ClaimClass,
    CategorizationError,
    LedgerKind,
    LoadClass,
    PairingKind,
    WaveSpeedSlot,
    backreaction_ledger_tags,
    bare_junction_gamma,
    combination_tone_parity_allowed,
    classify_ledger_pairing,
    difference_tone_allowed_subyield,
    effective_speeds,
    reciprocal_3port_s11_floor,
    require_ledger_pairing,
    require_load_class_for_alpha_invariance,
    require_wave_speed_slot,
)
from ave.gravity.backreaction import solve_backreaction


# ══════════════════════════════════════════════════════════════════════════════
# Ledger pairing (#651 / X44 taxonomy)
# ══════════════════════════════════════════════════════════════════════════════


@pytest.mark.claim_class("certification_entailed")
def test_flux_vs_add_inertial_is_entailed_certification() -> None:
    p = classify_ledger_pairing(LedgerKind.FAR_FIELD_FLUX, LedgerKind.TOTAL_ENERGY_ADD)
    assert p.kind is PairingKind.ENTAILED
    assert p.claim_class is ClaimClass.CERTIFICATION_ENTAILED
    assert p.is_certification


@pytest.mark.claim_class("reconciliation_fireable")
def test_flux_vs_adm_is_fireable_reconciliation() -> None:
    p = classify_ledger_pairing(LedgerKind.FAR_FIELD_FLUX, LedgerKind.ADM_DEFICIT)
    assert p.kind is PairingKind.FIREABLE
    assert p.claim_class is ClaimClass.RECONCILIATION_FIREABLE
    assert p.is_reconciliation


def test_forbidden_pairing_raises() -> None:
    with pytest.raises(CategorizationError, match="FORBIDDEN"):
        classify_ledger_pairing(LedgerKind.TOTAL_ENERGY_ADD, LedgerKind.ADM_DEFICIT)


def test_require_pairing_expect_mismatch_raises() -> None:
    with pytest.raises(CategorizationError, match="expected"):
        require_ledger_pairing(
            LedgerKind.FAR_FIELD_FLUX,
            LedgerKind.ADM_DEFICIT,
            expect=PairingKind.ENTAILED,
        )


def test_solve_backreaction_stamps_ledger_tags() -> None:
    res = solve_backreaction(N=12, amplitude=0.03, g_self=0.0, max_outer=2)
    tags = res["ledger_tags"]
    assert tags["source_convention"] == "add_field"
    assert tags["far_field_vs_adm"] == PairingKind.FIREABLE.value
    assert tags["far_field_vs_add_inertial"] == PairingKind.ENTAILED.value
    assert tags["adm_label_ledger"] == LedgerKind.ADM_DEFICIT.value


def test_komar_convention_tags_mark_add_inertial_fireable() -> None:
    tags = backreaction_ledger_tags(source_convention="komar")
    assert tags["far_field_vs_add_inertial"] == PairingKind.FIREABLE.value
    assert tags["far_field_vs_adm"] == PairingKind.FIREABLE.value


# ══════════════════════════════════════════════════════════════════════════════
# Wave-speed slots + SYM / ASYM (INVARIANT-S2 Pitfall #5)
# ══════════════════════════════════════════════════════════════════════════════


def test_alpha_slot_accepts_c_em_refuses_c_shear() -> None:
    assert require_wave_speed_slot("fine_structure_alpha", WaveSpeedSlot.C_EM) is WaveSpeedSlot.C_EM
    with pytest.raises(CategorizationError, match="Pitfall #5"):
        require_wave_speed_slot("fine_structure_alpha", WaveSpeedSlot.C_SHEAR)


def test_schwarzschild_slot_accepts_c_shear_refuses_c_em() -> None:
    assert (
        require_wave_speed_slot("schwarzschild_redshift", WaveSpeedSlot.C_SHEAR)
        is WaveSpeedSlot.C_SHEAR
    )
    with pytest.raises(CategorizationError, match="Pitfall #5"):
        require_wave_speed_slot("schwarzschild_redshift", WaveSpeedSlot.C_EM)


def test_sym_load_speeds_and_z_invariant() -> None:
    s = effective_speeds(0.64, load=LoadClass.SYM)
    assert s["c_shear"] == pytest.approx(0.8)
    assert s["c_EM"] == pytest.approx(1.0 / 0.64)
    assert s["Z_over_Z0"] == pytest.approx(1.0)
    require_load_class_for_alpha_invariance(LoadClass.SYM)


def test_asym_eps_load_modulates_z_and_blocks_alpha_invariance() -> None:
    s = effective_speeds(0.64, load=LoadClass.ASYM_EPS)
    assert s["c_EM"] == pytest.approx(1.0 / 0.8)
    assert s["Z_over_Z0"] == pytest.approx(1.0 / 0.8)
    with pytest.raises(CategorizationError, match="SYM"):
        require_load_class_for_alpha_invariance(LoadClass.ASYM_EPS)


# ══════════════════════════════════════════════════════════════════════════════
# Theorem keepers — parity (clm-invmtr) + 3-port (clm-v3port)
# ══════════════════════════════════════════════════════════════════════════════


@pytest.mark.claim_class("B_axiom_manifestation")
def test_parity_theorem_difference_tone_forbidden() -> None:
    assert difference_tone_allowed_subyield() is False
    assert combination_tone_parity_allowed(1, -1) is False  # ω_hi − ω_lo
    assert combination_tone_parity_allowed(2, -1) is True  # 2ω_lo − ω_hi (FWM)
    assert combination_tone_parity_allowed(1, 1) is False  # 2ω sum even
    assert combination_tone_parity_allowed(1, 0) is True  # fundamental


@pytest.mark.claim_class("A_identity")
def test_three_port_bare_gamma_and_s11_floor() -> None:
    assert bare_junction_gamma(3) == pytest.approx(-1.0 / 3.0)
    assert reciprocal_3port_s11_floor(3) == pytest.approx(1.0 / 3.0)
    assert bare_junction_gamma(4) == pytest.approx(-0.5)
