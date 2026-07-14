# THE QED-TRACE CHARTER — read QED's math as compressed medium data (ontology fence intact)

**Date:** 2026-07-14
**Register:** AVE substrate + EE (impedance, homogenization, saturation, port-Q). **Not** transverse-only-photon QED ontology; **not** the "suppressed quaternion physics" crank trope.
**Class:** Program charter (founding document). Every mapping below is **consistency-class until it fires**; the beta-function gate is the program's ONLY chord-class candidate.
**Repo of record:** **AVE-Core** — Grant ruling 2026-07-14 (overrides the sibling-repo routing; see Grant Rulings §0).
**Anchor / re-verification:** the grounding card was synthesized against AVE-Core HEAD `c12f2bdb`. This charter was **re-verified at the landing HEAD `db06ba82`** (origin/main at authoring; `c12f2bdb` is NOT an ancestor of `db06ba82` — the card's HEAD was one merge *ahead* of origin/main, so every receipt below was re-grepped at `db06ba82`). Line-number drift found on re-verification is recorded inline (see the Receipts table footnotes). QED-TRACE confirmed **absent** from the corpus by two methods at the anchor (`rg -l QED-TRACE` repo-wide → 0; grep of `_orchestration/index.md` + boards → 0); this is the founding document.

**Program (one line):** read QED's mathematical machinery — vacuum polarization Π(q²), running α, the Uehling potential, the propagator, the diagram sum — as **compressed data about the vacuum medium** (licensed), while keeping the ontology fence: no import of the transverse-only-photon ontology, myth-guard-first on the longitudinal/gauge sector (THE FENCE, §5).

**Headline honesty rail (stated first):** every mapping in the State Ledger is consistency-class until a gate fires. The beta-function gate is the one chord-class candidate, and **the grounding verdict is that it currently looks like a *category mismatch*, not a tuning gap** — the lattice's computed scale-dependent objects are all power laws, the corpus already refuted one log route, and the one existing running-α driver produced the WRONG SIGN. The gate below is shaped to test the *category question cheaply*, not to assume the derivation is live.

---

## §0 — GRANT RULINGS RECORDED (2026-07-14)

The four plumber questions (transcribed verbatim in §2.Q and §3) were put to Grant. Dispositions:

1. **Repo-of-record → CORE CARRIES.** The corpus routes the Feynman/QED interpretive walk to the AVE-QED sibling repo, not Core's KB — verbatim receipt: *"the interpretive walks (Feynman-diagrams-as-finite-network-scattering; …) are framings, not verified derivations — a research note at most, and the Feynman one belongs in the AVE-QED sibling repo, not Core's KB"* (`research/2026-07-08_electron-halfflux-selection_result.md:149-152`, Tier-3 PARKED). **Grant ruling OVERRIDES this routing: QED-TRACE lives in AVE-Core.** The override is recorded here against its receipt; the sibling-repo routing line is not silently contradicted — it is explicitly superseded by Grant decision for this program.
2. **The kernel-ON spend → GO.** Grant authorizes spending the kernel-ON (Axiom-4 saturation) route as the only candidate that could fake an all-scales fizz, knowing the one driver that tried it flat-lined at depth=1 with the wrong sign. Gate **in flight on branch `analysis/qed-trace-beta-gate`** (sibling lane; this Core charter carries the program, the gate spends in its own branch).
3. **The probe concession → CORE-SESSION DEFAULT (Grant veto window open).** Default: run the gate against the neutral A44 polarization form-factor (accepting it is power-law/dipole, not Coulomb), since the sourced-charge no-go closes the planted-monopole route. Recorded as the session default; Grant retains a veto window to instead frame the concession itself as the kill.
4. **The g−2 plumbing fork → OPEN, HELD.** Verbatim fork recorded in §3.Q4. The g−2 port reading is CONDITIONAL-GO, second priority behind the beta gate, held pending Grant's answer.

---

## §1 — THE STATE LEDGER (5 traced structures)

| # | Structure | What exists | Classification | Key receipts |
|---|---|---|---|---|
| 1 | **Renormalization = homogenization** | Π(q²)/running-α/Uehling tagged "Identical (RT-equivalence)" — but the register says **"argued (not independently computed here)"**, solidity 0.60, use-as-input-only; the strengthen-by literally names this gate: *compute Π(q²) from the cubic vertex with the BZ cutoff and show it equals QED's −(α/3π)q²ln(q²/m_e²) explicitly.* Homogenization machinery exists (#669 ksweep, Bloch quartic) but is linear / kernel-OFF and power-law. BZ loop integral exists but is a q-independent scalar. | **DERIVATION-TARGET (the one fireable gate).** Current "match" = consistency-by-import. | `q-g20f-vacuum-polarization.md:28,32,47`; `vol2/claim-quality.md:1485-1488`; `research/2026-07-13_srs-vertex-ksweep-backscatter_RESULT.md:19,32-37`; `src/ave/qed/brillouin_cutoff.py:116-151` |
| 2 | **Ward = conservation identities / anomalies = identity-breaks** | Ward-side HOST EXISTS: Axiom-3 Noether output ("Energy conservation and U(1) gauge symmetry follow as Noether consequences") + the identity-break leaf's "discriminating content exists ONLY at identity-BREAKS." Anomaly-side: literal "Ward identity" and "chiral/triangle/axial/ABJ anomaly" ABSENT (two-method); only parity-selection adjacents (Δc=3 chiral screening, C6 kill-switch, Ω-freeze handedness). | **Ward row = DICTIONARY (relabel, cheap). Anomaly row = ABSENT / would be a MINT** with mandatory category-flag: parity-selection-by-dispersion ≠ quantum non-conservation of an axial current. | `common_equations/eq_axiom_3.tex:27`; `common/axiom-register.md:231`; `common/identity-break-test-design.md §2`; `chiral-screening.md:11,22,24`; `divergence-test-substrate-map.md:205` |
| 3 | **Propagator = driving-point impedance** | Green's function = lattice impulse response (dictionary row); recover-QED continuum propagator self-classed Class-C consistency, rel. err (kℓ)²/12. Loaded-Q port register fully built (α⁻¹ = radiative Q; T1's α⁻³ atom rung). | **DICTIONARY + CONSISTENCY — mostly done.** Do not re-tag Class-C as derivation. | `cem-methods-survey.md:43`; `brillouin-zone-uv-cutoff.md:61`; `theorem-3-1-q-factor.md:147`; `resonant-lc-solitons.md:122` |
| 4 | **Series divergence = cold-lattice linearization breakdown** | Rich adjacent scaffold: Regime-I amplitude expansion S(r)=1−r²/2−…, small-signal limit r₁=√(2α), infinity-discipline, instanton-area match ∫√(1−A²)dA=π/4. But the corpus's series is a **convergent finite-radius Taylor series** (branch point at r=1, the yield wall); QED's is an **asymptotic zero-radius n!-in-coupling series**. No corpus content on n!-asymptoticity (two-method absence). | **ORGANIZING METAPHOR, currently mis-mapped.** Landable as walk-note ONLY reframed to the wall-at-r=1 object the corpus owns. | `four-regimes.md:26-85`; `node-up-small-large-signal.md:66,157-189`; `vol2/claim-quality.md:1311`; `electron-unknot.md:63` ("rigorous AVE running-coupling derivation is an open problem") |
| 5 | **g−2's α/2π = port-coupling correction** | g=2 leaf disciplined: [G2-FORCED] FORM chord, VALUE peer-with-Dirac, ×2 = imported canonical double-cover. a_e = α/(2π) ALREADY exists via a *different* mechanism (on-site Axiom-4 detuning πα/2 × 1/π² form-factor, materialized as `G_MINUS_2_TREE`), currently **under-tagged** — called "canonically derived" at ≥3 sites with no VALUE=echo tag though it rides the same (V/V_snap)²=4πα keystone identity that was echo-scoped for α⁻¹. Port reading = walkable FORM candidate only. | **SECOND TARGET (FORM-level).** VALUE is echo by construction; competing-mechanism question open (§3). | `research/2026-07-08_electron-g2-selforbit_result.md:3,8,14,83`; `src/scripts/vol_2_subatomic/simulate_g2.py:9-14,52,116`; `src/ave/topological/cosserat.py:641-655`; `vol4/claim-quality.md:1563` |

**Two corpus flags riding the whole ledger:** (i) the Feynman-as-network walk is PARKED and was routed to the **AVE-QED sibling repo, not Core's KB** (`research/2026-07-08_electron-halfflux-selection_result.md:149-152`) — **overridden into Core by Grant ruling §0.1**; (ii) Core currently carries the *anti*-diagram framing (*"No Feynman diagrams or renormalization are required"*, `higgs-mass.md:77`) — the charter inverts this to "diagrams as compressed medium data" and **must reconcile, not silently coexist** (the reconciliation sentence is §4.RECON, flagged PENDING-GRANT sign-off).

---

## §2 — THE BETA-FUNCTION GATE (the one chord-class candidate)

**THE HONEST CATEGORY QUESTION — the grounding verdict, plainly:** the classical cold lattice, as currently built, **does not have the fluctuation structure to produce a logarithm.** QED's log is the signature of virtual pairs flat in d(ln k) across decades; a linear kernel-OFF lattice has exactly one scale (ℓ_node) and a band edge, and every scale-dependent object the corpus has actually computed is a power law: Bloch anisotropy (qℓ)⁴, monotonic band-edge R(k), lanew pair force p=−3. The corpus **already considered and refuted a log route** (*"the measured |φ| ~ r^{−1.4..−2.6} is 3D multipole falloff, not a 2D log"*, `research/2026-07-03_lanew-pair-field-form_prereg.md:117`). The only candidate fluctuation source is the Axiom-4 saturation kernel (kernel-ON), and the one driver that tried it collapsed to depth=1 with negligible running (`src/scripts/vol_2_subatomic/simulate_running_alpha.py:5-10`). Worse, the KB itself hands the all-scales-pair region to different physics — sub-Compton "α stops running" (`q-g20f:55`). **This is a category mismatch until the kernel-ON route proves otherwise. The gate exists to buy that answer cheaply.**

### §2.1 — Pieces ledger (what the derivation needs vs what exists)

| Piece needed | Status | Receipt |
|---|---|---|
| Embedded probe charge (sourced monopole) | **ABSENT / CLOSED ROUTE** — sourced-charge no-go: charge is unsourced-topological | `common/the-sourced-charge-no-go-cascade.md:34-45` (clm-nogo4l) |
| Induced polarization cloud at r/k | **PARTIAL** — A44 neutral form-factor exists, but static, globally-neutral, power-law (p=−3) | `research/2026-07-03_lanew-pair-field-form_prereg.md:22`; `jcoupling…note.md:122-127` |
| Screening length in the EM/charge sector | **ABSENT** — the Coulomb tail is massless and unscreened; only weak-sector Yukawa + atomic Debye exist | `substrate-perspective-electron.md:125`; `gauge-boson-masses.md:41-43` |
| Π(q²) with q-dependence + log coefficient | **ABSENT** (the KB's own strengthen-by TODO) | `vol2/claim-quality.md:1488` |
| α(k) / running-coupling solver | **ABSENT** (one exploratory unwired driver, self-labeled "Does NOT reproduce QED running") | `src/scripts/vol_2_subatomic/simulate_running_alpha.py:5` |
| BZ-regulated loop integral | **PRESENT (FORM-derived)** but scalar, q-independent, linearly-divergent integrand — not the log-divergent bubble | `src/ave/qed/brillouin_cutoff.py:131-149` |
| Effective-medium-vs-k machinery | **PRESENT** but linear / kernel-OFF | #669 ksweep; `k4-bloch-dispersion-quartic_result.md` |

### §2.2 — Gate shape (cheap-first)

Extend the existing #669 ksweep harness **with the kernel ON** (the only candidate fizz source) and the probe question pre-adjudicated by Grant (planted monopole is a closed route — either run against the A44 neutral form-factor per ruling §0.3, or don't run). Measure effective coupling vs scale across ≥2 decades. **Do NOT build an α(k) solver before the kernel-ON pilot shows any non-power-law scale mixing.** Gate spends on branch `analysis/qed-trace-beta-gate` (sibling lane per Grant ruling §0.2).

### §2.3 — Frozen bins (pre-registered before any run)

| Bin | Signature | What it means |
|---|---|---|
| **LOG-EMERGES** | genuine ln(q) dependence, QED sign (α grows at short distance), coefficient → −α/3π | The program's one chord: QED's log IS homogenization data; clm-bqtasn's strengthen-by closes positive |
| **RIGHT-FORM / WRONG-COEFFICIENT** | log, right sign, wrong prefactor | FORM chord / VALUE echo — files exactly into the forces-FORMS-imports-VALUES meta-finding |
| **WRONG-FORM** | power law in (qℓ_node), no log — the currently-expected outcome | Category mismatch CONFIRMED for the classical route; structure (1) demotes permanently to dictionary status; the RT-equivalence "identical" claim survives only as an appeal (consistency-scaffold), and the KB should say so |
| **WRONG-SIGN** | any running with α *weakening* at short distance (what the existing driver produced: 1/α_eff 137.026→137.032 rising with energy) | Worse than wrong-form: fires AGAINST the asserted q-g20f sign, which was inherited from the RT appeal, not computed — triggers demotion of the "Identical (RT-equivalence)" rows |
| **NULL/FLAT** | negligible running (the depth=1 collapse repeated) | Category mismatch confirmed at the kernel-ON route too; gate closes; running-α stays imported |

**Honest framing for the negative bins:** WRONG-FORM/NULL is not a shame result. QED computes its log from a quantized-fluctuation postulate the substrate doesn't carry; a clean negative converts "AVE reproduces QED running" from an unexamined assertion into a *scoped import*, which is exactly the honesty-lag the register (solidity 0.60, "don't build deeper") already demands.

### §2.Q — The plumber questions (verbatim, only-Grant)

1. **Repo-of-record** — resolved: CORE CARRIES (§0.1).
2. **The kernel-ON spend** — *QED's log is pairs fizzing at every scale between here and the node, and the cold linear lattice only has one mesh size and a band edge — do you want to spend the kernel-ON (saturation) route as the only candidate that could fake an all-scales fizz, knowing the one driver that tried it flat-lined at depth=1 with the wrong sign?* Resolved: GO (§0.2).
3. **The probe concession** — *the QED-style computation wants a planted charge to screen, but the sourced-charge no-go says the substrate won't source a static monopole — do we run the gate against the neutral A44 polarization form-factor instead (accepting it's power-law/dipole, not Coulomb), or is that concession already the kill and the gate should be framed as testing exactly that?* Resolved: core-session default = run against A44 neutral form-factor, Grant veto window open (§0.3).

---

## §3 — THE SECOND TARGET (g−2 port reading) — CONDITIONAL-GO, HELD ON Q4

**Status:** walkable candidate at FORM level only, and it is a **second mechanism for an already-occupied slot.** The port register exists and is exact (loaded Q = α⁻¹, one power of α per cycle out the radiative Z_EM port; ÷2π = per-cycle→per-radian is resonator-native). But `simulate_g2.py` **already** produces a_e = α/(2π) via on-site Axiom-4 dielectric detuning (πα/2 × 1/π²), materialized in the engine at `src/ave/topological/cosserat.py:641-655` (`G_MINUS_2_TREE`). A port derivation must either **supersede** that chain or be shown **degenerate** with it (KEEP-BOTH pattern), **declared up front** — otherwise it is substitution-not-retraction.

**Echo rails (mandatory, pre-committed in any pre-reg):** α is a retained input, so ANY a_e = α/(2π) matches Schwinger the moment α is imported — **VALUE = echo by construction, tag FORM=candidate-chord / VALUE=echo**, exactly as the g2-selforbit prereg pre-committed peer-with-Dirac (verbatim: *"g=2 is peer-with-Dirac AT THE VALUE LEVEL … Do NOT headline g=2 as an emergence-class distinct-value chord"*, `research/2026-07-08_electron-g2-selforbit_prereg.md:89`). The instrument-echo-trap applies: a third α-derived display reading the same number escapes nothing. The earnable content is only whether the ÷2π is *independently forced* from port geometry without importing the 1/π² form-factor, with α firewalled off the FORM path.

**Go/no-go: CONDITIONAL GO, second priority behind the beta gate,** gated on Grant's plumbing-fork answer (Q4 below, **OPEN / HELD** per ruling §0.4). Pre-reg requirements when it runs: (a) force ÷2π from the per-radian radiative-port leak with no 1/π² import; (b) declare supersede-vs-degenerate vs `simulate_g2.py` by name; (c) constants firewall as in the g2-selforbit leaf; (d) walk the sector-ownership of the *correction* first (μ rides (2,3) charge; T1 showed Z_EM port ≠ longitudinal trapping walls).

### §3.Q4 — THE g−2 PLUMBING FORK (verbatim, OPEN / HELD)

> **Q4 — The g−2 plumbing fork:** does the anomaly leak out the **radiative port**, or is it an **on-site dielectric detuning** — same number, two different pipes — i.e. should a port charter **supersede** `simulate_g2.py`'s on-site chain or **stand alongside it as a declared-degenerate second view**?

**Disposition:** OPEN. The supersede-vs-degenerate declaration is **mandatory before any port pre-reg freezes** (KEEP-BOTH default: declared-degenerate unless the port path is shown to strictly dominate). Held pending Grant.

### §3.HK — Housekeeping that lands REGARDLESS of Q4 (executed on this branch)

Independent of the fork, four items land as pure honesty housekeeping (the g2-selforbit prereg's own peer-with-Dirac pre-commitment is the governing convention):

- **(a) echo-tag propagation** to the a_e = α/(2π) cites currently reading "canonically derived" with no VALUE=echo tag: `dama-alpha-slew-derivation.md:43`, `preferred-frame-and-emergent-lorentz.md:131`, `mond-hoop-stress.md:55`, and the `simulate_g2.py` docstring — each gets **FORM=candidate / VALUE=echo (α imported)** consistent with the g2-selforbit peer-with-Dirac pre-commitment.
- **(b) coverage-matrix g=2 reconciliation** (`research/2026-06-17_electron-coverage-matrix.md:52` "the ratio derives" vs `:68` "g=2 POSITED (imported)") — reconciled per the g2-selforbit result's own resolution (`_result.md §6`): g=2 is a **FORM forced conditional on the canonical double-cover** (g = N_cover), *neither* purely imported *nor* independently derived from nothing.
- **(c) LIVING_REFERENCE / README status sync** (`LIVING_REFERENCE.md:276,278` bare ✅ vs `README.md:219,221` echo-tag + postdiction demotion) — LIVING_REFERENCE aligned DOWN to the README's honest status (KEEP-BOTH note).
- **(d) the electron 2-loop "10 ppm" caveat.** The electron 2-loop (Q-G19α Petermann) headline is **postulate-conditional** — n_q-additivity was chosen to match a PDG-tuned bisection and is **RESOLVED-NEGATIVE (2026-05-31, kernel winding-blind)** (`q-g19a-petermann-saliency-closure.md:8,14,110`); it must NEVER ride the charter as an unconditional forward match. The **muon's +4.6σ tension is the honest forward row** (`research/2026-06-17_electron-coverage-matrix.md:56`; `q-g27` +4.6σ genuine disagreement).

---

## §4 — THE ORGANIZING LAYER (ranked cheapest→dearest; lands-as-prose vs needs-minting)

1. **Gauge reading — LANDS AS CHARTER PROSE (dictionary row, no minting).** "Gauge = reference/bookkeeping freedom; only impedance/|Γ|/boundary observables are physical" is already corpus-native across ≥4 leaves (A→A+∇Λ = coordinate-boost freedom, `gauge-boson-masses.md:28-34`; *"Only the magnitude is physical … gauge-invariant content is |Γ|=1"*, `trampoline-analogy-primer.md:265`; F11 "gauge structure = bookkeeping", `physics-lineage-map.md:154,181`; A-state gradient-only, KB `CLAUDE.md` INVARIANT-S2). The charter row *collects*, originates no number. SECTOR⊥GAUGE (`electron-identification.md:47`, `window-blind-bounding-plane.md:57`) is the load-bearing carve.
2. **Ward ↔ conservation-identity class — LANDS AS DICTIONARY ROW (near-free relabel).** Axiom-3 Noether output + identity-break §2. Slightly dearer than #1 only because it introduces Ward vocabulary the corpus doesn't currently use.
3. **Anomaly ↔ identity-break — NEEDS MINTING, with the mandatory category-flag.** Hosts are anomaly-*adjacent* only (chiral dispersion high-pass, C6, Ω-freeze handedness). The row is tagged derivation-target/absent with the explicit caveat: **parity-violation-by-selection-rule ≠ chiral anomaly** (quantum non-conservation of a classically-conserved axial current). Do not upgrade "AVE carries chirality content" into "AVE hosts the anomaly."
4. **Series reading — WALK-NOTE ONLY, reframed.** The charter claims the object the corpus owns — the convergent amplitude expansion hitting its branch-point wall at r=1 (the tank yielding), with Regime-I convergence and r₁=√(2α) already worked — and **explicitly disclaims the n!-in-coupling asymptotic story** as a distinct, absent object. Landing text carries the **finite-radius-vs-asymptotic distinction as a named caveat**; Grant can veto the disclaim (folded into the gate questions if he wants the n! story chased, but the grounding verdict is it's a category error as pitched).

### §4.RECON — Reconciliation sentence (PENDING-GRANT SIGN-OFF)

The charter must reconcile the standing anti-diagram prose (*"No Feynman diagrams or renormalization are required"*, `higgs-mass.md:77`) with "diagrams as compressed data." The proposed reconciliation:

> **the diagram sum is QED's serialization format for medium response, not a competing ontology.**

**⚠ PENDING-GRANT SIGN-OFF — this sentence re-scopes standing Core prose (`higgs-mass.md:77`) and is NOT landed as canon by this charter.** It is recorded here as the proposed reconciliation; the two framings are flagged as needing reconciliation (not silent coexistence) but the resolution text awaits Grant. The honest reading: the diagrams are data *about the same structural content* AVE claims to derive directly.

**Consensus-bias discipline per structure (symmetric standard):** (1) beta — QED *actually computes* its log, so the symmetric standard does NOT rescue AVE's uncomputed match; but a clean lattice negative is an ontology difference, not a demerit. (2) Ward — the relabel is peer: QED's Ward identities are also Noether bookkeeping, no one calls them predictions. (3) propagator — Class-C consistency is the same footing on which QED "recovers" classical EM; cap both. (4) series — QED's n! divergence is QED's own unsolved wart; don't manufacture a match to it. (5) g−2 — Schwinger's α/2π is also one-power-in-imported-α; the value-match is echo in BOTH frameworks, so the honest arena is FORM-forcing, where the corpus's mechanism competition (on-site vs port) is a real question.

---

## §5 — THE FENCE (no-QED-garbage, verbatim-anchored at HEAD `db06ba82`)

**FENCED (ontology import — forbidden), verbatim-anchored:**
- Framing the V-sector scalar in QED-vector terms: *"the **real V-sector scalar grade** … is **physical, NOT Gauss-deleted** … It must **never** be framed in QED-vector terms"* (`vocabulary-register.md:541`, def-9a4f07; reinforced by the load-bearing guard at `:552` — *"never frame (a) in QED-vector terms, and never wire the winding into the breather's (V_inc,V_ref) phasor"*).
- Calling V the EM gauge potential — it is *"a medium order-parameter/port-voltage, never the EM gauge potential"* (`physics-lineage-map.md:263`).
- The myth-guard overclaim: *"'Heaviside deleted a physical mode' is **FALSE for standard EM** … Never inflate this algebra-level necessity into a derivation of the mode"* (`vocabulary-register.md:575`, def-9b3d05 acceptance guard).
- Asserting the transverse-only-vacuum ontology (AVE *adds* a real longitudinal DOF where Maxwell has only the gauge slot).
- Wiring the (2,3) charge-winding into the A1 breather phasor: *"never wire the winding into the breather's own phasor (V_inc, V_ref)"* (`master-equation.md:20`, the TWO-"3"s disambiguation).

**LICENSED (math-as-data — permitted):** the transverse photon = T₂ Cosserat shear wave (*"The photon is the K4-TLM's stable T₂-only bound state — a knotted transverse Cosserat shear wave"*, `photon-identification.md:8-11` — transverse-only is *correct for the propagating photon*); reading QED's transverse-sector machinery (Π(q²), running α, Uehling, propagator) as RT-equivalent compressed data about kernel+lattice (q-g20f already does this); the algebra-level necessity of the scalar slot as *identification only*.

**The charter-critical constraint:** QED-TRACE reads QED math as medium data — but in standard QED the longitudinal/gauge sector is precisely the part carrying NO physical DOF. Reading QED's gauge structure as *evidence for* AVE's real longitudinal medium DOF is exactly the forbidden inflation, and reconstructs the "suppressed quaternion physics" crank-trope the corpus flags as a **LIVE sociological threat** (`physics-lineage-map.md:265`). **License the transverse sector as data; handle the longitudinal/gauge sector myth-guard-first.**

**Housekeeping flag (stale cross-ref, verified at `db06ba82` — flag-don't-fix, NOT repaired by this charter):** `physics-lineage-map.md:263` cites the never-frame-in-QED-vector-terms ban at `vocabulary-register.md:499-513`, but that line range is the **`chirality` def-node**, not the ban; **def-9a4f07 (the V-sector ban) actually lives at `vocabulary-register.md:538-553`** (grep-confirmed this session). Surfaced for the auditor/owner to repair; not touched here (outside the D1/D2 scope).

---

## §6 — RECEIPTS TABLE (all re-verified at HEAD `db06ba82`)

| Claim in this charter | Receipt (file:line) | Re-verify note @ `db06ba82` |
|---|---|---|
| Feynman walk PARKED, routed to AVE-QED (Grant-overridden) | `research/2026-07-08_electron-halfflux-selection_result.md:149-152` | ✅ verbatim confirmed |
| Propagator recover-QED = Class-C consistency | `brillouin-zone-uv-cutoff.md:61`; `vol2/claim-quality.md:1591` | ✅ |
| Green's fn = lattice impulse response (dictionary) | `cem-methods-survey.md:43` | ✅ |
| Π/running-α/Uehling "Identical (RT-equivalence)" | `q-g20f-vacuum-polarization.md:28,32,47,55` | ✅ |
| Π match ASSERTED not computed; solidity 0.60; strengthen-by = the gate | `vol2/claim-quality.md:1485-1488` | ✅ |
| SECTOR⊥GAUGE / gauge = coordinate freedom | `gauge-boson-masses.md:28-34`; `window-blind-bounding-plane.md:57`; `electron-identification.md:47` | ✅ |
| "No Feynman diagrams required" anti-framing (recon target) | `higgs-mass.md:77` | ✅ verbatim confirmed |
| The fence + myth-guard verbatim | `vocabulary-register.md:541,552,575`; `photon-identification.md:8-11`; `physics-lineage-map.md:263,265`; `master-equation.md:20` | ✅ all verbatim confirmed; def-9a4f07 @ `:538-553` (see §5 stale-xref flag) |
| Homogenization base linear/kernel-OFF, monotonic band-edge | `research/2026-07-13_srs-vertex-ksweep-backscatter_RESULT.md:19,32-37` | ✅ |
| Log route already refuted in-corpus | `research/2026-07-03_lanew-pair-field-form_prereg.md:117,22` | ✅ verbatim confirmed |
| Sourced-monopole no-go | `common/the-sourced-charge-no-go-cascade.md:34-45` (clm-nogo4l) | ✅ |
| Unscreened massless Coulomb tail | `substrate-perspective-electron.md:125` | ✅ |
| Running-α driver: negligible + WRONG SIGN | `src/scripts/vol_2_subatomic/simulate_running_alpha.py:5-10` | ✅ self-labeled "Does NOT reproduce QED running" |
| BZ loop integral scalar/q-independent/finite | `src/ave/qed/brillouin_cutoff.py:116-151` | ✅ |
| g=2 FORM-forced, peer-with-Dirac, ×2 imported | `research/2026-07-08_electron-g2-selforbit_result.md:3,8,14,83` + prereg `:89` | ✅ verbatim confirmed |
| a_e = α/2π on-site chain + engine constant | `src/scripts/vol_2_subatomic/simulate_g2.py:9-14,52,116`; `src/ave/topological/cosserat.py:641-655` | ✅ `G_MINUS_2_TREE` present |
| α⁻¹ = LOADED/radiative Q port register | `theorem-3-1-q-factor.md:147`; `resonant-lc-solitons.md:122` | ✅ |
| Under-tagged a_e cites (echo-tag targets, D2a) | `dama-alpha-slew-derivation.md:43`; `preferred-frame-and-emergent-lorentz.md:131`; `mond-hoop-stress.md:55` | ✅ all read "canonically derived" no VALUE=echo |
| README/LIVING_REFERENCE status conflict (D2c) | `README.md:219,221` vs `LIVING_REFERENCE.md:276,278` | ⚠ **LINE DRIFT** from card (README :216→:219, LIVING_REFERENCE :275→:276); content conflict CONFIRMED |
| Coverage-matrix g=2 :52 vs :68 tension (D2b) | `research/2026-06-17_electron-coverage-matrix.md:52,68` | ✅ tension confirmed; g2-selforbit `_result §6` provides the reconciliation |
| Q-G19α postulate-conditional; muon +4.6σ (D2d) | `q-g19a-petermann-saliency-closure.md:8,14,110`; coverage-matrix `:55,56` | ✅ RESOLVED-NEGATIVE caveat carried at leaf |
| Ward host = Axiom-3 Noether; anomaly literal ABSENT (two-method) | `common_equations/eq_axiom_3.tex:27`; `common/axiom-register.md:231`; `common/identity-break-test-design.md §2` | ✅ |
| Anomaly-adjacents only (parity-selection) | `chiral-screening.md:11,22,24`; `divergence-test-substrate-map.md:205` | ✅ |
| Gauge-reading constituents | `trampoline-analogy-primer.md:265`; `physics-lineage-map.md:154,181` | ✅ |
| Series: finite-radius wall vs n!-asymptotic; running-coupling "open problem" | `four-regimes.md:26-85`; `vol2/claim-quality.md:1311`; `electron-unknot.md:63` | ✅ |

**Anchor honesty:** the card's receipts were pinned to `c12f2bdb` (one merge ahead of origin/main). This charter is pinned to `db06ba82`. The only re-verification drift found is the README/LIVING_REFERENCE line numbers (recorded ⚠ above); every verbatim fence/reconciliation anchor holds at the stated line at `db06ba82`.

---

## APPENDIX A — STRING-THEORY SIDE-WALK (walk-note class; NO claims minted)

**Scope discipline:** this appendix is a **walk-note** in the same class as the series-reading (§4.4) — a consistency-lens observation, not a derivation, not a chord, not a value. Nothing here is minted, cited as a claim, or promoted to a KB leaf. It is recorded because the historical lineage rhymes with QED-TRACE's own "read the math as medium data" move, and one contact point is worth a future desk-check.

- **The lineage as resonance-without-a-medium.** The bootstrap → dual-resonance-model (Veneziano) → strings lineage is, read through the AVE lens, an attempt to build **resonance structure without positing a medium**: the Veneziano amplitude's Regge poles are a resonance spectrum, and the "string" was retrofitted as the object whose modes reproduce that spectrum. QED-TRACE's inverse move — *insist* on the medium and read the spectrum as its response — is the natural dual. This is an *observation about the shape of the two programs*, not a claim that AVE derives string theory or vice-versa.
- **The worldsheet = a 1D transmission line.** The string worldsheet action is, structurally, **medium math on one dimension** — a 1+1D wave equation with tension standing in for the line's distributed L/C. In EE terms the worldsheet is a 1D TL; the mode expansion is the TL's standing-wave spectrum. Consistency-class rhyme only; AVE's substrate is a 3D+port lattice, not a 1D sheet.
- **The landscape = modes without a constitutive layer.** The string landscape enumerates vacua as **mode configurations with no underlying constitutive layer** (no ε₀/μ₀/Z₀ that *forces* which modes are physical). This is precisely the layer AVE's fence insists on — the constitutive medium is what selects and grounds the modes. The contrast is the walk-note's point: same mode-counting mathematics, opposite stance on whether a constitutive substrate is required.
- **Regge-vs-(2,q)-ladder contact → FUTURE DESK-CHECK (flagged only).** The one concrete contact worth a later look: the **Regge trajectory** (J ∝ M², linear mass²-vs-spin) versus AVE's **(2,q) torus-knot ladder** (the baryon mass ladder indexed by winding). Whether the linear Regge slope and the (2,q) ladder spacing are the *same* combinatorial object viewed two ways, or merely superficially similar, is **an open desk-check** — not run here, not claimed. Flagged for a future consistency pass; if pursued, it freezes its own pre-reg with the FORM/VALUE firewall (a linear-in-index mass ladder is generic, so any match is echo-suspect until a distinct spacing coefficient is forced).

**Net:** walk-class throughout. The lineage rhyme licenses no number and no chord; it is recorded as context for why "read the math as medium data" is a recurring dual across programs that dropped (or never had) the constitutive layer.
