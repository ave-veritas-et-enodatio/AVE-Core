# FIELD-DEF LANE PART 2 — INTERLOCK STRUCTURE (calibration-parameter backbone) — SCHEMA-SPINE EXTENSION (Path A)

You are the implementer for Part 2 of the Field-def lane. This is a SEPARATE deliverable/PR from the electron pilot (Part 1) — do NOT co-mingle. This brief is self-contained and adjudicated; corrections in it are verified by grep and override any contrary corpus prose. **Nothing merges, pushes, or promotes to SOLID. Stage, run verify, STOP. The auditor verifies the schema DESIGN + the alpha population before merge.** INVARIANT-S11 governs: this is a DELIBERATE `.index/SCHEMA.md` spine edit.

FIRST ACTION: write this brief verbatim to `_orchestration/2026-06-14_interlock-schema-spine.md` on your branch as commit 1.

## 0. Worktree & branch (drift-robust — origin is actively moving; do NOT trust a pinned SHA)
- `git -C /Users/grantlindblom/AVE-staging/AVE-Core fetch origin`
- Base off CURRENT `origin/main` (it has moved twice this session; latest seen = `1c0afab7`, but verify live). Create a SEPARATE worktree from Part 1: `git -C /Users/grantlindblom/AVE-staging/AVE-Core worktree add -b analysis/2026-06-14-interlock-schema-spine /Users/grantlindblom/AVE-staging/AVE-Core-interlock-wt origin/main`
- **SURFACE-VERIFY (not SHA-pin), then STOP if drifted:** confirm the Part-2 surfaces match this brief before building — `SCHEMA.md` edge-class section at ~:191-226 (3 directional relations depends/strengthens/supports; record shape with `relation:` union at ~:203); `depends-on.jsonl` 8-key records (`source,target,relation,target_kind,target_solidity_recorded,strength,context,fraction`), ~700 edges, 1-directional; and the cited anchors in §3. If any Part-2 surface differs materially from this description, STOP and report.
- Never touch the main checkout or the Part-1 worktree (`AVE-Core-fielddef-wt`). `main` protected. Incremental commits (skeleton-first, one section per commit).

## 1. Mission
The interlock (mutual-constraint) is NOT first-class in the corpus — it exists only as prose. ~2/3 of the backbone already exists: inputs ARE tagged (`claims.jsonl build_band:"input-only"`, 143 claims incl. α/G/Ω_freeze/δ_strain); a directional derivation DAG exists (`depends-on.jsonl`, ~700 1-directional `depends` edges + free-text `context`); the param-count is stated in prose (`clm-5xon03`, solidity 0.65). **Do NOT rebuild the DAG — extend it.** Make the INTERLOCK first-class and machine-enforced.

## 2. NAMING (run ave-representation-capability-check before minting ANY token)
- **Relation token = `interlocks`** — VERIFIED collision-free (0 hits repo-wide) and aligned with the KB's own "Interlocked Inputs" prose. Use this.
- **Do NOT use `joint-constraint`** (102 hits — the established "Class E joint-constraint" prose term; semantic collision) and **do NOT use `brace`** (it denotes the MECHANICAL Cosserat over-bracing σ^A — trampoline-analogy-primer.md:155/359/465). "brace" may appear as a descriptive English word only, NEVER as a minted identifier/token/node_type.
- **Mechanism node_type:** mint your OWN node_type (NOT `def-` — Part 1 is editing `vocabulary-register.md`; a new node_type keeps you off that file and avoids a merge collision). Pick a collision-free id-prefix following the `\b<prefix>-[a-z0-9]{6}\b` convention (e.g. `ilk-`; verify 0 prior hits before minting). Run ave-representation-capability-check on the prefix + node-type name.

## 3. BUILD (extend .index/SCHEMA.md + the pipeline tools)
Extension points (verified at base):
- New node_type → add a record subsection near `SCHEMA.md:123`(Definition)/`:152`(Framework), update the six-type enumeration at `SCHEMA.md:5/:25/:56`, slot into the `(node_type,id)` ASCII sort at `:171`.
- New relation → extend the 3-edge-class enumeration at `SCHEMA.md:195-197`, the `relation:` union at `:203`, referential-integrity at `:43`, edge-class table row at `:26`; materialize rows in `depends-on.jsonl` (8-key shape).

**(1) First-class SYMMETRIC `interlocks` relation** — distinct from 1-directional `depends`. Decide + document the symmetric encoding (two mirrored directed rows per pair, OR a documented symmetric-sort convention) since the loader currently assumes directed edges. Each interlock edge carries: the two constants (endpoints) + the mechanism-node id + a `real_or_fitted` tag (`real-geometric-constraint | fitted-identification`). Extend `verify-kb-metadata` to validate the new relation's referential integrity (endpoints resolve, mechanism-node resolves, tag present).

**(2) Mechanism NODES** (your new node_type): one per joint-constraint mechanism — R·r=1/4 (Golden-Torus screening), R−r=1/2 (crossings), the Compton-trapping condition (the d=1 Nyquist cell-trap + ℓ_node=electron-Compton identification; prose-named, not a single equation). Each greppable, each tagged `{real-geometric-constraint | fitted-identification}`, each citing its existing corpus leaf: R·r=1/4 + R−r=1/2 + d=1 at `ch8-alpha-golden-torus.md:44-46`; Compton-trapping at `ch8:11` + `ch0-intro.md:21`. **This is where chord/echo gets ENFORCED per-mechanism, not narrated.**

**(3) LIVE independent-parameter COUNT** — a `verify-kb-metadata`-checked DERIVED number replacing the prose-at-0.65. **Precise semantics (load-bearing):** independent-count = (input-only nodes) − (nodes made dependent by a `REAL`-tagged interlock). A `FITTED` interlock does NOT reduce the count (an echo buys no parameter reduction; only a chord does). CI-check the derived count against an asserted expected value so a tag flip (fitted→real or real→fitted) visibly moves the count.

**(4) FALSIFICATION-NET as machine structure** — encode `omega-freeze-cosmic-grain-cascade.md:11` ("substrate has ONE DOF u₀*; the N observables project onto N joint-constrained channels; falsification of any one kills the operating-point and the entire model"). Operating-point ROOT node = **`clm-iouqn9`** (K4 Magic-Angle, u₀*≈0.187 — the single DOF); the net statement is hosted on **`clm-dsb560`** (single-Ω_freeze three-route projection). Wire `verify-kb-metadata` so that marking ANY interlocked channel `refuted` propagates a visible failure/flag to `clm-iouqn9` (the operating-point) — the model's strongest claim becomes CI-enforced. If the wiring reveals the root should be `clm-dsb560` rather than `clm-iouqn9`, STOP and surface it (don't decide).

## 4. POPULATE INSTANCE-1 (alpha) — HONEST current status, do NOT over-claim
Chain: input = **Ω_freeze** (measured IC, `clm-dsb560`/`clm-a7cbqq`, input-only) → u₀* (`clm-iouqn9`) → **[interlock-mechanism: R·r=1/4, tag = `fitted-identification`]** → α (`clm-0ktpcn`, input-only). Tag R·r=1/4 **FITTED** — `ch8-alpha-golden-torus.md:11` states it is "a named identification the substrate does NOT independently select." Do NOT pretend it's real. (The keystone lane separately assesses whether R·r=1/4 can move fitted→real via the menu/CRN test — NOT your call; you build + populate the CURRENT tag.) Because the brace is FITTED, the live count (item 3) must NOT drop for alpha.

## 5. Corrections to the original spec (verified by grep — apply)
- **clm-5xon03 reduces 26 SM params to `{m_e, α, G}` + 4 axioms** (NOT `{ℓ_node, α, G}`; m_e↔ℓ_node via m_e=ℏ/(c·ℓ_node) — note the conversion if you use ℓ_node). It is hosted at `vol1/claim-quality.md` (heading :42, id :43), solidity 0.65, build_band `ok-with-caveats` (NOT input-only).
- **The "all from a single Ω_freeze" framing is `clm-dsb560`, NOT clm-5xon03.** Cite clm-dsb560 for the single-Ω_freeze projection.
- **G has NO dedicated input-only node** — it appears only as a member of clm-5xon03's `{m_e,α,G}` set; its closure (`G=c⁴/(7ξT_EM(u₀*))`) is disclosed-OPEN (`clm-fgo20a` ok-with-caveats, `clm-jwyy6l` do-not-build). When you wire the G channel (if at all in instance-1 scaffolding), it cannot cite a clean input-only G node — represent it honestly or leave the G channel as a declared-but-unpopulated slot. Do NOT invent a G input node.
- **`a0c6d9f7` (the original grounding ref) does not exist** — ignore it; base off current origin/main per §0.

## 6. Skills (fire deliberately)
`ave-representation-capability-check` (naming + EVERY node/relation/prefix mint — esp. the brace/interlock/joint-constraint disambiguation); `consistency-vs-emergence` (the input/derived/interlocked classification + the real/fitted tag discipline — a fitted identification is a CONSISTENCY echo, not emergence); `ave-canonical-leaf-pull` (link mechanism nodes to existing leaves, don't re-derive); `verify-before-cite` (every line:number); plus INVARIANT-S11 (deliberate spine edit) governs throughout. Write a 60-second skill-selection plan in commit 1.

## 7. Execution & stop conditions
- Stage everything appropriately (new nodes `proposed` where status applies). Run `refresh-kb-metadata` + `make verify-kb-metadata` in-worktree; the new relation/node_type/derived-count/falsification-net checks must PASS. Run `make verify` if present.
- Do NOT merge, push, or SOLID-promote. Both PRs (Part 1 + Part 2) regenerate `claims.jsonl` → there WILL be a merge conflict on that generated file; that is the orchestrator's ordered-merge-then-regenerate problem, not yours — do not try to reconcile against Part 1.
- STOP-and-surface on any fork the brief doesn't cover: the operating-point root ambiguity (§3.4), the symmetric-encoding choice if the loader can't support it, the G-channel representation, or any real/fitted tag you can't ground.

## 8. Completion report (structured)
Return: (a) worktree/branch/base SHA (+ live origin head, + any surface drift); (b) the new node_type + id-prefix + the `interlocks` relation schema (the SCHEMA.md diff summary); (c) the mechanism nodes minted (ids + real/fitted tags + cited leaves); (d) the symmetric-encoding decision; (e) the live independent-param count: the derived value, the formula, and the CI assertion (confirm a FITTED alpha brace leaves it unchanged); (f) the falsification-net wiring (root node, the propagation rule, a demo that marking a channel `refuted` flags clm-iouqn9); (g) the alpha instance-1 population (the chain + the FITTED tag); (h) verify-kb-metadata result; (i) every deviation + open item for the auditor; (j) commit list. Be honest about anything that didn't validate.

---

## IMPLEMENTER 60-SECOND SKILL-SELECTION PLAN (commit 1)

- **ave-representation-capability-check** — fired on EVERY mint before writing: relation token `interlocks` (grepped: 0 hits repo-wide, collision-free); id-prefix `ilk-` (grepped: 0 hits, collision-free); node_type name `interlock-mechanism`; AVOID `joint-constraint` (38 hits in manuscript/, established prose term) and `brace`/`over-bracing` (the mechanical Cosserat σ^A — trampoline-analogy-primer.md:78/155/354/358/359/366/386/460/465). Capability check on the node_type: it must be able to host (mechanism statement + real/fitted tag + cited corpus leaf + derived-endpoint) and be a valid edge TARGET (hub encoding) — confirmed.
- **consistency-vs-emergence** — the real/fitted tag IS the chord/echo axis: `fitted-identification` = a CONSISTENCY echo (buys NO parameter reduction); `real-geometric-constraint` = a chord (removes a DOF). The independent-count formula enforces this (fitted→no-drop, real→−1). R·r=1/4 is FITTED (ch8:11 "the substrate does NOT independently select"), so the alpha brace is a consistency echo — count must NOT drop.
- **ave-canonical-leaf-pull** — every mechanism node CITES an existing corpus leaf, never re-derives: R·r=1/4 + R−r=1/2 + d=1 at ch8-alpha-golden-torus.md:44-46; the FITTED classification + Compton-trapping at ch8:11 + ch0-intro.md:21; falsification-net at omega-freeze-cosmic-grain-cascade.md:11.
- **verify-before-cite** — every file:line grepped LIVE at the base SHA before building (DONE: clm-iouqn9/dsb560/a7cbqq/0ktpcn/5xon03/fgo20a/jwyy6l all confirmed; ch8:11/:44-46, ch0:21, omega-freeze:11 all confirmed verbatim; SCHEMA anchors :5/:25/:56/:123/:152/:171/:191-226/:203/:43/:26 confirmed).
- **INVARIANT-S11 (governs)** — deliberate, verifier-gated spine extension (extend, don't reinvent): new node_type + relation declared in `.index/SCHEMA.md` + the pipeline tools, with its own greppable `\bilk-[a-z0-9]{6}\b` id; NEVER a parallel local scheme. Mirrors the `def-`/INVARIANT-S12 Stage-1+2 precedent exactly.

## SURFACE-VERIFY RESULT (at base 1c0afab7)
- `interlocks` token: 0 hits (collision-free) ✓ ; `ilk-` prefix: 0 hits ✓ ; `joint-constraint`: 38 hits (avoid) ✓ ; `over-bracing` σ^A: present (avoid `brace` as token) ✓
- `SCHEMA.md`: edge-class section :193-226 (3 relations depends/strengthens/supports), `relation:` union :203, 8-key shape :212, ref-integrity :43, edge-class table :26, Definition record :123, Framework record :152, sort key :171 — ALL MATCH.
- `depends-on.jsonl`: 700 edges (depends 685 / strengthens 12 / supports 3), 8-key shape — MATCH.
- claims.jsonl node-type histogram: axiom 4 / claim 287 / definition 13 / experiment 12 / invariant 22 / support 3 (341 total); input-only claims = 143 — MATCH.
- **SURFACE DRIFT FLAGGED (non-blocking):** SCHEMA.md `:5` says "SIX" node types (correct), but `:25` and `:56` still say "**five** node types" and omit `definition` — i.e. the Stage-2 `def-` LIVE (2026-06-08) update refreshed :5/:171 but missed the :25/:56 prose enumerations. claims.jsonl already materializes `definition` (13 records), so :25/:56 are stale. I bring them current (to the full set incl. `definition` + the new `interlock-mechanism`) when I edit those lines; flagged here so the auditor sees the pre-existing omission I corrected rather than a silent change.
