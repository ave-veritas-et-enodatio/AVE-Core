# A-008 convention propagation check — FROZEN pre-registration

**Date:** 2026-08-05 · **Branch:** `research/a008-factor-propagation` · **Lane:** core mini-lane,
CHECK class (derivation-only; no driver, no engine run, no KB edit).
**Dispatch record:** `_orchestration/docket-entries/2026-08-05-rulings-sheet-nine.md` item 2
("A-008 propagation check: GO"). **SVA pilot case:** this lane (header below).

> **Freeze discipline.** This prereg lands as its own pushed commit, before any analysis text
> exists. The bins in §2 are frozen here and are not editable downstream.

---

## §0 — Standard Vacuum Analysis header (SVA v0.2, 11 rows)

```
 1. SECTOR / OWNERSHIP:      The object under check is the Cosserat MICRO-ROTATION (T2/omega)
                             sector's gap frequency omega_m, and its projection onto the spin-1/2
                             observable clock omega_C. Cross-wiring check: the A1 dilatation
                             rest-mass STORE is NOT in scope (trampoline-framework.md:194 and
                             cosserat-mass-gap.md:149 re-scope the gap to the flywheel CLOCK, not
                             the mass store). No "A confines B" claim is made or needed.
 2. REGIME / PHASE-STATE:    MODE = linear / cold-lattice small-signal; REGIME = long-wavelength
                             (k -> 0) band-edge; PHASE-STATE = unsaturated (S(A) = 1, no Op14
                             clock modulation, no yield). Frame-vs-field is a KINEMATIC covering
                             relation, regime-independent; this row records that the check does
                             not reach into the saturated regime where omega would be graded.
 3. CIRCUIT STATEMENT:       Before any framework word: the substrate here is a reactive resonator
                             whose rotational branch has a non-zero cut-off (a high-pass / gapped
                             line). omega_m is that cut-off frequency. omega_C is the frequency a
                             spin-1/2 readout PORT reports when the same resonator is read through
                             a 2:1 covering. TOTAL-vs-SLOT: the quantity in dispute (E_g) is a
                             TOTAL port-observable (a threshold energy), not a series slot.
 4. PLANE & PROJECTION:      No Gamma or Z claim is made. The projection that IS declared: every
                             frequency numeral is tagged FRAME-side (medium SO(3) twist rate) or
                             FIELD-side (SU(2) spin-1/2 readout). Spectral-lane branch selection:
                             the branch in question is the k=0 bottom of the micro-rotational
                             (omega-character) manifold of the canonical Cosserat dynamical matrix.
 5. CONSTITUTIVE PROVENANCE: G_c, I_omega, gamma, rho: engine ENG-CHOICE placeholders
                             (cosserat_field_3d.py:12, :954). The RATIO G_c/I_omega is the object
                             this lane tests for promotion from ENG-CHOICE to RULED-BY-A-008.
                             ell_node = hbar/(m_e c): IMPORTED (CODATA m_e). The half-cover
                             factor 2: DERIVED (SU(2)->SO(3) covering degree), ratified.
 6. ENERGY LEDGER:           No port, no loss, no arrow. This lane moves no energy and names no
                             dissipation; it re-labels a frequency across a covering map. Rim-only.
 7. CALIBRATABILITY:         The target is a DIMENSIONLESS RATIO (omega_m/omega_C, and the integer
                             in E_g = N * hbar * omega_m). The MeV numerals are imported through
                             m_e and carry no independent content; they are used only as a
                             consistency witness set, never as a derivation input.
 8. DISCRIMINATION CLASS:    Not a discriminator lane. Class = DC-internal bookkeeping (a corpus
                             convention audit). Tautology filter: the check could return
                             RESIDUAL-CHOICE or CONVENTION-CONFLICT, so it is not a restatement of
                             A-008. SM counterfactual: N/A - no observable is predicted here.
 9. CERTIFICATION PLAN:      Bins frozen in §2 before analysis. UNRUN != PASSED: the witness-set
                             reconciliation (§3 method) must be executed by TWO named regex engines
                             with the engines named in the result, or the absence/completeness half
                             of the verdict is reported as NOT ESTABLISHED. Negative control: the
                             lane must locate at least one corpus site that would FALSIFY the
                             A-008 direction if read at face value, and report it verbatim.
10. ADJUDICATION ROUTING:    This lane ADJUDICATES NOTHING and EDITS NO KB FILE. Its output routes
                             a verdict to the orchestrator; any repair the verdict implies (KB
                             text, claim-card text, cite repin) is ROUTED, not executed here. If
                             the bin returns CONVENTION-CONFLICT the item escalates to Grant with
                             both sides quoted; if RESIDUAL-CHOICE, the named choice escalates.
11. NUMERICAL CONDITIONING:  No floating-point work. Every numeral is an integer, an integer ratio,
                             or a quoted corpus numeral. Named cancellation to watch: the two
                             independent factors of 2 (the SU(2)->SO(3) covering degree, and the
                             Klein-Gordon +/- branch doubling) which can compound to 4 or cancel to
                             1 depending on which side of the covering the doubling is applied.
                             That compounding IS the object under test. No iterated map, no
                             error-propagation model needed.
```

---

## §1 — Question, frozen

Under the A-008 canonical frame/field convention
(`manuscript/ave-kb/common/trampoline-framework.md`:224-227, Grant adjudication 2026-04-27)
applied CONSISTENTLY through (a) the `cosserat-mass-gap.md` chain
$m^2 = 4G_c/I_\omega$ and its rest-energy inference, and (b) the two-band lane's FLAG-1
(`research/2026-08-05_two-band-kinematics_result.md` §7):

1. Is $E_g = \hbar\omega_m$ or $E_g = 2\hbar\omega_m$?
2. Does the factor-4-vs-2 discrepancy in FLAG-1 reduce to a ruled factor, a residual choice, or a
   canon conflict?

## §2 — FROZEN BINS (exhaustive, mutually exclusive on question 2)

| bin | fires when |
|---|---|
| **FACTOR-CLOSED-BY-A008** | the discrepancy is exactly the already-ruled half-cover factor; applying A-008 consistently removes it with no new choice and no canon site contradicting the result |
| **RESIDUAL-CHOICE(named)** | A-008 constrains the ratio but leaves a further convention the corpus has not made; the surviving choice must be NAMED EXACTLY, with what each branch implies |
| **CONVENTION-CONFLICT(quoted)** | A-008 and another canon site cannot both be read at face value; BOTH sides quoted verbatim with file:line; no side is picked by this lane |

Bins are frozen. A bin fires on the FLAG-1 factor question only. Ancillary findings (stale cites,
prose defects, provenance-tag drift) are reported as FLAGS, not as bin-flips, and are ROUTED.

## §3 — Method, frozen

1. Re-derive the frame/field relation from A-008's own statement plus its cited provenance chain;
   do not import a convention from outside the corpus.
2. Build a convention-propagation table: every load-bearing site that carries $\omega_m$,
   $\omega_C$, $m_{\text{Cosserat}}$ or $E_g$, each tagged FRAME-side / FIELD-side, with its
   factor reading under A-008.
3. Reconcile against the corpus sites carrying $\omega_m \sim 1$ MeV. The witness list is
   RE-DERIVED by this lane with **two named regex engines** (per the two-band Tier-2 lesson that
   an absence claim on a single method is a false negative); both engines and both patterns are
   reported in the result.
4. Negative control (per §0 row 9): actively hunt for a corpus site that, read at face value,
   would invert the A-008 direction. Report it verbatim whether or not it changes the bin.

## §4 — Fence

This lane does NOT license: any statement about the electron's rest-mass value; any Zitterbewegung
CLAIM (only a reading of what the corpus's own identification implies); any KB edit; any change to
the two-band lane's `FORM-REPRODUCED-V-MISMATCH` verdict, which is independent of FLAG-1.

## §5 — Declared deviation at freeze time

The dispatch mandates the SVA §0 header at leaf **v0.2 with row 11**. On this lane's base
(`origin/main`, `0a37ddca`) `manuscript/ave-kb/common/standard-vacuum-analysis.md` is still
**v0.1 (10 rows)**; v0.2 exists only on the unmerged branch `kb/sheet-nine-execution-0805`. The
stricter (11-row) v0.2 header is used above, sourced from that branch. Surfaced, not resolved.
