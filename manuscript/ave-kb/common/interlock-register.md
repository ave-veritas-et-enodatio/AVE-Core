[↑ Common (Cross-Volume Resources) Index](index.md)

<!-- kb-frontmatter
kind: leaf
no-claim: "Canonical interlock register — hosts ilk- (joint-constraint-mechanism) nodes, the seventh tracked node type and the fourth edge class (interlocks). ilk- is a spine node-type specified in .index/SCHEMA.md and canonized in INVARIANT-S13 (extend-don't-reinvent); refresh-kb-metadata materializes each ilk- entry into claims.jsonl as a node_type: interlock-mechanism record and emits one interlocks edge per interlocked constant into depends-on.jsonl. This leaf originates no clm-/exp-/sup- node-body via frontmatter — the ilk- entries are body-hosted register entries (the ilk- analog of def- entries in the vocabulary register) — so it carries no-claim."
path-stable: "the canonical interlock-register leaf; makes the calibration-parameter interlock (mutual constraint) first-class + machine-enforced"
-->

<!-- interlock-meta
operating-point-root: clm-iouqn9
calibration-params: clm-0ktpcn clm-5xon03 clm-dsb560
expected-independent-count: 3
-->

# Interlock Register — Joint-Constraint Mechanisms (`ilk-` spine index)

The **source-of-truth index** for the AVE calibration-parameter **INTERLOCK** —
the substrate's mutual constraints among its calibration constants (α, G,
Ω_freeze, the operating point u₀*, …). Each entry is an `ilk-` node
(`\bilk-[a-z0-9]{6}\b`) recording the named substrate relation that mutually
constrains two (or more) constants, a `real_or_fitted` **chord/echo
classification**, an adjudication `status`, the `derived-endpoint` (the constant
made dependent iff the relation is real), and the EXISTING corpus leaf grounding
it. The interlock was previously prose-only; this register makes it first-class
and **verifier-gated**. The node-type + the symmetric `interlocks` relation are
specified in [`.index/SCHEMA.md`](../.index/SCHEMA.md) ("Interlock-mechanism
record") and canonized in [`INVARIANT-S13`](../CLAUDE.md) — a deliberate spine
extension per [`INVARIANT-S11`](../CLAUDE.md) (extend, don't reinvent), never a
parallel local scheme.

> **Prose umbrella.** This register is the CI-gated **machine home** for the
> `real_or_fitted` chord/echo axis. The prose organizing-principle home — the
> FORM-deriving / VALUE-importing meta-finding, with the per-constant accounting
> ({m_e, α, G} + the K=2G and E_yield instances) and the testing consequence — is
> [`form-deriving-value-importing.md`](form-deriving-value-importing.md). The
> chord / echo / mixed **definitions** are `def-` nodes (`def-ch0rd1` /
> `def-ech0v1` / `def-fmv001`) in
> [`vocabulary-register.md`](vocabulary-register.md). This register's tags are the
> authoritative per-mechanism classification those two leaves point back to.

> **Two derived, CI-enforced quantities ride on this register (INVARIANT-S13).**
> (1) The **LIVE independent-parameter count** = `(# calibration-param claim
> nodes) − (DOF removed by REAL, wired chords)`. Per Grant's 2026-06-14 G-ruling
> the node set is the explicitly-marked CALIBRATION set {m_e, α, G} (the
> `calibration-params:` meta line below: `clm-5xon03` m_e mass-scale, `clm-0ktpcn`
> α, `clm-dsb560` G via its Route-2), NOT the 143-member `build_band:"input-only"`
> band — resolving the earlier "two meanings of input" caveat. **Live count = 3**
> (all three fitted/mixed-value, none `real`-reduced). It is asserted in the
> `interlock-meta` block's `expected-independent-count:` (= 3) and recomputed by
> `make verify-kb-metadata` — a chord/echo tag flip (`fitted`/`mixed`→`real`)
> moves the count and breaks the assertion until the author deliberately updates
> it (α's `ilk-rr14gt` `fitted→real`, or G's `ilk-gravmb` `mixed→real` via Chain
> B′, each drops it 3→2). (2) The **falsification net**: per
> [`omega-freeze-cosmic-grain-cascade.md:11`](omega-freeze-cosmic-grain-cascade.md)
> the substrate has ONE DOF (the operating point `operating-point-root:` =
> `clm-iouqn9`, the K4 magic-angle u₀* ≈ 0.187); the interlocked channels are
> joint-constrained; **falsification of any one kills the operating point and the
> whole model** — marking any interlocked channel `refuted` propagates a verifier
> failure naming the root.

> **`real_or_fitted` is the chord/echo axis (`consistency-vs-emergence`,
> machine-enforced; THREE values as of the 2026-06-14 G-ruling).**
> `real-geometric-constraint` = a **chord**: the substrate independently forces
> the relation, so it removes one DOF (lowers the count via its
> `derived-endpoint`). `fitted-identification` = an **echo**: a named
> identification the substrate does NOT independently select — a consistency
> match that buys **NO** parameter reduction. `mixed` = **form-derived /
> value-fitted** (G): the FORM is derived (the Achromatic-Lens — SYM ε·μ
> co-scaling → Z=Z₀, Γ=0; the /7 PPN couplings) but the VALUE is a calibration
> input (the Machian-boundary-impedance termination ξ is back-solved from CODATA
> G). **COUNT SEMANTICS: `mixed` and `fitted-identification` BOTH do NOT reduce;
> ONLY `real-geometric-constraint` reduces.** A mixed mechanism's value-fitted
> half counts as an echo until its flip-test closes form-first (G via Chain B′).
> An echo — or a mixed value-fit — is not an emergence.

> **Status scope.** Newly minted mechanisms are seeded `proposed`, NEVER `SOLID`
> (an `ilk-` SOLID requires the mechanism AND its chord/echo classification to be
> adjudicated). Nothing here promotes to SOLID in this pass.

## Per-node field legend

Each `## <title>` heading carries a `<!-- id: ilk-xxxxxx -->` marker and a field
block (parallel to a `def-` vocabulary entry / a `claim-quality.md` `### Quality`
block, so refresh can parse it):

- **mechanism** — the constraint statement (the named substrate relation).
- **real-or-fitted** — `real-geometric-constraint` (chord — removes a DOF) | `mixed` (form-derived / value-fitted — removes none for counting, G's case) | `fitted-identification` (echo — removes none).
- **status** — `SOLID` (mechanism + classification adjudicated, cite confirms) | `proposed` (gated on review) | `retired` (superseded, preserved per Rule 12).
- **interlocks** — the interlocked constant `clm-` ids (the joint-constraint's endpoints; each emits one `interlocks` edge to THIS mechanism hub). Omit / `(none — catalogued)` for a catalogued-but-unwired mechanism.
- **derived-endpoint** — the constant made DEPENDENT iff `real-geometric-constraint` (the DOF a chord removes; must be one of the interlocked endpoints). For a `mixed` mechanism it is informational — the constant that WOULD become dependent if the value-fitted half closed form-first (e.g. G via Chain B′). `(none)` when not applicable (fitted, or unwired).
- **canonical-leaf** — the EXISTING corpus leaf `path:line` grounding the mechanism (ave-canonical-leaf-pull anchor; the file part is verifier-resolved).
- **grounding** — why the real/fitted classification is what it is (the chord/echo evidence; flag if uncertain).

> **Orthogonal view below (Grant 2026-06-24).** After the `ilk-` mechanism
> entries, the **[Calibration-Constant Criteria Register](#calibration-constant-criteria-register-per-constant-4-criteria--braced-status--graduation-gate)**
> gives the per-CONSTANT (`{m_e, α, G}`) view: the four Grant criteria
> (definition_uniqueness / routes_status / promotion_criterion / failure_causation)
> + a derived `braced_status` + the theory-level **graduation gate**. It mints no
> `ilk-` node and changes no `interlocks` edge — it is a VIEW over the nodes here,
> so the count machinery (`expected-independent-count: 3`) is byte-untouched.

---

## R·r = 1/4 (Golden-Torus screening)
<!-- id: ilk-rr14gt -->

- **mechanism:** R·r = 1/4 — at Axiom-4 self-saturation onset the electron bond LC tank's time-averaged elliptical-TIR phasor enclosed area equals the Nyquist cell cross-section area (πRr = π(d/2)²), fixing R·r = 1/4 at d = 1 ℓ_node. This is the screening regime (c) of the three-regime Golden-Torus closure that yields α⁻¹ = 4π³ + π² + π.
- **real-or-fitted:** fitted-identification
- **status:** proposed
- **interlocks:** clm-iouqn9, clm-0ktpcn
- **derived-endpoint:** clm-0ktpcn
- **canonical-leaf:** `vol1/ch8-alpha-golden-torus.md:11,44-46`
- **grounding:** GROUNDED FITTED. `vol1/ch8-alpha-golden-torus.md:11` states α's "exact value rests on ONE substrate-geometric identification per route — R·r=¼ (Golden-Torus route) … **which the substrate does NOT independently select**" (corroborated at `ch0-intro.md:21` and `vol1/claim-quality.md` clm-0ktpcn rationale; 4 dynamic engine tests + doc-34 S11-landscape-flatness + z₀ α-circularity all closed it Class B). A named identification = a consistency ECHO, not a chord → the alpha brace removes NO parameter. This is the INSTANCE-1 wired interlock: u₀* (clm-iouqn9, the operating point) ⟷ α (clm-0ktpcn) via R·r=1/4, with α the derived-endpoint that WOULD become dependent if this echo were ever lifted fitted→real.

---

## R − r = 1/2 (crossings / self-avoidance)
<!-- id: ilk-rmrhlf -->

- **mechanism:** R − r = 1/2 — at topologically-marked phase-space crossings two flux-tube strands touch at their edges without dielectric rupture; the centerline separation 2(R − r) must equal the tube diameter d (Ax 2 topo-kinematic isomorphism + dielectric-rupture self-avoidance). Crossings regime (b) of the Golden-Torus closure.
- **real-or-fitted:** real-geometric-constraint
- **status:** proposed
- **interlocks:** (none — catalogued)
- **derived-endpoint:** (none)
- **canonical-leaf:** `vol1/ch8-alpha-golden-torus.md:45`
- **grounding:** TAG = real-geometric-constraint, on the reading of `ch8-alpha-golden-torus.md:45` "centerline separation 2(R − r) **must equal** the tube diameter d" — a substrate-forced self-avoidance constraint (Ax 2 + dielectric rupture), not a named identification the substrate fails to select. FLAGGED for auditor: the corpus does not state "real" verbatim the way it states R·r=¼ is fitted at :11; "must equal" is read here as substrate-forcing. Catalogued-but-unwired in instance-1 (no `interlocks` edges) per brief §4 (only R·r=1/4 is the wired alpha brace), so this tag does not affect the live count.

---

## Compton-trapping condition (d = 1 Nyquist cell-trap + ℓ_node = electron-Compton identification)
<!-- id: ilk-cmptrp -->

- **mechanism:** the d = 1 ℓ_node Nyquist cell-trap (Ax 1 lattice sampling cutoff: the smallest stable soliton saturates at the Nyquist scale) COMBINED with the ℓ_node ≡ ℏ/(m_e c) identification fixing the lattice scale to the electron's Compton wavelength. Together these are the "Compton-resonance trapping condition" that FORCES α's scale (~1/137). Prose-named, not a single equation. Nyquist regime (a) of the Golden-Torus closure.
- **real-or-fitted:** fitted-identification
- **status:** proposed
- **interlocks:** (none — catalogued)
- **derived-endpoint:** (none)
- **canonical-leaf:** `vol1/ch8-alpha-golden-torus.md:11,44`
- **grounding:** TAG = fitted-identification, conservative. The d = 1 Nyquist cell-trap half (`ch8:44`) is substrate-forced (real); BUT the load-bearing scale-setting half — ℓ_node ≡ ℏ/(m_e c) (`ch0-intro.md:19,21`) — is an INPUT identification: `clm-5xon03` states "one of {m_e, ℓ_node} remains the input mass scale" (an empirical input, not derived). Because the mechanism's binding scale-fix rests on that input identification, the whole is conservatively tagged fitted-identification (echo). FLAGGED for auditor + Grant: this is a mixed mechanism (real Nyquist + fitted scale-identification) — whether to split it into two `ilk-` nodes (one real, one fitted) is an open design question. Catalogued-but-unwired in instance-1 (does not affect the count).

---

## G ← Machian-boundary-impedance termination (Achromatic-Lens far-field)
<!-- id: ilk-gravmb -->

- **mechanism:** the **Machian-boundary-impedance** termination — the dimensionless cosmological coupling ξ that sets Newton's G via `G = ℏc/(7 ξ m_e²)` (the "Bounding Limit 3" of the calibration chain), jointly constraining G to the operating point u₀* and m_e. This is a **MIXED** mechanism (G-ruling 2026-06-14): gravity's FORM is derived but G's VALUE is a calibration input. **(i) Form-derived half — the "Achromatic-Lens".** Under SYM-class scaling ε(r) and μ(r) co-scale by the same n(r), so Z_local(r) = √(μ/ε) ≡ Z₀ everywhere → Γ = 0 → reflectionless achromatic refraction (the matched-GRIN far-field); the 1/7 isotropic-impedance projection in a trace-reversed (ν=2/7) solid gives the /7 PPN coupling family. This half is substrate-derived (Ax 1 + Ax 4). **(ii) Value-fitted half — the ξ termination.** ξ ≈ 8.15×10⁴³ is NOT forward-derived: it is back-solved from CODATA G (`ξ = ℏc/(7 G m_e²)`, `constants.py:589` `XI_MACHIAN` — circular by construction; G itself is the CODATA-input "Bounding Limit 3", `constants.py:177` `G`, tagged at `constants.py:577`). So the lens SHAPE (achromatic, /7) is earned but the coupling MAGNITUDE is calibration. Hence `mixed`, not `real`.
- **real-or-fitted:** mixed
- **status:** proposed
- **interlocks:** clm-iouqn9, clm-dsb560
- **derived-endpoint:** clm-dsb560
- **canonical-leaf:** `common/full-derivation-chain.md:59,85`
- **grounding:** TAG = mixed (form-derived / value-fitted), per Grant's 2026-06-14 G-ruling. **Form-derived (Achromatic-Lens):** `common/full-derivation-chain.md:85` ("Newton's constant emerges as the Machian boundary impedance G = ℏc/(7 ξ m_e²)") + the achromatic-impedance-matching leaf (`vol3/gravity/ch03-macroscopic-relativity/achromatic-impedance-matching.md`: Z_local ≡ Z₀ via symmetric ε·μ scaling) + the Achromatic-Lens write-up (`vol4/claim-quality.md:694-698`: "gravity as an *achromatic* impedance lens … μ and ε scale together, preserving the characteristic impedance"). **Value-fitted (ξ termination):** `constants.py:589` `XI_MACHIAN = HBAR*C_0/(7.0*G*M_E**2)` — ξ is inverted OUT of CODATA G, not predicted; `constants.py:177` `G = 6.67430e-11` tagged "CODATA-input (Bounding Limit 3)" at `constants.py:577`. So G is a CALIBRATION input (consistency-class), NOT an emergence; the count must NOT drop for G. WIRED into the operating point (`clm-iouqn9` ⟷ G via this hub), so G is a falsification-net **channel** like α — refuting G's calibration node (`clm-dsb560`) propagates a verifier failure to `clm-iouqn9`. **derived-endpoint = `clm-dsb560`** (G's home — its Route-2 of the three-route single-Ω_freeze projection "α, G, and J_cosmic"; an EXISTING input-only claim, NOT a fabricated input-only node; G has no dedicated clean input-only claim). It is the constant that WOULD become dependent if G flipped `mixed→real`.
  - **flip-test (mixed→real) = Chain B′ — DISCLOSED-OPEN.** G derived from {ℓ_node, α} alone, bypassing R_H (the cosmological horizon). Currently **0 closed-form candidates** (`research/2026-05-19_h-infinity-chain-b-prime-showstoppers.md` verdict; `constants.py:583-588` "the corpus-honest open path to breaking the circularity is the Chain B′ independent G derivation … currently OPEN"; corpus-self-stated at `vol3/cosmology/ch05-dark-sector/cosmological-constant-closure.md` §"What would strengthen this further"). If Chain B′ ever lands, this node flips `mixed→real` and the live count drops 3→2.
  - **DISAMBIGUATION 1 — ξ ≠ R_H/ℓ_node.** ξ = 4π·(R_H/ℓ_node)·α⁻² ≈ 8.15×10⁴³ (`constants.py:589` `XI_MACHIAN`, `full-derivation-chain.md:85`). The cosmic cell-count R_H/ℓ_node ≈ 3.46×10³⁸ is ONE FACTOR inside ξ — NOT ξ itself (the 4π·α⁻² ≈ 2.36×10⁵ factor lifts it ~5 OOM). Do not conflate the bridge ratio with the coupling.
  - **DISAMBIGUATION 2 — ξ ≠ ξ_topo (homonym).** The dimensionless Machian hierarchy coupling ξ ≈ 8.15×10⁴³ is NOT ξ_topo = e/ℓ_node (units C/m, the electromechanical transduction constant, **INVARIANT-C2**). Same glyph, orthogonal physics (cosmological boundary impedance vs charge-dislocation transduction). Per the `ave-kb/CLAUDE.md` INVARIANT-S2 warning ("Do not confuse ξ_topo = e/ℓ_node … with the dimensionless Machian hierarchy coupling ξ ≈ 8.15×10⁴³").
  - **DISCHARGED (was flag-don't-fix, resolved by xi-symbol-cleanup PR):** the SAME formula ξ = 4π(R_H/ℓ_node)α⁻² was previously quoted at TWO magnitudes in the corpus — ≈ 8.15×10⁴³ here (`full-derivation-chain.md:85`, CLAUDE.md S2, `constants.py:589`) vs ≈ 3.455×10³⁸ at `common/xi-topo-traceability.md:23`. The 3.455×10³⁸ was the cosmic cell-count *factor* R_H/ℓ_node mis-paired with the full ξ formula (a 5.4-OOM mis-labelling). RESOLVED: `xi-topo-traceability.md:23` now reads 8.15×10⁴³ for ξ_M with a separate explicit row for the R_H/ℓ_node ≈ 3.46×10³⁸ factor. The G-ruling 8.15×10⁴³ value (= `constants.py:589` `XI_MACHIAN`) is now the single corpus magnitude.

---

# Calibration-Constant Criteria Register (per-constant 4-criteria + braced-status + graduation gate)

> **What this section adds (Grant directive 2026-06-24; KEEP-BOTH additive).** The
> `ilk-` entries above are organized **per joint-constraint mechanism** (R·r=¼,
> the Machian termination, …). This section is the orthogonal **per-CALIBRATION-CONSTANT**
> view: for EACH constant in the marked set `{m_e, α, G}` it tracks the four
> criteria Grant requires, plus a derived **braced-status** and the theory-level
> **graduation gate**. It does NOT mint any new `ilk-` node, does NOT carry an
> `<!-- id: ilk-xxxxxx -->` marker, and does NOT add or remove any `interlocks`
> edge — so the LIVE independent-parameter count machinery
> (`expected-independent-count: 3`, the falsification net, the four materialized
> `ilk-` nodes) is **byte-untouched** by this section. It is a prose + bolded-field
> register that POINTS AT the `ilk-` tags and `clm-` nodes already wired above
> (INVARIANT-S11 extend-don't-reinvent: this is a new VIEW over existing nodes,
> not a parallel scheme). The `###` per-constant subheadings are deliberately h3
> (not h2) so the `ilk-` register parser — which materializes a node only from a
> `## ` heading immediately followed by an `ilk-` id marker — never treats them as
> mechanism nodes.

## Per-constant criteria schema (the four fields + braced-status + class)

Each `### <constant>` subheading below carries a bolded field block parallel to an
`ilk-` entry's, with these per-constant fields:

- **class** — the FORM-vs-VALUE landing site (the [`form-deriving-value-importing.md`](form-deriving-value-importing.md) per-constant verdict): `SCALE / definitional-anchor` (m_e) | `ECHO` (α value) | `MIXED` (G). This is the human-facing roll-up of the wired `ilk-` `real_or_fitted` tag(s) for that constant.
- **definition_uniqueness (criterion 1)** — the ONE universal tractable definition / identity for the constant, and whether it is `ASSERTED` (a definitional anchor / named identification) or `UNIQUE-FORM` (a substrate-forced dimensionless skeleton). Flags any definition-display duplication / grade-attribution fork that muddies the single-definition claim.
- **routes_status (criterion 2)** — the lift-route map. **ENCODED HONESTLY per the Grant-RATIFIED 2026-06-24 rule: NEVER "exhausted"; only `open — N routes closed-negative, flip-condition LIVE/DEAD`.** A `closed-negative` route is REFUTED for that route; it is NOT a proof the route-space is empty. A brace is `forced` only when route-space-completeness is itself Grant-ratified — which has NOT happened for any constant — so this field forces the **closed ≠ exhausted** distinction and a brace is never quietly claimed forced when it is merely un-refuted. `N/A` only for the irreducible dimensional scale (m_e), where there is no route-space because there is nothing to derive it FROM (it IS the anchor).
- **promotion_criterion (criterion 3)** — the explicit, pre-registered condition that would promote `echo → form-derived` (`fitted → real`, or `mixed → real`). **The promotion criterion IS the VCA-R19 forced-not-accommodated knife**: the relation between constants must be FORCED by the substrate (no free dial that was tuned to fit), not merely ACCOMMODATED (consistent-after-the-fact). `N/A` for m_e (the anchor cannot be promoted — there is nothing to promote it from).
- **failure_causation (criterion 4)** — whether the constant's USE is currently causing a sim / derivation failure: `INNOCENT` (its use is corpus-honest and α-free / value-free where it must be) vs `CULPABLE` (its use bakes a circular value into a derivation that then "confirms" it). Records the specific culpability episode and the scrub that returned it to innocent, if any.
- **braced_status (derived)** — `forced-braced` (the relation IS forced — promotion criterion met, Grant-ratified) | `un-refuted-only` (closed-negative on named routes, flip-condition live, NOT route-space-complete → still an echo/mixed for counting) | `irreducible-anchor` (m_e). **No constant is `forced-braced` as of 2026-06-24.** This is the field the graduation gate reads.

> **How this integrates with the existing machinery (no double-counting).** The
> `class` + `braced_status` here are the human roll-up of the CI-gated
> `real_or_fitted` tags on the `ilk-` nodes above; the `routes_status` /
> `promotion_criterion` are the prose elaboration of each `ilk-` node's
> `grounding` + flip-test. **The count is still computed ONLY from the `ilk-`
> `real_or_fitted` tags** (`compute_independent_parameter_count`), NOT from this
> section — a constant graduates in the count exactly when its `ilk-` tag flips
> `fitted`/`mixed → real`, which moves `expected-independent-count` and breaks the
> CI assertion (the loud-on-drift gate). This section's `braced_status` is the
> NARRATIVE precondition for that flip; the `ilk-` tag is the machine truth. They
> agree by construction (a constant is `forced-braced` here IFF its `ilk-` tag is
> `real` there).

### m_e — the irreducible dimensionful scale (the 1 anchor)

- **constant:** m_e (electron rest mass), with its two derived voltage/length anchors `V_snap ≡ m_e c²/e ≈ 511 kV` and `ℓ_node ≡ ℏ/(m_e c) ≈ 3.86×10⁻¹³ m`.
- **class:** SCALE / definitional-anchor (per [`form-deriving-value-importing.md:66`](form-deriving-value-importing.md) "m_e / ℓ_node = DEFINITIONAL"; `clm-5xon03`).
- **definition_uniqueness (criterion 1):** ASSERTED. The one universal identity is the Axiom-1 calibration identity `ℓ_node ≡ ℏ/(m_e c)` (`eq_calibration_constants.tex:31-35`; `vol1/claim-quality.md:25` "one of {m_e, ℓ_node} remains an empirical input"), with `V_snap ≡ m_e c²/e` (`eq_calibration_constants.tex:57-61`; `constants.py:450`). m_e is an INPUT by construction — the single dimensionful scale that calibrates the lattice; nothing in the substrate is asked to SELECT its value. No definition-fork: it is the anchor, definitionally.
- **routes_status (criterion 2):** N/A — the irreducible dimensional scale. There is no lift-route map because there is nothing to derive m_e FROM: it IS the dimensional floor (one dimensionful scale is required by dimensional analysis, universal — see graduation gate). Encoding "N/A" here is NOT the closed≠exhausted distinction being waived; it is the recognition that the route-space is empty *a priori* (no antecedent to derive a scale from), distinct from α/G whose route-spaces are non-empty but closed-negative-so-far.
- **promotion_criterion (criterion 3):** N/A — the anchor cannot be promoted. There is no `echo → form-derived` transition for the unit anchor; "deriving m_e" would require a SECOND dimensionful input to express it against, which just relocates the irreducible scale. The dimensional-analysis floor makes literally-zero dimensionful inputs impossible (graduation gate), so m_e's irreducibility is universal, not an open gap.
- **failure_causation (criterion 4):** INNOCENT — the unit anchor. m_e's use is corpus-honest by construction: it sets the scale, it is never back-solved from a downstream quantity it then "confirms". It is the benign reference every dimensionful magnitude is expressed against. No culpability episode.
- **braced_status (derived):** irreducible-anchor. m_e is NOT counted as a brace-able echo — it is the dimensionful floor the graduation gate explicitly exempts. It does NOT lower or raise `expected-independent-count` (it is one of the three marked calibration claims, but its `ilk-cmptrp` half is `fitted-identification`, which removes no DOF; the count stays 3).
- **grounding:** `eq_calibration_constants.tex:31-35,57-61` (the two anchor identities); `clm-5xon03` + `vol1/claim-quality.md:25` (the one-empirical-input-mass-scale disclosure); [`form-deriving-value-importing.md:66`](form-deriving-value-importing.md) (DEFINITIONAL verdict). The relevant `ilk-` node is `ilk-cmptrp` (the Compton-trapping condition, whose load-bearing scale-fix IS the `ℓ_node ≡ ℏ/(m_e c)` input identification — tagged `fitted-identification` there because the binding half is this input).

### α — the fine-structure constant (ECHO, ilk-rr14gt)

- **constant:** α (fine-structure constant), `α⁻¹ ≈ 137.036`; interlocked to the operating point u₀* (`clm-iouqn9`) via R·r=¼ (`ilk-rr14gt`). Calibration claim `clm-0ktpcn`.
- **class:** ECHO (the *value*; `ilk-rr14gt` `real_or_fitted = fitted-identification`). Per [`form-deriving-value-importing.md:62`](form-deriving-value-importing.md): the α-decomposition FORM and the *scale* (~1/137) are forced; the *exact value* rests on R·r=¼, a named identification the substrate does NOT independently select.
- **definition_uniqueness (criterion 1):** UNIQUE-FORM **with one flagged display-duplication** (the def-vyvsn1 grade fork, formerly FLAG 1, is now RESOLVED). The one universal tractable FORM is `α⁻¹ = 4π³ + π² + π` (= `Λ_vol + Λ_surf + Λ_line`; `vol1/ch8-alpha-golden-torus.md:11`), a unique dimensionless skeleton. **`def-vyvsn1` grade-attribution fork — RESOLVED = T2 (Grant 2026-06-30):** the α-keyed yield threshold `V_yield = √α · V_snap` (`eq_calibration_constants.tex:63-67`; `constants.py:464`) had a sector-attribution conflict — `nonlinear-vacuum-capacitance.md:16` put the V_yield varactor on the LONGITUDINAL-A1 bond compliance, while `constants.py` + `pair-production-axiom-derivation.md:102` (#416) put it on the TRANSVERSE Cosserat-T2 self-trap. **Adjudicated: `V_yield` is the transverse-T2 self-trap wall; the A1 varactor was re-keyed to `V_snap`** ([`vocabulary-register.md`](vocabulary-register.md) def-vyvsn1 status SOLID), removing the conflict. It never changed α's ECHO class (the √α is the imported α-echo either way per `research/2026-06-24_forka-alpha-flip.md:75`), and the single-definition claim now stands clean. **FLAG — definition-display dup:** `eq_calibration_constants.tex` is `\input` TWICE in the foreword (`frontmatter/00_foreword.tex:50` and `:61`), so the α definition-display (`eq_calibration_constants.tex:51-55`) renders doubly — a display duplication, not a second derivation.
- **routes_status (criterion 2):** **OPEN — every named route closed-negative, flip-condition LIVE (NOT exhausted).** Per the Grant-RATIFIED closed≠exhausted rule: the named lift-routes to force the α *value* are each REFUTED, but the route-space is NOT provably empty. The original three routes (geometry / eigenmode / cross-route) + the 2026-06-24 keystone (coupling-PRODUCES) are joined by the four 2026-06-25 routes (variational/lattice A, EMT-percolation B, OCXO loaded-Q C, f_b-boundary D — consolidated register at [`research/2026-06-25_delta-strain-session-synthesis.md`](../../../research/2026-06-25_delta-strain-session-synthesis.md)).
  - **geometry route** (R·r=¼ substrate-selected) — closed-negative: `vol1/ch8-alpha-golden-torus.md:11` "which the substrate does NOT independently select" (4 dynamic engine tests + doc-34 S11-landscape-flatness).
  - **eigenmode route** (z₀ α-circularity) — closed-negative: the z₀ route closes the z₀-circularity (per the `ilk-rr14gt` grounding, `vol1/claim-quality.md` clm-0ktpcn rationale).
  - **cross-route** (over-determination of the ½/¼ pair) — closed-negative (the coincidence-magnet tell; 2026-06-04 re-challenge config-grep negative).
  - **coupling-PRODUCES route** (the Q-point pressure-equilibrium forces R·r=¼ α-free) — **closed-negative 2026-06-24 (the keystone):** [`research/2026-06-24_forka-alpha-flip.md:14,39`](../../../research/2026-06-24_forka-alpha-flip.md) "VERDICT: ECHO … No pressure condition produces the *product* R·r" — α re-enters via the √α bias ladder + Z₀∝α area-bridge. **flip-condition: LIVE** — any not-yet-tried pressure/eigenmode route that closes through the FORM (not √α) would flip it; the route-space is NOT exhausted ([`form-deriving-value-importing.md:80-82`](form-deriving-value-importing.md) "the flip-condition is live; the route-space is not provably exhausted"; `vol1/ch8-alpha-golden-torus.md:13` "scoped-echo register").
  - **variational / lattice strain-projection route (Open A, 2026-06-25)** — **closed-negative:** maximizing the substrate strain-projection `s_grav = Π·γ` does NOT select the α packing — the admissibility-weighted max lands at `K/G≈1.83` (`p≈0.193`, +5.17%), distinct from the K/G=2 trace-reversal lock (`+1.38%`, z=52 wrong target). Gravity-stable projection is a *constraint*, not the unconstrained optimum; G's ξ chain is α-circular. ([`research/2026-06-25_delta-strain-session-synthesis.md`](../../../research/2026-06-25_delta-strain-session-synthesis.md) §4 Open A; `research/2026-06-25_alpha-variational-strain-projection_result.md`.)
  - **EMT-percolation δ_strain route (Open B, 2026-06-25)** — **closed-negative:** forward δ_strain from rigidity-percolation / node-participation sensitivity misses the 2.2 ppm target by **−4 to −5 dex** (FT-1 BE control: −31 dex); the percolation routes are tautological (`1−p_cold/p_obs`) or lack an independent δu driver. Generic spring-network physics, not AVE-distinct. ([`research/2026-06-25_delta-strain-session-synthesis.md`](../../../research/2026-06-25_delta-strain-session-synthesis.md) §4 Open B; `research/2026-06-25_openB-delta-strain-percolation_result.md`.)
  - **OCXO loaded-Q route (Open C, 2026-06-25)** — **consistency-reframe (not a lift):** δ_strain reads as a Q-point √α bias-ladder / loaded-resonator SPECIFICATION mismatch (cold geometry vs CODATA in-situ charge-port), reproducing 2.2 ppm exactly because L0/L1/L2 use the same cold/CODATA α pair (tautology); the BE/latent forward routes stay dead. Reframes the *magnitude provenance* of the standing echo — it does NOT force the α value. ([`research/2026-06-25_delta-strain-session-synthesis.md`](../../../research/2026-06-25_delta-strain-session-synthesis.md) §4 Open C; `research/2026-06-25_alpha-loaded-q-ocxo_result.md`.)
  - **f_b boundary-participation route (Open D, 2026-06-25)** — **partial / OOM-bracket, not a chord:** geometry supplies the `~½` participation factor on top of an assumed `α²` boundary-coupling kernel (Open D brackets δ_strain to ~±10%), but the exact match needs `f_b≈0.455` (inversion-only tautology), not a discrete forward identity. Bracket + calibrated input, not an independent lift. ([`research/2026-06-25_delta-strain-session-synthesis.md`](../../../research/2026-06-25_delta-strain-session-synthesis.md) §4 Open D; `research/2026-06-25_f-boundary-participation_result.md`.)
  - **Net (2026-06-25 arc):** all four routes are closed-negative / consistency-reframe / partial — **none forces the α value through the FORM**. The α brace stays an ECHO; `braced_status` stays `un-refuted-only`, count contribution = 0 DOF removed, **flip-condition stays LIVE** (the route-space is not provably exhausted). Consolidated closed-route register: [`research/2026-06-25_delta-strain-session-synthesis.md`](../../../research/2026-06-25_delta-strain-session-synthesis.md) (audit-verified SOUND).
- **promotion_criterion (criterion 3):** VCA-R19 forced-not-accommodated. α's value graduates `echo → form-derived` (flips `ilk-rr14gt` `fitted → real`, dropping the count 3→2) IFF a route FORCES R·r=¼ (or the α-value directly) from the substrate WITHOUT importing α anywhere in the closure — i.e. a genuinely α-free closure of the dimensionless skeleton's *value*, FORCED not merely ACCOMMODATED. The 2026-06-24 keystone is the template of an accommodated-not-forced failure: the pressure route is α-free on INPUT but re-imports √α to CLOSE (`research/2026-06-24_forka-alpha-flip.md:80`), so it accommodates, it does not force.
- **failure_causation (criterion 4):** **CULPABLE-episode → SCRUBBED → INNOCENT-when-α-free.** The baked `Q_TANK = 1/α` in `cvr_model.py` was CULPABLE for the #41 circularity — a derivation that imports α (via Q=1/α) and then "confirms" α is circular by construction. RESOLVED by the α-free CI-gate: the import-time guards `assert "Q_TANK" not in globals()` / `"alpha-leak: Q_TANK (=1/alpha) must NOT be imported"` now scrub α-carriers out of the genesis solvers (`solvers/node_scattering_multiplicity.py:70`, `solvers/native_cage_imex.py:62,83`, `solvers/fork_b_saturation_tank.py:90`, `core/s1_winding_conservation_gate.py:23,43`). The 2026-06-24 keystone (`research/2026-06-24_engine-coupled-eigensolve_result.md:177-180`) RAN α-clean (κ̃=6/5, α-free; Q=137 stays EMPTY) — so α's use there is INNOCENT. Culpable ONLY when α is baked into the closure; innocent when α-free.
- **braced_status (derived):** un-refuted-only — NOT forced-braced. The α-value brace is closed-negative on every named route but the route-space is not route-space-complete (flip-condition live), so it is an ECHO for counting. `ilk-rr14gt` stays `fitted-identification`; count contribution = 0 DOF removed.
- **grounding:** `ilk-rr14gt` (above) + `vol1/ch8-alpha-golden-torus.md:11,13`; [`form-deriving-value-importing.md:62,80-82`](form-deriving-value-importing.md); the keystone [`research/2026-06-24_forka-alpha-flip.md:14,39,75,80`](../../../research/2026-06-24_forka-alpha-flip.md); the four 2026-06-25 routes (consolidated, audit-verified SOUND) [`research/2026-06-25_delta-strain-session-synthesis.md`](../../../research/2026-06-25_delta-strain-session-synthesis.md); `def-vyvsn1` ([`vocabulary-register.md:660-670`](vocabulary-register.md)); the α-free CI-gate guards (`solvers/*.py`, `core/s1_winding_conservation_gate.py`).

### G — Newton's constant (MIXED, ilk-gravmb)

- **constant:** G (Newton's constant), `G ≈ 6.674×10⁻¹¹` (`constants.py:177`); interlocked to the operating point u₀* (`clm-iouqn9`) via the Machian-boundary-impedance termination (`ilk-gravmb`). Calibration claim `clm-dsb560` (Route-2 of the three-route single-Ω_freeze projection).
- **class:** MIXED — form-derived / value-fitted (`ilk-gravmb` `real_or_fitted = mixed`; per [`form-deriving-value-importing.md:63`](form-deriving-value-importing.md), NEVER a pure echo — the derived-form half must be preserved).
- **definition_uniqueness (criterion 1):** MIXED definition. The one tractable identity is `G = ℏc/(7 ξ m_e²)` (`common/full-derivation-chain.md:85`; `constants.py:589` `XI_MACHIAN`). Its TWO halves carry opposite provenance: **(i) FORM-derived** — the Achromatic-Lens `/7` PPN projection (SYM ε·μ co-scaling → Z=Z₀, Γ=0; substrate-derived from Ax 1 + Ax 4, `ilk-gravmb` grounding) is a UNIQUE-FORM; **(ii) VALUE-fitted** — the dimensionless termination ξ ≈ 8.15×10⁴³ is ASSERTED (back-solved `ξ = ℏc/(7 G m_e²)` from CODATA G, `constants.py:589` — circular not forward). So the SHAPE is unique/forced; the MAGNITUDE is a calibration input. (Disambiguation guards on ξ ≠ R_H/ℓ_node and ξ ≠ ξ_topo live on `ilk-gravmb` above.)
- **routes_status (criterion 2):** **OPEN — Chain-B′ open (0 closed-form candidates), flip-condition LIVE (NOT exhausted).** The lift-route to force G's *value* form-first is **Chain B′** — G derived from {ℓ_node, α} alone, bypassing R_H (the cosmological horizon). Currently **0 closed-form candidates** (`research/2026-05-19_h-infinity-chain-b-prime-showstoppers.md` verdict; `constants.py:583-588` "the corpus-honest open path … currently OPEN"; `vol3/cosmology/ch05-dark-sector/cosmological-constant-closure.md` §"What would strengthen this further"). **DISTINCTION (Grant-RATIFIED closed≠exhausted):** Chain B′ is `OPEN — no candidate has closed`, which is NOT `route-space exhausted` — it is the un-landed flip-route. flip-condition: LIVE (a future closed-form Chain B′ flips it). The forward single-operating-point test `𝒥_cosmic` (CMB axis-of-evil → Ω̂_freeze) is the experimental converter ([`form-deriving-value-importing.md:119-123`](form-deriving-value-importing.md): PASS=chord, FAIL=echo).
- **promotion_criterion (criterion 3):** VCA-R19 forced-not-accommodated, instantiated as **Chain B′ closed-form (mixed→real)**. G graduates `mixed → real` (flips `ilk-gravmb` `mixed → real`, dropping the count 3→2) IFF a closed-form derivation of G from {ℓ_node, α} lands that does NOT back-solve ξ from CODATA G — i.e. ξ is FORCED forward (no CODATA-G dial tuned to fit), not ACCOMMODATED by inversion. The current `XI_MACHIAN = HBAR*C_0/(7.0*G*M_E**2)` (`constants.py:589`) is the accommodated-not-forced template: ξ is inverted OUT of the target it is meant to predict.
- **failure_causation (criterion 4):** **CULPABLE-circular (the value half).** G's VALUE-use is CULPABLE: ξ is back-solved from CODATA G (`constants.py:589`), so any derivation that "predicts" G through ξ is circular by construction — it confirms the input it consumed. This is NOT scrubbed (unlike α's Q_TANK) because it is the standing state of the mixed mechanism: the value half stays culpable-circular until Chain B′ closes form-first. The FORM half (the Achromatic-Lens /7 projection) is INNOCENT — it is derived, not back-solved. So G's failure_causation is half-and-half: form INNOCENT, value CULPABLE-circular.
- **braced_status (derived):** un-refuted-only (the value half) / form-derived (the form half) — NOT forced-braced overall. `ilk-gravmb` stays `mixed`; the value-fitted half counts as an echo (removes 0 DOF) until Chain B′ closes. The form half is a real chord but it does not by itself reduce the count (the count drops only on a `real` tag, which requires the WHOLE mechanism — including the value — to close form-first).
- **grounding:** `ilk-gravmb` (above) + `common/full-derivation-chain.md:59,85`; `constants.py:177,577,583-588,589`; [`form-deriving-value-importing.md:63`](form-deriving-value-importing.md); `research/2026-05-19_h-infinity-chain-b-prime-showstoppers.md` (Chain B′ verdict); `vol3/cosmology/ch05-dark-sector/cosmological-constant-closure.md` (the strengthen-further self-statement).

## The graduation gate (the zero-free-params answer)

> **The two-part answer Grant requires (2026-06-24), stated honestly.**

**(A) Literally-zero free parameters = NEVER.** A physical theory cannot have
zero dimensionful inputs: by **dimensional analysis** at least ONE dimensionful
scale is irreducible (you cannot manufacture a metre, a kilogram, or a second out
of pure dimensionless geometry). AVE's single dimensionful anchor is **m_e** (with
its derived `ℓ_node`, `V_snap`) — see the `### m_e` entry above:
`class = SCALE / definitional-anchor`, `routes = N/A`, `braced_status =
irreducible-anchor`. This floor is **universal** (it binds the SM, GR, and every
other framework equally — the SM also carries a dimensionful scale), so "AVE has
1 dimensionful input" is NOT an AVE-specific comedown; it is the dimensional-analysis
floor that no theory clears. **The honest headline is therefore "ONE dimensionful
input (m_e), irreducible — never literally zero."**

**(B) Zero DIMENSIONLESS free parameters = YES, IFF every dimensionless constant
is FORCED-braced (not fitted).** This is the achievable graduation target and the
knife is **VCA-R19 forced-not-accommodated applied to the RELATIONS between the
constants**: the theory reaches zero dimensionless free parameters exactly when
EVERY dimensionless calibration constant has `braced_status = forced-braced` —
i.e. its `ilk-` `real_or_fitted` tag has flipped to `real-geometric-constraint`
because a route FORCED the relation (no free dial tuned to fit), not merely
ACCOMMODATED it. **As of 2026-06-24 this is NOT met:**

| Dimensionless constant | `ilk-` tag | braced_status | what must close |
|---|---|---|---|
| **α** (value) | `ilk-rr14gt` `fitted-identification` | un-refuted-only | an α-free route that FORCES R·r=¼ / the α-value (flip-condition live, route-space NOT exhausted) |
| **G** (value half) | `ilk-gravmb` `mixed` | un-refuted-only | **Chain B′** closed-form (G from {ℓ_node, α}, ξ forced not back-solved) |

So the LIVE independent-parameter count is **3** (the marked `{m_e, α, G}`, none
`real`-reduced — `expected-independent-count: 3`, CI-asserted in the meta header).
The count drops `3 → 2` on the FIRST dimensionless flip (α via `ilk-rr14gt`, or G
via `ilk-gravmb` Chain B′) and `3 → 1` (= the irreducible m_e floor, the
zero-DIMENSIONLESS-free-params graduation) only when BOTH α and G flip
`forced-braced`. **The single forward test that would convert the {α, G}
operating-point story from echo to chord is `𝒥_cosmic`** (CMB axis-of-evil →
`Ω̂_freeze`: one operating point setting EM + gravity + cosmology) — PASS = chord,
FAIL = echo (the three-route commitment, [`form-deriving-value-importing.md:119-123`](form-deriving-value-importing.md)).

> **Honesty caveat (closed ≠ exhausted, restated at the gate).** The graduation to
> zero-dimensionless-free-params is **GATED, not pending-imminent**: every
> dimensionless brace is currently `un-refuted-only` (closed-negative on named
> routes, flip-condition LIVE), NOT `forced-braced`. No brace may be quietly
> claimed forced merely because its named lift-routes are un-refuted — the
> route-space is not provably complete for either α or G. The aspirational
> `u₀*`-as-single-DOF story (one operating point forcing both α and G) is the
> graduation TARGET, gated on `𝒥_cosmic`; it is not a current achievement. The
> `braced_status` field is the audit-able qualifier the gate reads, and it reads
> `un-refuted-only` for every dimensionless constant today.
