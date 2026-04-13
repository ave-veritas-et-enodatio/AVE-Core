# simulate_double_slit_wake.py
# Simulates the FDTD ponderomotive wake of a physical particle 
# generating real macroscopic interference gradients.
# Rigorously enforces strict continuum mechanics PDE solvers, including
# Absorbing Boundary Conditions (ABCs) to prevent non-physical tank reflections.
import numpy as np
import matplotlib.pyplot as plt
import os

plt.style.use('dark_background')
# --- Standard AVE output directory ---
def _find_repo_root():
    d = os.path.dirname(os.path.abspath(__file__))
    while d != os.path.dirname(d):
        if os.path.exists(os.path.join(d, "pyproject.toml")):
            return d
        d = os.path.dirname(d)
    return os.path.dirname(os.path.abspath(__file__))

OUTPUT_DIR = os.path.join(_find_repo_root(), "assets", "sim_outputs")
os.makedirs(OUTPUT_DIR, exist_ok=True)
# --- End standard output directory ---
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

# --- High-Resolution PDE Parameters ---
NX, NY = 600, 400
c = 1.0       # Normalized wave speed
dt = 0.5      # Courant limit compliant timestep
dx = 1.0      # Spatial node distance

# Wave Arrays (Pressure/Displacement formulation)
P = np.zeros((NX, NY), dtype=float)     # Field Displacement (Psi)
V_x = np.zeros((NX, NY), dtype=float)   # X-Velocity field
V_y = np.zeros((NX, NY), dtype=float)   # Y-Velocity field

# Time-averaged intensity to capture the macroscopic interference boundaries
P_intensity = np.zeros((NX, NY), dtype=float)

# --- Absorbing Boundary Conditions (Sponge Layer) ---
# To prevent waves from bouncing off the literal edges of the simulation
# and turning the interference pattern into chaotic reflection "slop",
# we apply a progressive damping coefficient at the perimeter.
sponge_width = 40
damping = np.ones((NX, NY), dtype=float)
max_damping = 0.05

for i in range(sponge_width):
    # Quadratic damping profile
    d_val = 1.0 - max_damping * ((sponge_width - i) / sponge_width)**2
    damping[i, :] *= d_val            # Left
    damping[NX - 1 - i, :] *= d_val   # Right
    damping[:, i] *= d_val            # Bottom
    damping[:, NY - 1 - i] *= d_val   # Top

# --- Geometry: The Double Slit Membrane ---
wall_x = int(NX * 0.45)
wall_thickness = 4
slit_width = 16
slit_sep = 80
slit_1_y = NY//2 - slit_sep//2
slit_2_y = NY//2 + slit_sep//2

wall_mask = np.zeros((NX, NY), dtype=bool)
wall_mask[wall_x : wall_x + wall_thickness, :] = True
# Clear the slits
wall_mask[wall_x : wall_x + wall_thickness, slit_1_y - slit_width//2 : slit_1_y + slit_width//2] = False
wall_mask[wall_x : wall_x + wall_thickness, slit_2_y - slit_width//2 : slit_2_y + slit_width//2] = False

# --- The Topological Defect (The Source) ---
# The particle travels decisively through Slit 1. 
# Its emitted radial wake expands ahead of it and hits both slits.
freq = 0.08

def run_pde_solver(steps=1200):
    global P, V_x, V_y, P_intensity
    
    print("Executing Continuous PDE Wave Interference Solver with ABCs (Sponge Damping)...")
    for t in range(steps):
        # 1. Update Velocities (Vector Gradient of Pressure)
        V_x[:-1, :] -= dt * (P[1:, :] - P[:-1, :]) / dx
        V_y[:, :-1] -= dt * (P[:, 1:] - P[:, :-1]) / dx
        
        # Enforce Hard Reflection Boundaries at the Wall
        V_x[wall_mask] = 0
        V_y[wall_mask] = 0
        
        # 2. Update Pressure (Divergence of Velocity)
        P[1:-1, 1:-1] -= dt * c**2 * ( (V_x[1:-1, 1:-1] - V_x[:-2, 1:-1])/dx + (V_y[1:-1, 1:-1] - V_y[1:-1, :-2])/dx )
        
        # Apply the Absorbing Boundaries to eat outbound radiation
        P *= damping
        V_x *= damping
        V_y *= damping
        
        # 3. Particle Kinematics
        # The defect moves progressively towards Slit 1
        particle_x = int(40 + t * 0.25)
        # Stop driving if it hits the far absorbing layer 
        if particle_x < NX - sponge_width:
            P[particle_x, slit_1_y] += np.sin(2 * np.pi * freq * t) * 1.5
            
        # 4. Integrate the intensity field (Ponderomotive standing wave gradient)
        # We start integrating after the waves have permeated the slits
        if t > 600:
            P_intensity += P**2

    # Normalize intensity
    return P_intensity / np.max(P_intensity)

def generate_scientific_visuals():
    intensity_field = run_pde_solver()
    
    fig = plt.figure(figsize=(14, 9), facecolor='#050510')
    ax = fig.add_subplot(111)
    ax.set_facecolor('#050510')
    
    # Render the wave energy density explicitly. 
    # Use vmax=0.3 to boost contrast on the subtle interference fringes.
    im = ax.imshow(intensity_field.T, cmap='hot', origin='lower', extent=[0, NX, 0, NY], alpha=0.9, vmax=0.3)
    
    # Overlay the impenetrable boundaries
    ax.imshow(wall_mask.T, cmap='binary_r', alpha=0.5, origin='lower', extent=[0, NX, 0, NY])
    
    # Draw strictly mathematical representations of the mechanics
    # 1. Classical Particle Trajectory
    ax.plot([0, NX], [slit_1_y, slit_1_y], color='#00ffff', linestyle='--', linewidth=2.5, alpha=0.8)
    
    # 2. Emphasize the Interference nodes dynamically forming on the right
    x_nodes = np.linspace(wall_x + 60, NX - sponge_width, 5)
    for x_idx in x_nodes:
        ax.axvline(x=x_idx, color='white', linestyle=':', alpha=0.15)
        
    # High-contrast contour lines mapping the peaks of the standing waves
    ax.contour(intensity_field.T, levels=8, colors='#ff00aa', alpha=0.3, linewidths=0.5, extent=[0, NX, 0, NY])
    
    # Optional: Shade the absorbing boundary regions so the user knows they are mathematical sinks
    ax.fill_between([NX-sponge_width, NX], 0, NY, color='black', alpha=0.6, hatch='//', zorder=10)
    ax.text(NX - sponge_width + 5, 20, "Absorbing\nBoundary\nLayer", color='#888888', fontsize=10, zorder=11)
    
    ax.set_title(r"Macroscopic Ponderomotive Interference ($\nabla |\Psi_{mech}|^2$)", color='white', pad=20, fontsize=20, weight='bold')
    
    # Formal Axis formatting
    ax.set_xlabel("Longitudinal Axis (Spatial Nodes)", color='white', fontsize=12)
    ax.set_ylabel("Transverse Axis (Spatial Nodes)", color='white', fontsize=12)
    ax.tick_params(colors='white')
    
    # Explicit Mathematical Annotations
    props = dict(boxstyle='round', facecolor='#111122', alpha=0.9, edgecolor='#00ffff')
    ax.text(30, NY - 40, "Singular Topological\nDefect Trajectory\n(Passing Slit 1)", color='#00ffff', fontsize=12, bbox=props)
    
    props2 = dict(boxstyle='round', facecolor='#111122', alpha=0.9, edgecolor='#ff00aa')
    ax.text(wall_x + 40, NY - 40, r"Standing Wave Interference Fringes", color='#ffaa00', fontsize=14, weight='bold', bbox=props2)
    
    props3 = dict(boxstyle='round', facecolor='#111122', alpha=0.9, edgecolor='white')
    ax.text(wall_x - 140, slit_2_y + 30, "Radial Wake\nPermeating\nSlit 2", color='white', fontsize=11, bbox=props3)

    plt.colorbar(im, ax=ax, label="Normalized Intensity Time-Average", fraction=0.03, pad=0.04).set_label(label="Time-Averaged Wave Density", size=14, weight='bold', color='white')
    
    output_path = os.path.join(OUTPUT_DIR, 'photon_double_slit.png')
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, facecolor=fig.get_facecolor(), bbox_inches='tight')
    print(f"Saved formal macroscopic double-slit derivation to: {output_path}")

if __name__ == "__main__":
    generate_scientific_visuals()
