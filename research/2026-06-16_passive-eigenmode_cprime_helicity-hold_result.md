# OPTION C′ — the NO-WORK Beltrami-helicity hold: BIN = NEGATIVE (earned)

> **🔴 RULE-12 DEMOTION (2026-06-16 — verify panel `w4wkm2erq`, tracker Phase 7; original verdict text below PRESERVED unedited).** The headline "BIN = NEGATIVE (earned)" / "keystone leans negative EARNED" is **RE-SCOPED** to: **the scalar-route is CLOSED-NEGATIVE; sector-cohabitation is UNTESTED.** The no-work H_bel hold was genuine (orthogonality `cos(g_perp,e)=1.86e-17`, full-Hamiltonian ramp 0.999×, NO pump — the conservativeness below stands) BUT C′ held a single **global SCALAR** (Beltrami helicity), and the electron charge is the **(2,3) integer PAIR** (`master-equation.md:20`: *"the unknot dilatation-mass **carrying** the (2,3) winding — two objects, not one"*). A single scalar cannot pin a two-integer winding, so the panel **RE-BINNED this DISQUALIFY-WRONG-OBJECT** — a method-artifact, not an earned keystone-negative. The durable verdict is therefore *"the scalar-hold route is CLOSED-negative; sector-cohabitation is UNTESTED,"* **NOT** "keystone leans negative earned." The original NEGATIVE-earned framing below is preserved per Rule 12 (substitution-not-retraction); read it through this re-scope.
>
> **STATUS:** OPTION C′ probe of the passive winding-protected electron eigenmode lane
> (prereg `2026-06-15_passive-eigenmode_prereg_FROZEN.md` + the C′ amendment §9.1 of
> `_orchestration/2026-06-15_passive-eigenmode-solve.md`, Grant-greenlit 2026-06-16). Branch
> `analysis/2026-06-15-eigenmode-heldbc`. **Result NOT banked — this is the implementer's
> mechanism result; the orchestrator adjudicates the bin + the chord/echo framing.**
>
> **BIN = NEGATIVE (EARNED, not pump-masked).** The NO-WORK H_bel constraint is genuinely
> energy-neutral (orthogonality residual machine-zero, full-Hamiltonian ramp 0.999× = the free
> ramp) — so unlike OPTION C (which DISQUALIFIED at 56× pump), C′ clears the DISQUALIFY bar and
> the negative is a real physics read. The negative lands on the **KEY DESIGN CHECK** the
> amendment §9.1 pre-registered as a possible finding: **the scalar H_bel is TOO COARSE to pin
> the (2,3) PAIR.** The charge is held to 1e-9, the breather persists (F1/F2 pass), but the
> (toroidal-2, poloidal-3) pair drifts off (2,3) identically to the hold-OFF run.

---

## §0 — What C′ tested (vs C)

| Axis | OPTION C (`held_bc_winding.py`) | OPTION C′ (`held_helicity_winding.py`) |
|:---|:---|:---|
| Held object | per-cell DIRECTOR TEMPLATE (real-space (2,3) phase pattern) | the conserved **H_bel = ∫ω·(∇×ω)dV** (corpus charge, single global scalar) |
| Mechanism | hard per-cell phase overwrite each step | NO-WORK correction ⊥ the ω-sector energy gradient (Gram-Schmidt + λ line-solve) |
| Energy ledger | **56× PUMP** (overwrites fight the free gradient flow) → DISQUALIFY | **0.999× = free ramp** (energy-neutral BY CONSTRUCTION) → conservative |
| Bin | DISQUALIFY (pump masks persistence) | **NEGATIVE (earned)** |

C is preserved intact (KEEP-BOTH / audit-trail). C′ is a new module + a new driver path
(`--hold-helicity`, `run_option_Cprime`); the C path (`--hold-winding`, `run_option_C`) stays
runnable for audit.

---

## §1 — The held charge (and the load-bearing spec-vs-code conflict)

🔴 **FLAG (load-bearing, flag-don't-fix — surfaced BEFORE scaffolding):** prereg §9.1 gives the
LITERAL formula `H_bel(omega) = sum(_beltrami_helicity(omega, dx)) * dx**3`. But the engine's
`cosserat_field_3d._beltrami_helicity` (`:450`) returns the **NORMALIZED handedness**
`h_local = ω·(∇×ω)/(|ω|·|∇×ω|) ∈ [−1,+1]` (doc 54_ §6), **not** the raw helicity density
`ω·(∇×ω)` the integral `∫ω·(∇×ω)dV` calls for. Measured on the planted (2,3) traveling seed
(N=26, R=5, r=2.5, dx=0.5):

- `sum(_beltrami_helicity)*dx³` = **137.19** — but **125.5 (91.5%) is VACUUM-CELL ARTIFACT**
  (cells where |ω|≈0, the `eps_h=1e-12` regularizer manufacturing spurious handedness); only 11.7
  comes from the shell. Its ∇_ω is stiff (‖grad‖≈5.6e6). The **137≈1/α resemblance is
  coincidental** (it tracks the box vacuum-cell count), NOT the corpus charge.
- `∫ω·(∇×ω)dV` (RAW) = **2.1e-4** — the verbatim corpus object (`master-equation.md`, two-"3"s
  block: *"charge = Beltrami helicity H_bel = ∫ω·(∇×ω)"*): smooth (‖grad‖≈0.71), scales s² in ω,
  robust 0.269 on the (1,1) Beltrami control. Small on the (2,3) plant because the **signed**
  helicity nearly cancels (shell density −5.1e-3, |density| integral 0.34 — structure present,
  sign-cancellation not absence).

**Resolution (per the brief: "§9.1 wins; flag the conflict, don't silently diverge"):** §9.1's
PROSE intent ("hold the conserved H_bel = ∫ω·(∇×ω), the corpus's actual charge") and its LITERAL
Python formula CONFLICT, because the named engine helper is normalized. **C′ holds the RAW
integral** (the object `master-equation.md` defines + §9.1's prose names), and records the
spec-literal normalized-sum each step for transparency. This conflict is surfaced to the
orchestrator, not silently resolved. *(See `held_helicity_winding.py` module header for the full
diagnostic block.)*

---

## §2 — The mechanism is sound: energy-neutral BY CONSTRUCTION (the C′ DISQUALIFY clearance)

`ave-conserved-vs-pumped` — the full-Hamiltonian witness (`eng_w.total_hamiltonian()`, NOT
`sum(ω²)` — the C false-positive guard-bug fixed in `86c1a641`):

| Witness | Value | Reading |
|:---|:---|:---|
| Orthogonality residual `cos(g_perp, e)` max | **1.86e-17** | machine-zero → no-work design holds exactly |
| ω-sector `total_hamiltonian` trajectory ramp | **0.999×** | identical to the FREE 0.998× ramp → NO PUMP |
| Charge held to target, rel-err max | **9.4e-9** | the λ line-solve closes the H_bel gap each step |
| `hold_pumps` | **False** | conservative → NEGATIVE is EARNED, not pump-masked |

The Gram-Schmidt construction (`g_perp = g − (⟨g,e⟩/⟨e,e⟩)e`, with `e = ∇_ω E_ω =
energy_gradient()[1]` = the SATURATED functional the engine's `step()` actually integrates)
makes `dE = ⟨e, λ g_perp⟩ = 0` to first order. The residual second-order curvature is the only
energy channel left, and the ledger confirms it is negligible (0.999× over 1500 steps). **This is
the categorical difference from C: C's neutrality was only *measured* (and failed 56×); C′'s is
*designed* (and holds to machine precision).**

---

## §3 — The KEY DESIGN CHECK finding: the scalar H_bel does NOT pin the (2,3) pair

`extract_2_3_omega_fast` on the (ω, π_ω) phasor (phase-space coordinates, A46-matched — NOT
real-space). The held run vs the hold-OFF run, (n, w_tor, w_pol, H_bel):

```
HELD-ON   n=0:(2,3) H=5.296e-5   n=60:(1,1)   n=120:(1,0)   n=240:(1,2)   n=540:(2,1)   [H pinned 5.296e-5 throughout]
HELD-OFF  n=0:(2,3) H=-3.2e-6    n=60:(1,1)   n=120:(1,0)   n=240:(1,2)   n=540:(1,1)   [H wanders -8.8e-4..+6.6e-4]
```

- **The scalar charge IS held:** H_bel pinned at 5.296e-05 to all printed digits across 540 steps
  (vs free H_bel wandering −8.8e-4 to +6.6e-4). The constraint works exactly.
- **The (2,3) PAIR is NOT maintained:** (w_tor, w_pol) drifts off (2,3) to (1,1)/(1,0)/(0,1)/…
  **identically in shape to the hold-OFF run.** `frac_tail_reads_2_3 = 0.00` on both held-ON and
  hold-OFF. F4 winding-conserved = False, hold-ON and hold-OFF alike.

**Attribution (`ave-apparatus-floor-attribution`):** this is NOT a lattice/dx floor and NOT a
pump artifact. The hold demonstrably pins the scalar (held vs free H_bel diverge by 4 OOM) yet the
pair trajectory is **bit-shaped-identical** to the free run — so the scalar constraint genuinely
leaves the (2,3)-pair-preserving subspace of ω-configurations unconstrained, and the free
dynamics wander through it. The single global helicity number is too coarse to pin two
independent winding integers (toroidal-2 AND poloidal-3). **This is the §9.1-anticipated finding,
stated verbatim: "If H_bel-conservation does NOT maintain (2,3), that is a finding (the scalar
helicity is too coarse to pin the pair) — report it, do not force."**

---

## §4 — Persistence reads (the mass-breather itself)

On the HELD run (cyclic/time-averaged, hazard-10):

| Read | Value | |
|:---|:---|:---|
| F1 breather exists | **True** | bounded, sustains core, true-wall persists; v_tail/seed = 0.681 |
| F2 breather stable | **True** | λ = −0.0112 (slowly-decaying/high-Q, no gain/runaway) |
| Gates G0–G4 | **ALL PASS** | G1-absolute 0.687 ≥ 0.60 (v14 known-positive reproduced); co-resolution TRUE |
| unknot envelope | **True** | single torus shell, 1 radial band (0₁ unknot guard) |

So the **A1 mass-breather persists** (wall-half vindicated, consistent with the prior corrected
re-run) — but it persists **carrying a winding that has drifted off (2,3)**, because the scalar
H_bel hold cannot pin the pair. The two sectors do not cohabit *as the (2,3) electron* under a
scalar-helicity constraint.

---

## §5 — BIN = NEGATIVE (earned), per §9.1

> **🔴 RULE-12 CORRECTION (2026-06-16 — verify panel `w4wkm2erq`, tracker Phase 7; verdict text below PRESERVED).** This "NEGATIVE (earned)" verdict is **RE-BINNED to DISQUALIFY-WRONG-OBJECT** and re-scoped to *"scalar-route CLOSED-NEGATIVE; sector-cohabitation UNTESTED."* The hold's conservativeness (NOT-DISQUALIFY-on-energy) is real, but the held object is a **global scalar (H_bel)** while the electron charge is the **(2,3) integer PAIR** (`master-equation.md:20`); a single scalar cannot pin a two-integer winding, so the negative is a **method-artifact of holding the wrong object**, not an earned keystone-negative. The §5 text below is preserved per Rule 12.

- **NOT DISQUALIFY:** the hold is energy-neutral by construction (ramp 0.999×, cos 1.86e-17) — the
  C pump is cleared.
- **NOT POSITIVE:** POSITIVE requires the (2,3) pair MAINTAINED *and* persistence *and* neutral.
  Persistence ✓ and neutral ✓, but pair-maintained ✗.
- **NEGATIVE (earned):** with H_bel held conservatively, the breather persists but the (2,3)
  charge-pair is not maintained → the conserved *scalar* does not protect the *pair* → the sectors
  do not cohabit as the (2,3) electron. **Earned because the hold is conservative** (the C
  DISQUALIFY masked exactly this question).

**Mechanism named (Rule 11 / honest closure):** a single global scalar invariant (helicity
integral) under-determines a two-integer (p,q) winding. Holding ∫ω·(∇×ω)dV pins one scalar degree
of freedom and leaves the entire (2,3)-preserving manifold free; the free Cosserat-ω dynamics
disperse the pair within it. To pin the *pair* would need a constraint that carries the toroidal
AND poloidal winding integers — not a single scalar charge. *(This bears on the held-BC re-aim's
ontology: the corpus charge=helicity is a scalar, but the electron's (2,3) is a pair; whether the
physical conserved object is the scalar H_bel or the (p,q) pair is the open question this surfaces
— flagged, NOT resolved here.)*

---

## §6 — Reproduction + artifacts

- Module: `src/ave/topological/held_helicity_winding.py` (C′ hold; C `held_bc_winding.py` intact)
- Driver: `src/scripts/vol_1_foundations/passive_eigenmode_driver.py` — `run_option_Cprime`,
  `--hold-helicity`
- Run: `python src/scripts/vol_1_foundations/passive_eigenmode_driver.py --hold-helicity
  --no-sweep --steps 1500` (co-resolving N=26, R=5, r=2.5, dx=0.5, v_width=2.5, ~5 core cells)
- SHA-pinned JSON: `results/passive_eigenmode_cprime_helicity_N26.json`
- `make verify` passes; G0–G4 all PASS; coupling KAPPA_TILDE=6/5 (α-FREE; ALPHA imported only to
  declare it is not a coupling input). Carrier discipline: C′ reads/writes `eng_w.omega` only;
  never the A1 `(V_inc, V_ref)` phasor (G0 double-count-clean preserved).

---

## §7 — Where §9.1's spec did not survive contact with the code (flag, don't paper over)

1. **`_beltrami_helicity` is NORMALIZED, not raw** (§1) — the §9.1 literal formula sums a
   vacuum-dominated handedness field, not the corpus integral. C′ holds the raw integral
   (matching §9.1's prose + `master-equation.md`); both recorded. **Load-bearing; surfaced to
   orchestrator.**
2. **The (2,3) is a PAIR; H_bel is a SCALAR** (§3, §5) — §9.1's KEY DESIGN CHECK anticipated this
   exactly, and it fired: conserving the scalar does not maintain the pair. This is the result, not
   a spec defect — but it means the §9.1 path (hold the scalar charge) cannot reach POSITIVE for
   the (2,3) electron by construction. The ontology question (is the conserved object the scalar
   H_bel or the (p,q) pair?) is surfaced, NOT resolved (implementer lane).

**Do NOT read this as echo or chord** — that is the orchestrator's adjudication. This doc reports
the mechanism result: the no-work H_bel hold is conservative (the C pump is cleared) and the
scalar charge is too coarse to pin the (2,3) pair (NEGATIVE, earned).
