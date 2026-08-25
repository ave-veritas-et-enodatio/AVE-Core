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
    "A_MATCHED_B",
    "saturation_kernel",
    "gamma_of_z",
    "gamma_of_A",
    "gamma_two_junction_uniform",
    "two_junction_gamma",
    "base_chart",
    "plot_bias_trajectory",
    "plot_frequency_locus",
    "plot_occupancy",
]

# Form-B matched crossing: Gamma_B(A) = 0 where sqrt(S(A)) = 1/2, i.e.
# S = 1/4, A = sqrt(1 - 1/16) = sqrt(15)/4 ~ 0.96825.
A_MATCHED_B: float = float(np.sqrt(15.0)) / 4.0

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


def gamma_of_A(A, form: str = "core"):
    """Bias locus Gamma(A) on the chart, in one of three forms.

    ``form="core"`` — the CANONICAL locus (cvr-reflection-smith.md Sec.2):

        Gamma(A_0) = (Z_core - Z_0)/(Z_core + Z_0),  Z_core(A_0) = Z_0*sqrt(S(A_0))

    Endpoints: A_0=0 -> Gamma=0 (matched, the free photon); A_0->1 -> Gamma->-1
    (the short-circuit TIR wall). A straight real-axis run, centre to left rim.

    ``form="J"`` and ``form="B"`` — the two GRADED two-junction constructions.
    Both start from the bare z=3 vertex: a wave down one bond sees the other
    two in parallel (z_load = 1/2), Gamma = (2-z)/z = -1/3 — a COUNTING fact
    (translation-circuit.md:189). SCOPING per the same line's T4 fork close:
    per-vertex / incoherent; in-band collective carriers homogenize the bare
    reflection (~0.12 of incoherent), so these loci describe the isolated
    junction, not an in-band collective carrier.

    **UNDERIVED-SIDE-ASSIGNMENT tag (both graded forms):** which side of the
    junction the bias lands on is an engineering CHOICE of the construction,
    not a derived substrate fact. The two choices are drawn as separate forms
    precisely so the choice stays visible:

    * ``"J"`` — bias on the JUNCTION side (the two far bonds carry sqrt(S);
      the feed bond stays cold): Gamma_J = (sqrt(S)/2 - 1)/(sqrt(S)/2 + 1).
      Endpoints -1/3 (A=0, the bare vertex) -> -1 (A->1, all far arms short).
    * ``"B"`` — bias on the BOND side (the feed bond carries sqrt(S); the far
      pair stays cold; normalization by the biased bond's own impedance):
      Gamma_B = (1/2 - sqrt(S))/(1/2 + sqrt(S)).
      Endpoints -1/3 (A=0) -> +1 (A->1), with the MATCHED CROSSING Gamma=0 at
      sqrt(S) = 1/2, i.e. A = sqrt(15)/4 (``A_MATCHED_B``).

    A UNIFORM bias (same sqrt(S) both sides) cancels exactly and pins -1/3 at
    all A — see ``gamma_two_junction_uniform`` (the invariance statement in the
    module docstring). Only the differential forms above split the vertex.
    """
    A = np.asarray(A, dtype=float)
    rootS = np.sqrt(saturation_kernel(A))
    if form == "core":
        return (rootS - 1.0) / (rootS + 1.0)
    if form == "J":
        return (rootS / 2.0 - 1.0) / (rootS / 2.0 + 1.0)
    if form == "B":
        return (0.5 - rootS) / (0.5 + rootS)
    raise ValueError(f"unknown form {form!r}; expected 'core', 'J', or 'B'")


def gamma_two_junction_uniform(A):
    """Vertex reflection under a UNIFORM bias — computed, not asserted.

    Both the feed bond and the two far bonds carry the SAME sqrt(S(A)), so the
    normalized load is z = (sqrt(S)/2)/sqrt(S) = 1/2 and

        Gamma = (z - 1)/(z + 1) = -1/3   exactly, at every A with S > 0.

    This function computes the ratio numerically (no algebraic shortcut) so the
    invariance is a TESTED property of the bilinear map, not a baked-in
    constant: the chart is blind to uniform medium changes (adversarially
    verified this lane, 2026-08-24; the self-cancellation principle as
    geometry). At A=1 exactly, S=0 and the ratio is 0/0 — the uniform-bias
    statement is scoped to S > 0 (the medium still exists).
    """
    A = np.asarray(A, dtype=float)
    rootS = np.sqrt(saturation_kernel(A))
    z_load = (rootS / 2.0)  # two biased far bonds in parallel: Z0*sqrt(S)/2
    z_feed = rootS          # biased feed bond: Z0*sqrt(S)
    return (z_load - z_feed) / (z_load + z_feed)


def two_junction_gamma(theta, *, A_line=0.0, A_ends=0.0):
    """Input reflection of the bond-between-two-z3-junctions composite.

    Minimal transfer-matrix (ABCD) model of one lattice bond spanning two z=3
    vertices, fed from a cold semi-infinite Z_0 bond:

        feed (Z_0) --[near junction: shunt Z_0/2]--[Z_0 line, length theta]--
                    --[far junction: load Z_0/2]

    The near vertex's other two bonds appear as a shunt of Z_0/2; the far
    vertex's other two bonds terminate the line in Z_0/2 (the parallel-pair
    counting fact, translation-circuit.md:189). ``theta`` is the bond's
    electrical length (radians); the cold Gamma(theta) locus is the composite's
    frequency response, since theta = omega * ell / c_bond.

    Optional bias: ``A_line`` scales the bond's characteristic impedance by
    sqrt(S(A_line)); ``A_ends`` scales both junction terminations by
    sqrt(S(A_ends)). Setting them EQUAL is a uniform bias of the composite
    relative to the cold feed (still a differential boundary at the feed
    plane); the fully uniform case (feed included) is the exact -1/3-at-DC
    invariance of ``gamma_two_junction_uniform``.

    SCOPING: an isolated / incoherent composite (per-vertex reading). In-band
    collective carriers homogenize the bare vertex reflection (~0.12 of the
    incoherent value, T4 fork close, translation-circuit.md:189) — this
    composite is the instrument's minimal frequency axis, not a claim about
    in-band collective transport.

    Returns complex Gamma (same shape as ``theta``).
    """
    theta = np.asarray(theta, dtype=float)
    sL = float(np.sqrt(saturation_kernel(A_line)))   # line impedance scale
    sE = float(np.sqrt(saturation_kernel(A_ends)))   # junction-arm scale
    z_line = sL          # Z0*sqrt(S_line), normalized by Z0
    z_end = 0.5 * sE     # two arms in parallel: (Z0/2)*sqrt(S_ends)

    t = np.tan(theta)
    # far load transformed back through the line — the standard IMPEDANCE
    # tan-form; theta=pi/2 is handled by floating-point tan overflow (verified
    # against an ABCD chain to <=3.4e-16 incl. the quarter-wave point). Only
    # the parallel combination below is done in admittances.
    with np.errstate(divide="ignore", invalid="ignore"):
        z_a = z_line * (z_end + 1j * z_line * t) / (z_line + 1j * z_end * t)
        # near junction: shunt z_end in parallel with the transformed branch
        y_in = 1.0 / z_end + 1.0 / z_a
        z_in = 1.0 / y_in
        g = (z_in - 1.0) / (z_in + 1.0)
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
        ax.fill(ring_x, ring_y, color=style.COLORS["accent"], alpha=0.55,
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


# ---------------------------------------------------------------------------
# Plot helpers — trajectories, frequency loci, occupancy
# ---------------------------------------------------------------------------
def plot_bias_trajectory(ax, A, form: str = "core", *, im_offset: float = 0.0,
                         endpoint_markers: bool = True, **plot_kw):
    """Draw a Gamma(A) bias trajectory on a chart axes.

    All three forms are real-axis loci; when several are drawn on one chart
    they overlap. ``im_offset`` shifts the drawn trace vertically for
    VISIBILITY ONLY — a caller using it must annotate the offset on the figure
    (honest-axes discipline; the driver does this).

    Returns the Line2D. Endpoint markers: circle at the A=0 end, arrowhead-like
    marker at the A=max end.
    """
    A = np.asarray(A, dtype=float)
    g = np.asarray(gamma_of_A(A, form), dtype=complex)
    (line,) = ax.plot(g.real, g.imag + im_offset, **plot_kw)
    if endpoint_markers:
        col = line.get_color()
        ax.plot([g.real[0]], [g.imag[0] + im_offset], "o", color=col, ms=5, zorder=3)
        ax.plot([g.real[-1]], [g.imag[-1] + im_offset], ">", color=col, ms=5, zorder=3)
    return line


def plot_frequency_locus(ax, theta, *, A_line=0.0, A_ends=0.0, **plot_kw):
    """Draw the two-junction composite's Gamma(theta) locus on a chart axes.

    ``theta`` is the bond electrical length (the frequency axis,
    theta = omega*ell/c_bond); bias per ``two_junction_gamma``. Returns the
    Line2D.
    """
    g = two_junction_gamma(theta, A_line=A_line, A_ends=A_ends)
    (line,) = ax.plot(g.real, g.imag, **plot_kw)
    return line


def plot_occupancy(ax_chart, A_t, form: str = "core", *, ax_hist=None,
                   bins: int = 60, scatter_kw=None, hist_kw=None):
    """Occupancy view: an envelope orbit A(t) -> chart trace + dwell density.

    ``A_t`` is the caller-supplied amplitude time series. THE ORBIT A(t) IS THE
    CALLER'S CHOICE — the instrument maps and histograms whatever it is given;
    the driver's demo orbit is explicitly tagged UNDERIVED-CHOICE.

    * On ``ax_chart``: the Gamma(A(t)) trace as a dwell-coloured 2D histogram
      (hexbin) over (Re Gamma, Im Gamma) — for the real-axis forms this is a
      1-pixel-tall strip, which is the honest picture (the locus IS the real
      axis).
    * On ``ax_hist`` (optional): the 1D dwell-density histogram over
      Re(Gamma), normalized to unit area — where on the chart the orbit
      spends its time (turning points of A(t) dominate, as for any envelope).

    Returns ``(hexbin_artist, hist_artist_or_None)``.
    """
    A_t = np.asarray(A_t, dtype=float)
    g = np.asarray(gamma_of_A(A_t, form), dtype=complex)
    skw = dict(gridsize=bins, cmap=style.CMAP_SEQ, mincnt=1, zorder=2.5)
    skw.update(scatter_kw or {})
    hb = ax_chart.hexbin(g.real, g.imag, **skw)
    hist_art = None
    if ax_hist is not None:
        hkw = dict(bins=bins, density=True, color=style.COLORS["ave"], alpha=0.85)
        hkw.update(hist_kw or {})
        _, _, hist_art = ax_hist.hist(g.real, **hkw)
        ax_hist.set_xlabel(style.axis_label("Reflection (real)", r"\mathrm{Re}(\Gamma)", ""))
        ax_hist.set_ylabel(style.axis_label("Dwell density", r"p(\mathrm{Re}\,\Gamma)", "1"))
    return hb, hist_art
