import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D
import os

def main():
    print("==========================================================")
    print(" AVE PLANCK SCALE: STRING THEORY TOPOLOGICAL SIMULATION")
    print("==========================================================\n")

    print("- Generating standard 1D 'String Resonance'...")
    print("- Superimposing AVE continuous LC wave parameters...")
    print("- Rendering topological dynamics...\n")

    # Animation parameters
    FRAMES = 120
    FPS = 30
    
    # Parametric equations for a 3_1 Trefoil knot (a "closed string")
    # x(t) = sin(t) + 2sin(2t)
    # y(t) = cos(t) - 2cos(2t)
    # z(t) = -sin(3t)
    
    t = np.linspace(0, 2*np.pi, 500)
    
    # Unperturbed Knot coordinates
    x_base = np.sin(t) + 2 * np.sin(2 * t)
    y_base = np.cos(t) - 2 * np.cos(2 * t)
    z_base = -np.sin(3 * t)

    fig = plt.figure(figsize=(10, 8), facecolor='#111111')
    ax = fig.add_subplot(111, projection='3d')
    ax.set_facecolor('#111111')

    # Plot base manifold (translucent to show it as a guide path)
    ax.plot(x_base, y_base, z_base, color='cyan', alpha=0.2, lw=4, label='AVE LC Impedance Bound')
    
    # The "String" trace (will be animated)
    # It acts as a continuous wave rippling along the 3_1 perimeter
    string_line, = ax.plot([], [], [], color='magenta', lw=4, alpha=0.9, label='Nambu-Goto "Closed String"')
    
    # A single trace cursor to show energy sweeping the manifold
    cursor, = ax.plot([], [], [], marker='o', color='white', markersize=8)

    ax.legend(loc='upper right', facecolor='#111111', edgecolor='white', labelcolor='white')
    ax.set_title("String Tension translated to Macroscopic LC Inductance", color='white', pad=20, fontsize=14)
    
    # Axis styling
    ax.set_axis_off()
    ax.set_xlim(-3, 3)
    ax.set_ylim(-3, 3)
    ax.set_zlim(-3, 3)

    plt.tight_layout()

    def update(frame):
        # We simulate the string 'vibrating' by superimposing a high-frequency
        # continuous transverse LC wave (Ponderomotive standing wave) along the knot.
        
        # Phase velocity
        phase = (frame / FRAMES) * 2 * np.pi
        
        # Harmonic perturbation simulating "string mechanics" (vibrations)
        # In AVE, this is simply the AC displacement current amplitude dD/dt
        amplitude = 0.2
        wave_freq = 10
        
        # The perturbation applies radially outward relative to the local curvature
        x_wave = x_base + amplitude * np.sin(wave_freq * t - 3 * phase) * np.cos(t)
        y_wave = y_base + amplitude * np.sin(wave_freq * t - 3 * phase) * np.sin(t)
        z_wave = z_base + amplitude * np.cos(wave_freq * t - 3 * phase)
        
        string_line.set_data(x_wave, y_wave)
        string_line.set_3d_properties(z_wave)
        
        # Move the leading trace cursor
        cursor_index = int((frame / FRAMES) * len(t)) % len(t)
        cursor.set_data([x_wave[cursor_index]], [y_wave[cursor_index]])
        cursor.set_3d_properties([z_wave[cursor_index]])
        
        # Slowly rotate the view
        ax.view_init(elev=30, azim=(frame * 360 / FRAMES))
        
        return string_line, cursor

    ani = animation.FuncAnimation(fig, update, frames=FRAMES, blit=False, interval=1000/FPS)
    
    os.makedirs('standard_model/animations', exist_ok=True)
    out_path = 'standard_model/animations/string_theory_lc_mapping.gif'
    
    print(f"Rendering Nambu-Goto LC trace to {out_path}...")
    ani.save(out_path, writer='pillow', fps=FPS)
    print("Success! Animation complete.")

if __name__ == "__main__":
    main()
