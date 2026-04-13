import pathlib
#!/usr/bin/env python3
"""
AVE ORBITAL TOPOLOGY FIGURE GENERATOR
======================================
Generates orbital knot topology diagrams for all elements in the periodic table.
Each figure shows:
  - Harmonic shell tracks (n=1, n=2, n=3, ...)
  - Soliton positions with angular spacing
  - Bidirectional force arrows (outward repulsion, inward confinement)
  - Nuclear core and electron configuration labels

All output goes to periodic_table/figures/<element>_topology.png
"""
import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# Import physics engine — NO ad-hoc values
# ---------------------------------------------------------------------------
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..')))
from ave.core.constants import ALPHA, L_NODE

OUTDIR = f"{str(pathlib.Path(__file__).parent.parent.parent.parent.absolute())}/periodic_table/figures"


# ============================================================================
# ELEMENT DEFINITIONS
# ============================================================================
# Each element defines:
#   symbol, Z, A, title, max_n,
#   shells: list of (n_track_radius, shell_label, n_resonators, color)
#   Notes describe the nuclear topology for the subtitle
# ============================================================================

ELEMENTS = [
    {
        'name': 'hydrogen_1', 'symbol': 'H', 'Z': 1, 'A': 1,
        'title': 'Hydrogen-1: Single Trefoil Knot',
        'subtitle': 'One soliton on $n = 1$; no equilibrium partner',
        'shells': [
            {'r': 0.7, 'label': '$n=1$', 'electrons': 1, 'color': '#ff7755', 'angle_offset': 0},
        ],
        'core_electrons': [],
    },
    {
        'name': 'helium_4', 'symbol': 'He', 'Z': 2, 'A': 4,
        'title': 'Helium-4: Paired Trefoil Lock',
        'subtitle': 'Two solitons at $180°$ on $n = 1$; complete closure',
        'shells': [
            {'r': 0.7, 'label': '$n=1$', 'electrons': 2, 'color': '#4488ff', 'angle_offset': 0},
        ],
        'core_electrons': [],
    },
    {
        'name': 'lithium_7', 'symbol': 'Li', 'Z': 3, 'A': 7,
        'title': 'Lithium-7: Core + Valence Soliton',
        'subtitle': '$1s^2$ closure + one outer soliton on $n = 2$',
        'shells': [
            {'r': 0.7, 'label': '$n=1$', 'electrons': 2, 'color': '#4488ff', 'angle_offset': 0},
            {'r': 1.1, 'label': '$n=2$', 'electrons': 1, 'color': '#ff7755', 'angle_offset': 0},
        ],
        'core_electrons': [],
    },
    {
        'name': 'beryllium_9', 'symbol': 'Be', 'Z': 4, 'A': 9,
        'title': 'Beryllium-9: Paired Valence Bridge',
        'subtitle': '$1s^2$ closure + two valence solitons at $180°$ on $n = 2$',
        'shells': [
            {'r': 0.7, 'label': '$n=1$', 'electrons': 2, 'color': '#4488ff', 'angle_offset': 0},
            {'r': 1.1, 'label': '$n=2$', 'electrons': 2, 'color': '#ff7755', 'angle_offset': np.pi/4},
        ],
        'core_electrons': [],
    },
    {
        'name': 'boron_11', 'symbol': 'B', 'Z': 5, 'A': 11,
        'title': 'Boron-11: Topological Horizon',
        'subtitle': '$1s^2$ + three trefoil solitons at $120°$ on $n = 2$',
        'shells': [
            {'r': 0.7, 'label': '$n=1$', 'electrons': 2, 'color': '#4488ff', 'angle_offset': 0},
            {'r': 1.1, 'label': '$n=2$', 'electrons': 3, 'color': '#ff7755', 'angle_offset': 0},
        ],
        'core_electrons': [],
    },
    {
        'name': 'carbon_12', 'symbol': 'C', 'Z': 6, 'A': 12,
        'title': 'Carbon-12: Tetrahedral Projection',
        'subtitle': '$1s^2$ + four solitons at $90°$ on $n = 2$ ($sp^3$)',
        'shells': [
            {'r': 0.7, 'label': '$n=1$', 'electrons': 2, 'color': '#4488ff', 'angle_offset': 0},
            {'r': 1.1, 'label': '$n=2$', 'electrons': 4, 'color': '#ff7755', 'angle_offset': np.pi/4},
        ],
        'core_electrons': [],
    },
    {
        'name': 'nitrogen_14', 'symbol': 'N', 'Z': 7, 'A': 14,
        'title': 'Nitrogen-14: Asymmetric Strain',
        'subtitle': '$1s^2$ + five crowded solitons at $72°$ on $n = 2$',
        'shells': [
            {'r': 0.7, 'label': '$n=1$', 'electrons': 2, 'color': '#4488ff', 'angle_offset': 0},
            {'r': 1.1, 'label': '$n=2$', 'electrons': 5, 'color': '#ff7755', 'angle_offset': 0},
        ],
        'core_electrons': [],
    },
    {
        'name': 'oxygen_16', 'symbol': 'O', 'Z': 8, 'A': 16,
        'title': 'Oxygen-16: Near-Complete Shell',
        'subtitle': '$1s^2$ + six solitons at $60°$ on $n = 2$',
        'shells': [
            {'r': 0.7, 'label': '$n=1$', 'electrons': 2, 'color': '#4488ff', 'angle_offset': 0},
            {'r': 1.1, 'label': '$n=2$', 'electrons': 6, 'color': '#ff7755', 'angle_offset': 0},
        ],
        'core_electrons': [],
    },
    {
        'name': 'fluorine_19', 'symbol': 'F', 'Z': 9, 'A': 19,
        'title': 'Fluorine-19: Halogen Strain Dipole',
        'subtitle': '$1s^2$ + seven solitons on $n = 2$; one vacancy drives reactivity',
        'shells': [
            {'r': 0.7, 'label': '$n=1$', 'electrons': 2, 'color': '#4488ff', 'angle_offset': 0},
            {'r': 1.1, 'label': '$n=2$', 'electrons': 7, 'color': '#ff7755', 'angle_offset': 0},
        ],
        'core_electrons': [],
    },
    {
        'name': 'neon_20', 'symbol': 'Ne', 'Z': 10, 'A': 20,
        'title': 'Neon-20: Complete $n=2$ Closure',
        'subtitle': '$1s^2 \\, 2s^2 \\, 2p^6$ — eight solitons at $45°$, noble gas',
        'shells': [
            {'r': 0.7, 'label': '$n=1$', 'electrons': 2, 'color': '#4488ff', 'angle_offset': 0},
            {'r': 1.1, 'label': '$n=2$', 'electrons': 8, 'color': '#44cc88', 'angle_offset': 0},
        ],
        'core_electrons': [],
    },
    {
        'name': 'sodium_23', 'symbol': 'Na', 'Z': 11, 'A': 23,
        'title': 'Sodium-23: Alkali Valence Soliton',
        'subtitle': '$[Ne]$ core + one valence soliton on $n = 3$',
        'shells': [
            {'r': 0.5, 'label': '$n=1$', 'electrons': 2, 'color': '#4488ff', 'angle_offset': 0},
            {'r': 0.85, 'label': '$n=2$', 'electrons': 8, 'color': '#44cc88', 'angle_offset': 0},
            {'r': 1.2, 'label': '$n=3$', 'electrons': 1, 'color': '#ff7755', 'angle_offset': 0},
        ],
        'core_electrons': [],
    },
    {
        'name': 'magnesium_24', 'symbol': 'Mg', 'Z': 12, 'A': 24,
        'title': 'Magnesium-24: Paired $3s$ Valence',
        'subtitle': '$[Ne]$ core + two valence solitons at $180°$ on $n = 3$',
        'shells': [
            {'r': 0.5, 'label': '$n=1$', 'electrons': 2, 'color': '#4488ff', 'angle_offset': 0},
            {'r': 0.85, 'label': '$n=2$', 'electrons': 8, 'color': '#44cc88', 'angle_offset': 0},
            {'r': 1.2, 'label': '$n=3$', 'electrons': 2, 'color': '#ff7755', 'angle_offset': np.pi/6},
        ],
        'core_electrons': [],
    },
    {
        'name': 'aluminum_27', 'symbol': 'Al', 'Z': 13, 'A': 27,
        'title': 'Aluminum-27: Trivalent Topology',
        'subtitle': '$[Ne]$ core + three valence solitons at $120°$ on $n = 3$',
        'shells': [
            {'r': 0.5, 'label': '$n=1$', 'electrons': 2, 'color': '#4488ff', 'angle_offset': 0},
            {'r': 0.85, 'label': '$n=2$', 'electrons': 8, 'color': '#44cc88', 'angle_offset': 0},
            {'r': 1.2, 'label': '$n=3$', 'electrons': 3, 'color': '#ff7755', 'angle_offset': 0},
        ],
        'core_electrons': [],
    },
    {
        'name': 'silicon_28', 'symbol': 'Si', 'Z': 14, 'A': 28,
        'title': 'Silicon-28: Semiconductor Boundary',
        'subtitle': '$[Ne]$ core + four valence solitons at $90°$ on $n = 3$ ($sp^3$)',
        'shells': [
            {'r': 0.5, 'label': '$n=1$', 'electrons': 2, 'color': '#4488ff', 'angle_offset': 0},
            {'r': 0.85, 'label': '$n=2$', 'electrons': 8, 'color': '#44cc88', 'angle_offset': 0},
            {'r': 1.2, 'label': '$n=3$', 'electrons': 4, 'color': '#ff7755', 'angle_offset': np.pi/4},
        ],
        'core_electrons': [],
    },
    # ------------------------------------------------------------------
    # HEAVY ELEMENTS (Period 3 closure + Period 4)
    # ------------------------------------------------------------------
    {
        'name': 'sulfur_32', 'symbol': 'S', 'Z': 16, 'A': 32,
        'title': 'Sulfur-32: Large Signal Avalanche',
        'subtitle': '$[Ne]$ core + six valence solitons at $60°$ on $n = 3$',
        'shells': [
            {'r': 0.5, 'label': '$n=1$', 'electrons': 2, 'color': '#4488ff', 'angle_offset': 0},
            {'r': 0.85, 'label': '$n=2$', 'electrons': 8, 'color': '#44cc88', 'angle_offset': 0},
            {'r': 1.2, 'label': '$n=3$', 'electrons': 6, 'color': '#ff7755', 'angle_offset': 0},
        ],
        'core_electrons': [],
    },
    {
        'name': 'argon_40', 'symbol': 'Ar', 'Z': 18, 'A': 40,
        'title': 'Argon-40: Complete $n=3$ Closure',
        'subtitle': '$1s^2 \\, 2s^2 \\, 2p^6 \\, 3s^2 \\, 3p^6$ — noble gas',
        'shells': [
            {'r': 0.5, 'label': '$n=1$', 'electrons': 2, 'color': '#4488ff', 'angle_offset': 0},
            {'r': 0.85, 'label': '$n=2$', 'electrons': 8, 'color': '#44cc88', 'angle_offset': 0},
            {'r': 1.2, 'label': '$n=3$', 'electrons': 8, 'color': '#44cc88', 'angle_offset': np.pi/8},
        ],
        'core_electrons': [],
    },
    {
        'name': 'calcium_40', 'symbol': 'Ca', 'Z': 20, 'A': 40,
        'title': 'Calcium-40: Large Signal Alkaline Earth',
        'subtitle': '$[Ar]$ core + two valence solitons at $180°$ on $n = 4$',
        'shells': [
            {'r': 0.35, 'label': '$n=1$', 'electrons': 2, 'color': '#4488ff', 'angle_offset': 0},
            {'r': 0.6,  'label': '$n=2$', 'electrons': 8, 'color': '#44cc88', 'angle_offset': 0},
            {'r': 0.9,  'label': '$n=3$', 'electrons': 8, 'color': '#44cc88', 'angle_offset': np.pi/8},
            {'r': 1.25, 'label': '$n=4$', 'electrons': 2, 'color': '#ff7755', 'angle_offset': np.pi/6},
        ],
        'core_electrons': [],
    },
    {
        'name': 'titanium_48', 'symbol': 'Ti', 'Z': 22, 'A': 48,
        'title': 'Titanium-48: Cuboctahedral Packing',
        'subtitle': '$[Ar]\\, 3d^2 \\, 4s^2$ — first d-block solitons',
        'shells': [
            {'r': 0.35, 'label': '$n=1$', 'electrons': 2, 'color': '#4488ff', 'angle_offset': 0},
            {'r': 0.6,  'label': '$n=2$', 'electrons': 8, 'color': '#44cc88', 'angle_offset': 0},
            {'r': 0.9,  'label': '$n=3$', 'electrons': 8, 'color': '#44cc88', 'angle_offset': np.pi/8},
            {'r': 1.05, 'label': '$3d$',  'electrons': 2, 'color': '#cc88ff', 'angle_offset': np.pi/4},
            {'r': 1.25, 'label': '$n=4$', 'electrons': 2, 'color': '#ff7755', 'angle_offset': 0},
        ],
        'core_electrons': [],
    },
    {
        'name': 'chromium_52', 'symbol': 'Cr', 'Z': 24, 'A': 52,
        'title': 'Chromium-52: Anomalous Half-Fill',
        'subtitle': '$[Ar]\\, 3d^5 \\, 4s^1$ — half-filled $d$ shell stability',
        'shells': [
            {'r': 0.35, 'label': '$n=1$', 'electrons': 2, 'color': '#4488ff', 'angle_offset': 0},
            {'r': 0.6,  'label': '$n=2$', 'electrons': 8, 'color': '#44cc88', 'angle_offset': 0},
            {'r': 0.9,  'label': '$n=3$', 'electrons': 8, 'color': '#44cc88', 'angle_offset': np.pi/8},
            {'r': 1.05, 'label': '$3d$',  'electrons': 5, 'color': '#cc88ff', 'angle_offset': 0},
            {'r': 1.25, 'label': '$n=4$', 'electrons': 1, 'color': '#ff7755', 'angle_offset': 0},
        ],
        'core_electrons': [],
    },
    {
        'name': 'iron_56', 'symbol': 'Fe', 'Z': 26, 'A': 56,
        'title': 'Iron-56: Maximum Binding Energy',
        'subtitle': '$[Ar]\\, 3d^6 \\, 4s^2$ — peak nuclear stability (FCC-14)',
        'shells': [
            {'r': 0.35, 'label': '$n=1$', 'electrons': 2, 'color': '#4488ff', 'angle_offset': 0},
            {'r': 0.6,  'label': '$n=2$', 'electrons': 8, 'color': '#44cc88', 'angle_offset': 0},
            {'r': 0.9,  'label': '$n=3$', 'electrons': 8, 'color': '#44cc88', 'angle_offset': np.pi/8},
            {'r': 1.05, 'label': '$3d$',  'electrons': 6, 'color': '#cc88ff', 'angle_offset': 0},
            {'r': 1.25, 'label': '$n=4$', 'electrons': 2, 'color': '#ff7755', 'angle_offset': np.pi/6},
        ],
        'core_electrons': [],
    },
]


def generate_topology(elem):
    """Generate an orbital topology figure for one element."""
    fig, ax = plt.subplots(figsize=(10, 10), facecolor='#0a0a0a')
    ax.set_facecolor('#0a0a0a')
    ax.set_xlim(-1.65, 1.65)
    ax.set_ylim(-1.65, 1.65)
    ax.set_aspect('equal')
    ax.axis('off')

    # =========================================================================
    # RADIAL METRIC STRAIN HEATMAP BACKGROUND
    # Simulates the continuous 1/r² strain field radiating from the nucleus.
    # Uses the 'inferno' colormap: bright core → dark edges, like the
    # lithium_topological_strain.png reference.
    # =========================================================================
    N = 500
    x_grid = np.linspace(-1.65, 1.65, N)
    y_grid = np.linspace(-1.65, 1.65, N)
    X, Y = np.meshgrid(x_grid, y_grid)
    R_grid = np.sqrt(X**2 + Y**2) + 0.01  # avoid divide by zero

    # Scale the strain field: brighter core for heavier elements
    Z_eff = elem['Z']
    strain = Z_eff / (R_grid**2 + 0.15)  # softened 1/r² well
    strain = strain / strain.max()  # normalize to [0, 1]

    # Apply inferno colormap with reduced alpha so shells remain visible
    ax.imshow(strain, extent=[-1.65, 1.65, -1.65, 1.65], origin='lower',
              cmap='inferno', alpha=0.35, zorder=0, aspect='auto')

    # =========================================================================
    # POLAR LATTICE GRID — subtle concentric rings + radial spokes
    # Represents the underlying fabric over which the strain heatmap is painted.
    # =========================================================================
    grid_color = '#333355'
    n_rings = 8
    max_ring_r = 1.6
    for k in range(1, n_rings + 1):
        r_ring = k * max_ring_r / n_rings
        circle = plt.Circle((0, 0), r_ring, fill=False,
                            edgecolor=grid_color, linewidth=0.3,
                            alpha=0.35, linestyle='-', zorder=0)
        ax.add_patch(circle)

    # Radial spokes (every 30°)
    for angle_deg in range(0, 360, 30):
        angle = np.radians(angle_deg)
        ax.plot([0, max_ring_r * np.cos(angle)],
                [0, max_ring_r * np.sin(angle)],
                color=grid_color, linewidth=0.3, alpha=0.25, zorder=0)

    # Draw harmonic background shells (light dashed)
    max_r = max(s['r'] for s in elem['shells'])
    for nr in np.linspace(0.25, max_r * 0.8, 3):
        circle = plt.Circle((0, 0), nr, fill=False, color='#444444',
                             linestyle='--', linewidth=0.5, zorder=1)
        ax.add_patch(circle)

    # =========================================================================
    # SHELL TRACKS AND SOLITONS
    # =========================================================================
    # Determine closed-shell capacity per harmonic:
    #   n=1 → 2 electrons (1s²)
    #   n=2 → 8 electrons (2s²2p⁶)
    #   n=3 → 8 electrons (3s²3p⁶) for our purposes (first 14 elements)
    shell_capacities = {1: 2, 2: 8, 3: 8}

    for shell_idx, shell in enumerate(elem['shells']):
        r = shell['r']
        n_elec = shell['electrons']
        color = shell['color']
        label = shell['label']
        offset = shell.get('angle_offset', 0)

        # Determine shell number from label
        shell_n = shell_idx + 1

        # Determine if this is a closed shell
        capacity = shell_capacities.get(shell_n, 8)
        is_closed = (n_elec >= capacity)
        is_outer = (r == max_r)

        # Shell track circle
        if is_closed:
            track_color = '#44cc88'  # green = saturated
        elif is_outer:
            track_color = '#ff9900'  # orange = active valence
        else:
            track_color = '#888888'  # grey = partial inner (shouldn't occur for these elements)

        track_lw = 2.5 if is_outer else 1.5
        circle = plt.Circle((0, 0), r, fill=False, color=track_color,
                             linewidth=track_lw, linestyle='-', zorder=2)
        ax.add_patch(circle)

        # Shell label
        ax.text(r * 0.65, -r * 0.65, label, color=track_color, fontsize=10,
                ha='center', zorder=5)

        # Place electrons/solitons
        if n_elec == 0:
            continue

        angles = [offset + 2 * np.pi * i / n_elec + np.pi/2 for i in range(n_elec)]

        for angle in angles:
            x = r * np.cos(angle)
            y = r * np.sin(angle)

            # Inner soliton dots are larger now (was 8, now 10)
            # Outer valence solitons remain 12
            marker_size = 12 if is_outer else 10
            marker_color = color if is_outer else track_color
            ax.plot(x, y, 'o', color=marker_color, markersize=marker_size,
                    zorder=8, markeredgecolor='white', markeredgewidth=0.4)

            # Force arrows ONLY on outermost non-closed shells with >1 soliton
            # This fixes Helium: it's closed (2/2), so no arrows
            if is_outer and not is_closed and n_elec > 1:
                rmag = np.sqrt(x**2 + y**2)
                dx_out, dy_out = x / rmag, y / rmag
                dx_in, dy_in = -dx_out, -dy_out

                # Outward repulsion arrows (red)
                for fan in [-0.2, -0.1, 0, 0.1, 0.2]:
                    ca, sa = np.cos(fan), np.sin(fan)
                    fdx = dx_out * ca - dy_out * sa
                    fdy = dx_out * sa + dy_out * ca
                    ax.annotate('', xy=(x + fdx*0.22, y + fdy*0.22),
                                xytext=(x + fdx*0.06, y + fdy*0.06),
                                arrowprops=dict(arrowstyle='->', color='#ff4422',
                                               lw=1.2, mutation_scale=9),
                                zorder=9)

                # Inward confinement arrows (blue)
                for fan in [-0.12, 0, 0.12]:
                    ca, sa = np.cos(fan), np.sin(fan)
                    fdx = dx_in * ca - dy_out * sa
                    fdy = dx_in * sa + dy_out * ca
                    ax.annotate('', xy=(x + fdx*0.18, y + fdy*0.18),
                                xytext=(x + fdx*0.05, y + fdy*0.05),
                                arrowprops=dict(arrowstyle='->', color='#44aaff',
                                               lw=1.4, mutation_scale=9),
                                zorder=9)

        # Angular separation label (if more than 1 electron on outer shell)
        if is_outer and n_elec > 1:
            sep_deg = 360.0 / n_elec
            label_r = r + 0.28
            for i in range(n_elec):
                mid_angle = angles[i] + np.pi / n_elec
                lx = label_r * np.cos(mid_angle)
                ly = label_r * np.sin(mid_angle)
                ax.text(lx, ly, f'${sep_deg:.0f}°$', color='#ff9900', fontsize=11,
                        ha='center', va='center', fontweight='bold', zorder=5)

    # Nucleus
    nuc_size = 22
    ax.plot(0, 0, 'o', color='#00e6b0', markersize=nuc_size, zorder=10)
    ax.text(0, 0, elem['symbol'], color='#0a0a0a', fontsize=14, fontweight='bold',
            ha='center', va='center', zorder=11)

    # Title
    ax.text(0, 1.55, elem['title'], color='white', fontsize=15,
            ha='center', va='center', fontweight='bold', zorder=12)
    ax.text(0, 1.42, elem['subtitle'], color='#cccccc', fontsize=11,
            ha='center', va='center', style='italic', zorder=12)

    # =========================================================================
    # HYDROGEN ANNOTATION: use the empty lower space
    # =========================================================================
    if elem['symbol'] == 'H':
        ax.text(0, -1.25, 'The standing wave closes on itself —',
                color='#aaaaaa', fontsize=10, ha='center', va='center',
                style='italic', zorder=12)
        ax.text(0, -1.38, 'no angular partner, no repulsion, no strain dipole.',
                color='#aaaaaa', fontsize=10, ha='center', va='center',
                style='italic', zorder=12)

    # Legend (only if outer shell has force arrows)
    has_forces = any(
        s['r'] == max_r
        and s['electrons'] > 1
        and s['electrons'] < shell_capacities.get(idx + 1, 8)
        for idx, s in enumerate(elem['shells'])
    )
    if has_forces:
        from matplotlib.lines import Line2D
        legend_elements = [
            Line2D([0], [0], marker='>', color='#ff4422', label='Outward: Soliton Repulsion',
                   markersize=8, linestyle='None'),
            Line2D([0], [0], marker='<', color='#44aaff', label='Inward: Harmonic Confinement',
                   markersize=8, linestyle='None'),
        ]
        legend = ax.legend(handles=legend_elements, loc='lower left',
                          facecolor='#1a1a1a', edgecolor='#444444', fontsize=9)
        for t in legend.get_texts():
            t.set_color('white')

    outpath = os.path.join(OUTDIR, f"{elem['name']}_topology.png")
    plt.savefig(outpath, dpi=300, bbox_inches='tight', facecolor='#0a0a0a')
    plt.close()
    print(f"  [ok] {elem['name']}_topology.png")
    return outpath


if __name__ == '__main__':
    print("=" * 60)
    print("AVE ORBITAL TOPOLOGY FIGURE GENERATOR")
    print(f"Output: {OUTDIR}")
    print("=" * 60)

    for elem in ELEMENTS:
        generate_topology(elem)

    print(f"\n{'=' * 60}")
    print(f"ALL {len(ELEMENTS)} TOPOLOGY FIGURES GENERATED")
    print("=" * 60)
