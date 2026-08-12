# Adjudication brief — DoF vs PORT (the longitudinal bulk scalar) — 2026-08-11

**Target:** `research/2026-08-11_dof-vs-port-ontology_walk-record.md` (claim ledger §1) +
`research/drivers/dof_port_ontology_check.py`. **Branch:** `analysis/dof-vs-port-ontology`.
**Not** PR #955 — this walk *challenges* #955's §4.1, so it is deliberately on its own branch.

**What this is.** A chat walk that reached an **axiom**. Adjudicate rows **M1–M5** and **G1–G3** of
the ledger. **C** rows need re-verification only; **D** rows need routing, not judgment.

**Posture: DEFAULT-TO-REFUTED** on every **M** row. A lane claim stands only if the reviewer can
state, in corpus words at file:line, why it does. Per-row: `CONFIRMED / DOWNGRADED / REFUTED`.

**★ The load-bearing row is M1.** M2 follows from it, §7's whole blast radius hangs off it, and
`g_* = 85.75` hangs off M2. **If M1 falls, stop and report — do not rescue it, and do not build a
better version of it.**

---

## The frozen criterion for M1 (quoted so no paraphrase becomes the pivot)

> **M1: "The longitudinal bulk scalar (dilatation) is a PORT, not a DoF. `θ = ∇·u` is built from the
> gradients of the three translational coordinates: no independent initial condition, no conjugate
> momentum. It is an irreducible channel with its own modulus (`K`), not a state variable."**

**M1 is REFUTED if any of these is found:**

1. **A seventh independent storage slot** in the operative per-node state vector — a scalar/volumetric
   coordinate carrying its **own initial condition and conjugate momentum**, anywhere in
   `src/ave/`. *(Driver family C tests exactly this and its family-D leg proves the detector reports
   7 when handed a synthetic 7-slot node — so a green C is a real negative, not a vacuous one.)*
2. **A canonical leaf that derives** an independent volumetric DoF from the K4/srs kinematics —
   as opposed to *asserting* one (C3 asserts; assertion is not derivation).
3. **A demonstration that `θ` can be excited independently of `u`** on the discrete lattice — i.e.
   that the common mode is a wire and not a mode of three wires.

**M1 is CONFIRMED only if** the reviewer positively establishes 1–3 all fail **and** finds no corpus
site that treats dilatation as a state. **"The driver is green" is not sufficient** — the driver
shows the *engine* does not contradict M1; the engine could be under-modelling. Say so if that is the
only support found, and return `DOWNGRADED` rather than `CONFIRMED`.

---

## Lenses

**L1 — M1 head-on (run first).** Fire the three refutation conditions above. Read the operative state
vector yourself; do not accept the driver's word. ⚑ Consensus-bias check: the state-vs-port
distinction is **standard in both circuit theory and continuum mechanics** — if you are inclined to
call it pedantic, ask whether you would accept "add the common mode as a fourth wire" in an ordinary
network problem.

**L2 — M2 and the `g_*` blast radius.** If M2 holds, `g_* = n³/N_K4 = 343/4 = 85.75`
(`vol3/claim-quality.md`:504–514) loses its basis, because `n` is a coefficient (D3: it slides with
`K/G`) and the cube of a coefficient is not a mode count. **Verify D3 independently** — do not re-run
the lane's driver as your second engine. Then state plainly whether the `g_*` claim survives, and if
it does, on what. **Do not repair it.**

**L3 — M3, the pseudoscalar.** Is it a formation parameter (C9: mirror image gives *"identical
physics"*) or does it carry dynamics somewhere? ⚑ **Mandatory fence:** C8 forbids reading numbers off
the biquaternion — *"never mint it as a substrate primitive or read a new number off it."* **A verdict
that derives a DoF count from the algebra violates the fence**; if the algebra is the only available
route, return `BLOCKED-ON-FENCE`.

**L4 — M4/M5 and Grant's G1/G2.** Is the four-category ladder a real distinction or re-labelling? For
M5: is *"DoF count is a PHASE property, port structure is a REGIME property"* actually falsifiable, or
unfalsifiable-by-construction? **Name a phase transition where the DoF count is claimed to change
(genesis/crystallization) and check whether the corpus states before/after counts.** G1 (the axiom's
silence on the scalar channel's port status) is **Grant's to rule, not yours** — verify the silence is
real and stop.

**L5 — G3 and the localization to `ρ*`.** The walk concedes the framing defect and then argues the
concession does not rescue this coefficient, on C6's authority. **Test both halves.** Is C6 as
decisive as quoted, at HEAD? And is the localization right — is `ρ* = k_a/k_s ≈ 9.77` genuinely the
*only* unfixed input downstream, or are there others the walk missed? ⚑ **Do not attempt to derive
`ρ*`** — out of scope, and it is a live open question.

**L6 — TURN THE WALK'S OWN CHARGE ON THE WALK.** The lane committed the exact category error it
alleges (R2), one turn before alleging it. **Re-read §2 and §4 for further instances**: any place the
lane counts algebraic grades, irreps, or ports as if they were state variables. R1 and R2 were
self-caught; assume there are others that were not.

**L7 — QUOTE + CITE GATE.** Every **C** row re-read at HEAD, byte-exact — this lane shipped a
fabricated quote in PR #955 and had **no quote gate**, so treat its quotations as unverified until you
have re-read them. Confirm **D1** (the dead cite) and **D2** (the four-line equivocation) rather than
taking them on the lane's word.

---

## Fences

- **Verify-not-derive.** Refute or confirm. Do not repair the walk, do not amend an axiom, do not
  touch `g_*`, do not derive `ρ*`.
- **No edits** to any KB leaf, axiom file, register, ruling, or manuscript file.
- **Do not enter the `Γ`-sign fork** (`backreaction.md`:194, wall-taxonomy §10, PR #869).
- **Frozen criteria travel verbatim** — M1 is quoted in full above for exactly that reason.
- **Stop-and-ask.** Two-attempt cap; a clean STUCK-POINT report beats a spun-out verdict.
- **`[DO-NOT-MERGE]`. Only Grant merges.**

## Outcome grammar (frozen)

Per row: `CONFIRMED` / `DOWNGRADED`(name the surviving narrower claim) / `REFUTED`(state the killing
fact). Then **one** disposition for the walk, from exactly this set:

| verdict | meaning |
|---|---|
| `ONTOLOGY-SUSTAINED` | M1 CONFIRMED ⇒ route the port/state relabel + the `g_*` re-adjudication as **proposals** to Grant |
| `ONTOLOGY-NARROWED` | M1 DOWNGRADED — **name the surviving scope** (e.g. holds for the engine, not for the axiom) |
| `ONTOLOGY-DEAD` | M1 REFUTED ⇒ the 7 stands as a DoF count, and **Axiom 1's "six" is the thing that needs amendment** |
| `BLOCKED-ON-AXIOM` | the question cannot be settled without Grant ruling G1 → back to Grant |

**`ONTOLOGY-DEAD` is a clean, useful outcome.** It would mean Grant's 3+3+1 is right as stated, the
mode-counting leaf is sound, and the defect is in Axiom 1 — a *more* consequential result than the
walk's own claim, and the reviewer should feel free to land there.

**Independently of the verdict, D1/D2/D3 stand as routable defects** — a dead cite, a four-line
equivocation, and a receipted non-invariance. Those do not depend on M1.

---

**How to launch.** Not auto-dispatched — Grant launches (his call on model + effort).
`ave-adversarial-pr-review` fits: `args = {pr: <this PR>, context: "walk record §1 ledger; adjudicate
M1-M5 + G1-G3; default-to-refuted; M1 is load-bearing", lenses: [L1…L7]}`. **L1 and L6 are worth the
most compute; L7 is mechanical but non-optional given this lane's quote history.**
