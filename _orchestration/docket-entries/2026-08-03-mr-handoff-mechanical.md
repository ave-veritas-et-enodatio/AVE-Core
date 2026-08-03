### ENTRY 2026-08-03-mr-handoff-mechanical (2026-08-03): MR-handoff mechanical batch — verified value fixes, cross-wire repairs, ratified-fork propagation

- **Class: EXECUTION of MECHANICAL-AFTER-VERIFY items from the 2026-08-03 MR-handoff decision docket.** No adjudication is taken here. Every site was **re-verified by content** before editing (line numbers had drifted; see the cite-re-pin correction file). Every value written was **recomputed two ways** from `src/ave/core/constants.py` by this lane, not copied from the handoff.
- **Rule-12 discipline:** every struck token/value is quoted verbatim and dated at its own site; nothing is deleted; no struck slot is refilled with an unverified successor.
- **Held items NOT touched** (gated ch08/ch15 ringdown wave; Petermann family; Grant-ruling-gated sites): `08_gravitational_waves.tex` in full, `14_phase_diagrams.tex:105`, `15_black_hole_orbital_resonance.tex:322`, `q-g19a-petermann-saliency-closure.md`.

---

#### B1 — LIGO GW saturation ratio. **KB site fixed; ch08 sites STAGED with receipt.**

**Executed:** `manuscript/ave-kb/common/temporal-saturation-regime-classifier.md:353` — `~10^-24` → `1.42e-28`, Rule-12 strike + full arithmetic in-place.

**Held-item ruling applied:** the ch08 *file* is inside the gated ringdown wave, so per the handoff's own fallback the `:61`/`:355` fixes are **staged, not executed**. Arithmetic receipt, banked here so the gated wave can land them without re-deriving:

| quantity | value | source |
|---|---|---|
| $\ell_{node}$ | $3.8615926772428334\times10^{-13}$ m | `constants.py` `L_NODE` $=\hbar/(m_ec)$ |
| $V_{snap}$ | $510{,}998.9499961642$ V | `constants.py` `V_SNAP` $=m_ec^2/e$ |
| inputs | $h=10^{-21}$, $f=100$ Hz | the leaf's own |
| $V_{GW} = h\,c\,\ell_{node}\,2\pi f$ | $\mathbf{7.273895\times10^{-23}}$ V | recomputed |
| $V_{GW}/V_{snap}$ | $\mathbf{1.4234658\times10^{-28}}$ | recomputed |

- **Diagnosed cause of the outlier family: a 3-decade $\ell_{node}$ slip** — $3.86\times10^{-10}$ m used where $3.86\times10^{-13}$ m belongs. Substituting the slipped length reproduces the outliers exactly: $V_{GW}=7.2739\times10^{-20}$ V (printed as "$\sim10^{-19}$ V") and ratio $1.4235\times10^{-25}$ (printed as "$\sim 2\times10^{-25}$"). The division in the print was correct; only the input was wrong.
- **Six corpus sites already carry 1.4e-28** and require no change: `vol6/appendix/geometric-inevitability/derived-numerical-constants.md:27` (formula **and** value), `vol3/gravity/ch08-gravitational-waves/ligo-gw-saturation-ratio.md:15`, `.../gw-detection-antenna.md:46`, `.../ch08-gravitational-waves/index.md:23`, `vol3/index.md:31`, `vol3/gravity/index.md:38`. Print `backmatter/03_geometric_inevitability.tex:167` also carries `1.42e-28`.
- **STAGED for the gated ch08 wave (3 sites, not 2):**
  1. `manuscript/vol_3_macroscopic/chapters/08_gravitational_waves.tex:61` — `$\sim 10^{-19}\;\text{V}$, which is $\sim 2 \times 10^{-25}$ times smaller` → $7.27\times10^{-23}$ V and $1.42\times10^{-28}$.
  2. `manuscript/vol_3_macroscopic/chapters/08_gravitational_waves.tex:355` — resultbox `\approx 2 \times 10^{-25}` → `\approx 1.42 \times 10^{-28}`; the following prose "Twenty-five orders of magnitude below saturation" → twenty-eight.
  3. ★ **NEWLY IDENTIFIED, not in the handoff list:** `manuscript/ave-kb/vol3/gravity/ch08-gravitational-waves/gw-propagation-lossless.md:42` carries the **same** `~1e-19 V` / `~1e-24` pair. It is the ch08 KB leaf and already carries a 2026-08-02 Rule-12 strike from the gated wave, so it is held with the rest of ch08 — but it must land in the same pass or the KB will be left self-inconsistent against the six sites above.
- **Also carrying the slipped chain (engine-side docstrings, NOT corpus claims, recorded not executed):** `src/ave/gravity/gw_propagation.py:849` and `src/tests/test_gw_propagation.py:122` both say "V_GW / V_SNAP ~ 10⁻¹⁹" — which is neither the correct ratio nor the slipped ratio (it is the slipped *voltage* misread as a ratio). Routed as an engine-docstring cleanup, out of scope for a corpus batch.

---

#### B2 — `k_HB` decimal slip. **Executed, no cascade.**

`manuscript/vol_5_biology/chapters/07_solvent_damping.tex:41` — $11.2$ N/m → $\mathbf{1.12}$ N/m.

- **Receipt:** $k_{HB} = E_{HB}/d_{HB}^2 = 3.4575\times10^{-20}\,\text{J} / (1.754\times10^{-10}\,\text{m})^2 = \mathbf{1.1246}$ N/m. Both inputs are canonical and independently sourced: $E_{HB}=0.2158$ eV (this chapter `:20`; `ave-kb/vol5/.../hbond-op4-equilibrium.md`, Op4) and $d_{HB}=1.754$ Å (`ave-kb/vol5/index.md:26`, `ave-kb/CLAUDE.md:318`). The print preserved the mantissa under a single decade shift.
- **Two-method no-cascade check.** The downstream $B_{solvent}$ at `:43` was **already computed on the correct 1.12**: $n k_{HB}\xi_{topo}^2/(2\pi f_{bb}) = 3\times1.1246\times(4.1490\times10^{-7})^2/(2\pi\times24.2\times10^{12}) = 3.82\times10^{-27}$ S, matching the printed $3.8\times10^{-27}$ S; the slipped $11.2$ would give $3.80\times10^{-26}$ S. The `:49` loading ratio is $G$-dominated and independent. **Only the `:41` transcription was wrong.**
- **Routed separately (recorded, not resolved):** this chain has **no KB home** for $k_{HB}$ — a repo-wide grep of `manuscript/ave-kb/` returns zero hits for the symbol, while both of its inputs are canonical. Noted in-comment at the site.

---

#### B3 — Lithium/Boron cross-wire. **Executed, print + KB in lockstep.**

- `manuscript/vol_6_periodic_table/chapters/02_chemistry.tex:22` — **before:** "the single unpaired outer nucleon orbiting the core at a massive **$11.84d$** gap"; **after:** "…at a massive **$9.72d$** gap".
- `manuscript/ave-kb/vol6/framework/chemistry-translation/quantum-vs-topological-shells.md:15` — byte-identical prose, same repair, same commit.
- **Receipts:** Lithium's own gap is $9.72d$ (`05_lithium.tex:44`, reinforced `:46`); $11.84d$ is booked to **Boron-11** (`vol6/claim-quality.md:152`, `clm-l416hl`: *"Solver places the Boron-11 7-nucleon halo at $R_{halo} = 11.84\,d$…"*; print `07_boron.tex:21/:31/:39/:53`).
- **Scope:** value cross-wire only. Boron's $11.84d$-vs-Horizon-limit interpretation is untouched and keeps its solidity-0.40 fit disclosure.

---

#### B4 — Boron `d` mislabel. **Executed.**

`manuscript/vol_6_periodic_table/chapters/07_boron.tex:23` — "the axiom-derived **proton charge radius** (gyroscopic spin radius of the cinquefoil knot)" → **spin radius**; the parenthetical was already correct and is kept.

- **Aligns with** `01_computational.tex:94` — *"the **proton spin radius** $d$ — the radius of a single nucleon's gyroscopic orbit"* — which derives it at `:91-104` from the Axiom-1 standing-wave condition (engine `D_PROTON`).
- **Coincidence flag (why the mislabel survived):** $d = 4\hbar/(m_pc) = \mathbf{0.8412}$ fm sits within **0.02%** of the CODATA-2018 proton **charge** radius $r_p = 0.8414$ fm. Numerically near-degenerate, physically distinct. AVE does not derive $r_p$ here and nothing in the chapter depends on identifying the two.

---

#### B5 — Magnesium alloy overclaim. **Demoted, body preserved.**

`manuscript/vol_6_periodic_table/chapters/14_magnesium.tex:37` — paragraph preserved verbatim; a `[DEMOTED 2026-08-03 — structural/interpretive]` note added beneath it.

- **Governing non-claim:** `vol6/claim-quality.md:566` (`clm-f8k2um`) — *"Does NOT claim quantitative predictions of bond enthalpies, electronegativity scales (Pauling / Mulliken), reaction kinetics, or **material constants from the topology alone**. The mapping is structural / interpretive."*
- The demotion names the three specific overreaches: "derives directly from", "precisely because", and "**at comparable bond strength** … is the direct macroscopic manifestation". The last is an **assumed premise imported from materials data**, not a topological output. The $24/27 = 89\%$ figure is nucleon-count arithmetic, not a strength prediction. No number edited.

---

#### B6 — $\rho_{bulk}$ engine-lockstep. **Executed at TEN sites — four more than the handoff named.**

$7.92\times10^6 \to \mathbf{7.91\times10^6}$ kg/m³ (3 s.f., matching every site's convention).

- **Receipt, two methods, both `src/ave/core/constants.py`:** banked `RHO_BULK` $= 7{,}909{,}692.740007466$; recomputed `XI_TOPO**2 * MU_0 / (P_C * L_NODE**2)` $= 7{,}909{,}692.740007466$ — **bit-identical**. The formula and the constant are the same object; the drift ($+0.13\%$) was transcription-only.
- **★ SCOPE EXPANSION — flagged, not silent.** The handoff named six sites and asked for a two-method sweep for "any 7th". Method 1 (literal `7.92` scan) plus method 2 (independent `rho_bulk`-symbol context scan) found **four additional** sites carrying the identical wrong value under the identical formula. All ten were re-pinned, because leaving four behind would have *created* a corpus inconsistency rather than closed one:

| # | site | in handoff list? |
|---|---|---|
| 1 | `manuscript/vol_1_foundations/chapters/04_continuum_electrodynamics.tex:177` | yes |
| 2 | `manuscript/ave-kb/vol1/claim-quality.md:643` | yes |
| 3 | `manuscript/ave-kb/vol1/index.md:31` | yes |
| 4 | `manuscript/ave-kb/vol1/dynamics/index.md:25` | yes |
| 5 | `manuscript/ave-kb/vol2/appendices/app-c-derivations/index.md:20` | yes |
| 6 | `manuscript/ave-kb/common/appendices-overview.md:64` | yes |
| 7 | `manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/lc-electrodynamics.md:35` | **NO** — and it is the **canonical derivation leaf**; it is now the receipt site |
| 8 | `manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/index.md:20` | **NO** |
| 9 | `manuscript/backmatter/01_appendices.tex:92` | **NO** |
| 10 | `manuscript/vol_0_engineering_compendium/chapters/02_analytical_summaries.tex:44` | **NO** |

*(Line numbers above are as-found on `origin/main`. The three `.tex` sites are displaced by their own in-place Rule-12 comment blocks and read `:194` / `:99` / `:53` after this branch lands; the seven KB sites are single-line edits and do not move. The receipt site `lc-electrodynamics.md:35` carries the same note. Content anchor for all ten: the `\rho_{bulk} = ... \xi_{topo}^2 \mu_0 / (p_c \ell_{node}^2)` line.)*

- **Already correct, untouched:** `backmatter/02_full_derivation_chain.tex:1117`, `backmatter/12_mathematical_closure.tex:50`, `vol4/claim-quality.md:870`/`:882` (all $7.91\times10^6$).
- **No cascade.** $G_{vac} = \rho_{bulk}c^2$ ($7.11$–$7.12\times10^{23}$ Pa) and $c_L$ are unaffected at printed precision; $v_T=\sqrt{G_{vac}/\rho_{bulk}}=c$ is exact either way.
- **Not a de-claim.** At site 10 the note states explicitly that this is a value re-pin and does not touch that chapter's `[DE-CLAIM 2026-08-02]` entries.

---

#### B7 — Si-28 comment self-contradiction. **Corrected (this was owed BEFORE any Grant ruling).**

`manuscript/vol_4_engineering/chapters/01_vacuum_circuit_analysis.tex` (comment block above the Si-28 paragraph) — the landed comment elected a side: *"the KB row is the staleness candidate (routed)"*. **Struck.** That election contradicts the ratified rev-2 correction fragment `2026-08-02-mr-no-kb-home-correction.md:5-6`.

Three receipts, all re-verified verbatim by content at HEAD:

1. **Both values are FITS; neither is "the derived authority."** `simulate_element.py:10-15` (own scope note): the radii *"were 1-parameter Nelder-Mead fits against CODATA mass targets"*; `:388-389` *"Numerically optimized to ~80.174370d … matching the 26053.188074 MeV empirical nuclear target"*; `solve_silicon.py:5-9` *"a 1-parameter inverse-problem solve, NOT a forward prediction"*; `symmetric-core-collapse.md:10` fits $83.0d$ to the **same** 26053.188 MeV target. The "engine computed it therefore it's canonical" argument is not available.
2. **Two models, not one solver with a stale mirror.** `semiconductor-nuclear-analysis.md:20` = "Bare $K/r$ Model" (`simulate_element.py`); `:22` = "Semiconductor Junction Model"; `:26-32` reconciles per element (Si-28 row `:32` — bare **85.6d** vs semiconductor **83.0d**); `:34` rules *"The semiconductor model R values are the definitive mass-validated quantities."*
3. **Therefore `platonic-progression.md:24`'s 83.0 is the SEMICONDUCTOR/DEFINITIVE value and is NOT stale.**

**The true divergence pair** is different: KB **bare** cell $85.6d$ vs engine **bare** hardcode $80.174370d$ — same model, two values. And the print quotes a **bare-model** $R$ under a regime where the KB rules the **semiconductor** $R$ definitive.

**STILL ROUTED TO GRANT (untouched, no number edited):** the **meter choice** — is the print quoting the wrong model for that passage, or has the KB bare cell gone stale against the engine?

---

#### B8 — Varactor re-key. **Ratified-fork propagation executed; ONE value substitution, flagged.**

The A1-vs-T2 keying is **ratified, not newly adjudicated here**: `nonlinear-vacuum-capacitance.md:18` — *"Grade-fork RESOLVED = T2 (Grant 2026-06-30; `def-vyvsn1` adjudicated)"* — whose own resultbox `:27` already prints $C_{eff}=C_0/\sqrt{1-(V/V_{snap})^2}$; corroborated at `ee-bench-plateau.md:18-20` (★Supersession, PR #562/#558). Applied at the first print site 2026-08-02 (commit `03591777`), whose note is scoped *"this note covers this subsection only"* — **this batch is that scope note's un-propagated remainder.**

**KB twin executed FIRST** (`ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/intermodulation-distortion.md`): head sector banner + in-place re-key at the varactor resultbox and the IP3 resultbox + explicit Rule-12 notes at the drive table and the falsification criterion. **Then print:** `01_vacuum_circuit_analysis.tex` — sector banner added at §The Non-Linear Source Term, token swap $V_{yield}\to V_{snap}$ in Eq. `eq:varactor_imd`, and the IP3 substitution at Eq. `eq:ip3`.

**★ THE VALUE SUBSTITUTION — disclosed explicitly, not silent.**

- **Struck:** $V_{IP3} = \sqrt{4/3}\,V_{yield} \approx 1.155\times43.65 \approx \mathbf{50.4}$ kV.
- **Banked:** $V_{IP3} = \sqrt{4/3}\,V_{snap} = 1.1547005\times510{,}998.95 = \mathbf{590{,}051}$ V $\approx 590$ kV.
- **The $11.7\times$ move is $1/\sqrt{\alpha}$**, disclosed at the site: $V_{snap}/V_{yield} = 1/\sqrt{\alpha} = 11.70624$ **identically**.
- **Cross-check both directions:** $\sqrt{4/3}\times V_{yield} = 50{,}404.8$ V reproduces the struck 50.4 kV **to the digit** — confirming the struck value's *arithmetic* was right and only its *keying* was wrong; and $50{,}404.8\times11.70624 = 590{,}051$ V.
- **Arithmetic drift vs the handoff, recorded:** the handoff quoted $590{,}047$ V. Recomputing from `constants.py` `V_SNAP` gives $\mathbf{590{,}050.76}$ V. Both round to $590$ kV; the banked digits are this lane's recompute, not the handoff's figure.
- **Deliberately NOT edited in place:** the drive table. Its two columns transform *differently* — the ratio column and all derived $C/C_0$, $S$, dBc entries are keying-invariant, while the absolute kV column rescales by $11.706$. Swapping the header alone would have left the table internally inconsistent. A note under the table states the transform and gives the rescaled kV column.
- **Does NOT revive the retracted tabletop foothold.** The 2026-06-21 per-node retraction stands untouched at both sites: re-keying the *apparatus-voltage* axis does not change the per-node strain $A = E_{local}/E_{yield}$, the honest $\approx1.2\times10^{-9}$, or the facility-class $E\approx1.3\times10^{15}$ V/m. Stated explicitly in both banners.

---

#### B9 — Fragment cite re-pins. **Six executed as a consolidated dated correction file; the seventh is collision-fenced.**

See `2026-08-03-mr-fragment-cite-repins-correction.md`. Summary: gw `:34→:42`, neon `:48→:65`, Si `:512→:579`, varactor `:720→:787` / `:756→:823`, poisson `:11→:33`, rho `:155→:177`.

**★ `bingham :36→:66` was NOT executed, and the reason is a scope finding.** That cite does **not** live in an `mr-*` docket fragment. Two-method search (`grep -ri bingham _orchestration/docket-entries/` → zero hits; `grep -rn analytical_summaries _orchestration/docket-entries/` → zero hits) locates it in the **board**: `_orchestration/2026-08-02_manuscript-reconciliation-board.md:60`, the vol0 finding header citing `02_analytical_summaries.tex:36` (actual: `:66`). The board is **not a docket fragment** and is currently touched by **two open branches** (`docs/mr-board-corrections-0803`, `docs/mr-epic-closeout`). Editing it here would collide. **Routed to whichever board lane lands next.**

---

#### B10 — D7-F1 split-close. **RECORD ONLY, both legs.**

- **Ledger leg: CLOSED.** The prep audit re-verified all five Table-I rows to the digit; `papers/2026_birefringence_letter/provenance.md:129` carries the v3-footing completion and `:131` the #844↔D7 merge-note stating *"the Table-I block above discharges D7-F1"*.
- **★ ENGINE leg: RE-DOCKETED as a named successor, NOT closed.** Verified at HEAD this session:
  - `src/ave/bench/birefringence.py:252` `delta_n_qed_electric_pvlas(E, *, geometry="propagating")` accepts **only** `"propagating"` (`:276`) and `"static"` (`:278`) — **there is no `"instantaneous"` branch**, while the sibling `coefficient_ratio_differential_pvlas` at `:391` *does* carry all three (`:445`/`:447`/`:449`). The asymmetry is real and live.
  - `src/scripts/vol_9_device/birefringence_gap1_hibef_feasibility.py:187` still calls it with `geometry="propagating"`.
  - `provenance.md:129` discloses the v2-vintage engine helper (*"the src helper still returns the v2 ratio"*).
- **Upstream of the exposure-plane figure re-render.** Both legs re-render together at the next submission revision. **Recorded, not executed** — this batch does not touch `src/ave/bench/` or the paper figures.

---

#### B11 — `mr-k2g` item (b). **DOES-NOT-VERIFY; receipt requested from the epic.**

The item states: *"`manuscript/ave-kb/common/appendices-overview.md` is BEHIND the manuscript on the Vol-0 appendix state (inverted mirror) — the KB leaf blesses appendix text the sweep is about to strike."*

Its one testable implication is **refuted** at HEAD:

- `manuscript/ave-kb/common/appendices-overview.md:71-76` carries the **drop banner**, not a blessing: *"DROPPED CLAIM (2026-04-20 audit): a prior bullet listed a second τ_yield formula `ℏc/(α² ℓ_node⁴) ≈ 7.21×10³⁴ Pa (Bingham-Plastic Limit)`. Removed because: (a) no derivation anywhere in the manuscript; (b) Planck-scale dimensional estimate…; (c) stated value off by 10⁶·⁴… Do not re-add without a derivation."* — live since **2026-04-20**.
- `manuscript/vol_0_engineering_compendium/chapters/02_analytical_summaries.tex:104` carries the **`[DE-CLAIM 2026-08-02]`** note citing that same KB banner.

So on this axis the KB **leads** the manuscript by ~3.5 months and the manuscript has since caught up. **Receipt requested:** which specific `appendices-overview.md` line was read as "blessing appendix text"? Without it the item cannot be actioned. *(The one thing this lane did change in that leaf is `:64`'s $\rho_{bulk}$ value under B6 — a value re-pin, unrelated to the τ_yield axis.)*

---

#### Validation

- `make verify` → exit 0; `verify-md-links` gating errors **0**; `verify-docket-keys` clean.
- `make refresh-kb-metadata` run after KB edits; idempotent on re-run.
- Pure-AVE-corpus: clean.
- Collision fence re-checked at branch time against all open branches — `kb/petermann-artifact-record`, `research/coldq-pole-v2p3`/`v2p4`, `kb/wall-taxonomy`, `docs/mr-addenda-0803`, `docs/mr-board-corrections-0803`, `docs/mr-epic-closeout`. **One overlap avoided by fencing** (the board, per B9). No file in this batch is touched by any open branch.
