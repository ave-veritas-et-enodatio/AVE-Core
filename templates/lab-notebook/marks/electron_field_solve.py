"""Engine solve of the electron (2,3) soliton -> V (=div u, capacitive) and
|B| (=|omega|, inductive) fields, via the canonical CosseratField3D.
No hardcoded physics: geometry from ave.core.constants; operators from the engine."""
import time, numpy as np
from ave.topological.cosserat_field_3d import CosseratField3D
from ave.core.constants import PHI   # golden ratio (canonical)

nx = 40
R_grid = 8.0                              # Golden-Torus major in grid cells
scale = R_grid / (PHI / 2.0)              # ell_node = scale cells  (R = phi/2 ell_node)
R_init = scale * (PHI / 2.0)              # = R_grid
r_init = scale * ((PHI - 1.0) / 2.0)      # = R_grid / phi^2  (R/r = phi^2)

t0 = time.time()
s = CosseratField3D(nx, nx, nx, dx=1.0, use_saturation=True)
s.initialize_electron_2_3_sector(R_target=R_init, r_target=r_init)
res = s.relax_to_ground_state(max_iter=1500, tol=1e-8, initial_lr=1e-3, verbose=False)
print("converged", res.get("converged"), "iters", res.get("iterations"),
      "E", res.get("final_energy"), "wall_s", round(time.time() - t0, 1))

u = np.asarray(s.u); om = np.asarray(s.omega)
strain = np.asarray(s.compute_strain())                       # (nx,nx,nx,3,3), K4-tetrahedral
divu = strain[..., 0, 0] + strain[..., 1, 1] + strain[..., 2, 2]   # V <- div u
Bmag = np.linalg.norm(om, axis=-1)                            # |B| <- |omega|
uabs = np.linalg.norm(u, axis=-1)                             # |u| (alt V candidate)
edens = np.asarray(s.energy_density())                        # capacitive+inductive energy
c = nx // 2
np.savez('/tmp/efield_solve.npz',
         V_xy=divu[:, :, c], V_xz=divu[:, c, :], V_yz=divu[c, :, :],
         B_xy=Bmag[:, :, c], B_xz=Bmag[:, c, :], B_yz=Bmag[c, :, :],
         U_xy=uabs[:, :, c], U_xz=uabs[:, c, :], U_yz=uabs[c, :, :],
         E_xy=edens[:, :, c], E_xz=edens[:, c, :], E_yz=edens[c, :, :],
         R_grid=R_grid, r_grid=r_init, nx=nx, ellnode_cells=scale)
print("|u| max", round(uabs.max(), 4), " |u| std xy/xz/yz=",
      [round(uabs[:, :, c].std(), 4), round(uabs[:, c, :].std(), 4), round(uabs[c, :, :].std(), 4)])
print("ell_node =", round(scale, 3), "cells ; R=%.2f r=%.2f cells" % (R_init, r_init))
print("|B| max", round(Bmag.max(), 4), " |div u| max", round(np.abs(divu).max(), 4))
print("slice std  V[xy,xz,yz]=", [round(divu[:, :, c].std(), 4), round(divu[:, c, :].std(), 4), round(divu[c, :, :].std(), 4)],
      " B[xy,xz,yz]=", [round(Bmag[:, :, c].std(), 4), round(Bmag[:, c, :].std(), 4), round(Bmag[c, :, :].std(), 4)])
