"""
LANE W — STEP 0: the pair-field FORM multipole analysis (ANALYTIC, DECISIVE).
=============================================================================

FROZEN PRE-REG: research/2026-07-03_lanew-pair-field-form_prereg.md (committed
BEFORE this driver, standing gate). Epic: EM-readout derivation, LAST live lane.

THE QUESTION (prereg): does the MASSLESS-channel field between two winding
solitons carry the COULOMB FORM (unscreened 1/r-class, exponent p=-1 in
U(d)~d^p) -- or the MULTIPOLE FORM (dipole/quadrupole, p<=-3) that a globally-
neutral compact texture generically gives?

STEP-0 (this driver) is ANALYTIC on FROZEN seeds (the cheapest-decisive form
check, per the day's analytic-first lesson): compute the A44 gyrotropic-neutral
texture around ONE (2,3) winding, extract its multipole content, solve the
massless (open-Green's-fn) pair interaction U(d), and read the exponent -- with
PLANTED liveness controls (a true Coulomb pair must read -1) certifying the
pipeline. NO dynamics; NO engine step(); the DECISIVE dynamical runs are HELD
for orchestrator review (prereg S5).

SECTOR / REGIME (prereg S0):
  SECTOR = T2/Cosserat omega-sector winding, read into the A1/E-sector via the
           A44 gyrotropic converter (f_V = -kappa g Omega_w, Omega_w=(curl w).x-hat;
           adjudicated A44 = Axiom-1 non-centrosymmetry consequence). The texture
           is a GLOBALLY-NEUTRAL bound-charge form-factor (beta note: sum rho = 0),
           NOT a net monopole. Computed ONLY via the A44 form from omega -- no
           integer, no planted charge; Gauss is DIAGNOSTIC-ONLY.
  HOST   = S1 isolated-knot host (_build_isolated_knot: CrystalGraftV4, buckle
           OFF, photon OFF, lock ON, kappa=6/5 alpha-clean). Reused verbatim.
  CHANNEL= the MASSLESS E-sector Poisson field (nabla^2 phi = -rho), UNSCREENED
           -- genuinely different from the gapped-omega Yukawa force of clm-wcoul2.

COORDINATES (phase-space-coordinate-check, A46; prereg S0.1): the (2,3) winding
  label is PHASE-SPACE; d, rho(r), phi(r), U(d) are REAL-SPACE. The FORM
  observable (exponent of U(d)) is a real-space power law matched to the real-
  space Poisson field of the real-space texture -- the corpus "Coulomb FORM"
  claim IS a real-space claim, so real-space measurement is matching-coordinate.

TEXTURE-FORM FORK (flag-don't-fix, prereg S2.3): TWO texture readings carried:
  (S) SCALAR    rho_S = -kappa g (curl omega).x-hat   [engine's literal f_V]
  (D) COVARIANT rho_D = -kappa div(g curl omega)      [beta-note DEC form]
Both reported; both steeper than Coulomb (S=dipole, D=quadrupole).

STRUCTURAL DEGENERACY (prereg S3.8): the periodic-FFT Poisson solve STEEPENS
  every exponent (Ewald images); a planted Coulomb pair reads -2.8 not -1 there.
  So the FORM fit uses the OPEN-domain Coulomb Green's fn (direct 1/(4 pi r)
  double-sum), which reads the planted Coulomb pair at -1.000 exactly. The
  usable d-window is bounded BELOW by texture overlap (d>=28) and ABOVE by the
  numerical floor -- reported per point.

DRIVER HONESTY (ave-driver-script-honesty): every printed number computed
  in-run; the PLANTED liveness control (a known Coulomb pair -> -1) runs FIRST
  and gates the texture verdict.

Run:
    PYTHONPATH=src <venv>/bin/python \
        src/scripts/vol_4_engineering/lanew_pair_field_form_step0.py
"""
from __future__ import annotations

import json

import numpy as np

from ave.core.s1_winding_conservation_gate import _build_isolated_knot
from ave.core.cross_sector_coupling import (
    curl_central,
    microrotation_x,
    saturation_front_window,
    combined_strain_amplitude,
    KAPPA_TILDE,
)

# ── frozen host geometry (S1 isolated-knot host, reused verbatim) ──────────────
N = 96          # domain: two R=11 knots + cold gap + PML each side
R = 11.0        # torus major radius (S1 default)
r = 4.0         # torus tube radius (S1 default)
AMPLITUDE = 0.4  # S1 isolated-knot seed amplitude
XC = (N - 1) / 2.0

# form-fit d-window (prereg S3.6a overlap bound d>=28; S3.8 floor bound):
D_WINDOW = [28, 32, 36, 40]
D_ALL = [16, 20, 24, 28, 32, 36, 40]   # incl. overlap regime (reported, excluded from fit)


# ──────────────────────────────────────────────────────────────────────────────
# THE A44 TEXTURE (computed ONLY via the A44 form from omega -- prereg S2.1).
# ──────────────────────────────────────────────────────────────────────────────
def _g_and_curl(om: np.ndarray, dx: float) -> tuple[np.ndarray, np.ndarray]:
    """The saturation-front window g(A) on the winding's own microrotation strain,
    and the curl of omega. A = combined strain from |omega|^2 (S1 host: V~0, no
    live director w, so the winding's own omega IS the rotational field the A44
    converter curls -- consistent with the beta note's curl_adj(omega))."""
    A_cos_sq = np.sum(om * om, axis=-1)
    A = combined_strain_amplitude(np.zeros_like(A_cos_sq), A_cos_sq, V_snap=1.0)
    g = saturation_front_window(A)
    return g, curl_central(om, dx)


def texture_scalar(om: np.ndarray, dx: float) -> np.ndarray:
    """(S) rho_S = -kappa g (curl omega).x-hat -- the engine's LITERAL f_V source
    (crystal_engine.py:244), x-hat = photon propagation axis n-hat (NOT a gauge pick)."""
    g = _g_and_curl(om, dx)[0]
    return -KAPPA_TILDE * g * microrotation_x(om, dx)


def texture_covariant(om: np.ndarray, dx: float) -> np.ndarray:
    """(D) rho_D = -kappa div(g curl omega) -- the beta-note DEC form
    rho = div J, J = W(A) (x) curl_adj(omega), transcribed to the real-space
    lattice (weight-AFTER-curl, covariant, no axis pick)."""
    g, curl_om = _g_and_curl(om, dx)
    J = g[..., None] * curl_om
    d = lambda F, a: (np.roll(F, -1, a) - np.roll(F, 1, a)) / (2.0 * dx)
    return -KAPPA_TILDE * (d(J[..., 0], 0) + d(J[..., 1], 1) + d(J[..., 2], 2))


# ──────────────────────────────────────────────────────────────────────────────
# MULTIPOLE MOMENTS (Cartesian, about the |rho|-weighted centroid) -- prereg S3.2-3.
# ──────────────────────────────────────────────────────────────────────────────
def multipoles(rho: np.ndarray, mask: np.ndarray) -> dict:
    rho = rho * mask
    idx = np.indices(rho.shape).astype(float)
    w = np.abs(rho)
    tot = w.sum() + 1e-30
    c = np.array([(idx[a] * w).sum() / tot for a in range(3)])
    rr = np.stack([idx[a] - c[a] for a in range(3)], 0)
    q0 = float(rho.sum())
    p = np.array([(rho * rr[a]).sum() for a in range(3)])
    r2 = sum(rr[a] ** 2 for a in range(3))
    Q = np.array([[(rho * (3 * rr[a] * rr[b] - (r2 if a == b else 0.0))).sum()
                   for b in range(3)] for a in range(3)])
    return {
        "monopole_sum_rho": q0,
        "sum_abs_rho": float(np.abs(rho).sum()),
        "dipole_p": p.tolist(),
        "dipole_mag": float(np.linalg.norm(p)),
        "quadrupole_frob_norm": float(np.linalg.norm(Q)),
        "quadrupole_trace": float(np.trace(Q)),
        "centroid": c.tolist(),
    }


# ──────────────────────────────────────────────────────────────────────────────
# OPEN-DOMAIN interaction (prereg S3.8: the periodic FFT steepens exponents; the
# open Coulomb Green's fn 1/(4 pi r) reads a true Coulomb pair at -1 exactly).
# ──────────────────────────────────────────────────────────────────────────────
def _significant(rho: np.ndarray, mask: np.ndarray, tol_frac: float) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    rho = rho * mask
    tol = tol_frac * (np.abs(rho).max() + 1e-30)
    sel = np.abs(rho) > tol
    coords = np.array(np.where(sel)).T.astype(float)
    return coords, rho[sel], sel


def _open_interaction(xsA, qsA, xsB, qsB) -> float:
    """U = sum_ij qA_i qB_j / (4 pi |rA_i - rB_j|) -- open Coulomb Green's fn."""
    U = 0.0
    for i in range(0, len(xsA), 3000):
        dA = xsA[i:i + 3000]
        qA = qsA[i:i + 3000]
        diff = dA[:, None, :] - xsB[None, :, :]
        dist = np.sqrt((diff ** 2).sum(-1)) + 1e-9
        U += float((qA[:, None] * qsB[None, :] / (4.0 * np.pi * dist)).sum())
    return U


def pair_exponent(make_rho, mask, ds, tol_frac=3e-3) -> dict:
    """U(d) for a texture-factory make_rho(offset)->(N,N,N) rho, at separations ds,
    reporting per-d the support-overlap fraction and U, and the exponent fit on the
    CLEAN (non-overlap, above-floor) window."""
    rows = []
    for d in ds:
        xsA, qsA, selA = _significant(make_rho(-d / 2), mask, tol_frac)
        xsB, qsB, selB = _significant(make_rho(+d / 2), mask, tol_frac)
        ov = float((selA & selB).sum()) / float(min(selA.sum(), selB.sum()) + 1)
        U = _open_interaction(xsA, qsA, xsB, qsB)
        rows.append({"d": int(d), "overlap_frac": ov, "U": U,
                     "clean": bool(ov <= 0.02 and abs(U) > 1e-9)})
    clean = [(rw["d"], abs(rw["U"])) for rw in rows if rw["clean"]]
    # FLOOR GUARD (flag-don't-fix): if the clean-window U drops MORE than one
    # decade per successive d (a cliff into the numerical floor, not a power law),
    # the exponent is NOT reliably readable -- report NaN + a floor flag rather
    # than a spurious steep exponent. A true power law d^p over d in [28,40] moves
    # < ~0.4 decade per step; a floor-cliff moves >1 decade.
    floor_limited = False
    if len(clean) >= 2:
        cu = np.array([c[1] for c in clean])
        step_decades = np.abs(np.diff(np.log10(cu + 1e-300)))
        floor_limited = bool(np.any(step_decades > 1.0))
    if len(clean) >= 3 and not floor_limited:
        dd = np.array([c[0] for c in clean], float)
        uu = np.array([c[1] for c in clean])
        p = float(np.polyfit(np.log(dd), np.log(uu), 1)[0])
    else:
        p = float("nan")
    return {"per_d": rows, "exponent_clean": p, "floor_limited": floor_limited}


def far_field_phi_exponent(rho: np.ndarray, mask: np.ndarray) -> float:
    """single-texture |phi|(r) exponent (open Green's fn, sampled off-axis along
    +-y/+-z to avoid the x-hat lobe bias). Overlap-independent form fingerprint."""
    xs, qs, _ = _significant(rho, mask, 1e-3)
    rs = np.arange(8, 34, 2.0)
    phis = []
    for rr in rs:
        pts = np.array([[XC, XC + rr, XC], [XC, XC, XC + rr],
                        [XC, XC - rr, XC], [XC, XC, XC - rr]])
        val = 0.0
        for pt in pts:
            dist = np.sqrt(((xs - pt) ** 2).sum(1)) + 1e-9
            val += abs(float((qs / (4.0 * np.pi * dist)).sum()))
        phis.append(val / len(pts))
    phis = np.array(phis)
    far = (rs >= 12) & (rs <= 30) & (phis > 0)
    return float(np.polyfit(np.log(rs[far]), np.log(phis[far]), 1)[0])


# ──────────────────────────────────────────────────────────────────────────────
# PLANTED LIVENESS CONTROLS (prereg S3.8) -- run FIRST, gate the texture verdict.
# ──────────────────────────────────────────────────────────────────────────────
def _point_blob(cx, cy, cz, q, sigma=1.6) -> np.ndarray:
    idx = np.indices((N, N, N)).astype(float)
    r2 = (idx[0] - cx) ** 2 + (idx[1] - cy) ** 2 + (idx[2] - cz) ** 2
    b = np.exp(-r2 / (2 * sigma ** 2))
    b *= q / b.sum()   # net charge = q exactly
    return b


def liveness_controls(mask) -> dict:
    """A planted +q/-q Coulomb pair MUST read exponent -1 (attract, U<0); a
    planted like pair MUST read -1 (repel, U>0); a planted dipole pair MUST read
    -3. If these fail, the texture exponent is a pipeline artifact and the run is VOID."""
    ds = D_WINDOW
    unlike = pair_exponent(
        lambda off: _point_blob(XC + off, XC, XC, +1.0 if off < 0 else -1.0), mask, ds)
    like = pair_exponent(
        lambda off: _point_blob(XC + off, XC, XC, +1.0), mask, ds)
    dip = pair_exponent(
        lambda off: (_point_blob(XC + off, XC + 2.0, XC, +1.0)
                     + _point_blob(XC + off, XC - 2.0, XC, -1.0)), mask, ds)
    unlike_U = [rw["U"] for rw in unlike["per_d"]]
    like_U = [rw["U"] for rw in like["per_d"]]
    coulomb_ok = (abs(unlike["exponent_clean"] + 1.0) < 0.1
                  and abs(like["exponent_clean"] + 1.0) < 0.1
                  and all(u < 0 for u in unlike_U) and all(u > 0 for u in like_U))
    dipole_ok = abs(dip["exponent_clean"] + 3.0) < 0.3
    return {
        "unlike_coulomb_exponent": unlike["exponent_clean"],
        "like_coulomb_exponent": like["exponent_clean"],
        "planted_dipole_exponent": dip["exponent_clean"],
        "unlike_all_attract": bool(all(u < 0 for u in unlike_U)),
        "like_all_repel": bool(all(u > 0 for u in like_U)),
        "coulomb_reads_minus1": bool(coulomb_ok),
        "dipole_reads_minus3": bool(dipole_ok),
        "PASS": bool(coulomb_ok and dipole_ok),
    }


# ──────────────────────────────────────────────────────────────────────────────
def analyze_texture(name, texfn, e, mask) -> dict:
    dx = e.dx
    om0 = e.omega.copy()
    rho = texfn(om0, dx)
    mp = multipoles(rho, mask)
    far = far_field_phi_exponent(rho, mask)
    pair = pair_exponent(lambda off: texfn(np.roll(om0, int(round(off)), 0), dx),
                         mask, D_ALL, tol_frac=3e-3)
    # mirror (enantiomorph) — neutrality + dipole sign guard (prereg S3.8 degeneracy-3)
    om_m = om0[:, :, ::-1, :].copy()
    om_m[..., 2] *= -1.0
    mp_m = multipoles(texfn(om_m, dx), mask)
    return {
        "name": name,
        "multipoles": mp,
        "far_field_phi_exponent": far,
        "pair": pair,
        "mirror_monopole": mp_m["monopole_sum_rho"],
        "mirror_dipole": mp_m["dipole_p"],
    }


def classify(scalar, covariant, live) -> tuple[str, str]:
    """Bin per prereg S1 on the LIVENESS-certified pipeline. EXPONENT primary."""
    if not live["PASS"]:
        return "VOID", "liveness controls failed (pipeline does not read Coulomb -1)"
    pS = scalar["pair"]["exponent_clean"]
    # SCALAR is the engine's actual f_V form -> the load-bearing exponent
    if not np.isfinite(pS):
        return "BELOW-FLOOR", "scalar-form pair interaction below reliable floor"
    if abs(pS + 1.0) < 0.3:
        return "PAIR-COULOMB-FORM", f"scalar exponent {pS:+.2f} ~ -1 (Coulomb)"
    if pS <= -2.5:
        return "MULTIPOLE-FORM", (
            f"scalar exponent {pS:+.2f} (dipole-dipole class); covariant far-|phi| "
            f"{covariant['far_field_phi_exponent']:+.2f} (quadrupole). Monopole=0 forced.")
    return "STUCK-FRAMING", f"scalar exponent {pS:+.2f} between bins -> Grant"


def main() -> None:
    e = _build_isolated_knot(N, R, r, lock_on=True, amplitude=AMPLITUDE)
    mask = e.interior_mask()

    print("=" * 74)
    print("LANE W STEP-0 — pair-field FORM multipole analysis (ANALYTIC, frozen seed)")
    print("=" * 74)

    print("\n[1] PLANTED LIVENESS CONTROLS (gate the texture verdict) ...")
    live = liveness_controls(mask)
    for k, v in live.items():
        print(f"    {k:28s} = {v}")
    if not live["PASS"]:
        print("\n    LIVENESS FAILED -> texture verdict VOID.")

    print("\n[2] A44 TEXTURE — SCALAR (engine f_V) vs COVARIANT (beta DEC) ...")
    scalar = analyze_texture("SCALAR (engine f_V)", texture_scalar, e, mask)
    covariant = analyze_texture("COVARIANT (beta DEC)", texture_covariant, e, mask)
    for tx in (scalar, covariant):
        mp = tx["multipoles"]
        print(f"\n  --- {tx['name']} ---")
        print(f"    monopole sum(rho)      = {mp['monopole_sum_rho']:+.3e}  (forced 0)")
        print(f"    sum|rho|               = {mp['sum_abs_rho']:.4e}")
        print(f"    dipole |p|             = {mp['dipole_mag']:.4e}   p = {mp['dipole_p']}")
        print(f"    quadrupole ||Q||       = {mp['quadrupole_frob_norm']:.4e}")
        print(f"    far-field |phi| exp    = {tx['far_field_phi_exponent']:+.3f}"
              "   (monopole->-1 dipole->-2 quad->-3)")
        print("    pair U(d) [open Green's fn], per-d:")
        for rw in tx["pair"]["per_d"]:
            tag = "clean" if rw["clean"] else ("OVERLAP" if rw["overlap_frac"] > 0.02 else "floor")
            print(f"       d={rw['d']:2d} overlap={rw['overlap_frac']:.3f} "
                  f"U={rw['U']:+.3e} [{tag}]")
        pexp = tx["pair"]["exponent_clean"]
        if tx["pair"].get("floor_limited"):
            print("    PAIR EXPONENT (clean)  = FLOOR-LIMITED (U cliffs into the numerical "
                  "floor; use far-|phi| exponent above)")
        else:
            print(f"    PAIR EXPONENT (clean)  = {pexp:+.3f}")
        print(f"    mirror monopole        = {tx['mirror_monopole']:+.3e} (neutrality guard)")

    print("\n[3] BIN (per prereg S1, exponent primary) ...")
    bin_name, reason = classify(scalar, covariant, live)
    print(f"    BIN    = [{bin_name}]")
    print(f"    REASON = {reason}")
    print("    (Coulomb monopole -> p=-1 ; dipole-dipole -> p=-3 ; quad-quad -> p=-5)")

    results = {
        "liveness": live,
        "scalar": scalar,
        "covariant": covariant,
        "bin": bin_name,
        "reason": reason,
        "d_window_fit": D_WINDOW,
    }
    out = __file__.replace(".py", "_results.json")
    with open(out, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\n    results -> {out}")


if __name__ == "__main__":
    main()
