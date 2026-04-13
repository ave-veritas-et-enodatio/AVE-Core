"""
Applied Vacuum Engineering (AVE) - Unified Physics Engine.
This core library maps discrete mass geometry and continuum LC network dynamics
onto a rigorous LC matrix. 
"""
from __future__ import annotations


from .grid import VacuumGrid
from .node import TopologicalNode
from .universal_operators import universal_impedance, universal_saturation, universal_reflection

__all__ = [
    'VacuumGrid', 'TopologicalNode',
    'universal_impedance', 'universal_saturation', 'universal_reflection'
]
