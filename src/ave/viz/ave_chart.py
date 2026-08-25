"""AVE chart — the doubly-normalized Smith-chart INSTRUMENT for the vacuum circuit.

An engineering plotting instrument, not an ontology claim. It renders the
reflection-coefficient disk with the vacuum medium's own datasheet constants
baked into the normalization, so any substrate operating point / trajectory /
occupancy can be read the way an RF engineer reads a device on a Smith chart.

THE DOUBLE NORMALIZATION (both scales are the medium's own datasheet constants)
-------------------------------------------------------------------------------
1. **Impedance by Z_0** — every impedance on the chart is z = Z/Z_0, the
   vacuum's own characteristic impedance (``ave.core.constants.Z_0``). The
   chart centre IS the matched cold lattice.
2. **Amplitude by A_yield** — every bias / operating point is A = |V|/V_yield
   (``V_YIELD``), the Axiom-4 saturation scale, entering through the kernel
   S(A) = sqrt(1 - A^2) and the canonical trajectory Z_core(A) = Z_0*sqrt(S(A))
   (cvr-reflection-smith.md Sec.2).

UNIFORM-BIAS INVARIANCE (the self-cancellation principle as geometry)
---------------------------------------------------------------------
Under a UNIFORM bias every impedance in a junction network rescales by the SAME
sqrt(S), and the bilinear map Gamma = (z2 - z1)/(z2 + z1) is invariant under
common rescaling of both arms — so the bare z=3 vertex reflection
Gamma = (2-z)/z = -1/3 is EXACT at all orders of a uniform bias, and only a
DIFFERENTIAL bias splits it (adversarially verified this lane, 2026-08-24).
Normalized-chart statement: **the chart is blind to uniform medium changes** —
phase-only epistemology drawn as geometry. See ``gamma_two_junction_uniform``
and the ``test_ave_chart.py`` uniform-rescale invariance test.

PARK COMPLIANCE (binding)
-------------------------
The CP^1 / one-chart-per-sector ONTOLOGY canonization is Grant-PARKED
(``_orchestration/open-items/2026-08-18-smith-chart-cp1-canonization.md``).
This module is the INSTRUMENT — engineering plotting machinery only; it mints
no ontology claim (no CP^1 identification, no per-sector chart doctrine).
Whether this build trips the park's re-open condition ("an engine lane actually
wants the chart as a live instrument") is GRANT'S ruling, not this lane's.

TIER NOTE: ``ave.viz.style`` keeps its presentation-tier no-``ave.core``
invariant. THIS module is instrument-tier — it draws physics-anchored
annotations (the 1-alpha rim band), so it imports canonical constants from
``ave.core.constants`` (ALPHA). It never re-derives them.

CANONICAL ANCHORS (verify-before-cite; grep in manuscript/ave-kb):
  - Gamma(A_0) = (Z_core - Z_0)/(Z_core + Z_0), Z_core = Z_0*sqrt(S(A_0))
      cvr-reflection-smith.md Sec.2 (Op3 of the canonical trajectory)
  - |Gamma|^2 = 1 - alpha (AVE-DISTINCT rim band; owned by alpha=1/Q,
      clm-rtdmsn)                    cvr-reflection-smith.md Sec.3
  - z=3 vertex Gamma = (2-z)/z = -1/3, a COUNTING fact
      translation-circuit.md:189 (scoped per-vertex/incoherent; in-band
      collective carriers homogenize, ~0.12 of incoherent — T4 fork close)
  - Sector discipline at the rim poles: PR#260 B3-DEGENERATE (see
      ``base_chart`` docstring).
"""

from __future__ import annotations

import numpy as np

from ave.core.constants import ALPHA
from ave.viz import style

__all__ = [
    "GAMMA_WALL",
    "GAMMA_WALL_SQ",
    "saturation_kernel",
    "gamma_of_z",
    "base_chart",
]

# ---------------------------------------------------------------------------
# The AVE-distinct rim band (cvr-reflection-smith.md Sec.3, clm-rtdmsn)
# ---------------------------------------------------------------------------
# |Gamma|^2 = 1 - alpha ~ 0.99270; |Gamma| = sqrt(1-alpha) ~ 0.99635.
# The electron wall sits a hair INSIDE the rim: the gap to |Gamma|=1 IS alpha,
# the per-cycle radiative leak (alpha = 1/Q). Classification: the matched->short
# locus is CONSISTENCY; this 1-alpha relation is the AVE-DISTINCT corollary.
GAMMA_WALL_SQ: float = 1.0 - ALPHA  # |Gamma|^2 at the electron wall
GAMMA_WALL: float = float(np.sqrt(GAMMA_WALL_SQ))  # |Gamma| ~ 0.99635


def saturation_kernel(A):
    """S(A) = sqrt(1 - A^2), the Axiom-4 kernel, UNCLIPPED.

    Unlike ``cvr_model.saturation_kernel`` (which carries the graft-v2
    apparatus clip S_MIN/A_CAP for engine figures), the chart instrument keeps
    the exact kernel so the analytic endpoints (Gamma(1) = -1 etc.) are exact.
    Domain A in [0, 1]; values outside are clipped to the physical domain.
    """
    A = np.asarray(A, dtype=float)
    return np.sqrt(np.clip(1.0 - A**2, 0.0, 1.0))


def gamma_of_z(z):
    """The bilinear map Gamma = (z - 1)/(z + 1) for NORMALIZED impedance z = Z/Z_0.

    Op3 (operators.md:43) with the reference arm fixed at the chart's own
    normalization Z_0. z=1 -> 0 (matched); z=0 -> -1 (short); z=inf -> +1
    (open); z and 1/z map to +/- the same |Gamma| (the Mobius Z<->1/Z gauge).
    """
    z = np.asarray(z, dtype=complex)
    with np.errstate(divide="ignore", invalid="ignore"):
        g = np.where(np.isinf(z), 1.0 + 0j, (z - 1.0) / (z + 1.0))
    return g


def base_chart(ax=None, *, rim_band: bool = True, annotate: bool = True):
    """Draw the base AVE chart: unit disk + Smith grid + the 1-alpha rim band.

    Returns ``(fig, ax)``. Elements:

    * Unit circle + standard constant-r circles (r = 0.5, 1, 2) and constant-x
      arcs (x = +/-0.5, +/-1, +/-2) — the grid convention reused from the
      View-3 driver (``cvr_ee_sweep.py::_draw_smith``).
    * Centre annotated as the matched cold-lattice reference (z = 1, Z = Z_0,
      Gamma = 0 — the free photon, cvr-reflection-smith.md Sec.2).
    * The AVE-DISTINCT rim band shaded between |Gamma| = sqrt(1-alpha) and 1
      (cvr-reflection-smith.md Sec.3; ALPHA from ``ave.core.constants``).

    SECTOR DISCIPLINE at the rim poles (PR#260 B3-DEGENERATE, Grant-ratified;
    quoted in cvr-reflection-smith.md Sec.2 Rule-12 note): the mu-first vs
    eps-first routes to the rim are the chirality/spin SIGN-SELECTOR
    (mu-first => Gamma=-1, eps-first => Gamma=+1 are spin-conjugate), MUTE on
    the mass sector; the mass-cage is the A1 longitudinal bulk short
    (Z_bulk -> 0 => Gamma_bulk = -1). The fork is DEGENERATE on equilibrium
    observables (Z = Z_0*sqrt(S), |Gamma| = 1 both ways). The annotations below
    follow that discipline — the Gamma = -1 pole is NEVER labelled "the
    magnetic wall", and confinement is never cross-wired into the charge
    sector.
    """
    import matplotlib.pyplot as plt

    if ax is None:
        fig, ax = plt.subplots(figsize=style.figsize("square"))
    else:
        fig = ax.figure

    th = np.linspace(0, 2 * np.pi, 720)
    # unit circle
    ax.plot(np.cos(th), np.sin(th), "-", color=style.COLORS["data"], lw=1)
    # constant-resistance circles (grid convention per cvr_ee_sweep._draw_smith)
    for r in (0.5, 1.0, 2.0):
        c, rad = r / (1 + r), 1 / (1 + r)
        ax.plot(c + rad * np.cos(th), rad * np.sin(th),
                color=style.COLORS["muted"], lw=0.5, alpha=0.6)
    # constant-reactance arcs
    for x in (0.5, 1.0, 2.0, -0.5, -1.0, -2.0):
        rad = 1 / abs(x)
        xc, yc = 1 + rad * np.cos(th), (1 / x) + rad * np.sin(th)
        m = xc**2 + yc**2 <= 1.001
        ax.plot(xc[m], yc[m], color=style.COLORS["muted"], lw=0.5, alpha=0.6)
    ax.axhline(0, color=style.COLORS["muted"], lw=0.5, alpha=0.6)

    if rim_band:
        # annulus between |Gamma| = sqrt(1-alpha) and 1 — thin (~0.4% of the
        # radius) but real: the hair by which the electron wall misses the rim
        # IS alpha (cvr-reflection-smith.md Sec.3).
        ring_x = np.concatenate([np.cos(th), GAMMA_WALL * np.cos(th[::-1])])
        ring_y = np.concatenate([np.sin(th), GAMMA_WALL * np.sin(th[::-1])])
        ax.fill(ring_x, ring_y, color=style.COLORS["comparison"], alpha=0.55,
                lw=0, zorder=1.5,
                label=(r"$1-\alpha$ rim band: $|\Gamma|=\sqrt{1-\alpha}"
                       r"\approx" + f"{GAMMA_WALL:.5f}" + r"\,\to\,1$"))

    if annotate:
        ax.plot([0], [0], "o", color=style.COLORS["accent"], ms=6, zorder=3)
        ax.annotate("$\\Gamma=0$: matched cold lattice\n($Z=Z_0$, the free photon)",
                    xy=(0, 0), xytext=(0.08, -0.30), fontsize=7,
                    color=style.COLORS["accent"],
                    arrowprops=dict(arrowstyle="->", color=style.COLORS["accent"], lw=0.8))
        # Gamma=-1 pole: A1 longitudinal bulk short (mass-cage); mu-vs-eps is
        # a sign/spin selector only (PR#260 B3-DEGENERATE) — NOT "magnetic wall".
        ax.annotate("$\\Gamma=-1$: short\n(A1 longitudinal bulk short,\n"
                    "$Z_{bulk}\\to0$ — the mass-cage;\n"
                    "$\\mu$-first route = spin-sign selector only)",
                    xy=(-1, 0), xytext=(-0.97, 0.55), fontsize=6.5,
                    color=style.COLORS["data"],
                    arrowprops=dict(arrowstyle="->", color=style.COLORS["data"], lw=0.8))
        ax.annotate("$\\Gamma=+1$: open\n($\\varepsilon$-first route =\n"
                    "spin-conjugate sign;\ndegenerate fork, PR#260)",
                    xy=(1, 0), xytext=(0.42, -0.62), fontsize=6.5,
                    color=style.COLORS["data"],
                    arrowprops=dict(arrowstyle="->", color=style.COLORS["data"], lw=0.8))

    ax.set_aspect("equal")
    ax.set_xlim(-1.18, 1.18)
    ax.set_ylim(-1.18, 1.18)
    ax.set_xlabel(style.axis_label("Reflection (real)", r"\mathrm{Re}(\Gamma)", ""))
    ax.set_ylabel(style.axis_label("Reflection (imag)", r"\mathrm{Im}(\Gamma)", ""))
    return fig, ax
