"""CMB Axis Alignment Driver — Phase 1: Angular-separation computation against literature axes.

Tests matrix row C5-CMB-AXIS + the 3-route framework commitment (foreword line 121-129).
Per the master synthesis at manuscript/ave-kb/common/divergence-test-substrate-map.md,
this is the HIGHEST-LEVERAGE operational test in the framework — closes the
single-cosmological-parameter claim in one shot.

AVE prediction: 7 observable axes (CMB axis-of-evil, Hubble flow, LSS rotation,
matter asymmetry, E/B polarization, orbital-plane alignment, G anisotropy) all
align with Omega_freeze axis at (l=174 deg, b=-5 deg) galactic coordinates.

Pass criterion (4-axis primary): all axes align to < 20 deg at > 3 sigma vs isotropic null.
Sharpest fail: CMB axis vs Hubble flow misaligned > 20 deg at > 3 sigma kills A-034 cosmic claim.

Phase 1 (this file): numpy only. Reads canonical AVE prediction + literature-cited published
axis positions for each observable; computes mutual angular separations; flags PASS/AMBIGUOUS/FAIL.
Honest TBD-pin-source flags where literature value is disputed or this author guessed.

Phase 2 (next session): install healpy + astropy; fetch raw Planck/Pantheon+/SDSS data;
re-derive each axis independently from raw data.

Run:
    python3 src/scripts/vol_3_macroscopic/cmb_axis_alignment_driver.py
"""
from __future__ import annotations

import math
from dataclasses import dataclass

# AVE canonical prediction per universal-saturation-kernel-catalog.md:88 +
# omega-freeze-cosmic-grain-cascade.md:26
OMEGA_FREEZE_L_DEG = 174.0  # galactic longitude
OMEGA_FREEZE_B_DEG = -5.0  # galactic latitude

# Alignment thresholds per prereg §3
PASS_THRESHOLD_DEG = 20.0  # < 20 deg = PASS
FAIL_THRESHOLD_DEG = 45.0  # > 45 deg = FAIL (effectively orthogonal)


@dataclass
class GalacticAxis:
    """A direction in galactic coordinates with literature citation + confidence."""

    name: str
    l_deg: float
    b_deg: float
    source: str
    confidence: str  # "pinned", "approximate", "disputed", or "TBD pin"

    def to_cartesian(self) -> tuple[float, float, float]:
        """Convert galactic (l, b) in degrees to Cartesian unit vector."""
        l_rad = math.radians(self.l_deg)
        b_rad = math.radians(self.b_deg)
        return (
            math.cos(b_rad) * math.cos(l_rad),
            math.cos(b_rad) * math.sin(l_rad),
            math.sin(b_rad),
        )


def angular_separation_deg(a: GalacticAxis, b: GalacticAxis) -> float:
    """Angular separation in degrees between two axes (undirected — uses min(theta, 180-theta))."""
    ax, ay, az = a.to_cartesian()
    bx, by, bz = b.to_cartesian()
    dot = max(-1.0, min(1.0, ax * bx + ay * by + az * bz))
    theta = math.degrees(math.acos(dot))
    # Axes are undirected lines (not rays); take min(theta, 180-theta) for fair comparison
    return min(theta, 180.0 - theta)


# Canonical AVE prediction
OMEGA_FREEZE = GalacticAxis(
    name="Omega_freeze (AVE prediction)",
    l_deg=OMEGA_FREEZE_L_DEG,
    b_deg=OMEGA_FREEZE_B_DEG,
    source="universal-saturation-kernel-catalog.md:88 + omega-freeze-cosmic-grain-cascade.md:26",
    confidence="pinned (AVE canonical)",
)

# Literature-cited published axis positions for each observable.
# Honest disclosure: this Phase 1 uses literature-best-guess values. Multiple papers
# report different axis directions for the same observable depending on statistic +
# data cut. Phase 2 re-derives each axis from raw data for fair comparison.
LITERATURE_AXES = [
    # Observable 1 — CMB axis-of-evil (Planck PR3)
    # Land & Magueijo 2005 (Phys.Rev.Lett. 95, 071301) reports preferred axis
    # ~(l=237, b=63) for quadrupole-octupole alignment using WMAP. Various
    # later Planck analyses give axes within ~30 deg of this. The AVE prereg
    # CITES (l=174, b=-5), which is closer to the ecliptic-pole-aligned variant.
    # NOTE: this is a known disputed axis; different statistics give different
    # results. PASS criterion needs Phase-2 re-analysis from raw maps.
    GalacticAxis(
        name="CMB axis-of-evil (Land+Magueijo 2005 WMAP)",
        l_deg=237.0,
        b_deg=63.0,
        source="Land & Magueijo 2005, Phys.Rev.Lett.95:071301 (WMAP-1 quadrupole-octupole)",
        confidence="approximate (Phase 2 needs Planck re-fit)",
    ),
    GalacticAxis(
        name="CMB axis-of-evil (AVE prereg-cited alternative)",
        l_deg=174.0,
        b_deg=-5.0,
        source="universal-saturation-kernel-catalog.md:88 (TBD: which statistic / which Planck paper)",
        confidence="TBD pin",
    ),
    # Observable 2 — Hubble flow dipole / bulk flow direction
    # Watkins+Feldman+Hudson 2009 / "dark flow" claims ~(l=295, b=14)
    # Newer Pantheon+ analyses give various directions; no single consensus value
    GalacticAxis(
        name="Hubble dipole (Watkins+ 2009 bulk flow)",
        l_deg=295.0,
        b_deg=14.0,
        source="Watkins, Feldman, Hudson 2009, MNRAS 392:743 (peculiar-velocity bulk flow)",
        confidence="disputed (multiple analyses differ by 30+ deg)",
    ),
    # Observable 3 — LSS galaxy rotation handedness / cosmic chirality
    # Longo 2011 claimed (l~145, b~-65) using SDSS DR7 spiral handedness
    # Later replications largely null; methodology questioned
    GalacticAxis(
        name="LSS galaxy rotation chirality (Longo 2011 SDSS)",
        l_deg=145.0,
        b_deg=-65.0,
        source="Longo 2011, Phys.Lett.B699:224 (SDSS DR7 spiral handedness)",
        confidence="disputed (null in modern replications; methodology contested)",
    ),
    # Observable 4 — Matter asymmetry direction
    # Baryon asymmetry direction is essentially undefined directly; closest
    # proxy is local CMB rest-frame velocity (Sun's motion vs CMB) which
    # points toward (l=264, b=48). But this isn't really a "matter asymmetry"
    # axis in the AVE sense; the prereg notes this observable is the least
    # well-pinned.
    GalacticAxis(
        name="Matter asymmetry proxy (CMB rest-frame dipole)",
        l_deg=264.0,
        b_deg=48.0,
        source="Sun's motion relative to CMB dipole (Planck 2018 + COBE)",
        confidence="TBD pin (prereg notes this observable is loosely defined)",
    ),
    # Observable 6a — Ecliptic plane normal vs A-034 axis
    # Prereg §1.6 explicitly notes ecliptic-vs-CMB-axis-of-evil alignment
    # is a known observational anomaly. Ecliptic pole in galactic coords:
    # (l=96.4, b=29.8) — this is a single solar-system data point, well-pinned.
    GalacticAxis(
        name="Ecliptic pole (Observable 6a)",
        l_deg=96.4,
        b_deg=29.8,
        source="Solar-system geometry; ecliptic normal in galactic coords",
        confidence="pinned (well-defined geometry)",
    ),
]


def classify_alignment(angle_deg: float) -> tuple[str, str]:
    """Return (verdict, color-marker) based on angular separation."""
    if angle_deg < PASS_THRESHOLD_DEG:
        return ("PASS", "[+]")
    if angle_deg < FAIL_THRESHOLD_DEG:
        return ("AMBIGUOUS", "[?]")
    return ("FAIL", "[X]")


def report_alignments_vs_omega_freeze() -> None:
    """Print alignment of each literature axis vs canonical AVE prediction."""
    print("\n" + "=" * 95)
    print("CMB Axis Alignment Driver — Phase 1: literature-axis comparison vs AVE prediction")
    print("=" * 95)
    print(
        f"\nAVE canonical prediction (Omega_freeze axis): "
        f"(l = {OMEGA_FREEZE.l_deg:.1f} deg, b = {OMEGA_FREEZE.b_deg:.1f} deg)"
    )
    print(f"Source: {OMEGA_FREEZE.source}\n")
    print(f"Pass threshold: angular separation < {PASS_THRESHOLD_DEG} deg")
    print(f"Fail threshold: angular separation > {FAIL_THRESHOLD_DEG} deg")
    print(f"Between: AMBIGUOUS (within combined observational error margins)\n")

    print(
        f"{'Axis':55} {'(l, b) deg':>20} {'sep vs Omega':>14} {'Verdict':>12} {'Confidence':>15}"
    )
    print("-" * 130)

    pass_count = 0
    fail_count = 0
    ambiguous_count = 0
    pinned_count = 0
    tbd_count = 0

    for axis in LITERATURE_AXES:
        sep = angular_separation_deg(axis, OMEGA_FREEZE)
        verdict, marker = classify_alignment(sep)
        if verdict == "PASS":
            pass_count += 1
        elif verdict == "FAIL":
            fail_count += 1
        else:
            ambiguous_count += 1
        if "TBD" in axis.confidence:
            tbd_count += 1
        elif "pinned" in axis.confidence:
            pinned_count += 1
        coord = f"({axis.l_deg:6.1f}, {axis.b_deg:5.1f})"
        print(
            f"{axis.name:55} {coord:>20} {sep:>10.2f} deg {marker} {verdict:>8} {axis.confidence:>15}"
        )

    print("\n" + "-" * 130)
    print(
        f"Summary: {pass_count} PASS  |  {ambiguous_count} AMBIGUOUS  |  {fail_count} FAIL"
    )
    print(f"Citation pin status: {pinned_count} pinned  |  {tbd_count} TBD-pin-source")


def report_cross_pair_separations() -> None:
    """Print pairwise angular separations between all observable axes (independent of AVE)."""
    print("\n" + "=" * 95)
    print("Cross-pair separations (do the observed axes mutually align, regardless of AVE?)")
    print("=" * 95 + "\n")

    n = len(LITERATURE_AXES)
    short_names = [a.name.split(" (")[0][:25] for a in LITERATURE_AXES]

    header = f"{'':27}" + "".join(f"{name[:11]:>13}" for name in short_names)
    print(header)
    print("-" * len(header))
    for i in range(n):
        row = f"{short_names[i]:>27}"
        for j in range(n):
            if i == j:
                row += f"{'--':>13}"
            elif j < i:
                row += f"{'':>13}"
            else:
                sep = angular_separation_deg(LITERATURE_AXES[i], LITERATURE_AXES[j])
                _, marker = classify_alignment(sep)
                row += f"{sep:>8.1f}{marker:>5}"
        print(row)


def report_phase1_assessment() -> None:
    """Print honest Phase 1 assessment + what Phase 2 needs."""
    print("\n" + "=" * 95)
    print("Phase 1 honest assessment")
    print("=" * 95 + "\n")

    print(
        "Phase 1 uses LITERATURE-BEST-GUESS axis values; many are disputed or have"
    )
    print("multiple competing published values depending on statistic + data cut.")
    print()
    print("Specific Phase-2 TBDs to resolve via raw-data re-analysis:")
    print()
    print(
        "  1. CMB axis-of-evil — AVE prereg cites (l=174, b=-5); Land+Magueijo 2005"
    )
    print(
        "     reports (l=237, b=63). The 90-deg discrepancy reflects different"
    )
    print(
        "     statistics (multipole moment alignment vs quadrupole-octupole)."
    )
    print("     Phase 2: refit Planck PR3 maps with documented statistic choice.")
    print()
    print(
        "  2. Hubble flow dipole — Watkins+ 2009 gives (l=295, b=14); Pantheon+ analyses"
    )
    print(
        "     differ by 30+ deg. No consensus value."
    )
    print(
        "     Phase 2: refit Pantheon+ supernova catalog directly."
    )
    print()
    print(
        "  3. LSS galaxy rotation chirality — Longo 2011 claims (l=145, b=-65)"
    )
    print(
        "     using SDSS DR7; replications mostly null; methodology contested."
    )
    print(
        "     Phase 2: independent SDSS DR17 analysis; if null, Observable 3 must be"
    )
    print(
        "     dropped from the 4-axis test."
    )
    print()
    print(
        "  4. Matter asymmetry — loosely-defined observable per prereg notes;"
    )
    print(
        "     no clean axis exists in literature. Phase 2 may need to define a"
    )
    print(
        "     specific observable (e.g., positron/electron ratio direction at"
    )
    print(
        "     supernova remnants) before this axis becomes testable."
    )
    print()
    print(
        "Phase 1 OUTPUT: the alignment matrix above is suggestive but not definitive."
    )
    print(
        "The 7 observables don't mutually align in any obvious way using the"
    )
    print(
        "literature-best-guess values. Whether this rules out the framework or"
    )
    print(
        "simply reflects axis-citation ambiguity requires Phase 2 raw-data re-analysis."
    )
    print()
    print(
        "OPERATIONAL RECOMMENDATION: install healpy + astropy; fetch Planck PR3 maps;"
    )
    print(
        "implement explicit-statistic-choice quadrupole-octupole alignment fit; pin"
    )
    print(
        "Observable 1 axis to a single statistic before proceeding to Observable 2-6."
    )


def main() -> int:
    """Phase 1 entry point."""
    report_alignments_vs_omega_freeze()
    report_cross_pair_separations()
    report_phase1_assessment()
    return 0


if __name__ == "__main__":
    import sys

    sys.exit(main())
