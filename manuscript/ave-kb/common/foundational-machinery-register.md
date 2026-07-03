[↑ Common (Cross-Volume Resources) Index](index.md)

<!-- kb-frontmatter
kind: leaf
no-claim: "Canonical FOUNDATIONAL-MACHINERY register — a status / provenance / usage VIEW over the EXISTING `clm-` claim nodes that carry AVE's derived MACHINERY tier (named theorems + universal operators + kernels), the THIRD rung of the provenance ladder (axioms → machinery → calibration-inputs → applications). This leaf originates NO new node-body via frontmatter and mints NO new id: every member is an ALREADY-materialized `node_type: \"claim\"` node in claims.jsonl (a `<!-- id: clm-xxxxxx -->` entry in a `claim-quality.md` register), so a register that re-declared them would be a parallel scheme, forbidden by INVARIANT-S11 (extend, don't reinvent). It is the machinery-tier analog of the axiom-register (a VIEW over the four `axiom-N` framework nodes) and the interlock-register's per-constant Calibration-Constant Criteria Register (a VIEW over the `ilk-` nodes): a bolded-field VIEW that POINTS AT existing nodes (via their `clm-` id) and READS their recorded status/solidity/provenance/citation_count — NOT a source of new claims and NOT a rescoring. Hence no-claim."
path-stable: "the canonical foundational-machinery register leaf; makes AVE's derived-machinery tier (theorems + operators + kernels) first-class as a status/provenance/usage view over the member clm- claim nodes"
-->

<!-- foundational-machinery-meta
foundational-machinery: clm-gdd70j clm-sysqaf clm-6mvtsf clm-1eg13f clm-rtdmsn clm-6t3p6x clm-ka5zdx clm-law1ho clm-ofys5v clm-gz7ryg
expected-machinery-count: 10
expected-derived-count: 8
expected-definitional-count: 2
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

<!-- filled in a later commit -->

## §4 — Theorems (the named-theorem machinery)

<!-- filled in a later commit -->

## §5 — Kernels (the kernel machinery)

<!-- filled in a later commit -->

## §6 — Summary roll-up + the DERIVED-vs-DEFINITIONAL audit count

<!-- filled in a later commit -->

## §7 — Companion registers + the vol3→vol4 mis-volume artifact

<!-- filled in a later commit -->

## §8 — Schema / gate note (flagged, NOT built this pass) + design decisions to ratify

<!-- filled in a later commit -->
