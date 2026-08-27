### ENTRY 2026-08-03-mr-handoff-mechanical (2026-08-03): MR-handoff mechanical batch — verified value fixes, cross-wire repairs, ratified-fork propagation

- **Class: EXECUTION of MECHANICAL-AFTER-VERIFY items from the 2026-08-03 MR-handoff decision docket.** No adjudication is taken here. Every site was **re-verified by content** before editing (line numbers had drifted; see the cite-re-pin correction file). Every value written was **recomputed two ways** from `src/ave/core/constants.py` by this lane, not copied from the handoff.
- **Rule-12 discipline:** every struck token/value is quoted verbatim and dated at its own site; nothing is deleted; no struck slot is refilled with an unverified successor.
- **Held items NOT touched** (gated ch08/ch15 ringdown wave; Petermann family; Grant-ruling-gated sites): `08_gravitational_waves.tex` in full, `14_phase_diagrams.tex:105`, `15_black_hole_orbital_resonance.tex:322`, `q-g19a-petermann-saliency-closure.md`.
  - 🔵 *(**Path qualifier + hold verification, 2026-08-03 repair pass.** The bare filenames above read as one volume and are **two**: `08_gravitational_waves.tex` and `15_black_hole_orbital_resonance.tex` are `manuscript/vol_3_macroscopic/chapters/`, but **`14_phase_diagrams.tex` is `manuscript/vol_9_vacuum_datasheet/chapters/`** — there is no `14_phase_diagrams.tex` under vol\_3, so the unqualified list is not resolvable as written. Full paths: `manuscript/vol_3_macroscopic/chapters/08_gravitational_waves.tex`, `manuscript/vol_9_vacuum_datasheet/chapters/14_phase_diagrams.tex`, `manuscript/vol_3_macroscopic/chapters/15_black_hole_orbital_resonance.tex`, `manuscript/ave-kb/vol2/particle-physics/ch06-electroweak-higgs/q-g19a-petermann-saliency-closure.md`. **Hold verified by blob, not by assertion:** `git hash-object` on each of the four (plus the staged `manuscript/ave-kb/vol3/gravity/ch08-gravitational-waves/gw-propagation-lossless.md`) is **byte-identical to `origin/main`** — 5/5 untouched through both the original batch and the repair pass.)*

> 🟠 **REPAIR PASS 2026-08-03 (post-review; Rule 12 — no prior text in this entry is deleted, and every amendment is sited where the finding lives rather than collected at the end).** Seven repairs landed on top of `ae96ce22`, each recorded inline above/below at its own item: **(R1)** the $\rho_{bulk}$ sweep was scoped to `manuscript/` at 3 s.f. and read as corpus-complete — two `src/` sites (one a **live hardcode in an executed code path**) and the 4-s.f. `sagnac-rlve` twins were missed and are now repaired, with the historical `research/` tier enumerated and deliberately not edited (**§B6 amendment**). **(R2)** a same-form leaf the re-keying never reached is **flagged, not re-keyed**, because re-keying it is a ruling — the operating point moves by $1/\alpha$ (**§B8-adjacent**). **(R3)** the print chapter was left printing one constitutive equation two ways; the in-place swaps are **reverted to note-only** per the chapter's own Grant-merged precedent, value work retained (**§B8 ruling**). **(R4)** the B2 receipt's quoted division did not equal its quoted result; one canonical input elected (**§B2**). **(R5)** the staged ch08 ratio print carries a **second independent rounding** on top of the $\ell_{node}$ slip (**§B1**). **(R6)** three of this entry's own line-cites drifted again under its own edits (**§B3, §B11, and the cite-re-pins correction file**). **(R7)** the gw test tolerance, the `vol_9` path, and the commit count (**§B1, §B10, §Batch composition**). **Nothing held was touched; nothing adjudicated.**

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

> 🔴 **RECEIPT AMENDMENT 2026-08-03 (Rule 12 — the bullet above is preserved verbatim; this note corrects one clause of it so the ringdown-wave implementer inherits the true picture and not a tidier one).** The struck clause is: *"The division in the print was correct; only the input was wrong."* **That is true of the voltage leg and NOT true of the ratio leg.** The two legs fail differently, and the staged fix must not be planned as if they failed the same way:  <!-- rule12-freeze: base=3c6305f51bb3d277e56a2091b69300293d0c6b58 region=above offset=0 lines=27 bytes=4957 sha256=c5f396dcb54d618d0a3afb472035ca64cf671ab0c41327b05bcbb5403670ae02 -->
>
> | leg | slipped chain produces | print says | relation |
> |---|---|---|---|
> | **voltage** | $7.2739\times10^{-20}$ V | "$\sim10^{-19}$ V" | **exact** — a faithful order-of-magnitude statement of the slipped number. The slip fully explains it. |
> | **ratio** | $1.4235\times10^{-25}$ | "$\sim 2\times10^{-25}$" | **a SECOND, INDEPENDENT ROUNDING** — $2/1.4235 = 1.405$, i.e. the printed figure sits **$+40.5\%$ ($\approx$41%) above** what the slipped chain actually yields. A faithful round of $1.4235\times10^{-25}$ is $1.4\times10^{-25}$, not $2\times10^{-25}$. |
>
> **Consequence for the staged pass, stated plainly.** Fixing the $\ell_{node}$ slip alone reproduces the correct voltage but does **not** account for the printed ratio: the ratio print carries an extra, undocumented $\approx$1.4$\times$ upward round on top of the slip. So the ch08 sites are **two defects stacked**, not one propagated: (i) a 3-decade input slip, and (ii) a loose round applied to the already-wrong ratio. Both are superseded by the same replacement — the correct chain is $V_{GW} = 7.273895\times10^{-23}$ V and $V_{GW}/V_{snap} = \mathbf{1.4234658\times10^{-28}}$, recomputed above — but the implementer should record **both** in the strike, or the Rule-12 note at the site will mis-describe what was wrong. The same caution applies to the prose "Twenty-five orders of magnitude below saturation": the slipped chain's own exponent is $-25$, so that phrase is internally consistent with the slip and is corrected to twenty-eight by the same replacement.
- **Six corpus sites already carry 1.4e-28** and require no change: `vol6/appendix/geometric-inevitability/derived-numerical-constants.md:27` (formula **and** value), `vol3/gravity/ch08-gravitational-waves/ligo-gw-saturation-ratio.md:15`, `.../gw-detection-antenna.md:46`, `.../ch08-gravitational-waves/index.md:23`, `vol3/index.md:31`, `vol3/gravity/index.md:38`. Print `backmatter/03_geometric_inevitability.tex:167` also carries `1.42e-28`.
- **STAGED for the gated ch08 wave (3 sites, not 2):**
  1. `manuscript/vol_3_macroscopic/chapters/08_gravitational_waves.tex:61` — `$\sim 10^{-19}\;\text{V}$, which is $\sim 2 \times 10^{-25}$ times smaller` → $7.27\times10^{-23}$ V and $1.42\times10^{-28}$.
  2. `manuscript/vol_3_macroscopic/chapters/08_gravitational_waves.tex:355` — resultbox `\approx 2 \times 10^{-25}` → `\approx 1.42 \times 10^{-28}`; the following prose "Twenty-five orders of magnitude below saturation" → twenty-eight.
  3. ★ **NEWLY IDENTIFIED, not in the handoff list:** `manuscript/ave-kb/vol3/gravity/ch08-gravitational-waves/gw-propagation-lossless.md:42` carries the **same** `~1e-19 V` / `~1e-24` pair. It is the ch08 KB leaf and already carries a 2026-08-02 Rule-12 strike from the gated wave, so it is held with the rest of ch08 — but it must land in the same pass or the KB will be left self-inconsistent against the six sites above.
- **Also carrying the slipped chain (engine-side docstrings, NOT corpus claims, recorded not executed):** `src/ave/gravity/gw_propagation.py:849` and `src/tests/test_gw_propagation.py:122` both say "V_GW / V_SNAP ~ 10⁻¹⁹" — which is neither the correct ratio nor the slipped ratio (it is the slipped *voltage* misread as a ratio). Routed as an engine-docstring cleanup, out of scope for a corpus batch.

> 🟠 **ADDITION 2026-08-03, repair pass — the test that should have caught this cannot catch it. Routed WITH the docstring cleanup, not separately.** `src/tests/test_gw_propagation.py:125` asserts
> ```
> assert ratio < 1e-10  # Many orders of magnitude below saturation
> ```
> under a docstring (`:122`) claiming the ratio is $\sim10^{-19}$. **Run at HEAD, three ways:** the correct ratio is $1.4235\times10^{-28}$ ✓ passes; the 3-decade-slipped ratio is $1.4235\times10^{-25}$ ✓ **also passes**; and the docstring's own claimed $10^{-19}$ would ✓ **pass too**. The tolerance is **18 decades looser than the quantity it guards**, so the assertion is *true* but carries **zero discriminating power over exactly the defect B1 is fixing** — it would have stayed green through the entire slip. The sibling `test_gw_always_below_saturation` (`:131`, `assert ratio < 1e-3` against an actual $1.4235\times10^{-7}$ at $h=1$) is loose in the same way, though its stated purpose ("GW can NEVER saturate") is genuinely a bound-check, so its looseness is defensible where `:125`'s is not.
> **Routed (not executed here — this is a corpus batch and `src/tests/` is out of scope): tighten `:125` to the claimed tolerance**, i.e. assert against the canonical $1.42\times10^{-28}$ with a real relative bound rather than a 10⁻¹⁰ floor, **in the same pass as the `:122`/`:849` docstring cleanup**. Splitting them would leave a green test blessing a corrected docstring it does not actually check. Not a new work item — a scope addition to the already-routed engine-docstring cleanup.

---

#### B2 — `k_HB` decimal slip. **Executed, no cascade.**

`manuscript/vol_5_biology/chapters/07_solvent_damping.tex:41` — $11.2$ N/m → $\mathbf{1.12}$ N/m.

- **Receipt:** $k_{HB} = E_{HB}/d_{HB}^2 = 3.4575\times10^{-20}\,\text{J} / (1.754\times10^{-10}\,\text{m})^2 = \mathbf{1.1238}$ N/m. Both inputs are canonical and independently sourced: $E_{HB}=0.2158$ eV (this chapter `:20`; `ave-kb/vol5/.../hbond-op4-equilibrium.md`:79, Op4) and $d_{HB}=1.754$ Å (`ave-kb/vol5/index.md:26`, `ave-kb/CLAUDE.md:318`). The print preserved the mantissa under a single decade shift.

> 🔴 **DIGIT CORRECTION 2026-08-03 (Rule 12 quote-and-date; the struck digits are quoted here and the paragraph they sat in is preserved above, re-stated with the corrected digit rather than deleted).** The receipt bullet and the no-cascade bullet originally read **`= 1.1246` N/m** and **`3\times1.1246\times...`**. **That result did not equal its own quoted division:** $3.4575\times10^{-20} / (1.754\times10^{-10})^2 = 3.4575\times10^{-20}/3.076516\times10^{-20} = \mathbf{1.12384}$, not $1.1246$. The mismatch came from mixing the chain's **two canonical expressions of the same energy**, one per line. **One canonical input is now elected and used at every site:**  <!-- rule12-freeze: base=3c6305f51bb3d277e56a2091b69300293d0c6b58 region=above offset=0 lines=29 bytes=5522 sha256=dbdb3739f4b94088e9f69915a5664b42f1602ace31d8d41e3f1daa049563e231 -->
>
> | route | energy | $k_{HB} = E/d^2$ | status |
> |---|---|---|---|
> | $E_{HB} = 0.2158$ eV | $3.457497\times10^{-20}$ J | $\mathbf{1.1238}$ N/m | ★ **ELECTED** — the chapter's own cited input (`07_solvent_damping.tex:20`) and the **primary** Op4 output ($U_{raw}\times(1-\phi) = 0.8317 \times 0.2595 = 0.2158$ eV, `hbond-op4-equilibrium.md`:79) |
> | $E_{HB} = 4.98$ kcal/mol | $3.459952\times10^{-20}$ J | $1.1246$ N/m | not elected — the same energy re-expressed at 3 s.f. for comparison against the $5.02\pm0.05$ kcal/mol gas-phase dimer reference; the rounding is what reintroduces the 4th-digit difference |
>
> The two routes differ by **0.07%** — below every digit this chapter prints. **Nothing downstream moves:** the printed value is still $1.12$ N/m, and $B_{solvent} = 3.82\times10^{-27}$ S on **both** routes. **This correction is to the receipt's internal consistency only** (a quoted division that did not produce its quoted result), not to any corpus value. The same correction is applied at the print site's comment block, `manuscript/vol_5_biology/chapters/07_solvent_damping.tex`. ⚠ **The commit message of `f3422d1b` quotes the struck `1.1246`** and is immutable; this dated note is its correction of record.

- **Two-method no-cascade check.** The downstream $B_{solvent}$ at `:43` was **already computed on the correct 1.12**: $n k_{HB}\xi_{topo}^2/(2\pi f_{bb}) = 3\times1.1238\times(4.1490\times10^{-7})^2/(2\pi\times24.2\times10^{12}) = 3.82\times10^{-27}$ S, matching the printed $3.8\times10^{-27}$ S; the slipped $11.2$ would give $3.80\times10^{-26}$ S. The `:49` loading ratio is $G$-dominated and independent. **Only the `:41` transcription was wrong.**
- **Routed separately (recorded, not resolved):** this chain has **no KB home** for $k_{HB}$ — a repo-wide grep of `manuscript/ave-kb/` returns zero hits for the symbol, while both of its inputs are canonical. Noted in-comment at the site.

---

#### B3 — Lithium/Boron cross-wire. **Executed, print + KB in lockstep.**

- `manuscript/vol_6_periodic_table/chapters/02_chemistry.tex:22` — **before:** "the single unpaired outer nucleon orbiting the core at a massive **$11.84d$** gap"; **after:** "…at a massive **$9.72d$** gap".
- `manuscript/ave-kb/vol6/framework/chemistry-translation/quantum-vs-topological-shells.md:15` — byte-identical prose, same repair, same commit.
- **Receipts:** Lithium's own gap is $9.72d$ (`05_lithium.tex:44`, reinforced `:46`); $11.84d$ is booked to **Boron-11** (`vol6/claim-quality.md:152`, `clm-l416hl`: *"Solver places the Boron-11 7-nucleon halo at $R_{halo} = 11.84\,d$…"*; print `07_boron.tex:21/:31/:39/:53`).

> 🔵 **SELF-CITE RE-PIN 2026-08-03, repair pass (bookkeeping; no claim, value or disposition changes).** The boron print list above is quoted on **`origin/main` coordinates**, and **this batch's own B4 edit displaces three of the four** (the B4 label strike inserts a `% SCOPE:` comment block above the print paragraph). Post-branch the list reads **`:21` / `:52` / `:60` / `:74`** — i.e. `:21` unmoved, `:31→:52`, `:39→:60`, `:53→:74`. Both columns retained; the **content anchors** are primary and drift-proof: `R_{halo} = 11.8404 d` (`:21`), `The EE mutual coupling solver drops the Boron halo` (`:52`), the `Boron-11 Vacuum Density Flux` figure caption (`:60`), and `the $1/r$ falloff across the $11.84d$ gap` (`:74`). *(Same failure class as the three cites already re-pinned in `ae96ce22`: a batch's own in-place Rule-12 blocks displacing the batch's own line-cites.)*
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

> 🟠 **SCOPE AMENDMENT 2026-08-03, repair pass (Rule 12 — everything above in B6 is preserved verbatim and unedited; this note bounds it). THE TEN-SITE SWEEP WAS NOT CORPUS-COMPLETE, AND THE HEADING ABOVE READS AS IF IT WERE.** The struck framing is the B6 heading itself — *"**Executed at TEN sites — four more than the handoff named**"* — together with the receipt sentence *"**Ten sites re-pinned in the same commit** (two-method sweep …)"*. Both are true of what they covered and both **omit their own scope qualifier**: they covered `manuscript/` **at 3 significant figures only**. Three families were outside that net and were missed:  <!-- rule12-freeze: base=3c6305f51bb3d277e56a2091b69300293d0c6b58 region=above offset=0 lines=68 bytes=8229 sha256=3a668818a751e9f470fd0954d747d1ad1fd53297259197f7ef72376d72cca35c -->
>
> | tier | what | disposition |
> |---|---|---|
> | **A** | the ten `manuscript/` 3-s.f. sites listed above | re-pinned in `c5cf9fa3` (the original B6 commit) |
> | **B — MISSED: `src/`, live engine text** | `src/ave/core/lbm_3d.py`:9 — a docstring that **printed `7.92e6` while citing `constants.py:RHO_BULK` on the same line**, so the file contradicted itself in one sentence. `src/scripts/vol_4_engineering/simulate_sagnac_kinematic_entrainment.py`:65 (as-found) / `:84` (post-repair) — **a live hard-coded `rho_vacuum = 7.92e6` in an executed code path**, whose adjacent comment *also* wrote the formula as `mu_0 / (p_c * l_node^2)`, **omitting the $\xi_{topo}^2$ numerator entirely**. | **repaired in this pass.** The docstring re-pins to `7.9097e6` (5 s.f., matching the constant it cites). The script now **imports `RHO_BULK` from `ave.core.constants`** rather than transcribing a number, per `ave-canonical-source`; the comment formula is corrected to $\xi_{topo}^2\mu_0/(p_c\ell_{node}^2)$. **Live-fire:** the script was re-run end-to-end after the change and completes; `rho_vacuum` enters only via $Z_{vac} = \rho c$ inside a ratio already scaled by $10^{-15}$, so no printed figure or verdict moves. |
> | **C — MISSED: the 4-s.f. family** | `vol4/falsification/ch11-experimental-bench-falsification/sagnac-rlve.md` and its by-methodology twin `vol4/falsification/ch11-experimental-bench/sagnac-rlve.md`, both printing $\rho_{bulk} = 7.916\times10^6$ | **repaired in this pass** → $7.910\times10^6$ (4 s.f. of `RHO_BULK`). **No cascade, checked at the digit rather than asserted:** $19{,}300/7.910\times10^6 = 0.00243995$ vs the exact $0.00244004$ vs the struck value's $0.00243810$ — **all three print $0.00244$**. $v_{network} = 0.38$ m/s, $\Delta\phi = 2.07$ rad and $\kappa_{earth} = 6.97\times10^{-4}$ likewise unchanged. |
> | **D — historical `research/`** | six frozen dated documents, nine mentions | **recorded, deliberately NOT edited** — see below |
>
> **Tier D enumerated (frozen dated docs; re-pinning a value inside a dated result would falsify the record of what that document computed).** $7.92\times10^6$: `research/2026-05-17_C13b_bullet_cluster_prereg.md`:76; `research/2026-05-17_C14-DAMA_amplitude_prereg.md`:48; `research/2026-05-17_DAMA-bulk-transfer-function-reframe.md`:76. $7.916\times10^6$: `research/2026-05-17_parametric-coupling-kernel-prereg.md`:113; `research/2026-05-17_plumber-physical-audit-matched-LC.md`:27,:34,:37; `research/2026-05-18_flyby-anomaly-anderson-anchor-result.md`:237,:242.
>
> ★ **One tier-D site carries a live FALSE ATTRIBUTION — flagged, not fixed (dated-doc class).** `research/2026-05-18_flyby-anomaly-anderson-anchor-result.md`:237 reads verbatim: *"Canonical $\rho_{bulk} = 7.916 \times 10^6$ kg/m³ — substrate-derived as `RHO_BULK = ξ²μ₀/(p_c·ℓ²_node)` at `src/ave/core/constants.py` `RHO_BULK`. The provenance is **forward** (substrate → $\rho_{bulk}$ → $\kappa_{entrain} = 0.00244$ for Tungsten), NOT back-solved from $\kappa$. [provenance wording corrected 2026-06-03]"* — **`constants.py` `RHO_BULK` does not produce $7.916\times10^6$.** It produces $7{,}909{,}692.74$, i.e. $7.910\times10^6$. The sentence attributes a number to a named engine constant that does not yield it, and it already carries a *different* dated correction (2026-06-03) that repaired the derivation **direction** and left the **value** misattribution standing. Per flag-don't-fix and the frozen-document rule this is **recorded here and not edited there**; whether a dated research result may carry an in-place attribution correction is a corpus-posture question for Grant, not a mechanical one.
>
> **Two-method re-sweep after the repair pass** (whole repo; both methods run independently, per the grep-completeness discipline that a single pattern class false-negatives): literal `7.92`-with-density-context, literal `7.916`, and a `rho_bulk`/`RHO_BULK`-symbol context scan. **FINAL COUNT: 12 corpus sites re-pinned (10 tier-A + 2 tier-C) · 2 `src/` sites repaired (tier B) · 9 historical `research/` mentions across 6 files recorded-not-edited (tier D) · 0 remaining un-dispositioned.** *(The audit that routed this repair named "five" historical `research/` mentions; the re-sweep finds **nine across six files**. The larger number is reported rather than the routed one — surfaced, not silently reconciled.)* Receipt site for all tiers: `manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/lc-electrodynamics.md`, which carries the same amendment.

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

> 🟠 **METHOD ELECTION + ORCHESTRATOR RULING, 2026-08-03 (Rule 12 — the bullets above are preserved verbatim; the VALUE work they record STANDS. Only the equation-editing method changes).**  <!-- rule12-freeze: base=3c6305f51bb3d277e56a2091b69300293d0c6b58 region=above offset=0 lines=48 bytes=9348 sha256=c368a4256b13992103d7890d08763840bce3eb910821fb0e93c4caa9bcdac114 -->
>
> **The defect.** The print chapter was left printing the **same Axiom-4 constitutive equation two different ways, three subsections apart.** At §The Vacuum Varactor the chapter carries a Grant-merged correction (commit `03591777`, 2026-08-02) that is explicitly **note-only** — its own comment block states *"no equation, no number and no table row is edited"*, and `eq:varactor` still prints $V_{yield}$ with the note above it supplying *"read with $V_{yield} \to V_{snap}$"*. At §The Non-Linear Source Term the B8 pass **edited `eq:varactor_imd` and `eq:ip3` in place**. Two methods for one correction inside one chapter.
>
> **RULING (orchestrator, 2026-08-03): match the chapter's own Grant-merged precedent. Revert the in-place swaps to note-only.** Executed:
>
> | site | before this repair | after |
> |---|---|---|
> | `01_vacuum_circuit_analysis.tex` `eq:varactor_imd` (`:837` branch-tip → **`:857`** post-repair) | in-place: $C_0/\sqrt{1-(V/V_{snap})^2}$, $V_{snap}\approx511$ kV | **restored** to $C_0/\sqrt{1-(V/V_{yield})^2}$, $V_{yield}\approx43.65$ kV, read-with-substitution per the section note |
> | `01_vacuum_circuit_analysis.tex` `eq:ip3` (`:892` branch-tip → **`:927`** post-repair) | in-place: $\sqrt{4/3}\,V_{snap} \approx 590$ kV | **restored** to $\sqrt{4/3}\,V_{yield}\approx50.4$ kV, with the **banked 590,051 V receipt preserved in full** in the comment block and re-stated in the section note |
>
> **The value work is NOT reverted and is not in question.** $V_{IP3} = \sqrt{4/3}\,V_{snap} = 1.1547005 \times 510{,}998.95 = 590{,}051$ V $\approx 590$ kV, the exact $1/\sqrt{\alpha} = 11.70624$ move, and the both-directions cross-check ($\sqrt{4/3}\,V_{yield} = 50{,}404.8$ V reproducing the printed 50.4 kV to the digit) are **all retained** — now in the section note and the equation's comment block rather than in the equation body. A reader of the section gets the same number either way; the difference is purely where it is written.
>
> **ELECTED METHOD, recorded so the next lane does not re-litigate it: print side = NOTE-ONLY; KB side = IN-PLACE.** The split is deliberate, not an oversight. The KB leaf inherits the in-place convention from its own ratified upstream (`nonlinear-vacuum-capacitance.md`:27 prints the re-keyed resultbox directly), so `intermodulation-distortion.md` matching it is the consistent move on that side. The print chapter's precedent is note-only. **Print and KB therefore differ in METHOD and agree on CONTENT**, and both sides now say so explicitly. ⚠ **The commit message of `c363f2e6` describes the print edit as a "token swap … in Eq. `eq:varactor_imd`" and "the IP3 substitution at Eq. `eq:ip3`"** and is immutable; this dated note is its correction of record.

---

#### ★ B8-adjacent — a same-form leaf the re-keying pass did NOT reach. **FLAGGED, NOT RE-KEYED. Routed to Grant.**

`manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/parametric-coupling-kernel.md` cites `nonlinear-vacuum-capacitance.md` as its constitutive authority (`:46` as-found → `:80` post-banner) and then writes the **divergent** $C_{eff} = C_0/\sqrt{1-(V/V_{yield})^2}$ (`:48` → `:82`) — **the exact form that authority's resultbox no longer prints.** Live internal contradiction with its own cited upstream.

**Why this was NOT re-keyed with the rest of the family: re-keying it is a RULING, not propagation.** Unlike the IMD leaf — where the ratios are keying-invariant and only an absolute voltage column rescales — here the operating point *is* the physics, and it moves by exactly $1/\alpha$. Recomputed two ways from `src/ave/core/constants.py` (banked `V_SNAP`/`V_YIELD`, and independently $V_{yield}=\sqrt\alpha V_{snap}$; agreeing to the digit):

| quantity | as printed ($V_{yield}$-keyed) | if re-keyed to $V_{snap}$ | factor |
|---|---|---|---|
| $V_{pump}/V_\cdot$ | $0.428$ ("sub-yield") | $\mathbf{0.0366}$ | $\sqrt\alpha$ |
| $\delta_C/C_0$ | $4.59\%$ | $\mathbf{0.0335\%}$ | $\alpha$ |
| $\varepsilon_{coupled}^{per-node}$ | $0.288$ (order unity) | $\mathbf{0.0021}$ | $\alpha$ |
| $Q$ for $\kappa_{quality}=1$ ($Q\delta_C\ge2$) | $Q\gtrsim44$ | $\mathbf{Q\gtrsim5.98\times10^3}$ | $1/\alpha$ |
| the boxed closed form | $\delta C = e^2/(2m_ec^2)$ | $\delta C = \boldsymbol\alpha\,e^2/(2m_ec^2)$ | $\alpha$ |

Verified: $V_{pump} = \sqrt{2\alpha m_ec^2/C_0} = 18{,}694.13$ V on $C_0 = \varepsilon_0\ell_{node} = 3.4191\times10^{-24}$ F; $\delta C_{yield} = 1.56769\times10^{-25}$ F $= e^2/(2m_ec^2)$ **exactly** and $\delta C_{snap} = 1.14400\times10^{-27}$ F $= \alpha e^2/(2m_ec^2)$ **exactly**; ratio $137.03600 = 1/\alpha$. **The leaf's own headline — an appreciable sub-yield operating point, order-unity per-node coupling, and a "clean canonical form independent of $\alpha$" — is keying-dependent: under the $V_{snap}$ keying the $\alpha$-independence is an artifact, not a property of the substrate.** Re-keying would change the leaf's physical characterization, its detection-probability magnitude and its detector-class applicability. **This lane does not take that.**

**Landed instead: a flag-don't-fix banner** at the head of the leaf naming the contradiction, the two keying candidates, and the routed question. **Two other unbannered same-form sites** got pointer banners in the same commit: `biquaternion-complex-coupled-network-equations.md`:99 (whose resultbox is titled *"Keyed saturation (Grant-ratified sector split)"* — a ratification label sitting on a keying a later Grant ruling re-keyed) and `vol9/ch3-pin-port-configuration/vacuum-node-im3-distortion.md`:79 (where the **chord-candidate E-vs-B asymmetry is NOT exposed** — it turns on which drive variable keys which grade, orthogonal to which wall normalizes $A$ — but the **magnitude** leg riding on $A^2$ is; named, not evaluated).

**ROUTED TO GRANT (verbatim):** *"is the α-slew pump squeezing the BOND (A1 compliance — re-key, and sub-yield stops meaning what the leaf says) or twisting the TRANSVERSE sector (T2 — V_yield stands and only the divergent-form notation is wrong)?"*

**Also recorded, not fixed (smaller, same leaf):** `:23`/`:72` as-found (`:57`/`:106` post-banner) print $\delta_C/C_0 \approx 4.57\%$; the leaf's own $\tfrac14(V_{pump}/V_{yield})^2$ recomputes to $4.585\%$ — a $0.3\%$ arithmetic drift **within** the printed keying, independent of the fork. It should settle in the same pass, since the fork decides whether that cell survives.

---

#### B9 — Fragment cite re-pins. **Six executed as a consolidated dated correction file; the seventh is collision-fenced.**

See `2026-08-03-mr-fragment-cite-repins-correction.md`. Summary: gw `:34→:42`, neon `:48→:65`, Si `:512→:579`, varactor `:720→:787` / `:756→:823`, poisson `:11→:33`, rho `:155→:177`.

**★ `bingham :36→:66` was NOT executed, and the reason is a scope finding.** That cite does **not** live in an `mr-*` docket fragment. Two-method search (`grep -ri bingham _orchestration/docket-entries/` → zero hits; `grep -rn analytical_summaries _orchestration/docket-entries/` → zero hits) locates it in the **board**: `_orchestration/2026-08-02_manuscript-reconciliation-board.md:60`, the vol0 finding header citing `02_analytical_summaries.tex:36` (actual: `:66`). The board is **not a docket fragment** and is currently touched by **two open branches** (`docs/mr-board-corrections-0803`, `docs/mr-epic-closeout`). Editing it here would collide. **Routed to whichever board lane lands next.**

---

#### B10 — D7-F1 split-close. **RECORD ONLY, both legs.**

- **Ledger leg: CLOSED.** The prep audit re-verified all five Table-I rows to the digit; `papers/2026_birefringence_letter/provenance.md:129` carries the v3-footing completion and `:131` the #844↔D7 merge-note stating *"the Table-I block above discharges D7-F1"*.
- **★ ENGINE leg: RE-DOCKETED as a named successor, NOT closed.** Verified at HEAD this session:
  - `src/ave/bench/birefringence.py:252` `delta_n_qed_electric_pvlas(E, *, geometry="propagating")` accepts **only** `"propagating"` (`:276`) and `"static"` (`:278`) — **there is no `"instantaneous"` branch**, while the sibling `coefficient_ratio_differential_pvlas` at `:391` *does* carry all three (`:445`/`:447`/`:449`). The asymmetry is real and live.
  - `src/scripts/vol_9_device/birefringence_gap1_hibef_feasibility.py:187` still calls it with `geometry="propagating"`. 🔵 *(**Path qualifier, 2026-08-03 repair pass.** `src/scripts/` carries **two** vol-9 directories — `vol_9_device/` and `vol_9_vacuum_datasheet/` — so a bare "the vol\_9 script" is ambiguous in this repo. The call site is **`vol_9_device/`**, verified by content, and `:187` re-verifies at HEAD. The three-geometry sibling calls (`coefficient_ratio_differential_pvlas`) sit in the **same** file at `:385`/`:388`/`:390`, which is what makes the asymmetry visible inside one file.)* ★ **AND: the docket named ONE caller; a repo-wide re-grep finds TWO.** `src/scripts/vol_9_device/birefringence_prior_art_exposure_scan.py`:214 also calls `delta_n_qed_electric_pvlas(E, geometry="propagating")` (imported at `:67`). It is subject to the identical missing-`"instantaneous"`-branch exposure and **was not named** in the B10 record. Recorded, not executed — the successor lane must re-render **both** callers, and `vol_9_vacuum_datasheet/` contains none (checked: 4 files, zero hits).
  - `provenance.md:129` discloses the v2-vintage engine helper (*"the src helper still returns the v2 ratio"*).
- **Upstream of the exposure-plane figure re-render.** Both legs re-render together at the next submission revision. **Recorded, not executed** — this batch does not touch `src/ave/bench/` or the paper figures. 🔵 *(**Scope-fence qualifier, 2026-08-03 repair pass:** that sentence names two fenced areas and the caller above sits in **neither** — it is in `src/scripts/vol_9_device/`, a third location. The fence still holds in effect (this batch does not edit it either), but as written it under-describes the fence. Stated so the successor lane knows the engine leg spans `src/ave/bench/birefringence.py` **and** its `src/scripts/vol_9_device/` caller, not the library alone.)*

---

#### B11 — `mr-k2g` item (b). **DOES-NOT-VERIFY; receipt requested from the epic.**

The item states: *"`manuscript/ave-kb/common/appendices-overview.md` is BEHIND the manuscript on the Vol-0 appendix state (inverted mirror) — the KB leaf blesses appendix text the sweep is about to strike."*

Its one testable implication is **refuted** at HEAD:

- `manuscript/ave-kb/common/appendices-overview.md:71-76` carries the **drop banner**, not a blessing: *"DROPPED CLAIM (2026-04-20 audit): a prior bullet listed a second τ_yield formula `ℏc/(α² ℓ_node⁴) ≈ 7.21×10³⁴ Pa (Bingham-Plastic Limit)`. Removed because: (a) no derivation anywhere in the manuscript; (b) Planck-scale dimensional estimate…; (c) stated value off by 10⁶·⁴… Do not re-add without a derivation."* — live since **2026-04-20**.
- `manuscript/vol_0_engineering_compendium/chapters/02_analytical_summaries.tex:104` carries the **`[DE-CLAIM 2026-08-02]`** note citing that same KB banner. 🔵 *(**Self-cite re-pin 2026-08-03, repair pass:** `:104` is the `origin/main` coordinate; this batch's own B6 site-10 re-pin inserts a 9-line Rule-12 comment block above it, so post-branch it reads **`:113`**. Content anchor, drift-proof: the `\noindent\textbf{[DE-CLAIM 2026-08-02] Macroscopic Rheological Yield Stress (Bingham-Plastic Limit).}` paragraph opener. Bookkeeping only — the B11 finding is unchanged.)*

So on this axis the KB **leads** the manuscript by ~3.5 months and the manuscript has since caught up. **Receipt requested:** which specific `appendices-overview.md` line was read as "blessing appendix text"? Without it the item cannot be actioned. *(The one thing this lane did change in that leaf is `:64`'s $\rho_{bulk}$ value under B6 — a value re-pin, unrelated to the τ_yield axis.)*

---

#### Batch composition (recorded 2026-08-03, repair pass)

**This batch is EIGHT commits on `docs/mr-handoff-mechanical-0803`, not nine.** Verified two ways against `origin/main` @ `66fc7e69`: `git rev-list --count origin/main..HEAD` → **8**, and an explicit enumeration → `32a51a6c` (B1) · `f3422d1b` (B2) · `2e026d30` (B3/B4/B5) · `c5cf9fa3` (B6) · `e8fd371b` (B7) · `c363f2e6` (B8) · `758320a2` (B9/B10/B11) · `ae96ce22` (self-cite accuracy). Recorded because the batch was described in review as nine; the count is **8** at `ae96ce22`, plus the repair-pass commits that follow this note. **The eleven B-items map onto eight commits, not one-to-one** — `2e026d30` carries B3+B4+B5 and `758320a2` carries B9+B10+B11 — which is the likely source of the miscount. Item-count and commit-count are different quantities and are now both stated.

#### Validation

- `make verify` → exit 0; `verify-md-links` gating errors **0**; `verify-docket-keys` clean.
- `make refresh-kb-metadata` run after KB edits; idempotent on re-run.
- Pure-AVE-corpus: clean.
- Collision fence re-checked at branch time against all open branches — `kb/petermann-artifact-record`, `research/coldq-pole-v2p3`/`v2p4`, `kb/wall-taxonomy`, `docs/mr-addenda-0803`, `docs/mr-board-corrections-0803`, `docs/mr-epic-closeout`. **One overlap avoided by fencing** (the board, per B9). No file in this batch is touched by any open branch.
