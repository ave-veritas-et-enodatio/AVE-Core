# X41 — THE "NOT YET WHY" ARC: derivation + data confrontation + fork record — RESULT

**Date:** 2026-07-10 · **Lane:** implementer · **Branch:** `analysis/x41-scoping-why`
**FROZEN prereg (gated on):** `research/2026-07-10_x41-radiative-scoping-why_prereg_FROZEN.md`
(freeze commit `0180f85a`, PUSHED before this doc — git ordering = freeze proof).
**Adjudicators (P10 / X36):** EXISTING DATA + DERIVATION-FROM-AXIOMS/CANON. **NOT the engine** — the
engine cannot adjudicate a keying choice about its own kernel. **No KB/Letter edit** (research/ only;
`papers/` FIREWALLED).

## ★ ROUTED VERDICT CLASS: **[UNDERDETERMINED — K1 ∧ K2, with the transverse-reactive near-zone as the named discriminator]**

> **K3 (dynamical-content) is CLOSED DEAD** (= the excluded round-1/2/3b family; §STEP-1 of the prereg).
> **K1 (transverse projection) and K2 (impedance/mode-basis) are TWO LIVE, canonically-grounded candidate
> mechanisms** — both reproduce BOTH anchors, both re-derive Route C, both survive the spectroscopy
> re-kill — that the **axioms do NOT force one over the other.** They **diverge only on the
> transverse-reactive near-zone** (K1 loads, K2 not), an **UNBUILT probe**. **K1 is the stronger
> derivation candidate** (it is the drive-direction corollary of a *Grant-ratified* anti-cross-wire
> guarantee, #624/#558) but is **contingent on a surfaced canon contradiction** (`CLAUDE.md`:73+#624 vs
> `CLAUDE.md`:75) that only Grant can adjudicate. **K2 is Grant's preferred EE register** for STATING the
> boundary; it kills net-flux and captures the standing-wave sub-point, but for the load-bearing
> non-uniform-static case it **requires relocating the Axiom-4 kernel from the reactance (Op14) to
> `R_rad`** — a reinterpretation that conflicts with canon and **reduces to the #547 gauge-observability
> RIDER** for the uniform limit.
>
> **NET:** the postulate's "why" is **not closed by the axioms alone**, but the arc moves the state from
> the prereg baseline ("open, K3 dead") to **"open, K3 dead, TWO live canonically-grounded candidate
> mechanisms with a named canon-contradiction (Grant) and a named unbuilt discriminator (the near-zone
> probe)."** This is a real advance, recorded WITHOUT a "derived-why" headline (Rule 11; the seduction
> flag on the #624 rhyme is honored — see §7).

---

## SECTOR HEADER

- **MODE:** derivation-from-axioms/canon (not engine-fire). **REGIME:** the Letter's radiative sector
  (deep-cold, sub-yield, weak-field, transverse on-line pump) + the atomic-static sector (held Coulomb).
- **SECTOR:** the **T2 transverse permittivity** (`ε_eff=ε₀S`, keyed `V_yield`) — the birefringence-bearing
  object — vs the **orthogonal A1 longitudinal bond compliance** (`C_eff=C₀/S`, keyed `V_snap`); the
  **µ/Cosserat-B** sector is the consistency leg (§4). **A1 ⊥ T2** (`master-equation.md`:20 two-"3"s
  disambiguation, Grant-ratified; `CLAUDE.md`:73).

---

## STEP 3 — THE DERIVATION

### 3.0 What the axioms/canon supply (the substrate structure the kernel argument sits in)

The kernel argument is not a free scalar. Canon fixes a **two-domain impedance structure** per node
(`research/2026-07-07_semiconductor-cv-dip_RESULT.md`:200-216, Grant-ratified via PR #558; `node-up`:105
supersession; `CLAUDE.md`:73):

| channel | element | keyed on | read by | impedance domain |
|---|---|---|---|---|
| **T2 transverse permittivity** | `ε_eff=ε₀S` (rolls off) | `V_yield` (43.65 kV) | **transverse-polarized** EM probe | `Z_EM = Z_0` (Ω) |
| **A1 longitudinal bond compliance** | `C_eff=C₀/S` (diverges) | `V_snap` (511 kV) | **longitudinal (bulk)** probe | `Z_bulk` (mechanical `ρc`) |

VERBATIM anti-cross-wire guarantee (`semiconductor-cv-dip`:215): *"Because `Z_EM` (transverse, Ω) and
`Z_bulk` (longitudinal, mechanical `ρc`) live in **different impedance domains**, the two terminal pairs
cannot cross-couple — **that domain separation IS the anti-cross-wire guarantee**: a transverse-EM readout
can NEVER pick up the A1 compliance, and a longitudinal-bulk readout can NEVER pick up the T2 permittivity."*

**This guarantee is BIDIRECTIONAL** (a claim about the coupling between two impedance domains, which is
symmetric in drive↔readout): if the domains cannot cross-couple, then neither can a *longitudinal drive*
reach the T2 permittivity, nor a *transverse drive* reach the A1 compliance. #624 stated the **readout**
direction explicitly; the **drive** direction is the same coupling.

### 3.1 K1 [PROJECTION] — the derivation, and the surfaced contradiction it is contingent on

**The chain.** The Helmholtz decomposition splits any E into `E = E_L + E_T`: `E_L` longitudinal
(curl-free, source-slaved by `∇·E=ρ/ε₀`) and `E_T` transverse (divergence-free, the medium's own
radiative content).
- A **held static Coulomb field is PURELY LONGITUDINAL**: `E = −∇φ`, `∇×E = 0`, so `E_T = 0`
  **identically** (not "small" — exactly zero, for any static charge configuration).
- By the domain separation (§3.0, drive direction), a longitudinal `E_L` drives the **A1 bulk
  compliance** (`Z_bulk`, keyed `V_snap`), and **cannot cross-couple into the T2 permittivity**
  (`Z_EM`, keyed `V_yield`).
- Therefore the **T2 birefringence permittivity sees argument `= |E_T|/E_yield = 0`** for a held static
  Coulomb → `S_ε = 1` → **transparent, DERIVED-EXACT** (the zero is `E_T ≡ 0`, a Helmholtz identity, not
  a bookkeeping cancellation).
- A **propagating pump is purely transverse** (`E = E_T`) → T2 argument `= |E_T|/E_yield = A_V` at FULL
  magnitude → loads `δn_bir = −½A²` (MARK-1 EXACT — no `(kℓ_node)` suppression: this is an amplitude key
  on `E_T`, not a circulation key `∮E·dl`, so it avoids the KNOWN TRAP).

**⚑ K1 IS CONTINGENT ON A REAL, SURFACED CANON CONTRADICTION (flag-don't-fix — both verbatim, NOT
resolved here; Grant adjudicates, X36).** Two canonical statements collide at the longitudinal/transverse
projection, on *adjacent lines of the same file*:
- **`CLAUDE.md`:73 + `semiconductor-cv-dip`:215 (Grant-ratified via #558):** `Z_EM`(T2)⊥`Z_bulk`(A1),
  **cannot cross-couple** — a longitudinal drive reaches only A1. ⟹ **static-E does NOT load T2.**
- **`CLAUDE.md`:75 (VERBATIM):** *"A **static-E-only drive is ASYMMETRIC** … it loads the `ε` /
  capacitive sector only (`S_ε<1`, `S_μ=1`). This gives the **Op14 Meissner-asymmetric** impedance
  `Z_eff=Z_0√(S_μ/S_ε)` … `Z` **changes**, so the boundary reflects (`Γ≠0`)."* ⟹ **static-E DOES load
  `S_ε`.**
- **The collision:** if `CLAUDE.md`:75's "static-E" is the (longitudinal) lab/Coulomb field and its
  "`S_ε`" is the T2 permittivity, then :75 **contradicts** :73+#624. **The resolution hinges on whether
  `CLAUDE.md`:75's `S_ε<1` load is the T2 permittivity (K1 fails, #547-charge-keyed stands) or the A1
  compliance (K1 stands; the Op14 `Γ≠0` mirror is then a *longitudinal-probe* observable, invisible to a
  transverse birefringence probe).** The later, Grant-ratified #624 domain-separation *implies the latter*
  — but :75 was not propagated to match. **This is a corpus-consistency call for Grant, surfaced not
  decreed** (the auditor lane lands any KB edit).

**K1 re-attributes #547's muon overshoot to the A1 sector (the residual DRIVE cross-wire).** #547
(`em-keying-round3-eps-dc-mechanism_RESULT.md`, merged) computed the muon overshoot with the **T2 key**
(`A_V = V/V_yield`, M0, §9: `1.52×10⁶ µeV`) applied to the **longitudinal** proton Coulomb field. Per the
anti-cross-wire guarantee (drive direction), a longitudinal field cannot drive the T2 permittivity —
#547 **cross-coupled a longitudinal drive into `Z_EM`.** #547 itself carried the "**three-way
varactor-convention tangle**" as an OPEN Grant-adjudication item (its flags, verbatim: *"the ε-grade
varactor identity … surfaced for Grant's adjudication; not resolved here"*), and it predates full
integration of the #558 resolution. **Correctly sector-attributed:** the muon Lamb shift is an
**electrostatic (longitudinal-photon / vacuum-polarization) effect → an A1/`Z_bulk` probe**; re-keyed to
`V_snap` the A1 load is `~α×` the argument (`~α²×` the deficit) but STILL overshoots (`~1.1×10⁴ µeV`), so
the **A1 longitudinal static extension is separately constrained/scoped at `ℓ_node`** (the discreteness
cutoff, `p4`/#547 §9 band-split) — **while the T2 birefringence is transparent by `E_T≡0` (K1).** The
muon never was a T2-sector constraint; it became one only under #547's drive cross-wire.

**Symmetric-standard check (consensus-bias guard):** QED *also* separates the muonic-H Lamb shift
(longitudinal Coulomb / vacuum polarization) from vacuum birefringence (transverse light-by-light) — they
are different sectors there too. So K1's sector-separation is **not AVE special-pleading**; the
AVE-distinct content is only that the Ax-4 *saturation* keys on `E_T` (so a strong longitudinal field does
not saturate the transverse permittivity).

### 3.2 K2 [IMPEDANCE / MODE-BASIS] — the EE register, and the reactance-vs-`R_rad` fork

**What K2 delivers cleanly.**
- **Net-flux is NOT K2** (basis membership, not net Poynting) — so K2 survives the round-2 STEP-0 net-flux
  kill and correctly predicts a **standing wave LOADS despite zero net flux** (two counter-propagating
  on-line modes). **Confirmed by the p5 datum** (standing-wave CONTROL: `1−S_ε=4.75×10⁻²` at net
  `F=1.17×10⁻¹⁸≈0`).
- **Pump** (propagating, on-line) → loads full (MARK-1 EXACT). **`R_rad≡Z_0`** is canon
  (`substrate-native-terminology.md`:43, *"radiation resistance `R_rad≡Z_0` (wave-making drag, a real
  port)"*) — "the kernel lives inside the only resistor the vacuum has."
- **Muon** (held static, `ω=0`) → radiates zero power → zero `R_rad` coupling → **never meets the kernel →
  transparent** (MARK-2 reached, via "static → no `R_rad`").

**⚑ Where K2 is CONTESTED (the load-bearing headwind).** For the **non-uniform static** case (the muon /
atomic Coulomb), K2 must assert that a held static field **does not bias the reactance** at all — but
canon places the Ax-4 kernel **in the reactance** (Op14 `Z_eff=Z_0/√S`, `operators.md`:54; `ε_eff=ε₀S`),
and #547 M3 derives that a held bias `A_0` **shifts the small-signal reactance** `C₀·S(A_0)` a co-located
probe reads. K2 therefore needs the kernel **relocated from the reactance to `R_rad`** (a reinterpretation
of "loading" as `R_rad`-coupling-gated). **For a UNIFORM held field K2 REDUCES to the #547
gauge-observability RIDER** (both say: loaded-but-gauge-hidden / never-on-line coincide — no readable
shift). For the NON-uniform Coulomb the two diverge: #547-RIDER says the gradient is readable (`Γ≠0`,
refracts a probe — a static `ε`-gradient *is* a GRIN lens), K2 says it never biased `ε` in the first
place. **The discriminator between #547-M3 (reactance) and K2 (`R_rad`) is the EE-bench CVR test** (does a
held DC E shift the vacuum's small-signal `C`? — the deferred cRIO `C_eff(V)` bench), which the engine
cannot pre-empt (X36). So K2 is the correct **register** for stating the boundary and is derivation-clean
for the *uniform/on-line* facts, but it does **not** by itself derive the non-uniform-static transparency
against Op14 — it **inherits the incumbent RIDER** there.

### 3.3 Why the axioms do NOT force one (the honest UNDERDETERMINATION)

K1 and K2 **agree** on every adjudicated config: pump loads (both), Coulomb transparent (K1: `E_T≡0`; K2:
`ω=0`→no `R_rad`), static-B transparent (both, §4), standing wave loads (K1: transverse; K2: basis-member
— p5-confirmed). They **split only** on the **transverse-reactive near-zone** (antenna induction `1/r²`:
Helmholtz-transverse + reactive/off-line): **K1 says LOADS** (nonzero `E_T`), **K2 says NOT** (reactive,
`|Γ|=1`, off-line). No existing datum tests this (§STEP-4c). So the axioms + existing data are
**insufficient to force K1 vs K2** — the routed class is **UNDERDETERMINED**, with the near-zone probe as
the named discriminator.

---

## STEP 4 — DATA CONFRONTATION

### 4a — the two mandatory anchors (both keys pass)

| anchor | K1 [projection] | K2 [impedance/mode-basis] | incumbent #547 [charge-keyed] |
|---|---|---|---|
| **MARK-1 pump** (transverse, `A²≈6e-7`, `δn=−½A²`) | `E=E_T` → full load, `−½A²` **EXACT** | on-line → full load **EXACT** | full load (loads on `|E|`) |
| **MARK-2 muon** (held Coulomb, longitudinal) | `E_T≡0` → T2 load **= 0 EXACT** (derived); muon overshoot is A1-sector | `ω=0`→no `R_rad`→ T2 load `=0`; but reactance-bias contested | **LOADS** `1.52×10⁶ µeV` → scope-OUT (data-acquired) |

Both K1 and K2 reproduce MARK-2 as **derived zero** (vs #547's loads-then-scope-out). Per the prereg §4
flag, the muon **cannot discriminate** derived-zero from scope-out at the data level — the difference is
mechanism-class. **K1's zero is the sharpest** (`E_T≡0` is an exact Helmholtz identity for any static
charge).

### 4b — the spectroscopy re-kill check (do bound-state near-fields load?)

The strong field in a bound atom (the nuclear Coulomb) is **static + longitudinal → `E_T≡0`** → routes to
A1, NOT the T2 birefringence sector. The only nonzero T2 content in an atom is the **transverse
radiative/virtual** field (retardation/Breit, `~(Zα)²` of the Coulomb *in the transverse channel*, and
the on-shell transition fields are single-photon-tiny). **K1:** T2 loads only that transverse content →
parametrically negligible → **NOT re-killed by precision spectroscopy.** **K2:** on-shell transverse →
loads (tiny); off-shell/virtual → off-line → does not load → **also not re-killed.** (The muon's static
proton **magnetic** dipole field is `∂_tB=0` → Route-C transparent — µ-sector, not ε; it does not
resurrect a loading.) **Both keys survive** the atomic-spectroscopy re-kill; the strong-field overshoot
that killed the naive continuum law lived in the **longitudinal** channel both keys route away from T2.

### 4c — the near-zone discriminator: what existing data touches it (expected: none)

**Inventory result: NO existing datum touches the ε transverse-reactive near-zone.** The closest corpus
touch is the **µ-sector `(kr)²` near-zone table** (p5: `A_I∝(kr)²` suppression of the reactive *magnetic*
near-zone) — but that is the circulation sector and is consistent with BOTH keys. The **ε-side
transverse-reactive near-zone is UNTESTED.**
- **Named registered-probe CANDIDATE (flagged, NOT registered — a gated follow-on):** drive a
  **transverse-reactive near-zone E** (the induction zone of a small oscillating electric dipole,
  `kr≲1`: transverse, time-varying, non-radiating, source-attached) and read vacuum ε-loading. **K1 →
  loads; K2 → null.** This is the clean K1/K2 discriminator.
- **The one plumber-physical question (surfaced to Grant, pre-test-physics-check):** *in the antenna
  induction zone — the stored, non-radiating, transverse `1/r²` reactive field around a small oscillating
  dipole — does the vacuum's ε-nonlinearity engage (transverse energy, K1) or stay silent (reactive
  energy never on the line, K2)?*

---

## STEP 4′ — THE µ-SIDE CONSISTENCY LEG (both keys re-derive Route C; a check, not a discriminator)

- **K1 unification ("medium's own vs source-slaved"):** the µ-inductor keys on the **circulation /
  solenoidal** (induced, medium's-own) magnetic content `∮H·dℓ = ε₀∂_t∫E·dA`; a source-slaved static
  Biot-Savart B is curl-free in vacuum → zero circulation → transparent. Dual of "T2 keys on `E_T`":
  **both sectors — source-slaved (longitudinal-E / static-Biot-Savart-B) → transparent** (ONE principle).
- **K2 unification:** a static B is the `|Γ|=1` reactive limit (`ω=0`, no radiation) → off-line →
  transparent, identical to the static-E off-line argument; the p5 `(kr)²` reactive-near-zone suppression
  is consistent. **ONE principle (reactive/off-line → transparent).**

**Both re-derive Route C** (`S_B=√(1−A_I²)`, static B → `A_I=0` → transparent) under a single principle →
**no divergence to report.** (This is a consistency PASS for both, so it does not break the tie.)

---

## STEP 5 — FORK RECORD + VERDICT

| key | routed status | derivation footing | anchors | discriminator |
|---|---|---|---|---|
| **K3** dynamical-content | **CLOSED DEAD** | = excluded round-1/2/3b family (Letter verbatim) | — | — |
| **K1** transverse projection | **LIVE — DERIVED-WHY CANDIDATE (strongest), contingent on Grant** | drive-direction of the Grant-ratified anti-cross-wire guarantee (#624/#558); `E_T≡0` exact for static Coulomb; re-attributes #547 muon to A1. **CONTINGENT** on adjudicating `CLAUDE.md`:73+#624 vs :75. | MARK-1 ✓ EXACT; MARK-2 ✓ EXACT (`E_T≡0`) | near-zone → **LOADS** |
| **K2** impedance/mode-basis | **LIVE — the EE REGISTER; reduces to the #547 RIDER for uniform-static** | `R_rad≡Z_0` canon; kills net-flux; standing-wave p5-confirmed. **CONTESTED:** needs Ax-4 kernel relocated reactance→`R_rad` (conflicts Op14). | MARK-1 ✓ EXACT; MARK-2 ✓ (via `ω=0`→no `R_rad`) | near-zone → **NULL** |

**VERDICT CLASS: [UNDERDETERMINED — K1 ∧ K2, transverse-reactive near-zone the named discriminator].**
The postulate's "why" is **not closed by the axioms alone.** Honest state-change vs the prereg baseline:
**from "open, K3 dead" → "open, K3 dead, two live canonically-grounded candidate mechanisms, with (i) a
named canon contradiction for Grant (`CLAUDE.md`:73+#624 vs :75, the projection question) and (ii) a named
unbuilt discriminator (the transverse-reactive-near-zone probe)."** K1 leads on derivation footing; the
adjudication is Grant's (the contradiction) + a future bench (the probe) — **the engine cannot decide
it** (X36).

**No `[DERIVED-WHY]` headline is claimed** (Rule 11): the #624-rhyme is a *rhyme* (§7), the near-zone
discriminator is unbuilt, and the #547 re-attribution is a *surfaced* Grant item, not a decree. **No
criterion was dropped;** K1/K2 were not forced, so the routed bin is the honest UNDERDETERMINED one, not a
manufactured win. **No fourth key was minted** (Rule 12).

**NO figure** — the arc's product is structural (which sector the argument lives in); no numerical result
warrants a WHITE figure. **The Letter consequence is GATED FUTURE WORK only** (§7).

---

## 6 — CONSISTENCY-VS-EMERGENCE CLASSIFICATION

- The **UNDERDETERMINED verdict** is a structural (which-sector-owns-the-argument) result — **MANIFESTATION
  class** (a consequence of the K4 two-domain impedance structure + Helmholtz decomposition), scale-
  invariant, α-firewalled off the routing.
- The marks (pump `A²`, muon overshoot) ride CODATA-derived `E_c=√α·E_crit` — **CONSISTENCY-class
  magnitudes**, not headlined. **No emergence claim.**

---

## 7 — SURFACED TO GRANT / THE AUDITOR LANE (flag-don't-fix; NO KB/Letter edit landed here)

1. **⚑ Canon contradiction (the load-bearing one).** `CLAUDE.md`:73 + `semiconductor-cv-dip`:215
   (Z_EM⊥Z_bulk, cannot cross-couple, Grant-ratified #558) vs `CLAUDE.md`:75 (static-E-only loads
   `S_ε<1`, Op14 `Γ≠0` mirror). The projection question — *does a longitudinal static E load the T2
   permittivity, or only the A1 compliance?* — decides whether the radiative scoping is DERIVED (K1) or
   stays DATA-acquired (#547). **Surfaced with both verbatim; Grant adjudicates.** The auditor lane lands
   any `CLAUDE.md`:75 clarification (e.g. tagging its `S_ε` load as the A1/`Z_bulk` channel, its `Γ≠0` as
   a longitudinal-probe observable) — I do NOT draft it.
2. **⚑ #547 residual DRIVE cross-wire.** #547's muon overshoot loaded the **T2 permittivity** (keyed
   `V_yield`) with a **longitudinal** Coulomb field — the drive-direction of the cross-wire #558 fixed on
   the readout/form side. Under the anti-cross-wire guarantee the muon is an **A1** constraint, not a T2
   one. **This does NOT retract #547** (Rule 12): its charge-keyed math stands as the incumbent; the
   surfaced item is the *sector attribution* of its muon leg. Grant/auditor decide whether #547's §9
   gets an A1/T2 sector-attribution note.
3. **The near-zone probe** — a **registered-probe candidate** (transverse-reactive E, `kr≲1`, K1-loads /
   K2-null) and the **CVR bench** (held-DC-E vacuum-`C` shift, #547-M3 reactance vs K2 `R_rad`) are the
   two experiments that would close the fork. **Flagged, not registered** (gated follow-on; the deferred
   cRIO `C_eff(V)` bench is the natural home of the CVR test).
4. **Letter consequence — GATED FUTURE WORK ONLY.** IF Grant adjudicates the projection question toward
   K1, the Letter's "open postulate" could upgrade to a **derived T2-sector scoping** (the birefringence
   law keys on `E_T`; static longitudinal fields are the orthogonal A1 sector). **This is downstream of
   adversarial review + Grant; the Letter is FIREWALLED and untouched by this arc.**

---

## 8 — DISCIPLINE

- **challenge-canonical-negative:** #547 was challenged by grepping its CONFIGS (M0 used `V/V_yield` for a
  longitudinal field — the residual cross-wire), not its conclusion; the ½/¼ tell is guarded (all
  coefficients are the sqrt-kernel's own `−½A²`).
- **flag-don't-fix:** the `CLAUDE.md`:73-vs-:75 contradiction and the #547 sector-attribution are surfaced
  with both verbatim, resolved by NEITHER — Grant's call (§7). No canon rewritten.
- **Rule 11 honest closure:** the axioms do not force a key → the routed bin is UNDERDETERMINED, not a
  manufactured `[DERIVED-WHY]`. **Rule 12:** no retraction of #547, no fourth key minted.
- **P10 / X36:** the engine cannot adjudicate its own kernel's keying; the adjudicators named are the
  canon contradiction (Grant) + two unbuilt benches. **Seduction flags honored (§7 item 1):** the #624
  A1/T2 cross-wire is a *rhyme* that MOTIVATES K1 — the derivation rests on the *independently-grepped*
  domain-separation guarantee (#624:215) and the exact `E_T≡0` Helmholtz identity, not on the rhyme; the
  0-for-N forward-prediction ledger's thinning is respected (no chord banked — this is a candidate
  mechanism awaiting Grant + a bench).
- **phase-space-coordinate-check (A46):** keys/marks in matched coordinates (transverse projection /
  mode-basis / `A_V`); the near-zone `F`/`kr` axes are discriminator axes, never keying coordinates.
- **consistency-vs-emergence:** MANIFESTATION-class verdict; CONSISTENCY-class magnitudes; no emergence
  headline.
- **verify-before-cite:** every cite re-grepped at branch tip `117d9063` this session (Letter :446-454;
  #547 M0/M1/M2/M3 + §9; p5 standing-wave row; node-up:105 #558 supersession; `semiconductor-cv-dip`:200-216;
  `CLAUDE.md`:73,75; `master-equation.md`:20; `substrate-native-terminology.md`:43; `operators.md`:54).
- **NO KB canonization / NO Letter edit from this lane** — research/ docs only; all consequences are gated
  follow-ons for Grant + the auditor lane.
