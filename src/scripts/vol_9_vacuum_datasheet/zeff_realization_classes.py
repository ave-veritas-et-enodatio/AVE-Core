#!/usr/bin/env python3
"""Dark-sector response characterization — §2 THE Z_eff CURVES (transmission line).

Canonical sector-resolved wall (Op14 asymmetric Meissner form):

    Z_eff = Z0 * sqrt(S_mu / S_eps),   S_x = sqrt(1 - A_x^2)

with the small-signal sector parameters eps_eff = eps0*S_eps, mu_eff = mu0*S_mu
(CLAUDE.md INVARIANT-S2 small-signal block; constants.py:465). THREE realization
classes (universal-saturation-kernel-catalog SYM / ASYM-N(mu) / ASYM-N(eps);
op14-cosmic-horizon-profile.md:23,80-84; operators.md:54):

    SYM     (both sectors load):   S_mu = S_eps = S  ->  Z_eff = Z0      (INVARIANT)
    mu-only (Meissner, B-driven):  S_eps = 1         ->  Z_eff = Z0*sqrt(S_mu) -> 0
    eps-only(static-E / vac mirror):S_mu = 1          ->  Z_eff = Z0/sqrt(S_eps) -> inf

APPROACH PROFILE Z_eff(r): canon gives the LIMIT A^2(r)->1 at the Gamma=-1
saturation surface (op14-cosmic-horizon-profile.md:20) + the Schwarzschild
tracking c_shear = c0*(1-A^2)^(1/4) == c0*sqrt(1-rs/r) (temporal-values:29;
operators.md:56). That identity FORWARD-gives the strain profile
    S(A(r)) = 1 - rs/r        [derived-this-arc; flagged exponent convention]
(the op14-cosmic-horizon-profile.md:22 local-clock uses the STALE 1/2 exponent
=> S=sqrt(1-rs/r); both plotted, flag surfaced — not resolved).

REFLECTIVITY / ECHO PREDICTOR: standard graded-transmission-line reflection
(Born/WKB) -- the reflection per unit length is r(x)=1/2 d(lnZ)/dx and the total
amplitude R(Omega)=INT 1/2 (dlnZ/dx) exp(2i INT k dx') dx. This is TEXTBOOK
transmission-line math (graded impedance match), cited as such, NOT AVE-specific.
Canonical anchor for the SYM=zero-echo result: discrete-lattice-entropy-constant.md:59
("reflection set by the rate of change of Z; symmetric saturation -> dZ/dr=0 ->
no reflection to first order").

Class tags: Z_eff(A^2) three classes = canonical (Op14 forms rendered);
approach profile S(A(r))=1-rs/r = derived-this-arc; reflectivity curve =
derived-this-arc (standard WKB integral over the canonical profile).
"""
from __future__ import annotations

import csv
import os

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

import ave.core.constants as _avc
from ave.core.constants import EPSILON_0, MU_0, Z_0

_trapz = np.trapezoid if hasattr(np, "trapezoid") else np.trapz  # numpy 2.x renamed trapz

assert _avc.__file__.endswith("ave/core/constants.py"), "non-canonical constants source"
assert abs(Z_0 / np.sqrt(MU_0 / EPSILON_0) - 1.0) < 1e-12, "Z0 != sqrt(mu0/eps0)"

HERE = os.path.dirname(os.path.abspath(__file__))
FIGDIR = os.path.normpath(
    os.path.join(HERE, "../../../research/figures/2026-06-11-dark-sector-response")
)
os.makedirs(FIGDIR, exist_ok=True)


def S_of_A2(A2: np.ndarray) -> np.ndarray:
    return np.sqrt(np.clip(1.0 - A2, 0.0, 1.0))


# ----------------------------------------------------------------------
# §2.1 Z_eff(A^2) for the three realization classes
# ----------------------------------------------------------------------
A2 = np.linspace(0.0, 0.999, 500)
S = S_of_A2(A2)
Z_sym = np.full_like(A2, Z_0)              # S_mu=S_eps -> Z0
Z_mu = Z_0 * np.sqrt(S)                    # mu-only: Z0*sqrt(S_mu), S_eps=1 -> 0
Z_eps = Z_0 / np.sqrt(S)                   # eps-only: Z0/sqrt(S_eps), S_mu=1 -> inf

print("=" * 72)
print("§2.1 Z_eff(A^2) three realization classes  (Z0 = %.4f Ohm)" % Z_0)
print("=" * 72)
for a2 in (0.0, 0.117, 0.5, 0.9, 0.99):
    s = S_of_A2(np.array([a2]))[0]
    print(f"  A^2={a2:5.3f}  S={s:6.4f} | SYM={Z_0:8.2f}  "
          f"mu-only={Z_0*np.sqrt(s):8.2f}  eps-only={Z_0/np.sqrt(s):10.2f}  Ohm")

csv1 = os.path.join(FIGDIR, "zeff_realization_classes.csv")
with open(csv1, "w", newline="") as fh:
    w = csv.writer(fh)
    w.writerow(["A2", "S", "Z_SYM_ohm", "Z_mu_only_ohm", "Z_eps_only_ohm"])
    for i in range(len(A2)):
        w.writerow([f"{A2[i]:.5f}", f"{S[i]:.6f}", f"{Z_sym[i]:.4f}",
                    f"{Z_mu[i]:.4f}", f"{Z_eps[i]:.4f}"])
print(f"  wrote {csv1}")

# ----------------------------------------------------------------------
# §2.2 Approach profile Z_eff(r) toward a Gamma=-1 saturated boundary
# ----------------------------------------------------------------------
# canonical Schwarzschild tracking -> S(A(r)) = 1 - rs/r  (derived-this-arc)
# alternative op14-cosmic-horizon stale-1/2 -> S = sqrt(1 - rs/r) (flagged)
x = np.linspace(1.001, 10.0, 600)          # x = r/rs
S_track = 1.0 - 1.0 / x                     # primary (c_shear == Schwarzschild)
S_alt = np.sqrt(1.0 - 1.0 / x)             # alternative convention (flagged)

Zr_sym = np.full_like(x, Z_0)
Zr_mu = Z_0 * np.sqrt(S_track)
Zr_eps = Z_0 / np.sqrt(S_track)

csv2 = os.path.join(FIGDIR, "zeff_approach_profile.csv")
with open(csv2, "w", newline="") as fh:
    w = csv.writer(fh)
    w.writerow(["r_over_rs", "S_track(1-rs/r)", "S_alt(sqrt)",
                "Z_SYM", "Z_mu_only", "Z_eps_only"])
    for i in range(len(x)):
        w.writerow([f"{x[i]:.4f}", f"{S_track[i]:.6f}", f"{S_alt[i]:.6f}",
                    f"{Zr_sym[i]:.3f}", f"{Zr_mu[i]:.3f}", f"{Zr_eps[i]:.3f}"])
print(f"  wrote {csv2}")
print("\n§2.2 approach profile: S(A(r))=1-rs/r (derived); Z_eps diverges, Z_mu->0 at r->rs.")
print("     FLAG: op14-cosmic-horizon-profile.md:22 uses the stale 1/2 exponent")
print("     (S=sqrt(1-rs/r)); same 1/4-vs-1/2 tension temporal-values §4 flags. Both stored.")

# ----------------------------------------------------------------------
# §2.3 Reflectivity vs frequency — THE ECHO PREDICTOR (standard WKB integral)
# ----------------------------------------------------------------------
# Born/WKB graded-line reflection amplitude over the approach profile:
#   R(Omega) = INT 1/2 d(lnZ)/dx * exp( 2i INT_x^Xfar k dx' ) dx
# dimensionless Omega = omega*rs/c0 ; phase via local shear speed v(x)=c_shear/c0.
def reflectivity(Zr, x, Omega_grid, v):
    lnZ = np.log(Zr)
    dlnZ = np.gradient(lnZ, x)
    # cumulative optical path from the wall outward (so echoes phase-accumulate)
    phase_path = np.concatenate([[0.0], np.cumsum(0.5 * (1.0 / v[1:] + 1.0 / v[:-1])
                                                  * np.diff(x))])
    R = np.empty_like(Omega_grid, dtype=complex)
    for i, Om in enumerate(Omega_grid):
        integrand = 0.5 * dlnZ * np.exp(2j * Om * phase_path)
        R[i] = _trapz(integrand, x)
    return np.abs(R)


# Restrict the Born/WKB integral to the GRADED APPROACH REGION x>=x_grad: the
# first-order (weak-reflection) integral is self-consistent only where |R|<1.
# AT the wall (x->1) the canonical Gamma=-1 perfect reflector takes over (R=1,
# Op17-bounded; substrate-native-check CP10 — a boundary, not a bulk term).
x_grad = 1.10                               # graded region starts at r = 1.1 rs
m = x >= x_grad
xg = x[m]
v_shear = S_track[m] ** 0.5                 # c_shear/c0 = (1-A^2)^(1/4) = sqrt(S)
Omega = np.logspace(-2, 1.3, 240)           # rs/c0-normalized frequency

R_sym = reflectivity(Zr_sym[m], xg, Omega, v_shear)  # identically ~0 (dlnZ=0)
R_mu = reflectivity(Zr_mu[m], xg, Omega, v_shear)
R_eps = reflectivity(Zr_eps[m], xg, Omega, v_shear)
# Op17-bounded power reflectivity for the datasheet (R_pow <= 1 by construction)
Rpow_mu = np.minimum(R_mu**2, 1.0)
Rpow_eps = np.minimum(R_eps**2, 1.0)

csv3 = os.path.join(FIGDIR, "echo_reflectivity.csv")
with open(csv3, "w", newline="") as fh:
    w = csv.writer(fh)
    w.writerow(["Omega_rs_over_c0", "R_SYM", "R_mu_only", "R_eps_only",
                "Rpow_mu_bounded", "Rpow_eps_bounded"])
    for i in range(len(Omega)):
        w.writerow([f"{Omega[i]:.5e}", f"{R_sym[i]:.6e}", f"{R_mu[i]:.6e}",
                    f"{R_eps[i]:.6e}", f"{Rpow_mu[i]:.6e}", f"{Rpow_eps[i]:.6e}"])
print(f"  wrote {csv3}")
print("\n§2.3 ECHO PREDICTOR (graded-region |R|, r>=1.1 rs; wall is Gamma=-1, R=1):")
print(f"     SYM   max|R| = {R_sym.max():.3e}  (~0 by dlnZ=0 -> NO ECHO, canonical)")
print(f"     mu    max|R| = {R_mu.max():.3e}  -> max R_pow = {Rpow_mu.max():.3f}  (ECHO)")
print(f"     eps   max|R| = {R_eps.max():.3e}  -> max R_pow = {Rpow_eps.max():.3f}  (ECHO)")
print("     Low-Omega weighted (graded transition transmits high-freq, reflects low-freq).")

# live-fire dead-input/consistency: SYM reflectivity must be ~machine-zero
assert R_sym.max() < 1e-9 * max(R_mu.max(), R_eps.max(), 1e-30) + 1e-12, \
    "SYM reflectivity not vanishing -- canonical zero-echo result violated"

# ----------------------------------------------------------------------
# figures
# ----------------------------------------------------------------------
fig, axes = plt.subplots(1, 3, figsize=(16.5, 5))

ax = axes[0]
ax.plot(A2, Z_sym / Z_0, color="#4c72b0", lw=2.3, label="SYM (both sectors): invariant")
ax.plot(A2, Z_mu / Z_0, color="#55a868", lw=2.3, label=r"$\mu$-only (Meissner): $\to 0$")
ax.plot(A2, Z_eps / Z_0, color="#c44e52", lw=2.3, label=r"$\varepsilon$-only (mirror): $\to\infty$")
ax.axhline(1.0, color="gray", ls=":", lw=1)
ax.set_xlabel(r"operating-point $A^2$")
ax.set_ylabel(r"$Z_{eff}/Z_0$")
ax.set_title(r"§2.1 $Z_{eff}(A^2)=Z_0\sqrt{S_\mu/S_\varepsilon}$ — three classes")
ax.set_ylim(0, 5)
ax.legend(fontsize=8)
ax.grid(alpha=0.3)

ax = axes[1]
ax.plot(x, Zr_eps / Z_0, color="#c44e52", lw=2.3, label=r"$\varepsilon$-only $\to\infty$")
ax.plot(x, Zr_sym / Z_0, color="#4c72b0", lw=2.3, label="SYM (flat = no echo)")
ax.plot(x, Zr_mu / Z_0, color="#55a868", lw=2.3, label=r"$\mu$-only $\to 0$")
ax.axvline(1.0, color="black", ls="--", alpha=0.6, label=r"$\Gamma=-1$ wall $r=r_s$")
ax.set_xlabel(r"$r/r_s$ (approach to saturated boundary)")
ax.set_ylabel(r"$Z_{eff}/Z_0$")
ax.set_title(r"§2.2 approach profile $S(A(r))=1-r_s/r$ (derived-this-arc)")
ax.set_yscale("log")
ax.set_xlim(1, 6)
ax.legend(fontsize=8)
ax.grid(alpha=0.3, which="both")

ax = axes[2]
ax.loglog(Omega, R_eps, color="#c44e52", lw=2.3, label=r"$\varepsilon$-only echo")
ax.loglog(Omega, R_mu, color="#55a868", lw=2.3, label=r"$\mu$-only echo")
ax.loglog(Omega, np.maximum(R_sym, 1e-18), color="#4c72b0", lw=2.3,
          label="SYM (no echo, $\\sim$0)")
ax.set_xlabel(r"normalized frequency $\Omega=\omega r_s/c_0$")
ax.set_ylabel(r"reflectivity $|R(\Omega)|$")
ax.set_title("§2.3 ECHO PREDICTOR — graded-line WKB reflection")
ax.set_ylim(1e-6, 2)
ax.legend(fontsize=8)
ax.grid(alpha=0.3, which="both")

fig.suptitle(
    "Dark-sector response §2 — Z_eff (transmission-line characterization)  "
    "[SYM invariant=reflectionless; asymmetry=echo]  derived from constants.py",
    fontsize=11,
)
fig.tight_layout(rect=(0, 0, 1, 0.96))
out = os.path.join(FIGDIR, "fig2_zeff_echo_predictor.png")
fig.savefig(out, dpi=140)
print(f"\n  wrote {out}")
print("DONE §2.")
