# Surface-note beside `2026-06-17_bh-shear-echo-forward-prereg.md` — dated 2026-08-05

**This file exists because the document it is about is FROZEN.** `research/2026-06-17_bh-shear-echo-forward-prereg.md`
is a SHA-pinned forward pre-registration (frozen to `main` @ `04bcb4ac`). Per the ratified
vacated-cite pattern, **frozen text gets a dated surface-note, never a rewrite** — that prereg is
**byte-untouched** by this note and by the wave that carries it.

**Class:** scope surface-note. Mints nothing. Changes no solidity. Adjudicates no fork. Repairs
nothing in the frozen file.

---

## What is being surfaced

The frozen prereg's `ave-discrimination-check` at `:73` reads, verbatim:

> **AVE has no such knob:** its reflector is at the *fixed, parameter-free* radius
> `r_sat = 7GM/c²`, **outside** `r_s`, with no log-divergence.

Two things about that sentence have moved since it was frozen, and neither is a defect in the
prereg — a pre-registration is a record of what was staked in advance, and it stays as written.

### 1. It is RHO-A-conditional, and the fork it is conditional on is open

The density profile the delay derivation consumes is an **open fork**. Under the RHO-A branch
(`ρ = ρ₀`, constant) the sentence holds. Under the RHO-B branch (`ρ_eff = ρ₀/S³`, FORK-3(b);
`manuscript/ave-kb/common/wall-taxonomy.md` §9) it does **not**: the AVE delay **is** log-divergent
in the continuum and log-enhanced on the lattice, which makes it **structurally degenerate with the
standard ECO / near-horizon-firewall echo law** — a detected log-form echo delay would not select
AVE on that branch. Receipt: [`2026-08-04_echo-delay-regulated-sum_result.md`](2026-08-04_echo-delay-regulated-sum_result.md)
`FLAG-ECO-COROLLARY`. The collision was surfaced at that lane's *freeze*, not discovered at result
time, and that lane repaired neither document by design.

**Fork status at this note's date:** FORK-3(b)'s **axial** run has landed and returned
`ROOT-NOT-CERTIFIED` with **no physics bin adjudicated**
([`2026-08-04_coldq-axial-rhob_result.md`](2026-08-04_coldq-axial-rhob_result.md)). The fork is
therefore **open**, and neither branch is preferred here.

### 2. The QUANTITY the prereg staked has been superseded on the RHO-A branch

The prereg staked a `~4 ms` delay with a `3–10 ms` band. The current timing authority is
[`2026-08-04_echo-delay-regulated-sum_result.md`](2026-08-04_echo-delay-regulated-sum_result.md),
whose RHO-A configuration is **`DELAY-CERTIFIED`** and **`BIN-DA-CLOSED` adjudicated**. On that
branch the excess round-trip delay is a **fixed pure multiple of `r_sat/c₀`**, and it is **PROMPT,
ACHROMATIC and REGULATOR-FREE**. The old **band was not an uncertainty in the substrate
prediction** — it was the free-flight term of an **undeclared reference plane**, and declaring the
plane removes it. **Read the multiple and its SI values at the authority; they are deliberately not
transcribed here**, because that result doc propagates to no leaf and this note is a pointer, not a
second home for its numbers.

The RHO-B configuration is **`DELAY-NOT-CERTIFIED`** — two gates failed on that lane's own
freeze-time algebra — so **every RHO-B timing figure is a NOT-ADJUDICATED DIAGNOSTIC** and none of
them may be quoted as a prediction.

---

## What is NOT being claimed here

- **The prereg is not retracted.** Its *mechanism* stake — a `Γ_shear = −1` reflector exists,
  therefore echoes are predicted — is untouched by anything above.
- **No branch is selected.** This note does not prefer RHO-A over RHO-B or the reverse. That is
  what "the fork is open" means.
- **No number is refilled.** Nothing here supplies a replacement for the superseded `~4 ms`; the
  authority is cited so a reader gets the current value from the document that gates it under
  `make verify`.
- **Nothing propagates.** No `clm-` / `def-` is minted; no solidity moves; no falsification-ledger
  row is written.

## Companion site

The same discriminator sentence is repeated in the KB at
`manuscript/ave-kb/vol4/falsification/ch11-experimental-bench-falsification/existing-experimental-signatures.md`,
which receives an additive dated scope caveat in the same wave (the pre-existing Rule-12 banner
there is left byte-intact).

**Surfaced, not fixed — two further sibling sites carry the same now-conditional discriminator and
are OUTSIDE the ruled register**, tabulated rather than edited:
`manuscript/ave-kb/vol4/claim-quality.md` (the LIGO GW150914 black-hole-echoes bullet, *"no
log-divergent tunable position"*) and
`manuscript/ave-kb/vol4/falsification/ch11-experimental-bench/existing-signatures.md` (the
2026-06-17 OVERCLAIM-CORRECTION banner, same phrase). Both need the same RHO-A conditionality
qualifier; neither is in this wave's ruled set, and the echo-delay lane's own routing says the
relabel *"only a ruling can authorize."*
