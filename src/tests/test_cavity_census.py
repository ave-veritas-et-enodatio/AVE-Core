"""CAVITY-CENSUS STAGE-1 — instrument gate tests (the plants must FIRE).

FROZEN PRE-REG: research/2026-07-14_cavity-census-stage1_prereg_FROZEN.md
RESULT DOC    : research/2026-07-14_cavity-census-stage1_RESULT.md

These are the machine-checkable plant-firing gates the frozen prereg requires
(§6 item 1 "the plant-firing gates"; §0.4 ê_w-as-positive-control; §4 bin-firing —
NOT a "§6 (f)", which is phantom, corrected 2026-07-14): a planted
geometric-only winding, a Nyquist-starved read, and a sector-crosswired detector —
each must TRIP its gate; and a genuinely-planted two-sector (2,3) must be READ
(the positive control / validate-on-known). The plants are eigenvector-level, not
arithmetic. If any gate fails to fire, the census verdict is UNTRUSTED.

  G0  POSITIVE CONTROL — the canonical detector reads a genuinely planted (2,3).
  G1  PLANT: geometric-only winding (seed-carried ê_w) — the canonical detector
      REFUSES it (reads NOT-(2,3)); the coordinate-prereg direction leg is
      tautologically 2 (proving the seed carries it, and that the emergence read
      is immune to the seed).
  G2  PLANT: Nyquist-starved read — the Nyquist gate fires ⇒ INCONCLUSIVE.
  G3  PLANT: sector-crosswired detector — the correct wiring reads a DIFFERENT
      (p,q) than the crosswired one (the two axes read two different sectors).
  G4  α-CLEAN — no α-carrier on the module's verdict path (import-guard triad).
  G5  SPHERE-LEG ABCD — the α-clean radial cascade reproduces the analytic
      Dirichlet-sphere l=0 spectrum kR = nπ (a validate-on-known for the sphere leg).
"""

import numpy as np
import pytest


def test_g0_positive_control_reads_planted_2_3():
    """The canonical two-sector detector MUST read a genuinely planted (2,3)."""
    from ave.solvers.cavity_census import gate_positive_control

    r = gate_positive_control()
    assert r["reads_planted"], f"detector failed to read planted (2,3): {r['read']}"
    assert r["ok"], r


def test_g1_planted_geometric_only_trips():
    """A winding living ONLY in the seeded ê_w (trivial eigenvector sectors) must be
    REFUSED by the canonical detector; the coordinate-prereg seed leg reads it (2)."""
    from ave.solvers.cavity_census import gate_planted_geometric_only

    r = gate_planted_geometric_only()
    assert r["canonical_refuses_seed"], r
    assert r["seed_leg_tautological"], r
    assert r["tripped"], r


def test_g2_nyquist_starved_trips():
    """A genuine high winding under-sampled below 10 samples/period must read
    INCONCLUSIVE (the Nyquist gate fires); a well-sampled control must not."""
    from ave.solvers.cavity_census import gate_nyquist_starved

    r = gate_nyquist_starved()
    assert not r["starved_nyquist_ok"], r
    assert not r["starved_read_ok"], r
    assert r["control_nyquist_ok"], r
    assert r["tripped"], r


def test_g3_sector_crosswired_trips():
    """A crosswired detector (A1 into both loops) reads a DIFFERENT (p,q) than the
    correct wiring — proving the two axes read two distinct sectors (no double-count)."""
    from ave.solvers.cavity_census import gate_sector_crosswired

    r = gate_sector_crosswired()
    assert r["correct_pq"] in [(2, 3), (3, 2)], r
    assert r["crosswired_pq"] != r["correct_pq"], r
    assert r["tripped"], r


def test_g3b_all_plants_trip_detector_trustworthy():
    """The aggregate gate: positive control passes AND all three plants trip ⇒ the
    detector is trustworthy (the census verdict may be trusted)."""
    from ave.solvers.cavity_census import run_plant_gates

    g = run_plant_gates()
    assert g["detector_trustworthy"], g


def test_g4_alpha_clean_verdict_path():
    """No α-carrier reaches the module's verdict path (the import-guard triad; the
    sphere-leg ABCD reuses the METHOD of radial_eigenvalue, NOT its α-loaded
    atomic potential)."""
    import ave.solvers.cavity_census as cc

    src = __import__("inspect").getsource(cc)
    # the module must NOT import the α-carrying atomic solver entrypoint.
    assert "radial_eigenvalue_abcd" not in src, "α-loaded atomic ABCD leaked onto the path"
    assert "from ave.core.constants import" not in src, "constants (α-carrier) import leaked"
    for name in ("ALPHA", "Q_TANK", "V_SNAP", "KAPPA_CHIRAL_ELECTRON"):
        assert name not in dir(cc), f"α-carrier {name} on the module path"


def test_g5_sphere_abcd_matches_analytic_dirichlet_spectrum():
    """The α-clean ABCD radial cascade reproduces the analytic Dirichlet-sphere l=0
    spectrum kR = nπ (validate-on-known for the sphere leg)."""
    from ave.solvers.cavity_census import sphere_abcd_radial_spectrum

    s = sphere_abcd_radial_spectrum(l_max=1, n_modes=3)
    kR0 = s["eigen_kR"][0]
    for n, x in enumerate(kR0, start=1):
        assert abs(x - n * np.pi) < 0.02, f"l=0 mode {n}: {x} != {n}π"
    # l=0 ratios are exactly the integers 1,2,3
    assert s["ratios_to_l0n1"][0][:3] == [1.0, 2.0, 3.0], s["ratios_to_l0n1"]


@pytest.mark.engine_sim
def test_g6_cell_runs_dimensionless_and_lossless():
    """A census cell runs, is lossless (Hermitian ⇒ Im(ω)=0), and emits only
    dimensionless outputs on the winding path (Rail 2)."""
    from ave.solvers.cavity_census import CavityCensusConfig, autosize_N, run_cell

    c = run_cell(CavityCensusConfig(shape="sphere", bc_mode="geometric",
                                    R_over_lnode=1.0, N=autosize_N(1.0)))
    assert c["lossless"] and c["omega_im"] == 0.0
    assert c["alpha_clean"]
    # the winding class is one of the frozen bins (i) or an A1/A11 refinement. The
    # INCONCLUSIVE-* family reports the ACTUAL failing gate (amplitude/Nyquist/
    # disagree), not the collapsed always-"Nyquist" label (label-collapse repair).
    frozen_and_refined = {"(0,0)", "(1,1)", "(2,3)", "BASIS-AMBIGUOUS"}
    for key in ("bin_i_winding_class", "bin_i_winding_class_LA_fundamental"):
        wc = c[key]
        head = wc.split()[0]
        assert (head in frozen_and_refined or head.startswith("INCONCLUSIVE")
                or head.startswith("other-")), (key, wc)
    # KEEP-BOTH: both spectral ends are reported (SA defect band + LA fundamental).
    assert c["spectral_end_primary"].startswith("SA")
    assert "canonical_pq_LA" in c
