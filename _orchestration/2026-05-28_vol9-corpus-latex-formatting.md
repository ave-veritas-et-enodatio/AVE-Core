# Epic: Vol 9 + corpus-wide LaTeX formatting cleanup

**Opened**: 2026-05-28 (orchestration session, Grant)
**Branch convention**: implementor branches off `main`, PRs into `main` (matches recent Vol 9 practice PR #55-57; `analysis/integration` is stale).
**Physics touched**: NONE. Pure formatting / typesetting infrastructure. No KB claims, no derivations, no numerical values change.
**Origin**: external formatting review of Vol 9 ("The Vacuum Datasheet"). All empirical claims in the review were re-verified by grep before opening this epic (see Verification below).

---

## Scope decision (Grant, 2026-05-28)

- **Full corpus-wide path sweep** chosen (not Vol-9-only) so the margin gate can actually drop to ~30-50pt at the end.
- Branch off `main`, PR into `main`.
- Spawn an implementor for the whole formatting pass; orchestration session does the review + merge.

## Critical scope nuance (why this is more than "a Vol 9 preamble fix")

`manuscript/structure/preamble.tex` and `manuscript/structure/commands.tex` are **shared by every volume** (`main.tex` `\input{../structure/...}`). `check_latex_margins.py` runs on **every** volume's log via the `COMPILE_VOL` macro (`Makefile:154`) with a single shared `max_allowed` threshold. Therefore:

- Adding `seqsplit` / `\kbleaf` / `\sisetup` to the shared files is **safe & additive** — no other volume invokes siunitx at all (0 corpus-wide matches), so a `\sisetup` style decision cannot disturb existing renders.
- Demoting `\sloppy` and dropping the gate are **corpus-wide actions**. The gate header documents the shared foreword alone had 108pt overruns. The gate cannot drop below those overruns until the long-`\texttt{}`-path sweep covers foreword + Vols 0-6 + Vol 9. **Gate drop is the LAST step, data-driven from a full `make pdf` max-overrun measurement.**

## Verification (done at epic open — all review claims confirmed)

| Claim | Verified |
|---|---|
| siunitx loaded, invoked 0× | 0 across entire manuscript |
| `\times 10^{...}` hand-written in Vol 9 | exactly 108 |
| `\hline` in Vol 9 | 57 (14 chapters) |
| booktabs only in Ch7(12)/Ch14(15)/Ch8(6+2 hline mixed) | confirmed exactly |
| only Ch3 has captioned/labelled table floats | confirmed (2 `table` env, 2 `\caption`, both Ch3) |
| Ch3 template itself uses `[h]` + `\hline` + in-cell 90-char path | confirmed (lines 65,112 `[h]`; 68-74 `\hline`; line 71 path-in-cell) |
| tabularx loaded, unused | confirmed |
| Vol 9 longtables (take `\caption` directly) | 5: Ch4, Ch12, Ch15, Ch16(×2) |
| long `\texttt{}` paths corpus-wide | foreword 14; Vol 9 ~130; scattered Vols 1/2/3 + backmatter |

---

## Phases (ordered; build-verify + commit after each)

### Phase 1 — infra (shared `commands.tex`, additive, safe)
- Add `\usepackage{seqsplit}` to `preamble.tex` (or `commands.tex`).
- Define `\newcommand{\kbleaf}[1]{\texttt{\seqsplit{#1}}}` in `commands.tex`.
- Add a `\sisetup{}` block in `commands.tex` (`exponent-product=\times`, `per-mode=symbol`, plus sensible `group-digits`/`separate-uncertainty` defaults) and `\DeclareSIUnit` any custom units used in Vol 9 (audit unit strings first).
- DO NOT touch `\sloppy` or the gate yet.
- Build-check: `make vol9` (and one other volume, e.g. `make vol1`) still compiles.

### Phase 2 — Vol 9 tables (T1-1, T1-2, T3-1, T3-2, T3-3)
- Fix Ch3 first (it's the template): `[h]` → `[htbp]` (lines 65, 112), `\hline` → booktabs (`\toprule`/`\midrule`/`\bottomrule`, drop vertical rules).
- Propagate across the other 15 chapters: wrap each bare `tabular` in `\begin{table}[htbp]...\caption{...}\label{tab:vol9_<topic>}\end{table}`; `longtable` (Ch4/12/15/16) takes `\caption`+`\label` directly (no float wrap).
- Convert all 57 `\hline` → booktabs; standardize.
- Drop now-redundant `\vspace{...}` left after bare tables.
- For the widest 5-col `p{}` tables riding the overfull edge, switch to `tabularx{\linewidth}{...X...}` (T3-3) opportunistically.
- Build-check after each ~4 chapters; confirm Table numbers + List of Tables populate.

### Phase 3 — siunitx adoption (T1-3) — HIGHEST RISK, isolated pass
- 108 `\times 10^{...}` → `\num{}`/`\qty{}`; unify all unit strings (`\Omega`/`\,\Omega`, `MeV`, `kV`, `V/m`, etc.) → `\si{}`/`\qty{}`.
- CAUTION: many `\times 10^{...}` sit inside larger math expressions where `\num` is NOT a clean drop-in — convert by hand, verify each. `gensymb` is co-loaded (degree/celsius) — watch for clashes.
- Build-check frequently; this is where silent breakage hides.

### Phase 4 — corpus-wide long-path sweep (T2-1 completion)
- Apply `\kbleaf{}` to long `\texttt{}` path citations corpus-wide: foreword (14), Vol 9 (~130), Vols 1/2/3 + backmatter scattered hits. Greppable: `\texttt{[^}]{50,}}`. Leave short `\texttt{}` (claim ids like `clm-xxxxxx`, short filenames) alone.
- Demote `\sloppy` → `\sloppypar` (local) or remove, in `preamble.tex`.
- Build ALL volumes (`make pdf`), grep logs for `Overfull \hbox`, find the new max overrun.
- Set `check_latex_margins.py` `max_allowed` from that data (~30-50pt target). Update the threshold-history comment block.
- Update `_orchestration/index.md:65` follow-up (mark the per-overrun cleanup + gate-tightening DONE).

---

## Implementor instructions
- Branch `analysis/vol9-corpus-latex-formatting` off `main`.
- Commit per phase with clear messages. Push the branch. Do **NOT** open the PR or merge — orchestration session reviews + merges (audit-tag + `--no-ff` pattern).
- Pure-AVE-corpus rule applies to all commit messages.

## Status
- [ ] Phase 1 — infra
- [ ] Phase 2 — Vol 9 tables
- [ ] Phase 3 — siunitx
- [ ] Phase 4 — corpus path sweep + gate drop
