import matplotlib.pyplot as plt
import matplotlib.patches as patches
import os

def create_flowchart():
    fig, ax = plt.subplots(figsize=(12, 8), facecolor='#050510')
    ax.set_facecolor('#050510')
    ax.axis('off')

    # Define coordinates
    inputs_y = 0.8
    network_y = 0.5
    macro_y = 0.2
    
    # Helper to draw boxes
    def draw_box(x, y, text, color, width=0.22, height=0.12):
        box = patches.FancyBboxPatch((x - width/2, y - height/2), width, height, 
                                     boxstyle="round,pad=0.02",
                                     ec=color, fc='#111122', lw=2)
        ax.add_patch(box)
        ax.text(x, y, text, ha='center', va='center', color='white', 
                fontsize=11, fontweight='bold')

    # Helper to draw arrows
    def draw_arrow(start, end, color='white', text=None):
        ax.annotate('', xy=end, xytext=start,
                    arrowprops=dict(arrowstyle="->", color=color, lw=2,
                                    connectionstyle="arc3,rad=0.1"))
        if text:
            mid_x = (start[0] + end[0]) / 2
            mid_y = (start[1] + end[1]) / 2 + 0.02
            ax.text(mid_x, mid_y, text, color=color, fontsize=9, ha='center')

    # Inputs
    draw_box(0.2, inputs_y, "Planck's Constant ($h$)\nCirculation Quantum", '#ffaa00')
    draw_box(0.5, inputs_y, "Speed of Light ($c$)\nPhase Velocity", '#ffaa00')
    draw_box(0.8, inputs_y, "Elementary Charge ($e$)\nFlux Quantum", '#ffaa00')
    ax.text(0.5, inputs_y + 0.1, "1. Empirical Calibration Inputs", color='#ffaa00', fontsize=14, fontweight='bold', ha='center')

    # Network Constants
    draw_box(0.2, network_y, "Node Inductance\nL = h / (e² c)", '#00ffff')
    draw_box(0.5, network_y, "Node Distance\n$ℓ_{node}$ (Topology)", '#00ffff')
    draw_box(0.8, network_y, "Link Capacitance\nC = e² / (h c)", '#00ffff')
    ax.text(0.5, network_y + 0.1, "2. Derived Network Constants (LC Lattice)", color='#00ffff', fontsize=14, fontweight='bold', ha='center')

    # Macroscopic
    draw_box(0.2, macro_y, "Permeability\n$\mu_0 = L / ℓ_{node}$", '#00ff00')
    draw_box(0.5, macro_y, "Impedance\n$Z_0 = \sqrt{L/C}$", '#00ff00')
    draw_box(0.8, macro_y, "Permittivity\n$\epsilon_0 = C / ℓ_{node}$", '#00ff00')
    ax.text(0.5, macro_y + 0.1, "3. Emergent Continuum Moduli", color='#00ff00', fontsize=14, fontweight='bold', ha='center')

    # Arrows
    draw_arrow((0.2, inputs_y - 0.06), (0.2, network_y + 0.06), '#aaaaaa')
    draw_arrow((0.8, inputs_y - 0.06), (0.8, network_y + 0.06), '#aaaaaa')
    draw_arrow((0.5, inputs_y - 0.06), (0.5, network_y + 0.06), '#aaaaaa')

    draw_arrow((0.2, network_y - 0.06), (0.2, macro_y + 0.06), '#aaaaaa')
    draw_arrow((0.8, network_y - 0.06), (0.8, macro_y + 0.06), '#aaaaaa')
    draw_arrow((0.2, network_y - 0.06), (0.5, macro_y + 0.06), '#aaaaaa')
    draw_arrow((0.8, network_y - 0.06), (0.5, macro_y + 0.06), '#aaaaaa')

    plt.suptitle("AVE Framework: Constants Derivation Pipeline", color='white', fontsize=18, fontweight='bold', y=0.95)

    out_dir = os.path.join(os.path.dirname(__file__), '..', '..', 'assets', 'figures')
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, 'calibration_flowchart.png')
    plt.savefig(out_path, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor())
    print(f"Saved: {out_path}")

if __name__ == "__main__":
    create_flowchart()
