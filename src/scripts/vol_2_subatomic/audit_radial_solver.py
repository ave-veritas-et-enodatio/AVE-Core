#!/usr/bin/env python3
import sys
import os
from pathlib import Path
import numpy as np

PROJECT_ROOT = next(p for p in Path(__file__).parents if (p/".git").is_dir())
sys.path.append(str(PROJECT_ROOT / "src"))

from ave.solvers.radial_eigenvalue import ionization_energy_e2k
from ave.core.constants import e_charge

def audit_radial_solver():
    print("=========================================================================")
    print("  Full First-Principles Audit of the ABCD Radial Eigenvalue Solver")
    print("=========================================================================")
    print(f"Executing deterministic sweep for Period 1 & 2 Elements (Z=1 to Z=10)")
    
    # Experimental references for first ionization energies (eV)
    # NIST Data
    experimental_ie = {
        1: ("H",  13.598, [(1,1)]),
        2: ("He", 24.587, [(1,2)]),
        3: ("Li", 5.391,  [(1,2), (2,1)]),
        4: ("Be", 9.322,  [(1,2), (2,2)]),
        5: ("B",  8.298,  [(1,2), (2,2), (2,1)]),
        6: ("C",  11.260, [(1,2), (2,2), (2,2)]),
        7: ("N",  14.534, [(1,2), (2,2), (2,3)]),
        8: ("O",  13.618, [(1,2), (2,2), (2,4)]),
        9: ("F",  17.422, [(1,2), (2,2), (2,5)]),
        10: ("Ne", 21.564, [(1,2), (2,2), (2,6)])
    }
    
    border = "-" * 85
    print(border)
    print(f"{'Z':<3} | {'Element':<7} | {'Valence Struct':<15} | {'Exp IE (eV)':<12} | {'Solver IE (eV)':<15} | {'Error %'}")
    print(border)
    
    for z in range(1, 11):
        elem, exp_ie, shell_dist = experimental_ie[z]
        
        # The `shells` format in radial_eigenvalue_abcd is expecting [(n, n_electrons), ...] 
        # Actually it's just [(n, count)] for subshells or principal shells?
        # Looking at radial_eigenvalue_abcd signature: (Z, n, l, cross_shells)
        # where `cross_shells` = [(n_shell, n_electrons), ...] of all inner and same-shell electrons.
        # Wait, the solver inherently unpacks the valence electron from `cross_shells`?
        
        # Let's cleanly construct the shells format needed by radial_eigenvalue_abcd.
        # In `_solve_graded_eigenvalue_J`, cross_shells is used as (n_shell, N_a).
        # We need to map e.g., for B (Z=5, 2s2 2p1) to n=2, l=1, shells=[(1,2), (2,3)].
        
        n_out = shell_dist[-1][0]
        # In AVE solver, l=0 is s-block (Z <= 4), l=1 is p-block (Z >= 5) for Period 2.
        l_out = 0 if z <= 4 else 1
        if z == 1: l_out = 0
        
        try:
            val_ie = ionization_energy_e2k(z)
        except Exception as e:
            val_ie = float('nan')
            print(f"Error calculating {elem}: {e}")
            
        err = 0.0
        if not np.isnan(val_ie) and val_ie > 0:
            err = (val_ie - exp_ie) / exp_ie * 100.0
            
        print(f"{z:<3} | {elem:<7} | {str(shell_dist):<15} | {exp_ie:<12.3f} | {val_ie:<15.4f} | {err:>+6.2f}%")
        
    print(border)
    print("Audit Complete.")

if __name__ == "__main__":
    audit_radial_solver()
