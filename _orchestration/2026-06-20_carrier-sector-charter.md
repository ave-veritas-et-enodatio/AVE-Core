# Carrier-Sector Charter — charge / spin-½ / Pauli on the Cosserat (2,3) grade

**Founded:** 2026-06-20 · **Lane:** implementer (carrier-sector) · **Status:** chartered

This charter scopes the carrier sector — the substrate physics of **charge,
spin-½, and Pauli/spin-statistics** — and fixes the build perimeter, the open
interior, the roadmap, and the chord-vs-echo stake. It is the founding document
for the spin-statistics chord-hunt.

---

## 1 — SCOPE

The carrier sector lives on the **Cosserat (2,3) micro-rotation grade** — the
substrate of the periodic table (charge and intrinsic spin). Concretely:

- Charge / spin-½ / Pauli ride the **T2 ω micro-rotation grade** (the Cosserat
  couple-stress / intrinsic-spin DOF), NOT the A1 dilatation-mass grade.
- **A1 ⊥ T2** is load-bearing and Grant-ratified. The mass "3" (A1 dilatation,
  the Heaviside-excised longitudinal compression scalar) and the charge "3"
  (the Cosserat (2,3) micro-rotation winding) are **two distinct, orthogonal
  objects** — `manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md:20`
  (verified verbatim 2026-06-20). The hard rule: **never wire the winding into
  the A1 mass phasor `(V_inc, V_ref)`** — `V_ref` is a read-only projection of
  the same scalar `V`, not an independent DOF; doing so self-inflicts the
  genesis-24 / crystal `w_pol = 0` double-count.

The electron is the unknot dilatation-mass **carrying** the (2,3) winding — two
objects, not one.

---

## 2 — PERIMETER (built, representability-level)

What is already on `origin/main` at charter time, and at what scope:

### 2.1 Charge = forced-integer GIVEN the TKI [Q]≡[L] posit (#300)
- **File:** `src/ave/topological/charge_quantization.py`.
- **Scope:** charge is a forced integer **conditional on** the Topological-Knot
  Identification `[Q] ≡ [L]` (charge ≡ winding/linking number, Moffatt 1969).
  The AVE content is the `[Q]≡[L]` identification, which is **asserted**
  (conditional on the TKI), not derived from the substrate.
- **Open caveat C.3:** the DIRECT Chern–Simons/Beltrami helicity integral
  (`_hopf_density`) returns **~18% of p·q** at the tested scale (measured 1.08
  vs p·q = 6 at R≈7) — its magnitude does **not** quantize at this scale. C.3
  is ADDRESSED-BY-FORMULA, not closed-by-two-integrals-agreeing; it **STAYS
  OPEN** (`charge_quantization.py:21-24,350`, verified 2026-06-20).

### 2.2 Spin-½ = representable (#299)
- **File:** `src/ave/topological/cosserat_field_3d.py`, method
  `probe_spin_doublecover_holonomy` (built by PR #299).
- **Scope:** the substrate **CAN host** the SU(2) double-cover — the lift returns
  −I at 2π and +I at 4π, distinct from a trivial-vector baseline. This is
  **representability** (the substrate *can* host), **NOT** dynamical selection
  (NOT that it *must*). Per the result doc and the FM-derivation leaf, the gate
  corroborates the group-theory of the FM-on-K4 mechanism; it does **not** on its
  own force spin-½.
- **The substrate-blindness flag (the reason this charter's first build exists):**
  the only double-cover stand-in in `probe_spin_doublecover_holonomy` is OP_B —
  the analytic axis-angle SU(2) rotor `q_body = [cos(φ/2), axis·sin(φ/2)]`
  (`cosserat_field_3d.py:1353`). Its −I at 2π is **baked by the half-angle
  convention**: the lattice never enters. The representability is real, but the
  −I is a property of the rotor, not of the connectivity. The
  lattice-holonomy build (this charter's Part 2, `k4_lattice_holonomy.py`)
  is the substrate-native UPGRADE: the double-cover emerging from LATTICE
  CONNECTIVITY (a product of per-link A4 port-permutation rotations), not from
  an analytic rotor.

---

## 3 — INTERIOR (unbuilt)

What remains, and is explicitly NOT claimed:

- **(a) Dynamical SELECTION.** The substrate must *host* spin-½ as a dynamically
  selected state (it MUST, not merely CAN). Representability (#299, and the
  connectivity upgrade) does not establish selection.
- **(b) Pauli / spin-statistics EXCHANGE-antisymmetry.** The exchange-antisymmetry
  of two identical carriers under particle exchange. This is **distinct** from the
  A1 hard-sphere no-overlap wall (the mass-sector containment): exchange
  antisymmetry is a phase/sign on the wavefunction under braid, not a geometric
  no-overlap constraint.

---

## 4 — ROADMAP

In dependency order:

1. **K4 lattice-holonomy operator (this charter's Part 2) — PREREQUISITE.**
   The double-cover-from-connectivity machinery. Built first because every
   downstream gate composes frame-transport from real lattice links.
2. **Spin-statistics-exchange gate — FIRST physics gate** (pending the
   prerequisite + a **braid-reframe**). The exchange MUST be a real-space braid
   transporting two windings past each other under Axiom 4 (A4 dynamics), **NOT**
   an A↔B sublattice swap. An A↔B swap cannot be done by A4 (the rotation group
   T = A4) without the **reflections the chiral I4₁32 net lacks**:
   `manuscript/ave-kb/vol1/axioms-and-lattice/ch1-fundamental-axioms/k4-rotation-group.md:123`
   (verified verbatim 2026-06-20) — "To get an A↔B SWAP … we need to include
   reflections (full T_d = S₄) or some other physical mechanism." The chiral net
   has only the rotation subgroup; an exchange test built as a sublattice swap is
   testing the wrong object.
3. **Dynamical-selection gate** (interior (a)).
4. **Charge C.3 closure** (the direct Beltrami quantization at scale).

---

## 5 — CHORD-VS-ECHO STAKE (imposed-vs-derived lens)

The discriminating question for the whole sector:

- **The SM IMPOSES spin-statistics** via QFT axioms — Lorentz invariance,
  microcausality (local commutativity), and positivity of energy (the
  spin-statistics theorem assumes these). It does **NOT derive** antisymmetry
  from a microscopic substrate; antisymmetry is an axiom-level input.
- **A substrate FORCING antisymmetry from its OWN chiral rotation-only (T = A4)
  topology** — with no externally-imposed Lorentz/microcausality axiom — would be
  a forced structure the SM lacks. **That is a CHORD.**
- **Re-deriving the GENERIC double-cover → antisymmetry connection** (which any
  double-cover framework has, including standard SU(2) QM) is **peer-level, NOT an
  advance.** The double-cover → −I → fermionic-sign chain is shared by every
  spin-½ formalism; reproducing it is reproducing the textbook.

### THE BAR
- **Forcing, not representability.** The substrate must *select* the antisymmetric
  sector, not merely *admit* it.
- **Substrate-native, not stencil.** The mechanism must read the K4 connect-map
  (A4 port-permutations), not a Cartesian-FD rotation on a parity-mask (Ckpt-2).
- **Discriminator = "was a reflection needed?"** If the −1 (the antisymmetric
  sign) is forced by **A4-only** (the pure chiral rotation group) → **CHORD**:
  the substrate's own chirality forces what the SM imposes. If it needs a
  **T_d reflection** (an element of T_d \ T, which the chiral I4₁32 net lacks)
  → **ECHO**: the structure was imported, not forced by the chiral substrate.

The lattice-holonomy build (Part 2) does **not** land a prong of THE BAR above — the
bar is defined over the **two-particle exchange −1** (spin-statistics), and the build
establishes only the **single-particle 2π-rotation −1**: its −I is produced by a
**C3 vertex rotation cubed** — a pure A4 rotation, no reflection. That is
representability of the *rotation* double-cover (π₁(SO(3))=ℤ₂ from connectivity), the
PREREQUISITE — **not** the exchange sign. What it does establish is narrower and only
suggestive: *for the rotation sign, no reflection was needed.* Whether that result
**transfers to the exchange sign** is precisely the open discriminator the next gate
must settle — the exchange gate extends the same "was a reflection needed?" question
to the two-carrier braid, where the A↔B swap (unlike a 2π rotation) may demand a
T_d reflection the chiral net lacks.

---

## 6 — HONEST SCOPE OF THE PART-2 BUILD

The K4 lattice-holonomy operator is the **PREREQUISITE** — the lattice-holonomy
machinery plus the double-cover-from-connectivity (a substrate-native upgrade of
#299's analytic representability). It does **NOT** test exchange / spin-statistics
(the next gate). It does **NOT** establish dynamical selection. **Class-C** (no
over-claim): "the double-cover emerges from connectivity," NOT "spin-statistics
derived."

---

## Anchor ledger (verify-before-cite, all verified 2026-06-20 against the worktree
off `origin/main` @ `d83f77c3`)

| Claim | Anchor | Status |
|---|---|---|
| A1 ⊥ T2; never wire winding into A1 phasor | `master-equation.md:20` | verified verbatim |
| A↔B swap needs reflections (chiral net lacks them) | `k4-rotation-group.md:123` | verified verbatim — ⚠️ **RETIRED for the EXCHANGE question** (see §7 closure-status); scoped to a SUBLATTICE swap, NOT the carrier braid |
| K4 → A4 → 2T ⊂ SU(2); 2π→−I, 4π→+I | `k4-rotation-group.md:125-136` (§6) | verified |
| A4 = 12 even permutations of {p0..p3}; the 12 rotations | `k4-rotation-group.md:61-114` (§3-§4) | verified |
| Tetrahedral ports p0..p3 | `k4-rotation-group.md:17`; `k4_tlm.py:80-86` | verified |
| FM-on-K4 mechanism; #299 corroborates representability | `finkelstein-misner-spin-half-derivation.md` §2-§3 | verified |
| Charge forced-integer given TKI [Q]≡[L]; C.3 open ~18% | `charge_quantization.py:21-24,46,350` | verified |
| #299 spin representability, OP_B analytic rotor | `cosserat_field_3d.py:1277,1353` | verified |

---

## 7 — CLOSURE STATUS (2026-06-20, Rule-12 ADDITION — §1-§6 above PRESERVED unedited)

> **This section RECORDS the carrier-sector adjudication outcomes reached 2026-06-20. The
> roadmap (§4), the BAR (§5), and the Part-2 scope (§6) above are PRESERVED as the founding
> record. Full grounding + the FLAG-DON'T-FIX surfacing live in the synthesis doc
> [`research/2026-06-20_carrier-sector-adjudication-synthesis.md`](../research/2026-06-20_carrier-sector-adjudication-synthesis.md)
> and the FR result [`research/2026-06-20_fr-braid-spin-statistics_result.md`](../research/2026-06-20_fr-braid-spin-statistics_result.md).**

### 7.1 — 🚨 SALIENCE-GUARD (durable — read before any future exchange work)

**`k4-rotation-group.md:123` is RETIRED for the spin-statistics-EXCHANGE question.** That line
("To get an A↔B SWAP … we need to include reflections (full T_d = S₄)") is scoped to a
**SUBLATTICE A↔B swap for the bipartite-spinor argument** (`k4-rotation-group.md:121-123`) — a
**category error** for the carrier exchange. The carrier is a real-space `$0_1$` unknot LOOP
(`electron-identification.md:22`); identical-soliton exchange is a **real-space BRAID**, NOT a
sublattice permutation. **It must NOT be re-cited as the exchange discriminator.** This is the
**3rd-time regression** on this same line (the `w257o33nz` "structurally excluded" close was the
latest); the SALIENCE-GUARD exists because the line keeps *sounding* decisive across lenses.
The §4-§5 roadmap text above that frames the exchange via "the A↔B swap … may demand a T_d
reflection" (lines ~96-102, ~144) is **SUPERSEDED by this section** for the exchange question —
preserved per Rule 12 as the founding framing, but the live discriminator is the FR braid below.

### 7.2 — Spin-statistics-exchange gate = CLOSED (FR braid, PASS / PEER-ahead)

The FR two-loop braid gate (`src/ave/topological/fr_braid_exchange.py`, 14 tests) settles the
charter §5 BAR question "was a reflection needed?":

- **VERDICT: PASS** — the exchange σ holonomy = **−I** from **A4-only, reflection-free**
  partner-encirclement transport, the SAME `2T` element as the single-particle 2π −I (the FR
  homotopy "exchange ≅ 2π rotation of one soliton"). **No reflection needed.**
- **chord-vs-peer: PEER-ahead (generic-FR), NOT an AVE-distinct chord.** The non-A4 control
  also reaches −I → the double-cover → −1 chain is generic to any soliton/double-cover
  framework. The §5 BAR's chord prong (A4-lattice-forced) **did not fire**.
- All six anti-tautology guards hold; FR consistency holds. Detail: the FR result doc.

### 7.3 — The other carrier sub-sectors (verdicts; sources in the synthesis doc)

| Sub-sector | Verdict |
|---|---|
| Mass | ECHO-final (#311; mechanism ~94% saturation real, value echo / `m_e` definitional) |
| Chirality | echo / peer-with-SM (χ imposed-to-match-parity; charge=χ·strain a relabel; piezo-reframe = duplicate Class-B) |
| Baryogenesis | echo / consistency-class (η = imported EW-sphaleron scaffold; OOM-peer; sub-percent-retracted; PR #314 open). **FLAG:** `baryon-asymmetry.md:46` "every factor derived" vs adjudicated SM-imported/do-not-build — surfaced for Grant, NOT resolved. |
| Charge | representability (forced-given-TKI `[Q]≡[L]` asserted; C.3 ~18% OPEN) |
| Spin-½ | representability + topological-derivation (#299 representable, #312 from-connectivity) |
| Spin-statistics | **derived, PEER-ahead** (FR braid §7.2) |
| **Dynamical SELECTION** | **OPEN — no non-circular gate found** (4 mechanisms fail; charter §3(a) interior) |

### 7.4 — NET + next

Carrier sector = **representability-grade + spin-statistics-derived (PEER)**. The
FORM-derived / VALUE-imported signature extends here (5th instance). Spin-statistics being
**generic-FR PEER**, the chord-hunt re-points at the standing **FORWARD PREDICTIONS**
(optical-activity sign-flip + achiral-null; `(q·ℓ_node)⁴` dispersion; GW-echo; birefringence
~10⁶× QED) and at the **dynamical-SELECTION** gate (§3(a)) — the one remaining carrier-sector
interior whose closure would be the genuine chord candidate. None found this session.
