import pytest
import numpy as np
from ave.regime_4_rupture.caustic_solver import AxiomaticCausticSolver
from ave.core.constants import E_YIELD, Z_0

def test_intensity_bounded():
    """
    Ensures that as ray optics tries to force infinite intensity (z -> 0),
    the solver correctly bounds E_field at or below E_YIELD,
    and the saturation parameter S stays >= 0.
    """
    solver = AxiomaticCausticSolver()
    
    # 1 Petawatt laser focused tightly
    initial_power = 1e15
    NA = 0.5
    
    # Run solver from macroscopic focus distance down to 1 femtometer
    res = solver.resolve_focal_intensity(
        initial_power=initial_power,
        numerical_aperture=NA,
        z_start=0.1,
        z_end=1e-15,
        num_steps=1000
    )
    
    # Verify no elements exceed E_YIELD
    assert np.all(res['E_field'] <= E_YIELD * 1.0001)
    
    # Verify S is bounded in [0, 1]
    assert np.all(res['S'] >= 0.0)
    assert np.all(res['S'] <= 1.0)
    
    # Power must monotonically decrease or stay flat due to reflection
    diffs = np.diff(res['power'])
    assert np.all(diffs <= 0.0)
    
    # The final transmitted power must drop significantly for an extreme focus
    assert res['power'][-1] < initial_power

def test_caustic_waist():
    """
    Confirms that at the closest approach to the zero-area geometric point,
    the reflection coefficient Gamma is driven towards 1.0 safely.
    """
    solver = AxiomaticCausticSolver()
    
    # Extreme power attempting to force z->0 geometric singularity
    initial_power = 1e18
    NA = 0.8
    
    res = solver.resolve_focal_intensity(
        initial_power=initial_power,
        numerical_aperture=NA,
        z_start=0.01,
        z_end=1e-20,
        num_steps=500
    )
    
    # Nearest focus is the last element
    final_gamma = res['Gamma'][-1]
    final_S = res['S'][-1]
    
    # As the area shrinks arbitrarily, reflection must approach complete (Gamma -> 1)
    assert final_gamma > 0.99
    
    # Saturation parameter approaches 0 (yielding)
    assert final_S < 0.05
    
    # E_field should be saturated exactly up to the limit
    E_max = np.max(res['E_field'])
    assert np.isclose(E_max, E_YIELD, rtol=1e-3)
