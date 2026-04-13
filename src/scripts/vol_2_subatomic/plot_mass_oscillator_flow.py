import matplotlib.pyplot as plt
import matplotlib.patches as patches
import os

def create_flowchart():
    fig, ax = plt.subplots(figsize=(10, 8), facecolor='#050510')
    ax.set_facecolor('#050510')
    ax.axis('off')

    # Draw boxes
    def draw_box(x, y, text, color, width=0.4, height=0.12):
        box = patches.FancyBboxPatch((x - width/2, y - height/2), width, height, 
                                     boxstyle="round,pad=0.02",
                                     ec=color, fc='#111122', lw=2)
        ax.add_patch(box)
        ax.text(x, y, text, ha='center', va='center', color='white', 
                fontsize=11, fontweight='bold')

    # Draw arrows
    def draw_arrow(start, end, text=None, text_offset=(0.02, 0)):
        ax.annotate('', xy=end, xytext=start,
                    arrowprops=dict(arrowstyle="->", color='w', lw=2))
        if text:
            mid_x = (start[0] + end[0]) / 2 + text_offset[0]
            mid_y = (start[1] + end[1]) / 2 + text_offset[1]
            ax.text(mid_x, mid_y, text, color='#ffff00', fontsize=10, ha='left')

    # Steps
    draw_box(0.5, 0.85, "1. Ansatz Mass Estimate ($m_0$)\nSet initial particle radius $r_0 \propto 1/m_0$", '#00ffff')
    
    draw_box(0.5, 0.65, "2. Geometric Integrals (FEM)\nCompute dimensionless scalar fields:\n$I_{scalar}$, $I_{vector}$, $I_{tensor}$", '#ff00aa')
    
    draw_box(0.5, 0.45, "3. Compute Structural Metrics\nEffective Crossing Volume $\mathcal{V}_{cross}$\nTopological Scale Factor $\\beta$", '#00ff00')
    
    draw_box(0.5, 0.25, "4. Physical Feedback (LC Network)\nCalculate Total Potential $V_{total}$\nApply Packing Fraction $p_c$", '#ffaa00')
    
    draw_box(0.5, 0.05, "5. Mass Update ($m_{new}$)\n$m_{new} = V_{total} \cdot p_c / c^2$", '#00ffff')

    # Connections
    draw_arrow((0.5, 0.79), (0.5, 0.71))
    draw_arrow((0.5, 0.59), (0.5, 0.51))
    draw_arrow((0.5, 0.39), (0.5, 0.31))
    draw_arrow((0.5, 0.19), (0.5, 0.11))

    # Feedback loop
    ax.annotate('', xy=(0.3, 0.85), xytext=(0.3, 0.05),
                arrowprops=dict(arrowstyle="->", color='#ff0000', lw=2, connectionstyle="bar,fraction=-0.1"))
    
    ax.text(0.12, 0.45, r"Iterate until" + "\n" + r"$m_{new} \approx m_0$" + "\n" + r"(Eigenvalue)", 
            color='#ffaaaa', fontsize=12, fontweight='bold', ha='center', va='center',
            bbox=dict(facecolor='#330000', edgecolor='#ff0000', boxstyle='round,pad=0.5'))

    plt.suptitle("AVE Framework: Self-Consistent Mass Oscillator", color='white', fontsize=16, fontweight='bold', y=0.98)

    out_dir = os.path.join(os.path.dirname(__file__), '..', '..', 'assets', 'figures')
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, 'mass_oscillator_flowchart.png')
    plt.savefig(out_path, dpi=300, facecolor=fig.get_facecolor(), bbox_inches='tight')
    print(f"Saved: {out_path}")

if __name__ == "__main__":
    create_flowchart()
