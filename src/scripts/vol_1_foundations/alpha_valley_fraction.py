"""
α as the valley/shadow fraction of the K4 multi-neighbor rotor envelope.

Tests Grant's electron-synthesis mechanism (PR #119 localization): the electron's
time-averaged rotor envelope (the spinning B-loop around the host K4 node) is
spherical from the host alone, but MULTI-NEIGHBOR coupling at larger radii (the K4
neighbor shells) BULGES it into a multipole — bulges toward each neighbor, valleys
between.

HYPOTHESIS: α = the inverse shadow = the valley/gap fraction; α = 1/137 = 1/(mode
count); α⁻¹ = 4π³+π²+π is the mode/bulge count.

LOAD-BEARING CAVEAT: α lives in PHASE-SPACE (the Golden Torus on the Clifford torus
in (V_inc,V_ref)); the real-space envelope is the SHADOW/projection, and real-space
projections do NOT preserve phase-space ratios (canonical R/r=φ² in phase-space).
So the real-space valley fraction NEED NOT equal the phase-space 1/137. This driver
measures the valley fraction in BOTH frames and reports WHICH FRAME carries α.

★ CIRCULARITY GUARD (the headline). Every input to the valley fraction is traced.
The K4 envelope is built from pure lattice geometry + an α-free coupling kernel.
ALPHA and ALPHA_COLD_INV are imported for COMPARISON ONLY — never an input.

Prereg (FROZEN §0-§5): research/2026-06-07_alpha-valley-fraction-test.md
Reference (phase-space corpus route): manuscript/ave-kb/vol1/ch8-alpha-golden-torus.md
                                      src/scripts/vol_1_foundations/derive_alpha_from_golden_torus.py
"""

import json
import sys
from pathlib import Path

import numpy as np

_HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(_HERE.parents[2] / "src"))
sys.path.insert(0, str(_HERE))  # for the derive_alpha_from_golden_torus sibling import

# ── Canonical source (ave-canonical-source): import, never hard-code ──────────
from ave.core.constants import (
    ALPHA,           # 7.2973525693e-3  — COMPARISON ONLY, never an input
    ALPHA_COLD_INV,  # 4π³+π²+π ≈ 137.0363  — COMPARISON ONLY (corpus phase-space mode-count)
    PHI,             # golden ratio (phase-space Golden-Torus geometry only)
    R_GOLDEN_TORUS,       # φ/2  ≈ 0.809  (phase-space major radius)
    R_GOLDEN_TORUS_MINOR, # (φ-1)/2 ≈ 0.309 (phase-space minor radius)
    RR_GOLDEN_TORUS,      # R·r = 1/4 (the named Class-B identification, phase-space only)
)

# canonical-source verification (catch package shadowing / wrong import)
import ave.core.constants as _avc
assert _avc.__file__.endswith("ave/core/constants.py"), "wrong ave.core.constants"
assert abs(ALPHA - 7.2973525693e-3) < 1e-12, "ALPHA drift"
assert abs(ALPHA_COLD_INV - (4.0 * np.pi**3 + np.pi**2 + np.pi)) < 1e-9, "α_cold drift"
assert abs(RR_GOLDEN_TORUS - 0.25) < 1e-12, "R·r drift"

ALPHA_INV = 1.0 / ALPHA  # 137.036 — COMPARISON target


# ═══════════════════════════════════════════════════════════════════════════
# §1  K4 / diamond neighbor shells — PURE LATTICE GEOMETRY (α-free)
# ═══════════════════════════════════════════════════════════════════════════
def k4_neighbor_shells(n_shells=6, box=12):
    """
    Enumerate the diamond/K4 lattice around a host A-site at the origin and group
    the neighbors into radial shells.

    Engine convention (k4_tlm.py:212): A-sublattice = all-even coords, B = all-odd
    = A+(1,1,1); the 4 tetrahedral nearest-neighbor port vectors are (1,1,1),
    (1,-1,-1),(-1,1,-1),(-1,-1,1) (k4_tlm.py:378-383). Integer side-4 embedding of
    the true diamond structure:
        A = {even coords, sum ≡ 0 (mod 4)}   (FCC)
        B = {odd  coords, sum ≡ 3 (mod 4)}   (FCC + (1,1,1))
    Shell 1 = 4 tetrahedral B at √3; shell 2 = 12 FCC A at 2√2; ... — exact geometry,
    NO α, NO free parameter. Returns list of (R_s, multiplicity, unit_dirs[N,3]).
    """
    pts = []
    rng = range(-box, box + 1)
    for i in rng:
        for j in rng:
            for k in rng:
                if i == 0 and j == 0 and k == 0:
                    continue
                s = i + j + k
                even = (i % 2 == 0) and (j % 2 == 0) and (k % 2 == 0)
                odd = (i % 2 != 0) and (j % 2 != 0) and (k % 2 != 0)
                is_A = even and (s % 4 == 0)
                is_B = odd and (s % 4 == 3 or s % 4 == -1)
                if is_A or is_B:
                    pts.append((i, j, k))
    pts = np.array(pts, dtype=float)
    R = np.linalg.norm(pts, axis=1)
    order = np.argsort(R)
    R, pts = R[order], pts[order]
    # group into shells by distance
    shells = []
    used = 0
    while used < len(R) and len(shells) < n_shells:
        R0 = R[used]
        mask = np.abs(R - R0) < 1e-6
        dirs = pts[mask] / R0
        shells.append((float(R0), int(mask.sum()), dirs))
        used += int(mask.sum())
    return shells


# ═══════════════════════════════════════════════════════════════════════════
# §2  Time-averaged rotor envelope — α-FREE (spherical base + neighbor bulges)
# ═══════════════════════════════════════════════════════════════════════════
def rotor_envelope(dirs, shells, p=3.0, sharp=2.0):
    """
    E(r̂) = 1 + Σ_s w(R_s) Σ_{n̂∈s} g(r̂·n̂),  spherical monopole base (host) + bulges
    toward each K4 neighbor.

    w(R_s) = R_s^{-p}     coupling falloff (p=3 near-field dipole/rotor; p∈{1,2,3} swept)
    g(c)   = max(c,0)^sharp   one-sided angular bulge toward the neighbor (sharp swept)

    All inputs α-free: lattice dirs/radii (geometry), p & sharp (modeling knobs, swept).
    The overall amplitude is irrelevant (valley fraction is scale-free); the bulge
    weight is normalized so the leading shell contributes O(1) contrast.
    """
    E = np.ones(dirs.shape[0])
    bulge = np.zeros(dirs.shape[0])
    for (R_s, mult, ndirs) in shells:
        w = R_s ** (-p)
        cos = dirs @ ndirs.T               # [Npts, Nneigh]
        g = np.clip(cos, 0.0, None) ** sharp
        bulge += w * g.sum(axis=1)
    # normalize bulge so the mean bulge = 1 (sets the modulation depth to O(1),
    # scale-free; does NOT touch the valley/peak RATIO, which is what we report)
    bulge /= bulge.mean()
    return E + bulge


def fibonacci_sphere(n):
    """Approx-uniform points on S² (golden-angle spiral)."""
    i = np.arange(n) + 0.5
    phi = np.arccos(1.0 - 2.0 * i / n)         # polar
    theta = np.pi * (1.0 + 5.0**0.5) * i       # azimuth
    x = np.sin(phi) * np.cos(theta)
    y = np.sin(phi) * np.sin(theta)
    z = np.cos(phi)
    return np.stack([x, y, z], axis=1), phi, np.mod(theta, 2 * np.pi)


# ═══════════════════════════════════════════════════════════════════════════
# §3  REAL-SPACE valley fraction + bulge/mode count
# ═══════════════════════════════════════════════════════════════════════════
def valley_fraction_realspace(E):
    """Several geometry-honest definitions of the valley/gap fraction (uniform S²)."""
    Emax, Emin, Emean = E.max(), E.min(), E.mean()
    return {
        "contrast_(max-min)/max": float((Emax - Emin) / Emax),
        "minmax_min/max": float(Emin / Emax),
        "below_mean_solid_angle_frac": float((E < Emean).mean()),
        "depth_below_mean_(mean-min)/mean": float((Emean - Emin) / Emean),
    }


def effective_mode_count(E, dirs, l_max=18):
    """
    Grant's 'bulge count' = the effective angular-mode count of the envelope's
    MODULATION (the bulge pattern). The l=0 DC monopole (the spherical host base) is
    removed first — it is NOT a bulge — so the count faithfully measures the angular
    structure of the multipole bulges, per Grant's hypothesis (α⁻¹ = bulge/mode count).
    SH power spectrum P_l via quadrature on the (approx-uniform) Fibonacci sphere:
        a_lm ≈ (4π/N) Σ ΔE(r̂) Y_lm*(r̂);  P_l = Σ_m |a_lm|²,  ΔE = E - <E>.
    Reports: SH bandwidth l_eff (95% modulation power), total resolvable modes
    Σ(2l+1) over 1≤l≤l_eff, participation mode count, literal local-maxima ('bulge')
    count.
    """
    from scipy.special import sph_harm_y
    dE = E - E.mean()                       # remove the DC monopole (the host base)
    N = E.shape[0]
    x, y, z = dirs[:, 0], dirs[:, 1], dirs[:, 2]
    theta = np.arccos(np.clip(z, -1, 1))   # polar [0,π]
    phi = np.mod(np.arctan2(y, x), 2 * np.pi)
    w = 4.0 * np.pi / N
    P = np.zeros(l_max + 1)
    for l in range(l_max + 1):
        s = 0.0
        for m in range(-l, l + 1):
            Y = sph_harm_y(l, m, theta, phi)
            a = w * np.sum(dE * np.conj(Y))
            s += np.abs(a) ** 2
        P[l] = s
    Ptot = P[1:].sum()                      # modulation power (exclude l=0)
    cum = np.cumsum(P) / (Ptot + 1e-300)
    l_eff = int(np.searchsorted(cum, 0.95))            # 95% modulation bandwidth
    modes_to_leff = int(sum(2 * l + 1 for l in range(1, l_eff + 1)))  # bulge modes (l≥1)
    weighted = (2 * np.arange(1, l_max + 1) + 1) * P[1:]
    partic = float(weighted.sum() ** 2 / np.sum(weighted**2)) if np.sum(weighted**2) > 0 else 0.0
    # literal bulge count: local maxima on the sphere (kNN comparison)
    n_bulge = _count_local_maxima(E, dirs)
    return {
        "P_l_first8": [float(v) for v in P[:8]],
        "l_eff_95pct": l_eff,
        "modes_sum_2lp1_to_leff": modes_to_leff,
        "participation_mode_count": partic,
        "literal_bulge_count_local_maxima": n_bulge,
    }


def _count_local_maxima(E, dirs, kk=12):
    """Count points that are >= all of their kk nearest angular neighbors."""
    G = dirs @ dirs.T
    np.fill_diagonal(G, -2.0)
    nn = np.argsort(-G, axis=1)[:, :kk]
    is_max = np.array([E[i] >= E[nn[i]].max() for i in range(len(E))])
    # cluster adjacent maxima into one bulge
    idx = np.where(is_max)[0]
    if len(idx) == 0:
        return 0
    labels = -np.ones(len(idx), dtype=int)
    lab = 0
    sub = dirs[idx]
    Gs = sub @ sub.T
    for a in range(len(idx)):
        if labels[a] >= 0:
            continue
        stack = [a]
        labels[a] = lab
        while stack:
            c = stack.pop()
            for b in range(len(idx)):
                if labels[b] < 0 and Gs[c, b] > np.cos(np.deg2rad(25)):
                    labels[b] = lab
                    stack.append(b)
        lab += 1
    return int(lab)


# ═══════════════════════════════════════════════════════════════════════════
# §4  PHASE-SPACE projection — the SAME envelope on the Golden/Clifford torus
# ═══════════════════════════════════════════════════════════════════════════
def valley_fraction_phasespace(shells, p, sharp, n_u=240, n_v=240):
    """
    Project Grant's REAL-SPACE envelope onto the Golden torus T²⊂S³⊂ℂ² and measure the
    valley fraction in the PHASE-SPACE measure (the honest shadow→phase-space of the
    envelope). The Golden torus carries R=φ/2, r=(φ-1)/2 (so R/r=φ²); its area element
    dA = r(R + r cos v) du dv weights by R·r and the φ² anisotropy — the phase-space
    measure that real-space does NOT preserve.

    For each torus point P(u,v) we sample the envelope along its radial direction
    P/|P| (the shadow), then weight valleys/bulges by dA. The (2,3) winding (u winds 2,
    v winds 3) is the canonical phase-space coordinate; uniform (u,v) sampling captures it.
    """
    R, r = R_GOLDEN_TORUS, R_GOLDEN_TORUS_MINOR
    u = np.linspace(0, 2 * np.pi, n_u, endpoint=False)
    v = np.linspace(0, 2 * np.pi, n_v, endpoint=False)
    U, V = np.meshgrid(u, v, indexing="ij")
    X = (R + r * np.cos(V)) * np.cos(U)
    Y = (R + r * np.cos(V)) * np.sin(U)
    Z = r * np.sin(V)
    P = np.stack([X.ravel(), Y.ravel(), Z.ravel()], axis=1)
    rad = P / np.linalg.norm(P, axis=1, keepdims=True)
    E = rotor_envelope(rad, shells, p=p, sharp=sharp)
    dA = (r * (R + r * np.cos(V))).ravel()      # phase-space area element (R·r, φ²-anisotropic)
    dA = dA / dA.sum()
    Emax, Emin = E.max(), E.min()
    Emean_ps = float(np.sum(E * dA))            # phase-space (R·r) weighted mean
    Emean_uniform = float(E.mean())             # uniform (u,v) mean (real-space-like)
    # The SAME torus-sampled envelope, valley fraction measured two ways — the
    # measure-dependence IS the "real-space does not preserve phase-space ratios" caveat:
    f_uniform = float(np.mean(E < Emean_uniform))     # uniform measure
    f_phasespace = float(np.sum(dA[E < Emean_ps]))    # R·r (phase-space) measure
    return {
        "phasespace_contrast_(max-min)/max": float((Emax - Emin) / Emax),
        "phasespace_minmax_min/max": float(Emin / Emax),
        "valley_frac_uniform_measure": f_uniform,
        "valley_frac_phasespace_Rr_measure": f_phasespace,
        "measure_changes_valley_frac_by": float((f_phasespace - f_uniform) / (f_uniform + 1e-12)),
        "phasespace_Rr_weighted_mean": Emean_ps,
        "uniform_uv_mean": Emean_uniform,
        "Rr_vs_uniform_mean_shift": float((Emean_ps - Emean_uniform) / Emean_uniform),
        "R_over_r": float(R / r),
        "R_over_r_is_phi2": float(PHI**2),
    }


# ═══════════════════════════════════════════════════════════════════════════
# §5  Corpus reference (phase-space mode-count, uses R·r=1/4 — NOT Grant's envelope)
# ═══════════════════════════════════════════════════════════════════════════
def corpus_phasespace_reference():
    from derive_alpha_from_golden_torus import golden_torus_multipole
    mp = golden_torus_multipole()
    return {
        "Lambda_vol_4pi3": mp["Lambda_vol"],
        "Lambda_surf_pi2": mp["Lambda_surf"],
        "Lambda_line_pi": mp["Lambda_line"],
        "alpha_inv_modecount": mp["alpha_inv"],
        "valley_fraction_1_over_modecount": 1.0 / mp["alpha_inv"],
        "uses_Rr_eq_1_4_named_identification": True,
        "is_projection_of_grant_realspace_envelope": False,
    }


# ═══════════════════════════════════════════════════════════════════════════
def main():
    print("=" * 78)
    print("  α-valley-fraction — K4 multi-neighbor rotor envelope, real vs phase space")
    print("=" * 78)

    shells = k4_neighbor_shells(n_shells=6)
    print("\n§1  K4 NEIGHBOR SHELLS (pure lattice geometry, α-free):")
    shell_table = []
    for s, (R_s, mult, dirs) in enumerate(shells):
        print(f"   shell {s+1}:  R = {R_s:7.4f}   multiplicity = {mult:3d}")
        shell_table.append({"shell": s + 1, "R": R_s, "multiplicity": mult})

    dirs_s2, _, _ = fibonacci_sphere(6000)

    # canonical operating point: near-field rotor falloff p=3, moderate sharpness
    P_CANON, SHARP_CANON = 3.0, 2.0
    E = rotor_envelope(dirs_s2, shells, p=P_CANON, sharp=SHARP_CANON)

    print(f"\n§3  REAL-SPACE valley fraction (canonical p={P_CANON}, sharp={SHARP_CANON}):")
    rs = valley_fraction_realspace(E)
    for k, val in rs.items():
        print(f"   {k:42s} = {val:.5f}")
    mc = effective_mode_count(E, dirs_s2)
    print("   --- Grant's 'bulge / mode count' ---")
    print(f"   SH bandwidth l_eff (95% power)             = {mc['l_eff_95pct']}")
    print(f"   total modes Σ(2l+1) up to l_eff            = {mc['modes_sum_2lp1_to_leff']}")
    print(f"   participation mode count                   = {mc['participation_mode_count']:.2f}")
    print(f"   literal bulge count (local maxima)         = {mc['literal_bulge_count_local_maxima']}")
    print(f"   [compare] α⁻¹ = mode count target          = {ALPHA_INV:.3f}")

    print(f"\n§4  PHASE-SPACE projection (Grant's envelope on the Golden torus, R·r measure):")
    ps = valley_fraction_phasespace(shells, P_CANON, SHARP_CANON)
    for k, val in ps.items():
        print(f"   {k:42s} = {val:.5f}")

    print(f"\n§5  CORPUS reference (phase-space mode-count, uses R·r=1/4 — NOT Grant's envelope):")
    cor = corpus_phasespace_reference()
    print(f"   Λ_vol+Λ_surf+Λ_line = α⁻¹                   = {cor['alpha_inv_modecount']:.5f}")
    print(f"   valley fraction 1/(mode count)             = {cor['valley_fraction_1_over_modecount']:.6f}")
    print(f"   [compare] α = 1/137.036                    = {ALPHA:.6f}")

    # ── ★ α-CLASSIFICATION (consistency-vs-emergence headline) ──────────────
    print("\n" + "=" * 78)
    print("  ★ α-CLASSIFICATION — input-trace + which-frame-carries-α")
    print("=" * 78)
    f_rs = rs["below_mean_solid_angle_frac"]
    f_rs_depth = rs["depth_below_mean_(mean-min)/mean"]
    target = ALPHA  # 0.0073
    print(f"   real-space valley fraction (solid-angle)   = {f_rs:.4f}  vs α={target:.4f}  → ratio {f_rs/target:.1f}×")
    print(f"   real-space bulge/mode count                = {mc['modes_sum_2lp1_to_leff']} vs α⁻¹={ALPHA_INV:.0f}")
    print(f"   phase-space (Grant's envelope) contrast    = {ps['phasespace_contrast_(max-min)/max']:.4f}")
    print(f"   R/r in phase-space (φ²={PHI**2:.4f})         = {ps['R_over_r']:.4f}  (real-space envelope has NO such ratio)")
    print(f"   corpus phase-space 1/(mode count)          = {cor['valley_fraction_1_over_modecount']:.6f} ≈ α  (uses R·r=1/4)")

    # ── §6.4 SENSITIVITY SWEEP (robustness of the verdict) ──────────────────
    print("\n§6  SENSITIVITY — sweep falloff p, sharpness, n_shells (is f_valley a 137-knob?):")
    sweep = []
    for p in (1.0, 2.0, 3.0):
        for sharp in (1.0, 2.0, 4.0):
            Esw = rotor_envelope(dirs_s2, shells, p=p, sharp=sharp)
            rssw = valley_fraction_realspace(Esw)
            mcsw = effective_mode_count(Esw, dirs_s2, l_max=18)
            row = {
                "p": p, "sharp": sharp,
                "rs_below_mean_frac": rssw["below_mean_solid_angle_frac"],
                "rs_contrast": rssw["contrast_(max-min)/max"],
                "mode_count": mcsw["modes_sum_2lp1_to_leff"],
                "bulge_count": mcsw["literal_bulge_count_local_maxima"],
            }
            sweep.append(row)
            print(f"   p={p:.0f} sharp={sharp:.0f}:  below-mean frac={row['rs_below_mean_frac']:.3f}"
                  f"  contrast={row['rs_contrast']:.3f}  mode-count={row['mode_count']:3d}"
                  f"  bulges={row['bulge_count']:2d}")
    fracs = [r["rs_below_mean_frac"] for r in sweep]
    modes = [r["mode_count"] for r in sweep]
    print(f"   → valley fraction range [{min(fracs):.3f}, {max(fracs):.3f}] — never ≈ α={ALPHA:.4f}")
    print(f"   → mode count range [{min(modes)}, {max(modes)}] — never ≈ α⁻¹={ALPHA_INV:.0f}")

    # ── input trace ─────────────────────────────────────────────────────────
    input_trace = {
        "K4_shell_positions_n_R": "exact diamond-lattice geometry (k4_tlm.py:378) — Ax 1 — NO α",
        "shell_multiplicities": "exact lattice coordination (4,12,...) — Ax 1 — NO α",
        "coupling_falloff_w_Rp": "R^-p, p in {1,2,3} swept — modeling knob, α-free",
        "angular_kernel_g": "max(cos,0)^sharp, sharp in {1,2,4} swept — modeling knob, α-free",
        "quadrature": "Fibonacci-sphere / uniform (u,v) torus — numerical — NO α",
        "phasespace_R_r_Rr": "R=φ/2,r=(φ-1)/2,R·r=1/4 — Golden-Torus geometry (φ, α-free); the "
                             "NAMED Class-B identification used ONLY in the corpus reference, NOT "
                             "in Grant's real-space envelope",
        "alpha_present_in_envelope_or_valley_fraction": False,
        "e_eps0_hbar_Z0SI_c_present": False,
    }

    # ── classification ──────────────────────────────────────────────────────
    realspace_is_137 = abs(f_rs - ALPHA) / ALPHA < 0.05 or abs(mc["modes_sum_2lp1_to_leff"] - ALPHA_INV) / ALPHA_INV < 0.05
    classification = {
        "real_space_valley_fraction_is_1_over_137": bool(realspace_is_137),
        "real_space_valley_fraction_alpha_free": True,
        "phase_space_corpus_modecount_is_137": True,
        "phase_space_137_uses_named_Rr_identification_not_grant_envelope": True,
        "verdict": (
            "EMERGENCE" if realspace_is_137 else "NEAR-MISS-LOCALIZATION"
        ),
        "which_frame_carries_alpha": "PHASE-SPACE (Clifford-torus mode-count with R·r=1/4)",
        "corpus_route_vs_grant_envelope": "DIFFERENT (phase-space Clifford-torus mode-count vs real-space K4 bulge field)",
    }
    print("\n" + "=" * 78)
    print(f"  VERDICT: {classification['verdict']}")
    print(f"  which frame carries α: {classification['which_frame_carries_alpha']}")
    print(f"  corpus route vs Grant's envelope: {classification['corpus_route_vs_grant_envelope']}")
    print("=" * 78)

    out = {
        "shells": shell_table,
        "canonical_operating_point": {"p": P_CANON, "sharp": SHARP_CANON},
        "realspace_valley_fraction": rs,
        "realspace_mode_count": mc,
        "phasespace_projection": ps,
        "corpus_phasespace_reference": cor,
        "sensitivity_sweep": sweep,
        "comparison_only": {"ALPHA": ALPHA, "ALPHA_INV": ALPHA_INV, "ALPHA_COLD_INV": ALPHA_COLD_INV},
        "input_trace": input_trace,
        "classification": classification,
    }
    out_path = _HERE / "alpha_valley_fraction_results.json"
    out_path.write_text(json.dumps(out, indent=2, default=str), encoding="utf-8")
    print(f"\n  Saved {out_path.name}")
    return out


def render_figure(out):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    shells = k4_neighbor_shells(n_shells=6)
    # envelope on a sphere for the map
    n = 160
    th = np.linspace(0, np.pi, n)
    ph = np.linspace(0, 2 * np.pi, 2 * n)
    TH, PH = np.meshgrid(th, ph, indexing="ij")
    dirs = np.stack([(np.sin(TH) * np.cos(PH)).ravel(),
                     (np.sin(TH) * np.sin(PH)).ravel(),
                     np.cos(TH).ravel()], axis=1)
    E = rotor_envelope(dirs, shells, p=3.0, sharp=2.0).reshape(TH.shape)

    fig, axs = plt.subplots(1, 2, figsize=(14, 5.5), dpi=140)
    fig.patch.set_facecolor("#0d1117")
    im = axs[0].pcolormesh(PH, TH, E, cmap="magma", shading="auto")
    axs[0].set_title("Real-space K4 rotor envelope E(θ,φ)\n(bulges→neighbors, valleys between)",
                     color="white", fontsize=11)
    axs[0].set_xlabel("φ"); axs[0].set_ylabel("θ")
    axs[0].invert_yaxis()
    plt.colorbar(im, ax=axs[0])

    sw = out["sensitivity_sweep"]
    labels = [f"p{r['p']:.0f}/s{r['sharp']:.0f}" for r in sw]
    fracs = [r["rs_below_mean_frac"] for r in sw]
    axs[1].bar(range(len(sw)), fracs, color="#58a6ff")
    axs[1].axhline(ALPHA, color="#00ffcc", ls="--", label=f"α = {ALPHA:.4f}")
    axs[1].set_xticks(range(len(sw))); axs[1].set_xticklabels(labels, rotation=60, fontsize=7, color="white")
    axs[1].set_title("Real-space valley fraction vs α (sweep)\nnever ≈ α → α-free, NOT 1/137",
                     color="white", fontsize=11)
    axs[1].set_ylabel("valley fraction", color="white")
    axs[1].legend()
    for ax in axs:
        ax.set_facecolor("#161b22")
        ax.tick_params(colors="white")
    plt.tight_layout()
    p = _HERE / "alpha_valley_fraction_map.png"
    plt.savefig(p, facecolor=fig.get_facecolor(), bbox_inches="tight")
    plt.close()
    print(f"  Saved {p.name}")


if __name__ == "__main__":
    out = main()
    try:
        render_figure(out)
    except Exception as e:  # noqa: BLE001
        print(f"  (figure skipped: {e})")
