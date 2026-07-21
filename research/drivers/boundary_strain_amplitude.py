#!/usr/bin/env python3
"""BOUNDARY-STRAIN AMPLITUDE — the Fork-W conditional's single computation.

THE question (merged #773 §4(a)/§4(b)[NOT-YET-RATIFIABLE], docket
ENTRY 2026-07-20-forkw-kernel-keying review-repair R2): for a LOCALIZED A1
breather u=f(r) r_hat on the srs net, does the core-boundary DEVIATORIC
(transverse) swing stay sub-yield while the axial swing saturates -- so the
kernel rails k_a ALONE (the bulk-only wall FORCED by the keying) -- or does the
boundary deviatoric swing reach yield-scale, softening k_s at the wall too (the
channel-asymmetric wall NOT forced)?

FROZEN prereg (criteria committed + pushed ALONE first):
    research/2026-07-21_boundary-strain-amplitude_prereg-FROZEN.md

Frozen observable: rho_dev(r) = transverse-swing / axial-swing profile; verdict
datum at the saturation shell (argmax axial swing), amplitude normalized so peak
axial swing = A_yield. Bins (prereg s3): (1) K_A-ONLY-FORCED (peak deviatoric
<= 0.5 yield, ALL profiles + BOTH measures); (2) K_S-RAILS-TOO (>= 0.8 yield,
smooth members); (3) PROFILE-DEPENDENT (flips across family/measure); (4) UNDET.

Three legs (prereg s4): A ANALYTIC (exact spherical-elasticity kinematics),
B NUMERIC (per-bond srs strain decomposition, VERDICT-CONTROLLING), C the
pre-stress remap k_shear,eff = k_s + T/ell (axiom-register.md:193; sign matters).

  SECTOR : TRANSLATIONAL (Cauchy) vector sector of the chiral srs-z3 net
           (ave.core.chiral_lattice._SRS_8A/_SRS_NN; rank-2 Phi_b=k_a d^d+k_s(I-d^d)).
           k_a keyed on axial swing |d.du|, k_s on transverse swing |(I-dd).du|
           (#773 s2 Step 3). NOT a Cartesian Laplacian. Rule-14 reuse of the
           #770/#775 constituent_cage_ensemble bond model.
  REGIME : near-yield localized A1 breather core; cold-linear exterior.
  COORDS : A46-clean REAL-SPACE strain decomposition (axial vs transverse swing),
           matching the corpus real-space claim (eps_rr=f', eps_tt=f/r,
           deviatoric prop (f'-f/r)) -- NOT phase-space. phase-space-check PASS.
  CLASS  : KINEMATIC strain decomposition of an IMPOSED profile (NOT envelope
           self-consistency -- declared scope, prereg s0). Leg A = exact geometric
           IDENTITY; Leg B = its lattice MANIFESTATION; alpha-CLEAN, dimensionless.

ENGINE BYTE-UNTOUCHED: reuses research/drivers/constituent_cage_ensemble.py
 primitives (build_finite_srs), which import ave.core.* read-only. Pure kinematic
 imposition + strain read-out; NO dynamics, NO pin, NO RNG -> deterministic.

Run: PYTHONPATH=src:src/scripts/vol_1_foundations python3 \
        research/drivers/boundary_strain_amplitude.py
"""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path

import numpy as np

# -- Rule-14 reuse of the #770/#775 machinery (engine byte-untouched; ave.core.* read-only) --
_CCE_PATH = Path(__file__).with_name("constituent_cage_ensemble.py")
_spec = importlib.util.spec_from_file_location("cce", _CCE_PATH)
cce = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(cce)

RHO_STAR = cce.RHO_STAR   # 9.77337 = k_a (axial stiffness), DERIVED from nu_Hill=2/7 [import]
K_S = cce.K_S             # 1.0 = k_s (transverse stiffness)
ELL = float(cce._SRS_NN)  # bond length ell_node (nearest-neighbour distance)

A_YIELD = 1.0             # normalized yield swing (constituent model convention)
MARGIN_KA_ONLY = 0.5      # bin-1 frozen margin (prereg s3)
THRESH_KS_RAILS = 0.8     # bin-2 yield-scale threshold (prereg s3)


# =============================================================================
# The corpus-admissible localized-breather profile family (prereg s2)
#   each entry: f(r) and its analytic radial derivative f'(r); overall amplitude
#   is arbitrary (renormalized after measuring peak axial swing = A_yield).
# =============================================================================
def make_profiles(r_c=2.0):
    """Return {name: (f, fprime, kind)}; kind in {smooth, seed, sharp}.
    All localized (f->0 at inf), carrying net dilatation, div-free ~1/r^2 exterior
    (except gaussian seed = super-algebraic, and lorentzian = slower 1/r tail)."""
    rc = float(r_c)

    def smooth_eshelby(r):          # affine core -> div-free 1/r^2 tail (PRIMARY)
        return r * rc**2 / (r**2 + rc**2) ** 1.5

    def smooth_eshelby_p(r):        # d/dr [ r rc^2 (r^2+rc^2)^{-3/2} ]
        return rc**2 * (rc**2 - 2.0 * r**2) / (r**2 + rc**2) ** 2.5

    def gaussian_curlfree(r):       # u=grad(exp(-r^2/2 sig^2)); the #761/#767 seed
        return -(r / rc**2) * np.exp(-r**2 / (2.0 * rc**2))

    def gaussian_curlfree_p(r):
        return (1.0 / rc**2) * np.exp(-r**2 / (2.0 * rc**2)) * (r**2 / rc**2 - 1.0)

    def lorentzian(r):              # slower 1/r tail member
        return r * rc / (r**2 + rc**2)

    def lorentzian_p(r):            # d/dr [ r rc (r^2+rc^2)^{-1} ]
        return rc * (rc**2 - r**2) / (r**2 + rc**2) ** 2

    def sharp_eshelby(r):           # affine core hard-matched to 1/r^2 (the sharp LIMIT)
        return np.where(r < rc, r / rc, (rc / r) ** 2)

    def sharp_eshelby_p(r):
        return np.where(r < rc, 1.0 / rc, -2.0 * rc**2 / r**3)

    return {
        "smooth_eshelby": (smooth_eshelby, smooth_eshelby_p, "smooth"),
        "gaussian_curlfree": (gaussian_curlfree, gaussian_curlfree_p, "seed"),
        "lorentzian": (lorentzian, lorentzian_p, "smooth"),
        "sharp_eshelby": (sharp_eshelby, sharp_eshelby_p, "sharp"),
    }


# =============================================================================
# LEG A -- ANALYTIC (exact spherical-elasticity kinematics; prereg s4 Leg A)
#   eps_rr=f', eps_tt=f/r, D=f'-f/r (deviatoric shape), theta=f'+2f/r (dilatation)
# =============================================================================
def legA_analytic(profiles, R_max=40.0, n=400000):
    r = np.linspace(1e-4, R_max, n)
    out = {}
    for name, (f, fp, kind) in profiles.items():
        F = f(r)
        FP = fp(r)
        eps_rr = FP
        eps_tt = F / r
        D = eps_rr - eps_tt            # deviatoric shape (#773 "prop (f'-f/r)")
        theta = eps_rr + 2.0 * eps_tt  # dilatation
        axial = np.abs(eps_rr)
        isat = int(np.argmax(axial))
        peak_ax = axial[isat]
        # MEASURE-2 (continuum deviatoric shape, un-halved) and its bond-shear (1/2 D)
        M2 = float(np.max(np.abs(D)) / peak_ax)
        M2_bondshear = float(np.max(0.5 * np.abs(D)) / peak_ax)
        rho_at_shell = float(np.abs(D[isat]) / (peak_ax + 1e-30))
        # dilatation fraction of the strain energy density (isotropic proxy)
        dil_frac = float(np.sum(theta**2) / (np.sum(theta**2) + np.sum(D**2) + 1e-30))
        out[name] = {
            "kind": kind, "r_sat": float(r[isat]),
            "rho_dev_at_shell": rho_at_shell,
            "M2_deviatoric_shape": M2,             # max|f'-f/r| / max|f'|
            "M2_bondshear_half": M2_bondshear,     # max(1/2|f'-f/r|) / max|f'|
            "dilatation_fraction_interior_proxy": dil_frac,
        }
    # analytic fence (prereg s2): pure affine=0, pure exterior 1/r^2 = 3/2
    rr = np.linspace(1.0, 20.0, 100)
    D_ext = (-2.0 / rr**3) - (1.0 / rr**3)   # eps_rr - eps_tt for f=1/r^2
    out["_fence"] = {
        "pure_affine_rho_dev": 0.0,
        "pure_exterior_1_over_r2_rho_dev": float(np.abs(D_ext[0]) / np.abs(-2.0 / rr[0] ** 3)),
        "note": "admissible family bracketed rho_dev in [0 (affine), 3/2 (div-free tail)]",
    }
    return out


# =============================================================================
# LEG B -- NUMERIC (per-bond srs strain decomposition; VERDICT-CONTROLLING)
# =============================================================================
def _impose_and_decompose(pos, bi, bj, dhat, mid, center, f):
    """Impose u = f(r) r_hat; return per-bond axial swing, transverse swing,
    axial strain-along-bond (=stretch/ell), and bond midpoint radius."""
    rel = pos - center
    r = np.linalg.norm(rel, axis=1)
    rhat = rel / (r[:, None] + 1e-30)
    u = f(r)[:, None] * rhat
    du = u[bj] - u[bi]                                   # relative displacement
    axial_stretch = np.einsum("bi,bi->b", du, dhat)     # d.du (signed stretch)
    A_axial = np.abs(axial_stretch)                     # keys k_a
    perp = du - axial_stretch[:, None] * dhat
    A_trans = np.linalg.norm(perp, axis=1)              # |(I-dd).du| keys k_s
    r_mid = np.linalg.norm(mid - center, axis=1)
    return A_axial, A_trans, axial_stretch, r_mid


def _shell_bin(r_mid, A_axial, A_trans, dr=0.5, r_hi=None):
    """RMS axial/transverse swing per radial shell (bin width dr)."""
    if r_hi is None:
        r_hi = r_mid.max()
    edges = np.arange(0.0, r_hi + dr, dr)
    ctr, ax, tr, cnt = [], [], [], []
    for k in range(len(edges) - 1):
        m = (r_mid >= edges[k]) & (r_mid < edges[k + 1])
        if m.sum() < 3:
            continue
        ctr.append(0.5 * (edges[k] + edges[k + 1]))
        ax.append(float(np.sqrt(np.mean(A_axial[m] ** 2))))
        tr.append(float(np.sqrt(np.mean(A_trans[m] ** 2))))
        cnt.append(int(m.sum()))
    return np.array(ctr), np.array(ax), np.array(tr), np.array(cnt)


def legB_numeric(L, profiles, dr=0.5):
    pos, bi, bj, dhat, mid = cce.build_finite_srs(L)
    center = np.array([L / 2.0] * 3)
    r_hi = L / 2.0 - 1.0
    out = {}
    for name, (f, fp, kind) in profiles.items():
        A_axial, A_trans, _, r_mid = _impose_and_decompose(pos, bi, bj, dhat, mid, center, f)
        ctr, ax, tr, cnt = _shell_bin(r_mid, A_axial, A_trans, dr=dr, r_hi=r_hi)
        isat = int(np.argmax(ax))                       # saturation shell
        norm = ax[isat] + 1e-30                         # -> peak axial swing = A_yield
        ax_n, tr_n = ax / norm, tr / norm
        rho = tr_n / (ax_n + 1e-30)
        M = float(np.max(tr_n))                         # peak boundary deviatoric (yield units)
        # exterior-tail check: rho_dev far out (should approach the analytic 3/2 fence
        # for the div-free members; the pipeline validation, prereg s6 report item 3)
        ext = ctr > (0.6 * r_hi)
        rho_ext = float(np.median(rho[ext])) if ext.sum() else float("nan")
        out[name] = {
            "kind": kind,
            "r_sat": float(ctr[isat]),
            "rho_dev_at_shell": float(rho[isat]),       # MEASURE-1 ratio at r_sat
            "M_peak_transverse_yieldunits": M,          # MEASURE-1 verdict metric
            "rho_dev_exterior_tail": rho_ext,           # pipeline fence vs analytic 3/2
            "shells_r": ctr.tolist(),
            "Abar_axial_norm": ax_n.tolist(),
            "Abar_trans_norm": tr_n.tolist(),
            "rho_dev_profile": rho.tolist(),
            "n_bonds_per_shell": cnt.tolist(),
        }
    return out


# =============================================================================
# LEG C -- THE PRE-STRESS REMAP (axiom-register.md:193; sign matters -- #773 flag)
#   k_shear,eff = k_s + T/ell ; T_b = k_a * (d.du) (per-bond axial tension)
# =============================================================================
def legC_prestress_remap(L, profiles, dr=0.5, k_a=RHO_STAR, k_s=K_S, ell=ELL):
    pos, bi, bj, dhat, mid = cce.build_finite_srs(L)
    center = np.array([L / 2.0] * 3)
    r_hi = L / 2.0 - 1.0
    out = {}
    for name, (f, fp, kind) in profiles.items():
        A_axial, A_trans, stretch, r_mid = _impose_and_decompose(
            pos, bi, bj, dhat, mid, center, f)
        # locate the saturation shell (max RMS axial swing) and normalize so the peak
        # axial STRAIN (stretch/ell) = A_yield -> read the remap in yield-strain units.
        ctr, ax, tr, cnt = _shell_bin(r_mid, A_axial, A_trans, dr=dr, r_hi=r_hi)
        isat = int(np.argmax(ax))
        r_shell = ctr[isat]
        # peak axial strain over all bonds (for the A_yield normalization)
        eps_axial = stretch / ell                       # signed axial strain per bond
        peak_axial_strain = np.max(np.abs(eps_axial)) + 1e-30
        scale = A_YIELD / peak_axial_strain             # so peak axial strain -> A_yield
        eps_n = eps_axial * scale                       # normalized axial strain per bond
        # shell membership (bonds whose midpoint radius is in the saturation-shell bin)
        m_shell = (r_mid >= r_shell - 0.5 * dr) & (r_mid < r_shell + 0.5 * dr)
        # per-bond remap: T/ell = k_a * eps_axial ; k_shear,eff = k_s + T/ell
        Tover_ell = k_a * eps_n[m_shell]                # (T/ell)/1, in yield-strain units
        k_eff = k_s + Tover_ell
        frac_soften = float(np.mean(Tover_ell < 0.0)) if m_shell.sum() else float("nan")
        # per-orientation split: cos(psi) = |d . r_hat| at the bond midpoint
        rel_mid = mid - center
        rmid_hat = rel_mid / (np.linalg.norm(rel_mid, axis=1)[:, None] + 1e-30)
        cospsi = np.abs(np.einsum("bi,bi->b", dhat, rmid_hat))  # 1=radial, 0=hoop
        cs = cospsi[m_shell]
        Ts = Tover_ell
        radial = cs > 0.87       # ~<30deg from radial
        hoop = cs < 0.5          # ~>60deg from radial (tangential)
        diag = (~radial) & (~hoop)
        def _msign(mask):
            return float(np.mean(Ts[mask])) if mask.sum() else float("nan")
        out[name] = {
            "kind": kind, "r_shell": float(r_shell), "n_shell_bonds": int(m_shell.sum()),
            "peak_axial_strain_raw": float(peak_axial_strain),
            "mean_Tover_ell_shell": float(np.mean(Ts)) if m_shell.sum() else float("nan"),
            "mean_k_shear_eff_over_ks": float(np.mean(k_eff) / k_s) if m_shell.sum() else float("nan"),
            "fraction_shell_bonds_softened": frac_soften,
            "sign_verdict": ("SOFTENS" if m_shell.sum() and np.mean(Ts) < 0
                             else "STIFFENS" if m_shell.sum() else "n/a"),
            "orientation_split_mean_Tover_ell": {
                "radial_bonds": _msign(radial), "diagonal_bonds": _msign(diag),
                "hoop_bonds": _msign(hoop),
            },
            "note": ("T/ell = k_a * eps_axial in yield-strain units (peak axial strain "
                     "normalized to A_yield=1). SIGN + orientation split are the robust "
                     "deliverable (the #773-flagged countervailing mechanism); the absolute "
                     "magnitude scales with the (disclosed) yield-strain normalization. Sign "
                     "flips with the breather's DC dilatation sign; reported for outward "
                     "(f>0) core -- for the opposite dilatation sign, negate."),
        }
    return out


# =============================================================================
# FROZEN VERDICT (prereg s3 bins; assigned from the frozen-criteria outputs ONLY)
# =============================================================================
def assign_bin(legA, legB):
    """Bins (prereg s3): (1) K_A-ONLY-FORCED if M<=0.5 for ALL profiles AND BOTH
    measures; (2) K_S-RAILS-TOO if M>=0.8 for the SMOOTH members; (3) PROFILE-
    DEPENDENT if it flips across family or measure; (4) UNDETERMINED."""
    names = [n for n in legB if not n.startswith("_")]
    # MEASURE-1 (per-bond srs transverse swing, Leg B, PRIMARY)
    M1 = {n: legB[n]["M_peak_transverse_yieldunits"] for n in names}
    # MEASURE-2 (continuum deviatoric shape, Leg A) -- report both the un-halved
    # shape and the bond-shear (1/2) forms; the bond-shear one is the like-for-like
    # partner of MEASURE-1.
    M2_shape = {n: legA[n]["M2_deviatoric_shape"] for n in names}
    M2_half = {n: legA[n]["M2_bondshear_half"] for n in names}
    smooth = [n for n in names if legB[n]["kind"] in ("smooth", "seed")]

    all_below_half = all(M1[n] <= MARGIN_KA_ONLY for n in names) and \
        all(M2_half[n] <= MARGIN_KA_ONLY for n in names)
    smooth_yieldscale = all(M1[n] >= THRESH_KS_RAILS for n in smooth)
    # flip detectors
    m1_flip = (min(M1.values()) <= MARGIN_KA_ONLY) and (max(M1.values()) >= THRESH_KS_RAILS)
    measure_flip = any(
        (M1[n] <= MARGIN_KA_ONLY) != (M2_shape[n] <= MARGIN_KA_ONLY) for n in names)

    if all_below_half:
        b = "1_KA_ONLY_FORCED"
    elif smooth_yieldscale:
        b = "2_KS_RAILS_TOO"
    elif m1_flip or measure_flip:
        b = "3_PROFILE_DEPENDENT"
    else:
        b = "3_PROFILE_DEPENDENT"   # intermediate (0.5,0.8) no-clean-bin zone -> the fork
    return {
        "bin": b,
        "M1_per_bond_transverse_yieldunits": M1,
        "M2_deviatoric_shape": M2_shape,
        "M2_bondshear_half": M2_half,
        "smooth_members": smooth,
        "all_below_0p5_both_measures": bool(all_below_half),
        "smooth_at_yieldscale_ge_0p8": bool(smooth_yieldscale),
        "measure_dependence_flip": bool(measure_flip),
        "family_flip_measure1": bool(m1_flip),
    }


def rc_robustness(L, rc_scan=(1.5, 2.0, 3.0)):
    """Frozen REPORT item 1 (prereg s6): does the verdict metric M1 move with the
    core scale r_c within the resolvable band? (primary profile)."""
    out = {}
    for rc in rc_scan:
        profs = make_profiles(r_c=rc)
        lb = legB_numeric(L, profs)
        out[f"{rc:g}"] = {n: lb[n]["M_peak_transverse_yieldunits"]
                          for n in lb if not n.startswith("_")}
    return out


# =============================================================================
# FIGURE (white house style; ave.viz.style; honest axes/units; legend outside data)
# =============================================================================
def make_figure(out, path_png):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from ave.viz import style
    style.apply()
    C = style.COLORS

    lb = out["legB_numeric"]
    names = [n for n in lb if not n.startswith("_")]
    palette = [C["ave"], C["comparison"], C["data"], C["accent"]]

    fig, (axL, axR) = plt.subplots(1, 2, figsize=(10.8, 4.3))

    # (L) rho_dev(r) vs r for the admissible family, with r_sat + the 0.5/0.8 margins
    for name, col in zip(names, palette):
        d = lb[name]
        axL.plot(d["shells_r"], d["rho_dev_profile"], "o-", color=col, ms=4,
                 label=name.replace("_", "-"))
        axL.axvline(d["r_sat"], color=col, ls=":", lw=0.8, alpha=0.5)
    axL.axhline(1.5, color=C["muted"], ls="--", lw=1)
    axL.annotate("div-free tail ρ_dev=3/2 (deviatoric-dominated)", xy=(1, 1.5),
                 xytext=(1.0, 1.58), fontsize=6.5, color=C["muted"])
    axL.axhline(MARGIN_KA_ONLY, color=C["data"], ls=":", lw=1.0)
    axL.annotate("bin-1 margin 0.5", xy=(1, 0.5), xytext=(1.0, 0.36),
                 fontsize=6.5, color=C["data"])
    axL.set_xlabel("shell radius r  (node-spacings; from breather core)")
    axL.set_ylabel("ρ_dev(r) = transverse swing / axial swing  (per-bond RMS)")
    axL.set_xlim(0, 9)
    axL.set_ylim(0, 2.0)
    axL.legend(loc="upper right", fontsize=6.5, frameon=False)
    axL.annotate("dotted verticals = saturation shell r_sat (argmax axial swing)",
                 xy=(4, 0.05), xytext=(2.2, 0.03), fontsize=6.0, color=C["muted"])

    # (R) verdict metric M (peak boundary deviatoric, yield units) per profile, both measures
    x = np.arange(len(names))
    M1 = [lb[n]["M_peak_transverse_yieldunits"] for n in names]
    M2h = [out["legA_analytic"][n]["M2_bondshear_half"] for n in names]
    M2s = [out["legA_analytic"][n]["M2_deviatoric_shape"] for n in names]
    axR.bar(x - 0.25, M1, width=0.24, color=C["ave"], label="MEASURE-1 (srs per-bond, PRIMARY)")
    axR.bar(x, M2h, width=0.24, color=C["comparison"], label="MEASURE-2 bond-shear ½|f′−f/r|")
    axR.bar(x + 0.25, M2s, width=0.24, color=C["muted"], label="MEASURE-2 shape |f′−f/r|")
    axR.axhline(MARGIN_KA_ONLY, color=C["data"], ls=":", lw=1.2)
    axR.axhline(THRESH_KS_RAILS, color=C["accent"], ls="--", lw=1.0)
    axR.annotate("bin-1 ≤0.5", xy=(len(names) - 1, 0.5), xytext=(len(names) - 1.4, 0.53),
                 fontsize=6.5, color=C["data"])
    axR.annotate("bin-2 ≥0.8 (yield-scale)", xy=(0, 0.8), xytext=(-0.3, 0.83),
                 fontsize=6.5, color=C["accent"])
    axR.set_xticks(x)
    axR.set_xticklabels([n.replace("_", "\n") for n in names], fontsize=7)
    axR.set_ylabel("M = peak boundary deviatoric  (yield units, axial=1)")
    axR.set_ylim(0, 1.7)
    axR.legend(loc="upper center", fontsize=6.2, frameon=False)

    fig.savefig(path_png, dpi=150, bbox_inches="tight")
    fig.savefig(str(Path(path_png).with_suffix(".pdf")), bbox_inches="tight")
    plt.close(fig)


def main():
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--L", type=int, default=24)
    ap.add_argument("--r_c", type=float, default=2.0)
    ap.add_argument("--out", default=str(Path(__file__).with_name(
        "boundary_strain_amplitude_results.json")))
    args = ap.parse_args()

    profiles = make_profiles(r_c=args.r_c)
    out = {
        "provenance": {
            "class": "boundary-strain amplitude -- the Fork-W conditional's single "
                     "computation (#773 s4a owed follow-on); does a LOCALIZED A1 breather's "
                     "core-boundary DEVIATORIC swing stay sub-yield while axial saturates? "
                     "KINEMATIC strain decomposition of an imposed profile (declared scope); "
                     "engine byte-untouched (reuses constituent_cage_ensemble.py primitives).",
            "prereg": "research/2026-07-21_boundary-strain-amplitude_prereg-FROZEN.md (FROZEN, pushed ALONE)",
            "k_a_RHO_STAR": RHO_STAR, "k_s_K_S": K_S, "ell_node_SRS_NN": ELL,
            "A_yield": A_YIELD, "bin1_margin": MARGIN_KA_ONLY, "bin2_yieldscale": THRESH_KS_RAILS,
            "r_c": args.r_c, "L": args.L,
        },
    }
    out["legA_analytic"] = legA_analytic(profiles)
    out["legB_numeric"] = legB_numeric(args.L, profiles)
    out["legC_prestress_remap"] = legC_prestress_remap(args.L, profiles)
    out["verdict"] = assign_bin(out["legA_analytic"], out["legB_numeric"])
    out["rc_robustness_M1"] = rc_robustness(args.L)

    Path(args.out).write_text(json.dumps(out, indent=2))
    make_figure(out, str(Path(args.out).with_name("boundary_strain_amplitude.png")))

    # -- console summary (frozen-criteria outputs only) --
    print("k_a=%.4f k_s=%.1f ell_node=%.5f | bins: KA<=%.1f  KS>=%.1f" % (
        RHO_STAR, K_S, ELL, MARGIN_KA_ONLY, THRESH_KS_RAILS))
    print("LEG A analytic fence:", out["legA_analytic"]["_fence"])
    print("%-18s | rho@shell(B) | M1(B) | M2_½|D| | M2|D| | Cleg sign | rho_ext(B)" % "profile")
    for n in [x for x in out["legB_numeric"] if not x.startswith("_")]:
        b = out["legB_numeric"][n]; a = out["legA_analytic"][n]; c = out["legC_prestress_remap"][n]
        print("%-18s | %11.3f | %5.3f | %7.3f | %5.3f | %-9s | %.3f" % (
            n, b["rho_dev_at_shell"], b["M_peak_transverse_yieldunits"],
            a["M2_bondshear_half"], a["M2_deviatoric_shape"], c["sign_verdict"],
            b["rho_dev_exterior_tail"]))
    print("VERDICT bin:", out["verdict"]["bin"])
    print("  all_below_0.5_both_measures:", out["verdict"]["all_below_0p5_both_measures"],
          "| smooth_at_yieldscale>=0.8:", out["verdict"]["smooth_at_yieldscale_ge_0p8"],
          "| measure_flip:", out["verdict"]["measure_dependence_flip"])
    print("LEG C (pre-stress remap) sign by profile + orientation:")
    for n in [x for x in out["legC_prestress_remap"] if not x.startswith("_")]:
        c = out["legC_prestress_remap"][n]
        print("   %-18s %s  <k_eff/ks>=%.3f  soften-frac=%.2f  orient(rad/diag/hoop T/l)=%s" % (
            n, c["sign_verdict"], c["mean_k_shear_eff_over_ks"],
            c["fraction_shell_bonds_softened"],
            {k: round(v, 3) for k, v in c["orientation_split_mean_Tover_ell"].items()}))
    print("rc-robustness M1 (primary):",
          {rc: v.get("smooth_eshelby") for rc, v in out["rc_robustness_M1"].items()})
    return out


if __name__ == "__main__":
    main()
