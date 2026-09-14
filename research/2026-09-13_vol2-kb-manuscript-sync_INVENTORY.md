# INVENTORY — Vol 2 KB ↔ manuscript SYNC (Lane C, 2026-09-13)

**Lane:** C — KB ↔ manuscript sync, vol2 HOT lane only (electron-identity F-pass emphasis).
**Branch:** `claude/lane-c-kb-ms-vol2-sync` · **Base:** `origin/main` @ `5619dd56` (BOARD #1043 on main; local = origin, ff-only pull was a no-op).
**Class:** inventory. **Adjudicates nothing; edits no leaf and no print** (the one mechanical PR is §6.1 and lives on its own branch).
**Scope:** `manuscript/vol_2_subatomic/` (16 documents: 13 chapters + `main.tex` + `_manifest.tex` + `frontmatter/00_title.tex`) ↔ `manuscript/ave-kb/vol2/` (146 `.md` files in 18 chapter/appendix directories, ~11,000 lines).

**Standing frame (read first).**
- KB **leaves** are the source of truth. `index.md`, `claim-quality.md`, distillates, `BOARD.md` and `consistency-manifest.yaml` are derived; the manifest is claim/label bridging, **not** the leaf↔chapter sync source of truth. Everything below cites leaves and TeX primaries.
- Rule 12: a site under a dated banner is *disclosed*, not debt. A TeX `%` comment is **not printed** — a walk-back that lives only in a comment discloses in git and nowhere the reader sees; those are listed as WB-LAG (comment-only).
- Grep indexed; **reading discharged.** Each chapter slice was read in full by a dedicated reader (three on ch01, four on ch07, two on ch06), findings then went to independent verifiers (cite-verbatim; fence/Q1; disclosure/prior-art), and a completeness critic runs over the union. Read receipts are in §7. **This is a vol2-only slice of the F-row universe (16 of 175 documents); it discharges no F-row** — per the tracker's combined-pass protocol a row closes only on a full-universe read receipt. The per-row hit ledger in §3 is input to that pass, not a substitute for it.

**Coverage at this stamp (2026-09-13 19:15 PDT):** 19/20 reader slices returned (ch01-A, ch01-B, ch01-C, ch02, ch03, ch04, ch05, ch06-A, ch06-B, ch07-A, ch07-B, ch07-C, ch07-D, ch08, ch09, ch10, ch11, ch12-mp, ch12-fp); 1 still pending in the resumed workflow run `wf_45d693ef-5ac` (appx-front). Reader-reported findings: 136; corpse hits: 69 (7 live-wrong); findings with verifier verdicts: 37. Findings below marked **[first-hand]** were read and grep-verified by the lane directly, independent of any agent; the rest are **reader-reported** and carry the verifier verdict column where one exists (UNVERIFIED otherwise). Re-run `assemble_inventory.py` after the workflow completes to refresh §1–§3 and §7 from the journal.

---

## §0 — Headline

**Referential integrity is fixable mechanically; the debt is walk-back propagation lag in print, and — in one direction — in the KB.**

1. **TeX → KB line anchors (47):** 29 exact, 6 evolved-in-place, **10 moved** (4 printed, 6 comment-only), 1 dead-by-retraction, 1 research-note cite in print. The ten are re-pinned in draft PR #1046 (§6.1). The 2026-09-06 scan's two vol2 S5 flags were both real; the other eight were invisible to it.
2. **KB → TeX line anchors: seven dead**, six in `neutron-identification.md` — a PATH-STABLE leaf — pointing at table rows, `\end{center}` and blank lines (§4.2). Left for a KB-side PR (excerpt ratchet applies).
3. **Electron-identity corpse pass (vol2 slice, §3):** outside ch01, **zero live-wrong** hits for F-C1…F-C11 / K4 / K6 — every hit is a fence-excluded homonym (static Link `(2,3)` winding as charge/spin carrier; `Z = 1/α ≈ 137` as the atomic-number sound barrier; `α⁻¹` as a numeric constant) or a Q1 banner. Inside ch01 the readers surfaced **two live-wrong candidates** (verifier verdicts in §3 where returned): **F-C7 at print `01_topological_matter.tex:259`** — the figure caption *"a propagating Transverse EM Wave winds into a stationary Spin-1 helical loop … establishing the physical derivation of confined point-particles via continuum wave-crashing"* sells the free-precursor formation route as established, which `electron-identification.md:64` names *closed-negative* [first-hand: the caption is verbatim at :259 and carries no banner]; and **K6 at KB `torus-knot-uniqueness.md:106`** — the §7 lepton table's "Mass mechanism" column names the Faddeev-Skyrme energy on the `(2,3)` winding as what sets the electron mass, unbannered (reader-reported). The ch01-B reader (research-origin electron leaves) adds four more candidates: **K4** at KB `pair-production-axiom-derivation.md:35` and `:137` ("the $Q = 1/\alpha$ signature of TIR-confined electron", unmarked) and `electron-unknot-cosserat-seeder.md:120` (a ground-state search offered as the route to the canonical 137.036 Q, unbannered); **K6** at print `01:239` ("Higher $q$ produces more tightly wound solitons with correspondingly higher mass"); **F-C7** at `l3-electron-soliton-synthesis.md:314` (the N=128+ bulk-hosting escalation listed as open next work). None of these discharges or closes a row: the tracker's combined 175-document pass owns that; these are hit-ledger entries for it, each awaiting the three-lens verdict (§3).
4. **Top sync debts (first-hand, all un-propagated to print):** §2.1.

### §0.1 — Top five sync debts

| # | debt | print sites | KB truth (leaf) | why it matters | class |
|---|---|---|---|---|---|
| 1 | **Mass-sector ruling (2026-06-20, Grant-ratified) not in print.** "Mass is the stored inductive energy required to maintain the topological integrity of the standing wave" and the chapter-summary bullet "Inertial mass … is derived classically from distributed continuous inductance" stand flat. | `01_topological_matter.tex:35`, `:266` | `newtonian-inertia-as-lenz.md:14` — *"STORED INDUCTIVE ENERGY = the FLYWHEEL … the REST MASS store is A1"*; the ruling is propagated to **six** KB sites (`common-mode-twist-ledger.md:45-52` lists them) and to **zero** vol2 print sites (grep `flywheel\|A_1 (mass\|depression)` over non-comment vol2 TeX: only the ch04 spin-flywheel language, which is compatible). Print `01:168` (hollow-vortex section, 2026-07) already says the $A_1$ mass core — so print is also internally split. | A ratified physics ruling the leaf carries and the book contradicts. | WB-LAG · HIGH |
| 2 | **Δc_crit three-way identity carve (2026-08-24, Grant "proceed") not in print at either twin.** Print asserts "$\Delta c_{crit} = 3$ is simultaneously the K4 lattice connectivity, the trefoil crossing number, and the number of Cosserat sectors … *because* the K4 lattice is 3-connected" (ch03) and "which is simultaneously the trefoil crossing number" (ch06). | `03_neutrino_sector.tex:148-160` (all three legs + the *because* sentence), `06_electroweak_and_higgs.tex:363-366` (leg 2) | `chiral-screening.md:28-48` — leg 2 *"ASSERTED — and in tension with canon"*, leg 3 *"FAILS the counterfactual"*. | The revalidation already named `06:363-365` SUPERSEDED (F8); the ch03 twin is new and carries the strongest form. | WB-LAG · HIGH |
| 3 | **Neutrino body-topology has no KB leaf home, and the obsolete framing survives in a leaf and in print.** The 2026-05-06 corrigendum (closed-loop "twisted unknot" → torsional screw dislocation, open helix) lives only on `ch03-neutrino-sector/index.md:13` (an index — derived) and in print `03:13-15`; **no ch03 leaf and no claim-quality entry carries the screw-dislocation framing** (grep `screw\|open helix\|closed loop` over ch03 leaves and `clm-rji99i`: 0 hits). Meanwhile `regime-classification.md:15` (a leaf) still says **Twisted unknot** unbannered. | `01_topological_matter.tex:207` (regime table), `frontmatter/00_title.tex:18` ("neutrinos as dispersive twisted $0_1$ unknots"), `03_neutrino_sector.tex:272,274` (chapter summary — the `03:19` note covers only the Faddeev-Skyrme section) | `regime-classification.md:15` (stale, unbannered); the canonical framing is homeless at leaf level. | KB-INTERNAL + STALE-KB + WB-LAG in one cluster; needs a word on where the canonical leaf lives before any banner is written. | KB-INTERNAL · HIGH |
| 4 | **Proton mass-ratio headline prints the CODATA value as the derived value.** "precise derivation of the proton-to-electron mass ratio ($1836.15$)", "$m_p/m_e \approx 1836.15$ emerges dynamically as the exact eigenvalue", "The exact proton to electron mass ratio ($1836.15$) is derived"; the title page prints $\approx 1836.14$. Print's own equation (`02:264`) gives **1836.12**. | `02_baryon_sector.tex:7`, `:60`, `:463`; `frontmatter/00_title.tex:18` | `proton-identification.md:13` *"$m_p/m_e = 1836.12$ is derived with zero baryon-data-tuned parameters"*; `:73` D1 headline-fork ruling (2026-07-13, Grant option 2): the headline is the **+0.74 % bare-topology** result, the $-0.002\%$ is $\delta_{th}$-riding. `02:463` already carries the D1 "1-residual" wording but not the number. | Three headline sentences and the title page mis-state the framework's own number and posture. | CONTRA · MEDIUM |
| 5 | **θ-fork ruling (2026-08-23, Grant rulings (a)+(b)) not in print.** "generates a discrete CP-violating $\theta$-vacuum phase" and "trapped vacuum" stand flat. | `02_baryon_sector.tex:319`, `:327`, `:330` | `topological-fractionalization.md:50-76` — θ is the $\mathcal{J}$-dressing, not a vacuum angle; *"The 'CP-violating' adjective is UNDERIVED — and its opposite is asserted elsewhere"*; CP-parity of the dressing OPEN. | A three-week-old Grant ruling on a load-bearing adjective, absent from the printed chapter. | WB-LAG · MEDIUM |

**Runners-up (reader-reported, first-hand spot-checked where marked):** electron handedness — print `01:242` "An electron ($e^-$) is a right-handed unknot" while `chirality-and-antimatter.md:10` was relabelled by the 2026-07-09 R1 adjudication to left-handed Beltrami helicity (ch01-A M6) · "Hopfion" at `01:248` where the leaf twin says `$0_1$ unknot` (ch01-A M7) · `regime-classification.md:17` proton row lags print's real-space/phase-space relabel (STALE-KB, mechanical; ch01-A M5) · tube-geometry fork printed on both sides at `01:40` vs `01:148` while the KB has dated and routed it (ch01-C M5) · W/Z headline table `06:206-211` prints the loop-corrected 80,224 / 90,965 MeV where `lepton-spectrum.md:81` carries 79,923 / 90,624 (ch06-A M3) · neutrino mass eigenvalues `06:321` (9.58 meV) vs `higgs-mass.md:29` (~24 meV) (ch06-A M4) · Higgs breathing-mode mechanism demoted R40-B2a in the **sidecar only** — neither `higgs-mass.md`/`higgs-mechanism.md` nor print `06:808-834` carries the stamp (first-hand: `vol2/claim-quality.md:1710-1720` names the `:162` row; no leaf hit for the banner) · Beryllium 9.32 eV "entirely free of empirical parameters" at `07:277` with the walk-back only in a `%` comment (`07:282-295`) while the KB has 9.28 eV in `hierarchical-cascade-correction.md:54` · Boron 9.4 eV (`07:324`) vs KB 8.30 / 8.065 eV · Lithium 2s/2p l-degeneracy break with opposite sign to `orbital-penetration-penalties.md:39` (`07:224`) · ch05 `weak-coupling.md` lagging the 2026-07-02 print re-anchor (STALE-KB, leaf lags print) · gauge-invariance summary bullet `05:175` and objectivebox `05:8` un-rescoped after R43 (c) · struck ppm labels surviving in `q-g20f-vacuum-polarization.md:97`, `q-g27-muon-cosserat-saliency.md:80`, `ch06 index.md:36` (KB-internal, after the 2026-08-03 strike) · `proton-neutron-mass-split.md:10` "accounts for" (leaf lags the 2026-06-15 print correction — STALE-KB, mechanical).

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

### ch01-B

| TeX range | heading | KB leaf | status | note |
|---|---|---|---|---|
| 01:15-30 | \section{The Mathematical Topology of Mass} | mathematical-topology-of-mass.md | partial | Twin leaf exists by filename (title line absent from its head, so no heading match performed). NOT read in this slice — ch01-A owns it. No grade asserted here. |
| 01:32-35 | \section{Newtonian Inertia as Macroscopic Lenz's Law} | newtonian-inertia-as-lenz.md | partial | Twin leaf exists by filename; also cross-referenced from l3-electron-soliton-synthesis.md:303. NOT read in this slice (ch01-A). No grade asserted. |
| 01:37-121 | \section{The Electron: The Fundamental Unknot ($0_1$)} + scope carve 01:64-80 +… | electron-identification.md + electron-unknot.md | partial | ch01-A's twins; only electron-identification.md:88-93 spot-read here to verify the TeX cites at 01:50/:58/:79. The printed scope carve (01:64-80) is in sync with the KB g=2 / spin-half re-scopes (verified at l3:185, sub… |
| 01:123-143 | \subsection{Resolution of the Electrostatic Point-Charge Singularity} | claim-quality.md:9-38) | partial | Content matches clm-h9aqmt:16 ('finitely resolved' ropelength integral). The 'definitional couple' non-claim at clm-h9aqmt:20 and the leaf-level D.1 CIRCULAR gate (electron-bound-resonator-coverage.md:186) are NOT propa… |
| 01:145-148 | \subsection{The Dielectric Ropelength Limit} | electron-unknot.md | partial | ch01-A twin; ropelength-2pi forcing is asserted at clm-h9aqmt:17. Not read in this slice. |
| 01:150-167 | \subsection{The Hollow-Vortex Binding Structure (Class-C Consistency)} | hollow-vortex-binding.md | partial | ch01-A twin, not read here. Print 01:167 is IN SYNC with pair-production-axiom-derivation.md:103 (A1 mass core sub-saturated at A=sqrt(alpha)) and with the T2/V_yield self-trap — verified both sides. |
| 01:169-193 | \subsection{Deriving the Running Coupling Constant} (+ figures 01:181-193) | :21 (no dedicated running-coupling leaf in ch01) | partial | The 01:170 \kbleaf cite to clm-h9aqmt RESOLVES: clm-h9aqmt:18 carries 'This is a sketch' and :21 the beta-function non-claim. Known-debt item 01:170 is DISCHARGED at HEAD (the honesty scoping is printed inline). |
| 01:195-214 | \section{Regime Classification of Topological Matter} | regime-classification.md | partial | ch01-A twin, not read here. The electron row (01:208, 'II (Yield), $\Delta\phi = \alpha$; self-confinement') is CONSISTENT with pair-production-axiom-derivation.md:102 (the single electron's confining Gamma=-1 T2 wall i… |
| 01:216-239 | \section{The Torus Knot Phase Winding Ladder} |  clm-8c3yhs) | partial | ch01-A twins, not read here. Known-debt 01:218 and 01:237 are DISCHARGED at HEAD: both lines now carry the 'dimensionless coupling-budget ratio, NOT a length' correction inline with the proton-identification cite. l3:37… |
| 01:241-261 | \section{Chirality and Antimatter Disintegration} | chirality-and-antimatter.md | partial | ch01-A twin, not read here; its Handedness Register (D4) is quoted from pair-production-axiom-derivation.md:138. Known-debt 01:242 cite VERIFIED: clm-wcoul2 exists at vol4/claim-quality.md:1879 and the \kbleaf path reso… |
| 01:263-273 | \section*{Chapter Summary} + \section*{Exercises} | (none) | tex-only | Summary/exercise matter; no KB twin expected. Exercise 2 (01:273) restates the phase-space vs real-space disambiguation correctly (matches l3:47-57 INVARIANT-N1 note). |
| (none) | (no TeX twin) | l3-electron-soliton-synthesis.md | kb-only | Research-origin leaf (clm-8zpicx, solidity 0.40 'do not build on'). Only reachable from print via the % comment at 01:53. No printed section translates it. |
| (none) | (no TeX twin) | substrate-perspective-electron.md | kb-only | Research-origin leaf (clm-jupq56, solidity 0.35). Cited from print only in the % comment at 01:54. |
| (none) | (no TeX twin) | electron-bound-resonator-coverage.md | kb-only | Coverage sheet, no-claim frontmatter (originates no clm-). NOT cited anywhere in TeX 01 (two-method check: grep for kbleaf/.md in the chapter returns no reference). |
| (none) | (no TeX twin) | electron-unknot-cosserat-seeder.md | kb-only | Research-origin leaf (clm-gfdplp, solidity 0.50). NOT cited in TeX 01, yet 01:107-111 prints the v14 engine receipt this leaf demoted on 2026-08-11 — see mismatch M1. |
| (none) | (no TeX twin) | pair-production-axiom-derivation.md | kb-only | Research-origin leaf (clm-ezai5b, solidity 0.40). NOT cited in TeX 01. Its §4 sectoral resolution IS printed (01:167) even though the leaf is uncited. |

KB-only leaves (no print twin):
- `l3-electron-soliton-synthesis.md` — 318 lines, clm-8zpicx. No TeX twin. Carries three dated Rule-12 sites: :132 DIRECTION-OF-THE-2 strike (2026-08-06, R16/FLAG-D), :185 g=2 mechanism-vs-value banner (2026-07-09, cited from TeX 01:53), …
- `substrate-perspective-electron.md` — 296 lines, clm-jupq56. No TeX twin. Carries the 2026-06-21 g=2 Rule-12 re-scope at :11 (cited by TeX 01:54, resolves) plus the WALL-A deficit-knee re-tag (:132-148, Grant 2026-07-14). The WALL-A reta…
- `electron-bound-resonator-coverage.md` — 376 lines, no-claim coverage sheet. No TeX twin, and NOT cited from TeX 01. Carries the K4-echo kill in five places (Q≈30.8 NOT 137; :73, :89, :164, :170, :172, :228) — all Q1, self-disclosed. Carrie…
- `electron-unknot-cosserat-seeder.md` — 205 lines, clm-gfdplp. No TeX twin. 'Mode III on K4-TLM / Mode I PASS on Master Equation FDTD' at :112-:113 — the Mode I PASS row is 🔴 DEMOTED 2026-08-11 (R40-B2a) with the dated note at :144-:199. G…
- `pair-production-axiom-derivation.md` — 207 lines, clm-ezai5b. No TeX twin. Two-node pair nucleation (:35 'An electron is a bound state of the K4 lattice consisting of two adjacent K4 nodes...') vs TeX 01:38 single 0_1 unknot loop — FLAG-D…

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
| 1-11 | \chapter + objectivebox | index.md (derived) | tex-only | :7 headlines 'precise derivation of the proton-to-electron mass ratio ($1836.15$)' -- see MM-11/MM-12. |
| 12-27 | A-034 nuclear-scale instance paragraph | (none) | tex-only | grep 'A-034' over ch02 KB dir: 0 hits. |
| 30-41 | \section Borromean Confinement: Deriving the Strong Force (+fig :33-39, Scale P… | (none in ch02 dir) | tex-only | index.md:33 claims topological-fractionalization.md covers 'Borromean confinement; scale paradox' but that leaf carries only the Witten section (:8-46) + dated notes. :41 is quoted by proton-identification.md:152 as 'Ro… |
| 43-56 | \subsection The Topological Scaling Ansatz | (none; index.md:17 row only) | tex-only | :52 uses (137.036) as the 'dielectric saturation boundary' multiplier -- not a K4 Q=137 cage-emergent claim. |
| 58-65 | \section The Proton Mass: The Dynamic Tensor Deficit (resultbox Saturated FS Pr… | (none; index.md:18 row only) | tex-only | :60 'emerges dynamically as the exact eigenvalue' -- sibling of MM-11. |
| 67-76 | \subsection The Faddeev-Skyrme Coupling Constant | thermal-softening.md:42-52 | verbatim-match |  |
| 78-153 | \subsection Thermal Lattice Softening (label sec:thermal_softening) | thermal-softening.md:9-40 | partial | :92 cold triplet (1170.6 / 1849.70 / +0.7377%) byte-matches leaf :11 -- MR-board 02:81 [HIGH stale-value] RESOLVED at HEAD (sentence moved :81->:92; prior triplet preserved in % block :80-91). :120-129 nu_Hill clause ma… |
| 155-165 | \subsection The 3D Orthogonal Tensor Trace | thermal-softening.md:54-66 | verbatim-match |  |
| 167-179 | \subsection Computational Proof: Skew-Lines and The Toroidal Halo | thermal-softening.md:68-80 | verbatim-match |  |
| 181-220 | \subsection The Self-Consistent Mass Oscillator (1st occurrence: crossings, Gau… | thermal-softening.md:82-122 | verbatim-match | :182 'resolve the total saturated volume $\mathcal{V}_{total}$ of the toroidal halo' is print-only retired framing, disclosed within 8 lines (:188-191 'Do not fuse', :206) -- not debt. Duplicate subsection title with :2… |
| 222-235 | \subsection The Cinquefoil Confinement Bound | self-consistent-mass-oscillator.md:12-26 | partial | 2026-06-08 dimensional relabel propagated to both sides; wording differs (print integrates the relabel, leaf strikes-and-banners). :226 '(2,3) pattern ... ground-state topology is the unknot' = static winding dictionary… |
| 237-275 | \subsection The Self-Consistent Mass Oscillator (2nd occurrence: eigenvalue, 18… | self-consistent-mass-oscillator.md:28-64 | verbatim-match | :268 honesty-scoping paragraph mirrors leaf :64 + proton-identification.md:13. :238/leaf :30 share the stale 'derived in Chapter 2' cross-ref (MM-16). |
| 277-316 | \section The Baryon Resonance Spectrum: The Torus Knot Ladder | torus-knot-ladder-baryons.md:9-51 | diverged | Print :309 scope correction (2026-06-19, printed+dated) mirrors leaf :11/:41. Table c=9,11,13 rows match the 2026-07-02 canonical driver; c=15 row does NOT (MM-03). Fig caption :314 '+9.8%' / 'validated' (MM-04). Leaf-o… |
| 318-352 | \section Topological Fractionalization: The Origin of Quarks | topological-fractionalization.md:8-46 | diverged | Body verbatim; leaf carries the 2026-08-23 dated surface note (:50-76: theta is J-dressing not vacuum angle; 'CP-violating' UNDERIVED; Witten formula-not-mechanism) and the 2026-06-23 two-ontology section (:78-88) with … |
| 354-364 | \section Neutron Decay: The Threading Instability | proton-neutron-mass-split.md:8-10 | diverged | Print :357/:362 corrected 2026-06-15 to 'proposed structural origin ... not yet a first-principles derivation' (comment :356); leaf :10 still 'accounts for the mass surplus' (MM-06). Canonical honest scoping lives in kb… |
| 366-402 | \section The Helium-4 Nucleus (Mass-Stiffened Strong Force, Elastic Displacemen… | proton-neutron-mass-split.md:12-48 | verbatim-match | Both sides carry T_nuc 389.2 N (:376/leaf :23) then 390.5 N (:386,:390/leaf :28,:33) -- print-internal inconsistency mirrored verbatim, no sync dimension. |
| 404-414 | \subsection Simulation of Topological Core Gradients (+fig tensor_halo) | (none) | tex-only | :407 '1.955 fm' vs :390 '1.933 fm' -- print-internal; no KB twin (grep 'Core Gradients\|1.955' in KB dir: 0 hits). |
| 416-457 | \subsection The Hierarchy Bridge | proton-neutron-mass-split.md:50-89 | verbatim-match | 2026-06-15 G-ruling reconciliation landed on both sides (print :427/:449 inline; leaf :60/:82 bannered). Leaf :82 and print % comments :448/:465 cite claim-quality.md :754 -- stale (MM-09). Leaf :91-95 z0 note is kb-onl… |
| 459-467 | \section* Chapter Summary | index.md:11 (derived) | tex-only | :463 'exact ... ($1836.15$) is derived' (MM-11); :466 'strictly resolved' (MM-14). % comments :462/:465 are the 2026-06-15 Rule-12 trail; printed bullets already carry the corrected wording. |
| 469-472 | \section* Exercises | (none) | tex-only |  |

KB-only leaves (no print twin):
- `proton-identification.md` — Research-origin canonical hub (path-stable); no TeX twin. Carries the D1 headline-fork ruling 2026-07-13 (:73), the r_p two-routes KEEP-BOTH flag 2026-07-19 (:145-157) + 2026-08-23 third arm (:158-16…
- `neutron-identification.md` — Research-origin canonical hub; no TeX twin. Carries the honest scoping (mass split not derived, :15/:36/:54; lifetime not derived) that print :357/:362 now cite, plus the 2026-08-23 CP note (:73-83).…
- `quark-flavors.md` — GAP stub; points to topological-fractionalization.md. No debt.
- `torus-knot-ladder-baryons.md :23-35 forward rows c=17,19,21 + :49 stale-framing correction` — KB-only content inside a twinned leaf (print table stops at c=15).
- `topological-fractionalization.md :50-88 (2026-08-23 surface note + 2026-06-23 two-ontology reconciliation, clm-w8jn3q)` — KB-only sections inside a twinned leaf; the CP-adjective carve contradicts print :319 (MM-01); the two-ontology section does not contradict print (:322 already states Q_total=+1e integer).
- `proton-neutron-mass-split.md :91-95 (force-dilution vs coordination z0, 2026-06-08)` — KB-only consistency-class link; no print twin; not contradicted by print.

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
| 5-12 | objectivebox (chapter objectives) | (none; index.md:11 blurb is DERIVED) | tex-only | :8 states 'Derive the physical origin of Gauge Invariance (U(1))' flatly; no time-independent-only caveat (see CH05-M2). |
| 14-17 | \section Electrodynamics: The Gradient of Topological Phase | gauge-boson-masses.md:8-12 | verbatim-match | Markup-stripped diff clean. |
| 19-28 | \subsection Magnetism as Convective Vorticity | gauge-boson-masses.md:14-26 | verbatim-match | Only cosmetic: TeX $\ell_{node}$ vs leaf $l_{node}$. |
| 30-35 | \subsection The Inductive Origin of Gauge Invariance (body) | gauge-boson-masses.md:28-34 | verbatim-match | Both carry the printed R43 rescope 'This closure holds for time-independent Λ ONLY (rescoped 2026-08-10 under R43...)'. TeX:35 additionally carries '(eq_axiom_3.tex, Axiom 3's Noether clause)' and says 'this section' wh… |
| 37-50 | % Rule-12 repair trail (incompressibility premise struck 2026-08-03; E-leg corr… | gauge-boson-masses.md:36-50 (repair blockquote) | partial | TeX trail is comment-only, but the PRINTED :51 Premise note discloses the struck premise and the garbled E coverage in print, so this is disclosed. KB blockquote carries the full explanation with three 🔴 stamps (:38 R40… |
| 51 | Premise note (2026-08-03) + [SUPERSEDED 2026-08-10] + SECOND FAILURE (R43 (c)) … | gauge-boson-masses.md:36-50 + :79-83 (EOF SECOND FAILURE no… | partial | Print and leaf agree on substance: first failure (incompressibility) struck, second failure (no-restoring-force ⇒ no energy) rescoped, 'canon holds no valid derivation of any full U(1) family'. TeX:51 carries ONE generi… |
| 53-61 | \section The Weak Interaction: Inductive Cutoff Dynamics | gauge-boson-masses.md:52-63 | verbatim-match | wall-taxonomy.md:336-338 (Q20-Q22) records the declared emphasis/symbol drifts at leaf :55/:57/:62; anchors verified live at HEAD. |
| 63-74 | \subsection Deriving the Gauge Bosons (W/Z) as Evanescent Modes | gauge-boson-masses.md:65-75 | verbatim-match | TeX:74 ends 'reduces this stiffness ratio to:' (leads into examplebox); leaf :75 ends with '.' — cosmetic. |
| 76-89 | examplebox Deriving the Weak Mixing Angle via Isotropic Elasticity | weinberg-angle.md:8-38 | diverged | Print relabelled ν_vac→ν_Hill (commit dec3b7e1, 2026-08-02, CRIB-1, TeX only) and reworded :83 to 'trace-reversed operating point ... an averaging choice, not a lattice-emergent limit' with a Rule-12 comment banner at :… |
| 91-115 | \subsection The Absolute W Boson Mass: Chirality Mismatch Self-Energy | weak-coupling.md:8-36 | diverged | Print carries the Grant-ruled α² native re-anchor (commit 23a0ff2d, 2026-07-02, TeX only): 'product of two Axiom 4 susceptibility couplings', varactor, 'second-order reactive (intermodulation) term', resultbox titles 'T… |
| 117-119 | \section Electroweak Mechanics: Forward Reference | forward-to-ch6.md:8-10 | verbatim-match | Print says a_e = α/2π etc. are 'presented in full' in ch06 — a ch06-lane check, not ch05 debt. |
| 122-133 | % commented-out figure electroweak_acoustic_modes.png (FIGURE MISSING) | (none) | tex-only | Comment-only, Rule-12 honest; no KB twin expected. |
| 135-159 | \section The Gauge Layer / \subsection U(1) Electromagnetism from the Lattice P… | forward-to-ch6.md:12-40 | verbatim-match | Byte-level twin, BUT both :159 and leaf :40 assert 'U(1) Electromagnetism ... here derived from the physical structure of the substrate hardware' with no cross-reference to the printed R43 rescope at :35/:51 (see CH05-M… |
| 161-171 | \subsection SU(3) Color Charge from the Borromean Linkage | forward-to-ch6.md:42-52 | verbatim-match | Borromean 6^3_2 proton premise: ch02 proton-identification.md:22/:33 RELABELLED 2026-06-08 (real-space-topology slot), not refuted — no HIGH here. |
| 173-179 | \section* Chapter Summary | (none) | tex-only | :175 'Gauge Invariance is explicitly derived...' and :178 'U(1) and SU(3) Gauge symmetries are explicitly proven...' restate the pre-rescope claim flatly (CH05-M1, CH05-M3). |
| 181-185 | \section* Exercises | (none) | tex-only | No sync content. |
| 186-248 | % R40 batch-2a [NEEDS-RE-DERIVATION status-note heading] (2026-08-11) — comment… | gauge-boson-masses.md:131-203 (printed in leaf) | partial | Leaf prints the full note incl. axiom-register clause G bound response, A_g UNVALUED-RATIFIED-CONSTANT (R48), calibration count 3, BIAS-DEBT rider; TeX carries it only as % comment (:201-206 included). TeX row list (:22… |
| (none) | (KB-only) R40 batch-1 demotion note — DIES-WITH-THE-PHANTOM | gauge-boson-masses.md:87-129 | kb-only | Demotes the leaf's own :48 mass-flow/A-vs-u refutation-threat flag; no TeX twin (TeX:33 'to the mass flow' never carried the flag). |

KB-only leaves (no print twin):
- ` def-uatk1s premise-critical flag, 🔴 DEMOTED 2026-08-11 R40-B1)` — KB-only content block inside an otherwise TeX-twinned leaf; the flag targets TeX:33 wording but print never carried it; the flag itself is now demoted (threat void under the R40 carve). See CH05-M12.
- `gauge-boson-masses.md:79-83 (★ SECOND FAILURE EOF note, placement note + authorship fence)` — The substance is mirrored in print at TeX:51 (condensed, inline); the placement note and LANE-AUTHORED authorship fence are KB-only (print says 'repair prose LANE-AUTHORED against Tier-2 finding C22'…
- `gauge-boson-masses.md:87-129 (🔴 R40 batch-1 demotion note)` — No TeX twin; explains why the :48 flag dies. Not debt.

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
| 449-484 | \section{Schwinger's Anomalous Magnetic Moment ($g-2$)} | higgs-mass.md:36-77 | verbatim-match | LaTeX->MD translation is line-for-line; only markup differs (\boxed at 06:481 dropped at KB:74). clm-stgx1i register entry consistent (leading-order only). |
| 486-555 | \subsection{Toward the Second-Order Correction} (K4 Bethe-tree, Route B headlin… | two-stage), :246 (legacy engine) | partial | Print discloses the K4-Bethe-tree refutation (footnote dated 2026-05-13 at 06:512) and the 2026-08-02/03 scope + ppm-strike (06:536-542 prints 'at the printed five-decimal precision, and at no finer precision than that'… |
| 557-604 | \paragraph{Route B substrate derivation (full).} | q-g19a-petermann-saliency-closure.md:24-49 | verbatim-match | Five ingredients and the display block match. Both sides print the mutually inconsistent Δa_e (1/π²·⟨⟩·α/π) and C_2 (2/(πα)·⟨⟩) forms (06:598-604 = KB :47-48); KB self-discloses at :166-179, print only in a % comment. τ… |
| 606-626 | \paragraph{Numerical robustness (Route B base case, $\delta = 0$).} | q-g19a-petermann-saliency-closure.md:51-61 (+ :150-164 F3 s… | partial | Values match (-3.916e-3, -0.3416, +4.0%). KB :164 (2026-08-03) scopes the 'converges at N_t ≳ 2e5' and 'invariant under three derivative methods' receipts to the Stage-1 4% level (non-probative at ppm level; retardation… |
| 628-655 | \paragraph{Saliency closure ($\delta = -3\alpha/2$).} | q-g19a-petermann-saliency-closure.md:63-85 | verbatim-match | δ* = -0.01093, δ*/α = -1.4982, boxed δ = -αn_q/2 match. The RESOLVED-NEGATIVE verdict is carried by both sides further down (print 06:753-770; KB :221). |
| 657-723 | \paragraph{Final result --- printed-precision match at $C_2$, postulate-conditi… | q-g19a-petermann-saliency-closure.md:87-95, :207-216, :232 | verbatim-match | Values -1.772e-6, -0.32846, 1.15964e-3 vs 1.15965e-3 match KB :92/:209; ppm labels struck on both sides (commit 3ba628f3 print-side). Print anchors ':92/:100/:103 ... :121' at 06:723 are stale after the 2026-08-03 inser… |
| 725-775 | \paragraph{What still needs derivation (honest open items).} | q-g19a-petermann-saliency-closure.md:218-222 | verbatim-match | Print carries the 2026-08-02 RETRACTION REWRITE (RESOLVED NEGATIVE, one-point fit) with prior wording preserved in the % comment 06:731-752 (Rule 12 honored in print AND git). The cite ':110' at 06:770 is stale (content… |
| 777-783 | 'Zero parameters were fudged' + legacy g_minus_2_lattice.py superseded | q-g19a-petermann-saliency-closure.md:238-246 | partial | Ingredient list and engine-superseded note match. KB :240-244 adds the dated (2026-08-02) 'No fit parameters — at Stage 1' scope label at exactly this section; print lacks the label (its preceding paragraphs 06:709-723 … |
| 785-788 | \section{The Higgs Boson Mass} (intro: λ and v 'derived quantities') | lambda-higgs-derivation.md:12, :22 (no vol2 ch06 leaf) | diverged | Print 06:788 asserts 'both λ and v are derived quantities---not free parameters'; the vol6 leaf's :12 note re-scopes the Higgs<->K4-breathing identification as FORM-identification, not VALUE-derivation (quaternion-scala… |
| 790-796 | \subsection{The Fermi Constant from $M_W$ and $\sin^2\theta_W$} | mathematical-closure.md) | tex-only | No leaf twin found by grep for G_F / 248.8 / v_{AVE} in ave-kb/vol2/particle-physics/ch06-electroweak-higgs/. Not debt by itself. |
| 798-806 | \subsection{The Vacuum Expectation Value (VEV)} | (none in vol2 ch06) | tex-only | v_AVE ≈ 248.8 GeV (+1.1%) and the 376.73 Ω 'physical meaning' paragraph have no ch06 leaf twin; higgs-mechanism.md carries the Z_0 = 376.73 Ω identification only (out of slice). |
| 808-833 | \subsection{The K4 Breathing Mode: $M_H = v/\sqrt{N_{K4}}$} + resultbox + engin… | lambda-higgs-derivation.md:14-38 (PATH-STABLE sec:lambda_hi… | partial | λ = 1/8, M_H = v/2 ≈ 124,4xx MeV, and the 2026-05-17 Foundation Item 7 scope correction (-1.59% to -1.68% forward) are on both sides (print 06:828 = leaf :16). Divergences: (a) R40 batch-2a (2026-08-11) DEMOTED the acou… |
| 835-853 | \section{Summary of Electroweak Predictions} | higgs-mass.md:79-92 | partial | Tables identical row-for-row EXCEPT the M_H row (06:844, -0.55%) exists only in print (KB table has 7 rows, no M_H). 06:853 prints the 2026-06-15 'three retained calibration inputs' relabel with prior wording preserved … |
| 855-867 | \subsection{Standard Model $\leftrightarrow$ AVE Translation Dictionary} + fig:… | translation-particle-physics.md) | verbatim-match | Forwarder maps \input{../common/translation_particle_physics.tex} correctly by label (sec:sm_ave_translation) but its printed TeX line cite 'line 305' is stale (HEAD 06:860) — see ch06B-10. Figure caption 06:865 (partic… |

KB-only leaves (no print twin):
- `q-g20f-vacuum-polarization.md` — No TeX twin anywhere in 06_electroweak_and_higgs.tex (grep for 'vacuum polarization\|Uehling\|Landau pole\|RT-equivalence\|Renormalization Theorem' returns 0 hits in the whole chapter). Research-orig…
- `q-g27-muon-cosserat-saliency.md` — No TeX twin for the muon g-2 saliency in ch06 (grep for '502\|Cosserat saliency\|Fermilab\|a_\mu' returns 0 hits); its manuscript anchors (Vol 2 Ch 6:154-176 Cosserat constants) lie in the ch06-A sli…
- `higgs-mass.md:8-34 (The Neutrino Mass Spectrum)` — Twin is TeX 06:271 (\section{The Neutrino Mass Spectrum}) — OUTSIDE this slice (ch06-A). Listed only so the ch06-A lane knows the leaf named 'higgs-mass.md' holds the neutrino spectrum + Schwinger + …
- `index.md` — Derived index. :36 blurb lags the leaf (un-struck ppm labels; 'single remaining intuitive step at q-g19a:98' — now RESOLVED NEGATIVE at :221) — see ch06B-11. :34 correctly describes higgs-mass.md's a…

### ch07-A

| TeX range | heading | KB leaf | status | note |
|---|---|---|---|---|
| 1-11 | objectivebox | de-broglie-standing-wave.md:8-13 | verbatim-match |  |
| 13-17 | \section{Deterministic Reinterpretation of the Wavefunction} | de-broglie-standing-wave.md:15-20 | verbatim-match | KB carries <!-- claim-quality: clm-qde5gn --> |
| 19-34 | \subsection{The Helmholtz--Schrödinger Isomorphism} | de-broglie-standing-wave.md:22-42 | verbatim-match |  |
| 36-43 | \subsection{Transverse Shear vs. Longitudinal Bulk Cavities} | de-broglie-standing-wave.md:44-54 | diverged | Both sides carry the printed R40-B2a stamp (TeX :41 / KB :52). KB :50 adds a 2026-06-11 three-impedance-law channel note (gravity wave Z_shear != 377) that print :39 lacks (M9). TeX stamp pointer 'dated note at the end … |
| 45-48 | \subsection{Gravitational Parallax Interferometry} | de-broglie-standing-wave.md:56-60 | diverged | Print :46 writes n_s = 9/7 eps11 (no '1 +'); KB :58 writes n_s = 1 + 9/7 eps11 with a dated 2026-05-17 notation-cleanup note (M8). KB :60 is AHEAD of print: adds Delta-Phi ~ 250 rad at 100 eV / 1 m and the driver-script… |
| 50-63 | \section{Orbitals as Acoustic Resonant Cavities} | de-broglie-standing-wave.md:62-70 | verbatim-match |  |
| 65-84 | \subsection{Hydrogen Ground State from LC Impedance Matching} (+ examplebox) | de-broglie-standing-wave.md:72-95 | verbatim-match | '137 x l_node' is a_0 identification, not a K4 Q=137 corpse |
| 86-107 | \subsection{Angular Momentum Quantization} | de-broglie-standing-wave.md:97-111 | verbatim-match |  |
| 109-131 | \section{Hydrogen Energy Levels: AVE vs. CODATA} | de-broglie-standing-wave.md:113-124 | verbatim-match |  |
| 133-150 | \subsection{Numerical Verification: ODE Eigenvalue Solver} | ode-verification.md:8-30 | verbatim-match |  |
| 152-162 | \subsection{Dimensional Analysis: a_0 = l_node/alpha} | ode-verification.md:33-43 | verbatim-match | Known 07:161 site CONFIRMED at HEAD: the 2026-06-15 recon note is a % comment at :161, BUT the printed sentence at :162 already carries the Class-B identification caveat inline ('a Class-B geometric \emph{identification… |
| 164-178 | \subsection{Regime Identification of Atomic Orbitals} | ode-verification.md:45-53 | verbatim-match | Both sides say r<a_0 is Regime II (Yield); this conflicts with de-broglie-n.md:10 / de-broglie-standing-wave.md:244 (linear / deep Regime I) — KB-INTERNAL M12. |
| 180-185 | \section{Helium and the Symmetric Topological Cavity} | helium-symmetric-cavity.md:8-12 | verbatim-match |  |
| 187-198 | \subsection{QM <-> AVE Translation Dictionary} | qm-ave-translation.md:10-16 | verbatim-match | Table body is \input{../common/translation_qm.tex}; KB points to common/translation-tables/translation-qm.md (not read; outside slice) |
| 200-210 | \subsection{The Spatial Extent of the 0_1 Unknot} | helium-symmetric-cavity.md:14-24 | partial | KB drops the final sentence (:210 'The observed 1s continuous spatial density ...'); no contradiction |
| 212-235 | \subsection{The Mutual Cavity Loading Architecture} + 3-Phase Evaluator Pipelin… | helium-symmetric-cavity.md:26-42; orbital-penetration-penal… | diverged | TeX Phase A/B/C pipeline vs KB 'N-Electron Pipeline' (Op1 N_s=1.0/N_p=0.5, Op3 T^2, Hund) — different N_eff assignment rule (M4 facet). Li resultbox :218-228 (2s 5.75 eV / 2p 13.26 eV) has NO numeric KB twin (0 hits); m… |
| 237-250 | \subsection{Phase C: Transverse Buckling vs. Hopf Strain} | (none) | tex-only | :239 carries printed R40-B2a stamp (Euler-buckling/K-carrier family). :243 N_eff=1.0+0.5=1.5 and +72%->-2.6% has no KB home (MR board 07:243; revalidation finding 14) and contradicts :253 N_eff=2.0 (M4). :243 also carri… |
| 252-257 | He IE resultbox (24.19 eV, -1.6%) | helium-symmetric-cavity.md:44-50 | verbatim-match | KB elsewhere reports He at 24.37 eV / -0.88% (bonding-mode-formula.md:42, helium-coupling-first-principles.md:52, ionization-energy-validation.md:21, clm-w6kk5y:377) — different method; index.md:23 lists only 24.19. Fla… |
| 259-311 | \subsection{Field-Oriented Control (FOC) and the Secondary Density Wake} (+ Emi… | helium-symmetric-cavity.md:52-70 | partial | KB is condensed. KB silently omits the printed Be 9.32 eV claim (:277) whose walk-back lives ONLY in the % HISTORICAL NOTE :279-292 (M1). TeX :294-300 (27x spin ratio) and :303-311 (Emission Paradox) are tex-only. |
| 313-333 | \subsection{The p-Shell Isomorphism: Orthogonal Inductive Buckling} (+ Protein … | helium-symmetric-cavity.md:72-80 | partial | KB omits the printed Boron 9.4 eV IE claim (:324, contradicts subshell-junction-scattering.md:11 8.30 eV — M2) and omits the printed 'Tier-1 derivation status' protein-engine sentence (:333 — M5). |
| 335-350 | \section{The Atom as an Analog Ladder Filter} + \subsection{Screening as Freque… | analog-ladder-filter.md:8-20 | verbatim-match |  |
| 352-390 | \subsection{LC Components of the 1s Flux Loop} | analog-ladder-filter.md:22-60 | diverged | Text verbatim, but TeX :383 carries the printed R40-B2a stamp and KB :52 (its twin) carries none (STALE-KB M10). |
| 392-410 | \subsection{Intra-Shell Coupling: Coulomb Capacitance, Not Mutual Inductance} | analog-ladder-filter.md:62-72 | verbatim-match |  |
| 412-447 | \subsection{Multi-Shell Filter Cascade} (+ signal-flow figure + Regime Validati… | analog-ladder-filter.md:74-88 | partial | KB omits the tcolorbox figure (:419-438) and the 'Regime Validation' resultbox (:440-447) — tex-only content |
| 449-472 | \subsubsection{Explicit S(r) Metric Saturation Derivation} | (none) | tex-only | 0 KB hits for kappa_{Hopf} / 'Regime-Aware' / 'Regime Validation' across the ch07 dir (incl. radial-eigenvalue-solver.md) |
| 474-481 | filter-framework bullets | analog-ladder-filter.md:90-94 | verbatim-match |  |
| 483-506 | \subsection{Radial TL Eigenvalue and the Screening Rule} (intro + Regime IV res… | de-broglie-n.md:8-20 | diverged | Print :485/:488 asserts deep-core strain past the Regime IV yield limit for Z>=19; KB :10 asserts V/V_yield ~ Z alpha^2 ~ 1e-4 puts the entire atom in the linear regime (M6). Resultbox :486-490 'Regime IV Vacuum Yield B… |
| 508-521 | radial_eigenvalue sweep / IE = xi_0 R_y | de-broglie-n.md:20-28 | verbatim-match |  |
| 523-563 | \paragraph{The Screening Rule: Two Distinct Physics.} + AVE Screening Rule resu… | screening-rule.md:8-36 | verbatim-match |  |
| 565-570 | \subsection{Macro-Cavity Saturation} | macro-cavity-saturation.md:8-12 | verbatim-match | 'previous section' (TeX) vs 'helium section' (KB) — cosmetic |
| 572-577 | \subsubsection{Complete Geometry-to-Solver Pipeline} (intro) | geometry-pipeline.md:8-10 | verbatim-match | Stages A-E of geometry-pipeline.md correspond to TeX beyond 1100 (other slice) |
| 579-810 | \paragraph{Step 1: Single-Electron Eigenvalue} (a)-(h) + Step 1 Summary | de-broglie-standing-wave.md:127-239 (+ atom-as-radial-waveg… | partial | KB condenses (drops dimensional checks, 'Physical meaning of l', 'Coulomb l-degeneracy'). KB :240 adds a terminology note (mode-count, cavity-deformable, NOT the (2,3) winding) that print :725-726 lacks — print still ca… |
| 812-1100 | \paragraph{Step 2: Lattice Strain Between Shells} (a)-(f) incl. supercavitation… | de-broglie-standing-wave.md:242-261 | partial | KB is a summary paragraph + Step 2 Summary box. The c_P = c sqrt(10/3) P-wave paragraph (:1036-1053) has NO KB twin; print :1053 carries the R40-B1 stamp whose pointer resolves to a PRINTED note at :4150-4191 (disclosed… |

KB-only leaves (no print twin):
- `radial-eigenvalue-solver.md` — 816 lines; Steps 3+/E2 content. Grep-indexed only; no twin in TeX 1-1100 (likely twinned in the ch07-B/C ranges).
- `brillouin-zone-uv-cutoff.md` — Research-origin (GR-QED Stage-2); no twin in range 1-1100.
- `q-g20a-lamb-shift-structural-closure.md` — Research-origin (Lamb shift FORM match); no twin in range 1-1100.
- `bonding-mode-formula.md` — Stage E1; no twin in 1-1100 (He 24.37 eV value differs from the in-range 24.19 eV MCL value — different method; see notes).
- `complete-solver-architecture.md` — No twin in 1-1100 (references 'Step 2' summary values consistently with dbsw:244).
- `dual-formalism-architecture.md` — No twin in 1-1100; carries Li IE 5.32 eV (another Li value; see notes).
- `knot-vs-orbital-table.md` — No twin in 1-1100.
- `operator-domain-table.md` — No twin in 1-1100.
- `scale-separation.md` — No twin in 1-1100; carries the 'K = 2G from nu = 2/7, Axiom 2' wording that is the KB side of board item 07:3510 (outside this slice).
- `chiral-factor.md` — No twin in 1-1100; :45 '(2,3) trefoil produces 6/5' is the HOPF-01 antenna chiral factor (fence-excluded, see corpseHits).
- `helium-coupling-first-principles.md` — No twin in 1-1100.
- `stepped-impedance-resonator.md` — No twin in 1-1100.
- `hierarchical-cascade-correction.md` — No twin in 1-1100, but it is the KB's canonical Be value (9.28 eV, -0.45%) that the print :277 9.32 eV claim and its % HISTORICAL NOTE point at (M1).
- `ionization-energy-validation.md` — No twin in 1-1100; carries B exp 8.298 / AVE 8.065 (contradicts print :324 'Boron 9.4 eV', M2) and Li 5.525 (+2.46%).
- `subshell-junction-scattering.md` — No twin in 1-1100; :11 states Boron IE 8.30 eV (M2 KB side).
- `orbital-penetration-penalties.md` — Research-origin format (<!-- leaf: verbatim --> but no TeX section twin); mechanism twin of the Li resultbox :218-228 with the opposite sign of the 1/d penalty (M3). Its :48 is an R40 worklist SURVIV…

### ch07-B

| TeX range | heading | KB leaf | status | note |
|---|---|---|---|---|
| 1100-1159 | (Dirac/supercavitation correspondence table + resultbox 'Step 2 Summary', tail … | none found | tex-only | No ch07 KB leaf (assigned candidates or full-dir ls) contains 'supercavitat' or 'Dirac'; this content appears untranslated to KB. Not itself debt per the TEX-ONLY rule, but flagged as a coverage gap. |
| 1161-1201 | Stage A: Per-Electron Geometry; Stage B: Pair Classification | geometry-pipeline.md | verbatim-match | geometry-pipeline.md lines 12-31 reproduce Stage A/B equations and the pair-classification table verbatim (modulo markdown vs LaTeX table syntax). |
| 1203-1246 | Stage C, Type 1: Same-shell Hopf link (Op4+Op2) | helium-coupling-first-principles.md; geometry-pipeline.md | verbatim-match | helium-coupling-first-principles.md derives the same k_Hopf=2/Z(1-p_c/2) result with full He worked numbers matching TeX 1220-1246 and 1439-1446 exactly. |
| 1248-1313 | Stage C, Type 2 (orthogonal) and Type 3 (cross-shell elliptic-integral) + Li 1s… | geometry-pipeline.md | partial | geometry-pipeline.md lines 47-63 carry the Type-2/Type-3 formulas verbatim but omit the worked Li 1s-2s numerical check (TeX eq:li_cross_shell_energy, lines 1295-1312, K(1/4)=1.6858, 21.90 eV, k_cross=0.358). Omission o… |
| 1314-1360 | Stage D: Y-Matrix Assembly (Axiom 1, Kirchhoff / KCL) | geometry-pipeline.md (formula); macro-cavity-saturation.md … | diverged | geometry-pipeline.md:65-71 reproduces the Y-matrix KCL formulas verbatim, presenting them as part of the current 'Mutual Cavity Loading IE solver' pipeline (mirroring TeX:567's own mislabeling) -- while the sibling leaf… |
| 1361-1446 | Stage E1: Same-shell bonding mode + He verification | bonding-mode-formula.md; helium-coupling-first-principles.md | verbatim-match | bonding-mode-formula.md reproduces the full E1 derivation and He numeric verification (39.40 eV, 78.79 eV, IE=24.37 eV) byte-for-byte equivalent to TeX 1368-1446. |
| 1447-1546 | E2 intro (QM-contamination-audit % comment), vocabulary mapping, solver-archite… | complete-solver-architecture.md | verbatim-match | complete-solver-architecture.md's resultbox (lines 10-24) and QM-contamination checklist table (34-42) match TeX 1548-1556 and 1530-1546 verbatim. The QM-contamination-audit comment itself (TeX 1449-1455, a % comment) i… |
| 1558-1613 | (E2a) Enclosed-charge principle + V_net + V_eff (orbit shape/penetration intro) | atom-as-radial-waveguide.md | verbatim-match | atom-as-radial-waveguide.md lines 11-38 match TeX 1561-1613 verbatim, including the identical l^2 (not l(l+1)) centrifugal form used at this point in TeX. |
| 1614-1793 | (E2a-ii/E2b) Orbit parameters (Kepler), sigma computation for l=0 vs circular, … | radial-eigenvalue-solver.md (top section) | verbatim-match | radial-eigenvalue-solver.md lines 10-113 match TeX 1639-1820 verbatim including all Li 2s numbers (u_a=1/8, f_in=0.020, sigma=1.961, Z_net=1.039, comparison table). |
| 1822-1994 | (E2b-iii) The Atom as a Radial Waveguide -- 5-step waveguide/impedance-step/ref… | radial-eigenvalue-solver.md (E2b-iii section) | verbatim-match | radial-eigenvalue-solver.md lines 115-179 match TeX 1822-1994 verbatim, EXCEPT the antenna-scale 'Validation' table cell: TeX says 'Chiral Antenna' (line 1965/2187), KB says 'HOPF-01' (line 177/272) -- see mismatch ch07… |
| 1996-2011 | (E2c) Re-apply Step 1 with Z_net | radial-eigenvalue-solver.md | verbatim-match | Lines 180-188 match TeX verbatim. |
| 2012-2208 | (E2d) Radial eigenvalue solver specification -- 5-step algorithm, eigenvalue br… | radial-eigenvalue-solver.md | verbatim-match | Lines 190-282 match TeX 2012-2207 verbatim including the Li 2s bracket numbers (E_hi=30.6, E_lo=3.4, target 5.39 eV). |
| 2209-2250 | (E2d-ii) ABCD transfer matrix cascade setup (Axiom mapping, radial wave equatio… | radial-eigenvalue-solver.md | verbatim-match | Lines 284-300 match TeX 2209-2251 verbatim, including the shift here (both sides) from l^2 to l(l+1) in the centrifugal term -- consistent between TeX and KB at this specific location even though it differs from the l^2… |
| (pre-slice, 480-554, read per assignment) | Radial TL Eigenvalue and the Screening Rule (de Broglie refractive index, scree… | de-broglie-n.md; screening-rule.md | verbatim-match | Both leaves are exact matches for this pre-slice TeX section; included because they were on my required-reading candidate list. Genuinely outside my assigned 1100-2250 range. |
| (post-slice, 2711, read per assignment) | E2 Summary -- Dual-Formalism Architecture (resultbox) | dual-formalism-architecture.md | verbatim-match | Leaf's resultbox title and content match the TeX resultbox at line 2711 (spot-checked title string only, full body not diffed since outside my slice); also required reading per candidate list. |

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

### ch07-D

| TeX range | heading | KB leaf | status | note |
|---|---|---|---|---|
| 3400-3497 | (untitled continuation) Crossing angle / crossing potential / crossing radius /… |  | tex-only | Torus-knot crossing-angle derivation and the 'Approach 24: Complete Phase Integral' resultbox (asserts 'No correction factors. One phase integral. One eigenvalue.') have no dedicated KB leaf among the assigned set; the … |
| 3498-3555 | p-shell orthogonal coupling / K=2G attribution + Hund's Rule Emergence lead-in | scale-separation.md | diverged | Print corrected 2026-08-02 (Rule-12, prior wording preserved in a % comment); KB leaf scale-separation.md:49 still carries the pre-correction 'confirmed independently ... Axiom 2' wording -- mismatch M1. |
| 3556-3706 | \section{Scale Separation: Knot Topology vs Orbital Geometry} (orbital scale, k… | scale-separation.md | verbatim-match | Full section is a byte-level verbatim translation aside from the M1 divergence already noted at the p-shell-coupling passage. |
| 3616-3638 | \subsection{Phase 5: Sub-Shell Junction Scattering (Op10)} incl. Beryllium-to-B… | subshell-junction-scattering.md | partial | Verbatim match except the leaf's bare '($K=2G$)' label (line 38) drops the print's 'form-derived, value GR-imported; not an axiom' caveat -- mismatch M3 (LOW). |
| 3639-3650 | \subsubsection{Half-Shell L=0 Continuous Spherical Integration} (Nitrogen/Phosp… |  | tex-only | No leaf anywhere in the ch07-quantum-mechanics KB directory (checked all 29 files by filename/grep) covers this derivation. Not itself debt (no contradiction found), but a coverage gap worth flagging to KB maintainers. |
| 3667-3706 | Table: Knot vs Orbital Geometry + Table: Operator Domain Assignment |  operator-domain-table.md | verbatim-match | Both tables translate cell-for-cell. |
| 3708-3775 | \subsection{Helium Coupling from First Principles} | helium-coupling-first-principles.md | verbatim-match |  |
| 3777-3843 | \subsection{The Chiral Factor: p_c as Topological Coupling} | chiral-factor.md | verbatim-match | TeX 'Macroscopic Chiral Antenna' / KB 'Antenna (Vol. IV HOPF-01)' is a naming variant only, not a mismatch. |
| 3845-3958 | \section{The Atom as a Stepped Impedance Resonator} (Op3 reflection, crossing s… | stepped-impedance-resonator.md | verbatim-match |  |
| 3960-4013 | \section{Hierarchical Cascade Correction} (nuclear precedent, derivation, Beryl… | hierarchical-cascade-correction.md | verbatim-match |  |
| 4015-4074 | \section{Ionization Energy Validation: Z=1 to 14} (table, discussion, Al/Si res… | ionization-energy-validation.md | partial | Table and discussion verbatim-match the leaf; the printed Li row (+2.46%, line 4027) conflicts with a different Li figure (-1.2%) printed earlier in the same TeX chapter at line 2943 (outside this slice) -- TeX-internal… |
| 4076-4103 | \section{The Unified Topological Boundary Limit: Scaling to Z=118} (c(n)=n(n-1)… |  | tex-only | No leaf anywhere in the ch07 directory. New derivation territory not yet captured in KB. |
| 4105-4128 | \section{Eradicating Classical Quantum Mechanical Approximations in Phase A} (l… |  | tex-only | No leaf anywhere in the ch07 directory. |
| 4130-4148 | \section{Period 4 Anomaly: Vacuum Yield Breakdown and the d-Block Emergence} (R… |  | tex-only | No leaf anywhere in the ch07 directory; introduces 'Regime IV Vacuum Yield' / 'Polar Conjugate Mirror' mechanisms with no KB backing found. |
| 4149-4151 | Chapter Summary / Exercises |  | tex-only | Standard end-of-chapter material, no leaf expected. |
| 4152-4290 | [% comment block] R40 batch-1 / batch-2a demotion notes (DIES-WITH-THE-PHANTOM … | a (administrative) | tex-only | Entirely a % LaTeX comment (git-visible, not printed) documenting Rule-12 demotion stamps at earlier chapter lines (41, 239, 383, 1051), which lie outside the 3400-4290 slice and are presumably covered by an earlier-sli… |

KB-only leaves (no print twin):
- `brillouin-zone-uv-cutoff.md` — Research-origin GR-QED Stage-2 driver confirmation (clm-1wmyx3); no TeX twin anywhere in ch07 3400-4290 slice (chapter has no Lamb-shift/Brillouin-zone content in-range). Already carries its own 2026…
- `q-g20a-lamb-shift-structural-closure.md` — Research-origin Lamb-shift structural-closure leaf (clm-3i66gp); no TeX twin in this slice. Carries its own dated 🔴 2026-07-02 Rule-12 banner (alpha-factor cutoff correction, body preserved below per…

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

### ch09

| TeX range | heading | KB leaf | status | note |
|---|---|---|---|---|
| 1-13 | \chapter{Computational Proof and Anomaly Catalog} + objectivebox | (none — objective box has no dedicated leaf) | tex-only | Standard chapter-opening objective box; not distilled to its own KB leaf, not debt. |
| 15-28 | \section{Computational Proof of Scale Invariance} | computational-graph.md (heading: Computational Proof of Sca… | verbatim-match | Near-verbatim translation; matches clm-z73h6n claims exactly. |
| 30-72 | \section{Verification Summary} | computational-graph.md (heading: Verification Summary) | diverged | Table matches row-for-row except the CLN025 protein-folding Agreement cell: TeX prints the corrected 'qualitative$^\dagger$' value with a full Rule-12 footnote (lines 55-65); KB leaf still prints the pre-correction 'sub… |
| 74-124 | \section{Anomaly Catalog: Proposed Tests} | anomaly-catalog.md | diverged | Tier 3 and Tier 4 items match verbatim; Tier 2 item 2 (Muon g-2) diverges — TeX carries the corrected +245(56)/+502e-11/4.6-sigma/2026-05-18-walkback framing, KB leaf still has the pre-walkback 2.49e-9 framing (M1). |
| 126-185 | \section{Numerical Precision and Dimensional Coordination} | precision-policy.md | verbatim-match | Floating-point, guard-constant table, dimensional traceability resultbox, and precision-budget table all match; the KB leaf's Dimensional Analysis Chain prose already reflects the corrected (post-2026-06-15) calibration… |
| 187-252 | \section{Avoidance of Methodological Contamination} | methodological-contamination.md | diverged | Rydberg-emergence, Topological Orbital Radii, and Electron Saturation Radius subsections match verbatim (claims clm-oltvwy, clm-ak97cb). The Multi-Electron Repulsion subsection's Axiom-4/K=2G bullet diverges: TeX carrie… |
| 254-260 | Chapter Summary | (none) | tex-only | Standard chapter summary bullets, not separately distilled; content is a recap of the four leaves above with no new claims. |
| 262-266 | Exercises | (none) | tex-only | Pedagogical exercises, not distilled — expected, not debt. |
| (no TeX correspondence in 09_computational_proof.tex) | n/a | {index.md,graph-architecture.md} | kb-only | App D's real printed twin is vol_0_engineering_compendium/chapters/03_computational_graph.tex (a different volume), per the leaf's own banner. Assigned to this slice for full reading but has no ch09.tex counterpart to s… |

KB-only leaves (no print twin):
- `graph-architecture.md` — No corresponding section/citation exists anywhere in manuscript/vol_2_subatomic/chapters/09_computational_proof.tex (grepped for app-d/computational-graph/Poisson/Chiral LC Over-Bracing: zero hits). …
- `index.md` — Index wrapper for the above; same kb-only status relative to ch09.tex.

### ch10

| TeX range | heading | KB leaf | status | note |
|---|---|---|---|---|
| 1-19 | \chapter{Three Open Problems from Lattice Topology} + objectivebox | index.md | partial | Objectivebox bullets match index.md's chapter overview in substance; index.md is a DERIVED file and its Key Results table still shows the pre-walkback baryon-asymmetry figure (see notes) — not counted as a primary misma… |
| 21-89 | \section{The Strong CP Problem} | strong-cp.md | verbatim-match | Body (problem statement, theorem, 5-step proof, PQ comparison table) is a verbatim translation. KB leaf carries an additional 2026-08-23 θ-fork dated scope-carve banner not mirrored in TeX; this disambiguates against a … |
| 92-238 | \section{The Baryon Asymmetry} | baryon-asymmetry.md (+ g-star-derivation.md for the g_* sub… | verbatim-match | SUPERSEDED-HEADLINE warningbox (10:98-131) is byte-identical in substance to baryon-asymmetry.md:10-18. The 2026-06-20 Rule-12 walk-back (0.38%->0.79%/Consistency-check) is fully and correctly propagated to both TeX and… |
| 240-314 | \section{The Hubble Tension} | hubble-tension.md | verbatim-match | Examplebox including the 2026-06-15 KB-reconciliation A.2/A.3 corrections and the Class-E consistency-vs-emergence v1.1 refinement are printed in full in TeX (10:260-264), matching hubble-tension.md:31-39 almost word fo… |
| 316-356 | \section{Testable Prediction: $g_* = 85.75$} | g-star-prediction.md | diverged | TeX prints the g_*=85.75 falsifiable-prediction framing with no caveat; the KB leaf carries a 2026-08-18 Wave-2 D15b provenance rider (form-derived/value-imported, not zero-parameter) that is entirely absent from TeX. S… |
| 359-404 | \section{The Scale Invariance Principle} | scale-invariance-table.md + unification.md | verbatim-match | Table and the '26 of 26 parameters ... computed from 3 retained calibration inputs + 4 axioms' augmented wording (2026-06-15 recon A.4) are printed identically in TeX 10:373-404 and in both KB leaves. |
| 406-429 | \section{Quantitative Resolutions} | quantitative-resolutions.md | diverged | Strong-CP, Standard-Model, Hubble, and g_* rows match. The Baryon-asymmetry row diverges: TeX already shows the corrected '0.79% (OOM)/Consistency-check' (10:419) but quantitative-resolutions.md:15 still shows the pre-w… |
| 431-445 | Chapter Summary + Exercises | (none dedicated) | tex-only | No dedicated KB leaf mirrors the Summary/Exercises headings; their content (walk-back bullets, Class-E framing) is substantively identical to what's already covered by baryon-asymmetry.md and hubble-tension.md. TeX-only… |

### ch11

| TeX range | heading | KB leaf | status | note |
|---|---|---|---|---|
| 16-31 (\section{The Universal Energy Functional}, eq:universal_energy resultbox) | The Universal Energy Functional | universal-energy.md | verbatim-match | Resultbox, gradient-descent update rule, and convergence sentence translate word-for-word into the leaf. |
| 33-67 (\section{Overdriving Lattice QCD}, subsections Nuclear Coupling Constant + Uranium-235 Assembly) | Overdriving Lattice QCD: Heavy Nuclear Assembly | overdrive-nuclear.md | partial | Examplebox derivation and U-235 assembly bullets are verbatim; but see mismatch ch11-M1 (line 66 'at comparable accuracy' vs clm-dboxok non-claim, not caveated in either tex or this leaf). |
| 69-95 (\section{Overdriving AlphaFold}, subsections Biological Coupling Constant + Polyalanine Folding Demonstration) | Overdriving AlphaFold: First-Principles Protein Folding | overdrive-protein.md | partial | Prose translates verbatim (including the commented-out missing-figure float, correctly omitted from the leaf as a Rule-12-honest asset gap, not physics). See mismatch ch11-M2 re: scale-invariance framing vs program-arc-… |
| 97-119 (\section{Computational Scaling Comparison}, Table 1) | Computational Scaling Comparison | overdrive-comparison.md | verbatim-match | Table rows and the 'Parameters column' explanatory paragraph translate verbatim. |
| 121-127 (\section*{Chapter Summary}) | Chapter Summary | index.md (Key Results table only) | tex-only | No dedicated leaf hosts the Chapter Summary bullets or the line-125 %-comment Rule-12 banner; index.md's Key Results table is a derived summary, not a leaf translation of this section. Not treated as debt (already-discl… |
| 129-133 (\section*{Exercises}) | Exercises | (none) | tex-only | Exercise prompts have no KB twin anywhere in ch11-overdrive; expected — KB leaves host results/claims, not exercise text. |

KB-only leaves (no print twin):
- `axiom-survey.md` — Explicit GAP placeholder: documents that ch11 tex source contains no axiombox environments (chapter uses objectivebox/examplebox/resultbox only). Not a mismatch — it is an honest routing note that no…

### ch12-mp

| TeX range | heading | KB leaf | status | note |
|---|---|---|---|---|
| 1-22 | chapter preamble: objectivebox + Scope caveat (engineering-physics vs Clay-rigo… | index.md | verbatim-match | index.md restates the framework-conditional/not-Clay-rigorous framing faithfully; claim-quality.md (clm-c8q0z5/q5izb7/knveh6) treats this chapter-opening caveat as the print-side disclosure for every per-problem KB scop… |
| 25-88 (sec:ns_millennium) | The Navier-Stokes Smoothness Problem | navier-stokes-prize.md | verbatim-match | Discrete Laplacian, velocity/enstrophy bounds, Picard-Lindelof steps match TeX line-for-line. KB carries its own 2026-05-17 scope-correction banner (two Clay deviations); covered by the chapter caveat per clm-c8q0z5's o… |
| 91-152 (sec:ym_millennium, Steps 1-2) | Yang-Mills Mass Gap: Steps 1-2 (Lattice Hamiltonian, Mass Gap) | yang-mills-steps1-2.md | partial | MM-1: leaf omits the TeX:112 2026-07-09 scope-note correction (UV cutoff understated ~2.7x vs the true srs 3D band edge, clm-bnd5rq) even though the leaf otherwise reproduces the surrounding sentences verbatim. See mism… |
| 154-213 (Steps 3-5) | Yang-Mills: Gauge Group Emergence, Confinement, Infinite-Volume Limit | yang-mills-steps3-5.md | verbatim-match | N=(q+1)/2 resultbox, gauge-group/mass-scale table, Γ→-1 confinement, and infinite-volume argument all byte-match TeX. Leaf's 'SU(N) is an ansatz, not derived' banner is treated as disclosed via the chapter caveat per cl… |
| 215-325 (sec:rh_millennium) | The Riemann Hypothesis | riemann-hypothesis.md | verbatim-match | Spectral zeta, Euler product, regime-boundary table, functional equation, and critical-line argument all match. |
| 327-391 (sec:hc_millennium) | The Hodge Conjecture | hodge-conjecture.md | verbatim-match | Standing-wave/phase-matching/irrational-decay/rational-coefficients argument matches. |
| 393-467 (sec:bsd_millennium) | The Birch and Swinnerton-Dyer Conjecture | birch-swinnerton-dyer.md | partial | Leaf omits TeX's explicit K_MUTUAL=(cπ/2)αℏc/(1-α/3) closed form (line 423) — ordinary condensation, not a dated correction, so not reported as a mismatch. |
| 470-530 (sec:pnp_millennium) | The P versus NP Problem | p-vs-np.md | verbatim-match | Lattice-nodes/parallel-evaluation/relaxation/'rendered moot' argument matches; TeX itself (478, 529-530) already carries the non-resolution disclaimer inline. |
| 533-591 (sec:poincare_millennium) | The Poincare Conjecture (Solved) | poincare-conjecture.md | verbatim-match | Ricci-flow-as-impedance-relaxation / S^3-ground-state argument matches; both TeX and leaf explicitly disclaim any AVE claim to the Clay prize (Perelman's proof is canonical). Fence note: this section's Poincare/S^3 cont… |
| 594-696 | Synthesis: What the Seven Problems Reveal (3 structural properties + Formalizat… | (none dedicated — rolled into index.md Key Results table) | tex-only | Synthesis/formalization-gap tables (NS/YM/Riemann only) are TeX-only summary content; no separate KB leaf expected or needed for a synthesis section. |
| 698-711 | Chapter Summary + Exercises | (none) | tex-only | Standard pedagogical material, not leafed. |
| n/a — no TeX reference at all in ch12 | n/a | knot-vs-orbital-table-ch12.md | kb-only | Self-disclosed routing/GAP stub; see kbOnlyLeaves. |

KB-only leaves (no print twin):
- `knot-vs-orbital-table-ch12.md` — kind: leaf, no-claim: placeholder/routing. Self-disclosed GAP: the leaf says tab:knot_vs_orbital referenced in the ch12 taxonomy skeleton is actually located in Ch.7 (07_quantum_mechanics_and_orbital…

### ch12-fp

| TeX range | heading | KB leaf | status | note |
|---|---|---|---|---|
| 1-45 (preamble + objectivebox) | Appendix 12A preamble / objectivebox | (none — routing text only) | tex-only | Frames the appendix as occupying 'the boundary' between AVE's constructive proofs and Clay-rigorous formal math; explicitly disclaims Clay submission (TeX:6-9). No KB leaf twin; this is original appendix-level scoping p… |
| 43-207 | Osterwalder-Schrader Verification for Yang--Mills (OS1-OS5 + Reconstruction App… | yang-mills-steps1-2.md, yang-mills-steps3-5.md | tex-only | No verbatim/near-verbatim KB twin — this is new functional-analytic machinery (Schwinger functions, transfer-matrix positivity, OS axioms) layered on top of the two Ch.12 leaves' lattice-Hamiltonian/mass-gap/confinement… |
| 209-290 | Sobolev H^1 Bound for Navier-Stokes | navier-stokes-prize.md | tex-only | The H^1-bound proof (steps 1-3, TeX:243-262) is a rigorous restatement of the leaf's discrete-Laplacian-bound argument at higher formal polish, but the leaf itself has no H^1-Sobolev-norm framing — this is new content. … |
| 292-382 | Riemann Hypothesis: Spectral Boundary and Functional Equation | riemann-hypothesis.md | tex-only | New content: derives the completed-zeta functional equation from an ABCD two-port reciprocity argument (TeX:299-330) not present in the leaf (whose functional-equation step, :88-96, cites Axiom-2 reciprocity directly wi… |
| 384-435 | Formalization Gap Summary (Table tab:clay_gap_summary) | Poincare rows within this slice | tex-only | Consolidated summary table with no direct KB leaf twin (a table format doesn't exist in any assigned leaf). Cross-checked the YM/NS/Riemann rows against clm-q5izb7/clm-c8q0z5/clm-knveh6's 'framework-conditional, not Cla… |
| 437-453 | Verification (script pointer + correlation-length cross-ref) | (none) | tex-only | Points to src/scripts/vol_2_subatomic/simulate_millennium_proofs.py and to Appendix~derived_topological_numerology for the OS5 correlation length xi. This appendix (derived_topological_numerology) is outside this slice'… |

KB-only leaves (no print twin):
- `index.md` — Assigned for context (clm-e1pdfd) but has no counterpart in this slice's TeX file (12_appendix_formal_proofs.tex covers Appendix 12A: Formal Mathematical Proof Objects — OS verification / Sobolev / R…

### appx-front — **NO READ (slice did not return)**

---

## §2 — Mismatches (reader-reported; verifier verdict column)

Kinds: WB-LAG (KB walked back, print still asserts) · CONTRA · STALE-KB (print corrected, leaf lags) · DEAD-ANCHOR · KB-INTERNAL · TEX-ONLY. Verdict: CONFIRMED / DOWNGRADED / REFUTED / UNVERIFIED (verifier not yet returned).

| # | slice | sev | kind | print site | KB site | verdict | disclosed | known in | proposed action |
|---|---|---|---|---|---|---|---|---|---|
| 1 | ch01-A | HIGH | WB-LAG | `01_topological_matter.tex:35` | `newtonian-inertia-as-lenz.md:14` | **CONFIRMED** | no |  | Print-side propagation of the 2026-06-20 Grant-ratified mass-sector re-scope: the stored inductive energy is the T2/Cosserat FLYWHEEL (frequency regulation); the rest-mass STORE is the orthogonal A1 … |
| 2 | ch01-A | MEDIUM | WB-LAG | `01_topological_matter.tex:8` | `newtonian-inertia-as-lenz.md:14` | **CONFIRMED** | no |  | Same 2026-06-20 re-scope, chapter-objective echo site. Fix in lockstep with M1 (the objective promises mass-from-inductance as the chapter's learning outcome). |
| 3 | ch01-A | HIGH | WB-LAG | `01_topological_matter.tex:207` | `index.md:13` | **DOWNGRADED** | no |  | Print asserts the superseded closed-loop neutrino topology in the ch01 regime table with no local marker. The 2026-05-06 corrigendum IS printed — but at 03:13, two chapters away, and it does not name… |
| 4 | ch01-A | MEDIUM | KB-INTERNAL | `01_topological_matter.tex:207` | `regime-classification.md:15` | **DOWNGRADED** | no |  | Adjudicated per slice-instruction (a): regime-classification.md is a LEAF (kind: leaf, clm-ou2jym) and it carries the superseded closed-loop neutrino framing UNBANNERED, while the ch03 corrigendum (2… |
| 5 | ch01-A | MEDIUM | STALE-KB | `01_topological_matter.tex:209` | `regime-classification.md:17` | **DOWNGRADED** | no |  | Leaf lags print: print carries the real-space/phase-space correction (INVARIANT-N1: proton body = $6^3_2$ Borromean; $(2,5)$ is the phase-space portrait) that the leaf's 'Cinquefoil' Topology cell st… |
| 6 | ch01-A | MEDIUM | WB-LAG | `01_topological_matter.tex:242` | `chirality-and-antimatter.md:10` | **CONFIRMED** | no | 2026-09-06 scan S4a candidate site 01:242 | The leaf's own opening sentence was RELABELLED by the Grant 2026-07-09 R1 adjudication (canonical charge-sign = Beltrami helicity → $e^-$ = LH); the printed twin is the un-relabelled prior wording. N… |
| 7 | ch01-A | MEDIUM | CONTRA | `01_topological_matter.tex:248` | `chirality-and-antimatter.md:18` | **CONFIRMED** | no |  | Same sentence, one word apart: print calls the electron a 'Hopfion' (non-trivial real-space Hopf charge) where the leaf says '$0_1$ unknot'. The leaf twin was corrected; print was not. mathematical-t… |
| 8 | ch01-A | HIGH | WB-LAG | `01_topological_matter.tex:259` | `electron-identification.md:64` | **CONFIRMED** | no |  | Print figure caption sells the free-precursor formation route as established ('establishing the physical derivation of confined point-particles'), which the KB grades closed-negative / leans-falsifie… |
| 9 | ch01-A | LOW | DEAD-ANCHOR | `01_topological_matter.tex:79` | `electron-identification.md:92` | **CONFIRMED** | no |  | KB-side dead anchor: translation-circuit.md:637 no longer carries the quoted content (line 637 at HEAD reads 'The substrate's **cold-lattice ideal state** is the limit:'). Verified true location at H… |
| 10 | ch01-A | LOW | DEAD-ANCHOR | `01_topological_matter.tex:55` | `translation-circuit.md:839` | **CONFIRMED** | no |  | The 2026-08-02 comment block's own cite-repair (':637 → :767') has itself gone stale; the line is :839 at HEAD. Non-printed (% comment), so zero PDF impact — but it is the third recorded drift of thi… |
| 11 | ch01-A | MEDIUM | WB-LAG (leaf scope-note undated) | `01_topological_matter.tex:239` | `torus-knot-ladder.md:21` | **CONFIRMED** | no | 2026-09-06 scan S4a listed 01:218 and 01:237 in t… | Print carries the ladder's other three fences (dimensionless $r_{opt}$, $S=0$ $N/\Delta$ scope flag, cold-vs-thermal convention) but not the leaf's imported-assignment note; combined with 'zero empir… |
| 12 | ch01-A | LOW | UNIT-LABEL LAG (disclosed in print) | `01_topological_matter.tex:227` | `torus-knot-ladder.md:10` | **DOWNGRADED** | yes | 2026-09-06 scan S4a candidates 01:218 / 01:237 | Leaf stripped the $\ell_{node}$ units from every cell and calls them 'spurious'; print keeps them in all six cells and neutralises them with an inline clause (01:218) plus a dagger footnote (01:237) … |
| 13 | ch01-A | LOW | WB-LAG | `01_topological_matter.tex:40` | `electron-unknot.md:13` | **CONFIRMED** | no |  | The leaf pins a dated 2026-06-24 reading-scope on this exact clause; print has none. Graded LOW because print's own wording already attributes the trapping to the closed topological loop (the SURVIVI… |
| 14 | ch01-A | MEDIUM | WB-LAG (undated leaf demotion) | `01_topological_matter.tex:244` | `chirality-and-antimatter.md:28` | **DOWNGRADED** | no |  | The leaf and clm-hb2xmj both grade the annihilation section asserted-mechanism / peer-not-chord at solidity 0.30 ('do not build on'); print states the resolution flatly and prints the 1.022 MeV resul… |
| 15 | ch01-A | LOW | KB-INTERNAL (acknowledged OPEN fork — flag, do not adjudica… | `01_topological_matter.tex:147` | `electron-unknot.md:59` | **UNVERIFIED** | yes | ch01 index.md:44 names it: 'the **tube-geometry f… | electron-unknot.md:13 (tube radius $l_{node}/(2\pi)$) vs :59 (tube diameter $\equiv 1\,l_{node}$) differ by $\approx10\times$; PRINT carries BOTH sides verbatim at 01:40 and 01:147 with no flag. The … |
| 16 | ch01-A | LOW | WB-LAG (undated leaf scope note) | `01_topological_matter.tex:16` | `mathematical-topology-of-mass.md:20` | **DOWNGRADED** | no |  | Leaf tags the functional peer-with-standard / adopted ansatz (matching clm-oygz1i's non-claim: 'a **chosen ansatz** ... The leaf does not derive the Skyrme term independently from Axioms 1-4'); print… |
| 17 | ch01-B | MEDIUM | WB-LAG | `01_topological_matter.tex:110` | `electron-unknot-cosserat-seeder.md:113` | **UNVERIFIED (id shared by 7 slices; verdicts not attributable)** | no |  | Print (01:107-111) cites the v14 breathing-soliton engine receipt flatly as the current Engine implementation witness for M, Q, J. The KB leaf demoted exactly that receipt on 2026-08-11 (R40 batch-2a… |
| 18 | ch01-B | MEDIUM | CONTRA | `01_topological_matter.tex:120` | `electron-bound-resonator-coverage.md:186` | **UNVERIFIED (id shared by 7 slices; verdicts not attributable)** | no |  | Print says the examplebox algebra is 'proving' the reduced Compton wavelength IS the unknot circumference; the same identity is graded definitional/circular by the KB (leaf gate D.1 at :186, OPEN, cl… |
| 19 | ch01-B | LOW | DEAD-ANCHOR | `01_topological_matter.tex:55` | `translation-circuit.md:839` | **UNVERIFIED (id shared by 6 slices; verdicts not attributable)** | no |  | The 2026-08-02 de-claim comment repaired the anchor :637 -> :767; at HEAD the quoted string lives at translation-circuit.md:839 (lines 765-769 carry the delta_strain thermal chain, unrelated). Repair… |
| 20 | ch01-B | LOW | DEAD-ANCHOR | `01_topological_matter.tex:56` | `substrate-perspective-electron.md:11` | **UNVERIFIED (id shared by 5 slices; verdicts not attributable)** | no | TeX 01:55-56 % comment (2026-08-02 de-claim note)… | The 2026-06-21 Rule-12 g=2 banner at substrate-perspective-electron.md:11 cites translation-circuit.md:637; the quoted content is at :839 at HEAD. Repair 637 -> 839. Pure line-number repair; banner t… |
| 21 | ch01-B | LOW | DEAD-ANCHOR | `01_topological_matter.tex:56` | `substrate-perspective-electron.md:227` | **UNVERIFIED (id shared by 4 slices; verdicts not attributable)** | no | same 2026-08-02 TeX comment as M4 | Second :637 cite in the same leaf (§3 Magnetic moment generation, inline Rule-12 note). Repair 637 -> 839. Pure line-number repair. |
| 22 | ch01-B | LOW | DEAD-ANCHOR | `01_topological_matter.tex:56` | `electron-bound-resonator-coverage.md:56` | **UNVERIFIED (id shared by 4 slices; verdicts not attributable)** | no | same 2026-08-02 TeX comment as M4 | Third :637 cite in the slice (the g=2 coverage row's Rule-12 re-scope). Repair 637 -> 839. Pure line-number repair. |
| 23 | ch01-B | MEDIUM | KB-INTERNAL | `01_topological_matter.tex:167` | `l3-electron-soliton-synthesis.md:108` | **UNVERIFIED (id shared by 4 slices; verdicts not attributable)** | no |  | Two vol2/ch01 leaves disagree, unbannered on the l3 side. l3:108 states 'The macro two-threshold dialectic collapses to a SINGLE threshold at engine subatomic scale' (v_yield = V_SNAP), and l3:106 st… |
| 24 | ch01-B | LOW | CONTRA | `01_topological_matter.tex:230` | `l3-electron-soliton-synthesis.md:37` | **UNVERIFIED (id shared by 3 slices; verdicts not attributable)** | no |  | The l3 family table grades every q>=9 member 'unstable' with no named particle; print tabulates named assignments at q=9/11/13 (Delta(1600), Delta(1900), N(2190), 01:230-232, dated-aligned 2026-06-19… |
| 25 | ch01-B | LOW | CONTRA | `01_topological_matter.tex:242` | `pair-production-axiom-derivation.md:27` | **UNVERIFIED** | yes |  | Print calls e- a RIGHT-handed unknot; the leaf's canonical charge-sign is e- = LH Beltrami. This is DISCLOSED, not debt: pair-production-axiom-derivation.md:138 records the dated reconciliation — 'it… |
| 26 | ch01-B | MEDIUM | KB-INTERNAL | `(no TeX twin — KB-internal, both leaves are kb-only):0` | `electron-unknot-cosserat-seeder.md:120` | **UNVERIFIED** | no |  | The seeder leaf offers, unbannered, a route by which the engine would reach the canonical alpha^-1 Q-factor ('require amplitude tuning to reach canonical Q-factor ... a self-consistent ground-state s… |
| 27 | ch01-C | HIGH | WB-LAG | `01_topological_matter.tex:35` | `newtonian-inertia-as-lenz.md:14` | **CONFIRMED** | no |  | Print-side propagation of the 2026-06-20 Grant-ratified mass-sector ruling into Vol 2 Ch 1 §'Newtonian Inertia as Macroscopic Lenz's Law': a dated printed note stating the stored inductive energy is … |
| 28 | ch01-C | MEDIUM | WB-LAG | `01_topological_matter.tex:33` | `newtonian-inertia-as-lenz.md:14` | **CONFIRMED** | no |  | Same print note as M1 covers this line — the banner quotes this very mapping by name. No separate edit needed if M1's note is placed at the section head rather than after :35. |
| 29 | ch01-C | MEDIUM | WB-LAG | `01_topological_matter.tex:266` | `newtonian-inertia-as-lenz.md:14` | **CONFIRMED** | no |  | Chapter-summary bullet re-asserts the superseded store-identification after the section it summarises; needs the same A1-store / T2-flywheel split once M1 is ruled. Bundle with M1. |
| 30 | ch01-C | MEDIUM | WB-LAG | `01_topological_matter.tex:8` | `newtonian-inertia-as-lenz.md:14` | **CONFIRMED** | no |  | Objective-box bullet states the superseded store-identification as a chapter learning objective. Re-word to the flywheel / A1-depression split once M1 is ruled. Bundle with M1. |
| 31 | ch01-C | MEDIUM | WB-LAG | `01_topological_matter.tex:148` | `common-mode-twist-ledger.md:235` | **DOWNGRADED** | no |  | Print carries BOTH halves of a fork the KB has dated and routed: 01:40 prints the electron-unknot.md:13 geometry ('The unknot has circumference $\ell_{node}$ and tube radius $\ell_{node}/(2\pi)$') an… |
| 32 | ch01-C | MEDIUM | WB-LAG | `01_topological_matter.tex:40` | `spin-gyroscopic-isomorphism.md:45` | **DOWNGRADED** | no |  | The leaf carves 'macroscopic' explicitly as a term of art (leaf :15 — classical / deterministic-extended, a ~ℓ_node-scale circulation loop, NOT human-scale) and states the core is subatomic, not macr… |
| 33 | ch02 | MEDIUM | WB-LAG | `02_baryon_sector.tex:319` | `topological-fractionalization.md:60` | **UNVERIFIED** | no |  | Leaf carries a dated 2026-08-23 surface note (Grant rulings (a)+(b), docket 2026-08-23-theta-fork-ruling; :50-76) that (1) the theta here is the J-dressing, not a vacuum angle -- 'trapped vacuum' at … |
| 34 | ch02 | MEDIUM | CONTRA | `02_baryon_sector.tex:131` | `torus-knot-ladder-baryons.md:29` | **UNVERIFIED** | no |  | The printed 'maximum error ~2.4%' is the pre-2026-07-02 column maximum (old c=15 row). After the ADJUDICATED PDG-2024 anchor driver (print :309, Grant 2026-07-02) the print's own table :296 shows +4.… |
| 35 | ch02 | MEDIUM | CONTRA | `02_baryon_sector.tex:297` | `torus-knot-ladder-baryons.md:30` | **UNVERIFIED** | no |  | Print :309 states the 2026-07-02 canonical-driver update was applied to c=9,11,13 only; the c=15 row was left at the older PDG value (2420, +2.40%) while the leaf's driver-run row reads 2400 ± 100, +… |
| 36 | ch02 | MEDIUM | CONTRA | `02_baryon_sector.tex:314` | `torus-knot-ladder-baryons.md:30` | **UNVERIFIED** | no |  | Figure caption :314 prints a third, unsourced c=15 deviation (+9.8%) that matches neither the print table (:297, +2.40%) nor the leaf (:30, +3.249%), and still reads 'with zero adjusted parameters re… |
| 37 | ch02 | LOW | STALE-KB | `02_baryon_sector.tex:131` | `thermal-softening.md:37` | **UNVERIFIED** | yes | thermal-softening.md:40 FLAGGED-NOT-FIXED (2026-0… | Leaf lags the 2026-06-19 print verb walk-back ('validates' -> 'covers' + rider 'Read covers as consistency, not ensemble-validation'); the KB banner at :40 already discloses it and routes to the next… |
| 38 | ch02 | MEDIUM | STALE-KB | `02_baryon_sector.tex:357` | `proton-neutron-mass-split.md:10` | **UNVERIFIED** | no | partial: scan S4a/S5 02:357,02:362 (anchor side o… | Print was corrected 2026-06-15 (consistent-with-not-derived, per neutron-identification.md:52/:54) but the verbatim-twin leaf still asserts 'accounts for' with no banner -- KB-internal vs neutron-ide… |
| 39 | ch02 | LOW | DEAD-ANCHOR | `02_baryon_sector.tex:357` | `neutron-identification.md:52` | **UNVERIFIED** | no | scan S5 anchors 02:357/362 -> neutron-identificat… | Both printed cites (:357 and caption :362) point at :52, which at HEAD is the §2.1 heading; the cited content ('consistent with — but does not derive — the empirical' / 'Derivation TBD: compute the F… |
| 40 | ch02 | LOW | DEAD-ANCHOR | `02_baryon_sector.tex:362` | `neutron-identification.md:25` | **UNVERIFIED** | no |  | Leaf :25 quotes 'per Vol 2 Ch 2 figure caption (02_baryon_sector.tex:299)' with the pre-2026-06-15 wording; at HEAD the caption is :362 and reads 'is the proposed structural origin'. Same leaf cites … |
| 41 | ch02 | LOW | DEAD-ANCHOR | `02_baryon_sector.tex:448` | `proton-neutron-mass-split.md:82` | **UNVERIFIED** | no |  | claim-quality.md:754 at HEAD sits inside the positron-annihilation entry; the Hierarchy-Bridge 'algebraic substitution, not an independent derivation of $G$' caveat is clm-bh9p6s at :789. Leaf :82 (p… |
| 42 | ch02 | LOW | KB-INTERNAL | `02_baryon_sector.tex:165` | `proton-identification.md:68` | **UNVERIFIED** | no |  | Dead pointer: topological-fractionalization.md carries only the Witten section; the I_scalar ~1162 statement lives at thermal-softening.md:66 (twin of print :165) and self-consistent-mass-oscillator.… |
| 43 | ch02 | MEDIUM | WB-LAG | `02_baryon_sector.tex:463` | `proton-identification.md:73` | **UNVERIFIED** | no |  | KB D1 headline-fork ruling (2026-07-13, Grant option 2; leaf :73, mirrored in clm-cmic3e) enforces: headline = +0.74% bare topology; the -0.002% is delta_th-riding precision, NOT the headline; do NOT… |
| 44 | ch02 | LOW | CONTRA | `00_title.tex:18` | `proton-identification.md:13` | **UNVERIFIED** | no |  | Three different headline numbers in print for one object: 00_title.tex:18 '~1836.14' (matches neither), ch02 :7/:52/:60/:463 '1836.15' (CODATA), ch02 :264 '1836.12' (derived; leaf :13/:60, self-consi… |
| 45 | ch02 | MEDIUM | CONTRA | `02_baryon_sector.tex:41` | `proton-identification.md:156` | **UNVERIFIED** | no | proton-identification.md:145-157 FLAG 2026-07-19 … | Print-internal tension the KB has flagged but print has not: :41 (Route B, quoted verbatim at leaf :152) has the proton 'span multiple fundamental nodes' with 0.84 fm as an RMS-scattering artifact; :… |
| 46 | ch02 | LOW | CONTRA | `02_baryon_sector.tex:466` | `claim-quality.md:789` | **UNVERIFIED** | yes | 02:465 2026-06-15 KB-reconciliation (vol_2 brief … | Residual strength word only: the printed bullet continues 'by algebraic substitution (given the value-fitted $G$ input)', so the 2026-06-15 correction is printed inline; the leaf twin (proton-neutron… |
| 47 | ch02 | LOW | DEAD-ANCHOR | `02_baryon_sector.tex:126` | `thermal-softening.md:25` | **UNVERIFIED** | no | scan S4a 02:120/02:126 (leaf newer; 'added: REFUT… | Off-by-one KB anchors: at HEAD the thesaurus heading '### Hill — three distinct objects' is :224 and the VRH-average row ('Not a theorem and not a bound') is :228; the hazard note is :232. Print :120… |
| 48 | ch02 | LOW | KB-INTERNAL | `02_baryon_sector.tex:238` | `self-consistent-mass-oscillator.md:30` | **UNVERIFIED** | no |  | Print :238 and its verbatim leaf twin :30 both say the packing limit p_c ~0.1834 is 'derived in Chapter 2' -- this IS Vol 2 Ch 2, which does not derive p_c; proton-identification.md:70 attributes it … |
| 49 | ch03 | MEDIUM | WB-LAG | `03_neutrino_sector.tex:227` | `delta-cp-violation.md:22` | **UNVERIFIED (id shared by 7 slices; verdicts not attributable)** | no |  | Reword TeX 03:227 item 1 to match the leaf's corrected physical description ('half-period of the propagating Cosserat coil', not '0_1 unknot phase winding'), consistent with the chapter's own 2026-05… |
| 50 | ch03 | HIGH | WB-LAG | `03_neutrino_sector.tex:272` | `index.md:13` | **UNVERIFIED (id shared by 7 slices; verdicts not attributable)** | no |  | Rewrite Chapter Summary bullet 1 to state the canonical screw-dislocation / open-helix framing (as the objectivebox at line 7 and the corrigendum at line 13 of the SAME chapter already do), dropping … |
| 51 | ch03 | LOW | WB-LAG | `03_neutrino_sector.tex:274` | `index.md:13` | **UNVERIFIED (id shared by 6 slices; verdicts not attributable)** | no |  | Same block as M2 (Chapter Summary bullet 3); drop '$0_1$' label for the mass eigenstates when M2 is fixed. |
| 52 | ch03 | HIGH | WB-LAG | `03_neutrino_sector.tex:159` | `chiral-screening.md:35` | **UNVERIFIED (id shared by 5 slices; verdicts not attributable)** | no |  | Add a print-visible caveat at TeX 03:149-159 (resultbox + note) reflecting the 2026-08-24 carve: leg 1 (transfer-capacity chain) is derived-modulo-premise, but leg 2 (connectivity=trefoil crossing nu… |
| 53 | ch03 | MEDIUM | WB-LAG | `03_neutrino_sector.tex:250` | `delta-cp-violation.md:38` | **UNVERIFIED (id shared by 4 slices; verdicts not attributable)** | no |  | Qualify TeX 03:250's 'derive from three inputs / no curve fitting' framing per the leaf's 2026-05-17 Foundation-Item-13 scope correction: c_1=5 (hence c_1*c_3=45, hence sin^2(theta13)) is chosen-not-… |
| 54 | ch03 | MEDIUM | WB-LAG | `01_topological_matter.tex:207` | `index.md:13` | **UNVERIFIED (id shared by 4 slices; verdicts not attributable)** | no |  | Update the ch01 regime-classification table's Neutrino row Topology column from 'Twisted unknot' to the canonical 'Open helix (screw dislocation)' per the ch03 corrigendum, which explicitly anticipat… |
| 55 | ch03 | HIGH | WB-LAG | `00_title.tex:14` | `index.md:13` | **UNVERIFIED (id shared by 4 slices; verdicts not attributable)** | no |  | Update the Volume II front-matter abstract (most reader-visible text in the volume) from 'neutrinos as dispersive twisted 0_1 unknots, bound by the Faddeev-Skyrme energy functional' to reflect the ca… |
| 56 | ch03 | LOW | STALE-KB | `03_neutrino_sector.tex:122` | `claim-quality.md:251` | **UNVERIFIED (id shared by 3 slices; verdicts not attributable)** | yes |  | Trivial label-only sync: update claim-quality.md:251's flavor-splitting bullet from Delta(1620) to Delta(1600) to match the already-disclosed, dated (2026-06-19) TeX correction. Not a leaf (claim-qua… |
| 57 | ch04 | LOW | DEAD-ANCHOR (comment-only; not printed) | `04_quantum_spin.tex:81` | `claim-quality.md (clm-salw2h):408` | **CONFIRMED** | no | 2026-09-06 scan S4a 04:111 (file-level 'leaf newe… | Comment-only line-number repair in the % block at TeX:81-88: :407->:408, :408->:409, :409->:410, :410->:411, ':419' (TeX:88 'Claim solidity 0.70 at :419.') -> :420. Verified via git show: the clm-sal… |
| 58 | ch04 | LOW | DEAD-ANCHOR (KB-side line cite drift) | `04_quantum_spin.tex:111` | `larmor-derivation.md:61` | **CONFIRMED** | no |  | Leaf-side line-number repair: ':407–410' -> ':408–411' and ':419' -> ':420' at larmor-derivation.md:61; the per-item cites '(:407)' at :63, '(:408)' at :64, ':410' at :65 and '(:409)' at :67 each shi… |
| 59 | ch04 | LOW | DEAD-ANCHOR (KB-side line cite drift) | `04_quantum_spin.tex:111` | `visual-equivalence.md:22` | **CONFIRMED** | no |  | Leaf-side line-number repair at visual-equivalence.md:22: ':407–410' -> ':408–411', ':419' -> ':420', and the inline '(:407)', '(:408)', '(:410)', '(:409)' each +1. Same cause as M1/M2. |
| 60 | ch04 | MEDIUM | CONTRA (topology: printed figure caption still names the el… | `04_quantum_spin.tex:62` | `larmor-derivation.md:10` | **CONFIRMED** | no |  | Route for ruling/fix: the 2026-08-02 softening (commit e947ce4a) touched :53/:68 only and left the fig:spin_precession caption on the pre-migration trefoil identity. Print is internally inconsistent … |
| 61 | ch04 | LOW | STALE-TEX-COMMENT (comment-only; TeX % FLAG-DON'T-FIX block… | `04_quantum_spin.tex:94` | `larmor-derivation.md:57` | **DOWNGRADED** | yes | MR board 2026-08-02 'vol2 -- 13 findings' item 04… | Comment-only append at TeX:89-97 noting the OWED KB-leaf edit LANDED (larmor-derivation.md:55-67 and visual-equivalence.md:14-24 both carry the 2026-08-02 KB-lockstep banner and the ~~struck~~ prior … |
| 62 | ch04 | LOW | KB-INTERNAL (derived index vs its own bannered leaves: inde… | `04_quantum_spin.tex:6` | `index.md:11` | **CONFIRMED** | no |  | Index is DERIVED (kind: index) and not the sync source of truth -- flag only. On the next index regeneration, mirror the leaf banner (e.g. 'defined structurally as ... on the disclosed spin-½ selecti… |
| 63 | ch05 | MEDIUM | WB-LAG | `05_electroweak_gauge_theory.tex:175` | `gauge-boson-masses.md:34` | **UNVERIFIED** | no |  | Chapter Summary bullet restates the pre-R43 claim flatly ('explicitly derived'); the printed rescope at :35/:51 (time-independent family only; 'canon holds no valid derivation of any full U(1) family… |
| 64 | ch05 | LOW | WB-LAG | `05_electroweak_gauge_theory.tex:8` | `gauge-boson-masses.md:83` | **UNVERIFIED** | no |  | Objective bullet promises a U(1) derivation the body (printed :35/:51) now rescopes to the time-independent residual family. Same ruling as CH05-M1. |
| 65 | ch05 | LOW | WB-LAG | `05_electroweak_gauge_theory.tex:178` | `gauge-boson-masses.md:83` | **UNVERIFIED** | no |  | 'explicitly proven' overreaches both the printed R43 rescope (gbm:83) and the sidecar non-claims for clm-jkpfd4 (claim-quality.md:816 'not original to AVE'; :817 'not a uniqueness theorem' — sidecar,… |
| 66 | ch05 | MEDIUM | KB-INTERNAL (forward-to-ch6.md:40 is byte-identical to TeX:… | `05_electroweak_gauge_theory.tex:159` | `gauge-boson-masses.md:83` | **UNVERIFIED** | no |  | The plaquette section presupposes unitary link variables U_ij=e^{iθ_ij} and derives the Maxwell action; whether 'U(1) Electromagnetism ... derived' (:159 / forward-to-ch6.md:40) and 'full U(1) family… |
| 67 | ch05 | MEDIUM | STALE-KB | `05_electroweak_gauge_theory.tex:83` | `weinberg-angle.md:26` | **UNVERIFIED** | no | MR board vol2 #13 (02:92 LOW mirror-drift: '~20 f… | Print carries the ruled reword (post-#840-audit R3 / CRIB-1; Rule-12 banner at TeX:84 is a % comment, prior wording preserved there and in git). Leaf :26 still reads the superseded 'topological latti… |
| 68 | ch05 | MEDIUM | STALE-KB (print carries Grant-ruled α² native re-anchor, co… | `05_electroweak_gauge_theory.tex:115` | `weak-coupling.md:30` | **UNVERIFIED** | no |  | Print (:103, :109, :115) frames α² as the intermodulation product of two Axiom-4 varactor couplings and explicitly denies the Feynman two-vertex reading; leaf :30 (and :22, :24 'Interaction Lagrangia… |
| 69 | ch05 | LOW | STALE-KB | `05_electroweak_gauge_theory.tex:103` | `weak-coupling.md:22` | **UNVERIFIED** | no |  | Same family as CH05-M6 (opening sentence of the α² paragraph). Fix together. |
| 70 | ch05 | LOW | DEAD-ANCHOR (KB leaf -> common register; texPath here is th… | `vocabulary-register.md:886` | `gauge-boson-masses.md:34` | **UNVERIFIED** | no |  | vocabulary-register.md:870 is now def-t2ph01's status line; def-l0ngdu id is at :883, the cited no-restoring-force clause at :886 (which also carries the 🔴 DEMOTED 2026-08-11 R40-B2a stamp). Repoint … |
| 71 | ch05 | LOW | DEAD-ANCHOR (KB leaf -> common register; texPath is the cit… | `vocabulary-register.md:886` | `gauge-boson-masses.md:42` | **UNVERIFIED** | no |  | :867 is now def-t2ph01's adjudicated-meaning line; def-l0ngdu header/id at :882/:883, quoted clauses at :886. Repoint :867 -> :883 and :870 -> :886. (TeX:233 % comment 'known-positive vocabulary-regi… |
| 72 | ch05 | LOW | DEAD-ANCHOR (KB leaf -> common register; texPath is the cit… | `vocabulary-register.md:901` | `gauge-boson-masses.md:48` | **UNVERIFIED** | no |  | :882 is now the def-l0ngdu section header; def-uatk1s id is at :898 and the 'COUNTERPART SECTOR VARIABLES ... NOT one field' clause at :901. Repoint :882 -> :898 (or :901). |
| 73 | ch05 | LOW | WB-LAG (partial; comment-only note body). The status STAMP … | `05_electroweak_gauge_theory.tex:51` | `gauge-boson-masses.md:176` | **UNVERIFIED** | yes | scan S4a 05:51 (leaf newer, added STRUCK/correcte… | Two residuals: (a) the printed pointer 'dated note at the end of this file' dangles in the PDF (comment-only); (b) the TeX comment row list (:227) carries only the :51 def-l0ngdu-family row, while th… |
| 74 | ch05 | LOW | WB-LAG (KB flag, itself 🔴 DEMOTED 2026-08-11 R40-B1 at the … | `05_electroweak_gauge_theory.tex:33` | `gauge-boson-masses.md:48` | **UNVERIFIED** | no |  | Print never carried the 'mass flow' wording flag (def-uatk1s: u and A are counterpart sector variables, NOT one field). The refutation-threat half of the flag is demoted as void under the R40 carve (… |
| 75 | ch05 | LOW | KNOWN-RESOLVED (re-check of scan S4a 05:35 and MR board vol… | `05_electroweak_gauge_theory.tex:35` | `gauge-boson-masses.md:34` | **UNVERIFIED** | yes | scan S4a 05:35; MR board vol2 #7 (05:35 [MEDIUM][… | Close both as resolved-and-disclosed: the board's PRINTED sentence 'Because the vacuum substrate is incompressible' survives only in the % comment at TeX:38; TeX:35 and leaf :34 are byte-twins carryi… |
| 76 | ch06-A | MEDIUM | WB-LAG (claim-quality-sidecar demotion unpropagated to TeX … | `06_electroweak_and_higgs.tex:17` | `claim-quality.md:162` | **UNVERIFIED (id shared by 7 slices; verdicts not attributable)** | no | vol2/claim-quality.md R40 batch-2a demotion note … | Add a Rule-12 dated caveat at TeX 06:17 (and mirror it into higgs-mechanism.md:13) noting the acoustic-relaxation MECHANISM for the 125 GeV resonance is DEMOTED 2026-08-11 (R40-B2a, NEEDS RE-DERIVATI… |
| 77 | ch06-A | MEDIUM | WB-LAG | `06_electroweak_and_higgs.tex:363` | `chiral-screening.md:35` | **UNVERIFIED (id shared by 7 slices; verdicts not attributable)** | no | MR-board revalidation F8 (06:363-365 Δc_crit prov… | Print at 06:363-365 needs the 2026-08-24 carve's caveat: 'connectivity = trefoil crossing number' is demoted to asserted-pending-derivation and 'connectivity = Cosserat sector count' fails the counte… |
| 78 | ch06-A | MEDIUM | CONTRA / STALE-KB | `06_electroweak_and_higgs.tex:210` | `lepton-spectrum.md:81` | **UNVERIFIED (id shared by 6 slices; verdicts not attributable)** | no |  | TeX's own headline W/Z summary table (06:206-211) already reports the SELF-CONSISTENT loop-corrected values (80,224/90,965 MeV, -0.19%/-0.24%, via the K4 Bethe-tree S11 back-saturation derived at 06:… |
| 79 | ch06-A | MEDIUM | CONTRA | `06_electroweak_and_higgs.tex:321` | `higgs-mass.md:29` | **UNVERIFIED (id shared by 5 slices; verdicts not attributable)** | no |  | TeX's Bethe-lattice cos(2π/c) eigenvalue derivation (06:283-335) gives ν1=9.58, ν2=19.33, ν3=23.75 meV (sum 52.7 meV) and explicitly states 'Normal hierarchy, m1<m2<m3'. higgs-mass.md's simpler 1/c t… |
| 80 | ch06-A | LOW | STALE-KB (TeX diagram unpropagated correction) | `06_electroweak_and_higgs.tex:193` | `lepton-spectrum.md:73` | **UNVERIFIED (id shared by 4 slices; verdicts not attributable)** | no |  | TeX's arrow diagram labels BOTH remaining arrows identically as α·p_c, which does not match TeX's own boxed τ formula two lines above (06:186, m_τ = m_e·p_c/α²). lepton-spectrum.md's 'Net-α-power red… |
| 81 | ch06-A | LOW | DEAD-ANCHOR | `sm-ave-translation.md:10` | `06_electroweak_and_higgs.tex:860` | **UNVERIFIED (id shared by 4 slices; verdicts not attributable)** | no |  | Update sm-ave-translation.md's cited line number from 305 to 860 (the \input actually sits there at HEAD; line 305 is mid-neutrino Bethe-lattice text, unrelated). Pure line-number repair. |
| 82 | ch06-A | LOW | KB-INTERNAL (inconsistent disclosure visibility) | `higgs-mechanism.md:54` | `lepton-spectrum.md:29` | **UNVERIFIED (id shared by 4 slices; verdicts not attributable)** | no |  | The same dated, already-worded Rule-12 open-flag text for the contested √(3/7) label is a VISIBLE rendered blockquote in lepton-spectrum.md:29, but only a HIDDEN HTML comment (invisible on render) at… |
| 83 | ch06-A | LOW | DEAD-ANCHOR | `06_electroweak_and_higgs.tex:422` | `verify-md-links.py:808` | **UNVERIFIED (id shared by 3 slices; verdicts not attributable)** | yes | verify-md-links.py WAIVED_KBLEAF adjudication (re… | Already tracked as a known, deliberately-waived dead cite pending a canonical tracked anchor for the four-lemma Goldstone derivation. No action needed beyond what the tooling already does (loud waive… |
| 84 | ch06-B | MEDIUM | WB-LAG (DISCLOSED-ONLY-IN-COMMENT; routed-not-ruled) | `06_electroweak_and_higgs.tex:516` | `q-g19a-petermann-saliency-closure.md:179` | **UNVERIFIED** | no | q-g19a F5 block (:166-179, 2026-08-03) explicitly… | comment-only. Every C_2 value printed on 06:516-723 rides the 2/(πα) convention and would halve (-0.3416 -> -0.1708, +4% -> -48%) if Grant resolves the :47/:48 inconsistency the other way; print also… |
| 85 | ch06-B | MEDIUM | WB-LAG (DISCLOSED-ONLY-IN-COMMENT) | `06_electroweak_and_higgs.tex:575` | `q-g19a-petermann-saliency-closure.md:193` | **UNVERIFIED** | no | TeX % comment 06:523-525 ('tau_retard = 1/omega_C… | comment-only. Print 06:575 asserts τ_retard = 1/ω_C 'set by the unknot geometric scale' and 06:626 reads the τ-peak as 'confirming ... the geometric pinning of the retardation'; the Grant ruling (202… |
| 86 | ch06-B | LOW | WB-LAG (dated KB scope note absent from print) | `06_electroweak_and_higgs.tex:620` | `q-g19a-petermann-saliency-closure.md:164` | **UNVERIFIED** | no |  | KB :164 (2026-08-03, F3) scopes the 'converges at N_t ≳ 2e5' (06:610) and 'three derivative methods' (06:620) receipts to the Stage-1 4% level and declares them non-probative for the retardation bias… |
| 87 | ch06-B | LOW | DEAD-ANCHOR | `06_electroweak_and_higgs.tex:723` | `q-g19a-petermann-saliency-closure.md:131` | **UNVERIFIED** | no | 2026-09-06 scan S4a lists 06:722 as a staleness c… | Verified at HEAD: :12/:14/:92 still resolve; :100 is now a blank blockquote line, :103 is 'What survives from the body above', :121 is 'Consequence: the dispute recorded above dissolves'. Repoint :10… |
| 88 | ch06-B | LOW | DEAD-ANCHOR | `06_electroweak_and_higgs.tex:770` | `q-g19a-petermann-saliency-closure.md:110` | **UNVERIFIED** | no | 2026-09-06 scan S5 (line 243): '06:770 -> q-g19a.… | Verified at HEAD: :110 is a python line inside the 2026-08-03 instrument-audit block; the cited RESOLVED-NEGATIVE bullet is now at :221. Repoint :110 -> :221. The same ':110' also appears in the % co… |
| 89 | ch06-B | LOW | WB-LAG (dated scope label absent from print) | `06_electroweak_and_higgs.tex:777` | `q-g19a-petermann-saliency-closure.md:242` | **UNVERIFIED** | yes |  | KB :240-244 (2026-08-02) adds the 'at Stage 1' scope label at exactly this section; print's list (trefoil, Compton retardation, LC equipartition, 1/π², α/π) is the Stage-1 list and δ = -3α/2 is not i… |
| 90 | ch06-B | MEDIUM | WB-LAG (register-side demotion; also KB-INTERNAL register-v… | `06_electroweak_and_higgs.tex:810` | `claim-quality.md (register carrier: clm-p7rfkb :162 R40-B2a stamp + R40 batch-2a note :1710-1720; NO leaf carries the stamp — higgs-mechanism.md and vol6 lambda-higgs-derivation.md:26 are unstamped):1717` | **UNVERIFIED** | no | R40 batch-2a (2026-08-11/12): claim-quality.md:16… | Route. Print 06:808-833 (and 06:831 'the volume pulsation of the fundamental lattice cell') asserts the K4 dilatational breathing mode flatly; under R40/Axiom 5 clause G the A1/bulk slot is a bound r… |
| 91 | ch06-B | MEDIUM | WB-LAG (scope/strength overclaim vs leaf) | `06_electroweak_and_higgs.tex:788` | `lambda-higgs-derivation.md:12` | **UNVERIFIED** | no |  | Route for a printed scope line. The vol6 leaf :12 (referencing research/2026-06-06 biquaternion result, G3-FAIL) re-scopes the Higgs<->breathing-mode identification as FORM not VALUE; register clm-p7… |
| 92 | ch06-B | LOW | DEAD-ANCHOR | `06_electroweak_and_higgs.tex:833` | `constants.py (engine file cited via \kbleaf, not a KB leaf):679` | **UNVERIFIED** | no |  | Printed line-number cite is stale: the symbol lives at constants.py:679 at HEAD (content unchanged). Repoint 'line 338' -> 679 or drop the line number (the symbol cite is stable). |
| 93 | ch06-B | LOW | DEAD-ANCHOR (KB->TeX direction) | `06_electroweak_and_higgs.tex:860` | `sm-ave-translation.md:10` | **UNVERIFIED** | no |  | Forwarder's TeX line cite is stale (HEAD 06:860). Repoint 'line 305' -> 860, or cite by the label sec:sm_ave_translation which the leaf already names. |
| 94 | ch06-B | LOW | KB-INTERNAL (leaf vs its own index) | `index.md (KB-INTERNAL: 'tex' side here is the derived index):36` | `q-g19a-petermann-saliency-closure.md:14` | **UNVERIFIED** | no | q-g19a ppm-strike block :196-204 enumerates un-sw… | Regenerate the index row from the leaf: strike '10 ppm with postulate' and '50 ppm at $C_2$ / ≈10 ppm at $a_e$ total' (Grant ruling 2026-08-03, 'every one of them is struck'); replace 'corpus admits … |
| 95 | ch06-B | MEDIUM | KB-INTERNAL | `q-g27-muon-cosserat-saliency.md (KB-INTERNAL: leaf vs sibling leaf):57` | `q-g19a-petermann-saliency-closure.md:221` | **UNVERIFIED** | no |  | Route (inventory only; no adjudication). q-g27 builds the muon forward (+502e-11, 4.6σ) on the universal -3α/2 Stage-2 term (:55-59, :71) and names 'the n_q-additive Q-G19α framework it builds on' (:… |
| 96 | ch06-B | LOW | KB-INTERNAL | `q-g20f-vacuum-polarization.md (KB-INTERNAL: leaf vs sibling leaf):97` | `q-g19a-petermann-saliency-closure.md:196` | **UNVERIFIED** | no | q-g19a :198-204 enumerates un-swept sites (four i… | Strike '(50 ppm, postulate-conditional)' and 'at 50 ppm precision' at q-g20f:97 per the 2026-08-03 ruling, copying the leaf's '[ppm label struck 2026-08-03 per Grant ruling]' marker (text exists verb… |
| 97 | ch06-B | LOW | KB-INTERNAL | `q-g27-muon-cosserat-saliency.md (KB-INTERNAL: leaf vs sibling leaf):80` | `q-g19a-petermann-saliency-closure.md:196` | **UNVERIFIED** | no |  | Strike '50 ppm postulate-conditional' and 'the 50 ppm figure' at q-g27:80 per the 2026-08-03 ruling (same marker as ch06B-13). |
| 98 | ch06-B | LOW | KB-INTERNAL (register lags leaf) | `claim-quality.md (KB-INTERNAL: derived register vs leaf; clm-v2sg8z):1443` | `q-g19a-petermann-saliency-closure.md:221` | **UNVERIFIED** | no |  | Register refresh (owner call, not this lane): :1443/:1447/:1460 still carry the ppm labels struck 2026-08-03; :1449 and :1460 still caveat n_q-additivity as 'the single remaining intuitive step' alth… |
| 99 | ch07-A | MEDIUM | WB-LAG (DISCLOSED-ONLY-IN-COMMENT) | `07_quantum_mechanics_and_orbitals.tex:277` | `hierarchical-cascade-correction.md:54` | **UNVERIFIED** | no |  | comment-only: print :277 asserts the static FOC/J_2s model yields Be IE = 9.32 eV parameter-free; the walk-back ('% appears to match experiment by coincidence—the ACTUAL correction is the hierarchica… |
| 100 | ch07-A | MEDIUM | CONTRA | `07_quantum_mechanics_and_orbitals.tex:324` | `subshell-junction-scattering.md:11` | **UNVERIFIED** | no |  | Print sells a 9.4 eV Boron IE 'prediction'; the KB states Boron's IE is 8.30 eV (subshell-junction-scattering.md:11) and the KB validation table lists B AVE 8.065 / exp 8.298 / -2.80% (ionization-ene… |
| 101 | ch07-A | MEDIUM | CONTRA | `07_quantum_mechanics_and_orbitals.tex:220` | `orbital-penetration-penalties.md:29` | **UNVERIFIED** | no |  | Opposite sign of the same mechanism: print :220-227 says the 1/d shunt STRIPS the 2s binding (2s E_bind = 5.75 eV at :224 vs 2p 13.26 eV at :225, '2p ... locked tightly', :227 '2s mode ... scattering… |
| 102 | ch07-A | MEDIUM | CONTRA | `07_quantum_mechanics_and_orbitals.tex:243` | `helium-symmetric-cavity.md:34` | **UNVERIFIED** | no | MR board 2026-08-02 vol2 07:243 [route-to-core]; … | CONFIRMED at HEAD: :243 still prints N_eff = 1.5 and '+72% ... down to -2.6%' (0 KB hits for '72', '1.0 + 0.5', 'Euler Buckling'), and :253 still prints He 1s^2 N_eff = 2.0 -> 24.19 eV (KB-homed at h… |
| 103 | ch07-A | MEDIUM | WB-LAG | `07_quantum_mechanics_and_orbitals.tex:333` | `program-arc-map.md:371` | **UNVERIFIED** | no | revalidation 2026-09-06 item 11:123 (N13 protein … | Print asserts the protein-folding engine has 'Tier-1 derivation status'; the KB program-arc-map registers arc N13 (protein impedance-folding) as NEGATIVE with 'Core walk-back STAGED, B4 row may be ST… |
| 104 | ch07-A | MEDIUM | CONTRA | `07_quantum_mechanics_and_orbitals.tex:488` | `de-broglie-n.md:10` | **UNVERIFIED** | no |  | Print :485 ('the deep core strain dramatically intensifies as nuclear mass scales', V_local/V_yield ~ Z alpha^2 A_0/r) and the :486-490 'Regime IV Vacuum Yield Boundary' resultbox (Z>=19 pushed past … |
| 105 | ch07-A | MEDIUM | WB-LAG | `07_quantum_mechanics_and_orbitals.tex:726` | `de-broglie-standing-wave.md:240` | **UNVERIFIED** | no | def-quant3 (common/vocabulary-register.md:258-275… | Print :725-726 calls the de Broglie standing-wave integer n 'the winding number ... a topological invariant'; the KB leaf's terminology note (:240, per def-quant3) re-scopes it as the cavity-deformab… |
| 106 | ch07-A | MEDIUM | WB-LAG | `07_quantum_mechanics_and_orbitals.tex:46` | `de-broglie-standing-wave.md:58` | **UNVERIFIED** | no |  | KB :58 carries a dated correction ('notation parallelism cleanup 2026-05-17 — prior leaf revision wrote n_s without the explicit "1 +", which the C11 driver script inherited as a factor-7-low bug'); … |
| 107 | ch07-A | LOW | WB-LAG | `07_quantum_mechanics_and_orbitals.tex:39` | `de-broglie-standing-wave.md:50` | **UNVERIFIED** | no |  | Print :39 asserts photons OR gravity waves are matched at Z = 377 Ohm; KB :50 (dated 2026-06-11 three-impedance-law channel note) scopes 377 Ohm to photons only (Z_EM) and gives gravity waves a diffe… |
| 108 | ch07-A | LOW | STALE-KB | `07_quantum_mechanics_and_orbitals.tex:383` | `analog-ladder-filter.md:52` | **UNVERIFIED** | no | R40 worklist row 07_quantum_mechanics_and_orbital… | Print :383 is stamped DEMOTED R40-B2a (Z_LC=12.31 Ohm bulk-modulus attribution); the verbatim KB twin analog-ladder-filter.md:52 carries no stamp and no Rule-12 banner. Near-mechanical (copy the rule… |
| 109 | ch07-A | LOW | DEAD-ANCHOR | `07_quantum_mechanics_and_orbitals.tex:41` | `de-broglie-standing-wave.md:267` | **UNVERIFIED** | yes |  | The printed stamp (status IS disclosed in print) points to a 'dated note at the end of this file', but the R40 batch-2a note in the TeX is entirely a % comment block (:4204-4290; 0 non-comment lines)… |
| 110 | ch07-A | LOW | KB-INTERNAL | `07_quantum_mechanics_and_orbitals.tex:173` | `ode-verification.md:49` | **UNVERIFIED** | no |  | Two ch07 leaves disagree, unbannered: ode-verification.md:49 (mirrored verbatim in print :173) places r < a_0 in Regime II (Yield), while de-broglie-n.md:10 says the entire atom is in the linear regi… |
| 111 | ch07-B | HIGH | CONTRA | `07_quantum_mechanics_and_orbitals.tex:1446` | `macro-cavity-saturation.md:10` | **UNVERIFIED** | no |  | Print itself is internally inconsistent and my whole assigned slice sits inside the inconsistency. TeX:558 (just before my slice) states the 'Topological N-Port Y-Matrix architecture' (i.e. exactly S… |
| 112 | ch07-B | HIGH | KB-INTERNAL | `07_quantum_mechanics_and_orbitals.tex:1314` | `index.md:45` | **UNVERIFIED** | no |  | The ch07 index.md itself documents (line 45, in its 'Derivations and Detail' table) that macro-cavity-saturation.md records supersession of the N-port Y-matrix by mutual cavity loading -- yet the SAM… |
| 113 | ch07-B | LOW | CONTRA | `07_quantum_mechanics_and_orbitals.tex:1965` | `radial-eigenvalue-solver.md:177` | **UNVERIFIED** | no |  | Cosmetic label drift only, no numeric/physics conflict found: the 'Validation' column of the nuclear/atomic/antenna/galactic cross-scale-isomorphism table names the antenna-scale validation 'Chiral A… |
| 114 | ch07-C | MEDIUM | CONTRA — eq:kappa_hopf: print carries a sign-alternating pa… | `07_quantum_mechanics_and_orbitals.tex:3288` | `radial-eigenvalue-solver.md:731` | **UNVERIFIED (id shared by 7 slices; verdicts not attributable)** | no |  | Route for ruling; not mechanical. Facts for the ruler: git log -L shows TeX 3288 and KB 731 both unchanged since initial release de9d2293 (2026-04-13) — the leaf was never verbatim at this spot. The … |
| 115 | ch07-C | MEDIUM | CONTRA — 'Hopf link back-EMF' bullet: print (3318-3329) ass… | `07_quantum_mechanics_and_orbitals.tex:3323` | `radial-eigenvalue-solver.md:741` | **UNVERIFIED (id shared by 7 slices; verdicts not attributable)** | no |  | Same ruling as M1 (companion prose to the parity factor). Print's Period-3 claim ('and natively resolves the Period-3 binding' at 3328) has no KB home anywhere in ave-kb (grep 'Inductive Drag' / 'Per… |
| 116 | ch07-C | MEDIUM | KB-INTERNAL (also print-internal) — E2k (TeX 3200 '(all she… | `07_quantum_mechanics_and_orbitals.tex:3306` | `radial-eigenvalue-solver.md:739` | **UNVERIFIED (id shared by 6 slices; verdicts not attributable)** | no |  | The correction exists in print (3611) and KB (scale-separation.md:35) as an undated 'Note:' at the OTHER site only; the E2k site still presents same-n CDF screening as the architecture. Candidate for… |
| 117 | ch07-C | MEDIUM | KB-INTERNAL (also print-internal) — the E2 Summary box (TeX… | `07_quantum_mechanics_and_orbitals.tex:2728` | `dual-formalism-architecture.md:21` | **UNVERIFIED (id shared by 5 slices; verdicts not attributable)** | no |  | Ruling needed on whether the Y->S half of the Dual-Formalism box is historical (then it needs a dated superseded banner at TeX 2711-2737 and dual-formalism-architecture.md:10) or still standing (then… |
| 118 | ch07-C | MEDIUM | KB-INTERNAL (also print-internal) — Li IE printed as 5.32 e… | `07_quantum_mechanics_and_orbitals.tex:3136` | `radial-eigenvalue-solver.md:689` | **UNVERIFIED (id shared by 4 slices; verdicts not attributable)** | no | vol2/claim-quality.md clm-oltvwy:348 (derived sid… | Sidecar already instructs 'Treat the ±2.8% headline as the validated solver bound' and lists 'Reconcile the Li per-element residual' as strengthen-by. Leaf-level: a dated cross-note at radial-eigenva… |
| 119 | ch07-C | LOW | KB-INTERNAL (also print-internal) — Be printed as 8.21 eV /… | `07_quantum_mechanics_and_orbitals.tex:3138` | `radial-eigenvalue-solver.md:690` | **UNVERIFIED (id shared by 4 slices; verdicts not attributable)** | no | vol2/claim-quality.md clm-oltvwy:347,:364 and clm… | Narrative-stage snapshot: E2k (TeX 3152-3164) immediately calls the E2d-E2j architecture 'the fundamental problem', so the table is partially self-disclosed by narrative, but not by any dated marker.… |
| 120 | ch07-C | LOW | KB-INTERNAL — three unreconciled He first-IE precisions acr… | `07_quantum_mechanics_and_orbitals.tex:3134` | `radial-eigenvalue-solver.md:688` | **UNVERIFIED (id shared by 4 slices; verdicts not attributable)** | no |  | The 24.19 vs 24.37 pair are different methods (MCL vs Hopf-link circuit) and may coexist by design; the '0.008%' at chiral-factor.md:28 / TeX 3851 (ch07-D) matches neither and is the outlier to route… |
| 121 | ch07-D | MEDIUM | STALE-KB | `07_quantum_mechanics_and_orbitals.tex:3529` | `scale-separation.md:49` | **UNVERIFIED (id shared by 7 slices; verdicts not attributable)** | no | MR board vol2 finding 07:3510 (2026-08-02); TeX-s… | Update scale-separation.md:49 to drop the 'confirmed independently ... Axiom 2' wording and replace with the already-ruled 2026-08-02 correction verbatim available in TeX 07:3529-3541: K=2G is GR-imp… |
| 122 | ch07-D | MEDIUM | WB-LAG | `07_quantum_mechanics_and_orbitals.tex:3496` | `claim-quality.md:393` | **UNVERIFIED (id shared by 7 slices; verdicts not attributable)** | no | claim-quality.md clm-oltvwy (line ~349) and clm-w… | Add a print-visible qualifier to the 'Approach 24: Complete Phase Integral' resultbox (07:3486-3499) noting that corrections A/B/C (hierarchical cascade, SIR, Op10 -- introduced later in this same ch… |
| 123 | ch07-D | LOW | STALE-KB | `07_quantum_mechanics_and_orbitals.tex:3654` | `subshell-junction-scattering.md:38` | **UNVERIFIED (id shared by 6 slices; verdicts not attributable)** | no |  | Append the same parenthetical print already carries -- '(form-derived, value GR-imported; not an axiom of this framework)' -- to the bare '($K=2G$)' label in subshell-junction-scattering.md:38, copyi… |
| 124 | ch07-D | LOW | TEX-INTERNAL-CONTRA (disclosed only in a derived sidecar) | `07_quantum_mechanics_and_orbitals.tex:4027` | `claim-quality.md:349` | **UNVERIFIED (id shared by 5 slices; verdicts not attributable)** | yes | claim-quality.md clm-oltvwy rationale (Li residua… | No mechanical fix proposed here (adjudicating which Li figure is canonical is a physics/architecture call, flagged in claim-quality as already open); note only that the print-side inconsistency betwe… |
| 125 | ch09 | MEDIUM | STALE-KB | `09_computational_proof.tex:92` | `anomaly-catalog.md:15` | **UNVERIFIED (id shared by 7 slices; verdicts not attributable)** | no |  | Replace the anomaly-catalog.md muon g-2 bullet with the corrected framing already printed at ch09.tex:85-95 (observed anomaly +245(56)e-11 vs AVE forward-prediction +502e-11 via Q-G27, 4.6-sigma, wal… |
| 126 | ch09 | MEDIUM | STALE-KB | `09_computational_proof.tex:56` | `computational-graph.md:30` | **UNVERIFIED (id shared by 7 slices; verdicts not attributable)** | no |  | Update the Agreement-column cell of the Verification Summary table in computational-graph.md from 'sub-3 A' to the corrected 'qualitative (see Rule-12 scope note, clm-u4vmgk)' language now printed in… |
| 127 | ch09 | HIGH | STALE-KB | `09_computational_proof.tex:249` | `methodological-contamination.md:71` | **UNVERIFIED (id shared by 6 slices; verdicts not attributable)** | no |  | Print carries the dated 2026-08-02 CRIB-1 AXIOM-ATTRIBUTION correction (ch09.tex:236-249, citing ave-kb/common/form-deriving-value-importing.md:87 [verified: K=2G row, GR-IMPORTED] and vol1/claim-qua… |
| 128 | ch10 | MEDIUM | WB-LAG | `10_open_problems.tex:320` | `g-star-prediction.md:10` | **UNVERIFIED (id shared by 7 slices; verdicts not attributable)** | no |  | Add a footnote or in-line parenthetical to TeX §Testable Prediction (10:316-322, and/or the g_* row of the quantitative-resolutions table at 10:423) carrying the 2026-08-18 Wave-2 D15b provenance rid… |
| 129 | ch10 | HIGH | STALE-KB (also KB-INTERNAL vs the sibling baryon-asymmetry.… | `10_open_problems.tex:419` | `quantitative-resolutions.md:15` | **UNVERIFIED (id shared by 7 slices; verdicts not attributable)** | no | 2026-06-20 Rule-12 walk-back / auditor FINDING 2 … | Update quantitative-resolutions.md:15 to match the already-corrected wording in baryon-asymmetry.md:70 and TeX:419 — '0.79% (OOM)' / 'Consistency-check' with a footnote citing the 2026-06-20 Rule-12 … |
| 130 | ch11 | MEDIUM | CONTRA | `11_standard_model_overdrive.tex:66` | `claim-quality.md:604` | **UNVERIFIED** | no | research/2026-09-06_mr-board-revalidation_RESULT.… | Qualify or remove 'at comparable accuracy' in ch11 line 66. clm-dboxok (vol2/claim-quality.md ~:604) explicitly non-claims a head-to-head accuracy benchmark against Lattice QCD; the printed sentence … |
| 131 | ch11 | MEDIUM | STALE-KB | `11_standard_model_overdrive.tex:123` | `program-arc-map.md:371` | **UNVERIFIED** | no | research/2026-09-06_mr-board-revalidation_RESULT.… | Do not silently reword — this needs adjudication, not a mechanical edit. Determine whether program-arc-map N13 ('protein impedance-folding' EE-reflection-channel mechanism, cross-repo AVE-Protein lan… |
| 132 | ch12-mp | MEDIUM | STALE-KB | `12_the_millennium_prizes.tex:112` | `yang-mills-steps1-2.md:30` | **UNVERIFIED** | no |  | Copy the TeX 'Scope note (2026-07-09, #604/#607)' paragraph (12mp:112) verbatim into yang-mills-steps1-2.md immediately after the sentence ending '...eliminating UV divergence.' (leaf line 30), so th… |
| 133 | ch12-fp | HIGH | CONTRA | `12_appendix_formal_proofs.tex:170` | `yang-mills-steps1-2.md:46` | **UNVERIFIED** | no |  | OS5's 'Correlation Length (Derived Magic Number)' argument (TeX :164-171) asserts the trefoil (crossing number q=3) is 'the lightest stable topological defect,' but yang-mills-steps1-2.md:46 (Step 2,… |
| 134 | ch12-fp | MEDIUM | CONTRA | `12_appendix_formal_proofs.tex:197` | `yang-mills-steps1-2.md:10` | **UNVERIFIED** | yes |  | The 'Yang--Mills Continuum QFT (Formal Statement)' resultbox (TeX :188-201) states flatly, as an achieved conclusion of applying the OS Reconstruction Theorem, that 'there exists a unique Wightman qu… |
| 135 | ch12-fp | MEDIUM | CONTRA | `12_appendix_formal_proofs.tex:280` | `navier-stokes-prize.md:10` | **UNVERIFIED** | yes |  | The 'Navier-Stokes Smoothness (Formal Statement)' resultbox (TeX:276-284) asserts a global smooth C^infty((0,infty); H^1(R^3)) solution as an achieved result. The trailing 'Remaining Clay gap' paragr… |
| 136 | ch12-fp | MEDIUM | CONTRA | `12_appendix_formal_proofs.tex:357` | `riemann-hypothesis.md:10` | **UNVERIFIED** | yes |  | The 'Zero-Free Region, Physical Contrapositive' resultbox (TeX:355-363) states the Riemann Hypothesis's conclusion flatly as a 'Theorem,' with a full physical proof, of exactly the statement Clay is … |


#### Fragments + verifier notes

**1. CH01A-M1** (ch01-A, CONFIRMED)
- print `01_topological_matter.tex:35` — `Mass is the stored inductive energy required to maintain the topological integrity of the standing wave.`
- KB `newtonian-inertia-as-lenz.md:14` — `> **🔴 STORED INDUCTIVE ENERGY = the FLYWHEEL (spin/frequency-regulation), the REST MASS *store* is A1 (2026-06-20, Rule 12 — body above PRESERVED unedited; Grant-ratified mass-sector ruling).**`
- verifiers: CONFIRMED: Both fragments verified byte-verbatim (tex 01_topological_matter.tex:35, kb newtonian-inertia-as-lenz.md:14). Read tex lines 1-60: no print…

**2. CH01A-M2** (ch01-A, CONFIRMED)
- print `01_topological_matter.tex:8` — `\item Understand how mass emerges macroscopically from the continuous distributed inductance of closed optical loops (Lenz's Law).`
- KB `newtonian-inertia-as-lenz.md:14` — `the re-scope only re-labels *which sector stores the rest mass* (A1, not the inductive flywheel)`
- verifiers: CONFIRMED: Both fragments verified byte-verbatim: TeX line 8 ("\item Understand how mass emerges macroscopically from the continuous distributed induc…

**3. CH01A-M3** (ch01-A, DOWNGRADED)
- print `01_topological_matter.tex:207` — `Neutrino ($\nu$)           & Twisted unknot      & I--II boundary & Chiral phase below yield \\`
- KB `index.md:13` — `The closed-loop framing has been **superseded** by the Cosserat torsional screw-dislocation model`
- verifiers: DOWNGRADED: Both fragments verify byte-verbatim: tex 01_topological_matter.tex:207 "Neutrino ($\nu$) & Twisted unknot & I--II boundary & Chiral phase b…

**4. CH01A-M4** (ch01-A, DOWNGRADED)
- print `01_topological_matter.tex:207` — `Neutrino ($\nu$)           & Twisted unknot      & I--II boundary & Chiral phase below yield \\`
- KB `regime-classification.md:15` — `\| Neutrino ($\nu$) \| Twisted unknot \| I--II boundary \| Chiral phase below yield \|`
- verifiers: DOWNGRADED: Both fragments verify byte-exact: tex 01_topological_matter.tex:207 and KB regime-classification.md:15 both read "Neutrino ($\nu$) ... Twis…

**5. CH01A-M5** (ch01-A, DOWNGRADED)
- print `01_topological_matter.tex:209` — `Proton ($p$)               & $(2,5)$ phase portrait & II (Yield)    & $6^3_2$ Borromean linkage at saturation \\`
- KB `regime-classification.md:17` — `\| Proton ($p$) \| $(2,5)$ Cinquefoil \| II (Yield) \| Borromean linkage at saturation \|`
- verifiers: DOWNGRADED: Fragments verified: tex line 209 exact match; KB regime-classification.md line 17 exact match ('\\| Proton ($p$) \\| $(2,5)$ Cinquefoil \\| II…

**6. CH01A-M6** (ch01-A, CONFIRMED)
- print `01_topological_matter.tex:242` — `An electron ($e^-$) is a right-handed unknot; a positron ($e^+$) is physically identical, but wound as a left-handed unknot.`
- KB `chirality-and-antimatter.md:10` — `the electron ($e^-$) carries **left-handed** Beltrami helicity (the LH content of the confined flux, per [`pair-production-axiom-derivation.md`](pair-production-axiom-derivation.md):27,79); the posit…`
- verifiers: CONFIRMED: Both fragments verified byte-verbatim: tex:242 exact match (full line quoted, part of the "Chirality and Antimatter Disintegration" section…

**7. CH01A-M7** (ch01-A, CONFIRMED)
- print `01_topological_matter.tex:248` — `previously trapped within the closed LC resonance of the Hopfion, unwinds`
- KB `chirality-and-antimatter.md:18` — `previously trapped within the closed LC resonance of the $0_1$ unknot, unwinds`
- verifiers: CONFIRMED: Both fragments verified byte-verbatim: tex 01_topological_matter.tex:248 says "...closed LC resonance of the Hopfion, unwinds"; kb chiralit…

**8. CH01A-M8** (ch01-A, CONFIRMED)
- print `01_topological_matter.tex:259` — `A spatial solver demonstrating how a propagating Transverse EM Wave winds into a stationary Spin-1 helical loop when encountering extreme localised network impedance ($Z \to Z_{crit}$). The discrete …`
- KB `electron-identification.md:64` — `The genesis / self-lock arc that would *dynamically create* the fluxoid from a free precursor is **closed-negative** (electron-genesis-from-free-precursor leans-falsified; the engine pumps H at $dt\t…`
- verifiers: CONFIRMED: Both fragments verified byte-verbatim: tex:259 (figure caption, \label{fig:photon_spin_structure}) and kb electron-identification.md:64. No…

**9. CH01A-M9** (ch01-A, CONFIRMED)
- print `01_topological_matter.tex:79` — `\kbleaf{ave-kb/vol2/particle-physics/ch01-topological-matter/electron-identification.md} (the $g=2$`
- KB `electron-identification.md:92` — `The honest stance is canonical at [`translation-circuit.md`](../../../common/translation-tables/translation-circuit.md):637 ("$g = 2$ is POSITED, not derived").`
- verifiers: CONFIRMED: Both fragments verified byte-verbatim. TeX line 79 (\kbleaf{...electron-identification.md} (the $g=2$) is confirmed at 01_topological_matte…

**10. CH01A-M10** (ch01-A, CONFIRMED)
- print `01_topological_matter.tex:55` — `%      translation-circuit.md:767 ("**$g = 2$ is POSITED, not derived**"; the sweep's kb_truth`
- KB `translation-circuit.md:839` — `- **$g = 2$ is POSITED, not derived** (`ave-evidence-framing-discipline`); the anomalous part $a_e = \alpha/2\pi$ is the slip (§10.2/§10.3), but the leading $g=2$ is an input.`
- verifiers: CONFIRMED: Both fragments verified byte-verbatim: tex line 55 (grep -nF exact match) sits inside the 2026-08-02 %-comment Rule-12 block spanning ~41-5…

**11. CH01A-M11** (ch01-A, CONFIRMED)
- print `01_topological_matter.tex:239` — `All values use $\kappa_{FS} = 8\pi(1 - 1/(14\pi^2))$ from \texttt{ave.core.constants} with zero empirical fits.`
- KB `torus-knot-ladder.md:21` — `but **which particle occupies each rung** — the "Particle (real-space body)" column — is an **imported identification** (electron ↔ $(2,3)$, proton ↔ $(2,5)$, …), not substrate-forced. The rung STRUC…`
- verifiers: CONFIRMED: Both fragments verified byte-verbatim: tex fragment at manuscript/vol_2_subatomic/chapters/01_topological_matter.tex:239 (matches exactly, …

**12. CH01A-M12** (ch01-A, DOWNGRADED)
- print `01_topological_matter.tex:227` — `$(2,3)$ trefoil ($3_1$)    & 3  & $8.317\,\ell_{node}$ & SU(2) & Electron ($0_1$ unknot) \\`
- KB `torus-knot-ladder.md:10` — `so $r_{opt}$ is a **pure number, NOT a length** (the $\ell_{node}$ units previously attached to it were spurious)`
- verifiers: DOWNGRADED: Both fragments verified byte-verbatim: tex:227 is the exact trefoil table row (grep -nF confirms line 227, not 218/237 as the alreadyKnownI…

**13. CH01A-M13** (ch01-A, CONFIRMED)
- print `01_topological_matter.tex:40` — `feed into each other in a closed topological loop ($\nabla \times \mathbf{A} = k\mathbf{A}$), permanently trapping the energy.`
- KB `electron-unknot.md:13` — `🔴 *(2026-06-24: "permanently trapping the energy" is **topology-pinned** (the closed Beltrami loop / Ax2 winding) + boundary, NOT a bulk self-focusing well — the bulk self-trap is a Cartesian artifac…`
- verifiers: CONFIRMED: Both fragments verified byte-verbatim: tex 01_topological_matter.tex:40 carries "...feed into each other in a closed topological loop ($\na…

**14. CH01A-M14** (ch01-A, DOWNGRADED)
- print `01_topological_matter.tex:244` — `The AVE framework resolves this mathematical paradox via \textbf{Optical Phase Cancellation}.`
- KB `chirality-and-antimatter.md:28` — `> **Tag (peer, not chord).** The observable $2\gamma$ at $2 m_e c^2 = 1.022$ MeV is the **standard-QED result** — AVE claims **no** distinct cross-section, branching ratio, or kinematic distribution …`
- verifiers: DOWNGRADED: Both fragments verified byte-verbatim: tex fragment at actual line 246 (claimed 244, off by 2) in manuscript/vol_2_subatomic/chapters/01_to…

**15. CH01A-M15** (ch01-A, UNVERIFIED)
- print `01_topological_matter.tex:147` — `The minimum discrete diameter of the flux tube is normalised to one fundamental lattice pitch ($d \equiv 1 l_{node}$).`
- KB `electron-unknot.md:59` — `The minimum discrete diameter of the flux tube is normalised to one fundamental lattice pitch ($d \equiv 1 l_{node}$).`
- verifiers: 

**16. CH01A-M16** (ch01-A, DOWNGRADED)
- print `01_topological_matter.tex:16` — `stable particles are defined as finite-energy soliton solutions to the generalised \textbf{Faddeev-Skyrme Energy Functional}`
- KB `mathematical-topology-of-mass.md:20` — `> **Peer + finiteness note.** The Faddeev-Skyrme energy functional is **standard soliton field theory** (Faddeev–Niemi / Skyrme), imported here as calculational scaffolding — **peer-with-standard**, …`
- verifiers: DOWNGRADED: Both fragments verified byte-verbatim: tex fragment at 01_topological_matter.tex:16 exactly as quoted; kb fragment at mathematical-topology…

**17. M1** (ch01-B, UNVERIFIED (id shared by 7 slices; verdicts not attributable))
- print `01_topological_matter.tex:110` — `breathing-soliton seed gives $\mathcal{M} > 0$, $\mathcal{Q} = 1$,`
- KB `electron-unknot-cosserat-seeder.md:113` — `**Mode I PASS** — engine autonomously hosts breathing soliton`
- verifiers: 

**18. M2** (ch01-B, UNVERIFIED (id shared by 7 slices; verdicts not attributable))
- print `01_topological_matter.tex:120` — `proving it is the geometric circumference of the $0_1$ unknot.`
- KB `electron-bound-resonator-coverage.md:186` — `\| D.1 \| **$\ell_{\mathrm{node}}$ CIRCULAR** — definitional, $m_e$ is the input ruler; one-ruler TARGET not achieved ($G$ makes count plausibly TWO) \| C \| OPEN — clm-5xon03 \|`
- verifiers: 

**19. M3** (ch01-B, UNVERIFIED (id shared by 6 slices; verdicts not attributable))
- print `01_topological_matter.tex:55` — `translation-circuit.md:767 ("**$g = 2$ is POSITED, not derived**"; the sweep's kb_truth`
- KB `translation-circuit.md:839` — `- **$g = 2$ is POSITED, not derived** (`ave-evidence-framing-discipline`); the anomalous part $a_e = \alpha/2\pi$ is the slip (§10.2/§`
- verifiers: 

**20. M4** (ch01-B, UNVERIFIED (id shared by 5 slices; verdicts not attributable))
- print `01_topological_matter.tex:56` — `field said :637 -- re-verified at HEAD the line is :767, cite repaired here).`
- KB `substrate-perspective-electron.md:11` — `(../../../common/translation-tables/translation-circuit.md):637`
- verifiers: 

**21. M5** (ch01-B, UNVERIFIED (id shared by 4 slices; verdicts not attributable))
- print `01_topological_matter.tex:56` — `field said :637 -- re-verified at HEAD the line is :767, cite repaired here).`
- KB `substrate-perspective-electron.md:227` — `(../../../common/translation-tables/translation-circuit.md):637`
- verifiers: 

**22. M6** (ch01-B, UNVERIFIED (id shared by 4 slices; verdicts not attributable))
- print `01_topological_matter.tex:56` — `field said :637 -- re-verified at HEAD the line is :767, cite repaired here).`
- KB `electron-bound-resonator-coverage.md:56` — `(../../../common/translation-tables/translation-circuit.md):637`
- verifiers: 

**23. M7** (ch01-B, UNVERIFIED (id shared by 4 slices; verdicts not attributable))
- print `01_topological_matter.tex:167` — `inside which the $A_1$ mass core operates sub-saturated at $A = \sqrt{\alpha}$`
- KB `l3-electron-soliton-synthesis.md:108` — `> **Subatomic-scale convention**: per Vol 4 Ch 1 verbatim,`
- verifiers: 

**24. M8** (ch01-B, UNVERIFIED (id shared by 3 slices; verdicts not attributable))
- print `01_topological_matter.tex:230` — `$9_1$ knot         & 9  & $2.772\,\ell_{node}$ & SU(5) & $\Delta(1600)$ \\`
- KB `l3-electron-soliton-synthesis.md:37` — `\| $\geq 9$ \| unstable \| 2 \| (odd) \|`
- verifiers: 

**25. M9** (ch01-B, UNVERIFIED)
- print `01_topological_matter.tex:242` — `An electron ($e^-$) is a right-handed unknot; a positron ($e^+$) is physically identical, but wound as a left-handed unknot.`
- KB `pair-production-axiom-derivation.md:27` — `\| Parity-conserving output \| Two contra-rotating Beltrami vortices: $e^-$ (LH chirality) + $e^+$ (RH chirality); $m_e c^2$ each \|`
- verifiers: 

**26. M10** (ch01-B, UNVERIFIED)
- print `(no TeX twin — KB-internal, both leaves are kb-only):0` — `(n/a)`
- KB `electron-unknot-cosserat-seeder.md:120` — `a self-consistent ground-state search (imaginary-time descent or Newton-Raphson) would tune to exact canonical`
- verifiers: 

**27. ch01C-M1** (ch01-C, CONFIRMED)
- print `01_topological_matter.tex:35` — `Mass is the stored inductive energy required to maintain the topological integrity of the standing wave.`
- KB `newtonian-inertia-as-lenz.md:14` — `> **🔴 STORED INDUCTIVE ENERGY = the FLYWHEEL (spin/frequency-regulation), the REST MASS *store* is A1 (2026-06-20, Rule 12 — body above PRESERVED unedited; Grant-ratified mass-sector ruling).**`
- verifiers: CONFIRMED: Both fragments verified byte-verbatim: TeX 01_topological_matter.tex:35 "Mass is the stored inductive energy required to maintain the topol…

**28. ch01C-M2** (ch01-C, CONFIRMED)
- print `01_topological_matter.tex:33` — `Under the Topo-Kinematic isomorphism, inductance maps to mass ($[L] \equiv [M]$).`
- KB `newtonian-inertia-as-lenz.md:14` — `the **stored inductive energy is the FLYWHEEL** spin / frequency-regulation energy of the T2 / Cosserat micro-rotation ($\omega$) sector`
- verifiers: CONFIRMED: Both fragments verified byte-verbatim: tex 01_topological_matter.tex:33 "Under the Topo-Kinematic isomorphism, inductance maps to mass ($[L…

**29. ch01C-M3** (ch01-C, CONFIRMED)
- print `01_topological_matter.tex:266` — `\item Inertial mass ($m$) is derived classically from distributed continuous inductance ($L$), where acceleration generates a back-EMF (Lenz's Law).`
- KB `newtonian-inertia-as-lenz.md:14` — `the re-scope only re-labels *which sector stores the rest mass* (A1, not the inductive flywheel). Body preserved per Rule-12.`
- verifiers: CONFIRMED: Both fragments verified byte-verbatim: tex 01_topological_matter.tex:266 (my initial grep -nF miscarried on shell-escaping of literal "$m$"…

**30. ch01C-M4** (ch01-C, CONFIRMED)
- print `01_topological_matter.tex:8` — `\item Understand how mass emerges macroscopically from the continuous distributed inductance of closed optical loops (Lenz's Law).`
- KB `newtonian-inertia-as-lenz.md:14` — `**not** the rest-mass *store* — which is the orthogonal **A1 longitudinal DILATATION** depression`
- verifiers: CONFIRMED: Both fragments verified byte-verbatim: tex line 8 (objectivebox bullet, lines 5-11, no caveat anywhere in the box or within 15 lines) and K…

**31. ch01C-M5** (ch01-C, DOWNGRADED)
- print `01_topological_matter.tex:148` — `The minimum discrete diameter of the flux tube is normalised to one fundamental lattice pitch ($d \equiv 1 l_{node}$).`
- KB `common-mode-twist-ledger.md:235` — `> **They differ by $\pi$ on the tube diameter and by $2\pi$ on the circumference. They cannot both be right.**`
- verifiers: DOWNGRADED: Both fragments verify byte-verbatim at the cited lines (tex:148, ledger.md:235). Read tex:100-160 — no printed caveat or comment banner nea…

**32. ch01C-M6** (ch01-C, DOWNGRADED)
- print `01_topological_matter.tex:40` — `undergoes macroscopic \textbf{gyroscopic precession} in the presence of an external magnetic field`
- KB `spin-gyroscopic-isomorphism.md:45` — `(the extended core is $\sim\ell_{node} \approx 3.86\times10^{-13}$ m — subatomic, **not** macroscopic)`
- verifiers: DOWNGRADED: Both fragments verified byte-verbatim: tex 01_topological_matter.tex:40 ("...undergoes macroscopic \textbf{gyroscopic precession} in the pr…

**33. MM-01** (ch02, UNVERIFIED)
- print `02_baryon_sector.tex:319` — `generates a discrete CP-violating $\theta$-vacuum phase`
- KB `topological-fractionalization.md:60` — `The "CP-violating" adjective is UNDERIVED`
- verifiers: 

**34. MM-02** (ch02, UNVERIFIED)
- print `02_baryon_sector.tex:131` — `covers the baryon ladder through crossing number $c = 15$ with maximum error $\sim 2.4\%$`
- KB `torus-knot-ladder-baryons.md:29` — `\| $(2,13)$ \| 13 \| 2194.636 \| $N(2190)$ \| 2100 ± 50 \| $+4.506\%$`
- verifiers: 

**35. MM-03** (ch02, UNVERIFIED)
- print `02_baryon_sector.tex:297` — `$(2,15)$ & 15 & 2478  & $\Delta(2420)$ & 2420  & $+2.40\%$`
- KB `torus-knot-ladder-baryons.md:30` — `\| $(2,15)$ \| 15 \| 2477.968 \| $\Delta(2420)$ \| 2400 ± 100 \| $+3.249\%$`
- verifiers: 

**36. MM-04** (ch02, UNVERIFIED)
- print `02_baryon_sector.tex:314` — `its $+9.8\%$ deviation from $\Delta(2420)$`
- KB `torus-knot-ladder-baryons.md:30` — `\| $(2,15)$ \| 15 \| 2477.968 \| $\Delta(2420)$ \| 2400 ± 100 \| $+3.249\%$`
- verifiers: 

**37. MM-05** (ch02, UNVERIFIED)
- print `02_baryon_sector.tex:131` — `covers the baryon ladder through crossing number $c = 15$ with maximum error $\sim 2.4\%$`
- KB `thermal-softening.md:37` — `validates the baryon ladder through crossing number $c = 15$ with maximum error $2.4\%$`
- verifiers: 

**38. MM-06** (ch02, UNVERIFIED)
- print `02_baryon_sector.tex:357` — `is the proposed structural origin of (and provides an upper-bound estimate for)`
- KB `proton-neutron-mass-split.md:10` — `This elastic expansion tension accounts for the mass surplus the neutron possesses relative to the bare proton`
- verifiers: 

**39. MM-07** (ch02, UNVERIFIED)
- print `02_baryon_sector.tex:357` — `neutron-identification.md} :52`
- KB `neutron-identification.md:52` — `### §2.1 — Why the mass split is structurally bounded`
- verifiers: 

**40. MM-08** (ch02, UNVERIFIED)
- print `02_baryon_sector.tex:362` — `The elastic expansion required to accommodate the threaded electron is the proposed structural origin`
- KB `neutron-identification.md:25` — `accounts for the $1.293$ MeV mass surplus of the neutron over the proton`
- verifiers: 

**41. MM-09** (ch02, UNVERIFIED)
- print `02_baryon_sector.tex:448` — `(:754)`
- KB `proton-neutron-mass-split.md:82` — `per `claim-quality.md` :754`
- verifiers: 

**42. MM-10** (ch02, UNVERIFIED)
- print `02_baryon_sector.tex:165` — `evaluates the scalar component to $\mathcal{I}_{scalar} \approx 1162\,m_e$`
- KB `proton-identification.md:68` — `Documented in `vol2/particle-physics/ch02-baryon-sector/topological-fractionalization.md``
- verifiers: 

**43. MM-11** (ch02, UNVERIFIED)
- print `02_baryon_sector.tex:463` — `The exact proton to electron mass ratio ($1836.15$) is derived`
- KB `proton-identification.md:73` — `THE headline claim is the $+0.74\%$ bare-topology emergence result`
- verifiers: 

**44. MM-12** (ch02, UNVERIFIED)
- print `00_title.tex:18` — `the proton/electron mass ratio ($\approx 1836.14$)`
- KB `proton-identification.md:13` — `the proton's mass ratio $m_p/m_e = 1836.12$ is derived with zero baryon-data-tuned parameters`
- verifiers: 

**45. MM-13** (ch02, UNVERIFIED)
- print `02_baryon_sector.tex:41` — `The $6^3_2$ Borromean knot spans multiple fundamental nodes`
- KB `proton-identification.md:156` — `Disposition: KEEP-BOTH`
- verifiers: 

**46. MM-14** (ch02, UNVERIFIED)
- print `02_baryon_sector.tex:466` — `The Hierarchy Problem is strictly resolved`
- KB `claim-quality.md:789` — `The Hierarchy Bridge is **algebraic substitution**, not an independent derivation of $G$`
- verifiers: 

**47. MM-15** (ch02, UNVERIFIED)
- print `02_baryon_sector.tex:126` — `(\kbleaf{ave-kb/common/theorem-thesaurus.md}`
- KB `thermal-softening.md:25` — `:227, §"Hill — three distinct objects" at :223`
- verifiers: 

**48. MM-16** (ch02, UNVERIFIED)
- print `02_baryon_sector.tex:238` — `derived in Chapter 2`
- KB `self-consistent-mass-oscillator.md:30` — `derived in Chapter 2`
- verifiers: 

**49. M1** (ch03, UNVERIFIED (id shared by 7 slices; verdicts not attributable))
- print `03_neutrino_sector.tex:227` — `\item $\pi$: The base torsional half-turn of the $0_1$ unknot phase winding.`
- KB `delta-cp-violation.md:22` — `the neutrino is an open helix in the torsional sector, *not* a closed unknot phase winding`
- verifiers: 

**50. M2** (ch03, UNVERIFIED (id shared by 7 slices; verdicts not attributable))
- print `03_neutrino_sector.tex:272` — `Neutrinos are structurally defined as $0_1$ twisted unknots. Because they have zero self-crossings, their topological Skyrme gradient vanishes`
- KB `index.md:13` — `Corrigendum (2026-05-06 session): Earlier editions described the neutrino as a "$0_1$ twisted unknot" (closed loop)`
- verifiers: 

**51. M3** (ch03, UNVERIFIED (id shared by 6 slices; verdicts not attributable))
- print `03_neutrino_sector.tex:274` — `Neutrino oscillation is the classical dispersive beat frequency of the three distinct $0_1$ mass eigenstates`
- KB `index.md:13` — `Any remaining "twisted unknot" prose in cross-references should be read as the obsolete framing`
- verifiers: 

**52. M4** (ch03, UNVERIFIED (id shared by 5 slices; verdicts not attributable))
- print `03_neutrino_sector.tex:159` — `the trefoil has $c = 3$ crossings \textit{because} the K4 lattice is 3-connected`
- KB `chiral-screening.md:35` — `Connectivity = trefoil crossing number: ASSERTED -- and in tension with canon`
- verifiers: 

**53. M5** (ch03, UNVERIFIED (id shared by 4 slices; verdicts not attributable))
- print `03_neutrino_sector.tex:250` — `All four PMNS parameters derive from three inputs: the torus knot crossing numbers ($c_1 = 5$, $c_3 = 9$)... No curve fitting is used`
- KB `delta-cp-violation.md:38` — `c_1=5 starting value of mode-space ladder is NOT derived from substrate primitives in any canonical leaf grep'd`
- verifiers: 

**54. M6** (ch03, UNVERIFIED (id shared by 4 slices; verdicts not attributable))
- print `01_topological_matter.tex:207` — `Neutrino ($\nu$)           & Twisted unknot      & I--II boundary & Chiral phase below yield \\`
- KB `index.md:13` — `Any remaining "twisted unknot" prose in cross-references should be read as the obsolete framing`
- verifiers: 

**55. M7** (ch03, UNVERIFIED (id shared by 4 slices; verdicts not attributable))
- print `00_title.tex:14` — `neutrons as dispersive twisted $0_1$ unknots, bound by the Faddeev-Skyrme energy functional`
- KB `index.md:13` — `The closed-loop framing has been **superseded** by the Cosserat torsional screw-dislocation model`
- verifiers: 

**56. M8** (ch03, UNVERIFIED (id shared by 3 slices; verdicts not attributable))
- print `03_neutrino_sector.tex:122` — `the $\nu_3$ baryon-partner label was updated $\Delta(1620) \to \Delta(1600)$`
- KB `claim-quality.md:251` — `$\nu_3$ with $\Delta(1620)$ $(2,9)$`
- verifiers: 

**57. ch04-M1** (ch04, CONFIRMED)
- print `04_quantum_spin.tex:81` — `:407 "Does NOT claim a violation of standard QM predictions`
- KB `claim-quality.md (clm-salw2h):408` — `Does NOT claim a violation of standard QM predictions for spin-dependent observables`
- verifiers: CONFIRMED: TeX comment fragment ":407 \"Does NOT claim a violation of standard QM predictions" verified byte-verbatim at 04_quantum_spin.tex:81 (grep …

**58. ch04-M2** (ch04, CONFIRMED)
- print `04_quantum_spin.tex:111` — `standard QM fails to make. Canonical: \kbleaf{ave-kb/vol2/claim-quality.md} (\texttt{clm-salw2h},`
- KB `larmor-derivation.md:61` — `](../../claim-quality.md):407–410, `clm-salw2h` *Specific Non-Claims and Caveats*; solidity $0.70$ at :419)`
- verifiers: CONFIRMED: Both fragments verified byte-verbatim: TeX 04_quantum_spin.tex:111 (file-level \kbleaf cite, no line number, correctly judged not stale) an…

**59. ch04-M3** (ch04, CONFIRMED)
- print `04_quantum_spin.tex:111` — `standard QM fails to make. Canonical: \kbleaf{ave-kb/vol2/claim-quality.md} (\texttt{clm-salw2h},`
- KB `visual-equivalence.md:22` — `](../../claim-quality.md):407–410, `clm-salw2h` *Specific Non-Claims and Caveats*; solidity $0.70$ at :419)`
- verifiers: CONFIRMED: Both quoted fragments are byte-verbatim at the cited locations (tex 04_quantum_spin.tex:111; leaf visual-equivalence.md:22). Line-by-line c…

**60. ch04-M4** (ch04, CONFIRMED)
- print `04_quantum_spin.tex:62` — `representing the $3_1$ electron knot`
- KB `larmor-derivation.md:10` — `the electron is the $0_1$ unknot in real space`
- verifiers: CONFIRMED: Fragment verbatim-verified at TeX:62 (grep -nF exact match) and at KB larmor-derivation.md:10 (grep -nF exact match), though the finding's …

**61. ch04-M5** (ch04, DOWNGRADED)
- print `04_quantum_spin.tex:94` — `so the scoping currently lives ONLY in the clm-salw2h register and has propagated to neither the`
- KB `larmor-derivation.md:57` — `> **[2026-08-02 — scope of the equivalence, per `clm-salw2h`; KB-lockstep with the merged print correction]**`
- verifiers: DOWNGRADED: Both fragments verify byte-verbatim: TeX 04_quantum_spin.tex:94 "so the scoping currently lives ONLY in the clm-salw2h register and has pro…

**62. ch04-M6** (ch04, CONFIRMED)
- print `04_quantum_spin.tex:6` — `Define Quantum Spin ($1/2\hbar$) structurally as the macroscopic angular momentum`
- KB `index.md:11` — `Quantum Spin ($1/2\hbar$) is derived as the macroscopic angular momentum`
- verifiers: CONFIRMED: All fragments verified byte-verbatim: tex :6 (objectivebox "Define Quantum Spin..."); index.md:11 ("...is derived as the macroscopic angula…

**63. CH05-M1** (ch05, UNVERIFIED)
- print `05_electroweak_gauge_theory.tex:175` — `Gauge Invariance is explicitly derived as the macroscopic consequence of the classical Helmholtz Decomposition`
- KB `gauge-boson-masses.md:34` — `and *not* the full time-dependent U(1) group`
- verifiers: 

**64. CH05-M2** (ch05, UNVERIFIED)
- print `05_electroweak_gauge_theory.tex:8` — `Derive the physical origin of Gauge Invariance (U(1)) as the classical network-dynamic freedom`
- KB `gauge-boson-masses.md:83` — `canon holds **no valid derivation of any full U(1) family**`
- verifiers: 

**65. CH05-M3** (ch05, UNVERIFIED)
- print `05_electroweak_gauge_theory.tex:178` — `$U(1)$ and $SU(3)$ Gauge symmetries are explicitly proven to map identically onto the discrete geometric Plaquette Action`
- KB `gauge-boson-masses.md:83` — `canon holds **no valid derivation of any full U(1) family**`
- verifiers: 

**66. CH05-M4** (ch05, UNVERIFIED)
- print `05_electroweak_gauge_theory.tex:159` — `here derived from the physical structure of the substrate hardware`
- KB `gauge-boson-masses.md:83` — `canon holds **no valid derivation of any full U(1) family**`
- verifiers: 

**67. CH05-M5** (ch05, UNVERIFIED)
- print `05_electroweak_gauge_theory.tex:83` — `Substituting the trace-reversed operating point $\nu_{\text{Hill}} \equiv 2/7$`
- KB `weinberg-angle.md:26` — `Substituting the trace-reversed topological lattice limit $\nu_{vac} \equiv 2/7$:`
- verifiers: 

**68. CH05-M6** (ch05, UNVERIFIED)
- print `05_electroweak_gauge_theory.tex:115` — `not a Feynman two-vertex loop.`
- KB `weak-coupling.md:30` — `The self-energy is a **two-vertex process** (second-order perturbation theory):`
- verifiers: 

**69. CH05-M7** (ch05, UNVERIFIED)
- print `05_electroweak_gauge_theory.tex:103` — `The factor $\alpha^2$ is the product of \textbf{two Axiom~4 susceptibility couplings}.`
- KB `weak-coupling.md:22` — `The factor $\alpha^2$ is derived from the interaction Lagrangian.`
- verifiers: 

**70. CH05-M8** (ch05, UNVERIFIED)
- print `vocabulary-register.md:886` — `The **EM longitudinal** $\nabla\cdot\mathbf{A}$ is **GAUGE**: the curl-only EM Lagrangian gives it no restoring force.`
- KB `gauge-boson-masses.md:34` — `(../../../common/vocabulary-register.md)`:870`, `def-l0ngdu``
- verifiers: 

**71. CH05-M9** (ch05, UNVERIFIED)
- print `vocabulary-register.md:886` — `**One word each way — $\nabla\cdot\mathbf{u}$ propagates; $\nabla\cdot\mathbf{A}$ is gauge.**`
- KB `gauge-boson-masses.md:42` — `(../../../common/vocabulary-register.md)`:867` (`def-l0ngdu`; the quoted clauses below are at `:870`)`
- verifiers: 

**72. CH05-M10** (ch05, UNVERIFIED)
- print `vocabulary-register.md:901` — `are **COUNTERPART SECTOR VARIABLES**`
- KB `gauge-boson-masses.md:48` — `(../../../common/vocabulary-register.md)`:882`, `def-uatk1s`, SOLID 2026-07-21`
- verifiers: 

**73. CH05-M11** (ch05, UNVERIFIED)
- print `05_electroweak_gauge_theory.tex:51` — `[DEMOTED 2026-08-11 --- R40-B2a: NEEDS RE-DERIVATION, not dead; dated note at the end of this file]`
- KB `gauge-boson-masses.md:176` — `- **`:38`** — stamped at `:38`. *(family: K-static vs constitutive-fact; banked `uncertain`)*`
- verifiers: 

**74. CH05-M12** (ch05, UNVERIFIED)
- print `05_electroweak_gauge_theory.tex:33` — `to the mass flow introduces a uniform, irrotational velocity potential to the background network.`
- KB `gauge-boson-masses.md:48` — `The paragraph above still describes $\nabla\Lambda$ as added *"to the mass flow"*, which reads $\mathbf{A}$ as the mechanical momentum field.`
- verifiers: 

**75. CH05-M13** (ch05, UNVERIFIED)
- print `05_electroweak_gauge_theory.tex:35` — `\textbf{This closure holds for time-independent $\Lambda$ ONLY} (rescoped 2026-08-10 under R43; see the second-failure note below)`
- KB `gauge-boson-masses.md:34` — `and *not* the full time-dependent U(1) group`
- verifiers: 

**76. M1** (ch06-A, UNVERIFIED (id shared by 7 slices; verdicts not attributable))
- print `06_electroweak_and_higgs.tex:17` — `corresponds to a transient acoustic mode---a topological node undergoing rapid structural relaxation upon high-energy impact`
- KB `claim-quality.md:162` — `The empirical $125$ GeV LHC resonance is interpreted as a **transient acoustic relaxation mode** of the LC network, not a fundamental scalar field excitation. 🔴 **[DEMOTED 2026-08-11 — R40-B2a: NEEDS…`
- verifiers: 

**77. M2** (ch06-A, UNVERIFIED (id shared by 7 slices; verdicts not attributable))
- print `06_electroweak_and_higgs.tex:363` — `A channel is \emph{compliant} if $\Delta c \le \Delta c_\text{crit} = 3$ --- the K4 lattice connectivity itself (three bonds per node, each transferring at most one torsional unit per interaction), w…`
- KB `chiral-screening.md:35` — `**Connectivity = trefoil crossing number: ASSERTED — and in tension with canon.**`
- verifiers: 

**78. M3** (ch06-A, UNVERIFIED (id shared by 6 slices; verdicts not attributable))
- print `06_electroweak_and_higgs.tex:210` — `$W$    & $M_W^{\text{tree}} / (1 - \|S_{11}^{\text{sc}}\|^2)$  & 80,224 MeV  & 80,379 MeV  & $-0.19\%$ \\`
- KB `lepton-spectrum.md:81` — `\| $W$ \| $m_e/(\alpha^2 p_c \sqrt{3/7})$ \| 79,923 MeV \| 80,379 MeV \| $-0.57\%$ \|`
- verifiers: 

**79. M4** (ch06-A, UNVERIFIED (id shared by 5 slices; verdicts not attributable))
- print `06_electroweak_and_higgs.tex:321` — `$\nu_1$ & $(2,5)$ & 5 &  $0.1324$ & $9.58$ \\`
- KB `higgs-mass.md:29` — `\| $\nu_1$ \| Proton $(2,5)$ \| 5 \| $\sim 24$ \|`
- verifiers: 

**80. M5** (ch06-A, UNVERIFIED (id shared by 4 slices; verdicts not attributable))
- print `06_electroweak_and_higgs.tex:193` — `m_e \xrightarrow{\alpha\sqrt{3/7}} m_\mu \xrightarrow{\alpha \cdot p_c} m_\tau \xrightarrow{\alpha \cdot p_c} M_W`
- KB `lepton-spectrum.md:73` — `m_e \xrightarrow{\text{torsion: }\alpha\sqrt{3/7}} m_\mu \xrightarrow{\text{bending: }p_c/\alpha^2} m_\tau \xrightarrow{\text{+2nd vertex: }\alpha} M_W`
- verifiers: 

**81. M6** (ch06-A, UNVERIFIED (id shared by 4 slices; verdicts not attributable))
- print `sm-ave-translation.md:10` — `Source: `\input{../common/translation_particle_physics.tex}` in `vol_2_subatomic/chapters/06_electroweak_and_higgs.tex`, line 305.`
- KB `06_electroweak_and_higgs.tex:860` — `\input{../common/translation_particle_physics.tex}`
- verifiers: 

**82. M7** (ch06-A, UNVERIFIED (id shared by 4 slices; verdicts not attributable))
- print `higgs-mechanism.md:54` — `<!-- 🔴 OPEN FLAG (Rule 12): the "torsion-shear / PAT" label on $\sqrt{3/7}$ is contested`
- KB `lepton-spectrum.md:29` — `> **🔴 OPEN FLAG (Rule 12 — `√(3/7)` "PAT torsion-shear" label; Grant's physics adjudication pending.`
- verifiers: 

**83. M8** (ch06-A, UNVERIFIED (id shared by 3 slices; verdicts not attributable))
- print `06_electroweak_and_higgs.tex:422` — `Four lemmas are proven from Axioms~1 and~4 (see\linebreak \kbleaf{p2.9b\_goldstone\_proof.md}):`
- KB `verify-md-links.py:808` — `"manuscript/vol_2_subatomic/chapters/06_electroweak_and_higgs.tex",         r"p2.9b\_goldstone\_proof.md",`
- verifiers: 

**84. ch06B-01** (ch06-B, UNVERIFIED)
- print `06_electroweak_and_higgs.tex:516` — `C_2^{\text{AVE}} = \frac{2}{\pi\alpha}\langle (S_d - S_q)\,(-\dot{\Sigma}_{\text{near}})\rangle = -0.32846`
- KB `q-g19a-petermann-saliency-closure.md:179` — `**NOT ADJUDICATED HERE.** Which normalization is substrate-derived is a physics question, **routed to Grant**, open as of this block.`
- verifiers: 

**85. ch06B-02** (ch06-B, UNVERIFIED)
- print `06_electroweak_and_higgs.tex:575` — `with $\tau_{\text{retard}} = 1/\omega_C$ (one Compton-loop transit time,`
- KB `q-g19a-petermann-saliency-closure.md:193` — `> 1. **$\tau_{\text{retard}} = 1/\omega_C$ is asserted, not derived.**`
- verifiers: 

**86. ch06B-03** (ch06-B, UNVERIFIED)
- print `06_electroweak_and_higgs.tex:620` — `is invariant under three independent derivative methods (analytic,`
- KB `q-g19a-petermann-saliency-closure.md:164` — `**Scope note for §"Numerical robustness" above.**`
- verifiers: 

**87. ch06B-04** (ch06-B, UNVERIFIED)
- print `06_electroweak_and_higgs.tex:723` — `(:12/:14 the two-stage split, :92/:100/:103 the values, :121 the postulate-conditional cell).`
- KB `q-g19a-petermann-saliency-closure.md:131` — `*Cite-integrity note: this insertion shifts the line numbers of all content below it.`
- verifiers: 

**88. ch06B-05** (ch06-B, UNVERIFIED)
- print `06_electroweak_and_higgs.tex:770` — `(\kbleaf{ave-kb/vol2/particle-physics/ch06-electroweak-higgs/q-g19a-petermann-saliency-closure.md}:110.)`
- KB `q-g19a-petermann-saliency-closure.md:110` — `> shift_idx = int(tau_retard / dt) % n_t`
- verifiers: 

**89. ch06B-06** (ch06-B, UNVERIFIED)
- print `06_electroweak_and_higgs.tex:777` — `\noindent\textbf{Zero parameters were fudged.} The trefoil $(2,3)$,`
- KB `q-g19a-petermann-saliency-closure.md:242` — `> **No fit parameters — *at Stage 1*.**`
- verifiers: 

**90. ch06B-07** (ch06-B, UNVERIFIED)
- print `06_electroweak_and_higgs.tex:810` — `The Higgs boson is the radial breathing mode of the K4 unit cell.`
- KB `claim-quality.md (register carrier: clm-p7rfkb :162 R40-B2a stamp + R40 batch-2a note :1710-1720; NO leaf carries the stamp — higgs-mechanism.md and vol6 lambda-higgs-derivation.md:26 are unstamped):1717` — `Register row (clm-p7rfkb) recording a bound bulk-oscillation mechanism — the :163 K4-cell BREATHING mode is a dilatational eigenmode requiring the A1 restoring force`
- verifiers: 

**91. ch06B-08** (ch06-B, UNVERIFIED)
- print `06_electroweak_and_higgs.tex:788` — `both $\lambda$ and $v$ are derived quantities---not free parameters`
- KB `lambda-higgs-derivation.md:12` — `The SM Higgs is a **FORM-identification** onto that grade, **not** a VALUE-derivation`
- verifiers: 

**92. ch06B-09** (ch06-B, UNVERIFIED)
- print `06_electroweak_and_higgs.tex:833` — `(\texttt{constants.py}, line 338)`
- KB `constants.py (engine file cited via \kbleaf, not a KB leaf):679` — `M_HIGGS_MEV: float = HIGGS_VEV_MEV / np.sqrt(N_K4)`
- verifiers: 

**93. ch06B-10** (ch06-B, UNVERIFIED)
- print `06_electroweak_and_higgs.tex:860` — `\input{../common/translation_particle_physics.tex}`
- KB `sm-ave-translation.md:10` — `in `vol_2_subatomic/chapters/06_electroweak_and_higgs.tex`, line 305.`
- verifiers: 

**94. ch06B-11** (ch06-B, UNVERIFIED)
- print `index.md (KB-INTERNAL: 'tex' side here is the derived index):36` — `4% forward → 10 ppm with postulate`
- KB `q-g19a-petermann-saliency-closure.md:14` — `**[ppm labels struck 2026-08-03 per Grant ruling — see the ppm-strike block below]**`
- verifiers: 

**95. ch06B-12** (ch06-B, UNVERIFIED)
- print `q-g27-muon-cosserat-saliency.md (KB-INTERNAL: leaf vs sibling leaf):57` — `$$\delta^{\mu} = -\frac{3\alpha}{2} - \frac{\alpha\sqrt{3/7}}{2\pi}$$`
- KB `q-g19a-petermann-saliency-closure.md:221` — `So $\delta = -3\alpha/2$ is a **1-point fit**, not a winding law`
- verifiers: 

**96. ch06B-13** (ch06-B, UNVERIFIED)
- print `q-g20f-vacuum-polarization.md (KB-INTERNAL: leaf vs sibling leaf):97` — `electron anomalous moment matches QED at 50 ppm precision`
- KB `q-g19a-petermann-saliency-closure.md:196` — `**No ppm number replaces the struck ones — not even the converged 60.**`
- verifiers: 

**97. ch06B-14** (ch06-B, UNVERIFIED)
- print `q-g27-muon-cosserat-saliency.md (KB-INTERNAL: leaf vs sibling leaf):80` — `the 50 ppm figure is conditional on the $n_q$-additivity postulate`
- KB `q-g19a-petermann-saliency-closure.md:196` — `**No ppm number replaces the struck ones — not even the converged 60.**`
- verifiers: 

**98. ch06B-15** (ch06-B, UNVERIFIED)
- print `claim-quality.md (KB-INTERNAL: derived register vs leaf; clm-v2sg8z):1443` — `gives $C_2 = -0.32846$ → 50 ppm at $C_2$ / ≈10 ppm at $a_e$ total.`
- KB `q-g19a-petermann-saliency-closure.md:221` — `So $\delta = -3\alpha/2$ is a **1-point fit**, not a winding law`
- verifiers: 

**99. ch07A-M1** (ch07-A, UNVERIFIED)
- print `07_quantum_mechanics_and_orbitals.tex:277` — `the AVE engine evaluates Beryllium's total ionization energy to \textbf{9.32 eV} entirely free of empirical parameters or tuning coefficients`
- KB `hierarchical-cascade-correction.md:54` — `IE_\text{Be, AVE} = 9.28\;\text{eV} \quad (\text{exp: } 9.322\;\text{eV}, \quad \Delta = -0.45\%)`
- verifiers: 

**100. ch07A-M2** (ch07-A, UNVERIFIED)
- print `07_quantum_mechanics_and_orbitals.tex:324` — `predicting Boron's tightly bound $9.4$~eV Ionization Energy dynamically without fitting parameters`
- KB `subshell-junction-scattering.md:11` — `its ionization energy drops precipitously from Beryllium ($9.32$ eV) to $8.30$ eV`
- verifiers: 

**101. ch07A-M3** (ch07-A, UNVERIFIED)
- print `07_quantum_mechanics_and_orbitals.tex:220` — `suffers an exact $1/d$ impedance mismatch scattering (Op3 boundary), stripping its native resonance`
- KB `orbital-penetration-penalties.md:29` — `This penalty lowers the eigenfrequency of the penetrating mode (stronger binding).`
- verifiers: 

**102. ch07A-M4** (ch07-A, UNVERIFIED)
- print `07_quantum_mechanics_and_orbitals.tex:243` — `The isolated $s^2$ shell loads structurally not as $2.0$, but perfectly as $N_{eff} = 1.0 + 0.5 = 1.5$.`
- KB `helium-symmetric-cavity.md:34` — `Compressional $s$-orbitals load fully ($N_s = 1.0$), while transversal $p$-orbitals load exactly at half-efficiency ($N_p = 0.5$)`
- verifiers: 

**103. ch07A-M5** (ch07-A, UNVERIFIED)
- print `07_quantum_mechanics_and_orbitals.tex:333` — `The folding engine achieves Tier-1 derivation status organically`
- KB `program-arc-map.md:371` — `\| N13 \| **Protein impedance-folding** (impedance carries the fold) \| NEGATIVE (all EE-reflection channels dead)`
- verifiers: 

**104. ch07A-M6** (ch07-A, UNVERIFIED)
- print `07_quantum_mechanics_and_orbitals.tex:488` — `strictly past the structural \textbf{Regime IV Yield Limit}`
- KB `de-broglie-n.md:10` — `the nuclear voltage $V/V_{\text{yield}} \sim Z\alpha^2 \approx 10^{-4}$ places the entire atom in the linear regime (Axiom 4 check)`
- verifiers: 

**105. ch07A-M7** (ch07-A, UNVERIFIED)
- print `07_quantum_mechanics_and_orbitals.tex:726` — `standing wave on the flux ring---a topological invariant,`
- KB `de-broglie-standing-wave.md:240` — `a **cavity-deformable** embedding count that *ionization destroys*. This is **NOT** the topologically-protected $(2,3)$ **winding**`
- verifiers: 

**106. ch07A-M8** (ch07-A, UNVERIFIED)
- print `07_quantum_mechanics_and_orbitals.tex:46` — `the spatial coordinate metric ($n_s = \frac{9}{7}\varepsilon_{11}$)`
- KB `de-broglie-standing-wave.md:58` — `($n_s = 1 + \tfrac{9}{7}\varepsilon_{11}$)`
- verifiers: 

**107. ch07A-M9** (ch07-A, UNVERIFIED)
- print `07_quantum_mechanics_and_orbitals.tex:39` — `they are perfectly impedance-matched to empty space ($Z = 377 \ \Omega$)`
- KB `de-broglie-standing-wave.md:50` — `A **gravity wave** is a transverse **shear** wave with impedance $Z_{shear} = \rho\,c_{shear}$ (a *different* value)`
- verifiers: 

**108. ch07A-M10** (ch07-A, UNVERIFIED)
- print `07_quantum_mechanics_and_orbitals.tex:383` — `\textbf{[DEMOTED 2026-08-11 --- R40-B2a: NEEDS RE-DERIVATION, not dead; dated note at the end of this file]}`
- KB `analog-ladder-filter.md:52` — `This is *not* 377 $\Omega$. The electron interacts with the vacuum's bulk modulus (acoustic impedance), not the shear modulus (electromagnetic impedance).`
- verifiers: 

**109. ch07A-M11** (ch07-A, UNVERIFIED)
- print `07_quantum_mechanics_and_orbitals.tex:41` — `\textbf{[DEMOTED 2026-08-11 --- R40-B2a: NEEDS RE-DERIVATION, not dead; dated note at the end of this file]}`
- KB `de-broglie-standing-wave.md:267` — `## R40 batch-2a — [NEEDS-RE-DERIVATION status-note heading] (2026-08-11)`
- verifiers: 

**110. ch07A-M12** (ch07-A, UNVERIFIED)
- print `07_quantum_mechanics_and_orbitals.tex:173` — `$r < a_0$ (inner core) & II (Yield) & $V_{local} \sim V_{yield}$; strong confinement \\`
- KB `ode-verification.md:49` — `\| $r < a_0$ (inner core) \| II (Yield) \| $V_{local} \sim V_{yield}$; strong confinement \|`
- verifiers: 

**111. ch07-B-M1** (ch07-B, UNVERIFIED)
- print `07_quantum_mechanics_and_orbitals.tex:1446` — `\text{IE} = 78.79 - 54.42 = 24.37\,\text{eV}$. \checkmark`
- KB `macro-cavity-saturation.md:10` — `However, these methods have been formally superseded by the **Mutual Cavity Loading** architecture (detailed in the helium section).`
- verifiers: 

**112. ch07-B-M2** (ch07-B, UNVERIFIED)
- print `07_quantum_mechanics_and_orbitals.tex:1314` — `Stage D: Y-Matrix Assembly (Axiom~1, Kirchhoff).`
- KB `index.md:45` — `Supersession of N-port Y-matrix by mutual cavity loading`
- verifiers: 

**113. ch07-B-M3** (ch07-B, UNVERIFIED)
- print `07_quantum_mechanics_and_orbitals.tex:1965` — `& Radiating aperture & Chiral Antenna \\`
- KB `radial-eigenvalue-solver.md:177` — `\| Antenna \| Coaxial feed \| Radiating aperture \| HOPF-01 \|`
- verifiers: 

**114. M1** (ch07-C, UNVERIFIED (id shared by 7 slices; verdicts not attributable))
- print `07_quantum_mechanics_and_orbitals.tex:3288` — `N_{\rm Hopf} \times \frac{P_C}{2} \times (-1)^{n - l - 1}`
- KB `radial-eigenvalue-solver.md:731` — `\kappa_{\rm Hopf}(r) = N_{\rm Hopf} \times \frac{P_C}{2} \times \sigma_{\rm partner}(r)`
- verifiers: 

**115. M2** (ch07-C, UNVERIFIED (id shared by 7 slices; verdicts not attributable))
- print `07_quantum_mechanics_and_orbitals.tex:3323` — `\textbf{Inductive Drag} ($+\kappa$), decreasing`
- KB `radial-eigenvalue-solver.md:741` — `This is *not* a potential in $V_{\rm eff}$---it enters the *denominator* of $k^2(r)$.`
- verifiers: 

**116. M3** (ch07-C, UNVERIFIED (id shared by 6 slices; verdicts not attributable))
- print `07_quantum_mechanics_and_orbitals.tex:3306` — `same-$n$ co-radial partners), with`
- KB `radial-eigenvalue-solver.md:739` — `(including same-$n$ co-radial partners)`
- verifiers: 

**117. M4** (ch07-C, UNVERIFIED (id shared by 5 slices; verdicts not attributable))
- print `07_quantum_mechanics_and_orbitals.tex:2728` — `Both are needed for multi-electron atoms:`
- KB `dual-formalism-architecture.md:21` — `> Both are needed for multi-electron atoms:`
- verifiers: 

**118. M5** (ch07-C, UNVERIFIED (id shared by 4 slices; verdicts not attributable))
- print `07_quantum_mechanics_and_orbitals.tex:3136` — `Li & 3 & P3 + Op2 (ABCD taper) &`
- KB `radial-eigenvalue-solver.md:689` — `\| Li \| 3 \| P3 + Op2 (ABCD taper) \| 5.32 \| $1.2\%$ \|`
- verifiers: 

**119. M6** (ch07-C, UNVERIFIED (id shared by 4 slices; verdicts not attributable))
- print `07_quantum_mechanics_and_orbitals.tex:3138` — `Be & 4 & P3 + P2 (ABCD + Hopf) &`
- KB `radial-eigenvalue-solver.md:690` — `\| Be \| 4 \| P3 + P2 (ABCD + Hopf) \| 8.21 \| $11.9\%$ \|`
- verifiers: 

**120. M7** (ch07-C, UNVERIFIED (id shared by 4 slices; verdicts not attributable))
- print `07_quantum_mechanics_and_orbitals.tex:3134` — `He & 2 & P2 (circuit, Hopf link) &`
- KB `radial-eigenvalue-solver.md:688` — `\| He \| 2 \| P2 (circuit, Hopf link) \| 24.37 \| $0.9\%$ \|`
- verifiers: 

**121. M1** (ch07-D, UNVERIFIED (id shared by 7 slices; verdicts not attributable))
- print `07_quantum_mechanics_and_orbitals.tex:3529` — `The agreement is a \emph{coincidence of two numbers}, not an independent confirmation:`
- KB `scale-separation.md:49` — `confirmed independently by the elastic modulus ratio $G/K = 1/2$ (since $K = 2G$ from $\nu = 2/7$, Axiom 2), giving a reduced coupling:`
- verifiers: 

**122. M2** (ch07-D, UNVERIFIED (id shared by 7 slices; verdicts not attributable))
- print `07_quantum_mechanics_and_orbitals.tex:3496` — `(Eq.~\ref{eq:crossing_angle}).  No correction factors.  One phase integral.  One eigenvalue.`
- KB `claim-quality.md:393` — `the leaf explicitly states "Be and B remain open: the corrections are applied *outside* the phase integral, violating the action principle" (radial-eigenvalue-solver.md §E2j). The complete-phase-inte…`
- verifiers: 

**123. M3** (ch07-D, UNVERIFIED (id shared by 6 slices; verdicts not attributable))
- print `07_quantum_mechanics_and_orbitals.tex:3654` — `at the $K=2G$ operating point (form-derived, \emph{value} GR-imported; not an axiom of this framework --- see the note at the $p$-shell orthogonal-coupling derivation)`
- KB `subshell-junction-scattering.md:38` — `its interactions are rigorously governed by the **Topological Subshell Impedance Cascade** ($K=2G$). Its mutual admittance to the $2s$ electrons explicitly drops by exactly half`
- verifiers: 

**124. M4** (ch07-D, UNVERIFIED (id shared by 5 slices; verdicts not attributable))
- print `07_quantum_mechanics_and_orbitals.tex:4027` — `3  & Li &  5.525 &  5.392 & $+2.46\%$ & --- \\`
- KB `claim-quality.md:349` — `Lithium ($Z = 3$) currently lists $+2.46\%$ in the validation table but the corrected ABCD-taper-plus-Op2 pipeline elsewhere in the same chapter reports $-1.2\%$.`
- verifiers: 

**125. M1** (ch09, UNVERIFIED (id shared by 7 slices; verdicts not attributable))
- print `09_computational_proof.tex:92` — `catalog text reported the observational target $2.49 \times 10^{-9}$`
- KB `anomaly-catalog.md:15` — `**Muon $g-2$:** $\Delta a_\mu = 2.49 \times 10^{-9}$. AVE predicts a vacuum self-energy correction from lattice topology.`
- verifiers: 

**126. M2** (ch09, UNVERIFIED (id shared by 7 slices; verdicts not attributable))
- print `09_computational_proof.tex:56` — `previously printed ``sub-3 \AA'' in the Agreement column. Per the truth-source`
- KB `computational-graph.md:30` — `\| Protein folding (CLN025) \| RMSD = 2.59 A \| I \| sub-3 A \| 0 \|`
- verifiers: 

**127. M3** (ch09, UNVERIFIED (id shared by 6 slices; verdicts not attributable))
- print `09_computational_proof.tex:249` — `couple exclusively as discrete geometric LC resonators subject to the $8\pi\alpha$ spatial packing fraction and to the $K = 2G$ operating point --- the latter form-derived but \emph{value} GR-importe…`
- KB `methodological-contamination.md:71` — `Electrons within the same principal shell ($n$) couple exclusively as discrete geometric LC resonators subject to the $K = 2G$ topological limit and the $8\pi\alpha$ spatial packing fraction.`
- verifiers: 

**128. M1** (ch10, UNVERIFIED (id shared by 7 slices; verdicts not attributable))
- print `10_open_problems.tex:320` — `The derivation $g_* = 7^3/4 = 85.75$ disagrees with the Standard`
- KB `g-star-prediction.md:10` — `Provenance caveat 2026-08-18, Wave-2 D15b rider: the `/7` in this expression rides the canon G MIXED `/7` FORM — form-derived, value-imported per the FORM-deriving/VALUE-importing meta-finding (PRs #…`
- verifiers: 

**129. M2** (ch10, UNVERIFIED (id shared by 7 slices; verdicts not attributable))
- print `10_open_problems.tex:419` — `Baryon asymmetry & $\eta = \delta_{CP} \alpha_W^4 C_{sph}/g_*$ & 0.79\% (OOM) & \textbf{Consistency-check}`
- KB `quantitative-resolutions.md:15` — `\| Baryon asymmetry \| $\eta = \delta_{CP} \alpha_W^4 C_{sph}/g_*$ \| 0.38% \| **Solved** \| <!-- claim-quality: clm-4vwsjc -->`
- verifiers: 

**130. ch11-M1** (ch11, UNVERIFIED)
- print `11_standard_model_overdrive.tex:66` — `Seconds on a single core, versus months on a supercomputer for Lattice QCD at comparable accuracy.`
- KB `claim-quality.md:604` — `Does NOT claim AVE replaces Lattice QCD or AlphaFold in their respective production roles. The comparison is methodological (scaling, free parameters), not a head-to-head accuracy benchmark.`
- verifiers: 

**131. ch11-M2** (ch11, UNVERIFIED)
- print `11_standard_model_overdrive.tex:123` — `The universe is structurally scale-invariant.`
- KB `program-arc-map.md:371` — `NEGATIVE (all EE-reflection channels dead) — **cross-repo (AVE-Protein lane); Core walk-back STAGED, B4 row may be STALE** `[PARTIAL-RECEIPT]``
- verifiers: 

**132. MM-1** (ch12-mp, UNVERIFIED)
- print `12_the_millennium_prizes.tex:112` — `So $2\,\omega_C$ \emph{understates} the true UV band edge by $\approx 2.7\times$ (canonical: \kbleaf{ave-kb/vol1/.../srs-band-structure.md}, \texttt{clm-bnd5rq}).`
- KB `yang-mills-steps1-2.md:30` — `This imposes a hard ultraviolet cutoff at $\omega_\mathrm{max} = 2c/\ell_\mathrm{node}$. No mode can oscillate faster, eliminating UV divergence.`
- verifiers: 

**133. ch12fp-01-os5-lightest-defect-contra** (ch12-fp, UNVERIFIED)
- print `12_appendix_formal_proofs.tex:170` — `where $c_\mathrm{min} = 3$ (trefoil) is the lightest stable topological`
- KB `yang-mills-steps1-2.md:46` — `The *simplest* topological defect on the lattice is the unknot ($0_1$) --- a single closed electromagnetic flux loop whose minimum circumference is $\ell_\mathrm{node}$. Its rest energy defines the m…`
- verifiers: 

**134. ch12fp-02-ym-os-reconstruction-overclaim** (ch12-fp, UNVERIFIED)
- print `12_appendix_formal_proofs.tex:197` — `Has mass gap $\Delta = m_e c^2 > 0$ (inherited from the lattice).`
- KB `yang-mills-steps1-2.md:10` — `Osterwalder–Schrader reconstruction requires Schwinger functions defined continuously on $\mathbb{R}^4$ which AVE does not provide.`
- verifiers: 

**135. ch12fp-03-ns-smoothness-overclaim** (ch12-fp, UNVERIFIED)
- print `12_appendix_formal_proofs.tex:280` — `lattice Navier-Stokes system has a unique global smooth solution`
- KB `navier-stokes-prize.md:10` — `The AVE "proof" relies on TWO deviations from the Clay formulation: (i) **fixed lattice spacing ℓ_node ≈ 386 fm** = UV cutoff (Clay problem explicitly requires NO UV cutoff; with cutoff, regularity i…`
- verifiers: 

**136. ch12fp-04-rh-zerofree-overclaim** (ch12-fp, UNVERIFIED)
- print `12_appendix_formal_proofs.tex:357` — `All non-trivial zeros of $\zeta(s)$ satisfy $\mathrm{Re}(s) = 1/2$, i.e.,`
- KB `riemann-hypothesis.md:10` — `The lattice spectral-ζ identification is suggestive structural analogy; it should NOT be cited as proving the Riemann Hypothesis.`
- verifiers: 


---

## §3 — Electron-identity corpse pass (F-C1 … F-C11, K4, K6) — vol2 slice

Per-row counts over the slices read so far; 'slices reporting zero hits' is the read receipt for that row in that slice (a full read, not a grep). **No row is discharged by this table** (16 of 175 documents).

| row | live-wrong | Q1 | fence-excluded | Q2 | slices reporting zero hits |
|---|---:|---:|---:|---:|---|
| F-C1 | 0 | 0 | 1 | 0 | ch01-A, ch01-B, ch01-C, ch02, ch03, ch04, ch05, ch06-A, ch07-A, ch07-B, ch07-C, ch07-D, ch08, ch09, ch10, ch11, ch12-mp, ch12-fp |
| F-C2 | 0 | 0 | 0 | 0 | ch01-A, ch01-B, ch01-C, ch02, ch03, ch04, ch05, ch06-A, ch06-B, ch07-A, ch07-B, ch07-C, ch07-D, ch08, ch09, ch10, ch11, ch12-mp, ch12-fp |
| F-C3 | 0 | 0 | 1 | 0 | ch01-A, ch01-B, ch02, ch03, ch04, ch05, ch06-A, ch06-B, ch07-A, ch07-B, ch07-C, ch07-D, ch08, ch09, ch10, ch11, ch12-mp, ch12-fp |
| F-C4 | 0 | 0 | 0 | 0 | ch01-A, ch01-B, ch01-C, ch02, ch03, ch04, ch05, ch06-A, ch06-B, ch07-A, ch07-B, ch07-C, ch07-D, ch08, ch09, ch10, ch11, ch12-mp, ch12-fp |
| F-C5 | 0 | 0 | 1 | 0 | ch01-B, ch01-C, ch02, ch03, ch04, ch05, ch06-A, ch06-B, ch07-A, ch07-B, ch07-C, ch07-D, ch08, ch09, ch10, ch11, ch12-mp, ch12-fp |
| F-C6 | 0 | 0 | 0 | 0 | ch01-A, ch01-B, ch01-C, ch02, ch03, ch04, ch05, ch06-A, ch06-B, ch07-A, ch07-B, ch07-C, ch07-D, ch08, ch09, ch10, ch11, ch12-mp, ch12-fp |
| F-C7 | 2 | 6 | 7 | 0 | ch03, ch04, ch05, ch06-A, ch06-B, ch07-A, ch07-B, ch07-C, ch07-D, ch08, ch09, ch10, ch11, ch12-mp, ch12-fp |
| F-C8 | 0 | 2 | 3 | 0 | ch03, ch04, ch05, ch06-A, ch06-B, ch07-A, ch07-B, ch07-C, ch07-D, ch08, ch09, ch10, ch11, ch12-mp, ch12-fp |
| F-C9 | 0 | 0 | 6 | 0 | ch01-B, ch01-C, ch02, ch03, ch04, ch06-A, ch06-B, ch07-A, ch07-B, ch07-C, ch07-D, ch08, ch09, ch10, ch11, ch12-mp, ch12-fp |
| F-C10 | 0 | 0 | 0 | 0 | ch01-A, ch01-B, ch01-C, ch02, ch03, ch04, ch05, ch06-A, ch06-B, ch07-A, ch07-B, ch07-C, ch07-D, ch08, ch09, ch10, ch11, ch12-mp, ch12-fp |
| F-C11 | 0 | 2 | 0 | 0 | ch01-B, ch02, ch03, ch04, ch05, ch06-A, ch06-B, ch07-A, ch07-B, ch07-C, ch07-D, ch08, ch09, ch10, ch11, ch12-mp, ch12-fp |
| K4 | 3 | 8 | 2 | 0 | ch02, ch03, ch04, ch05, ch06-A, ch06-B, ch07-B, ch07-C, ch07-D, ch08, ch09, ch10, ch11, ch12-mp, ch12-fp |
| K6 | 2 | 2 | 21 | 0 | ch03, ch05, ch06-A, ch07-B, ch07-D, ch08, ch09, ch10, ch11, ch12-mp, ch12-fp |

#### Hits

- **F-C1** · fence-excluded · kb `q-g19a-petermann-saliency-closure.md:18` — `CMB-velocity phase-lock` — Lexical homonym only: a DAMA annual-modulation 'phase-lock' (itself struck [CMB-PHASE-EXCLUDED] 2026-07-04 on the same line), not the electron-identity 'dynamical lock' corpse. Recorded so the row is not reported as an …
- **F-C3** · fence-excluded · tex `01_topological_matter.tex:109` — `of $\mathcal{M}, \mathcal{Q}, \mathcal{J}$ for any field; the v14` — Only engine-version string in the chapter. It reports what a named seed's boundary invariants evaluate to ($\mathcal{M}>0$, $\mathcal{Q}=1$, $\mathcal{J}\approx0$) via boundary_invariants.py — a readout, not a ranked pl…
- **F-C5** · fence-excluded · tex `01_topological_matter.tex:110` — `breathing-soliton seed gives $\mathcal{M} > 0$, $\mathcal{Q} = 1$,` — Adjudicated per slice-instruction (b). This is the row's own fence — a circuit/engine model reporting M, Q, J for a seed WITHOUT selling a genesis-cook: no energize-lock, no Level-2 remanence, no vN target/charter langu…
- **F-C7** · live-wrong · verifier: CONFIRMED · tex `01_topological_matter.tex:259` — `how a propagating Transverse EM Wave winds into a stationary Spin-1 helical loop when encountering extreme localised network impedance ($Z \to Z_{crit}$) ... e…` — [fragment is an elided quotation of one printed caption line — the two halves are byte-verbatim at :259, the ellipsis replaces 'The discrete sequential excitation of the substrate LC nodes guarantees charge containment,… — CONFIRMED: Fragment is byte-verbatim at 01_topological_matter.tex:259 (both quoted halves match; grep -nF confirms). Read lines 220-290 of the tex: no… / CONFIRMED: Both quoted fragment halves are byte-verbatim at manuscript/vol_2_subatomic/chapters/01_topological_matter.tex:259 (grep -nF confirms …
- **F-C7** · fence-excluded · tex `01_topological_matter.tex:167` — `The electron's \emph{existence} is held independently by the transverse-Cosserat ($T_2$) charge/spin $\Gamma = -1$\gammaundeclared{} self-trap wall at $V_{yiel…` — This is the row's explicit fence: the BOUNDARY $\Gamma=-1$ / $V_{yield}$ self-trap wall is the SURVIVING localizer, not the corpse. Print even states the A1 core sits sub-saturated at $A=\sqrt{\alpha}$ INSIDE it, matchi…
- **F-C7** · Q1 · kb `electron-identification.md:13` — `The bulk-interior-mode route is the **FALSIFIED** one (Cartesian-grid artifact); localization is **topological/boundary**` — Dated 2026-06-24 Rule-12 banner naming the bulk self-trap dead with its result doc; body preserved.
- **F-C7** · Q1 · kb `electron-identification.md:64` — `The genesis / self-lock arc that would *dynamically create* the fluxoid from a free precursor is **closed-negative** (electron-genesis-from-free-precursor lean…` — Names the free-precursor genesis route dead in the leaf body. This is the authority M8 cites.
- **F-C7** · Q1 · kb `electron-unknot.md:13` — `NOT a bulk self-focusing well — the bulk self-trap is a Cartesian artifact, RULED OUT by Stage-2 Mode-III` — Dated 2026-06-24 inline Rule-12 scope note on the 'permanently trapping the energy' clause; names the corpse dead.
- **F-C7** · Q1 · kb `l3-electron-soliton-synthesis.md:273` — `**(α) Continuum-limit-only**: the $(2, 3)$ corpus electron exists as a continuum-limit object that the discrete K4-TLM engine at N=32 cannot host. N=128+ might…` — Branch-(alpha) body = the bulk/continuum self-hosting route. Preserved verbatim under Rule 12 with the dated 🔴 kill banner immediately below at :275. Named as dead at the site.
- **F-C7** · Q1 · kb `l3-electron-soliton-synthesis.md:275` — `the bulk self-trap is a **Cartesian-grid artifact**` — Dated close (2026-06-24, Rule 12): the BULK self-trap is named an artifact and localization is redirected to 'topological/coupling (the (2,3) winding + H_couple) + the Γ=−1 boundary cavity' — i.e. the F-C7 fence object.…
- **F-C7** · Q1 · kb `l3-electron-soliton-synthesis.md:277` — `🟡 **EVIDENTIARY-EXPOSURE POINTER (2026-07-03, verdict-exposure sweep — status-demotion, NOT retraction).**` — Dated status-demotion (2026-07-03) that RE-OPENS the branch-(alpha) refutation pending the srs-z3 re-run. It is a bannered, dated status note, not an offer of bulk self-trap as the current route — so Q1, but note it lea…
- **F-C7** · live-wrong · verifier: UNVERIFIED · kb `l3-electron-soliton-synthesis.md:314` — `2. **N=128+ lattice escalation** — tests Branch (α) continuum-limit hypothesis.` — 'Open framework-level work (post-L3 closure)' list item 2 offers the N=128+ bulk-hosting escalation as a current next thing to do, with NO superseded marker and no pointer to the 🔴 banner 39 lines above at :275. A reade…
- **F-C7** · fence-excluded · tex `01_topological_matter.tex:167` — `the transverse-Cosserat ($T_2$) charge/spin $\Gamma = -1$` — This is the BOUNDARY Γ=-1 / V_yield self-trap wall — explicitly the surviving localizer per the F-C7/F-C8 fence. Print also names the A1 mass core as sub-saturated at A=sqrt(alpha) inside it, matching pair-production-ax…
- **F-C7** · fence-excluded · tex `01_topological_matter.tex:191` — `the self-formed $\Gamma=-1$` — Figure caption: 19 wall nodes at yield (A>0.9, S->0.045) forming the self-formed Γ=-1 TIR cage wall on the srs net. This is the amplitude-rail boundary wall (Wall-A role 2 per substrate-perspective-electron.md:139-142),…
- **F-C7** · fence-excluded · kb `pair-production-axiom-derivation.md:102` — `the **transverse Cosserat ($T_2$) sector self-traps.**` — The T2 self-trap at V_yield is the boundary Γ=-1 wall the fence holds out; the leaf explicitly distinguishes it from the longitudinal A1 channel. Not the corpse.
- **F-C7** · fence-excluded · tex `01_topological_matter.tex:167` — `self-trap wall at $V_{yield}$` — This is the BOUNDARY $\Gamma=-1$ / $V_{yield}$ transverse-Cosserat ($T_2$) self-trap — named verbatim in the F-C7/F-C8 fence as the SURVIVING localizer. No bulk self-trap and no free-precursor seed is offered; the same …
- **F-C7** · fence-excluded · kb `q-g18-schwinger-pair-wkb.md:35` — `the probability of reaching the $\Gamma = -1$ wall at $A = 1$` — The surviving boundary localizer used as the tunneling target for pair nucleation — not a bulk self-trap and not a staged seed-photon-to-self-trap growth path. Fence applies.
- **F-C7** · fence-excluded · kb `proton-identification.md:160` — `the flux tube as the clipped equilibrium locus at the yield boundary` — Route C (2026-08-23 third arm) is the V_yield BOUNDARY locus -- the surviving-localizer homonym named in the fence -- registered as a candidate ontology only, with its neutrality/minimum-N uses 'adversarially refuted' (…
- **F-C8** · fence-excluded · tex `01_topological_matter.tex:191` — `the self-formed $\Gamma=-1$\gammaundeclared{} TIR cage wall (\S\ref{sec:hollow_vortex_binding}; the transverse-Cosserat $T_2$ self-trap of the vacuum-circuit s…` — Same surviving-homonym fence as F-C7: boundary TIR cage, engine-exact statics readout. No longitudinal-bulk wall and no constitutive-loop/remanence capability is offered. Caption is the twin of electron-identification.m…
- **F-C8** · Q1 · kb `mass-closure-theorem.md:24` — `Any reading of the Step-2 "constructively interferes into a standing-wave loop" as a **bulk self-focused interior mode** is the **FALSIFIED route**` — Dated 2026-06-24 Rule-12 closure-mechanism scoping with body preserved; the $mc^2=E_{reactive}$ identity is explicitly carved out as untouched. No remanence/constitutive-loop capability is offered anywhere in this leaf.
- **F-C8** · Q1 · tex `01_topological_matter.tex:152` — `the melted vacuum is incompressible, the bulk-compression restoring term is deleted` — Print itself names the bulk-compression soliton route as deleted ('this is a *cavity* balance (Laplace pressure versus circulation), not a bulk-compression soliton'), which is the F-C8 'rest mass = self-trapped LONGITUD…
- **F-C8** · fence-excluded · tex `01_topological_matter.tex:191` — `the transverse-Cosserat $T_2$ self-trap of the vacuum-circuit sector` — Figure caption; same homonym as 01:167 — the self-formed $\Gamma=-1$ TIR cage wall at yield. No 'rest mass = self-trapped LONGITUDINAL-bulk wall' and no constitutive-loop / remanence capability is offered. Fence applies.
- **F-C8** · fence-excluded · kb `proton-identification.md:168` — `rest mass = the A1 longitudinal-dilatation depression` — Lexical match on 'longitudinal' only. This is the PR#260/#311 'mass = A1' sector-ownership ruling applied to baryons (A1 ⊥ T2; X_L = flywheel, not rest-mass store), dated 2026-07-19. No self-trap, no bulk-wall, no reman…
- **F-C9** · fence-excluded · kb `hollow-vortex-binding.md:104` — `and NOT the genesis-v5 seed value $\Gamma=80.75$. Do not cross-wire the two $\Gamma$'s.` — Homonym guard: the surviving object is the Kelvin circulation $\Gamma=\oint u\cdot dl$; the genesis-v5 seed value is named only to exclude it. The leaf's §4 trail additionally lists the five existence routes with their …
- **F-C9** · fence-excluded · tex `05_electroweak_gauge_theory.tex:35` — `leaves every winding and linking integer unchanged` — 'winding' here is the topological/charge-integer dictionary sense (static Link winding stands), not (2,3) self-assembly or a dynamical mass-pin (K6). Grep-term homonym only.
- **F-C9** · fence-excluded · tex `05_electroweak_gauge_theory.tex:51` — `and of every winding/linking integer follows from` — Same topological-integer homonym; no manufacture/genesis path offered.
- **F-C9** · fence-excluded · tex `05_electroweak_gauge_theory.tex:171` — `which flux loop carries the dominant phase winding` — Colour label = phase-winding permutation label; charge/winding dictionary sense, not the corpse.
- **F-C9** · fence-excluded · kb `gauge-boson-masses.md:34` — `leaves every winding and linking integer unchanged` — Byte-twin of TeX:35; same homonym.
- **F-C9** · fence-excluded · kb `forward-to-ch6.md:52` — `which flux loop carries the dominant phase winding` — Byte-twin of TeX:171; same homonym.
- **F-C11** · Q1 · kb `electron-identification.md:15` — `the **(2,3) winding RIDES the cage as STATIC charge** (`Link(∂Ω,F)∈ℤ`, un-walked-back), it does **not** pin the mass.` — Dated 2026-06-24 second-pass Rule-12 localizer relabel; names both dynamical loci NEGATIVE (#415/#417) and preserves the un-walked-back static-Link dictionary (the row's fence).
- **F-C11** · Q1 · kb `claim-quality.md:1375` — `AVE genesis arcs to date are closed-negative (the engine does not self-form the winding; the seeder PLANTS it — cf `clm-gfdplp`).` — Names the genesis/formation route from a free precursor AS DEAD — 'genesis arcs closed-negative to date' — with the kill's claim id cited (clm-gfdplp), inside a paths-to-derived survey explicitly labelled 'a survey of c…
- **K4** · Q1 · kb `electron-identification.md:64` — `The tank quality $Q = 1/\alpha$ is cited as an **identity**, not a derivation.` — $Q=1/\alpha$ appears only with its derivation-status explicitly denied — not sold as cage-emergent. (Per the standing ruling I do not inventory $\{m_e,\alpha,G\}$ calibration inputs themselves.)
- **K4** · Q1 · kb `index.md:48` — `T3.4b cold/α-FREE Q **≈30.8 NOT 137 = clean ECHO-corroboration of Q=1/α being calibration**` — Index blurb names the kill explicitly (the cold Q is 30.8, not 137; $Q=1/\alpha$ is calibration). Also the reason F-C10 scores zero here: this index advertises no ranked plumber order, genesis lanes, or v9-v15 direction…
- **K4** · Q1 · kb `electron-bound-resonator-coverage.md:73` — `**T3.4b** — cold/α-FREE Q from ring-down: **Q≈30.8, NOT 137 → corpus $Q=1/\alpha$ is an instance-baked ECHO**` — The K4 corpse (Q=137 / Q=1/alpha as cage-emergent identity) is named dead with the empirical negative in the row itself. Corroborated at the same leaf :170 (gate B.1 'NEGATIVE ×2, NO refill') and :228 (T3.4b suite row).
- **K4** · Q1 · kb `electron-bound-resonator-coverage.md:89` — `**α STAYS ECHO AT THE ELECTRON — FIVE independent ways**` — Five-way enumeration of why alpha (and hence Q=1/alpha) is an echo at the electron, with explicit 'NO promotion echo→chord' and Rule-12 HTML-comment trail dated 2026-06-19. Named as dead.
- **K4** · Q1 · kb `electron-bound-resonator-coverage.md:172` — `The slot stays EMPTY (anti-substitution); **no new Build-B slot is minted.**` — Dated adjudication (gate wmighcz1z verdict, 2026-06-19): the re-posed loaded-Q derivation of 137 is CIRCULAR, both provenance branches collapse to the echo, 'There is **no α-free path to $137$** through the loaded port.…
- **K4** · Q1 · kb `electron-bound-resonator-coverage.md:105` — `🟡 **DEMOTED 2026-08-15 — electron-identity Phase B (priority-ordering, not a K-row).**` — The 'THE load-bearing next step (do this ONE thing first)' Fork-A coupled-network Q block (:111-:154, which offers a ranked next-move routing) is dated-demoted 2026-08-15 with the Fork-A body preserved under Rule 12. Th…
- **K4** · Q1 · kb `electron-unknot-cosserat-seeder.md:75` — `**cited as an identity/ECHO (Class-B), not an autonomous derivation**` — The Layer-3 alpha^-1 = 4pi^3+pi^2+pi Q-factor is explicitly marked identity/echo, not a forward value derivation, at the site. Self-disclosed.
- **K4** · Q1 · kb `electron-unknot-cosserat-seeder.md:102` — `matches canonical 137.036 \| PASS (after fitting; not autonomous)` — Test-8 row discloses the fit in the result cell itself ('after fitting; not autonomous'). Named as dead at the site.
- **K4** · live-wrong · verifier: UNVERIFIED · kb `electron-unknot-cosserat-seeder.md:120` — `a self-consistent ground-state search (imaginary-time descent or Newton-Raphson) would tune to exact canonical` — Offered as the standing route by which the engine would reach the canonical (137.036) Q-factor, unbannered, with no pointer to the 2026-06-19 anti-substitution ruling (electron-bound-resonator-coverage.md:172, 'the slot…
- **K4** · live-wrong · verifier: UNVERIFIED · kb `pair-production-axiom-derivation.md:35` — `produces the $Q = 1/\alpha$ signature` — Quoted L3 corpus block offers Q = 1/alpha as the electron's signature with NO adjacent marker, in a leaf that carries other dated corrections but not this one. Post-2026-06-19 the corpus grades Q=1/alpha an instance-bak…
- **K4** · live-wrong · verifier: UNVERIFIED · kb `pair-production-axiom-derivation.md:137` — `$Q = 1/\alpha$ signature of TIR-confined electron` — Cross-reference blurb advertising Q = 1/alpha as the TIR-confined electron's signature, unmarked. Same corpse as :35; the theorem-3-1-q-factor.md target itself carries the 2026-06-19 Rule-12 Amendment re-attributing 137…
- **K4** · fence-excluded · tex `01_topological_matter.tex:172` — `The baseline empirical value ($\alpha \approx 1/137.036$)` — Only 137 occurrence in the chapter, and it is explicitly labelled 'baseline empirical value' — the calibration-input reading required by ruling A5, the exact opposite of the killed 'cage-emergent Q=137 / Q=1/α identity'…
- **K4** · fence-excluded · tex `07_quantum_mechanics_and_orbitals.tex:1083` — `$1/\alpha$ & 137 & 1.000  & \text{Lattice sound barrier} \\` — Z_max = 1/alpha row of the cavitation-number table (v/c = Z alpha/n = 1); a maximum-atomic-number statement, not Q = 137 sold as a cage-emergent electron identity. (a_0 = 137 l_node at :82/:162 is likewise the Bohr-radi…
- **K6** · fence-excluded · tex `01_topological_matter.tex:165` — `drilled and held open by the $(2,3)$ Cosserat circulation, and closed by the surface tension of the void--vacuum boundary` — The $(2,3)$ here is the Class-C hollow-vortex opener in a banked consistency picture, and print explicitly denies it any existence/pinning role two lines later (01:167 'existence ... held independently by the ... $\Gamm…
- **K6** · Q1 · kb `pair-production-axiom-derivation.md:79` — `Transverse curl is forced into $(2, 3)$ winding on the bond` — Step-7 sells the (2,3) winding as the dynamical closure that pins the pair's rest mass ('the pair is now a stable standing wave with rest mass $m_e c^2$ each'). The leaf carries the dated kill in-file at :103 ('now RUN …
- **K6** · Q1 · kb `pair-production-axiom-derivation.md:123` — `$(2, 3)$ winding in $(V_{\text{inc}}, V_{\text{ref}})$ phasor trajectory on the bond, at amplitude corresponding to rest energy $m_e c^2$ per pair member.` — Option-D nucleation rule imposes the (2,3) winding as the dynamical output that carries the rest energy. Same corpse as :79. The #417 NEGATIVE is in-file at :103 but 20 lines up and in a different section (§4), so a §5-…
- **K6** · live-wrong · verifier: UNVERIFIED · tex `01_topological_matter.tex:239` — `Higher $q$ produces more tightly wound solitons with correspondingly higher mass.` — Print ties winding/crossing count directly to MASS, unbannered — the closest printed relative of the K6 corpse ('(2,3) winding sold as the DYNAMICAL mass-pin'), and in tension with the A1-dilatation-mass ⊥ Cosserat-(2,3…
- **K6** · fence-excluded · tex `01_topological_matter.tex:239` — `Rolfsen names ($3_1$, $5_1$, \ldots) label $(2,q)$ \textbf{phase-space winding portraits}` — Same TeX line, separate clause: the static phase-space winding dictionary (electron body = 0_1 unknot; proton body = 6^3_2 Borromean) is exactly the surviving homonym the K6 fence holds out. Not the corpse.
- **K6** · fence-excluded · kb `electron-unknot-cosserat-seeder.md:73` — `\| **Layer 3** \| $(2, 3)$ phase-space winding \| Clifford-torus winding in $(V_{\text{inc}}, V_{\text{ref}})$ phasor space` — Static tank / Clifford-torus (2,3) winding — the surviving homonym per the K6 and F-C9 fences, not the dynamical mass-pin.
- **K6** · fence-excluded · kb `l3-electron-soliton-synthesis.md:47` — `> **Real-space ⊥ phase-space disambiguation (INVARIANT-N1 cross-ref, 2026-07-09).**` — Dated INVARIANT-N1 note keeping the (2,q) winding in phase space and the real-space body as the 0_1 unknot — the fence object itself.
- **K6** · live-wrong · verifier: DOWNGRADED · kb `torus-knot-uniqueness.md:106` — `\| Electron \| $(2, 3)$ trefoil + 0 Cosserat torsion quanta \| base Faddeev-Skyrme on (2,3) \| $\sim 0.511$ MeV (measured) \|` — The §7 lepton table's 'Mass mechanism' column names the Faddeev-Skyrme energy ON THE (2,3) WINDING as what sets the electron's mass, unbannered, in a leaf carrying no Rule-12 banner anywhere. A reader at HEAD would take… — REFUTED: Fragment is byte-verbatim at line 106 (grep -nF confirms; leaf read in full, 1-150). But the site sits inside the K6 fence ("static Link wi… / CONFIRMED: Fragment is byte-verbatim at torus-knot-uniqueness.md:106 (grep -nF confirms). Read the full 150-line leaf: the file's only banner (line…
- **K6** · fence-excluded · tex `02_baryon_sector.tex:226` — `phase profile follows the $(2,3)$ pattern` — Static (2,q) winding dictionary (electron (2,3) -> proton (2,5) 'phase-space per-loop polarization winding'), explicitly 'even though its ground-state topology is the unknot'. Static Link winding stands; not offered as …
- **K6** · fence-excluded · kb `self-consistent-mass-oscillator.md:16` — `follows the $(2,3)$ pattern` — Verbatim twin of TeX :226; same static-winding-dictionary usage (also proton-identification.md:21, relabelled 2026-06-08 as phase-space winding, NOT real-space).
- **K6** · fence-excluded · tex `04_quantum_spin.tex:13` — `the $0_1$ unknot flux tube in real space carrying a rotating $(2,3)$ phase-space Clifford-torus winding pattern` — The (2,3) winding is named as the static phase-space Clifford-torus winding the unknot carries (charge/winding dictionary homonym) and is used as the SPIN flywheel ontology; no claim that the (2,3) winding is the dynami…
- **K6** · fence-excluded · tex `04_quantum_spin.tex:24` — `the electron is the $0_1$ unknot in real space carrying a literal macro-physical $(2,3)$ phase-space Clifford-torus winding pattern that stores inductive kinet…` — Same homonym as :13 -- (2,3) as the phase-space winding storing inductive energy for the angular-momentum argument; no mass-pin or genesis mechanism offered.
- **K6** · fence-excluded · kb `spin-as-precession.md:10` — `the $0_1$ unknot flux tube in real space carrying a rotating $(2,3)$ phase-space Clifford-torus winding pattern` — Verbatim twin of TeX:13; same fence.
- **K6** · fence-excluded · kb `larmor-derivation.md:10` — `the electron is the $0_1$ unknot in real space` — Verbatim twin of TeX:24 (with an added Vol 1 Ch 8 link); same fence.
- **K6** · fence-excluded · tex `06_electroweak_and_higgs.tex:514` — `The canonical AVE electron is the $(2,3)$ Cosserat unknot` — Names the Cosserat unknot (real-space 0_1 with a (2,3) phase-space portrait) as the SUBSTRATE for the g-2 correlation; not offered as the dynamical mass-pin. Static/phase-space winding homonym survives per the K6 fence.
- **K6** · fence-excluded · tex `06_electroweak_and_higgs.tex:560` — `\item \textbf{(2,3) phase-space trefoil currents.} The Cosserat unknot` — (2,3) used as the Clifford-torus phase-space current portrait I_d = cos(2ω t), I_q = sin(3ω t) for the two-loop kernel; a current dictionary, not a mass-pin mechanism.
- **K6** · fence-excluded · tex `06_electroweak_and_higgs.tex:647` — `where $n_q = 3$ is the q-axis poloidal winding number of the (2,3)` — Static winding number feeding the (refuted, and so-labelled in print at 06:753-770) saliency postulate; not the dynamical mass-pin corpse.
- **K6** · fence-excluded · tex `06_electroweak_and_higgs.tex:777` — `\noindent\textbf{Zero parameters were fudged.} The trefoil $(2,3)$,` — Lists the (2,3) trefoil as a corpus-canonical Stage-1 input to the g-2 kernel; static winding, not mass-pin.
- **K6** · fence-excluded · kb `q-g19a-petermann-saliency-closure.md:28` — `1. **$(2,3)$ phase-space trefoil currents.**` — Same phase-space current portrait as TeX 06:560; the leaf explicitly says 'The trefoil lives in *phase space*, not real space; the real-space soliton is the unknot $0_1$' (:30).
- **K6** · fence-excluded · kb `q-g19a-petermann-saliency-closure.md:14` — `the q-axis poloidal winding of the (2,3) trefoil` — Static winding number n_q = 3 in the Stage-2 postulate, which the same line marks RESOLVED NEGATIVE; not a mass-pin claim.
- **K6** · fence-excluded · kb `q-g27-muon-cosserat-saliency.md:30` — `The phase-space (2,3) trefoil topology is preserved` — Phase-space trefoil retained as the g-2 kernel geometry for the muon; not offered as the dynamical mass-pin.
- **K6** · fence-excluded · kb `de-broglie-standing-wave.md:240` — `This is **NOT** the topologically-protected $(2,3)$ **winding**` — Names the static Link/(2,3) winding only to distinguish it from the de Broglie mode-count; the (2,3) winding is the surviving charge dictionary (fence), not sold as a dynamical mass-pin.
- **K6** · fence-excluded · kb `chiral-factor.md:45` — `at macroscopic scales, the $(2,3)$ trefoil produces $6/5$` — HOPF-01 PCB antenna torus-knot chiral factor chi = alpha*pq/(p+q); a macroscopic antenna resonator, not the electron mass-pin. (Leaf is outside the TeX 1-1100 twin set; listed because the whole ch07 KB dir was swept.)
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
- **ch01-B** — `01_topological_matter.tex` 1-273 (full) (of 273); `l3-electron-soliton-synthesis.md` 1-318 (full; chunks 1-160, 160-318) (of 318); `substrate-perspective-electron.md` 1-296 (full; chunks 1-150, 150-296) (of 296); `electron-bound-resonator-coverage.md` 1-376 (full; chunks 1-130, 130-280, 280-376) (of 376); `electron-unknot-cosserat-seeder.md` 1-205 (full; chunks 1-110, 110-205) (of 205); `pair-production-axiom-derivation.md` 1-207 (full; chunks 1-120, 120-207) (of 207); `claim-quality.md` 1-60 (clm-h9aqmt entry through terminator) and 1179-1360 (clm-gfdplp, clm-8zpicx, clm-ka5zdx, clm-ezai5b, clm-lj4ok5, clm-jupq56, clm-8c3yhs entries through terminators) — targeted entries per brief, not whole file (of 1774); `translation-circuit.md` 635-640, 765-769, 835-842 (anchor-verification spot reads only) (of 1145); `electron-identification.md` 88-93 (anchor-verification spot read only; ch01-A slice owns the full read) (of 0)
- **ch01-C** — `01_topological_matter.tex` 1-273 (of 273); `common-mode-twist-ledger.md` 1-369 (long lines re-read past col 900 via tail dump) (of 369); `torus-knot-uniqueness.md` 1-150 (of 150); `finkelstein-misner-spin-half-derivation.md` 1-202 (long lines 14/65/156 re-read past col 900) (of 202); `spin-gyroscopic-isomorphism.md` 1-63 (long lines 15/47 re-read past col 900) (of 63); `q-g18-schwinger-pair-wkb.md` 1-82 (of 82); `newtonian-inertia-as-lenz.md` 1-16 (full; pulled because common-mode-twist-ledger.md:50 names it as propagated mass-sector banner site #2 and the slice brief required it) (of 16); `claim-quality.md` 395-425 (clm-salw2h), 1290-1320 (clm-lj4ok5), 1344-1378 (clm-8c3yhs), 1615-1660 (clm-cmtwst) — entry-scoped read as instructed, not whole file (of 1774); `claim-quality.md` 1873-1935 (clm-wcoul2 entry only — anchor/status check for printed TeX 01:242 cite) (of 0)
- **ch02** — `02_baryon_sector.tex` 1-240, 241-472 (of 472); `index.md` 1-39 (of 39); `proton-identification.md` 1-84, 85-168 (of 168); `neutron-identification.md` 1-134 (of 134); `thermal-softening.md` 1-124 (of 124); `proton-neutron-mass-split.md` 1-48, 46-62, 60-97 (of 97); `quark-flavors.md` 1-12 (of 12); `self-consistent-mass-oscillator.md` 1-66 (of 66); `torus-knot-ladder-baryons.md` 1-51 (of 51); `topological-fractionalization.md` 1-90 (of 90); `claim-quality.md` 42-110 (clm-mnb3lt 42-70, clm-k6olj8 72-100), 274-340 (clm-67jn9o 274-297, clm-w8jn3q 299-328), 752-756, 779-810 (clm-bh9p6s 779-806), 1382-1450 (clm-6kwzot 1382-1409, clm-cmic3e 1411-1438); entries only, not full file (of 1774); `00_title.tex` 18 (grep only, per instruction) (of 19)
- **ch03** — `03_neutrino_sector.tex` 1-281 (full file) (of 281); `index.md` 1-37 (full file) (of 37); `chiral-screening.md` 1-48 (full file) (of 48); `delta-cp-violation.md` 1-81 (full file) (of 81); `neutrino-translation-table.md` 1-12 (full file) (of 12); `pmns-eigenvalues.md` 1-51 (full file) (of 51); `pmns-junction-model.md` 1-25 (full file) (of 25); `claim-quality.md` 211-271 (clm-7o8clt and clm-rji99i entries only, through their --- terminators, per task scope; full 1774-line file NOT read in full) (of 1774); `01_topological_matter.tex` 195-215 (partial, targeted at the 01:207 regime-classification table per slice-specific instruction (b); not an assigned slice file, not read in full) (of 215); `00_title.tex` grep-only for 'twisted' (line 14 located and quoted); not Read in full, per slice-specific instruction which asked for a targeted grep on this file (of 0)
- **ch04** — `04_quantum_spin.tex` 1-125 (of 125); `index.md` 1-28 (of 28); `larmor-derivation.md` 1-69 (of 69); `spin-as-precession.md` 1-20 (of 20); `visual-equivalence.md` 1-26 (of 26); `spin-half-paradox.md` 1-18 (of 18); `claim-quality.md` 401-428 (clm-salw2h entry through its --- terminator at 427; spot-verified 407-411, 419-421, 1146-1154) (of 1774)
- **ch05** — `05_electroweak_gauge_theory.tex` 1-248 (sed 1-130, 131-247; awk line-map 1-248; wc -l reports 247 because the last line has no trailing newline) (of 248); `gauge-boson-masses.md` 1-204 (sed 1-120, 121-204; awk line-map 1-204) (of 204); `index.md` 1-32 (of 32); `weak-coupling.md` 1-38 (of 38); `weinberg-angle.md` 1-40 (of 40); `forward-to-ch6.md` 1-54 (of 54); `claim-quality.md` 103-127 (clm-5zuo7g), 130-155 (clm-q8un7j), 809-834 (clm-jkpfd4), 274-297 (clm-67jn9o dependency) — partial, entries only (of 1774); `vocabulary-register.md` 878-923 (def-l0ngdu :882-895 and def-uatk1s :897-909 in full) plus grep-pinned single lines 575, 727, 867, 870, 882, 1085, 1423 — partial (of 1736); `2026-08-02_manuscript-reconciliation-board.md` 28-60 (CRIB-1/CRIB-1′), 617-700 (vol2 13 findings) — partial (of 1222); `2026-09-06_tex-kb-staleness_scan.txt` 85-100 plus grep-pinned lines 95-96, 164, 200, 259 — partial (of 368); `2026-09-06_mr-board-revalidation_RESULT.md` grep only (no 05:/ch05 item present; line 188 unrelated) — partial (of 283); `proton-identification.md` grep-pinned lines 13-116 (Borromean/🔴 rows) — partial, cross-check only (of 168); `form-deriving-value-importing.md` 110-120 — partial (CRIB-1′ cross-check) (of 667); `wall-taxonomy.md` 336-338 (anchor check only) (of 0); `translation-circuit.md` 214 (anchor check only) (of 0); `q-g47-substrate-scale-cosserat-closure.md` 28 (anchor check only) (of 0)
- **ch06-A** — `06_electroweak_and_higgs.tex` 1-450 (full assigned slice; read as 1-250, 250-449, 449-451 overlapping chunks for full coverage) (of 867); `higgs-mechanism.md` 1-62 (full file) (of 62); `lepton-spectrum.md` 1-86 (full file) (of 86); `spontaneous-symmetry-breaking.md` 1-87 (full file) (of 87); `sm-ave-translation.md` 1-12 (full file) (of 12); `index.md` 1-38 (full file) (of 38); `chiral-screening.md` 1-48 (full file) (of 48); `claim-quality.md` 95-179 (clm-5zuo7g, clm-q8un7j, clm-p7rfkb entries through their --- terminators), 240-297 (clm-rji99i entry through its --- terminator), 1660-1774 (R40 batch-2a dated note referenced by clm-p7rfkb, through EOF) (of 1774); `higgs-mass.md` 1-94 (full file; discovered during sectionMap-building as the KB twin for TeX's Neutrino Mass Spectrum + Schwinger sections, read in full and grep-verified for mismatch M3/M4) (of 94); `verify-md-links.py` 795-819 (WAIVED_KBLEAF table, consulted to confirm mismatch M8 is a pre-existing tracked waiver) (of 0)
- **ch06-B** — `06_electroweak_and_higgs.tex` 449-660, 661-867 (assigned range read in full) (of 867); `q-g19a-petermann-saliency-closure.md` 1-130, 131-256 (of 256); `q-g20f-vacuum-polarization.md` 1-149 (of 149); `q-g27-muon-cosserat-saliency.md` 1-88 (of 88); `higgs-mass.md` 1-94 (of 94); `index.md` 1-38 (of 38); `claim-quality.md` 158-215 (clm-p7rfkb, clm-stgx1i through --- terminators), 1441-1530 (clm-v2sg8z, clm-bqtasn, clm-8niffj through --- terminators), 1665-1774 (R40 batch-2a status note, cited by clm-p7rfkb:162) (of 1774); `lambda-higgs-derivation.md` 1-44 (not assigned; read in full as the only KB twin of TeX 06:808-834, per closure-roadmap.md:201) (of 44); `sm-ave-translation.md` 1-12 (not assigned; forwarder twin of 06:855-860) (of 12); `2026-08-02_manuscript-reconciliation-board.md` 615-665 (vol2 findings block only, for alreadyKnownIn) (of 1222); `2026-09-06_tex-kb-staleness_scan.txt` grep-indexed only (lines 97-101, 243, 353 for 06_electroweak sites); not a full read (of 368); `r40_sweep_worklist_verified.json` 1740-1760, 1820-1840 (acoustic-Higgs/breathing-mode family entries only) (of 4674)
- **ch07-A** — `07_quantum_mechanics_and_orbitals.tex` 1-250, 251-500, 501-750, 751-1000, 1001-1100 (assigned range, full); plus 4146-4210 and 4251-4290 read only to verify the R40 end-of-chapter note pointers (of 4290); `de-broglie-standing-wave.md` 1-200, 201-340 (full) (of 340); `index.md` 1-63 (full) (of 63); `qm-ave-translation.md` 1-18 (full) (of 18); `atom-as-radial-waveguide.md` 1-42 (full) (of 42); `macro-cavity-saturation.md` 1-14 (full) (of 14); `ode-verification.md` 1-55 (full) (of 55); `de-broglie-n.md` 1-30 (full) (of 30); `helium-symmetric-cavity.md` 1-82 (full) (of 82); `analog-ladder-filter.md` 1-96 (full) (of 96); `geometry-pipeline.md` 1-75 (full) (of 75); `screening-rule.md` 1-38 (full) (of 38); `orbital-penetration-penalties.md` 1-58 (full) (of 58); `hierarchical-cascade-correction.md` 1-60 (full) (of 60); `chiral-factor.md` 1-51 (full) (of 51); `scale-separation.md` 1-68 (full) (of 68); `helium-coupling-first-principles.md` 1-64 (full) (of 64); `bonding-mode-formula.md` 1-44 (full) (of 44); `stepped-impedance-resonator.md` 1-92 (full) (of 92); `subshell-junction-scattering.md` 1-42 (full) (of 42); `ionization-energy-validation.md` 1-52 (full) (of 52); `complete-solver-architecture.md` 1-44 (full) (of 44); `dual-formalism-architecture.md` 1-28 (full) (of 28); `knot-vs-orbital-table.md` 1-22 (full) (of 22); `operator-domain-table.md` 1-19 (full) (of 19); `radial-eigenvalue-solver.md` GREP-INDEX ONLY (no full read; content is Steps 3+/E2, outside range 1-1100). Hit lines inspected: 119, 164, 178, 194, 294, 693, 697, 712, 768 (of 816); `brillouin-zone-uv-cutoff.md` GREP-INDEX ONLY (research-origin leaf; 0 hits for any range-1-1100 heading/keyword) (of 120); `q-g20a-lamb-shift-structural-closure.md` GREP-INDEX ONLY (research-origin leaf; 0 hits for any range-1-1100 heading/keyword) (of 73); `claim-quality.md` 331-369 (clm-oltvwy), 372-398 (clm-w6kk5y), 623-649 (clm-ak97cb), 837-868 (clm-qde5gn) — each through its --- terminator (of 1774); `vocabulary-register.md` 258-275 (def-quant3 entry only, for M7 context) (of 1736); `program-arc-map.md` 371 only (N13 row, grep-pinned, for M5) (of 416); `r40_sweep_worklist_verified.json` 520-540, 1874-1905, 2433-2476, 3696-3712 (ch07 rows only) (of 4674)
- **ch07-B** — `07_quantum_mechanics_and_orbitals.tex` 1100-2250 (assigned slice, full); plus context-only reads 470-570 and 250-260 (of 4290); `bonding-mode-formula.md` 1-45 (full) (of 45); `helium-coupling-first-principles.md` 1-65 (full) (of 65); `radial-eigenvalue-solver.md` 1-816 (full) (of 816); `complete-solver-architecture.md` 1-45 (full) (of 45); `dual-formalism-architecture.md` 1-28 (full) (of 28); `de-broglie-n.md` 1-30 (full) (of 30); `screening-rule.md` 1-38 (full) (of 38); `orbital-penetration-penalties.md` 1-59 (full) (of 59); `geometry-pipeline.md` 1-75 (full) (of 75); `atom-as-radial-waveguide.md` 1-42 (full) (of 42); `macro-cavity-saturation.md` 1-14 (full) (of 14); `index.md` 1-64 (full) (of 64); `claim-quality.md` 325-397 (clm-oltvwy full entry 330-368; clm-w6kk5y full entry 371-397) (of 0)
- **ch07-C** — `07_quantum_mechanics_and_orbitals.tex` 2250-3400 (assigned range, read in full in 5 chunks); plus targeted grep-only lookups outside range (161, 558, 3134-3139, 3565-3611, 3851, 4007, 4027) to place twins (of 4290); `radial-eigenvalue-solver.md` 1-816 (of 816); `dual-formalism-architecture.md` 1-28 (of 28); `screening-rule.md` 1-38 (of 38); `subshell-junction-scattering.md` 1-42 (of 42); `hierarchical-cascade-correction.md` 1-60 (of 60); `helium-coupling-first-principles.md` 1-64 (of 64); `knot-vs-orbital-table.md` 1-22 (of 22); `complete-solver-architecture.md` 1-44 (of 44); `index.md` 1-63 (of 63); `operator-domain-table.md` 1-19 (of 19); `qm-ave-translation.md` 1-18 (of 18); `de-broglie-standing-wave.md` 1-340 (of 340); `brillouin-zone-uv-cutoff.md` 1-120 (of 120); `q-g20a-lamb-shift-structural-closure.md` 1-73 (of 73); `helium-symmetric-cavity.md` 1-82 (of 82); `stepped-impedance-resonator.md` 1-92 (of 92); `analog-ladder-filter.md` 1-96 (of 96); `geometry-pipeline.md` 1-75 (of 75); `scale-separation.md` 1-68 (of 68); `orbital-penetration-penalties.md` 1-58 (of 58); `ode-verification.md` 1-55 (of 55); `chiral-factor.md` 1-51 (of 51); `bonding-mode-formula.md` 1-44 (of 44); `atom-as-radial-waveguide.md` 1-42 (of 42); `de-broglie-n.md` 1-30 (of 30); `macro-cavity-saturation.md` 1-14 (of 14); `ionization-energy-validation.md` 1-52 (of 52); `claim-quality.md` 331-398 (clm-oltvwy 331-369, clm-w6kk5y 371-398, each through its --- terminator) (of 1774); `radial_eigenvalue.py` 1840-1870 (context only, for the kappa_hopf parity factor; grep elsewhere) (of 0)
- **ch07-D** — `07_quantum_mechanics_and_orbitals.tex` 3400-3650, 3650-3900, 3900-4150, 4150-4290 (of 4290); `scale-separation.md` 1-68 (of 68); `subshell-junction-scattering.md` 1-42 (of 42); `helium-coupling-first-principles.md` 1-64 (of 64); `chiral-factor.md` 1-51 (of 51); `stepped-impedance-resonator.md` 1-92 (of 92); `hierarchical-cascade-correction.md` 1-60 (of 60); `ionization-energy-validation.md` 1-52 (of 52); `knot-vs-orbital-table.md` 1-22 (of 22); `brillouin-zone-uv-cutoff.md` 1-120 (of 120); `q-g20a-lamb-shift-structural-closure.md` 1-73 (of 73); `operator-domain-table.md` 1-19 (of 19); `claim-quality.md` 325-420 (clm-oltvwy, clm-w6kk5y), 615-680 (clm-ak97cb), 1520-1545 (clm-3i66gp), 1589-1615 (clm-1wmyx3) (of 1774)
- **ch08** — `08_planck_and_string_theory.tex` 1-103 (full) (of 103); `index.md` 1-27 (full) (of 27); `planck-scale-derivation.md` 1-72 (full) (of 72); `string-theory-translation.md` 1-32 (full) (of 32); `claim-quality.md` 555-591 (clm-g6e3zw entry, located via grep -n "<!-- id: clm-" then read through terminating ---; rest of 1774-line file not in scope for this slice) (of 1774)
- **ch09** — `09_computational_proof.tex` 1-266 (full) (of 266); `index.md` 1-34 (full) (of 34); `anomaly-catalog.md` 1-34 (full) (of 34); `computational-graph.md` 1-37 (full) (of 37); `methodological-contamination.md` 1-78 (full) (of 78); `precision-policy.md` 1-57 (full) (of 57); `index.md` 1-29 (full) (of 29); `graph-architecture.md` 1-132 (full) (of 132); `claim-quality.md` 331-400, 623-690, 944-1010, 1030-1080 (targeted entries for clm-oltvwy, clm-ak97cb/clm-nhlo1e/clm-oygz1i, clm-z73h6n/clm-ghs75o, clm-pf84ng/clm-o3q9ul, per task instruction to read these 4 entries through their terminators) (of 1200); `claim-quality.md` 180-220 (targeted: clm-u4vmgk entry, for :190 dead-anchor verification) (of 636); `form-deriving-value-importing.md` 80-95 (targeted: K=2G row for :87 anchor verification) (of 667); `claim-quality.md` 660-670 (targeted: :665 anchor verification) (of 670); `ch8-alpha-golden-torus.md` 8-14 (targeted: :11 anchor verification) (of 14); `q-g27-muon-cosserat-saliency.md` grep-targeted lines 8,14,22,23,59,71,73,75,88 (walk-back verification, not full read — out of assigned slice, used only for cite-verification) (of 88)
- **ch10** — `10_open_problems.tex` 1-445 (full file) (of 445); `baryon-asymmetry.md` 1-74 (full file) (of 74); `g-star-derivation.md` 1-22 (full file) (of 22); `g-star-prediction.md` 1-32 (full file) (of 32); `hubble-tension.md` 1-61 (full file) (of 61); `index.md` 1-35 (full file) (of 35); `quantitative-resolutions.md` 1-22 (full file) (of 22); `scale-invariance-table.md` 1-29 (full file) (of 29); `strong-cp.md` 1-69 (full file) (of 69); `unification.md` 1-14 (full file) (of 14); `claim-quality.md` 480-700 (clm-gfs4j8:485-509, clm-4vwsjc:511-533, clm-mroghg:540-562, entries read through their '---' terminators); 860-945 (clm-xhdai6:871-909, read through its '---' terminator) (of 1774); `claim-quality.md` 495-530 (clm-uu6dl5:505-527, read through its '---' terminator) (of 1399)
- **ch11** — `11_standard_model_overdrive.tex` 1-133 (full) (of 133); `index.md` 1-34 (full) (of 34); `axiom-survey.md` 1-14 (full) (of 14); `overdrive-comparison.md` 1-19 (full) (of 19); `overdrive-nuclear.md` 1-38 (full) (of 38); `overdrive-protein.md` 1-24 (full) (of 24); `universal-energy.md` 1-28 (full) (of 28); `claim-quality.md` 585-649 (clm-dboxok entry at 591-620, located via grep -n 'id: clm-'; adjacent entries read for context/terminator confirmation) (of 649); `program-arc-map.md` 360-380 (N13 row context, located via grep -n N13; not one of the slice's required full-read files) (of 649); `2026-09-06_mr-board-revalidation_RESULT.md` 87-88 (grep-located items 15/16 confirming known-debt status) (of 100); `ch8-alpha-golden-torus.md` 1-13 (due-diligence check on the %-comment's \kbleaf :11 anchor; outside slice scope, not a full read) (of 222)
- **ch12-mp** — `12_the_millennium_prizes.tex` 1-711 (full file, single read) (of 711); `index.md` 1-41 (full file) (of 41); `birch-swinnerton-dyer.md` 1-72 (full file) (of 72); `hodge-conjecture.md` 1-64 (full file) (of 64); `knot-vs-orbital-table-ch12.md` 1-16 (full file) (of 16); `navier-stokes-prize.md` 1-70 (full file) (of 70); `p-vs-np.md` 1-55 (full file) (of 55); `poincare-conjecture.md` 1-63 (full file) (of 63); `riemann-hypothesis.md` 1-111 (full file) (of 111); `yang-mills-steps1-2.md` 1-62 (full file) (of 62); `yang-mills-steps3-5.md` 1-65 (full file) (of 65); `claim-quality.md` 420-499, 900-959 (targeted: clm-q5izb7, clm-c8q0z5, clm-knveh6 entries only, per slice instructions) (of 1774); `srs-band-structure.md` 1-298 (full file, cross-check for the 12mp:112 \kbleaf cite target) (of 298)
- **ch12-fp** — `12_appendix_formal_proofs.tex` 1-453 (full file) (of 453); `yang-mills-steps1-2.md` 1-62 (full file) (of 62); `yang-mills-steps3-5.md` 1-65 (full file) (of 65); `navier-stokes-prize.md` 1-70 (full file) (of 70); `riemann-hypothesis.md` 1-111 (full file) (of 111); `index.md` 1-51 (full file) (of 51); `claim-quality.md` 429-498 (clm-q5izb7, clm-c8q0z5), 910-1049 (clm-knveh6, clm-e1pdfd) (of 1774)
- **appx-front: NO RECEIPT**
