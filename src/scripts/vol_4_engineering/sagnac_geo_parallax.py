"""
Vol 4 Engineering — Sagnac galactic-wind + GEO-sync Shapiro reference baselines.

SCOPE NOTE (2026-05-17 audit): This script computes baseline numerics for two
matrix rows that were retired to corroborative-null status in the 2026-05-16
session. Neither prediction is currently load-bearing as an AVE-distinct forward
test; both retain reference-baseline value for comparing against any future
AVE-distinct derivation that would need to compute residuals above these
baselines.

Protocol 11 (static-fiber galactic-wind Sagnac):
- Script computes naive Fizeau-style (4π L v_gal)/(λ c) phase shift for a 200-m
  fiber loop at v_gal = 370 km/s. Result is large (~1.9 M-rad).
- This is the predicted-magnitude that the C17-PROTOCOL-11-SAGNAC-WIND matrix
  row used to claim as forward AVE-distinct prediction.
- C17 was RETIRED 2026-05-16 (commit 9b2f8d6) to corroborative-null status
  per AVE's own physics:
  (i) Closed-loop Sagnac integral of uniform 370 km/s wind = 0 (basic geometry,
      independent of substrate physics).
  (ii) Any open-loop Fizeau-style drift is cubic-symmetry-suppressed to
       (q*l_node)^4 ~ 10^-22 at optical wavelengths per K4 Fd-3m space group
       (see AVE-QED Q-G24 / lorentz_violation_constraints).
- AVE predicts NULL. Existing Brillet-Hall + Wolf null bounds CORROBORATE AVE.
- The print statement claim of "massive, detectable sinusoidal daily oscillation"
  is unsupported by current corpus state; preserved here only as the naive-Fizeau
  computational baseline for reference.

Protocol 12 (GEO-sync ground-to-GEO laser TOF):
- Script computes Delta_t = 2GM/c^3 * ln(R_geo/R_earth), the standard GR Shapiro
  delay for a ground-to-GEO laser link.
- This is the predicted-magnitude that the C18-PROTOCOL-12-GEO-SYNC matrix row
  used to claim as AVE-extra TOF stretch beyond Shapiro.
- C18 was RETIRED 2026-05-16 (commit 59a88ad) to corroborative-null status:
  AVE's gravitational refractive index n(r) = 1 + 2GM/c^2*r per Vol 3 Ch 3
  refractive-index-of-gravity.md:11 is "mathematically identical to the spatial
  transverse trace of the Gordon optical metric" (line 14) — i.e., the GR
  Shapiro integrand. AVE and GR compute the same TOF at O(GM/c^2 r).
- AVE = GR at this order. No AVE-distinct prediction. The script's output IS
  the standard GR Shapiro value (~17 mm for ground-to-GEO; consistent with
  what LRO/GRACE-FO laser ranging already confirms).
- The print statement claim "proving gravitational LC dispersion" was unsupported
  by the actual computation (pure Shapiro, not AVE-distinct).

Both halves of this script are preserved as Shapiro-baseline / Fizeau-baseline
references for any future AVE-distinct derivation that would need to compute its
prediction as a residual above these GR/standard baselines. See:
- manuscript/ave-kb/common/closure-roadmap.md §0.5 (scope-correction changelog
  for C17 + C18 retirement entries)
- manuscript/ave-kb/common/divergence-test-substrate-map.md (C17 + C18 row
  rewrites with corroborative-null status)
- manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/preferred-frame-
  and-emergent-lorentz.md (cohesive narrative on K4 cubic-symmetry suppression)
"""

import numpy as np

from ave.core.constants import C_0, G


def simulate_sagnac_geo_parallax() -> None:
    print("--- Vol 4 Engineering: Sagnac + GEO-Sync baseline references (NOT AVE-distinct forward predictions) ---")
    print("(NOTE: Both protocols retired to corroborative-null status 2026-05-16.")
    print(" See module docstring + closure-roadmap.md §0.5 for scope corrections.)")

    # 1. Sagnac-Parallax (Galactic Wind Vectoring) — naive Fizeau baseline
    print("\n[Protocol 11: Naive Fizeau baseline for galactic-wind static-fiber Sagnac]")
    print("(C17 retired 2026-05-16: AVE predicts NULL via cubic-symmetry suppression.")
    print(" Naive-Fizeau result below would need ~10^-22 suppression to match AVE.)")
    v_gal = 370e3  # m/s (Earth velocity relative to CMB rest frame)
    L_fiber = 200.0  # m (baseline loop)
    wavelength = 1550e-9  # m (telecom-band laser)

    # Naive Fizeau-style: Delta Phi ~ (4 * pi * L * v) / (lambda * c_0)
    # Does NOT include K4 cubic-symmetry suppression that AVE actually predicts.
    naive_fizeau_rad = (4 * np.pi * L_fiber * v_gal) / (wavelength * C_0)
    print(f"Naive Fizeau magnitude (no cubic-symmetry suppression): {naive_fizeau_rad:.2e} rad")
    ave_predicted_rad = naive_fizeau_rad * 1e-22  # (q*l_node)^4 suppression factor
    print(f"AVE-predicted (with cubic-symmetry suppression ~10^-22): {ave_predicted_rad:.2e} rad")
    print("=> Existing Brillet-Hall + Wolf null bounds CORROBORATE AVE's null prediction.")

    # 2. GEO-Synchronous Impedance Differential — standard GR Shapiro baseline
    print("\n[Protocol 12: Standard GR Shapiro baseline for ground-to-GEO laser TOF]")
    print("(C18 retired 2026-05-16: AVE's n(r) = 1 + 2GM/c^2r is identical to Gordon optical metric;")
    print(" AVE = GR Shapiro at O(GM/c^2 r). No AVE-distinct prediction at this order.)")
    M_earth = 5.972e24  # kg
    R_earth = 6371e3  # m
    H_geo = 35786e3  # m
    R_geo = R_earth + H_geo

    # Standard GR Shapiro delay (AVE n(r) IS this same function per Vol 3 Ch 3):
    # n(r) = 1 + 2GM/(r * c^2)
    # Delta_t = integral from R_earth to R_geo of (n(r) - 1)/c dr
    # Delta_t = 2GM / c^3 * ln(R_geo / R_earth)
    delta_t_s = (2 * G * M_earth) / (C_0**3) * np.log(R_geo / R_earth)
    print(f"GR Shapiro Delay (AVE = GR identical): {delta_t_s * 1e12:.2f} picoseconds")

    path_stretch_mm = delta_t_s * C_0 * 1000.0
    print(f"Path Stretch (GR Shapiro, AVE = GR identical): {path_stretch_mm:.6f} mm")
    print("=> Existing LRO + GRACE-FO + ILRS laser-ranging GR-Shapiro confirmations CORROBORATE AVE = GR identity.")


if __name__ == "__main__":
    simulate_sagnac_geo_parallax()
