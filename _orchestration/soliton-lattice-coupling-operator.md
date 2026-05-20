# Soliton-Lattice Coupling Operator Epic

**Status**: ACTIVE — Session 1 (scoping research doc only) ready to spawn
**Last updated**: 2026-05-19 EOD
**Originating session**: Orchestration session post-SDSS DR17 merge + Grant operator-output reframing 2026-05-19 EOD

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
| **1 (this epic)** | **Scoping research doc** — corpus inventory + operator structure sketch + derivation prereqs + testable predictions list + multi-session arc outline. **NO derivation in this session.** | 1-2 hr | ACTIVE — ready to spawn |
| 2 | Substrate-physics derivation of $\hat{\mathcal{O}}_{\text{soliton}}$ from Op14 + Cosserat + parametric coupling + frame-dragging interior | 3-5 hr (estimate) | QUEUED — gated on Session 1 prereq inventory |
| 3 | Application to planetary scale (8 planets × 2 axes = 16 data-points) | 2-3 hr | QUEUED — gated on Session 2 derivation |
| 4 | Extrapolation to galactic + LSS scale; predict $\hat{n}_{\text{galaxy-class}}$ for SDSS DR17 comparison | 2-3 hr | QUEUED — gated on Session 3 |
| 5 (conditional) | Refinement based on Sessions 1-4 outcomes | TBD | CONDITIONAL |

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
