# Cosmic-ε / DE Projection Scoping Epic

**Status**: ACTIVE — Session 2 (projection-mechanism derivation) ready to spawn; Session 1 CLOSED 2026-05-19 EOD via merge `af8c522` + audit tag `audit/2026-05-19_cosmic-epsilon-de-projection-scoping`
**Last updated**: 2026-05-19 EOD
**Originating session**: Orchestration session post-batch (γ A-034 catalog ε/μ extension + E-field-as-overbracing identification + projection-vs-measurement conflation catch)

## Grant adjudications 2026-05-19 EOD (resolves Session 1 plumber-physical questions Q1/Q2/Q3)

**Q1 — DE static vs dynamic? → DYNAMIC** (water-crystallization analogy lands cleanly). The Friedmann static-Λ limit corresponds to "ice in equilibrium" post-crystallization-front; AVE's DE is the crystallization happening NOW at the cosmic horizon — substrate still phase-transitioning, latent heat still being released. Class E framing already encodes this as ongoing operating-point process at $u_0^*$.

**Q2 — Op14 cosmic-horizon profile?** Op14 IS canonical at Vol 1 Ch 6 §1.13: $Z_{\text{eff}} = Z_0/\sqrt{S(A)}$ — substrate impedance modulated by saturation kernel. Three canonical leaves exist. **The cosmic-horizon-scale profile is the missing piece** — analog of `frame-dragging-impedance-convolution.md:20`'s Kerr-interior profile, but for cosmic-horizon saturation rather than BH event horizon. Session 2 derives THIS profile, NOT a new operator. Per `ave-canonical-leaf-pull` v1.2 trigger 16: **(c)-operator-application** at a new scale.

**Q3 — α/β/γ verdict? → γ (composite Class E + ASYM-N(ε))**. Both axes complementary:
- Class E captures the joint-constraint structure at operating-point $u_0^*$ (DE is one of N joint observables of $\{G, H_\infty, \hat{\Omega}_{\text{freeze}}, \alpha\}$)
- ASYM-N(ε) cosmic-row captures the saturation-mechanism class (cosmic-ε saturation companion to Row 14 K4-crystallisation-SYM*; fills the gap-cell in γ catalog extension)
- Together: complete framing without overcommitment to either single axis. If "thermodynamic latent-heat flow" 4th-category turns out load-bearing later, Session 2 can extend.

## Why this exists

Multiple converging threads from 2026-05-19 EOD orchestration have surfaced an unsettled structural question: **what IS dark energy in AVE's framework, structurally?**

Threads converging:

1. **Cosmic-ε gap-cell** flagged in γ catalog extension at commit `6436d65`: A-034 has ASYM-N(μ) at galactic scale (MOND), no ASYM-N(ε) at any cosmic-scale row. DE candidacy for that gap.
2. **DE-as-saturated-capacitor intuition** (Grant 2026-05-19 EOD initial framing — was DE the ε-sector cosmic analog of MOND-μ?)
3. **RMS→DC framing pushback** (orchestration response, Grant accepted: substrate-scale RMS gives wrong magnitude, ε-sector cosmic-row needs different mechanism)
4. **E-field-as-over-bracing identification** (Grant 2026-05-19 EOD): per Ax 1 Cosserat translational DOF, the bond over-bracing $u_0^*$ in $\hat{\Omega}_{\text{freeze}}$ direction IS a static E-field component at substrate scale. Sets universal stiffness via magic-angle.
5. **Projection-vs-measurement conflation catch** (Grant 2026-05-19 EOD): orchestration was demanding magnitude-equality between raw substrate E-field energy and cosmic-scale DE measurement. This is QFT-style cosmological constant problem framing. AVE doesn't have to inherit it. **DE measurement is a projection of bulk substrate dynamics, NOT a sum of raw microscopic field energies.**

The structural question: **how does DE measurement (cosmic-scale observable) project from the substrate's dynamics (over-bracing static field + ongoing K4 crystallisation at horizon + Class E operating-point structure)?**

Until this is settled at a scoping level, ANY downstream classification ("DE is Class E", "DE is ASYM-N(ε)", "DE is the latent-heat-of-crystallisation observable", etc.) is built on an unverified projection chain.

## Scope (multi-session research arc)

| Session | Deliverable | Effort | Status |
|---|---|---|---|
| 1 | Scoping research doc (Q1/Q2/Q3 surfaced + (a)-(e) classification + projection-chain inventory) | 1-2 hr | **CLOSED 2026-05-19 EOD via merge `af8c522` + audit tag `audit/2026-05-19_cosmic-epsilon-de-projection-scoping`** |
| **2 (this session)** | **Op14 cosmic-horizon profile derivation + projection-chain trace + γ (composite Class E + ASYM-N(ε)) catalog row addition** | 4-8 hr | ACTIVE — ready to spawn |
| 3 | Downstream walk-back if Session 2 reveals corpus framing inconsistencies (`cosmological-constant-closure.md` framing reconciliation per anomaly A2 from Session 1) | 1-2 hr | QUEUED |
| 4 (conditional) | 4th-category framing if "thermodynamic latent-heat flow" surfaces as load-bearing during Session 2 | TBD | CONDITIONAL |

## Session 2 (this session) — implementor brief

### Goal

Three concrete deliverables (per Session 1 Q1/Q2/Q3 adjudications):

1. **Op14 cosmic-horizon saturation profile leaf** at `manuscript/ave-kb/vol3/cosmology/ch04-generative-cosmology/op14-cosmic-horizon-profile.md` (or equivalent path). Analog of `frame-dragging-impedance-convolution.md:20`'s Kerr-interior asymmetric saturation profile, but for cosmic-horizon scale. Derives how $Z_{\text{eff}} = Z_0/\sqrt{S(A)}$ behaves as $r \to R_H$ during ongoing K4 crystallisation. Does NOT require new operator — applies canonical Op14 (Vol 1 Ch 6 §1.13) at new scale.

2. **Projection-chain trace** from substrate dynamics (over-bracing $u_0^*$ + ongoing K4 crystallisation at $R_H$ + Cosserat translational-DOF) → cosmic-scale DE measurement ($\rho_\Lambda$ via Friedmann). Per Session 1 scoping doc Phase 2's 6-component inventory. NO magnitude-matching attempts (per v1.2 trigger 16 sub-case (e-i) — projection-trace not energy-equality).

3. **A-034 catalog row addition** at `manuscript/ave-kb/common/universal-saturation-kernel-catalog.md` — new cosmic-scale ASYM-N(ε) row companion to Row 14 K4-crystallisation-SYM*. Fills the gap-cell from γ extension at commit `6436d65`. Row content: scale = cosmic horizon; $A$ definition = (substrate ε-sector strain at $R_H$) / (saturation threshold from Ax 4); saturation event = ongoing crystallisation maintaining $\partial_t \rho_n = 0$; empirical anchor = $\rho_\Lambda$ measurement from supernova / CMB / BAO.

### Branch + commit

- Branch: `analysis/cosmic-epsilon-de-projection-session2` from `analysis/integration` HEAD (verify at session start)
- Multi-commit acceptable (per-deliverable commits OK, OR single batch commit per `ave-walk-back` discipline)
- Push at end
- **DO NOT MERGE** — orchestration handles merge

### Phase plan

#### Phase 0 — verification (15-20 min)

- Read Session 1 scoping doc at `research/2026-05-19_cosmic-epsilon-de-projection-scoping.md`
- Read this brief's Grant adjudications section
- Verify Op14 canonical references resolve: `frame-dragging-impedance-convolution.md:20` (BH case), Vol 1 Ch 6 §1.13 (definition), `op14-local-clock-modulation.md`, `op14-cross-sector-trading.md`, `lattice-impedance-decomposition.md`
- Verify `lattice-genesis-hubble-tension.md` + `cosmological-constant-closure.md` framings
- Create branch

#### Phase 1 — Op14 cosmic-horizon profile derivation (90-120 min)

Apply `ave-canonical-leaf-pull` v1.2 trigger 16 (c)-operator-application classification: this is Op14 at a NEW scale, not a new operator.

Derive (or assemble from canonical pieces):
- $Z_{\text{eff}}(r)$ profile as $r \to R_H$
- Saturation behavior $S(A(r)) \to 0$ at horizon
- Asymmetric ε/μ sub-profile if applicable (per Q3 γ = ASYM-N(ε))
- Connection to crystallisation rate (dynamic per Q1)

Output: canonical leaf at `manuscript/ave-kb/vol3/cosmology/ch04-generative-cosmology/op14-cosmic-horizon-profile.md` (or equivalent path — implementor chooses placement).

Skill discipline:
- `ave-canonical-leaf-pull` v1.2 — trigger 16 (c)-classification load-bearing
- `verify-before-cite` v1.3 — every canonical-leaf citation grep-confirmed
- `consistency-vs-emergence` v1.1 — Class E framing for $Z_{\text{eff}}(R_H)$ as operating-point projection
- `ave-evidence-framing-discipline` — derivation strength matches actual derivation, not synthesis

#### Phase 2 — Projection-chain trace (60-90 min)

Walk through the 6-component inventory from Session 1 Phase 2 in order:
1. Substrate over-bracing $u_0^*$ + $\hat{\Omega}_{\text{freeze}}$ direction (set at cosmic genesis)
2. K4 crystallisation rate at horizon (dynamic per Q1)
3. Cosserat translational-DOF projection (Ax 1 ε ↔ macroscopic E)
4. Ax 2 TKI scale invariance (substrate-scale → cosmic-scale)
5. Op14 long-range coupling (using Phase 1's new cosmic-horizon profile)
6. Boundary observables $\mathcal{M}/\mathcal{Q}/\mathcal{J}$ at cosmic horizon

For each: how does the projection produce $\rho_\Lambda$ at the macroscopic Friedmann equation? NOT a magnitude-matching exercise. Show the structural chain.

Output: research doc at `research/2026-05-NN_cosmic-epsilon-de-projection-mechanism.md` (or 2026-05-20 if session spans midnight).

#### Phase 3 — A-034 catalog row addition (30-45 min)

Apply `ave-walk-back` discipline (single commit for the catalog edit + closure-roadmap entry).

Add new row to `manuscript/ave-kb/common/universal-saturation-kernel-catalog.md` per γ extension's gap-cell:

```
| Cosmic (DE / ε-sector) | ASYM-N(ε) | substrate ε-strain at R_H / saturation threshold | Ongoing crystallisation maintaining ∂_t ρ_n = 0 | ρ_Λ measurement (supernova + CMB + BAO) |
```

Update the companion-row links table to show the explicit pairing with Row 14 K4-crystallisation-SYM*.

Update closure-roadmap with the addition + reference to Session 2 derivation + this commit.

#### Phase 4 — Audit + push (15-20 min)

- Self-audit per the (a)-(e) classification check
- Push branch
- Do NOT merge

### Skill discipline

- `ave-canonical-leaf-pull` v1.2 — MANDATORY trigger 16 throughout
- `verify-before-cite` v1.3 — every citation
- `consistency-vs-emergence` v1.1 — Class E for DE observable
- `ave-walk-back` — Phase 3 catalog row addition
- `ave-evidence-framing-discipline` — Op14 cosmic-horizon profile claim strength
- `pre-test-physics-check` — if Phase 1 derivation surfaces a load-bearing physics question that wasn't in Q1/Q2/Q3, STOP and surface

### CRITICAL FAILURE MODES TO AVOID (carried forward from Session 1 brief)

1. NO magnitude-matching attempts (raw substrate field energy vs DE measurement).
2. NO RMS→DC averaging as projection mechanism.
3. NO microscopic/macroscopic conflation.
4. NO inventing new operator (Op14 already exists).

### Expected return summary

- Branch + tip commit hash
- Per-phase commit hashes
- Phase 1 Op14 cosmic-horizon profile leaf path
- Phase 2 research doc path + projection-chain summary
- Phase 3 catalog row addition + companion-row link update
- (a)-(e) classification verdict (should be (c)-operator-application + (a)-missing-row composite)
- Any anomalies surfaced
- Confirmation of push + no merge

## Session 1 (this epic) — implementor brief

### Goal

Produce a single research doc that establishes:

1. **DE measurement definition** — what specifically does DE measure as a cosmic-scale OBSERVABLE? Cite the corpus's existing framings (latent-heat-of-crystallisation per `lattice-genesis-hubble-tension.md`, $\rho_\Lambda$ derivation in `cosmological-constant-closure.md`, etc.)
2. **Projection chain** — from substrate dynamics (over-bracing static E, K4 crystallisation rate at horizon, Class E $u_0^*$ operating-point) to DE measurement. NOT a magnitude-matching exercise; explicitly trace how Ax 2 TKI + Op14 + boundary-observables project substrate-scale physics to cosmic-scale observable.
3. **Catalog classification options** — three candidate framings, scoped without committing:
   - **(α) Class E only** — DE is one of N joint observables of the cosmic operating-point $u_0^*$; sufficient framing per `consistency-vs-emergence` v1.1; no new catalog row needed.
   - **(β) ASYM-N(ε) cosmic-row** — DE is the missing companion to K4-crystallisation-SYM\* (Row 14); add new row to A-034 catalog filling the γ-extension gap-cell at cosmic-scale ε column.
   - **(γ) Both** — Class E captures joint-constraint at operating-point; ASYM-N(ε) captures the saturation-event mechanism class. The two framings are projection-axes-complementary not mutually exclusive.
4. **Three plumber-physical questions for Grant pre-Session-2** — surface load-bearing structural choices that need adjudication before any projection-mechanism derivation is attempted.
5. **Multi-session arc outline** — what Sessions 2-4 need.

**NO derivation in this session. Scoping only.** Output: research doc at `research/2026-05-NN_cosmic-epsilon-de-projection-scoping.md` (or 2026-05-20 if session spans midnight).

**EXPLICIT CONSTRAINT**: NO magnitude-matching attempts. Any analysis that compares "raw substrate field energy" to "observed DE energy density" is the projection-vs-measurement conflation that this epic exists to walk back. Per `ave-canonical-leaf-pull` v1.1 trigger 16 (and per its candidate v1.2 amendment for projection-vs-measurement sub-case): demand projection-trace, not magnitude-matching.

### Branch + commit

- Branch: `analysis/cosmic-epsilon-de-projection-scoping` from `analysis/integration` HEAD `0275a6a` (post-GZ-DECaLS Outcome-E merge; or current at session start — verify in Phase 0)
- Single commit at end of Phase 6
- Push at end
- **DO NOT MERGE** — orchestration handles merge

### Phase plan

#### Phase 0 — verification (15 min)

- Read this brief
- Verify `verify-before-cite` v1.3 + `consistency-vs-emergence` v1.1 + `ave-canonical-leaf-pull` v1.1 are at HEAD on skills repo
- Verify the corpus building-block citations resolve at AVE-Core HEAD:
  - `manuscript/ave-kb/vol3/cosmology/ch04-generative-cosmology/lattice-genesis-hubble-tension.md` (LC crystallisation rate framing)
  - `manuscript/ave-kb/vol3/cosmology/ch05-dark-sector/cosmological-constant-closure.md` ($\rho_\Lambda$ + "5 Independent Tests" table)
  - `manuscript/ave-kb/common/universal-saturation-kernel-catalog.md` (γ extension at 6436d65 with ε/μ axis + gap-cells + companion-rows)
  - `manuscript/ave-kb/common/omega-freeze-cosmic-grain-cascade.md` (Class E joint-constraint at $u_0^*$)
  - `manuscript/ave-kb/common/boundary-observables-m-q-j.md` (M/Q/J cosmic-boundary observables)
  - `manuscript/ave-kb/vol1/axioms-and-lattice/ch1-fundamental-axioms/zero-parameter-universe.md` (Ax 1 Cosserat translational DOF → ε)
- Create branch `analysis/cosmic-epsilon-de-projection-scoping`

#### Phase 1 — DE measurement definition (30 min)

Cite the corpus's existing DE framings VERBATIM (per `verify-before-cite` v1.3):

- What does $\rho_\Lambda$ measure operationally? (e.g., the cosmological-constant contribution to Einstein equation; inferred from supernova distance-modulus residuals, CMB power-spectrum acoustic peaks, BAO scale)
- What's $H_\infty$ measure operationally? (LC crystallisation rate per `lattice-genesis-hubble-tension.md`)
- What's the relationship $\rho_\Lambda$ ↔ $H_\infty$ in AVE? (currently downstream: $\rho_\Lambda \sim H_\infty^2 / G$)
- Frame DE as a **macroscopic observable of bulk substrate dynamics**, NOT a sum of microscopic field energies.

#### Phase 2 — Projection chain inventory (30 min)

For each component, identify what canonical leaf provides the projection mechanism:

| Component | Canonical leaf | Projection role |
|---|---|---|
| Substrate-scale over-bracing $u_0^*$ in $\hat{\Omega}_{\text{freeze}}$ | `omega-freeze-cosmic-grain-cascade.md:13-40` | Static substrate state at every K4 node |
| K4 crystallisation rate at horizon | `lattice-genesis-hubble-tension.md` | Ongoing dynamics: rate of new node addition at horizon scale |
| Cosserat translational-DOF projection | Ax 1 + `q-g47-substrate-scale-cosserat-closure.md` | Substrate-scale ε ↔ macroscopic-scale E-field relationship |
| Ax 2 TKI scale invariance | `axiom-definitions.md` | Cross-scale mechanism: same physics at every scale |
| Op14 long-range coupling | `frame-dragging-impedance-convolution.md:20` + `operators.md` | Substrate response to bulk strain at scale of interest |
| Boundary observables M/Q/J | `boundary-observables-m-q-j.md` | Class E joint-constraint structure at cosmic horizon |

For each: 1-paragraph summary of role; what's known; what's missing for the projection chain.

#### Phase 3 — Catalog classification scoping (30 min)

Three framing options, scoped without committing:

**(α) Class E only**: DE is one of N joint observables of cosmic-scale operating-point $u_0^*$. Per `consistency-vs-emergence` v1.1, Class E captures this naturally. No new A-034 catalog row needed; the cosmic-ε gap-cell is "filled" by saying Class E subsumes ASYM-N(ε) at the operating-point level.

**(β) ASYM-N(ε) cosmic-row**: Add a new row to A-034 catalog at cosmic scale, ASYM-N(ε), companion to Row 14 K4-crystallisation-SYM\*. The saturation event is something cosmic-scale-ε-specific (TBD what physically). Catalog row would fill γ extension gap-cell explicitly.

**(γ) Both framings, projection-axes-complementary**: Class E captures the joint-constraint at operating-point (microscopic substrate property at $u_0^*$); ASYM-N(ε) captures the saturation-mechanism class at cosmic-scale ε (macroscopic projection observable). These are different projections; not mutually exclusive.

For each: pros/cons; what verification would settle which; structural cost.

#### Phase 4 — Three plumber-physical questions for Grant (15-20 min)

Surface load-bearing structural questions that need Grant adjudication BEFORE Session 2 projection-mechanism derivation can proceed. Examples to consider (implementor refines):

- **Q1**: Is DE measured as a STATIC observable (rate of universe expansion in a steady-state sense) or a DYNAMIC observable (time-varying crystallisation rate)? This determines whether the projection chain is static (over-bracing → ε-cosmic-projection) or dynamic (crystallisation-rate → ρ_Λ time-dependence).
- **Q2**: Does the projection chain require additional substrate-physics not yet in corpus (e.g., a specific "horizon-scale Op14 saturation profile" beyond what `frame-dragging-impedance-convolution.md:20` gives for gravitational case)? Or do all required pieces already exist as canonical leaves?
- **Q3**: For the catalog-classification decision (α/β/γ), which framing IS the framework's actual stance on DE — operating-point joint-constraint, saturation-event row, or both? Or does the projection-vs-measurement insight from 2026-05-19 EOD mean DE shouldn't be either of these, and instead some new third-category classification is needed?

#### Phase 5 — Multi-session arc outline (15 min)

Lay out what Sessions 2-4 need:
- Session 2 projection-mechanism derivation: which canonical leaves integrate, what intermediate results are needed, expected form of the projection chain
- Session 3 catalog row classification commit: small kb edit; what triggers it
- Session 4 downstream walk-back: conditional; only if classification changes existing corpus framing

#### Phase 6 — Audit + push (10 min)

- Self-audit per checklist
- Push branch
- Do NOT merge

### Skill discipline

- `verify-before-cite` v1.3 — every corpus citation re-grepped at execution time
- `ave-canonical-leaf-pull` v1.1 — trigger 16 mandatory throughout (this scoping IS a framework-design proposal in disguise; classify per (a)-(e) at every step)
- `consistency-vs-emergence` v1.1 — Class E framing for DE observable
- `ave-evidence-framing-discipline` — strength language must precisely match scoping-doc-not-derivation discipline
- `pre-test-physics-check` — APPLICABLE for Phase 4 plumber-physical questions
- Pure-AVE-corpus rule

### EXPLICIT FAILURE MODES TO AVOID (per Grant adjudications 2026-05-19 EOD)

1. **DO NOT invent new field theory or new framework structure.** Trigger 16 (a)-(e) classification applies. This scoping should land in (a)-match or (a)-missing-row, NOT (e)-genuinely-new.
2. **DO NOT magnitude-match raw substrate field energies to cosmic-scale DE measurement.** That's the QFT-style cosmological constant problem framing. AVE doesn't have to inherit it. Demand projection-trace through Ax 2 + Op14 + boundary-observables, not energy-density-equality.
3. **DO NOT propose RMS→DC averaging as the projection mechanism.** Orchestration already walked back that framing 2026-05-19 EOD; current corpus framing is latent-heat-of-crystallisation-rate at horizon.
4. **DO NOT conflate microscopic substrate property (over-bracing E field, $u_0^*$) with macroscopic measurement (DE energy density).** Per Grant 2026-05-19 EOD catch.

### Expected return summary

- Branch + tip commit hash
- Single commit + summary
- Phase 1: DE measurement definition (1-paragraph)
- Phase 2: 6 projection-chain components inventoried
- Phase 3: 3 catalog classification options (α/β/γ) with pros/cons
- Phase 4: 3 plumber-physical questions for Grant pre-Session-2
- Phase 5: multi-session arc estimated effort
- Any anomalies surfaced (corpus gaps, framing inconsistencies, etc.)
- Confirmation of push + no merge

### Constraints (repeat)

- NO derivation. Scoping only.
- NO magnitude-matching attempts.
- NO modifications to `_orchestration/*.md` or corpus leaves; deliverable is `research/` artifact.
- If a derivation seems trivial enough to attempt mid-session, STOP — Session 2 scope.
- If projection-chain inventory surfaces a corpus structural inconsistency, STOP and report rather than fix.

## Cross-references

- γ A-034 catalog extension (commit `6436d65`) — provides cosmic-ε gap-cell framing
- E-field-as-over-bracing identification (orchestration session 2026-05-19 EOD chat log)
- Projection-vs-measurement conflation catch (orchestration session 2026-05-19 EOD chat log, post #6 GZ-DECaLS merge)
- `consistency-vs-emergence` v1.1 — Class E operating-point projection
- `ave-canonical-leaf-pull` v1.1 trigger 16 — framework-extension proposals must work within existing universal-scale machinery
- Existing DE corpus: `lattice-genesis-hubble-tension.md`, `cosmological-constant-closure.md`, `omega-freeze-cosmic-grain-cascade.md`
