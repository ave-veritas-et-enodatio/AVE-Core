import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D
import os

def main():
    print("==========================================================")
    print(" AVE SUBATOMIC SCALE: ELECTROWEAK DIELECTRIC SPARK")
    print("==========================================================\n")

    print("- Generating precursor tightly bound topological state (Neutron)...")
    print("- Initiating topological rupture (Beta Decay)...")
    print("- Rendering the 'W-Boson' as a macroscopic transient Dielectric Phase-Arc...\n")

    # Animation parameters
    FRAMES = 120
    FPS = 30
    
    # We will simulate a knot that "snaps" at frame 40,
    # throwing a high-energy transient spark (W-) across the gap
    # until it settles into a lower energy state (Proton + Electron).

    t = np.linspace(0, 2*np.pi, 500)
    
    fig = plt.figure(figsize=(10, 8), facecolor='#111111')
    ax = fig.add_subplot(111, projection='3d')
    ax.set_facecolor('#111111')

    # Continuous flux lines of the neutron
    knot_line, = ax.plot([], [], [], color='blue', lw=3, label='Primary Flux Geometry')
    
    # The "W-Boson" spark
    spark_line,  = ax.plot([], [], [], color='white', lw=5, alpha=0.9, label='Transient Macroscopic Spark (W-Boson)')
    
    # The resulting decay product (Electron)
    electron_line, = ax.plot([], [], [], color='magenta', lw=2, alpha=0, label='Decay Product Phase-Lock ($e^-$)')

    ax.legend(loc='upper right', facecolor='#111111', edgecolor='white', labelcolor='white')
    ax.set_title("W-Boson explicitly mapped as a Transient Dielectric Short", color='white', pad=20, fontsize=14)
    
    # Axis styling
    ax.set_axis_off()
    ax.set_xlim(-3, 3)
    ax.set_ylim(-3, 3)
    ax.set_zlim(-3, 3)

    plt.tight_layout()

    def update(frame):
        # A 5-crossing complex knot breaking into a simpler 3-crossing
        
        # Pre-decay: tight, high-tension knot
        if frame < 40:
            x = np.sin(t) + 1.5 * np.sin(2 * t)
            y = np.cos(t) - 1.5 * np.cos(2 * t)
            z = -np.sin(5 * t) * (1 - frame/80)
            
            knot_line.set_data(x, y)
            knot_line.set_3d_properties(z)
            
            spark_line.set_data([], [])
            spark_line.set_3d_properties([])
            
        # The Spark (W-Boson) occurs at frame 40-50
        elif 40 <= frame <= 50:
            # Knot begins to drift and unravel
            x = np.sin(t) + 1.0 * np.sin(2 * t)
            y = np.cos(t) - 1.0 * np.cos(2 * t)
            z = -np.sin(3 * t)
            
            knot_line.set_data(x, y)
            knot_line.set_3d_properties(z)
            
            # The Spark is a severe, high frequency burst between the severing ends
            spark_t = np.linspace(-0.5, 0.5, 50)
            spark_x = 1.5 + np.random.normal(0, 0.2, 50)
            spark_y = np.random.normal(0, 0.2, 50)
            spark_z = spark_t * 5 + np.random.normal(0, 0.5, 50)
            
            spark_line.set_data(spark_x, spark_y)
            spark_line.set_3d_properties(spark_z)
            
        # Post-decay: lower energy proton and ejected electron
        else:
            # Proton relaxes
            x = np.sin(t) + 0.8 * np.sin(2 * t)
            y = np.cos(t) - 0.8 * np.cos(2 * t)
            z = -np.sin(3 * t) * 0.5
            
            knot_line.set_data(x, y)
            knot_line.set_3d_properties(z)
            
            spark_line.set_data([], [])
            spark_line.set_3d_properties([])
            
            # Electron is born and drifts away
            drift = (frame - 50) * 0.1
            e_x = 2 + drift + 0.5 * np.sin(3*t)
            e_y = drift + 0.5 * np.cos(3*t)
            e_z = 0.5 * -np.sin(2*t)
            
            electron_line.set_alpha(min(1.0, (frame-50)/20))
            electron_line.set_data(e_x, e_y)
            electron_line.set_3d_properties(e_z)
            
        # Rotate view
        ax.view_init(elev=20, azim=(frame * 360 / FRAMES))
        
        return knot_line, spark_line, electron_line

    ani = animation.FuncAnimation(fig, update, frames=FRAMES, blit=False, interval=1000/FPS)
    
    os.makedirs('standard_model/animations', exist_ok=True)
    out_path = 'standard_model/animations/electroweak_dielectric_spark.gif'
    
    print(f"Rendering Dielectric Phase-Arc to {out_path}...")
    ani.save(out_path, writer='pillow', fps=FPS)
    print("Success! Animation complete.")

if __name__ == "__main__":
    main()
