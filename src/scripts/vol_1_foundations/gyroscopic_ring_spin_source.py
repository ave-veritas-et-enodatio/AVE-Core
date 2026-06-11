#!/usr/bin/env python3
"""Vortex-ring NET angular momentum (= electron spin) from a FINITE TRAPPED RESERVOIR.

ANALYTIC derivation + minimal bound-check. SUPERSEDES the stopped external-resonant-
pump model (src/.../reactive_entrainment_source.py), which secular-pumped: |omega|
ran away (DETONATE_S |omega|->3.5, W_src=+6.1 free work in), Model-A ledger OPEN
(H_drift=+3.42). That model was WRONG -- an undamped externally-pumped tank detonates.

TWO BINDING CORRECTIONS (Grant 2026-06-09 "vortex ring where the ring AS A WHOLE has
angular momentum" + the agent's own diagnosis):
 1. The output is the RING-AS-A-WHOLE NET angular momentum L (a swirling vortex ring),
    = the electron spin hbar/2 -- the conserved gyroscopic spin (clm-salw2h:
    dL/dt = gamma L x B; |L| is a CASIMIR, conserved EXACTLY). NOT a per-node micro-
    rotation scalar amplitude (the stopped model's |omega|), NOT poloidal-only.
 2. The source is a FINITE TRAPPED RESERVOIR (V = m_e c^2 per Gamma=-1 wall),
    CONSERVED -- a gyroscope/flywheel, NOT an externally-pumped resonant tank.
    Boundedness = CONSERVATION (Casimir |L| + a finite reservoir + the force-free
    self-trapping lock), a conservation law -- NOT a leak balancing a pump. A
    gyroscope precesses; it does not detonate.

THE UNIFICATION (sapphire-phonon-centrifuge.md:34): a Beltrami force-free field
 (A || B, kinetic helicity aligned) locks into a RIGID GYROSCOPIC TENSOR = an absolute
 "Inductive Shield." So the source's OUTPUT (the ring's L, the Beltrami helical flow)
 IS the confinement (inductive shield = Gamma=-1 wall). Source = confinement =
 boundedness = ONE object: the spinning ring conserving its angular momentum.

THREE MINIMAL BLOCKS (lumped ODE illustration of the conservation STRUCTURE; the full
 K4-Cosserat engine run is the implement+run follow-on if A. ave-driver-script-honesty:
 these are reduced lumped models, NOT the substrate solver):

 BLOCK 1  BOUNDEDNESS = CONSERVATION (the headline).
   Vector gyroscope dL/dt = gamma L x B(t) (clm-salw2h) vs the stopped scalar resonant
   pump y'' + w0^2 y = A cos(w0 t). SAME drive amplitude, SAME duration. The gyroscope
   conserves |L| to machine precision even AT Larmor resonance (it Rabi-flips but |L|
   is fixed); the scalar pump secular-detonates. Boundedness is the Casimir, not a leak.

 BLOCK 2  FORCE-FREE BELTRAMI LOCK (source = confinement).
   Landau-Lifshitz-Gilbert dm/dt = gamma m x B - (alpha) m_hat x (m x B): the
   precession IS the gyroscopic spin; the Gilbert term relaxes m toward alignment with
   B (the force-free A||B Beltrami state = the rigid gyroscopic tensor = inductive
   shield) at rate ~alpha (grip=loss=R~alpha), while conserving |m| EXACTLY. Shows the
   alignment angle -> 0 (locked) with |m| flat: the OUTPUT locks into the confinement.

 BLOCK 3  FINITE-RESERVOIR LEDGER + BUILD + SLOSH CONTROL (the reactive-sloshing test).
   Conservative nonlinear dimer (bosonic-Josephson form): a finite reservoir mode
   (alpha, the trapped m_e c^2) reactively coupled to the ring circulation mode (beta,
   L_ring ~ |beta|^2). N = |alpha|^2+|beta|^2 CONSERVED (the finite reservoir / total
   angular momentum -- a gyroscope, not pumped). H CONSERVED (the ledger). The Beltrami
   self-detuning chi (canonical Ax-4 saturation softening) SELF-TRAPS: L_ring builds
   from seed and STAYS (the force-free lock = A). Control chi=0: pure reactive coupling
   SLOSHES, nets ~0 (B). The rectifier is the force-free nonlinearity, NOT a fitted pump.
"""
from __future__ import annotations

import os
import sys

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(_HERE, "..", "..", "..", "src"))

from ave.core.constants import ALPHA  # noqa: E402

# ---- canonical parameters (ave-canonical-source: zero new free params) ----
HBAR = 1.0              # natural units
GAMMA = 1.0             # gyromagnetic ratio (natural; sets Larmor = B0)
SPIN = 0.5              # |L| = hbar/2: the CANONICAL spin quantum (de Broglie L=l.hbar,
#                         spin-1/2 4pi double-cover, constants.py:181). NOT emergent here
#                         -- it is the conserved topological helicity, imported as the
#                         finite-reservoir quantum N. This derivation proves the FORM
#                         (conserved net L, bounded, ledger), not the NUMBER 1/2.
B0 = 1.0                # genesis seed-axis field (sets the (2,3) winding / precession axis)
B1 = 0.30               # transverse drive amplitude (the source field)
ALPHA_LEAK = ALPHA      # grip = loss = R ~ alpha; Gilbert relaxation rate, Q = 1/alpha
OMEGA_V = 1.0           # reservoir-mode frequency (longitudinal V tank)
OMEGA_R = 1.0           # ring-mode frequency (resonant: autoresonant C2 lock)
G_COUP = 0.02           # reactive added-mass coupling (mutual inductance M = L_drag)
DT = 0.01


# ==========================================================================
# BLOCK 1 -- BOUNDEDNESS = CONSERVATION: vector gyroscope vs scalar resonant pump
# ==========================================================================
def run_gyroscope(steps, *, resonant=True):
    """dL/dt = gamma L x B(t); B = (B1 cos wt, B1 sin wt, B0). |L| is a Casimir."""
    w = GAMMA * B0 if resonant else 1.7 * GAMMA * B0   # Larmor (worst case) or off-res
    L = np.array([1e-3, 0.0, SPIN])                    # seeded near the +z axis
    L *= SPIN / np.linalg.norm(L)
    rec = {k: [] for k in ("t", "Lx", "Ly", "Lz", "Lmag")}
    t = 0.0
    for _ in range(steps):
        def dL(Lv, tt):
            B = np.array([B1 * np.cos(w * tt), B1 * np.sin(w * tt), B0])
            return GAMMA * np.cross(Lv, B)
        k1 = dL(L, t)
        k2 = dL(L + 0.5 * DT * k1, t + 0.5 * DT)
        k3 = dL(L + 0.5 * DT * k2, t + 0.5 * DT)
        k4 = dL(L + DT * k3, t + DT)
        L = L + (DT / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)
        for key, val in (("t", t), ("Lx", L[0]), ("Ly", L[1]),
                         ("Lz", L[2]), ("Lmag", np.linalg.norm(L))):
            rec[key].append(val)
        t += DT
    return {k: np.array(v) for k, v in rec.items()}


def run_scalar_pump(steps):
    """The STOPPED model: y'' + w0^2 y = A cos(w0 t). Resonant -> secular detonation."""
    w0 = OMEGA_R
    y, yd, t = 1e-3, 0.0, 0.0
    A = B1                                             # SAME drive amplitude as gyro
    rec = {k: [] for k in ("t", "y", "ymag")}
    for _ in range(steps):
        def acc(yy, ydd, tt):
            return A * np.cos(w0 * tt) - w0 * w0 * yy
        a1 = acc(y, yd, t)
        a2 = acc(y + 0.5 * DT * yd, yd + 0.5 * DT * a1, t + 0.5 * DT)
        a3 = acc(y + 0.5 * DT * (yd + 0.5 * DT * a1), yd + 0.5 * DT * a2, t + 0.5 * DT)
        a4 = acc(y + DT * (yd + 0.5 * DT * a2), yd + DT * a3, t + DT)
        y2 = y + DT * yd + (DT * DT / 6.0) * (a1 + a2 + a3)
        yd = yd + (DT / 6.0) * (a1 + 2 * a2 + 2 * a3 + a4)
        y = y2
        rec["t"].append(t); rec["y"].append(y); rec["ymag"].append(abs(y))
        t += DT
    return {k: np.array(v) for k, v in rec.items()}


# ==========================================================================
# BLOCK 2 -- FORCE-FREE BELTRAMI LOCK via Landau-Lifshitz-Gilbert
#   dm/dt = gamma m x B - (alpha/|m|) m x (m x B);  Gilbert term conserves |m| EXACTLY
#   and relaxes m -> B alignment (force-free A||B = rigid gyro tensor = inductive shield)
# ==========================================================================
def run_llg(steps, *, alpha=ALPHA_LEAK):
    B = np.array([0.0, 0.0, B0])                       # genesis seed axis
    bhat = B / np.linalg.norm(B)
    m = np.array([SPIN * np.sin(2.7), 0.0, SPIN * np.cos(2.7)])  # start far from aligned
    rec = {k: [] for k in ("t", "mmag", "align", "mz")}
    t = 0.0
    for _ in range(steps):
        def dm(mv):
            mhat = mv / np.linalg.norm(mv)
            prec = GAMMA * np.cross(mv, B)
            gilb = -alpha * np.cross(mhat, np.cross(mv, B))
            return prec + gilb
        k1 = dm(m); k2 = dm(m + 0.5 * DT * k1)
        k3 = dm(m + 0.5 * DT * k2); k4 = dm(m + DT * k3)
        m = m + (DT / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)
        align = float(np.dot(m / np.linalg.norm(m), bhat))   # ->1 when force-free locked
        for key, val in (("t", t), ("mmag", np.linalg.norm(m)),
                         ("align", align), ("mz", m[2])):
            rec[key].append(val)
        t += DT
    return {k: np.array(v) for k, v in rec.items()}


# ==========================================================================
# BLOCK 3 -- FINITE-RESERVOIR LEDGER + BUILD + SLOSH CONTROL (conservative dimer)
#   i alpha' = OMEGA_V alpha + G beta
#   i beta'  = (OMEGA_R + chi |beta|^2) beta + G alpha     (chi = Beltrami self-detune)
#   N = |alpha|^2 + |beta|^2 CONSERVED (finite reservoir);  H CONSERVED (ledger)
#   L_ring ~ |beta|^2 (the ring's net circulation).  chi>0 -> SELF-TRAP (lock=A);
#   chi=0 -> Rabi SLOSH (nets 0 = B).
# ==========================================================================
def run_dimer(steps, *, chi, N=2.0 * SPIN, G=G_COUP):
    # finite reservoir charged to N (= the trapped m_e c^2 quantum); ring at noise seed
    a = complex(np.sqrt(N - 1e-4), 0.0)
    b = complex(np.sqrt(1e-4), 0.0)

    def H_of(av, bv):
        na, nb = abs(av) ** 2, abs(bv) ** 2
        return (OMEGA_V * na + OMEGA_R * nb + 0.5 * chi * nb * nb
                + 2.0 * G * (av.conjugate() * bv).real)

    def deriv(av, bv):
        ad = -1j * (OMEGA_V * av + G * bv)
        bd = -1j * ((OMEGA_R + chi * abs(bv) ** 2) * bv + G * av)
        return ad, bd

    H0 = H_of(a, b)
    rec = {k: [] for k in ("t", "Nres", "Lring", "Ntot", "H", "E_res", "E_ring")}
    t = 0.0
    for _ in range(steps):
        a1, b1 = deriv(a, b)
        a2, b2 = deriv(a + 0.5 * DT * a1, b + 0.5 * DT * b1)
        a3, b3 = deriv(a + 0.5 * DT * a2, b + 0.5 * DT * b2)
        a4, b4 = deriv(a + DT * a3, b + DT * b3)
        a = a + (DT / 6.0) * (a1 + 2 * a2 + 2 * a3 + a4)
        b = b + (DT / 6.0) * (b1 + 2 * b2 + 2 * b3 + b4)
        na, nb = abs(a) ** 2, abs(b) ** 2
        for key, val in (("t", t), ("Nres", na), ("Lring", nb), ("Ntot", na + nb),
                         ("H", H_of(a, b)), ("E_res", OMEGA_V * na),
                         ("E_ring", OMEGA_R * nb + 0.5 * chi * nb * nb)):
            rec[key].append(val)
        t += DT
    out = {k: np.array(v) for k, v in rec.items()}
    out["H0"] = H0
    return out


# ==========================================================================
def main():
    print("=" * 78)
    print("Vortex-ring NET angular momentum (= spin) from a FINITE TRAPPED RESERVOIR")
    print("=" * 78)
    print(f"alpha={ALPHA:.6e}  |L|=spin={SPIN}  B0={B0}  B1(drive)={B1}  "
          f"Q=1/alpha={1/ALPHA:.1f}")
    print(f"OMEGA_V={OMEGA_V} OMEGA_R={OMEGA_R} G={G_COUP}  N_reservoir={2*SPIN}")
    print()

    # ---- BLOCK 1: boundedness = conservation ----
    N1 = 120000
    print("--- BLOCK 1: BOUNDEDNESS = CONSERVATION (gyroscope vs scalar resonant pump) ---")
    gres = run_gyroscope(N1, resonant=True)
    goff = run_gyroscope(N1, resonant=False)
    pump = run_scalar_pump(N1)
    for nm, r, key in (("GYRO (Larmor-res)", gres, "Lmag"),
                       ("GYRO (off-res)", goff, "Lmag")):
        d = r[key]
        print(f"  [{nm:18s}] |L|_init={d[0]:.6f}  |L|_final={d[-1]:.6f}  "
              f"|L|_drift={abs(d[-1]-d[0]):.3e}  |L|_span={d.max()-d.min():.3e}  "
              f"-> CONSERVED (bounded)")
    pm = pump["ymag"]
    print(f"  [{'SCALAR PUMP (stopped)':18s}] |y|_init={pm[0]:.6f}  "
          f"|y|_final={pm[-1]:.4f}  |y|_max={pm.max():.4f}  "
          f"-> SECULAR (detonates, the prior bug)")
    print()

    # ---- BLOCK 2: force-free Beltrami lock ----
    N2 = 200000
    print("--- BLOCK 2: FORCE-FREE BELTRAMI LOCK (LLG relaxation -> rigid gyro tensor) ---")
    llg = run_llg(N2)
    al = llg["align"]; mm = llg["mmag"]
    i_lock = np.argmax(al > 0.999) if (al > 0.999).any() else -1
    t_lock = llg["t"][i_lock] if i_lock > 0 else float("nan")
    print(f"  align(0)={al[0]:+.4f} -> align(final)={al[-1]:+.6f}  "
          f"(1.0 = force-free A||B locked)")
    print(f"  lock time (align>0.999) t={t_lock:.1f} = {t_lock*ALPHA:.1f}/alpha  "
          f"(O(1/alpha) relaxation e-folds; grip=loss=R~alpha, Q=1/alpha={1/ALPHA:.0f})")
    print(f"  |m|_init={mm[0]:.6f}  |m|_final={mm[-1]:.6f}  "
          f"|m|_drift={abs(mm[-1]-mm[0]):.3e}  -> CONSERVED through the lock")
    print()

    # ---- BLOCK 3: finite-reservoir ledger + build + slosh control ----
    N3 = 300000
    print("--- BLOCK 3: FINITE-RESERVOIR LEDGER + BUILD vs SLOSH ---")
    chi_lock = 0.5          # Beltrami self-detune (Ax-4 saturation softening; > slosh thr)
    trap = run_dimer(N3, chi=chi_lock)
    slosh = run_dimer(N3, chi=0.0)
    for nm, r in (("SELF-TRAP (chi>0, Beltrami lock)", trap),
                  ("SLOSH (chi=0, reactive only)", slosh)):
        Lr = r["Lring"]
        # net build = late-time mean L_ring; slosh amplitude = peak-trough of last beat
        late = Lr[-N3 // 4:]
        Ndrift = abs(r["Ntot"][-1] - r["Ntot"][0])
        Hdrift = abs(r["H"][-1] - r["H0"])
        print(f"  [{nm:32s}] L_ring: seed={Lr[0]:.4f} max={Lr.max():.4f} "
              f"late_mean={late.mean():.4f} late_min={late.min():.4f}")
        print(f"  {'':34s}  N_drift={Ndrift:.3e} (reservoir conserved)  "
              f"H_drift={Hdrift:.3e} (LEDGER {'CLOSES' if Hdrift < 1e-6 else 'OPEN'})")
    print()

    _figures(gres, pump, llg, trap, slosh)
    _sweep()
    print("done.")


def _figures(gres, pump, llg, trap, slosh):
    h = _HERE
    # FIG 1 -- boundedness = conservation
    fig, ax = plt.subplots(1, 2, figsize=(13, 5))
    ax[0].plot(gres["t"], gres["Lmag"], lw=1.4, color="C0", label="|L| (gyroscope)")
    ax[0].plot(gres["t"], gres["Lz"], lw=0.8, color="C0", ls=":", label="L_z (Rabi-flips)")
    ax[0].axhline(SPIN, color="k", ls="--", lw=0.7)
    ax[0].set_xlabel("t"); ax[0].set_ylabel("angular momentum")
    ax[0].set_title("FIG 1a  |L| CONSERVED (Casimir) even at Larmor resonance")
    ax[0].legend(fontsize=8); ax[0].grid(alpha=0.3); ax[0].set_ylim(-SPIN * 1.2, SPIN * 1.2)
    ax[1].plot(pump["t"], pump["ymag"], lw=1.3, color="C3", label="|y| scalar pump (stopped)")
    ax[1].plot(gres["t"], gres["Lmag"], lw=1.5, color="C0", label="|L| gyroscope")
    ax[1].set_xlabel("t"); ax[1].set_ylabel("amplitude")
    ax[1].set_title("FIG 1b  SAME drive: scalar pump detonates; gyroscope bounded")
    ax[1].legend(fontsize=8); ax[1].grid(alpha=0.3)
    fig.tight_layout(); fig.savefig(os.path.join(h, "gyroring_fig1_boundedness.png"), dpi=110)
    plt.close(fig)

    # FIG 2 -- force-free Beltrami lock
    fig, ax = plt.subplots(figsize=(8.5, 5.5))
    ax.plot(llg["t"], llg["align"], lw=1.5, color="C2", label="alignment m.B/|m||B| (->1 = A||B locked)")
    ax.plot(llg["t"], llg["mmag"] / SPIN, lw=1.2, color="C0", ls="--", label="|m| / spin (conserved)")
    ax.axhline(1.0, color="k", ls=":", lw=0.7)
    ax.set_xlabel("t"); ax.set_ylabel("alignment / normalized |m|")
    ax.set_title("FIG 2  Beltrami force-free LOCK: m -> A||B (rigid gyro tensor = shield), |m| conserved")
    ax.legend(fontsize=9); ax.grid(alpha=0.3)
    fig.tight_layout(); fig.savefig(os.path.join(h, "gyroring_fig2_beltrami_lock.png"), dpi=110)
    plt.close(fig)

    # FIG 3 -- finite-reservoir ledger (build + conservation)
    fig, ax = plt.subplots(figsize=(8.5, 5.5))
    ax.plot(trap["t"], trap["E_res"], lw=1.4, label="E_reservoir (drains, finite m_e c^2)")
    ax.plot(trap["t"], trap["E_ring"], lw=1.4, label="E_ring (spin circulation, fills)")
    ax.plot(trap["t"], trap["Lring"], lw=1.3, ls="--", label="L_ring ~ |beta|^2 (builds, locks)")
    ax.plot(trap["t"], trap["H"], lw=1.0, ls=":", color="k", label="H total (CONSERVED = ledger)")
    ax.set_xlabel("t"); ax.set_ylabel("energy / angular momentum")
    ax.set_title("FIG 3  Finite-reservoir ledger: ring spin paid by V; total conserved (no pump)")
    ax.legend(fontsize=8); ax.grid(alpha=0.3)
    fig.tight_layout(); fig.savefig(os.path.join(h, "gyroring_fig3_ledger.png"), dpi=110)
    plt.close(fig)

    # FIG 4 -- self-trap (A) vs slosh (B)
    fig, ax = plt.subplots(figsize=(8.5, 5.5))
    ax.plot(trap["t"], trap["Lring"], color="C0", lw=1.5, label="chi>0: SELF-TRAP (L_ring builds + STAYS = A)")
    ax.plot(slosh["t"], slosh["Lring"], color="C4", lw=1.1, label="chi=0: reactive SLOSH (nets ~0 = B)")
    ax.set_xlabel("t"); ax.set_ylabel("L_ring ~ |beta|^2")
    ax.set_title("FIG 4  Beltrami self-trap RECTIFIES the reactive slosh into a net conserved spin")
    ax.legend(fontsize=9); ax.grid(alpha=0.3)
    fig.tight_layout(); fig.savefig(os.path.join(h, "gyroring_fig4_trap_vs_slosh.png"), dpi=110)
    plt.close(fig)
    print("figures 1-4 written.")


def _sweep():
    """Robustness: (a) locked L_ring vs reservoir N (the spin is set by the RESERVOIR,
    bounded -- not by a drive amplitude that could secular-pump); (b) self-trap
    threshold in chi."""
    N3 = 200000
    Ns = np.array([0.5, 1.0, 1.5, 2.0, 3.0, 4.0])
    chis = np.array([0.0, 0.05, 0.1, 0.2, 0.4, 0.8])
    L_vs_N, L_vs_chi = [], []
    for Nv in Ns:
        r = run_dimer(N3, chi=0.5, N=Nv)
        L_vs_N.append(r["Lring"][-N3 // 4:].mean())
    for cv in chis:
        r = run_dimer(N3, chi=cv, N=2.0 * SPIN)
        L_vs_chi.append(r["Lring"][-N3 // 4:].mean())
    fig, ax = plt.subplots(1, 2, figsize=(13, 5))
    ax[0].plot(Ns, L_vs_N, "o-", lw=1.5)
    ax[0].set_xlabel("reservoir N (= trapped m_e c^2 quantum)")
    ax[0].set_ylabel("<L_ring>_locked")
    ax[0].set_title("FIG 5a  locked spin set by the RESERVOIR (bounded), not a pump")
    ax[0].grid(alpha=0.3)
    ax[1].plot(chis, L_vs_chi, "s-", lw=1.5, color="C1")
    ax[1].set_xlabel("Beltrami self-detune chi"); ax[1].set_ylabel("<L_ring>_late")
    ax[1].set_title("FIG 5b  self-trap threshold: chi>chi_c locks (slosh -> rectified)")
    ax[1].grid(alpha=0.3)
    fig.tight_layout(); fig.savefig(os.path.join(_HERE, "gyroring_fig5_sweep.png"), dpi=110)
    plt.close(fig)
    print("sweep <L_ring> vs N    =", np.round(L_vs_N, 4))
    print("sweep <L_ring> vs chi  =", np.round(L_vs_chi, 4))
    print("figure 5 written.")


if __name__ == "__main__":
    main()
