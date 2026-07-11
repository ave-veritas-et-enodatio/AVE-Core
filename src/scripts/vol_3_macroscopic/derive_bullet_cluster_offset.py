r"""
Quantitative C13b test -- Bullet-Cluster lensing-peak-vs-gas OFFSET from the (gamma)
ponderomotive substrate-strain halo, by LINEAR SUPERPOSITION of static eta_eff halos.

Governing prereg (FROZEN, untouched): research/2026-05-17_C13b_bullet_cluster_prereg.md
Branch under test: (gamma) -- geometric/ponderomotive eta_eff halo superposition
(Grant-adjudicated 2026-05-17; dm-mechanism-unification.md:54). (alpha)/(beta) are
superseded AND non-fireable (missing source term / propagation eq / dispersion /
dynamic-strain->offset, prereg :78-81); only (gamma) can genuinely fire. See result doc
research/2026-07-11_C13b_bullet_cluster_result.md.

WHAT THIS DRIVER DERIVES (the substrate prediction):
  the location of the gravitational-lensing convergence peak, as the argmax of the LINEAR
  SUPERPOSITION of static ponderomotive substrate-strain halos (leaf bullet-cluster.md:28:
  "The substrate-strain halos LINEARLY SUPERPOSE ... and pass through each other
  ballistically"). Each halo is the AVE eta_eff / Axiom-4 saturation enhancement sourced
  by a baryonic mass concentration; lensing reads the superposed halo through the Gordon
  optical metric (n = 1 - h_perp). The PREDICTED OFFSET is the projected separation between
  that computed peak and the X-ray gas peak. It is a genuine field argmax (NOT a restated
  kinematic input): under different source assignments the peak lands in different places,
  and the P11 sabotage gates below drive it to ~0.

WHAT IS IMPORTED-OBSERVATIONAL (legitimate for an astro comparison, tagged):
  cluster feature POSITIONS (Clowe+ 2006 centroids), baryonic/lensing MASSES, redshift,
  plate scale, cluster core scales, and the empirical ~150 kpc offset ANCHOR the
  prediction is compared against. NOT lattice-derived; the observational geometry the
  prediction runs on. Sources: Clowe+ 2006 (ApJ 648 L109); Paraficz+ 2016 (A&A 594 A121);
  Markevitch 2006; Springel & Farrar 2007 (MNRAS 380 911). Full per-number cites in doc.

WHAT IS LATTICE-DERIVED:
  the halo PROFILE (eta_eff kernel g_eff = g_N + sqrt(g_N a0) sqrt(1 - g_N/a0),
  ave.regime_3_saturated.galactic_rotation.ave_saturation_acceleration; the same kernel
  whose SPARC-validated source is M_disk = M_star + M_gas, multi-galaxy-validation.md:23),
  a0 = A0_LATTICE = c H_inf/(2 pi) (no telescope parameter), the linear-superposition
  prescription (Ax1 + Ax4 linear regime, bullet-cluster.md:28), and G, M_SUN, c, H_inf
  from constants.py. Cross-check profile = static Gordon 1/r halo (h_perp ~ M/r,
  gordon-optical-metric.md:33; boundary-trapping-test.md:15).

KEEP-BOTH source hypotheses (the load-bearing physics fork):
  H_baryon : halo amplitude ~ TOTAL baryonic mass, each component co-moving with its own
             source -- gas halo on the (dominant) gas, star halo on the stars. This is the
             Axiom-2 / eta_eff "mass sources strain" reading. Gas DOMINATES the baryons
             (Clowe abstract: "plasma ... the dominant baryonic mass component").
  H_star   : halo amplitude ~ STELLAR (collisionless) mass only, at the galaxy centroids.
             The leaf's "halo co-moves with stars" reading -- an UNDERIVED assertion
             (auditor 2026-07-11; corpus's own grade vol1/claim-quality.md:480
             "asserted, not derived ... matched-by-construction").

P10: (gamma) fires -- prediction is a computed field argmax, not a kinematic prescription
     (the pre-existing simulate_bullet_cluster_fdtd.py IS a kinematic prescription with no
     gas component -> that one meets the P10 HALT; this driver resolves it via the honest
     two-component gas+star source). P11: sabotage gates below are fireable.
"""

from __future__ import annotations

import numpy as np

from ave.core.constants import C_0, G, H_INFINITY, M_SUN
from ave.regime_3_saturated.galactic_rotation import A0_LATTICE, ave_saturation_acceleration
from ave_path_util import sim_output

# Exact parsec (IAU 2015 B2): 1 pc = 648000/pi AU, 1 AU = 149597870700 m.
KPC = 1e3 * (648000.0 / np.pi) * 149597870700.0  # m
_trapz = getattr(np, "trapezoid", None) or np.trapz  # NumPy 2.0 renamed trapz

# ==========================================================================
# IMPORTED-OBSERVATIONAL INPUTS -- Bullet Cluster 1E 0657-558   (NOT lattice-derived)
# On-sky frame: origin = sub-cluster (bullet) X-ray gas peak; +x = West (bullet travel);
# +y = North. Positions from Clowe+ 2006 centroids (plate scale 4.413 kpc/arcsec). Frame
# validated: main<->sub mass-peak separation 722 kpc vs lit. 720 kpc (Springel-Farrar 2007).
# ==========================================================================
Z_REDSHIFT = 0.296  # [Clowe+ 2006]

POS = {  # (x_kpc, y_kpc)
    "gas_sub":  (0.0,    0.0),      # bullet X-ray gas peak = origin
    "gal_sub":  (193.0, -22.0),     # bullet mass/galaxy (collisionless) peak; 8-sigma lensing
    "gas_main": (-334.0, -26.0),    # main-cluster X-ray gas peak
    "gal_main": (-523.0, -116.0),   # main-cluster mass/galaxy peak; 12-sigma lensing
}
# Baryonic component masses [Msun]. Absolute normalization is irrelevant to the PEAK
# LOCATION (only ratios + positions + core scales matter); we anchor stellar mass at
# ~11% of the R<250 kpc lensing mass (Paraficz+ 2016) and set gas = ratio * stars.
M_STAR = {"sub": 0.11 * 2.0e14, "main": 0.11 * 2.5e14}   # ~2.2e13, ~2.75e13
GAS_STAR_RATIO_DEFAULT = 5.0  # cluster-wide gas-dominant (Clowe abstract); swept below

# Core scales [kpc] (IMPORTED cluster structure; swept). Bullet gas is COMPACT+dense;
# main ICM is EXTENDED (beta-model core theta_c=112.5"~500 kpc, Paraficz); galaxies compact.
RC = {"gas_sub": 80.0, "gas_main": 300.0, "star": 50.0}

# Empirical offset anchor (sub-cluster lensing-vs-gas), IMPORTED-OBSERVATIONAL.
# Canonical ~150 kpc = dense-tip / along-collision-axis (Clowe 2006; JWST 2025). In the
# Clowe gas-CENTROID frame used for POS above, the star-gas separation is 194 kpc. The
# observed offset thus spans ~150-194 kpc depending on the gas fiducial.
OFFSET_OBS_KPC = 150.0
OFFSET_OBS_SIG_KPC = 30.0
OFFSET_INFRAME_KPC = float(np.hypot(*POS["gal_sub"]))  # 194 kpc: star-gas sep in THIS frame

GRID_HALF_KPC = 1100.0
GRID_N = 441  # ~5 kpc pixels


# ==========================================================================
# LATTICE-DERIVED HALO PROFILES  (radial projected surface density of ONE halo)
# ==========================================================================
def eta_eff_surface_density(R_kpc: np.ndarray, mass_msun: float, r_core_kpc: float,
                            saturate: bool = True) -> np.ndarray:
    r"""
    Projected effective LENSING surface density Sigma_eff(R) of one AVE ponderomotive halo:
    a cored baryonic source enhanced by the Axiom-4 eta_eff saturation kernel, projected
    along the line of sight. Convergence kappa \propto Sigma_eff.
      cored baryons  M_enc(r) = M r^3 / (r^2+r_c^2)^{3/2}   (Plummer; finite core)
      g_N(r)         = G M_enc(r)/r^2
      g_eff(r)       = ave_saturation_acceleration(g_N)      (eta_eff kernel, a0=A0_LATTICE)
      M_eff(r)       = g_eff r^2 / G                          (effective lensing mass)
      rho_eff(r)     = (1/4 pi r^2) dM_eff/dr
      Sigma_eff(R)   = 2 int_R^inf rho_eff(r) r/sqrt(r^2-R^2) dr   (Abel projection)

    IMPORTANT (kernel-dormancy, per adversarial review 2026-07-11): across the whole
    peak-assignment region (R < ~230 kpc) the cluster-core Newtonian field has g_N >> a0
    (high-acceleration regime), so the eta_eff kernel returns g_eff/g_N = 1.000 -- it is
    DORMANT and only engages at R >~ 600 kpc outskirts (leaf bullet-cluster.md:28: "cluster-
    scale strains are far below saturation"). The peak LOCATION is therefore set by linear
    superposition of ~Newtonian baryon mass, independent of the saturation kernel and radial
    law. `saturate=False` reproduces this as an explicit Newtonian null (see main()).
    """
    M = mass_msun * M_SUN
    r_c = r_core_kpc * KPC
    r = np.logspace(np.log10(0.03 * r_c), np.log10(80.0 * max(r_c, 200.0 * KPC)), 4000)
    M_enc = M * r**3 / (r**2 + r_c**2) ** 1.5
    g_N = G * M_enc / r**2
    g_eff = ave_saturation_acceleration(g_N, a0=A0_LATTICE) if saturate else g_N
    M_eff = g_eff * r**2 / G
    rho_eff = np.clip(np.gradient(M_eff, r) / (4.0 * np.pi * r**2), 0.0, None)

    R = np.atleast_1d(R_kpc) * KPC
    Sigma = np.empty_like(R, dtype=float)
    for i, RR in enumerate(R):
        rr = r[r > RR]
        integrand = rho_eff[r > RR] * rr / np.sqrt(rr**2 - RR**2)
        Sigma[i] = 2.0 * _trapz(integrand, rr)
    return Sigma


def gordon_pointmass_surface_density(R_kpc: np.ndarray, mass_msun: float, r_core_kpc: float) -> np.ndarray:
    r"""
    Robustness cross-check: static Gordon point-mass halo h_perp ~ M/r (canonical
    gordon-optical-metric.md:33 epsilon_11=7GM/c^2 r; transverse-refractive-index.md:23
    n=1+nu_vac epsilon_11; boundary-trapping-test.md:15 h_perp ~ 1/r). Cored 1/R
    convergence kappa \propto M/sqrt(R^2+r_c^2). Different radial law from eta_eff; used to
    show the PEAK-LOCATION verdict is robust to profile choice.
    """
    R = np.atleast_1d(R_kpc) * KPC
    r_c = r_core_kpc * KPC
    return mass_msun * M_SUN / np.sqrt(R**2 + r_c**2)


# ==========================================================================
# SUPERPOSITION + PEAK-FIND
# ==========================================================================
def superpose_kappa(sources, profile, xs, ys) -> np.ndarray:
    """kappa_total(x,y) = sum_i profile(|(x,y)-r_i|, M_i, rc_i)  -- LINEAR superposition."""
    XX, YY = np.meshgrid(xs, ys)
    kappa = np.zeros_like(XX, dtype=float)
    r_tab = np.linspace(0.0, np.sqrt(2) * 2 * GRID_HALF_KPC, 2400)
    for (x0, y0), mass, rc in sources:
        if mass <= 0:
            continue
        s_tab = profile(np.maximum(r_tab, 1e-3), mass, rc)
        Rk = np.sqrt((XX - x0) ** 2 + (YY - y0) ** 2)
        kappa += np.interp(Rk.ravel(), r_tab, s_tab).reshape(XX.shape)
    return kappa


def local_maxima(kappa, xs, ys, min_frac=0.03):
    """Genuine 2D local maxima (pixel==max of 3x3 nbhd) above min_frac*global_max, val-sorted."""
    from scipy.ndimage import maximum_filter

    mx = maximum_filter(kappa, size=3, mode="nearest")
    ismax = (kappa >= mx) & (kappa > min_frac * float(np.max(kappa)))
    XX, YY = np.meshgrid(xs, ys)
    pts = [(float(XX[j, i]), float(YY[j, i]), float(kappa[j, i])) for j, i in zip(*np.where(ismax))]
    pts.sort(key=lambda p: -p[2])
    return pts


def assign_peak(maxima, center, radius_kpc):
    """Highest-value local max within radius_kpc of center; None if the sub-peak is swallowed."""
    cx, cy = center
    cands = [p for p in maxima if np.hypot(p[0] - cx, p[1] - cy) <= radius_kpc]
    return cands[0] if cands else None


def weighted_centroid(kappa, xs, ys, center, radius_kpc):
    """Convergence-weighted centroid within radius_kpc of center (robustness cross-check)."""
    XX, YY = np.meshgrid(xs, ys)
    cx, cy = center
    w = np.where(np.hypot(XX - cx, YY - cy) <= radius_kpc, kappa, 0.0)
    tot = float(np.sum(w))
    return (float(np.sum(w * XX) / tot), float(np.sum(w * YY) / tot)) if tot > 0 else center


def sources_for(hypothesis, ratio=GAS_STAR_RATIO_DEFAULT, rc=RC):
    star = [(POS["gal_sub"], M_STAR["sub"], rc["star"]),
            (POS["gal_main"], M_STAR["main"], rc["star"])]
    if hypothesis == "H_star":
        return star
    if hypothesis == "H_baryon":
        gas = [(POS["gas_sub"], ratio * M_STAR["sub"], rc["gas_sub"]),
               (POS["gas_main"], ratio * M_STAR["main"], rc["gas_main"])]
        return star + gas
    raise ValueError(hypothesis)


def predicted(sources, profile):
    xs = np.linspace(-GRID_HALF_KPC, GRID_HALF_KPC, GRID_N)
    ys = np.linspace(-GRID_HALF_KPC, GRID_HALF_KPC, GRID_N)
    kappa = superpose_kappa(sources, profile, xs, ys)
    maxima = local_maxima(kappa, xs, ys)
    # sub-cluster peak: search near the sub features (midpoint of gas_sub & gal_sub)
    sub_c = (0.5 * (POS["gas_sub"][0] + POS["gal_sub"][0]),
             0.5 * (POS["gas_sub"][1] + POS["gal_sub"][1]))
    pk_sub = assign_peak(maxima, sub_c, radius_kpc=230.0)
    cen_sub = weighted_centroid(kappa, xs, ys, sub_c, radius_kpc=230.0)
    off_peak = None if pk_sub is None else float(np.hypot(pk_sub[0], pk_sub[1]))  # dist to gas_sub=origin
    off_cen = float(np.hypot(cen_sub[0], cen_sub[1]))
    return {"kappa": kappa, "xs": xs, "ys": ys, "maxima": maxima,
            "peak_sub": (None if pk_sub is None else (pk_sub[0], pk_sub[1])),
            "centroid_sub": cen_sub, "offset_peak_kpc": off_peak, "offset_centroid_kpc": off_cen,
            "n_maxima": len(maxima)}


# ==========================================================================
# MAIN
# ==========================================================================
def main() -> None:
    print("=" * 78)
    print("C13b (gamma) quantitative test -- Bullet-Cluster lensing-vs-gas offset")
    print("linear superposition of static ponderomotive eta_eff halos (Ax2/Ax4, Gordon)")
    print("=" * 78)
    print(f"a0 = A0_LATTICE = c*H_inf/(2pi) = {A0_LATTICE:.6e} m/s^2  [lattice-derived]")
    print(f"  c={C_0:.6e} m/s   H_inf={H_INFINITY:.6e} 1/s   [constants.py]")
    print(f"IMPORTED offset anchor: {OFFSET_OBS_KPC:.0f}+/-{OFFSET_OBS_SIG_KPC:.0f} kpc "
          f"(canonical dense-tip); {OFFSET_INFRAME_KPC:.0f} kpc (star-gas sep in Clowe frame)")
    print(f"geometry: sub star-gas sep = {OFFSET_INFRAME_KPC:.0f} kpc; "
          f"main<->sub mass-peak sep = {np.hypot(POS['gal_main'][0]-POS['gal_sub'][0], POS['gal_main'][1]-POS['gal_sub'][1]):.0f} kpc")
    print()

    results = {}
    for prof_name, profile in [("eta_eff", eta_eff_surface_density),
                               ("gordon_1/r", gordon_pointmass_surface_density)]:
        print(f"--- profile: {prof_name}  (gas/star ratio = {GAS_STAR_RATIO_DEFAULT:.0f}) ---")
        for hyp in ("H_baryon", "H_star"):
            res = predicted(sources_for(hyp), profile)
            results[(prof_name, hyp)] = res
            op = res["offset_peak_kpc"]
            op_s = "SWALLOWED(no distinct sub-peak)" if op is None else f"{op:6.1f} kpc"
            d = None if op is None else op - OFFSET_OBS_KPC
            dd = "" if d is None else f"| Delta(vs150)={d:+6.1f} ({d/OFFSET_OBS_SIG_KPC:+.1f}s)"
            print(f"  {hyp:9s}: peak-offset={op_s:>18s}  centroid-offset={res['offset_centroid_kpc']:6.1f} kpc "
                  f"| n_max={res['n_maxima']} {dd}")
        print()

    # ---- robustness: gas/star ratio sweep (eta_eff) ----
    print("--- robustness: predicted sub-offset (kpc, eta_eff) vs gas/star ratio ---")
    print("  gas/star |  H_baryon peak  H_baryon centroid |  (H_star peak = %.0f, centroid = %.0f)"
          % (results[("eta_eff", "H_star")]["offset_peak_kpc"] or -1,
             results[("eta_eff", "H_star")]["offset_centroid_kpc"]))
    for ratio in (0.8, 2.0, 3.0, 5.0, 7.0):
        rb = predicted(sources_for("H_baryon", ratio=ratio), eta_eff_surface_density)
        pk = "SWALLOWED" if rb["offset_peak_kpc"] is None else f"{rb['offset_peak_kpc']:6.1f}"
        print(f"  {ratio:7.1f}  |  {pk:>13s}  {rb['offset_centroid_kpc']:15.1f} |")
    print("  (ratio 0.8 = stripped-core census; 5-7 = cluster-wide gas-dominant [Clowe abstract])")
    print()

    # ---- kernel-dormancy probe + Newtonian null (per adversarial review 2026-07-11) ----
    # The eta_eff kernel is DORMANT where the peak is set: g_N >> a0 in the cluster core, so
    # g_eff/g_N = 1.000 until the far outskirts. Hence the MISS is a linear-superposition-of-
    # baryons result, INDEPENDENT of the saturation kernel and radial law.
    print("--- kernel dormancy: g_eff/g_N for a 1e14 Msun source (rc=80 kpc) ---")
    Msrc = 1e14 * M_SUN
    rc = 80.0 * KPC
    for R in (10.0, 50.0, 150.0, 230.0, 600.0, 1000.0):
        r = R * KPC
        M_enc = Msrc * r**3 / (r**2 + rc**2) ** 1.5   # Plummer enclosed mass
        gN = G * M_enc / r**2
        ratio = float(ave_saturation_acceleration(gN, a0=A0_LATTICE)) / gN
        tag = "DORMANT" if ratio < 1.01 else "engaged"
        print(f"   R={R:6.0f} kpc: g_N/a0={gN/A0_LATTICE:9.2f}  g_eff/g_N={ratio:6.3f}  ({tag})")
    print("--- Newtonian null (saturation DISABLED, g_eff=g_N): verdict must be identical ---")

    def _newt(R, m, rc):
        return eta_eff_surface_density(R, m, rc, saturate=False)

    for hyp in ("H_baryon", "H_star"):
        n = predicted(sources_for(hyp), _newt)
        e = results[("eta_eff", hyp)]
        print(f"   {hyp:9s}: Newtonian peak-offset={n['offset_peak_kpc']:.1f} kpc  "
              f"vs eta_eff {e['offset_peak_kpc']:.1f} kpc  -> "
              f"{'IDENTICAL' if abs((n['offset_peak_kpc'] or -1)-(e['offset_peak_kpc'] or -1))<10 else 'DIFFERS'} "
              f"(kernel-independent)")
    print()

    _sabotage(results)
    _make_figure(results)


def _sabotage(results):
    print("=" * 78)
    print("P11 SABOTAGE (planted-violation proofs; each must MOVE the prediction)")
    print("=" * 78)
    base_off = results[("eta_eff", "H_baryon")]["offset_peak_kpc"]  # peak = the Clowe observable

    # [A] zero the GAS-halo amplitude -> only stellar halos remain -> peak-offset must JUMP
    #     to the H_star value, proving the gas amplitude is what drags the peak onto the gas.
    star_only = [(POS["gal_sub"], M_STAR["sub"], RC["star"]),
                 (POS["gal_main"], M_STAR["main"], RC["star"])]
    a = predicted(star_only, eta_eff_surface_density)["offset_peak_kpc"]
    print(f"[A] zero gas-halo amplitude (M_gas->0): peak-offset {base_off:.1f} -> {a:.1f} kpc "
          f"(jumps up: gas caused the low offset)")
    assert a is not None and (a - base_off) > 40.0, "SABOTAGE-A FAILED: offset insensitive to gas"

    # [B] move the stellar halos ONTO the gas peaks -> peak-offset must collapse ~0,
    #     proving the offset is read from geometry via the field, not hardcoded to 150/194.
    on_gas = [(POS["gas_sub"], M_STAR["sub"], RC["star"]),
              (POS["gas_main"], M_STAR["main"], RC["star"])]
    b = predicted(on_gas, eta_eff_surface_density)["offset_peak_kpc"]
    print(f"[B] stars moved onto gas peaks: H_star peak-offset "
          f"{results[('eta_eff','H_star')]['offset_peak_kpc']:.1f} -> {b:.1f} kpc (collapses ~0)")
    assert b is not None and b < 25.0, "SABOTAGE-B FAILED: offset not read from geometry"

    # [C] zero ALL amplitudes -> no field.
    kap_c = superpose_kappa([(POS["gal_sub"], 0.0, RC["star"])],
                            eta_eff_surface_density,
                            np.linspace(-GRID_HALF_KPC, GRID_HALF_KPC, GRID_N),
                            np.linspace(-GRID_HALF_KPC, GRID_HALF_KPC, GRID_N))
    print(f"[C] zero ALL halo amplitudes: max(kappa)={np.max(kap_c):.3e} (must be 0)")
    assert np.max(kap_c) == 0.0, "SABOTAGE-C FAILED: field nonzero with zero source"
    print("P11: all sabotage gates fire (prediction is a genuine function of halo physics).\n")


def _make_figure(results):
    import matplotlib.pyplot as plt

    fig, axes = plt.subplots(1, 2, figsize=(13.5, 5.4), sharex=True, sharey=True)
    for ax, hyp, title in zip(
        axes, ("H_baryon", "H_star"),
        (f"H_baryon: halo ~ total baryons (gas/star={GAS_STAR_RATIO_DEFAULT:.0f})\n"
         "[Axiom-2 / eta_eff mass-sources-strain reading]",
         "H_star: halo ~ stellar mass only\n[leaf 'co-moves with stars' -- underived assertion]"),
    ):
        res = results[("eta_eff", hyp)]
        xs, ys, kappa = res["xs"], res["ys"], res["kappa"]
        im = ax.pcolormesh(xs, ys, kappa / np.max(kappa), shading="auto", cmap="magma")
        ax.plot(POS["gas_sub"][0], POS["gas_sub"][1], "c^", ms=12, label="X-ray gas peaks")
        ax.plot(POS["gas_main"][0], POS["gas_main"][1], "c^", ms=12)
        ax.plot(POS["gal_sub"][0], POS["gal_sub"][1], "o", mfc="none", mec="white", ms=9,
                label="galaxy (collisionless) = OBSERVED lensing peaks")
        ax.plot(POS["gal_main"][0], POS["gal_main"][1], "o", mfc="none", mec="white", ms=9)
        if res["peak_sub"] is not None:
            ax.plot(res["peak_sub"][0], res["peak_sub"][1], "x", color="lime", ms=14, mew=3,
                    label="AVE predicted lensing peak (sub)")
        ax.plot(res["centroid_sub"][0], res["centroid_sub"][1], "+", color="deepskyblue",
                ms=14, mew=2.5, label="AVE predicted centroid (sub)")
        off = res["offset_peak_kpc"]
        offs = "swallowed" if off is None else f"{off:.0f} kpc"
        ax.set_title(f"{title}\npred sub-offset (peak)={offs}; (centroid)={res['offset_centroid_kpc']:.0f} kpc "
                     f"| obs {OFFSET_OBS_KPC:.0f}-{OFFSET_INFRAME_KPC:.0f}", fontsize=8.5)
        ax.set_xlabel("collision axis  x [kpc]  (West ->)")
        ax.set_aspect("equal")
        ax.set_xlim(-750, 350)
        ax.set_ylim(-350, 300)
    axes[0].set_ylabel("y [kpc]  (North ->)")
    axes[0].legend(loc="lower left", fontsize=6.5, framealpha=0.7)
    fig.suptitle("C13b (gamma): lensing peak from LINEAR SUPERPOSITION of eta_eff halos "
                 "(normalized convergence)\nH_baryon peak sits on the gas (MISS); "
                 "only H_star (underived) recovers the offset", fontsize=10)
    fig.tight_layout()
    out = sim_output("bullet_cluster_offset_gamma.png")
    fig.savefig(out, dpi=170, bbox_inches="tight")
    print(f"figure -> {out}")


if __name__ == "__main__":
    main()
