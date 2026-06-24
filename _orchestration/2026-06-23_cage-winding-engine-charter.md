# BUILD CHARTER — the cage⊗winding engine (the unbuilt electron)

**Created:** 2026-06-23 · orchestrator-tracked · **Status:** SCOPED, awaiting Grant go on Gate 0
**Origin:** the bottleneck behind #391 (the charge chord can't be measured) + the lattice-discovery epic ([`2026-06-23_lattice-discovery-program.md`](2026-06-23_lattice-discovery-program.md)). Corpus-grounded scope = workflow `wf9eo42m5`.

The electron is a Cosserat (2,3) **charge-winding** confined inside an A1 dilatation **mass-cage** (the Γ=−1 wall). **No built engine carries both** — and that gap is exactly where the AVE-distinct charge chord lives.

---

## Why it hasn't been built (grounded)

1. **Sector-separation is a derived firewall, not laziness.** `engine-capability-map.md:19` — "No single engine carries more than one or two [DOF]; that gap is the whole point of this map." Enforced by FW1: the A1 cage engine is a *scalar* field (∇×∇V≡0) → irrotational → **mathematically cannot host the winding** (`cavitation_flow.py:12`).
2. **The obvious coupling DETONATES.** The naive trilinear H_couple is an *indefinite* Hamiltonian (unbounded below) → the discrete dynamics **pump/runaway** (verified: H_photon, H_bel, |L_ω| all blow up; the H_bel −4107 precedent). A conservative coupling was only de-risked ~3 days ago (the skew-Hermitian circulator, PR #321).
3. **Deferred behind cheap wins, Grant-gated not blocked.** L3 mass-cage is built+GREEN; **L4/L5 (winding + self-formation) are UNBUILT** (no T4/T5 test files; all L4 matrix rows ⬜). The stop-point was deliberate.
4. **The two-grid reconciliation is the genuinely hard piece** — `engine-capability-map.md:71`: the continuum-scalar-FDTD grid the cage lives on vs the K4-tetrahedral grid the Cosserat ω lives on. "This grid-bridge is the hard part."

---

## Architecture — EXTEND `cosserat_field_3d.py` (not fresh, not master_equation)

One **shared K4-tetrahedral grid**, extending the winding host. It already carries: (a) the (2,3) winding ansatz (the charge DOF the scalar cage engine structurally can't host); (b) an energy-conserving velocity-Verlet integrator (damping=0, `:940`); (c) the **moving Γ=−1 impedance-boundary cage** as a TIR reflective short via an *exact harmonic LC-reactance Strang-split rotation* (`:953-989`); (d) the **α-separated** topological factor κ̃ = pq/(p+q) = 6/5 (`:99,:127`).

**The key unification:** rendering the cage as a Γ=−1 *boundary condition* (not a bulk c_eff(V) term) both (i) avoids the master-equation detonation-at-the-wall AND (ii) **is the same conservative-rotation form the circulator H_couple needs.** The chiral kernel κ̃=6/5 and the circulator coupling are *one object* — the cage primitive and the coupling are already the same machinery in the host.

- **DOF:** A1 dilatation (mass-cage = moving-impedance boundary) ⊥ Cosserat (2,3) ω (charge-winding = Beltrami helicity). Strict guard (`master-equation.md:20`): the winding is **never** wired into the breather's (V_inc,V_ref) phasor (the genesis-24 double-count) — already enforced at `:241-242`.
- **Coupling:** the conservative skew-Hermitian **circulator** — a unitary e^{−iHt} rotation on the *phase-space LC-quadrature* winding a=q+ip/ω (NOT the real-space rigid rotation L_ω — that coordinate distinction is why it passes where the locks detonated). No-pump by construction. NOT the energize-lock, NOT a shared phasor, NOT the trilinear potential.
- **Confinement:** the α-free Z_eff=√S route (Z_core=Z₀√S → 0Ω as A→1).

---

## Validate-on-known ladder (must pass IN ORDER before any chord is trusted)

- **GATE 0 — host α-cleanliness (the FIRST de-risk, the hard STOP):** add the α-leak import-guard (assert ALPHA/Q_TANK/ELECTRON not in globals), import **κ̃=6/5 NOT κ_chiral=α·κ̃**, reproduce the cold-Q≈30.8≠137 known-negative with the **Q-slot EMPTY**. *If the guard trips or 137 reappears, the build STOPS* — the host is α-contaminated.
- **Rung 0–2:** A1 compression mode (c_bulk=√2); cage precursor (c_eff stiffens c0·S^(−1/2)→∞); Γ=−1 wall crosses the −0.25 gate by A=0.95. ⚠ **RE-DERIVE the wall on the chiral K4/Cosserat stencil** before trusting — L3's ✅ is on a Cartesian 7-pt stencil with a hand-planted core + opposite native-stencil sign (A.1/A.2 base-crack; literal −1 unreachable, clipped ≈−0.45).
- **Rung 3–5:** mass = gapped bound breathing eigenmode (ω_cutoff>0; m_e is the *calibration anchor*, never an output); cold-Q reproduces 30.8≠137 (the chord-vs-echo decider, strict anti-substitution); persistence (EM-port-closed ⇒ Hermitian ⇒ Q→∞, consistency-class).
- **Rung 6 — integer charge (UNBUILT, GATE C.3 OPEN):** charge = closed Beltrami helicity, winding ±1. The direct H_bel integral currently returns ~18% of the p·q product at R≈7 and does **not** normalize to the integer — closing this on a finer lattice is real work.

---

## The chord it measures — scope to Observable-C, NOT the #391 echo

- **A — far-field F(r):** pure Coulomb echo. The validate-on-known gate, not a chord.
- **B — short-range departure (#391's "headline chord"):** **CANDIDATE-ECHO — do NOT scope to this.** QED produces the same short-range 1/r departure via vacuum-polarization/Uehling. (Confirms the audit's #391 verdict.)
- **★ C — co- vs anti-handed |F| MAGNITUDE asymmetry:** **THE PRIMARY CHORD DELIVERABLE.** A parity-clean medium gives equal magnitudes (SM-consistent genuine zero); AVE-distinct = a handedness-dependent magnitude split. Buildable on *posited* caged windings.
- **D — (q·ℓ_node) correction:** the corpus already deflates its quartic sibling to FORM-distinct/ECHO-magnitude (slope-4 asserted not derived; 6×6 eigensolve gives slope 2). Treat with caution.
- **Success criterion (corpus-adjudicated):** the engine "works" = demonstrates **α-free FORM-emergence** (the winding self-forms, the α-free Q emerges), NOT a magnitude readout. ⚠ But self-formation = L5 genesis = the *leaning-negative* keystone track. **Scope the chord to Observable-C on posited windings — do NOT gate it on solving genesis.**

---

## Risks

1. **PUMP (highest):** adopt ONLY the conservative circulator + a live conservation-canary that halts on H-drift. The trilinear precedent detonated.
2. **α-CONTAMINATION:** the host ships κ_chiral=α·κ̃ as DEFAULT — wiring that imports α and fakes a 137. MUST run α-free κ̃=6/5 (Gate 0).
3. **Two-grid scale / ℓ_node:** d_sat for a real electron is Compton-scale → imports m_e. Keep the chord **dimensionless** (Observable-C is a magnitude *ratio* — clean).
4. **Handedness is saturation-only** ⇒ the chord is a **DRIVEN/near-yield-regime** measurement, not cold. A cold null would be a wrong-regime artifact (ave-regime-phase-state-check).
5. **WRITHE-BLIND STENCIL (the false-negative trap):** a force kernel that reads only local bond directions sees identical multisets for L/R windings → false "no handedness" zero (the trap that killed optical-activity before). **The writhe-aware kernel does not exist — it is the real build cost.**
6. **POSITED-NOT-SELF-FORMED:** Rungs plant a saturated core (legitimate consistency-class posit); the self-formation chord-decider is the separate leaning-negative genesis track.

---

## Effort + first milestone

**Moderate-to-large, staged:** Gate 0 + Rungs 0–5 re-validation on the extended host ≈ 1–2 sessions (wiring + live-fire; the pieces exist behind default-OFF flags). Re-deriving the Γ=−1 wall on the chiral stencil (A.1/A.2) ≈ 1–2 sessions. **Observable-C with the writhe-aware force kernel + the H_bel integral (the real cost) ≈ 3–5 sessions** — the writhe-aware kernel is the main new build.

**FIRST MILESTONE (Gate 0 + Rung 4):** add the α-leak guard, import κ̃=6/5, turn the moving-Γ=−1 boundary ON, re-run `test_l3_mass_cage.py` to reproduce cold-Q≈30.8≠137 with the Q-slot empty. Smallest validate-on-known proving the host is α-clean + the cage survives on the winding-host **before** any winding/coupling/chord work. Guard trips or 137 reappears → STOP.

**Recommendation:** EXTEND `cosserat_field_3d.py`. Start with Gate 0 (cheap, hard-STOP de-risk). The held PRs (#391/#390) do not block it.
