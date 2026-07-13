# F6 depletion TIER-1 charter — global two-reservoir ODE ledger (handoff brief)

**Date:** 2026-07-13 · **Grant GO (Q4):** 2026-07-13 · **Class:** charter (draft the discriminator
BEFORE any driver) — modeled on the #662 remanence-charter pattern
(`research/2026-07-12_remanence-r10-fixed-n_CHARTER.md`: charter doc + frozen bins +
fireable-vs-entailed + fool-modes). **Charter first; PR DO-NOT-MERGE; driver only after charter
review.**

**Sector header (mandatory).** MODE: global bookkeeping ODE ledger, NOT a field solve — **no
`a(t)` evolver exists in the engine** (`solve_backreaction` is static-elliptic; the engine has
local first-law only, no global state object). REGIME: the top-stage cascade port
(Machian-horizon termination), at/near the cosmic operating point. PHASE-STATE: a held static
store (ρ_latent) draining one-way into the T2 bath across the off-line↔on-line boundary. SECTOR:
this is the **A-class (continuous drainage)** behavior of the **local top port** — a static-sector
store transferring into a thermal reservoir; it is **not** the A1 dilatation-mass sector and not a
Cosserat-winding claim.

---

## 0 · One-paragraph charter

F6 is the **irreversible ε→T2 depletion** primitive — the DE-tracks-matter chord, the one
ΛCDM-distinct thing AVE could carry and the make-or-break the corpus has never built
(`manuscript/ave-kb/vol3/cosmology/ch04-generative-cosmology/dark-energy-latent-heat-definition.md:139,144`).
**Tier 1 is a GLOBAL TWO-RESERVOIR ODE LEDGER** (ρ_latent ↔ T2 bath): does a one-way,
Ax3-legal, conservation-respecting transfer whose rate is slaved to lower-stage occupancy produce
a DE component that **tracks matter** in form — and is that form distinguishable from a bare
cosmological constant in the ledger's own observable? **No `a(t)` field solve** — tier 1 books
reservoir exchange, nothing more. **TIER-2** (one X40-class discrete-click demo) is a **separate
follow-on gated on this charter's review**.

---

## 1 · Mission and scope

Draft the F6 **tier-1** charter: the two-reservoir ledger, its frozen bins, its fireable-vs-entailed
split, its fool-modes, and its mandatory Ax3 carve. The charter is the deliverable; the driver
comes after review. The charter must make explicit that tier-1 is a **ledger, not a field solve**
(the engine has no `a(t)`; `solve_backreaction` is static-elliptic; there is no global ΔE_cryst
state object today).

---

## 2 · The walked architecture (ruling-grade inputs — Grant-walked 2026-07-13)

Record these four elements as ruling-grade inputs (the walked map):

| Element | Identity |
|---|---|
| **Source** | **ρ_latent** — the static sector's held store (the latent heat of ongoing crystallization). |
| **Destination** | **the T2 bath** — the huge thermal reservoir; irreversibility comes from its mode-count, not from a nonlinearity. |
| **Transducer / locus** | **the mass envelope** — where the transfer is physically effected. |
| **Door** | **the off-line ↔ on-line boundary** — the gate the transfer passes through. |

---

## 3 · Cascade address

**F6 = the A-class (continuous drainage) behavior of the LOCAL top port** — the Machian-horizon
termination. Canon already prices that port as a **distributed transmission-line input impedance
at the Hubble-horizon termination** (Machian G row, `manuscript/ave-kb/common/translation-tables/translation-circuit.md`
Machian-G ↔ TL-input-impedance row, ~:126). **F6 is the claim that the Re(Z) at that termination
is nonzero and one-way** — the port has a real, irreversible drainage channel, not a purely
reactive/lossless one.

- **The FRW `3H·ρ_latent` rate reads as the matched termination's absorption rate** — the
  top-stage loaded Q ~ O(1) (matched), which is exactly where the cascade's far end already sits.
- **DE-TRACKS-MATTER = the top port's A-rate slaved to the lower stages' B-occupancy** — how much
  clicked-in matter loads the envelope sets the top port's drainage rate. **That inter-stage
  slaving IS the chord**, and it is **precisely what no canon site derives** (the Machian integral
  is spatial, produces G, and moves no energy; no inter-stage energy coupling exists in canon).

---

## 4 · Hard constraints (each gets a named detector in the charter)

- **`bias ≠ release` detector.** The R-A operating-point **bias must be untouched by the release
  mechanism** — the drainage cannot move the bias point. Detector: assert the operating-point bias
  is invariant under the release channel being ON vs OFF.
- **`electron-no-drain` detector.** The port **must not drain its own transducer** — electron
  stability. Detector: the electron's intrinsic store is not depleted by the top-port A-channel
  (Q→∞ preserved; no self-drain).
- **`muon-fence` detector.** The muon **loads T2 but does not decay by that channel** — loading
  the bath is not the muon's decay route. Detector: T2 loading by the muon is separable from and
  does not drive the muon's actual decay channel.

---

## 5 · Licensed mechanisms only (the diode/rectifier class is DEAD)

**Licensed (Ax3-legal, use one of these three):**

1. **Entropic mode-count transfer** — arrow-of-time class: energy-conserving one-way TRANSFER into
   the huge T2 reservoir (dS>0), **NOT a friction loss, so Ax3-COMPLIANT**
   (`dark-energy-latent-heat-definition.md:84-86`). Irreversibility from reservoir mode-count, not
   nonlinearity.
2. **X40-class discrete topological minting** — one-way **at the click**, energy-conserving,
   consistency-class (`research/2026-07-10_x40-ring-closure-transient_result.md`: Λ banked whole,
   drift ~2×10⁻¹⁶, minted only at the discrete ring-completion event).
3. **The skew-Hermitian circulator** — orthogonal field-space rotation, conserves + transfers, but
   **magnitude imposed** (`src/ave/core/cross_sector_coupling.py:137-141`; the one-way 3-port loop,
   PR #321).

**The DIODE / RECTIFIER CLASS IS DEAD — cite all four deaths:**

1. **The Ax4 kernel is even-in-A and cannot rectify** — the one RUN test was NULL
   (`research/2026-06-08_rrad-l-rectification_result.md`: `S(A)=√(1−A²)` instantaneous, even,
   memoryless; identical 2nd-order response to symmetric and asymmetric drive).
2. **Any true rectifying loop is Level-2 memristive = dissipative**
   (`manuscript/ave-kb/common/substrate-hysteresis-index.md:24-25`: rectification/latching/
   path-memory requires Level-2 dynamics — the smooth kernel does not implement it; the loop
   encloses `∮S dr` = dissipated energy). So "lossless + rectifier" is a contradiction in the
   corpus's own loop taxonomy.
3. **The diode threshold V_f is FREE, not forced** (`research/2026-07-08_p4-forward-voltage-threshold_RESULT.md`:
   no canonical scale forces a forward-voltage dead zone; kernel analytic at origin, dispersion
   gapless).
4. **Chirality-ratchet-as-arrow is REFUTED — do not reopen** (`dark-energy-latent-heat-definition.md:89-90,99-100`:
   "No future reader should re-introduce the chirality-ratchet as the cosmological arrow"). An
   ideal-diode framing risks re-opening this retracted slot.

**The v4 detonation (do not repeat it).** Any **continuous trilinear-potential transfer is the v4
detonation** — `H = κ̃∫gV[w·∇×ω]` is **linear in each field ⇒ INDEFINITE Hamiltonian, unbounded
below ⇒ the discrete dynamics PUMP / DETONATE** (`src/ave/core/crystal_graft_v4.py:160-166`, verbatim
comment). The **v5 spec** is bounded, norm-preserving, **source-depletion-not-reaction**, no
indefinite-Hamiltonian pump (`research/2026-06-10_bemf-feedback-smoke_result.md` §8). Tier-1's
ledger must not smuggle a trilinear pump back in through the ODE.

---

## 6 · Ax3 reconciliation (mandatory carve)

*(This carve governs the whole discriminator. The transfer must be entropic / event-gated,
**never dissipative**.)*

**(i) The Ax3 constraint.** Sub-yield the substrate is **lossless / reactive**. A legitimate F6
transfer is therefore **not free to be a friction loss**: it must be either (a) an
**entropic one-way transfer** made irreversible by the T2 reservoir's mode-count (dS>0, energy
conserved, `dark-energy-latent-heat-definition.md:84-86`), or (b) an **event-gated discrete
minting** (one-way at a click, X40-class). Both are Ax3-COMPLIANT precisely because neither
imports sub-yield dissipation.

**(ii) The amorphous-retirement precedent (address it explicitly).** The **plastic / STZ sub-yield
dissipation route FAILED Ax3 and stays RETIRED**
(`manuscript/ave-kb/common/substrate-native-terminology.md:62`: "thixotropic STZ / liquefies /
plastic" as a load-bearing mechanism "imports dissipation, which would radiate, contradicting the
result"). F6's drainage must **not** reconstruct that retired leak under a cosmological name. Any
tier-1 ledger term that is a continuous sub-yield loss is the retired Ax3 leak re-imported.

**(iii) ★NEW FOOL-MODE — the re-imported Ax3 leak.** A **LEDGER-CONSISTENT PASS achieved via a
continuous sub-yield dissipative transfer** = the retired leak re-imported. It must be classed
**IMPOSED-LEAK, not F6-CANDIDATE** — a fool-mode the charter names up front, alongside the
FORM-DEGENERATE bin below.

---

## 7 · Scope (CC-HONEST, binding)

- **Existence + FORM of DE-tracks-matter ONLY.** Tier-1 asks whether a matter-slaved, Ax3-legal,
  conservation-respecting drainage produces a DE component whose **form** tracks matter — nothing
  about its magnitude.
- **NO magnitude matching.** The **naive ρ_latent value is ~120 OOM over ρ_Λ**; the **10^122 trap
  is rejected canon** — the naive zero-point/mode-count magnitude path "still gives a too-large
  naive answer" and DE is reframed as latent heat, not zero-point energy
  (`manuscript/ave-kb/vol3/cosmology/ch05-dark-sector/cosmological-constant-closure.md:58-62`; the
  10^122 framing is the leaf's headline at `:8`). **The charter must NOT attempt to match the
  ρ_latent magnitude to ρ_Λ.**
- **ρ_latent parameterization = Grant-GO'd 2026-07-13, INPUT-ONLY.** It enters at **clm-s4n33u,
  solidity 0.45, build_status "input-only, don't build deeper"**
  (`manuscript/ave-kb/vol3/cosmology/ch04-generative-cosmology/dark-energy-latent-heat-definition.md:122`).
  Use it as an input parameter; do not deepen the ρ_latent / ΔE_cryst derivation in this charter.

---

## 8 · Frozen bins (tier-1) + deliverables / sequencing

**Fireable-vs-entailed (the charter drafts the full table; minimum content):**

| Content | Class |
|---|---|
| Reservoir conservation (ρ_latent + T2 bath total invariant to machine precision) | Partly **ENTAILED** (ledger construction) — do not bank as the chord |
| The top-port A-rate being **slaved to lower-stage B-occupancy** | **FIREABLE** (this is the chord) |
| DE-component **form** vs a bare cosmological constant in the ledger observable | **FIREABLE** |
| Ablation: slaving OFF → DE form collapses to constant | **FIREABLE ablation** |

**Frozen bins (minimum — freeze PRE-RUN):**

- **(i) LEDGER-CONSISTENT.** The two-reservoir ledger conserves, the transfer is Ax3-legal
  (entropic/event-gated), and the DE component's **form tracks matter** distinguishably from a
  constant — the DE-tracks-matter FORM exists.
- **(ii) LEDGER-VIOLATES-CONSERVATION.** The ledger fails to conserve (ρ_latent + T2 total drifts),
  or the only transfer that produces tracking is dissipative — **fail** (and if dissipative, it is
  the §6(iii) IMPOSED-LEAK fool-mode, not F6).
- **(iii) FORM-DEGENERATE.** The ledger runs and conserves, but **DE-tracks-matter is
  indistinguishable from a cosmological constant in the ledger's observable** — the form is
  degenerate; F6's chord does not resolve at tier-1 (a real negative on the FORM question, not an
  instrument gap).

**Deliverables / sequencing:**

1. **This charter** (picture · walked architecture · cascade address · constraints · licensed
   mechanisms · Ax3 carve · scope · bins) — reviewed before any driver.
2. **FROZEN prereg** (the frozen bins + tolerances) — sibling file, **freeze-by-push BEFORE any
   driver**.
3. **Tier-1 driver** (the two-reservoir ODE ledger) — only after charter + prereg review.
4. **TIER-2** (one X40-class discrete-click demo) — separate follow-on, gated on this charter's
   review.

**Rails:** freeze-by-push; sabotage plants act on evolved ledger observables; adversarial review
via a `scriptPath` wrapper that inlines ARGS and calls
`workflow({scriptPath: '.claude/workflows/ave-adversarial-pr-review.js'}, ARGS)` (the named-workflow
args path silently drops args); **DO-NOT-MERGE** — only Grant merges.

---

## 9 · References (grep-verified anchors — 2026-07-13, at this PR's base d0037d8f)

- `research/2026-07-12_remanence-r10-fixed-n_CHARTER.md` — the #662 charter pattern this brief is
  modeled on (charter + frozen bins + fireable-vs-entailed + fool-modes + Ax3 carve).
- `manuscript/ave-kb/vol3/cosmology/ch04-generative-cosmology/dark-energy-latent-heat-definition.md:84-86`
  (Ax3-legal one-way T2 transfer, dS>0), `:89-90,99-100` (chirality-ratchet-as-arrow REFUTED,
  do-not-reopen), `:122` (clm-s4n33u ρ_latent solidity 0.45, input-only), `:139,144,146` (F6 =
  the one ΛCDM-distinct chord, UNBUILT; photon_deplete=True detonates).
- `manuscript/ave-kb/common/translation-tables/translation-circuit.md` Machian-G row (~:126) —
  Machian G = distributed TL input impedance at Hubble-horizon termination.
- `src/ave/core/crystal_graft_v4.py:160-166` — trilinear = INDEFINITE Hamiltonian, unbounded
  below, PUMP/DETONATE (the v4 detonation to avoid).
- `research/2026-06-10_bemf-feedback-smoke_result.md` §8 — v5 spec: bounded, norm-preserving,
  source-depletion-not-reaction.
- `research/2026-06-08_rrad-l-rectification_result.md` — kernel even-in-A cannot rectify (run NULL).
- `manuscript/ave-kb/common/substrate-hysteresis-index.md:24-25` — rectification/latching = Level-2
  memristive = dissipative.
- `research/2026-07-08_p4-forward-voltage-threshold_RESULT.md` — V_f FREE (no forced dead zone).
- `manuscript/ave-kb/common/substrate-native-terminology.md:62` — plastic/STZ sub-yield dissipation
  FAILs Ax3 (amorphous-retirement precedent).
- `research/2026-07-10_x40-ring-closure-transient_result.md` — X40 discrete minting (one-way at
  click, Λ banked whole). `src/ave/core/cross_sector_coupling.py:137-141` — skew-Hermitian 3-port
  circulator (magnitude imposed).
- `manuscript/ave-kb/vol3/cosmology/ch05-dark-sector/cosmological-constant-closure.md:8,58-62` —
  10^122 framing; naive-magnitude path rejected (latent-heat reframe, not zero-point).
