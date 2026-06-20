"""Figures for the GRADED VACUUM IMPEDANCE NETWORK (Vol.9 Ch.3 §6 device-circuit-models).

Generated FROM THE ACTUAL ENGINE — NOT hand-drawn, NOT faked (the §6 caption is
explicit: "Plots are not faked"). Each slot is computed from a live, MERGED solver:

  (i)   fig:vol9_graded_network_schematic  — the 3-channel graded-network schematic
        (Z_EM matched Γ=0 ; Z_shear/Z_bulk Γ=-1) + chiral circulator + confinement
        terminations. LINE-ART (matplotlib), labelled with the LIVE channel numbers
        pulled from the engine (the c_L/c_T ratio, the radiative floor, the Γ map).
  (ii)  fig:vol9_graded_network_smith       — per-channel Γ vs S(A), generated from the
        live varactor operator (vacuum_varactor_scatter.py, PR#305): Z_bond=Z0·√S(A),
        Γ→-1 as S→0 for Z_shear/Z_bulk ; Z_EM matched flat Γ=0. Plus a Smith-chart view.
  (iii) fig:vol9_forkA_discriminator        — Fork-A discriminator. The ISOLATED arm is
        generated from BOTH live engines: the graded-vacuum-network isolation eigensolver
        (graded_vacuum_network.py, PR#297 — intrinsic mode lossless, Q→∞) AND the α-FREE
        cold-cage FDTD ringdown (Q_ringdown≈30.8, the canonical N=72/6000 anchor; NOT 137).
        The COUPLED-arm mode-splitting is HONESTLY MARKED deferred-pending-H_couple
        (Build-B, NOT implemented) — NOT faked.
  (iv)  fig:vol9_graded_network_op_sweep     — operating-point sweep: channel impedances
        vs saturation S, from the live varactor map (Z=Z0·√S): Z_EM flat ; Z_bulk/Z_shear→0.

DISCIPLINE
  * substrate-native : the operators imported are the K4/Cosserat-native varactor scatter
    and the tetrahedral isolation eigensolver; NO Cartesian-Laplacian, NO ε-load.
  * α-FREE where relevant : the cold-cage anchor is the engine's α-free ringdown
    (Q≈30.8, NOT 137); the radiative floor Z_RADIATION≈29.98 is band-consistent-NOT-
    identity (DEC-5). ALPHA is never imported into any figure path.
  * ave-canonical-source : kernels / constants / ratios are IMPORTED from the engine
    (saturation_kernel, RATIO_BULK_SHEAR_MECH, Z_RADIATION), never hardcoded.
  * deterministic : fixed configs; re-running regenerates byte-stable PNGs (the FDTD
    ringdown is a deterministic leapfrog from a fixed seeded core — no RNG).

Result/KB context:
  research/2026-06-19_electron-Q-coupled-network_result.md (isolation Q→∞ ; cold-cage 30.8)
  research/2026-06-20_vacuum-varactor-scatter_result.md     (the varactor Γ map)
  manuscript/ave-kb/vol9/ch3-pin-port-configuration/device-circuit-models.md §6

Run:
  PYTHONPATH=src python3 src/scripts/vol_9_device/graded_vacuum_network_figures.py
The PNGs land in manuscript/vol_9_vacuum_datasheet/figures/graded_network/ (on the
graphicspath) so the manuscript \includegraphics resolves them directly.
"""

from __future__ import annotations

import os
import sys

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

# Make the ave package importable when run as a bare script.
_REPO_SRC = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", "src"))
if _REPO_SRC not in sys.path:
    sys.path.insert(0, _REPO_SRC)

# ── LIVE engine imports (READ-ONLY: figures only, no engine mutation) ──────────
from ave.core.constants import ALPHA, Z_RADIATION  # noqa: E402

# α⁻¹ = 137.036, the BAKED-ECHO contrast reference. DISPLAY-ONLY: it is drawn as the
# "the cold cage does NOT reproduce this" reference line in slot (iii); it is NEVER a
# computation input. Derived from the canonical constant (ave-canonical-source), NOT a
# magic literal (mirrors test_l3_mass_cage.py:206 "a DOWNSTREAM consistency reference
# ONLY"). The engine modules above stay α-FREE (import-guarded); this label lives only
# in the driver as the echo to contrast against.
ALPHA_INV = 1.0 / ALPHA  # ≈ 137.036
from ave.solvers.graded_vacuum_network import (  # noqa: E402
    RATIO_BULK_SHEAR_MECH,  # = sqrt(10/3) ≈ 1.82574 (c_L/c_T, α-free, DERIVED)
    IsolationConfig,
    solve_isolation_Q,
)
from ave.solvers.vacuum_varactor_scatter import (  # noqa: E402
    radiative_port_reflection,
    saturation_kernel,
)

# Output dir: a graded_network/ subdir of the vol_9 figures dir (added to graphicspath).
_FIG_DIR = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "..",
        "..",
        "..",
        "manuscript",
        "vol_9_vacuum_datasheet",
        "figures",
        "graded_network",
    )
)
os.makedirs(_FIG_DIR, exist_ok=True)

DPI = 130

# Channel palette (consistent across all four slots).
C_EM = "#1f6fb2"     # matched radiative port
C_SHEAR = "#27ae60"  # deviatoric G (charge-3 Cosserat winding)
C_BULK = "#c0392b"   # A1 dilatation (mass-3) at K=2G


def _gamma_mu_load(S: np.ndarray) -> np.ndarray:
    """Reflection of the LONGITUDINAL μ-load Z_bond=Z0·√S vs matched Z0: Γ=(Z-1)/(Z+1).
    As S→0, Z→0, Γ→-1 (the mass/charge cage SHORT — the corrected sign, NOT the ε-load
    Z→∞/Γ=+1). Computed from the engine kernel value of S, not a hardcoded curve."""
    Z = np.sqrt(S)
    return (Z - 1.0) / (Z + 1.0)


# ═════════════════════════════════════════════════════════════════════════════
# (ii) Per-channel Smith / Γ vs S(A)  —  from the live varactor operator
# ═════════════════════════════════════════════════════════════════════════════
def fig_ii_smith() -> str:
    """fig:vol9_graded_network_smith — per-channel reflection.

    Z_EM is the MATCHED radiative port: Γ_EM = 0, flat (independent of S).
    Z_shear and Z_bulk are the saturable μ-loads Z_bond = Z0·√S(A): Γ → -1 as S(A) → 0
    (the confinement SHORT). Both shear and bulk follow the SAME varactor Γ(S) law
    (they differ in DOMAIN — mechanical/acoustic — and in the dimensionless channel
    ratio c_L/c_T, not in the Γ-vs-S shape), so the curve is shared; the channels are
    distinguished by their operating-S markers.

    S(A) is the LIVE engine kernel saturation_kernel(A)=√(1-A²); A∈[0,A_cap). Left
    panel: Γ vs S(A). Right panel: the same trajectory on a Smith chart (real Γ axis,
    Z0-normalised), from the matched centre Γ=0 to the short Γ=-1."""
    # Sweep A up to (just under) the cap; read S from the LIVE kernel (un-clipped so the
    # full S→0 trend is visible — A_cap/S_min relaxed exactly as the vol_4 driver does).
    A = np.linspace(0.0, 0.9999, 700)
    S = saturation_kernel(A, A_cap=0.999999, S_min=1e-12)  # LIVE engine kernel
    gamma_mech = _gamma_mu_load(S)  # μ-load: shear + bulk share this Γ(S)
    gamma_em = np.zeros_like(S)     # matched port: Γ_EM ≡ 0

    # operating markers: A=0 (vacuum, S=1, Γ=0) and the deployed A_cap=0.99 floor.
    S_cap = float(saturation_kernel(np.array(0.99)))
    g_cap = float(_gamma_mu_load(np.array(S_cap)))

    fig, (axL, axR) = plt.subplots(1, 2, figsize=(11.6, 5.2))

    # ── left: Γ vs S(A) per channel ──
    axL.plot(S, gamma_mech, color=C_BULK, lw=2.4,
             label=r"$Z_{\rm bulk},\,Z_{\rm shear}$ ($\mu$-load $Z=Z_0\sqrt{S}$): $\Gamma\!\to\!-1$")
    axL.plot(S, gamma_em, color=C_EM, lw=2.4, ls="-",
             label=r"$Z_{\rm EM}\equiv Z_0$ (matched port): $\Gamma=0$ (flat)")
    axL.axhline(-1.0, color="grey", lw=0.9, ls=":")
    axL.axhline(0.0, color="grey", lw=0.9, ls=":")
    axL.plot(1.0, 0.0, "o", color="k", ms=6)
    axL.annotate("vacuum: $S=1$, $\\Gamma=0$", xy=(1.0, 0.0), xytext=(0.55, -0.22),
                 fontsize=8.5, arrowprops=dict(arrowstyle="->", lw=0.9))
    axL.plot(S_cap, g_cap, "s", color=C_BULK, ms=7)
    axL.annotate(f"$A_{{cap}}=0.99$: $S={S_cap:.3f}$,\n$\\Gamma\\approx{g_cap:.3f}$",
                 xy=(S_cap, g_cap), xytext=(0.40, -0.78), fontsize=8.5,
                 arrowprops=dict(arrowstyle="->", lw=0.9))
    axL.annotate("$S\\!\\to\\!0$ (cage SHORT)\n$\\Gamma\\!\\to\\!-1$", xy=(0.02, -0.97),
                 xytext=(0.12, -0.55), fontsize=8.5, color=C_BULK,
                 arrowprops=dict(arrowstyle="->", lw=0.9, color=C_BULK))
    axL.set_xlabel(r"saturation $S(A)=\sqrt{1-A^2}$  (live engine kernel)")
    axL.set_ylabel(r"reflection $\Gamma=(Z-1)/(Z+1)$")
    axL.set_xlim(0.0, 1.02)
    axL.set_ylim(-1.12, 0.30)
    axL.invert_xaxis()  # saturation increases left→right (S:1→0)
    axL.grid(alpha=0.3)
    axL.legend(fontsize=8.3, loc="upper left")
    axL.set_title(r"Per-channel $\Gamma$ vs saturation $S(A)$")

    # ── right: the same trajectory on a (real-axis) Smith chart ──
    theta = np.linspace(0, 2 * np.pi, 400)
    axR.plot(np.cos(theta), np.sin(theta), color="grey", lw=1.0)  # |Γ|=1 unit circle
    # constant-resistance circles (r=0,1,3) for orientation
    for r, a in ((0.0, 0.35), (1.0, 0.45), (3.0, 0.30)):
        cx = r / (1 + r)
        rad = 1.0 / (1 + r)
        axR.plot(cx + rad * np.cos(theta), rad * np.sin(theta), color="grey", lw=0.7, alpha=a)
    axR.axhline(0.0, color="grey", lw=0.7, alpha=0.5)
    # μ-load trajectory: Γ real, sweeping 0 → -1 as S:1→0 (along the negative real axis)
    axR.plot(gamma_mech, np.zeros_like(gamma_mech), color=C_BULK, lw=3.0,
             label=r"$Z_{\rm bulk},Z_{\rm shear}$: $\Gamma:0\!\to\!-1$")
    axR.plot(0.0, 0.0, "o", color=C_EM, ms=10,
             label=r"$Z_{\rm EM}$ matched: $\Gamma=0$ (centre)")
    axR.plot(-1.0, 0.0, "*", color=C_BULK, ms=15, label=r"short $\Gamma=-1$ ($S\!\to\!0$)")
    axR.set_xlim(-1.25, 1.25)
    axR.set_ylim(-1.25, 1.25)
    axR.set_aspect("equal")
    axR.set_xlabel(r"$\mathrm{Re}\,\Gamma$")
    axR.set_ylabel(r"$\mathrm{Im}\,\Gamma$")
    axR.legend(fontsize=8.0, loc="upper right")
    axR.set_title("Smith view ($Z_0$-normalised)")

    fig.suptitle(
        r"Graded-network per-channel reflection from the live varactor operator: "
        r"$Z_{\rm EM}$ matched ($\Gamma=0$), $Z_{\rm shear}/Z_{\rm bulk}\to\Gamma=-1$ as $S(A)\to0$",
        fontsize=10.5,
    )
    p = os.path.join(_FIG_DIR, "vol9_graded_network_smith.png")
    fig.tight_layout(rect=(0, 0, 1, 0.95))
    fig.savefig(p, dpi=DPI)
    plt.close(fig)
    return p


# ═════════════════════════════════════════════════════════════════════════════
# (iv) Operating-point sweep — channel impedances vs saturation S
# ═════════════════════════════════════════════════════════════════════════════
def fig_iv_op_sweep() -> str:
    """fig:vol9_graded_network_op_sweep — channel impedances vs saturation S.

    From the live varactor map Z_bond = Z0·√S(A):
      * Z_EM  ≡ Z0 : FLAT (the matched radiative port; saturation-independent).
      * Z_bulk, Z_shear : Z = Z0·√S → 0 as S → 0 (the cage SHORT). They are plotted
        in their OWN dimensionless normalisation (Z/Z_channel0) since they live in
        MECHANICAL/acoustic units (ρ×speed), not Z0 Ω — the mixed-impedance-domain
        caveat in §6: writing "Z_bulk=√2·Z0" is the electrical-vs-mechanical mis-scope.
        The bulk/shear channels differ by the α-FREE c_L/c_T ratio (imported from the
        engine, RATIO_BULK_SHEAR_MECH), shown as the bulk-channel vertical offset.

    Saturation axis S∈(0,1] is read straight off the live kernel via an A-sweep, so the
    curve IS the engine's S(A), not an analytic stand-in."""
    A = np.linspace(0.0, 0.9999, 700)
    S = saturation_kernel(A, A_cap=0.999999, S_min=1e-12)  # LIVE kernel
    sqrtS = np.sqrt(S)

    # channel impedances, each in its OWN dimensionless normalisation (Z/Z_channel0):
    Z_em = np.ones_like(S)                         # matched, flat
    Z_shear = sqrtS                                # μ-load → 0
    # bulk carries the α-free c_L/c_T factor relative to shear (same √S saturation shape,
    # different channel speed): plotted as ratio·√S in shear-normalised units to show the
    # bulk/shear GAP location (alpha-free; from the engine ratio).
    Z_bulk = RATIO_BULK_SHEAR_MECH * sqrtS

    fig, ax = plt.subplots(figsize=(8.6, 5.4))
    ax.plot(S, Z_em, color=C_EM, lw=2.6, label=r"$Z_{\rm EM}\equiv Z_0$ (matched; flat)")
    ax.plot(S, Z_shear, color=C_SHEAR, lw=2.6,
            label=r"$Z_{\rm shear}=\rho\,c_{\rm shear}\propto\sqrt{S}\to0$")
    ax.plot(S, Z_bulk, color=C_BULK, lw=2.6, ls="-",
            label=(r"$Z_{\rm bulk}=\rho\,c_{\rm bulk}\propto\frac{c_L}{c_T}\sqrt{S}\to0$"
                   rf"  ($c_L/c_T={RATIO_BULK_SHEAR_MECH:.3f}$)"))

    ax.annotate("$S\\to0$:  $Z_{\\rm bulk},Z_{\\rm shear}\\to0$ (cage SHORT)",
                xy=(0.02, 0.05), xytext=(0.22, 0.55), fontsize=9,
                arrowprops=dict(arrowstyle="->", lw=1.0))
    ax.plot(1.0, 1.0, "o", color="k", ms=6)
    ax.annotate("vacuum $S=1$\n(all channels matched)", xy=(1.0, 1.0), xytext=(0.55, 1.45),
                fontsize=8.5, arrowprops=dict(arrowstyle="->", lw=0.9))

    ax.set_xlabel(r"saturation $S(A)=\sqrt{1-A^2}$  (live engine kernel; $S:1\to0$ as the core saturates)")
    ax.set_ylabel(r"channel impedance  $Z/Z_{\rm channel,0}$  (each in its own domain units)")
    ax.set_xlim(0.0, 1.02)
    ax.set_ylim(0.0, max(1.7, RATIO_BULK_SHEAR_MECH + 0.15))
    ax.invert_xaxis()  # increasing saturation left→right
    ax.grid(alpha=0.3)
    ax.legend(fontsize=8.6, loc="upper left")
    ax.set_title(
        "Operating-point sweep: channel impedances vs saturation $S$\n"
        r"($Z_{\rm EM}$ flat; $Z_{\rm bulk}/Z_{\rm shear}\to0$ as $S\to0$ — from the live $Z=Z_0\sqrt{S}$ map)"
    )
    # caveat banner: mixed impedance domains (the §6 three-impedance mis-scope warning)
    ax.text(0.5, 0.02,
            r"mixed domains: only $Z_{\rm EM}$ is electrical ($\Omega$); "
            r"$Z_{\rm shear},Z_{\rm bulk}$ are mechanical/acoustic ($\rho\times$speed)",
            transform=ax.transAxes, ha="center", va="bottom", fontsize=7.6,
            bbox=dict(boxstyle="round", fc="#fff6e6", ec="grey", alpha=0.9))
    p = os.path.join(_FIG_DIR, "vol9_graded_network_op_sweep.png")
    fig.tight_layout()
    fig.savefig(p, dpi=DPI)
    plt.close(fig)
    return p


# ═════════════════════════════════════════════════════════════════════════════
# (iii) Fork-A discriminator — ISOLATED arm (live), coupled arm DEFERRED (honest)
# ═════════════════════════════════════════════════════════════════════════════
def _cold_cage_Q() -> dict:
    """α-FREE cold-cage Q from the engine's CANONICAL FDTD breathing-mode ring-down
    (test_l3_mass_cage.py:728-744: N=72, pml=12, 6000 leapfrog steps). Deterministic
    (a fixed-seed Gaussian core + leapfrog — NO RNG). Returns Q_ringdown≈30.8 and
    Q_linewidth≈3.8 — the canonical α-free anchor (NOT 137).

    This re-runs the engine helpers from src/tests/engine_acceptance/_bulk.py READ-ONLY
    (no engine file is modified). The N=72/6000 config is REQUIRED to land on the
    canonical 30.8 anchor — a downscaled grid drifts (N=48 gives ~100), so we use the
    exact corpus config the 30.8 number is defined at."""
    ea = os.path.join(_REPO_SRC, "tests", "engine_acceptance")
    if ea not in sys.path:
        sys.path.insert(0, ea)
    import _bulk as B  # noqa: PLC0415 — engine-acceptance helper, READ-ONLY

    eng = B.make_cage_engine(N=72, S_min=1e-3, A_cap=0.999, pml_thickness=12)
    probe = B.breathing_kick_cage(eng, frac=0.9, core_sigma=8.0, kick_width=2.0, kick_amp=0.01)
    dVdt = B.record_breathing_dVdt(eng, probe, 6000)
    ev = B.cutoff_eigenfrequency(eng, dVdt)
    rd = B.ringdown_Q(eng, dVdt, ev["omega_cutoff"])
    return {
        "omega_cutoff": float(ev["omega_cutoff"]),
        "Q_ringdown": float(rd["Q_ringdown"]),
        "Q_linewidth": float(ev["q_linewidth"]),
        "ipk": int(ev["ipk"]),
        "peak_mean": float(ev["peak_mean"]),
        "dVdt": dVdt,
    }


def _isolation_Q_sweep() -> dict:
    """The ISOLATED-arm intrinsic Q vs grid resolution N, from the live tetrahedral
    isolation eigensolver (graded_vacuum_network.solve_isolation_Q). With the EM port
    OPEN the operator is near-Hermitian on the confined core ⇒ Im(ω)→0 ⇒ Q grows toward
    ∞ with resolution (the lossless-confined intrinsic mode — the Build-A halt result).
    With the EM port CLOSED (Γ_EM=-1) the operator is exactly Hermitian ⇒ Q=∞.

    α-FREE: the isolation solver imports ONLY α-free ratios (RATIO_BULK_SHEAR_MECH),
    never Q_TANK/ALPHA. Returns the open-port Q(N) trajectory + the closed-port ∞ flag.

    Uses the DENSE LAPACK path (solve_isolation_Q) deliberately: at these resolutions the
    bound mode's loss rate Im(ω) is ~1e-5…1e-8 (lossless-confined), and the sparse
    ARPACK shift-invert path seeds a RANDOM start vector that perturbs such a near-zero
    denominator at the ~1e-7 level → non-reproducible PNGs. The dense LAPACK eig is
    bit-deterministic (verified: identical Q across repeat runs), so the figure is exactly
    reproducible (the brief's determinism mandate). The trend Q→∞ with N is unchanged;
    dense caps N≈14 (Q~6e7), which already shows the divergence cleanly. The closed-port
    (Γ_EM=-1, Hermitian) Q=∞ is exact (Im(ω)=0)."""
    Ns = [8, 10, 12, 14]
    Q_open = []
    for N in Ns:
        port = max(2, N // 6)
        sig = max(2.0, N / 6.5)
        r = solve_isolation_Q(
            IsolationConfig(N=N, sigma=sig, port_thickness=port, em_port_closed=False)
        )
        Q_open.append(float(r["Q"]) if r.get("ok") else float("nan"))
    # closed-port Hermitian ⇒ Q=∞ — exact via the dense path at small N.
    r_closed = solve_isolation_Q(
        IsolationConfig(N=14, sigma=2.5, port_thickness=3, em_port_closed=True)
    )
    return {
        "N": Ns,
        "Q_open": Q_open,
        "Q_closed": float(r_closed["Q"]) if r_closed.get("ok") else float("inf"),
        "closed_is_inf": bool(not np.isfinite(r_closed.get("Q", np.inf))),
    }


def fig_iii_forkA_discriminator() -> dict:
    """fig:vol9_forkA_discriminator — the Fork-A discriminator (ISOLATED arm live;
    COUPLED arm honestly DEFERRED).

    LEFT panel — the ISOLATED arm, generated from TWO live engines:
      * the intrinsic isolation eigen-Q vs resolution N (Q→∞, lossless-confined; the
        Build-A halt result) — Q is the dimensionless |Re ω|/(2|Im ω|).
      * the α-FREE cold-cage FDTD ringdown anchor Q_ringdown≈30.8 (the radiative/loaded
        floor; NOT 137) — drawn as a horizontal anchor with the radiative-floor band
        [Z_RADIATION≈29.98 … cold-cage 30.8], band-consistent-NOT-identity (DEC-5).
    RIGHT panel — the Fork-A discriminator SCHEMATIC: ISOLATED ⇒ two channels cross
      freely (no avoided crossing); COUPLED ⇒ mode-splitting / avoided crossing whose
      gap sets the loaded Q toward the OBSERVED electron Q (NOT the baked 137). The
      coupled curve is drawn as a DASHED 'deferred-pending-H_couple' placeholder — it is
      NOT computed (Build-B / H_couple is not implemented), and it is labelled as such.
      NO faked coupled data is plotted.

    Returns the engine diagnostics dict (Q values) so the caller can print/verify."""
    cold = _cold_cage_Q()
    iso = _isolation_Q_sweep()
    Q_cold = cold["Q_ringdown"]
    Z_rad = float(Z_RADIATION)

    fig, (axL, axR) = plt.subplots(1, 2, figsize=(12.2, 5.4))

    # ── LEFT: isolated intrinsic Q(N) → ∞  +  α-free cold-cage anchor ──
    Q_open = np.array(iso["Q_open"], dtype=float)
    axL.semilogy(iso["N"], Q_open, "o-", color=C_BULK, lw=2.2, ms=7,
                 label=r"isolated intrinsic eigen-$Q$ (EM port open): $\to\infty$")
    axL.axhline(Q_cold, color=C_EM, lw=2.4, ls="-",
                label=rf"$\alpha$-free cold-cage ring-down $Q\approx{Q_cold:.1f}$ (NOT 137)")
    # radiative-Q floor band [Z_RADIATION .. cold-cage], band-consistent-not-identity
    band_lo, band_hi = min(Z_rad, Q_cold), max(Z_rad, Q_cold)
    axL.axhspan(band_lo, band_hi, color=C_EM, alpha=0.16)
    axL.axhline(Z_rad, color=C_EM, lw=1.0, ls=":",
                label=rf"radiative floor $Z_{{\rm rad}}=Z_0/4\pi\approx{Z_rad:.2f}$ (band-consistent, $\neq$ identity, DEC-5)")
    axL.axhline(ALPHA_INV, color="grey", lw=1.0, ls="--",
                label=rf"$\alpha^{{-1}}={ALPHA_INV:.1f}$ (baked echo — NOT reproduced cold)")
    axL.set_xlabel(r"lattice resolution $N$ (dense isolation eigensolve)")
    axL.set_ylabel(r"$Q=|\mathrm{Re}\,\omega|/(2|\mathrm{Im}\,\omega|)$")
    axL.set_ylim(10, 1e9)
    axL.grid(alpha=0.3, which="both")
    axL.legend(fontsize=7.6, loc="center right")
    axL.set_title(
        "ISOLATED arm (live engines): intrinsic $Q\\to\\infty$ (lossless-confined)\n"
        rf"$\alpha$-free loaded floor $Q\approx{Q_cold:.1f}$ (cold cage) — neither is 137"
    )

    # ── RIGHT: Fork-A discriminator schematic (coupled DEFERRED) ──
    g = np.linspace(-1.0, 1.0, 400)  # a detuning/coupling axis (schematic)
    # ISOLATED: two bare channel branches cross freely (no interaction) — real engine
    # behaviour at H_couple=0 (the isolation arm IS the no-coupling limit).
    axR.plot(g, 0.6 * g, color=C_SHEAR, lw=2.4, label="isolated: free crossing (shear branch)")
    axR.plot(g, -0.6 * g, color=C_BULK, lw=2.4, label="isolated: free crossing (bulk branch)")
    axR.plot(0.0, 0.0, "x", color="k", ms=10, mew=2.5)
    axR.annotate("free crossing\n(no avoided gap)\n$H_{\\rm couple}=0$", xy=(0.0, 0.0),
                 xytext=(0.18, 0.55), fontsize=8.5, arrowprops=dict(arrowstyle="->", lw=0.9))
    # COUPLED (DEFERRED): the avoided-crossing the coupled solve WOULD produce — drawn
    # as a faint dashed sketch with an explicit "NOT computed" stamp. NOT engine data.
    gap = 0.30
    upper = 0.5 * (0.6 * g - 0.6 * g) + np.sqrt((0.6 * g) ** 2 + gap ** 2)
    lower = -np.sqrt((0.6 * g) ** 2 + gap ** 2)
    axR.plot(g, upper, color="grey", lw=1.6, ls="--", alpha=0.6)
    axR.plot(g, lower, color="grey", lw=1.6, ls="--", alpha=0.6,
             label="coupled: avoided crossing (SCHEMATIC)")
    axR.annotate("mode-splitting gap\n$\\Rightarrow$ loaded $Q\\to$ OBSERVED $Q$ (not 137)",
                 xy=(0.0, gap), xytext=(-0.95, 0.55), fontsize=8.0,
                 arrowprops=dict(arrowstyle="->", lw=0.9, color="grey"))
    axR.text(0.5, 0.04,
             "COUPLED ARM DEFERRED — pending Build-B $H_{\\rm couple}$ (NOT implemented).\n"
             "Dashed avoided-crossing is a SCHEMATIC, not engine data (not faked: not computed).",
             transform=axR.transAxes, ha="center", va="bottom", fontsize=8.0,
             bbox=dict(boxstyle="round", fc="#ffecec", ec="#c0392b", alpha=0.95))
    axR.set_xlabel("coupling / detuning (schematic axis)")
    axR.set_ylabel("mode frequency (schematic)")
    axR.set_xlim(-1.05, 1.05)
    axR.set_ylim(-1.0, 1.0)
    axR.grid(alpha=0.25)
    axR.legend(fontsize=7.8, loc="upper left")
    axR.set_title("Fork-A: isolated free-crossing (live) vs coupled mode-splitting (deferred)")

    fig.suptitle(
        "Fork-A discriminator — ISOLATED arm from the live isolation eigensolver + "
        rf"$\alpha$-free cold-cage ringdown ($Q\approx{Q_cold:.1f}$); COUPLED arm deferred-pending-$H_{{\rm couple}}$",
        fontsize=10.2,
    )
    p = os.path.join(_FIG_DIR, "vol9_forkA_discriminator.png")
    fig.tight_layout(rect=(0, 0, 1, 0.94))
    fig.savefig(p, dpi=DPI)
    plt.close(fig)
    return {
        "path": p,
        "Q_cold_ringdown": Q_cold,
        "Q_linewidth": cold["Q_linewidth"],
        "omega_cutoff": cold["omega_cutoff"],
        "Z_radiation": Z_rad,
        "Q_open_sweep": iso["Q_open"],
        "Q_closed_is_inf": iso["closed_is_inf"],
    }


# ═════════════════════════════════════════════════════════════════════════════
# (i) Network schematic — three reactance branches + circulator + terminations
# ═════════════════════════════════════════════════════════════════════════════
def fig_i_schematic() -> str:
    """fig:vol9_graded_network_schematic — the canonical 3-channel graded-network.

    LINE-ART (per the §6 slot spec: "This is a SCHEMATIC ... not a data plot"). Three
    reactance branches (Z_EM, Z_shear, Z_bulk) fanning out of a shared chiral circulator,
    each ending in its confinement-surface termination:
      * Z_EM   → matched port  Γ_EM = 0   (open radiative port; the EM grade).
      * Z_shear→ short Γ = -1  (deviatoric G, the charge-3 Cosserat winding).
      * Z_bulk → short Γ = -1  (A1 dilatation, the mass-3, at K=2G).
    The branch LABELS carry the LIVE engine numbers (the α-free c_L/c_T ratio, the
    radiative-floor Γ_EM bound, the saturated-cage Γ→-1) so even the schematic is
    engine-sourced, not invented. The bulk↔shear inter-grade coupling is the conserved
    H_couple; the EM↔mechanical coupling needs a transducer (TKI, gated — flagged, not
    asserted) — both annotated. mixed-impedance-domain caveat is on the figure."""
    # LIVE engine anchors used as schematic labels (READ-ONLY).
    ratio = float(RATIO_BULK_SHEAR_MECH)            # c_L/c_T, α-free, DERIVED
    rp = radiative_port_reflection()                 # the matched-port diagnostics
    gamma_em_into_rad = float(rp["gamma_bound_into_radiation_load"])  # ≈ -0.853
    Z_rad = float(Z_RADIATION)

    fig, ax = plt.subplots(figsize=(11.0, 6.6))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 9)
    ax.axis("off")

    # ── shared chiral circulator (centre hub) ──
    hub = (3.0, 4.5)
    circ = plt.Circle(hub, 0.95, fill=False, lw=2.2, color="#6c3483")
    ax.add_patch(circ)
    # circulating arrows (chirality)
    th = np.linspace(0.2, 1.55 * np.pi, 60)
    ax.plot(hub[0] + 0.62 * np.cos(th), hub[1] + 0.62 * np.sin(th), color="#6c3483", lw=1.8)
    ax.annotate("", xy=(hub[0] + 0.62 * np.cos(th[-1] + 0.08), hub[1] + 0.62 * np.sin(th[-1] + 0.08)),
                xytext=(hub[0] + 0.62 * np.cos(th[-1]), hub[1] + 0.62 * np.sin(th[-1])),
                arrowprops=dict(arrowstyle="-|>", lw=2.0, color="#6c3483"))
    ax.text(hub[0], hub[1] - 0.02, "chiral\ncirculator", ha="center", va="center",
            fontsize=8.5, color="#6c3483", fontweight="bold")
    # input feed into the hub
    ax.annotate("", xy=(hub[0] - 0.95, hub[1]), xytext=(0.6, hub[1]),
                arrowprops=dict(arrowstyle="-|>", lw=1.8, color="k"))
    ax.text(0.45, hub[1] + 0.28, "drive /\nport", ha="left", va="bottom", fontsize=8.5)

    # ── branch geometry: three reactance arms to the right, fanned vertically ──
    arms = [
        # (y, color, name, Z-label, termination-label, term-color, term-Γ)
        (7.2, C_EM, r"$Z_{\rm EM}\equiv Z_0$" + "\n(EM grade)",
         "matched radiative port",
         rf"$\Gamma_{{\rm EM}}=0$ (matched)", C_EM),
        (4.5, C_SHEAR, r"$Z_{\rm shear}=\rho\,c_{\rm shear}$" + "\n(deviatoric $G$, charge-3)",
         r"$Z=Z_0\sqrt{S}\to0$",
         r"$\Gamma=-1$ (cage SHORT)", C_SHEAR),
        (1.8, C_BULK, r"$Z_{\rm bulk}=\rho\,c_{\rm bulk}$" + "\n(A1 dilatation, mass-3, $K{=}2G$)",
         rf"$c_L/c_T={ratio:.3f}$ vs shear",
         r"$\Gamma=-1$ (cage SHORT)", C_BULK),
    ]
    x0 = hub[0] + 0.95
    x_box = 6.0
    x_term = 9.7
    for (y, col, name, zlab, term, tcol) in arms:
        # wire from hub to the reactance box
        ax.plot([x0, x_box - 0.9], [hub[1], y], color=col, lw=2.0)
        # reactance box
        box = plt.Rectangle((x_box - 0.9, y - 0.5), 1.8, 1.0, fill=True, fc="white",
                            ec=col, lw=2.2)
        ax.add_patch(box)
        ax.text(x_box, y + 0.16, name.split("\n")[0], ha="center", va="center",
                fontsize=8.6, color=col, fontweight="bold")
        ax.text(x_box, y - 0.30, name.split("\n")[1], ha="center", va="center",
                fontsize=6.8, color=col)
        ax.text(x_box, y - 0.78, zlab, ha="center", va="top", fontsize=7.4, color="#333")
        # wire to the termination
        ax.plot([x_box + 0.9, x_term - 0.35], [y, y], color=col, lw=2.0)
        # termination symbol: matched port (open triangle) vs short (ground bar)
        if "matched" in term:
            ax.annotate("", xy=(x_term + 0.55, y), xytext=(x_term - 0.35, y),
                        arrowprops=dict(arrowstyle="-|>", lw=2.0, color=tcol))
            ax.text(x_term + 0.7, y, "radiate", ha="left", va="center", fontsize=7.6, color=tcol)
        else:
            # short-to-ground bar
            ax.plot([x_term - 0.35, x_term - 0.35], [y - 0.5, y + 0.5], color=tcol, lw=3.0)
            for dy in (-0.32, 0.0, 0.32):
                ax.plot([x_term - 0.35, x_term - 0.05], [y + dy, y + dy + 0.18], color=tcol, lw=1.6)
        ax.text(x_term + 0.05, y - 0.85, term, ha="center", va="top", fontsize=7.6,
                color=tcol, fontweight="bold")

    # ── inter-grade coupling annotations ──
    # bulk ↔ shear : conserved H_couple (a real wire between the two mechanical grades)
    ax.annotate("", xy=(x_box, 1.8 + 0.55), xytext=(x_box, 4.5 - 0.55),
                arrowprops=dict(arrowstyle="<|-|>", lw=1.6, color="#8e44ad", ls="--"))
    ax.text(x_box + 1.05, 3.15, r"$H_{\rm couple}$" + "\n(bulk$\\leftrightarrow$shear,\nconserved)",
            ha="left", va="center", fontsize=7.8, color="#8e44ad")
    # EM ↔ mechanical : needs a transducer (TKI, gated — flagged not asserted)
    ax.annotate("", xy=(x_box, 7.2 - 0.55), xytext=(x_box, 4.5 + 0.55),
                arrowprops=dict(arrowstyle="<|-|>", lw=1.4, color="grey", ls=":"))
    ax.text(x_box + 1.05, 5.9, "EM$\\leftrightarrow$mech:\ntransducer (TKI),\ngated — flagged",
            ha="left", va="center", fontsize=7.4, color="grey")

    ax.set_title(
        "Graded vacuum impedance network: three reactance channels + chiral circulator "
        "+ confinement terminations\n"
        rf"(live anchors: $c_L/c_T={ratio:.3f}$, $Z_{{\rm rad}}=Z_0/4\pi\approx{Z_rad:.2f}\,\Omega$, "
        rf"$\Gamma_{{\rm EM\to rad}}\approx{gamma_em_into_rad:.3f}$)",
        fontsize=10.0,
    )
    ax.text(0.5, 0.015,
            r"mixed impedance domains: only $Z_{\rm EM}$ is electrical ($\Omega$); "
            r"$Z_{\rm shear},Z_{\rm bulk}$ mechanical/acoustic. Consistency re-expression of "
            r"the three-impedance law (foundation repair, open gates) — not a substrate primitive.",
            transform=ax.transAxes, ha="center", va="bottom", fontsize=7.2,
            bbox=dict(boxstyle="round", fc="#f4f6f7", ec="grey", alpha=0.95))
    p = os.path.join(_FIG_DIR, "vol9_graded_network_schematic.png")
    fig.tight_layout()
    fig.savefig(p, dpi=DPI)
    plt.close(fig)
    return p


def main() -> None:
    print("GRADED VACUUM IMPEDANCE NETWORK — figure generation (deterministic, engine-sourced)")
    print("=" * 78)
    p_i = fig_i_schematic()
    print(f"  (i)   schematic        -> {os.path.relpath(p_i, _REPO_SRC)}  ({os.path.getsize(p_i)} B)")
    p_ii = fig_ii_smith()
    print(f"  (ii)  smith/Gamma      -> {os.path.relpath(p_ii, _REPO_SRC)}  ({os.path.getsize(p_ii)} B)")
    p_iv = fig_iv_op_sweep()
    print(f"  (iv)  op-sweep         -> {os.path.relpath(p_iv, _REPO_SRC)}  ({os.path.getsize(p_iv)} B)")
    print("  (iii) running α-free cold-cage FDTD ring-down (N=72/6000, ~40 s)...")
    d_iii = fig_iii_forkA_discriminator()
    print(f"  (iii) forkA discrim.   -> {os.path.relpath(d_iii['path'], _REPO_SRC)}  ({os.path.getsize(d_iii['path'])} B)")
    print("=" * 78)
    print("ENGINE ANCHORS (live):")
    print(f"  cold-cage Q_ringdown      = {d_iii['Q_cold_ringdown']:.4f}   (canonical anchor ≈ 30.8, NOT 137)")
    print(f"  cold-cage Q_linewidth     = {d_iii['Q_linewidth']:.4f}   (≈ 3.8)")
    print(f"  ω_cutoff                  = {d_iii['omega_cutoff']:.4f} rad/time")
    print(f"  radiative floor Z_RAD     = {d_iii['Z_radiation']:.4f} Ω (band-consistent, DEC-5)")
    print(f"  isolation Q(N) open sweep = {[round(q, 1) for q in d_iii['Q_open_sweep']]}  (→ ∞, lossless-confined)")
    print(f"  isolation Q closed = ∞ ?  = {d_iii['Q_closed_is_inf']}")
    print(f"  c_L/c_T (bulk/shear)      = {RATIO_BULK_SHEAR_MECH:.5f}   (α-free, DERIVED)")
    print("=" * 78)
    print("DONE — 4 PNGs written to", os.path.relpath(_FIG_DIR, _REPO_SRC))
    print("  slot (iii) coupled arm = DEFERRED-pending-H_couple (NOT faked).")


if __name__ == "__main__":
    main()
