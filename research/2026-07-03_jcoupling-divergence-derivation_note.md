# The β arc — deriving J_coupling from Axiom 1 and computing ∇·J_coupling on the srs DEC

**Epic:** EM-readout derivation — Stage-2b entry condition. **Arc:** β (the axiom-native LC coupling current).
**Branch:** `analysis/jcoupling-divergence-derivation`. **Kind:** ANALYTIC note + scratch DEC computations. NO instrument build.
**Prior (read FIRST):** `research/2026-07-03_em-readout-stage2b-step0-continuity_note.md` — reduced the whole dynamical route to one term: `d/dt(∇·E) = −∇·J_coupling`, so Stage-2b lives or dies on whether `∇·J_coupling ≢ 0`. That note LEANED dead-by-`∇·∇×≡0` but flagged the coupling FORM as a framing question requiring a proper derivation (§4, `flag-don't-fix`). This note settles it by DERIVATION + computation on the exact srs `∂₁/∂₂`, not by assumption.

**Disciplines:** `substrate-native-check` (operators are the srs/K4-native DEC `∂₁,∂₂`, not Cartesian — walked before any computation) · `verify-before-cite` (every file:line re-verified at HEAD this session, log §7) · `ave-prereg` (swept the existing coupling zoo BEFORE deriving fresh — §3) · `phase-space-coordinate-check` (the circulator candidate lives in mode-amplitude phase-space, not real-space field — §3.1) · `flag-don't-fix` (two computed corrections to my own intermediate reasoning surfaced verbatim, §5) · `consistency-vs-emergence` (this is a FORM/structural analysis; no value claim).

---

## 0. OUTCOME BINS (frozen BEFORE deriving)

- **[J-MIXED-EXISTS]** — an axiom-derived coupling with `∇·J ≢ 0` that evades all three closures (not pure curl, not a static texture, not a propagating longitudinal mode). Name the term, its provenance chain, the hardest-ledger row. Stage-2b revives with THIS term as the transducer.
- **[NO-AXIOM-NATIVE-TERM]** — every axiom-licensed coupling is either divergence-free or already-closed. The dynamical route closes at derivation grade; the epic routes to Z (harmonic) + W (winding pairs) definitively.
- **[STUCK-FRAMING]** — a fork the axioms cannot settle; surface to Grant.

**LEAN (recorded before computing, from the Stage-2b note + the coupling-zoo sweep):** likely NO-AXIOM-NATIVE-TERM at the *net-monopole* level, with a live-but-neutral J-mixed term at the *local* level — the discriminating question is whether "sources ∇·E" means net enclosed charge (monopole) or a bound-charge texture (polarization). Bin chosen only after §4–§5.

---

## 1. THE AXIOM-1 NODE, AS CANON STATES IT (the derivation's ground)

`eq_axiom_1.tex:25` (verbatim, verified §7): each node carries **six intrinsic DOF — three translational (capacitive coupling ε₀, identified with E) and three microrotational (inductive coupling μ₀, identified with B)** — and *"the intrinsic translation ↔ E, rotation ↔ B coupling makes every node a native LC oscillator."* `axiom-definitions.md:16` restates identically.

So the per-node structure is a literal LC tank:
- **C-branch (capacitive):** the 3 translational DOF `u ↔ E/ε₀`. Charge-like variable `Q_node = C·V`, energy `½ε₀E²`.
- **L-branch (inductive):** the 3 microrotational DOF `ω ↔ B/μ₀`. Flux-like variable `Φ_node = L·I`, energy `½μ₀⁻¹B²`.
- **Coupling:** the two branches share the node. Energy trades C↔L at the LC rate.

**The coupling current is the derived object.** In an LC tank, the current that flows from the L-branch into the C-branch is `I = dΦ/dt` routed through the shared node — the rate the inductive (rotational/B) sector charges the capacitive (translational/E) sector. On a lattice this is a *field*: `J_coupling(node)` = the per-node E-sector source sourced by the neighbouring rotational flux. This is the term that appears in the Ampère-role update (Stage-2b note eq. I):

```
∂_t(ε_eff E)  =  +∇×(μ_eff⁻¹ B)  −  J_coupling            … (I)
```

**Per-term ledger of the node structure:**

| Step | Content | Ledger |
|---|---|---|
| node = LC tank (C=translational/ε₀, L=microrotational/μ₀) | `eq_axiom_1.tex:25` verbatim | **AXIOM-DERIVED** |
| E ↔ u (translational), B ↔ ω (microrotational) | `eq_axiom_1.tex:25` | **AXIOM-DERIVED** |
| coupling = rate the L-branch charges the C-branch at the shared node | LC-tank definition | **AXIOM-DERIVED** (structural) |
| the specific FORM of `J_coupling(ω)` on the lattice | NOT fixed by the axiom sentence — the axiom names the *coupling exists*, not its stencil | **ENGINEERING-CHOICE** (the fork §2) |
| a shared `(V_inc, V_ref)` phasor between the two "3"s | `master-equation.md:20` — the A1⊥T2 fence, genesis-24 no-double-count guard | **FORBIDDEN-INSERTION** |

The last row is load-bearing: canon forbids wiring the winding into the breather's own phasor. So `J_coupling` must be a *cross-sector Hamiltonian coupling* (`device-circuit-models.md:201`: "grades may couple ONLY through a conserved energize-lock Hamiltonian pair, NEVER a shared (V_inc, V_ref) phasor"), not a phasor merge.

---

## 2. THE FORM FORK — three structurally distinct `J_coupling(ω)` (Stage-2b note §3, re-derived)

The axiom fixes that the coupling exists and is cross-sector; it does NOT hand us the stencil. The stencil is a fork with three structurally distinct branches, each with a determinate divergence on the DEC:

- **(J-curl)** `J = curl_adj(g·ω)` — the Ampère form: B drives E as a curl. `g = g(A)` a saturation weight applied **at the source** (a face/circulation weight, before the curl).
- **(J-grad)** `J = grad(h(A))` — a longitudinal drive, gradient of a saturation scalar.
- **(J-mixed)** `J = W(A) ⊙ curl_adj(ω)` — a curl of the rotational field, then multiplied **at the field point** (an edge/real-space weight `W(A)`, applied AFTER the curl). Neither pure curl nor pure grad. **This is the ONLY structurally-new candidate** and, crucially, it is exactly the FORM the corpus's existing shear↔bulk converters already carry (§3.2).

The Stage-2b note's decisive reduction (its §2): take `∇·` of (I). By the DEC theorem `div∘curl_adj = −∂₁∂₂ = 0` (`srs_dec.py:242` verbatim: *"any F=curl_adj(anything) has div F ≡ 0, hence zero enclosed charge"*), the `∇×(μ⁻¹B)` term drops, so **`∂_t(∇·(ε_eff E)) = −∇·J_coupling` exactly**. The entire continuity behaviour is `∇·J_coupling`. Compute it per branch.

---

## 3. SWEEP OF CANON'S EXISTING COUPLING CANDIDATES (ave-prereg — done BEFORE deriving fresh)

Grepped and read the corpus's coupling constructions. Each classified by (i) where its divergence lives, (ii) its ledger class, (iii) whether it evades all three closed routes.

### 3.1 The skew-Hermitian circulator (PR #321, `node_circulator_coupling.py`, `device-circuit-models.md:203`)

**Structure:** a 2×2 (or 3×3) HERMITIAN generator `d/dt[a_bulk; a_shear] = −iH[a_bulk; a_shear]` acting on **complex MODE AMPLITUDES** `a = q + i·p/ω` — the analytic signal of an LC reactance pair (`node_circulator_coupling.py:39-51`). **This is a 0-dimensional (lumped) coupling: it rotates two scalar amplitudes.**

- **`∇·` verdict:** N/A — there is no spatial current to take a divergence of. The circulator couples mode energies, not a field. **`phase-space-coordinate-check` flag:** it lives in the (V_inc, V_ref)/impedance-plane mode-amplitude phase-space (A46), NOT the real-space E-field. It cannot appear in the `∇·E` continuity equation at all — it is a different object.
- **Ledger:** the skew form is FORCED trivially (lossless ⇒ Hermitian generator); the non-reciprocity SIGN is lattice-sourced (chirality χ) but the MAGNITUDE is IMPOSED (`forced_vs_imposed()` verdict, `node_circulator_coupling.py:561-566`). Verdict PARTIAL / ECHO-at-magnitude.
- **Evades the three closures?** Vacuously — it is not a spatial current, so "not pure curl / not static texture / not longitudinal mode" don't apply. **It is NOT a `J_coupling` candidate for the ∇·E question.** (It is the right object for the *mode-energy* Fork-A, a different question.)

### 3.2 The gyrotropic converter + trilinear buckle (`cross_sector_coupling.py`, graft-v3/v4)

**This is the live J-mixed FORM.** `gyrotropic_converter_forces` (`cross_sector_coupling.py:66-90`):
```
f_V = −κ̃ · g_front · Ω_w ,   Ω_w = (∇×w)·x̂
```
and `trilinear_buckle_forces` (`:110-152`): `f_V = −κ̃ · g_wall · (w·∇×ω)`.

The E-sector source `f_V` is **a saturation-front window `g(A)` multiplying a curl of the rotational field.** In DEC terms this is `W(A) ⊙ curl_adj(ω)` with `W(A)=g` an A1-sector saturation scalar applied at the field point — **exactly the (J-mixed) branch.**

- **Ledger:** the converter is adjudicated (A44, Grant 2026-06-09, `crystal_engine.py:225`, `cross_sector_coupling.py:9-11`) as *"an Axiom-1 non-centrosymmetry consequence — engine-completeness, NOT a new postulate."* `κ̃ = pq/(p+q) = 6/5` is α-free. **So the FORM is AXIOM-DERIVED (Axiom-1 non-centrosymmetry); the magnitude κ̃ is α-free-topological.** This is the hardest-ledger row of the whole arc — see §6.
- **`∇·` verdict:** computed §4 — LOCALLY nonzero, globally neutral.
- **Evades the closures?** Not pure curl (the weight breaks co-exactness). Not a *static* texture — it fires on the evolving ω (its divergence is time-dependent through ω's Faraday evolution). Not a propagating longitudinal mode — it is a saturation-gated bound-charge source, confined to the front `g(A)`, not a free `∇h` wave. **It evades all three — at the LOCAL level.** The catch is §4's global result.

### 3.3 Genesis-24 / k4_cosserat_coupling Lenz addendum (`k4_cosserat_coupling.py`)

**Structure:** the coupling is the GRADIENT of a scalar reflection-energy `L_c = (V²/V_SNAP²)·W_refl(u,ω)` (`k4_cosserat_coupling.py:112-124`); the force is `∂L_c/∂(u,ω)`, and the reciprocal EMF is `−2·V_inc·∂L_c/∂V_sq` with a Lenz back-EMF sign (`:843-855`). This is a **potential-gradient** coupling — structurally the (J-grad) family (source = grad of a saturation scalar).
- **Ledger:** the `∂L_c/∂(u,ω)` channel is flagged **A28-redundant with Op14** and drives the empirical runaway (`:274-285`, `disable_cosserat_lc_force`). The Lenz-EMF path is OFF-by-default (double-counts Op14's varactor).
- **`∇·` verdict:** (J-grad) ⇒ `∇·(grad h) = ∇²h ≠ 0` — but this is the RETIRED static-texture mechanism (Stage-2a `[NO-FLUX-STRUCTURAL]`) OR a forbidden propagating longitudinal drive. Does NOT evade the closures (Stage-2b note §3 J-grad). Not a new transducer.

### 3.4 The chiral-lattice pitch coupling (I4₁32 screw) — the most substrate-native J-mixed candidate

The directive singled this out: *does the srs chirality license a term mixing curl and non-curl content?* The srs net IS chiral (`chiral_lattice.py:47-75`, both enantiomorphs). **Computed §4.3 — verdict below is decisive and NEGATIVE.**

---

## 4. THE COMPUTATION — ∇·J on the exact srs DEC (`src/ave/topological/srs_dec.py`, merged)

Scratch drivers (`scratchpad/dec_probe{,2,3,4}.py`, not committed — this is a note). srs `L=3` supercell: nodes=216, edges=324, faces=324; Betti `(b0,b1,b2)=(1,3,218)`. Operators are the exact integer `∂₁/∂₂`; `div=−∂₁`, `grad=∂₁ᵀ`, `curl_adj=∂₂`. `div∘curl_adj` on the operator = **exact 0** (theorem confirmed).

### 4.1 Per-form divergence (random cochains)

| Form | `max\|div J\|` | Verdict |
|---|---|---|
| (J-curl) `J = curl_adj(ω_face)` | `2.0e-15` | **≡ 0** (machine) — dies by the theorem |
| (J-curl-wS) `J = curl_adj(S_face·ω_face)` (weight AT SOURCE) | `1.8e-15` | **≡ 0** — source-weighting stays co-exact, still dies |
| (J-grad) `J = grad(h_node)` | `1.1e+01` | ≠ 0 but longitudinal/static-retired (§3.3) — closed |
| **(J-mixed) `J = W(A) ⊙ curl_adj(ω_face)`** (weight AT FIELD) | **`8.4e+00`** | **≠ 0** — the weighted curl is NOT co-exact |

**The decisive structural fact:** applying the saturation weight `W(A)` **after** the curl (at the edge/field point) breaks co-exactness and sources `div J ≠ 0`; applying it **before** (at the face/source) does not. The gyrotropic/trilinear converters (§3.2) are the AFTER form. So a genuinely axiom-derived (A44) coupling DOES carry `∇·J ≠ 0`. **(J-mixed) is live at the local level.** Hodge split: `‖exact part‖/‖J‖ = 0.48` — nearly half the weighted-curl is a gradient (charge-sourcing) component.

### 4.2 The global-vs-local discriminator (the load-bearing correction — `flag-don't-fix`)

Summing the sourced charge density `ρ = div J` over the closed periodic complex:

```
sum(ρ)   = +0.0e+00   (exact)      ← TOTAL enclosed charge
sum|ρ|   =  128.0                   ← total UNSIGNED charge (the texture is real)
max|ρ|   =  2.78                    ← peak local density
```

**`∇·J_coupling` is LOCALLY nonzero but sums to EXACTLY ZERO.** Structural reason (computed + proven): `sum(div J) = 1ᵀ(−∂₁)J = −(∂₁ᵀ1)ᵀJ = −(grad 1)ᵀJ = 0`, because `grad(1) = 0` (a constant 0-cochain has zero gradient). **On the closed periodic srs, Gauss-with-no-boundary forces the total charge of ANY current to zero.** The weighted-curl sources a globally-neutral ± bound-charge texture — a **polarization / form-factor**, NOT a net monopole.

Sub-region check (localized support, `dec_probe4.py`): a Gauss pillbox `r < 0.25 rmax` reads `Q_enclosed = +0.63`; `r < 0.6 rmax` reads `+0.0096`; the running integral `Q(r)` **rises to ±0.6 at finite r then returns to 0 at the boundary.** This is precisely a multipole/form-factor charge distribution — the signature of BOUND (polarization) charge, not free monopole charge. A net monopole would need `Q(r→∞) ≠ 0`, i.e. charge flux leaving the domain (an open sink / a source at infinity), which the axiom-native coupling does not supply.

### 4.3 CHIRALITY-SPECIFIC verdict (the directive's flagged candidate)

Two honest results, one a **correction to my own intermediate reasoning** (`flag-don't-fix`):

1. **Both enantiomorphs source the IDENTICAL local-charge texture.** RH: `max|ρ|=2.78`, `sum(ρ)=0`. LH: `max|ρ|=2.35`, `sum(ρ)=0`. The weighted-curl divergence is NOT unique to chirality — the achiral diamond would source the same neutral texture. **The screw does not manufacture a net-monopole `∇·J` that the weight doesn't already give (and the weight only gives a neutral texture).**
2. **CORRECTION (surfaced verbatim):** an intermediate probe (`dec_probe2.py` Q3b) computed `div_R(curl_adj_R(ω) − curl_adj_L(ω)) = 10.5 ≠ 0` and I nearly read it as "chirality sources divergence." **This is a cross-complex CATEGORY ERROR** — `curl_adj_L` is the boundary map of a DIFFERENT complex (different faces), so `div_R` applied to its output is not a within-complex operation and the nonzero is meaningless. Corrected in `dec_probe3.py`: within EACH complex, `sum(ρ)=0` and the chirality-difference of a proper single-complex current is div-free. **Chirality does NOT license a curl-mixing term with net divergence.** The chirality-candidate is CLOSED-NEGATIVE for the net-charge question.

### 4.4 The harmonic sector (why lane Z is still the survivor)

`b1 = 3` harmonic 1-cochains (the three T³ handles) are in `ker(div) ∩ ker(curl)` by definition — so `div(harmonic) = 0` too. The harmonic sector carries **HOLONOMY (loop flux around non-contractible cycles), NOT enclosed charge.** This confirms the Stage-2b note's lane-Z routing: net-charge-like emergence, if anywhere, lives in the loop-holonomy sector as a linking/winding invariant — invisible to the `∇·E` monopole channel entirely, and requiring an edge-field (1-cochain) readout, not a node-potential.

---

## 5. THE ANSWER — bin, chain, verdict

### 5.1 The derivation chain (summary)

1. Axiom 1 ⇒ node = LC tank, C=translational/E, L=microrotational/B, coupled at the shared node (`eq_axiom_1.tex:25`, AXIOM-DERIVED).
2. `J_coupling` = the rate the L(ω/B)-branch charges the C(u/E)-branch — a cross-sector Hamiltonian coupling (A1⊥T2 fence forbids a shared phasor; `master-equation.md:20`, `device-circuit-models.md:201`).
3. The FORM is a three-way fork; only (J-mixed) `W(A)⊙curl_adj(ω)` is structurally new (ENGINEERING-CHOICE among axiom-consistent stencils).
4. The corpus already carries (J-mixed): the gyrotropic/trilinear converter, adjudicated A44 as an Axiom-1 non-centrosymmetry consequence (AXIOM-DERIVED form, α-free κ̃).
5. On the exact srs DEC: (J-mixed) sources `∇·J ≠ 0` **LOCALLY** (weight-after-curl breaks co-exactness; Hodge exact-fraction 0.48).
6. **BUT** `sum(∇·J) = 0` exactly (Gauss-no-boundary on the closed complex): the sourced charge is a globally-NEUTRAL polarization/form-factor texture (`Q(r)` rises then returns to 0), NOT a net monopole.
7. Chirality does not change this (both enantiomorphs give the identical neutral texture; the chiral-difference net-divergence was a cross-complex category error, corrected).
8. The net-charge sector is the harmonic `b1=3` holonomy — div-free, loop-flux not enclosed-charge, invisible to `∇·E`.

### 5.2 BIN

**[NO-AXIOM-NATIVE-TERM] — at the net-monopole (Coulomb-charge) grade, with a named live term at the polarization grade.**

The precise verdict, honestly split:

- **For the electron's net Coulomb charge (the Stage-2b target):** NO axiom-native `J_coupling` sources a NET `∇·E` monopole. Every axiom-licensed coupling either (a) is divergence-free by the `∇·∇×≡0` theorem (pure/source-weighted curl, and the harmonic sector), (b) is the retired-static / forbidden-longitudinal (J-grad), or (c) — the one that DOES source local `∇·J` — sums to exactly zero (a neutral bound-charge texture, not a monopole). **The dynamical route to the electron's net Coulomb field closes at derivation grade.** Net charge is a topological (linking/winding) quantity in the harmonic sector, per Axiom 2 (charge = winding), NOT a monopole sourced by the LC coupling current. This is fully consistent with — and independently re-derives — the Stage-2a `[NO-FLUX-STRUCTURAL]` static negative and the corpus's charge-as-winding ontology.

- **A genuinely-new term DOES exist, but it is NEUTRAL:** the (J-mixed) weighted-curl `W(A)⊙curl_adj(ω)` (the A44 converter form) sources a local, globally-neutral, saturation-gated polarization charge density. This is NOT the electron's monopole, but it IS a real axiom-derived cross-sector transducer — the natural home of a **bound-charge / vacuum-polarization form factor** around a winding, not a source of net charge. Named here so it is not lost.

**Routing (confirming the Stage-2b note):** route the epic to **lane Z** (harmonic/holonomy — net charge as a linking invariant on the `b1=3` handles, edge-field 1-cochain readout with the DEC harmonic projector) **+ lane W** (winding pairs, `clm-wcoul2`). Do NOT build the Stage-2b settling test on a `∇·E`-monopole target — it is derivation-dead. IF a settler is ever built for the *polarization form-factor*, the (J-mixed) A44 converter is its term and §6 is its hardest ledger row.

### 5.3 The hardest-ledger row (as required by the bins)

The (J-mixed) converter's FORM is adjudicated AXIOM-DERIVED (A44: Axiom-1 non-centrosymmetry, `crystal_engine.py:225`). **The hardest row is whether "Axiom-1 non-centrosymmetry" genuinely LICENSES the weight-AFTER-curl ordering** (which sources local `∇·J`) versus the weight-AT-SOURCE ordering (which stays div-free). The A44 ruling asserts the converter is engine-completeness, but the DEC computation shows the two orderings are physically distinct (one sources bound charge, one does not) — and the axiom sentence does not itself fix the ordering. **That ordering is the ENGINEERING-CHOICE the axiom under-determines**; it does not affect the bin (both orderings give zero NET charge), but it IS the load-bearing choice for any polarization-form-factor claim. Surfaced, not resolved.

---

## 6. WHAT THE CHILD ARC WOULD DECIDE (flag to Grant / orchestrator — NOT resolved here)

One framing question the axioms under-determine, surfaced per `flag-don't-fix` (not steered):

**Is the electron's Coulomb field a NET-MONOPOLE `∇·E ≠ 0` object at all, in AVE?** This note shows the LC coupling current cannot source a net monopole (Gauss-no-boundary + charge-as-winding). Two readings, and the axioms alone do not pick:
- **(a) Charge is purely topological (harmonic/winding), and the "Coulomb field" is the far-field of a holonomy** — then there IS no monopole `∇·E` to source, the Stage-2b `∇·E` target was mis-posed, and lane Z is the whole answer. (This is the reading most consistent with Axiom 2 charge=winding + `clm-wcoul2`.)
- **(b) Charge is a net monopole that the substrate sources at an OPEN boundary / core defect** — then the closed-complex Gauss result is an artifact of periodicity, and the real test needs an open domain with a core sink. But that sink is not an axiom-native LC coupling; it would be a new postulate.

Reading (a) is the strong lean (it needs no new postulate and matches canon). But it is a FRAMING call about what "the electron's charge" IS, which routes to Grant, not to a unilateral build. **This is the STUCK-FRAMING residue of an otherwise-decisive NO-AXIOM-NATIVE-TERM bin** — the bin is clean; only the *interpretation of the target* has a fork.

---

## 7. verify-before-cite log (all re-verified at HEAD this session)

| Anchor | Verification |
|---|---|
| `eq_axiom_1.tex:25` | "native LC oscillator"; six DOF (3 translational/ε₀/E ⊥ 3 microrotational/μ₀/B) ✓ |
| `axiom-definitions.md:16` | same DOF map ✓ |
| `srs_dec.py:242` | `div∘curl_adj = −∂₁∂₂ = 0 ← THE THEOREM ... hence zero enclosed charge` verbatim ✓ |
| `master-equation.md:20` | A1⊥T2 fence, "never wire the winding into the breather's own phasor (V_inc,V_ref)" ✓ |
| `device-circuit-models.md:201` | "grades may couple ONLY through a conserved energize-lock Hamiltonian pair, NEVER a shared (V_inc,V_ref) phasor" ✓ |
| `device-circuit-models.md:203` | circulator PARTIAL, 4 gates PASS, magnitude imposed ✓ |
| `cross_sector_coupling.py:9-11,66-90` | A44 "Axiom-1 non-centrosymmetry consequence"; `f_V=−κ̃·g·Ω_w`, `Ω_w=(∇×w)·x̂` ✓ |
| `crystal_engine.py:225` | A44 "CONSEQUENCE / engine-completeness of Axiom-1 non-centrosymmetry" ✓ |
| `node_circulator_coupling.py:39-51,561-566` | mode-amplitude generator; forced-vs-imposed ECHO-at-magnitude ✓ |
| `k4_cosserat_coupling.py:112-124,274-285,843-855` | gradient-of-L_c coupling; A28-redundant; Lenz-EMF OFF-default ✓ |
| DEC computations | `scratchpad/dec_probe{,2,3,4}.py` on merged `srs_dec.py`, shared `.venv` ✓ |

**Disciplines applied:** substrate-native-check (DEC not Cartesian) · verify-before-cite (this log) · ave-prereg (§3 zoo swept before §4 fresh derivation) · phase-space-coordinate-check (circulator flagged as mode-amplitude, §3.1) · flag-don't-fix (§4.2 global-vs-local + §4.3 category-error correction surfaced verbatim; §6 framing fork to Grant) · consistency-vs-emergence (FORM analysis, no value claim). **NO instrument build — note + scratch only, per the arc charter. Stage-2b revival gated on orchestrator review.**
