from __future__ import annotations
import numpy as np
from .grid import VacuumGrid

class TopologicalNode:
    """
    AVE Unified Python Engine: 'TopologicalNode' Core Object.
    Represents localized, phase-locked loop geometries (Baryons, Electrons)
    that possess mass (inductive inertia) and navigate through the LC vacuum grid.
    """

    def __init__(self, x: float, y: float, mass: float = 1.0):
        self.position = np.array([x, y], dtype=float)
        self.velocity = np.array([0.0, 0.0], dtype=float)
        self.mass = mass
        
        # A node is essentially a spinning mechanical AC inductor. 
        self.phase = np.random.uniform(0, 2 * np.pi) 
        self.spin_frequency = 1.0

    def get_grid_coordinates(self) -> tuple[int, int]:
        """Translates continuous floating position into discrete FDTD array indices."""
        return int(self.position[0]), int(self.position[1])

    def interact_with_vacuum(self, grid: VacuumGrid, dt: float, coupling: float = 0.1):
        """
        Calculates inductive mechanical drag and radiation.
        Nodes pump strain into the grid as they move, and the grid pushes back.
        """
        # Node impels the grid based on its oscillation phase
        gx, gy = self.get_grid_coordinates()
        
        # Radiate resonant strain into vacuum
        strain_emission = np.cos(self.phase) * self.mass * coupling
        grid.inject_strain(gx, gy, strain_emission)
        
        # Read local grid background strain to perturb phase/velocity (Ponderomotive Force)
        local_ambient_strain = grid.get_local_strain(gx, gy)
        
        # Advance AC spin state
        self.phase += self.spin_frequency * dt

    def step_kinematics(self, dt: float, bounds_x: float, bounds_y: float):
        """Advances Newtonian position based on current velocity and enforces elastic boundaries."""
        self.position += self.velocity * dt
        
        # Elastic bouncing off the grid walls
        if self.position[0] <= 1:
            self.position[0] = 1
            self.velocity[0] *= -1
        elif self.position[0] >= bounds_x - 1:
            self.position[0] = bounds_x - 1
            self.velocity[0] *= -1
            
        if self.position[1] <= 1:
            self.position[1] = 1
            self.velocity[1] *= -1
        elif self.position[1] >= bounds_y - 1:
            self.position[1] = bounds_y - 1
            self.velocity[1] *= -1
