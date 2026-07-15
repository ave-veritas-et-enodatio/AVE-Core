[↑ Common (Cross-Volume Resources) Index](index.md)

<!-- kb-frontmatter
kind: leaf
claims: [clm-strreg, clm-crit2a]
path-stable: "canonical home for the step-vs-ladder strain-register carve (Grant Ruling 11) + the storage-α / response-α criteria carve (Grant Ruling 12); referenced from envelope-anatomy (the knee row gains its register label) and translation-circuit §4"
-->

# Strain Registers — the step/ladder carve (Ruling 11) and the storage-α / response-α criteria (Ruling 12)

> **Sector / regime / phase-state declaration (substrate-native-first).**
> **MODE:** the constitutive reading of Axiom 4's kernel $S(A) = \sqrt{1-(A/A_{yield})^2}$ — *which* strain the kernel eats, and *which* α-criterion marks each contour. Static-configuration reasoning; no driven dynamics except where the AC bridge (§2, Ruling 12) is named explicitly.
> **SECTOR:** the saturation amplitude $A$ is the per-node operating-point state along the Ax-4 kernel (INVARIANT-S2 operating-point clause), gauge-relative (only gradients of $A$ are observable). This leaf carves the *argument* of the kernel, not a new sector — it is orthogonal to the A1 ⊥ T2 ⊥ spin ownership split.
> **PHASE-STATE:** sub-yield, lossless-reactive, up to the knee ($A^2 = 2\alpha$); the wall ($S\to0$) is the far endpoint. Both carves below are FORM-level Grant rulings — **RULED conventions, not derivations** (values ride CODATA-derived imports).

**Status: two Grant-ruled FORM carves. RULED, not derived — a ruled convention is still a convention.**
- **Ruling 11 (RULED, Grant verbatim "Yes, I agree with where the walk is ending up"; record: the 2026-07-15 register-walk docket continuation, `_orchestration/2026-07-10_rulings-docket.md`):** the kernel consumes **FIELD-strain** (the per-cell drop), NOT **voltage-strain** (the potential). `clm-strreg`.
- **Ruling 12 (RULED, Grant verbatim "ratify", in-chat 2026-07-15; record: same docket continuation):** the two α-thresholds are two **criteria** on one nonlinear element — **storage-α** ($A^2=\alpha$) vs **response-α** ($A^2=2\alpha$); the factor of 2 is the Taylor-½ of the root kernel. `clm-crit2a`.

These two carves are **orthogonal** (§3): the register axis (step vs ladder) crosses the criterion axis (storage vs response) into a 2×2.

---

## §1 — Ruling 11: the kernel eats FIELD-strain, not voltage-strain (the step register)

<!-- claim-quality: clm-strreg -->

**The carve.** The constitutive kernel's argument $A$ is the **field-strain** — the per-cell drop $E\cdot\ell_{node}$ (the *gradient* register), read one node-span at a time — **not** the **voltage-strain** — the potential (the accumulated $d_{sat}/r$ over an interaction span). Grounds walked (all three point the same way):

1. **The varactor ground.** A varactor biases on the voltage across *its own junction* — one cell span — not on absolute potential referenced to infinity. The substrate-native varactor (Ax-4 kernel, `translation-circuit.md` §4 line 111) is biased by the field across one node, $E\cdot\ell_{node}$.
2. **The dielectric ground.** Every physical dielectric saturates against the local field $E$ — its polarization is $P(E)$, never a function of the absolute potential. The kernel is the vacuum's $P(E)$; it keys on $E$.
3. **The locality / gauge ground.** The mechanical twin of *potential* is total displacement $u$; a kernel on $u$ would violate lattice translation invariance (absolute-position dependence). **Strain is $\partial u$**, and the electrical twin of strain is $E$ (the field, $\nabla\phi$), not $\phi$. A translation-invariant constitutive law must key on the gradient register.

**The ladder theorem (the reconciliation — Ruling 11's positive content).** The two registers are **not** competitors: **the potential IS the series sum of the per-cell drops.** The voltage register is the **line integral of the field register** ($V = \int E\,d\ell = \sum_{\text{cells}} E\cdot\ell_{node}$). **Cells feel steps; ports / interactions see sums.** The kernel — a per-cell constitutive law — eats the step (field-strain); an interaction spanning many cells reads the sum (voltage-strain). Both registers are real; they live at different scales of the same ladder.

**Both knees are real, each with its job (REGISTERED-NOT-EXECUTED beyond the FORM):**

| Knee | Value (native units, $\ell_{node}=d_{sat}$) | Register | Job |
|---|---|---|---|
| **field knee** | $(2\alpha)^{-1/4} = 2.877\,\ell_{node}$ | step / per-cell (gradient) | the **cell / dress knee** — where one cell's field-strain reaches $A^2=2\alpha$; measured as the $r99$ outer edge of the correction cloud (ratio $1.06$) in PR #696 (`research/2026-07-14_knee-contour-check_NOTE.md` §4.3, field-strain PRIMARY :143) |
| **voltage knee** | $(2\alpha)^{-1/2} = 8.278\,\ell_{node}$ | ladder / port (sum) | the **interaction / port knee** — where the *summed* potential reaches the same deficit; the FLAGGED voltage-strain knee of the knee-NOTE (:145), now **re-read as the correct port register** (below) |

Note $(2\alpha)^{-1/2} = \big[(2\alpha)^{-1/4}\big]^2$: the voltage knee is the square of the field knee, exactly as the ladder-sum (a line integral) relates to its per-cell step.

**Op4/Op14's $(d_{sat}/r)^2$ argument = a CANDIDATE integrated port expression of a field-biased ladder.** ★ **REGISTERED CHECK (the Op4 ladder integral):** integrate the per-cell field-strain dress radially and compare to the closed-form $Z_0\,(1-(d_{sat}/r)^2)^{-1/4}$. A **match closes the fork completely** (the port expression is the honest ladder-sum of a field-biased kernel); a **mismatch = a real defect in a canonical operator** (flag-don't-fix — surface it, do not rescue). Not fired here; this leaf fixes only the register the kernel keys on.

**Consequence — the 1/4 map's Q#1 fork RESOLVES under this ruling.** The `research/2026-07-14_quarter-power-map.md` (THE 1/4 MAP) Q#1 fork — the driver kernel consumes field-strain $(d_{sat}/s)^2$ (knee $2.877$) while `methodological-contamination.md:48` uses voltage-strain $d_{sat}/r$ (knee $8.278$) — is **resolved**: both are correct **in their own register**. The `r_knee` quarter-power VALUE is retained, **fork-conditional no more** (it rides the α-echo per the knee-NOTE's own echo-classification; the register ambiguity that made it fork-conditional is closed).

**No correction owed at `methodological-contamination.md`.** That leaf's pairwise voltage-strain example ($A = d_{sat}/r_{ij}$, `:46-48`; manuscript twin `vol_2_subatomic/.../09_computational_proof.tex:206-208`) is the **INTERACTION register used correctly** — a pair of atomic electrons interacting across a Bohr-radius span reads the ladder *sum*, which is exactly the voltage-strain. Ruling 11 vindicates it (it is not a defect); the knee-NOTE's ⚑ FLAG on the voltage-strain is thereby **resolved, not fixed** — it was the port register all along.

**Gate-(b) pre-registration note.** The gate-(b) envelope-eigenmode freeze should pre-register the **field knee** $(2\alpha)^{-1/4}$ as the **dress-edge candidate** (surface iii of the envelope anatomy; see [`envelope-anatomy.md`](envelope-anatomy.md) surface (iii) + its radial-ladder table, whose knee row now carries this **step/field register** label).

---

## §2 — Ruling 12: the two α-criteria — storage-α vs response-α (the Taylor-½)

<!-- claim-quality: clm-crit2a -->

**The carve.** The two α-thresholds that thread the corpus are **two criteria on one nonlinear element**, not two values of one criterion:

- **STORAGE criterion — "stored fraction $= \alpha$":** $A^2 = \alpha \Rightarrow A = \sqrt{\alpha} \approx 0.0854$. The **entire yield family**: $V_{YIELD} = \sqrt{\alpha}\,V_{SNAP}$ (`constants.py:505`), $E_{YIELD} = V_{YIELD}/\ell_{node}$ (`:516`), $E_{YIELD\_KINETIC} = \sqrt{\alpha}\,m_ec^2$ (`:499`), $h_{yield} = \sqrt{\alpha}$ (the genesis-seed amplitude mark).
- **RESPONSE criterion — "deficit $\Delta S = \alpha$":** $A^2 = 2\alpha \Rightarrow A = \sqrt{2\alpha} \approx 0.1208$. The **knee family**: `A_YIELD_SQ = 2·α` (`chiral_lattice_v10.py:30`), `R_I = √(2α)` (`constants.py:525`).

**The 2 is the Taylor-½ of the root kernel — UNCONDITIONAL.** The deficit of the quarter-arc kernel is $\Delta S = 1 - \sqrt{1-A^2} \approx A^2/2$ (leading order). So "deficit $=\alpha$" gives $A^2/2 = \alpha \Rightarrow A^2 = 2\alpha$, while "stored fraction $=\alpha$" gives $A^2=\alpha$ directly. **The factor of 2 is the $\tfrac12$ from the square-root's Taylor expansion** — a property of the kernel's *shape*, present whether or not any wave is involved.

**Equipartition is the AC bridge (regime-dependent), not the source of the 2.** The traveling-wave half-half quadrature split (equipartition) is what makes the deficit numerically *equal the per-sector share* — an **AC bridge**. It is **regime-dependent**: standing waves slosh energy between quadratures (the #698 phase findings are the live demo — the endpoint vs quiet-window-mean split), so the ½ that equipartition supplies is a **wave** property, whereas the ½ in $\Delta S \approx A^2/2$ is the **kernel's own**. The tell: the *static* dress (no wave, no equipartition) uses $\sqrt{2\alpha}$ and matches $r99$ — the response-criterion 2 survives with no wave present, because it is the kernel's Taylor-½, not the wave's quadrature-½.

**The near-collision is the two criteria's clock projections.** $\sqrt{1-\alpha} = 0.996345$ (the storage-criterion clock) vs $(1-2\alpha)^{1/4} = 0.996331$ (the response-criterion clock) differ by $\Delta = 1.4\times10^{-5}$. These are the two criteria's $\sqrt{S}$-projections evaluated at their respective contours — a near-collision *because* they are two readings of one kernel one Taylor-order apart, not a coincidence to be mined.

**RENAME NOTE (gentle, walk-record).** The $\sqrt{\alpha}$ family's *"yield"* name is **soft** — nothing yields at $A=\sqrt\alpha$ (it is the **storage-α mark**, the stored-fraction-$=\alpha$ contour). Actual breakdown is the **wall at $A=1$** ($S\to0$). The name is legacy; the physics is the storage criterion, not a yield event. (No rename executed — flagged for the vocabulary lane.)

---

## §3 — The 2×2: register axis ⟂ criterion axis

The two rulings carve **orthogonal** axes. Populated across the corpus:

| | **STORAGE criterion** ($A^2=\alpha$, stored fraction) | **RESPONSE criterion** ($A^2=2\alpha$, deficit $\Delta S$) |
|---|---|---|
| **STEP register** (per-cell field-strain, gradient) | $h_{yield} = \sqrt\alpha$, $E_{YIELD}$ (the field-register storage mark) | field knee $(2\alpha)^{-1/4} = 2.877\,\ell_{node}$ (cell/dress knee) |
| **LADDER register** (summed voltage-strain, port) | $V_{YIELD} = \sqrt\alpha\,V_{SNAP}$ (the port-register storage mark) | voltage knee $(2\alpha)^{-1/2} = 8.278\,\ell_{node}$ (interaction/port knee) |

The corpus populates **3 of 4 cells** under names that never advertised the axis. Explicitly: **$h_{yield}$ is a field-register quantity carrying the storage criterion** (step × storage); $V_{YIELD}$ is the same criterion in the port register (ladder × storage); the two knees are the response criterion in each register. The 2×2 is the map; the labels are the new bookkeeping.

★ **CRITERION-TAG MANDATE — RATIFIED (Grant "ratify", in-chat 2026-07-15).** Every $\sqrt\alpha$ / $\sqrt{2\alpha}$ site is to be tagged **storage-α vs response-α**, folded into the contour-tag sweep (the sweep moves from gated to **QUEUED**; see the next-steps register in the docket). This is a bookkeeping-discipline mandate, not a physics claim.

---

## §4 — Status, class, and what is NOT claimed

- **Both carves are RULED FORM conventions, honestly consistency-class — NOT emergence, NOT derivation.** Grant ruled the *form* (which strain; which criterion marks which contour); the *values* ride CODATA-derived imports (α, $\ell_{node}=\hbar/m_ec$, $V_{SNAP}=m_ec^2/e$). A ruled convention organizes the corpus; it does not derive α or the knee value (the `r_knee` value stays α-echo-classified per the knee-NOTE).
- **The Op4 ladder integral is REGISTERED-not-executed** (§1): the fork is closed at the FORM level (both registers real), and pinned at the VALUE level only when the ladder integral matches (or a mismatch flags a canonical-operator defect).
- **Ruling 11 does not overturn the canonical dielectric specialization** $A=\Delta\phi/\alpha$ (`eq_axiom_4.tex:31`): $\Delta\phi$ is the per-cell phase drop (the field / step register), consistent with the carve.

## Cross-references

- [`envelope-anatomy.md`](envelope-anatomy.md) — surface (iii) knee / dress edge (the field knee is the dress-edge candidate) + the radial-ladder circuit table (whose knee row carries the step/field register label).
- [`translation-tables/translation-circuit.md`](translation-tables/translation-circuit.md) §4 — the knee / dress-edge / uniform-field / gradient rows the register carve annotates.
- [`../vol2/proofs-computation/ch09-computational-proof/methodological-contamination.md`](../vol2/proofs-computation/ch09-computational-proof/methodological-contamination.md) — the pairwise voltage-strain example = the interaction / port register used correctly (no correction owed).
- `research/2026-07-14_quarter-power-map.md` (THE 1/4 MAP) + `research/2026-07-14_knee-contour-check_NOTE.md` (PR #696) — the field/voltage knee numerics and the Q#1 fork this ruling resolves (both report-only, echo-classified).
- `_orchestration/2026-07-10_rulings-docket.md` — the 2026-07-15 register-walk continuation carrying Rulings 11 + 12 verbatim.
