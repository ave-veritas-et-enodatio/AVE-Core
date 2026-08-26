# P2 engineering-scoping receipts (2026-08-25)

Preserved from the pre-G2 scoping lane. **Engineering parameters only** — the
lane was firewalled from reporting any verdict-bearing physics quantity, and
the firewall audit verified that boundary INTACT ("no S-profile, no S_min,
no railing statement, no g, no M/Q, no field content; every printed receipt is
convergence/cost only").

**What is here and why it was expensive to get:**
- `scale.py` / `scale24.out` — cost and sparsity vs lattice size; **max
  affordable L = 20**.
- `converge.py` / `converge.out` — outer fixed-point behaviour. **Outer
  iteration count is MESH-INDEPENDENT** (19 at relax=0.7 for every L from 2 to
  24). Mild engagement: any initial guess reaches the same fixed point.
- `accel.py` / `accel.out` — the strongly-engaged regime, which is **P2's own
  regime**: intrinsic contraction 0.97–0.99, plain Picard at relax=1.0 FAILS,
  moderate under-relaxation makes it WORSE (tail ratio > 1), relax=0.3
  converges in 99 outers, **Anderson/DIIS depth 6 converges in 66**.
- `imposition_proto.py` — the winding-imposition interface, **prototyped and
  run green at L=4**; no solver change required (the shipped `Termination`
  already accepts arbitrary per-tone per-port phasors).
- `comb.py`, `loopcheck.py` — boundary-loop coordinates and the aliasing
  check.
- `a1_scaffold_schematic.txt` — the A1 lane's circuit schematic.

**Two measured facts that became load-bearing** (both recorded in R58 §4):
1. A per-port **uniform** drive is annihilated *exactly* by decision-1's
   common-mode projection, and the solve then reports `converged=True` **on
   the trivial zero state** — hence the mandatory non-triviality gate
   ("converged" is not "non-zero").
2. `⟨exp(i(2φ+3ψ))⟩ = 0` for every L tested: the multiples (2L, 3L) alias
   **exactly** onto the uniform vector, so the representable-winding window is
   bounded by L and each (p,q) needs a margin receipt.

**Multi-start sensitivity was tested at MILD engagement only** — not at strong
engagement, "which is where a solution FAMILY would show." The P2 prereg must
mandate its own multi-start receipt there.
