# R58 — G2 decisions 2 and 4 RULED; decision 1 re-shaped by measurement; the carrier fork surfaced as a deadlock (2026-08-25)

### ENTRY 2026-08-25-ruling-r58-g2-decisions

**Grant, verbatim (the rulings):**
- On decision 2 (observable set): *"A2: include"* — and, on re-presentation,
  *"ok here right?"* confirming it stands.
- On decision 4 (g as a verdict observable): *"yes, should be a unit test?"*
- On the A3 collapse check: *"go"*.
- On the scaffold: *"whats the ee circuit? actual map the schematic and
  analyze the circuit"* — answered by the A1 lane, below.
- Standing process instruction, same session: *"we should have every rec from
  you challeneged against my physical intuition."*

**Why this entry exists:** the P2-prereg firewall audit flagged as a BLOCKER
that decision 4 was being carried as RULED while the corpus (at `766d5179`)
still recorded it as an orchestrator recommendation — the ruling existed only
in chat. This entry closes that gap and records the same-day measurements that
re-shaped decision 1.

## §1 — RULINGS

- **Decision 2 — RULED: INCLUDE.** The P2 verdict set is S-profile railing
  **plus** the projected M/Q read on **two imposition representatives** (the
  equivalence-class receipt).
- **Decision 4 — RULED: YES**, with the unit-test question answered as a
  two-object split: the **extractor** is unit-testable and must be (its
  can-fire control: a configuration whose charge and mass distributions are
  identical must return **g = 1** — the anti-Dirac-smuggling test); the
  **verdict** (g = 2 from a solved state) is a frozen prereg criterion, not a
  unit test. Both are gated on §3's blocker.

## §2 — Decision 1, re-shaped by measurement (the A1 circuit lane)

The lane's headline ("both scaffold options are mirrors") is **WITHDRAWN** —
the swept parameter was a *transmission* coefficient, not a source reflection,
so every circuit label on it named a circuit the code never built. What
survives, and it re-shapes the decision:

1. **The ϖ-projection receipt CANNOT FIRE.** `M` is real (real-positive
   scatter weights; CONNECT a permutation), so a global phase on the drive
   multiplies the whole solution and the envelope reads `|v|` — the physics
   cannot move. Measured independently twice: **1.6e-12**. **Epic guard 8 is
   discharged for free by the reality of M**, the ϖ objection to
   source-termination evaporates, and decision 1's two options are equivalent
   on the axis that motivated the fork. **The orchestrator's proposed receipt
   was a tautology; it is deleted, not repaired.**
2. **The solver's docstring label is wrong**: it says "KUBC /
   voltage-clamped"; the code imposes the incident wave and **discards** the
   arriving one — `S_source = 0`, a **matched generator / TLM wave port**.
   Relabel unconditionally.
3. **Replace the dead receipt** with `exchange_amp/‖v‖`, which the module
   already computes; **normalize the idle criterion** (freeze
   `source_amp/‖v‖`; book `P_net` as a convergence receipt).
4. **G2 must additionally freeze what "injection-lock" means** — decision 1
   names a *drive* specification; the lane substituted node-current Norton
   injection on an uncut lattice, a different object, and the one that trips
   the `term=None` structural-zero branch.

## §3 — Blockers found (both verified verbatim at their anchors)

- **S1 — no machinery maps an HB solution to M, Q, or g.**
  `harmonic_balance_srs.py` is scalar-only by its own header (*"The
  T2/Cosserat channel is NOT wired in … no winding observable exists here"*).
  **This blocks decisions 2 AND 4** — both ruled, neither executable. The
  T2-channel wiring is therefore the gate on the ruled observables, not a
  follow-on. (Cost note: Stage 1 already built and merged the transverse
  graded scatter, so the remaining work is the join.)
- **S2 — the varactor kernel does not mix tones.** Measured: an undriven tone
  stays identically zero (1e-300) with two driven tones present on a strongly
  non-uniform field. Structural: `S` is a functional of the cycle-averaged
  envelope, so each tone solves an independent linear system and the coupling
  is **amplitude-only**, not phase-coherent. Whether a tone-ratio can carry a
  winding through amplitude-only coupling is an open question about the
  MACHINERY.
- **S4 — Picard degrades in P2's own regime** (intrinsic contraction
  0.97–0.99; moderate under-relaxation makes it worse). Anderson/DIIS depth 6
  converges in 66 outers where Picard at relax=1.0 fails at 150.

## §4 — ★ THE CARRIER DEADLOCK (S3) — Grant's open fork, now with measurements

Two ways to write the (2,3) onto the boundary:

| carrier | measured under decision 1's projection |
|---|---|
| **tone-ratio** (phase advances 2:3 in TIME, ports uniform — the phase-space reading) | **ANNIHILATED EXACTLY** — projected norm 0; the solve then reports `converged=True` on the **trivial zero state** |
| **spatial (p,q) texture** on the boundary loop (the real-space reading) | **SURVIVES** — residual common mode 1e-15.6 relative |

**The deadlock:** the only imposition that survives decision 1's projection is
the **real-space** one — which is exactly what **epic guard 3 polices** (the
(2,3) is a phase-space portrait; a naive real-space imposition is the
conflation class). Two live rulings pull opposite ways.

**The escape:** §2's deletion of the projection requirement makes the
phase-space carrier legal again. **Therefore decision 1 and the carrier fork
are COUPLED and cannot be ruled independently.**

**Mandatory regardless:** a **non-triviality gate** — "converged" is not
"non-zero" (the lane produced a converged trivial solution that would have
read as a result). Plus a per-(p,q) **aliasing margin receipt**: the multiples
(2L, 3L) alias exactly onto the uniform vector, so the representable-winding
window is bounded by L.

## §5 — Decision 3: DISTINCT, and a canon finding

The envelope fork and the storage/response contour fork are **DISTINCT** —
demoted honestly to "definitional, empirically un-separated" (the lane's
"decisive" receipt was **circular** and is withdrawn). A global rescale
A²→2A² acts identically on both criteria and preserves their ratio, so it
cannot generate the relative factor that defines the contour fork.

★ **BANKED FINDING — the two 0.9963 clocks are the SAME NUMBER, exactly.**
Solving canon's response condition without truncating —
`ΔS = 1 − √(1−A²) = α ⇒ A² = 2α − α²` — gives `S_resp = 1−α` while
`S_store = √(1−α)`, so `S_resp = S_store²` and both readouts equal
`√(1−α)` identically, for all α. **Canon's flagged "near-collision,
Δ = 1.4e-5" is a LINEARIZATION ARTIFACT of canon's own leading-order
truncation, not a coincidence between two contours.** Sympy-verified
(`simplify(response − storage) → 0`). Canon's practical guidance (*"the rate
alone cannot discriminate the contour — always carry the tag"*) is **correct
and strengthened** — the two are identical, not merely close — but its stated
basis needs re-scoping. **Routed as its own item.**

## §6 — SCX Phase-1: AGREE (independent-solver cross-check PASSES)

ngspice and the engine agree on all 10 distinct interior mode frequencies to
**≤ 4.85e-10 relative**, multiplicities exactly matched, interior mode count
62 vs 62. IMPLEMENTATION-VERIFICATION class — it says nothing about the
vacuum. `AGREE` was **not** the pre-registered expectation (the prereg
recorded DIVERGE as "substantial and expected"). PR #1016; the means-test
register's Class-B row can now be marked RUN.
