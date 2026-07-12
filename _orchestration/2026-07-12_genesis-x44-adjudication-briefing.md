# Adjudication briefing — Genesis #655 + X44 #652

**Date:** 2026-07-12 · **After:** A1–A3 stack + L5/mass-sector wire-ins.
**Stance:** HOLD / do-not-merge until Grant rules. This is adjudication
**briefing**, not a merge and not a new engine.

---

## Genesis D1–D4 — PR #655 — bin (ii) A-WEAKENED

### What was asked

Grant contention: electron genesis may need **new-node birth** (N→N+1), not only
a fixed-N pattern. Phase-0 KEEP-BOTH; fire D1–D4 before choosing (A) vs (B).

### What landed

| Gate | Result |
|---|---|
| D1 DOF / \(N^3\) invariant | PASS on crystal / ME / harness (partly install-tautology on fixed mesh) |
| D2 fixed-N persistence | **FAIL** — `E_persist≈0.82` (<0.85), `φ_persist=0`, `rank4_pass=false` |
| D3 (B) necessitated? | **Not entailed** by corpus leaves cited |
| D4 cosmology OOM | SKIPPED until (B) is ruled |

**Frozen meaning:** Fixed-N pattern is **insufficient** for lasting localization
on the declared harness battery. That **weakens (A)**; it does **not** select
(B), does **not** authorize `genesis_v{N}` / graph-growth, and does **not** close
R10 remanence (still open under (A)).

### Physical picture

On today’s anhysteretic engines, a photon-lock / bulk-density probe does not
**keep** a localized state (energy and amplitude persistence fail the P11
floors). That is consistent with “something is missing for lasting electron-like
localization” — but the missing piece could still be **constitutive remanence
(R10)** on fixed N, not necessarily minting nodes. D3 explicitly found no
load-bearing leaf that *derives* Compton-scale N→N+1 as necessary.

### Recommended Grant rulings (pick one)

| Option | Meaning | Next work |
|---|---|---|
| **G1 — KEEP-BOTH continues** | Bank (ii); no (B) yet | Next discriminator: remanence-vs-node-mint fork on a **named** persistence battery (still no `genesis_v{N}`) |
| **G2 — Soft-select (B) explore** | (A) weakened enough to charter a **firewalled** N→N+1 probe | Only with explicit firewall + no fourth-engine sprawl; D4 OOM fence comes back |
| **G3 — Hold for R10 first** | Insist remanence loop is prior in build-order (capability map) | Genesis (B) stays closed until R10 has a real DOF |

**Recommendation:** **G3 or G1**, not G2, until remanence is faced — matches
engine-capability build-order (loop before node-creation) and D3’s “not entailed.”

### Merge

Do **not** merge #655 as “authorization to grow the lattice.” Merge only as
**banked discriminator (ii)** if Grant wants the record on `main`.

---

## X44 Komar source — PR #652 — bin (iii) UNRECONCILED

### What was asked

Grant RULED (c): Picard source \(T_{00}^{\rm src}=T_{00}^{\rm matter}\sqrt{S(A)}\)
(Komar / redshift weight) should reconcile far-field Gauss flux with ADM
\(M_{\rm eff}=M-U_{\rm bind}\).

### What landed

| Quantity | Result |
|---|---|
| \(\eta_{\rm mixed}\) (flux vs \(M_{\rm eff}\)) | **+1.05** at N=24/32/40 (stable — not resolution noise) |
| \(\Delta_{\rm clock}\leftrightarrow U_{\rm bind}\) MATCH | **FAIL** (~93–97% relative mismatch) |
| Gauss ≡ ∫T₀₀^src | PASS (install-tautology) |
| √S→S / 1/S retune | Out of scope; not done |

**Frozen meaning:** Installing √S alone does **not** close the `#86` gap. The
Komar-weighted flux functional and the strain-energy \(U_{\rm bind}\) ledger are
**different functionals**; \(\Delta_{\rm clock}/U_{\rm bind}\sim 0.03$–\(0.07\)
in-band while η stays O(1).

### Physical picture

Far-field “mass from flux” under √S weighting sits near bare M minus a small
clock deficit. The engine’s ADM-style \(M_{\rm eff}\) subtracts a much larger
binding functional built from \(|\nabla\varepsilon|^2\). They will not agree by
construction until the **ledger definition** is homogenized — weighting the
Picard source does not rewrite what \(U_{\rm bind}\) means.

EE analogue: changing how you drive the source network doesn’t make two
different wattmeters agree if they integrate different branches.

### Recommended Grant rulings (pick one)

| Option | Meaning | Next work |
|---|---|---|
| **X1 — Bank unreconciliation** | √S Komar as default source stays; gap is named Class-C open | Doc-only: `#86` gap = functional mismatch; no further retune without new ruling |
| **X2 — Homogenize ledger** | New prereg: redefine \(M_{\rm eff}\) or \(U_{\rm bind}\) to match Δ_clock class | Freeze-first; KEEP-BOTH with legacy ADD |
| **X3 — Revert default to ADD** | Komar was exploratory; ADD remains production | Mode flag stays; default flip |

**Recommendation:** **X1** (bank the negative) or **X2** if Grant wants a
ledger-unification prereg — **not** silent √S→S retune (already forbidden).

### Merge

Do **not** merge #652 as “gravity reconciled.” Merge only as **banked bin (iii)
record** if Grant wants the Komar default + negative on `main`.

---

## How this sits relative to the A1–A3 effort

| Effort | Relation |
|---|---|
| A1–A3 BC kit | Orthogonal — universe port for local solids |
| L5×A1 | Soft-seed pad deconvolution — **worked** |
| Mass-sector×A1 | Hard Mode-I close-pair — **port fail** at primary |
| Genesis #655 | Localization persistence / node-mint fork — **not** solved by BC kit |
| X44 #652 | Gravity ADM/flux ledger — **not** solved by BC kit |

The BC stack does not adjudicate genesis or Komar. Those need the rulings above.
