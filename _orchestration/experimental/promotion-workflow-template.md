# Promotion Workflow Template: Sibling-Repo → AVE-Core Engine Work

**Canonical home**: `_orchestration/promotion-workflow-template.md`
**Established**: 2026-05-20 EOD — extracted from `exp-a1-hopf-repo-audit.md` Axis 8 + adapted from `ave-ip-divide-discipline` Step 5
**Applies to**: any sibling-repo (AVE-HOPF / AVE-PONDER / AVE-Fusion / AVE-Protein / AVE-Metamaterials / AVE-Propulsion / AVE-VirtualMedia / AVE-APU / AVE-QED) promoting engine work to AVE-Core
**Companion skill**: [`~/.claude/skills/ave-ip-divide-discipline/SKILL.md`](file:///Users/grantlindblom/.claude/skills/ave-ip-divide-discipline/SKILL.md) Step 5 (Extraction procedure)

> This template captures the discipline for promoting engine work from private sibling repos to public AVE-Core. Sibling repos hold application IP + bench-specific implementations; AVE-Core holds substrate-physics theory + canonical methodology. The promotion direction is unidirectional (private → public) and requires explicit classification + IP-stripping before content lands in public canon.

## When to fire

Trigger this workflow BEFORE promoting any code, methodology, KB content, or test infrastructure from a sibling repo to AVE-Core. Examples:

- Generalizable methodology developed in sibling repo (e.g., NEC2 ALPHA-post-processing in AVE-HOPF `scripts/hopf_02_nec2_run.py:245-330`) needs to become canonical AVE-Core for reuse across multiple experiments
- Test pattern from sibling repo (e.g., L↔R mirror exactness verification in AVE-HOPF `tests/test_hopf02_geometry.py`) generalizes to a corpus-wide discipline test
- Engine constants developed for sibling repo's needs (e.g., a new canonical parameter) should live in `ave.core.constants` not sibling-specific
- KB leaf in sibling repo's manuscript covers content that belongs in cross-volume AVE-Core canon

## Pre-promotion checklist (10 steps)

### Step 1 — Classification check

Classify the content per [`ave-ip-divide-discipline`](file:///Users/grantlindblom/.claude/skills/ave-ip-divide-discipline/SKILL.md) Step 2:

| Class | Description | Promotion eligibility |
|---|---|---|
| **L0** | Pure substrate physics, no application-specific framing (axioms, canonical theorems, fundamental identities) | ✓ Promote as-is |
| **L1** | Theory-supporting derivation, IP-strippable (methodology + general-physics machinery; specific application targets removable) | ✓ Promote AFTER stripping (Step 2) |
| **L2** | Theory-application bridge (general methodology tightly bound to specific bench design) | ⚠ Promote with caution; may need re-derivation rather than direct extraction |
| **L3** | Application/hardware IP (PCBA design, vendor protocols, mandrel CAD, commercial parameters) | ✗ DO NOT promote — keep private |
| **L4** | Commercial/IP-protected (patent-pending material, trade secrets, partnership-specific) | ✗ DO NOT promote |

**If unsure**: surface to Grant adjudication before promotion. Default to staying private (false-positive of "this is L1, promote" is much costlier than "this is L2, defer").

### Step 2 — IP stripping (L1 only)

For L1 content, strip before promotion:

| What to strip | Example (HOPF) |
|---|---|
| Mechanism names tied to commercial application | "HOPF-02 enantiomer" → "chiral antenna pair" |
| Application targets | "for VNA fab" → (omit) |
| Specific bench-design parameters | "50×185 mm board, 4 v-score lines" → (omit) |
| Quantitative claims tied to commercial value | "$123 BOM" → (omit) |
| Vendor-specific protocols | "JLCPCB ENIG finish + impedance control" → (omit) |
| Sub-repo's branch/commit refs | "per AVE-HOPF/.agents/HANDOFF.md TODO #3" → cite by content not source-repo |
| 3D-print mandrel CAD | (do not include in promotion) |

The stripped content should be readable as substrate-physics methodology WITHOUT any indication of which application motivated it. After stripping, ask: "could a graduate student reading this in AVE-Core understand it as physics, without seeing the sibling repo?" If no, more stripping needed.

### Step 3 — Constants-source check

Verify the promoted code imports from canonical sources, not hardcoded values:

```python
# WRONG:
ALPHA = 7.2973525693e-3
ELL_NODE = 3.862e-13

# CORRECT:
from ave.core.constants import ALPHA, ELL_NODE
```

Per `ave-canonical-source` skill discipline + the HOPF-02 audit lesson (`scripts/hopf_02_nec2_run.py:88` constants-gate leak): every numerical constant must trace to `ave.core.constants` or `ave.core.gravity` etc., never hardcoded as a float literal.

Also extend `tests/verify_local_universe.py` MAGIC_NUMBERS whitelist if new canonical values are introduced.

### Step 4 — Test promotion

If tests are promoted alongside code:

- Promoted tests must pass via AVE-Core's `make verify` + `make test`, NOT just the sibling repo's test runner
- Test fixtures that depend on sibling-specific paths (e.g., `AVE-HOPF/hardware/...`) must be re-anchored to AVE-Core-relative paths or generalized
- If the test pattern itself is novel discipline (e.g., L↔R mirror exactness), consider promotion to a skill at `~/.claude/skills/ave-<pattern>/SKILL.md` rather than just test code

### Step 5 — `.ip-graph.yaml` entry

Add an APP-XX entry to the sibling repo's `.ip-graph.yaml` mapping the promoted public destination ← the private origin:

```yaml
# AVE-HOPF/.ip-graph.yaml
applications:
  APP-01:
    private_repo: AVE-HOPF
    private_path: scripts/hopf_02_nec2_run.py:245-330
    private_classification: L1
    extraction_date: 2026-MM-DD
    public_destination: AVE-Core/src/ave/regime_1_linear/nec2_wrapper.py
    public_classification: L0 (after stripping)
    extraction_note: "α-post-processing methodology for NEC2 classical baseline; application-specific (p,q) inputs removed"
```

Per `ave-ip-divide-discipline` Step 4, this is the bidirectional cross-reference graph that prevents pointer-opacity violations downstream.

If `.ip-graph.yaml` does not yet exist in the sibling repo, this is the seed entry — also document the bi-directional pointer pattern (`<!-- private-downstream: APP-XX -->` in public AVE-Core; `<!-- ave-core-upstream: <path> -->` in private sibling).

### Step 6 — Public AVE-Core commit message

The AVE-Core commit landing the promoted content:

- ✓ Note "extracted via ave-ip-divide-discipline" (audit trail)
- ✓ Note the L-classification of the extracted content (e.g., "L0 substrate-physics methodology")
- ✓ Apply skill discipline (`ave-canonical-source` for constants; `ave-canonical-leaf-pull` for KB integration)
- ✗ DO NOT name the private source repo
- ✗ DO NOT include any L2-L4 details that survived through Step 2 stripping
- ✗ DO NOT cite sibling-repo file paths

If you need to reference origin context, use opaque APP-XX reference: "per `.ip-graph.yaml` APP-XX".

### Step 7 — Private sibling repo commit message

The sibling repo's commit accompanying the promotion (typically the rename / move / refactor on the sibling side):

- ✓ Note "general substrate-physics theory now lives at AVE-Core/<path>"
- ✓ Add `<!-- ave-core-upstream: <path> -->` HTML comment in the sibling chapter/leaf that previously held the content
- ✓ Update sibling's `AGENTS.md` or equivalent if the import path changes
- ✓ Run sibling repo's `make verify` + `make test` post-extraction to confirm nothing broke

### Step 8 — Cascade-impact check (`ave-walk-back` discipline)

Does the promoted content change any AVE-Core matrix rows, canonical leaves, or skill triggers?

- If matrix rows in `divergence-test-substrate-map.md` need updates → `ave-walk-back` propagation across the 8-12 dependent files
- If canonical leaves need cross-reference updates → propagate per `ave-walk-back`
- If skill triggers are affected (e.g., new constant invalidates an existing MAGIC_NUMBERS whitelist entry) → skill amendment in same commit cycle

The bundle: promotion + cascade walk-back + skill amendment all land as coordinated batch per `ave-walk-back` Type-D framing.

### Step 9 — Sub-epic update

If the promotion concerns a tracked sub-epic (e.g., `_orchestration/exp-a1-hopf.md`):

- Update the sub-epic doc to reflect the new public location of the promoted content
- Cross-reference the `.ip-graph.yaml` APP-XX entry
- If the promotion closes a sub-epic phase (e.g., Phase 5 canonical tie-back), mark ✓ DONE

### Step 10 — Bidirectional verification

After all artifacts land:

- Verify the `.ip-graph.yaml` entry resolves both directions
- Verify the public AVE-Core file imports work in a clean Python environment
- Verify the private sibling repo's tests still pass (the extraction shouldn't break upstream)
- If `ave-ip-verify-pairing` tooling exists per `ave-ip-divide-discipline`, run it

## Common pitfalls (per audit-surfaced patterns)

### Pitfall 1 — Promoting L2 content as L1

The most common failure mode. L1 content has methodology general enough to extract; L2 content is tightly coupled to bench design. If after Step 2 stripping the content still reads as application-specific, it's L2 not L1. Defer or re-derive.

### Pitfall 2 — Constants-gate leak

Per AVE-HOPF audit `scripts/hopf_02_nec2_run.py:88` finding: a constant hardcoded to evade the canonical-source skill, then evades the test-time constants-gate because the whitelist doesn't cover that value. Per Step 3, double-check both the source code AND the MAGIC_NUMBERS whitelist.

### Pitfall 3 — Pointer-opacity violations (Class F)

Per `ave-ip-divide-discipline` Step 4 Class F: explicit `AVE-HOPF/...` paths in PUBLIC AVE-Core violate opacity. Per AVE-HOPF audit, 18 violations in `exp-a1-hopf.md` + 10+ in `project-hopf-02.md` were surfaced. After promotion, ensure public AVE-Core content uses opaque APP-XX pointers, not direct private-repo paths.

### Pitfall 4 — Skipping ave-walk-back cascade

A promotion that closes Step 1-7 but skips Step 8 leaves the AVE-Core matrix in an inconsistent state. Per `ave-walk-back` discipline, ALWAYS run cascade-impact check before considering the promotion complete.

### Pitfall 5 — Forgetting sibling repo's HANDOFF.md update

Per `ave-handoff-canonical-locale`: any state change in a sibling repo's canon should be reflected in that repo's `.agents/HANDOFF.md`. Promotion is a state change.

## Reverse promotion (Core → sibling)

Less common but tracked: when general AVE-Core canon needs application-specific extension in a sibling repo, the reverse direction follows the same discipline in reverse:

- L0/L1 content stays public-canonical in AVE-Core
- The sibling repo cites it via `<!-- ave-core-upstream: <path> -->` HTML comment
- The sibling repo's application-specific extension is L2+ and stays private
- No content "moves" from Core to sibling — the sibling cites upstream

Per AVE-HOPF AGENTS.md:107 "Authority rule for citations: AVE-Core for axioms / α / foundations": this is the established pattern.

## Audit verification

After completing a promotion, run:

```bash
# AVE-HOPF audit pattern (verify the extraction worked)
cd /Users/grantlindblom/AVE-staging/AVE-HOPF
git log --oneline -5  # show promotion commit
make verify           # constants-gate + Core parity must be green
make test             # tests still pass post-extraction

# AVE-Core audit pattern (verify the import works)
cd /Users/grantlindblom/AVE-staging/AVE-Core
git log --oneline -5
make verify
make test
python -c "from ave.<promoted_module> import <promoted_symbol>"
```

## First test case: NEC2 ALPHA-post-processing (HOPF → Core)

Per `exp-a1-hopf-repo-audit.md` Axis 8 R8.1: the NEC2 ALPHA-post-processing methodology in `AVE-HOPF/scripts/hopf_02_nec2_run.py` lines 245-330 is the canonical first test case for this template.

When ready to promote (gated on Grant adjudication post-A1-HOPF measurement):

- Step 1: L1 classification (substrate-physics methodology; application-specific (p,q) targets removable)
- Step 2: Strip "HOPF-02", "Δf shift", specific (p,q) values; preserve α-post-processing math
- Step 3: Import ALPHA from `ave.core.constants` (NOT hardcoded)
- Step 4: Promote test fixtures from `tests/test_hopf02_geometry.py` if generalizable
- Step 5: Seed `.ip-graph.yaml` APP-01 entry
- Step 6-10: Standard

Target public location candidate: `AVE-Core/src/ave/regime_1_linear/nec2_wrapper.py` or similar.

## Cross-references

### Skill discipline anchors
- `~/.claude/skills/ave-ip-divide-discipline/SKILL.md` — canonical IP-divide procedure (this template adapts Step 5)
- `~/.claude/skills/ave-canonical-source/SKILL.md` — Step 3 constants-source check
- `~/.claude/skills/ave-walk-back/SKILL.md` — Step 8 cascade-impact propagation
- `~/.claude/skills/ave-handoff-canonical-locale/SKILL.md` — Step 7+9 doc-locale discipline
- `~/.claude/skills/ave-canonical-leaf-pull/SKILL.md` — Step 6 leaf-pull when promoting KB content

### Related orchestration docs
- [`experimental-arc.md`](experimental-arc.md) parent epic — Phase 4 cross-repo coordination owns this template's invocation
- [`a1-hopf/exp-a1-hopf-repo-audit.md`](a1-hopf/exp-a1-hopf-repo-audit.md) Axis 8 — origin of this template
- [`a1-hopf/exp-a1-hopf.md`](a1-hopf/exp-a1-hopf.md) sub-epic — first test case for NEC2 promotion

### Sibling-repo HANDOFF anchors
- [`AVE-HOPF/.agents/HANDOFF.md`](../../AVE-HOPF/.agents/HANDOFF.md) — promotion-aware state holder
- AVE-PONDER, AVE-Fusion, AVE-Protein, AVE-Metamaterials, AVE-APU, AVE-Propulsion, AVE-VirtualMedia, AVE-QED — same pattern when those repos host promotable content

## Audit trail

- 2026-05-20 EOD — Template established from `exp-a1-hopf-repo-audit.md` Axis 8 R8.1 + adapted from `ave-ip-divide-discipline` Step 5. First test case (NEC2 ALPHA-post-processing) queued for post-A1-HOPF-measurement adjudication.
