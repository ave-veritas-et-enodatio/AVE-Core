import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import os

def create_neon20_plot():
    fig = plt.figure(figsize=(10, 10), facecolor='#050510')
    ax = fig.add_subplot(111, projection='3d')
    ax.set_facecolor('#050510')

    # Trigonal bipyramid geometry for the 5 alpha particles
    # r and h are arbitrary for visualization, but let's represent them symmetrically
    r = 1.0
    h = 1.5

    # Coordinates
    eq1 = np.array([r, 0, 0])
    eq2 = np.array([-0.5*r, r*np.sqrt(3)/2, 0])
    eq3 = np.array([-0.5*r, -r*np.sqrt(3)/2, 0])
    p1 = np.array([0, 0, h])
    p2 = np.array([0, 0, -h])

    points = [eq1, eq2, eq3, p1, p2]
    
    # Plot bonds (edges of the bipyramid)
    # Equatorial triangle
    bonds = [
        (eq1, eq2), (eq2, eq3), (eq3, eq1),
        (eq1, p1), (eq2, p1), (eq3, p1),
        (eq1, p2), (eq2, p2), (eq3, p2)
    ]
    
    for bond in bonds:
        pA, pB = bond
        ax.plot([pA[0], pB[0]], [pA[1], pB[1]], [pA[2], pB[2]], color='#00ffcc', lw=3, alpha=0.8)

    # Note: the Neon-20 bond lengths in the manuscript computation gave exactly 18617.730 MeV.
    # We will annotate the bonds with conceptual d_ij distances.
    
    # Plot alpha particles as large spheres
    u, v = np.mgrid[0:2*np.pi:30j, 0:np.pi:15j]
    sphere_r = 0.25
    for p in points:
        x = p[0] + sphere_r * np.cos(u) * np.sin(v)
        y = p[1] + sphere_r * np.sin(u) * np.sin(v)
        z = p[2] + sphere_r * np.cos(v)
        ax.plot_surface(x, y, z, color='#ff00aa', alpha=0.9, edgecolor='k', lw=0.5)

    # Annotate alpha particles (moved further out to avoid overlap)
    ax.text(eq1[0]*1.4, eq1[1]*1.4, eq1[2], '$\\alpha_1$', color='white', fontsize=16, fontweight='bold')
    ax.text(eq2[0]*1.4, eq2[1]*1.4, eq2[2], '$\\alpha_2$', color='white', fontsize=16, fontweight='bold')
    ax.text(eq3[0]*1.4, eq3[1]*1.4, eq3[2], '$\\alpha_3$', color='white', fontsize=16, fontweight='bold')
    ax.text(p1[0], p1[1], p1[2]*1.3, '$\\alpha_{North}$', color='white', fontsize=16, fontweight='bold')
    ax.text(p2[0], p2[1], p2[2]*1.3, '$\\alpha_{South}$', color='white', fontsize=16, fontweight='bold')

    # Annotate d_ij bonds
    def annotate_bond(pA, pB, label):
        mid = (pA + pB) / 2
        # Offset bond text slightly to prevent overlap with the line
        ax.text(mid[0]*1.1, mid[1]*1.1, mid[2]*1.1, label, color='#00ffcc', fontsize=14,
                bbox=dict(facecolor='#111122', edgecolor='none', alpha=0.8))

    annotate_bond(eq1, eq2, '$d_{eq}$')
    annotate_bond(eq1, p1, '$d_{polar}$')

    # Add a descriptive tech box (moved down to avoid title overlap)
    ax.text2D(0.05, 0.85, 
              "Neon-20 ($^{20}$Ne) Structure:\nTrigonal Bipyramid (5 $\\alpha$ particles)\n\n"
              "Total Binding Energy = $\\sum M_{topo}(d_{ij})$\n"
              "Computed Mass = 18617.730 MeV", 
              transform=ax.transAxes, color='white', fontsize=14,
              bbox=dict(facecolor='#111122', edgecolor='#ff00aa', boxstyle='round,pad=0.5'))

    ax.set_title("Neon-20 Poly-Alpha Geometry", color='white', fontsize=18, fontweight='bold', pad=20)
    
    # Clean up axes
    ax.set_axis_off()
    ax.view_init(elev=20., azim=45)
    
    plt.tight_layout()
    
    out_dir = os.path.join(os.path.dirname(__file__), '..', '..', 'assets', 'figures')
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, 'neon20_bipyramid.png')
    plt.savefig(out_path, dpi=300, facecolor=fig.get_facecolor(), bbox_inches='tight')
    print(f"Saved: {out_path}")

if __name__ == "__main__":
    create_neon20_plot()
