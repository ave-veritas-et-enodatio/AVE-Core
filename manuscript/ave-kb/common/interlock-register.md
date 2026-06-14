[↑ Common (Cross-Volume Resources) Index](index.md)

<!-- kb-frontmatter
kind: leaf
no-claim: "Canonical interlock register — hosts ilk- (joint-constraint-mechanism) nodes, the seventh tracked node type and the fourth edge class (interlocks). ilk- is a spine node-type specified in .index/SCHEMA.md and canonized in INVARIANT-S13 (extend-don't-reinvent); refresh-kb-metadata materializes each ilk- entry into claims.jsonl as a node_type: interlock-mechanism record and emits one interlocks edge per interlocked constant into depends-on.jsonl. This leaf originates no clm-/exp-/sup- node-body via frontmatter — the ilk- entries are body-hosted register entries (the ilk- analog of def- entries in the vocabulary register) — so it carries no-claim."
path-stable: "the canonical interlock-register leaf; makes the calibration-parameter interlock (mutual constraint) first-class + machine-enforced"
-->

<!-- interlock-meta
operating-point-root: clm-iouqn9
expected-independent-count: 143
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

> **Two derived, CI-enforced quantities ride on this register (INVARIANT-S13).**
> (1) The **LIVE independent-parameter count** = `(# input-only claim nodes) −
> (DOF removed by REAL, wired chords)`, asserted in the `interlock-meta` block's
> `expected-independent-count:` and recomputed by `make verify-kb-metadata` — a
> chord/echo tag flip (`fitted`↔`real`) moves the count and breaks the assertion
> until the author deliberately updates it. (2) The **falsification net**: per
> [`omega-freeze-cosmic-grain-cascade.md:11`](omega-freeze-cosmic-grain-cascade.md)
> the substrate has ONE DOF (the operating point `operating-point-root:` =
> `clm-iouqn9`, the K4 magic-angle u₀* ≈ 0.187); the interlocked channels are
> joint-constrained; **falsification of any one kills the operating point and the
> whole model** — marking any interlocked channel `refuted` propagates a verifier
> failure naming the root.

> **`real_or_fitted` is the chord/echo axis (`consistency-vs-emergence`,
> machine-enforced).** `real-geometric-constraint` = a **chord**: the substrate
> independently forces the relation, so it removes one DOF (lowers the count via
> its `derived-endpoint`). `fitted-identification` = an **echo**: a named
> identification the substrate does NOT independently select — a consistency
> match that buys **NO** parameter reduction. An echo is not an emergence.

> **Status scope.** Newly minted mechanisms are seeded `proposed`, NEVER `SOLID`
> (an `ilk-` SOLID requires the mechanism AND its chord/echo classification to be
> adjudicated). Nothing here promotes to SOLID in this pass.

## Per-node field legend

Each `## <title>` heading carries a `<!-- id: ilk-xxxxxx -->` marker and a field
block (parallel to a `def-` vocabulary entry / a `claim-quality.md` `### Quality`
block, so refresh can parse it):

- **mechanism** — the constraint statement (the named substrate relation).
- **real-or-fitted** — `real-geometric-constraint` (chord — removes a DOF) | `fitted-identification` (echo — removes none).
- **status** — `SOLID` (mechanism + classification adjudicated, cite confirms) | `proposed` (gated on review) | `retired` (superseded, preserved per Rule 12).
- **interlocks** — the interlocked constant `clm-` ids (the joint-constraint's endpoints; each emits one `interlocks` edge to THIS mechanism hub). Omit / `(none — catalogued)` for a catalogued-but-unwired mechanism.
- **derived-endpoint** — the constant made DEPENDENT iff `real-geometric-constraint` (the DOF a chord removes; must be one of the interlocked endpoints). `(none)` when not applicable (fitted, or unwired).
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
