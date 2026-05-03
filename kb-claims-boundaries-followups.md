# KB Claim Boundaries — Followups

Issues surfaced during execution of the kb-claims-boundaries plan that are outside the scope of any individual dispatch.

> **Discipline:** Do NOT fix inline. Do NOT expand dispatch scope. Do NOT silently absorb. Triage before PR merge.

---

## 2026-05-02 — Some claim bounds have no leaf-level statement; only invariant-doc statement

- **Surfaced by:** mad-participant-1 (Dispatch D2 — baseline adversarial review on α-and-gravity)
- **Location:** `manuscript/ave-kb/vol1/`, `manuscript/ave-kb/vol3/gravity/`
- **Description:** Several boundary claims that the framework **does** make at the project-invariant level (CLAUDE.md, LIVING_REFERENCE.md "Common Pitfalls") are not explicitly stated in any individual leaf. Specific instance: "α is exactly invariant under Symmetric Gravity; multi-species Δα/α = 0" is asserted in CLAUDE.md (Axiom 3 entry) and in LIVING_REFERENCE.md Pitfall #5, but no leaf in `vol1/` or `vol3/gravity/` explicitly states it. Adversarial baseline review formed 9 findings against the α-and-gravity surface; consulting the leaves cited in summary Key Results retracted **zero** findings, because the leaves are silent on the bound rather than supportive of it.
- **Implication for boundaries work:** the convention spec's "leaves are the source" rule is too strict. Some bounds are derivable from leaves but not explicitly stated in them; for those, the canonical statement lives in CLAUDE.md or LIVING_REFERENCE.md. The boundaries doc should distinguish leaf-traceable bounds from invariant-doc-traceable bounds in its "Leaf references" footer. (Convention spec §6 amended in this dispatch to reflect this.)
- **Implication for the KB itself (the substantive followup):** the leaves arguably **should** explicitly state these bounds, so future readers can follow the up-link from a result to a leaf and see the bound in context. For example, vol3/gravity should have a leaf (or section in an existing leaf) that states "α is exactly invariant under Symmetric Gravity" with derivation. This is a content gap in the KB, not in the boundaries mechanism.
- **Recommended owner:** kb-content-distiller (for the leaf authoring); kb-taxonomy-architect (for placement decisions about where new content goes).
- **Severity:** medium — the boundaries mechanism still works (sidecars cite the invariant doc honestly), but the leaves' silence is a separate KB content quality issue worth addressing.

---

## 2026-05-02 — Interpretive tension on impedance at the event horizon

- **Surfaced by:** generalist-coder (Dispatch D3 — vol3 sidecar)
- **Location:** `manuscript/ave-kb/vol3/gravity/ch02-general-relativity/einstein-field-equation.md` (~line 42) vs `manuscript/ave-kb/vol3/gravity/ch08-gravitational-waves/invariant-gravitational-impedance.md` and `gw-propagation-lossless.md` (whole leaves)
- **Description:** The Einstein-field-equation leaf states that at $r_s$ "both $\mu_{eff}$ and $\varepsilon_{eff}$ collapse to zero, the local impedance drops to zero ($Z \to 0$), and the reflection coefficient reaches $\Gamma = -1$ (total confinement)." The GW leaves state that under Symmetric Gravity $Z(r) = Z_0$ is **invariant everywhere** and $\Gamma = 0$ at any gravitational gradient. Both are technically reconcilable (constitutive parameters individually go to zero while their ratio is preserved; the $\Gamma = -1$ statement applies to a different boundary condition than the GW transverse-mode case), but the leaves do not flag the distinction. A reader visiting both leaves will see contradictory $Z$ and $\Gamma$ statements about the same horizon. The vol3 sidecar's "Einstein Field Equation Reinterpretation" entry calls out the tension; the underlying leaves should be cross-linked or each amended with a one-line note clarifying which boundary condition applies.
- **Recommended owner:** kb-content-distiller (or vol3-gravity domain expert)
- **Severity:** medium

---

## 2026-05-02 — Hubble derivation circularity flagged in leaves but not in vol3 index

- **Surfaced by:** generalist-coder (Dispatch D3 — vol3 sidecar)
- **Location:** `manuscript/ave-kb/vol3/index.md` line 14 (Key Results "Asymptotic Hubble Constant" entry) vs `manuscript/ave-kb/vol3/cosmology/ch04-generative-cosmology/lattice-genesis-hubble-tension.md` (~line 29)
- **Description:** The lattice-genesis leaf explicitly states the Hubble relation is a "geometric self-consistency check" rather than an independent prediction (because $R_H \equiv c/H_\infty$ enters the definition of $G$ via $\xi$). The vol3 index Key Results table presents $H_\infty \approx 69.32$ km/s/Mpc with no qualifier, suggesting an independent prediction. This is exactly the summary-conflation pattern the sidecar convention is designed to bound — the sidecar entry catches it, but the index summary remains misleading until the next refresh. Could be addressed by adding an asterisk / footnote in the Key Results row or referencing the consistency-proof framing inline.
- **Recommended owner:** kb-content-distiller (Boundaries Mode refresh) or vol3 index author
- **Severity:** low

---

## 2026-05-02 — Hubble value 69.32 vs 69.33 inconsistency between leaf and Master Prediction Table

- **Surfaced by:** kb-accuracy-reviewer (Dispatch D6a — pilot accuracy review)
- **Location:** `manuscript/ave-kb/vol3/cosmology/ch04-generative-cosmology/lattice-genesis-hubble-tension.md` (table row "AVE $H_\infty$: 69.33 km/s/Mpc") vs `LIVING_REFERENCE.md` row #23 ("69.32 km/s/Mpc") vs `manuscript/ave-kb/entry-point.md` ("69.32 km/s/Mpc")
- **Description:** The Asymptotic Hubble Constant is reported as 69.32 km/s/Mpc in LIVING_REFERENCE.md and entry-point.md, but as 69.33 km/s/Mpc in the lattice-genesis leaf's comparison table. The vol3 sidecar uses 69.32 (matching the canonical sources). This is a last-digit inconsistency between sources; either a rounding-convention difference or a stale value in one location.
- **Recommended owner:** kb-content-distiller (reconcile leaf to canonical Master Prediction Table value, OR explicitly state the rounding convention in both locations)
- **Severity:** low

---

## 2026-05-02 — Missing `<!-- leaf: verbatim -->` marker on two vol3 leaves (INVARIANT-S5 violation)

- **Surfaced by:** kb-accuracy-reviewer (Dispatch D6a) noted as out-of-scope structural observation
- **Location:**
  - `manuscript/ave-kb/vol3/applied-physics/ch14-sonoluminescence/sonoluminescence-derivation.md` (line 2 absent)
  - `manuscript/ave-kb/vol3/condensed-matter/ch11-thermodynamics/kolmogorov-spectral-cutoff.md` (line 2 absent)
- **Description:** Both leaves are missing the `<!-- leaf: verbatim -->` annotation that INVARIANT-S5 (CLAUDE.md) requires on line 2 of every leaf. Pre-existing structural defect; surfaced incidentally during sidecar-citation auditing.
- **Recommended owner:** kb-structure-reviewer (or any link-validator pass)
- **Severity:** low

---

## 2026-05-02 — Pilot validation findings closed within scope

- **Surfaced by:** kb-accuracy-reviewer (D6a) and kb-structure-reviewer (D6b)
- **Description:** Two pilot-validation reviews ran. All Critical and Warning findings within boundaries-mechanism scope have been addressed inline:
  - Entry-point bootstrap directive's broken `#volumes` anchor link → replaced with explicit per-volume enumeration in prose.
  - INVARIANT-S7 in `CLAUDE.md` → hyperlinks added for cross-cutting and per-volume sidecars.
  - Convention spec §3 PATH-STABLE prose vs example contradiction → resolved (line 3 placement is authoritative; explanation added).
  - Vol3 sidecar GW entry collapsed regime table → restored per-signal breakdown citing einstein-field-equation.md table.
  - Vol3 sidecar Hawking entry added "particle-pair creation" framing not in leaf → reverted to the leaf's actual phrasing.
  - Vol3 sidecar flyby entry mis-listed missions ("Rosetta" instead of "Pioneer") → corrected to leaf's "Pioneer, Galileo, NEAR".
  - Vol3 sidecar BH entry leaf-references footer cited apparently-contradictory leaf without context → footer now distinguishes primary $\Gamma = 0$ source from the differently-framed leaf and points to the followups entry on interpretive tension.
- **Items not addressed inline (deferred to other followups):** Hubble 69.32 vs 69.33 (above), missing leaf markers on 2 vol3 leaves (above), and the pre-D3 interpretive tension on horizon impedance (already logged).
- **Severity:** n/a — closure record

---

## 2026-05-02 — vol5 index references unauthored `protein-folding-engine/` subtree

- **Surfaced by:** generalist-coder (Dispatch D5 — vol5 sidecar)
- **Location:** `manuscript/ave-kb/vol5/index.md` line 30 (Domains table row "Protein Folding Engine" pointing to `./protein-folding-engine/index.md`); cross-link in `manuscript/ave-kb/vol5/biological-applications/consciousness-cavity-eigenmode.md` line 53 to `../protein-folding-engine/network-solver/anesthesia-ch5.md`.
- **Description:** The vol5 index lists "Protein Folding Engine" as a domain covering Chapters 3–5 ($Z_\text{topo}$ definition, 8-tier architecture, 2D TL network solver, 20-protein PDB validation, $S_{11}$ objective, Kramers folding time). No leaves exist in this repository under `vol5/protein-folding-engine/` — the directory is unauthored. Per `LIVING_REFERENCE.md` lines 343–345 and 360–365, the protein folding engine implementation lives in a separate private repo (`AVE-Protein`); only the LC mapping theory (Chs. 1–2) is in this repo. Multiple Key Results in the vol5 index ($S_{11}$ Objective Function, Folding Speed Limit, Full Kramers Folding Time, 20-protein PDB Validation, $Z_\text{topo}$ per-residue table) point to leaves that do not exist here. The vol5 sidecar surfaces this but cannot bound the absent leaves; agent navigation following the index will hit broken links. The cross-link from `consciousness-cavity-eigenmode.md` to `../protein-folding-engine/network-solver/anesthesia-ch5.md` is a confirmed broken internal link.
- **Recommended owner:** kb-taxonomy-architect (decision: replicate sanitized leaves in this repo, or amend vol5/index.md to drop / footnote the engine-only Key Results and Domains rows); kb-content-distiller (execution).
- **Severity:** medium — affects index integrity and creates broken internal links; the boundaries mechanism cannot bound results whose leaves are not present.

---

## 2026-05-02 — vol5 $\eta_\text{eq}$ and $S_{11}$ functional bounds sourced from translation table only

- **Surfaced by:** generalist-coder (Dispatch D5 — vol5 sidecar)
- **Location:** `manuscript/ave-kb/vol5/common/translation-protein-solver.md` (row "Protein compaction" → $\eta_\text{eq} = P_C(1-\nu)$); `LIVING_REFERENCE.md` Master Prediction Table entry #39 (Villin Rg).
- **Description:** Two bounds in the vol5 sidecar — the $\eta_\text{eq}$ packing-fraction formula and the $S_{11}$ folding-functional definition — have no derivation leaf in this volume. They are sourced from the vol5 solver translation table (which is itself a mapping table, not a derivation), from `CLAUDE.md` INVARIANT-N4 ($S_{11}$ dual-meaning), and from `LIVING_REFERENCE.md` Master Prediction Table entry #39. The functional-definition leaves are in the private `AVE-Protein` engine repo. This is the same content-gap pattern logged in the 2026-05-02 α-invariance followup, applied here to the protein-folding side. The sidecar handled provenance honestly per Convention §6 amended.
- **Recommended owner:** kb-content-distiller (for any leaf authoring decision); kb-taxonomy-architect (for placement once the protein-folding-engine subtree question is resolved).
- **Severity:** low (boundaries mechanism handled it via honest provenance citation; the underlying gap is the same one already logged for α-invariance).

---

## 2026-05-02 — vol6 mass-defect summary table omits the fit-vs-prediction qualifier present in the source leaf

- **Surfaced by:** generalist-coder (Dispatch — vol6 sidecar)
- **Location:** `manuscript/ave-kb/vol6/framework/mass-defect-summary.md` (table of CODATA vs Topological mass for $Z=1$–$14$, errors $0.00001\%$ to $0.02739\%$); contrast with `manuscript/ave-kb/vol6/framework/computational-mass-defect/semiconductor-nuclear-analysis.md` line 7 (explicit methodology note: per-nucleus inter-alpha distance $R$ is fit per nucleus to recover the empirical mass; the reported sub-percent figures are fitting tolerances, not ab-initio prediction errors).
- **Description:** The semiconductor-nuclear-analysis leaf carries a load-bearing methodology blockquote disclosing the one-parameter-per-nucleus geometric fit. The mass-defect-summary leaf and the vol6 index Key Results row ("Mass defect accuracy: $0.00001\%$ to $0.02739\%$") present the same numbers without the qualifier, which a reader of the summary alone will misread as an ab-initio mass-prediction accuracy. This is the same summary-conflation pattern as the vol3 Hubble entry already logged (2026-05-02). The vol6 sidecar's "Mass-Defect Accuracy" entry catches it; the index/summary stay misleading until refresh.
- **Recommended owner:** kb-content-distiller (Boundaries Mode refresh) or vol6 framework author (add asterisk/footnote to mass-defect-summary table and the vol6 index Key Results row pointing to the methodology note).
- **Severity:** low — boundaries mechanism handles it; fix is editorial.

---

## 2026-05-02 — vol6 heavy-element catalog "$<0.5\%$ across 105 elements" headline understates worst-case error

- **Surfaced by:** generalist-coder (Dispatch — vol6 sidecar)
- **Location:** `manuscript/ave-kb/vol6/appendix/heavy-element-catalog/index.md` Key Results row "Fibonacci proxy accuracy: $< 0.5\%$ across 105 elements"; `manuscript/ave-kb/vol6/index.md` Period 3 description; full-element-table.md per-row data.
- **Description:** The "$< 0.5\%$ across 105 elements" headline is a typical-case figure. Inspection of `full-element-table.md` shows several Tier-C entries materially above $0.5\%$: Cl-35 at $1.465\%$, Zn-65 at $0.898\%$, Rb-85 at $0.849\%$, Pd-106 at $0.742\%$, Cd-112 at $0.716\%$, several others in the $0.5$–$0.7\%$ range. The vol6 sidecar's "Heavy Element Catalog" entry tiers the accuracy honestly (Tier A $0.000\%$, Tier B $\le 0.0002\%$, Tier C "typically $< 0.5\%$ but exceeds for several rows"). The index headline should be qualified as "typically $< 0.5\%$, with worst-case $\sim 1.5\%$ at Cl-35" or similar.
- **Recommended owner:** kb-content-distiller (Boundaries Mode refresh) or vol6 appendix author.
- **Severity:** low — the table itself is not wrong; only the summary phrasing is too clean.

---

## 2026-05-02 — vol6 Tritium beta-decay "$\sim 11.3$ MeV" framing risks confusion with empirical Q-value (18.6 keV)

- **Surfaced by:** generalist-coder (Dispatch — vol6 sidecar)
- **Location:** `manuscript/ave-kb/vol6/framework/computational-mass-defect/radioactive-decay-impedance.md` ("topological contraction yields an exothermic energy release of $\sim 11.3$ MeV").
- **Description:** The leaf reports the Tritium $\to ^3$He decay as releasing $\sim 11.3$ MeV from Q-factor optimization. The empirical $\beta$-decay endpoint energy for tritium is $18.6$ keV (about 600× smaller). The leaf appears to be reporting an internal framework quantity (the difference between the unstable and stable topology mass-defects as the framework computes them) rather than the measured $\beta$-particle endpoint, but does not flag the distinction. A reader comparing this leaf's number to the empirical $Q_\beta$ will see an apparent six-hundred-fold discrepancy with no in-leaf explanation. Either the framework figure means something different from the measured $Q_\beta$ (and should say so), or there is a substantive numerical error.
- **Recommended owner:** vol6 framework author or nuclear-domain reviewer (clarify what the $11.3$ MeV refers to and how it relates to empirical $Q_\beta = 18.6$ keV).
- **Severity:** medium — potential substantive error or load-bearing missing qualifier on a numerical claim.

---

## 2026-05-02 — vol6 ABCD transfer-matrix cascade flagged as the open problem for $Z \ge 15$, but heavy-element catalog presents results without the gating caveat

- **Surfaced by:** generalist-coder (Dispatch — vol6 sidecar)
- **Location:** `manuscript/ave-kb/vol6/framework/computational-mass-defect/abcd-transfer-matrix.md` (key-open-problem statement); `manuscript/ave-kb/vol6/appendix/heavy-element-catalog/full-element-table.md` and `index.md` (Z=15–119 results presented without referencing the open problem).
- **Description:** The ABCD leaf states that determining the correct ABCD cascade order and junction impedances for the alpha-cluster network is "the key open problem" and that current heavy-element results will be replaced by deterministic ABCD predictions when the problem is solved. The heavy-element catalog presents Z=15–119 mass predictions (Fibonacci-proxy tier) without a forward-pointer to this gating caveat. A reader of the catalog alone may not realize the methodology is provisional. The vol6 sidecar's "ABCD Transfer Matrix" and "Heavy Element Catalog" entries note this; the catalog should cross-link to the ABCD leaf as the methodological status note.
- **Recommended owner:** kb-content-distiller or vol6 appendix author (add cross-link from heavy-element-catalog/index.md to abcd-transfer-matrix.md as the methodological status indicator).
- **Severity:** low — informational completeness; not a numerical error.

---

## 2026-05-02 — vol4 index references PONDER-05 / `hardware-programs/` with no leaf backing

- **Surfaced by:** generalist-coder (Dispatch D4 — vol4 sidecar)
- **Location:** `manuscript/ave-kb/vol4/index.md` lines 12 and 23 (Key Results and Domains tables — "Hardware Programs" row); linked target `vol4/hardware-programs/index.md`.
- **Description:** The vol4 index Key Results / Domains tables cite "HOPF-01 $\Delta f/f = \alpha \cdot pq/(p+q)$ (zero free parameters); PONDER-05 469 $\mu$N predicted thrust; K4-TLM unitary to machine epsilon; Universal `AVE_VACUUM_CELL` SPICE subcircuit" with a link to `[Hardware Programs](hardware-programs/index.md)`. The `vol4/hardware-programs/` directory does not exist; the link is broken. The "PONDER-05" identifier and the "469 µN predicted thrust" number do not appear in any vol4 leaf. The actual vol4 chiral-thrust leaf (`circuit-theory/ch2-topological-thrust-mechanics/chiral-thrust-derivation.md`) gives PONDER-01 with **40.1 µN** predicted thrust at $V=30$ kV / $\beta = 10^3$ / $Q = 10^4$ / $N = 10{,}000$. The HOPF-01 build guide and the K4-TLM material exist under `falsification/` and `future-geometries/` respectively, but the index points to a missing parent. The vol4 sidecar's "Chiral Acoustic Rectification Thrust (PONDER-01)" entry flags the PONDER-05 number as routing-only (no leaf source).
- **Recommended owner:** kb-taxonomy-architect (decide whether to create `hardware-programs/` as a true domain or rewrite the index pointers); kb-content-distiller (if PONDER-05 is real and exists in source, surface its derivation to a leaf; if it is index drift from a longer-form PONDER-01 → PONDER-05 evolution discussion, normalize the index numbering).
- **Severity:** medium — the broken link is a navigation defect; the unbacked numerical claim is exactly the kind of derived-as-given hazard the sidecar convention exists to catch.

---

## 2026-05-02 — vol4 caustic leaf has units inconsistency on $E_{YIELD}$

- **Surfaced by:** generalist-coder (Dispatch D4 — vol4 sidecar)
- **Location:** `manuscript/ave-kb/vol4/advanced-applications/ch20-optical-caustic-resolution/index.md` Key Results table (~line 14).
- **Description:** The leaf states "Maximum focal intensity $E_{\max} = E_{YIELD} = \sqrt{\alpha} \cdot m_e c^2 / e \approx 43.65$ kV/m". The expression $\sqrt{\alpha} m_e c^2 / e$ evaluates to **43.65 kV** (a voltage, the macroscopic onset $V_{yield}$), not **43.65 kV/m** (a field). The macroscopic field equivalent $E_{yield} = V_{yield}/\ell_{node} \approx 1.13 \times 10^{17}$ V/m is the value used elsewhere in vol4 (regimes-of-operation, ee-bench-plateau). The "kV/m" units in this leaf are inconsistent with the formula and with the rest of vol4's macroscopic field-yield usage.
- **Recommended owner:** kb-content-distiller or vol4-engineering domain expert.
- **Severity:** low — the substantive bound (focal intensity capped by the same asymmetric saturation kernel used elsewhere) is correct; the units glitch in the Key Results row is a leaf-level edit fix.

---

## 2026-05-02 — vol4 leaves switch between $V_{yield}$ (43.65 kV) and "60 kV" without flagging

- **Surfaced by:** generalist-coder (Dispatch D4 — vol4 sidecar)
- **Location:** `manuscript/ave-kb/vol4/simulation/ch15-autoresonant-breakdown/theory.md` (~line 6, "$\sim 43.65\,\text{kV}$ point-yield, or the $60\,\text{kV}$ bulk-avalanche limit"); `manuscript/ave-kb/vol4/falsification/ch11-experimental-bench-falsification/ybco-phased-array.md` (uses 59 kV / 60 kV throughout); `manuscript/ave-kb/vol4/falsification/ch11-experimental-bench-falsification/metric-levitation-limit.md` (uses 43.65 kV).
- **Description:** Several Vol 4 leaves use a "60 kV bulk-avalanche limit" as if it were a third dielectric threshold alongside $V_{yield}$ (43.65 kV) and $V_{snap}$ (511 kV). The 60 kV figure originates from the tokamak-paradox derivation as the D-T ion-collision strain ($V_{topo} \approx 60.3$ kV) — it is a specific physical strain at a specific scenario, not a separate axiomatic yield. Using "60 kV" as the rupture threshold in YBCO-array and autoresonant-PLL leaves elides the distinction. The vol4 sidecar's "$V_{yield}$ vs $V_{snap}$" entry flags this; the leaves themselves should either harmonize or explicitly distinguish the 60 kV strain-at-tokamak from the axiomatic yield thresholds.
- **Recommended owner:** kb-content-distiller or vol4-engineering domain expert.
- **Severity:** medium — the numerical distinction is small and the engineering predictions are not derailed by the discrepancy, but the conceptual conflation is the same kind of derived-as-given hazard the cross-cutting tripwires catch elsewhere.

---

## 2026-05-02 — vol4 up-link label diverges from sibling volumes

- **Surfaced by:** kb-structure-reviewer (Dispatch D12b — final structure review)
- **Location:** `manuscript/ave-kb/vol4/index.md` line 1 — `[↑ Entry Point](../entry-point.md)` (every other volume index uses `[↑ AVE Knowledge Base](../entry-point.md)`)
- **Description:** Pre-existing label inconsistency surfaced by D12b structure review. Path is correct in all cases; only label text diverges. An automated link validator that requires literal label match against `AVE Knowledge Base` will flag vol4. Out of scope for the boundaries dispatch (predates this work); not fixed inline per scope discipline.
- **Recommended owner:** kb-structure-reviewer or any link-validator pass; kb-content-distiller for the actual edit.
- **Severity:** low

---

## 2026-05-02 — common/index.md "genuinely zero free parameters" omits conditional qualifier

- **Surfaced by:** kb-accuracy-reviewer (Dispatch D12a — final accuracy review)
- **Location:** `manuscript/ave-kb/common/index.md` Key Results row — "Complete derivation chain: 4 axioms + Golden Torus α derivation → 8 derivation layers → **genuinely zero free parameters**"
- **Description:** The common sidecar's Mathematical Closure entry explicitly states the framework is "structurally zero-parameter, conditional on thermal closure of $\delta_{strain}$ at $T_{CMB}$" and that one currently-fitted scalar remains. The common/index.md Key Results headline asserts "genuinely zero free parameters" without the conditional qualifier — the same summary-conflation pattern the boundaries mechanism is designed to bound. Bootstrap directive points to the sidecar so a careful agent will catch this; the index headline is misleading on its own.
- **Recommended owner:** kb-content-distiller (Boundaries Mode refresh) or common author.
- **Severity:** low — boundaries mechanism handles it; fix is editorial.

---

## 2026-05-02 — Bootstrap directive coverage gap on subtopic / chapter indexes

- **Surfaced by:** mad-participant-1 (Dispatch D12c — final adversarial review)
- **Location:** All chapter and subtopic `index.md` files below the volume level (e.g., `manuscript/ave-kb/vol3/gravity/index.md`, `vol3/gravity/ch01-gravity-yield/index.md`, etc.). Bootstrap directives currently exist on `entry-point.md` and the 7 volume-level `index.md` files; they do not appear on any deeper index.
- **Description:** A consumer (agent or human) entering the KB at a deep-link to a subtopic index — e.g., navigating directly to `vol3/gravity/index.md` from an external reference — does not encounter a bootstrap directive at that node. The CLAUDE.md INVARIANT-S7 covers the loose-pages case for cross-cutting bounds (CLAUDE.md is auto-loaded), but the volume-specific sidecar load instruction is only seen if the consumer traverses up to the volume index first. Per D12c measurement: K=0 → K=5 retractions when the directives ARE seen (mechanism works); coverage gap means deep-link entry doesn't trigger the load.
- **Recommended owner:** kb-content-distiller or kb-taxonomy-architect (decision: extend bootstrap directive to subtopic indexes? Use an abbreviated form? Rely on up-link traversal?).
- **Severity:** medium — affects deep-link entry which is a real usage pattern; current mechanism still helps when consumers traverse from entry-point or volume index.

---

## 2026-05-02 — vol2 sidecar lacks Hubble entry; cross-cutting sidecar incorrectly listed it

- **Surfaced by:** kb-accuracy-reviewer (Dispatch D12a — final accuracy review)
- **Location:** `manuscript/ave-kb/vol2/claims-boundaries.md` (no Hubble entry); cross-cutting `claims-boundaries.md` Hubble entry references footer (originally said "vol1, vol2, vol3 sidecars all carry volume-scoped entries" — corrected inline to vol1 + vol3 only).
- **Description:** Vol2 leaves do touch $H_\infty$ in cosmology framing but the vol2 sidecar (which prioritized particle physics, atomic IE, and Millennium problems) has no Hubble entry. The cross-cutting sidecar incorrectly asserted vol2 carried one; corrected inline. Adding a vol2 Hubble entry that cross-references the vol3 canonical treatment would close the inconsistency.
- **Recommended owner:** kb-content-distiller (Boundaries Mode — author a brief vol2 Hubble entry that defers to vol3 and the cross-cutting sidecar).
- **Severity:** low

---

## 2026-05-02 — Cross-cutting α-invariance citation corrected (D12c Finding 7 closed)

- **Action taken:** The cross-cutting α-invariance entry's References footer previously cited "CLAUDE.md Axiom 3 entry ('α invariance' sub-bullet)" as the invariant-level source. CLAUDE.md INVARIANT-S2 carries the four axioms in bare form; the α-invariance sub-bullet (and the temporal/spatial lattice-decomposition sub-bullet) actually lives in LIVING_REFERENCE.md's Axiom 3 entry. Corrected the citation to point at LIVING_REFERENCE.md and noted CLAUDE.md's bare-form scope explicitly. The boundaries-mechanism routing path (entry-point bootstrap → cross-cutting sidecar → this entry) is unchanged; this is a citation-fidelity fix, not a structural change.
- **Closes:** D12c Finding 7 (citation-fidelity hairline).
- **Severity:** n/a — closure record

---

## 2026-05-02 — Subtopic-index bootstrap directive coverage extended (post-D12 followup)

- **Action taken:** Bootstrap directive blockquote added to all 26 subtopic-level `index.md` files (one level below volume) with adjusted relative paths: `../claims-boundaries.md` for volume scope, `../../claims-boundaries.md` for cross-cutting. Chapter-level (level 3+) indexes intentionally not yet covered — defer until measurement shows residual need.
- **Closes:** "Bootstrap directive coverage gap on subtopic / chapter indexes" (D12c) — partially. Subtopic level addressed; chapter level still open as explicit deferral.
- **Closes:** "vol4 up-link label diverges from sibling volumes" (D12b Warning 2) — fixed `[↑ Entry Point]` → `[↑ AVE Knowledge Base]`.
- **Closes:** "Missing `<!-- leaf: verbatim -->` marker on two vol3 leaves" (D6a Note 8) — added marker to `sonoluminescence-derivation.md` and `kolmogorov-spectral-cutoff.md`.
- **Severity:** n/a — closure record

---

## 2026-05-02 — D12 final validation findings closed within scope

- **Surfaced by:** kb-accuracy-reviewer (D12a) and kb-structure-reviewer (D12b)
- **Description:** Final adversarial validation reviews ran. All Critical and Warning findings within boundaries-mechanism scope have been addressed inline:
  - Cross-cutting Hubble entry footer falsely listed vol2 → corrected to vol1, vol3 (with vol2-Hubble-gap surfaced as separate followup above).
  - Cross-cutting ξ_topo entry counting error ("three calibration inputs" with 4 listed) → fixed to "four CODATA constants" with explicit reference to the 3 canonical hardware scales.
  - Cross-cutting sidecar stale "Status: stub" note ("four most prominent tripwires" when there are now 9) → updated to "Status: active" with accurate enrichment history.
  - Volume sidecar canonicality preambles enumerated 4 of 9 cross-cutting tripwires → all 7 preambles updated to drift-proof phrasing ("see cross-cutting sidecar for canonical list; do not infer from this preamble").
  - Cross-cutting Framework-Derived vs Clay-Rigorous footer cited `.tex` source files → corrected to KB leaf paths under `vol2/nuclear-field/ch12-millennium-prizes/`.
  - CONVENTIONS.md sidecar structure block had PATH-STABLE on wrong line → corrected to line 3 with explanation.
  - CONVENTIONS.md preamble template enumerated 4 entries → corrected to drift-proof phrasing.
  - Entry-point bootstrap directive lacked per-volume hyperlinks → all 7 volume sidecar links now hyperlinked from the directive.
  - D12c MAD measurement confirmed K=0 → K=5 retractions; mechanism produces intended causal effect.
- **Items not addressed inline (deferred to other followups):** vol4 up-link label inconsistency (above), common/index.md "genuinely zero free parameters" qualifier (above), bootstrap directive coverage gap on subtopic indexes (above), vol2 missing Hubble entry (above).
- **Severity:** n/a — closure record
