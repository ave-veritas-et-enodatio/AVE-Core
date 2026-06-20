# SYNTHESIS — Carrier-sector adjudication arc (2026-06-20)

**Date:** 2026-06-20 · **Lane:** implementer (carrier-sector) · **Class:** **C (synthesis)**
**Status:** RECORDS adjudications; mints NO new `clm-`; cites each verdict's source.

This is the tracked record of the 2026-06-20 carrier-sector adjudication arc, so the
session's work lives in the corpus rather than orchestrator memory alone. The carrier sector =
**charge / spin-½ / Pauli on the Cosserat (2,3) micro-rotation grade** (charter
[`_orchestration/2026-06-20_carrier-sector-charter.md`](../_orchestration/2026-06-20_carrier-sector-charter.md)).

**Every verdict below is grounded (verify-before-cite) against the worktree off `origin/main`
@ `c6950a29` — the citations are the verdicts' SOURCES, to be checked, NOT trusted blind.**

**Discipline applied:** `verify-before-cite` (every file:line grepped) · `consistency-vs-
emergence` (each sub-verdict tagged) · `ave-discrimination-check` (chord-vs-echo per item) ·
`flag-don't-fix` (the one corpus internal-inconsistency surfaced, not resolved) ·
`ave-canonical-source`.

---

## 0 — ANCHOR-CORRECTIONS LEDGER (flag-don't-fix; stale-prose corrections recorded)

Two anchors in the orchestrating prose were stale; corrected here, not silently propagated:

1. **`KAPPA_CHIRAL_ELECTRON` location/symbol.** Prose said `cosserat_field_3d.py:566` /
   `KAPPA_TILDE`. The DEFINITION is at
   [`cosserat_field_3d.py:131`](../src/ave/topological/cosserat_field_3d.py): `KAPPA_CHIRAL_ELECTRON = ALPHA * KAPPA_TILDE_ELECTRON`
   (symbol is `KAPPA_TILDE_ELECTRON`, defined `= 6/5 = 1.2` at `:94`; `:566` is a function
   default *usage*, not the definition). Substance (χ pinned to α) unchanged.

2. **`clm-4vwsjc` registry home.** The `confidence 0.4 / do-not-build` status lives at
   `vol2/claim-quality.md:476,491,496`, NOT in `baryon-asymmetry.md` (which carries only
   `claims: [clm-4vwsjc]`). Pinned per the freeze-handedness note FINDING 2
   ([`research/2026-06-10_freeze-handedness-survey_note.md:87`](2026-06-10_freeze-handedness-survey_note.md)).

---

## 1 — MASS sector = ECHO-final

**Verdict: ECHO-final** (the mass-sector chord-residual closed-negative).

- **Source:** PR #311 merged (`analysis/2026-06-20-gate3-near-saturation`; merge `47bcb8ed`;
  the near-saturation ECHO-FINAL verdict pinned at `681771eb`, strengthened to cross-family +
  full-saturation at `08a8c193`). The fork-B GATE3 near-saturation test closed the mass-sector
  chord-residual as negative.
- **Mechanism vs value (consistency-vs-emergence):** the saturation-driven mass mechanism is
  **real** (~94% saturation-driven; peer-or-ahead of the SM, which has no mechanism for the
  electron mass at all — it is a free Yukawa). The **value** `m_e` is **echo / definitional**
  (the electron mass is a *definitional* anchor in the AVE constant chain, not a substrate-
  selected number) — consistent with the FORM-derived / VALUE-imported meta-finding
  ([[project_form_value_meta_finding]]): `m_e = definitional`.
- **Class:** the mechanism is manifestation/consistency-class; the value is echo. This matches
  the broader pattern (α = echo, G = MIXED, K=2G = GR-imported).

---

## 2 — CHIRALITY = echo / peer-with-SM

**Verdict: ECHO / peer-with-SM** — chirality is imposed-to-match-parity, not substrate-forced.

- **χ imposed-to-match-parity; charge = χ·strain is a relabel.** The chiral coupling is pinned
  to α by fiat: [`cosserat_field_3d.py:131`](../src/ave/topological/cosserat_field_3d.py)
  `KAPPA_CHIRAL_ELECTRON = ALPHA * KAPPA_TILDE_ELECTRON` (with `KAPPA_TILDE_ELECTRON = 6/5` at
  `:94`). The chiral modulus is **set to α**, not derived; charge-as-χ·strain is a relabeling
  of the existing winding/helicity content, not a new mechanism.
- **The noncentrosymmetric-χ reframe is a DUPLICATE, not a new claim.** "The vacuum is a chiral
  non-centrosymmetric medium, EM is its piezo response" is **already canonical Class-B**:
  [`research/2026-06-08_vacuum-as-chiral-piezoelectric.md:8`](2026-06-08_vacuum-as-chiral-piezoelectric.md)
  ("a **Class B consistency-class reframe** … **not** a new substrate-mechanism derivation");
  the noncentrosymmetric `I4₁32` symmetry condition is at `:18`. Re-deriving it in the carrier
  sector adds nothing.
- **Matter-excess IS corpus-established, NOT a new claim.** The matter/antimatter asymmetry is
  already in the corpus at `manuscript/ave-kb/vol2/nuclear-field/ch10-open-problems/baryon-asymmetry.md`
  (claim `clm-4vwsjc`, registered in `manuscript/predictions.yaml:667`; orchestration thread
  `clm-4vwsjc` is the registry id). The carrier-sector work does not introduce matter-excess; it
  cites the existing claim.
- **Class:** echo / peer-with-SM. The SM also imposes parity violation (it is built into the
  electroweak sector by hand); AVE imposing χ to match parity is **peer**, not behind — but it
  is **not a chord** (nothing is forced that the SM lacks).

---

## 3 — BARYOGENESIS = echo / consistency-class

**Verdict: ECHO / consistency-class** — the η formula imports the EW-sphaleron scaffold.

- **η formula = imported EW-sphaleron scaffold.** The corpus η formula
  $\eta = \delta_{CP}\,\alpha_W^4\,C_{sph}/g_*$ lives at
  [`baryon-asymmetry.md:42-46`](../manuscript/ave-kb/vol2/nuclear-field/ch10-open-problems/baryon-asymmetry.md).
  **🚩 FLAG-DON'T-FIX — corpus internal inconsistency (surfaced, NOT resolved):** the leaf
  asserts (`:46`) "**Every factor is derived from AVE lattice constants**", but the adjudication
  ([`research/2026-06-10_freeze-handedness-survey_note.md:50`](2026-06-10_freeze-handedness-survey_note.md))
  classifies the same formula as **consistency-class with an imported electroweak-baryogenesis
  formula** — "the `α_W⁴ C_sph/g_*` scaffold is **SM-imported**" — and the registry pins
  `clm-4vwsjc` at **confidence 0.4, build_status "do not build on, rework needed"**
  (`vol2/claim-quality.md:491,496`). The leaf's "every factor derived" headline and the
  adjudicated "SM-imported scaffold, do-not-build" status are in tension. This is surfaced for
  Grant adjudication; NOT silently reframed.
- **Already-adjudicated 2026-06-10 (FINDING 2).** The freeze-handedness survey already settled
  the magnitude-link as CONTRADICTED-soft / consistency-class / do-not-build
  ([`2026-06-10_freeze-handedness-survey_note.md:47,50,68`](2026-06-10_freeze-handedness-survey_note.md)).
  The carrier-sector work does not re-open this.
- **Walk-back PR #314 OPEN.** Branch `walkback/baryon-asymmetry-finding2` exists (worktree
  `/private/tmp/ave-baryon-walkback`); the walk-back is in flight, not yet merged.
- **Symmetric-standard (consensus-bias guard):** at the **OOM** level the substrate's
  baryogenesis story is **peer-or-ahead-of-SM** (the SM also has no first-principles η — it is a
  free input / requires beyond-SM CP violation). What is **retracted** is the **sub-percent /
  zero-parameter** headline (the "every factor derived" over-claim). Honest tag: **consistency-
  class, OOM-peer, sub-percent-retracted.**

---

## 4 — DYNAMICAL SELECTION = no non-circular gate (representability stands)

**Verdict: no non-circular dynamical-selection gate found.** Representability stands; selection
does not.

- The carrier perimeter is **representability-grade**, not dynamical-forcing-grade:
  - **Charge = forced-integer GIVEN the TKI** (`[Q] ≡ [L]`, Moffatt 1969) — the AVE content is
    the `[Q]≡[L]` identification, **asserted** (conditional on the TKI), not derived
    ([`charge_quantization.py:6`](../src/ave/topological/charge_quantization.py); charter §2.1).
    **C.3 STAYS OPEN:** the direct Beltrami/Chern–Simons helicity integral returns **~18% of
    p·q** at the tested scale and does NOT quantize there
    ([`charge_quantization.py:24`](../src/ave/topological/charge_quantization.py)).
  - **Spin-½ = representable** (#299): the substrate **CAN host** the SU(2) double-cover, but the
    only stand-in is the **analytic axis-angle rotor** `q_body(φ) = (cos(φ/2), …)`
    ([`cosserat_field_3d.py:236,1277,1302`](../src/ave/topological/cosserat_field_3d.py)) — its
    −I is **baked by the half-angle convention** (charter §2.2). The #312 lattice-holonomy
    operator upgrades this to **double-cover-from-connectivity**, but that is still
    *representability* (the substrate *can*), not *selection* (the substrate *must*).
- **Four dynamical-selection mechanisms were considered and none gives a non-circular gate:**
  min-reflection, genesis, stability, mass-cage — each either re-imports the premise or
  re-derives a representability result. (Recorded as the session's negative finding; charter
  §3(a) names dynamical SELECTION as the unbuilt interior item.)
- **Class:** the carrier sector is established at **representability + topological-derivation**
  grade. Dynamical SELECTION is **open**.

---

## 5 — THE CLOSE-CRACK: the `w257o33nz` "structurally excluded" close was WRONG

**The spin-statistics question was prematurely closed; that close is corrected.**

- The `w257o33nz` close attempt canonized the carrier spin-statistics question as "structurally
  EXCLUDED" by re-citing
  [`k4-rotation-group.md:123`](../manuscript/ave-kb/vol1/axioms-and-lattice/ch1-fundamental-axioms/k4-rotation-group.md)
  ("To get an A↔B SWAP … we need to include reflections (full T_d = S₄)") as the **exchange
  discriminator**. **That line is scoped to an A↔B SUBLATTICE swap for the bipartite-spinor
  argument** (`k4-rotation-group.md:121-123`, verified verbatim) — a **category error** for the
  carrier exchange.
- The double-check `wkg5zfrai` returned **all four assumption-checks FALSE**: the electron is a
  real-space `$0_1$` unknot LOOP
  ([`electron-identification.md:22`](../manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/electron-identification.md)),
  and identical-soliton exchange is a **real-space BRAID**, NOT a sublattice permutation. Per FR
  (1968) the exchange is homotopic to a 2π rotation → the `−1` flows from
  `π₁(SO(3)) = ℤ₂ → SU(2)` — **rotations only, no reflection**.
- **This is a 3rd-time regression on the SAME retired discriminator** — a shared-seductive-
  narrative blind-spot (the `:123` reflection-bar keeps getting re-cited across lenses because it
  *sounds* decisive). Per the multi-lane FAILURE-MODE memory: redundancy fails on a shared
  blind-spot; what catches it is an adversarial-by-design lens + reading the operative object (the
  real-space loop, the holonomy code), NOT a second enthusiastic lane.
- **SALIENCE-GUARD (durable):** `k4-rotation-group.md:123` is **RETIRED for the exchange
  question**. It must NOT be re-cited as the spin-statistics-exchange discriminator. The live
  gate is the FR braid (§6).

---

## 6 — SPIN-STATISTICS (this session's FR braid gate) = derived, PEER-ahead

**Verdict: PASS — derived, ahead-of-SM-axiom — chord-vs-peer = PEER-ahead (generic-FR).**

- **Result:** the two-loop exchange holonomy = **−I** from A4-only, reflection-free
  partner-encirclement transport, the SAME `2T` element as the single-particle 2π −I (the FR
  homotopy). Full detail + guard table:
  [`research/2026-06-20_fr-braid-spin-statistics_result.md`](2026-06-20_fr-braid-spin-statistics_result.md)
  (operator `src/ave/topological/fr_braid_exchange.py`, 14 tests + 19 #312 = 33).
- **chord-vs-peer (honest ceiling):** **PEER-ahead, NOT an AVE-distinct chord.** The non-A4
  control (a generic-axis 2π loop) ALSO reaches −I, so the double-cover → −1 chain is generic to
  any soliton/double-cover framework. The pre-registered AVE-distinct prong (A4-lattice-forced,
  fails-on-non-A4) **did not fire**.
- **Charter §5 BAR answered:** "was a reflection needed?" → **NO** (A4-only, reflection-free).
  The single-particle 2π result **transfers** to the two-loop exchange. The `:123` reflection-bar
  is corrected as a category error (§5).

---

## 7 — NET: carrier-sector status + where the chord-hunt goes next

**Carrier sector = representability-grade + spin-statistics-derived (PEER).**

| Sub-sector | Verdict | Class |
|---|---|---|
| Mass | ECHO-final (#311) | mechanism real (~94% saturation), value echo/`m_e` definitional |
| Chirality | echo / peer-with-SM | χ imposed-to-match-parity; charge=χ·strain a relabel; piezo-reframe = duplicate Class-B |
| Baryogenesis | echo / consistency-class | η = imported EW-sphaleron scaffold; OOM-peer; sub-percent-retracted; PR #314 open |
| Charge | representability (forced-given-TKI) | `[Q]≡[L]` asserted; C.3 ~18%, OPEN |
| Spin-½ | representability + topological-derivation | #299 representable, #312 from-connectivity; FM-on-K4 |
| Spin-statistics | **derived, PEER-ahead (FR braid, this session)** | A4-only reflection-free; generic-FR, not a chord |
| Dynamical selection | **OPEN — no non-circular gate** | the unbuilt interior (charter §3(a)) |

- **The FORM-derived / VALUE-imported signature extends here** ([[project_form_value_meta_finding]]):
  the carrier sector **derives FORMS** (the double-cover, the exchange −1, charge-as-winding) but
  **imports VALUES** (χ = α, `m_e` definitional, η from EW scaffold) — a 5th instance of the same
  meta-pattern (after α=echo, G=MIXED, m_e=definitional, K=2G=GR-imported, parity).
- **Where the chord-hunt goes next (if it continues).** Spin-statistics is now closed at
  **PEER-grade** (generic-FR), so it is **not** the AVE-distinct chord. The live AVE-distinct
  candidates are the **standing FORWARD PREDICTIONS** — falsifiable, beyond-SM numbers the
  substrate forces — NOT the representability/derivation results:
  1. the **optical-activity sign-flip + achiral-null** (the chiral substrate predicts a parity-
     odd selection rule; achiral control → null);
  2. the **`(q·ℓ_node)⁴` dispersion** (a lattice-discreteness signature absent in the continuum);
  3. the **GW-echo** (a substrate-stiffness signature);
  4. the **birefringence coefficient ~10⁶× QED** — the AVE/QED ratio
     `δn_AVE/δn_QED = 1/(4 a_EH α³)` as a field-independent structural quantity
     ([`research/2026-06-04_birefringence-coefficient-prereg.md:30`](2026-06-04_birefringence-coefficient-prereg.md)).
- **Dynamical SELECTION** (charter §3(a)) is the remaining carrier-sector interior. If a
  non-circular selection gate can be built (the substrate MUST select the antisymmetric/spin-½
  sector, not merely admit it), that — not the FR derivation — would be the carrier-sector chord
  candidate. None found this session.

