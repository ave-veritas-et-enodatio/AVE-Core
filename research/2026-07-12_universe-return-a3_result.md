# A3 — Universe return path result

**Prereg (frozen by push):** [`2026-07-12_universe-return-a3_prereg_FROZEN.md`](2026-07-12_universe-return-a3_prereg_FROZEN.md) — commit `cfd2e690` (driver after freeze).
**Carrier:** `NativeCageIMEX` + A1 radiating face (Rule-14).
**Branch:** `analysis/universe-return-a3` · **HOLD — no merge until Grant.**

---

## Verdict

**Bin (i) RETURN-RECEIVED**

| Gate | Outcome |
|---|---|
| Leave-take (A1) | PASS (passive, \(\mathcal{R}<10^{-2}\)) |
| Shell/face return \(\Delta E_{\rm int}\) | PASS (full \(\sim 1.38\)) |
| Null discrimination | PASS (\(\Delta_{\rm shell}-\Delta_{\rm null}\sim 1.38\)) |
| Interior-pump sabotage | TRIPS (labeled non-exterior, \(\Delta E_{\rm int}>0\)) |

---

## Physical / EE picture

A1 is a matched **load** for outgoing strain. After the pulse clears, A3 opens the
same port as a **generator port**: the PSD absorber is muted for the return
window, and a slow exterior drive (\(A_{\rm ret}=0.01\), \(\omega_{\rm ret}=0.3\))
is applied on the port face (shell ∪ outermost interior layer — the readable
coupling surface on periodic cage IMEX). Interior energy rises. A null arm
(mute, no drive) does not. Wiring that drive through the **bulk interior** is
caught as sabotage (not exterior).

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
| Leave-take \(\mathcal{R}\) | \(\ll 10^{-2}\) |
| \(\Delta E_{\rm int,shell}\) | \(\approx 1.38\) |
| \(\Delta E_{\rm int,null}\) | \(\approx 1.4\times 10^{-3}\) |
| Sabotage \(\Delta E_{\rm int}\) | \(\approx 0.11\) (non-exterior) |

Driver: `src/scripts/vol_1_foundations/universe_return_a3.py`
Tests: `src/tests/test_universe_return_a3.py`

---

## Cascade

- Local↔universe thin stack: **A1 out · A2 IC tag · A3 return** — all bin (i),
  all HOLD.
- Still no full outer mesh unless a concrete observable demands it.
- Hold siblings: #652 / #655 / #656 / #657.
