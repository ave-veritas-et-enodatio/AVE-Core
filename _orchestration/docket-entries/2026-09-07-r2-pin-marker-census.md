### ENTRY 2026-09-07-r2-pin-marker-census

**Lane:** doc/tooling — the MIGRATION half of ruling **R2**
(`2026-08-06-rulings-decision-batch.md`, Grant verbatim *"1. agree / 2. agree /
3. agree / 4. agree / 5. agree"*; re-authorised 2026-09-07, *"build the pin
marker"*). The gate half — teaching `verify-md-links.py` the marker — is a
parallel lane's and is **not** touched here.

Base for every number below: `5a36cea5`, measured in a pristine `git worktree`
(the line-cite pass walks the filesystem, so untracked local files would
otherwise resolve paths a fresh clone cannot).

---

## 1. The token

    <path>:<line>@<sha>            <path>:<start>-<end>@<sha>

`<sha>` is 7–40 lowercase hex. The marker is **per-cite**: it exempts exactly
the cite it is attached to and nothing else on the row. That is the whole point
of R2 — the heuristic it replaces is row-scoped.

**Coinage: 0 collisions at `5a36cea5`,** by two structurally different methods
(`git grep -cIE` over the index; a Python `re` walk of every tracked non-binary
blob). Both re-run with a **range-aware** pattern, because:

> ★ **The obvious probe is wrong.** `:[0-9]+@[0-9a-f]{7}` MISSES every range
> cite — in `foo.md:50-57@<sha>` the `-57` sits between the digits and the
> `@`. It under-collected on this migration's own second file. The correct
> pattern is `:[0-9]+(-{1,2}[0-9]+)?@[0-9a-f]{7}`, and it now lives as one
> constant (`pin_census_lib.MARKED_CITE_TAIL_RE`) rather than being retyped.

## 2. Census — the numbers R2 quoted are stale, and so is their shape

R2's "96" was KB-scoped at snapshot `d5a1b06b`. Re-measured at `5a36cea5`:

| scope | line-cites on a SHA-bearing line | distinct lines | lines >500 chars |
|---|---|---|---|
| corpus-wide | **525** | 271 | 182 |
| KB only | **156** | — | — |

Method: `pin_census_lib` imports `iter_line_cites`, `cite_target_uncheckable`
and `resolve_cite_candidates` **from `verify-md-links.py` itself**, so the
census measures the exact population the gate acts on rather than a lookalike
one. Cites with no `:NN` are excluded (the gate has no line to check).

Classification of those 525:

| class | n | what it is |
|---|---:|---|
| **LIVE** | **480** | resolves at HEAD; a normal cite that merely shares a row with somebody else's provenance SHA |
| **TRUE-PIN** | **5** | does not resolve at HEAD; corroborated at a SHA on its own row |
| **DEAD** | **0** | path resolves, line does not, nothing claims a pin |
| UNRESOLVED-PATH | 34 | path names nothing anywhere (house shorthand, sibling-repo files, line-wrapped names) — already advisory-reported |
| SKIPPED-SHAPE | 6 | glob / home-dir / ephemeral target — out of scope for both tools |

(Re-running the census on this branch AFTER the §5 pilot returns 523 / TRUE-PIN
3: the two migrated cites leave the bare-cite grammar once they carry a marker,
which is exactly the behaviour a marker-only gate wants.)

**99% of what the exemption hides is a live cite.** That is R2's false-negative
claim, measured.

## 3. The load-bearing consequence: re-keying the gate is FREE

Removing the SHA exemption today makes **zero** cites newly gate. Measured two
ways, and they agree:

1. the census: LIVE 480 / DEAD 0;
2. the gate's own `check_line_cites`, run over the same population with
   `pinned` forced False — `checked = 480`, `dead line cite = 0`
   (plus 32 pre-existing `blank line cite` advisories, which do not gate).

So the marker migration is not a prerequisite for the re-key. It buys machine-
readability for five cites; the re-key buys 480 cites of coverage.

## 4. Classifier precision — MEASURED BY HAND, and it is poor where it matters

19 cites resolved by hand, reading the cited line at HEAD **and** at the pinned
SHA:

| class | hand-checked | classifier correct |
|---|---:|---|
| LIVE | 10 (random sample) | **10 / 10** |
| UNRESOLVED-PATH | 4 | **4 / 4** |
| TRUE-PIN | **5 — the whole population** | **2 / 5 (40%)** |
| DEAD | 0 in population | emptiness confirmed by the §3 second method |

The three TRUE-PIN misses share one mechanism, and it is not fixable by regex:
**a cite can EXIST at a SHA that sits on its row for an unrelated reason.** Two
of the three are cites broken by a *rename*, riding a session-stamp SHA; one
resolves at its SHA to content that flatly contradicts the citing sentence
(the row cites an E1b CMB-LSS result, the line at that SHA is a C3-MUON-DELTA
row). The correct repair for all three is to **fix the path**, not to pin it.

→ **Do not bulk-migrate on this classifier.** `migrate-pin-markers.py`
therefore requires a hand-verified allow-list by default; `--allow-unverified`
exists but prints the measured precision first.

## 5. Pilot

`_orchestration/docket-entries/` was the suggested pilot directory. **It has
zero TRUE-PIN cites** (71 on SHA-bearing lines: 64 LIVE, 7 UNRESOLVED-PATH), so
the pilot moved to `_orchestration/`, which holds 2 — both hand-confirmed.

| `_orchestration/` | before | after |
|---|---:|---:|
| line-cites on SHA-bearing lines | 150 | 148 |
| TRUE-PIN | 2 | 0 |
| LIVE | 134 | 134 |
| DEAD | 0 | 0 |
| cites carrying `@sha` | 0 | 2 |

Idempotent on the live corpus as well as in the fixtures: a second `--apply`
reports 0 candidates and changes no bytes.

**Corpus-wide migration is NOT done and is a separate decision.** The residue is
three cites, all of which want a path repair rather than a marker — see §4.

## 6. Refusals, by construction

`migrate-pin-markers.py` will not machine-edit a byte-frozen document. Any
candidate in a `*prereg-FROZEN*` file, a `research/**/*prereg*.md`, or a
`research/**/*[-_]result.md` is listed for a human and the run exits **2**, so
"refused" cannot be mistaken for "nothing to do". Proven both directions on
synthetic repos: exit 2 with the file byte-identical on the frozen path, exit 0
with the cite marked on byte-identical content at an ordinary path.

## 7. Open for Grant

1. **Re-key now, migrate later?** §3 says the two are independent. The gate lane
   can drop the row-scoped exemption today at zero cost; nothing waits on this
   census.
2. **The three §4 misses want path repairs, not markers.** That is corpus
   editing, not tooling — outside this lane's scope. Route it, or leave it.
3. **Prose-declared pins that still resolve (28 of the 480).** An author wrote
   "as shipped at", the cite resolves anyway, so it is LIVE and the migrator
   leaves it. Under a marker-only gate these are checked and pass. Confirm that
   is the wanted posture rather than marking them for intent.
