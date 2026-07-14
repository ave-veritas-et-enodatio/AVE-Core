# m_p/m_e Mass-Ratio — Value-Blind AUDIT CARD

**Date:** 2026-07-13
**Class:** AUDIT-CARD (read-only findings). This card **informs Grant's walk; it
demotes nothing.** No claim-id is touched, no leaf is re-graded, no CI gate is
changed by this document. It is a value-blind audit of an already-canonized
prediction, assembled so the emergence-vs-echo walk is made with the same
value-blind data the α-keystone adjudication received.
**Audited claim:** the proton mass ratio `clm-cmic3e` (δ_th thermal softening) +
`clm-w8jn3q` ("why exactly 3 loops", OPEN).
**Re-verification footing:** every load-bearing receipt below was re-verified at
this worktree's HEAD `9bfc50ef` (origin/main, merge of #674). The live-solver
numbers were reproduced by live-fire this session (`PYTHONPATH=src python3` against
`ave.core.constants` + `ave.topological.faddeev_skyrme`). The original audit lanes
ran against `f007fe34`; the load-bearing values are byte-identical at both SHAs.
**Cross-repo receipts:** the provenance chronology (below) cites the pre-split
historical archive `/Users/grantlindblom/Applied-Vacuum-Engineering` by commit SHA
per workspace cross-repo citation convention.

> **Scope / sector note.** This audits the *value provenance and coincidence
> exposure* of a dimensionless ratio (`m_p/m_e`) that AVE derives via a
> topology-forced eigenvalue chain plus one thermal correction. It is not a
> substrate-mechanism audit; MODE/REGIME are inherited from the proton leaf
> (cold Faddeev-Skyrme ground state + Ax4-saturated core). Symmetric-standard
> rail: SM makes no pure-number `m_p/m_e` claim (m_e is a Yukawa input, lattice
> QCD reaches ~1% given inputs), so the ppm bar this leaf faces is one SM is
> exempt from *because AVE claims more*.

---

## The claim as canonized

**What the leaf asserts** (`manuscript/ave-kb/vol2/particle-physics/ch02-baryon-sector/proton-identification.md`):

- The proton is the `(2,5)` **phase-space** winding rung of the baryon ladder; its
  mass eigenvalue is the one-term self-consistent loop
  `x_core = I_scalar/(1 − V_total·p_c)`, +1 Ax2 charge twist
  (`src/ave/core/constants.py:954-956`).
- **Bare-topology claim:** cold κ_FS = 8π → ratio **1849.70 (+0.7377%)** — the
  emergence result (re-verified live-fire this session; matches
  `proton-identification.md:13`).
- **Corrected claim:** thermal softening δ_th = 1/(14π²) → ratio **1836.117
  (−0.002% vs CODATA 1836.15267343)** — framed as precision-residual, NOT headline.
- **Parameter claim:** "zero baryon-data-tuned parameters" (line 13); provenance is
  electron-sector (m_e, α) only.

**The leaf already prices most of this honestly:**
- `proton-identification.md:13` verbatim: *"The δ_th thermal correction is the
  precision-setter — do NOT headline the −0.002% as pure geometry."*
- `self-consistent-mass-oscillator.md:64` + `constants.py:943-944`: **"1-residual
  Skyrme, NOT 'zero-parameter'"** — p_c = 8πα is canonical-packing-plausible, not
  line-by-line derived.

**Internal inconsistency at the flagship:** §2.1's six-input table marks p_c *"✅
none — derived from α"* and closes *"Zero fit parameters"* (`proton-identification.md:73`,
bold headline live at HEAD) — contradicting both its own primary sources AND its own
line 13. The optimistic slot was never reconciled down. (This is the B2 correction-note
item, Grant-gated; **out of scope for this card, flagged not fixed.**)

---

## The chain verdict-shape

**Parameter ledger (6 inputs):**

| Input | Value | Class |
|---|---|---|
| κ_FS^cold = 8π | 25.133 | topology-forced (solid angle) |
| c₅ = 5 | 5 | topology-forced integer; the proton↔(2,5) *rung assignment* is a matched structural assignment, not baryon-derived |
| V_total = 2 | 2.0 | forced dual-reactance count (Grant-adjudicated 2026-06-01); discriminator PASS (V=1→1424, V=p_c→1203 — an integer cannot flex to absorb a residual) |
| +1 twist | 1 m_e | topology-forced (Ax2) |
| p_c = 8πα | 0.18340 | **fed-in-flagged residual** per both primary sources; **unflagged** at flagship §2.1 (the internal conflict above) |
| δ_th = 1/(14π²) | 0.0072372 | **fed-in precision-setter**; honestly self-classified, but the value was re-derived once (1/(28π)→1/(14π²), exactly ×2/π) when the solver changed — see provenance |

α itself is **imported CODATA** (`constants.py:163`), not the AVE 4π³+π²+π echo — consistent with the electron-sector-provenance framing.

**Verdict-shape:** "zero baryon-data-tuned" **holds** — no input is fit to a baryon
observable. "Zero fit parameters" **does not hold** by the corpus's own sources — it
is 1-residual (p_c) plus one un-pinned O(1) factor inside δ_th (the 2/π mean/peak ratio).

**The 3-loop dependence: NONE.** Traced through code — the eigenvalue consumes
`I_SCALAR_1D`, V=2, p_c, +1. The loop count enters only charge-fractionalization and
real-space-topology legs. Resolving or refuting `clm-w8jn3q` ("why exactly 3") does
not move 1836.117.

**Arithmetic reproduction: PASS, two-method (re-run this session).** Live solver +
analytic from the stored literal: corrected **1836.1170402290593** (−0.00194%) matches
`constants.py:956`/`:1005` and `proton-identification.md:13` exactly; cold
**1849.6979** (+0.7377%) matches `proton-identification.md:13` exactly. Literal↔solver
pinned at rtol=1e-12 (`test_constants_literals.py`).

**Chain flags:**
- (a) `thermal-softening.md:11` **carried** a STALE cold triplet (I_scalar 1185 /
  ratio 1872 / ~2%) contradicted by the live solver (I_scalar^(cold) 1170.6 / 1849.7 /
  +0.7377%). **This card's companion hygiene PR corrects it (item A1, same PR);** the
  archive dig (below) shows that stale triplet is the un-refactored 2026-02-25
  prose, inherited verbatim. Note the cold I_scalar is **1170.6**, not the ≈1162
  softened value at `proton-identification.md:68` / `constants.py:910`.
- (b) No CI gate protects the −0.002% at claimed tolerance; tightest empirical gate is
  **0.5%** (`test_ave_engine.py:118`, `abs(ratio−1836.15)/1836.15 < 0.005`) — 250×
  looser. A δ_th regression inside 0.5% would pass silently. The +0.74% emergence
  claim IS effectively gated (cold fails 0.5%).

---

## The provenance verdict-shape

### The original verdict (INSIDE AVE-Core): pre-git mint, unrecoverable

Inside AVE-Core the history bottoms out at the repo root `de9d2293` (2026-04-13),
which **already contains** δ_th = 1/(14π²), the "previous value 1/(28π)" note
(`constants.py:889-890`), AND the thermal-softening leaf opening with the cold
overshoot. Pickaxe re-run this session: `git log -S "14.0 * pi**2" -- src/ave/core/constants.py`
hits **only** the root `de9d2293`. So *inside this repository* the correction and
the residual it closes entered in the same (root) commit, and the before/after-residual
question was **not recoverable**.

### 🟢 RESOLVED 2026-07-13 (archive-provenance dig): the chronology IS recoverable

A cross-repo dig into the pre-split historical archive
`/Users/grantlindblom/Applied-Vacuum-Engineering` (first commit predates the
2026-04-13 AVE-Core root) **recovers the full chronology as git fact.** The record
shows a **residual-first / fitted-after** pattern across THREE successive, mutually
incompatible mechanisms — each re-tuned to re-hit CODATA after the underlying
computation moved (all four SHAs + dates re-verified this session against the archive
repo; content quoted from `git show`):

| # | Archive SHA | Date | Mechanism | Residual it names / closes |
|---|---|---|---|---|
| 1 | `3432f066` | 2026-02-13 | $m_p = m_e\,\alpha^{-1}\,\Omega_{topo}$ with $\Omega_{topo}=4\pi+5/6\approx13.3997$ → 938.43 MeV | *"**Error:** 0.017%"* — a topological form-factor tuned to hit 938 MeV |
| 2 | `cf08cac7` | 2026-02-20 | ABANDONS #1; introduces $x_{core}=I_{scalar}/(1-V_{total}p_c)+1$, hand-set `I_SCALAR=1162.0`, $V_{total}=2.0$ ("FEM ≈1.974 … saturates to perfect integer 2.0"), $p_c=8\pi\alpha$, +1 twist → 1836.14 | *"converges … to within **0.0007%**"* (the I_scalar literal already matches CODATA) |
| 3 | `deba5edb` | 2026-02-25 | INTRODUCES δ_th = 1/(28π) (from $\nu_{vac}=2/7$ × "a factor of 2 — two tensor gradient indices"); a real cold solver now returns 1185/1872 | comment verbatim: *"yielding a proton ratio of ≈ 1872 (approximately 2% above the empirical value)"* — the correction is authored to close a **known** 2% overshoot |
| 4 | `879aa801` | 2026-03-03 | RECALIBRATES δ_th 1/(28π)→1/(14π²) by inserting the **×2/π** factor, triggered by the *"Gradient saturation upgrade"* (a solver change that moved I_scalar) | *"1842.39 m_e (0.34%) → 1836.12 m_e (0.002%)"*; the residual-driver comment naming the overshoot is deleted in the same commit — which is why AVE-Core's inherited note looks clean |

**Verdict (superseding the "unrecoverable" reading above, dated 2026-07-13):** the
δ_th **value** provenance is now **established as calibration, not prediction, as git
fact.** Each time the computation changed (hand-set literal → real cold solver →
gradient-saturation solver), a correction was introduced or re-tuned to bring the
ratio back onto CODATA. The "substitution tracks the fit" shape the original audit
flagged (value re-derived once, exactly ×2/π) is now the *documented* mechanism, not
an inference.

**What this does and does not touch:**
- The **bare-topology +0.74% leg is UNTOUCHED** — it is the post-Ax4-refactor
  live-solver value (1849.70, verified live-fire), real at HEAD, and NOT a conflation
  with the archive-era residuals (which were 2% / 0.80% / 0.34% at successive dates).
- The δ_th-riding **−0.002% ppm** result is the leg whose value provenance is now
  pinned as calibration.
- The **n–p mass split gate** (in flight; see below) now carries the entire structural
  burden for δ_th: it is the one test where δ_th cannot be re-tuned to hide behind bulk
  mass.
- **No 🔴 header is proposed for `constants.py`** — any demotion/annotation of the
  runtime constant is a separate Grant-gated decision; this card is read-only.

**Single-use vs multi-site (unchanged):** δ_th is applied at exactly one physical site
(κ_FS), two-method-confirmed; all other corpus hits are downstream citations or
do-not-conflate disclaimers. Counter-weight: the same unchanged δ_th spans the whole
ladder with no per-particle refit — but the corpus's own epic (§40) found it lands ppm
**only at the proton** and misses Δ(1232) at +2.35%:
*"PROTON-SPECIFIC tightness … a COINCIDENCE, NOT a spectrum property."*

**Review history (updated):** two prior adversarial passes. (1) The 2026-05-18 audit
exonerated on git-stability — but git-stability inside AVE-Core cannot speak to a
pre-AVE-Core mint, so that exoneration was **weaker than it read**; the archive dig is
what actually settles the provenance direction it could not. (2) The 2026-06-07 epic
§39-40 (sharper): F4 WARN — precision-setter, re-derived once, un-pinned π/2 factor,
"DON'T headline −0.002%," Δ-miss coincidence. The leaves faithfully carry that framing.

**The 14:** no independent receipt as "14" — it is arithmetic collapse (7×8)/(2×2). The
only independently-motivated integer is the 7, from ν_vac = 2/7, which traces to K=2G —
corpus-logged as **GR-imported, not substrate-forced** (PR#261; the genuine central-force
Cauchy route gives ν=1/4, a different "14"). So the precision-setter's provenance chain
bottoms out in an acknowledged import-echo plus one un-pinned 2/π.

---

## The coincidence verdict-shape

**Lenz / 6π⁵ (computed this session):** 6π⁵ = **1836.1181087**; CODATA = 1836.15267343;
corpus value = 1836.1170402. The corpus's forward value sits **33.3× closer to Lenz's
1951 6π⁵ numerology than to CODATA** (|Δ| = 0.001068 vs 0.035633), undershooting CODATA
by essentially the same 0.002% that 6π⁵ does. Two-method-confirmed: **no corpus site
mentions 6π⁵ or Lenz in the mass-ratio context** (the corpus's "Lenz" hits are the
back-EMF mechanism). The corpus's own defense of the −0.002% ("misses CODATA, therefore
not reverse-fit") **does not discriminate here — missing CODATA by 0.002% is exactly
hitting 6π⁵.**

**Structure vs π-polynomial:** the chain `I_scalar/(1−2·8πα)+1` has no π⁵ form, and the
FS solver is a forward minimize with no 1836/1162 target literal in the loop
(grep-confirmed). So the 6π⁵ proximity is coincidence-on-coincidence (anything near
CODATA is near 6π⁵) — but it is a **value-blind datum the α-keystone adjudication got
and this leaf has not.**

**α-adjacency:** δ_th = **0.99176·α** (14π² = 138.174 is **0.83%** from α⁻¹ = 137.036),
computed this session. The stated provenance is α-free (ν_vac, 8π, 2/π) — an unexploited
numerical coincidence, not a hidden α-substitution.

**α-PORT FRAMING CHECK (archive dig, 2026-07-13):** Grant's physical hypothesis — that
δ_th ≈ α might be a *radiative / α-strength port coupling* (which would make the adjacency
physically motivated rather than coincidental) — is **COUNTER-INDICATED on the record.**
No artifact at any archive date frames the thermal correction as radiative or α-coupling;
δ_th is constructed from ν_vac = 2/7 and a mean/peak (2/π) or tensor-index (2) factor at
every date, and the stated construction **cancels α exactly** (κ_FS = 8πα/α = 8π). The
δ_th ≈ α adjacency remains an **unmotivated coincidence**, not an α-port.

**Menu size:** the residual to close is δ ≈ 0.00724; the corpus vocabulary offers
1/(14π²)=0.00724, 1/(4π³)=0.00806, 1/(2π⁴)=0.00513, 1/(16π²)=0.00633, α≈0.00730 at that
scale — a real menu, with one demonstrably-adjustable O(1) factor (the π/2, added
2026-03-03) doing the selecting.

**Symmetric standard:** cut at SM-equivalent rigor, the **+0.74% bare-topology result
from integers-plus-imported-α is the genuinely unusual content and survives this audit
intact.** The ppm digits are where the exposure concentrates. The one item the leaf does
not price is the 6π⁵ receipt.

---

## What would settle it

Cheapest-first, T1-gate style:

1. **★ The n–p mass split — the mandatory second shot (gate #1).** Same chain, same
   δ_th, no refit: does the `(2,5)`-adjacent neutron construction produce **+1.293 MeV
   (+2.53 m_e) with the correct sign** (neutron heavier)? This is the sharpest
   discriminator available — a coincidence-tuned δ_th has no reason to survive a
   *difference* measurement where the bulk mass cancels and only chain structure remains.
   **Pre-register sign + magnitude band before running.** *Gate:* right sign AND within
   ~2× → strong structure signal; wrong sign → the ppm precision is confirmed
   proton-specific coincidence (the Δ +2.35% miss, epic §40, already points that way; the
   n-p split is cheaper and sharper). After the archive dig, **this gate carries the
   entire structural burden for δ_th's value.**
2. **Pin the 2/π mean-to-peak factor independently** — a one-page derivation from the
   rectified-noise statistics, written value-blind, no proton reference. If it pins,
   δ_th's last un-pinned knob closes; if it can only be motivated *given* the target, tag
   it honestly as the 2nd residual. (The archive shows this factor was *inserted*
   2026-03-03 to re-close a solver-shifted residual — so the value-blind derivation is
   exactly the test of whether it stands on its own.)
3. **Value-blind re-derivation protocol** — hand a fresh agent the three factors'
   *physical definitions only* (no values, no proton target, no thermal-softening leaf)
   and ask for δ_th's form. Does 1/(14π²) — vs 1/(28π), vs 1/(4π³) — come back? One
   session, decisive on the menu question.
4. **CI gate decision (Grant's fork):** either gate
   `|ratio − 1836.15267343|/1836.15267343 < 3e-5` (making −0.002% machine-protected) or
   formally headline +0.74% and keep −0.002% tagged δ_th-riding. Currently the claimed
   precision is 250× looser than its tightest gate (0.5%).
5. **Pre-git artifact reconstruction — NOW DISCHARGED (2026-07-13).** The archive dig
   supplies exactly the pre-release artifacts this item asked for: `deba5edb`
   (1/(28π) authored WITH the 2% overshoot named) and `879aa801` (recalibrated to
   1/(14π²) when the solver moved). The provenance direction git-inside-AVE-Core could
   not speak to is settled: **calibration, not independent prediction.**

---

## Receipts table

All arithmetic computed this session; all file:line re-verified at HEAD `9bfc50ef`; all
archive SHAs re-verified against `/Users/grantlindblom/Applied-Vacuum-Engineering`;
both absence claims two-method-confirmed.

| # | Receipt | Location | Verified |
|---|---|---|---|
| R1 | Canonical eigenvalue `I_SCALAR_1D/(1−V·P_C)+1.0` = 1836.1170402290593 | `src/ave/core/constants.py:954-956,1005` | live-fire + analytic |
| R2 | Cold bare-topology 1849.6979 (+0.7377%); cold I_scalar^(cold) = 1170.586 | live solver κ=8π; matches `proton-identification.md:13` | live-fire (this session) |
| R3 | δ_th = 1/(14π²) = 0.0072372; "previous value 1/(28π)" note; derivation block | `constants.py:876-896` | grep + read |
| R4 | 3-factor decomposition ν_vac/κ_cold × 2/π | `thermal-softening.md:18-27`; `full-derivation-chain.md:484-489` | grep + read |
| R5 | "1-residual, NOT zero-parameter" self-label | `self-consistent-mass-oscillator.md:64`; `constants.py:943-944` | verbatim |
| R6 | Flagship §2.1 "Zero fit parameters" bold headline (live) vs line-13 / p_c-residual conflict | `proton-identification.md:73` vs `:13` | read (this session) |
| R7 | *(INSIDE AVE-Core)* mint is pre-git: root `de9d2293` already carries 14π² + 28π note; pickaxe on `14.0 * pi**2` hits only root | `git rev-list --max-parents=0`; `git log -S` | git forensics (re-run) |
| R8 | Live cold-vs-softened split: I_scalar^(cold)=1170.6 (→1849.70) vs I_SCALAR_1D=1161.987 (→1836.117) — line 11 describes the cold trace, :68/`constants.py:910` the softened | live solver | live-fire (this session) |
| R9 | δ_th single-site application (κ_FS); all other hits downstream/disclaimer | corpus-wide 2-method grep | confirmed |
| R10 | Δ(1232) same-δ_th miss +2.35%; "proton-specific tightness = COINCIDENCE"; π/2 un-pinned (F4 WARN) | `_orchestration/2026-06-07_electron-synthesis-epic.md` §40 | verbatim |
| R11 | ν_vac=2/7 ← K=2G, GR-imported (PR#261); Cauchy route → ν=1/4 | `constants.py:626`; `vol1/claim-quality.md:644,663` | grep |
| R12 | 6π⁵ = 1836.1181087; corpus value **33.3×** closer to it than CODATA; zero corpus mentions | computed + 2-method absence grep | this session |
| R13 | δ_th = 0.99176·α; 14π² (138.174) vs α⁻¹ (137.036) = 0.83%; adjacency unnoted in corpus | computed + 2-method absence | this session |
| R14 | No 1836/1162 target literal in FS solver loop (forward minimize) | `faddeev_skyrme.py`; grep empty | 2-method |
| R15 | Tightest empirical CI gate 0.5%; no −0.002% gate | `test_ave_engine.py:118` | read-and-run |
| R16 | Stale cold triplet (1185/1872/~2%) in thermal-softening leaf — **corrected by companion PR item A1 (same PR)** | `thermal-softening.md:11` (pre-fix) | live-fire |
| **A1** | Archive `3432f066` (2026-02-13): $\Omega_{topo}=4\pi+5/6$ fit → 938.43 MeV, *"Error: 0.017%"* | `Applied-Vacuum-Engineering` `git show 3432f066` | git forensics (this session) |
| **A2** | Archive `cf08cac7` (2026-02-20): eigenvalue chain w/ hand-set I_SCALAR=1162, V=2.0, +1 twist → 1836.14, *"0.0007%"* | `Applied-Vacuum-Engineering` `git show cf08cac7` | git forensics |
| **A3** | Archive `deba5edb` (2026-02-25): δ_th=1/(28π) INTRODUCED; code comment (:2523) verbatim *"yielding a proton ratio ≈ 1872 (2% above empirical 1836.15)"* names the residual it closes | `Applied-Vacuum-Engineering` `git show deba5edb` | git forensics |
| **A4** | Archive `879aa801` (2026-03-03): δ_th recalibrated 1/(28π)→1/(14π²) via ×2/π; 1842.39 (0.34%) → 1836.12 (0.002%); triggered by "Gradient saturation upgrade" | `Applied-Vacuum-Engineering` `git show 879aa801` | git forensics |
| **A5** | α-port framing: NO archive artifact frames δ_th as radiative/α-coupling; construction cancels α (8πα/α=8π) | `Applied-Vacuum-Engineering` full-history grep | 2-method absence |

**Bottom line for the walk:** the **+0.74% bare-topology emergence result is clean,
gated, and survives all lanes.** The ppm digits ride a δ_th correction whose value
provenance is — as of the 2026-07-13 archive dig — **established calibration, not
prediction, as git fact**: introduced 2026-02-25 to close a named 2% overshoot,
recalibrated 2026-03-03 (×2/π) when the solver moved, single-site, whose only
independent integer traces to a GR-import echo, which misses at the sibling rung, whose
landing point is arithmetically Lenz's 6π⁵, and whose α-adjacency is an unmotivated
coincidence (no α-port on the record). **The n–p mass split with the same frozen chain
is the cheapest shot that lets the substrate adjudicate** — and now carries the whole
structural burden for δ_th.

---

## 🟠 ADDENDUM 2026-07-14 — the n-p gate FIRED bin (iv); the "entire structural burden" framing is superseded (body above preserved per KEEP-BOTH)

The card body above (written 2026-07-13 19:02) assigns the n-p mass split gate "the
entire structural burden for δ_th" at three sites (§provenance, §what-would-settle-it #1,
bottom line) and enumerates **only sign/magnitude outcomes**. That gate had **already
fired 8 minutes before this card landed**, into a bin the card's outcome space did not
contain. All facts below re-verified this session (git + read).

**(1) The gate fired bin (iv) CHAIN-INSUFFICIENT.** Prereg `b498d89a` (2026-07-13 18:42,
`research/2026-07-13_np-mass-split-gate_prereg.md`), driver+result `80a76d96` (18:54,
PR #676) — same frozen chain, same δ_th, no refit. Verdict verbatim: *"the canonical
neutron construction (n = 6_2^3 cup 0_1) does NOT define a computable mass split without
new assumptions (the dominant elastic-expansion-tension term is mechanism-named,
magnitude-underived: neutron-identification.md:36,77; constants.py:1104). Enumerated 5
missing choices (C1-C5); did NOT make them."* The composite Faddeev-Skyrme derivation
the split needs **does not exist in the corpus today** — the split is uncomputable, which
is outside the card's sign/magnitude outcome space. **δ_th-free sub-finding banked:** the
SIGN is FORCED POSITIVE (neutron heavier) — both named contributions (threaded 0_1 rest
mass ≥ 0; Ax1 Borromean strain ≥ 0) are positive-definite additions to the bare proton.

**(2) The gate's own "does not load δ_th" reading OVER-REACHED (per the #676 review).**
The `80a76d96` message concluded *"the difference measurement does not actually load
delta_th — the discriminator is structurally mismatched to the corpus ontology"* and
reassigned the burden to the Δ(1232) miss. The #676 independent review found that
interpretation **over-reached**: the corpus TBD-pin (`neutron-identification.md:36,77`)
instructs a **proton-shaped** FS derivation — verbatim *"Same shape as proton mass
eigenvalue derivation"* / *"would parallel self-consistent-mass-oscillator.md for the
proton but with the additional threaded-electron constraint"* — and the proton eigenvalue
**consumes the δ_th-softened κ_FS**. So δ_th-loading is **UNDETERMINED** (the C5 choice
the gate did not make), with carry-over arguably the canonical default. Neither "n-p
carries the *entire* burden" (this card's body) nor "n-p *never* loads δ_th" (the gate
message) is correct; the truth is between and **currently unbuilt**.

**(3) Current burden assignment.** The operative **already-FIRED** δ_th cross-check
remains the **Δ(1232) +2.35% miss** (epic-§40) — proton-specific ppm tightness is a
coincidence at the sibling rung. The **buildable** shot is **ROUTE A**: a composite FS
derivation per the TBD-pin, value-blind, with a **warm-κ_FS (δ_th-softened) vs cold-8π
ablation** measuring the split's δ_th-loading directly — a **Grant-gated charter
candidate**, not a queued driver.

**What is NOT changed:** the card's load-bearing CONCLUSION — δ_th's value provenance =
**calibration-not-prediction as git fact** (residual-first/fitted-after archive
chronology, α-port counter-indicated, +0.74% bare-topology leg untouched) — is
independently intact and NOT touched by this addendum. Only the forward-looking
"n-p-carries-the-burden" *recommendation* is superseded. **No 🔴 header proposed for
constants.py** (Grant-gated). Receipts: `git show -s 80a76d96 b498d89a`;
`neutron-identification.md:36,77`; PR #676.
