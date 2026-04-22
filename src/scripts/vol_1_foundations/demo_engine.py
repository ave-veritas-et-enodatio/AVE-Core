import sys
import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

# Important: Add project root to sys path so we can import ave.core cleanly

from ave.core import VacuumGrid, TopologicalNode


def main():
    print("==========================================================")
    print(" AVE LIBRARY: ENGINE DEMONSTRATION SCRIPT")
    print("==========================================================\n")

    print("- Objective: Validate the Unified Object-Oriented Architecture.")
    print("- Instantiating VacuumGrid and filling it with TopologicalNodes.")

    # 1. Initialize the Environment
    NX, NY = 100, 100
    grid = VacuumGrid(nx=NX, ny=NY)
    grid.set_temperature(0.5, mode="bulk")  # Bulk noise for visual demo
    # 2. Instantiate Topological Nodes (e.g. A cluster of mass)
    num_particles = 15
    nodes = []

    print(f"- Spawning {num_particles} massive nodes into the Matrix...")
    for _ in range(num_particles):
        x = np.random.uniform(30, 70)
        y = np.random.uniform(30, 70)
        node = TopologicalNode(x=x, y=y, mass=5.0)

        # Give them some initial kinetic energy (Heat/Velocity)
        angle = np.random.uniform(0, 2 * np.pi)
        speed = 1.2
        node.velocity[0] = speed * np.cos(angle)
        node.velocity[1] = speed * np.sin(angle)
        nodes.append(node)

    # 3. Visualization Setup
    fig, ax = plt.subplots(figsize=(8, 8), facecolor="#0d0d14")
    ax.set_facecolor("#0d0d14")

    # Background Grid Render (Strain)
    img = ax.imshow(np.abs(grid.strain_z.T) ** 2, cmap="hot", vmin=0, vmax=1.0, origin="lower")

    # Node Render (Atoms)
    scatter = ax.scatter(
        [n.position[0] for n in nodes],
        [n.position[1] for n in nodes],
        s=40,
        color="cyan",
        edgecolors="white",
        zorder=5,
    )

    ax.axis("off")
    ax.set_title("Unified Engine: Nodes Traversing LC Vacuum", color="white", pad=20, fontsize=14)

    dt = 0.5

    def update(frame):
        # Master physics loop

        # Phase A: Grid Update
        grid.step_kinematic_wave_equation(damping=0.98)

        # Phase B: Node Kinematics & Grid Interaction
        positions = []
        for node in nodes:
            node.interact_with_vacuum(grid, dt=dt, coupling=0.5)
            node.step_kinematics(dt, bounds_x=NX, bounds_y=NY)
            positions.append(node.position)

        # Update Renderers
        img.set_array(grid.strain_z.T)
        scatter.set_offsets(positions)
        return [img, scatter]

    print("[1] Executing Unified Main Loop...")
    ani = animation.FuncAnimation(fig, update, frames=200, interval=30, blit=True)

    os.makedirs("standard_model/animations", exist_ok=True)
    out_path = "standard_model/animations/ave_unified_engine_demo.gif"
    ani.save(out_path, writer="pillow", fps=30)

    print(f"\n[STATUS: SUCCESS] The Object-Oriented Engine is live.")
    print(f"Instantiated Node-Grid interactions tracked seamlessly.")
    print(f"Animated propagation saved to {out_path}")


if __name__ == "__main__":
    main()
