# INTERNAL provenance — Reach paper (saturating-family exclusion map)

**NOT part of the paper.** This is the audit trail the public paper deliberately
does not carry (pure-physics rule: the paper cites no private repo, no framework
volumes, no program history). Every quantitative claim in the paper maps here to
its corpus source — canonical claim-id, driver, result doc, solidity band — or to
its external citation. Mirrors the pattern of
`papers/2026_birefringence_letter/provenance.md`.

**Status:** PHASE-1 SKELETON. The paper has NO prose yet; this file carries the
CLAIM-INVENTORY provenance (the §3 table of `outline.md`) and the reference /
flag / verify skeleton. The number-by-number map is populated when the paper is
drafted.

---

## 1. Claim → source map (phase-1: from `outline.md` §3 claim inventory)

The full claim table lives in `outline.md` §3 (C1–C12) with class + provenance per
claim. Corpus-internal sources, verified at worktree HEAD this session:

| claim | corpus source | claim-id | solidity |
|---|---|---|---|
| C4 (muonic-H exclusion, band) | `research/2026-07-05_problem3-muonic-lamb_RESULT.md` | `clm-sve3xc` | 0.80 |
| C5 (pitch-cutoff robustness, super-pitch) | `research/2026-07-06_em-keying-round3-eps-dc-mechanism_RESULT.md` §9 finding [18] | `clm-sve3xc` (rationale) | 0.80 |
| C6 (U91+ no-real-solution) | `research/2026-07-05_problem3-muonic-lamb_RESULT.md` "SECONDARY"; fork-memo §1 Z-table | `clm-sve3xc` | 0.80 |
| C7 (whole-family shared constraint) | `manuscript/ave-kb/common/historical-precedents.md:47` | (framing; consistency) | — |
| C8 (charge-keyed / held-field loads) | `research/2026-07-06_em-keying-round3-eps-dc-mechanism_RESULT.md` | `clm-chgky3` | **0.55 input-only** |
| C9 (static-B transparency, separate sector) | `manuscript/ave-kb/vol4/falsification/ch11-experimental-bench-falsification/pvlas-static-b-verdict.md` | `clm-pvlas1` | 0.80 |
| C10 (E-route 3-way discriminator) | `manuscript/ave-kb/vol4/falsification/ch12-falsifiable-predictions/vacuum-birefringence-e4.md`; Letter `main.tex` | `clm-pp3qwf` | 0.80 |
| C11/C12 (B-I zero-bir shares transparency; single-cone scope) | Letter `main.tex` (FIX-2 DEFECT-B/C, MINOR-1) | (external RT/Boillat) | — |

**Solidity-band discipline note:** C8 (`clm-chgky3`) is input-only (0.55, srs-C₄₄
cross-lattice borrow gates it). It is cited to CLOSE the "is the atomic exposure
contingent on an open keying escape?" question, but NO headline claim rests on it —
C7 (whole-family exposure) is a floor-independence argument that stands without C8
(KEEP-BOTH posture). Do not build paper structure above the 0.55 band.

## 2. External reference verification (Crossref/arXiv, two-method — to populate at draft)

The external references are already Crossref/arXiv-verified in the birefringence
Letter's `refs.bib` + `provenance.md` §12 / §11 this-program; the reach paper
REUSES the verified entries (re-verify at draft time per verify-before-cite):

| ref | citation | status (Letter provenance) |
|---|---|---|
| `RussoTownsend2023` | Russo & Townsend, JHEP 01 (2023) 039, arXiv:2211.10689 | Crossref DOI + arXiv verified (Letter §12 DEFECT-B) |
| `Boillat1970` | Boillat, J. Math. Phys. 11(3), 941 (1970), DOI 10.1063/1.1665231 | Crossref full (Letter §12) |
| `Plebanski1970` | Plebański, Lectures on Non-Linear Electrodynamics, 1970 | INSPIRE author/title/year; NORDITA imprint UNconfirmable — **FLAG** (Letter §12) |
| `BornInfeld1934` | Born & Infeld, Proc. R. Soc. A 144, 425 (1934), DOI 10.1098/rspa.1934.0059 | Confirmed (Letter §3) |
| `Antognini2013` | Antognini et al., Science 339, 417 (2013), DOI 10.1126/science.1230016 | Crossref full (Letter §10) |
| `Ejlli2020` (PVLAS) | Ejlli et al., Phys. Rep. 871, 1 (2020), DOI 10.1016/j.physrep.2020.06.001 | Crossref full (Letter §3) |
| BMV static-B null | (external; retrieve + Crossref-verify at draft — §7-E NEEDS-DERIVATION) | NOT yet carried numerically |

## 3. Complete-enumeration vs model-dependent cell audit (the map's honesty)

Per `outline.md` §2 cell tags: **[E]** enumeration / **[M]** model-dependent /
**[X]** external-data / **[F]** forward. The audit that MUST accompany the table:

- **[E] cells are theorem-grade** and hold for the whole named subfamily (the W3
  zero-birefringence column: Boillat 1970 uniqueness + RT 2023 completeness). These
  are the enumeration spine; a referee can check them against the cited theorems.
- **[M] cells are point-computations** for the specific member as worked (the
  elliptic-branch W1/W2). Solidity flows from the corpus claim-id (0.80).
- **[F] cells are forward** (not yet measured); the E-route is `clm-pp3qwf` 0.80.
- **`?` cells are NEEDS-DERIVATION** (`outline.md` §7) — shown OPEN, not asserted.

## 4. Discipline tags (phase 1)

- **verify-before-cite:** solidity bands re-grepped from `claims.jsonl` +
  `claim-quality.md` at worktree HEAD; RT four-member + Boillat uniqueness read
  verbatim from Letter `main.tex`/`refs.bib`.
- **consistency-vs-emergence:** theorem/computation/consistency/forward only; NO
  emergence claim. Worked-member `E_c` is CODATA-derived through α, m_e
  (falsification/consistency-class per `clm-sve3xc`).
- **flag-don't-fix:** the tanh/rational family table the brief cites is NOT in the
  corpus (§5 FLAG-1 below).
- **Rule 11 honest closure:** worked-member self-exclusion presented as the teeth,
  not a rescue target.
- **pure-AVE-corpus:** no external-context references of any kind; pure NLED physics.

## 5. FLAGGED FOR GRANT (judgment calls the auditor/Grant owns)

1. **FLAG-1 — the tanh/rational family members are NOT corpus-sourced.** The brief
   describes the fork memo's family table as "elliptic / Born–Infeld / tanh /
   rational as coefficient–scale pairs." A two-method grep (the two named files +
   corpus-wide) finds NO tanh or rational member anywhere. The fork memo carries
   ONLY the elliptic kernel; `historical-precedents.md` "Root 3" frames the B-I
   family + elliptic branch but names no tanh/rational member. **Decision needed:**
   (a) commission the tanh + rational representatives as new derivations
   (`outline.md` §7-F, §7-A/B/C), or (b) present the first submission on the
   corpus-grounded rows only (RT four + elliptic branch + generic B-I-type) and
   defer the constructed representatives. **Recommend (b) for first submission.**
2. **FLAG-2 — how much of the paper is framework-branded.** Keith's design has the
   main result framework-INDEPENDENT; the worked member is "a numerator-softening
   elliptic branch." **Decision:** does the worked member get named as the
   framework's SVE branch (linking the birefringence Letter), or stay a neutral
   "elliptic softening representative" with the Letter cited only as the E-route
   source? (Affects whether this paper cross-cites the Letter as same-author work.)
3. **FLAG-3 — the coefficient–scale-plane bound (`outline.md` §7-D).** The
   strongest form is a REGION of the (coefficient, scale) plane excluded by each
   window. The corpus has point-computations, not the plane bound. **Decision:** is
   the plane bound in-scope for THIS paper (a substantial new derivation), or is the
   row-list map the deliverable and the plane bound a follow-on?
4. **FLAG-4 — venue + length (`outline.md` §5).** Recommend PRD regular article
   (primary) / NJP open-access (fallback). **Decision:** Grant picks; affects
   length target and abstract cap.
5. **FLAG-5 — Plebański imprint (inherited from the Letter, Letter provenance §12).**
   The `Plebanski1970` NORDITA imprint is not database-confirmable; if a referee
   wants a fully grounded imprint, keep Boillat as sole primary uniqueness cite.

## 6. Build + verify status (phase 1)

- `make verify`: GREEN (ξ-namespace advisory pre-existing + non-gating, as in the
  Letter). `verify-md-links` clean.
- No `src/` change (phase 1 is documentation only — outline + inventory).
- No new physics derivation (phase 1 scope).
