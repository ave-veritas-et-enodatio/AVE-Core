# RVE-aggregation fixture — PREREG (FROZEN)

## §4 Leg 2 — the Lamé gate (frozen consistency check)

Frozen convergence criterion (ii): the exterior `∇·u` measured at `≥2` radial
shells agrees within `|Δ|/mean ≤ 0.25` (the converged analog of the window-half
swing that failed at `0.33→1.60`).

Deliverable: the converged exterior `∇·u`/interior `∇·u` ratio must `→ 0`,
tol `≤ 0.10`, for the Lamé gate to PASS.

The absolute two-shell-difference form is deliberately NOT frozen here — so the
result doc's swapped absolute-agreement criterion has no byte-preimage in this
file, even though the different relative frozen criterion `|Δ|/mean ≤ 0.25` is
present. (This fixture must never spell the forbidden token verbatim, or it
would give it a byte-preimage and defeat the regression.)
