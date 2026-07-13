# A3 — Universe return path result

**Prereg (frozen by push):** [`2026-07-12_universe-return-a3_prereg_FROZEN.md`](2026-07-12_universe-return-a3_prereg_FROZEN.md) — commit `cfd2e690` (driver after freeze).
**Carrier:** `NativeCageIMEX` + A1 radiating face (Rule-14).
**Branch:** `analysis/universe-return-a3` · **HOLD — no merge until Grant.**

---

## Verdict

**Bin (i) RETURN-RECEIVED** (via the FROZEN shell-only mask + null-differenced criterion)

| Gate (enforcing = FROZEN shell-only) | Outcome |
|---|---|
| Leave-take (A1) | PASS (passive, \(\mathcal{R}=2.1\times10^{-4}<10^{-2}\)) |
| **Shell-ONLY return** \(\Delta E_{\rm int}\) (prereg-pure mask) | PASS (\(1.191\)) |
| **Null-differenced discrimination** \(\Delta_{\rm shell}-\Delta_{\rm null}\) (enforcing) | PASS (\(1.190 \gg 10^{-6}\)) |
| Interior-pump sabotage | TRIPS (labeled non-exterior, `source_is_exterior=False`) |

Diagnostic leg (KEEP-BOTH; non-enforcing): shell ∪ interior-face drive reads
\(\Delta E_{\rm int}=1.38\) — larger because it drives **inside** the Rule-10
interior ΔE mask (R7).

---

## Physical / EE picture

A1 is a matched **load** for outgoing strain. After the pulse clears, A3 opens the
same port as a **generator port**: the PSD absorber is muted for the return
window, and a slow exterior drive (\(A_{\rm ret}=0.01\), \(\omega_{\rm ret}=0.3\))
is applied **on the port shell only** (the frozen prereg configuration). Interior
energy rises (\(\Delta E_{\rm int}=1.191\)) while a null arm (mute, no drive) does
not carry a comparable rise. Wiring that drive through the **bulk interior** is
caught as sabotage (not exterior).

**R7 correction (2026-07-12).** The original ship drove `shell ∪ outermost
interior layer` and justified it by claiming a pure shell-only kick "stays
unreadable" on periodic cage IMEX. That justification is **false**: the
prereg-pure shell-only drive still fires (\(\Delta E_{\rm int}=1.191\) vs null
\(1.4\times10^{-3}\)) without driving inside the Rule-10 interior ΔE mask. The
shell-only mask is now the **enforcing** configuration; the shell+face variant is
a labeled diagnostic leg (reads \(1.38\), inflated because it drives inside the
measurement region).

Fast \(\omega=4\) was tried first and **cancelled** over the window (net
\(\Delta E\le 0\)) — honesty: the frozen tone must be slow enough that the
local solid actually hears a same-sign push. That is an EE bandwidth point, not
a bin dodge.

**Does not claim:** live Machian mesh, CMB identity of the packet, remanence,
or emergence of \(G\).

---

## Numbers (full suite, `fast=False`)

| Quantity | Value |
|---|---|
| \(\omega_{\rm ret}\) | \(0.3\) (frozen in driver) |
| \(A_{\rm ret}\) | \(0.01\) |
| Leave-take \(\mathcal{R}\) | \(2.1\times10^{-4}\;(\ll 10^{-2})\) |
| \(\Delta E_{\rm int,shell}\) (**FROZEN shell-only, enforcing**) | \(1.191\) |
| \(\Delta E_{\rm int}\) (shell+face, **diagnostic only**) | \(1.38\) |
| \(\Delta E_{\rm int,null}\) (no drive) | \(1.43\times 10^{-3}\) |
| **\(\Delta_{\rm shell}-\Delta_{\rm null}\)** (enforcing discrimination) | \(1.190\) |
| Sabotage \(\Delta E_{\rm int}\) | non-exterior (`source_is_exterior=False`), trips |

**R8 null-floor note (2026-07-12).** The no-drive null reads \(\Delta E_{\rm int}
= 1.43\times10^{-3}\) — a mode-switch slosh that sits **~3 orders of magnitude
above** the frozen \(10^{-6}\) absolute floor (and its per-arm `received` flag is
unreliable: it flips sign with grid/window). The frozen absolute floors therefore
do **not** encode the no-drive systematic. The enforcing criterion is the
**null-differenced** \(\Delta_{\rm shell}-\Delta_{\rm null}\) (huge here); the
per-arm `received` gate is demoted to diagnostic. A future weak-packet claim in the
\(10^{-6}\!-\!10^{-3}\) band would be **systematic, not reception**.

Driver: `src/scripts/vol_1_foundations/universe_return_a3.py`
Tests: `src/tests/test_universe_return_a3.py` (9 passed)

---

## Deviation ledger (dated; frozen prereg byte-untouched)

**2026-07-12 (post-adversarial-review) — shell-only violation (R7).** The frozen
prereg says the drive is "exterior — applied on the shell only". The shipped mask
was `shell ∪ outermost-interior-face`, driving **inside** the Rule-10 interior ΔE
measurement mask; its docstring justification ("a shell-only kick stays
unreadable") is false. REPAIR: the prereg-pure **shell-only** mask is now the
enforcing configuration (\(\Delta E_{\rm int}=1.191\) vs null \(1.4\times10^{-3}\);
bin holds), and the shell+face variant is retained as a labeled diagnostic leg
(reads \(1.38\)). Headline numbers updated to the pure-mask values.

**2026-07-12 (post-adversarial-review) — vacuous null floor (R8).** The null arm
(zero kick) reads `received=True` at \(\Delta E=1.43\times10^{-3}\) (~3 OOM above
the \(10^{-6}\) floor). REPAIR: the **null-differenced** comparison
(\(\Delta_{\rm shell}-\Delta_{\rm null}\), here \(1.190\)) is now the enforcing
criterion; the per-arm `received` gate is demoted to diagnostic. Noted: the frozen
absolute floors sit ~3 OOM below the no-drive systematic and do not encode the
noise scale.

**2026-07-12 — sibling-bin propagation (A2 R4).** A2 is now **frozen bin (ii)
STUB-WEAK** (one-shot sabotage silent) with a post-freeze live-pump axis that
trips (KEEP-BOTH). A3 stacks on A2's tip **code** (the working face + IC helper),
not on A2's bin value; bin (ii) still means the face stays green with bias ON, so
the A3 construction is unaffected.

---

## Cascade

- Local↔universe thin stack: **A1 out (bin i) · A2 IC tag (frozen bin ii
  STUB-WEAK; post-freeze live-pump axis trips) · A3 return (bin i)** — all HOLD.
- Still no full outer mesh unless a concrete observable demands it.
- Hold siblings: #652 / #655 / #656 / #657.
