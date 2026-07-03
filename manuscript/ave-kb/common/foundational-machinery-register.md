[↑ Common (Cross-Volume Resources) Index](index.md)

<!-- kb-frontmatter
kind: leaf
no-claim: "Canonical FOUNDATIONAL-MACHINERY register — a status / provenance / usage VIEW over the EXISTING `clm-` claim nodes that carry AVE's derived MACHINERY tier (named theorems + universal operators + kernels), the THIRD rung of the provenance ladder (axioms → machinery → calibration-inputs → applications). This leaf originates NO new node-body via frontmatter and mints NO new id: every member is an ALREADY-materialized `node_type: \"claim\"` node in claims.jsonl (a `<!-- id: clm-xxxxxx -->` entry in a `claim-quality.md` register), so a register that re-declared them would be a parallel scheme, forbidden by INVARIANT-S11 (extend, don't reinvent). It is the machinery-tier analog of the axiom-register (a VIEW over the four `axiom-N` framework nodes) and the interlock-register's per-constant Calibration-Constant Criteria Register (a VIEW over the `ilk-` nodes): a bolded-field VIEW that POINTS AT existing nodes (via their `clm-` id) and READS their recorded status/solidity/provenance/citation_count — NOT a source of new claims and NOT a rescoring. Hence no-claim."
path-stable: "the canonical foundational-machinery register leaf; makes AVE's derived-machinery tier (theorems + operators + kernels) first-class as a status/provenance/usage view over the member clm- claim nodes"
-->

<!-- foundational-machinery-meta
foundational-machinery: clm-gdd70j clm-sysqaf clm-6mvtsf clm-1eg13f clm-rtdmsn clm-6t3p6x clm-ka5zdx clm-law1ho clm-ofys5v clm-gz7ryg
expected-machinery-count: 10
expected-derived-count: 7
expected-definitional-count: 3
-->

# Foundational-Machinery Register — Derived Theorems / Operators / Kernels (status / provenance / usage view)

The **source-of-truth index** for AVE's **derived MACHINERY** — the named
theorems, universal operators, and kernels that vol1 / vol2 / vol3 (and the
engine) build on. This is the **third rung of the provenance ladder**:

> **axioms** (`axiom-register.md`) → **machinery** (THIS register) →
> **calibration-inputs** {m_e, α, G} (`interlock-register.md`) →
> **applications** (the scale-instance `clm-`s).

Rungs 1, 2, and 4-inputs already have first-class tracking; the derived-machinery
tier was tracked only as scattered `clm-` claims, informally "near-foundational
machinery" ([`session/kb-improvements.md`](../session/kb-improvements.md): "the
universal operators (Op14 `clm-1eg13f`), Theorem 3.1′ (`clm-rtdmsn`), and the
parametric-coupling kernel (`clm-6t3p6x`) are near-foundational machinery that
vol1/vol2/vol3 build on"). This register consolidates the status view.

## Sections

- **§0 — Register discipline (VIEW, not new-id-scheme).**
- **§1 — Membership set (the load-bearing call — surface for Grant).**
- **§2 — Per-entry view fields (READ from existing claim records).**
- **§3 — Operators (the universal-operator machinery).**
- **§4 — Theorems (the named-theorem machinery).**
- **§5 — Kernels (the kernel machinery).**
- **§6 — Summary roll-up + the DERIVED-vs-DEFINITIONAL audit count.**
- **§7 — Companion registers + the vol3→vol4 mis-volume artifact this homes.**
- **§8 — Schema / gate note (flagged, NOT built this pass) + design decisions to ratify.**

## §0 — Register discipline (VIEW, not new-id-scheme)

> **This is a VIEW, not a new node scheme (INVARIANT-S11 — extend, don't
> reinvent).** Every member of this register is an **ALREADY first-class claim
> node**: `refresh-kb-metadata` materializes one `node_type: "claim"` record per
> `<!-- id: clm-xxxxxx -->` entry across the `claim-quality.md` registers into
> [`.index/claims.jsonl`](../.index/claims.jsonl). This register does **not**
> re-declare those nodes and mints **no** new id — that would be the
> shadow-scheme rot INVARIANT-S11 exists to stop. It is a bolded-field register
> that **POINTS AT** the existing machinery `clm-` nodes (by id) and **READS**
> their recorded fields (title / solidity / build_band / depends-on /
> citation_count) — it never recomputes or rescores anything. It is the direct
> machinery-tier analog of the `axiom-register.md` (a VIEW over the four
> `axiom-N` framework nodes — the forthcoming companion register on branch
> `analysis/axiom-register`; cross-linked as a live link when it merges, kept as
> a backtick reference here so this leaf's link-integrity gate does not depend on
> an unmerged sibling) and the interlock-register's
> [Calibration-Constant Criteria Register](interlock-register.md) (a VIEW over
> the `ilk-` nodes that mints no `ilk-` id and touches no count machinery).

> **Node-count invariance (zero new IDs).** Because every member is an existing
> `clm-` node and this leaf carries `no-claim` (no `claims:` / `exp-id:` /
> `sup-id:` frontmatter), materializing this leaf adds **zero** nodes to
> `claims.jsonl`. The `foundational-machinery:` meta line is a machine-readable
> list of member ids (the analog of the interlock-register's
> `calibration-params:` line), NOT a node declaration — parsing it emits no
> record and no edge. `make verify-kb-metadata` node count is **UNCHANGED** by
> this leaf (see §8 for the gate note; the count-invariance is confirmed in the
> validation footer).

> **What "machinery" means here (the tier boundary).** A member is
> **derived MACHINERY** iff it is a reusable theorem / operator / kernel that the
> per-domain application leaves *build on* (it is a `depends-on` target of
> downstream claims and/or the engine's shared code path), as distinct from an
> **application** — a scale-instance that USES the machinery at one domain
> (galactic rotation, protein fold, BCS, a specific bench). The boundary is not
> always sharp; §1 flags every borderline machinery-vs-application inclusion for
> Grant rather than silently deciding it.

## §1 — Membership set (the load-bearing call — surface for Grant)

> **This is the load-bearing decision — surfaced for Grant to RATIFY, not
> silently frozen.** The membership set is 10 `clm-` nodes (the
> `foundational-machinery:` meta line). Below: the enumeration, its provenance
> grep, and every borderline machinery-vs-application call flagged (per §0's tier
> boundary — I did NOT silently decide the borderline ones).

**The three brief-named seeds (verified present, canonical entries):**

| `clm-` | machinery | canonical entry |
|---|---|---|
| `clm-1eg13f` | Op14 — Saturation Modulates Local Clock Rate | `vol4/claim-quality.md:1222` |
| `clm-rtdmsn` | Theorem 3.1′ — Electron Q-Factor from LC Tank at TIR Boundary | `vol4/claim-quality.md:1352` |
| `clm-6t3p6x` | Parametric Coupling Kernel (Axiom-4 vacuum varactor) | `vol4/claim-quality.md:1246` |

All three verified: `grep -rn "id: clm-1eg13f"` / `clm-rtdmsn` / `clm-6t3p6x`
each resolve to exactly one `<!-- id: … -->` marker in `vol4/claim-quality.md`.

**The operator-machinery core (the universal-operator basis, READ, not enumerated
per-Op):**

The universal operators Op1–Op22 are **NOT** each their own `clm-` node — the
corpus tracks them as **catalog + owner claims**, not 22 separate claim entries.
Verified by `grep -rniE "^## .*\bOp[0-9]+\b"` in the `claim-quality.md` files:
the only operator-owning claim entries are three, plus the two Op14 vol4 entries:

| `clm-` | machinery | canonical entry | what it owns |
|---|---|---|---|
| `clm-gdd70j` | Universal Operators (Z, S, Γ, …) — Same Function, Different Scales | `vol1/claim-quality.md:551` | the Op1–Op8 shared-code-path OWNER claim (the operator formulae) |
| `clm-sysqaf` | Universal Operator Catalog (Op1–Op22) — Catalog of Record | `common/claim-quality.md:946` | the Op1–Op22 catalog of record (cited by `operators.md`) |
| `clm-6mvtsf` | Op1 Universal Impedance — the Single Structural Invariant | `common/claim-quality.md:974` | the scale-invariance-inheritance thesis (Op4–22 inherit from Op1) |
| `clm-1eg13f` | Op14 — Saturation Modulates Local Clock Rate | `vol4/claim-quality.md:1222` | the Op14 local-clock-modulation mechanism |

> **DESIGN CALL (surfaced): operators are tracked as owner+catalog claims, not
> 22 per-Op nodes.** The brief said "the universal operators Op1–Op21 → their
> `clm-`s (enumerate from `operators.md` … e.g. Op14=`clm-1eg13f`)." The corpus
> reality (grep-verified) is that `operators.md` frontmatter declares exactly
> THREE `clm-`s — `clm-sysqaf` (catalog), `clm-6mvtsf` (Op1 invariant thesis),
> `clm-gdd70j` (Op1 impedance formula, owned in vol1) — and Op14 additionally
> has two vol4 mechanism claims (`clm-1eg13f` local-clock, `clm-p2tp9i`
> cross-sector-trading). There is **no per-Op claim node** for Op2, Op3, Op5–13,
> Op15–22. So the operator machinery is represented by its **owner + catalog +
> Op1-invariant + Op14-mechanism** nodes, which IS the reusable-machinery layer
> the applications build on. **FLAG for Grant:** two Op14-specific vol4 entries
> exist — `clm-1eg13f` (local-clock, the brief seed, INCLUDED) and `clm-p2tp9i`
> (cross-sector-trading ρ=−0.990, `vol4/claim-quality.md:1194`). `clm-p2tp9i` is
> an **empirical engine-MEASUREMENT of an Op14 consequence** (a simulation
> result, not the operator definition), so it reads as an application-of-Op14,
> NOT operator machinery — **EXCLUDED, flagged**. Op1's owner is split across two
> nodes (`clm-gdd70j` the formula in vol1, `clm-6mvtsf` the invariant thesis in
> common); both are included as they are distinct machinery facets.

> **NUMBERING FLAG (Grant): "Op1–Op21" vs the catalog's "Op1–Op22".** The brief
> said Op1–Op21; the canonical catalog `operators.md:9` + `clm-sysqaf` title both
> say **Op1–Op22** (Op22 = Avalanche Factor $M=1/S^2$). This register defers to
> the canonical catalog (Op1–**Op22**). Not a membership change (no per-Op nodes
> exist either way) — surfaced so the "21" in the brief is not silently adopted
> over the corpus's "22".

**The named-theorem machinery (grep `^## .*Theorem` in `claim-quality.md`):**

| `clm-` | theorem | canonical entry | machinery vs application |
|---|---|---|---|
| `clm-rtdmsn` | Theorem 3.1′ — Electron Q-Factor at TIR Boundary | `vol4/claim-quality.md:1352` | MACHINERY (brief seed) — but VALUE-scoped echo (see §4) |
| `clm-ka5zdx` | Mass-Closure Theorem: $mc^2 = E_{\text{reactive}}$ | `vol2/claim-quality.md:1231` | MACHINERY — reusable mass↔reactive-energy identity |
| `clm-ofys5v` | Substrate-Observability Rule (Universal No-Hair Theorem) | `common/claim-quality.md:624` | MACHINERY — universal $\Gamma=-1$ boundary-observability rule |
| `clm-law1ho` | AVE BH Horizon $r_{\text{sat}}=7GM/c^2$ + Area Theorem | `vol3/claim-quality.md:1084` | **BORDERLINE** (see flag) |

> **BORDERLINE FLAG (Grant) — `clm-law1ho` BH Area Theorem.** Titled "…+ Area
> Theorem" (a named theorem, so it grepped in), but its body is an **AVE-specific
> BH-horizon RESULT** ($r_{\text{sat}}=7GM/c^2$) applying the machinery (it
> depends on `clm-iouqn9` the magic-angle + `clm-x19btt`, and axioms 2,4). It
> reads more as a **gravity APPLICATION that contains a theorem-shaped
> sub-result** than as reusable cross-domain machinery. **INCLUDED provisionally,
> flagged** — Grant's call whether the Area-Theorem sub-result is machinery (the
> entropy/area law is reused) or the whole entry is a vol3 application. Recommend:
> if kept, it is machinery only in its Area-Theorem facet, not the $7GM/c^2$
> horizon-radius facet.

**The kernel machinery (grep `[Kk]ernel` in `claim-quality.md`):**

| `clm-` | kernel | canonical entry | machinery vs application |
|---|---|---|---|
| `clm-6t3p6x` | Parametric Coupling Kernel (Axiom-4 vacuum varactor) | `vol4/claim-quality.md:1246` | MACHINERY (brief seed) |
| `clm-gz7ryg` | A-034 Single-Kernel Unification — one saturation kernel at all scales | `common/claim-quality.md:794` | MACHINERY — the cross-scale kernel-unification claim |

> **KERNEL-vs-Axiom-4 boundary (Grant).** The saturation kernel *shape*
> $S(A)=\sqrt{1-A^2}$ itself is **Axiom 4** — it lives on rung 1
> (`axiom-register.md`), NOT here. What IS machinery here: the **parametric
> coupling kernel** `clm-6t3p6x` (an Axiom-4-varactor apparatus kernel the DAMA/
> detector predictions build on) and the **single-kernel unification claim**
> `clm-gz7ryg` (the reusable "one kernel at all scales" thesis, dep `clm-sysqaf`).
> **EXCLUDED as applications, flagged:** the per-scale saturation-kernel INSTANCES
> — protein fold (`vol5`, A-034), Schwinger pair (`vol2` Q-G18), Big Bang
> (`common` A-034 cosmic), the A4 constitutive gate (`vol9`) — these USE the
> kernel at one domain, they are not the kernel machinery. The
> `universal-saturation-kernel-catalog.md` (26 instances) is the application
> catalog; `clm-gz7ryg` is its machinery-tier unification claim.

**Deliberately NOT included (application tier, per §0 boundary — flagged so the
exclusion is auditable, not silent):**

- `clm-p2tp9i` — Op14 cross-sector-trading ρ=−0.990 (empirical engine
  measurement of an Op14 consequence — an application/measurement, not the
  operator).
- The saturation-kernel scale-instances (protein / Schwinger / Big Bang / BCS /
  galactic) — applications of Axiom-4's kernel at one domain each.
- `clm-4r4jiy` (Q-G22 strain convention), `clm-fgo20a` (Q-G24 Newtonian limit),
  `clm-n3un96` (τ_relax) — these are Op14/Axiom-4 **usage/derivation results**
  physically co-located in `vol4/claim-quality.md`, not reusable operator/theorem/
  kernel machinery. (Flagged because they sit adjacent to the seeds in the same
  register and could be mis-swept in.)

## §2 — Per-entry view fields (READ from existing claim records)

Each `### <machinery name>` entry in §3–§5 carries a bolded field block. **Every
field is READ from the member's existing claim record (`claims.jsonl` /
`depends-on.jsonl` / its `claim-quality.md` entry) — none is recomputed or
rescored here.** The fields:

- **clm-id** — the existing `clm-` node this entry is a view over (the grep
  anchor: `grep -rn "id: clm-…"` reaches the canonical entry; `grep -rn "clm-…"`
  reaches every citing leaf). Never a new id.
- **title** — the member claim's `## ` heading title, verbatim from its record.
- **status** ∈ {**DERIVED**, **DEFINITIONAL**} — the machinery-tier provenance
  axis (the analog of the axiom-register's status axis, but two-valued for the
  machinery tier):
  - **DERIVED** = proven-from-axioms: the member's `depends-on` cone bottoms out
    in one or more `axiom-N` framework nodes (± intermediate `clm-`s), i.e. it is
    a *theorem of* the axioms, not a fresh posit.
  - **DEFINITIONAL** = posited: the member is a definition / catalog / naming /
    identification that INTRODUCES structure rather than deriving it from the
    axioms (its content is a chosen convention or an organizing catalog, not a
    proof). This is the FORM-derives / VALUE-imports meta-finding at the
    machinery tier: a DEFINITIONAL member is a machinery *posit*, a DERIVED
    member is a machinery *theorem*.
  > **status ≠ solidity, and DERIVED ≠ "value-forced".** `status` records
  > *provenance* (theorem-of-axioms vs posit), a separate axis from `solidity`
  > (how solid the derivation/measurement is) and from the chord/echo VALUE axis
  > (`interlock-register.md`). A member can be DERIVED (a genuine theorem of the
  > axioms) and still be a **VALUE-level echo** — Theorem 3.1′ (`clm-rtdmsn`) is
  > the canonical case: DERIVED in FORM (α⁻¹ = Q-factor is a theorem of Ax 1/2/3)
  > yet VALUE-scoped as a Class-B echo (the exact 137 rests on R·r=¼, which the
  > substrate does not independently select; see §4). The two axes are
  > orthogonal and this register keeps them so.
- **axiom-provenance** — the `axiom-N` ids in the member's `depends-on` cone
  (READ from `depends-on.jsonl` `target_kind == "axiom"`), cross-referenced to
  `axiom-register.md`. `(none direct — via clm-deps)` when the member reaches the
  axioms only transitively through claim dependencies.
- **solidity** — the member's recorded `solidity` + `build_band` (READ from
  `claims.jsonl`; NOT recomputed). The number is the corpus's, restated.
- **usage** — the member's `citation_count` (READ from `claims.jsonl`; = the
  number of leaves citing it in `cites.jsonl`). The machinery-tier "how much does
  vol1/vol2/vol3 build on this" signal — high citation_count = load-bearing
  machinery.
- **flags** — any borderline / mis-volume / value-echo caveat, cross-referenced
  to the §1 flag.

> **All §3–§5 numbers are as-of the branch base (`origin/main` @ f556dcdc).**
> This register READS them; if a member's solidity or citation_count changes in a
> later refresh, this VIEW is regenerated to match (it is never the source of
> truth for those numbers — the claim record is).

## §3 — Operators (the universal-operator machinery)

The universal-operator basis (Op1–Op22 per `operators.md` / `clm-sysqaf`),
represented by its owner + catalog + Op1-invariant + Op14-mechanism claim nodes
(§1 explains why there is no per-Op node). All fields READ from records.

### Op1–Op8 Universal Operators (Z, S, Γ, …) — Same Function, Different Scales
<!-- view of claim node: clm-gdd70j -->

- **clm-id:** `clm-gdd70j` ([`vol1/claim-quality.md:551`](../vol1/claim-quality.md)).
- **title:** "Universal Operators (Z, S, Γ) — Same Function, Different Scales" — the Op1–Op8 shared-code-path owner claim (Z impedance, S saturation, Γ reflection, U pairwise, Y→S multiport, λ_min eigenvalue-target, FFT spectral, Γ_pack packing).
- **status:** **DERIVED** — a theorem of Axiom 4 (the S / impedance / reflection algebra is built on the saturation kernel; its `depends-on` is `Axiom 4`).
- **axiom-provenance:** `axiom-4` (direct, READ from `depends-on`).
- **solidity:** 0.80, `ok-with-caveats` (READ). Caveat: operator-identity is *structural* (same code path), not per-scale predictive.
- **usage:** `citation_count = 9` — the **most-cited machinery member**; the operator basis vol1–vol5 leaves build on. Load-bearing.
- **flags:** Op1's owner is split — this node owns the Op1–Op8 *formulae*; `clm-6mvtsf` (below) owns the Op1 *invariant-inheritance thesis*. Both included as distinct facets (§1).

### Op1–Op22 Universal Operator Catalog — Catalog of Record
<!-- view of claim node: clm-sysqaf -->

- **clm-id:** `clm-sysqaf` ([`common/claim-quality.md:946`](claim-quality.md)).
- **title:** "Universal Operator Catalog (Op1–Op22) — Catalog of Record" — the single-source-of-truth catalog cited by `operators.md`.
- **status:** **DEFINITIONAL** — a CATALOG / naming register (it *names + tags* the 22 operators CANONICAL/SYNTHESIS; it does not derive them). Its `depends-on` is `clm-gdd70j` (the one formula it restates), reaching no axiom of its own. Machinery *posit*, not theorem.
- **axiom-provenance:** `(none direct — via clm-gdd70j → axiom-4)`.
- **solidity:** 0.80, `ok-with-caveats` (READ).
- **usage:** `citation_count = 1`.
- **flags:** the "Op1–**Op22**" span (canonical) vs the brief's "Op1–Op21" numbering flag lives here (§1). SYNTHESIS-labelled Op15/18/20 + A43 v10/v11 corrections are internal to this catalog, not membership.

### Op1 Universal Impedance — the Single Structural Invariant
<!-- view of claim node: clm-6mvtsf -->

- **clm-id:** `clm-6mvtsf` ([`common/claim-quality.md:974`](claim-quality.md)).
- **title:** "Op1 Universal Impedance — the Single Structural Invariant" — the scale-invariance-inheritance thesis (Op4–Op22 inherit invariance from Op1's $Z=\sqrt{\mu/\varepsilon}$).
- **status:** **DERIVED** — the inheritance thesis is a (structural) theorem over the operator basis; deps `clm-gdd70j` + `clm-sysqaf` reach `axiom-4` transitively. (Its own rationale concedes the per-operator inheritance is asserted-by-construction, which lowers its *solidity*, not its provenance class.)
- **axiom-provenance:** `(none direct — via clm-gdd70j → axiom-4)`.
- **solidity:** 0.60, `input-only` (READ) — the softest operator member; the "all Op4–22 inherit" step is structural, not per-operator-proven.
- **usage:** `citation_count = 1`.
- **flags:** none beyond the Op1-owner-split noted on `clm-gdd70j`.

### Op14 — Saturation Modulates Local Clock Rate
<!-- view of claim node: clm-1eg13f -->

- **clm-id:** `clm-1eg13f` ([`vol4/claim-quality.md:1222`](../vol4/claim-quality.md)) — a **brief-named seed**.
- **title:** "Op14 Saturation Modulates Local Clock Rate" — Op14's $Z_{eff}(r)=Z_0/\sqrt{S(r)}$ modulates the local clock rate $\omega_{local}=\omega_{global}\sqrt{1-A^2(r)}$ (the substrate-native time-dilation mechanism; parallels gravitational $n(r)=1/\sqrt S$).
- **status:** **DERIVED** — a clean theorem of Axiom 4 ($\omega_{local}$ follows from $c_{eff}=c_0\sqrt S$; `depends-on` is `Axiom 4`).
- **axiom-provenance:** `axiom-4` (direct, READ).
- **solidity:** 0.80, `ok-with-caveats` (READ) — pinned just below 0.9 because the $c_{eff}=c_0\sqrt S$ step is asserted from the kernel rather than re-derived in-leaf.
- **usage:** `citation_count = 1`.
- **flags:** **vol3→vol4 mis-volume artifact** (§7) — this Op14 machinery lives in vol4/ though it is cross-volume operator machinery vol1/vol3 build on. The sibling Op14 entry `clm-p2tp9i` (cross-sector-trading ρ=−0.990, engine MEASUREMENT) is EXCLUDED as an application (§1).

## §4 — Theorems (the named-theorem machinery)

The named theorems (grep `^## .*Theorem` in the `claim-quality.md` registers).
All fields READ from records.

### Theorem 3.1′ — Electron Q-Factor from LC Tank at TIR Boundary
<!-- view of claim node: clm-rtdmsn -->

- **clm-id:** `clm-rtdmsn` ([`vol4/claim-quality.md:1352`](../vol4/claim-quality.md)) — a **brief-named seed**.
- **title:** "Theorem 3.1′ — Electron Q-Factor from LC Tank at TIR Boundary" — $\alpha^{-1}=Q_{tank}=Q_{vol}+Q_{surf}+Q_{line}=4\pi^3+\pi^2+\pi=137.036$; two independent paths (LC-tank + multipole) agree to $\delta_{strain}=2.225\times10^{-6}$.
- **status:** **DERIVED (in FORM) / VALUE-ECHO.** DERIVED: the Q-factor decomposition is a theorem of Ax 1/2/3 (`depends-on` = `axiom-1, axiom-2, axiom-3`). **But VALUE-scoped:** the entry itself carries a 🔴 (2026-06-15 keystone α-verdict) — this is the Q-factor *reframe* of α⁻¹, a **Class-B named geometric identification** whose *scale* (~1/137) is forced but whose *exact value* rests on R·r=¼, which the substrate does not independently select (both lift-routes closed). Cross-ref the `interlock-register.md` `ilk-rr14gt` echo tag.
- **axiom-provenance:** `axiom-1, axiom-2, axiom-3` (direct, READ).
- **solidity:** 0.85, `ok-to-build` (READ) — the **highest-solidity machinery member**; two-path-agreeing closed derivation (form). (Solidity is on the FORM; it does not certify the value as forced — that is the orthogonal echo axis.)
- **usage:** `citation_count = 1`.
- **flags:** the DERIVED-form / VALUE-echo split is the canonical demonstration that `status` (§2) is orthogonal to the chord/echo VALUE axis. **vol3→vol4 mis-volume** (§7). Do NOT headline this as a value-derivation of 137 (α is a *retained input*, per the entry's 🔴).

### Mass-Closure Theorem: $mc^2 = E_{\text{reactive}}$
<!-- view of claim node: clm-ka5zdx -->

- **clm-id:** `clm-ka5zdx` ([`vol2/claim-quality.md:1231`](../vol2/claim-quality.md)).
- **title:** "Mass-Closure Theorem: $mc^2 = E_{\text{reactive}}$" — mass as stored reactive (LC-tank) energy.
- **status:** **DERIVED** — a theorem of ALL FOUR axioms (`depends-on` = `axiom-1, axiom-2, axiom-3, axiom-4`; the only member reaching all four directly).
- **axiom-provenance:** `axiom-1, axiom-2, axiom-3, axiom-4` (direct, READ).
- **solidity:** 0.50, `input-only` (READ) — the softest theorem member.
- **usage:** `citation_count = 1`.
- **flags:** included as machinery (a reusable mass↔reactive-energy identity the electron/soliton leaves build on); a Grant call whether its low solidity + single citation argue for application-tier instead — surfaced, not decided.

### The Substrate-Observability Rule (Universal No-Hair Theorem)
<!-- view of claim node: clm-ofys5v -->

- **clm-id:** `clm-ofys5v` ([`common/claim-quality.md:624`](claim-quality.md)).
- **title:** "The Substrate-Observability Rule (Universal No-Hair Theorem)" — a $\Gamma=-1$ boundary totally traps the interior; only M, Q, J are externally measurable, at every scale (electron → nucleus → planetary magnetopause → BH → cosmic horizon).
- **status:** **DEFINITIONAL** — the entry's OWN rationale: "**Internally coherent as a definitional rule; the trapping mechanism is asserted, not derived**." It POSITS a universal observability constraint (no `axiom-N` or `clm-` dependency at all). A machinery posit, not a theorem.
- **axiom-provenance:** `(none — no depends-on edges; a standalone posited rule)`.
- **solidity:** 0.55, `input-only` (READ) — the trapping step (|Γ|²→1) is asserted from the Axiom-4 kernel, not shown.
- **usage:** `citation_count = 1`.
- **flags:** "No-Hair *Theorem*" in the title but the corpus classes it a *rule/posit* — a naming-vs-provenance mismatch surfaced for Grant. DEFINITIONAL per the corpus's own honest self-statement, not a downgrade by this register.

### AVE BH Horizon: $r_{\text{sat}}=7GM/c^2$ + Area Theorem
<!-- view of claim node: clm-law1ho -->

- **clm-id:** `clm-law1ho` ([`vol3/claim-quality.md:1084`](../vol3/claim-quality.md)).
- **title:** "AVE BH Horizon: $r_{\text{sat}}=7GM/c^2$ + Area Theorem".
- **status:** **DERIVED** — deps `axiom-2, axiom-4` + `clm-iouqn9` (magic-angle) + `clm-x19btt` (compactness limit).
- **axiom-provenance:** `axiom-2, axiom-4` (direct, READ) + transitively via `clm-iouqn9`.
- **solidity:** 0.55, `input-only` (READ; confidence 0.90 but gated down to 0.55 by its `clm-iouqn9` dep at 0.55).
- **usage:** `citation_count = 1`.
- **flags:** **BORDERLINE machinery-vs-application (§1).** The "+ Area Theorem" facet is reusable machinery; the $r_{\text{sat}}=7GM/c^2$ horizon-radius facet is a vol3 gravity APPLICATION. Included provisionally; Grant's call whether to keep (as an Area-Theorem-only member) or move to application tier. The single strongest exclusion candidate in the set.

## §5 — Kernels (the kernel machinery)

The kernels (grep `[Kk]ernel` in the `claim-quality.md` registers). **The
saturation-kernel SHAPE $S(A)=\sqrt{1-A^2}$ itself is Axiom 4 — rung 1, NOT here
(§1 kernel-vs-Axiom-4 boundary).** These two members are the *derived* /
*organizing* kernel machinery built ON Axiom 4. All fields READ from records.

### Parametric Coupling Kernel (Axiom-4 Vacuum Varactor at Sub-Yield α-Slew Operating Point)
<!-- view of claim node: clm-6t3p6x -->

- **clm-id:** `clm-6t3p6x` ([`vol4/claim-quality.md:1246`](../vol4/claim-quality.md)) — a **brief-named seed**.
- **title:** "Parametric Coupling Kernel (Axiom 4 Vacuum Varactor at Sub-Yield α-Slew Operating Point)" — the $\varepsilon_{det}=4\pi\kappa_{quality}/N^2$ apparatus kernel ($C_{eff}(V)=C_0/\sqrt{1-(V/V_{yield})^2}$ varactor + α-slew refresh) the DAMA / detector-network predictions build on.
- **status:** **DERIVED** — a theorem of Axiom 4 (the vacuum-varactor $C_{eff}(V)$) plus Theorem 3.1′; `depends-on` = `axiom-4, clm-rtdmsn, clm-vjv4zf`.
- **axiom-provenance:** `axiom-4` (direct, READ) + Theorem 3.1′ (`clm-rtdmsn`, the $Z_{radiation}=Z_0/4\pi$ inheritance) + `clm-vjv4zf` (constitutive $C_{eff}(V)$ form).
- **solidity:** 0.60, `input-only` (READ) — closes to leading order; the entry is candid that $\kappa_{quality}$ per detector + per-defect detuning are load-bearing-open.
- **usage:** `citation_count = 1`.
- **flags:** **vol3→vol4 mis-volume** (§7). REACTIVE-power class; the entry explicitly disclaims being the real-power κ_entrain Sagnac mechanism (a co-located but distinct kernel — not double-counted here).

### A-034 Single-Kernel Unification — One Saturation Kernel at All Scales
<!-- view of claim node: clm-gz7ryg -->

- **clm-id:** `clm-gz7ryg` ([`common/claim-quality.md:794`](claim-quality.md)).
- **title:** "A-034 Single-Kernel Unification — One Saturation Kernel at All Scales" — the reusable "same dimensionless $S(A)=\sqrt{1-A^2}$ at every scale, inherited from Axiom 4 not re-postulated per scale" thesis (the machinery-tier claim over the 26-instance A-034 catalog).
- **status:** **DEFINITIONAL** — the entry's OWN caveat: "**Does NOT derive Axiom 4 itself; the kernel is the postulated Axiom 4 form. This entry asserts its single-kernel cross-scale applicability, not its first-principles origin.**" It POSITS cross-scale applicability (via TKI); its `depends-on` is `clm-sysqaf` (the catalog), reaching no axiom of its own. A machinery *organizing posit*, not a theorem.
- **axiom-provenance:** `(none direct — asserts inheritance from axiom-4 via TKI/axiom-2, but its recorded depends-on is clm-sysqaf only)`.
- **solidity:** 0.62, `input-only` (READ).
- **usage:** `citation_count = 1`.
- **flags:** the SHAPE it unifies is Axiom 4 (rung 1); this member is the *unification claim*, not the kernel. The per-scale INSTANCES (protein / Schwinger / Big Bang / BCS / `clm-dxdsvt` 26-catalog) are EXCLUDED as applications (§1).

## §6 — Summary roll-up + the DERIVED-vs-DEFINITIONAL audit count

<!-- filled in a later commit -->

## §7 — Companion registers + the vol3→vol4 mis-volume artifact

<!-- filled in a later commit -->

## §8 — Schema / gate note (flagged, NOT built this pass) + design decisions to ratify

<!-- filled in a later commit -->
