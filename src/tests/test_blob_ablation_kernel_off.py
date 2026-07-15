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
  5. the sub-yield guard: the frozen seed sits well below A²=1.

Ref: research/2026-07-15_blob-ablation_NOTE.md ; driver
src/scripts/vol_1_foundations/blob_ablation_kernel_off.py.
"""

from __future__ import annotations

from scripts.vol_1_foundations.blob_ablation_kernel_off import (
    _build_variant,
    run_ablation,
)
from scripts.vol_1_foundations.gpersist_localization_observable import (
    _core_holding,
    _classify_cell,
    run_instrumented,
)


# --------------------------------------------------------------------------
# 1 + 2 — the S≡1 disabled-flag is real and lossless on the torus
# --------------------------------------------------------------------------
def test_off_lin_pins_z_local_to_matched():
    """The disclosed off_lin override keeps z_local ≡ Z₀(=1) at EVERY step —
    max |z_local − 1| over the whole run is machine-zero (matched, Γ=0)."""
    res = run_ablation(N=10, pml=0, mode="pair", kernel="off_lin", amp_scale=1.0, fast=True)
    assert res["kernel"] == "off_lin"
    assert res["linear_pin_max_abs"] < 1e-9, res["linear_pin_max_abs"]


def test_off_lin_torus_conserves_energy():
    """S≡1 on the torus (no sponge) is a lossless reactive system: H is conserved
    over the quiet window. Gross-failure guard (the production gate is 2 %)."""
    res = run_ablation(N=10, pml=0, mode="pair", kernel="off_lin", amp_scale=1.0, fast=True)
    h_rel = res["core_holding"]["H_rel"]
    assert abs(h_rel) <= 0.05, f"torus off_lin H_rel={h_rel:+.4f} — override may be lossy/buggy"
    assert not res["aborted_over_yield"]


# --------------------------------------------------------------------------
# 3 — Rule-14 anti-drift: on/amp1.0 reproduces the corrected #698 instrument
# --------------------------------------------------------------------------
def test_on_baseline_parity_with_698_instrument():
    """kernel='on', amp_scale=1.0, no ablation must reproduce the #698
    run_instrumented core-holding to machine precision (same primitives)."""
    ref = run_instrumented(10, 3, "pair", True, plant=False)
    ref["classification"] = _classify_cell(ref)
    ref_ch = _core_holding(ref)
    mine = run_ablation(N=10, pml=3, mode="pair", kernel="on", amp_scale=1.0, fast=True)
    my_ch = mine["core_holding"]
    for k in ("E_core_full_driveoff", "E_core_full_quietavg", "E_core_full_rel",
              "E_rest_interior_rel", "H_rel"):
        assert abs(ref_ch[k] - my_ch[k]) <= 1e-9, (k, ref_ch[k], my_ch[k])


# --------------------------------------------------------------------------
# 4 — native toggle genuinely disables the memristive kernel
# --------------------------------------------------------------------------
def test_off_mem_builds_with_memristive_disabled():
    on = _build_variant(10, 3, "pair", "on", 1.0)._coupled
    off = _build_variant(10, 3, "pair", "off_mem", 1.0)._coupled
    assert on.use_memristive_saturation is True
    assert on.k4.use_memristive_saturation is True
    assert off.use_memristive_saturation is False
    assert off.k4.use_memristive_saturation is False


# --------------------------------------------------------------------------
# 5 — sub-yield guard: the frozen seed is well below A²=1
# --------------------------------------------------------------------------
def test_baseline_seed_is_sub_yield():
    res = run_ablation(N=10, pml=3, mode="pair", kernel="on", amp_scale=1.0, fast=True)
    assert res["sub_yield"] is True
    assert res["max_A2_local"] < 1.0
    assert not res["aborted_over_yield"]
