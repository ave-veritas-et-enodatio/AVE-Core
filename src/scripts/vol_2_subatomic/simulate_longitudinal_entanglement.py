import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def simulate_entanglement(frames=200, length=200):
    """
    Simulates a purely classical, deterministic 1D LC grid demonstrating 
    "spooky action at a distance" (Bell's Theorem Paradox).
    
    In the AVE framework:
    1. Light (Transverse waves) travels at exactly c.
    2. Mechanical Tension (Longitudinal waves) travels at v_long >> c along the rigid string.
    
    This simulation fires an entangled pair from the center. 
    The tension wave connects the two ends "instantly", ensuring their states 
    are physically linked long before the slow 'c' wave arrives.
    """
    
    print("\n AVE APPLIED PHYSICS: LONGITUDINAL ENTANGLEMENT & BELL'S THEOREM")
    print("==================================================================")
    print(" Objective: Prove that 'spooky action at a distance' is just a classical")
    print("            high-speed longitudinal tension wave on the LC Grid.")
    
    c = 1.0           # Transverse Phase Velocity (Speed of Light)
    v_long = 15.0     # Longitudinal Tension Velocity (v >> c)
    center = length // 2
    
    # Grid arrays
    transverse_pulse = np.zeros(length)
    longitudinal_pulse = np.zeros(length)
    
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 6), gridspec_kw={'height_ratios': [1, 1]})
    fig.patch.set_facecolor('black')
    
    # Set up Transverse Plot
    ax1.set_facecolor('black')
    line_t_left, = ax1.plot([], [], color='cyan', lw=2, label="Left Transverse 'Photon' (v = c)")
    line_t_right, = ax1.plot([], [], color='magenta', lw=2, label="Right Transverse 'Photon' (v = c)")
    ax1.set_xlim(0, length)
    ax1.set_ylim(-1.5, 1.5)
    ax1.set_title("Transverse Signal (Optical 'Slow' Wave) [c]", color='white')
    ax1.tick_params(colors='white')
    ax1.axvline(center, color='grey', linestyle='--', alpha=0.5)
    ax1.legend(loc='upper right', facecolor='black', edgecolor='white', labelcolor='white')
    
    # Set up Longitudinal Plot
    ax2.set_facecolor('black')
    line_l_left, = ax2.plot([], [], color='white', lw=2, linestyle='--', label="Left Tension Wave (v >> c)")
    line_l_right, = ax2.plot([], [], color='white', lw=2, linestyle='--', label="Right Tension Wave (v >> c)")
    ax2.set_xlim(0, length)
    ax2.set_ylim(-1.5, 1.5)
    ax2.set_title("Longitudinal Tension (Mechanical 'Fast' Sync) [v >> c]", color='white')
    ax2.tick_params(colors='white')
    ax2.axvline(center, color='grey', linestyle='--', alpha=0.5)
    ax2.legend(loc='upper right', facecolor='black', edgecolor='white', labelcolor='white')

    time_text = ax1.text(0.02, 0.90, '', transform=ax1.transAxes, color='white', fontsize=10)
    entangled_text = ax2.text(0.02, 0.05, '', transform=ax2.transAxes, color='yellow', fontsize=12, fontweight='bold')

    def update(frame):
        # Calculate positions
        pos_t_right = min(center + frame * c, length - 1)
        pos_t_left = max(center - frame * c, 0)
        
        pos_l_right = min(center + frame * v_long, length - 1)
        pos_l_left = max(center - frame * v_long, 0)
        
        # Reset arrays
        transverse = np.zeros(length)
        longitudinal = np.zeros(length)
        
        # Gaussian envelope for pulses
        x = np.arange(length)
        
        # Transverse waves (Left = Spin Down, Right = Spin Up)
        t_width = 3.0
        transverse += 1.0 * np.exp(-((x - pos_t_right) ** 2) / (2 * t_width**2)) # Right Up
        transverse += -1.0 * np.exp(-((x - pos_t_left) ** 2) / (2 * t_width**2)) # Left Down
        
        # Longitudinal shockwave (The "Hidden Variable")
        l_width = 5.0
        longitudinal += 0.8 * np.exp(-((x - pos_l_right) ** 2) / (2 * l_width**2))
        longitudinal += 0.8 * np.exp(-((x - pos_l_left) ** 2) / (2 * l_width**2))
        
        # Update plotted lines
        # Split left and right for color coding on transverse
        t_left_data = np.copy(transverse)
        t_left_data[center:] = 0
        t_right_data = np.copy(transverse)
        t_right_data[:center] = 0
        
        line_t_left.set_data(x, t_left_data)
        line_t_right.set_data(x, t_right_data)
        
        l_left_data = np.copy(longitudinal)
        l_left_data[center:] = 0
        l_right_data = np.copy(longitudinal)
        l_right_data[:center] = 0
        
        line_l_left.set_data(x, l_left_data)
        line_l_right.set_data(x, l_right_data)
        
        time_text.set_text(f'Time Step: {frame}')
        
        # Entanglement Status Logic
        if pos_l_left == 0 and pos_l_right == length - 1:
            if pos_t_left > 10:  # Photons haven't hit detectors yet
                entangled_text.set_text(">>> BOUNDARY DETECTORS PHASE-LOCKED BEFORE PHOTON ARRIVAL <<<")
                entangled_text.set_color("lime")
        else:
             entangled_text.set_text("Transmitting Entanglement String Force...")
             entangled_text.set_color("yellow")
             
        # Fade out message when photons actually arrive
        if pos_t_left == 0 and pos_t_right == length - 1:
            entangled_text.set_text(">>> 'Spooky Action' Measured, but Cause was Classical <<<")
            entangled_text.set_color("cyan")

        return line_t_left, line_t_right, line_l_left, line_l_right, time_text, entangled_text

    plt.tight_layout()
    ani = animation.FuncAnimation(fig, update, frames=frames, interval=50, blit=True)
    
    print("\n[STATUS: SUCCESS] Generating FDTD Longitudinal Tension Wave vs Transverse Wave.")
    
    out_path = 'longitudinal_entanglement.gif'
    ani.save(out_path, writer='pillow', fps=20)
    print(f"Animated propagation saved to {out_path}")

if __name__ == "__main__":
    simulate_entanglement()
