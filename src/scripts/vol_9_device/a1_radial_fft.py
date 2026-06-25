#!/usr/bin/env python
"""A1 SPATIAL cavity-mode FFT --- the spatial mode spectrum of the A1 dilatation
breather. Re-homed (net-new canonical) driver for Vol-9 Ch.9.

EXPLICITLY DISTINCT from the TEMPORAL ring-down FFT in Ch.17 (the
omega_cutoff ~ 2.87 ring-down envelope, FFT over time-steps). THIS driver takes
the FFT over the real-space RADIAL coordinate of the SAME most-bound A1
eigenvector the two-natured figure (Ch.3a) uses, to read out the SPATIAL mode
content (node count / overtone structure / dominant wavelength). The two FFTs
answer different questions:
  Ch.17 TEMPORAL FFT --> the mode FREQUENCY (omega_cutoff ~ 2.87, the ring-down).
  Ch.9  SPATIAL  FFT --> the mode SHAPE in space (nodes, overtones, wavelength).

The honest result (CONSISTENCY-class --- re-expresses the same on-main A1
eigenvector, no new claim):
  * the radial profile of |A1| is a SINGLE localized lobe (nodeless fundamental,
    monotone decay outside the core) --> the 1D radial FFT is FEATURELESS: no
    overtone ladder, no discrete spatial-harmonic peaks (the windowed FFT of one
    non-periodic lobe smears, it does not resolve overtones).
  * the rigorous 3D power spectrum P(|k|) peaks at lambda ~ 3.7 cells, with
    spectral centroid lambda_c ~ 2.2 cells and a BROADBAND envelope (half-power
    width ~ 0.5 cyc/cell). This breadth is the Fourier-conjugate of the sharp
    ~2-cell stiff-core localization (a tightly localized lobe in real space is
    broadband in k --- not a multi-mode spectrum).

So the A1 mass-cavity is a Gamma=-1-boundary-confined NODELESS fundamental, not
a structured standing-wave with overtones. (mass = A1 is the ratified
grade-assignment, PR#260 --- not a driver measurement of A1-vs-T2.)
Every array is real on-main engine output.
"""
from __future__ import annotations

import json
from pathlib import Path

import numpy as np
from scipy.sparse.linalg import eigsh

from ave.solvers.coupled_eigensolve import (
    CoupledEigenConfig,
    solve_coupled_spectrum,
    _build_seeded_sim,
    _decompose_eigenvector,
    _interior_radius,
)


def compute() -> dict:
    """LIVE: pull the most-bound A1 eigenvector, build the uniform radial
    profile, take the 1D radial FFT and the rigorous 3D power spectrum."""
    N = 24
    cfg = CoupledEigenConfig(N=N)
    spec = solve_coupled_spectrum(cfg, winding_on=True)
    sim = _build_seeded_sim(cfg, winding_on=True)
    H = sim._assemble_H()
    vals, vecs = eigsh(H, k=cfg.k_eigs, which="SA")
    order = np.argsort(vals)
    vals, vecs = vals[order], vecs[:, order]
    bm = spec["bound_multiplicity"]
    best_idx, best_cf = 0, -1.0
    for idx in range(max(1, bm)):
        d = _decompose_eigenvector(vecs[:, idx], sim)
        if d["a1_core_frac"] > best_cf:
            best_cf, best_idx = d["a1_core_frac"], idx
    v = vecs[:, best_idx]
    nd = sim.ndof
    a1 = np.real(v[:nd]).reshape(N, N, N)            # signed A1 grade
    rr = _interior_radius(N).reshape(N, N, N)
    if a1[rr < 3.0].sum() < 0:                        # fix global eigen-sign: core positive
        a1 = -a1
    a1abs = np.abs(a1)

    # --- uniform radial profiles (dr = 0.5 cell; the geometric display bins of
    #     the Ch.3a figure are not FFT-able, so re-bin on a uniform grid) ---
    dr, rmax = 0.5, N / 2.0
    edges = np.arange(0.0, rmax + dr, dr)
    centers = 0.5 * (edges[:-1] + edges[1:])
    rflat, fa, fs = rr.reshape(-1), a1abs.reshape(-1), a1.reshape(-1)
    prof_abs = np.array([fa[(rflat >= edges[b]) & (rflat < edges[b + 1])].mean()
                         if ((rflat >= edges[b]) & (rflat < edges[b + 1])).any() else np.nan
                         for b in range(len(centers))])
    prof_sig = np.array([fs[(rflat >= edges[b]) & (rflat < edges[b + 1])].mean()
                         if ((rflat >= edges[b]) & (rflat < edges[b + 1])).any() else np.nan
                         for b in range(len(centers))])
    ix = np.arange(len(centers))
    prof_abs = np.interp(ix, ix[np.isfinite(prof_abs)], prof_abs[np.isfinite(prof_abs)])
    prof_sig = np.interp(ix, ix[np.isfinite(prof_sig)], prof_sig[np.isfinite(prof_sig)])

    def fft1d(prof):
        n = len(prof)
        win = np.hanning(n)
        F = np.abs(np.fft.rfft((prof - prof.mean()) * win))
        f = np.fft.rfftfreq(n, d=dr)                  # cycles / cell
        return f, F

    f_a, P_a = fft1d(prof_abs)
    f_s, P_s = fft1d(prof_sig)

    def dom(f, P):
        k = np.argmax(P[1:]) + 1
        return float(f[k]), (float(1.0 / f[k]) if f[k] > 0 else np.inf), float(P[k] / P[1:].sum())

    dk_a, lam_a, frac_a = dom(f_a, P_a)
    dk_s, lam_s, frac_s = dom(f_s, P_s)

    # count spectral peaks above 25% of max (harmonic content). A single
    # localized lobe smears into a low-k ramp, not a discrete overtone ladder.
    def npeaks(P):
        P2 = P[1:]
        thr = 0.25 * P2.max()
        return int(np.sum((P2[1:-1] > thr) & (P2[1:-1] > P2[:-2]) & (P2[1:-1] > P2[2:]))) \
            + (1 if P2[0] > thr else 0)

    # --- 3D power spectrum P(|k|) (rigorous cross-check) ---
    A = np.fft.fftshift(np.fft.fftn(a1))
    Pk = np.abs(A) ** 2
    kf = np.fft.fftshift(np.fft.fftfreq(N, d=1.0))   # cycles/cell
    KX, KY, KZ = np.meshgrid(kf, kf, kf, indexing="ij")
    Kmag = np.sqrt(KX**2 + KY**2 + KZ**2).reshape(-1)
    pk = Pk.reshape(-1)
    kedges = np.arange(0.0, Kmag.max() + 1.0 / N, 1.0 / N)
    kcent = 0.5 * (kedges[:-1] + kedges[1:])
    Pk_rad = np.array([pk[(Kmag >= kedges[b]) & (Kmag < kedges[b + 1])].mean()
                       if ((Kmag >= kedges[b]) & (Kmag < kedges[b + 1])).any() else 0.0
                       for b in range(len(kcent))])
    kk = np.argmax(Pk_rad[1:]) + 1
    dom_k3d, lam_3d = float(kcent[kk]), (float(1.0 / kcent[kk]) if kcent[kk] > 0 else np.inf)
    k_centroid = float((kcent * Pk_rad).sum() / Pk_rad.sum())
    above = Pk_rad >= 0.5 * Pk_rad.max()
    k_hpwidth = float(kcent[above].max() - kcent[above].min())
    r_peak = float(centers[np.argmax(prof_abs)])

    return {
        "N": N,
        "forkb_omega": round(float(spec["forkb_omega"]), 4),
        "a1_core_frac": round(float(best_cf), 4),
        "radial_centers": centers,
        "prof_abs": prof_abs,
        "prof_sig": prof_sig,
        "r_peak_cells": round(r_peak, 2),
        "f_a": f_a, "P_a": P_a, "f_s": f_s, "P_s": P_s,
        "dom_k_1d_abs": round(dk_a, 4), "lam_1d_abs": round(lam_a, 2),
        "npeaks_1d_abs": npeaks(P_a),
        "dom_k_1d_sig": round(dk_s, 4), "lam_1d_sig": round(lam_s, 2),
        "npeaks_1d_sig": npeaks(P_s),
        "kcent": kcent, "Pk_rad": Pk_rad,
        "dom_k_3d": round(dom_k3d, 4), "lam_3d_cells": round(lam_3d, 2),
        "k_centroid": round(k_centroid, 4), "lam_centroid_cells": round(1.0 / k_centroid, 2),
        "k_hpwidth": round(k_hpwidth, 4),
    }


def build_figure(res: dict, out_png: Path) -> Path:
    import matplotlib.pyplot as plt

    from ave.viz import style

    style.apply("print")
    WARM = style.COLORS["comparison"]   # vermillion --- mass channel (A1)
    COOL = style.COLORS["accent"]       # bluish-green --- 3D spectrum
    GRY = style.COLORS["muted"]

    centers = res["radial_centers"]
    prof_abs = res["prof_abs"]
    prof_sig = res["prof_sig"]
    f_a, P_a, f_s, P_s = res["f_a"], res["P_a"], res["f_s"], res["P_s"]
    kcent, Pk_rad = res["kcent"], res["Pk_rad"]

    # house style sets constrained_layout (ave.mplstyle:42); keep it and tune
    # padding through the layout engine.
    fig, ax = plt.subplots(1, 3, figsize=(13.5, 4.2))
    fig.get_layout_engine().set(w_pad=0.06, wspace=0.06)

    # (1) radial breather (single localized lobe)
    ax[0].plot(centers, prof_abs / prof_abs.max(), "-o", ms=3, color=WARM,
               label="$|a_{A1}|$ envelope")
    ax[0].plot(centers, prof_sig / np.abs(prof_sig).max(), "-", color=GRY, lw=1,
               label="signed monopole")
    ax[0].set_xlabel(style.axis_label("Radius from core", "r", "cells"))
    ax[0].set_ylabel(style.axis_label("A1 amplitude", "a_{A1}", "norm."))
    ax[0].set_ylim(bottom=min(0.0, float((prof_sig / np.abs(prof_sig).max()).min())))
    style.legend(ax[0], where="below")
    ax[0].text(0.97, 0.95, f"single lobe, peak $r\\approx{res['r_peak_cells']}$ cells\n"
                           "(nodeless fundamental)",
               transform=ax[0].transAxes, va="top", ha="right", fontsize=7.5,
               bbox=dict(boxstyle="round,pad=0.3", fc="white", ec=WARM, lw=1.0))

    # (2) 1D radial FFT (featureless)
    ax[1].plot(f_a, P_a / P_a[1:].max(), "-", color=WARM, label="$|a_{A1}|$ envelope")
    ax[1].plot(f_s, P_s / P_s[1:].max(), "-", color=GRY, lw=1, label="signed")
    ax[1].set_xlabel(style.axis_label("Radial spatial freq.", "k_r", "cyc/cell"))
    ax[1].set_ylabel(style.axis_label("$|$FFT$|$", "", "norm."))
    style.legend(ax[1], where="below")
    ax[1].text(0.97, 0.95, "featureless:\nno overtone ladder",
               transform=ax[1].transAxes, va="top", ha="right", fontsize=7.5,
               bbox=dict(boxstyle="round,pad=0.3", fc="white", ec=GRY, lw=1.0))

    # (3) 3D power spectrum P(|k|) (broadband)
    ax[2].plot(kcent, Pk_rad / Pk_rad[1:].max(), "-", color=COOL)
    ax[2].axvline(res["dom_k_3d"], color=COOL, ls=":", lw=1,
                  label=f"peak $\\lambda\\approx{res['lam_3d_cells']}$")
    ax[2].axvline(res["k_centroid"], color=GRY, ls="--", lw=1,
                  label=f"centroid $\\lambda_c\\approx{res['lam_centroid_cells']}$")
    ax[2].set_xlabel(style.axis_label("Spatial freq. magnitude", "|k|", "cyc/cell"))
    ax[2].set_ylabel(style.axis_label("$P(|k|)$", "", "norm."))
    style.legend(ax[2], where="below")
    ax[2].text(0.97, 0.95, f"BROADBAND\nhalf-power width $\\approx{res['k_hpwidth']}$\n"
                           "(conjugate of ~2-cell core)",
               transform=ax[2].transAxes, va="top", ha="right", fontsize=7.5,
               bbox=dict(boxstyle="round,pad=0.3", fc="white", ec=COOL, lw=1.0))

    # panel letters outside data
    for a, lab in zip(ax, ("A", "B", "C")):
        a.text(-0.12, 1.07, lab, transform=a.transAxes, fontsize=13,
               fontweight="bold", va="top", ha="right")

    written = style.save(fig, out_png, formats=("png",))
    plt.close(fig)
    return written[0]


def main() -> None:
    here = Path(__file__).resolve().parent
    out_dir = here / "_output"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_png = out_dir / "a1_spatial_cavity_mode_fft.png"
    out_json = out_dir / "a1_spatial_cavity_mode_fft.json"

    res = compute()

    print("=== A1 cavity eigenmode (on-main) ===")
    print(f"forkb_omega={res['forkb_omega']:.4f}  a1_core_frac={res['a1_core_frac']:.3f}  N={res['N']}")
    print("\n=== 1D FFT of |A1| radial envelope (SPATIAL, Ch.9 --- NOT the Ch.17 temporal FFT) ===")
    print(f"radial profile peak at r={res['r_peak_cells']} cells (single localized lobe)")
    print(f"dominant k_r = {res['dom_k_1d_abs']:.4f} cyc/cell  -> lambda = {res['lam_1d_abs']:.2f} cells")
    print(f"peaks above 25% of max: {res['npeaks_1d_abs']}  (featureless = nodeless fundamental)")
    print("\n=== 1D FFT of signed-monopole A1 ===")
    print(f"dominant k_r = {res['dom_k_1d_sig']:.4f} cyc/cell  -> lambda = {res['lam_1d_sig']:.2f} cells")
    print(f"peaks above 25% of max: {res['npeaks_1d_sig']}")
    print("\n=== 3D power spectrum P(|k|) (rigorous) ===")
    print(f"dominant |k| = {res['dom_k_3d']:.4f} cyc/cell  -> lambda = {res['lam_3d_cells']:.2f} cells")
    print(f"spectral centroid <k> = {res['k_centroid']:.4f} cyc/cell  -> lambda_c = {res['lam_centroid_cells']:.2f} cells")
    print(f"half-power width = {res['k_hpwidth']:.4f} cyc/cell  (BROADBAND --- conjugate of the ~2-cell core)")

    png = build_figure(res, out_png)
    print(f"\nsaved {png}")

    def _clean(d: dict) -> dict:
        out = {}
        for k, v in d.items():
            if isinstance(v, np.ndarray):
                out[k] = (f"<ndarray shape={v.shape} dtype={v.dtype}>"
                          if v.size > 64 else [float(x) for x in v])
            else:
                out[k] = v
        return out

    provenance = {
        "class": "CONSISTENCY (re-expresses the same on-main A1 eigenvector as Ch.3a; "
                 "not a new test/claim)",
        "distinct_from": "Ch.17 TEMPORAL ring-down FFT (omega_cutoff ~ 2.87); THIS is the "
                         "SPATIAL mode spectrum (FFT over the radial coordinate)",
        "mass_A1": "mass = A1 is the ratified grade ASSIGNMENT (PR#260), not a measurement",
        "result": "radial profile = single localized lobe (nodeless fundamental); 1D FFT "
                  "featureless (no overtones); 3D P(|k|) peak lambda~3.7 cells, centroid "
                  "lambda_c~2.2 cells, BROADBAND (conjugate of the sharp ~2-cell stiff-core "
                  "localization)",
        **_clean(res),
        "figure_png": str(png),
    }
    out_json.write_text(json.dumps(provenance, indent=2))
    print(f"== provenance JSON -> {out_json}")


if __name__ == "__main__":
    main()
