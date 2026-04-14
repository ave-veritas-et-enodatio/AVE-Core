import numpy as np
import matplotlib.pyplot as plt
import os

from ave.core.constants import D_PROTON
from ave.solvers.topology_optimizer import TopologicalOptimizer

R_CRUCIBLE = 150.0 * D_PROTON  
K_CRUCIBLE = 1000.0  

def calculate_principal_axes(coords):
    center = np.mean(coords, axis=0)
    shifted = coords - center
    I_tensor = np.zeros((3, 3))
    for i in range(len(coords)):
        r = shifted[i]
        r2 = np.dot(r, r)
        I_tensor += r2 * np.eye(3) - np.outer(r, r)
    eigenvalues, _ = np.linalg.eigh(I_tensor)
    return sorted(eigenvalues)

def plot_time_lapse(coords_t0, coords_t1, coords_t2, A_NUCLEONS, title, filename):
    fig = plt.figure(figsize=(18, 6))
    
    stages = [
        (coords_t0, "T=0: Pre-Quench Initialization"),
        (coords_t1, "T=50%: Topological Annealing"),
        (coords_t2, "T=100%: Deep Quench Structural Matrix")
    ]
    
    for idx, (flat_c, subtitle) in enumerate(stages):
        ax = fig.add_subplot(1, 3, idx+1, projection='3d')
        c3d = flat_c.reshape((A_NUCLEONS, 3))
        
        # Color coding: Stage 1 (Raw Void) -> Stage 2 (Condensing) -> Stage 3 (Crystallized)
        color = 'grey' if idx == 0 else ('orange' if idx == 1 else 'red')
        alpha_v = 0.5 if idx == 0 else 0.9
        
        ax.scatter(c3d[:,0], c3d[:,1], c3d[:,2], c=color, s=80, alpha=alpha_v, edgecolor='black')
        
        # Crucible wireframe
        u = np.linspace(0, 2 * np.pi, 20)
        v = np.linspace(0, np.pi, 20)
        x_s = R_CRUCIBLE * np.outer(np.cos(u), np.sin(v))
        y_s = R_CRUCIBLE * np.outer(np.sin(u), np.sin(v))
        z_s = R_CRUCIBLE * np.outer(np.ones(np.size(u)), np.cos(v))
        ax.plot_wireframe(x_s, y_s, z_s, color='blue', alpha=0.03)
        
        ax.set_xlim(-R_CRUCIBLE*1.1, R_CRUCIBLE*1.1)
        ax.set_ylim(-R_CRUCIBLE*1.1, R_CRUCIBLE*1.1)
        ax.set_zlim(-R_CRUCIBLE*1.1, R_CRUCIBLE*1.1)
        ax.set_title(subtitle, fontsize=13)
        ax.axis('off')
        
    fig.suptitle(title, fontsize=16, fontweight='bold', y=0.98)
    plt.tight_layout()
    plt.savefig(filename, dpi=300, bbox_inches='tight')
    plt.close()

def run_stage_1_helium():
    print("\n--- STAGE 1: Helium-4 Generation from Unstructured Void ---")
    
    A_NUCLEONS = 4
    np.random.seed(42)
    node_masses = [1.007, 1.007, 1.008, 1.008]
    node_charges = [1.0, 1.0, 0.0, 0.0]
    
    r_rand = R_CRUCIBLE * 0.9 * np.cbrt(np.random.rand(A_NUCLEONS))
    theta_rand = np.arccos(2 * np.random.rand(A_NUCLEONS) - 1)
    phi_rand = 2 * np.pi * np.random.rand(A_NUCLEONS)
    
    x_0 = r_rand * np.sin(theta_rand) * np.cos(phi_rand)
    y_0 = r_rand * np.sin(theta_rand) * np.sin(phi_rand)
    z_0 = r_rand * np.cos(theta_rand)
    
    initial_flat = np.column_stack((x_0, y_0, z_0)).flatten()
    
    opt = TopologicalOptimizer(
        node_masses=node_masses, 
        interaction_scale='nuclear', 
        node_charges=node_charges,
        boundary_radius=R_CRUCIBLE,
        boundary_k=K_CRUCIBLE
    )
    
    final_coords, _, history = opt.quench(
        initial_coords=initial_flat,
        T=400.0, 
        stepsize=20*D_PROTON,
        niter=200,
        options={'maxiter': 500, 'ftol': 1e-6, 'disp': False},
        record_history=True
    )
    
    t0 = initial_flat.reshape((A_NUCLEONS, 3))
    t1 = history[len(history)//2] if len(history) > 0 else t0
    t2 = final_coords
    
    prince = calculate_principal_axes(t2)
    slicer = 3.0 * (prince[0] * prince[1] * prince[2])**(1.0/3.0) / (prince[0] + prince[1] + prince[2])
    print(f"[*] Isotropy Index ($I_{{iso}}$) => {slicer:.4f} (1.0 = Alpha Tetrahedron)")
    
    plot_time_lapse(t0, t1, t2.flatten(), A_NUCLEONS, 
                    title="Stage 1: Vacuum-to-Helium Alpha Synthesis ($N=4$)",
                    filename="assets/sim_outputs/alchemist_forge_stage1_He.png")

def run_stage_2_oxygen():
    print("\n--- STAGE 2: Oxygen-16 Generation from Helium-4 Buffers ---")
    
    A_NUCLEONS = 16
    np.random.seed(111)
    
    # Oxygen 16 = 8 protons, 8 neutrons = 4 Alphas
    node_masses = [1.007, 1.007, 1.008, 1.008] * 4
    node_charges = [1.0, 1.0, 0.0, 0.0] * 4
    
    N_ALPHAS = 4
    ALPHA_RADIUS = 3.0 * D_PROTON  
    alpha_base = np.array([[1, 1, 1], [-1, -1, 1], [-1, 1, -1], [1, -1, -1]]) * (ALPHA_RADIUS / np.sqrt(3))
    
    initial_coords = []
    for i in range(N_ALPHAS):
        r_rand = R_CRUCIBLE * 0.7 * np.cbrt(np.random.rand())
        theta_rand = np.arccos(2 * np.random.rand() - 1)
        phi_rand = 2 * np.pi * np.random.rand()
        cx, cy, cz = r_rand * np.sin(theta_rand) * np.cos(phi_rand), r_rand * np.sin(theta_rand) * np.sin(phi_rand), r_rand * np.cos(theta_rand)
        
        rot_angles = np.random.rand(3) * 2 * np.pi
        sa, ca = np.sin(rot_angles), np.cos(rot_angles)
        Rx = np.array([[1, 0, 0], [0, ca[0], -sa[0]], [0, sa[0], ca[0]]])
        Ry = np.array([[ca[1], 0, sa[1]], [0, 1, 0], [-sa[1], 0, ca[1]]])
        Rz = np.array([[ca[2], -sa[2], 0], [sa[2], ca[2], 0], [0, 0, 1]])
        rot_matrix = Rz @ Ry @ Rx
        
        alpha_rotated = alpha_base @ rot_matrix.T
        initial_coords.extend(alpha_rotated + np.array([cx, cy, cz]))
        
    initial_flat = np.array(initial_coords).flatten()
    
    opt = TopologicalOptimizer(
        node_masses=node_masses, 
        interaction_scale='nuclear', 
        node_charges=node_charges,
        boundary_radius=R_CRUCIBLE,
        boundary_k=K_CRUCIBLE
    )
    
    final_coords, _, history = opt.quench(
        initial_coords=initial_flat,
        T=800.0, 
        stepsize=6*D_PROTON,
        niter=150,
        options={'maxiter': 500, 'ftol': 1e-6, 'disp': False},
        record_history=True
    )
    
    t0 = initial_flat.reshape((A_NUCLEONS, 3))
    t1 = history[len(history)//2] if len(history) > 0 else t0
    t2 = final_coords
    
    prince = calculate_principal_axes(t2)
    slicer = 3.0 * (prince[0] * prince[1] * prince[2])**(1.0/3.0) / (prince[0] + prince[1] + prince[2])
    print(f"[*] Isotropy Index ($I_{{iso}}$) => {slicer:.4f} (1.0 = Rigid Lattice)")
    
    plot_time_lapse(t0, t1, t2.flatten(), A_NUCLEONS, 
                    title="Stage 2: Helium-to-Oxygen Hierarchical Synthesis ($N_{He}=4$)",
                    filename="assets/sim_outputs/alchemist_forge_stage2_O16.png")

if __name__ == "__main__":
    run_stage_1_helium()
    run_stage_2_oxygen()
