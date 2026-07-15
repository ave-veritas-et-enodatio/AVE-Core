"""BLOB-ABLATION kernel-OFF driver — unit guards on the ablation instruments.

These are NOT the physics verdict (that is the frozen battery, adjudicated in
research/2026-07-15_blob-ablation_NOTE.md). They guard the driver's three new
mechanisms so a green-main change cannot silently break the discriminator:

  1. the disclosed S≡1 disabled-flag (`off_lin`) actually PINS z_local ≡ Z₀ every
     step (the linearization is real, not a mislabelled nonlinear run);
  2. the S≡1 engine on a torus (no absorber) CONSERVES energy (lossless-reactive
     sanity — a blow-up would mean the override is buggy → INSTRUMENT);
  3. the `on` / amp 1.0 / no-ablation path reproduces the corrected #698
     `run_instrumented` core-holding byte-for-byte (Rule-14 anti-drift);
  4. the native toggle `off_mem` genuinely builds with the memristive kernel OFF;
  5. the sub-yield guard: the operative Cosserat seed front is R_II (A²=0.75, the
     nonlinear→saturated knee — NOT the frozen header's √α; see the NOTE
     AMENDMENTS), and every cell stays sub-yield (A²_local < 1).

Cost note (repo CI-partition constraint): the three distinct engine runs are
computed ONCE via session-scoped fixtures and shared across assertions (keeps the
added CI time near the 30-min `make test` timeout margin).

Ref: research/2026-07-15_blob-ablation_NOTE.md ; driver
src/scripts/vol_1_foundations/blob_ablation_kernel_off.py.
"""

from __future__ import annotations

import pytest

from scripts.vol_1_foundations.blob_ablation_kernel_off import (
    _build_variant,
    run_ablation,
)
from scripts.vol_1_foundations.gpersist_localization_observable import (
    _classify_cell,
    _core_holding,
    run_instrumented,
)

_N = 10  # small but keeps a non-trivial PML interior ((N-2·pml)³ = 4³ = 64)


@pytest.fixture(scope="module")
def torus_off_lin():
    """S≡1 (off_lin) on the torus — shared by the pin + conservation guards."""
    return run_ablation(N=_N, pml=0, mode="pair", kernel="off_lin", amp_scale=1.0, fast=True)


@pytest.fixture(scope="module")
def pml_on():
    """kernel-ON baseline on the PML box — shared by parity + sub-yield guards."""
    return run_ablation(N=_N, pml=3, mode="pair", kernel="on", amp_scale=1.0, fast=True)


# --------------------------------------------------------------------------
# 1 + 2 — the S≡1 disabled-flag is real and lossless on the torus
# --------------------------------------------------------------------------
def test_off_lin_pins_z_local_to_matched(torus_off_lin):
    """The disclosed off_lin override keeps z_local ≡ Z₀(=1) at EVERY step —
    max |z_local − 1| over the whole run is machine-zero (matched, Γ=0)."""
    assert torus_off_lin["kernel"] == "off_lin"
    assert torus_off_lin["linear_pin_max_abs"] < 1e-9, torus_off_lin["linear_pin_max_abs"]


def test_off_lin_torus_conserves_energy(torus_off_lin):
    """S≡1 on the torus (no sponge) is a lossless reactive system: H is conserved
    over the quiet window. Gross-failure guard (the production gate is 2 %)."""
    h_rel = torus_off_lin["core_holding"]["H_rel"]
    assert abs(h_rel) <= 0.05, f"torus off_lin H_rel={h_rel:+.4f} — override may be lossy/buggy"
    assert not torus_off_lin["aborted_over_yield"]


# --------------------------------------------------------------------------
# 3 — Rule-14 anti-drift: on/amp1.0 reproduces the corrected #698 instrument
# --------------------------------------------------------------------------
def test_on_baseline_parity_with_698_instrument(pml_on):
    """kernel='on', amp_scale=1.0, no ablation must reproduce the #698
    run_instrumented core-holding to machine precision (same primitives)."""
    ref = run_instrumented(_N, 3, "pair", True, plant=False)
    ref["classification"] = _classify_cell(ref)
    ref_ch = _core_holding(ref)
    my_ch = pml_on["core_holding"]
    for k in ("E_core_full_driveoff", "E_core_full_quietavg", "E_core_full_rel",
              "E_rest_interior_rel", "H_rel"):
        assert abs(ref_ch[k] - my_ch[k]) <= 1e-9, (k, ref_ch[k], my_ch[k])


# --------------------------------------------------------------------------
# 4 — native toggle genuinely disables the memristive kernel (build-only, cheap)
# --------------------------------------------------------------------------
def test_off_mem_builds_with_memristive_disabled():
    on = _build_variant(_N, 3, "pair", "on", 1.0)._coupled
    off = _build_variant(_N, 3, "pair", "off_mem", 1.0)._coupled
    assert on.use_memristive_saturation is True
    assert on.k4.use_memristive_saturation is True
    assert off.use_memristive_saturation is False
    assert off.k4.use_memristive_saturation is False


# --------------------------------------------------------------------------
# 5 — sub-yield guard: the frozen seed is well below A²=1
# --------------------------------------------------------------------------
def test_baseline_seed_is_sub_yield(pml_on):
    assert pml_on["sub_yield"] is True
    assert pml_on["max_A2_local"] < 1.0
    assert not pml_on["aborted_over_yield"]
