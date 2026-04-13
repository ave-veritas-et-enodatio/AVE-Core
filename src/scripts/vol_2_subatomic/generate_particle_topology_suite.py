"""
Fermion & Baryon Topology Figure Suite
======================================
Generates publication-quality 3D topology figures for all fundamental
particles in the AVE framework:

  1. Electron  (0_1 Unknot)
  2. Muon      (0_1 Unknot, Cosserat rotation excitation)
  3. Tau       (0_1 Unknot, Cosserat curvature-twist excitation)
  4. Neutrino  (Twisted 0_1 Unknot, dispersive)
  5. Proton    (6^3_2 Borromean Link)
  6. Neutron   (6^3_2 Borromean Link + threaded 0_1 Unknot)
  7. Summary   (All particles in a single 2x3+1 panel)
"""
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import os

plt.style.use('dark_background')
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), '..', '..', 'assets', 'sim_outputs')
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ─── Topology Generators ────────────────────────────────────────────

def unknot(R=2.0, resolution=500):
    """0_1 Unknot: a simple closed loop (circle) in 3D."""
    t = np.linspace(0, 2 * np.pi, resolution)
    x = R * np.cos(t)
    y = R * np.sin(t)
    z = np.zeros_like(t)
    return x, y, z, t

def excited_unknot(R=2.0, mode='rotation', resolution=500):
    """
    Cosserat excitation of the unknot.
    - mode='rotation': torsional ripple (Muon — 1 quantum)
    - mode='curvature': bending ripple (Tau — full curvature sector)
    """
    t = np.linspace(0, 2 * np.pi, resolution)
    x = R * np.cos(t)
    y = R * np.sin(t)
    if mode == 'rotation':
        # Torsional (out-of-plane) oscillation — 3 lobes (α√(3/7) coupling)
        z = 0.35 * np.sin(3 * t)
    elif mode == 'curvature':
        # Strong curvature-twist excitation — 5 lobes
        z = 0.6 * np.sin(5 * t)
    else:
        z = np.zeros_like(t)
    return x, y, z, t

def twisted_unknot(R=2.0, resolution=500):
    """Dispersive twisted unknot: neutrino. A helical open loop."""
    t = np.linspace(0, 4 * np.pi, resolution)
    pitch = 0.8
    x = R * np.cos(t) * np.exp(-0.05 * t)
    y = R * np.sin(t) * np.exp(-0.05 * t)
    z = pitch * t / (2 * np.pi)
    return x, y, z, t

def borromean_link(R=1.5, resolution=500):
    """6^3_2 Borromean linkage: three mutually interlocked rings."""
    t = np.linspace(0, 2 * np.pi, resolution)
    rings = []
    
    # Ring 1: XY plane
    x1 = R * np.cos(t)
    y1 = R * np.sin(t)
    z1 = np.zeros_like(t)
    rings.append((x1, y1, z1, t))
    
    # Ring 2: YZ plane (offset)
    x2 = np.zeros_like(t)
    y2 = R * np.cos(t)
    z2 = R * np.sin(t)
    rings.append((x2, y2, z2, t))
    
    # Ring 3: XZ plane (offset)
    x3 = R * np.cos(t)
    y3 = np.zeros_like(t)
    z3 = R * np.sin(t)
    rings.append((x3, y3, z3, t))
    
    return rings

def threaded_borromean(R_borro=1.5, R_thread=0.4, resolution=500):
    """Neutron: Borromean link with a threaded unknot in the central void."""
    rings = borromean_link(R_borro, resolution)
    
    # Small unknot threaded through the central void
    t_inner = np.linspace(0, 2 * np.pi, resolution)
    x_in = R_thread * np.cos(t_inner)
    y_in = R_thread * np.sin(t_inner)
    z_in = np.zeros_like(t_inner)
    inner = (x_in, y_in, z_in, t_inner)
    
    return rings, inner

# ─── Plotting Helpers ────────────────────────────────────────────────

RING_COLORS = ['#ff3366', '#33ccff', '#ffcc00']
ELECTRON_COLOR = '#00ffcc'
MUON_COLOR = '#ff9900'
TAU_COLOR = '#ff3399'
NEUTRINO_COLOR = '#9966ff'
NEUTRON_THREAD_COLOR = '#66ffcc'

def setup_3d_ax(fig, pos=111):
    ax = fig.add_subplot(pos, projection='3d')
    ax.set_facecolor('#050510')
    ax.xaxis.set_pane_color((0, 0, 0, 0))
    ax.yaxis.set_pane_color((0, 0, 0, 0))
    ax.zaxis.set_pane_color((0, 0, 0, 0))
    ax.grid(False)
    ax.set_axis_off()
    return ax

def set_cubic_limits(ax, lim=3.0):
    ax.set_xlim([-lim, lim])
    ax.set_ylim([-lim, lim])
    ax.set_zlim([-lim, lim])

def plot_phase_loop(ax, x, y, z, t, color, lw=4, alpha=0.9, label=None):
    """Plot with phase-mapped color along the loop."""
    ax.scatter(x, y, z, c=t, cmap='hsv', s=15, alpha=alpha, edgecolors='none')
    ax.plot(x, y, z, color=color, linewidth=lw * 0.3, alpha=0.4)
    if label:
        ax.text2D(0.5, 0.02, label, transform=ax.transAxes, color='white',
                  fontsize=11, ha='center', weight='bold',
                  bbox=dict(boxstyle='round', facecolor='#111122', alpha=0.8, edgecolor=color))

# ─── Individual Figures ──────────────────────────────────────────────

def figure_electron():
    fig = plt.figure(figsize=(8, 8), facecolor='#050510')
    ax = setup_3d_ax(fig)
    x, y, z, t = unknot()
    plot_phase_loop(ax, x, y, z, t, ELECTRON_COLOR,
                    label=r"Electron  $e^-$  ·  $0_1$ Unknot  ·  0.511 MeV")
    ax.set_title("Electron: Ground-State Unknot ($0_1$)", color='white', fontsize=15, pad=15)
    set_cubic_limits(ax)
    ax.view_init(elev=30, azim=45)
    path = os.path.join(OUTPUT_DIR, 'topology_electron.png')
    plt.savefig(path, dpi=300, facecolor=fig.get_facecolor(), bbox_inches='tight')
    plt.close()
    print(f"[+] {path}")

def figure_muon():
    fig = plt.figure(figsize=(8, 8), facecolor='#050510')
    ax = setup_3d_ax(fig)
    x, y, z, t = excited_unknot(mode='rotation')
    plot_phase_loop(ax, x, y, z, t, MUON_COLOR,
                    label=r"Muon  $\mu^-$  ·  Cosserat Rotation  ·  105.7 MeV")
    ax.set_title("Muon: Torsional Cosserat Excitation", color='white', fontsize=15, pad=15)
    set_cubic_limits(ax)
    ax.view_init(elev=30, azim=45)
    path = os.path.join(OUTPUT_DIR, 'topology_muon.png')
    plt.savefig(path, dpi=300, facecolor=fig.get_facecolor(), bbox_inches='tight')
    plt.close()
    print(f"[+] {path}")

def figure_tau():
    fig = plt.figure(figsize=(8, 8), facecolor='#050510')
    ax = setup_3d_ax(fig)
    x, y, z, t = excited_unknot(mode='curvature')
    plot_phase_loop(ax, x, y, z, t, TAU_COLOR,
                    label=r"Tau  $\tau^-$  ·  Curvature-Twist  ·  1776.8 MeV")
    ax.set_title("Tau: Curvature-Twist Cosserat Excitation", color='white', fontsize=15, pad=15)
    set_cubic_limits(ax)
    ax.view_init(elev=30, azim=45)
    path = os.path.join(OUTPUT_DIR, 'topology_tau.png')
    plt.savefig(path, dpi=300, facecolor=fig.get_facecolor(), bbox_inches='tight')
    plt.close()
    print(f"[+] {path}")

def figure_neutrino():
    fig = plt.figure(figsize=(8, 8), facecolor='#050510')
    ax = setup_3d_ax(fig)
    x, y, z, t = twisted_unknot()
    plot_phase_loop(ax, x, y, z, t, NEUTRINO_COLOR,
                    label=r"Neutrino  $\nu_e$  ·  Twisted $0_1$  ·  < 0.8 eV")
    ax.set_title("Neutrino: Dispersive Twisted Unknot", color='white', fontsize=15, pad=15)
    set_cubic_limits(ax, lim=4.0)
    ax.view_init(elev=20, azim=30)
    path = os.path.join(OUTPUT_DIR, 'topology_neutrino.png')
    plt.savefig(path, dpi=300, facecolor=fig.get_facecolor(), bbox_inches='tight')
    plt.close()
    print(f"[+] {path}")

def figure_proton():
    fig = plt.figure(figsize=(8, 8), facecolor='#050510')
    ax = setup_3d_ax(fig)
    rings = borromean_link()
    for i, (x, y, z, t) in enumerate(rings):
        ax.plot(x, y, z, color=RING_COLORS[i], linewidth=4, alpha=0.85,
                label=f"Loop {i+1}")
    ax.text2D(0.5, 0.02, r"Proton  $p$  ·  $6^3_2$ Borromean  ·  938.3 MeV",
              transform=ax.transAxes, color='white', fontsize=11, ha='center', weight='bold',
              bbox=dict(boxstyle='round', facecolor='#111122', alpha=0.8, edgecolor='#ff3366'))
    ax.set_title(r"Proton: $6^3_2$ Borromean Linkage", color='white', fontsize=15, pad=15)
    set_cubic_limits(ax, lim=2.5)
    ax.view_init(elev=25, azim=40)
    path = os.path.join(OUTPUT_DIR, 'topology_proton.png')
    plt.savefig(path, dpi=300, facecolor=fig.get_facecolor(), bbox_inches='tight')
    plt.close()
    print(f"[+] {path}")

def figure_neutron():
    fig = plt.figure(figsize=(8, 8), facecolor='#050510')
    ax = setup_3d_ax(fig)
    rings, inner = threaded_borromean()
    for i, (x, y, z, t) in enumerate(rings):
        ax.plot(x, y, z, color=RING_COLORS[i], linewidth=3.5, alpha=0.75)
    x_in, y_in, z_in, t_in = inner
    ax.scatter(x_in, y_in, z_in, c=t_in, cmap='hsv', s=12, alpha=0.95, edgecolors='none')
    ax.plot(x_in, y_in, z_in, color=NEUTRON_THREAD_COLOR, linewidth=1.5, alpha=0.5)
    ax.text2D(0.5, 0.02,
              r"Neutron  $n$  ·  $6^3_2 \cup 0_1$  ·  939.6 MeV",
              transform=ax.transAxes, color='white', fontsize=11, ha='center', weight='bold',
              bbox=dict(boxstyle='round', facecolor='#111122', alpha=0.8, edgecolor=NEUTRON_THREAD_COLOR))
    ax.set_title(r"Neutron: Borromean Link $\cup$ Threaded Unknot", color='white', fontsize=15, pad=15)
    set_cubic_limits(ax, lim=2.5)
    ax.view_init(elev=25, azim=40)
    path = os.path.join(OUTPUT_DIR, 'topology_neutron.png')
    plt.savefig(path, dpi=300, facecolor=fig.get_facecolor(), bbox_inches='tight')
    plt.close()
    print(f"[+] {path}")

# ─── Summary Panel ───────────────────────────────────────────────────

def figure_summary_panel():
    fig = plt.figure(figsize=(20, 14), facecolor='#050510')
    fig.suptitle("AVE Topological Particle Zoo", color='white', fontsize=22, y=0.97, weight='bold')

    panels = [
        ("Electron $e^-$\n$0_1$ Unknot\n0.511 MeV", unknot, ELECTRON_COLOR, 'fermion'),
        ("Muon $\\mu^-$\nCosserat Rotation\n105.7 MeV", lambda: excited_unknot(mode='rotation'), MUON_COLOR, 'fermion'),
        ("Tau $\\tau^-$\nCurvature-Twist\n1776.8 MeV", lambda: excited_unknot(mode='curvature'), TAU_COLOR, 'fermion'),
        ("Neutrino $\\nu_e$\nTwisted $0_1$\n< 0.8 eV", twisted_unknot, NEUTRINO_COLOR, 'fermion'),
        ("Proton $p$\n$6^3_2$ Borromean\n938.3 MeV", None, None, 'proton'),
        ("Neutron $n$\n$6^3_2 \\cup 0_1$\n939.6 MeV", None, None, 'neutron'),
    ]

    for idx, (label, gen_fn, color, kind) in enumerate(panels):
        row = idx // 3
        col = idx % 3
        ax = fig.add_subplot(2, 3, idx + 1, projection='3d')
        ax.set_facecolor('#050510')
        ax.xaxis.set_pane_color((0, 0, 0, 0))
        ax.yaxis.set_pane_color((0, 0, 0, 0))
        ax.zaxis.set_pane_color((0, 0, 0, 0))
        ax.grid(False)
        ax.set_axis_off()

        if kind == 'fermion':
            x, y, z, t = gen_fn()
            ax.scatter(x, y, z, c=t, cmap='hsv', s=8, alpha=0.9, edgecolors='none')
            ax.plot(x, y, z, color=color, linewidth=1, alpha=0.3)
            lim = 4.0 if 'Neutrino' in label else 3.0
        elif kind == 'proton':
            rings = borromean_link()
            for i, (x, y, z, t) in enumerate(rings):
                ax.plot(x, y, z, color=RING_COLORS[i], linewidth=3, alpha=0.85)
            lim = 2.5
        elif kind == 'neutron':
            rings, inner = threaded_borromean()
            for i, (x, y, z, t) in enumerate(rings):
                ax.plot(x, y, z, color=RING_COLORS[i], linewidth=2.5, alpha=0.7)
            x_in, y_in, z_in, t_in = inner
            ax.scatter(x_in, y_in, z_in, c=t_in, cmap='hsv', s=6, alpha=0.9, edgecolors='none')
            lim = 2.5

        ax.set_xlim([-lim, lim])
        ax.set_ylim([-lim, lim])
        ax.set_zlim([-lim, lim])
        ax.view_init(elev=25, azim=40)

        # Label below each subplot
        border_color = color if color else '#ff3366'
        ax.text2D(0.5, -0.02, label, transform=ax.transAxes, color='white',
                  fontsize=10, ha='center', va='top',
                  bbox=dict(boxstyle='round', facecolor='#111122', alpha=0.85, edgecolor=border_color))

    plt.tight_layout(rect=[0, 0.02, 1, 0.95])
    path = os.path.join(OUTPUT_DIR, 'topology_particle_zoo.png')
    plt.savefig(path, dpi=300, facecolor=fig.get_facecolor(), bbox_inches='tight')
    plt.close()
    print(f"[+] {path}")

# ─── Main ────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 60)
    print("  AVE Fermion & Baryon Topology Figure Suite")
    print("=" * 60)
    figure_electron()
    figure_muon()
    figure_tau()
    figure_neutrino()
    figure_proton()
    figure_neutron()
    figure_summary_panel()
    print("=" * 60)
    print("  All figures generated successfully.")
    print("=" * 60)
