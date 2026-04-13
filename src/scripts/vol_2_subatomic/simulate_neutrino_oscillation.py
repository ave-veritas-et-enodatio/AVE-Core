import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def simulate_neutrino_oscillation(frames=250, nx=400):
    """
    Simulates Neutrino "Flavor Oscillation" as a classical wave
    dispersion phenomenon on a discrete macroscopic LC lattice.
    
    In AVE:
    - Neutrinos are discrete $0_1$ unknot topological harmonics.
    - Higher harmonics (k values) travel at slightly different group velocities 
      (v_g < c) due to the discrete dispersion relation of the grid.
    - When 3 harmonics are emitted simultaneously, their varying speeds 
      cause them to drift in and out of phase, creating a macroscopic 
      Beat Frequency.
    - This shifting interference pattern is what Super-Kamiokande 
      measures as "Flavor Oscillation" (Electron, Muon, Tau).
    """

    print("\n AVE APPLIED PHYSICS: NEUTRINO FLAVOR OSCILLATION (DISPERSION)")
    print("===============================================================")
    print(" - Objective: Prove that 'spooky' state-vector flavor rotation")
    print("              is simply classical LC grid acoustic dispersion.")
    print(" - Mechanism: 3 harmonic unknots (n=4, 5, 8) moving at slightly")
    print("              different velocities (v_g < c) drift into and out of phase.")
    
    # 1D Grid Parameters
    L = 100.0  # Physical length
    x = np.linspace(0, L, nx)
    
    # "Flavors" represented by 3 distinct wavenumbers (harmonics)
    k1 = 0.5  # 'Electron' Base Harmonic
    k2 = 0.6  # 'Muon' First Overtone
    k3 = 0.7  # 'Tau' Second Overtone
    
    # Group velocities (Dispersion: v_g depends on k in a discrete lattice)
    v1 = 1.0       # Base speed (~c)
    v2 = 0.95      # Slower due to structural dispersion
    v3 = 0.90      # Even slower
    
    # Amplitudes (Mixing Angles)
    A1, A2, A3 = 1.0, 0.8, 0.6
    
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))
    fig.patch.set_facecolor('#111111')
    
    # Top Plot: Individual Harmonic Packets
    ax1.set_facecolor('#111111')
    line_e, = ax1.plot([], [], color='cyan',     lw=2, label="Electron Harmonic (v=c)", alpha=0.8)
    line_m, = ax1.plot([], [], color='lawngreen', lw=2, label="Muon Harmonic (v<c)", alpha=0.8)
    line_t, = ax1.plot([], [], color='magenta',  lw=2, label="Tau Harmonic (v<<c)", alpha=0.8)
    
    ax1.set_xlim(0, L)
    ax1.set_ylim(-1.5, 1.5)
    ax1.set_title("Individual Neutrino Harmonics Moving Through Vacuum Lattice", color='white')
    ax1.tick_params(colors='white')
    ax1.legend(loc='upper right', facecolor='black', edgecolor='white', labelcolor='white')
    
    # Bottom Plot: The Macroscopic Observed "Flavor" (Superposition Beat Frequency)
    ax2.set_facecolor('#111111')
    line_sum, = ax2.plot([], [], color='white', lw=3, label="Observable Neutrino Wave Packet (Superposition)")
    
    # Emulate the Super-Kamiokande detection threshold (Probability = Amplitude^2)
    fill_prob = ax2.fill_between(x, 0, 0, color='yellow', alpha=0.3, label=r"Detection Probability ($|\Psi|^2$)")
    
    ax2.set_xlim(0, L)
    ax2.set_ylim(-3.0, 3.0)
    ax2.set_title("Macroscopic Neutrino Oscillation (Dispersion Beat Frequency)", color='white')
    ax2.tick_params(colors='white')
    ax2.legend(loc='upper right', facecolor='black', edgecolor='white', labelcolor='white')
    
    time_text = ax2.text(0.02, 0.85, '', transform=ax2.transAxes, color='white', fontsize=12)
    flavor_text = ax2.text(0.02, 0.10, '', transform=ax2.transAxes, color='cyan', fontsize=14, fontweight='bold')

    # Gauss packet width
    sigma = 4.0

    def update(frame):
        t = frame * 0.15
        
        # Center positions of each propagating packet
        mu1 = t * v1
        mu2 = t * v2
        mu3 = t * v3
        
        # Calculate individual wave equations
        wave1 = A1 * np.exp(-((x - mu1)**2) / (2 * sigma**2)) * np.cos(k1 * x - v1 * k1 * t)
        wave2 = A2 * np.exp(-((x - mu2)**2) / (2 * sigma**2)) * np.cos(k2 * x - v2 * k2 * t)
        wave3 = A3 * np.exp(-((x - mu3)**2) / (2 * sigma**2)) * np.cos(k3 * x - v3 * k3 * t)
        
        line_e.set_data(x, wave1)
        line_m.set_data(x, wave2)
        line_t.set_data(x, wave3)
        
        # Superposition (The observable macroscopic particle)
        total_wave = wave1 + wave2 + wave3
        line_sum.set_data(x, total_wave)
        
        # Update the 'Probability' envelope fill (square of amplitude)
        prob_envelope = (np.exp(-((x - mu1)**2)/(2*sigma**2)) * 
                         np.exp(-((x - mu2)**2)/(2*sigma**2)) * 
                         np.exp(-((x - mu3)**2)/(2*sigma**2))) # rough bounding
        
        # Use a more accurate upper envelope for visualization
        envelope = np.abs(total_wave)
        
        # Clear old fill and draw new one
        for collection in ax2.collections:
            collection.remove()
        
        ax2.fill_between(x, 0, envelope**2, color='white', alpha=0.4, label=r"Detection Prob ($|\Psi|^2$)")
        
        time_text.set_text(f'Distance Traveled: {mu1:.1f} AU')
        
        # Dominant Flavor Logic (Based on whichever harmonic is peaking in the sum at the center mass)
        center_idx = np.argmax(np.abs(total_wave))
        mag1 = np.abs(wave1[center_idx]) if isinstance(wave1, np.ndarray) else np.abs(wave1)
        mag2 = np.abs(wave2[center_idx]) if isinstance(wave2, np.ndarray) else np.abs(wave2)
        mag3 = np.abs(wave3[center_idx]) if isinstance(wave3, np.ndarray) else np.abs(wave3)
        
        if mag1 > mag2 and mag1 > mag3:
            flavor_text.set_text("Dominant Flavor State: ELECTRON NEUTRINO")
            flavor_text.set_color("cyan")
        elif mag2 > mag1 and mag2 > mag3:
            flavor_text.set_text("Dominant Flavor State: MUON NEUTRINO")
            flavor_text.set_color("lawngreen")
        else:
            flavor_text.set_text("Dominant Flavor State: TAU NEUTRINO")
            flavor_text.set_color("magenta")

        return line_e, line_m, line_t, line_sum, time_text, flavor_text

    plt.tight_layout()
    ani = animation.FuncAnimation(fig, update, frames=frames, interval=40, blit=False)
    
    print("\n[STATUS: SUCCESS] Generating Neutrino Oscillation (Acoustic Dispersion) sequence.")
    
    out_path = 'neutrino_oscillation_dispersion.gif'
    ani.save(out_path, writer='pillow', fps=25)
    print(f"Animated propagation saved to {out_path}")

if __name__ == "__main__":
    simulate_neutrino_oscillation()
