### ENTRY 2026-08-03-mr-fragment-cite-repins-correction (2026-08-03): consolidated dated correction — drifted file:line cites re-pinned across six `mr-*` fragments

- **Class: bookkeeping correction under Rule 12 / the news-fragments convention (`README.md:7`). Originals are UNTOUCHED — no other lane's fragment is edited.** Not adjudication; no claim, value, or disposition in any referenced fragment changes. Only the `file:line` coordinates are re-pinned.
- **Consolidated, one file rather than six.** `README.md:7` requires *"a dated `-correction` suffix file referencing the original"*; it does not require one file per original, and `verify-docket-keys.py` enforces **key uniqueness only** (no filename↔key mapping). The manuscript-reconciliation epic's lanes are closed, so every fragment below is another lane's — a single dated file referencing each original satisfies the convention with the least corpus churn. If a reviewer wants one-per-original instead, this file splits cleanly along its rows.
- **Why the drift:** all seven cites were captured during the 2026-08-02 sweep and have since been displaced by landed corrections in the same files (Rule-12 banners, DE-CLAIM notes, scope corrections) — none by a content change to the cited claim itself. **Every target below was re-verified BY CONTENT, not by line arithmetic.**

#### Re-pin table

The **content anchor** is the primary, drift-proof key; the two line columns are secondary. `main` = `origin/main` @ `66fc7e69`; `branch` = after `docs/mr-handoff-mechanical-0803` lands (that branch's own edits displace four of these further).

| # | fragment + line carrying the stale cite | cited file | content anchor (primary key) | on `main` | after branch |
|---|---|---|---|---|---|
| 1 | `2026-08-02-mr-gw-ch08-residuals-correction.md:5` | `manuscript/ave-kb/vol3/gravity/ch08-gravitational-waves/gw-propagation-lossless.md` | `LIGO gravitational waves have strain` | ~~`:34`~~ → **`:42`** | `:42` (unchanged — file not touched) |
| 2 | `2026-08-02-mr-vol6-crosswires.md:5` | `manuscript/vol_6_periodic_table/chapters/12_neon.tex` | `as in a neon discharge tube` | ~~`:48`~~ → **`:65`** | `:65` (unchanged) |
| 3 | `2026-08-02-mr-no-kb-home.md:7`; `2026-08-02-mr-no-kb-home-correction.md:7`, `:8`, `:9` | `manuscript/vol_4_engineering/chapters/01_vacuum_circuit_analysis.tex` | `the derivation of Silicon-28 ($Z=14, A=28$)` | ~~`:512`~~ → **`:579`** | **`:619`** |
| 4 | `2026-08-02-mr-varactor-keying.md:4`; `2026-08-02-mr-varactor-keying-correction.md:6`, `:7` | `manuscript/vol_4_engineering/chapters/01_vacuum_circuit_analysis.tex` | `C_{vac}(V) = \frac{C_0}{\sqrt{1 - (V/…)^2}}` (IMD varactor resultbox, `\label{eq:varactor_imd}`) | ~~`:720`~~ → **`:787`** | **`:837`** |
| 5 | `2026-08-02-mr-varactor-keying-correction.md:7` | `manuscript/vol_4_engineering/chapters/01_vacuum_circuit_analysis.tex` | `V_{IP3} = \sqrt{\frac{4}{3}}\; V_{…}` (`\label{eq:ip3}`) | ~~`:756`~~ → **`:823`** | **`:892`** |
| 6 | `2026-08-02-mr-legacy-negatives.md:12` | `manuscript/vol_0_engineering_compendium/chapters/03_computational_graph.tex` | `\paragraph{The Poisson-Disk Solution:}` | ~~`:11`~~ → **`:33`** | `:33` (unchanged) |
| 7 | `2026-08-02-mr-legacy-negatives.md:11` | `manuscript/vol_1_foundations/chapters/04_continuum_electrodynamics.tex` | `\rho_{bulk} = \frac{m_{node}}{V_{node}}` | ~~`:155`~~ → **`:177`** | **`:194`** |

**Note on row 6.** `:11` was not merely stale — on `main` it lands inside a `%` comment block, not on the substantive claim. The Poisson-disk two-register item's actual print site is the `\paragraph{The Poisson-Disk Solution:}` at `:33`. The item's substance is unaffected.

**Note on rows 4/5.** These two sites are *re-keyed in place* by the branch above ($V_{yield}\to V_{snap}$, and $50.4$ kV → $590$ kV at row 5). The `mr-varactor-keying-correction.md:6` routed question — *"confirm whether the `:720`/`:756` request is now narrowed (mechanical `V_snap` re-key per the ratified line) or still open"* — is thereby **answered in the narrowed direction and executed**; see `2026-08-03-mr-handoff-mechanical.md` §B8 for the receipts and the flagged value substitution.

**Note on row 3.** `2026-08-02-mr-no-kb-home-correction.md:7`'s claim that *"repo-wide grep for `80.174` in `manuscript/` returns exactly one hit"* was **re-verified and still holds** at the new line. Only the coordinate moved.

#### ★ The seventh cite in the handoff's FLAG-1 table was NOT executed — scope finding

`bingham :36→:66` **does not live in an `mr-*` docket fragment.** Two-method search: `grep -ri bingham _orchestration/docket-entries/` → **zero hits**; `grep -rn analytical_summaries _orchestration/docket-entries/` → **zero hits**. It is located instead in the **board**, `_orchestration/2026-08-02_manuscript-reconciliation-board.md:60` — the vol0 finding header citing `manuscript/vol_0_engineering_compendium/chapters/02_analytical_summaries.tex:36`; the printed `\item \textbf{Macroscopic Rheological Yield Stress (Bingham-Plastic Limit):}` is now at **`:66`** (displaced by that chapter's own landed `[DE-CLAIM 2026-08-02]` block).

**Not executed, deliberately:** the board is not a docket fragment (so this correction-file convention does not cover it), and it is currently modified by **two open branches** — `docs/mr-board-corrections-0803` and `docs/mr-epic-closeout`, both of which touch that exact file. Editing it here would produce a needless server-side conflict of precisely the class this convention exists to retire. **Routed to whichever board lane lands next**; the anchor above is drift-proof.
