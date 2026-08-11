# THE 𝒜_g DERIVATION (R46 DERIVE-FIRST) — PRE-REGISTRATION (FROZEN)

**Date:** 2026-08-10 · **Branch:** `lane/2026-08-10-ag-derivation` · **Base:** `origin/main` @ `8424995f`
**Lane brief:** [`_orchestration/2026-08-10_ag-derivation-brief.md`](../_orchestration/2026-08-10_ag-derivation-brief.md) (R46, `_orchestration/docket-entries/2026-08-10-rulings-r45-r47.md`).
**Freeze discipline:** this prereg is committed ALONE and pushed (freeze-by-push) BEFORE any 𝒜_g number is computed, any driver code exists, or any consumer arithmetic is executed. The hypothesis, the consumer set, the per-consumer methods, and the verdict grammar below are frozen at push time.
**Class:** DERIVATION-ADJUDICATION lane. Mints no `clm-`/`def-`/`exp-`/`sup-`/`ilk-`; edits no KB leaf, register, ledger, or ruling; changes no solidity; all propagation ROUTED. Engine `src/ave` byte-untouched (consumed read-only + run; `git diff --stat 8424995f..HEAD -- src/` must be empty at every commit).

---

## §0 — Standard Vacuum Analysis header (SVA v0.2-pilot)

 1. **SECTOR / OWNERSHIP:** object = **𝒜_g**, Axiom 5 (Substrate DC Bias)'s grade-coupling area [m²] — the clause-G bridge constant between the A1 displacement dress `u₀` and the operating-point grade `ε₁₁`. Both objects live on the A1 bulk/dilatation slot; T2 and Cosserat byte-untouched; TWO-"3"s guard active (mass=A1 ⊥ charge=Cosserat-winding; never cross-wired). The dress `u₀ = B r̂/r²` and the grade `ε₁₁ = A(r)` are TWO OBJECTS throughout; every step names which it pins.
 2. **REGIME / PHASE-STATE (per R45 comprehensive-map doctrine, per consumer):** all three consumers read the **crystalline phase, cold-linear Regime-I, exterior D(A)→1 limit**. C1 (dress normalization): static exterior, `r ≫ r_sat`. C2 (halo added-mass): deep-space sub-band evanescent operating point (walk RECORD §1(d)(ii) — ~20 OOM below band edge), small-signal. C3 (κ chain): the code's own weak/moderate-field contractive regime; the `A→1` saturated shell is OUT of every consumer's normalization window. Clause S content is consumed as genesis-deposited **boundary data on the crystalline phase** (R45's Ax5 nuance), never as formation dynamics (keystone-LOCK untouched). DC bias point: the quiescent Q-point (clause Q) is the reference throughout.
 3. **CIRCUIT STATEMENT:** in circuit terms the question is whether the bias network's **transduction ratio** between its two DC state variables — the deposited flux-per-source (dress) and the graded operating point (grade) — is a **geometric property of the unit cell** (an area = pure number × cell area) or a **network calibration** (rides the imported G/ξ termination chain). Total-vs-slot: 𝒜_g is a constitutive constant, not a per-port observable; no series-slot claim is made.
 4. **PLANE & PROJECTION:** no signed Γ or Z claim is made by this lane. All flux statements are total enclosed-surface integrals (`∮·n̂` over exterior spheres, radial projection); solid-angle (4π-class) bookkeeping is declared EXPLICITLY at every step — convention factors are exhibited, never absorbed silently.
 5. **CONSTITUTIVE PROVENANCE:** `ε₁₁ = 7GM/c²r` profile — DERIVED-form/VALUE-imported (clm-zbvfpi; ν=2/7 and κ=c⁴/7G GR-imported per #261, not re-argued). Clause G bridge — RATIFIED AXIOM (R43; text travels verbatim, §2 below). `B(M)` accounting — clause S, dimensional VALUE via the imported G/ξ chain (as ratified). ℓ_node = ħ/m_ec — core-derived (`constants.py:293`). ρ_bulk, ξ_topo — canonical (`constants.py:356,:758`). **The hypothesis under test is exactly whether 𝒜_g joins the core-derived column or the imported column.**
 6. **ENERGY LEDGER:** no port is opened or closed by this lane; all consumer physics is reactive/stores-and-returns (P9 is explicitly NOT-A-PORT). No loss word is used.
 7. **CALIBRATABILITY:** the target is the **dimensionless ratio `c ≡ 𝒜_g/ℓ_node²`** — self-calibratable class. Each consumer's output is expressed as this ratio (or as an honest UNVALUED/BRACKET bin).
 8. **DISCRIMINATION CLASS:** DC-internal (the bias network's own constitutive constant; `clm-acdc07` carve). No AVE-vs-SM discriminator is claimed on any outcome; the SM counterfactual is N/A (SM carries no A1 dress). Tautology filter: the internal relation `B = 7𝒜_g GM/c²` alone is ONE equation in TWO unknowns — a consumer "agreeing" via the internal relation alone pins NOTHING and must be binned UNVALUED, never counted as an independent 𝒜_g value (frozen sub-case rule, §4).
 9. **CERTIFICATION PLAN:** gates in §6 frozen before any number exists; UNRUN ≠ PASSED; negative control = the code-side Green's-function convention check runs on the STANDARD 7-pt Laplacian reference (known 1/r Green's function) before the native operator is read. Prereg lands as its own pushed commit.
10. **ADJUDICATION ROUTING:** frozen in §4 verbatim from the brief. On DISAGREE → STOP, route to Grant immediately, no repair attempted, no further derivation. On DERIVED(c) / CONSISTENT-UNVALUED → result doc + DO-NOT-MERGE PR + own Tier-2 before any CLEARED language; the R46/R47 register consequences (interlock entry, count adjudication) are the DOC LANE's to execute on Grant's ruling, never this lane's edits.
11. **NUMERICAL CONDITIONING:** all consumer algebra is executed symbolically (sympy) with float cross-checks (numpy, fixed seed); no iterated map is used by the lane's own algebra. The C3 lattice solve inherits `backreaction.py`'s certified Picard contraction (consumed, not modified); its 1/r-coefficient fit uses the code's own boundary-robust two-model discriminator (bare log-log slopes are known-inflated in the Dirichlet box — `backreaction.py:476-497`). Regex engines named: BSD `grep -rniE` + Python `re` (GNU grep absent on this host — bound-constitutive deviation #1, inherited).

---

## §1 — Frozen hypothesis (R46, verbatim)

From `_orchestration/docket-entries/2026-08-10-rulings-r45-r47.md` (R46):

> **DERIVE-FIRST (Grant: "so let's derive first"):** 𝒜_g enters NO register until the derivation lane adjudicates the frozen hypothesis **𝒜_g = c·ℓ_node²** (c a pure number; ℓ_node = ħ/m_ec — core-derived). […] If DERIVED: 𝒜_g is core-derived, the interlock count never moves, and the import question dissolves. If NOT: 𝒜_g enters the interlock register with the count adjudication (3→4 or new edge class) as a Grant ruling.

## §2 — The ratified axiom clauses consumed (verbatim; λ → 𝒜_g per R46)

From `research/2026-08-10_bound-constitutive_result.md` §2.6 (BC-SRC as ratified by R43; R46 renames the constant: *"the coupling constant formerly drafted as λ is 𝒜_g (the grade-coupling area, [m²])"*):

> **S (deposit).** A matter defect deposits a nonzero net A1 dilatation flux: `∮_S u·n̂ = 4πB(M)` over any enclosing exterior surface, with `B(M)` = the defect's A1 mass accounting (dimensional VALUE via the imported G/ξ chain).
> **G (grade coupling / bridge).** The operating-point grade is the bound sector's potential: `u₀ = −λ∇ε₁₁`, with the grade pinned by the elliptic law `−∇·[κD(A)∇ε₁₁] = T₀₀`, `κ = c⁴/7G` (VALUE imported). Equivalently: the canon backreaction solve becomes BC-LAW in potential form.

**The internal relation (brief, verbatim):** *"the internal relation B = 7·𝒜_g·GM/c²"* — R43's built-in falsifier (*"The λ over-determination test (B = 7λGM/c² across all consumers — the axiom's built-in falsifier)"*).

## §3 — THE FROZEN CONSUMER SET (exactly three; receipts at freeze)

The brief, verbatim: *"compute 𝒜_g independently from EACH receipted consumer: (1) the dress normalization (the canon ε₁₁ = 7GM/c²r profile + the clause-G bridge against the canon dress amplitude); (2) the halo added-mass row (the bulk near-field store, port-register:35 family); (3) the backreaction.py solve's normalization (the κ chain). THREE independent 𝒜_g values."*

**C1 — the dress normalization.**
- *Receipts:* grade profile `ε₁₁ = 7GM/c²r` = clm-zbvfpi (`manuscript/ave-kb/vol3/claim-quality.md:1254-1258`, *"the inherited linear elastic-Poisson / Schwarzschild profile (ε₁₁ = 7GM/c²r …)"*; `r_sat = 7GM/c²`). Canon dress-amplitude state going in: `research/2026-08-09_screening-theorem_result.md:19,:68` (`qₐ ∝ mₐ` — PROPORTIONAL); `research/2026-08-07_a1-port-sourcing_result.md:387` (*"NO receipted DC-anchor normalization closes the amplitude"*) and `:552` (the absolute normalization of BOTH channels ABSENT).
- *Frozen method:* (a) apply clause G to the canon profile symbolically → predicted dress amplitude `B_pred(𝒜_g)`; receipt that this reproduces the internal relation exactly (coherence check, sympy). (b) Two-engine corpus sweep (BSD grep + Python `re`; patterns for `B =`, `4πB`, `∮u·n̂`, dress-amplitude phrasing over `research/` + `manuscript/`) enumerating every site that states an ABSOLUTE (dimensional) dress amplitude for a given source mass. (c) If an absolute canon `B(M)` exists → `𝒜_g^{C1} = B·c²/(7GM)` (symbolic; then `c^{C1} = 𝒜_g^{C1}/ℓ_node²`). If the sweep confirms proportional-only → **C1 output = UNVALUED** (no independent absolute anchor; agrees-by-construction).

**C2 — the halo added-mass row.**
- *Receipts:* `manuscript/ave-kb/common/port-register.md:35` (*"The dark-matter halo = the bulk channel's reactive NEAR-FIELD (stores/loads, added-mass — shapes rotation curves), NOT a port"*) + `:77` (P9 row; walk-record backing `research/2026-07-19_deep-space-reactive-bulk-walk_RECORD.md:54,:68`); kinetic-term hosting: `research/2026-08-10_bound-constitutive_result.md` §4.3 (*"Halo P9 added-mass: hosted by the kinetic term ∫|π|²/2ρ — the convected near-field's energy is KINETIC"*); substrate density ρ_bulk (`constants.py:758`). The row is walk-level mechanism; NO frozen numeric halo normalization is known at freeze — if the sweep finds one, it is used; else the row's magnitude-class IS the DM identification itself (the halo the row names is the phenomenological dark-matter mass at galactic radii).
- *Frozen method:* (a) convected-dress added mass, exact: `u(x,t) = u₀(x−Vt)`, `π = −ρ(V·∇)u₀`, `E_add = ∫|π|²/2ρ ≡ ½ m_add V²`; compute `m_add` for `u₀ = B r̂/r²` symbolically (sympy; angular integrals exact) over the exterior `r ∈ [r_c, ∞)`, with the inner-cutoff dependence stated honestly. (b) Express `m_add(𝒜_g; M, r_c)` via the internal relation. (c) Invert the row's magnitude-class: what `𝒜_g` makes `m_add` ~ the halo mass-class the row assigns it (declared bracket: `m_add/M ∈ [1, 10]` at galactic parameters — the DM-to-baryon magnitude the rotation-curve reading requires)? Output = value or honest BRACKET; then compare against ℓ_node² scale. If the bracket spans no stable decade (cutoff-dominated beyond canon's ability to pin `r_c`), **C2 output = UNVALUED-BRACKET** with the dependence exhibited.
- *Fence:* this route READS the P9 row's receipted magnitude-class; it does NOT adjudicate the DM mechanism, does not touch SPARC-parity claims, and does not mint any halo physics.

**C3 — the backreaction solve's normalization (the κ chain).**
- *Receipts:* `src/ave/gravity/backreaction.py:94` (`KAPPA_GRAV = C_0**4/(7.0*G)`), `:12` (the solve), `:28-32` (M_eff + *"the far-field Gauss flux is expected to reconcile with M_eff (X44 fireable gate)"*), `:437` (Gauss≡Picard ledger), `:455` (the tautological profile check DEMOTED — inherited: reproducing `7GM/c²r` is NOT treated as a gate here either).
- *Frozen method:* (a) READ the code's operative source normalization (how `∫T₀₀` maps to the 1/r amplitude — the Green's-function convention, incl. any 4π), on the standard 7-pt reference operator FIRST (negative control), then the native operator. (b) RUN the code (point + blob configurations, `return_fields=True`); on the converged field compute the discrete enclosed flux of the clause-G dress, `∮(−𝒜_g∇ε₁₁)·n̂`, as a function of enclosed `M_eff`; express as `B_code = f · 𝒜_g · G·M_eff/c²` with `f` MEASURED (fit + R²; two radii for exterior-independence). (c) The C3 output is the measured chain coefficient `f` against the internal relation's `7`: `f = 7` (within the fit's stated convention reconciliation, every 4π exhibited) ⇒ the κ chain agrees with C1's profile-side relation; `f ≠ 7` after explicit convention reconciliation ⇒ **the consumers DISAGREE** (this is the concrete seam where OVER-DETERMINATION-FAILS can fire). C3 pins `𝒜_g`'s VALUE only jointly with an absolute `B`; standalone it adjudicates chain COHERENCE — binned per §4's sub-case rule.
- *Fence (brief, verbatim):* *"the engine codes the solve (stencil-lens — backreaction.py's normalization is a CONSUMER here, not an adjudicator)"*. No engine file is edited.

**Independence assessment (declared at freeze, part of the frozen record):** C1 and C3 both touch the `7GM/c²r`-profile family (C1 the canon statement, C3 the code chain) — their INDEPENDENT content is the convention-coherence of two different receipted homes of that family plus C1's absolute-anchor sweep; C2 is the only consumer with an external magnitude anchor (the DM identification). A three-way agreement that consists ONLY of internal-relation restatements is NOT over-determination — it is binned UNVALUED per row 8's tautology filter.

## §4 — FROZEN VERDICT GRAMMAR (brief, verbatim) + sub-case mapping

> Verdicts: **DERIVED(c)** — all three agree at a pure number × ℓ_node² (state c exactly and its geometric origin candidate); **CONSISTENT-UNVALUED** — they agree with each other but not at ℓ_node² scale (𝒜_g is real, one value, not core-derived → the interlock/count adjudication fires); **OVER-DETERMINATION-FAILS** — the consumers DISAGREE: BC-SRC's internal falsifier has fired; route to Grant immediately (this is the axiom's own test port doing its job).

**Lane-frozen operationalization (declared here at freeze; the brief's sentence governs on any conflict):**
1. Agreement is SYMBOLIC-EXACT after explicitly-exhibited convention reconciliation (4π-class solid-angle bookkeeping shown step-by-step). Any residual factor after reconciliation = DISAGREE. No numerical tolerance buys agreement; the C3 lattice fit's discretization error bounds only the MEASUREMENT of `f`, never a symbolic residual.
2. A consumer whose output is UNVALUED / UNVALUED-BRACKET (no independent absolute pin) cannot contribute an "agreeing value"; it contributes coherence only. **DERIVED(c)** therefore requires: three VALUED outputs, all equal, at pure-number × ℓ_node² — per the brief's own words ("all three agree at a pure number × ℓ_node²").
3. Any pairwise DISAGREE among VALUED outputs, or `f ≠ 7` after reconciliation (C3), fires **OVER-DETERMINATION-FAILS** → STOP → route to Grant immediately (SVA row 10). No repair, no re-derivation, no framing rescue.
4. Everything else — including the all-coherent-but-underdetermined case — is **CONSISTENT-UNVALUED**, with the exact sub-case stated (which consumers valued, which not, and what would upgrade each).
5. "Pure number" means a closed-form dimensionless constant of geometric/topological origin (integers, rationals, π-family, √-family of the lattice geometry) NOT passing through G, ξ, α, or any CODATA import. A value at `(imported-hierarchy) × ℓ_node²` (e.g. ξ-carrying) is NOT-at-ℓ_node²-scale by definition.

## §5 — Expectation (ave-prereg; stated before any computation)

Going in, the receipts say: canon's dress normalization is proportional-only (C1 receipts above), the halo row is walk-level mechanism with the DM identification as its only magnitude anchor (C2), and the κ chain is certified on ratio/shape gates (κ-scale-invariant; C3). The structurally-likely outcome is therefore **CONSISTENT-UNVALUED** — coherence without an absolute pin — unless (a) the C1 sweep surfaces an absolute anchor unknown at freeze, or (b) C2's bracket collapses to a stable value. **DERIVED(c)** requires all three consumers to value 𝒜_g at pure-number × ℓ_node²; no receipt at freeze suggests this. The concrete places a genuine **OVER-DETERMINATION-FAILS** could fire: the 4π-class seam between the code's Green's-function convention and the canon profile (C3's measured `f` vs 7), and a C2 value landing incompatible with any C1 absolute anchor found. Discriminating observations: C1 absolute-anchor existence; C2 required-magnitude vs ℓ_node² scale; C3 measured `f`.

## §6 — Frozen gate table (UNRUN ≠ PASSED)

| Gate | Frozen criterion |
|---|---|
| **G-QUOTE** | Every ruled/frozen quote above byte-checks against its cited file:line, two engines (BSD grep -F + Python exact-substring) |
| **G-C1** | Two-engine sweep executed with patterns disclosed; absolute-vs-proportional adjudicated with per-site receipts; output binned per §3-C1's frozen rule |
| **G-C2** | `m_add` integral exact (sympy) + independent numeric cross-check (numpy, fixed seed, ≤1e-8 rel); cutoff dependence exhibited; inversion executed against the declared bracket; output binned per §3-C2 |
| **G-C3** | Reference-operator negative control run BEFORE the native read; code run point + blob; `f` measured with fit receipts (R² ≥ 0.99 point-source class) at two exterior radii; every convention factor exhibited |
| **G-VERDICT** | §4 mapping applied mechanically; on DISAGREE the lane STOPS and routes to Grant with no further derivation content |
| **G-ENGINE-FLAG** | `git diff --stat 8424995f..HEAD -- src/` empty at every commit |
| **G-NUM** | Driver two full runs byte-identical (sha256 logged); number-check script green with `--mutation-receipt` firing; `make verify` green in the worktree at the result commit |

## §7 — Instruments (named at freeze)

Driver `research/drivers/ag_derivation_lane.py` → `ag_derivation_lane_results.json`; number-check `research/drivers/ag_derivation_lane_number_check.py` (`--mutation-receipt`; auto-discovered by the `make verify` umbrella). Engines: sympy (symbolic), numpy fixed-seed (float), `backreaction.py` (consumed read-only), BSD `grep` + Python `re` (sweeps). Constants ONLY via `from ave.core.constants import ...` (ave-canonical-source; no hard-coded values). Worktree `PYTHONPATH=$PWD/src` discipline per repo CLAUDE.md.

---

> **Prereg provenance.** Written by the 𝒜_g derivation lane (R46) in throwaway worktree `AVE-Core-worktrees/wt-ag-derivation` off `origin/main` @ `8424995f`. Skill set applied: ave-prereg (this doc), SVA v0.2 §0 header, ave-canonical-source (§7), verify-before-cite (every receipt read at HEAD before citation), consistency-vs-emergence (ledger owed in result doc), ave-worktree-paths (worktree-absolute paths from first call). Committed ALONE + pushed before any derivation content. `[DO-NOT-MERGE]` rides the lane's PR; Tier-2 before any CLEARED language.
