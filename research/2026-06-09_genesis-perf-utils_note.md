# Genesis performance utilities (2026-06-09)

**What.** Two reusable library modules under `src/ave/utils/` + one benchmark.
`genesis_parallel_runner.py` fans the independent genesis matrix (arms × fracs ×
run-length-doublings) across cores; `fast_winding_extractor.py` is a NumPy-
vectorized twin of the graft-v2 ω-carrier (2,3) extractor.

**Why.** The wall-clock sinks are not the engine step (N=32 step ≈ 1.4 ms). They
are (a) SEQUENTIAL arm execution (`crystal_graft_v2_run.full_run` runs e_main /
e_chir / e_null serially though they are independent) and (b) the PYTHON-LOOP
winding extractor (per-angle `arctan2` / `_interp_vec` calls at every checkpoint
× arm × frac). No physics changed; only how fast the EXISTING measurement runs.

**Measured (this session, N=52, 14-core macOS, py3.11).**
- Extractor: 62.03 ms/call → 2.49 ms/call = **24.9×**, equivalence gate
  **bit-identical** (max|Δ| = 0.00e+00) on planted-(2,3) / null / random.
- Parallel runner: 6 × 10 s dummy = 60.02 s serial → 10.14 s parallel = **5.9×**;
  serial == parallel (determinism preserved, same seed ⇒ same result).

**float32 REJECTED.** The same ω field feeds the conservation canaries (H drift,
|L_ω| secular slope) at the 1e-3 level; an f32 extractor would both miss the
1e-12 equivalence gate and desync the energy ledger. The extractor stays float64.
