# RESULT — Compositeness-Defense Gate-0 (analytic)

**Status:** RUN-COMPLETE (analytic). **VERDICT: SPLIT by channel** — see §0.
**Prereg (FROZEN):** [`2026-07-03_compositeness-defense-gate0_prereg.md`](2026-07-03_compositeness-defense-gate0_prereg.md) @ commit `e414d6c8`.
**Docket:** B2 (COMPOSITENESS-DEFENSE arc), Grant-commissioned 2026-07-03.
**Branch:** `analysis/compositeness-defense` (off `origin/main` @ `e06b6e9d`). NO self-merge.
**Classification (`consistency-vs-emergence`):** DEFENSE / CONSISTENCY for the two settled channels; ILL-DEFINED for the one open channel. NO chord minted (charge channel chord-room ~zero, pre-registered §2 of prereg; moment channel is echo/consistency).

---

## 0. VERDICT (one line per channel + the composite)

- **Wall channel (ii) — DEFENSE-DERIVED.** A transverse EM hard probe does NOT see the electron's Γ=−1 wall as a mirror: the EM-transverse channel is impedance-matched (Γ_EM = 0 everywhere under SYM scaling, corpus-derived), so the "wall" is a bulk/shear object invisible to the EM probe. The naive "7-OOM-too-big body vs 1e-19 m bound" tension is DISSOLVED — the probe is in the matched channel, not reflecting off the body.
- **Charge channel (i) — ILL-DEFINED at current corpus grade (the load-bearing blocker).** F₁(q²) ≡ 1 holds rigorously IF-AND-ONLY-IF the exterior EM readout of the boundary integer is exactly Coulombic (1/r). **The corpus does not derive the exterior electric-field shape** — it is internally CONTRADICTORY (one leaf: 1/r Coulomb leak; another: exponentially-suppressed hedgehog tail; the 1/r-vs-α·1/r shape is a flagged open item). So the topological-charge argument's PREMISE is asserted-not-derived. Named blocker + what's missing (§2, §5).
- **Moment channel (iii) — DEFENSE / CONSISTENCY (not a chord).** F₂ deviations live in the gapped-ω sector; the magnitude is BLOCKED (ω_gap host-knob, per clm-wcoul2) and the sign/existence content is signed-Coulomb consistency (echo — a_e = α/2π re-reads the baked α). No F₂ deviation is derivable above the g−2 bound at current grade; equally, no distinct sub-bound chord is derivable. Survives-by-consistency, no chord.
- **COMPOSITE BIN: [ILL-DEFINED]** (prereg §5) — the arc PROCEEDS to the HELD engine leg, whose job is to resolve the charge-channel exterior-tail-profile fork numerically. The wall channel closes as DEFENSE-DERIVED regardless (independent of the engine leg).

**Ontology-fork resolution:** the derivation selects **candidate (ii)-collapses** (the wall is not an EM scatterer — corpus-derived) and **narrows candidate (i) to the exterior-tail-profile fork it cannot settle analytically** (reading (a) exactly-Coulombic vs reading (b) ℓ_node-departure — the corpus premise is contradictory, so this is the fork-to-computable the engine leg must run). Candidate (iii) resolves to CONSISTENCY, not chord. **No unilateral pick** on the (a)/(b) fork — surfaced with the engine-leg computation as the discriminator (per pre-test-physics-check trigger 9).

---

## 1. WALL CHANNEL (ii) — DEFENSE-DERIVED

### 1.1 The claim

A hard transverse EM probe of wavelength λ ≪ ℓ_node does not reflect off the electron's Γ=−1 confinement wall, because that wall is a **bulk/shear-channel** boundary and the **EM-transverse channel is impedance-matched** at it.

### 1.2 The derivation (corpus-cited, verified this session @ e06b6e9d)

The three-impedance law assigns every reflection statement a channel subscript. For the electron:

- **EM channel is matched.** `electron-bh-isomorphism.md:24` (verbatim): *"the characteristic impedance Z_EM(r) = √(μ'(r)/ε'(r)) = Z₀ is invariant at all radii, because both μ' and ε' scale identically with n(r). There is no EM impedance mismatch and no EM reflection coefficient (Γ_EM = 0 everywhere under SYM scaling)."* This is the SYM-scaling mechanism: gravity/saturation scales μ and ε **together**, so their ratio (the EM impedance) is invariant. Derived, not asserted.
- **The wall is bulk/shear.** `bulk-impedance-at-saturation-boundary.md:71` (electron row, verbatim): *"EM channel: Z_EM = Z₀ (matched vacuum); confinement is not EM-short."* The Γ=−1 wall is Z_bulk → 0 (`three-channel-impedances.md:22`, `bulk-impedance:73`).
- **Matched ⇒ transparent (δ→∞).** `translation-circuit.md:541` (δ↔Γ conjugate, verbatim): *"matched (Γ = 0, photon) → δ → ∞ (transparent, all-bulk propagation)."* An EM probe in a matched channel is not reflected; it propagates through.

### 1.3 Dictionary-translated counterfactual (Step 2.7)

QED: the electron's Coulomb potential scatters a probe by Rutherford/Mott — there is no "mirror" in QED either; the electron is transparent to a photon except via the Coulomb/Compton coupling. AVE's Γ_EM = 0 is CONSISTENT with QED's no-mirror electron. **This is DEFENSE (the exposure's "does a hard photon punch through and see the loop?" is answered: the photon is in the matched channel — there is no wall to punch through in the EM channel), classified CONSISTENCY vs the dictionary-translated QED (no AVE-distinct chord here).**

### 1.4 The ω_C = Compton-frequency coincidence (derived consistency, not asserted)

The wall's characteristic frequency is ω_C = c/ℓ_node ≈ 7.76e20 rad/s, and ℏω_C = m_e c² = 511 keV EXACTLY (`constants.py:294`, verified). Since ℓ_node = ℏ/(m_e c) is the Compton wavelength BY the calibration-anchor identification (`electron-identification.md:54,60`), the wall's bandwidth scale IS the electron mass scale by construction — not a coincidence to be explained but an identity of the calibration. "Above the wall's bandwidth" = "above m_e" = where QED's own structure (pair production, ℏω > 2m_e c²) turns on. So the statement "the AVE wall becomes irrelevant exactly where QED's own electron stops being a single point" is a **consistency of the calibration identity**, not an independent chord. Honest framing: it is a pleasing internal consistency (the AVE structure scale and the QED structure scale coincide because both ARE the Compton scale), NOT an AVE-distinct prediction. (Flag: this is the same instrument-echo-trap as the g−2 row — ℓ_node = Compton wavelength is a doubly-over-determined echo, `claim-quality.md` clm-stgx1i / the coverage-matrix g−2 row.)

---

## 2. CHARGE CHANNEL (i) — ILL-DEFINED (the load-bearing blocker)

### 2.1 The topological-charge argument, stated

Charge is 𝓠 = Link(∂Ω, F_substrate) ∈ ℤ — a **boundary linking integer**, a 1D line-integral observable (`boundary-observables-m-q-j.md:20`), NOT a bulk density ρ(r). If the probe couples only to this integer, and the exterior field of the integer is exactly the point-charge Coulomb field, then F₁(q²) ≡ 1 at all q² — pointlike by topology. This is the DEFENSE-DERIVED outcome the arc hoped for.

### 2.2 Where it holds — and where it BREAKS (the sharpened fork)

Per the prereg §1.3 sharpening (form factor measures the SOURCE's departure from a point): an exactly-1/r exterior tail IS the point-charge field ⇒ F₁ ≡ 1 identically (Rutherford off pure Coulomb has F = 1). So the topological argument's conclusion (F₁ ≡ 1) holds **IF AND ONLY IF the exterior EM readout of the boundary integer is exactly Coulombic (1/r) with no ℓ_node-scale departure.** The integer-ness of 𝓠 is not sufficient by itself — a finite-thickness source with integer total charge still has a form factor if its exterior field departs from 1/r at ℓ_node scale.

### 2.3 The corpus premise is ASSERTED-NOT-DERIVED and INTERNALLY CONTRADICTORY (flag-don't-fix)

The exact-Coulombic exterior — the load-bearing premise of the F₁ ≡ 1 argument — is **not derived** in the corpus, and two leaves are in tension:

- **Leaf A (asserts 1/r Coulomb leak):** `translation-circuit.md:541` (verbatim): *"the evanescent tail leaking out is the long-range (~ℓ_node/r Coulomb) field, i.e. how a trapped soliton couples to the outside vacuum."* — asserts a 1/r-shaped Coulomb tail.
- **Leaf B (says exponentially-suppressed hedgehog, no stated Coulomb 1/r):** `substrate-perspective-electron.md:109` (verbatim, "Outside the loop, Regime I vacuum"): *"‖ω‖², ‖V_inc‖² | Decay rapidly (hedgehog tail; exponentially-suppressed in saturation regime)"*; the ONLY long-range survivor stated there is the **1/r² Op14 gravitational** refractive-index gradient (`:113`, `:169`), NOT a Coulomb 1/r electric tail.
- **The shape itself is a flagged open item:** `claim-quality.md:1311` (verbatim): *"WHY topological strain equals ℓ_node/r rather than α·ℓ_node/r from first principles is an open multi-week analytical item."* — the 1/r-vs-α·(1/r) coefficient/shape of the near-field strain is unresolved.
- **A grep for a DERIVED Coulomb 1/r exterior electric field of the electron returns EMPTY** (this session, `git grep` for `Coulomb...field | electric field...1/r | charge...1/r` excluding 1/r² — no derivation hit). The corpus derives the 1/r² GRAVITATIONAL tail (Op14) and the exponential ω-hedgehog decay, but NOT the Coulomb 1/r ELECTRIC tail whose shape the F₁ argument needs.

**Consequence:** the analytic Gate-0 CANNOT rigorously establish reading (a) (F₁ ≡ 1), because its premise (exactly-Coulombic exterior) is (1) asserted in one leaf, (2) apparently contradicted (exponential hedgehog) in another, and (3) shape-open in the register. It also cannot establish reading (b) (a specific ℓ_node departure) because no departure profile is derived. **This is [ILL-DEFINED] per prereg §5** — the charge-channel form factor is not derivable at current corpus grade. Named blocker: the exterior electric-field profile of the boundary integer (1/r exact? α·1/r? exponentially-screened with a 1/r² gravitational survivor only?). What's missing: a substrate-native derivation OR numerical measurement of E(r) outside the seeded 0₁ at r ≥ ℓ_node.

### 2.4 Asymmetric stakes still hold (pre-registered, prereg §2)

IF the engine leg lands reading (b) (a resolved O(1) ℓ_node-scale departure), it lands in **EXPOSURE-CONFIRMED**: an O(1) ℓ_node-scale F₁ departure is a shell-like (sinc(qR)-class) form factor deviating at q ≳ m_e, ~5 OOM inside the LEP contact bound (B2, Λ ≳ 10 TeV ≈ 10⁵×(1/ℓ_node)). Charge-channel chord room ≈ zero, as pre-registered. IF it lands reading (a) (exact 1/r to tolerance), DEFENSE-DERIVED and the gap closes. The engine leg is thus a genuine survival discriminator, not a chord hunt.

---

## 3. MOMENT CHANNEL (iii) — DEFENSE / CONSISTENCY (no chord)

### 3.1 Where the moment structure lives

F₂ (the magnetic form factor) is carried by the winding circulation = the **gapped ω (Cosserat rotation) sector**, which is a DIFFERENT sector from the gapless EM charge channel (sector-ownership, prereg §0 CP2). Per `clm-wcoul2` (verified §claim-quality.md:1612–1640 this session): the winding couples electrically through the gapped ω sector via a massive-vector-like (Yukawa) exchange.

### 3.2 The bound comparison (B1, the sharpest knife)

- **g = 2 (leading):** POSITED, not axiom-derived (`electron-identification.md:58`, verified — 2026-06-21 Rule-12 re-scope: the 2π/4π double-cover forces spin-½, NOT the value of g; proton/neutron g≠2 are the decisive falsifier). So AVE does not independently predict g=2; it imports the Dirac value. An imported value cannot deviate from the bound — it IS the bound's central value by import. CONSISTENCY.
- **a_e = α/2π (g−2 Petermann):** parameter-free at +4.0% (symmetric Route B), 50 ppm only conditional on the n_q-additivity postulate (`electron-identification.md:59`, verified). This RE-READS the baked α (the coverage-matrix g−2 row `clm-stgx1i`: FORM=chord-shaped 1/π² form-factor / VALUE=ECHO, α PLUGGED IN). So the a_e match is an ECHO/CONSISTENCY, not an independent F₂ prediction — and its +4.0% parameter-free forward sits ABOVE the ~1e-12 g−2 agreement bound (B1), i.e. AVE's parameter-free F₂ forward is 4% off, which is NOT a bound violation (it is a not-yet-closed derivation, honestly scoped as +4.0% / 50ppm-conditional), and NOT a sub-bound chord either.
- **Magnitude BLOCKED (pre-declared, prereg §3):** the engine's ω-sector force magnitude rides ω_gap = host-knob (not Ω_C = c/ℓ_node), per clm-wcoul2 (`claim-quality.md:1624`). So no AVE F₂ q²-magnitude is derivable at current engine grade — the Yukawa range/mediator-mass is artifact-scale.

### 3.3 Verdict on the moment channel

No F₂ deviation is derivable ABOVE the g−2 bound (the parameter-free forward is 4% off in the coefficient, a derivation-gap, not a bound-exceeding deviation of a converged prediction). Equally, no DISTINCT sub-bound q²-shaped F₂ chord is derivable (magnitude blocked; the sign/shape content is signed-Coulomb consistency — the same COULOMB-RECOVERY lesson as clm-wcoul2). **Moment channel: survives-by-consistency, no chord.** Chord room here is gated on the two clm-wcoul2 strengthen-by items (map ω_gap → Ω_C; find a plane-conservative far-field extraction) — a future-work dependency, not this Gate-0.

---

## 4. THE BOUNDS-TABLE COMPARISON (all five, per channel)

| Bound | Channel | AVE Gate-0 status | Verdict |
|---|---|---|---|
| B1 g−2 / F₂(0) ~1e-12 | moment (F₂) | a_e = α/2π is an ECHO (consumes α); parameter-free forward +4.0% (derivation-gap, not a converged deviation); magnitude BLOCKED (ω_gap host-knob) | CONSISTENCY — no bound-exceeding deviation derivable; no sub-bound chord derivable |
| B2 LEP contact Λ ≳ 10 TeV | charge (F₁) | F₁ ≡ 1 IFF exterior exactly Coulombic — PREMISE asserted-not-derived + corpus-contradictory | ILL-DEFINED; IF engine lands reading (b) O(1) departure → EXPOSURE-CONFIRMED (5 OOM inside) |
| B3 LEP/SLC Bhabha dσ/dΩ | F₁ + F₂ | same F₁ blocker; F₂ echo | ILL-DEFINED (rides B2's F₁ resolution) |
| B4 Møller (E158) | ee corr. (gapped-ω) | short-range ω-mediated e-e correction exists in principle; magnitude artifact-scale (ω_gap) | future-work (§6), not derivable now |
| B5 electron "radius" | F₁/F₂ extent | ℓ_node ≈ 3.86e-13 m is ~5–9 OOM larger than quoted r_e bounds — BUT this is the naive real-space-body tension the wall-channel result (§1) DISSOLVES (EM probe is in the matched channel, not reflecting off the body) | DEFENSE for the naive tension; the real F₁ question is §2's exterior-tail fork |

**No derived deviation EXCEEDS any bound at this Gate-0.** The one place a bound-exceeding outcome could arise (B2, reading (b)) is exactly the ILL-DEFINED blocker the engine leg resolves. So the honest state: **survival is intact everywhere a verdict is derivable; the one channel that could break survival (charge F₁) is not yet derivable and is handed to the engine leg with EXPOSURE-CONFIRMED pre-registered as the (b)-outcome bin.**

---

## 5. THE BLOCKER, NAMED (what the engine leg must resolve)

**Blocker:** the exterior electric-field profile E(r) of the boundary-charge integer 𝓠 = Link(∂Ω, F) at r ≥ ℓ_node, in the matched EM channel. Specifically: is E(r) ∝ 1/r² (exact Coulomb potential ⇒ 1/r potential ⇒ F₁ ≡ 1), or does it carry an ℓ_node-scale departure (⇒ F₁ = 𝓕[departure])?

**Why the analytics can't settle it:** the corpus (a) asserts a 1/r Coulomb leak in one leaf (`translation-circuit.md:541`), (b) states exponentially-suppressed hedgehog decay with only a 1/r² GRAVITATIONAL long-range survivor in another (`substrate-perspective-electron.md:109,113`), and (c) flags the near-field strain shape (1/r vs α·1/r) as an open multi-week item (`claim-quality.md:1311`). No leaf DERIVES the exterior Coulomb electric field's shape. The premise of the F₁ ≡ 1 argument is therefore not available at corpus grade.

**What's missing / the engine leg's job (HELD, prereg §7):** measure E(r) (or the ω-field normal stress T^{rr}) outside a seeded, self-subtracted 0₁ unknot on the writhe-campaign host, over r ∈ [ℓ_node, several·ℓ_node], and fit the exterior profile. Frozen bins already declared in prereg §7 (TAIL-EXACT-COULOMB / TAIL-DEPARTS / GAMMA-EM-NONZERO / ENGINE-BLOCKED). Note the clm-wcoul2 caveat: the host's far-field is Yukawa-screened at the gapped-ω scale and the magnitude is knob-ridden — so the engine leg must extract the EM-channel (gapless) exterior field specifically, NOT the ω-channel (gapped) force, or it will measure the screened Yukawa tail and mis-read it as an F₁ departure. This channel-separation requirement is itself a design constraint the engine-leg prereg must freeze.

---

## 6. FUTURE-WORK NOTES (not this Gate-0)

- **Møller-scattering observable (B4):** a short-range gapped-ω e-e correction is in principle a parity/Møller observable (E158-class). Currently artifact-scale (ω_gap host-knob, clm-wcoul2), so NO bench-reachable prediction. Becomes assessable only after the clm-wcoul2 strengthen-by item (map ω_gap → Ω_C). One-line note, artifact-scale caveat.
- **The g−2 Petermann closure (n_q-additivity postulate)** is the gating item for any F₂ chord; tracked at C3-MUON-DELTA (`electron-identification.md:71`), out of scope here.

---

## 7. DISCIPLINE LEDGER

- **`verify-before-cite`:** every file:line re-verified against `origin/main` @ `e06b6e9d` this session. Drifts: none carried forward unverified. Key verifications: `electron-bh-isomorphism.md:24`, `bulk-impedance-at-saturation-boundary.md:71`, `translation-circuit.md:541`, `substrate-perspective-electron.md:109/113/169`, `claim-quality.md:1311/1612-1640`, `electron-identification.md:54/57/58/59`, `boundary-observables-m-q-j.md:20`, `constants.py:282/294`.
- **`flag-don't-fix`:** the charge-channel exterior-field contradiction (Leaf A 1/r Coulomb vs Leaf B exponential hedgehog + 1/r² gravitational-only) is SURFACED with both verbatim quotes + file:line (§2.3), NOT resolved. This is the load-bearing blocker; Grant adjudication + the engine leg resolve it, not a reframe.
- **`consistency-vs-emergence`:** wall channel DEFENSE/CONSISTENCY; moment channel CONSISTENCY/ECHO; charge channel ILL-DEFINED. No emergence-class claim. No chord minted.
- **`ave-discrimination-check` Step 2.7:** F₁ ≡ 1 (if it held) would MATCH dictionary-translated QED tree-level ⇒ consistency not chord. a_e = α/2π MATCHES QED ⇒ echo. ω_C = Compton coincidence is a calibration-identity echo. All chord language withheld.
- **`ave-prereg` Step 3.7:** form-end (existence/sign) was primary; F₂ magnitude pre-declared BLOCKED, so no gate demanded a blocked-magnitude number.
- **INVARIANT-N1:** no new substrate noun; F₁/F₂/Γ_EM(q) are measurement quantities on the existing three-channel impedance MODEL.

---

## 8. WHAT UPDATES THE CORPUS (staged, auditor lands the manual)

Because the composite bin is **[ILL-DEFINED]** (not DEFENSE-DERIVED or CHORD-CANDIDATE), the prereg §5 corpus-update actions (coverage-matrix row → DEFENSE, boundary-observables q²-conditioned no-hair paragraph) are **NOT** fully triggered — the charge channel is not yet closed. However, TWO honest partial updates ARE warranted and are surfaced for the auditor to land (implementer surfaces, auditor lands per lane discipline):

1. **The wall channel closes (DEFENSE-DERIVED).** `boundary-observables-m-q-j.md` should carry a q²-conditioned statement that the Γ=−1 wall is EM-transparent (Γ_EM = 0) so a hard EM probe does not reflect off the body — the naive "7-OOM body vs 1e-19 m bound" tension is dissolved at the impedance level (matched channel). This is corpus-derived (SYM scaling) and dischargeable now. Surfaced for the auditor.
2. **The coverage-matrix compositeness row** should move from "zero coverage" to **"OPEN-GAP NARROWED: wall channel DEFENSE-DERIVED (Γ_EM=0); moment channel CONSISTENCY (F₂ echo, magnitude blocked); charge channel F₁ ILL-DEFINED pending exterior-tail engine leg (EXPOSURE-CONFIRMED pre-registered as the (b)-outcome)."** — an honest status, not a closure. Surfaced for the auditor.

Claim minting: NO new chord/emergence claim (composite ILL-DEFINED). A DEFENSE-class claim for the wall channel (Γ_EM = 0 ⇒ EM-transparent-to-hard-probe) is mint-eligible as CONSISTENCY-class (it re-reads the corpus-derived SYM-scaling result in the compositeness context) — proposed for the auditor to adjudicate the 6-char id + solidity, NOT minted unilaterally here.
