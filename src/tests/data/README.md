# Test reference data

- `a2be127d_omega_ref.npz` — ω-engine reference trajectory for the R1-1 default-ω-path
  regression test (`test_k4_quaternion_storage.py::test_r1_1_omega_path_reference`).
  Generated on commit `a2be127d` (merge #1064) with an 8³ grid, seeded random `u0`/`w0`
  (rng 20261009, amplitude 1e-4), via `CosseratField3D.step()`. Arrays: `u0`, `w0`, `dt`,
  `dt3`, `E0`; 10 default-dt steps (`u_def`/`om_def`/`ud_def`, PML=0, damping=0),
  10 explicit fixed-dt steps (`u_fix`/`om_fix`/`ud_fix`, same dt), and 10 steps with
  PML=4/damping=0.05 (`u_pml`/`om_pml`/`ud_pml`). Default-dt and fixed-dt cases are
  bit-identical by construction — the `omega_path_dt_perturb` mutant (dt·(1+1e-12) in the
  ω branch) breaks this equality and the exact-array comparison against the reference.
