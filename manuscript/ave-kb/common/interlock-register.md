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

- **mechanism:** the **Machian-boundary-impedance** termination — the dimensionless cosmological coupling ξ that sets Newton's G via `G = ℏc/(7 ξ m_e²)` (the "Bounding Limit 3" of the calibration chain), jointly constraining G to the operating point u₀* and m_e. This is a **MIXED** mechanism (G-ruling 2026-06-14): gravity's FORM is derived but G's VALUE is a calibration input. **(i) Form-derived half — the "Achromatic-Lens".** Under SYM-class scaling ε(r) and μ(r) co-scale by the same n(r), so Z_local(r) = √(μ/ε) ≡ Z₀ everywhere → Γ = 0 → reflectionless achromatic refraction (the matched-GRIN far-field); the 1/7 isotropic-impedance projection in a trace-reversed (ν=2/7) solid gives the /7 PPN coupling family. This half is substrate-derived (Ax 1 + Ax 4). **(ii) Value-fitted half — the ξ termination.** ξ ≈ 8.15×10⁴³ is NOT forward-derived: it is back-solved from CODATA G (`ξ = ℏc/(7 G m_e²)`, `constants.py:556` — circular by construction; G itself is the CODATA-input "Bounding Limit 3", `constants.py:544`). So the lens SHAPE (achromatic, /7) is earned but the coupling MAGNITUDE is calibration. Hence `mixed`, not `real`.
- **real-or-fitted:** mixed
- **status:** proposed
- **interlocks:** clm-iouqn9, clm-dsb560
- **derived-endpoint:** clm-dsb560
- **canonical-leaf:** `common/full-derivation-chain.md:59,85`
- **grounding:** TAG = mixed (form-derived / value-fitted), per Grant's 2026-06-14 G-ruling. **Form-derived (Achromatic-Lens):** `common/full-derivation-chain.md:85` ("Newton's constant emerges as the Machian boundary impedance G = ℏc/(7 ξ m_e²)") + the achromatic-impedance-matching leaf (`vol3/gravity/ch03-macroscopic-relativity/achromatic-impedance-matching.md`: Z_local ≡ Z₀ via symmetric ε·μ scaling) + the Achromatic-Lens write-up (`vol4/claim-quality.md:694-698`: "gravity as an *achromatic* impedance lens … μ and ε scale together, preserving the characteristic impedance"). **Value-fitted (ξ termination):** `constants.py:556` `XI_MACHIAN = HBAR*C_0/(7.0*G*M_E**2)` — ξ is inverted OUT of CODATA G, not predicted; `constants.py:544` tags G itself "CODATA-input (Bounding Limit 3)". So G is a CALIBRATION input (consistency-class), NOT an emergence; the count must NOT drop for G. WIRED into the operating point (`clm-iouqn9` ⟷ G via this hub), so G is a falsification-net **channel** like α — refuting G's calibration node (`clm-dsb560`) propagates a verifier failure to `clm-iouqn9`. **derived-endpoint = `clm-dsb560`** (G's home — its Route-2 of the three-route single-Ω_freeze projection "α, G, and J_cosmic"; an EXISTING input-only claim, NOT a fabricated input-only node; G has no dedicated clean input-only claim). It is the constant that WOULD become dependent if G flipped `mixed→real`.
  - **flip-test (mixed→real) = Chain B′ — DISCLOSED-OPEN.** G derived from {ℓ_node, α} alone, bypassing R_H (the cosmological horizon). Currently **0 closed-form candidates** (`research/2026-05-19_h-infinity-chain-b-prime-showstoppers.md` verdict; `constants.py:550-555` "the corpus-honest open path to breaking the circularity is the Chain B′ independent G derivation … currently OPEN"; corpus-self-stated at `vol3/cosmology/ch05-dark-sector/cosmological-constant-closure.md:106-112`). If Chain B′ ever lands, this node flips `mixed→real` and the live count drops 3→2.
  - **DISAMBIGUATION 1 — ξ ≠ R_H/ℓ_node.** ξ = 4π·(R_H/ℓ_node)·α⁻² ≈ 8.15×10⁴³ (`constants.py:541`, `full-derivation-chain.md:85`). The cosmic cell-count R_H/ℓ_node ~ 10³⁹ is ONE FACTOR inside ξ — NOT ξ itself (the 4π and α⁻² factors lift it ~5 OOM). Do not conflate the bridge ratio with the coupling.
  - **DISAMBIGUATION 2 — ξ ≠ ξ_topo (homonym).** The dimensionless Machian hierarchy coupling ξ ≈ 8.15×10⁴³ is NOT ξ_topo = e/ℓ_node (units C/m, the electromechanical transduction constant, **INVARIANT-C2**). Same glyph, orthogonal physics (cosmological boundary impedance vs charge-dislocation transduction). Per the `ave-kb/CLAUDE.md` INVARIANT-S2 warning ("Do not confuse ξ_topo = e/ℓ_node … with the dimensionless Machian hierarchy coupling ξ ≈ 8.15×10⁴³").
  - **FLAG (flag-don't-fix, for auditor + Grant):** the SAME formula ξ = 4π(R_H/ℓ_node)α⁻² is quoted at TWO magnitudes in the corpus — ≈ 8.15×10⁴³ here (`full-derivation-chain.md:85`, CLAUDE.md S2, `constants.py:541`) vs ≈ 3.455×10³⁸ at `common/xi-topo-traceability.md:23` (which converts via G = c⁴/(7 ξ T_EM)). A ~10⁵ discrepancy; the G-ruling mandates the 8.15×10⁴³ value, used here. NOT reconciled — surfaced for adjudication.
