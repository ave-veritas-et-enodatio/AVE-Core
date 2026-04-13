import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import os

def main():
    print("==========================================================")
    print(" AVE: MUON DECAY FDTD TOPOLOGICAL ANIMATOR")
    print("==========================================================\n")

    fig, ax = plt.subplots(figsize=(8, 8))
    fig.patch.set_facecolor('#111111')
    ax.set_facecolor('#111111')
    
    # Limits for the vacuum slice
    ax.set_xlim(-6, 6)
    ax.set_ylim(-6, 6)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title(r"Topological Rupture: Muon ($\mu^-$) Decay", color='white', fontsize=16, pad=20)
    
    # Subtitle for Neutrino emission
    subtitle = ax.text(0, -5.5, "State: High-Tension $3_1$ Geometry (Muon)", 
                       color='orange', fontsize=12, ha='center', va='center')

    # Base Trefoil Knot Equation (2D Projection)
    t = np.linspace(0, 2 * np.pi, 300)
    base_x = np.sin(t) + 2 * np.sin(2 * t)
    base_y = np.cos(t) - 2 * np.cos(2 * t)

    # Plot elements
    knot_line, = ax.plot([], [], lw=3, color='orange')
    
    # We will simulate a transverse ripple moving outwards
    # We'll draw 3 concentric circles for the shockwave
    shock_1, = ax.plot([], [], lw=2, color='white', alpha=0.0)
    shock_2, = ax.plot([], [], lw=1.5, color='cyan', alpha=0.0)
    shock_3, = ax.plot([], [], lw=1, color='blue', alpha=0.0)

    # Simulation parameters
    total_frames = 120
    trigger_frame = 40
    
    r_mu = 0.25 # Tight Muon
    r_e = 1.2   # Relaxed Electron
    
    def init():
        knot_line.set_data([], [])
        shock_1.set_data([], [])
        shock_2.set_data([], [])
        shock_3.set_data([], [])
        return knot_line, shock_1, shock_2, shock_3, subtitle

    def update(frame):
        # 1. Knot Geometry Logic
        if frame < trigger_frame:
            # Stable Muon
            current_r = r_mu
            knot_color = 'orange'
            subtitle.set_text("State: High-Tension $3_1$ Geometry (Muon)")
            subtitle.set_color('orange')
        elif frame < trigger_frame + 15:
            # Unspooling (expansion)
            progress = (frame - trigger_frame) / 15.0
            # Ease out expansion
            eased_progress = 1 - (1 - progress)**3
            current_r = r_mu + (r_e - r_mu) * eased_progress
            
            # Interpolate color from orange to blue
            # Orange: (1.0, 0.65, 0.0)
            # Blue: (0.2, 0.4, 1.0)
            r_c = 1.0 - (1.0 - 0.2) * progress
            g_c = 0.65 - (0.65 - 0.4) * progress
            b_c = 0.0 + (1.0 - 0.0) * progress
            knot_color = (r_c, g_c, b_c)
            
            subtitle.set_text("State: Topological Snapping (Relaxation)")
            subtitle.set_color('white')
        else:
            # Stable Electron
            current_r = r_e
            knot_color = '#3366ff' # Blue
            subtitle.set_text(r"State: Lowest-Impedance $3_1$ Geometry (Electron) + $\nu_\mu$ Wake")
            subtitle.set_color('#3366ff')
            
        # Add high-frequency jitter (RMS Vacuum Noise) to the knot
        jitter = np.random.normal(0, 0.02 * current_r, len(t))
        
        # Apply rotation to make it dynamic
        theta = frame * 0.05
        rot_matrix = np.array([[np.cos(theta), -np.sin(theta)],
                               [np.sin(theta),  np.cos(theta)]])
        
        coords = np.vstack((base_x * current_r + jitter, base_y * current_r + jitter))
        rotated_coords = np.dot(rot_matrix, coords)
        
        knot_line.set_data(rotated_coords[0], rotated_coords[1])
        knot_line.set_color(knot_color)
        
        # 2. Neutrino Shockwave Logic
        if frame >= trigger_frame:
            # Speed of light propagation
            c = 0.2
            elapsed = frame - trigger_frame
            
            radius_1 = elapsed * c + r_e * 0.5
            radius_2 = radius_1 - 0.2
            radius_3 = radius_1 - 0.4
            
            # Fade out as it expands (1/r dispersion)
            alpha_wave = max(0, 1.0 - (elapsed / 40.0))
            
            theta_cir = np.linspace(0, 2*np.pi, 200)
            
            if radius_1 > 0:
                shock_1.set_data(radius_1 * np.cos(theta_cir), radius_1 * np.sin(theta_cir))
                shock_1.set_alpha(alpha_wave)
            if radius_2 > 0:
                shock_2.set_data(radius_2 * np.cos(theta_cir), radius_2 * np.sin(theta_cir))
                shock_2.set_alpha(alpha_wave * 0.8)
            if radius_3 > 0:
                shock_3.set_data(radius_3 * np.cos(theta_cir), radius_3 * np.sin(theta_cir))
                shock_3.set_alpha(alpha_wave * 0.5)
        else:
            shock_1.set_alpha(0)
            shock_2.set_alpha(0)
            shock_3.set_alpha(0)

        return knot_line, shock_1, shock_2, shock_3, subtitle

    ani = animation.FuncAnimation(fig, update, frames=total_frames,
                                  init_func=init, blit=True, interval=50)

    os.makedirs('standard_model/animations', exist_ok=True)
    out_path = 'standard_model/animations/lepton_decay_neutrino_wake.gif'
    print("Rendering frames, please wait...")
    ani.save(out_path, writer='pillow', fps=20)
    print(f"Success! Animation saved to: {out_path}")

if __name__ == "__main__":
    main()
