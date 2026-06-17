"""L2 — EM in a biased medium (Axiom-4 operating-point / varactor modulation).

Each test below is a falsifiable physics CLAIM with a PRE-REGISTERED pass/fail
bin in its docstring (frozen BEFORE running). The medium is the canonical
EM-sector varactor (eps_eff=eps0*S(A0), mu_eff=mu0*S(A0), C_eff=C0/S) built on
the SAME canonical bond-LC / Z0 / c0 the L0 medium (T0.2) validates; the kernel
S(A)=sqrt(1-A^2) and the eps0/mu0/Z0/c0 constants are IMPORTED from
ave.core.constants (ave-canonical-source) — never hard-coded. The varactor forms
and the SYM/ASYM split are read off the canonical KB:
  * S(A)=sqrt(1-A^2)                         constants.py:46; master_equation_fdtd.py:11
  * eps_eff=eps0*S, mu_eff=mu0*S, C_eff=C0/S CLAUDE.md:58,60; cvr-dc-operating-point.md:22-29
  * c_EM=c0/S, Z_EM=Z0*sqrt(S_mu/S_eps)      CLAUDE.md:64; cvr §2 (clm-8nkvwy:111)
  * SYM (Z=Z0, Gamma=0) vs ASYM (E-only)     CLAUDE.md:60 (W6 2026-06-05)
  * alpha-invariance under SYM via c_EM       CLAUDE.md:69-71 (clm-3zz0f6, solidity 0.85)

phase-space-coordinate-check (A46): the L2 corpus claims live in the EM-sector
IMPEDANCE-PLANE / phase-velocity coordinates (c_EM, Z_EM, Gamma, group delay vs
frequency). The 1D graded EM line in `_em_media.py` measures in EXACTLY those
coordinates. (The 3D irregular srs vector-TLM was checked and REJECTED as the L2
substrate: a localized index step washes out in the centroid speed there, and the
corpus claim is not a 3D-real-space lattice claim — verified empirically
2026-06-17. The faithful substrate is the canonical-bond-LC graded line.)

────────────────────────────────────────────────────────────────────────────────
LOAD-BEARING FINDING surfaced at design time (flag-don't-fix, Operating Principle 6)
────────────────────────────────────────────────────────────────────────────────
The orchestration brief's T2.1 phrasing ("n=1/S(A0); a packet measurably SLOWS
inside it") does NOT match the canonical EM/TRANSVERSE-sector convention. The
canonical Maxwell phase velocity is c_EM = c0/S(A0) (CLAUDE.md:64,
cvr-dc-operating-point.md:28), which with S<1 SPEEDS the packet UP (c_EM>c0); the
EM-sector refractive index is therefore n_EM = c0/c_EM = S(A0) < 1, NOT 1/S. The
"1/S" in the brief IS the canonical c_EM/c0 RATIO (and the C_eff/C0 LONGITUDINAL
varactor), but it is the SPEED ratio, not the refractive index, and the EM packet
ADVANCES rather than slows. The sector that SLOWS is the mechanical/shear sector
c_shear=c0*sqrt(S) (the rest-mass / Schwarzschild-reduction clock), which is
ORTHOGONAL to the transverse photon (master-equation.md:20; the genesis-24
double-count warning). These tests measure the TRANSVERSE photon, so they assert
the canonical c_EM=c0/S (advance), and the sign is reported honestly. This is the
AVE-distinct content: an EM probe through a SYM-biased region is ADVANCED, while a
matter clock in the same region is RETARDED — same operating point, opposite-sign
delay in the two sectors.
"""

from __future__ import annotations

import numpy as np

from ave.core.constants import EPSILON_0, C_0, Z_0

from . import _em_media as EM
from . import _viz as VZ


# ─────────────────────────────────────────────────────────────────────────────
# T2.1 — refractive index: a region at A0 modulates c_EM = c0/S(A0)
# ─────────────────────────────────────────────────────────────────────────────
def test_t2_1_refractive_index():
    """T2.1 [CONSISTENCY] — a region at operating-point A0 has c_EM = c0/S(A0).

    A region biased to A0 (SYM) sees the canonical EM varactor eps_eff=eps0*S,
    mu_eff=mu0*S, so its Maxwell phase velocity is c_EM = 1/sqrt(mu_eff eps_eff)
    = c0/S(A0) and its EM refractive index is n_EM = c0/c_EM = S(A0). A tone
    burst measurably CHANGES SLOPE in the biased region (it ADVANCES — c_EM>c0 —
    per the canonical EM convention; see the module FINDING). Visual: the x-t
    spacetime shows the packet change slope crossing the region boundary.

    Inputs (consistency-vs-emergence): kernel S(A) [Axiom 4, constants.py:46] +
    canonical eps0/mu0/c0 [ave.core.constants]. CONSISTENCY: reproduces the
    refractive-index relation via the canonical varactor mechanism; not an
    emergence (no forced dimensionless number).

    PRE-REGISTERED BINS (frozen before run):
      * PASS : the analytic EM-sector relations hold to < 1e-9 relative —
               c_EM/c0 == 1/S(A0) AND n_EM == S(A0) AND Z_EM == Z0 (SYM) —
               AND the time-domain packet's in-region phase-front slope differs
               from the cold-lattice slope in the SLOWING^-1 (advancing) sense by
               the predicted factor 1/S to within 8% (discrete-grid tolerance).
      * FAIL : analytic relations off by >= 1e-9, OR the measured in-region speed
               ratio is not the predicted 1/S(A0) to within 8% (no measurable
               index change, or the wrong sense/magnitude).
      * Report the measured in-region vs cold phase-velocity ratio regardless.
    """
    EM.assert_canonical_constants()
    # medium grounding: the L2 varactor builds on the SAME canonical bond-LC Z0
    # the L0 medium (T0.2) validates — confirm the link (ave-canonical-source).
    assert abs(EM.bond_lc_z0() - Z_0) / Z_0 < 1e-12, "L2 medium Z0 != canonical bond-LC Z0"
    A0 = 0.7
    S = float(EM.S_of_A(A0))
    p = EM.em_params(A0, A0)  # SYM region

    # analytic EM-sector relations
    c_ratio = float(p["c_EM"]) / C_0
    n_em = float(p["n_EM"])
    z_ratio = float(p["Z_EM"]) / Z_0
    rel_c = abs(c_ratio - 1.0 / S)
    rel_n = abs(n_em - S)
    rel_z = abs(z_ratio - 1.0)

    # time-domain: measure the in-region phase velocity from the x-t band slope.
    # Use the ENERGY-CENTROID trajectory (robust; the argmax peak is noisy under
    # the global-dt leapfrog), windowed by where the centroid sits (cold vs region).
    N = 600
    region = (250, 420)
    A_eps = np.zeros(N)
    A_mu = np.zeros(N)
    A_eps[region[0]:region[1]] = A0
    A_mu[region[0]:region[1]] = A0  # SYM
    line = EM.run_em_line(N, A_eps, A_mu, 1100, freq=0.05, src=12, record_every=2)
    st = line["spacetime"]
    times = line["times"]
    idx = np.arange(N)
    cen = np.array([
        (np.sum(idx * f) / f.sum()) if f.sum() > 1e-12 else np.nan for f in st
    ])
    valid = ~np.isnan(cen)
    # cold window: centroid well left of the region (and past the launch transient);
    # in-region window: centroid inside the region (with a margin off each edge).
    cold = valid & (cen > 30) & (cen < region[0] - 20)
    inreg = valid & (cen > region[0] + 15) & (cen < region[1] - 15)

    def _slope(mask):
        if mask.sum() < 5:
            return np.nan
        return float(np.polyfit(times[mask], cen[mask], 1)[0])

    v_cold = _slope(cold)
    v_reg = _slope(inreg)
    speed_ratio = v_reg / v_cold if (v_cold and not np.isnan(v_reg) and not np.isnan(v_cold)) else np.nan
    pred_ratio = 1.0 / S
    rel_speed = abs(speed_ratio / pred_ratio - 1.0) if not np.isnan(speed_ratio) else 9.99

    print(f"\n--- T2.1 refractive index (EM varactor, A0={A0}, S={S:.4f}) ---")
    print(f"  c_EM/c0 = 1/S  : {c_ratio:.6f}  (pred {1.0 / S:.6f}, rel {rel_c:.2e})")
    print(f"  n_EM    = S    : {n_em:.6f}  (pred {S:.6f}, rel {rel_n:.2e})")
    print(f"  Z_EM/Z0 (SYM)  : {z_ratio:.6f}  (pred 1.0, rel {rel_z:.2e})")
    print(f"  measured x-t slope: cold v={v_cold:.4f}  in-region v={v_reg:.4f}")
    print(f"  speed ratio in/cold = {speed_ratio:.4f}  (pred 1/S = {pred_ratio:.4f}, rel {rel_speed:.3f}, PASS<0.08)")
    print("  FINDING: EM-sector packet ADVANCES (c_EM=c0/S>c0); shear sector would slow (c_shear=c0*sqrt(S))")

    assert rel_c < 1e-9, f"FAIL: c_EM/c0 != 1/S — rel {rel_c:.2e}"
    assert rel_n < 1e-9, f"FAIL: n_EM != S — rel {rel_n:.2e}"
    assert rel_z < 1e-9, f"FAIL: Z_EM != Z0 under SYM — rel {rel_z:.2e}"
    assert not np.isnan(speed_ratio), "FAIL: could not measure in-region phase velocity"
    assert rel_speed < 0.08, (
        f"FAIL: measured in-region speed ratio {speed_ratio:.4f} off 1/S {pred_ratio:.4f} by > 8%"
    )

    if VZ.viz_enabled():
        def _draw(fig):
            ax1, ax2 = fig.subplots(1, 2)
            VZ._panel_em_spacetime(ax1, line, region=region,
                                   title=f"x-t: packet slope change at A0={A0} region (c_EM=c0/S)")
            # overlay the measured energy-centroid trajectory
            ax1.plot(cen[valid], times[valid], color="cyan", lw=0.9, ls=":",
                     label="energy centroid")
            ax1.legend(loc="upper left", fontsize=7, framealpha=0.5)
            A_grid = np.linspace(0.0, 0.95, 200)
            ax2.plot(A_grid, 1.0 / EM.S_of_A(A_grid), label="c_EM/c0 = 1/S (EM, advances)")
            ax2.plot(A_grid, EM.S_of_A(A_grid), label="n_EM = S (<1)")
            ax2.plot(A_grid, np.sqrt(EM.S_of_A(A_grid)), ls="--",
                     label="c_shear/c0 = sqrt(S) (matter, slows)")
            ax2.axvline(A0, color="k", ls=":", lw=0.8)
            ax2.set_xlabel("operating point A0")
            ax2.set_ylabel("ratio to cold lattice")
            ax2.set_title("EM varactor characteristic (canonical)")
            ax2.legend(fontsize=8)
        path = VZ.save_l2_figure("T2.1", "refractive index — c_EM = c0/S(A0)", _draw)
        print(f"  [viz] refractive-index figure -> {path}")


# ─────────────────────────────────────────────────────────────────────────────
# T2.2 — ACHROMATIC LENSING (the headline; the gravity bridge)
# ─────────────────────────────────────────────────────────────────────────────
def test_t2_2_achromatic_lensing():
    """T2.2 [CONSISTENCY-of-MECHANISM, HEADLINE] — a SYM gradient deflects/retards
    a wave FREQUENCY-INDEPENDENTLY, with Z matched (Gamma=0).

    A SYM gradient (eps and mu co-scaled, S_eps=S_mu=S(A0(x))) keeps the impedance
    Z_EM = Z0*sqrt(S/S) = Z0 INVARIANT across the gradient (-> Gamma=0,
    reflectionless) while c_EM=c0/S(A0(x)) varies. Because c_EM depends ONLY on the
    operating point A0 and has NO frequency dependence, the deflection/retardation
    is the SAME for every frequency in the band — the AVE-DISTINCT mechanism for
    gravitational lensing (achromatic, unlike any chromatic dielectric).

    Acceptance, two parts:
      (i)  the excess group delay (the retardation a probe accrues crossing the
           gradient) is EQUAL across the frequency band (achromatic), and equals
           the path-integral prediction sum dx (1/c_EM - 1/c0) [frequency-independent];
      (ii) Z stays matched across the gradient -> Gamma ~ 0 (no spurious reflection).

    consistency-vs-emergence: CONSISTENCY-of-MECHANISM (reproduces achromatic
    lensing). The deflection MAGNITUDE is FORM-DERIVED (the path integral of
    (1/c_EM-1/c0)=(S-1)/c0 over the profile), NOT a fitted number; per the brief,
    if the magnitude turned out forced/non-fit it would be FLAGGED as a
    CHORD-candidate, NOT asserted. We assert only the achromaticity + match
    (consistency); the magnitude is reported, and the chord question is left OPEN
    (the form is derived but the dimensionful value rides the operating-point A0(x)
    profile, which is an input here — not a forced dimensionless number).

    PRE-REGISTERED BINS (frozen before run):
      * PASS : (i) relative spread of the excess group delay across the band
                   (w in [0.08, 0.45]) < 1e-3 (achromatic) AND it matches the
                   path-integral prediction to < 1e-3 relative;
               (ii) max |Gamma| across the band < 1e-6 (SYM reflectionless).
      * FAIL : group-delay spread >= 1e-3 (CHROMATIC — would falsify the
               achromatic mechanism) OR |Gamma| >= 1e-6 (SYM not reflectionless).
      * Report the deflection magnitude (group delay) and its frequency spread.
    """
    EM.assert_canonical_constants()
    A0 = 0.7
    N = 120
    dx = 1.0
    # smooth SYM gradient (Gaussian bump in the operating point)
    x = (np.arange(N) - N / 2) / (N * 0.18)
    prof = A0 * np.exp(-x * x)
    w_grid = np.linspace(0.05, 0.5, 40)
    gd, gam, path_pred = EM.group_delay_excess(prof, prof, dx, w_grid)  # SYM

    band = (w_grid > 0.08) & (w_grid < 0.45)
    gd_band = gd[band]
    gd_mean = float(gd_band.mean())
    gd_spread = float(gd_band.std() / abs(gd_mean)) if gd_mean != 0 else 9.99
    rel_pred = abs(gd_mean / path_pred - 1.0)
    gamma_max = float(gam.max())

    print(f"\n--- T2.2 ACHROMATIC LENSING (SYM gradient, A0_peak={A0}) ---")
    print(f"  excess group delay (deflection): mean {gd_mean:+.5f}  [normalized cell·step units]")
    print(f"      path-integral prediction    : {path_pred:+.5f}  (freq-INDEPENDENT, rel {rel_pred:.2e})")
    print(f"      frequency spread across band: {gd_spread:.3e}   (PASS < 1e-3 = ACHROMATIC)")
    print(f"  (ii) max |Gamma| across band    : {gamma_max:.3e}   (PASS < 1e-6 = SYM reflectionless)")
    print("  -> deflection is FREQUENCY-INDEPENDENT (achromatic) AND Z-matched. The AVE-distinct")
    print("     gravitational-lensing mechanism. Magnitude is FORM-derived (∫(S-1)dx); chord-vs-echo")
    print("     of the MAGNITUDE is OPEN (rides the A0(x) profile, an input) -> NOT asserted as a chord.")

    # (i) achromaticity + path-integral match
    assert gd_spread < 1e-3, (
        f"FAIL: deflection is CHROMATIC — group-delay spread {gd_spread:.3e} >= 1e-3"
    )
    assert rel_pred < 1e-3, (
        f"FAIL: group delay {gd_mean:.5f} != path-integral {path_pred:.5f} (rel {rel_pred:.2e})"
    )
    # (ii) reflectionless
    assert gamma_max < 1e-6, (
        f"FAIL: SYM gradient NOT reflectionless — max |Gamma| {gamma_max:.3e} >= 1e-6"
    )

    if VZ.viz_enabled():
        # the x-t render of a wave traversing the SYM gradient (no reflection)
        N_t = 600
        prof_t = A0 * np.exp(-(((np.arange(N_t) - N_t / 2) / (N_t * 0.12)) ** 2))
        line = EM.run_em_line(N_t, prof_t, prof_t, 900, freq=0.06, src=12)

        def _draw(fig):
            ax1, ax2 = fig.subplots(1, 2)
            # the flat-line achromaticity plot (deflection vs frequency)
            ax1.plot(w_grid, gd, "o-", color="#2ca02c", ms=3,
                     label="excess group delay (deflection)")
            ax1.axhline(path_pred, color="k", ls="--", lw=1.0,
                        label=f"path-integral pred {path_pred:.3f} (freq-indep)")
            ax1.set_xlabel("angular frequency w (rad/step)")
            ax1.set_ylabel("excess group delay (deflection)")
            ax1.set_title(f"ACHROMATIC: spread {gd_spread:.1e} (flat = achromatic)")
            ax1.legend(fontsize=8)
            ax12 = ax1.twinx()
            ax12.plot(w_grid, np.maximum(gam, 1e-18), color="#d62728", lw=0.8)
            ax12.set_yscale("log")
            ax12.set_ylabel("|Gamma| (log) — SYM reflectionless", color="#d62728")
            VZ._panel_em_spacetime(ax2, line,
                                   title="x-t: wave traverses SYM gradient (Gamma=0, no reflection)")
        path = VZ.save_l2_figure(
            "T2.2", "ACHROMATIC LENSING — deflection vs frequency (flat) + x-t", _draw)
        print(f"  [viz] achromatic-lensing figure -> {path}")


# ─────────────────────────────────────────────────────────────────────────────
# T2.3 — asymmetric mirror: static-E-only bias -> Z change -> Gamma != 0
# ─────────────────────────────────────────────────────────────────────────────
def test_t2_3_asymmetric_mirror():
    """T2.3 [CONSISTENCY] — a static-E-only (asymmetric) bias loads eps only ->
    Z changes -> Gamma != 0 (the vacuum-impedance mirror).

    A static-E-only drive has no dB/dt to load the mu / micro-rotational sector,
    so it loads eps only: S_eps=S(A0), S_mu=1 (CLAUDE.md:60, W6 2026-06-05). Then
    Z_EM = Z0*sqrt(S_mu/S_eps) = Z0/sqrt(S) != Z0 -> the boundary reflects
    (Gamma != 0): the Op14 Meissner-asymmetric vacuum-impedance mirror (Vol 4
    Ch 11). This CONTRASTS with T2.2's reflectionless SYM case (Z=Z0, Gamma=0).

    CP10 (boundary-not-bulk): the mirror is rendered as the BOUNDARY reflection
    Gamma=(Z2-Z1)/(Z2+Z1) at the impedance step, R=Gamma^2 bounded <= 1 — NOT a
    bulk confining force.

    PRE-REGISTERED BINS (frozen before run):
      * PASS : the analytic ASYM step Gamma = (Z_EM - Z0)/(Z_EM + Z0) with
               Z_EM = Z0/sqrt(S(A0)) is NONZERO (|Gamma| > 0.10 at A0=0.9) AND the
               time-domain flux-split reflected fraction at a sharp ASYM step is
               within a factor 2 of the analytic R AND is >= 5x the SYM-control
               reflected fraction (which sits at the grid back-scatter floor).
               i.e. ASYM reflects, SYM does not.
      * FAIL : ASYM |Gamma| <= 0.10 (no mirror) OR the time-domain ASYM/SYM
               reflection contrast < 5x (the contrast collapses) OR the measured
               ASYM reflection is not within 2x of analytic R.
      * Report the ASYM Gamma, R, and the measured reflected fractions.
    """
    EM.assert_canonical_constants()
    A0 = 0.9
    S = float(EM.S_of_A(A0))
    p_asym = EM.em_params(A0, 0.0)   # E-only: S_eps=S, S_mu=1
    p_sym = EM.em_params(A0, A0)     # control: SYM
    z_asym = float(p_asym["Z_EM"]) / Z_0
    z_sym = float(p_sym["Z_EM"]) / Z_0
    gamma_asym = EM.gamma_step(1.0, z_asym)
    gamma_sym = EM.gamma_step(1.0, z_sym)
    R_asym = gamma_asym ** 2

    # time-domain: flux-split reflected fraction off a sharp E-only step vs SYM step
    N = 900
    step = 500

    def _refl(A_eps_r, A_mu_r):
        A_eps = np.zeros(N)
        A_mu = np.zeros(N)
        A_eps[step:] = A_eps_r
        A_mu[step:] = A_mu_r
        return EM.reflected_fraction_flux(N, A_eps, A_mu, 2800, freq=0.06,
                                          src=12, probe=250)

    refl_asym = _refl(A0, 0.0)   # E-only step
    refl_sym = _refl(A0, A0)     # SYM step (control)
    contrast = refl_asym / (refl_sym + 1e-9)
    rel_R = refl_asym / R_asym if R_asym > 0 else 9.99

    print(f"\n--- T2.3 asymmetric mirror (A0={A0}, S={S:.4f}) ---")
    print(f"  ASYM (E-only): Z_EM/Z0 = 1/sqrt(S) = {z_asym:.4f}  Gamma = {gamma_asym:+.4f}  R=Gamma^2={R_asym:.4f}")
    print(f"  SYM  control : Z_EM/Z0 = {z_sym:.4f}  Gamma = {gamma_sym:+.2e} (reflectionless)")
    print(f"  flux-split reflected fraction: ASYM {refl_asym:.4f}  vs  SYM {refl_sym:.4f}")
    print(f"      ASYM/analytic-R = {rel_R:.2f} (PASS 0.5..2);  ASYM/SYM contrast = {contrast:.1f}x (PASS >= 5)")

    assert abs(gamma_asym) > 0.10, (
        f"FAIL: ASYM bias gives no mirror — |Gamma| {abs(gamma_asym):.4f} <= 0.10"
    )
    assert abs(gamma_sym) < 1e-9, (
        f"FAIL: SYM control is not reflectionless — |Gamma| {abs(gamma_sym):.2e}"
    )
    assert 0.5 < rel_R < 2.0, (
        f"FAIL: measured ASYM reflection {refl_asym:.4f} not within 2x of analytic R {R_asym:.4f}"
    )
    assert contrast >= 5.0, (
        f"FAIL: contrast collapsed — ASYM {refl_asym:.4f} not >= 5x SYM {refl_sym:.4f} ({contrast:.1f}x)"
    )

    if VZ.viz_enabled():
        A_eps = np.zeros(N)
        A_mu = np.zeros(N)
        A_eps[step:] = A0  # E-only step
        line = EM.run_em_line(N, A_eps, A_mu, 2200, freq=0.06, src=12)

        def _draw(fig):
            ax1, ax2 = fig.subplots(1, 2)
            VZ._panel_em_spacetime(ax1, line, region=(step, N),
                                   title="x-t: ASYM (E-only) step — incident + REFLECTED bounce")
            labels = ["SYM\n(Z=Z0)", "ASYM E-only\n(Z=Z0/√S)"]
            zr = [z_sym, z_asym]
            gr = [abs(gamma_sym), abs(gamma_asym)]
            xb = np.arange(2)
            ax2.bar(xb - 0.2, zr, 0.4, label="Z_EM/Z0", color="#1f77b4")
            ax2.bar(xb + 0.2, gr, 0.4, label="|Gamma|", color="#d62728")
            ax2.axhline(1.0, color="k", ls=":", lw=0.8)
            ax2.set_xticks(xb)
            ax2.set_xticklabels(labels)
            ax2.set_title("Z mismatch -> Gamma (ASYM mirror vs SYM matched)")
            ax2.legend(fontsize=8)
            for i, (z, g) in enumerate(zip(zr, gr)):
                ax2.annotate(f"Z={z:.3f}\n|Γ|={g:.3f}", xy=(i, max(z, g)),
                             xytext=(0, 4), textcoords="offset points",
                             ha="center", fontsize=8)
        path = VZ.save_l2_figure("T2.3", "asymmetric mirror — Z mismatch reflects (vs SYM matched)", _draw)
        print(f"  [viz] asymmetric-mirror figure -> {path}")


# ─────────────────────────────────────────────────────────────────────────────
# T2.4 — alpha-invariance under SYM scaling (the canonical claim)
# ─────────────────────────────────────────────────────────────────────────────
def test_t2_4_alpha_invariance_sym():
    """T2.4 [CONSISTENCY of the canonical claim clm-3zz0f6] — alpha is invariant
    under SYM scaling because c_EM (=c0/S) enters alpha, NOT c_shear (=c0*sqrt(S)).

    Under SYM, eps_eff=eps0*S and c_EM=c0/S, so in alpha = e^2/(4 pi eps_eff hbar
    c_EM) the product eps_eff*c_EM = (eps0*S)(c0/S) = eps0*c0 — the S CANCELS and
    alpha(A0) = alpha0 EXACTLY across an A0 sweep (CLAUDE.md:69; clm-3zz0f6,
    solidity 0.85). The canonical discipline (INVARIANT-S2 / clm-3zz0f6, the
    Phase-3-A3 walk-back) is: use c_EM, NOT c_shear. Substituting c_shear=c0*sqrt(S)
    gives the WRONG alpha_eff/alpha0 = 1/S^{3/2} != 1 — the category error, checked
    here as a NEGATIVE CONTROL so the test cannot pass for the wrong reason.

    consistency-vs-emergence: CONSISTENCY of the canonical claim — alpha itself is
    a calibration identity (the alpha-keystone is an ECHO at value level); this
    test confirms the SYM-invariance STRUCTURE (eps_eff*c_EM = eps0*c0), it does
    NOT derive alpha. The ratio alpha(A0)/alpha0 is computed from the canonical
    eps0,c0 + kernel S(A); no CODATA alpha is used as input (the e, hbar, 4pi
    cancel in the ratio), so this is a structural identity check, not an emergence.

    PRE-REGISTERED BINS (frozen before run):
      * PASS : alpha(A0)/alpha0 == 1 to < 1e-12 for EVERY A0 in the sweep
               {0, 0.3, 0.5, 0.7, 0.9} when c_EM is used; AND the c_shear
               negative control gives 1/S^{3/2} (DEVIATES from 1 by > 1e-3 for
               A0 >= 0.3) — confirming the test discriminates the right speed.
      * FAIL : alpha(A0)/alpha0 deviates from 1 by >= 1e-12 with c_EM (SYM
               invariance broken) OR the c_shear control does NOT deviate
               (the test isn't actually discriminating c_EM vs c_shear).
      * Report alpha(A0)/alpha0 for both speed choices across the sweep.
    """
    EM.assert_canonical_constants()
    A0_sweep = (0.0, 0.3, 0.5, 0.7, 0.9)

    def alpha_ratio(A0, *, use_shear: bool):
        # alpha = e^2/(4 pi eps_eff hbar c). Ratio to cold cancels e, hbar, 4pi.
        Se = float(EM.S_of_A(A0))
        eps_eff = EPSILON_0 * Se
        c = C_0 * np.sqrt(Se) if use_shear else C_0 / Se  # c_shear vs c_EM (SYM)
        return (EPSILON_0 * C_0) / (eps_eff * c)

    print("\n--- T2.4 alpha-invariance under SYM (c_EM, not c_shear) ---")
    cem = {}
    csh = {}
    for A0 in A0_sweep:
        cem[A0] = alpha_ratio(A0, use_shear=False)
        csh[A0] = alpha_ratio(A0, use_shear=True)
        print(f"  A0={A0}: alpha/alpha0  c_EM-form = {cem[A0]:.12f}   "
              f"c_shear-form (WRONG) = {csh[A0]:.6f}  (=1/S^1.5)")

    # c_EM form: invariant to machine precision for every A0
    max_dev_cem = max(abs(cem[A0] - 1.0) for A0 in A0_sweep)
    # c_shear control: must DEVIATE for A0 >= 0.3 (so the test discriminates)
    min_dev_csh = min(abs(csh[A0] - 1.0) for A0 in A0_sweep if A0 >= 0.3)

    print(f"  max |alpha/alpha0 - 1| (c_EM)    : {max_dev_cem:.3e}  (PASS < 1e-12 — INVARIANT)")
    print(f"  min |alpha/alpha0 - 1| (c_shear) : {min_dev_csh:.3e}  (control must be > 1e-3 — DISCRIMINATES)")

    assert max_dev_cem < 1e-12, (
        f"FAIL: alpha NOT invariant under SYM with c_EM — max deviation {max_dev_cem:.3e}"
    )
    assert min_dev_csh > 1e-3, (
        f"FAIL: c_shear control did not deviate — test not discriminating c_EM vs c_shear "
        f"(min deviation {min_dev_csh:.3e})"
    )

    if VZ.viz_enabled():
        A_grid = np.linspace(0.0, 0.95, 200)
        r_cem = np.array([alpha_ratio(a, use_shear=False) for a in A_grid])
        r_csh = np.array([alpha_ratio(a, use_shear=True) for a in A_grid])

        def _draw(fig):
            ax = fig.subplots(1, 1)
            ax.plot(A_grid, r_cem, color="#2ca02c", lw=2.0,
                    label="alpha/alpha0 with c_EM=c0/S  (INVARIANT = 1)")
            ax.plot(A_grid, r_csh, color="#d62728", lw=1.5, ls="--",
                    label="alpha/alpha0 with c_shear=c0√S  (WRONG: 1/S^{3/2})")
            ax.axhline(1.0, color="k", ls=":", lw=0.8)
            ax.set_xlabel("SYM operating point A0")
            ax.set_ylabel("alpha(A0) / alpha0")
            ax.set_title("T2.4 — alpha INVARIANT under SYM (c_EM), category error with c_shear "
                         "(clm-3zz0f6)")
            ax.legend(fontsize=9)
            ax.set_ylim(0.8, 4.0)
        path = VZ.save_simple_figure(
            "T2.4", "alpha-invariance under SYM scaling (c_EM vs c_shear)", _draw)
        print(f"  [viz] alpha-invariance figure -> {path}")
