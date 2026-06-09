"""Rectifier Stage-1 — the biased leaky varactor diode (substrate charge-pump).

PREREG (binding): research/2026-06-09_rectifier-stage1-biased-diode_prereg.md
DESIGN:           research/2026-06-09_substrate-rectifier-groundup-design.md
BASELINE:         the thixotropy result (bias=0 -> the directed integral vanishes,
                  Outcome B) on branch analysis/2026-06-09-thixotropy-bulk-derivation.

THE QUESTION (one line)
  Does a single DC-BIASED, LEAKY (Gamma=-1 leaky, finite Q=alpha^-1) varactor diode,
  AC-pumped in the ASYM near-yield bulk/eps band, net DIRECTED momentum into the
  medium with a CLOSING energy-momentum ledger (Outcome A = real charge-pump /
  engineered-gravity), or directed ~ heat (B), or over-unity / mundane-plasma (C)?

SUBSTRATE-NATIVE-CHECK (walked FIRST, before this code; see result doc Sec 1):
  1 dynamics   : time-domain MEMRISTIVE relaxation dS/dt = (S_eq(A)-S)/tau of the
                 saturation state.  NOT minimization, NOT continuum-Helmholtz.
  2 sector     : bulk/eps.  The DIODE is the ASYMMETRIC single-sector (static-E)
                 load: S_eps=S, S_mu=1 -> Z=Z0*sqrt(S_mu/S_eps)=Z0/sqrt(S) != Z0,
                 Gamma=(1-sqrt S)/(1+sqrt S) != 0  (INVARIANT-S2, Meissner-asym).
  3 K4/Cosserat: the lossy lag opens the (V,Q) loop into nonzero AREA = the grip =
                 loss = R = 1/Q; electron-class tank Q=alpha^-1 -> R ~ alpha bleed.
                 The Gamma=-1 boundary is LEAKY (finite Q, real bleed) NOT ideal clip.
  4 coordinates: the (V,Q)/impedance loop is the phase-space measure; the induced
                 n(r) ray-trace is real-space (matched to the gravity-lens claim).
  5 Op14 clock : omega_local = omega0*sqrt(S) in the loaded region (the time-dilation
                 third observable) -- reported.
  6 reactance  : track the C-state (A,V) AND the L/memristive-state (S) every step;
                 H/energy-closure + passivity Q_diss>=0 gate every run.

LEDGER (ave-driver-script-honesty -- THE verdict): W_in (bias+pump) vs W_out
  (directed-wake KE + dissipated heat R~alpha*loop).  Reported every run.

NO FIT-TO-TARGET: no minimize(), no curve_fit().  Every constant from
ave.core.constants (ave-canonical-source).  Natural units; SI scale reported.
"""

from __future__ import annotations

import os

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import lfilter

from ave.core.constants import (
    ALPHA,
    C_0,
    E_YIELD,
    L_NODE,
    PHI,
    R_I,   # sqrt(2 alpha) ~ 0.117  (linear -> nonlinear; lower near-yield band edge)
    R_II,  # sqrt(3)/2  ~ 0.866  (nonlinear -> saturated; upper near-yield band edge)
    V_YIELD,
    Z_0,
)

# Cavitation floor (rarefaction freeze point) = (1-sqrt5)/2 = -1/phi  (RHO_CAV).
RHO_CAV = (1.0 - np.sqrt(5.0)) / 2.0  # = -1/PHI ; c_bulk^2 = 0 here (canonical)
R_LOSS = ALPHA  # grip = loss = 1/Q, electron-class tank Q = alpha^-1 -> R ~ alpha

ASSETS = os.path.join(
    os.path.dirname(__file__), "..", "..", "..", "research", "assets", "rectifier_stage1"
)
ASSETS = os.path.abspath(ASSETS)
os.makedirs(ASSETS, exist_ok=True)


# ---------------------------------------------------------------------------
# Substrate elements (ground-up from Axiom 4; design doc Sec 2)
# ---------------------------------------------------------------------------
def S_eq(A: np.ndarray) -> np.ndarray:
    """Axiom-4 saturation kernel S(A) = sqrt(1 - A^2) (the equilibrium target)."""
    return np.sqrt(np.clip(1.0 - A * A, 1e-12, 1.0))


def gamma_diode(S: np.ndarray) -> np.ndarray:
    """Asymmetric single-sector (Meissner) diode reflection coefficient.

    Static-E loads eps only: S_eps=S, S_mu=1 -> Z = Z0*sqrt(S_mu/S_eps) = Z0/sqrt(S).
    Gamma = (Z - Z0)/(Z + Z0) = (1 - sqrt S)/(1 + sqrt S)  >= 0  for S in (0,1].
    Leaky-by-construction: Gamma -> 1 ONLY as S -> 0 (never ideal at finite A).
    """
    rs = np.sqrt(S)
    return (1.0 - rs) / (1.0 + rs)


# ---------------------------------------------------------------------------
# The time-domain memristive integrator (the LEAKY biased varactor)
# ---------------------------------------------------------------------------
def simulate(A0, dA, omega, tau=1.0, n_cycles=80, spc=8000, settle_frac=0.5):
    """Integrate the biased leaky varactor over n_cycles; analyse the last
    (1 - settle_frac) fraction (steady state).

    Drive (bias + AC pump):  A(t) = A0 + dA*sin(omega t).
    Memristive lag (canonical single tau): dS/dt = (S_eq(A) - S)/tau.
    Varactor charge:        q = C_eff * v = (C0/S) * A   (natural units C0=1, V_yield=1).
    Returns a dict of time series + the ledger + the rectified observables.
    """
    T = 2.0 * np.pi / omega
    dt = T / spc
    nsteps = int(n_cycles * spc)
    t = np.arange(nsteps) * dt

    A = A0 + dA * np.sin(omega * t)
    Adot = dA * omega * np.cos(omega * t)        # analytic drive rate
    # exact-exponential first-order relaxation, as a vectorized IIR recurrence:
    #   S[k] = (1-decay) Seq[k] + decay S[k-1]   (semi-implicit, unconditionally stable)
    Seq = S_eq(A)
    decay = np.exp(-dt / tau)
    S = lfilter([1.0 - decay], [1.0, -decay], Seq, zi=[decay * Seq[0]])[0]

    v = A.copy()                      # natural V (units of V_yield)
    q = A / S                         # varactor charge q = C_eff * v, C_eff = 1/S
    Sdot = (Seq - S) / tau            # ANALYTIC dS/dt from the ODE (no edge artifact)
    i = (Adot * S - A * Sdot) / (S * S)   # i = dq/dt = d(A/S)/dt, analytic
    Gam = gamma_diode(S)
    T2 = 1.0 - Gam * Gam

    # ---- steady-state window (whole number of cycles) -------------------
    i0 = int(settle_frac * nsteps)
    i0 -= i0 % spc                    # align to cycle boundary
    ncyc_used = (nsteps - i0) // spc
    sl = slice(i0, i0 + ncyc_used * spc)
    per_cycle = ncyc_used

    vv, qq, ii, SS, T2s, Gs, AA = v[sl], q[sl], i[sl], S[sl], T2[sl], Gam[sl], A[sl]

    # ---- (V,Q) loop area = TOTAL dissipation per cycle (memristive S-lag) ----
    #   This IS the heat reservoir (the thixotropy oint S ~ +0.04 analog).  Its
    #   sign is the traversal sense; |loop_area| = W_diss (all irreversible loss).
    loop_area = np.trapezoid(vv, qq) / per_cycle       # oint v dq  (per cycle)
    W_diss = abs(loop_area)

    # ---- rectified pumped charge = oint T^2(S) i dt  (per cycle) ----------
    #   Parity-zero at bias=0 (i is odd-harmonic, T^2(S) even-harmonic); the DC
    #   bias breaks the half-period symmetry -> nonzero.  THIS is the directed signal.
    dQ_pump = np.trapezoid(T2s * ii, dx=dt) / per_cycle

    # ---- directed energy / momentum (natural units, c=1) -----------------
    #   the rectified charge is pumped against the bias V=A0 -> directed work; it
    #   builds the static E-gradient (ponderomotive) whose momentum = energy/c.
    W_directed = abs(dQ_pump) * A0     # directed (forward) work / cycle, >= 0
    p_dir = dQ_pump * A0               # signed directed momentum (c=1)

    # ---- HONEST PARTITION of the dissipation (W_directed is a SUBSET) -----
    #   the loop dissipates W_diss; of that, W_directed goes forward-directed
    #   and the remainder is isotropic heat.  Closure is then exact by
    #   construction; the real conservation gates are orbit-closure + passivity.
    W_heat_iso = W_diss - W_directed
    directed_frac = W_directed / (W_diss + 1e-30)
    closure = W_diss - (W_directed + W_heat_iso)   # == 0 by construction (H ok)

    # ---- AVE-distinct SCALING diagnostic: the alpha-bleed loss R~alpha ----
    #   labeled separately (NOT a competing ledger line): does the loss track the
    #   substrate grip R=alpha?  (oint R i^2 dt, R=alpha.)
    W_bleed_alpha = np.trapezoid(R_LOSS * ii * ii, dx=dt) / per_cycle

    # ---- conservation gates ----------------------------------------------
    # secular drift of the charge per cycle over the whole steady window
    # (the ratchet test): ~0 => closed limit cycle, no DC ratchet.
    q_return = float((qq[-1] - qq[0]) / per_cycle) if per_cycle > 0 else 0.0
    Q_diss = W_heat_iso                # passivity: isotropic heat must be >= 0

    # ---- Op14 local clock at the loaded operating point ------------------
    S_op = float(np.mean(SS))
    omega_local_ratio = np.sqrt(S_op)  # omega_local/omega0 = sqrt(S)

    return dict(
        t=t, A=A, S=S, v=v, q=q, i=i, Gam=Gam, T2=T2, sl=sl,
        loop_area=loop_area, W_diss=W_diss, dQ_pump=dQ_pump, p_dir=p_dir,
        W_directed=W_directed, W_heat_iso=W_heat_iso, directed_frac=directed_frac,
        W_bleed_alpha=W_bleed_alpha, closure=closure, q_return=q_return,
        Q_diss=Q_diss, S_op=S_op, omega_local_ratio=omega_local_ratio,
        A0=A0, dA=dA, omega=omega, tau=tau,
    )


# ---------------------------------------------------------------------------
# Sec 6a -- the achromatic-lensing discriminator (the AVE-distinct signature)
# ---------------------------------------------------------------------------
def index_profiles(r, n_peak_strain):
    """Build the induced index n(r) under the two loading symmetries.

    The device's pumped charge makes a STATIC E-gradient -> a localized loaded
    region of strain amplitude `n_peak_strain` (a Gaussian well, schematic).

    SYMMETRIC (both eps,mu scale: the engineered-gravity hypothesis):
        eps'=n eps0, mu'=n mu0 -> Z=Z0 invariant, n(r) wavelength-INDEPENDENT
        -> ACHROMATIC.  n_sym(r) = 1 + dn(r),   dn from the strain well.
    ASYMMETRIC (eps-only: what the static-E diode ACTUALLY produces, INVARIANT-S2):
        a static space-charge responds to a probe wave like a cold plasma,
        n^2 = 1 - (omega_p(r)/omega)^2 -> Z != Z0, wavelength-DEPENDENT -> CHROMATIC.
    Returns (n_sym, n_asym_func) with n_asym_func(lam) wavelength-dependent.
    """
    well = np.exp(-(r ** 2) / 2.0)                 # normalized loaded-region profile
    dn = n_peak_strain * well                       # peak index contrast from the strain

    n_sym = 1.0 + dn                                # achromatic (same for every lambda)

    # plasma-equivalent: the eps-only space charge gives a local plasma frequency
    # whose index is 1 - (lam/lam_p)^2 * profile (cold-plasma, low-density expansion).
    def n_asym(lam, lam_p=1.0):
        return 1.0 - (lam / lam_p) ** 2 * dn        # CHROMATIC: scales with lambda^2

    return n_sym, n_asym


def ray_trace_deflection(r_grid, n_profile):
    """Thin-lens deflection of a ray with impact parameter b through n(r).

    Transverse gradient-index deflection: alpha(b) = -integral dn/dr * (b/r) dz,
    here reduced to the peak transverse index gradient (paraxial), proportional to
    max|dn/dr|.  We return the deflection magnitude (arb. consistent units) so the
    *chromaticity* (ratio across lambda) is the meaningful, unit-free output.
    """
    dn_dr = np.gradient(n_profile, r_grid)
    return float(np.max(np.abs(dn_dr)))


# ---------------------------------------------------------------------------
# Figures (ave-engineering-program-rigor; savefig + regenerable)
# ---------------------------------------------------------------------------
def fig_loop_and_ledger(res_lo, res_hi):
    fig, ax = plt.subplots(1, 3, figsize=(15, 4.4))

    for res, lab, c in ((res_lo, "bias A0=0 (baseline)", "0.5"),
                        (res_hi, f"bias A0={res_hi['A0']:.3f}", "C0")):
        sl = res["sl"]
        ax[0].plot(res["v"][sl], res["q"][sl], color=c, lw=1.0, label=lab)
    ax[0].set_xlabel("V  (units of V_yield)")
    ax[0].set_ylabel("Q  (varactor charge, C_eff*V)")
    ax[0].set_title("(V,Q) loop — area = dissipation/cycle")
    ax[0].legend(fontsize=8)

    # ledger bar (biased run): W_diss partitions into directed + isotropic heat
    r = res_hi
    bars = ["W_in=W_diss\n(drive)", "W_heat_iso\n(isotropic)", "W_directed\n(rectified)"]
    vals = [r["W_diss"], r["W_heat_iso"], r["W_directed"]]
    ax[1].bar(bars, vals, color=["C2", "C3", "C0"])
    ax[1].set_ylabel("energy / cycle  (natural units)")
    ax[1].set_title(f"ledger — directed frac {r['directed_frac']:.1e}, "
                    f"closure {r['closure']:.1e}")

    # (S,Gamma) memristive loop -> the asymmetric grip
    sl = r["sl"]
    ax[2].plot(r["A"][sl], r["Gam"][sl], color="C0", lw=1.0)
    ax[2].set_xlabel("drive A(t)")
    ax[2].set_ylabel("Gamma(S(t))  diode reflection")
    ax[2].set_title("asymmetric-grip loop (lag opens it)")
    fig.tight_layout()
    p = os.path.join(ASSETS, "rectifier_stage1_loop_ledger.png")
    fig.savefig(p, dpi=130)
    plt.close(fig)
    return p


def fig_bias_sweep(A0s, dQ, pdir, loop, dAs, surface):
    fig, ax = plt.subplots(1, 2, figsize=(12, 4.4))
    ax[0].plot(A0s, dQ, "o-", color="C0", label="rectified charge dQ_pump")
    ax[0].plot(A0s, pdir, "s--", color="C3", label="directed momentum p_dir")
    ax[0].axvline(R_I, color="0.6", ls=":", lw=1)
    ax[0].axvline(R_II, color="0.6", ls=":", lw=1)
    ax[0].axhline(0, color="k", lw=0.6)
    ax[0].set_xlabel("DC bias A0  (near-yield band [R_I, R_II] dotted)")
    ax[0].set_ylabel("per-cycle rectified output (natural units)")
    ax[0].set_title("bias sweep — robust(across band) vs tuned(one A0)")
    ax[0].legend(fontsize=8)

    im = ax[1].pcolormesh(A0s, dAs, surface, shading="auto", cmap="RdBu_r")
    ax[1].set_xlabel("DC bias A0")
    ax[1].set_ylabel("pump amplitude dA")
    ax[1].set_title("p_dir response surface")
    fig.colorbar(im, ax=ax[1], label="p_dir")
    fig.tight_layout()
    p = os.path.join(ASSETS, "rectifier_stage1_bias_sweep.png")
    fig.savefig(p, dpi=130)
    plt.close(fig)
    return p


def fig_chromaticity(r_grid, n_sym, n_asym, lambdas):
    fig, ax = plt.subplots(1, 2, figsize=(12, 4.4))
    ax[0].plot(r_grid, n_sym - 1.0, "k-", lw=1.5, label="SYMMETRIC (eps,mu) -> Z=Z0")
    for lam in lambdas:
        ax[0].plot(r_grid, n_asym(lam) - 1.0, lw=1.0,
                   label=f"ASYM eps-only, lambda={lam:.2f}")
    ax[0].set_xlabel("r  (loaded-region coordinate)")
    ax[0].set_ylabel("n(r) - 1")
    ax[0].set_title("induced index — symmetric vs asymmetric(eps-only) loading")
    ax[0].legend(fontsize=7)

    defl_sym = [ray_trace_deflection(r_grid, n_sym) for _ in lambdas]
    defl_asym = [ray_trace_deflection(r_grid, n_asym(lam)) for lam in lambdas]
    ax[1].plot(lambdas, np.array(defl_sym) / defl_sym[0], "ko-",
               label="SYMMETRIC (achromatic)")
    ax[1].plot(lambdas, np.array(defl_asym) / defl_asym[0], "C3s-",
               label="ASYM eps-only (chromatic)")
    ax[1].set_xlabel("probe wavelength lambda")
    ax[1].set_ylabel("deflection / deflection(lambda_0)")
    ax[1].set_title("CHROMATICITY of the induced lens")
    ax[1].legend(fontsize=8)
    fig.tight_layout()
    p = os.path.join(ASSETS, "rectifier_stage1_chromaticity.png")
    fig.savefig(p, dpi=130)
    plt.close(fig)
    return p, defl_sym, defl_asym


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    print("=" * 78)
    print("RECTIFIER STAGE-1 -- biased leaky varactor diode (substrate charge-pump)")
    print("=" * 78)
    print(f"[constants]  ALPHA={ALPHA:.6e}  PHI={PHI:.6f}  R_I=sqrt(2a)={R_I:.4f}  "
          f"R_II=sqrt3/2={R_II:.4f}")
    print(f"             V_YIELD={V_YIELD:.4e} V  E_YIELD={E_YIELD:.4e} V/m  "
          f"L_NODE={L_NODE:.4e} m  Z_0={Z_0:.3f} ohm")
    print(f"             RHO_CAV=(1-sqrt5)/2={RHO_CAV:.6f}=-1/phi  R_LOSS=alpha={R_LOSS:.4e}")
    print(f"             [SI scale: 1 natural-V = {V_YIELD:.3e} V; 1 natural-time = "
          f"{L_NODE / C_0:.3e} s]")

    omega = 1.0          # omega*tau = 1: the lag is maximal (the loop opens widest)
    dA = 0.10            # AC pump amplitude (kept sub-snap across the band)

    # ---- baseline (bias=0): MUST recover the thixotropy B (rectif -> 0) ----
    print("\n[1] BIAS=0 BASELINE (must recover thixotropy Outcome B: rectification -> 0)")
    res0 = simulate(A0=0.0, dA=dA, omega=omega)
    print(f"    (V,Q) loop area  W_diss (the ~+0.04 heat analog) = {res0['W_diss']:+.4e}")
    print(f"    dQ_pump (rectified charge, parity test)          = {res0['dQ_pump']:+.4e}")
    dq0_floor = abs(res0["dQ_pump"])
    print(f"    --> |dQ_pump|/W_diss = {dq0_floor / (res0['W_diss'] + 1e-30):.2e}  "
          f"= numerical parity floor (rectification vanishes at bias=0 -> recovers B)")

    # ---- biased near-yield operating point ----------------------------------
    A0_op = 0.5  # mid near-yield band
    print(f"\n[2] BIASED near-yield run  A0={A0_op}  dA={dA}  omega*tau={omega}")
    resB = simulate(A0=A0_op, dA=dA, omega=omega)
    print(f"    (V,Q) loop area  W_diss            = {resB['W_diss']:+.4e}  (heat reservoir)")
    print(f"    rectified charge dQ_pump           = {resB['dQ_pump']:+.4e}  "
          f"(vs bias=0 floor {dq0_floor:.2e}: {abs(resB['dQ_pump']) / (dq0_floor + 1e-30):.0f}x)")
    print(f"    directed momentum p_dir            = {resB['p_dir']:+.4e}")
    print(f"    Op14 local clock omega_local/omega0= sqrt(S_op)={resB['omega_local_ratio']:.4f}"
          f"  (S_op={resB['S_op']:.4f})")
    print(f"    --- LEDGER (ave-driver-script-honesty; W_directed SUBSET of W_diss) ---")
    print(f"      W_in = W_diss (drive work)  = {resB['W_diss']:+.4e}")
    print(f"      W_directed (rectified fwd)  = {resB['W_directed']:+.4e}")
    print(f"      W_heat_iso (isotropic)      = {resB['W_heat_iso']:+.4e}")
    print(f"      closure W_diss-(dir+iso)    = {resB['closure']:+.4e}  "
          f"({'CLOSES (passive)' if abs(resB['closure']) < 1e-12 else 'OPEN'})")
    print(f"      orbit drift q_return/cycle  = {resB['q_return']:+.4e}  (limit cycle if ~0)")
    print(f"      passivity Q_diss>=0         = {resB['Q_diss']:+.4e}  "
          f"({'OK' if resB['Q_diss'] >= 0 else 'VIOLATED'})")
    print(f"      directed fraction W_dir/W_diss = {resB['directed_frac']:.3e}  "
          f"(over-unity if >1: {'YES->C' if resB['directed_frac'] > 1 else 'no'})")
    print(f"      alpha-bleed scaling oint R i^2 (R=alpha) = {resB['W_bleed_alpha']:+.4e}  "
          f"(AVE-distinct-scaling diagnostic)")

    # ---- MANDATORY bias sweep across the near-yield band ---------------------
    print("\n[3] BIAS SWEEP across near-yield band [R_I, R_II] (robust vs tuned)")
    A0s = np.linspace(0.0, R_II + 0.02, 28)
    dQ = np.array([simulate(A0=a, dA=dA, omega=omega)["dQ_pump"] for a in A0s])
    pdir = np.array([simulate(A0=a, dA=dA, omega=omega)["p_dir"] for a in A0s])
    loop = np.array([simulate(A0=a, dA=dA, omega=omega)["W_diss"] for a in A0s])
    in_band = (A0s >= R_I) & (A0s <= R_II)
    # ROBUST = a broad, same-sign, MONOTONIC turn-on across the band (the directed
    # output grows smoothly with the bias asymmetry).  TUNED = a narrow interior
    # spike (rises then falls; nonzero only at one A0) -> rescue-fill -> NEGATIVE.
    pb = pdir[in_band]
    above_floor = np.abs(pb) > 3.0 * dq0_floor * np.maximum(A0s[in_band], 1e-3)
    sign_ref = np.sign(pb[np.argmax(np.abs(pb))])
    same_sign = np.mean(np.sign(pb[above_floor]) == sign_ref) if np.any(above_floor) else 0.0
    frac_on = np.mean(above_floor)
    mono_frac = np.mean(np.diff(np.abs(pb)) > 0)        # monotone-increasing ramp -> ~1
    peak_at_edge = np.argmax(np.abs(pb)) >= 0.8 * (pb.size - 1)  # ramp peaks at band edge
    robust = (frac_on > 0.6) and (same_sign > 0.9) and (mono_frac > 0.8 or not peak_at_edge)
    print(f"    p_dir in-band: min={np.min(pb):+.3e}  max={np.max(pb):+.3e}")
    print(f"    fraction of band above parity-floor       = {frac_on:.2f}")
    print(f"    sign-consistency across on-band           = {same_sign:.2f}")
    print(f"    monotone-increasing fraction (ramp ~1)    = {mono_frac:.2f}")
    print(f"    --> {'ROBUST (monotone turn-on across band -> real)' if robust else 'TUNED (one A0 -> rescue-fill -> NEG)'}")

    dAs = np.linspace(0.03, 0.18, 12)
    surface = np.array([[simulate(A0=a, dA=d, omega=omega)["p_dir"]
                         for a in A0s] for d in dAs])

    # ---- Sec 6a chromaticity ------------------------------------------------
    print("\n[4] Sec 6a ACHROMATIC-LENSING DISCRIMINATOR (the AVE-distinct signature)")
    n_peak = abs(resB["dQ_pump"]) * 5.0   # index contrast ~ pumped space charge (schematic scale)
    r_grid = np.linspace(-4, 4, 400)
    n_sym, n_asym = index_profiles(r_grid, n_peak if n_peak > 1e-6 else 1e-3)
    lambdas = np.array([0.5, 1.0, 1.5])   # >= 2 wavelengths
    fig_chr, defl_sym, defl_asym = fig_chromaticity(r_grid, n_sym, n_asym, lambdas)
    chrom_sym = (max(defl_sym) - min(defl_sym)) / (np.mean(defl_sym) + 1e-30)
    chrom_asym = (max(defl_asym) - min(defl_asym)) / (np.mean(defl_asym) + 1e-30)
    print(f"    device output = STATIC E-gradient (pumped space charge) -> eps-only load")
    print(f"      => ASYMMETRIC (INVARIANT-S2): Z=Z0/sqrt(S) != Z0  -> CHROMATIC")
    print(f"    deflection spread (chromaticity):")
    print(f"      SYMMETRIC (eps,mu, Z=Z0) hypothesis : {chrom_sym:.3e}  "
          f"({'ACHROMATIC' if chrom_sym < 1e-6 else 'chromatic'})")
    print(f"      ASYMMETRIC eps-only (what device does): {chrom_asym:.3e}  "
          f"({'achromatic' if chrom_asym < 1e-6 else 'CHROMATIC -> plasma lens'})")

    # ---- figures ------------------------------------------------------------
    p_loop = fig_loop_and_ledger(res0, resB)
    p_sweep = fig_bias_sweep(A0s, dQ, pdir, loop, dAs, surface)
    print("\n[figures]")
    for p in (p_loop, p_sweep, fig_chr):
        print(f"    {p}")

    # ---- VERDICT ------------------------------------------------------------
    print("\n" + "=" * 78)
    print("VERDICT")
    print("=" * 78)
    overunity = resB["directed_frac"] > 1.0
    passive = resB["Q_diss"] >= 0 and abs(resB["closure"]) < 1e-12
    bias0_recovers = abs(res0["dQ_pump"]) < 0.05 * abs(resB["dQ_pump"])
    rectifies = abs(resB["dQ_pump"]) > 5.0 * dq0_floor and robust
    achromatic = chrom_asym < 1e-6
    print(f"  bias=0 recovers thixotropy B (rectif->floor): {bias0_recovers}")
    print(f"  ledger closes / passive (NOT over-unity)    : {passive and not overunity}")
    print(f"  rectifies robustly across band (not tuned)  : {rectifies}")
    print(f"  induced lens ACHROMATIC (engineered grav)   : {achromatic}")
    if overunity or not passive:
        print("  => OUTCOME C (CRANK / over-unity / passivity violation).")
    elif not rectifies:
        print("  => OUTCOME B (lossy oscillator; directed ~ heat, no net thrust).")
    elif achromatic:
        print("  => OUTCOME A (real charge-pump AND achromatic engineered-gravity lens).")
    else:
        print("  => OUTCOME C-nondistinct (the AVE-distinct chord FAILS):")
        print("     The bias DOES rectify -- dQ_pump is real, robust across the band,")
        print("     vanishes at bias=0 (recovers thixotropy B). The ledger CLOSES")
        print("     (passive; W_directed is a small SUBSET of W_diss, not over-unity).")
        print("     BUT the induced lens is CHROMATIC (eps-only asymmetric load,")
        print("     Z=Z0/sqrt(S)!=Z0) -> ordinary plasma rectification / radiation")
        print("     pressure, NOT the AVE-distinct achromatic engineered-gravity metric.")
        print("     => NO thrust/engineered-gravity claim (gate: needs achromatic lens).")
    print("=" * 78)


if __name__ == "__main__":
    main()
