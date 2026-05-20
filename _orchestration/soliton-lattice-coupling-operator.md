# Soliton-Lattice Coupling Operator Epic

**Status**: ACTIVE — Session 2 (operator derivation at planetary scale) ready to spawn; Session 1 CLOSED 2026-05-19 EOD via merge `d413726` + audit tag `audit/2026-05-19_soliton-lattice-coupling-operator-scoping`
**Last updated**: 2026-05-19 EOD
**Originating session**: Orchestration session post-SDSS DR17 merge + Grant operator-output reframing 2026-05-19 EOD

## Grant adjudications 2026-05-19 EOD (resolves Session 1 plumber-physical questions Q1'/Q2'/Q3')

**Q1' — precise vs class prediction for mag-spin tilts? → CLASS prediction** (fluid-dynamics Reynolds-number analogy). Operator predicts class structure (rocky / metallic-H / icy-mantle differential coupling regime; aligned / moderate / tilted-vs-spin offset class). Specific values (Earth's exact 11° / Saturn's exact <1° / Uranus's exact 59°) emerge from micro-complexity beyond the operator's predictive granularity. Same pattern as turbulent flow: bulk Reynolds number predicts laminar/turbulent regime; specific velocity field at every microscopic point is chaotic.

**Q2' — single Ω_freeze vs cascaded-per-planet inheritance? → BOTH** (cosmic genesis first, then nested cascade). Cosmic Ω_freeze is the source (frozen at K4 crystallisation seed event). Cascaded propagation through nested rotators per `omega-freeze-cosmic-grain-cascade.md:118-128` §4: cosmic → galactic disk axes → stellar spins → planetary spin axes → Earth inner-core super-rotation. Each formation event is a substrate phase-transition that inherits + modulates by local conditions. The operator's "Ω_freeze direction" for any given soliton is the LOCAL inherited direction, not cosmic-genesis directly.

**Q3' — specific-value vs stable-branch for 3 anomalies? → N-body-scaled predictability** (Reynolds-number analog). Low N (solar system, 8 planets): operator predicts specific values within tolerance. High N (galaxy, 10¹¹ stars): operator predicts class/statistical properties only. Solar system is in the LOW-N regime where specific-value prediction is structurally possible — but the SDSS DR17 galactic-scale work IS the HIGH-N regime where only bulk statistical-direction prediction is meaningful.

Scoring rubric implication: planetary scale targets specific obliquity per body within ±15° tolerance; galactic scale targets coherent-direction mean within σ_LSS of empirical.

## Why this exists

The SDSS DR17 epic (merged 2026-05-19 EOD at `9f976e0`, audit tag `audit/2026-05-19_c5-sdss-dr17-spin-orientation`) surfaced a Marginal-D result with the LSS galaxy-spin axis at $(l=129°, b=79°)$, $\sigma=6.83°$ — **coherent (low scatter) but 36.75° offset from the CMB axis-of-evil at $(l=60.28°, b=50.48°)$**.

The orchestration session's first-pass framing treated this as "cascade-loose alignment tolerance." Grant adjudication walked that back 2026-05-19 EOD: the 36.75° offset is NOT scatter — it's the coherent output of an **underspecified substrate-physics operator** $\hat{\mathcal{O}}_{\text{soliton}}$ that maps the cosmic chirality direction $\hat{\Omega}_{\text{freeze}}$ to the observable axis of a bound-soliton class, parameterized by the soliton's $(M, \omega, \mathcal{M})$ structure:

$$\hat{\mathcal{O}}_{\text{soliton}}\bigl(\hat{\Omega}_{\text{freeze}}; \, M_s, \omega_s, \mathcal{M}_s\bigr) \to \hat{n}_{\text{observable}}$$

The framework currently has all the building-block pieces (Op14 asymmetric saturation profile, Cosserat micropolar rotational DOF per Ax 1, parametric coupling kernel, frame-dragging interior strain pattern, geodynamo VCA, planetary magnetosphere magnetopause-standoff Op14 validation) but lacks an **integrated derivation** of the operator's functional form.

Until the operator is derived, the SDSS DR17 result (and downstream LSS spin / orbital plane / galaxy chirality observables) can't be interpreted as either AVE-confirming or AVE-disconfirming — the prediction is "the operator's coherent output at this scale" with the operator's output undetermined.

Empirical data already exists in spades. The solar system gives 8 planetary spin obliquities + 8 magnetic-axis tilts = 16 axis-data-points constraining the operator. Two outliers (Venus retrograde, Uranus 98° tilt) are particularly informative — standard solar-system formation explains them via ad-hoc giant-impact hypotheses. AVE has the substrate-physics structural opportunity to derive them as predicted equilibrium configurations.

## Scope (multi-session research arc)

| Session | Deliverable | Effort | Status |
|---|---|---|---|
| 1 | Scoping research doc (corpus inventory + operator structure sketch + derivation prereqs + testable predictions + multi-session arc outline) | 1-2 hr | **CLOSED 2026-05-19 EOD via merge `d413726` + audit tag `audit/2026-05-19_soliton-lattice-coupling-operator-scoping`**. Refactored to A-034 catalog-extension framing per `ave-canonical-leaf-pull` v1.1 trigger 16 — 4 of 6 prereqs collapse to existing canonical leaves; total arc 16-25 hr → 5-9 hr |
| **2 (this session)** | **Catalog row additions + $A_{\text{soliton}}$ definition + planetary-scale scoring against 16 axis-data-points** | 3-5 hr | ACTIVE — ready to spawn |
| 3 | Galactic-scale extension to SDSS DR17 via the added Row(s) | 1-2 hr | QUEUED |
| 4 | LSS-scale + cross-catalog (Shamir 2022) extension | 1-2 hr | QUEUED |
| 5 (conditional) | Refinement based on Sessions 2-4 outcomes | TBD | CONDITIONAL |

## Session 2 (this session) — implementor brief

### Goal

Per the refactored Session 1 scoping doc (`research/2026-05-20_soliton-lattice-coupling-operator-scoping.md`) and Grant Q1'/Q2'/Q3' adjudications above:

1. **Add 1-4 new rows to A-034 catalog** at `manuscript/ave-kb/common/universal-saturation-kernel-catalog.md` covering: planetary spin-axis alignment with Ω_freeze, planetary magnetic-vs-spin-axis offset, galactic spin-axis alignment, LSS spin-axis. Per Session 1's (a)-missing-row classification per `ave-canonical-leaf-pull` v1.2 trigger 16.

2. **Define $A_{\text{soliton}}$ concretely** for each new row using compressed prereqs P-1 through P-6 from Session 1 refactor (4 of 6 resolve to "apply existing canonical leaf at file:line" — substrate Larmor freq via parametric-coupling-kernel, Op14 interior strain via frame-dragging-impedance-convolution, Cosserat body-frame via Q-G47, J decomposition via boundary-observables-m-q-j). P-3 (mass-scaling per structural class) and P-4 (multi-resonance landscape) retain empirical-scoring work.

3. **Planetary-scale scoring**: apply $A_{\text{soliton}}$ + kernel $S(A) = \sqrt{1-A^2}$ to 8 planets × 2 axes = 16 data-points. Per Q1' adjudication, target is CLASS prediction (within ±15° tolerance per body), NOT specific-value matching. Per Q3' adjudication, low-N regime makes specific-value prediction structurally possible — but tolerance band is wide.

### Branch + commit

- Branch: `analysis/soliton-lattice-coupling-operator-session2` from `analysis/integration` HEAD (verify at session start)
- Multi-commit OK
- Push at end
- **DO NOT MERGE** — orchestration handles merge

### Phase plan

#### Phase 0 — verification (15 min)

- Read Session 1 refactor at `research/2026-05-20_soliton-lattice-coupling-operator-scoping.md`
- Read Grant adjudications above
- Verify the 6 compressed prereq citations resolve at HEAD (per refactor)
- Verify γ catalog extension at commit `6436d65` provides the row-structure template
- Create branch

#### Phase 1 — A-definition derivation (90-120 min)

For each new catalog row (1-4 rows depending on Session 2 verdict), define $A_{\text{soliton}}$ structurally:

- Inputs: soliton parameters $(M_s, \omega_s, \mathcal{M}_s, \text{topology class})$
- Inherited Ω_freeze direction (LOCAL per Q2' cascade, not cosmic directly)
- Coupling-strength dependence on per-class $g_{\text{class}}$ (rocky / metallic-H / icy-mantle) per P-3
- Resonance/anti-resonance regions for stable retrograde / 90° / aligned solutions per P-4

Skill discipline:
- `ave-canonical-leaf-pull` v1.2 — trigger 16 (a)-missing-row for the catalog additions; trigger 1-13 for any derivation pieces
- `consistency-vs-emergence` v1.1 — Class E for the operator-output observables
- `verify-before-cite` v1.3 — all citations

#### Phase 2 — A-034 catalog row additions (45-60 min)

Apply `ave-walk-back` discipline (single commit batch).

Add the 1-4 new rows to `manuscript/ave-kb/common/universal-saturation-kernel-catalog.md` per γ extension template. Update ε/μ axis classification, gap-cells (which fill, if any), companion-row links table.

Update closure-roadmap with new entry referencing Session 2.

#### Phase 3 — Planetary-scale scoring (60-90 min)

Apply the derived $A_{\text{soliton}}$ + kernel to 16 planetary axis-data-points:

| Body | Spin obliquity (deg) | Magnetic tilt (deg) | Operator-predicted class | Match? |
|---|---|---|---|---|
| Mercury | 0.034 | ~0 weak | ? | ? |
| Venus | 177.4 | none | ? | ? |
| Earth | 23.44 | ~11 | ? | ? |
| Mars | 25.19 | none | ? | ? |
| Jupiter | 3.13 | ~10 | ? | ? |
| Saturn | 26.73 | <1 | ? | ? |
| Uranus | 97.77 | 59 | ? | ? |
| Neptune | 28.32 | 47 | ? | ? |

Per Q1' (class prediction) + Q3' (low-N specific-value tolerance ±15°):
- Score "class match" if operator predicts correct broad class (aligned / moderate / retrograde / 90°+)
- Score "specific match" if operator predicts within ±15° tolerance band

Report:
- N/16 specific matches
- N/16 class matches  
- 3 anomaly resolution (Saturn-aligned-vs-Uranus-tilted; Venus retrograde; Uranus 98°) — does operator predict these as stable equilibria or non-trivial outliers?

Output: research doc at `research/2026-05-NN_soliton-coupling-operator-session2-planetary-scoring.md`.

#### Phase 4 — Audit + push (15 min)

- Self-audit + ave-discrimination-check (the 16-data-point scoring is potentially AVE-distinct — apply SM-counterfactual + interpretive-alternatives if outcome >50% class matches)
- Push branch
- Do NOT merge

### Skill discipline

- `ave-canonical-leaf-pull` v1.2 — trigger 16 (a)-missing-row throughout
- `verify-before-cite` v1.3
- `consistency-vs-emergence` v1.1 — Class E
- `ave-walk-back` — Phase 2 catalog row commit
- `ave-discrimination-check` — Phase 3 scoring outcome interpretation
- `ave-evidence-framing-discipline` — strength language for "operator predicts X" claims
- `pre-test-physics-check` — if Phase 1 derivation surfaces new load-bearing physics question, STOP

### Expected return summary

- Branch + tip commit hash
- Per-phase commit hashes + summaries
- Phase 1 A-definitions per new row (1-4 definitions)
- Phase 2 catalog rows added (count + summary of each)
- Phase 3 planetary-scale scoring: N/16 specific matches + N/16 class matches + 3-anomaly resolution status
- ave-discrimination-check verdict if Phase 3 outcome >50% match
- Any anomalies surfaced
- Confirmation of push + no merge

## Session 1 (this epic) — implementor brief

### Goal

Produce a single research doc that establishes:
1. **Operator definition** — what does $\hat{\mathcal{O}}_{\text{soliton}}$ map, with what inputs and outputs, in what units
2. **Corpus building blocks** — inventory the existing AVE pieces that need to be integrated
3. **Derivation prereqs** — what specific substrate-physics derivations need to land before Session 2 can produce an integrated operator formula
4. **Testable predictions** — concrete planetary + galactic data the operator must reproduce
5. **Multi-session arc outline** — what Sessions 2-5 will need

**NO derivation in this session.** Scoping only. Output: a single research doc at `research/2026-05-19_soliton-lattice-coupling-operator-scoping.md` (or `2026-05-20_*` if session spans midnight).

### Branch + commit

- Branch: `analysis/soliton-lattice-coupling-operator-scoping` from `analysis/integration` HEAD `9f976e0` (post-SDSS merge) — verify in Phase 0
- Push: yes (at end)
- Merge: NO — orchestration handles merge after audit

### Phase plan

#### Phase 0 — verification (15 min)

- Read this brief
- Verify `verify-before-cite` v1.3 + `consistency-vs-emergence` v1.1 are at HEAD on skills repo
- Verify the corpus building-block citations resolve at AVE-Core HEAD (`9f976e0`):
  - `manuscript/ave-kb/vol3/gravity/ch02-general-relativity/frame-dragging-impedance-convolution.md:20`
  - `manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/parametric-coupling-kernel.md`
  - `manuscript/ave-kb/vol3/cosmology/ch06-solar-system/planetary-magnetospheres.md`
  - `manuscript/ave-kb/vol3/applied-physics/ch13-geophysics/geodynamo-vca-back-emf.md`
  - `manuscript/ave-kb/common/omega-freeze-cosmic-grain-cascade.md` §3.1 + §4 nested-cascade conjecture
- Create branch `analysis/soliton-lattice-coupling-operator-scoping`

#### Phase 1 — Operator definition (30 min)

Define $\hat{\mathcal{O}}_{\text{soliton}}$ structurally:

- **Inputs**: $\hat{\Omega}_{\text{freeze}}$ (direction; substrate-frozen at cosmic genesis) + soliton parameters $(M_s, \omega_s, \mathcal{M}_s, \text{topology})$
- **Output**: $\hat{n}_{\text{observable}}$ — observable axis (which? spin-axis, magnetic-dipole-axis, both?) for the soliton class
- **Functional form (sketch only)**: $\hat{n}_{\text{obs}} = R(\theta(M, \omega, \mathcal{M})) \cdot \hat{\Omega}_{\text{freeze}}$ for some rotation matrix $R$ with angular parameter $\theta$ that depends on soliton structure
- **Symmetry constraints**: parity (left-handed vs right-handed solutions per I4_132 chirality), time-reversal, scale invariance per Ax 2

State explicitly: this is a definitional sketch, NOT a derivation. The substrate-physics derivation is Session 2's scope.

#### Phase 2 — Corpus building-block inventory (45 min)

Read + summarize each building block's contribution to the eventual integrated operator:

1. **Op14 asymmetric saturation profile** (`frame-dragging-impedance-convolution.md`) — substrate response to rotating mass; prograde-vs-retrograde Op14 saturation asymmetry. Verbatim quote of the mechanism.
2. **Parametric coupling kernel** (`parametric-coupling-kernel.md`) — coupling between rotating LC tanks and external substrate forcing. How does this map to planetary-soliton ↔ cosmic-substrate?
3. **Cosserat micropolar rotational DOF** (Ax 1 + cross-volume) — 3 rotational DOF per node; the substrate-native rotational coupling channel. How do bound solitons engage with these DOF?
4. **Frame-dragging interior strain pattern** (`04_generative_cosmology.tex` Kerr-interior discussion, and Vol 3 Ch 2 §138 + Vol 3 Ch 3 §178 as cited in `universal-saturation-kernel-catalog.md:101`) — same mechanism that locked $\hat{\Omega}_{\text{freeze}}$ at cosmic genesis, scaled down to planetary mass.
5. **Geodynamo VCA back-EMF** (`geodynamo-vca-back-emf.md`) — Earth's magnetic field from substrate-VCA back-EMF. Single data point on magnetic-vs-spin-axis offset (~11°).
6. **Planetary magnetosphere magnetopause-standoff** (`planetary-magnetospheres.md`) — Op14 substrate-coupling validated at 5-planet scale (Earth 8.7%, Jupiter 11.8%, Saturn 22.8%, Uranus 11.6%, Neptune 16.4% standoff error). The operator partially works at this scale — what does it predict, what doesn't it?
7. **Boundary observables M/Q/J** (`boundary-observables-m-q-j.md`) — Class E candidate per consistency-vs-emergence v1.1; M/Q/J at $\Gamma=-1$ boundaries are joint-constrained. Planetary surfaces / magnetospause / magnetotail are $\Gamma=-1$ boundaries — connection?
8. **omega-freeze-cosmic-grain-cascade §4 nested-cascade conjecture** (lines 118-128) — explicit corpus statement that $\hat{\Omega}_{\text{freeze}}$ projects through nested rotators; the operator is what makes this concrete.

For each: file:line, 1-paragraph summary, what's still missing for the integrated operator.

#### Phase 3 — Derivation prereqs (30 min)

List the specific substrate-physics derivations that need to land BEFORE Session 2 can produce an integrated operator formula. Examples (implementor refines):

- Substrate Larmor-frequency analog: what's the substrate-frequency that planetary rotation rates couple to? Is it $c/\ell_{node}$, some axiom-derived combination, or scale-dependent?
- Op14 saturation profile in the soliton-interior frame vs the substrate-rest frame
- Coupling-strength dependence on soliton mass: $\propto M_s^?$
- Resonance/anti-resonance regions in the $(M, \omega, \mathcal{M})$ parameter space — where do retrograde solutions become stable?
- Cosserat coupling between bound rotating bodies and substrate rotational DOF — substrate-rest-frame vs body-frame transformations

Each prereq gets: what's the question, what's the corpus context, what's the expected derivation path, estimated effort.

#### Phase 4 — Testable predictions list (30 min)

Concrete observables the operator must reproduce. Compile from solar system + galactic data:

**Solar system (16 data points)**:

| Body | Spin obliquity | Magnetic axis tilt | Size ($R_\oplus$) | Rotation period (hr) |
|---|---|---|---|---|
| Mercury | 0.034° | ~0° (weak field) | 0.383 | 1407 |
| Venus | **177.4°** | None | 0.949 | **−5832** (retrograde) |
| Earth | 23.44° | ~11° | 1 | 23.93 |
| Mars | 25.19° | None (crustal only) | 0.532 | 24.62 |
| Jupiter | 3.13° | ~10° | 11.21 | 9.93 |
| Saturn | 26.73° | **<1°** | 9.45 | 10.66 |
| Uranus | **97.77°** | **59°** | 4.01 | 17.24 |
| Neptune | 28.32° | **47°** | 3.88 | 16.11 |

Three key questions:
- Why is Saturn's magnetic axis essentially aligned (<1°) while Uranus's is 59°? Both are gas giants with similar rotation periods. Difference: Saturn has metallic-hydrogen layer near surface; Uranus has icy mantle with conducting fluid much deeper.
- Why Venus retrograde? Slow rotation (243 days) + no magnetic field. Slow-rotation resonance that anti-aligns spin?
- Why Uranus 98°? Standard explanation is giant-impact, ad-hoc. AVE could derive as stable-equilibrium in the operator's resonance landscape.

**Galactic scale**:
- SDSS DR17 LSS spin axis: $(l=129°, b=79°)$, $\sigma=6.83°$ — operator's coherent output at galaxy-class soliton scale
- Predict where the operator points $\hat{\Omega}_{\text{freeze}}$ for galaxy-class $(M_{\text{gal}}, \omega_{\text{gal}}, \mathcal{M}_{\text{gal}})$ → compare to data
- Galactic-disk axis distributions (SDSS galaxy catalog)
- Binary star orbital plane axes (Gaia DR3)

**LSS scale**:
- Pantheon+ Hubble bulk-flow direction at (l=129.76°, b=−13.64°), σ=24.0° — different soliton class (matter rather than galaxy-spin); operator may map to different observable axis
- Walmsley+2022 GZ DECaLS independent classification — gives second data point at galactic scale

#### Phase 5 — Multi-session arc outline (15 min)

Lay out what Sessions 2-5 need:
- Session 2 derivation: which corpus building blocks integrate, what intermediate results are needed, expected functional form of the integrated operator
- Session 3 planetary-scale test: scoring rubric (how many of the 16 axis-data-points must the operator reproduce within what tolerance for the operator to count as "working at planetary scale"?)
- Session 4 galactic-scale extrapolation: how does the planetary-scale operator extrapolate? Does it need re-derivation at galactic scale, or just parameter substitution?
- Session 5 conditional refinement: branch points based on Session 3 outcomes

#### Phase 6 — Audit + push (10 min)

- ave-auditor verdict (self-audit acceptable; brief is research-doc-only)
- Push branch `analysis/soliton-lattice-coupling-operator-scoping`
- Do NOT merge — orchestration handles

### Skill discipline (Session 1)

- `verify-before-cite` v1.3 — every corpus citation re-grepped at execution time; triggers 7c + 8 for cross-branch / commit-application
- `ave-canonical-leaf-pull` — Phase 2 building-block inventory; enumerate all canonical leaves for soliton-substrate coupling
- `ave-prereg` — SKIP (this is a scoping doc, not a new derivation)
- `consistency-vs-emergence` v1.1 — when discussing operator output, frame as Class E operating-point projection per the new skill body
- `pre-test-physics-check` — APPLICABLE if Phase 4 testable-predictions section locks in adjudication criteria for Sessions 2-4; surface plumber-physical question to orchestration if so
- Pure-AVE-corpus rule

### Expected return summary

- Branch + tip commit
- Single-commit hash + summary
- Phase 1 operator definition (1-paragraph)
- Phase 2 building-block count (8 inventoried)
- Phase 3 derivation prereqs count + 1-line description of each
- Phase 4 testable predictions count
- Phase 5 multi-session arc estimated total effort
- Any anomalies surfaced (corpus gaps, structural-physics surprises)
- Confirmation of push + no merge

### Constraints

- **NO derivation in this session.** Scoping only.
- Do NOT modify `_orchestration/*.md`
- Do NOT modify corpus leaves (manuscript/ave-kb/*); the scoping doc is a research/ artifact
- If a derivation seems trivial enough to attempt mid-session, STOP and report — that's Session 2 scope; Session 1 is pure scoping
- If Phase 2 inventory surfaces a corpus structural inconsistency, STOP and report rather than fix

## Cross-references

- Originating SDSS DR17 epic: [`c5-sdss-dr17-spin-orientation.md`](c5-sdss-dr17-spin-orientation.md) (CLOSED 2026-05-19 EOD; audit tag `audit/2026-05-19_c5-sdss-dr17-spin-orientation`)
- Cosmic axis cascade: [`omega-freeze-cosmic-grain-cascade.md`](../manuscript/ave-kb/common/omega-freeze-cosmic-grain-cascade.md) §3.1 Observable 6 + §4 Nested-cascade conjecture
- Class E framework: `~/.claude/skills/consistency-vs-emergence/SKILL.md` v1.1 (operating-point projection)
- Planetary-magnetosphere prior: [`planetary-magnetospheres.md`](../manuscript/ave-kb/vol3/cosmology/ch06-solar-system/planetary-magnetospheres.md) Uranus anomaly + 5-planet validation table
- Frame-dragging substrate-physics prior: [`frame-dragging-impedance-convolution.md:20`](../manuscript/ave-kb/vol3/gravity/ch02-general-relativity/frame-dragging-impedance-convolution.md) Op14 asymmetric saturation
- Parametric coupling prior: [`parametric-coupling-kernel.md`](../manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/parametric-coupling-kernel.md)
