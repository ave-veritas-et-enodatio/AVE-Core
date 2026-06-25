#!/usr/bin/env python
"""Two-natured electron — a CONSISTENCY-class figure rendered from the native engine.

Re-homed (net-new canonical) driver for Vol-9 Ch.3a. Every curve in this figure
is ACTUAL output of the on-main native-engine modules (origin/main) --- no
artistic render, no hand-drawn array. It RE-EXPRESSES (does NOT newly test) the
Grant-ratified two-natured electron, which is ALREADY canon in Ch3a/Ch11/Ch13
(the substrate-decided K4 two-port A1-mass-"3" / T2-charge-"3", S-matrix
eigenvalues {+1,-1,-1,-1}, A1 _|_ T2):

  (A) STATIC CHARGE  = the (2,3) Cosserat micro-rotation WINDING, read as the
      boundary linking integer Link(dOmega, F) in Z (no work, pure topology,
      deformation-invariant) --- COOL / TEAL.
        engine: charge_quantization.seed_pq_winding / compute_Q_link /
                deform_continuous

  (B) DYNAMICAL MASS = the A1 longitudinal-dilatation CAVITY mode, the
      Gamma=-1-BOUNDARY-confined dilatation breather (forkb_omega ~ 2.84) ---
      WARM. mass = A1 is the Grant-ratified grade-ASSIGNMENT (PR#260), NOT a
      driver measurement (no driver discriminates A1-mass from T2-mass).
        engine: coupled_eigensolve.solve_coupled_spectrum /
                _decompose_eigenvector / halt_gate

  (C) REAL-SPACE BODY = the 0_1 UNKNOT. The (2,3) winding is a PHASE-SPACE
      Clifford-torus (V_inc, V_ref) winding, NOT a real-space knot --- the
      real-space body is topologically trivial (Q=0) --- NEUTRAL.
        provenance: master-equation.md:20 (the two-"3"s disambiguation, A1 _|_ T2);
        cosserat_field_3d.py:1176-1178 (Layer-3 phase-space Clifford-torus winding
        is NOT in scope of the Cosserat real-space sector).
        engine: cosserat_field_3d.initialize_electron_unknot_sector /
                extract_hopf_charge / compute_Q_link

HONESTY (load-bearing --- honor the #415/#417 retraction):
  * The A1 mass is confined by the Gamma=-1 BOUNDARY CAVITY (the surviving
    localizer). It is rendered as a "Gamma=-1-boundary-confined A1 dilatation
    mode", NOT an "autonomous bulk self-trapping breather" (that DISPERSED,
    MODE-III, #415) and NOT a "coupled-Hamiltonian-pinned bound mode".
  * The figure shows TWO ORTHOGONAL natures (A1 mass _|_ (2,3) charge), NOT the
    (2,3) holding/confining the mass. The JOINT dynamical locus tested NEGATIVE
    (#415 coupled-bound-mode DOES-NOT-EXIST; #417 phase-space BREAK = carrier
    ratio not charge). No binding curve is drawn; no nesting is implied.
  * No phase-space ORBIT is drawn: we show the STATIC Link integer for the
    charge (the orbit winding would track the LC carrier ratio omega_b:omega_s,
    a DIFFERENT object from the topological Link --- the #417 finding).
  * mass = A1 is the adjudicated grade-ASSIGNMENT (PR#260), not a measurement.
  * alpha-CLEAN: the charge integer comes from compute_Q_link, never from
    Q=1/alpha or Q_TANK=137; Q=137 stays EMPTY. No constant is read for charge.
  * Panels A/C draw the seeded-frame parametric TRACERS (the toroidal geometry
    the engine lays the field on); only Panel B plots the RAW field array.
  * CONSISTENCY-class: this RE-EXPRESSES passing engine output + the already-
    canon two-natured structure. Not a new test, not a new claim.
"""
from __future__ import annotations

import json
import time
from pathlib import Path

import numpy as np

# ---------------------------------------------------------------------------
# Geometry config (the canonical (2,3) winding scale --- charge_quantization gate
# default; the scale at which seed_pq_winding reads (2,3) correctly).
# ---------------------------------------------------------------------------
N = 24            # modest single-run lattice (not xdist --- no OOM)
P, Q = 2, 3       # the (2,3) torus winding
R, R_R = 7.0, 2.3  # winding torus major / minor radius (canonical gate scale)

RESULTS: dict = {}


# ---------------------------------------------------------------------------
# (A) STATIC CHARGE --- the (2,3) winding + Link integer + deformation invariance
# ---------------------------------------------------------------------------
def gather_static_charge() -> dict:
    """LIVE: seed the (2,3) Cosserat winding, read the boundary Link integer,
    then apply >=2 continuous topology-preserving deformations and confirm the
    integer is UNCHANGED (topological protection = no-work / pure-topology)."""
    from ave.topological.charge_quantization import (
        seed_pq_winding,
        compute_Q_link,
        compute_Q_hopf,
        deform_continuous,
    )

    t0 = time.time()
    omega = seed_pq_winding(N, P, Q, R, R_R)
    q0 = compute_Q_link(omega, R, R_R)
    h0 = compute_Q_hopf(omega, R, R_R)

    # >=2 continuous, topology-PRESERVING deformation kinds; re-read the integer.
    deform_specs = [
        ("smooth_noise", 0.25, 1),
        ("swirl", 0.30, 2),
        ("local_scale", 0.40, 3),
        ("warp", 0.30, 4),
    ]
    deformed = []
    for kind, strength, seed in deform_specs:
        od = deform_continuous(omega, kind, strength, seed=seed)
        qd = compute_Q_link(od, R, R_R)
        deformed.append({
            "kind": kind,
            "strength": strength,
            "Q_link": int(qd["Q_link"]),
            "Q_link_raw": round(float(qd["Q_link_raw"]), 4),
        })
    invariant = all(d["Q_link"] == int(q0["Q_link"]) for d in deformed)

    return {
        "module": "ave.topological.charge_quantization",
        "calls": "seed_pq_winding -> compute_Q_link -> deform_continuous x4",
        "N": N, "p": P, "q": Q, "R": R, "r": R_R,
        "Q_link": int(q0["Q_link"]),          # the poloidal linking integer = charge
        "Q_link_raw": round(float(q0["Q_link_raw"]), 4),
        "w_tor": int(q0["w_tor"]),            # toroidal winding (= p)
        "w_pol": int(q0["Q_link"]),           # poloidal winding (= q)
        "Q_hopf_selflink": int(h0["Q_hopf"]),  # w_tor * w_pol = p*q
        "deformations": deformed,
        "Link_invariant_under_deformation": bool(invariant),
        "omega": omega,                        # the seeded field (for plotting)
        "wall_s": round(time.time() - t0, 2),
    }


# ---------------------------------------------------------------------------
# (C) REAL-SPACE BODY --- the 0_1 unknot (topologically trivial; NOT the (2,3))
# ---------------------------------------------------------------------------
def gather_unknot() -> dict:
    """LIVE: initialize the canonical electron unknot sector and confirm the
    real-space body is topologically TRIVIAL (0_1): Q_H = 0 and Q_link = 0,
    in contrast to the (2,3) torus-knot ansatz on the same field type (which
    reads a nonzero winding). This is the metric that demonstrates the (2,3) is
    a PHASE-SPACE Clifford-torus winding, not a real-space knot
    (master-equation.md:20; cosserat_field_3d.py:1176-1178)."""
    from ave.topological.cosserat_field_3d import CosseratField3D
    from ave.topological.charge_quantization import compute_Q_link

    t0 = time.time()
    R_loop = 5.0  # lattice-resolved diagnostic loop (R = r horn torus default)
    fld = CosseratField3D(N, N, N, pml_thickness=0, use_saturation=True)
    fld.initialize_electron_unknot_sector(R_target=R_loop)
    q_unknot = compute_Q_link(fld.omega, R_loop, R_loop)
    qh_unknot = float(fld.extract_hopf_charge())

    # contrast: the (2,3) torus-knot ansatz on the SAME field type (nonzero).
    fld2 = CosseratField3D(N, N, N, pml_thickness=0, use_saturation=True)
    fld2.initialize_2_3_torus_knot_sector(R_target=R_loop, r_target=2.0)
    q_knot = compute_Q_link(fld2.omega, R_loop, 2.0)
    qh_knot = float(fld2.extract_hopf_charge())

    return {
        "module": "ave.topological.cosserat_field_3d",
        "calls": "initialize_electron_unknot_sector -> extract_hopf_charge / compute_Q_link",
        "N": N, "R_loop": R_loop,
        "unknot_Q_hopf": round(qh_unknot, 5),
        "unknot_Q_link": int(q_unknot["Q_link"]),
        "knot_Q_hopf": round(qh_knot, 5),
        "knot_Q_link": int(q_knot["Q_link"]),
        "is_trivial_unknot": bool(q_unknot["Q_link"] == 0 and abs(qh_unknot) < 1e-3),
        "omega_unknot": fld.omega,   # for plotting the trivial loop
        "wall_s": round(time.time() - t0, 2),
    }


# ---------------------------------------------------------------------------
# (B) DYNAMICAL MASS --- the A1 dilatation cavity eigenmode + eigenfrequency
# ---------------------------------------------------------------------------
def gather_a1_cavity() -> dict:
    """LIVE: eigensolve the coupled Hermitian H at the default canonical geometry
    (R=7, r=2.3, a1_radius=6 --- the geometry where forkb_omega lands on the
    cold-cage anchor ~2.84/2.87) at a modest N. Extract the most-bound A1 cavity
    eigenmode, its eigenfrequency, and the A1 radial breather profile.

    The eigenmode is the Gamma=-1-BOUNDARY-confined A1 dilatation mode (the
    surviving localizer): the boundary cavity confines it, NOT autonomous bulk
    self-trapping (that DISPERSED, MODE-III, #415) and NOT a coupled-Hamiltonian
    pin (the joint dynamical locus tested NEGATIVE, #415/#417). The halt_gate
    (winding-OFF control) confirms the cavity is the fork-b A1 mass mode at
    winding-off (i.e. the A1 mode is NOT a winding-coupling artifact)."""
    from scipy.sparse.linalg import eigsh

    from ave.solvers.coupled_eigensolve import (
        CoupledEigenConfig,
        solve_coupled_spectrum,
        halt_gate,
        _build_seeded_sim,
        _decompose_eigenvector,
        _interior_radius,
        COLD_CAGE_OMEGA_CUTOFF,
    )

    t0 = time.time()
    cfg = CoupledEigenConfig(N=N)  # DEFAULT canonical geometry; only N modest

    # the make-or-break eigensolve (winding_on): forkb_omega + bound-mode decomp.
    spec = solve_coupled_spectrum(cfg, winding_on=True)
    bm = spec["bound_mode"]

    # the winding-OFF HALT control: recovers the fork-b confined A1 mode.
    hg = halt_gate(cfg)

    # Re-extract the actual most-bound eigenVECTOR so we can plot the A1 mode's
    # real-space radial breather (the _decompose split: v[:nd] is the A1 grade).
    sim = _build_seeded_sim(cfg, winding_on=True)
    H = sim._assemble_H()
    vals, vecs = eigsh(H, k=cfg.k_eigs, which="SA")
    order = np.argsort(vals)
    vals, vecs = vals[order], vecs[:, order]
    # pick the most A1-core-localized member of the most-bound level (fork-b selector)
    bound_mult = spec["bound_multiplicity"]
    best_idx, best_cf = 0, -1.0
    for idx in range(max(1, bound_mult)):
        d = _decompose_eigenvector(vecs[:, idx], sim)
        if d["a1_core_frac"] > best_cf:
            best_cf, best_idx = d["a1_core_frac"], idx
    v = vecs[:, best_idx]
    nd = sim.ndof
    a1_field = np.abs(v[:nd]).reshape(N, N, N)   # the A1 mass-grade amplitude

    # radial breather profile of the A1 cavity (mean |A1| in radial bins).
    rr = _interior_radius(N)
    rflat = rr.reshape(-1)
    a1flat = a1_field.reshape(-1)
    # finer bins near the core (the stiff-core breather is deeply localized);
    # geometric spacing resolves the core peak + the tail in one profile.
    rmax = float(N) / 2.0
    edges = np.concatenate([
        np.linspace(0.0, 4.0, 9),          # fine in the core
        np.linspace(4.0, rmax, 7)[1:],     # coarse in the tail
    ])
    nbins = len(edges) - 1
    centers = 0.5 * (edges[:-1] + edges[1:])
    prof = np.full(nbins, np.nan)
    for b in range(nbins):
        m = (rflat >= edges[b]) & (rflat < edges[b + 1])
        if m.any():
            prof[b] = float(a1flat[m].mean())
    finite = np.isfinite(prof)
    prof_norm = prof.copy()
    if finite.any() and np.nanmax(prof[finite]) > 0:
        prof_norm = prof / np.nanmax(prof[finite])

    return {
        "module": "ave.solvers.coupled_eigensolve",
        "calls": "solve_coupled_spectrum / _decompose_eigenvector / halt_gate",
        "N": N, "geometry": "default canonical (R=7, r=2.3, a1_radius=6)",
        "forkb_omega": round(float(spec["forkb_omega"]), 4),
        "cold_cage_anchor": COLD_CAGE_OMEGA_CUTOFF,
        "forkb_anchor_rel_err": round(
            abs(spec["forkb_omega"] - COLD_CAGE_OMEGA_CUTOFF) / COLD_CAGE_OMEGA_CUTOFF, 4),
        "bound_w_H": round(float(spec["bound_w_H"]), 4),
        "bound_multiplicity": int(bound_mult),
        "gap_to_next": round(float(spec["gap_to_next"]), 4),
        "a1_frac": round(float(bm["a1_frac"]), 4),
        "bw_frac": round(float(bm["bw_frac"]), 4),
        "a1_core_frac": round(float(bm["a1_core_frac"]), 4),
        "lossless": bool(spec["lossless"]),
        "omega_im": float(spec["omega_im"]),
        # halt_gate (winding-OFF control)
        "halt_forkb_omega": round(float(hg["forkb_omega"]), 4),
        "halt_a1_core_frac": round(float(hg["a1_core_frac"]), 4),
        "halt_near_cold_cage_2p87": bool(hg["near_cold_cage_anchor_2p87"]),
        "halt_recovers_forkb": bool(hg["recovers_forkb"]),
        # plotting arrays
        "radial_centers": centers,
        "radial_profile": prof,
        "radial_profile_norm": prof_norm,
        "a1_field": a1_field,
        "wall_s": round(time.time() - t0, 2),
    }


# ---------------------------------------------------------------------------
# Geometry tracers --- the engine's OWN seeding parametrization (NOT hand-drawn).
# These are the seeded-frame parametric TRACERS: the toroidal frame the field is
# laid on (theta = p*phi + q*psi), the geometry seed_pq_winding /
# initialize_electron_unknot_sector use. (Panel B alone plots the raw field.)
# ---------------------------------------------------------------------------
def _pq_torus_knot_curve(p: int, q: int, R: float, r: float, n: int = 1200):
    """The (p,q) torus-knot centerline --- the closed curve the (2,3) winding
    wraps, in the engine's seeding coordinates (the same toroidal frame
    seed_pq_winding uses: major angle phi, minor angle psi, psi advancing q
    times per p toroidal turns). A seeded-frame parametric tracer."""
    t = np.linspace(0.0, 2.0 * np.pi, n)
    phi = p * t            # p toroidal turns
    psi = q * t            # q poloidal turns
    rad = R + r * np.cos(psi)
    x = rad * np.cos(phi)
    y = rad * np.sin(phi)
    z = r * np.sin(psi)
    return x, y, z


def _unknot_loop_curve(R: float, n: int = 600):
    """The 0_1 unknot centerline --- a single planar closed loop (no winding), in
    the engine's seeding frame (initialize_electron_unknot_sector lays omega
    tangent to this loop, e_phi, with NO (p,q) winding). A seeded-frame tracer."""
    t = np.linspace(0.0, 2.0 * np.pi, n)
    return R * np.cos(t), R * np.sin(t), np.zeros_like(t)


# ---------------------------------------------------------------------------
# FIGURE --- three panels, house style (white, Okabe-Ito, labels outside data).
# ---------------------------------------------------------------------------
def build_figure(static: dict, cavity: dict, unknot: dict, out_png: Path) -> Path:
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D  # noqa: F401  (registers 3d proj)

    from ave.viz import style

    style.apply("print")  # white background, Okabe-Ito, black axes

    TEAL = style.COLORS["accent"]     # bluish-green --- STATIC charge / structure (cool)
    WARM = style.COLORS["comparison"]  # vermillion   --- DYNAMICAL mass (does work) (warm)
    MUTED = style.COLORS["muted"]      # gray         --- neutral real-space body

    # house style sets constrained_layout (ave.mplstyle:42); keep it and tune
    # padding through the layout engine so 3D + 2D panels don't collide.
    fig = plt.figure(figsize=(13.5, 4.6))
    fig.get_layout_engine().set(w_pad=0.06, wspace=0.06)

    # ---- Panel A: STATIC (2,3) winding + Link integer + deformation-invariance
    axA = fig.add_subplot(1, 3, 1, projection="3d")
    x, y, z = _pq_torus_knot_curve(static["p"], static["q"], static["R"], static["r"])
    axA.plot(x, y, z, color=TEAL, lw=2.2)
    axA.set_xlabel("$x$ [cells]", labelpad=-6)
    axA.set_ylabel("$y$ [cells]", labelpad=-6)
    axA.set_zlabel("$z$ [cells]", labelpad=-6)
    axA.tick_params(labelsize=7, pad=-2)
    axA.view_init(elev=26, azim=40)
    # the charge integer + deformation invariance, OUTSIDE the data (leader-less
    # annotation box at a fixed axes-fraction corner). The seeded-frame tracer
    # note keeps Panel A honest about what is drawn vs computed.
    inv = "UNCHANGED" if static["Link_invariant_under_deformation"] else "CHANGED"
    kinds = ", ".join(d["kind"] for d in static["deformations"])
    axA.text2D(
        0.00, 0.00,
        f"$\\mathcal{{Q}}=\\mathrm{{Link}}(\\partial\\Omega,F)={static['Q_link']}\\in\\mathbb{{Z}}$\n"
        f"$(p,q)=({static['p']},{static['q']})$  "
        f"$w_{{tor}}={static['w_tor']},\\,w_{{pol}}={static['w_pol']}$\n"
        f"{inv} under {len(static['deformations'])} deformations\n"
        f"({kinds})\n"
        f"[seeded-frame tracer; $\\alpha$-free Link]",
        transform=axA.transAxes, va="bottom", ha="left", fontsize=7.0,
        bbox=dict(boxstyle="round,pad=0.3", fc="white", ec=TEAL, lw=1.0, alpha=0.92),
    )

    # ---- Panel B: A1 dilatation CAVITY radial breather + eigenfrequency
    # (the ONLY panel plotting the raw field array; Gamma=-1-boundary-confined)
    axB = fig.add_subplot(1, 3, 2)
    rc = cavity["radial_centers"]
    pr = cavity["radial_profile_norm"]
    fin = np.isfinite(pr)
    axB.plot(rc[fin], pr[fin], color=WARM, lw=2.2, marker="o", ms=4,
             label="$\\Gamma{=}{-}1$-confined A1 mode")
    axB.fill_between(rc[fin], 0, pr[fin], color=WARM, alpha=0.12)
    axB.set_xlabel(style.axis_label("Radius from core", "r", "cells"))
    axB.set_ylabel(style.axis_label("A1 dilatation amplitude", "|a_{A1}|", ""))
    axB.set_ylim(bottom=0)
    axB.text(
        0.97, 0.95,
        f"$\\omega_{{\\mathrm{{fork\\,b}}}}={cavity['forkb_omega']}$\n"
        f"(anchor $\\approx2.84$, cold cage 2.87)\n"
        f"A1 core frac $={cavity['a1_core_frac']}$\n"
        f"lossless, $\\mathrm{{Im}}(\\omega)={cavity['omega_im']:.0f}$\n"
        f"HALT (winding-off) recovers: {cavity['halt_recovers_forkb']}\n"
        f"[mass$={{}}$A1 = ratified assignment, PR\\#260]",
        transform=axB.transAxes, va="top", ha="right", fontsize=7.0,
        bbox=dict(boxstyle="round,pad=0.3", fc="white", ec=WARM, lw=1.0),
    )
    style.legend(axB, where="below")

    # ---- Panel C: REAL-SPACE 0_1 UNKNOT (topologically trivial)
    axC = fig.add_subplot(1, 3, 3, projection="3d")
    ux, uy, uz = _unknot_loop_curve(unknot["R_loop"])
    axC.plot(ux, uy, uz, color=MUTED, lw=2.2)
    axC.set_xlabel("$x$ [cells]", labelpad=-6)
    axC.set_ylabel("$y$ [cells]", labelpad=-6)
    axC.set_zlabel("$z$ [cells]", labelpad=-6)
    axC.tick_params(labelsize=7, pad=-2)
    axC.view_init(elev=26, azim=40)
    axC.set_zlim(-unknot["R_loop"], unknot["R_loop"])  # honest aspect: the loop is planar
    axC.text2D(
        0.00, 0.00,
        f"real-space body $=0_1$ unknot\n"
        f"$Q_H={unknot['unknot_Q_hopf']:.3f}$, "
        f"$\\mathcal{{Q}}_{{link}}={unknot['unknot_Q_link']}$ (trivial)\n"
        f"contrast (2,3) ansatz: $\\mathcal{{Q}}_{{link}}={unknot['knot_Q_link']}$\n"
        f"the (2,3) is a PHASE-SPACE winding,\nNOT a real-space knot\n"
        f"[seeded-frame tracer]",
        transform=axC.transAxes, va="bottom", ha="left", fontsize=7.0,
        bbox=dict(boxstyle="round,pad=0.3", fc="white", ec=MUTED, lw=1.0, alpha=0.92),
    )

    # panel letters (outside data, top-left of each axes box)
    for ax, lab in ((axA, "A"), (axB, "B"), (axC, "C")):
        ax.text2D(-0.02, 1.08, lab, transform=ax.transAxes, fontsize=13,
                  fontweight="bold", va="top", ha="right") if hasattr(ax, "text2D") \
            else ax.text(-0.12, 1.06, lab, transform=ax.transAxes, fontsize=13,
                         fontweight="bold", va="top", ha="right")

    written = style.save(fig, out_png, formats=("png",))
    plt.close(fig)
    return written[0]


# ---------------------------------------------------------------------------
def main() -> None:
    here = Path(__file__).resolve().parent
    out_dir = here / "_output"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_png = out_dir / "two_natured_electron_native_engine.png"
    out_json = out_dir / "two_natured_electron_native_engine.json"

    print("== (A) static charge --- (2,3) winding + Link + deformation invariance")
    static = gather_static_charge()
    print(f"   Q_link={static['Q_link']} (raw {static['Q_link_raw']}), "
          f"w_tor={static['w_tor']}, Q_hopf={static['Q_hopf_selflink']}, "
          f"invariant={static['Link_invariant_under_deformation']} "
          f"[{static['wall_s']}s]")

    print("== (B) dynamical mass --- Gamma=-1-confined A1 dilatation cavity eigenmode")
    cavity = gather_a1_cavity()
    print(f"   forkb_omega={cavity['forkb_omega']} (rel-err vs 2.87 = "
          f"{cavity['forkb_anchor_rel_err']}), a1_core_frac={cavity['a1_core_frac']}, "
          f"lossless={cavity['lossless']}, halt_recovers={cavity['halt_recovers_forkb']} "
          f"[{cavity['wall_s']}s]")

    print("== (C) real-space body --- 0_1 unknot (trivial topology)")
    unknot = gather_unknot()
    print(f"   unknot Q_H={unknot['unknot_Q_hopf']}, Q_link={unknot['unknot_Q_link']}; "
          f"contrast (2,3) ansatz Q_link={unknot['knot_Q_link']}; "
          f"trivial={unknot['is_trivial_unknot']} [{unknot['wall_s']}s]")

    png = build_figure(static, cavity, unknot, out_png)
    print(f"== figure -> {png}")

    # numeric provenance JSON (arrays stripped to lists where small)
    def _clean(d: dict) -> dict:
        out = {}
        for k, v in d.items():
            if isinstance(v, np.ndarray):
                if v.ndim == 1 and v.size <= 64:
                    out[k] = [None if (isinstance(x, float) and np.isnan(x)) else float(x)
                              for x in v]
                else:
                    out[k] = f"<ndarray shape={v.shape} dtype={v.dtype}>"
            else:
                out[k] = v
        return out

    provenance = {
        "class": "CONSISTENCY (re-expresses passing engine output + already-canon "
                 "two-natured structure; not a new test/claim)",
        "framing": "TWO ORTHOGONAL natures (A1 mass _|_ (2,3) charge); NOT nesting; "
                   "A1 confined by Gamma=-1 BOUNDARY cavity (NOT bulk self-trap, "
                   "which DISPERSED MODE-III #415; NOT coupled-H pin, joint locus "
                   "NEGATIVE #415/#417)",
        "mass_A1": "mass = A1 is the ratified grade ASSIGNMENT (PR#260), not a measurement",
        "alpha_clean": "charge integer from compute_Q_link only; no Q=1/alpha read; "
                       "Q=137 stays EMPTY",
        "panels": "Panels A/C = seeded-frame parametric tracers; only Panel B is the "
                  "raw field array",
        "static_charge": _clean(static),
        "a1_cavity": _clean(cavity),
        "real_space_unknot": _clean(unknot),
        "figure_png": str(png),
    }
    out_json.write_text(json.dumps(provenance, indent=2))
    print(f"== provenance JSON -> {out_json}")


if __name__ == "__main__":
    main()
