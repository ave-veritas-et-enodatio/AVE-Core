# INVENTORY — Vol 2 KB ↔ manuscript SYNC (Lane C, 2026-09-13)

**Lane:** C — KB ↔ manuscript sync, vol2 HOT lane only (electron-identity F-pass emphasis).
**Branch:** `claude/lane-c-kb-ms-vol2-sync` · **Base:** `origin/main` @ `5619dd56` (BOARD #1043 on main; local = origin, ff-only pull was a no-op).
**Class:** inventory. **Adjudicates nothing; edits no leaf and no print** (the one mechanical PR is §6.1 and lives on its own branch).
**Scope:** `manuscript/vol_2_subatomic/` (16 documents: 13 chapters + `main.tex` + `_manifest.tex` + `frontmatter/00_title.tex`) ↔ `manuscript/ave-kb/vol2/` (146 `.md` files in 18 chapter/appendix directories, ~11,000 lines).

**Standing frame (read first).**
- KB **leaves** are the source of truth. `index.md`, `claim-quality.md`, distillates, `BOARD.md` and `consistency-manifest.yaml` are derived; the manifest is claim/label bridging, **not** the leaf↔chapter sync source of truth. Everything below cites leaves and TeX primaries.
- Rule 12: a site under a dated banner is *disclosed*, not debt. A TeX `%` comment is **not printed** — a walk-back that lives only in a comment discloses in git and nowhere the reader sees; those are listed as WB-LAG (comment-only).
- Grep indexed; **reading discharged.** Each chapter slice was read in full by a dedicated reader (three on ch01, four on ch07, two on ch06), findings then went to independent verifiers (cite-verbatim; fence/Q1; disclosure/prior-art), and a completeness critic runs over the union. Read receipts are in §7. **This is a vol2-only slice of the F-row universe (16 of 175 documents); it discharges no F-row** — per the tracker's combined-pass protocol a row closes only on a full-universe read receipt. The per-row hit ledger in §3 is input to that pass, not a substitute for it.

**Coverage at this stamp (2026-09-13 19:09 PDT):** 11/20 reader slices returned (ch01-A, ch01-C, ch02, ch03, ch04, ch05, ch06-A, ch06-B, ch07-A, ch07-C, ch08); 9 still pending in the resumed workflow run `wf_45d693ef-5ac` (ch01-B, ch07-B, ch07-D, ch09, ch10, ch11, ch12-mp, ch12-fp, appx-front). Reader-reported findings: 107; corpse hits: 39 (2 live-wrong); findings with verifier verdicts: 0. Findings below marked **[first-hand]** were read and grep-verified by the lane directly, independent of any agent; the rest are **reader-reported** and carry the verifier verdict column where one exists (UNVERIFIED otherwise). Re-run `assemble_inventory.py` after the workflow completes to refresh §1–§3 and §7 from the journal.

---

## §0 — Headline

**Referential integrity is fixable mechanically; the debt is walk-back propagation lag in print, and — in one direction — in the KB.**

1. **TeX → KB line anchors (47):** 29 exact, 6 evolved-in-place, **10 moved** (4 printed, 6 comment-only), 1 dead-by-retraction, 1 research-note cite in print. The ten are re-pinned in draft PR #1046 (§6.1). The 2026-09-06 scan's two vol2 S5 flags were both real; the other eight were invisible to it.
2. **KB → TeX line anchors: seven dead**, six in `neutron-identification.md` — a PATH-STABLE leaf — pointing at table rows, `\end{center}` and blank lines (§4.2). Left for a KB-side PR (excerpt ratchet applies).
3. **Electron-identity corpse pass (vol2 slice, §3):** in every slice read so far, **zero live-wrong** hits for F-C1…F-C11 / K4 / K6. Every hit is a fence-excluded homonym (static Link `(2,3)` winding as charge/spin carrier; `Z = 1/α ≈ 137` as the atomic-number sound barrier; `α⁻¹` as a numeric constant) or a Q1 banner. The ch01 slices — the ones that carry the electron-identity leaves — are listed in the coverage note above if still pending; their result is the one that matters for the F-row ledger.
4. **Top sync debts (first-hand, all un-propagated to print):** §2.1.

### §0.1 — Top five sync debts

| # | debt | print sites | KB truth (leaf) | why it matters | class |
|---|---|---|---|---|---|
| 1 | **Mass-sector ruling (2026-06-20, Grant-ratified) not in print.** "Mass is the stored inductive energy required to maintain the topological integrity of the standing wave" and the chapter-summary bullet "Inertial mass … is derived classically from distributed continuous inductance" stand flat. | `01_topological_matter.tex:35`, `:266` | `newtonian-inertia-as-lenz.md:14` — *"STORED INDUCTIVE ENERGY = the FLYWHEEL … the REST MASS store is A1"*; the ruling is propagated to **six** KB sites (`common-mode-twist-ledger.md:45-52` lists them) and to **zero** vol2 print sites (grep `flywheel\|A_1 (mass\|depression)` over non-comment vol2 TeX: only the ch04 spin-flywheel language, which is compatible). Print `01:168` (hollow-vortex section, 2026-07) already says the $A_1$ mass core — so print is also internally split. | A ratified physics ruling the leaf carries and the book contradicts. | WB-LAG · HIGH |
| 2 | **Δc_crit three-way identity carve (2026-08-24, Grant "proceed") not in print at either twin.** Print asserts "$\Delta c_{crit} = 3$ is simultaneously the K4 lattice connectivity, the trefoil crossing number, and the number of Cosserat sectors … *because* the K4 lattice is 3-connected" (ch03) and "which is simultaneously the trefoil crossing number" (ch06). | `03_neutrino_sector.tex:148-160` (all three legs + the *because* sentence), `06_electroweak_and_higgs.tex:363-366` (leg 2) | `chiral-screening.md:28-48` — leg 2 *"ASSERTED — and in tension with canon"*, leg 3 *"FAILS the counterfactual"*. | The revalidation already named `06:363-365` SUPERSEDED (F8); the ch03 twin is new and carries the strongest form. | WB-LAG · HIGH |
| 3 | **Neutrino body-topology has no KB leaf home, and the obsolete framing survives in a leaf and in print.** The 2026-05-06 corrigendum (closed-loop "twisted unknot" → torsional screw dislocation, open helix) lives only on `ch03-neutrino-sector/index.md:13` (an index — derived) and in print `03:13-15`; **no ch03 leaf and no claim-quality entry carries the screw-dislocation framing** (grep `screw\|open helix\|closed loop` over ch03 leaves and `clm-rji99i`: 0 hits). Meanwhile `regime-classification.md:15` (a leaf) still says **Twisted unknot** unbannered. | `01_topological_matter.tex:207` (regime table), `frontmatter/00_title.tex:18` ("neutrinos as dispersive twisted $0_1$ unknots"), `03_neutrino_sector.tex:272,274` (chapter summary — the `03:19` note covers only the Faddeev-Skyrme section) | `regime-classification.md:15` (stale, unbannered); the canonical framing is homeless at leaf level. | KB-INTERNAL + STALE-KB + WB-LAG in one cluster; needs a word on where the canonical leaf lives before any banner is written. | KB-INTERNAL · HIGH |
| 4 | **Proton mass-ratio headline prints the CODATA value as the derived value.** "precise derivation of the proton-to-electron mass ratio ($1836.15$)", "$m_p/m_e \approx 1836.15$ emerges dynamically as the exact eigenvalue", "The exact proton to electron mass ratio ($1836.15$) is derived"; the title page prints $\approx 1836.14$. Print's own equation (`02:264`) gives **1836.12**. | `02_baryon_sector.tex:7`, `:60`, `:463`; `frontmatter/00_title.tex:18` | `proton-identification.md:13` *"$m_p/m_e = 1836.12$ is derived with zero baryon-data-tuned parameters"*; `:73` D1 headline-fork ruling (2026-07-13, Grant option 2): the headline is the **+0.74 % bare-topology** result, the $-0.002\%$ is $\delta_{th}$-riding. `02:463` already carries the D1 "1-residual" wording but not the number. | Three headline sentences and the title page mis-state the framework's own number and posture. | CONTRA · MEDIUM |
| 5 | **θ-fork ruling (2026-08-23, Grant rulings (a)+(b)) not in print.** "generates a discrete CP-violating $\theta$-vacuum phase" and "trapped vacuum" stand flat. | `02_baryon_sector.tex:319`, `:327`, `:330` | `topological-fractionalization.md:50-76` — θ is the $\mathcal{J}$-dressing, not a vacuum angle; *"The 'CP-violating' adjective is UNDERIVED — and its opposite is asserted elsewhere"*; CP-parity of the dressing OPEN. | A three-week-old Grant ruling on a load-bearing adjective, absent from the printed chapter. | WB-LAG · MEDIUM |

**Runners-up (reader-reported, first-hand spot-checked where marked):** Higgs breathing-mode mechanism demoted R40-B2a in the **sidecar only** — neither `higgs-mass.md`/`higgs-mechanism.md` nor print `06:808-834` carries the stamp (first-hand: `vol2/claim-quality.md:1710-1720` names the `:162` row; no leaf hit for the banner) · Beryllium 9.32 eV "entirely free of empirical parameters" at `07:277` with the walk-back only in a `%` comment (`07:282-295`) while the KB has 9.28 eV in `hierarchical-cascade-correction.md:54` · Boron 9.4 eV (`07:324`) vs KB 8.30 / 8.065 eV · Lithium 2s/2p l-degeneracy break with opposite sign to `orbital-penetration-penalties.md:39` (`07:224`) · ch05 `weak-coupling.md` lagging the 2026-07-02 print re-anchor (STALE-KB, leaf lags print) · gauge-invariance summary bullet `05:175` and objectivebox `05:8` un-rescoped after R43 (c) · struck ppm labels surviving in `q-g20f-vacuum-polarization.md:97`, `q-g27-muon-cosserat-saliency.md:80`, `ch06 index.md:36` (KB-internal, after the 2026-08-03 strike) · `proton-neutron-mass-split.md:10` "accounts for" (leaf lags the 2026-06-15 print correction — STALE-KB, mechanical).

---

## §1 — TeX file ↔ KB leaf map

Legend: **verbatim-match** twin · **partial** (leaf is a translation but has diverged / been bannered beyond print) · **diverged** · **tex-only** · **kb-only** (research-origin leaf, no print twin). Chapter → KB directory: ch01 → `particle-physics/ch01-topological-matter` (20 leaves, 15 of them research-origin) · ch02 → `ch02-baryon-sector` · ch03 → `ch03-neutrino-sector` · ch04 → `ch04-quantum-spin` (+ `appendices/app-b-paradoxes/spin-half-paradox.md`) · ch05 → `ch05-electroweak-mechanics` · ch06 → `ch06-electroweak-higgs` · ch07 → `quantum-orbitals/ch07-quantum-mechanics` (29 leaves) · ch08 → `nuclear-field/ch08-planck-string` · ch09 → `proofs-computation/ch09-computational-proof` (+ `appendices/app-d`) · ch10 → `nuclear-field/ch10-open-problems` · ch11 → `proofs-computation/ch11-overdrive` · ch12 (both files) → `nuclear-field/ch12-millennium-prizes` (+ `appendices/app-c`) · `main.tex`/`_manifest.tex`/`00_title.tex` → no leaf (the vol2 appendices in `ave-kb/vol2/appendices/` source from `backmatter/01_appendices_lean.tex` and `common/translation_*.tex`, outside `vol_2_subatomic/`).


### ch01-A

| TeX range | heading | KB leaf | status | note |
|---|---|---|---|---|
| 5-13 | objectivebox + chapter opening ('matter is not a substance distinct from the va… | index.md:13 (DERIVED index, no leaf twin) | partial | Index prose tracks the chapter opening and already carries the running-coupling 'sketch/open problem' fence. Objective bullet 2 (01:8) repeats the inductance=mass framing the newtonian-inertia leaf re-scoped 2026-06-20 … |
| 15-30 | \section{The Mathematical Topology of Mass} | mathematical-topology-of-mass.md:8-32 | partial | Body is a byte-level translation match (both resultboxes, both surrounding paragraphs). Leaf carries TWO scope notes print lacks: :20 peer-with-standard/finiteness note and :30 the real-space/phase-space Hopf-charge fen… |
| 32-35 | \section{Newtonian Inertia as Macroscopic Lenz's Law} | newtonian-inertia-as-lenz.md:10-12 (+ banner :14) | diverged | Body verbatim-identical; leaf :14 carries a dated Grant-ratified 🔴 Rule-12 re-scope (2026-06-20) that print does not carry in any form (not even a % comment). Highest-value finding in the slice (M1). |
| 37-40 | \section{The Electron: The Fundamental Unknot ($0_1$)} — identity paragraphs | electron-unknot.md:11-13; electron-identification.md §1 :26… | partial | 01:38-40 matches electron-unknot.md:11-13. Print carries the g=2 / spin-half import relabel (2026-06-21 KB banner) as a printed scope carve at 01:64-80 — DISCLOSED, honest. Print does NOT carry the leaf's second 2026-06… |
| 42-63 | % DE-CLAIM 2026-08-02 comment block (NOT PRINTED) | electron-identification.md:92 + l3-electron-soliton-synthes… | tex-only | Comment-only, but the printed scope carve at 64-80 restates its content in print, so this is NOT a disclosed-only-in-comment case. The comment's repaired cite (translation-circuit.md:767) is itself dead at HEAD — M10. |
| 64-80 | \paragraph{Scope carve for the gyromagnetic value and for spin-half (2026-08-02… | electron-identification.md:92 ($g=2$ row) + :89-90 ([SPIN-H… | verbatim-match | Print carries the KB's 2026-06-21/2026-07-08 demotions faithfully (POSITED / structure-vs-selection / proton-neutron falsifier) and cites the leaf. Already-known item '01:40-80 g=2 de-claim' confirmed CLOSED and print-v… |
| 82-111 | \paragraph{Substrate-native identity (canonical 2026-05-15).} + Engine implemen… | (none in ch01 slice) | tex-only | M/Q/J boundary-observable triplet and the v14 breathing-soliton seed status have no twin in any assigned ch01 leaf. Not debt. Note the adjacent pair 01:97 ($\mathcal{J}_{electron}=1/2$) vs 01:111 (seed gives $\mathcal{J… |
| 113-121 | examplebox: Calculating the Fundamental Unknot Circumference | electron-unknot.md:15-31 | verbatim-match | Identical problem/solution/numbers ($\ell_{node}\approx3.86\times10^{-13}$ m). |
| 123-141 | \subsection{Resolution of the Electrostatic Point-Charge Singularity} | electron-unknot.md:33-53 | verbatim-match | Full parity including $U_{AVE}=1.0\,m_ec^2$ resultbox and the $\approx\frac{\alpha}{2}m_ec^2$ Regime-I remark. |
| 143-148 | \subsection{The Dielectric Ropelength Limit} | electron-unknot.md:55-59 | verbatim-match | Identical. (Its $d\equiv1\ell_{node}$ is one side of the acknowledged-open tube-geometry fork — M15.) |
| 150-167 | \subsection{The Hollow-Vortex Binding Structure (Class-C Consistency)} | hollow-vortex-binding.md:39-69 + §3 :116-152 | verbatim-match | Best-synced section in the slice. All four checked values agree: $\sigma=0.18712$, $R^*\approx1.6\,\ell_{node}$ (band 1.34-1.85), robust band $[0.59,3.58]$, $\Gamma\approx0.775$; all THREE honesty scopings (import-by-id… |
| 169-179 | \subsection{Deriving the Running Coupling Constant} | electron-unknot.md:61-73 | verbatim-match | Print carries the sketch/open-problem fence and cites clm-h9aqmt, matching the leaf and the claim-quality non-claims. 2026-09-06 scan candidate 01:170 reads CLOSED at HEAD. |
| 181-193 | figures: electron_3d_knot.png + electron_lattice_net_S.png captions | electron-identification.md:39-41 (same figure + caption) | partial | 01:191 caption matches the leaf's figure caption (19 wall nodes at yield, $\Gamma=-1$ TIR cage, meridian doorway) — fence-excluded surviving localizer. 01:189 'topological winding number ($N=1$) derives the origin of in… |
| 195-214 | \section{Regime Classification of Topological Matter} | regime-classification.md:8-19 | diverged | Header paragraph verbatim. TWO row-level problems: neutrino row identical on both sides and both superseded by the 2026-05-06 corrigendum (M3 print / M4 leaf); proton row diverged, with the LEAF stale relative to print … |
| 216-239 | \section{The Torus Knot Phase Winding Ladder} | torus-knot-ladder.md:8-27 | partial | Print carries the 2026-06-19 dimensional-provenance relabel, the 2026-06-19 stale-value alignment, the $S=0$ $N/\Delta$ SCOPE FLAG and the cold-vs-thermal flag — all DISCLOSED. Two residues: table cells still print $\el… |
| 241-261 | \section{Chirality and Antimatter Disintegration} | chirality-and-antimatter.md:8-28 | diverged | Three divergences: 01:242 RH-unknot label vs the leaf's 2026-07-09 R1 canonical LH-Beltrami relabel (M6); 01:248 'Hopfion' where the leaf says '$0_1$ unknot' (M7); leaf :28 peer-not-chord tag has no print twin (M14). Pr… |
| 257-261 | figure: photon_helical_spin.png caption (Spin-1 Helical Confinement) | electron-identification.md:64 (genesis closed-negative) | tex-only | No KB twin. The caption sells a formation route ('physical derivation of confined point-particles via continuum wave-crashing') that the KB grades closed-negative — the slice's one live-wrong corpse site (M8). |
| 263-273 | \section*{Chapter Summary} + \section*{Exercises} | (none) | tex-only | Summary bullet 2 restates Lenz-inertia — that half stays correct under the 2026-06-20 banner ('the Lenz's-law inertia/back-EMF mechanism stays correct'), so it is NOT counted as a second WB-LAG site. Exercise 2 correctl… |

KB-only leaves (no print twin):
- `mass-closure-theorem.md` — No TeX twin section anywhere in ch01 (no 'mass-closure' / '$mc^2 = E_reactive$' string in the chapter). Research-origin derived-theorem leaf carrying four dated banners (2026-06-24 closure scoping, 2…
- `electron-identification.md` — Canonical 4-property hub with no verbatim TeX twin section; it FEEDS print at 01:38-40 (identity), 01:64-80 (the printed scope carve cites it) and 01:191 (same figure). Answering slice question (g): …
- `index.md` — DERIVED index (kind: index), not a sync source of truth. Read in full for corpse exposure: its blurbs are honest (common-mode-twist-ledger blurb names the SUPERSEDED additive premise and the OPEN ite…
- ` not read in full)` — Nine further leaves live in ch01-topological-matter/ and were NOT in the slice: common-mode-twist-ledger.md, electron-bound-resonator-coverage.md, electron-unknot-cosserat-seeder.md, finkelstein-misn…

### ch01-B — **NO READ (slice did not return)**

### ch01-C

| TeX range | heading | KB leaf | status | note |
|---|---|---|---|---|
| 5-11 | objectivebox (chapter objectives) | newtonian-inertia-as-lenz.md | diverged | Objective 2 ('mass emerges macroscopically from the continuous distributed inductance of closed optical loops (Lenz's Law)') is the inductive-store framing that newtonian-inertia-as-lenz.md:14's dated 2026-06-20 Rule-12… |
| 15-30 | \section{The Mathematical Topology of Mass} | mathematical-topology-of-mass.md | partial | Name-level mapping only — that leaf is NOT in this slice's read set, so no grade is asserted. Faddeev-Skyrme functional + Hopf-charge resultboxes. |
| 32-35 | \section{Newtonian Inertia as Macroscopic Lenz's Law} | newtonian-inertia-as-lenz.md | diverged | TeX 01:33 and 01:35 are BYTE-VERBATIM twins of leaf :10 and :12 (only LaTeX quote glyphs differ). The leaf's Rule-12 banner at :14 sits immediately under that preserved body; the TeX carries no counterpart. Primary WB-L… |
| 37-40 | \section{The Electron: The Fundamental Unknot ($0_1$)} | electron-unknot.md + electron-identification.md | partial | Leaves outside this slice's read set (mapped, not graded). In-slice bearing: 01:40 carries the '$\ell_{node}$ circumference / $\ell_{node}/(2\pi)$ tube radius' geometry that common-mode-twist-ledger.md:232-237 flags as … |
| 42-63 | % DE-CLAIM 2026-08-02 comment block | electron-identification.md | partial | COMMENT-ONLY (not printed) — but its content IS also printed at 01:64-80, so the comment is a provenance trail, not a comment-only disclosure. No DISCLOSED-ONLY-IN-COMMENT finding here. |
| 64-80 | \paragraph{Scope carve for the gyromagnetic value and for spin-half (2026-08-02… | finkelstein-misner-spin-half-derivation.md:14,:106 + spin-g… | verbatim-match | CONFIRMED PRINT-VISIBLE (non-comment \paragraph in the LaTeX body). STRUCTURE-derived / SELECTION-imported split, PEER-WITH-SM and [SPIN-HALF-POSITED] all match the three KB sites. The 2026-08-02 g=2 / spin-half de-clai… |
| 82-111 | \paragraph{Substrate-native identity (canonical 2026-05-15).} | boundary-observables-m-q-j.md | partial | Leaves outside slice read set. 01:109 'v14 breathing-soliton seed' is the only engine-version string in the chapter (see corpse pass). |
| 113-121 | examplebox (Fundamental Unknot Circumference) | electron-unknot.md:19,:22,:28 | partial | common-mode-twist-ledger.md:222 quotes exactly this $E=T_{max,g}/C_{loop}$ law from electron-unknot.md as 'Branch B's strongest anchor' inside an OPEN fork; the TeX prints it flatly as a proof ('proving it is the geomet… |
| 123-143 | \subsection{Resolution of the Electrostatic Point-Charge Singularity} | electron-unknot.md | partial | Mapped, not graded (leaf outside slice read set). |
| 145-148 | \subsection{The Dielectric Ropelength Limit} | electron-unknot.md:59 | diverged | TeX 01:148 is the verbatim twin of electron-unknot.md:59 ('$d \equiv 1 l_{node}$' floor + ropelength $2\pi$). common-mode-twist-ledger.md:232-237 and fence 8 (:334) record that this is INCOMPATIBLE with the :13 geometry… |
| 150-167 | \subsection{The Hollow-Vortex Binding Structure (Class-C Consistency)} | hollow-vortex-binding.md | partial | Leaf outside slice read set. Print carries its own three honesty scopings inline at 01:167 (σ imported-by-interface-identity, R* dimensionally forced, form-consistency-not-chord) — self-disclosing. |
| 169-179 | \subsection{Deriving the Running Coupling Constant} |  claim-quality.md clm-h9aqmt:18,:21 | verbatim-match | 01:170 prints the 'sketch / open problem' honesty scoping and cites clm-h9aqmt; clm-h9aqmt:18 and :21 carry the same non-claim text. The 2026-09-06 S4a candidate 01:170 reads DISCHARGED at HEAD. Anchor \kbleaf{ave-kb/vo… |
| 195-214 | \section{Regime Classification of Topological Matter} | regime-classification.md | partial | Mapped, not graded (leaf outside slice). Row 'Neutrino ($\nu$) \| Twisted unknot' is consistent with torus-knot-uniqueness.md:116 ('geometrically a $0_1$ unknot screw defect'); proton row '(2,5) phase portrait / $6^3_2$… |
| 216-239 | \section{The Torus Knot Phase Winding Ladder} | torus-knot-ladder.md (primary) + torus-knot-uniqueness.md (… | partial | In-slice check: torus-knot-uniqueness.md:114 item (a) RETRACTS muon=(2,5). TeX 01 contains ZERO occurrences of 'muon' (grep -c = 0) and its only (2,5) uses are proton (01:209,:228,:237,:239,:273). TeX 06 has exactly one… |
| 241-261 | \section{Chirality and Antimatter Disintegration} | chirality-and-antimatter.md | partial | Leaf outside slice read set. 01:242 (S4a known) prints the consistency-class scoping and the host-knob screening caveat, matching clm-wcoul2's non-claims (vol4/claim-quality.md:1888,:1890) — reads DISCHARGED at HEAD. |
| 263-268 | \section*{Chapter Summary} | newtonian-inertia-as-lenz.md | diverged | 01:266 restates the superseded inductance = rest-mass-store identification in the summary bullets. See M3. |
| 270-273 | \section*{Exercises} | torus-knot-ladder.md | partial | Exercise 2 (01:273) sells 'higher crossing number drives a more tightly-wound soliton requiring higher localized inductive energy (mass)' — the (2,q) budget ladder, with the phase-space/real-space carve printed inline. … |

KB-only leaves (no print twin):
- `common-mode-twist-ledger.md` — Research-origin leaf (Grant ordering 2026-08-02), NO TeX twin anywhere in vol_2 ch01. Mints clm-cmtwst. Fully self-bannered: §1 SCOPE BLOCK marks the additive ledger SUPERSEDED (canon transduction 20…
- `torus-knot-uniqueness.md` — No dedicated TeX 01 section; TeX 01:216-239 is torus-knot-ladder.md's twin, not this leaf's. Canonical home of the (2,3)-uniqueness derivation; carries the 2026-05-18 FI-13 resolution block (:112-118…
- `finkelstein-misner-spin-half-derivation.md` — No TeX twin section. Print's only trace is the 01:64-80 scope carve, which correctly reproduces the leaf's STRUCTURE/SELECTION split. §6.5 (photons do not inherit 4π) and §7 (4π-vs-SI 'plausibility-s…
- `spin-gyroscopic-isomorphism.md` — Near-kb-only: TeX 01:40's 'gyroscopic precession' clause is its only print echo. The leaf's two guards (gyro≡Bloch is PEER-WITH-SM not an AVE-distinct chord; 'macroscopic' is a term of art meaning ~ℓ…
- `q-g18-schwinger-pair-wkb.md` — Fully kb-only w.r.t. ch01: no Schwinger / pair-production content is printed anywhere in 01_topological_matter.tex. clm-lj4ok5 is graded solidity 0.40 'do not build on, rework needed' (claim-quality.…

### ch02

| TeX range | heading | KB leaf | status | note |
|---|---|---|---|---|
| 1-10 | objectivebox (chapter head) | (none) | tex-only | :7 headlines 'precise derivation ... ($1836.15$)' -- see M9. |
| 12-26 | A-034 nuclear-scale instance paragraph | (none) | tex-only | No ch02 KB twin; cross-refs Vol 3 / backmatter. |
| 28-41 | \section Borromean Confinement: Deriving the Strong Force (intro, fig borromean… | (none at HEAD) | tex-only | index.md:33 (derived) says topological-fractionalization.md covers 'Borromean confinement; scale paradox' but that leaf carries only the Witten section at HEAD. :36 % comment + :37 corrected caption in sync with KB (1-r… |
| 43-56 | \subsection The Topological Scaling Ansatz | (none; index.md:17 Key Results row only) | tex-only | :45 INVARIANT-N1 % comment; print reads 'substrate lattice' (corrected). |
| 58-65 | \section The Proton Mass: The Dynamic Tensor Deficit | (none; index.md:18 Key Results row only) | tex-only | :60 'emerges dynamically as the exact eigenvalue' -- see M8. |
| 67-76 | \subsection The Faddeev-Skyrme Coupling Constant (kappa_FS) | thermal-softening.md:42-52 | verbatim-match |  |
| 78-131 | \subsection Thermal Lattice Softening (delta_th) [sec:thermal_softening] | thermal-softening.md:9-40 | partial | :92 refreshed cold triplet == leaf :11 (MR-board 02:81 RESOLVED; Rule-12 prior triplet preserved only in % comment :81-91). :118-126 nu_Hill == leaf :25 (MR-board 02:92 RESOLVED; prior wording only in % comment :103-117… |
| 133-153 | figure thermal_skyrmion_comparison | (none) | tex-only | Caption :151 refreshed and discloses stale artwork in print; % comment :136-150 flag-don't-fix on PNG regeneration. |
| 155-165 | \subsection The 3D Orthogonal Tensor Trace (I_tensor) | thermal-softening.md:54-66 | verbatim-match |  |
| 167-179 | \subsection Computational Proof: Skew-Lines and The Toroidal Halo | thermal-softening.md:68-80 | verbatim-match |  |
| 181-220 | \subsection The Self-Consistent Mass Oscillator (The Structural Eigenvalue) [1s… | thermal-softening.md:82-122 | verbatim-match | Opener :182 ('total saturated volume V_total of the toroidal halo') has no KB twin sentence and is retired 8 lines later at :190 (disclosed by proximity). Duplicate subsection title with :237 (already flagged at self-co… |
| 222-235 | \subsection The Cinquefoil Confinement Bound | self-consistent-mass-oscillator.md:12-26 | partial | Print carries the 2026-06-08 dimensionless-r_opt relabel inline (:228/:231/:235, cites proton-identification.md S1 property 3 = :23 LIVE); leaf carries it as banners :18/:26. Same physics; scan 02:235 NOT debt. |
| 237-268 | \subsection The Self-Consistent Mass Oscillator (The Structural Eigenvalue) [2n… | self-consistent-mass-oscillator.md:28-64 (+ proton-identifi… | verbatim-match | :268 honesty scoping printed; cites proton-identification.md load-bearing finding = :13 LIVE (scan 02:268 NOT debt). :238 'derived in Chapter 2' cross-ref mirrored verbatim at leaf :30 -- see M14. |
| 270-275 | figure mass_oscillator_flowchart | (none) | tex-only |  |
| 277-316 | \section The Baryon Resonance Spectrum: The Torus Knot Ladder | torus-knot-ladder-baryons.md:9-49 | partial | :279-305 verbatim; table rows c=5..13 agree; c=15 row diverged (M10); :307 Feature 3 rewritten vs leaf :47 (both post-walk-back, same substance); :309 printed dated scope correction in sync with leaf :11/:41; caption :3… |
| 318-340 | \section Topological Fractionalization: The Origin of Quarks | topological-fractionalization.md:8-45 | partial | Body verbatim-match. Leaf :50-76 (2026-08-23 theta-fork dated note) and :78-88 (two-ontology reconciliation clm-w8jn3q, 2026-06-23) have no print twin -- see M1. |
| 342-352 | commented-out figure borromean_weyl_bridge | (none) | tex-only | Float commented out (missing PNG), disclosed in % comment; nothing printed. |
| 354-364 | \section Neutron Decay: The Threading Instability | proton-neutron-mass-split.md:8-10 (+ neutron-identification… | diverged | Print :357/:362 corrected 2026-06-15 (LF-03, % comment :356) to consistent-with-not-derived; leaf twin :10 still 'accounts for' (M2); cited anchor neutron-identification.md:52 is now the heading, content at :54 (M3); le… |
| 366-398 | \section The Helium-4 Nucleus (Mass-Stiffened Strong Force; Elastic Displacemen… | proton-neutron-mass-split.md:12-44 | verbatim-match | TeX-internal value drift mirrored verbatim in leaf: :376 '389.2 N' vs :382 '390.5 N' (flag-don't-fix). |
| 400-402 | \subsection Spacetime Circuit Analysis: The Quadrupole Oscillator | proton-neutron-mass-split.md:46-48 | verbatim-match |  |
| 404-414 | \subsection Simulation of Topological Core Gradients + figure tensor_halo | (none) | tex-only | :406 INVARIANT-N1 % comment; print reads 'chiral LC network' (corrected). :407 '1.955 fm' vs :386 '1.933 fm' TeX-internal drift (flag-don't-fix). |
| 416-457 | \subsection The Hierarchy Bridge: Unifying the Strong Force and Gravity | proton-neutron-mass-split.md:50-89 | verbatim-match | Both sides carry the 2026-06-15 A.1 corrections (print :427/:449 corrected, prior wording in % comments :426/:448 only; leaf :60/:82 banners). Leaf :91-95 (z_0 coordination note, 2026-06-08) kb-only, not contradicted. |
| 459-467 | \section* Chapter Summary | (none; index.md:11 is the derived analogue) | tex-only | :463 'exact ... ($1836.15$) is derived' (M7); :466 'strictly resolved' (M13). % comments :462/:465 not printed; printed bullets carry the corrected zero-parameter / algebraic-substitution wording. |
| 469-472 | \section* Exercises | (none) | tex-only |  |

KB-only leaves (no print twin):
- `proton-identification.md (full leaf)` — Research-origin canonical hub, no TeX section twin; cited from TeX :235 (S1 property 3 = :23 LIVE) and :268 (load-bearing finding = :13 LIVE). Carries the D1 headline-fork ruling 2026-07-13 (:73) and…
- `neutron-identification.md (full leaf)` — Research-origin canonical; cited from TeX :357/:362 as ':52' (content now at :54). Its own TeX anchors (:23 ':294', :25 ':299', :64 ':294,299', :114 ':292-301') are dead at HEAD (content at :357/:362…
- `quark-flavors.md` — GAP stub; no TeX twin; points to topological-fractionalization.md.
- `topological-fractionalization.md:50-88` — 2026-08-23 theta-fork dated note (theta = J-dressing, 'CP-violating' UNDERIVED, import status sharpened) + Two-Ontology Reconciliation (clm-w8jn3q, Grant-ratified 2026-06-23) -- no print twin; the fi…
- `torus-knot-ladder-baryons.md:31-35, :49` — c=17/19/21 rows, 2026-05-18 precision summary, and the 2026-05-18 stale-framing correction have no print twin (print table stops at c=15; Exercise :471 asks the reader to compute c=17).
- `proton-neutron-mass-split.md:91-95` — 'Force-dilution counts against the coordination z_0, not the impedance Z_0 (2026-06-08)' -- kb-only consistency-class note; not contradicted by print.
- `index.md` — DERIVED (not source of truth). :33 blurb says topological-fractionalization.md covers Borromean confinement / scale paradox / scaling ansatz / FS proton energy -- at HEAD that leaf carries only the W…

### ch03

| TeX range | heading | KB leaf | status | note |
|---|---|---|---|---|
| 1-15 | Objectivebox + chapter intro + 2026-05-06 corrigendum | index.md | verbatim-match | Objectivebox (7) and intro (15) already use the corrected open-helix/screw-dislocation framing; the printed corrigendum at :13 matches index.md:13 nearly verbatim (both dated 2026-05-06, same content). |
| 17-39 | Section 1: Mass Without Charge -- Faddeev-Skyrme Argument (Historical/Transitio… | (none) | tex-only | No ch03 KB leaf translates this section. It is explicitly self-bannered as historical/superseded at TeX:19, consistent with the chapter corrigendum. No leaf needed since it's disclosed non-canonical content. |
| 41-97 | Section 2: The Chiral Exclusion Principle (Parity Violation) | (none) | tex-only | No dedicated leaf exists for the chiral-dispersion/parity-violation derivation itself (chiral-screening.md is a different section -- PMNS Step 1). All four Rule-12-flagged sites in this section (figures/examplebox at :6… |
| 99-123 | Section 3: The Neutrino Mass Eigenvalue + flavor-splitting table | (none dedicated; summarized only in index.md Key Results ta… | tex-only | Mass formula and value (0.024 eV, sum 0.054 eV) appear in index.md's Key Results table but this derivation section has no dedicated leaf; clm-rji99i in claim-quality.md covers it at the claim-quality (derived) level onl… |
| 125-135 | Section 4: Neutrino Oscillation -- Dispersive Beat Frequencies | (none) | tex-only | No leaf translation for the beat-frequency wave-packet section. |
| 141-160 | Section 5 Step 1: Chiral Screening Threshold | chiral-screening.md | diverged | Core formula and threshold match verbatim, but the leaf carries a dated (2026-08-24) 🔴 carve demoting 2 of the 3 identity legs that TeX still states flatly -- see mismatch M4. |
| 161-196 | Section 5 Step 2: Regime Boundary Eigenvalues in Mode Space | pmns-eigenvalues.md | verbatim-match | All three regime derivations (compliance/impedance-matched/screened) and their sin^2(theta) formulas match verbatim. |
| 198-211 | Section 5 Step 3: Perturbative Junction Corrections | pmns-junction-model.md | verbatim-match | Resultbox and all three mixing-angle formulas match verbatim, including the factor-of-2 explanation. |
| 213-231 | Section 5 Step 4: CP-Violating Phase | delta-cp-violation.md (top, Step 4 section) | diverged | delta_CP formula and items 2-3 match verbatim; item 1's physical-meaning wording diverges -- TeX retains stale '0_1 unknot phase winding' language the leaf has already corrected. See mismatch M1. |
| 232-268 | Section 5 Step 5: Results and Comparison + Mass Hierarchy | delta-cp-violation.md (bottom, Step 5 section) | diverged | All four numeric PMNS values and the mass-hierarchy ratios match verbatim (see notes, item c). TeX:250's 'derive from three inputs / no curve fitting' framing diverges from the leaf's dated 2026-05-17 Scope Correction d… |
| 270-276 | Chapter Summary | index.md (overview paragraph) | diverged | Bullets 2 and 4 are consistent with index.md's corrected description; bullets 1 and 3 revert to the superseded '0_1 twisted unknot' framing despite the chapter's own corrigendum 259 lines earlier. See mismatches M2, M3. |
| 278-281 | Exercises | (none) | tex-only | No leaf translation expected for exercise prompts. |

KB-only leaves (no print twin):
- `neutrino-translation-table.md` — Self-flagged GAP stub: leaf says TeX references \input{../common/translation_neutrino.tex} at 'approximately lines 260-274' and that file doesn't exist on disk. Verified against the full 281-line cur…

### ch04

| TeX range | heading | KB leaf | status | note |
|---|---|---|---|---|
| 1-10 | \chapter{Quantum Spin as Classical Gyroscopic Precession} + objectivebox | index.md:9-11 | partial | index.md is DERIVED (kind: index), not a leaf. Blurb paraphrases the objectives; TeX:6 says 'Define Quantum Spin ... structurally as' whereas index:11 says 'is derived as' (see mismatch M6). |
| 12-15 | \section{Introduction} | spin-as-precession.md:8-12 | verbatim-match | TeX 'Vol 1 Ch~\ref{ch:alpha_golden_torus}' rendered as KB link [Vol 1 Ch 8](../../../vol1/ch8-alpha-golden-torus.md); link target exists at HEAD. |
| 17-21 | \section{Continuous Mechanics of the Spinor Transition} | spin-as-precession.md:14-18 | verbatim-match | Byte-level match of both paragraphs. |
| 23-54 | \subsection{The Larmor Derivation via Topological Gyroscopes} (+ examplebox 43-… | larmor-derivation.md:8-55 | partial | Body verbatim. KB:10 adds a 'per [Vol 1 Ch 8]' cross-link absent from TeX:24. TeX:53 (softened 2026-08-02, commit e947ce4a) and KB:55 carry the same softened sentence; KB:55 additionally preserves the struck 'proving th… |
| 56-68 | \subsection{Visual Equivalence: The Simulation of Spin} (+ figure 59-64) | visual-equivalence.md:8-16 | partial | TeX:57/66/68 match KB:10/12/16 verbatim (KB:14 preserves the struck 'profound mechanical victory' paragraph per Rule 12). The figure environment 59-64 has NO KB twin (leaf omits the figure); its caption at TeX:62 says '… |
| 70-97 | % comment block: 🔴 [SCOPE SOFTENING 2026-08-02 ... FLAG-DON'T-FIX] | larmor-derivation.md:57-67 and visual-equivalence.md:18-24 | diverged | COMMENT-ONLY in TeX (not printed). It is the Rule-12 preservation of the prior :53/:68 wording plus a FLAG-DON'T-FIX block. Its claim-quality line cites (:407-:410, :419) are +1 stale at HEAD (M1) and its FLAG statement… |
| 98-112 | \paragraph{Scope of the equivalence (2026-08-02, per clm-salw2h).} (PRINTED) | larmor-derivation.md:57-67 and visual-equivalence.md:18-24 | verbatim-match | PRINTED dated scope note carrying all three clm-salw2h non-claims + PEER-WITH-SM + solidity 0.70 + \kbleaf{ave-kb/vol2/claim-quality.md}. The KB banners carry the same three limits. The 2026-08-02 disclosure is therefor… |
| 114-119 | \section*{Chapter Summary} | (none; index.md:11 paraphrases bullet 3) | tex-only | Bullet at :118 'formally re-derived as continuous classical torque responses, eliminating standard probability-jump mechanisms' is unsoftened but sits 6 lines after the printed 2026-08-02 scope paragraph; same strength … |
| 121-125 | \section*{Exercises} | (none) | tex-only | No KB twin; no claims beyond the chapter body. |
| (none in ch04) | (KB-only w.r.t. this slice) The Spin-1/2 Paradox | spin-half-paradox.md:8-16 | kb-only | TeX twin is NOT in vol_2_subatomic: grep for 'Spin-1/2 Paradox' / 'Finkelstein-Misner Kink' across manuscript/**/*.tex hits only manuscript/backmatter/01_appendices.tex and manuscript/vol_0_engineering_compendium/chapte… |
| (none) | (KB-only, derived) Ch.4 index | index.md:1-28 | kb-only | Derived index; Key Results table (mu=gamma L, dL/dt, omega_L, Bloch equivalence) matches TeX eqs 27-41 and :66. Carries no banner (see M6). |

KB-only leaves (no print twin):
- `spin-half-paradox.md` — Research/appendix-origin leaf tagged claims: [clm-salw2h]; its TeX twin lives outside vol_2_subatomic (backmatter/01_appendices.tex, vol_0 ch01) so it is KB-only relative to ch04. Carries the 2026-07…
- `index.md` — Derived index (kind: index). No TeX twin beyond paraphrase of objectives/summary.

### ch05

| TeX range | heading | KB leaf | status | note |
|---|---|---|---|---|
| 2-12 | \chapter{Electroweak Mechanics and Gauge Symmetries} + objectivebox | (index.md:9-11 — derived index blurb, not a leaf) | tex-only | Objectivebox bullet :8 'Derive the physical origin of Gauge Invariance (U(1))...' has no leaf twin; index.md:11 paraphrases it without the R43 rescope. See mismatch ch05-M09. |
| 14-18 | \section{Electrodynamics: The Gradient of Topological Phase} | gauge-boson-masses.md:8-12 | verbatim-match | Byte-consistent (only \ell_{node} vs l_{node} glyph difference elsewhere). |
| 19-28 | \subsection{Magnetism as Convective Vorticity} | gauge-boson-masses.md:14-26 | verbatim-match | Cosmetic only: TeX :28 '$\xi_{topo} \equiv e/\ell_{node}$' vs leaf :26 'e/l_{node}'. |
| 30-51 | \subsection{The Inductive Origin of Gauge Invariance} | gauge-boson-masses.md:28-50 (body + 2026-08-03 repair block… | partial | Body :31-35 matches leaf :30-34 verbatim incl. the printed 'This closure holds for time-independent Lambda ONLY (rescoped 2026-08-10 under R43...)'. Print :51 is a condensed premise note + inline SECOND FAILURE note + p… |
| 53-62 | \section{The Weak Interaction: Inductive Cutoff Dynamics} | gauge-boson-masses.md:52-63 | verbatim-match | Leaf :57 bolds 'below' where TeX italicises (declared quote-drift row wall-taxonomy.md:336, PASS). External cites to gauge-boson-masses.md:39 expect the l_c line now at :55 — see ch05-M07. |
| 63-74 | \subsection{Deriving the Gauge Bosons (W/Z) as Evanescent Modes} | gauge-boson-masses.md:65-75 | verbatim-match | Cosmetic: TeX :74 ends 'reduces this stiffness ratio to:' (leads into examplebox); leaf :75 ends 'reduces this stiffness ratio.' (examplebox split into weinberg-angle.md). |
| 76-89 | examplebox [Deriving the Weak Mixing Angle via Isotropic Elasticity] | weinberg-angle.md:8-38 | diverged | Print was corrected 2026-08-02 (post-#840 R3, CRIB-1, comment-only banner at :84): :81 nu_Hill symbol, :83 'trace-reversed operating point ... an averaging choice, not a lattice-emergent limit'. Leaf :20/:26 still carry… |
| 91-115 | \subsection{The Absolute $W$ Boson Mass: Chirality Mismatch Self-Energy} | weak-coupling.md:8-36 | diverged | Print re-anchored the alpha^2 framing 2026-07-02 (commit 23a0ff2d 'L2 electroweak: native re-anchor of α² framing (Grant-ruled, light touch)'): :103 'two Axiom~4 susceptibility couplings' / varactor, :104 resultbox reti… |
| 117-119 | \section{Electroweak Mechanics: Forward Reference} | forward-to-ch6.md:8-10 | verbatim-match | Both promise 'the Schwinger anomalous magnetic moment ($a_e = \alpha/2\pi$) ... presented in full in' ch06 — cross-slice check against the 2026-08-02 ch01 g=2/spin-half de-claim belongs to the ch01/ch06 lanes, not flagg… |
| 122-133 | % FIGURE MISSING (commented-out figure electroweak_acoustic_modes.png) | (none) | tex-only | Comment-only; honest TODO, no KB twin needed. |
| 135-159 | \section{The Gauge Layer} / \subsection{U(1) Electromagnetism from the Lattice … | forward-to-ch6.md:12-40 | verbatim-match | Print :135-159 and leaf :14-40 are byte-consistent with each other; NEITHER carries the R43 (c) rescope that lives in gauge-boson-masses.md:34/:83 and TeX :35/:51. Whether the rescope ('canon holds no valid derivation o… |
| 161-171 | \subsection{SU(3) Color Charge from the Borromean Linkage} | forward-to-ch6.md:42-52 | verbatim-match | Byte-consistent. |
| 173-179 | \section*{Chapter Summary} | (none) | tex-only | Bullets :175 ('Gauge Invariance is explicitly derived...') and :178 ('explicitly proven to map identically') carry no caveat; see ch05-M08 and ch05-M10. |
| 181-184 | \section*{Exercises} | (none) | tex-only | No physics claims beyond the chapter body. |
| 185-247 | % R40 batch-2a --- [NEEDS-RE-DERIVATION status-note heading] (2026-08-11) [comm… | gauge-boson-masses.md:131-204 (printed in-leaf) | partial | TeX carries the R40 arc (Axiom 5 clause G, A_g UNVALUED-RATIFIED-CONSTANT per R48, BIAS-DEBT) as % comment only; the KB leaf prints it. TeX row list carries only the ':51 def-l0ngdu rider' row; KB batch-2a demotes two r… |

### ch06-A

| TeX range | heading | KB leaf | status | note |
|---|---|---|---|---|
| 06:14-29 \section{Reinterpretation of the Higgs Mechanism} | Reinterpretation of the Higgs Mechanism | higgs-mechanism.md:8-27 | verbatim-match | Near word-for-word match. KB leaf carries none of claim-quality.md:162's 2026-08-11 R40-B2a DEMOTED banner for the acoustic-relaxation-mode sentence — see mismatch M1. |
| 06:31-60 \section{The Weak Mixing Angle from the Perpendicular Axis Theorem} | The Weak Mixing Angle from the Perpendicular Axis Theorem | higgs-mechanism.md:29-60 | partial | Derivation verbatim-matches. TeX prints the full OPEN FLAG disclosure box as visible text (06:58); the leaf carries the identical wording only as a hidden HTML comment (54) — see mismatch M7. |
| 06:62-127 \section{The W and Z Boson Masses} (incl. Cosserat length) | The W and Z Boson Masses | spontaneous-symmetry-breaking.md:8-72 | verbatim-match | Tree-level M_W/M_Z derivation matches verbatim. Does not cover TeX's later loop-correction refinement (06:235-269) — see M3. |
| 06:129-138 \section{W and Z Bosons as Dielectric Plasma Arcs} | W and Z Bosons as Dielectric Plasma Arcs | spontaneous-symmetry-breaking.md:74-85 | verbatim-match | Word-for-word match. |
| 06:140-213 \section{The Three-Generation Lepton Spectrum} (Gen 1/2/3 + summary table) | The Three-Generation Lepton Spectrum | lepton-spectrum.md:10-84 | partial | Prose/derivations verbatim-match. Divergences: (a) OPEN FLAG visibility (M7); (b) KB-only corrective arrow-diagram note not propagated to TeX (M5); (c) TeX's own summary table already shows loop-corrected W/Z figures th… |
| 06:215-234 Carrier note (D1 ratification, z=3 srs vs z=4 diamond) | Carrier note (2026-08-02, D1 ratification) | engine-capability-map.md §8b.0 | verbatim-match | Fully printed disclosure (not a comment); both cited anchors verified present and correct. Not one of the 6 assigned ch06 leaves but resolves cleanly — no dead anchor. |
| 06:235-269 Loop Correction + Self-Consistent Back-Saturation (P2.7) | Loop Correction (Impedance Mismatch Loss) / Self-Consistent Back-Saturation | (none found) | tex-only | No leaf in ch06-electroweak-higgs/ hosts this derivation at all; feeds mismatch M3 (headline W/Z values diverge between this TeX content and every KB summary table). |
| 06:271-282 \section{The Neutrino Mass Spectrum} (intro formula) | The Neutrino Mass Spectrum | higgs-mass.md:8-21 | verbatim-match | Formula and 0.024 eV figure match verbatim. |
| 06:283-335 Flavor Splitting via the Bethe-Lattice Ring Eigenvalue | Flavor Splitting via the Bethe-Lattice Ring Eigenvalue | higgs-mass.md:23-34 ("Flavor Splitting via the Torus Knot L… | diverged | Different formula (cos(2π/c) Bethe eigenvalue vs simple 1/c), different per-flavor meV values, and opposite hierarchy-ordering direction for the same three flavors — see mismatch M4. |
| 06:337-447 Mass-Squared Splittings (Goldstone-corrected junction coupling) + Lemma 5 open problem | Mass-Squared Splittings: Goldstone-Corrected Junction Coupling | Lemma-5 content itself | tex-only | The Δc_crit=3 compliance-threshold sub-claim (06:363-365) maps to chiral-screening.md and is diverged/WB-LAG (M2). The surrounding Goldstone-coupling derivation and Lemma 5's open-problem status (three eliminated routes… |
| sm-ave-translation.md:10 (forwarder line-number cite) | SM-AVE Translation forwarder | 06_electroweak_and_higgs.tex line-pointer | diverged | Cites TeX line 305 for the \input{translation_particle_physics.tex}; actual line at HEAD is 860 — dead anchor, M6. |

KB-only leaves (no print twin):
- `lepton-spectrum.md:66-73` — 'Net-α-power reduction note' + relabeled generation-hierarchy arrow diagram (torsion:/bending:/+2nd vertex: labels, p_c/α² for μ→τ, α for τ→W) is KB-only — no twin in TeX. It explicitly 'retires' the…
- `chiral-screening.md:28-48` — The dated 2026-08-24 three-way-identity carve (demoting 'connectivity = trefoil crossing number' to asserted-pending-derivation, and failing 'connectivity = Cosserat sector count' outright) is KB-onl…
- `higgs-mass.md:79-92 (Summary table + 2026-06-15 KB-reconciliation calibration-inputs banner)` — Mostly maps to TeX content past line 450 (out of this slice's range) and is a visible, well-disclosed correction on its own terms (strikethrough + replacement text, not a hidden comment) — noted for …

### ch06-B

| TeX range | heading | KB leaf | status | note |
|---|---|---|---|---|
| 449-484 | \section{Schwinger's Anomalous Magnetic Moment ($g-2$)} | higgs-mass.md:36-77 (clm-stgx1i) | verbatim-match | Line-for-line translation. Only diff: TeX 481 uses \boxed{\frac{\alpha}{2\pi}}; KB :74 prints it unboxed. KB sidecar clm-stgx1i:195 adds an alpha-echo tag (value rides alpha, a calibration input) — not printed, but ruli… |
| 486-556 | \subsection{Toward the Second-Order Correction} (QED expansion, K4 Bethe-tree C… | two-stage), :256 (legacy engine) | partial | TeX 489-510 (QED expansion; C_2^Lattice = S_11[Y_K4] ≈ -0.0094 at 495; K4 Bethe-tree 'Topological Derivation' 509-510) is TEX-ONLY historical framing — DISCLOSED in print by footnote 512 ('Annotation updated 2026-05-13 … |
| 557-604 | \paragraph{Route B substrate derivation (full).} | q-g19a-petermann-saliency-closure.md:24-49 | verbatim-match | Five ingredients + combined equation match verbatim. Both sides carry the 1/pi^2 Delta a_e form (TeX 600 / KB :47) AND the 2/(pi alpha) C_2 form (TeX 603 / KB :48); the leaf's F5 block (:166-179, 2026-08-03) flags these… |
| 606-626 | \paragraph{Numerical robustness (Route B base case, $\delta = 0$).} | q-g19a-petermann-saliency-closure.md:51-61 | partial | Numbers match (-3.916e-3, -0.3416, +4.0%, parity zeros). KB table row :59 Delta a_e^(2) = -9.21e-7 / PDG -8.86e-7 is KB-only (print omits it; leaf F5 :177 flags that row as the un-doubled convention). KB :150-164 F3 (20… |
| 628-653 | \paragraph{Saliency closure ($\delta = -3\alpha/2$).} | q-g19a-petermann-saliency-closure.md:63-85 | verbatim-match | delta^* = -0.01093, delta^*/alpha = -1.4982, boxed delta = -3alpha/2 all match. |
| 655-723 | \paragraph{Final result --- printed-precision match at $C_2$, postulate-conditi… | :14 (two-stage) | partial | Values match: TeX 699 -1.772e-6 / 700 -0.32846 = KB :92; TeX 704 1.15964e-3 vs 1.15965e-3 = KB :209; ppm labels struck on both sides (MR-board 06:564 stale-value RESOLVED at HEAD; Rule-12 trail in % 655-695). TeX 702-70… |
| 725-775 | \paragraph{What still needs derivation (honest open items).} | q-g19a-petermann-saliency-closure.md:218-222 | verbatim-match | RESOLVED NEGATIVE (2026-05-31) bullet printed at 753-769 matches KB :221 (KB additionally keeps the 2026-05-16 'STRUCTURAL CLOSURE ADVANCED' history and the '50-ppm headline' proper-noun back-reference flagged at :200).… |
| 777-783 | \noindent\textbf{Zero parameters were fudged.} + legacy engine superseded | q-g19a-petermann-saliency-closure.md:238-246, :256 | partial | Body sentence matches KB :246; KB :240-244 carries a dated (2026-08-02) Stage-1 scope label that print lacks (mismatch M6, LOW — print 753-769 immediately above already states Stage-2 is postulate-dependent). |
| 785-788 | \section{The Higgs Boson Mass} (intro: lambda and v derived; v_AVE ≈ 248.8 GeV) | (no ch06 leaf) — clm-p7rfkb sidecar :161-163; vol6 lambda-h… | tex-only | No ch06 KB leaf carries this section (higgs-mass.md, despite its name, holds only neutrino/Schwinger/summary; higgs-mechanism.md and spontaneous-symmetry-breaking.md headings do not cover it). v_AVE ≈ 248.8 GeV appears … |
| 790-796 | \subsection{The Fermi Constant from $M_W$ and $\sin^2\theta_W$} | mathematical-closure.md:118 lists the chain G_F <- {M_W, si… | tex-only | No KB twin for the G_F formula. |
| 798-806 | \subsection{The Vacuum Expectation Value (VEV)} | (none) — clm-p7rfkb:161 (VEV <-> Z_0 = 376.73 Ohm) is the o… | tex-only | v_AVE = 1/sqrt(sqrt2 G_F) ≈ 248.8 GeV (+1.1%) has no leaf body; the 376.73 Ohm identification is in the derived sidecar clm-p7rfkb:161 (solidity 0.30). |
| 808-833 | \subsection{The K4 Breathing Mode: $M_H = v/\sqrt{N_{K4}}$} + resultbox + 'Why … | lambda-higgs-derivation.md:22-42 (PATH-STABLE sec:lambda_hi… | partial | Leaf label sec:lambda_higgs_derivation ≠ TeX label sec:higgs_mass_derivation (vol6 leaf, not a ch06 twin). Derivation matches in substance (lambda = 1/8, M_H = v/2); leaf :35 prints ≈124,400 MeV vs TeX 822 124,417 MeV; … |
| 835-853 | \section{Summary of Electroweak Predictions} | higgs-mass.md:79-92 (clm-q8un7j) | partial | TeX table 841-848 has 8 rows; KB table :84-90 has 7 — the TeX 844 row '$M_H$ (Higgs) & 124,417 MeV & 125,100 MeV & $-0.55\%$' has no KB row (TEX-ONLY; git -S shows the row was never in the leaf). TeX 853 prints the CORR… |
| 855-860 | \subsection{Standard Model $\leftrightarrow$ AVE Translation Dictionary} + \inp… | sm-ave-translation.md:8-10 (routing forwarder, no-claim) | partial | Forwarder :8 is label-stable (sec:sm_ave_translation) but :10 cites 'line 305' — the \input is at TeX 860 at HEAD (mismatch M9). TeX 858 'Table~the main text consolidates' is a broken \ref artifact (cosmetic, tex-only). |
| 862-867 | \begin{figure} topology_particle_zoo.png caption | (none) | tex-only | Figure caption only. Caption 'Every mass is computed from $m_e$, $\alpha$, and $G$ with zero Standard Model parameters' is consistent with the corrected 853 sentence. Caption's 'muon: $\sqrt{3/7}$-turn impedance twist' … |

KB-only leaves (no print twin):
- `q-g20f-vacuum-polarization.md` — No TeX twin anywhere in ch06 (grep 'vacuum polarization\|Uehling\|Landau pole' over the whole .tex = 0 hits). Research-origin leaf with its own dated banners (:10 2026-07-03, :22/:37 2026-07-14, :105…
- `q-g27-muon-cosserat-saliency.md` — No TeX twin in ch06 ('502', 'Fermilab', delta_Cosserat = 0 hits in the whole .tex); it cites Vol 2 Ch 6:154-176 (outside this slice). Carries the 2026-05-18 factor-2 walk-back (:14) and the √(3/7) OP…
- ` v_substrate)` — KB-only paragraph with its own 2026-07-04 [CMB-PHASE-EXCLUDED] banner; no print twin in this slice.
- `F8, ppm-STRIKE RULING)` — Audit/ruling blocks with no print twin; their consequences reach print only via % comments 518-535/544-556/655-695/716-719/765-766 (comment-only) plus the executed strike. The :131 cite-integrity not…
- `q-g19a-petermann-saliency-closure.md:224-236 (Falsification predictions table + Falsifier)` — KB-only; :236 Falsifier 'at 50 ppm precision' is a threshold the leaf itself routes (:201) — not inventoried as debt.
- `higgs-mass.md:8-34 (The Neutrino Mass Spectrum; clm-p7rfkb)` — Twin lies outside this slice's TeX range (another lane); listed for completeness of the leaf read.

### ch07-A

| TeX range | heading | KB leaf | status | note |
|---|---|---|---|---|
| 1-11 | objectivebox | de-broglie-standing-wave.md:8-13 | verbatim-match | four bullets identical |
| 13-34 | \section{Deterministic Reinterpretation of the Wavefunction} + \subsection{The … | de-broglie-standing-wave.md:15-42 | verbatim-match | clm-qde5gn |
| 36-43 | \subsection{Transverse Shear vs. Longitudinal Bulk Cavities} | de-broglie-standing-wave.md:44-54 | partial | Both sides carry the printed/bannered R40-B2a DEMOTED stamp (TeX:41 / KB:52) — disclosed. KB:50 adds a 2026-06-11 three-impedance-law note (itself R40-stamped) with no print twin. TeX:41 carries a stray `\gammaundeclare… |
| 45-48 | \subsection{Gravitational Parallax Interferometry} | de-broglie-standing-wave.md:56-60 | diverged | KB writes $n_s = 1 + \tfrac{9}{7}\varepsilon_{11}$ with a dated 2026-05-17 notation note and adds $\Delta\Phi \approx 250$ rad + driver; print writes $n_s = \frac{9}{7}\varepsilon_{11}$ with no number (M1). |
| 50-62 | \section{Orbitals as Acoustic Resonant Cavities} | de-broglie-standing-wave.md:62-70 | verbatim-match | figure replaced by placeholder in KB |
| 64-81 | \subsection{Hydrogen Ground State from LC Impedance Matching} (+ examplebox) | de-broglie-standing-wave.md:72-95 | verbatim-match | $137\times\ell_{node}$ = $a_0=\ell_{node}/\alpha$; not the K4 Q=137 corpse |
| 83-100 | \subsection{Angular Momentum Quantization} | de-broglie-standing-wave.md:97-111 | verbatim-match |  |
| 102-121 | \section{Hydrogen Energy Levels: AVE vs. CODATA} | de-broglie-standing-wave.md:113-124 | verbatim-match |  |
| 123-151 | \subsection{Numerical Verification: ODE Eigenvalue Solver} | ode-verification.md:8-30 | verbatim-match |  |
| 153-162 | \subsection{Dimensional Analysis: $a_0 = \ell_{node}/\alpha$} | ode-verification.md:33-43 | verbatim-match | Known item 07:161: the 2026-06-15 recon note at :161 is a % comment, BUT the Class-B identification caveat is PRINTED at :162 and mirrored at KB:43 — disclosed in print, not comment-only. \kbleaf ch8-alpha-golden-torus.… |
| 164-180 | \subsection{Regime Identification of Atomic Orbitals} | ode-verification.md:45-53 | verbatim-match | twin-consistent, but the table's 'inner core = Regime II (Yield)' conflicts KB-internally with de-broglie-n.md:10 and de-broglie-standing-wave.md:244 (M10) |
| 182-187 | \section{Helium and the Symmetric Topological Cavity} | helium-symmetric-cavity.md:8-12 | verbatim-match |  |
| 189-197 | \subsection{QM $\leftrightarrow$ AVE Translation Dictionary} | qm-ave-translation.md:10-16 | verbatim-match | table body is \input{../common/translation_qm.tex} vs KB pointer to common/translation-tables/translation-qm.md — not diffed (out of slice) |
| 199-206 | \subsection{The Spatial Extent of the $0_1$ Unknot} | helium-symmetric-cavity.md:14-24 | partial | TeX:206 trailing sentence ('The observed $1s$ continuous spatial density $\rho(r)$ is not the unknot structure itself...') absent from KB |
| 208-232 | \subsection{The Mutual Cavity Loading Architecture} + \paragraph{The 3-Phase Ev… | helium-symmetric-cavity.md:26-42 | diverged | KB body is 'The N-Electron Pipeline' (Op1/Op3/Hund, N_s=1.0 / N_p=0.5 via K=2G); TeX body is Phase A (penetration)/B (T^2 loading)/C (buckling) with a Lithium 2s/2p resultbox (TeX:221-231) that has no KB twin and whose … |
| 234-247 | \subsection{Phase C: Transverse Buckling vs. Hopf Strain} | (none) | tex-only | No KB twin (0 hits for Euler/buckl/N_eff=1.5 in ch07 dir). TeX:239 printed R40-B2a DEMOTED stamp; TeX:243 N_eff=1.5 / +72%->-2.6% = known revalidation finding 14 (M3); TeX:245-247 Hund 4α/6α penalties also KB-homeless. |
| 249-256 | Helium 1st Ionization Energy resultbox (24.19 eV, -1.6%) | helium-symmetric-cavity.md:44-50 | verbatim-match | twin-consistent; KB-internal three-way He-IE figure conflict (M9) |
| 258-302 | \subsection{Field-Oriented Control (FOC) and the Secondary Density Wake} | helium-symmetric-cavity.md:52-70 | partial | KB condensed. TeX:277 'Beryllium ... 9.32 eV entirely free of empirical parameters' sentence dropped by KB; TeX:282-295 % HISTORICAL NOTE (comment-only) records that the static 9.32 eV result 'appears to match experimen… |
| 304-309 | \paragraph{The Emission Paradox: "Jumping Up is Going Down".} | (none) | tex-only | no contradiction found |
| 311-333 | \subsection{The $p$-Shell Isomorphism: Orthogonal Inductive Buckling} | helium-symmetric-cavity.md:72-80 | partial | KB condensed and silently drops TeX:324 'Boron ... 9.4 eV' (M5) and TeX:333 'Tier-1 derivation status' (M12); TeX:322 Coplanar/Orthogonal choice list and TeX:329-330 p^6 Neon paragraph condensed/absent |
| 335-354 | \section{The Atom as an Analog Ladder Filter} + \subsection{Screening as Freque… | analog-ladder-filter.md:8-20 | verbatim-match |  |
| 356-389 | \subsection{LC Components of the $1s$ Flux Loop} | analog-ladder-filter.md:22-60 | partial | values identical; TeX:383 carries the printed R40-B2a DEMOTED stamp, KB:52 twin does not (M6) |
| 391-405 | \subsection{Intra-Shell Coupling: Coulomb Capacitance, Not Mutual Inductance} | analog-ladder-filter.md:62-72 | verbatim-match |  |
| 407-446 | \subsection{Multi-Shell Filter Cascade} (+ tcolorbox signal-flow figure, Regime… | analog-ladder-filter.md:74-88 | partial | tcolorbox figure and the 'Regime Validation' resultbox (TeX:444-446) have no KB twin |
| 448-470 | \subsubsection{Explicit S(r) Metric Saturation Derivation} (L_eff, C_eff, k^2_e… | (none) | tex-only | 0 hits for kappa_{Hopf} / Regime-Aware in ch07 dir |
| ≈471-478 | 'This filter framework naturally produces:' bullets | analog-ladder-filter.md:90-94 | verbatim-match |  |
| 480-489 | \subsection{Radial TL Eigenvalue and the Screening Rule} preamble + resultbox{T… | de-broglie-n.md:10 | diverged | print: deep core crosses Regime IV yield for Z>=19; KB: entire atom in linear regime, Z_0=377 everywhere (M7); also TeX-internal vs TeX:938 'deep Regime I' |
| 490-513 | resultbox{De Broglie Refractive Index on the AVE Lattice} + IE = xi_0 R_y | de-broglie-n.md:12-28 | verbatim-match |  |
| 515-553 | \paragraph{The Screening Rule: Two Distinct Physics.} + resultbox{AVE Screening… | screening-rule.md:8-36 | verbatim-match | TeX:536 §\ref{sec:lattice_js2} -> label lives at TeX:3735 (outside slice), KB writes §`sec:lattice_js2` |
| 555-560 | \subsection{Macro-Cavity Saturation} | macro-cavity-saturation.md:8-12 | verbatim-match | 'previous section' -> 'helium section' translation adaptation only |
| 562-567 | \subsubsection{Complete Geometry-to-Solver Pipeline} heading + intro | geometry-pipeline.md:8-10 | verbatim-match | heading/intro only; the KB leaf's Stage A-E body twins TeX:1161-1370 (ch07-B slice), NOT the Step 1/Step 2 text that follows here |
| 569-870 | \paragraph{Step 1: Single-Electron Eigenvalue} (a)-(h) + resultbox{Step 1 Summa… | de-broglie-standing-wave.md:127-240 | partial | KB condenses (drops dimensional checks, the l-degeneracy / 'Why l matters' prose at TeX:823-857). KB:240 adds a Terminology note (mode-count vs topological winding, def-quant3) that print lacks while TeX:725-726 prints … |
| 872-1019 | \paragraph{Step 2: Lattice Strain Between Shells} (a)-(e) | de-broglie-standing-wave.md:242-261 | partial | KB is a summary paragraph + Step 2 Summary resultbox; all quoted values (Z x 2.8e-10, 0.007, Z_0 invariant, 1e-16, lambda_EM >> gap) agree |
| 1020-1053 | \subparagraph{(f) Lattice supercavitation and the $Z = 1/\alpha$ limit.} + \par… | de-broglie-standing-wave.md:246-250 | partial | KB carries c_S = c only. TeX:1036-1053 c_P derivation is tex-only and print-stamped R40-B1 at :1053; its pointer 'dated demotion note at the end of this chapter' resolves to a PRINTED note at TeX:4150-4157 (batch-1) — d… |
| 1055-1100 | Cavitation criterion + Z table + physical interpretation | de-broglie-standing-wave.md:252 | partial | KB condensed; both sides carry Z = 1/alpha = 137 as the sound barrier / max atomic number (not the K4 Q=137 corpse) |

KB-only leaves (no print twin):
- `geometry-pipeline.md (Stages A-E body, :12-73)` — twin is TeX:1161-1370 (ch07-B slice); only the heading/intro (:8-10) twins TeX:562-567
- `atom-as-radial-waveguide.md` — galaxy/planetary/atom enclosed-source table; no twin located in TeX 1-1100 (likely E2b-iii, radial-eigenvalue-solver.md:115 lineage, TeX >1100)
- `bonding-mode-formula.md` — twin at TeX ~1446 (24.37 eV He check) — outside slice
- `complete-solver-architecture.md` — no twin in 1-1100; not located
- `dual-formalism-architecture.md` — E2 summary (Li 5.32 eV) — outside slice
- `knot-vs-orbital-table.md` — outside slice
- `operator-domain-table.md` — outside slice
- `scale-separation.md` — outside slice; carries un-swept 'K = 2G from nu = 2/7, Axiom 2' at :49 (see notes)
- `subshell-junction-scattering.md` — outside slice; carries B IE = 8.30 eV at :11 (used for M5) and un-swept K=2G at :38
- `helium-coupling-first-principles.md` — twin at TeX:3795 (24.37 eV) — outside slice
- `chiral-factor.md` — twin at TeX:3851 ('He IE to 0.008%') — outside slice; used for M9
- `hierarchical-cascade-correction.md` — twin at TeX:3962+ (sec:hierarchical_cascade_correction) — outside slice; used for M4
- `ionization-energy-validation.md` — twin at TeX:4026 — outside slice; still contains raw LaTeX tabular markup (not translated to Markdown); used for M5/M9
- `stepped-impedance-resonator.md` — twin sec:sir_atom TeX:3880 — outside slice; grep-only
- `radial-eigenvalue-solver.md` — 816 lines, E2b-E2k — TeX >1100; grep-only
- `orbital-penetration-penalties.md` — research-origin leaf marked `<!-- leaf: verbatim -->` but no TeX heading twin in 1-1100; duplicated kb-frontmatter block at :4-7 and :9-12 (cosmetic); used for M2
- `q-g20a-lamb-shift-structural-closure.md` — research-origin, no TeX twin in range; grep-only
- `brillouin-zone-uv-cutoff.md` — research-origin, no TeX twin in range; grep-only

### ch07-B — **NO READ (slice did not return)**

### ch07-C

| TeX range | heading | KB leaf | status | note |
|---|---|---|---|---|
| 2250-2387 | (E2d-ii) ABCD transfer matrix cascade (Op1, Op3, Op5, Op6) — continuation from … | radial-eigenvalue-solver.md:284-373 | verbatim-match | Equation labels dropped in KB (normal LaTeX->MD); content verbatim. |
| 2388-2433 | (E2e) Non-penetrating orbits (l >= 1, Problem 4) — eq:centrifugal_barrier, eq:c… | radial-eigenvalue-solver.md:375-399 | verbatim-match | KB 399 drops the '(Eq. sigma_op4)' cross-reference present at TeX 2430; cosmetic. |
| 2434-2493 | Four canonical circuit problems — composition rules (tables + decomposition rul… | radial-eigenvalue-solver.md:401-427 | verbatim-match |  |
| 2494-2600 | (E2f) Graded impedance taper (Axiom 2) — eq:1s_density, eq:smooth_screening, eq… | radial-eigenvalue-solver.md:429-474 | verbatim-match |  |
| 2601-2639 | Lithium Verification (Z=3, 1s^2 2s^1) — 193.28 eV pair, 5.58 eV ABCD, result ta… | radial-eigenvalue-solver.md:476-498 | verbatim-match |  |
| 2640-2710 | (E2g) Two-solver architecture and the 3.5% systematic | radial-eigenvalue-solver.md:500-521 | verbatim-match |  |
| 2711-2737 | resultbox: E2 Summary — Dual-Formalism Architecture (Y->S + ABCD, 'Both are nee… | dual-formalism-architecture.md:8-26 | verbatim-match | Verbatim twin, but the box's Y->S / N-port formalism is declared 'formally superseded' by macro-cavity-saturation.md:10 (TeX 558) with no banner at either site — see mismatch M4. |
| 2739-2857 | (E2h) Lattice fluid mechanics and the coupled-soliton problem — eq:madelung_con… | radial-eigenvalue-solver.md:523-573 | verbatim-match | Checked E2h 'lattice dispersion pressure Q' against the R40-B2a bulk-acoustic-carrier demotion: it is the Bohm-Q term of the same radial ODE, not the bulk-modulus carrier; not flagged, not adjudicated. |
| 2858-2969 | (E2i) Op2 crossing correction for penetrating orbits — eq:op2_cross_shell; 5.32… | radial-eigenvalue-solver.md:575-627 | verbatim-match | KB 579 adds '(clm-9s9apq, via Axiom 3)' where TeX 2872 has '(Axiom~3)'; a cite addition, not a divergence. |
| 2970-3151 | (E2j) Same-shell interactions as coupled transmission lines — eq:coupled_line_z… | radial-eigenvalue-solver.md:629-693 | verbatim-match | KB 651 reads '(Vol. V)' where TeX 3030 reads '(Vol.~V, Ch.~2)' — cosmetic drop of the chapter number. The validation table numbers (Li 5.32/1.2%, Be 8.21/11.9%) are contradicted elsewhere in the chapter — see M5/M6/M7. |
| 3152-3357 | (E2k) Complete phase integral: all operators inside V(r) — parts 1-2 (operator … | radial-eigenvalue-solver.md:695-752 | diverged | Two content divergences: (a) TeX 3288 eq:kappa_hopf carries a '(-1)^{n - l - 1}' parity factor absent from KB 731; (b) TeX 3315-3329 'Hopf link back-EMF' bullet carries the Inductive Drag (+kappa) / Mutual Inductance (-… |
| 3358-3400 | (E2k) 3. Torus knot crossing geometry (eq:intersection_number) + 4. Crossing an… | radial-eigenvalue-solver.md:754-772 | verbatim-match | KB continues (773-816: cos-theta, crossing potential, crossing radius, Approach 24 resultbox) as the twin of TeX 3400-3500 — outside ch07-C. |

KB-only leaves (no print twin):
- `q-g20a-lamb-shift-structural-closure.md` — True KB-only (research-origin): no 'Lamb' heading anywhere in ch07 TeX (only unrelated body hits at 07:43,72,77). Carries dated Rule-12 banner (2026-07-02) at :10 and orthogonality guard (2026-07-05)…
- `brillouin-zone-uv-cutoff.md` — True KB-only (research-origin, engine-capability class): no 'Brillouin' in ch07 TeX. Carries dated Rule-12 banner (2026-07-03) at :11-19 and a flag-don't-fix drift note at :100-108.
- `orbital-penetration-penalties.md` — Marked '<!-- leaf: verbatim -->' but no 'Orbital Penetration' heading found anywhere in ch07 TeX; twin unlocated (possibly another chapter). Also carries a duplicated kb-frontmatter block (:4-7 and :…
- `de-broglie-standing-wave.md` — Twin TeX 07:13-~260 (ch07-A, outside my range). Carries R40-B2a DEMOTED banners (2026-08-11) at :50,:52 and the dated re-derivation note :267-339; K6 fence-excluded terminology note at :240.
- `ode-verification.md` — Twin TeX 07:123 (ch07-A). Carries the KB-reconciliation 2026-06-15 banner at :43 whose print twin is the known %-comment-only note at TeX 07:161 (already in the 'known and disclosed' list; that site …
- `helium-symmetric-cavity.md` — Twin TeX 07:182 (ch07-A). :49 He IE 24.19 eV / -1.6% (Mutual Cavity Loading) — one of three unreconciled He precisions in the dir (see M7). :34 'K=2G vacuum modulus constraint' is R40-premise family …
- `qm-ave-translation.md` — Twin TeX 07:189 (ch07-A).
- `analog-ladder-filter.md` — Twin TeX 07:335 (ch07-A). :52 'The electron interacts with the vacuum's bulk modulus (acoustic impedance), not the shear modulus' — same claim family as the R40-B2a demotion stamped on de-broglie-sta…
- `screening-rule.md` — Twin TeX 07:480-540 (ch07-A). Listed as a candidate for my range but its content (sigma_total rule) is not in 2250-3400.
- `de-broglie-n.md` — Twin TeX 07:494 resultbox (ch07-A).
- `macro-cavity-saturation.md` — Twin TeX 07:555-558 (ch07-A). :10 'formally superseded by the **Mutual Cavity Loading** architecture' contradicts the Dual-Formalism box in my range — see M4.
- `geometry-pipeline.md` — Twin TeX 07:562 'Complete Geometry-to-Solver Pipeline' (ch07-A).
- `bonding-mode-formula.md` — Twin TeX 07:1368 '(E1) Same-shell bonding mode' (ch07-B).
- `complete-solver-architecture.md` — Twin TeX 07:1548 resultbox (ch07-B). :42 QM-contamination checklist row '\| WKB / ABCD cascade \| No \| $\checkmark$ \|' asserts the solver does NOT use an ABCD cascade, contradicting E2d-ii..E2k (my…
- `atom-as-radial-waveguide.md` — Twin TeX 07:1822/1972 (ch07-B).
- `scale-separation.md` — Twin TeX 07:3565-3611 (ch07-D). :29 'Same-$n$ electrons are **excluded** from the CDF screening' and :35 'Previous versions of the solver incorrectly included same-$n$ electrons ... double-counting' …
- `subshell-junction-scattering.md` — Twin TeX 07:3621 'Phase 5: Sub-Shell Junction Scattering (Op10)' (ch07-D). Listed as a candidate for my range; not in 2250-3400.
- `knot-vs-orbital-table.md` — Twin TeX 07:3663 table caption 'Knot topology vs orbital geometry: scale separation.' (ch07-D). Candidate for my range; not in 2250-3400.
- `operator-domain-table.md` — Twin TeX 07:3698 table caption 'Operator domain assignment for the IE solver.' (ch07-D).
- `helium-coupling-first-principles.md` — Twin TeX 07:3734 (ch07-D). Candidate for my range; not in 2250-3400. :52 He IE 24.37 eV agrees with my-range site TeX 3134 / KB 688.
- `chiral-factor.md` — Twin TeX 07:3813 (ch07-D). :28 'He IE to 0.008%' (TeX 3851) is a third He precision figure (vs 0.9% and -1.6%) — see M7. :45 '(2,3) trefoil produces 6/5' is a K6 fence-excluded hit.
- `stepped-impedance-resonator.md` — Twin TeX 07:3879 (ch07-D). Raw-LaTeX leaf; stray '% ===' LaTeX comment lines leaked at :90-92.
- `hierarchical-cascade-correction.md` — Twin TeX 07:3961 (ch07-D). Candidate for my range; not in 2250-3400. Raw-LaTeX leaf; stray '% ===' lines at :58-60. :56 Be -7.1% -> -0.45% contradicts my-range Be 11.9% 'remain open' — see M6.
- `ionization-energy-validation.md` — Twin TeX 07:4013 (ch07-D). Raw-LaTeX tabular leaf. :22 Li 5.525 / +2.46% contradicts my-range Li 5.32 / 1.2% — see M5. :52 provenance pin (A47 v11c) for ionization_energy_e2k.
- `index.md` — DERIVED (kind: index), not a sync source. :23 lists He IE 24.19 eV / -1.6% (mutual cavity loading) while the leaf twin of my range (radial-eigenvalue-solver.md:688) prints 24.37 / 0.9% — different me…

### ch07-D — **NO READ (slice did not return)**

### ch08

| TeX range | heading | KB leaf | status | note |
|---|---|---|---|---|
| 08:12-17 | \section{The Dimensionality Crisis in Modern Physics} | planck-scale-derivation.md:16-22 (### The Dimensionality Cr… | verbatim-match | Word-for-word translation (LaTeX->Markdown syntax swap only, e.g. \textit->*). |
| 08:19-32 | \section{String Tension as Mutual Inductance} + resultbox | planck-scale-derivation.md:24-40 | verbatim-match | T_AVE = m_e^2c^3/hbar approx 0.212 N identical in both; resultbox rendered as > **[Resultbox]** blockquote per INVARIANT-S1. |
| 08:34-45 | \subsection{Deriving the Regge Slope (\alpha')} examplebox | planck-scale-derivation.md:42-60 | verbatim-match | alpha'=0.75 GeV^-2, 17% gap, alpha'_baryon=4.09e-4 GeV^-2 identical; fragments verified byte-exact via grep -nF at TeX:40-41 and leaf:51-54. |
| 08:47-63 | \subsection{String Tension Comparison Table} + dimensional-analysis para | planck-scale-derivation.md:62-70 | verbatim-match | Table row 'Hadronic Regge slope alpha\' \| 0.750 GeV^-2 \| 0.9 GeV^-2 \| 17%' byte-identical TeX:56 vs leaf:67 (verified). Index.md:18 Key Results row also carries the same triple (0.750/0.9/17%) -- three-way parity con… |
| 08:64-74 | \section{Why Extra Dimensions Are Unnecessary} | string-theory-translation.md:8-20 | verbatim-match | All three enumerated reasons (volume-bearing flux tubes, dielectric saturation/Axiom 4, Faddeev-Skyrme topological stability) identical wording. |
| 08:76-90 | \section{Topological Resonance vs Closed Strings} + figure | string-theory-translation.md:22-30 | partial | Prose paragraphs verbatim-match. The figure itself is reduced in the KB leaf to a bare placeholder '[Figure: string_theory_lc_mapping.pdf --- see manuscript/vol_2_subatomic/chapters/]' (leaf:28) -- it does NOT reproduce… |
| 08:91-97 | \section*{Chapter Summary} | (none) | tex-only | No KB leaf twin; summary bullets restate results already covered by planck-scale-derivation.md and string-theory-translation.md verbatim-match sections above. Not debt (TEX-ONLY per rules, and content is non-conflicting… |
| 08:99-103 | \section*{Exercises} | (none) | tex-only | Exercises are conventionally not translated into KB leaves anywhere in the corpus; consistent with that pattern, not debt. |

### ch09 — **NO READ (slice did not return)**

### ch10 — **NO READ (slice did not return)**

### ch11 — **NO READ (slice did not return)**

### ch12-mp — **NO READ (slice did not return)**

### ch12-fp — **NO READ (slice did not return)**

### appx-front — **NO READ (slice did not return)**

---

## §2 — Mismatches (reader-reported; verifier verdict column)

Kinds: WB-LAG (KB walked back, print still asserts) · CONTRA · STALE-KB (print corrected, leaf lags) · DEAD-ANCHOR · KB-INTERNAL · TEX-ONLY. Verdict: CONFIRMED / DOWNGRADED / REFUTED / UNVERIFIED (verifier not yet returned).

| # | slice | sev | kind | print site | KB site | verdict | disclosed | known in | proposed action |
|---|---|---|---|---|---|---|---|---|---|
| 1 | ch01-A | HIGH | WB-LAG | `01_topological_matter.tex:35` | `newtonian-inertia-as-lenz.md:14` | **UNVERIFIED** | no |  | Print-side propagation of the 2026-06-20 Grant-ratified mass-sector re-scope: the stored inductive energy is the T2/Cosserat FLYWHEEL (frequency regulation); the rest-mass STORE is the orthogonal A1 … |
| 2 | ch01-A | MEDIUM | WB-LAG | `01_topological_matter.tex:8` | `newtonian-inertia-as-lenz.md:14` | **UNVERIFIED** | no |  | Same 2026-06-20 re-scope, chapter-objective echo site. Fix in lockstep with M1 (the objective promises mass-from-inductance as the chapter's learning outcome). |
| 3 | ch01-A | HIGH | WB-LAG | `01_topological_matter.tex:207` | `index.md:13` | **UNVERIFIED** | no |  | Print asserts the superseded closed-loop neutrino topology in the ch01 regime table with no local marker. The 2026-05-06 corrigendum IS printed — but at 03:13, two chapters away, and it does not name… |
| 4 | ch01-A | MEDIUM | KB-INTERNAL | `01_topological_matter.tex:207` | `regime-classification.md:15` | **UNVERIFIED** | no |  | Adjudicated per slice-instruction (a): regime-classification.md is a LEAF (kind: leaf, clm-ou2jym) and it carries the superseded closed-loop neutrino framing UNBANNERED, while the ch03 corrigendum (2… |
| 5 | ch01-A | MEDIUM | STALE-KB | `01_topological_matter.tex:209` | `regime-classification.md:17` | **UNVERIFIED** | no |  | Leaf lags print: print carries the real-space/phase-space correction (INVARIANT-N1: proton body = $6^3_2$ Borromean; $(2,5)$ is the phase-space portrait) that the leaf's 'Cinquefoil' Topology cell st… |
| 6 | ch01-A | MEDIUM | WB-LAG | `01_topological_matter.tex:242` | `chirality-and-antimatter.md:10` | **UNVERIFIED** | no | 2026-09-06 scan S4a candidate site 01:242 | The leaf's own opening sentence was RELABELLED by the Grant 2026-07-09 R1 adjudication (canonical charge-sign = Beltrami helicity → $e^-$ = LH); the printed twin is the un-relabelled prior wording. N… |
| 7 | ch01-A | MEDIUM | CONTRA | `01_topological_matter.tex:248` | `chirality-and-antimatter.md:18` | **UNVERIFIED** | no |  | Same sentence, one word apart: print calls the electron a 'Hopfion' (non-trivial real-space Hopf charge) where the leaf says '$0_1$ unknot'. The leaf twin was corrected; print was not. mathematical-t… |
| 8 | ch01-A | HIGH | WB-LAG | `01_topological_matter.tex:259` | `electron-identification.md:64` | **UNVERIFIED** | no |  | Print figure caption sells the free-precursor formation route as established ('establishing the physical derivation of confined point-particles'), which the KB grades closed-negative / leans-falsifie… |
| 9 | ch01-A | LOW | DEAD-ANCHOR | `01_topological_matter.tex:79` | `electron-identification.md:92` | **UNVERIFIED** | no |  | KB-side dead anchor: translation-circuit.md:637 no longer carries the quoted content (line 637 at HEAD reads 'The substrate's **cold-lattice ideal state** is the limit:'). Verified true location at H… |
| 10 | ch01-A | LOW | DEAD-ANCHOR | `01_topological_matter.tex:55` | `translation-circuit.md:839` | **UNVERIFIED** | no |  | The 2026-08-02 comment block's own cite-repair (':637 → :767') has itself gone stale; the line is :839 at HEAD. Non-printed (% comment), so zero PDF impact — but it is the third recorded drift of thi… |
| 11 | ch01-A | MEDIUM | WB-LAG (leaf scope-note undated) | `01_topological_matter.tex:239` | `torus-knot-ladder.md:21` | **UNVERIFIED** | no | 2026-09-06 scan S4a listed 01:218 and 01:237 in t… | Print carries the ladder's other three fences (dimensionless $r_{opt}$, $S=0$ $N/\Delta$ scope flag, cold-vs-thermal convention) but not the leaf's imported-assignment note; combined with 'zero empir… |
| 12 | ch01-A | LOW | UNIT-LABEL LAG (disclosed in print) | `01_topological_matter.tex:227` | `torus-knot-ladder.md:10` | **UNVERIFIED** | yes | 2026-09-06 scan S4a candidates 01:218 / 01:237 | Leaf stripped the $\ell_{node}$ units from every cell and calls them 'spurious'; print keeps them in all six cells and neutralises them with an inline clause (01:218) plus a dagger footnote (01:237) … |
| 13 | ch01-A | LOW | WB-LAG | `01_topological_matter.tex:40` | `electron-unknot.md:13` | **UNVERIFIED** | no |  | The leaf pins a dated 2026-06-24 reading-scope on this exact clause; print has none. Graded LOW because print's own wording already attributes the trapping to the closed topological loop (the SURVIVI… |
| 14 | ch01-A | MEDIUM | WB-LAG (undated leaf demotion) | `01_topological_matter.tex:244` | `chirality-and-antimatter.md:28` | **UNVERIFIED** | no |  | The leaf and clm-hb2xmj both grade the annihilation section asserted-mechanism / peer-not-chord at solidity 0.30 ('do not build on'); print states the resolution flatly and prints the 1.022 MeV resul… |
| 15 | ch01-A | LOW | KB-INTERNAL (acknowledged OPEN fork — flag, do not adjudica… | `01_topological_matter.tex:147` | `electron-unknot.md:59` | **UNVERIFIED** | yes | ch01 index.md:44 names it: 'the **tube-geometry f… | electron-unknot.md:13 (tube radius $l_{node}/(2\pi)$) vs :59 (tube diameter $\equiv 1\,l_{node}$) differ by $\approx10\times$; PRINT carries BOTH sides verbatim at 01:40 and 01:147 with no flag. The … |
| 16 | ch01-A | LOW | WB-LAG (undated leaf scope note) | `01_topological_matter.tex:16` | `mathematical-topology-of-mass.md:20` | **UNVERIFIED** | no |  | Leaf tags the functional peer-with-standard / adopted ansatz (matching clm-oygz1i's non-claim: 'a **chosen ansatz** ... The leaf does not derive the Skyrme term independently from Axioms 1-4'); print… |
| 17 | ch01-C | HIGH | WB-LAG | `01_topological_matter.tex:35` | `newtonian-inertia-as-lenz.md:14` | **UNVERIFIED** | no |  | Print-side propagation of the 2026-06-20 Grant-ratified mass-sector ruling into Vol 2 Ch 1 §'Newtonian Inertia as Macroscopic Lenz's Law': a dated printed note stating the stored inductive energy is … |
| 18 | ch01-C | MEDIUM | WB-LAG | `01_topological_matter.tex:33` | `newtonian-inertia-as-lenz.md:14` | **UNVERIFIED** | no |  | Same print note as M1 covers this line — the banner quotes this very mapping by name. No separate edit needed if M1's note is placed at the section head rather than after :35. |
| 19 | ch01-C | MEDIUM | WB-LAG | `01_topological_matter.tex:266` | `newtonian-inertia-as-lenz.md:14` | **UNVERIFIED** | no |  | Chapter-summary bullet re-asserts the superseded store-identification after the section it summarises; needs the same A1-store / T2-flywheel split once M1 is ruled. Bundle with M1. |
| 20 | ch01-C | MEDIUM | WB-LAG | `01_topological_matter.tex:8` | `newtonian-inertia-as-lenz.md:14` | **UNVERIFIED** | no |  | Objective-box bullet states the superseded store-identification as a chapter learning objective. Re-word to the flywheel / A1-depression split once M1 is ruled. Bundle with M1. |
| 21 | ch01-C | MEDIUM | WB-LAG | `01_topological_matter.tex:148` | `common-mode-twist-ledger.md:235` | **UNVERIFIED** | no |  | Print carries BOTH halves of a fork the KB has dated and routed: 01:40 prints the electron-unknot.md:13 geometry ('The unknot has circumference $\ell_{node}$ and tube radius $\ell_{node}/(2\pi)$') an… |
| 22 | ch01-C | MEDIUM | WB-LAG | `01_topological_matter.tex:40` | `spin-gyroscopic-isomorphism.md:45` | **UNVERIFIED** | no |  | The leaf carves 'macroscopic' explicitly as a term of art (leaf :15 — classical / deterministic-extended, a ~ℓ_node-scale circulation loop, NOT human-scale) and states the core is subatomic, not macr… |
| 23 | ch02 | MEDIUM | WB-LAG | `02_baryon_sector.tex:319` | `topological-fractionalization.md:60` | **UNVERIFIED** | no |  | Print asserts a 'CP-violating theta-vacuum phase' (and 'trapped vacuum' at :327, :330) flatly; the leaf's dated 2026-08-23 theta-fork note (Grant rulings (a)+(b)) at :50-76 says (1) theta is the J-dr… |
| 24 | ch02 | MEDIUM | STALE-KB | `02_baryon_sector.tex:357` | `proton-neutron-mass-split.md:10` | **UNVERIFIED** | no |  | Print was corrected 2026-06-15 (LF-03 D-class, % comment :356: 'accounts for' SUPERSEDED -> consistent-with-not-derived, no physics change) and cites neutron-identification.md as the honest anchor; t… |
| 25 | ch02 | LOW | DEAD-ANCHOR | `02_baryon_sector.tex:357` | `neutron-identification.md:52` | **UNVERIFIED** | no | 2026-09-06 scan S5 (02:357/362 -> neutron-identif… | The cited ':52' is now the §2.1 heading; the cited sentence ('This bound is consistent with — but does not derive — the empirical $\Delta m c^2 = 1.293$ MeV.' + 'Derivation TBD: compute the FS energy… |
| 26 | ch02 | LOW | DEAD-ANCHOR | `02_baryon_sector.tex:357` | `neutron-identification.md:23` | **UNVERIFIED** | no |  | Leaf->TeX anchors are dead at HEAD: :23 ':294' -> :357; :64 '`vol_2_subatomic/chapters/02_baryon_sector.tex:294,299`' -> :357,362; :114 '`manuscript/vol_2_subatomic/chapters/02_baryon_sector.tex:292-… |
| 27 | ch02 | LOW | STALE-KB | `02_baryon_sector.tex:362` | `neutron-identification.md:25` | **UNVERIFIED** | yes |  | Leaf :25 quotes the SUPERSEDED caption wording ('accounts for') as the canonical Vol 2 quote; print caption :362 was corrected 2026-06-15 to 'is the proposed structural origin of ... (a bound consist… |
| 28 | ch02 | LOW | STALE-KB | `02_baryon_sector.tex:131` | `thermal-softening.md:37` | **UNVERIFIED** | yes | #847 audit R3, 2026-08-02 (thermal-softening.md:4… | Leaf is the last KB site carrying the pre-walk-back verb 'validates'; print :131 reads 'covers' with the rider 'Read ``covers'' as consistency, not ensemble-validation'. The leaf's own :40 banner rec… |
| 29 | ch02 | MEDIUM | WB-LAG | `02_baryon_sector.tex:463` | `proton-identification.md:73` | **UNVERIFIED** | no |  | Chapter Summary headlines 'The exact ... ($1836.15$) is derived': (a) 1836.15 is the CODATA value, the derived value is 1836.12 (leaf :13 '**the proton\'s mass ratio $m_p/m_e = 1836.12$ is derived wi… |
| 30 | ch02 | MEDIUM | WB-LAG | `02_baryon_sector.tex:60` | `proton-identification.md:73` | **UNVERIFIED** | no |  | Section opener says the empirical 1836.15 'emerges ... as the exact eigenvalue'; the derived eigenvalue is 1836.12 (-0.002%) and the D1 ruling (leaf :73) makes +0.74% the headline. Nearest printed ca… |
| 31 | ch02 | LOW | WB-LAG | `02_baryon_sector.tex:7` | `proton-identification.md:13` | **UNVERIFIED** | no |  | Objectivebox headlines 'precise derivation ... ($1836.15$)' (CODATA value as the derived value; headline posture contrary to D1 ruling, leaf :73). Same fix family as M7/M8. |
| 32 | ch02 | LOW | CONTRA | `02_baryon_sector.tex:297` | `torus-knot-ladder-baryons.md:30` | **UNVERIFIED** | no |  | The :309 ADJUDICATED note (2026-07-02) makes the PDG-2024 anchor driver canonical for the table but lists only c=9,11,13 as updated; the c=15 row still carries the older PDG mass 2420 / +2.40% while … |
| 33 | ch02 | LOW | CONTRA | `02_baryon_sector.tex:314` | `torus-knot-ladder-baryons.md:30` | **UNVERIFIED** | no |  | Figure caption gives a third c=15 deviation (+9.8%) that matches neither the print table :297 (+2.40%) nor the leaf :30 (+3.249%), and contradicts print :131 ('covers ... through c = 15'). The captio… |
| 34 | ch02 | LOW | CONTRA | `00_title.tex:18` | `proton-identification.md:13` | **UNVERIFIED** | no |  | Volume title page prints 1836.14, which is neither the derived 1836.12 (leaf :13; self-consistent-mass-oscillator.md:61; thermal-softening.md:13 '1836.117') nor CODATA 1836.153 (TeX :268) nor ch02's … |
| 35 | ch02 | LOW | WB-LAG | `02_baryon_sector.tex:466` | `proton-neutron-mass-split.md:89` | **UNVERIFIED** | yes |  | Residual strength adverb: print keeps 'strictly resolved' after the 2026-06-15 A.1 re-scope (leaf :82 banner; claim-quality clm-bh9p6s solidity 0.40 'do not build on' / 'algebraic substitution, not a… |
| 36 | ch02 | LOW | KB-INTERNAL | `02_baryon_sector.tex:238` | `self-consistent-mass-oscillator.md:30` | **UNVERIFIED** | no |  | Print and leaf agree verbatim, but both say p_c is 'derived in Chapter 2' (this IS Vol 2 Ch 2, which does not derive p_c), while proton-identification.md:66/:70 attribute it to 'Vol 1 Ch 8 closure: $… |
| 37 | ch03 | MEDIUM | WB-LAG | `03_neutrino_sector.tex:227` | `delta-cp-violation.md:22` | **UNVERIFIED** | no |  | Reword TeX 03:227 item 1 to match the leaf's corrected physical description ('half-period of the propagating Cosserat coil', not '0_1 unknot phase winding'), consistent with the chapter's own 2026-05… |
| 38 | ch03 | HIGH | WB-LAG | `03_neutrino_sector.tex:272` | `index.md:13` | **UNVERIFIED** | no |  | Rewrite Chapter Summary bullet 1 to state the canonical screw-dislocation / open-helix framing (as the objectivebox at line 7 and the corrigendum at line 13 of the SAME chapter already do), dropping … |
| 39 | ch03 | LOW | WB-LAG | `03_neutrino_sector.tex:274` | `index.md:13` | **UNVERIFIED** | no |  | Same block as M2 (Chapter Summary bullet 3); drop '$0_1$' label for the mass eigenstates when M2 is fixed. |
| 40 | ch03 | HIGH | WB-LAG | `03_neutrino_sector.tex:159` | `chiral-screening.md:35` | **UNVERIFIED** | no |  | Add a print-visible caveat at TeX 03:149-159 (resultbox + note) reflecting the 2026-08-24 carve: leg 1 (transfer-capacity chain) is derived-modulo-premise, but leg 2 (connectivity=trefoil crossing nu… |
| 41 | ch03 | MEDIUM | WB-LAG | `03_neutrino_sector.tex:250` | `delta-cp-violation.md:38` | **UNVERIFIED** | no |  | Qualify TeX 03:250's 'derive from three inputs / no curve fitting' framing per the leaf's 2026-05-17 Foundation-Item-13 scope correction: c_1=5 (hence c_1*c_3=45, hence sin^2(theta13)) is chosen-not-… |
| 42 | ch03 | MEDIUM | WB-LAG | `01_topological_matter.tex:207` | `index.md:13` | **UNVERIFIED** | no |  | Update the ch01 regime-classification table's Neutrino row Topology column from 'Twisted unknot' to the canonical 'Open helix (screw dislocation)' per the ch03 corrigendum, which explicitly anticipat… |
| 43 | ch03 | HIGH | WB-LAG | `00_title.tex:14` | `index.md:13` | **UNVERIFIED** | no |  | Update the Volume II front-matter abstract (most reader-visible text in the volume) from 'neutrinos as dispersive twisted 0_1 unknots, bound by the Faddeev-Skyrme energy functional' to reflect the ca… |
| 44 | ch03 | LOW | STALE-KB | `03_neutrino_sector.tex:122` | `claim-quality.md:251` | **UNVERIFIED** | yes |  | Trivial label-only sync: update claim-quality.md:251's flavor-splitting bullet from Delta(1620) to Delta(1600) to match the already-disclosed, dated (2026-06-19) TeX correction. Not a leaf (claim-qua… |
| 45 | ch04 | LOW | DEAD-ANCHOR (comment-only; not printed) | `04_quantum_spin.tex:81` | `claim-quality.md (clm-salw2h):408` | **UNVERIFIED** | no | 2026-09-06 scan S4a 04:111 (file-level 'leaf newe… | Comment-only line-number repair in the % block at TeX:81-88: :407->:408, :408->:409, :409->:410, :410->:411, ':419' (TeX:88 'Claim solidity 0.70 at :419.') -> :420. Verified via git show: the clm-sal… |
| 46 | ch04 | LOW | DEAD-ANCHOR (KB-side line cite drift) | `04_quantum_spin.tex:111` | `larmor-derivation.md:61` | **UNVERIFIED** | no |  | Leaf-side line-number repair: ':407–410' -> ':408–411' and ':419' -> ':420' at larmor-derivation.md:61; the per-item cites '(:407)' at :63, '(:408)' at :64, ':410' at :65 and '(:409)' at :67 each shi… |
| 47 | ch04 | LOW | DEAD-ANCHOR (KB-side line cite drift) | `04_quantum_spin.tex:111` | `visual-equivalence.md:22` | **UNVERIFIED** | no |  | Leaf-side line-number repair at visual-equivalence.md:22: ':407–410' -> ':408–411', ':419' -> ':420', and the inline '(:407)', '(:408)', '(:410)', '(:409)' each +1. Same cause as M1/M2. |
| 48 | ch04 | MEDIUM | CONTRA (topology: printed figure caption still names the el… | `04_quantum_spin.tex:62` | `larmor-derivation.md:10` | **UNVERIFIED** | no |  | Route for ruling/fix: the 2026-08-02 softening (commit e947ce4a) touched :53/:68 only and left the fig:spin_precession caption on the pre-migration trefoil identity. Print is internally inconsistent … |
| 49 | ch04 | LOW | STALE-TEX-COMMENT (comment-only; TeX % FLAG-DON'T-FIX block… | `04_quantum_spin.tex:94` | `larmor-derivation.md:57` | **UNVERIFIED** | yes | MR board 2026-08-02 'vol2 -- 13 findings' item 04… | Comment-only append at TeX:89-97 noting the OWED KB-leaf edit LANDED (larmor-derivation.md:55-67 and visual-equivalence.md:14-24 both carry the 2026-08-02 KB-lockstep banner and the ~~struck~~ prior … |
| 50 | ch04 | LOW | KB-INTERNAL (derived index vs its own bannered leaves: inde… | `04_quantum_spin.tex:6` | `index.md:11` | **UNVERIFIED** | no |  | Index is DERIVED (kind: index) and not the sync source of truth -- flag only. On the next index regeneration, mirror the leaf banner (e.g. 'defined structurally as ... on the disclosed spin-½ selecti… |
| 51 | ch05 | MEDIUM | STALE-KB | `05_electroweak_gauge_theory.tex:83` | `weinberg-angle.md:26` | **UNVERIFIED** | no | MR board 2026-08-02 vol2 [LOW][mirror-drift][ruli… | Add a dated Rule-12 banner to weinberg-angle.md:26 preserving the prior body and copying TeX :83 (corrected sentence) + :84 (the 2026-08-02 corrigendum text: 'the phrase above previously read "the tr… |
| 52 | ch05 | LOW | STALE-KB | `05_electroweak_gauge_theory.tex:81` | `weinberg-angle.md:20` | **UNVERIFIED** | no | MR board 2026-08-02 vol2 [LOW][mirror-drift][ruli… | Symbol-only relabel nu_vac -> nu_Hill in weinberg-angle.md:20/:23/:26 (and gauge-boson-masses.md:42 which still writes $\nu_{\text{vac}} = 2/7$ while :38 already writes nu_Hill). Board classifies the… |
| 53 | ch05 | MEDIUM | STALE-KB (reads as CONTRA on mechanism gloss: print explici… | `05_electroweak_gauge_theory.tex:115` | `weak-coupling.md:30` | **UNVERIFIED** | no |  | Leaf lags the 2026-07-02 Grant-ruled print re-anchor (commit 23a0ff2d). Needs the ruled text to be mirrored into weak-coupling.md with a Rule-12 banner preserving the prior gloss; the print carries n… |
| 54 | ch05 | LOW | STALE-KB | `05_electroweak_gauge_theory.tex:103` | `weak-coupling.md:22` | **UNVERIFIED** | no |  | Companion site of ch05-M03 (same 2026-07-02 re-anchor); resolve together. Print :103 also adds the substrate-native gloss 'here $\mathcal{L}_{\text{int}}$ denotes the interaction contribution to the … |
| 55 | ch05 | LOW | STALE-KB | `05_electroweak_gauge_theory.tex:104` | `weak-coupling.md:24` | **UNVERIFIED** | no |  | Companion site of ch05-M03 (resultbox retitled in print 2026-07-02; equation body identical on both sides). Resolve together. |
| 56 | ch05 | LOW | DEAD-ANCHOR (KB->KB) | `05_electroweak_gauge_theory.tex:35` | `gauge-boson-masses.md:34` | **UNVERIFIED** | no |  | vocabulary-register.md:870 is now def-t2ph01's status line; def-l0ngdu header is at :882, id at :883, the quoted 'One word each way' clause at :893 (verification field). Repair the line number (print… |
| 57 | ch05 | LOW | DEAD-ANCHOR (KB->KB) | `05_electroweak_gauge_theory.tex:51` | `gauge-boson-masses.md:42` | **UNVERIFIED** | yes |  | vocabulary-register.md:867 and :870 now fall inside def-t2ph01 (:863-880); def-l0ngdu is :882-895. Repair :867->:882 and :870->:893 (or :886 adjudicated-meaning). The paragraph is already 🔴 DEMOTED (… |
| 58 | ch05 | LOW | DEAD-ANCHOR (KB->KB) | `05_electroweak_gauge_theory.tex:33` | `gauge-boson-masses.md:48` | **UNVERIFIED** | yes |  | vocabulary-register.md:882 is now the def-l0ngdu header; def-uatk1s header is :897, id :898. Repair :882->:898. Note the host paragraph gbm:48 (the 'mass flow' A-vs-u PREMISE-CRITICAL flag) is 🔴 DEMO… |
| 59 | ch05 | LOW | DEAD-ANCHOR (external cites into this slice's leaf; citer i… | `06_temperature_characteristics.tex:79` | `gauge-boson-masses.md:39` | **UNVERIFIED** | no | 2026-09-06 scan S5 :259 (15_falsification_tests.t… | gauge-boson-masses.md:39 is a bare blockquote spacer inside the 2026-08-03 repair block; the cited content ('defines a fundamental **Characteristic Length Scale** ($l_c = \sqrt{\gamma_c/G_{vac}}$)') … |
| 60 | ch05 | MEDIUM | WB-LAG (chapter-summary bullet un-rescoped; the R43 rescope… | `05_electroweak_gauge_theory.tex:175` | `gauge-boson-masses.md:83` | **UNVERIFIED** | no |  | Summary bullet asserts flat 'explicitly derived' gauge invariance; the leaf (and print :35/:51) rescopes to the residual time-independent family only. Needs an author/ruling pass on the summary wordi… |
| 61 | ch05 | LOW | WB-LAG (objectivebox bullet un-rescoped; disclosure printed… | `05_electroweak_gauge_theory.tex:8` | `gauge-boson-masses.md:34` | **UNVERIFIED** | no |  | Companion of ch05-M10; same rider would close it. No KB twin for the objectivebox. |
| 62 | ch05 | LOW | TEX-ONLY overclaim vs clm-jkpfd4 non-claims (comparator is … | `05_electroweak_gauge_theory.tex:178` | `claim-quality.md:817` | **UNVERIFIED** | no |  | 'explicitly proven' vs sidecar :816 'The Wilson-action argument is **standard lattice-gauge-theory mathematics**' (not original to AVE) and :817 SU(3) identification 'is not a uniqueness theorem' (so… |
| 63 | ch05 | LOW | KB-INTERNAL candidate (gauge-boson-masses.md:83 'canon hold… | `05_electroweak_gauge_theory.tex:159` | `forward-to-ch6.md:40` | **UNVERIFIED** | no |  | Answers the slice question: print :135-159 and leaf :14-40 are byte-consistent with EACH OTHER and neither carries the R43 (c) rescope. Whether the rescope (which targets the Helmholtz/Lambda gauge-f… |
| 64 | ch05 | LOW | DISCLOSED-ONLY-IN-COMMENT (partial): the DEMOTED stamp prin… | `05_electroweak_gauge_theory.tex:51` | `gauge-boson-masses.md:131` | **UNVERIFIED** | yes |  | Print reader is pointed at a note that does not print (the Axiom 5 clause G / A_g UNVALUED-RATIFIED-CONSTANT per R48 / BIAS-DEBT arc lives only in comments :187-247; the slice's :201-206 comments are… |
| 65 | ch05 | LOW | KNOWN-DEBT RE-CHECK (05:35/05:51 def-l0ngdu compressibility… | `05_electroweak_gauge_theory.tex:51` | `gauge-boson-masses.md:38` | **UNVERIFIED** | yes | MR board 2026-08-02 vol2 [MEDIUM][other][route-to… | None. At HEAD the false premise is struck in print (:51 names it verbatim as 'First failure (2026-08-03)'), the E-leg replacement is SUPERSEDED in print (:51 '[SUPERSEDED 2026-08-10 --- that last cla… |
| 66 | ch06-A | MEDIUM | WB-LAG (claim-quality-sidecar demotion unpropagated to TeX … | `06_electroweak_and_higgs.tex:17` | `claim-quality.md:162` | **UNVERIFIED** | no | vol2/claim-quality.md R40 batch-2a demotion note … | Add a Rule-12 dated caveat at TeX 06:17 (and mirror it into higgs-mechanism.md:13) noting the acoustic-relaxation MECHANISM for the 125 GeV resonance is DEMOTED 2026-08-11 (R40-B2a, NEEDS RE-DERIVATI… |
| 67 | ch06-A | MEDIUM | WB-LAG | `06_electroweak_and_higgs.tex:363` | `chiral-screening.md:35` | **UNVERIFIED** | no | MR-board revalidation F8 (06:363-365 Δc_crit prov… | Print at 06:363-365 needs the 2026-08-24 carve's caveat: 'connectivity = trefoil crossing number' is demoted to asserted-pending-derivation and 'connectivity = Cosserat sector count' fails the counte… |
| 68 | ch06-A | MEDIUM | CONTRA / STALE-KB | `06_electroweak_and_higgs.tex:210` | `lepton-spectrum.md:81` | **UNVERIFIED** | no |  | TeX's own headline W/Z summary table (06:206-211) already reports the SELF-CONSISTENT loop-corrected values (80,224/90,965 MeV, -0.19%/-0.24%, via the K4 Bethe-tree S11 back-saturation derived at 06:… |
| 69 | ch06-A | MEDIUM | CONTRA | `06_electroweak_and_higgs.tex:321` | `higgs-mass.md:29` | **UNVERIFIED** | no |  | TeX's Bethe-lattice cos(2π/c) eigenvalue derivation (06:283-335) gives ν1=9.58, ν2=19.33, ν3=23.75 meV (sum 52.7 meV) and explicitly states 'Normal hierarchy, m1<m2<m3'. higgs-mass.md's simpler 1/c t… |
| 70 | ch06-A | LOW | STALE-KB (TeX diagram unpropagated correction) | `06_electroweak_and_higgs.tex:193` | `lepton-spectrum.md:73` | **UNVERIFIED** | no |  | TeX's arrow diagram labels BOTH remaining arrows identically as α·p_c, which does not match TeX's own boxed τ formula two lines above (06:186, m_τ = m_e·p_c/α²). lepton-spectrum.md's 'Net-α-power red… |
| 71 | ch06-A | LOW | DEAD-ANCHOR | `sm-ave-translation.md:10` | `06_electroweak_and_higgs.tex:860` | **UNVERIFIED** | no |  | Update sm-ave-translation.md's cited line number from 305 to 860 (the \input actually sits there at HEAD; line 305 is mid-neutrino Bethe-lattice text, unrelated). Pure line-number repair. |
| 72 | ch06-A | LOW | KB-INTERNAL (inconsistent disclosure visibility) | `higgs-mechanism.md:54` | `lepton-spectrum.md:29` | **UNVERIFIED** | no |  | The same dated, already-worded Rule-12 open-flag text for the contested √(3/7) label is a VISIBLE rendered blockquote in lepton-spectrum.md:29, but only a HIDDEN HTML comment (invisible on render) at… |
| 73 | ch06-A | LOW | DEAD-ANCHOR | `06_electroweak_and_higgs.tex:422` | `verify-md-links.py:808` | **UNVERIFIED** | yes | verify-md-links.py WAIVED_KBLEAF adjudication (re… | Already tracked as a known, deliberately-waived dead cite pending a canonical tracked anchor for the four-lemma Goldstone derivation. No action needed beyond what the tooling already does (loud waive… |
| 74 | ch06-B | LOW | DEAD-ANCHOR | `06_electroweak_and_higgs.tex:723` | `q-g19a-petermann-saliency-closure.md:121` | **UNVERIFIED** | no | 2026-09-06 scan S4a 06:722 (scan.txt:100, 'leaf n… | Printed anchors :12/:14/:92 still resolve; :100 (now a blank quote line), :103 (now 'What survives from the body above'), :121 (now 'Consequence: the dispute ... dissolves') do not. Content moved by … |
| 75 | ch06-B | LOW | DEAD-ANCHOR | `06_electroweak_and_higgs.tex:770` | `q-g19a-petermann-saliency-closure.md:110` | **UNVERIFIED** | no | 2026-09-06 scan S5 anchor 06:770 -> q-g19a:110 'a… | The cited RESOLVED-NEGATIVE / winding-blind / 1-point-fit verdict now lives at leaf :221 ('**→ RESOLVED NEGATIVE (2026-05-31, FT-b saliency-derivability):**'); :110 is a python line inside the 2026-0… |
| 76 | ch06-B | MEDIUM | WB-LAG (comment-only; ROUTED, not a walk-back) | `06_electroweak_and_higgs.tex:603` | `q-g19a-petermann-saliency-closure.md:173` | **UNVERIFIED** | no | slice brief: Petermann normalization ROUTED dispu… | Print 600 (Delta a_e = (1/pi^2)<..>(alpha/pi), implying C_2 = <..>/(pi alpha)) and 603 (C_2 = (2/(pi alpha))<..>) are the same two forms the leaf :170-173 flags as inconsistent by exactly 2, with a f… |
| 77 | ch06-B | LOW | WB-LAG (comment-only) | `06_electroweak_and_higgs.tex:575` | `q-g19a-petermann-saliency-closure.md:193` | **UNVERIFIED** | no |  | Print 575-576 states tau_retard = 1/omega_C 'set by the unknot geometric scale' flatly (leaf body :37 has the identical wording, Rule-12 preserved); the Grant ruling block :189-194 (2026-08-03) recor… |
| 78 | ch06-B | LOW | WB-LAG | `06_electroweak_and_higgs.tex:620` | `q-g19a-petermann-saliency-closure.md:164` | **UNVERIFIED** | no |  | Leaf F3 (:150-164, 2026-08-03) finds the 'converges at N_t >~ 2e5' (print 609-610) and 'invariant under three independent derivative methods' (print 620-621) receipts non-probative for the retardatio… |
| 79 | ch06-B | LOW | WB-LAG (missing scope label) | `06_electroweak_and_higgs.tex:777` | `q-g19a-petermann-saliency-closure.md:242` | **UNVERIFIED** | yes |  | KB :240-244 (2026-08-02) labels the 'no fit parameters' section as a Stage-1-only statement; print 777-781 lacks the label. Disclosed in print by the immediately preceding bullet 753-769 ('Stage-2 cl… |
| 80 | ch06-B | MEDIUM | WB-LAG | `06_electroweak_and_higgs.tex:810` | `claim-quality.md (clm-p7rfkb; DERIVED sidecar — NO leaf carries this banner: vol6 lambda-higgs-derivation.md:26 and the ch06 leaves have zero 'R40' hits):162` | **UNVERIFIED** | no |  | claim-quality:1710-1720 (R40 batch-2a, 2026-08-11) stamps the acoustic-Higgs/breathing-mode family: 'the :163 K4-cell BREATHING mode is a dilatational eigenmode requiring the A1 restoring force; the … |
| 81 | ch06-B | LOW | DEAD-ANCHOR | `06_electroweak_and_higgs.tex:860` | `sm-ave-translation.md:10` | **UNVERIFIED** | no |  | Forwarder :10 cites the \input at 'line 305'; at HEAD it is at 860 (:8 is label-stable via sec:sm_ave_translation, so content is findable). Repair 305 -> 860 or drop the number. |
| 82 | ch06-B | LOW | DEAD-ANCHOR | `06_electroweak_and_higgs.tex:833` | `constants.py (code anchor cited via \kbleaf, not a KB leaf):679` | **UNVERIFIED** | no |  | constants.py:338 is 'ELL_C: float = np.sqrt(6.0) * L_NODE'; the cited definition is at :679. Repair the line number. |
| 83 | ch06-B | LOW | KB-INTERNAL (both sides KB: sibling cross-ref carries a ppm… | `q-g19a-petermann-saliency-closure.md:191` | `q-g20f-vacuum-polarization.md:97` | **UNVERIFIED** | no |  | q-g20f:97 sibling blurb restates '50 ppm precision' as a deviation claim; the q-g19a ruling block :189-204 enumerates unswept sites but does NOT list q-g20f:97. A dated strike tag copying q-g19a:95 '… |
| 84 | ch06-B | LOW | KB-INTERNAL (both sides KB: sibling cross-ref carries a str… | `q-g19a-petermann-saliency-closure.md:191` | `q-g27-muon-cosserat-saliency.md:80` | **UNVERIFIED** | no |  | q-g27:80 cross-ref title and trailing clause ('the 50 ppm figure is conditional on ...') carry the struck label; not in the q-g19a :198-204 unswept enumeration. Same verbatim strike-tag copy as M11. |
| 85 | ch06-B | LOW | KB-INTERNAL (leaf vs its own index; index is DERIVED) | `q-g19a-petermann-saliency-closure.md:8` | `index.md:36` | **UNVERIFIED** | no |  | index.md:36 title '(4% forward → 10 ppm with postulate)' and blurb '50 ppm at $C_2$ / ≈10 ppm at $a_e$ total' pre-date the 2026-08-03 strike executed in the leaf title :8 and :14; its anchor 'at q-g1… |
| 86 | ch06-B | MEDIUM | KB-INTERNAL | `q-g19a-petermann-saliency-closure.md:221` | `q-g27-muon-cosserat-saliency.md:71` | **UNVERIFIED** | no |  | q-g27 asserts 'zero fit parameters' (:10, :71) for delta^mu = -3alpha/2 - alpha sqrt(3/7)/(2pi) (:57) and 'Mechanism structurally closed' (:71), while q-g19a:221 (RESOLVED NEGATIVE 2026-05-31) grades… |
| 87 | ch06-B | LOW | DEAD-ANCHOR (leaf-internal; :112 and :123 at :244 now point… | `q-g19a-petermann-saliency-closure.md:244` | `q-g19a-petermann-saliency-closure.md:131` | **UNVERIFIED** | yes |  | Disclosed by the leaf's own :131 cite-integrity note ('re-resolved by section name'). The :240-244 block is a dated 2026-08-02 record; under R39 byte-fence (CONVENTIONS) an in-span numeric edit may b… |
| 88 | ch07-A | LOW | WB-LAG (dated KB notation correction 2026-05-17; print stil… | `07_quantum_mechanics_and_orbitals.tex:46` | `de-broglie-standing-wave.md:58` | **UNVERIFIED** | no |  | Route to core: print the '1 +' DC unit (matches KB:58 and clm-qde5gn:845) and optionally the KB's DeltaPhi ≈ 250 rad figure; KB:58 records that the missing '1 +' was inherited by the C11 driver as a … |
| 89 | ch07-A | MEDIUM | CONTRA (direction + values): print resultbox 'Deterministic… | `07_quantum_mechanics_and_orbitals.tex:224` | `orbital-penetration-penalties.md:39` | **UNVERIFIED** | no |  | Ruling needed: reconcile the sign of the l-degeneracy break and the Li 2s/2p numbers between print (TeX:221-231) and the canonical leaf; clm-oltvwy:348 already flags a Li residual inconsistency (+2.4… |
| 90 | ch07-A | MEDIUM | CONTRA / TEX-ONLY-contradicting (TeX:243 N_eff=1.5, +72%->-… | `07_quantum_mechanics_and_orbitals.tex:243` | `helium-symmetric-cavity.md:44` | **UNVERIFIED** | yes | research/2026-09-06_mr-board-revalidation_RESULT.… | Status at HEAD: still present; the printed R40-B2a DEMOTED stamp at TeX:239 (4 lines above) demotes the paragraph's bulk-modulus/K->G premise as NEEDS RE-DERIVATION but does NOT reconcile N_eff=1.5 v… |
| 91 | ch07-A | MEDIUM | WB-LAG, comment-only (DISCLOSED-ONLY-IN-COMMENT): the walk-… | `07_quantum_mechanics_and_orbitals.tex:277` | `hierarchical-cascade-correction.md:54` | **UNVERIFIED** | no |  | Print a dated one-line note at TeX:277 that the static FOC/J_2s 9.32 eV is superseded by the hierarchical-cascade result (§sec:hierarchical_cascade_correction, TeX:3962), and/or add a Rule-12 banner … |
| 92 | ch07-A | MEDIUM | CONTRA (value): print states Boron IE = 9.4 eV; KB records … | `07_quantum_mechanics_and_orbitals.tex:324` | `subshell-junction-scattering.md:11` | **UNVERIFIED** | no |  | Ruling/correction needed in print: replace or caveat the 9.4 eV figure against the KB-canonical Boron values; consider a Rule-12 note on helium-symmetric-cavity.md:78 recording the dropped print clai… |
| 93 | ch07-A | LOW | STALE-KB: print carries the dated R40-B2a demotion stamp on… | `07_quantum_mechanics_and_orbitals.tex:383` | `analog-ladder-filter.md:52` | **UNVERIFIED** | yes |  | Mirror the dated stamp (verbatim text exists at de-broglie-standing-wave.md:52 and TeX:383) onto analog-ladder-filter.md:52. Caveat: the TeX % row list tags ':383 ... [banked uncertain]' (TeX:4271) —… |
| 94 | ch07-A | MEDIUM | CONTRA (regime): print resultbox 'The Regime IV Vacuum Yiel… | `07_quantum_mechanics_and_orbitals.tex:488` | `de-broglie-n.md:10` | **UNVERIFIED** | no |  | Ruling needed: the Regime IV yield-boundary resultbox has no KB home and contradicts the canonical leaf and the chapter's own Step 2(b); either banner it in print or home+grade it in the KB. Also not… |
| 95 | ch07-A | MEDIUM | WB-LAG (re-scope): print asserts (TeX:725-726) 'winding num… | `07_quantum_mechanics_and_orbitals.tex:725` | `de-broglie-standing-wave.md:240` | **UNVERIFIED** | no |  | Print the mode-count/topological-winding terminology note (or a footnote to def-quant3) at TeX:725-726; def-quant3 is not yet a ratified corrigendum, so this needs a ruling on wording rather than a v… |
| 96 | ch07-A | MEDIUM | KB-INTERNAL (three He-IE precision figures, none bannered):… | `07_quantum_mechanics_and_orbitals.tex:253` | `chiral-factor.md:28` | **UNVERIFIED** | no |  | Ruling needed: label the two architectures' He-IE results distinctly (MCL 24.19 vs bonding-mode 24.37) and either substantiate or strike the 0.008% cell in chiral-factor.md:28 (and its print twin TeX… |
| 97 | ch07-A | LOW | KB-INTERNAL (twin-consistent with print, but conflicts with… | `07_quantum_mechanics_and_orbitals.tex:173` | `ode-verification.md:49` | **UNVERIFIED** | no |  | Fold into the M7 regime ruling: decide whether the r < a_0 core is Regime II (yield) or deep Regime I and reconcile the three leaves + TeX:173/:485-488/:938. |
| 98 | ch07-A | LOW | DEAD-ANCHOR in print (pointer to a comment-only target): th… | `07_quantum_mechanics_and_orbitals.tex:41` | `de-broglie-standing-wave.md:267` | **UNVERIFIED** | yes |  | Un-comment (print) the batch-2a note at TeX:4204-4290, or re-point the three stamps at the % comment. The note's text already exists verbatim (markup-reduced) as the KB banner at de-broglie-standing-… |
| 99 | ch07-A | MEDIUM | TEX-ONLY overclaim vs leaf grade: the KB twin paragraph dro… | `07_quantum_mechanics_and_orbitals.tex:333` | `helium-symmetric-cavity.md:80` | **UNVERIFIED** | no |  | Route to core with the vol2 ch11 protein items (revalidation: 11:123 N13 protein NEGATIVE un-propagated): caveat or strike 'Tier-1 derivation status' in print to match clm-w6kk5y:381. |
| 100 | ch07-A | LOW | CONTRA / diverged (pipeline definition): print Phase A = si… | `07_quantum_mechanics_and_orbitals.tex:214` | `helium-symmetric-cavity.md:32` | **UNVERIFIED** | no |  | Ruling needed on which pipeline decomposition is canonical; at minimum disambiguate the overloaded 'Phase A/B/C' labels between TeX:214-233 and ionization-energy-validation.md:11. |
| 101 | ch07-C | MEDIUM | CONTRA — eq:kappa_hopf: print carries a sign-alternating pa… | `07_quantum_mechanics_and_orbitals.tex:3288` | `radial-eigenvalue-solver.md:731` | **UNVERIFIED** | no |  | Route for ruling; not mechanical. Facts for the ruler: git log -L shows TeX 3288 and KB 731 both unchanged since initial release de9d2293 (2026-04-13) — the leaf was never verbatim at this spot. The … |
| 102 | ch07-C | MEDIUM | CONTRA — 'Hopf link back-EMF' bullet: print (3318-3329) ass… | `07_quantum_mechanics_and_orbitals.tex:3323` | `radial-eigenvalue-solver.md:741` | **UNVERIFIED** | no |  | Same ruling as M1 (companion prose to the parity factor). Print's Period-3 claim ('and natively resolves the Period-3 binding' at 3328) has no KB home anywhere in ave-kb (grep 'Inductive Drag' / 'Per… |
| 103 | ch07-C | MEDIUM | KB-INTERNAL (also print-internal) — E2k (TeX 3200 '(all she… | `07_quantum_mechanics_and_orbitals.tex:3306` | `radial-eigenvalue-solver.md:739` | **UNVERIFIED** | no |  | The correction exists in print (3611) and KB (scale-separation.md:35) as an undated 'Note:' at the OTHER site only; the E2k site still presents same-n CDF screening as the architecture. Candidate for… |
| 104 | ch07-C | MEDIUM | KB-INTERNAL (also print-internal) — the E2 Summary box (TeX… | `07_quantum_mechanics_and_orbitals.tex:2728` | `dual-formalism-architecture.md:21` | **UNVERIFIED** | no |  | Ruling needed on whether the Y->S half of the Dual-Formalism box is historical (then it needs a dated superseded banner at TeX 2711-2737 and dual-formalism-architecture.md:10) or still standing (then… |
| 105 | ch07-C | MEDIUM | KB-INTERNAL (also print-internal) — Li IE printed as 5.32 e… | `07_quantum_mechanics_and_orbitals.tex:3136` | `radial-eigenvalue-solver.md:689` | **UNVERIFIED** | no | vol2/claim-quality.md clm-oltvwy:348 (derived sid… | Sidecar already instructs 'Treat the ±2.8% headline as the validated solver bound' and lists 'Reconcile the Li per-element residual' as strengthen-by. Leaf-level: a dated cross-note at radial-eigenva… |
| 106 | ch07-C | LOW | KB-INTERNAL (also print-internal) — Be printed as 8.21 eV /… | `07_quantum_mechanics_and_orbitals.tex:3138` | `radial-eigenvalue-solver.md:690` | **UNVERIFIED** | no | vol2/claim-quality.md clm-oltvwy:347,:364 and clm… | Narrative-stage snapshot: E2k (TeX 3152-3164) immediately calls the E2d-E2j architecture 'the fundamental problem', so the table is partially self-disclosed by narrative, but not by any dated marker.… |
| 107 | ch07-C | LOW | KB-INTERNAL — three unreconciled He first-IE precisions acr… | `07_quantum_mechanics_and_orbitals.tex:3134` | `radial-eigenvalue-solver.md:688` | **UNVERIFIED** | no |  | The 24.19 vs 24.37 pair are different methods (MCL vs Hopf-link circuit) and may coexist by design; the '0.008%' at chiral-factor.md:28 / TeX 3851 (ch07-D) matches neither and is the outlier to route… |


#### Fragments + verifier notes

**1. CH01A-M1** (ch01-A, UNVERIFIED)
- print `01_topological_matter.tex:35` — `Mass is the stored inductive energy required to maintain the topological integrity of the standing wave.`
- KB `newtonian-inertia-as-lenz.md:14` — `> **🔴 STORED INDUCTIVE ENERGY = the FLYWHEEL (spin/frequency-regulation), the REST MASS *store* is A1 (2026-06-20, Rule 12 — body above PRESERVED unedited; Grant-ratified mass-sector ruling).**`
- verifiers: 

**2. CH01A-M2** (ch01-A, UNVERIFIED)
- print `01_topological_matter.tex:8` — `\item Understand how mass emerges macroscopically from the continuous distributed inductance of closed optical loops (Lenz's Law).`
- KB `newtonian-inertia-as-lenz.md:14` — `the re-scope only re-labels *which sector stores the rest mass* (A1, not the inductive flywheel)`
- verifiers: 

**3. CH01A-M3** (ch01-A, UNVERIFIED)
- print `01_topological_matter.tex:207` — `Neutrino ($\nu$)           & Twisted unknot      & I--II boundary & Chiral phase below yield \\`
- KB `index.md:13` — `The closed-loop framing has been **superseded** by the Cosserat torsional screw-dislocation model`
- verifiers: 

**4. CH01A-M4** (ch01-A, UNVERIFIED)
- print `01_topological_matter.tex:207` — `Neutrino ($\nu$)           & Twisted unknot      & I--II boundary & Chiral phase below yield \\`
- KB `regime-classification.md:15` — `\| Neutrino ($\nu$) \| Twisted unknot \| I--II boundary \| Chiral phase below yield \|`
- verifiers: 

**5. CH01A-M5** (ch01-A, UNVERIFIED)
- print `01_topological_matter.tex:209` — `Proton ($p$)               & $(2,5)$ phase portrait & II (Yield)    & $6^3_2$ Borromean linkage at saturation \\`
- KB `regime-classification.md:17` — `\| Proton ($p$) \| $(2,5)$ Cinquefoil \| II (Yield) \| Borromean linkage at saturation \|`
- verifiers: 

**6. CH01A-M6** (ch01-A, UNVERIFIED)
- print `01_topological_matter.tex:242` — `An electron ($e^-$) is a right-handed unknot; a positron ($e^+$) is physically identical, but wound as a left-handed unknot.`
- KB `chirality-and-antimatter.md:10` — `the electron ($e^-$) carries **left-handed** Beltrami helicity (the LH content of the confined flux, per [`pair-production-axiom-derivation.md`](pair-production-axiom-derivation.md):27,79); the posit…`
- verifiers: 

**7. CH01A-M7** (ch01-A, UNVERIFIED)
- print `01_topological_matter.tex:248` — `previously trapped within the closed LC resonance of the Hopfion, unwinds`
- KB `chirality-and-antimatter.md:18` — `previously trapped within the closed LC resonance of the $0_1$ unknot, unwinds`
- verifiers: 

**8. CH01A-M8** (ch01-A, UNVERIFIED)
- print `01_topological_matter.tex:259` — `A spatial solver demonstrating how a propagating Transverse EM Wave winds into a stationary Spin-1 helical loop when encountering extreme localised network impedance ($Z \to Z_{crit}$). The discrete …`
- KB `electron-identification.md:64` — `The genesis / self-lock arc that would *dynamically create* the fluxoid from a free precursor is **closed-negative** (electron-genesis-from-free-precursor leans-falsified; the engine pumps H at $dt\t…`
- verifiers: 

**9. CH01A-M9** (ch01-A, UNVERIFIED)
- print `01_topological_matter.tex:79` — `\kbleaf{ave-kb/vol2/particle-physics/ch01-topological-matter/electron-identification.md} (the $g=2$`
- KB `electron-identification.md:92` — `The honest stance is canonical at [`translation-circuit.md`](../../../common/translation-tables/translation-circuit.md):637 ("$g = 2$ is POSITED, not derived").`
- verifiers: 

**10. CH01A-M10** (ch01-A, UNVERIFIED)
- print `01_topological_matter.tex:55` — `%      translation-circuit.md:767 ("**$g = 2$ is POSITED, not derived**"; the sweep's kb_truth`
- KB `translation-circuit.md:839` — `- **$g = 2$ is POSITED, not derived** (`ave-evidence-framing-discipline`); the anomalous part $a_e = \alpha/2\pi$ is the slip (§10.2/§10.3), but the leading $g=2$ is an input.`
- verifiers: 

**11. CH01A-M11** (ch01-A, UNVERIFIED)
- print `01_topological_matter.tex:239` — `All values use $\kappa_{FS} = 8\pi(1 - 1/(14\pi^2))$ from \texttt{ave.core.constants} with zero empirical fits.`
- KB `torus-knot-ladder.md:21` — `but **which particle occupies each rung** — the "Particle (real-space body)" column — is an **imported identification** (electron ↔ $(2,3)$, proton ↔ $(2,5)$, …), not substrate-forced. The rung STRUC…`
- verifiers: 

**12. CH01A-M12** (ch01-A, UNVERIFIED)
- print `01_topological_matter.tex:227` — `$(2,3)$ trefoil ($3_1$)    & 3  & $8.317\,\ell_{node}$ & SU(2) & Electron ($0_1$ unknot) \\`
- KB `torus-knot-ladder.md:10` — `so $r_{opt}$ is a **pure number, NOT a length** (the $\ell_{node}$ units previously attached to it were spurious)`
- verifiers: 

**13. CH01A-M13** (ch01-A, UNVERIFIED)
- print `01_topological_matter.tex:40` — `feed into each other in a closed topological loop ($\nabla \times \mathbf{A} = k\mathbf{A}$), permanently trapping the energy.`
- KB `electron-unknot.md:13` — `🔴 *(2026-06-24: "permanently trapping the energy" is **topology-pinned** (the closed Beltrami loop / Ax2 winding) + boundary, NOT a bulk self-focusing well — the bulk self-trap is a Cartesian artifac…`
- verifiers: 

**14. CH01A-M14** (ch01-A, UNVERIFIED)
- print `01_topological_matter.tex:244` — `The AVE framework resolves this mathematical paradox via \textbf{Optical Phase Cancellation}.`
- KB `chirality-and-antimatter.md:28` — `> **Tag (peer, not chord).** The observable $2\gamma$ at $2 m_e c^2 = 1.022$ MeV is the **standard-QED result** — AVE claims **no** distinct cross-section, branching ratio, or kinematic distribution …`
- verifiers: 

**15. CH01A-M15** (ch01-A, UNVERIFIED)
- print `01_topological_matter.tex:147` — `The minimum discrete diameter of the flux tube is normalised to one fundamental lattice pitch ($d \equiv 1 l_{node}$).`
- KB `electron-unknot.md:59` — `The minimum discrete diameter of the flux tube is normalised to one fundamental lattice pitch ($d \equiv 1 l_{node}$).`
- verifiers: 

**16. CH01A-M16** (ch01-A, UNVERIFIED)
- print `01_topological_matter.tex:16` — `stable particles are defined as finite-energy soliton solutions to the generalised \textbf{Faddeev-Skyrme Energy Functional}`
- KB `mathematical-topology-of-mass.md:20` — `> **Peer + finiteness note.** The Faddeev-Skyrme energy functional is **standard soliton field theory** (Faddeev–Niemi / Skyrme), imported here as calculational scaffolding — **peer-with-standard**, …`
- verifiers: 

**17. ch01C-M1** (ch01-C, UNVERIFIED)
- print `01_topological_matter.tex:35` — `Mass is the stored inductive energy required to maintain the topological integrity of the standing wave.`
- KB `newtonian-inertia-as-lenz.md:14` — `> **🔴 STORED INDUCTIVE ENERGY = the FLYWHEEL (spin/frequency-regulation), the REST MASS *store* is A1 (2026-06-20, Rule 12 — body above PRESERVED unedited; Grant-ratified mass-sector ruling).**`
- verifiers: 

**18. ch01C-M2** (ch01-C, UNVERIFIED)
- print `01_topological_matter.tex:33` — `Under the Topo-Kinematic isomorphism, inductance maps to mass ($[L] \equiv [M]$).`
- KB `newtonian-inertia-as-lenz.md:14` — `the **stored inductive energy is the FLYWHEEL** spin / frequency-regulation energy of the T2 / Cosserat micro-rotation ($\omega$) sector`
- verifiers: 

**19. ch01C-M3** (ch01-C, UNVERIFIED)
- print `01_topological_matter.tex:266` — `\item Inertial mass ($m$) is derived classically from distributed continuous inductance ($L$), where acceleration generates a back-EMF (Lenz's Law).`
- KB `newtonian-inertia-as-lenz.md:14` — `the re-scope only re-labels *which sector stores the rest mass* (A1, not the inductive flywheel). Body preserved per Rule-12.`
- verifiers: 

**20. ch01C-M4** (ch01-C, UNVERIFIED)
- print `01_topological_matter.tex:8` — `\item Understand how mass emerges macroscopically from the continuous distributed inductance of closed optical loops (Lenz's Law).`
- KB `newtonian-inertia-as-lenz.md:14` — `**not** the rest-mass *store* — which is the orthogonal **A1 longitudinal DILATATION** depression`
- verifiers: 

**21. ch01C-M5** (ch01-C, UNVERIFIED)
- print `01_topological_matter.tex:148` — `The minimum discrete diameter of the flux tube is normalised to one fundamental lattice pitch ($d \equiv 1 l_{node}$).`
- KB `common-mode-twist-ledger.md:235` — `> **They differ by $\pi$ on the tube diameter and by $2\pi$ on the circumference. They cannot both be right.**`
- verifiers: 

**22. ch01C-M6** (ch01-C, UNVERIFIED)
- print `01_topological_matter.tex:40` — `undergoes macroscopic \textbf{gyroscopic precession} in the presence of an external magnetic field`
- KB `spin-gyroscopic-isomorphism.md:45` — `(the extended core is $\sim\ell_{node} \approx 3.86\times10^{-13}$ m — subatomic, **not** macroscopic)`
- verifiers: 

**23. M1** (ch02, UNVERIFIED)
- print `02_baryon_sector.tex:319` — `generates a discrete CP-violating $\theta$-vacuum phase`
- KB `topological-fractionalization.md:60` — `adjective is UNDERIVED — and its opposite is asserted elsewhere.`
- verifiers: 

**24. M2** (ch02, UNVERIFIED)
- print `02_baryon_sector.tex:357` — `This elastic expansion tension is the proposed structural origin of (and provides an upper-bound estimate for) the mass surplus`
- KB `proton-neutron-mass-split.md:10` — `This elastic expansion tension accounts for the mass surplus the neutron possesses relative to the bare proton.`
- verifiers: 

**25. M3** (ch02, UNVERIFIED)
- print `02_baryon_sector.tex:357` — `\kbleaf{ave-kb/vol2/particle-physics/ch02-baryon-sector/neutron-identification.md} :52`
- KB `neutron-identification.md:52` — `### §2.1 — Why the mass split is structurally bounded (without being derived)`
- verifiers: 

**26. M4** (ch02, UNVERIFIED)
- print `02_baryon_sector.tex:357` — `This elastic expansion tension is the proposed structural origin of (and provides an upper-bound estimate for) the mass surplus`
- KB `neutron-identification.md:23` — `(per `vol_2_subatomic/chapters/02_baryon_sector.tex:294`)`
- verifiers: 

**27. M5** (ch02, UNVERIFIED)
- print `02_baryon_sector.tex:362` — `The elastic expansion required to accommodate the threaded electron is the proposed structural origin of the $1.293$ MeV mass surplus`
- KB `neutron-identification.md:25` — `(`02_baryon_sector.tex:299`): "The elastic expansion required to accommodate the threaded electron accounts for the $1.293$ MeV mass surplus of the neutron over the proton."`
- verifiers: 

**28. M6** (ch02, UNVERIFIED)
- print `02_baryon_sector.tex:131` — `covers the baryon ladder through crossing number $c = 15$ with maximum error $\sim 2.4\%$`
- KB `thermal-softening.md:37` — `validates the baryon ladder through crossing number $c = 15$ with maximum error $2.4\%$`
- verifiers: 

**29. M7** (ch02, UNVERIFIED)
- print `02_baryon_sector.tex:463` — `The exact proton to electron mass ratio ($1836.15$) is derived via a non-linear eigenvalue extraction of the Faddeev-Skyrme energy functional`
- KB `proton-identification.md:73` — `**THE headline claim is the $+0.74\%$ bare-topology emergence result; the $-0.002\%$ is $\delta_{th}$-riding precision, NOT the headline**`
- verifiers: 

**30. M8** (ch02, UNVERIFIED)
- print `02_baryon_sector.tex:60` — `The empirical mass ratio $m_p/m_e \approx 1836.15$ emerges dynamically as the exact eigenvalue of non-linear inductive resonance.`
- KB `proton-identification.md:73` — `**THE headline claim is the $+0.74\%$ bare-topology emergence result; the $-0.002\%$ is $\delta_{th}$-riding precision, NOT the headline**`
- verifiers: 

**31. M9** (ch02, UNVERIFIED)
- print `02_baryon_sector.tex:7` — `Evaluate the precise derivation of the proton-to-electron mass ratio ($1836.15$) from the non-linear Faddeev-Skyrme energy functional.`
- KB `proton-identification.md:13` — `**the proton's mass ratio $m_p/m_e = 1836.12$ is derived with zero baryon-data-tuned parameters**`
- verifiers: 

**32. M10** (ch02, UNVERIFIED)
- print `02_baryon_sector.tex:297` — `$(2,15)$ & 15 & 2478  & $\Delta(2420)$ & 2420  & $+2.40\%$`
- KB `torus-knot-ladder-baryons.md:30` — `\| $(2,15)$ \| 15 \| 2477.968 \| $\Delta(2420)$ \| 2400 ± 100 \| $+3.249\%$ \| $11/2^+$ ✓ \|`
- verifiers: 

**33. M11** (ch02, UNVERIFIED)
- print `02_baryon_sector.tex:314` — `its $+9.8\%$ deviation from $\Delta(2420)$ indicates higher-order corrections`
- KB `torus-knot-ladder-baryons.md:30` — `\| $(2,15)$ \| 15 \| 2477.968 \| $\Delta(2420)$ \| 2400 ± 100 \| $+3.249\%$ \| $11/2^+$ ✓ \|`
- verifiers: 

**34. M12** (ch02, UNVERIFIED)
- print `00_title.tex:18` — `the proton/electron mass ratio ($\approx 1836.14$)`
- KB `proton-identification.md:13` — `**the proton's mass ratio $m_p/m_e = 1836.12$ is derived with zero baryon-data-tuned parameters**`
- verifiers: 

**35. M13** (ch02, UNVERIFIED)
- print `02_baryon_sector.tex:466` — `The Hierarchy Problem is strictly resolved: Gravity is shown by algebraic substitution (given the value-fitted $G$ input)`
- KB `proton-neutron-mass-split.md:89` — `The $\sim 10^{40}$ gap between the strong force and gravity (the Hierarchy Problem) is the kinematic dilution`
- verifiers: 

**36. M14** (ch02, UNVERIFIED)
- print `02_baryon_sector.tex:238` — `the topological packing limit ($p_c \approx 0.1834$) derived in Chapter 2`
- KB `self-consistent-mass-oscillator.md:30` — `the topological packing limit ($p_c \approx 0.1834$) derived in Chapter 2`
- verifiers: 

**37. M1** (ch03, UNVERIFIED)
- print `03_neutrino_sector.tex:227` — `\item $\pi$: The base torsional half-turn of the $0_1$ unknot phase winding.`
- KB `delta-cp-violation.md:22` — `the neutrino is an open helix in the torsional sector, *not* a closed unknot phase winding`
- verifiers: 

**38. M2** (ch03, UNVERIFIED)
- print `03_neutrino_sector.tex:272` — `Neutrinos are structurally defined as $0_1$ twisted unknots. Because they have zero self-crossings, their topological Skyrme gradient vanishes`
- KB `index.md:13` — `Corrigendum (2026-05-06 session): Earlier editions described the neutrino as a "$0_1$ twisted unknot" (closed loop)`
- verifiers: 

**39. M3** (ch03, UNVERIFIED)
- print `03_neutrino_sector.tex:274` — `Neutrino oscillation is the classical dispersive beat frequency of the three distinct $0_1$ mass eigenstates`
- KB `index.md:13` — `Any remaining "twisted unknot" prose in cross-references should be read as the obsolete framing`
- verifiers: 

**40. M4** (ch03, UNVERIFIED)
- print `03_neutrino_sector.tex:159` — `the trefoil has $c = 3$ crossings \textit{because} the K4 lattice is 3-connected`
- KB `chiral-screening.md:35` — `Connectivity = trefoil crossing number: ASSERTED -- and in tension with canon`
- verifiers: 

**41. M5** (ch03, UNVERIFIED)
- print `03_neutrino_sector.tex:250` — `All four PMNS parameters derive from three inputs: the torus knot crossing numbers ($c_1 = 5$, $c_3 = 9$)... No curve fitting is used`
- KB `delta-cp-violation.md:38` — `c_1=5 starting value of mode-space ladder is NOT derived from substrate primitives in any canonical leaf grep'd`
- verifiers: 

**42. M6** (ch03, UNVERIFIED)
- print `01_topological_matter.tex:207` — `Neutrino ($\nu$)           & Twisted unknot      & I--II boundary & Chiral phase below yield \\`
- KB `index.md:13` — `Any remaining "twisted unknot" prose in cross-references should be read as the obsolete framing`
- verifiers: 

**43. M7** (ch03, UNVERIFIED)
- print `00_title.tex:14` — `neutrons as dispersive twisted $0_1$ unknots, bound by the Faddeev-Skyrme energy functional`
- KB `index.md:13` — `The closed-loop framing has been **superseded** by the Cosserat torsional screw-dislocation model`
- verifiers: 

**44. M8** (ch03, UNVERIFIED)
- print `03_neutrino_sector.tex:122` — `the $\nu_3$ baryon-partner label was updated $\Delta(1620) \to \Delta(1600)$`
- KB `claim-quality.md:251` — `$\nu_3$ with $\Delta(1620)$ $(2,9)$`
- verifiers: 

**45. ch04-M1** (ch04, UNVERIFIED)
- print `04_quantum_spin.tex:81` — `:407 "Does NOT claim a violation of standard QM predictions`
- KB `claim-quality.md (clm-salw2h):408` — `Does NOT claim a violation of standard QM predictions for spin-dependent observables`
- verifiers: 

**46. ch04-M2** (ch04, UNVERIFIED)
- print `04_quantum_spin.tex:111` — `standard QM fails to make. Canonical: \kbleaf{ave-kb/vol2/claim-quality.md} (\texttt{clm-salw2h},`
- KB `larmor-derivation.md:61` — `](../../claim-quality.md):407–410, `clm-salw2h` *Specific Non-Claims and Caveats*; solidity $0.70$ at :419)`
- verifiers: 

**47. ch04-M3** (ch04, UNVERIFIED)
- print `04_quantum_spin.tex:111` — `standard QM fails to make. Canonical: \kbleaf{ave-kb/vol2/claim-quality.md} (\texttt{clm-salw2h},`
- KB `visual-equivalence.md:22` — `](../../claim-quality.md):407–410, `clm-salw2h` *Specific Non-Claims and Caveats*; solidity $0.70$ at :419)`
- verifiers: 

**48. ch04-M4** (ch04, UNVERIFIED)
- print `04_quantum_spin.tex:62` — `representing the $3_1$ electron knot`
- KB `larmor-derivation.md:10` — `the electron is the $0_1$ unknot in real space`
- verifiers: 

**49. ch04-M5** (ch04, UNVERIFIED)
- print `04_quantum_spin.tex:94` — `so the scoping currently lives ONLY in the clm-salw2h register and has propagated to neither the`
- KB `larmor-derivation.md:57` — `> **[2026-08-02 — scope of the equivalence, per `clm-salw2h`; KB-lockstep with the merged print correction]**`
- verifiers: 

**50. ch04-M6** (ch04, UNVERIFIED)
- print `04_quantum_spin.tex:6` — `Define Quantum Spin ($1/2\hbar$) structurally as the macroscopic angular momentum`
- KB `index.md:11` — `Quantum Spin ($1/2\hbar$) is derived as the macroscopic angular momentum`
- verifiers: 

**51. ch05-M01** (ch05, UNVERIFIED)
- print `05_electroweak_gauge_theory.tex:83` — `Substituting the trace-reversed operating point $\nu_{\text{Hill}} \equiv 2/7$ (the isotropic Voigt--Reuss--Hill average at the GR-imported $K = 2G$ point --- an averaging choice, not a lattice-emerg…`
- KB `weinberg-angle.md:26` — `> Substituting the trace-reversed topological lattice limit $\nu_{vac} \equiv 2/7$:`
- verifiers: 

**52. ch05-M02** (ch05, UNVERIFIED)
- print `05_electroweak_gauge_theory.tex:81` — `Applying the standard isotropic relation $E = 2G(1+\nu_{\text{Hill}})$ maps the stiffness entirely to the geometric vacuum Poisson ratio:`
- KB `weinberg-angle.md:20` — `> Applying the standard isotropic relation $E = 2G(1+\nu_{vac})$ maps the stiffness entirely to the geometric vacuum Poisson ratio:`
- verifiers: 

**53. ch05-M03** (ch05, UNVERIFIED)
- print `05_electroweak_gauge_theory.tex:115` — `The $\alpha^2$ scaling is thus the intermodulation product of two Axiom~4 varactor couplings, not a Feynman two-vertex loop.`
- KB `weak-coupling.md:30` — `The self-energy is a **two-vertex process** (second-order perturbation theory):`
- verifiers: 

**54. ch05-M04** (ch05, UNVERIFIED)
- print `05_electroweak_gauge_theory.tex:103` — `The factor $\alpha^2$ is the product of \textbf{two Axiom~4 susceptibility couplings}.`
- KB `weak-coupling.md:22` — `The factor $\alpha^2$ is derived from the interaction Lagrangian.`
- verifiers: 

**55. ch05-M05** (ch05, UNVERIFIED)
- print `05_electroweak_gauge_theory.tex:104` — `\begin{resultbox}{Torsional-EM Susceptibility Coupling}`
- KB `weak-coupling.md:24` — `> **[Resultbox]** *Torsional-EM Interaction Lagrangian*`
- verifiers: 

**56. ch05-M06** (ch05, UNVERIFIED)
- print `05_electroweak_gauge_theory.tex:35` — `(\kbleaf{ave-kb/common/vocabulary-register.md}, \texttt{def-l0ngdu})`
- KB `gauge-boson-masses.md:34` — ``:870`, `def-l0ngdu``
- verifiers: 

**57. ch05-M07** (ch05, UNVERIFIED)
- print `05_electroweak_gauge_theory.tex:51` — `(\kbleaf{ave-kb/common/vocabulary-register.md}, \texttt{def-l0ngdu}): the mechanical dilatation $\nabla\cdot\mathbf{u}$ is \textbf{dynamical}`
- KB `gauge-boson-masses.md:42` — ``:867` (`def-l0ngdu`; the quoted clauses below are at `:870`)`
- verifiers: 

**58. ch05-M08** (ch05, UNVERIFIED)
- print `05_electroweak_gauge_theory.tex:33` — `to the mass flow introduces a uniform, irrotational velocity potential`
- KB `gauge-boson-masses.md:48` — ``:882`, `def-uatk1s``
- verifiers: 

**59. ch05-M09** (ch05, UNVERIFIED)
- print `06_temperature_characteristics.tex:79` — `(canonical \kbleaf{gauge-boson-masses.md:39})`
- KB `gauge-boson-masses.md:39` — `>`
- verifiers: 

**60. ch05-M10** (ch05, UNVERIFIED)
- print `05_electroweak_gauge_theory.tex:175` — `\item Gauge Invariance is explicitly derived as the macroscopic consequence of the classical Helmholtz Decomposition: shifting the irrotational coordinate velocity of the LC grid ($\nabla \Lambda$) w…`
- KB `gauge-boson-masses.md:83` — `only the residual time-independent family is derived here, and canon holds **no valid derivation of any full U(1) family**`
- verifiers: 

**61. ch05-M11** (ch05, UNVERIFIED)
- print `05_electroweak_gauge_theory.tex:8` — `\item Derive the physical origin of Gauge Invariance (U(1)) as the classical network-dynamic freedom to shift the irrotational background coordinate velocity via Helmholtz Decomposition.`
- KB `gauge-boson-masses.md:34` — `What this leaf therefore derives is the **residual, time-independent** gauge family`
- verifiers: 

**62. ch05-M12** (ch05, UNVERIFIED)
- print `05_electroweak_gauge_theory.tex:178` — `\item $U(1)$ and $SU(3)$ Gauge symmetries are explicitly proven to map identically onto the discrete geometric Plaquette Action and the $\mathbb{Z}_3$ Borromean Linkage permutation group, respectivel…`
- KB `claim-quality.md:817` — `but is not a uniqueness theorem`
- verifiers: 

**63. ch05-M13** (ch05, UNVERIFIED)
- print `05_electroweak_gauge_theory.tex:159` — `\textbf{U(1) Electromagnetism} is therefore the enforcement of unitary topological continuity across the discrete graph`
- KB `forward-to-ch6.md:40` — `**U(1) Electromagnetism** is therefore the enforcement of unitary topological continuity across the discrete graph`
- verifiers: 

**64. ch05-M14** (ch05, UNVERIFIED)
- print `05_electroweak_gauge_theory.tex:51` — `\textbf{[DEMOTED 2026-08-11 --- R40-B2a: NEEDS RE-DERIVATION, not dead; dated note at the end of this file]}`
- KB `gauge-boson-masses.md:131` — `## R40 batch-2a — [NEEDS-RE-DERIVATION status-note heading] (2026-08-11)`
- verifiers: 

**65. ch05-M15** (ch05, UNVERIFIED)
- print `05_electroweak_gauge_theory.tex:51` — `\noindent\textbf{Premise note (2026-08-03).} The step above deliberately does \emph{not} assume an incompressible substrate.`
- KB `gauge-boson-masses.md:38` — `> **Why the old premise was false.** It read *"Because the vacuum substrate is incompressible ($K = 2G$) …"*.`
- verifiers: 

**66. M1** (ch06-A, UNVERIFIED)
- print `06_electroweak_and_higgs.tex:17` — `corresponds to a transient acoustic mode---a topological node undergoing rapid structural relaxation upon high-energy impact`
- KB `claim-quality.md:162` — `The empirical $125$ GeV LHC resonance is interpreted as a **transient acoustic relaxation mode** of the LC network, not a fundamental scalar field excitation. 🔴 **[DEMOTED 2026-08-11 — R40-B2a: NEEDS…`
- verifiers: 

**67. M2** (ch06-A, UNVERIFIED)
- print `06_electroweak_and_higgs.tex:363` — `A channel is \emph{compliant} if $\Delta c \le \Delta c_\text{crit} = 3$ --- the K4 lattice connectivity itself (three bonds per node, each transferring at most one torsional unit per interaction), w…`
- KB `chiral-screening.md:35` — `**Connectivity = trefoil crossing number: ASSERTED — and in tension with canon.**`
- verifiers: 

**68. M3** (ch06-A, UNVERIFIED)
- print `06_electroweak_and_higgs.tex:210` — `$W$    & $M_W^{\text{tree}} / (1 - \|S_{11}^{\text{sc}}\|^2)$  & 80,224 MeV  & 80,379 MeV  & $-0.19\%$ \\`
- KB `lepton-spectrum.md:81` — `\| $W$ \| $m_e/(\alpha^2 p_c \sqrt{3/7})$ \| 79,923 MeV \| 80,379 MeV \| $-0.57\%$ \|`
- verifiers: 

**69. M4** (ch06-A, UNVERIFIED)
- print `06_electroweak_and_higgs.tex:321` — `$\nu_1$ & $(2,5)$ & 5 &  $0.1324$ & $9.58$ \\`
- KB `higgs-mass.md:29` — `\| $\nu_1$ \| Proton $(2,5)$ \| 5 \| $\sim 24$ \|`
- verifiers: 

**70. M5** (ch06-A, UNVERIFIED)
- print `06_electroweak_and_higgs.tex:193` — `m_e \xrightarrow{\alpha\sqrt{3/7}} m_\mu \xrightarrow{\alpha \cdot p_c} m_\tau \xrightarrow{\alpha \cdot p_c} M_W`
- KB `lepton-spectrum.md:73` — `m_e \xrightarrow{\text{torsion: }\alpha\sqrt{3/7}} m_\mu \xrightarrow{\text{bending: }p_c/\alpha^2} m_\tau \xrightarrow{\text{+2nd vertex: }\alpha} M_W`
- verifiers: 

**71. M6** (ch06-A, UNVERIFIED)
- print `sm-ave-translation.md:10` — `Source: `\input{../common/translation_particle_physics.tex}` in `vol_2_subatomic/chapters/06_electroweak_and_higgs.tex`, line 305.`
- KB `06_electroweak_and_higgs.tex:860` — `\input{../common/translation_particle_physics.tex}`
- verifiers: 

**72. M7** (ch06-A, UNVERIFIED)
- print `higgs-mechanism.md:54` — `<!-- 🔴 OPEN FLAG (Rule 12): the "torsion-shear / PAT" label on $\sqrt{3/7}$ is contested`
- KB `lepton-spectrum.md:29` — `> **🔴 OPEN FLAG (Rule 12 — `√(3/7)` "PAT torsion-shear" label; Grant's physics adjudication pending.`
- verifiers: 

**73. M8** (ch06-A, UNVERIFIED)
- print `06_electroweak_and_higgs.tex:422` — `Four lemmas are proven from Axioms~1 and~4 (see\linebreak \kbleaf{p2.9b\_goldstone\_proof.md}):`
- KB `verify-md-links.py:808` — `"manuscript/vol_2_subatomic/chapters/06_electroweak_and_higgs.tex",         r"p2.9b\_goldstone\_proof.md",`
- verifiers: 

**74. M1** (ch06-B, UNVERIFIED)
- print `06_electroweak_and_higgs.tex:723` — `(:12/:14 the two-stage split, :92/:100/:103 the values, :121 the postulate-conditional cell).`
- KB `q-g19a-petermann-saliency-closure.md:121` — `> **Consequence: the dispute recorded above dissolves.**`
- verifiers: 

**75. M2** (ch06-B, UNVERIFIED)
- print `06_electroweak_and_higgs.tex:770` — `(\kbleaf{ave-kb/vol2/particle-physics/ch06-electroweak-higgs/q-g19a-petermann-saliency-closure.md}:110.)`
- KB `q-g19a-petermann-saliency-closure.md:110` — `> shift_idx = int(tau_retard / dt) % n_t`
- verifiers: 

**76. M3** (ch06-B, UNVERIFIED)
- print `06_electroweak_and_higgs.tex:603` — `= \frac{2}{\pi\alpha}\,\langle (S_d - S_q)\,(-\dot{\Sigma}_{\text{near}})\rangle.`
- KB `q-g19a-petermann-saliency-closure.md:173` — `**Inconsistent by exactly 2**, and the consequence is not ppm-scale:`
- verifiers: 

**77. M4** (ch06-B, UNVERIFIED)
- print `06_electroweak_and_higgs.tex:575` — `with $\tau_{\text{retard}} = 1/\omega_C$ (one Compton-loop transit time,`
- KB `q-g19a-petermann-saliency-closure.md:193` — `1. **$\tau_{\text{retard}} = 1/\omega_C$ is asserted, not derived.**`
- verifiers: 

**78. M5** (ch06-B, UNVERIFIED)
- print `06_electroweak_and_higgs.tex:620` — `is invariant under three independent derivative methods (analytic,`
- KB `q-g19a-petermann-saliency-closure.md:164` — `> **Scope note for §"Numerical robustness" above.**`
- verifiers: 

**79. M6** (ch06-B, UNVERIFIED)
- print `06_electroweak_and_higgs.tex:777` — `\noindent\textbf{Zero parameters were fudged.} The trefoil $(2,3)$,`
- KB `q-g19a-petermann-saliency-closure.md:242` — `> **No fit parameters — *at Stage 1*.**`
- verifiers: 

**80. M7** (ch06-B, UNVERIFIED)
- print `06_electroweak_and_higgs.tex:810` — `The Higgs boson is the radial breathing mode of the K4 unit cell.`
- KB `claim-quality.md (clm-p7rfkb; DERIVED sidecar — NO leaf carries this banner: vol6 lambda-higgs-derivation.md:26 and the ch06 leaves have zero 'R40' hits):162` — `🔴 **[DEMOTED 2026-08-11 — R40-B2a: NEEDS RE-DERIVATION, not dead; dated note at the end of this file]**`
- verifiers: 

**81. M9** (ch06-B, UNVERIFIED)
- print `06_electroweak_and_higgs.tex:860` — `\input{../common/translation_particle_physics.tex}`
- KB `sm-ave-translation.md:10` — `line 305.`
- verifiers: 

**82. M10** (ch06-B, UNVERIFIED)
- print `06_electroweak_and_higgs.tex:833` — `(\texttt{constants.py}, line 338)`
- KB `constants.py (code anchor cited via \kbleaf, not a KB leaf):679` — `M_HIGGS_MEV: float = HIGGS_VEV_MEV / np.sqrt(N_K4)  # = v/2`
- verifiers: 

**83. M11** (ch06-B, UNVERIFIED)
- print `q-g19a-petermann-saliency-closure.md:191` — `**No ppm label on any $C_2$ value in this corpus is defensible**, and every one of them is struck.`
- KB `q-g20f-vacuum-polarization.md:97` — `matches QED at 50 ppm precision **only conditional on the $n_q$-additivity postulate**`
- verifiers: 

**84. M12** (ch06-B, UNVERIFIED)
- print `q-g19a-petermann-saliency-closure.md:191` — `**No ppm label on any $C_2$ value in this corpus is defensible**, and every one of them is struck.`
- KB `q-g27-muon-cosserat-saliency.md:80` — `50 ppm postulate-conditional)](q-g19a-petermann-saliency-closure.md)`
- verifiers: 

**85. M13** (ch06-B, UNVERIFIED)
- print `q-g19a-petermann-saliency-closure.md:8` — `# AVE-Native Petermann Coefficient via Route B: 4% forward (no postulate) → ~~10 ppm at $a_e$~~ **[struck 2026-08-03 per Grant ruling`
- KB `index.md:36` — `(4% forward → 10 ppm with postulate)`
- verifiers: 

**86. M14** (ch06-B, UNVERIFIED)
- print `q-g19a-petermann-saliency-closure.md:221` — `So $\delta = -3\alpha/2$ is a **1-point fit**, not a winding law`
- KB `q-g27-muon-cosserat-saliency.md:71` — `The derivation uses only canonical corpus constants (Vol 2 Ch 6:154–176): no fit parameters.`
- verifiers: 

**87. M15** (ch06-B, UNVERIFIED)
- print `q-g19a-petermann-saliency-closure.md:244` — `(:112, §"What still needs derivation")`
- KB `q-g19a-petermann-saliency-closure.md:131` — `> *Cite-integrity note: this insertion shifts the line numbers of all content below it.`
- verifiers: 

**88. M1** (ch07-A, UNVERIFIED)
- print `07_quantum_mechanics_and_orbitals.tex:46` — `the spatial coordinate metric ($n_s = \frac{9}{7}\varepsilon_{11}$) and the temporal coordinate metric ($n_t = \frac{2}{7}\varepsilon_{11}$)`
- KB `de-broglie-standing-wave.md:58` — `$n_s = 1 + \tfrac{9}{7}\varepsilon_{11}$`
- verifiers: 

**89. M2** (ch07-A, UNVERIFIED)
- print `07_quantum_mechanics_and_orbitals.tex:224` — `\item $2s$ State ($l=0$ penetrating): $E_{bind} = 5.75$ eV`
- KB `orbital-penetration-penalties.md:39` — `\| 2s \| 0 \| Yes — $1/d$ shunt applied \| More negative (tighter bound) \|`
- verifiers: 

**90. M3** (ch07-A, UNVERIFIED)
- print `07_quantum_mechanics_and_orbitals.tex:243` — `The isolated $s^2$ shell loads structurally not as $2.0$, but perfectly as $N_{eff} = 1.0 + 0.5 = 1.5$`
- KB `helium-symmetric-cavity.md:44` — `By applying the Mutual Cavity Loading architecture to Helium's $1s^2$ shell ($N_{eff} = 2.0$), the active engine solver computes the first ionization energy algebraically:`
- verifiers: 

**91. M4** (ch07-A, UNVERIFIED)
- print `07_quantum_mechanics_and_orbitals.tex:277` — `the AVE engine evaluates Beryllium's total ionization energy to \textbf{9.32 eV} entirely free of empirical parameters or tuning coefficients`
- KB `hierarchical-cascade-correction.md:54` — `>     IE_\text{Be, AVE} = 9.28\;\text{eV} \quad (\text{exp: } 9.322\;\text{eV}, \quad \Delta = -0.45\%)`
- verifiers: 

**92. M5** (ch07-A, UNVERIFIED)
- print `07_quantum_mechanics_and_orbitals.tex:324` — `predicting Boron's tightly bound $9.4$~eV Ionization Energy dynamically without fitting parameters`
- KB `subshell-junction-scattering.md:11` — `drops precipitously from Beryllium ($9.32$ eV) to $8.30$ eV`
- verifiers: 

**93. M6** (ch07-A, UNVERIFIED)
- print `07_quantum_mechanics_and_orbitals.tex:383` — `\textbf{[DEMOTED 2026-08-11 --- R40-B2a: NEEDS RE-DERIVATION, not dead; dated note at the end of this file]}`
- KB `analog-ladder-filter.md:52` — `This is *not* 377 $\Omega$. The electron interacts with the vacuum's bulk modulus (acoustic impedance), not the shear modulus (electromagnetic impedance).`
- verifiers: 

**94. M7** (ch07-A, UNVERIFIED)
- print `07_quantum_mechanics_and_orbitals.tex:488` — `the intense core gradients force the localized vacuum ($r_{yield} \approx Z \cdot \alpha^2 A_0$) strictly past the structural \textbf{Regime IV Yield Limit}`
- KB `de-broglie-n.md:10` — `the nuclear voltage $V/V_{\text{yield}} \sim Z\alpha^2 \approx 10^{-4}$ places the entire atom in the linear regime (Axiom 4 check)`
- verifiers: 

**95. M8** (ch07-A, UNVERIFIED)
- print `07_quantum_mechanics_and_orbitals.tex:725` — `The integer $n$ is the \textbf{winding number} of the`
- KB `de-broglie-standing-wave.md:240` — `**Terminology note (mode-count vs topological winding).**`
- verifiers: 

**96. M9** (ch07-A, UNVERIFIED)
- print `07_quantum_mechanics_and_orbitals.tex:253` — `By applying the Mutual Cavity Loading architecture to Helium's $1s^2$ shell ($N_{eff} = 2.0$), the active engine solver computes the first ionization energy algebraically:`
- KB `chiral-factor.md:28` — `\| Atomic (this chapter) \| $J_{s^2} = \frac{1}{2}(1+8\pi\alpha)$ \| He IE to 0.008% \|`
- verifiers: 

**97. M10** (ch07-A, UNVERIFIED)
- print `07_quantum_mechanics_and_orbitals.tex:173` — `$r < a_0$ (inner core) & II (Yield) & $V_{local} \sim V_{yield}$; strong confinement`
- KB `ode-verification.md:49` — `\| $r < a_0$ (inner core) \| II (Yield) \| $V_{local} \sim V_{yield}$; strong confinement \|`
- verifiers: 

**98. M11** (ch07-A, UNVERIFIED)
- print `07_quantum_mechanics_and_orbitals.tex:41` — `\textbf{[DEMOTED 2026-08-11 --- R40-B2a: NEEDS RE-DERIVATION, not dead; dated note at the end of this file]}`
- KB `de-broglie-standing-wave.md:267` — `## R40 batch-2a — [NEEDS-RE-DERIVATION status-note heading] (2026-08-11)`
- verifiers: 

**99. M12** (ch07-A, UNVERIFIED)
- print `07_quantum_mechanics_and_orbitals.tex:333` — `The folding engine achieves Tier-1 derivation status organically because the macroscopic molecular mechanics are simply the expanded $0_1$ limits of the individual atomic AC stators resisting phase d…`
- KB `helium-symmetric-cavity.md:80` — `**Isomorphism to Protein Folding Torsional Limits.**`
- verifiers: 

**100. M13** (ch07-A, UNVERIFIED)
- print `07_quantum_mechanics_and_orbitals.tex:214` — `\paragraph{The 3-Phase Evaluator Pipeline.}`
- KB `helium-symmetric-cavity.md:32` — `**The N-Electron Pipeline.** The atomic solver pipeline invokes three universal scale-invariant operators to compute exact ionization energies without free parameters:`
- verifiers: 

**101. M1** (ch07-C, UNVERIFIED)
- print `07_quantum_mechanics_and_orbitals.tex:3288` — `N_{\rm Hopf} \times \frac{P_C}{2} \times (-1)^{n - l - 1}`
- KB `radial-eigenvalue-solver.md:731` — `\kappa_{\rm Hopf}(r) = N_{\rm Hopf} \times \frac{P_C}{2} \times \sigma_{\rm partner}(r)`
- verifiers: 

**102. M2** (ch07-C, UNVERIFIED)
- print `07_quantum_mechanics_and_orbitals.tex:3323` — `\textbf{Inductive Drag} ($+\kappa$), decreasing`
- KB `radial-eigenvalue-solver.md:741` — `This is *not* a potential in $V_{\rm eff}$---it enters the *denominator* of $k^2(r)$.`
- verifiers: 

**103. M3** (ch07-C, UNVERIFIED)
- print `07_quantum_mechanics_and_orbitals.tex:3306` — `same-$n$ co-radial partners), with`
- KB `radial-eigenvalue-solver.md:739` — `(including same-$n$ co-radial partners)`
- verifiers: 

**104. M4** (ch07-C, UNVERIFIED)
- print `07_quantum_mechanics_and_orbitals.tex:2728` — `Both are needed for multi-electron atoms:`
- KB `dual-formalism-architecture.md:21` — `> Both are needed for multi-electron atoms:`
- verifiers: 

**105. M5** (ch07-C, UNVERIFIED)
- print `07_quantum_mechanics_and_orbitals.tex:3136` — `Li & 3 & P3 + Op2 (ABCD taper) &`
- KB `radial-eigenvalue-solver.md:689` — `\| Li \| 3 \| P3 + Op2 (ABCD taper) \| 5.32 \| $1.2\%$ \|`
- verifiers: 

**106. M6** (ch07-C, UNVERIFIED)
- print `07_quantum_mechanics_and_orbitals.tex:3138` — `Be & 4 & P3 + P2 (ABCD + Hopf) &`
- KB `radial-eigenvalue-solver.md:690` — `\| Be \| 4 \| P3 + P2 (ABCD + Hopf) \| 8.21 \| $11.9\%$ \|`
- verifiers: 

**107. M7** (ch07-C, UNVERIFIED)
- print `07_quantum_mechanics_and_orbitals.tex:3134` — `He & 2 & P2 (circuit, Hopf link) &`
- KB `radial-eigenvalue-solver.md:688` — `\| He \| 2 \| P2 (circuit, Hopf link) \| 24.37 \| $0.9\%$ \|`
- verifiers: 


---

## §3 — Electron-identity corpse pass (F-C1 … F-C11, K4, K6) — vol2 slice

Per-row counts over the slices read so far; 'slices reporting zero hits' is the read receipt for that row in that slice (a full read, not a grep). **No row is discharged by this table** (16 of 175 documents).

| row | live-wrong | Q1 | fence-excluded | Q2 | slices reporting zero hits |
|---|---:|---:|---:|---:|---|
| F-C1 | 0 | 0 | 0 | 0 | ch01-A, ch01-C, ch02, ch03, ch04, ch05, ch06-A, ch06-B, ch07-A, ch07-C, ch08 |
| F-C2 | 0 | 0 | 0 | 0 | ch01-A, ch01-C, ch02, ch03, ch04, ch05, ch06-A, ch06-B, ch07-A, ch07-C, ch08 |
| F-C3 | 0 | 0 | 2 | 0 | ch01-A, ch02, ch03, ch04, ch05, ch06-A, ch06-B, ch07-C, ch08 |
| F-C4 | 0 | 0 | 0 | 0 | ch01-A, ch01-C, ch02, ch03, ch04, ch05, ch06-A, ch06-B, ch07-A, ch07-C, ch08 |
| F-C5 | 0 | 0 | 1 | 0 | ch01-C, ch02, ch03, ch04, ch05, ch06-A, ch06-B, ch07-A, ch07-C, ch08 |
| F-C6 | 0 | 0 | 0 | 0 | ch01-A, ch01-C, ch02, ch03, ch04, ch05, ch06-A, ch06-B, ch07-A, ch07-C, ch08 |
| F-C7 | 1 | 3 | 3 | 0 | ch02, ch03, ch04, ch05, ch06-A, ch06-B, ch07-A, ch07-C, ch08 |
| F-C8 | 0 | 1 | 3 | 0 | ch03, ch04, ch05, ch06-A, ch06-B, ch07-A, ch07-C, ch08 |
| F-C9 | 0 | 0 | 2 | 0 | ch01-C, ch02, ch03, ch04, ch05, ch06-A, ch06-B, ch07-C, ch08 |
| F-C10 | 0 | 0 | 0 | 0 | ch01-A, ch01-C, ch02, ch03, ch04, ch05, ch06-A, ch06-B, ch07-A, ch07-C, ch08 |
| F-C11 | 0 | 2 | 0 | 0 | ch02, ch03, ch04, ch05, ch06-A, ch06-B, ch07-A, ch07-C, ch08 |
| K4 | 0 | 2 | 5 | 0 | ch03, ch04, ch05, ch06-A, ch06-B, ch07-C, ch08 |
| K6 | 1 | 0 | 13 | 0 | ch03, ch05, ch06-A, ch08 |

#### Hits

- **F-C3** · fence-excluded · tex `01_topological_matter.tex:109` — `of $\mathcal{M}, \mathcal{Q}, \mathcal{J}$ for any field; the v14` — Only engine-version string in the chapter. It reports what a named seed's boundary invariants evaluate to ($\mathcal{M}>0$, $\mathcal{Q}=1$, $\mathcal{J}\approx0$) via boundary_invariants.py — a readout, not a ranked pl…
- **F-C3** · fence-excluded · kb `ionization-energy-validation.md:52` — `**Provenance pin (A47 v11c):**` — 'v11c' is the A47 atomic-IE provenance-pin label (SHA 0401388, 2026-04-09 restoration arc), not the v11 electron-genesis engine charter; no LOOP GAP ranks, remanence, or 'platform ACTIVE' routing anywhere in the slice
- **F-C5** · fence-excluded · tex `01_topological_matter.tex:110` — `breathing-soliton seed gives $\mathcal{M} > 0$, $\mathcal{Q} = 1$,` — Adjudicated per slice-instruction (b). This is the row's own fence — a circuit/engine model reporting M, Q, J for a seed WITHOUT selling a genesis-cook: no energize-lock, no Level-2 remanence, no vN target/charter langu…
- **F-C7** · live-wrong · verifier: UNVERIFIED · tex `01_topological_matter.tex:259` — `how a propagating Transverse EM Wave winds into a stationary Spin-1 helical loop when encountering extreme localised network impedance ($Z \to Z_{crit}$) ... e…` — [fragment is an elided quotation of one printed caption line — the two halves are byte-verbatim at :259, the ellipsis replaces 'The discrete sequential excitation of the substrate LC nodes guarantees charge containment,…
- **F-C7** · fence-excluded · tex `01_topological_matter.tex:167` — `The electron's \emph{existence} is held independently by the transverse-Cosserat ($T_2$) charge/spin $\Gamma = -1$\gammaundeclared{} self-trap wall at $V_{yiel…` — This is the row's explicit fence: the BOUNDARY $\Gamma=-1$ / $V_{yield}$ self-trap wall is the SURVIVING localizer, not the corpse. Print even states the A1 core sits sub-saturated at $A=\sqrt{\alpha}$ INSIDE it, matchi…
- **F-C7** · Q1 · kb `electron-identification.md:13` — `The bulk-interior-mode route is the **FALSIFIED** one (Cartesian-grid artifact); localization is **topological/boundary**` — Dated 2026-06-24 Rule-12 banner naming the bulk self-trap dead with its result doc; body preserved.
- **F-C7** · Q1 · kb `electron-identification.md:64` — `The genesis / self-lock arc that would *dynamically create* the fluxoid from a free precursor is **closed-negative** (electron-genesis-from-free-precursor lean…` — Names the free-precursor genesis route dead in the leaf body. This is the authority M8 cites.
- **F-C7** · Q1 · kb `electron-unknot.md:13` — `NOT a bulk self-focusing well — the bulk self-trap is a Cartesian artifact, RULED OUT by Stage-2 Mode-III` — Dated 2026-06-24 inline Rule-12 scope note on the 'permanently trapping the energy' clause; names the corpse dead.
- **F-C7** · fence-excluded · tex `01_topological_matter.tex:167` — `self-trap wall at $V_{yield}$` — This is the BOUNDARY $\Gamma=-1$ / $V_{yield}$ transverse-Cosserat ($T_2$) self-trap — named verbatim in the F-C7/F-C8 fence as the SURVIVING localizer. No bulk self-trap and no free-precursor seed is offered; the same …
- **F-C7** · fence-excluded · kb `q-g18-schwinger-pair-wkb.md:35` — `the probability of reaching the $\Gamma = -1$ wall at $A = 1$` — The surviving boundary localizer used as the tunneling target for pair nucleation — not a bulk self-trap and not a staged seed-photon-to-self-trap growth path. Fence applies.
- **F-C8** · fence-excluded · tex `01_topological_matter.tex:191` — `the self-formed $\Gamma=-1$\gammaundeclared{} TIR cage wall (\S\ref{sec:hollow_vortex_binding}; the transverse-Cosserat $T_2$ self-trap of the vacuum-circuit s…` — Same surviving-homonym fence as F-C7: boundary TIR cage, engine-exact statics readout. No longitudinal-bulk wall and no constitutive-loop/remanence capability is offered. Caption is the twin of electron-identification.m…
- **F-C8** · Q1 · kb `mass-closure-theorem.md:24` — `Any reading of the Step-2 "constructively interferes into a standing-wave loop" as a **bulk self-focused interior mode** is the **FALSIFIED route**` — Dated 2026-06-24 Rule-12 closure-mechanism scoping with body preserved; the $mc^2=E_{reactive}$ identity is explicitly carved out as untouched. No remanence/constitutive-loop capability is offered anywhere in this leaf.
- **F-C8** · fence-excluded · tex `01_topological_matter.tex:191` — `the transverse-Cosserat $T_2$ self-trap of the vacuum-circuit sector` — Figure caption; same homonym as 01:167 — the self-formed $\Gamma=-1$ TIR cage wall at yield. No 'rest mass = self-trapped LONGITUDINAL-bulk wall' and no constitutive-loop / remanence capability is offered. Fence applies.
- **F-C8** · fence-excluded · kb `proton-identification.md:168` — `rest mass = the A1 longitudinal-dilatation depression` — This is the ratified #260/#311 mass=A1 ruling (rest mass = A1 longitudinal dilatation; charge = Cosserat winding; A1 perp T2) propagated to the baryon sector on 2026-07-19. No self-trap / remanence / constitutive-loop l…
- **F-C9** · fence-excluded · kb `hollow-vortex-binding.md:104` — `and NOT the genesis-v5 seed value $\Gamma=80.75$. Do not cross-wire the two $\Gamma$'s.` — Homonym guard: the surviving object is the Kelvin circulation $\Gamma=\oint u\cdot dl$; the genesis-v5 seed value is named only to exclude it. The leaf's §4 trail additionally lists the five existence routes with their …
- **F-C9** · fence-excluded · kb `de-broglie-standing-wave.md:240` — `This is **NOT** the topologically-protected $(2,3)$ **winding** (charge $=\mathrm{Link}(\partial\Omega,F)\in\mathbb{Z}$, def-3638f2), which survives ionization` — names the static (2,3) Link winding as the charge dictionary — the F-C9 fence (charge = winding dictionary STANDS); no self-assembly / graduation / manufacture path offered
- **F-C11** · Q1 · kb `electron-identification.md:15` — `the **(2,3) winding RIDES the cage as STATIC charge** (`Link(∂Ω,F)∈ℤ`, un-walked-back), it does **not** pin the mass.` — Dated 2026-06-24 second-pass Rule-12 localizer relabel; names both dynamical loci NEGATIVE (#415/#417) and preserves the un-walked-back static-Link dictionary (the row's fence).
- **F-C11** · Q1 · kb `claim-quality.md:1375` — `AVE genesis arcs to date are closed-negative (the engine does not self-form the winding; the seeder PLANTS it — cf `clm-gfdplp`).` — Names the genesis/formation route from a free precursor AS DEAD — 'genesis arcs closed-negative to date' — with the kill's claim id cited (clm-gfdplp), inside a paths-to-derived survey explicitly labelled 'a survey of c…
- **K4** · Q1 · kb `electron-identification.md:64` — `The tank quality $Q = 1/\alpha$ is cited as an **identity**, not a derivation.` — $Q=1/\alpha$ appears only with its derivation-status explicitly denied — not sold as cage-emergent. (Per the standing ruling I do not inventory $\{m_e,\alpha,G\}$ calibration inputs themselves.)
- **K4** · Q1 · kb `index.md:48` — `T3.4b cold/α-FREE Q **≈30.8 NOT 137 = clean ECHO-corroboration of Q=1/α being calibration**` — Index blurb names the kill explicitly (the cold Q is 30.8, not 137; $Q=1/\alpha$ is calibration). Also the reason F-C10 scores zero here: this index advertises no ranked plumber order, genesis lanes, or v9-v15 direction…
- **K4** · fence-excluded · tex `01_topological_matter.tex:172` — `The baseline empirical value ($\alpha \approx 1/137.036$)` — Only 137 occurrence in the chapter, and it is explicitly labelled 'baseline empirical value' — the calibration-input reading required by ruling A5, the exact opposite of the killed 'cage-emergent Q=137 / Q=1/α identity'…
- **K4** · fence-excluded · tex `02_baryon_sector.tex:52` — `3(1836.15)(137.036)(0.212\text{ N})` — alpha^{-1} = 137.036 enters as a numeric constant in the confinement scaling ansatz; not Q=137 / Q=1/alpha sold as a cage-emergent identity. alpha is used as a calibration input here (ruling A5).
- **K4** · fence-excluded · kb `neutron-identification.md:43` — `$m_n \approx 1.001378\,m_p` — Digit-substring false positive on '137' (m_n/m_p = 1.001378); no Q=137 content.
- **K4** · fence-excluded · kb `de-broglie-standing-wave.md:252` — `At $Z = 1/\alpha \approx 137$, $\mathcal{C} = 1$ and no bound state exists — the AVE derivation of the maximum atomic number.` — homonym: Z_max = 1/alpha is the orbital-velocity/cavitation limit (v/c = Z alpha), not Q = 137 as a cage-emergent identity
- **K4** · fence-excluded · tex `07_quantum_mechanics_and_orbitals.tex:1083` — `$1/\alpha$ & 137 & 1.000  & \text{Lattice sound barrier} \\` — same homonym as KB:252 — atomic-number sound barrier, not Q=137; the a_0 = 137 l_node sites (TeX:80, :162) are the Bohr-radius identification, also not the corpse
- **K6** · fence-excluded · tex `01_topological_matter.tex:165` — `drilled and held open by the $(2,3)$ Cosserat circulation, and closed by the surface tension of the void--vacuum boundary` — The $(2,3)$ here is the Class-C hollow-vortex opener in a banked consistency picture, and print explicitly denies it any existence/pinning role two lines later (01:167 'existence ... held independently by the ... $\Gamm…
- **K6** · live-wrong · verifier: UNVERIFIED · kb `torus-knot-uniqueness.md:106` — `\| Electron \| $(2, 3)$ trefoil + 0 Cosserat torsion quanta \| base Faddeev-Skyrme on (2,3) \| $\sim 0.511$ MeV (measured) \|` — The §7 lepton table's 'Mass mechanism' column names the Faddeev-Skyrme energy ON THE (2,3) WINDING as what sets the electron's mass, unbannered, in a leaf carrying no Rule-12 banner anywhere. A reader at HEAD would take…
- **K6** · fence-excluded · tex `02_baryon_sector.tex:226` — `The electron's phase profile follows the $(2,3)$ pattern with $c_3 = 3$ phase crossings, even though its ground-state topology is the unknot ($0_1$).` — Static (2,q) winding-ladder dictionary entry (the surviving static Link winding); not offered as the DYNAMICAL mass-pin. KB twins identical at self-consistent-mass-oscillator.md:16 and torus-knot-ladder-baryons.md:13; :…
- **K6** · fence-excluded · tex `04_quantum_spin.tex:13` — `the $0_1$ unknot flux tube in real space carrying a rotating $(2,3)$ phase-space Clifford-torus winding pattern` — The (2,3) winding is named as the static phase-space Clifford-torus winding the unknot carries (charge/winding dictionary homonym) and is used as the SPIN flywheel ontology; no claim that the (2,3) winding is the dynami…
- **K6** · fence-excluded · tex `04_quantum_spin.tex:24` — `the electron is the $0_1$ unknot in real space carrying a literal macro-physical $(2,3)$ phase-space Clifford-torus winding pattern that stores inductive kinet…` — Same homonym as :13 -- (2,3) as the phase-space winding storing inductive energy for the angular-momentum argument; no mass-pin or genesis mechanism offered.
- **K6** · fence-excluded · kb `spin-as-precession.md:10` — `the $0_1$ unknot flux tube in real space carrying a rotating $(2,3)$ phase-space Clifford-torus winding pattern` — Verbatim twin of TeX:13; same fence.
- **K6** · fence-excluded · kb `larmor-derivation.md:10` — `the electron is the $0_1$ unknot in real space` — Verbatim twin of TeX:24 (with an added Vol 1 Ch 8 link); same fence.
- **K6** · fence-excluded · tex `06_electroweak_and_higgs.tex:561` — `is a real-space $0_1$ unknot whose Clifford-torus phase-space portrait` — The (2,3) winding here is the phase-space trefoil supplying the d/q currents for the g-2 saliency kernel, not the (2,3) winding sold as the DYNAMICAL mass-pin. Static Link / phase-space winding stands per the K6 fence.
- **K6** · fence-excluded · tex `06_electroweak_and_higgs.tex:647` — `where $n_q = 3$ is the q-axis poloidal winding number of the (2,3)` — n_q used as the q-axis winding of the phase-space trefoil in a (refuted, disclosed at 753-769) saliency postulate; no mass-pin claim.
- **K6** · fence-excluded · kb `q-g19a-petermann-saliency-closure.md:30` — `The trefoil lives in *phase space*, not real space; the real-space soliton is the unknot $0_1$.` — Explicitly the phase-space (2,3) portrait; not a dynamical mass-pin claim.
- **K6** · fence-excluded · kb `q-g19a-petermann-saliency-closure.md:85` — `where $n_q = 3$ is the **q-axis poloidal winding number** of the $(2,3)$ trefoil` — Same homonym as TeX 647; the RESOLVED-NEGATIVE status of the n_q law is carried at :221 (Q1-style disclosure), no mass-pin content.
- **K6** · fence-excluded · kb `chiral-factor.md:45` — `at macroscopic scales, the $(2,3)$ trefoil produces $6/5$` — (2,3) used as the HOPF-01 antenna chiral geometric factor pq/(p+q); not sold as the dynamical mass-pin of the electron
- **K6** · fence-excluded · kb `de-broglie-standing-wave.md:240` — `This is **NOT** the topologically-protected $(2,3)$ **winding**` — Terminology note explicitly separating the de Broglie mode-count from the static Link (2,3) winding (charge = Link dictionary, def-3638f2); no dynamical mass-pin claim. Leaf's TeX twin is in ch07-A, outside 2250-3400.
- **K6** · fence-excluded · kb `chiral-factor.md:45` — `at macroscopic scales, the $(2,3)$ trefoil produces $6/5$` — HOPF-01 antenna trefoil geometric factor (alpha x pq/(p+q)); not the (2,3) winding sold as the electron's dynamical mass-pin. Leaf's TeX twin (3813+) is in ch07-D.

---

## §4 — Line-anchor drift, both directions (measured by archaeology, not by "leaf changed after tex")

Method: for each `leaf.md:NN` cite, `git log -S` finds the earliest commit that wrote the cite; the leaf **at that commit** at line NN is the intended content; that content is then located at HEAD. This is exact where the 2026-09-06 scan's S5 bucket ("anchor unverified: leaf changed after this .tex") was only a candidate flag.

### 4.1 TeX → KB (47 anchored cites in `vol_2_subatomic/chapters/*.tex`, comments included)

| Result | Count | Sites |
|---|---:|---|
| lands exactly | 29 | — |
| line text evolved in place (still the right line) | 6 | 04:91→larmor-derivation.md:55 · 04:92→visual-equivalence.md:14 · 06:57→lepton-spectrum.md:29 · 07:3515 & 09:241→form-deriving-value-importing.md:87 · 07:3521→srs-band-structure.md:116 |
| **moved (banner inserted above)** | **10** | **printed:** 02:357, 02:362 (neutron-identification.md :52→:54) · 06:770 (q-g19a…:110→:221 — at HEAD :110 is a Python line) · 10:109 (vol2/claim-quality.md :483-486,491,496→:518-521,526,531). **comment-only:** 01:55 (translation-circuit.md :767→:839) · 02:111 (theorem-thesaurus.md :227→:228) · 02:356 (:52→:54) · 06:666 (q-g19a :105→:216) · 06:671 (closure-roadmap :84→:85) · 10:399 (full-derivation-chain.md :850→:854) |
| dead by retraction (no line to re-pin to) | 1 | 06:548 (comment) → q-g19a…:95 "Deviation: 50 ppm" — STRUCK 2026-08-03 |
| unresolvable path | 1 | 10:103 (print) cites `research/2026-06-10_freeze-handedness-survey_note.md:50` — resolves and is on-topic, but it is a research-note cite in print, not a KB leaf |

All ten moved anchors are re-pinned in the mechanical PR (§6). The scan's two vol2 S5 flags (02:357/362, 06:770) are confirmed real; the scan could not see the other eight because six are comment-only and 10:109 is a sidecar range cite.

### 4.2 KB → TeX (vol2 leaves citing `0N_*.tex:NN`) — **worse, and untouched tonight**

| KB site | cites | what that TeX line is at HEAD | status |
|---|---|---|---|
| `neutron-identification.md:23` | `02_baryon_sector.tex:294` (composite-topology framing) | `(2,9) & 9 & 1582 & Δ(1600) …` ladder table row | **dead** |
| `neutron-identification.md:25` | `02_baryon_sector.tex:299` (figure caption "elastic expansion …") | `\end{center}` | **dead** (caption is now 02:362) |
| `neutron-identification.md:64` | `02_baryon_sector.tex:294`, `06_electroweak_and_higgs.tex:660` | table row; a `%` comment | **dead** |
| `neutron-identification.md:68`, `:115` | `06_electroweak_and_higgs.tex:131` | blank line | **dead** |
| `neutron-identification.md:114` | `02_baryon_sector.tex:292` | `(2,5) & 5 & 938 & Proton` table row | **dead** |
| `neutron-identification.md:71` | `10_open_problems.tex:33` | "Any θ≠0 gives the neutron an electric dipole moment" | ok |
| `proton-identification.md:152` | `02_baryon_sector.tex:41` | "Resolving the Scale Paradox …" | ok |
| `thermal-softening.md:40` | `02_baryon_sector.tex:131` | δ_th evaluation line | ok |
| `q-g19a-petermann-saliency-closure.md:173` | `06_electroweak_and_higgs.tex:516` | `C_2^{AVE} = … = -0.32846` | ok |
| `q-g19a-petermann-saliency-closure.md:226` | `06_electroweak_and_higgs.tex:154` | blank line | **dead** |

Seven dead KB→TeX anchors, six of them in one leaf. These are KB-side edits: the new-cite excerpt ratchet applies, and `neutron-identification.md` is PATH-STABLE (inbound from `common/full-derivation-chain`, vol6 hydrogen, vol4 ch11), so any insertion must go at EOF or be line-count-neutral. Recommended as PR-2 (§6.2), not done here.

---


---


---


---

## §5 — Known debt re-checked at HEAD `5619dd56` (status only; nothing re-minted)

| known item | source | status at HEAD |
|---|---|---|
| 01:40 g=2 / spin-half overclaim | MR board vol2 #5 | **CLOSED** — de-claim printed at `01:64-80` (2026-08-02), KB twins bannered [first-hand] |
| 01:170 → `vol2/claim-quality.md` (S4a) | 09-06 scan | **no debt** — the clm-h9aqmt running-coupling caveat is printed at `01:170` itself [first-hand] |
| 01:218 / 01:237 → `proton-identification.md` (S4a, "🔴 refuted") | 09-06 scan | **no debt** — the cited §1 property 3 is live at leaf `:23`; the 🔴 markers are the 2026-06-08 relabels the print already mirrors (ch02 reader) |
| 01:242 → `vol4/claim-quality.md` clm-wcoul2 (S4a) | 09-06 scan | **no debt** — id resolves at `vol4/claim-quality.md:1879` [first-hand] |
| 02:81 cold Faddeev-Skyrme triplet | MR board vol2 #1 | **RESOLVED** — print `02:92` = leaf `thermal-softening.md:11`; prior triplet preserved in `%` comment (ch02 reader) |
| 02:92 ν_vac → ν_Hill | MR board vol2 #13 | **RESOLVED** in print; leaf `:25` carries the relabel (ch02 reader) |
| 02:235 / 02:268 → `proton-identification.md` (S4a) | 09-06 scan | **no debt** — relabel printed inline; cites land on live content (ch02 reader) |
| 02:357 / 02:362 → `neutron-identification.md:52` (S5) | 09-06 scan | **REAL** — re-pinned `:54` in #1046 [first-hand archaeology]; plus STALE-KB at `proton-neutron-mass-split.md:10` (§2) |
| 04:53 / 04:68 "proving" / "profound mechanical victory" | MR board vol2 #6 | **CLOSED** both sides, disclosure printed at `04:98-112` (ch04 reader) |
| 04:111 → `vol2/claim-quality.md` (S4a) | 09-06 scan | **false positive** — `git log -L401,426` shows the clm-salw2h entry unchanged since 2026-07-08 (ch04 reader) |
| 05:35 / 05:51 def-l0ngdu compressibility premise | MR board vol2 #7; 09-06 scan | **RESOLVED and disclosed** on both sides (ch05 reader) |
| 06:363-365 Δc_crit provenance (F8) | revalidation §7 | **SUPERSEDED, still un-propagated**; ch03 twin `03:148-160` added [first-hand] — §0.1 #2 |
| 06:466 50-ppm postulate-conditional tag | MR board vol2 #3 | disclosed by the adjacent Stage-1/Stage-2 wording per ch06-B reader (M6 notes the missing "at Stage 1" label at `06:777`) |
| 06:618 / 06:722 / 06:770 → `q-g19a…` (S4a/S5) | 09-06 scan | `06:770` **REAL**, re-pinned `:221` in #1046; `06:723` still carries three drifted sub-anchors (`:100`, `:103`, `:121`) — §2 ch06-B M1 |
| 07:243 $N_{eff}=1.5$ with no KB home | MR board vol2 #9; revalidation #14 | **STILL PRESENT** at HEAD; the R40-B2a DEMOTED stamp 4 lines above demotes the premise but the contradiction with `:253` stands (ch07-A M3) |
| 09:50 sub-3 Å scope note | revalidation | pending ch09 slice |
| 11:66 "comparable accuracy"; 11:123 protein N13 NEGATIVE | revalidation #15/#16 | pending ch11 slice |
| 06:230 / 06:313; 07:3510; 12mp:112 | MR board / scan | pending ch06-A / ch07-D / ch12-mp slices |

---

## §6 — PR outline

### 6.1 Opened tonight (draft): [#1046](https://github.com/ave-veritas-et-enodatio/AVE-Core/pull/1046) — `fix/2026-09-13-vol2-dead-line-anchors` @ `300bc406`

Ten in-place line-number re-pins across four vol2 chapter files (§4.1). No prose, no value, no claim moves; file line counts unchanged, so nothing inbound shifts. `make verify` on that commit in a clean detached worktree: **exit 0**; CI on the PR: all six jobs green (`make verify + make test`, manuscript compile, inbound cite shift, excerpt ratchet, fired riders, test-engine). Title carries `[REVIEW: pending-orchestrator]`; not merged by this lane.

### 6.2 Recommended, NOT opened (priority order)

**PR-2a — mechanical, KB-side + remaining anchors (no physics; excerpt ratchet applies to KB cites; PATH-STABLE leaves need line-count-neutral edits):**
- `neutron-identification.md` KB→TeX re-pins by the leaf's own quoted excerpts: `:23` `02:294` → `02:357`; `:25` `02:299` → `02:362`; `:64` `02:294,299` → `02:357,362`; `:68` and `:115` `06:131` → `06:134`; `:114` `02:292-301` → `02:354-364`; `:64`/`:115` `06:660` cites the struck 50-ppm sentence (dead by retraction — strike the cite or point it at the `%` preservation block). `q-g19a-petermann-saliency-closure.md:226` `06:154-176` → `06:157-179` (verify the examplebox range).
- `gauge-boson-masses.md:34/42/48` → `vocabulary-register.md` anchors (`:870`→`:893`, `:867`→`:882`, `:882`→`:898`; def-l0ngdu / def-uatk1s moved) — ch05 M06–M08.
- `larmor-derivation.md:61-65`, `visual-equivalence.md:22`, TeX `04:81-88` (comment) → `vol2/claim-quality.md` anchors drifted +1 (`:407-410`→`:408-411`, `:419`→`:420`) — ch04 M1–M3.
- `sm-ave-translation.md:10` "line 305" → `06:860`; print `06:833` `constants.py` "line 338" → `:679` — ch06-B M9/M10. `06:723` sub-anchors `:100/:103/:121` — ch06-B M1.

**PR-2b — print carves whose wording already exists verbatim in a KB banner (mechanical propagation of a ratified ruling; orchestrator dispatch, Rule-12 preserved bodies):**
- `01:35` (+ summary `:266`): mass-sector ruling footnote mirroring `newtonian-inertia-as-lenz.md:14`.
- `03:148-160` and `06:363-366`: Δc_crit carve mirroring `chiral-screening.md:28-48`.
- `02:319/:327/:330`: θ-fork note mirroring `topological-fractionalization.md:50-76`.
- `06:808-834` (+ `higgs-mass.md` / `higgs-mechanism.md`): the R40-B2a stamp on the breathing-mode mechanism that the sidecar `:162` row already carries.
- `07:277`: promote the Be 9.32 eV `%` HISTORICAL NOTE to a printed dated note pointing at `hierarchical-cascade-correction.md:54`.
- `05:175` / `05:8`: rescope "explicitly derived" gauge invariance to the residual time-independent family (`gauge-boson-masses.md:83`).

**PR-2c — KB-side STALE-KB (leaf lags a print correction; banner copies the print wording):** `proton-neutron-mass-split.md:10` "accounts for" (print corrected 2026-06-15); `thermal-softening.md:37` "validates" (#847 R3 flagged); `weinberg-angle.md:20/23/26` ν_vac → ν_Hill (CRIB-1); `weak-coupling.md:22-30` 2026-07-02 re-anchor (two-vertex → two Axiom-4 varactor couplings); `analog-ladder-filter.md:52` R40-B2a stamp mirror.

**Needs a ruling before any edit (not PR material):** where the canonical neutrino screw-dislocation leaf lives (§0.1 #3); the 1836.15 headline wording under D1 (§0.1 #4); Li 2s/2p sign (`07:224` vs `orbital-penetration-penalties.md:39`); Boron 9.4 vs 8.30 eV (`07:324`); the Regime-IV yield-boundary resultbox `07:485-488` vs the linear-regime leaf (`de-broglie-n.md:10`); three He-IE figures (24.19 / 24.37 / "0.008 %"); the $\kappa_{Hopf}$ sign form (`07:3288` vs `radial-eigenvalue-solver.md:731`); overloaded "Phase A/B/C" pipeline labels; caption "the $3_1$ electron knot" (`04:62`); the $c=15$ ladder row (three different deviations: `02:297` +2.40 %, `02:314` +9.8 %, leaf +3.249 %).

---

## §7 — Receipts

- **Verify:** `make verify` on the main checkout at `5619dd56` → exit 2, failing only on `verify-lane-number-checks` scanning stale `.claude/worktrees/wf_*` copies of `r40_quote_claim_strength_number_check.py` (local litter, not repo content). Same HEAD in a fresh detached worktree → **exit 0**. Fix branch `300bc406` in that worktree → **exit 0**; PR #1046 CI: 6/6 green.
- **Anchor sweeps:** `anchor_sweep.py` (TeX→KB, 47 cites, archaeology by earliest `git log -S` commit) and the KB→TeX variant (§4.2) — both read-only, run at `5619dd56`.
- **Workflow:** run `wf_45d693ef-5ac` (20 reader slices → verifiers → critic). First launch stalled on a usage limit (6 readers finished); resumed with the six cached and the rest on Opus (ch01) / Sonnet (others), verifiers on Sonnet with the fence/Q1 lens on Opus, critic on Opus.
- **Read receipts (per slice; a slice missing here has not returned):**
- **ch01-A** — `01_topological_matter.tex` 1-273 (full: 1-140, 141-273) (of 273); `index.md` 1-48 (of 48); `mathematical-topology-of-mass.md` 1-34 (of 34); `newtonian-inertia-as-lenz.md` 1-16 (of 16); `electron-unknot.md` 1-75 (of 75); `electron-identification.md` 1-195 (1-100, 100-195) (of 195); `mass-closure-theorem.md` 1-172 (1-90, 90-172) (of 172); `hollow-vortex-binding.md` 1-206 (1-90, 90-206) (of 206); `regime-classification.md` 1-21 (of 21); `torus-knot-ladder.md` 1-29 (of 29); `chirality-and-antimatter.md` 1-73 (of 73); `claim-quality.md` PARTIAL — the 9 assigned entries read through their '---' terminators: 10-41 (clm-h9aqmt), 73-103 (clm-k6olj8), 675-700 (clm-oygz1i), 701-726 (clm-jwyy6l), 727-750 (clm-ou2jym), 751-778 (clm-hb2xmj), 1148-1180 (clm-uatcql), 1238-1266 (clm-ka5zdx), 1554-1590 (clm-hvb7q3) (of 1774); `index.md` 1-37 (cross-check for slice-instruction (a)) (of 37); `03_neutrino_sector.tex` PARTIAL 1-30 (cross-check of the printed 2026-05-06 corrigendum only; not an assigned slice file) (of 281)
- **ch01-B: NO RECEIPT**
- **ch01-C** — `01_topological_matter.tex` 1-273 (of 273); `common-mode-twist-ledger.md` 1-369 (long lines re-read past col 900 via tail dump) (of 369); `torus-knot-uniqueness.md` 1-150 (of 150); `finkelstein-misner-spin-half-derivation.md` 1-202 (long lines 14/65/156 re-read past col 900) (of 202); `spin-gyroscopic-isomorphism.md` 1-63 (long lines 15/47 re-read past col 900) (of 63); `q-g18-schwinger-pair-wkb.md` 1-82 (of 82); `newtonian-inertia-as-lenz.md` 1-16 (full; pulled because common-mode-twist-ledger.md:50 names it as propagated mass-sector banner site #2 and the slice brief required it) (of 16); `claim-quality.md` 395-425 (clm-salw2h), 1290-1320 (clm-lj4ok5), 1344-1378 (clm-8c3yhs), 1615-1660 (clm-cmtwst) — entry-scoped read as instructed, not whole file (of 1774); `claim-quality.md` 1873-1935 (clm-wcoul2 entry only — anchor/status check for printed TeX 01:242 cite) (of 0)
- **ch02** — `02_baryon_sector.tex` 1-125, 126-250, 251-472 (full) (of 472); `index.md` 1-39 (full) (of 39); `quark-flavors.md` 1-12 (full) (of 12); `torus-knot-ladder-baryons.md` 1-51 (full) (of 51); `self-consistent-mass-oscillator.md` 1-66 (full) (of 66); `thermal-softening.md` 1-124 (full) (of 124); `topological-fractionalization.md` 1-90 (full) (of 90); `proton-neutron-mass-split.md` 1-97 (full) (of 97); `neutron-identification.md` 1-134 (full) (of 134); `proton-identification.md` 1-85, 86-168 (full) (of 168); `claim-quality.md` 42-70 (clm-mnb3lt), 73-100 (clm-k6olj8), 274-297 (clm-67jn9o), 300-328 (clm-w8jn3q), 779-806 (clm-bh9p6s), 1382-1409 (clm-6kwzot), 1412-1438 (clm-cmic3e) -- each entry through its --- terminator; remainder not assigned (of 1774)
- **ch03** — `03_neutrino_sector.tex` 1-281 (full file) (of 281); `index.md` 1-37 (full file) (of 37); `chiral-screening.md` 1-48 (full file) (of 48); `delta-cp-violation.md` 1-81 (full file) (of 81); `neutrino-translation-table.md` 1-12 (full file) (of 12); `pmns-eigenvalues.md` 1-51 (full file) (of 51); `pmns-junction-model.md` 1-25 (full file) (of 25); `claim-quality.md` 211-271 (clm-7o8clt and clm-rji99i entries only, through their --- terminators, per task scope; full 1774-line file NOT read in full) (of 1774); `01_topological_matter.tex` 195-215 (partial, targeted at the 01:207 regime-classification table per slice-specific instruction (b); not an assigned slice file, not read in full) (of 215); `00_title.tex` grep-only for 'twisted' (line 14 located and quoted); not Read in full, per slice-specific instruction which asked for a targeted grep on this file (of 0)
- **ch04** — `04_quantum_spin.tex` 1-125 (of 125); `index.md` 1-28 (of 28); `larmor-derivation.md` 1-69 (of 69); `spin-as-precession.md` 1-20 (of 20); `visual-equivalence.md` 1-26 (of 26); `spin-half-paradox.md` 1-18 (of 18); `claim-quality.md` 401-428 (clm-salw2h entry through its --- terminator at 427; spot-verified 407-411, 419-421, 1146-1154) (of 1774)
- **ch05** — `05_electroweak_gauge_theory.tex` 1-247 (full; two chunks 1-130, 131-247) (of 247); `gauge-boson-masses.md` 1-204 (full; two chunks 1-110, 111-204) (of 204); `index.md` 1-32 (full) (of 32); `weak-coupling.md` 1-38 (full) (of 38); `weinberg-angle.md` 1-40 (full) (of 40); `forward-to-ch6.md` 1-54 (full) (of 54); `claim-quality.md` 103-160 (clm-5zuo7g + clm-q8un7j through their --- terminators), 809-840 (clm-jkpfd4 through its --- terminator) — partial by assignment (of 1774); `vocabulary-register.md` 860-912 (def-t2ph01 tail, def-l0ngdu :882-895 in full, def-uatk1s :897-910) plus grep index for def-l0ngdu / 'One word each way' — partial by assignment (of 1736); `2026-08-02_manuscript-reconciliation-board.md` 615-622, 640-700 (vol2 findings block incl. 05:35 and 02:92) — partial, for alreadyKnownIn only (of 1222); `2026-09-06_tex-kb-staleness_scan.txt` 8-13, 90-97, 259 (ch05 S4a rows 05:35/05:51; S5 row gauge-boson-masses.md:39) — partial, for alreadyKnownIn only (of 368); `06_temperature_characteristics.tex` 79 only (external citer of gauge-boson-masses.md:39) — outside slice, anchor check only (of 0)
- **ch06-A** — `06_electroweak_and_higgs.tex` 1-450 (full assigned slice; read as 1-250, 250-449, 449-451 overlapping chunks for full coverage) (of 867); `higgs-mechanism.md` 1-62 (full file) (of 62); `lepton-spectrum.md` 1-86 (full file) (of 86); `spontaneous-symmetry-breaking.md` 1-87 (full file) (of 87); `sm-ave-translation.md` 1-12 (full file) (of 12); `index.md` 1-38 (full file) (of 38); `chiral-screening.md` 1-48 (full file) (of 48); `claim-quality.md` 95-179 (clm-5zuo7g, clm-q8un7j, clm-p7rfkb entries through their --- terminators), 240-297 (clm-rji99i entry through its --- terminator), 1660-1774 (R40 batch-2a dated note referenced by clm-p7rfkb, through EOF) (of 1774); `higgs-mass.md` 1-94 (full file; discovered during sectionMap-building as the KB twin for TeX's Neutrino Mass Spectrum + Schwinger sections, read in full and grep-verified for mismatch M3/M4) (of 94); `verify-md-links.py` 795-819 (WAIVED_KBLEAF table, consulted to confirm mismatch M8 is a pre-existing tracked waiver) (of 0)
- **ch06-B** — `06_electroweak_and_higgs.tex` 449-660, 661-867 (assigned range 449-867 in full) (of 867); `q-g19a-petermann-saliency-closure.md` 1-130, 131-256 (full) (of 256); `q-g20f-vacuum-polarization.md` 1-149 (full) (of 149); `q-g27-muon-cosserat-saliency.md` 1-88 (full) (of 88); `higgs-mass.md` 1-94 (full) (of 94); `index.md` 1-38 (full) (of 38); `claim-quality.md` 158-215 (clm-p7rfkb 158-182, clm-stgx1i 184-211), 1441-1530 (clm-v2sg8z 1441-1465, clm-bqtasn 1467-1495, clm-8niffj 1497-1523), 1700-1774 (R40 batch-2a note); partial by design (of 1774); `sm-ave-translation.md` 1-12 (full; twin of TeX 855-860) (of 12); `lambda-higgs-derivation.md` 1-44 (full; only KB leaf translating TeX 808-833) (of 44)
- **ch07-A** — `07_quantum_mechanics_and_orbitals.tex` 1-1100 in full (chunks 1-250, 251-500, 501-750, 751-1000, 1001-1100); plus out-of-range pointer-target check 4145-4215 (read) and grep of 4240-4290 for the % R40 batch-2a row list; grep-only for 24.37/0.008%/Stage A/sec labels elsewhere (of 4290); `index.md` 1-63 (of 63); `de-broglie-standing-wave.md` 1-340 (1-250, 251-340) (of 340); `qm-ave-translation.md` 1-18 (of 18); `helium-symmetric-cavity.md` 1-82 (of 82); `atom-as-radial-waveguide.md` 1-42 (of 42); `macro-cavity-saturation.md` 1-14 (of 14); `ode-verification.md` 1-55 (of 55); `analog-ladder-filter.md` 1-96 (of 96); `geometry-pipeline.md` 1-75 (of 75); `screening-rule.md` 1-38 (of 38); `de-broglie-n.md` 1-30 (of 30); `orbital-penetration-penalties.md` 1-58 (of 58); `hierarchical-cascade-correction.md` 1-60 (of 60); `helium-coupling-first-principles.md` 1-64 (of 64); `chiral-factor.md` 1-51 (of 51); `bonding-mode-formula.md` 1-44 (of 44); `complete-solver-architecture.md` 1-44 (of 44); `dual-formalism-architecture.md` 1-28 (of 28); `knot-vs-orbital-table.md` 1-22 (of 22); `operator-domain-table.md` 1-19 (of 19); `scale-separation.md` 1-68 (of 68); `subshell-junction-scattering.md` 1-42 (of 42); `ionization-energy-validation.md` 1-52 (of 52); `radial-eigenvalue-solver.md` GREP-ONLY (headings + numeric/corpse terms); not read in full — twins TeX >1100 (E2b-E2k) (of 816); `stepped-impedance-resonator.md` GREP-ONLY (corpse/numeric terms); twin sec:sir_atom at TeX:3880, outside slice (of 92); `q-g20a-lamb-shift-structural-closure.md` GREP-ONLY (corpse/numeric terms); research-origin, no twin in 1-1100 (of 73); `brillouin-zone-uv-cutoff.md` GREP-ONLY (corpse/numeric terms); research-origin, no twin in 1-1100 (of 120); `claim-quality.md` 331-369 (clm-oltvwy), 372-398 (clm-w6kk5y), 623-649 (clm-ak97cb), 837-868 (clm-qde5gn); grep-only for K=2G / protein elsewhere (of 1774); `vocabulary-register.md` 255-275 only (def-quant3 entry, for M8 dating) (of 0); `ch8-alpha-golden-torus.md` 9-13 only (anchor check for TeX:161 \kbleaf :11) (of 0)
- **ch07-B: NO RECEIPT**
- **ch07-C** — `07_quantum_mechanics_and_orbitals.tex` 2250-3400 (assigned range, read in full in 5 chunks); plus targeted grep-only lookups outside range (161, 558, 3134-3139, 3565-3611, 3851, 4007, 4027) to place twins (of 4290); `radial-eigenvalue-solver.md` 1-816 (of 816); `dual-formalism-architecture.md` 1-28 (of 28); `screening-rule.md` 1-38 (of 38); `subshell-junction-scattering.md` 1-42 (of 42); `hierarchical-cascade-correction.md` 1-60 (of 60); `helium-coupling-first-principles.md` 1-64 (of 64); `knot-vs-orbital-table.md` 1-22 (of 22); `complete-solver-architecture.md` 1-44 (of 44); `index.md` 1-63 (of 63); `operator-domain-table.md` 1-19 (of 19); `qm-ave-translation.md` 1-18 (of 18); `de-broglie-standing-wave.md` 1-340 (of 340); `brillouin-zone-uv-cutoff.md` 1-120 (of 120); `q-g20a-lamb-shift-structural-closure.md` 1-73 (of 73); `helium-symmetric-cavity.md` 1-82 (of 82); `stepped-impedance-resonator.md` 1-92 (of 92); `analog-ladder-filter.md` 1-96 (of 96); `geometry-pipeline.md` 1-75 (of 75); `scale-separation.md` 1-68 (of 68); `orbital-penetration-penalties.md` 1-58 (of 58); `ode-verification.md` 1-55 (of 55); `chiral-factor.md` 1-51 (of 51); `bonding-mode-formula.md` 1-44 (of 44); `atom-as-radial-waveguide.md` 1-42 (of 42); `de-broglie-n.md` 1-30 (of 30); `macro-cavity-saturation.md` 1-14 (of 14); `ionization-energy-validation.md` 1-52 (of 52); `claim-quality.md` 331-398 (clm-oltvwy 331-369, clm-w6kk5y 371-398, each through its --- terminator) (of 1774); `radial_eigenvalue.py` 1840-1870 (context only, for the kappa_hopf parity factor; grep elsewhere) (of 0)
- **ch07-D: NO RECEIPT**
- **ch08** — `08_planck_and_string_theory.tex` 1-103 (full) (of 103); `index.md` 1-27 (full) (of 27); `planck-scale-derivation.md` 1-72 (full) (of 72); `string-theory-translation.md` 1-32 (full) (of 32); `claim-quality.md` 555-591 (clm-g6e3zw entry, located via grep -n "<!-- id: clm-" then read through terminating ---; rest of 1774-line file not in scope for this slice) (of 1774)
- **ch09: NO RECEIPT**
- **ch10: NO RECEIPT**
- **ch11: NO RECEIPT**
- **ch12-mp: NO RECEIPT**
- **ch12-fp: NO RECEIPT**
- **appx-front: NO RECEIPT**
