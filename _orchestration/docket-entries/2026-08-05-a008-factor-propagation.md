# A-008 convention propagation check (2026-08-05)

**Dispatch:** `2026-08-05-rulings-sheet-nine.md` item 2 — *"A-008 propagation check: GO — propagate
the A-008 canonical frame/field convention (trampoline-framework.md:224-227) through
cosserat-mass-gap.md + the two-band FLAG-1; escalates only if a residual choice survives."*
**Lane:** core mini-lane, CHECK class (derivation-only; no driver, no engine run, no KB edit).
**Branch:** `research/a008-factor-propagation` · **Base:** `origin/main` at `0a37ddca`.
**Prereg (frozen ALONE, pre-analysis):** `research/2026-08-05_a008-factor-propagation_prereg-FROZEN.md`.
**Note:** `research/2026-08-05_a008-factor-propagation_note.md`.

## Verdict

**BIN: `FACTOR-CLOSED-BY-A008`.** **$E_g = \hbar\omega_m$**, not $2\hbar\omega_m$
($= 2\,m_ec^2 = 1.022$ MeV — the pair threshold the corpus already books as the bandgap).

The discrepancy is exactly one factor of the already-ruled half-cover. Two independent 2's are in
play — the SU(2)→SO(3) covering degree and the Klein–Gordon $\pm$ branch doubling — living on
opposite sides of the covering map. FLAG-1 compounds them onto one numeral. Frame side: branch
bottom $\omega_m = 2$, beat $2\omega_m = 4$. Field side (one application of the covering): branch
bottom $\omega_C = 1$, beat $2\omega_C = \omega_m$. $E_g$ is field-side in every corpus use.

**Per the dispatch's own escalation clause ("escalates only if a residual choice survives"): no
residual choice survives on the factor question.** One direction-prose residue is quoted below and
does not reopen it.

## What A-008 forbids

FLAG-1's candidate (a), $G_c/I_\omega = 1/4$, is not merely unselected — it is a corpus path
already struck out by name on the same 2026-04-27 adjudication.
`research/_archive/L5/axiom_derivation_status.md`:1395 verbatim: *"**Reconciliation A (SUPERSEDED —
moduli surgery unnecessary):** ~~Re-pin Cosserat moduli so m_Cosserat = m_e = 1. Requires
`G_c/I_ω = 1/4`.~~ Unnecessary."* FLAG-1's candidate (b) ≡ (c) is the one A-008 selects.

**Corollary:** A-008 pins the RATIO $G_c/I_\omega = 1$ (given $\ell_{node} \equiv \hbar/(m_ec)$),
leaving only the absolute moduli free. The corpus's ENG-CHOICE-placeholder tag on the pair
understates this. Routed as FLAG-P.

## Corpus reconciliation

Fourteen tracked non-lane files carry $\omega_m \sim 1$ MeV (re-derived here, two regex engines
named in the note; the Tier-2 verify's "$\geq 9$" confirmed and exceeded). **All fourteen are
already A-008-consistent as written** — each reaches $\sim$1 MeV by converting $\omega_m = 2$
through $\hbar\omega_C = 0.511$ MeV, i.e. each already asserts $\omega_m = 2\omega_C$. Three
further sites independently put the observable gap at $2m_ec^2 = 1.022$ MeV, and
`lattice-model-register.md`:104 already places the field-side branch bottom exactly where FLAG-1
says it must be ($\omega_0 = \omega_C$) — by projection, without touching a modulus.

$E_g = 2.044$ MeV occurs at exactly three places in the corpus, all descended from one text: the
two-band result §7/§8 and its two landings (`translation-circuit.md`:355-364,
`common/claim-quality.md`:1649). That is the repair surface.

## Flags surfaced (verbatim in the note; none resolved here)

| flag | content | routing |
|---|---|---|
| **FLAG-D** | direction-of-the-2 prose: `l3-electron-soliton-synthesis.md`:132 *"observable frequency = 2 × medium frequency"* contradicts A-008 and its OWN boxed :134 *"m_e (observable) = m_Cosserat (medium) / 2"*. Already flagged 2026-07-08 (`electron-g2-selforbit_result.md`:73), whose cite `:103-105` has line-shifted to `:132-134`. Also `trampoline-framework.md`:220 first clause reads backwards against its own second clause. **Does not reopen the bin** — over-determined against by the leaf's own box, the 14-site witness set, and the three gap-energy sites. **The single hinge:** if Grant rules D2 canonical, the verdict inverts and 14 sites become wrong. | **Grant** (direction call), then doc lane |
| **FLAG-C** | 15 sites cite the gap as `trampoline-framework.md:188`; on `main` that line is the microrotation EOM — the gap is at `:192`. Pure line-shift. | doc lane |
| **FLAG-H** | two objects called "the mass gap" differ by exactly the half-cover 2: Cosserat $\hbar\omega_m \approx 1.022$ MeV vs Yang-Mills $\Delta = m_ec^2 \approx 0.511$ MeV. The existing "three distinct 2's" guard carries neither of this lane's two 2's. | auditor (taxonomy extension) |
| **FLAG-P** | ratio-RULED vs scale-ENG-CHOICE not distinguished at `cosserat-mass-gap.md`:151, `translation-circuit.md`:365-369, `common/claim-quality.md`:1648. | auditor |
| **FLAG-S** | the mandated SVA v0.2 leaf (11 rows) is NOT on `main` — only on the unmerged `kb/sheet-nine-execution-0805`. This lane used the stricter 11-row header from that branch and declared the deviation at freeze. On that branch the fenced block still self-labels "SVA v0.1-pilot" while carrying eleven rows. | whoever lands v0.2 |

## Routed repairs — ten items, NONE executed

R1-R2 the two FLAG-1 landings; R3 a Rule-12 header on the two-band result; R4 Grant's direction
call; R5 the shifted g2-lane cite; R6 `trampoline-framework.md`:220; R7 the fifteen `:188` repins;
R8 the provenance tags; R9 the do-not-fuse taxonomy extension; R10 a side-tag line in
`cosserat-mass-gap.md` §4 (the leaf carries the frame-side $\omega_m$ and the field-side
$\omega_C$ without ever naming the projection between them — that omission is what FLAG-1 fell
through). Full table in the note §6.

## Fence

Consistency / convention audit. Mints nothing, moves no solidity, adjudicates no physics fork. Does
NOT license any rest-mass statement, any Zitterbewegung claim, any change to the two-band lane's
`FORM-REPRODUCED-V-MISMATCH` verdict (independent of FLAG-1 and untouched), or any promotion of
$E_g = 2m_ec^2$ to an AVE result — that value is definitional given $m_e$, as
`translation-circuit.md`:890 already tags it.

## Validation

`make verify` — ALL PHYSICS PROTOCOLS PASSED, per commit. No number-check gate minted: the lane
runs no driver and the note carries no backticked numerals.
