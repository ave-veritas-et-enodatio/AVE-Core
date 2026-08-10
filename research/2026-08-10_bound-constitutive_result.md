# THE BOUND-SECTOR CONSTITUTIVE LAW (R41) — RESULT

**Date:** 2026-08-10 · **Branch:** `lane/2026-08-10-bound-constitutive` · **Base:** `origin/main` @ `6c291196`
**Frozen prereg:** [`2026-08-10_bound-constitutive_prereg-FROZEN.md`](2026-08-10_bound-constitutive_prereg-FROZEN.md), committed ALONE + pushed at `ac6a176c` (2026-08-10T13:36:55Z, freeze-by-push) before any derivation content, driver code, or lane number existed.
**Driver:** [`research/drivers/bound_constitutive_lane.py`](drivers/bound_constitutive_lane.py) → [`bound_constitutive_lane_results.json`](drivers/bound_constitutive_lane_results.json) + [`bound_constitutive_lane_number_check.py`](drivers/bound_constitutive_lane_number_check.py) (`--mutation-receipt`; auto-discovered by the `make verify` umbrella). Two full runs byte-identical (sha256 `0dbf1a58…`).
**Class:** DERIVATION. **Mints no `clm-`/`def-`/`exp-`/`sup-`/`ilk-`; edits no KB leaf, register, ledger, or ruling; changes no solidity; all propagation ROUTED.** The item-(0) repair and every axiom-adjacent statement below are **PROPOSALS for Grant's ratification**, not edits. Engine `src/ave` byte-untouched (`git diff --stat 6c291196..HEAD -- src/` empty).
**Lane brief:** [`_orchestration/2026-08-10_bound-sector-constitutive-brief.md`](../_orchestration/2026-08-10_bound-sector-constitutive-brief.md) (Grant GO, R41).

**Instrument deviations, disclosed FIRST (direction-of-effect stated):** (1) GNU `grep` is absent on this host; the sweep's engine 1 was BSD `grep -rniE` (ugrep shim bypassed) — both engines agreed on every text-file hit set, so no observed effect. (2) The driver's front tracker was calibrated on the CONTROLS before banking (threshold-radius → median-energy → two-detector half-max arrival): the first two forms carried known biases (decaying-max reach; 2D wake), each reproduced and replaced; and the first force stencil (compact-Laplacian minus composed-grad-div) was NOT discretely curl-curl — the receipted flat direction leaked at wave speed until the force was built as the LITERAL double curl. Direction-of-effect: the fixes make the flat-direction and front receipts HONEST (the leak was instrument error of exactly the Stage-1 non-DEC-pair class, caught by the K-loaded control calibration the prereg froze). (3) The front receipts run on a 2D grid with the 3D constitutive operator (P-speed algebra dimension-independent); the radial receipts are 1D-spherical. Disclosed; the prereg froze "toy-lattice" without dimension.

---

## §0 — REGIME / SECTOR / PHASE-STATE (prereg SVA §0 governs; restated)

**MODE** — constitutive-structure derivation + axiom-text adjudication. **REGIME** — cold-linear Regime-I throughout; past-wall out of scope. **SECTOR** — the A1 bulk/dilatation slot's missing structure; T2 and Cosserat byte-untouched (rotational fence-reach STOP checked at §1–§5: no step routes bulk-slot content through micro-rotation). TWO-"3"s guard active. The dress `u₀ = B/r²` and the grade `ε₁₁ = A(r)` are TWO OBJECTS throughout (each pinned statement names its object). **STENCIL** — no run of `src/ave` corroborates anything here; every numeric receipt is the purpose-built driver.

---

## HEADLINE

> **VERDICT (four-tuple + the upstream adjudication; per-item, no aggregation; pre-Tier-2 form):**
>
> **(0) ADJUDICATED — recommended reading: the written axiom form is the TEMPORAL-GAUGE (Weyl-gauge) MAXWELL SYSTEM, taken literally.** Both routes agree. The exact symmetry of the written action is the residual, time-independent gauge family `A → A + ∇λ(x)` (driver R0a: exact zero); full time-dependent U(1) FAILS on the written form with exact remainder `ε₀(∂_t𝐀)·∇(∂_tλ) + ½ε₀|∇(∂_tλ)|²` (R0b); and the residual symmetry's Noether content is precisely the pointwise conservation of the Gauss function `∇·(ε₀∂_t𝐀)` (R0c). So `:22` is wrong at the ACTION level (no A₀ ⇒ Gauss's law is not an equation of motion of this action) and right at the DYNAMICS-ON-THE-CONSTRAINT-SURFACE level; `:27` is wrong for full U(1) and right for the residual family — whose Noether charge IS the Gauss constraint the corpus needs. The two "wrong labels" and the #935 flat direction are one fact: **the axioms wrote the temporal-gauge chassis and never wrote the constraint; the constraint is exactly item (i).** Repair text drafted (§1.3); consequence audit complete (77 sites two-method; 10 NEEDS-RESCOPE, 4 drift findings, remainder TRUE-UNDER-REPAIR / INDEPENDENT; §1.4). Grant-ratification object.
>
> **(i) DERIVED — the bound-sector constitutive law is an INITIAL-DATA-CLASS Gauss law (BC-LAW), not a multiplier/holonomic constraint — and deriving WHICH class it is, is the load-bearing result.** (1) CONSERVATION: `∂_t(∇·π) = 0` in vacuum is a theorem of the receipted curl-only dynamics (Noether route: R0c symbolic; DEC route: R2, machine-exact on the literal double-curl stencil), extended to `∂_t(∇·π) = −∇·j_m` under any local source coupling. (2) DEPOSIT: the enclosed flux `∮u·n̂` over any exterior surface equals the defect's caged A1 dilatation content by Gauss's theorem + the PR#260 confinement theorem (`eq_axiom_4.tex:53-60`: rest mass IS the A1 dilatation sector at V_snap, `def-vyvsn1`) — the B↔M identification is the banked mass = A1 accounting; its dimensional normalization rides the imported G/ξ chain (FORM derived, VALUE imported, 5th instance of the meta-finding). (3) QUIESCENCE: `∇·π = 0` and `θ = 0` away from defects is canon's cold-quiescent operating point (the vacuum definition), not new structure. (4) UNIQUENESS: the decaying curl-free exterior of a point deposit is `u₀ = B r̂/r²` (R5, `dsolve` + Helmholtz; the residual-gauge softness is fully absorbed into θ's initial data, which clause (2) pins — with decay, harmonic shifts vanish). **No new axiom is required** on this adjudication; the honest fallback framing, if Grant reads clause (3) as new content, is `DERIVED-VIA-NEW-AXIOM(quiescent-substrate initial-data law)` — presented for ratification either way. **The A1/EM sector asymmetry is derived, not assumed:** the A1 charge is transportable (its current `π/ρ` is unconstrained, so collapse can pile dilatation — mass accretes), while the EM/winding charge's axiom-native currents are divergence-free (the four-lock no-go, banked) — this lane's law is NOT the closed sourced-static-monopole path, and the difference is stated per step (§2.4).
>
> **(ii) DERIVED — the no-signalling theorem for the real, non-gauge bound field.** T1: the receipted evolution is local with ONE finite characteristic speed c (transverse; R3: 0.9959c measured) and ZERO longitudinal characteristic speed (R1; R3: static to `1.6e-19` — and NOT by the K→0 route the LC-1 receipt closes: the receipted potential lacks the deviatoric-restoring stencil entirely, which is why there is no `√(4/3)c` floor). T2: the BC-LAW constraint is conserved by that evolution (R0c/R2), causally, given matter-current locality. T3: the energy estimate — flux `|𝐒| = |−ρc²u̇×(∇×u)| ≤ c·(energy density)`, with the longitudinal sector contributing NO flux term — gives the domain-of-dependence theorem: no energy or information crosses outside the c-cone, at any frequency, and the bound sector's own transport speed is zero. The GRAVIMETER scenario (FORK 2) lands CAUSAL: far-dress updates are mediated by the curl sector (the receipted system is operator-identical to temporal-gauge Maxwell under the transverse+flat decomposition, where the moving dress's convective update `∂_t E = c²∇×B` rides the curl sector inside the cone — the boosted-Coulomb exhibit transplants verbatim), so a local grade reading changes no earlier than the cone allows. T4 vs LC-1's frozen cell (*"An energy-carrying inter-event channel at ≠ c ⇒ arc-level kill"*): **the bound sector is not an energy-carrying inter-event channel at ANY speed** — established by theorem + receipts, not vocabulary; the no-port language appears in this lane only as a CONCLUSION. Scope honestly stated: the theorem covers the receipted dynamics + BC-LAW; it does not adjudicate LC-1's cell (that re-adjudication is the orchestrator's, triggered per the brief's frozen sentence on (i)+(ii) both DERIVED-class).
>
> **(iii) DERIVED (FORM; values imported unchanged) — the bound-sector energy functional is the constraint sector's DIRICHLET functional plus the convective kinetic term:** `E_bound = ∫ ½·κ·D(A)·|∇ε₁₁|² dV + ∫ |π|²/2ρ dV`, with `κ = c⁴/7G` (the canon elliptic solve `−∇·[κD(A)∇ε₁₁] = T₀₀` IS this functional's Euler–Lagrange equation — the FORM the corpus has been running un-derived in `backreaction.py`; κ's VALUE stays imported). Finding #3's crux is resolved, not waved: the bare curl-only Hamiltonian genuinely scores ZERO on a static dress — correct, and the per-cell `A²` loading reading is ALSO wrong (it diverges at large r, and canon already rules absolute A unobservable: *"only spatial gradients of A … are physically observable"*, KB CLAUDE.md) — the dress's energy rides the GRADIENT structure of the loaded cells, which is finite, positive, Coulomb-class (`∝1/r⁴` density; R4 exact), stores-and-returns (Ax3-legal), convects with the source (halo P9 added-mass = the kinetic term, per the deep-space walk receipts). Mass = A1 hosted at the source term/caged core. Consistent with (i): same constraint, same field, one bookkeeping.
>
> **(iv) DERIVED (FORM; the honesty keystone) — the cut is ZONE/POLE structure, not a frequency gate, and its placement falls out of the pole structure of the receipted dynamics + BC-LAW with the pulsar comparison appearing NOWHERE in the chain.** The constraint sector's response to a source is the elliptic solve at EVERY drive frequency (near-zone, `1/r²`, reactive, quasi-static tracking with `O((ωr/c)²)` curl-mediated corrections) and has NO radiative pole at ANY frequency (no finite-ω longitudinal eigenmode exists to carry a `1/r` term — R1/R3/R5: the receipted radial sector transports nothing, machine zero, while the K-loaded control radiates). So the same structure banks statically and cannot radiate, at all ω — "banks where it banks, silent where the pulsars listen" is one derived fact about pole structure, not two tuned behaviors. The static /7 chain survives byte-identical (every consumer is static-only per the base-state audit; the FORM is the constraint's elliptic response, the ν = 2/7 VALUE stays GR-imported per #261 — neither #261 gate re-argued, §5.3). Reading-B's owed mechanism (`port-register.md:91`) is discharged: there is no "mode that propagates freely at √(10/3)c in its linear passband" in the receipted dynamics — the passband was the import's; the corpus owed a mechanism for a phantom. The 3/7 trace factor is now CITED (R6; `θ = (1−2ν)ε₁₁ = (3/7)ε₁₁`, static projection algebra, consuming ν as input, unchanged — discharging the #935 disclosure).
>
> **Conditionality banner:** items (i)–(iv) are derived under item (0)'s RECOMMENDED reading (temporal-gauge-literal). Under the alternative "standard-Maxwell" reading, the EM-sector A_L would be pure gauge — but (i)–(iv) run in the MECHANICAL sector's own variables (u, π) and consume the EM mapping nowhere (FORK 1 disposition, §2.5), so the four-tuple is robust to the EM-side fork; what the alternative reading would change is the item-(0) repair text itself and the def-l0ngdu re-scoping, both routed to Grant.

---

## §1 — ITEM (0): the axiom-text adjudication (Grant-ratification object)

### §1.1 Route (α) — what the written form IS (driver receipts R0a/R0b/R0c; sympy + fixed-seed float)

The written action (`eq_axiom_3.tex:18`): `𝓛 = ½ε₀|∂_t𝐀|² − (1/2μ₀)|∇×𝐀|²`, no A₀ term, no source term.

1. **Exact residual symmetry (R0a):** for time-independent `λ(x)`, `𝓛(𝐀 + ∇λ) − 𝓛(𝐀) ≡ 0` exactly (`∂_t∇λ = 0`, `∇×∇λ = 0`). Machine-verified symbolically.
2. **Full U(1) fails (R0b):** for time-dependent `λ(x,t)`, the difference is exactly `ε₀(∂_t𝐀)·∇(∂_tλ) + ½ε₀|∇(∂_tλ)|²` — the addendum's charge verified with the remainder exhibited. So `:27`'s "U(1) gauge symmetry follows as Noether consequence" is FALSE as written for the full group.
3. **The residual symmetry's Noether content IS the Gauss function (R0c):** the charge per test function, `Q_λ = ∫ε₀∂_t𝐀·∇λ = −∫λ ∇·(ε₀∂_t𝐀)` + surface (identity machine-verified), and on-shell `∂_t∇·(ε₀∂_t𝐀) = −(1/μ₀)∇·(∇×∇×𝐀) ≡ 0` (div∘curl∘curl ≡ 0, symbolic + fixed-seed float). **The written theory conserves the Gauss function pointwise; it does not FIX its value.** That is the exact mathematical content of #935's flat-direction finding (`ε₀Ä_L = 0`, conserved momentum) — the conserved momentum IS `−ε₀E_L`, the Gauss sector.
4. **Ontology of the pieces:** the longitudinal CONFIGURATION `A_L`'s static part shifts under the residual symmetry (gauge-soft); the longitudinal MOMENTUM `Π_L = ε₀∂_tA_L = −ε₀E_L` is residual-gauge-INVARIANT and physical. "∇·A is gauge" and "the flat direction is a real state variable" are BOTH true — of the configuration and of the momentum respectively. The corpus's straddle dissolves.

**Temporal-gauge identification:** this is precisely standard Maxwell in the Weyl gauge `A₀ = 0`: same dynamics as Maxwell ON the constraint surface `∇·(ε₀E) = ρ` (a surface these equations preserve but do not select); Gauss's law is the initial-data constraint that the A₀ multiplier would have enforced and the written action omits. The label "standard Maxwell Lagrangian" is therefore FALSE of the action and TRUE of the constrained dynamics. Route (α)'s facts are ENTAILED algebra (prereg §6) — labeled DEMONSTRATED; the adjudication below is the fireable part.

### §1.2 Route (β) — which reading canon load-bearingly consumes

FOR the literal/temporal-gauge reading: the corpus's operative dynamics IS this system at derivation grade (`the-sourced-charge-no-go-cascade.md:114-119`: `∂_t(∇·E) ≡ 0`, *"set by initial data, not emergent"* — the constraint-conservation half of the temporal-gauge structure, already derived and MERGED); #935's verifier-reproduced flat direction; vol2 ch05's own U(1) account derives the RESIDUAL family (*"network-dynamic freedom to shift the irrotational background"*, single-valued Λ) and concedes at `:51` *"there is no scalar-potential companion here to absorb φ → φ − ∂_tΛ"*. FOR the standard-Maxwell reading: def-l0ngdu/def-uatk1s (*"∇·A is gauge"*, SOLID) and the MYTH-GUARD (*"What Heaviside–Gibbs dropped was a gauge slot"*). **Adjudication: the two bodies of usage are RECONCILED, not opposed, by the temporal-gauge reading with the configuration/momentum split (§1.1.4)** — def-l0ngdu's sentence is true of the configuration; the no-go cascade's and #935's structure is true of the momentum; nothing in canon requires full-U(1) invariance of the written action, and the one derivation that tried (ch05) built the residual family. Routes agree → **recommended reading: temporal-gauge-literal, with the constraint owed — and item (i) is the owed constraint.**

### §1.3 The repair text (PROPOSAL — replaces the two false sentences; everything else byte-unchanged)

For `:22`: *"This is the temporal-gauge (Weyl-gauge, A₀-free) form of the Maxwell Lagrangian: standard Maxwell dynamics are recovered on the Gauss-constrained initial-data surface — `∇·(ε₀∂_t𝐀)` is a constant of motion of these equations, pinned to its source value by the bound-sector constitutive law [BC-LAW leaf], not by an equation of motion of this action (the written action carries no scalar-potential/multiplier term). Recovered as the substrate's effective action in the linear regime (A ≪ A_yield)."*

For `:27`: *"Energy conservation follows as a Noether consequence of time-translation invariance. The written action's exact internal symmetry is the residual (time-independent) gauge family 𝐀 → 𝐀 + ∇λ(x); its Noether content is the pointwise conservation of the Gauss function ∇·(ε₀∂_t𝐀). Full time-dependent U(1) is NOT a symmetry of this action (the |∂_t𝐀|² term shifts by ε₀(∂_t𝐀)·∇(∂_tλ) + ½ε₀|∇(∂_tλ)|²); it is recovered on the constraint surface in the covariant completion. Lorentz invariance follows only in the continuum limit — emergent, not exact (unchanged)."*

### §1.4 The consequence audit (two-method sweep; counts as measured: 73 pattern sites + 4 off-pattern known sites; engines agreed on every text file)

Full per-site table in the sweep record (session artifact; dispositions summarized here — the sweep is PATTERN-BOUNDED: paraphrase-only consumers outside the known-site list would evade both engines equally, disclosed).

- **NEEDS-RESCOPE (10):** `eq_axiom_3.tex:22`,`:27` (the anchors); `backmatter/02_full_derivation_chain.tex:153-154` and `backmatter/12_mathematical_closure.tex:79` (verbatim label copies); `01_fundamental_axioms.tex:299` + KB mirrors `kirchhoff-network-method.md:43`, `vol1/claim-quality.md:752` (*"enforces local gauge invariance"* → the exact content is the residual symmetry / discrete Gauss-generator conservation); `q-g20f-vacuum-polarization.md:66` (load-bears BOTH labels + "relativistic" against `:27`'s own emergent-Lorentz demotion); `qed-trace-charter.md:33` family (hosts `:27` verbatim — content survives as the Gauss-generator statement; FROZEN docs get dated surface-notes, never rewrites); `session/axiom-homologation.md:14`.
- **DRIFT findings (4, confirmed at HEAD):** D1 `backmatter/02:163-164` still lists **Lorentz invariance** in the Noether list (against `eq_axiom_3.tex:27` at HEAD). D2 `axiom-register.md:174` (*"proven internal theorem"*) vs `:231` (*"ASSERTED-not-derived … underived dynamics leg"*) — the Ax3 equivalence status contradicts itself within one register. D3 `axiom-register.md:173` asserts the equivalence flatly against `eq_axiom_3.tex:37`'s necessary-not-sufficient flag. D4 `01_fundamental_axioms.tex:71` same pre-flag equivalence claim. All four routed (flag-don't-fix).
- **TRUE-UNDER-REPAIR:** the Maxwell-recovery-at-S≈1 regime claims, the conservation-law consumers, all `src/` docstring sites, and the MYTH-GUARD — the latter with the lane's caution attached: the MYTH-GUARD's "gauge slot" story is true of TEXTBOOK Maxwell; the WRITTEN action differs on exactly that point until BC-LAW supplies the constraint.
- **INDEPENDENT (with two flags routed):** the vol2 ch05 Helmholtz-U(1) complex (its own derivation; flag (a): ch05:35's *"a channel with no restoring force stores no energy"* holds only for time-independent Λ — the kinetic term is NOT curl-only, and the longitudinal channel stores `½ε₀|∂_tA_L|²`; flag (b): the `:155` Wilson-plaquette "recovers −¼F_{μν}F^{μν}" produces only the magnetic term from spatial plaquettes — the covariant label is shorthand overreach of the same A₀-less shape as the anchor). INVARIANT-S2's Ax3 row (carries neither label; mild D3-adjacent softness noted).

**G-AX0-2M: routes agree; repair drafted; audit complete → item (0) ADJUDICATED (recommended: temporal-gauge-literal).**

---

## §2 — ITEM (i): the constitutive law (BC-LAW)

### §2.1 The law, stated

For the mechanical translational sector in its own variables (displacement `u`, momentum `π = ρu̇`, dilatation `θ = ∇·u`), under the receipted curl-only dynamics `ρü = −ρc²∇×(∇×u) + f_source`:

> **BC-LAW.** (a) *Conservation:* `∂_t(∇·π) = −∇·j_m` — in vacuum `∂_t(∇·π) ≡ 0`. (b) *Quiescence (initial data):* away from defects the substrate sits at its cold-quiescent operating point: `∇·π = 0`, `θ = 0`. (c) *Deposit:* each defect's enclosed dilatation flux equals its caged A1 content: `∮_S u·n̂ = ∫_encl θ = ` the defect's caged dilatation `= 4πB`, the mass = A1 accounting. (d) *Uniqueness:* the exterior bound field is the unique decaying curl-free solution of `∇·u = θ_source`, i.e. `u₀ = B r̂/r²` for a point deposit.
>
> The law is **initial-data class** (temporal-gauge/Gauss class), NOT multiplier/holonomic class — and that classification is derived, not chosen (§2.3).

### §2.2 Route (a) — the symmetry/constraint derivation (continuum)

1. **Conservation leg (DERIVED — new this lane, both engines).** The receipted force is a double curl, so `∇·(force) ≡ 0` (R0c symbolic; R2 machine-exact `≤1e-12` on the toy including sourced continuity). Equivalently: the residual shift symmetry `u → u + ∇λ(x)` of the curl-only action has Noether content = pointwise conservation of `∇·π` (the same algebra as §1.1.3, transplanted — the receipted mechanical form and temporal-gauge Maxwell are the SAME operator class). This answers #935's "no multiplier structure has an axiom preimage" honestly: **the preimage of the GAUSS structure is the residual symmetry the action does have; what has no preimage is a MULTIPLIER — and none is needed, because the constraint class is initial-data, not holonomic.**
2. **Kinematic freeze (DERIVED).** `∂_tθ = ∇·u̇ = (∇·π)/ρ`. Wherever clause (b) holds (`∇·π = 0`), the dilatation pattern `θ(x)` is FROZEN — carried as static bias. The #935 under-determination (`A_L(t) = A_L(0) + V_L·t` drift) is exactly the statement that the drift rate is the conserved `∇·π`; clause (b) sets it to zero where the vacuum is quiescent, and clause (a) keeps it there causally.
3. **Deposit leg (BANKED + Gauss's theorem).** `∮_S u·n̂ = ∫_encl ∇·u` (math). The exterior is div-free (the dress: `∇·u₀ = 4πB δ³`, #930 §1.5.0 receipt), so the flux over ANY exterior surface reads the core's caged content. The identification of that content with the mass accounting is PR#260's confinement theorem (`eq_axiom_4.tex:53-60`: *"rest mass is the A1 dilatation sector at V_snap"*, `def-vyvsn1`) + R38's banked mass = A1. The B↔M dimensional normalization rides the imported G/ξ chain — FORM derived, VALUE imported (the meta-finding's 5th instance).
4. **Uniqueness leg (DERIVED, math).** Curl content radiates off at c (T2 dynamical), leaving the harmonic + source-pinned part; the unique decaying curl-free field with `∇·u = 4πBδ³` is `B r̂/r²` (Helmholtz; R5 `dsolve` receipt `u' + 2u/r = 0 → u = C/r²`). **The residual-gauge softness does not leave the dress soft:** a static shift `u → u + ∇λ(x)` changes θ by `∇²λ`; θ is pinned by (b)+(c), so admissible shifts have `∇²λ = 0`, and with decay the only harmonic λ is constant → zero shift. The flat direction's entire freedom is absorbed into θ's initial data, which the law pins.

### §2.3 Why initial-data class and not multiplier class (the load-bearing classification)

A holonomic/multiplier constraint (`∇·u = s` enforced by a pressure field at all times) is the INCOMPRESSIBLE-MEDIUM structure — and an incompressible medium is the textbook infinite-signal-speed idealization: the multiplier field transmits force instantaneously (push a piston, the column moves). If item (i) had landed there, item (ii) would be FALSE. The receipted dynamics does not contain that structure (no multiplier has an axiom preimage — #935, banked, correct); it contains the OTHER Gauss structure: a conserved quantity whose value is initial data, preserved causally by a local flow (§3). **The #935 knife is honored, not reconstructed:** the flat direction remains a genuine state variable; BC-LAW does not re-classify it as constraint-class — it pins the physical VALUE of its conserved data by (b)+(c). Dynamics alone under-determines the dress (#935's finding stands); dynamics + vacuum definition + source inventory determines it. That is the same epistemic structure as Maxwell in temporal gauge, where Gauss's law is likewise not a theorem of the dynamics but a property of the physical state, preserved by the dynamics.

### §2.4 The sector fence (four-lock no-go NOT reconstructed)

The four locks close the EM/winding sector's *sourced net monopole from quiescence* (axiom-native currents there are curl-form, `∇·J ≡ 0` — charge cannot pile). The A1 sector's transport current is `π/ρ` — NOT constrained divergence-free — so dilatation can pile by TRANSPORT (collapse flows pile θ into a core through every enclosing surface, changing enclosed content at exactly the rate the surface flux says; nothing is created). **The A1/EM asymmetry is therefore derived:** mass accretes continuously by transport; net EM charge cannot arise from quiescence; winding charge is separately integer-protected (Ax2). No step here mints a sourced monopole in the closed sector; Lock 3's maximum principle is not touched (the A1 deposit is transported through the boundary, not conjured under it); the statics-tautology knife (`whatever was seeded`) is ACCEPTED and answered — the seed inventory is clause (c)'s banked accounting, and "formation" enters only as constraint-surface bookkeeping, never as a formation-dynamics claim (keystone-LOCK untouched).

### §2.5 FORK 1 disposition (the variable-class collision)

The derivation ran entirely in the mechanical sector's own variables (u, π); it consumed NO u↔A / u↔E translation row. The register's live collision (def-uatk1s u↔A vs def-tk1xfm u↔E vs the six-row `x↔q` vs A↔momentum-class) is therefore NOT load-bearing for the four-tuple — it is routed as a register finding (the two SOLID rows cite each other as support without flagging the class conflict; `def-uatk1s:892`). Within THIS lane's structure the internal split is: dress-configuration `u₀` (pinned by BC-LAW), momentum `π` (carries the conserved Gauss function), grade `ε₁₁ = A(r)` (the Ax4 operating-point object, pinned by the elliptic solve of §4/§5) — three objects, each named at each use.

**G-LAW-2M: routes (a) Noether-continuum and (b) DEC-network (the discrete divergence of the literal double-curl force vanishes identically — R2 — with TH-5 honored: the incidence identity is bookkeeping, and the law's CONTENT is clauses (b)+(c), both named to their receipted homes) agree on the bin → item (i) DERIVED.**

---

## §3 — ITEM (ii): the no-signalling theorem

### §3.1 T1 — locality + characteristic structure

The receipted EOM is local. Its principal structure under Helmholtz decomposition: transverse sector — wave operator at speed c (R3 receipt: front at `0.9959c`, two-detector half-max arrival); longitudinal sector — NO spatial operator at all (`∇×∇×(∇φ) ≡ 0`): zero characteristic speed, receipt-exact (R3: a curl-free pulse moves NOTHING, `max|Δu| = 1.6e-19` over the full run; no detector ever triggers). **The LC-1 K=0 trap is answered structurally, not by tuning:** the imported W's longitudinal floor `v_L ≥ √(4/3)c` at K=0 comes from its deviatoric-restoring stencil acting on longitudinal patterns; the receipted potential HAS no such term — its potential is curl-keyed only. The difference is which operator the axioms wrote, and the toy runs BOTH: the K=2G-loaded control's longitudinal front is DETECTED at `1.8182c` (within 0.4% of the frozen `√(10/3)c = 1.8257…`), so the instrument provably sees the phantom where it exists and its absence where it doesn't (the prereg's liveness pair, both green).

### §3.2 T2 — constraint conservation, causal

`∂_t(∇·π) = −∇·j_m` is a LOCAL identity of the flow (R0c/R2). The constraint surface (BC-LAW values) is preserved step-by-step by local operations only; matter currents ride the defect/T2 sectors at ≤ c (banked). No global re-solve happens anywhere in the dynamics — the elliptic language of the STATICS is a solution method, not a propagation mechanism.

### §3.3 T3 — the energy estimate and domain of dependence

Energy density `e = ½ρ|u̇|² + ½ρc²|∇×u|²`; the receipted flow gives `∂_t e = ∇·𝐒` with flux `𝐒 = −ρc² u̇×(∇×u)` (vector identity, exact). By AM–GM, `|𝐒| ≤ c·e`. Standard shrinking-cone/Grönwall argument: data outside a ball of radius `r + c·t` cannot affect the ball of radius r at time t — **no energy, hence no information, crosses any surface faster than c, at any frequency.** The longitudinal sector appears in `𝐒` only through `∇×u`: purely longitudinal content contributes ZERO flux — its energy does not move at all (R3/R5 receipts: machine-zero transport). All inter-event transport rides the curl sector's c-cone.

### §3.4 The gravimeter scenario (FORK 2) — the real-field observability leg

The bound field is observable (Ax4: the grade modulates n(r)); a gauge escape is unavailable and none is used. The question the #935 Tier-2 left standing: when a distant source moves, does a local reading of the bias update acausally? **No — derived:** under the transverse+flat decomposition the receipted system is operator-identical to temporal-gauge Maxwell, where the moving source's convected dress is an EXACT solution whose far-field update is carried entirely by the curl sector (`∂_tE = c²∇×B`: the moving dress carries curl content ~ (V/c)·dress-gradient, and its curl-curl supplies precisely the convective `ü` the flat sector cannot supply itself — the boosted-Coulomb exhibit, transplanted verbatim because the operator is the same). A purely-flat far dress CANNOT update (`ü ≡ 0` there — R3); every update to θ, `∇·π`, or u at a field point is delivered by local matter current (§3.2) or by curl-sector arrival (§3.3), both inside the cone. A gravimeter reading the local grade sees the change no earlier than c allows. **FORK 2 lands on the causal branch.** (The §2 frozen sub-clause — a derived superluminal obstruction — did not fire; the branch was fireable and the K-loaded control shows what firing would have looked like.)

### §3.5 T4 — statement against LC-1's frozen cell

Frozen cell (`_orchestration/2026-08-04_lorentz-compliance-arc-brief.md:44`, verbatim `[sic]`): *"An energy-carrying inter-event channel at ≠ c ⇒ arc-level kill"*; `:59`: *"LC-1 runs first and its kill condition is arc-terminating."*

**Status established by this lane:** the bound/longitudinal sector of the receipted dynamics under BC-LAW is **not an energy-carrying inter-event channel at any speed** — its own characteristic speed is zero (T1, receipts), it carries zero energy flux (T3, the flux vector has no longitudinal term), and every observable it feeds updates only inside the c-cone (T3+§3.4). This is the demonstration the #935 Tier-2 found void, now derived: constrained-conservation legs (T2), retardation/domain-of-dependence (T3), the real-field observability case (§3.4) — with the finding-#1 knives self-applied: no step consumed the no-port vocabulary as a premise (Re(Z), "port", and "bound" appear above only in conclusions or banked quotes); the GR/EM parallels are carried WITH their disanalogy (GR and gauge-fixed EM escape via *pure gauge*; this field is real, and the escape here is zero-characteristic + curl-mediated updates — a different, derived mechanism); `clm-acdc07` is consumed nowhere. **Scope:** this lane STATES the theorem; LC-1's cell re-adjudication is the orchestrator's, triggered by the brief's frozen sentence — (i) DERIVED ∧ (ii) DERIVED — an arithmetic fact on the brief's words, labeled TRIGGERED, not derived.

**G-NOSIG-3: T1/T2/T3 derived + T4 stated verbatim; both liveness controls green → item (ii) DERIVED.**

---

## §4 — ITEM (iii): the energy functional

### §4.1 The crux, faced (finding #3 is correct)

The bare receipted Hamiltonian `H = ∫|π|²/2ρ + ½ρc²|∇×u|²` scores exactly ZERO on a static curl-free dress — both terms vanish. This is not an error to explain away; it is the statement that the WRITTEN action stores nothing in the constraint sector, for the same reason it contains no constraint (§1): the coupling that loads the constraint sector was never written. The functional below is the (i)-consistent completion.

### §4.2 The functional (route a: the Dirichlet form of the constraint solve)

> `E_bound = ∫ ½ κ D(A) |∇ε₁₁|² dV + ∫ |π|²/2ρ dV`, `κ = c⁴/7G`, `D(A) = 1/S(A)`.

**Derivation of the FORM:** the canon elliptic gravity solve `−∇·[κ D(A) ∇ε₁₁] = T₀₀` (`saturating-modulus-and-backreaction.md:50-52`; coded `backreaction.py:12-17`) is EXACTLY the Euler–Lagrange equation of the first term against the source coupling `∫T₀₀ ε₁₁ dV` — i.e., the corpus's working gravity statics has been extremizing this functional all along without its derivation. Under BC-LAW the constraint sector's stored energy IS this Dirichlet form: the response field's energy rides its GRADIENT structure. The `κ` VALUE stays imported (the G/ξ chain, #261 provenance unchanged); the FORM is the (i)-law's own variational shape — one structure, not two (the G-ENERGY-HOST consistency requirement: the functional's EL equation is the law's static limit; checked by inspection above).

**Why gradients and not the per-cell `A²` loading (the wrong candidate, killed by a receipt):** a naive per-cell reading (each loaded cell stores `∝A²`) diverges linearly at large r for the `A ∝ 1/r` grade AND contradicts canon's own rule that the absolute operating point is unobservable — *"only spatial gradients of A across the substrate are physically observable, not absolute per-node values"* (KB `CLAUDE.md`, INVARIANT-S2 operating-point paragraph). Uniform-A content is self-cancelling (relative-offset principle); what stores net, observable energy is the gradient structure. The Dirichlet form is the unique quadratic functional consistent with both the canon rule and the canon solve.

**Integrability + positivity (R4, exact):** for the Coulomb-class exterior the energy density is `∝1/r⁴`; `∫(B/r²)²4πr²dr = 4πB²(1/r_in − 1/r_out)` — finite outside any core, positive term-by-term. Cold-linear regime: `D(A) ≈ 1` exterior; the `D(A) → ∞` wall behavior is past-wall-adjacent and out of scope (declared).

### §4.3 Duty hosting (route b)

- **mass = A1:** hosted at the source coupling/caged core — the deposit clause's content is the functional's source term; `m c²` = the caged A1 content's energy (PR#260 banked, accounting unchanged).
- **Halo P9 added-mass:** hosted by the kinetic term `∫|π|²/2ρ` — the convected near-field's energy is KINETIC (stores on acceleration, returns on deceleration, zero steady drag — the deep-space reactive-bulk walk receipts, banked). Stores-and-returns: both terms are reactive; no resistive term exists (Ax3-lossless, `eq_axiom_3.tex:24` — legal).
- **Convection:** the functional is evaluated on fields that ride the source (§3.4's exhibit); its content moves with the source and radiates nothing on the longitudinal line (§3/§5).
- **Gauss-undeleted reality (G-SCALAR-REAL's duty):** the bound sector's energy is real, positive, localized — MORE substantive than a gauge artifact, and now with a functional, discharging the #935 finding-#3 gap that retired the original G-SCALAR-REAL PASS.

**G-ENERGY-HOST: derived FORM, (i)-consistent, crux resolved, all duties hosted → item (iii) DERIVED (FORM; κ VALUE imported unchanged).**

---

## §5 — ITEM (iv): the ν = 2/7 reconciliation (the honesty keystone)

### §5.1 The response function of the constrained sector

Drive a localized source `T₀₀(t) = T̄₀₀ e^{iωt}` (or a matter current `j_m` at frequency ω). The bound sector's response, from (i)+(ii)+(iii):

- **Near zone (banks):** the constraint solve — elliptic, the (iii)-functional's EL equation — evaluated on the instantaneous source, with corrections `O((ωr/c)²)` delivered by the curl sector (§3.4's mechanism). This response exists at EVERY ω including ω = 0; at ω = 0 it IS the static /7 chain: `ε₁₁ = 7GM/c²r`, the `1/7` projection, `θ = (3/7)ε₁₁` (R6 exact: `ν(K=2G) = 2/7`, `1 − 2ν = 3/7` — the trace-factor receipt now CITED by a verdict sentence, discharging the #935 #4/#17 disclosure). Every ingredient consumes ν as a STATIC input; the ν VALUE stays GR-imported (#261, byte-unchanged).
- **Far zone (does not radiate):** a `1/r` radiative term requires a finite-ω pole on the longitudinal line — a propagating eigenmode to carry it. The receipted dynamics has NONE at any ω (T1: zero characteristic speed; R1: `ω² ≡ 0`; R5: the driven receipted radial sector transports nothing, machine zero, while the K-loaded control radiates through the same instrument). No pole, no `1/r` term, no radiated power — at every drive frequency.

**The cut is therefore ZONE/POLE structure, not a frequency gate.** "Banks statically" and "does not radiate" are one derived fact — the constraint sector's transfer function has a full elliptic near-zone response and no radiative pole — not two behaviors with a tuned crossover. There is no frequency at which the static response switches off, and no frequency at which a radiative channel switches on. The Tier-2's "frequency-gated ontology" charge dissolves: nothing is gated; the same `W`-less structure serves both regimes because the two regimes read different TERMS of the response (near-zone `1/r²` vs far-zone `1/r`), and the second term does not exist.

### §5.2 The pulsar-independence receipt (G-CUT-DERIVED's dependency list)

Item (iv)'s complete input set: the receipted action (`eq_axiom_3.tex:18`); BC-LAW (§2); the Helmholtz decomposition; the energy estimate (§3.3); the canon elliptic FORM with its imported κ (§4); driver receipts R1/R3/R5/R6. **The pulsar comparators (`δ_HT`, `δ_DP`), the PM rate, and every observational bound appear NOWHERE in this chain** — swept over §5's text and the driver source by both engines: zero hits for the comparator tokens. The cut sits where the pole structure puts it; that the pulsars happen to listen on the pole-free side is a CONSEQUENCE, not an input. (What the pulsars DID adjudicate — the imported-K reading's self-exclusion — is #935's banked content, consumed here only as the reason the K-loaded control exists in the driver.)

### §5.3 Anti-reconstruction (the #261 fences, honored)

Nothing above claims K = 2G is geometrically forced (Gate 1's closed configuration — the z=4 Keating one-parameter family — is not re-argued) or constitutively forced (Gate 2's closed configuration — the SYM-branch `ρ = Z_eff²` invariance — is not re-argued). The static stiffness `κ = c⁴/7G` and `ν_vac = 2/7` remain VALUE-imports exactly as #261/#506 left them; this lane derives the FORM of the static response (the constraint's elliptic Dirichlet structure) and the ABSENCE of the radiative channel — neither touches the imported values, and the ½/¼-knife finds nothing suspiciously improved (the /7 numbers are byte-identical before and after). The `srs-band-structure.md:146` seam (the static import GENERATING the `√(10/3)` P-branch) is a CONSUMER of the phantom, already routed by #935's audit — this lane adds its mechanism sentence: a static ratio was fed to a wave operator the axioms never wrote.

### §5.4 Reading-B's owed mechanism (`port-register.md:91`), discharged

The register's debt: *"the corpus then owes a mechanism for why a mode that propagates freely at √(10/3)c in its linear passband does not radiate from a strong quadrupolar source."* Answer: **there is no such mode and no such passband in the receipted dynamics** — the `√(10/3)c` branch is a theorem of the imported W (the driver's control arm, where the instrument duly detects it at `1.8182c`), not of the axioms. The corpus owed a mechanism for a phantom's silence; the actual structure has nothing to silence. The debt transfers from "explain the suppression" to the R40 sweep's re-derivation queue for the register row itself (routed, not edited).

**G-CUT-DERIVED: placement derived from pole structure; dependency list pulsar-free; #261 gates untouched; /7 values byte-unchanged; Reading-B discharged → item (iv) DERIVED (FORM; values imported unchanged).**

---

## §6 — Consistency-vs-emergence ledger

| Quantity | FORM | VALUE | Class |
|---|---|---|---|
| Item (0) reading + repair | adjudicated this lane (routes α+β) | — | ADJUDICATION (Grant-ratification object; route-α algebra = DEMONSTRATED/entailed) |
| BC-LAW (item i) | **derived** this lane (Noether/DEC conservation + banked deposit + quiescence + uniqueness) | B↔M normalization rides imported G/ξ | derivation (FORM); consistency (VALUE) — meta-finding 5th instance |
| No-signalling theorem (item ii) | **derived** this lane (T1–T3 + §3.4) | — | derivation; Maxwell/GR-CLASS on this axis (peer, **no chord**) |
| Energy functional (item iii) | **derived** FORM (Dirichlet-of-the-law + kinetic) | κ = c⁴/7G imported | derivation (FORM) / consistency (VALUE) |
| The cut (item iv) | **derived** (zone/pole structure) | ν = 2/7, /7 chain imported, byte-unchanged | derivation (FORM) / consistency (VALUES) |
| Front speeds, ratios (driver) | receipts | 0.9959c; 1.8182c (control); 2/7; 3/7 | instrument receipts (liveness both directions) |
| LC-1 cell eligibility | arithmetic on the brief's frozen sentence | — | TRIGGERED (entailed; not derived; orchestrator's to run) |

No emergence-class claim. **No chord on any outcome** (prereg §0 row 8: success makes the bound sector Maxwell/GR-class — peer, the opposite of distinct). Mints nothing; edits no leaf; changes no solidity.

## §7 — The frozen gate table (UNRUN ≠ PASSED)

| Gate | Frozen criterion (prereg §7) | Measured | Score |
|---|---|---|---|
| **G-QUOTE** | every ruled/frozen quote byte-checks, two engines | LC-1 `:44`/`:59` + brief grammar/addendum re-verified by direct `sed` at freeze; sweep quotes byte-verified by the sweep's two engines; §-quotes above carry file:line | **PASS** |
| **G-AX0-2M** | routes agree; repair drafted; audit complete | §1: α+β agree (temporal-gauge-literal); repair §1.3; audit §1.4 (77 sites, counts pinned; PATTERN-BOUNDED disclosed) | **PASS** |
| **G-LAW-2M** | both routes; preimages enumerated; TH-5 + four-lock + flat-direction knives applied; pinned object declared | §2: Noether-continuum + DEC-network agree; the multiplier-preimage question answered by CLASS derivation (§2.3); knives at §2.3/§2.4; objects named per use | **PASS** |
| **G-NOSIG-3** | T1/T2/T3 derived, T4 verbatim, controls green, knives self-applied | §3; controls: transverse 0.9959c, control-P detected 1.8182c, longitudinal static 1.6e-19, receipted radial machine-zero | **PASS** |
| **G-ENERGY-HOST** | derived, (i)-consistent, crux resolved, duties hosted | §4; EL-equation identity checked by inspection; R4 exact | **PASS** |
| **G-CUT-DERIVED** | placement derived; dependency list pulsar-free; #261 untouched; /7 unchanged; :91 answered | §5.1–§5.4 | **PASS** |
| **G-SECTOR** | no micro-rotation routing; TWO-3s; two-object split maintained | checked at §1–§5: zero Cosserat-channel consumption; dress/grade named per use | **PASS** |
| **G-SHEAR-UNTOUCHED** | T2 byte-untouched | photon/GW sectors cited as banked only; no re-derivation, re-scaling, re-anchoring | **PASS** |
| **G-BANKED** | banked inputs never relitigated; challenge-receipts on closed-negative contact | #935 knives consumed as banked (§1–§2); #261 contact carries §5.3; four-lock contact carries §2.4; R24 untouched (FORK 1 de-fanged §2.5); keystone-LOCK untouched (§2.4) | **PASS** |
| **G-ENGINE-FLAG** | `git diff --stat base..HEAD -- src/` empty | empty at every commit of this lane | **PASS** |
| **G-NUM** | numerals machine-verified; mutation receipt fires; `make verify` green in worktree | number check: 20 checks green; `--mutation-receipt` fires (2 detectors); runs byte-identical (`0dbf1a58…`); `make verify` at result commit | **PASS** (verify receipt at commit) |

## §8 — Verdict assembly, routing

**VERDICT (per-item, no aggregation, pre-Tier-2):** **(0) ADJUDICATED** (recommended: temporal-gauge-literal; repair + audit → Grant). **(i) DERIVED.** **(ii) DERIVED.** **(iii) DERIVED (FORM; κ imported).** **(iv) DERIVED (FORM; values imported).**

Routing:
1. **Item (0) repair proposal + the D1–D4 drift findings + the register variable-class collision (§2.5) + the ch05 flags (§1.4) → Grant/orchestrator** (ratification objects; flag-don't-fix throughout — zero corpus edits made).
2. **(i)+(ii) both DERIVED-class → the LC-1 frozen-cell re-adjudication is TRIGGERED per the brief's frozen sentence** — the orchestrator's move, not this lane's.
3. **(iii)+(iv) → the R40 demotion sweep as routed input** (the sweep's NEEDS-RE-DERIVATION rows now have the derived FORM to re-derive against); the `port-register.md:91` debt-transfer and the `srs-band-structure.md:146` mechanism sentence ride the same routing.
4. **Tier-2 (this lane's own, before any CLEARED wording):** pre-flagged primary targets — the §2.2 deposit-leg's use of PR#260 (accounting vs derivation), the §2.3 class-derivation (does it quietly reconstruct the assertion?), the §3.4 operator-identity transplant (is the mechanical/Maxwell isomorphism load-bearing beyond the shared operator?), the §4.2 gradient-vs-A² adjudication, and the §5.2 pulsar-independence sweep's completeness.

---

> **Result-doc provenance.** Frozen prereg committed ALONE + pushed at `ac6a176c` (2026-08-10T13:36:55Z) before any derivation content, driver code, or lane number existed — byte-untouched since. Driver committed before this result; two full runs byte-identical (sha256 `0dbf1a58cb60387dea8f06e6f4efb21e4fea2a75c59340bd8dde6ddf9b304027`). Two-method receipts as scored: symmetry algebra = sympy exact + fixed-seed float; conservation = Noether-symbolic + DEC-numeric; fronts = purpose-built toy with known-good AND known-violating controls; sweeps = BSD grep + Python re (GNU-grep substitution disclosed). Engine `src/ave` byte-untouched. Past-wall out of scope at every use. `[DO-NOT-MERGE][REVIEW: pending-orchestrator]`. Companions: the frozen prereg, the brief + R41, #935 at its merged home, LC-1 @ `be04ea03` (branch state), the #261 record, PR#260/`eq_axiom_4.tex`, the four-lock cascade leaf, the consumer-sweep record.
