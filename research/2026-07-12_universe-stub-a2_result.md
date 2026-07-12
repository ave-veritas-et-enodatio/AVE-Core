# A2 — Universe stub result

**Prereg (frozen by push):** [`2026-07-12_universe-stub-a2_prereg_FROZEN.md`](2026-07-12_universe-stub-a2_prereg_FROZEN.md) — commit `257c3141` (driver after freeze).
**Carrier:** `NativeCageIMEX` + A1 radiating face (Rule-14).
**Branch:** `analysis/universe-stub-a2` · **HOLD — no merge until Grant.**

---

## Verdict

**Bin (i) STUB-PASSIVE-BIASED**

| Gate | Outcome |
|---|---|
| Closed-box | PASS |
| Bias ON: passivity | PASS (\(H_{\max}/H_0 = 1\)) |
| Bias ON: \(\mathcal{R}=H_{\rm end}/H_0\) | PASS (\(\sim 8\times 10^{-6} \ll 10^{-2}\)) |
| \(\Delta_{\rm bias}\) (primary: \(\|A_{\rm asym,on}-A_{\rm asym,off}\|\)) | PASS (\(\sim 4\times 10^{-3} > 10^{-6}\)) |
| Sabotage (live-pump miswiring of \(\theta=10\theta_\star\), wrong sign) | TRIPS (energy injection) |

---

## Physical / EE picture

Cosmic freeze does not rebuild the horizon inside the local box. It leaves a
**projected preferred-axis tag** — here a slow \(z\)-hat velocity kick at
\(t=0\) with amplitude \(\sin\theta_\star\), \(\theta_\star=\sqrt{\alpha}\)
(Decision-5 scale, frozen literal; no `ALPHA` on the verdict path).

A1 is still the **matched port**: with the tag ON, the launched sech still
leave-takes (\(\mathcal{R}\) tiny, no energy injection). OFF vs ON is visible
as a mid-window asymmetry shift about \(\hat{e}_\Omega\) — the world is not
perfectly isotropic, but the port does not care enough to reflect.

What **must** trip is wiring that tag as a **continuous drive** (treating IC
as a live pump). One-shot oversized IC can still radiate cleanly on a long
window; the Discriminator-7 gate therefore uses the live-pump miswiring, which
explodes \(H\) — the stub is doing its job when that fails loud.

**Does not claim:** live Machian integral, outer mesh, derived \(G\),
\(\Omega_{\rm freeze}\to\alpha/u_0^*\) forward chain, remanence, or emergence.

---

## Numbers (full suite, `fast=False`)

| Quantity | Value |
|---|---|
| \(\theta_\star\) | \(0.08543648040856954\) (frozen) |
| \(\hat{\Omega}\) | \(+1\) |
| \(\mathcal{R}_{\rm off}\) / \(\mathcal{R}_{\rm on}\) | \(\sim 3\times 10^{-6}\) / \(\sim 8\times 10^{-6}\) |
| \(A_{\rm asym,off}\) / \(A_{\rm asym,on}\) | \(\approx -0.250\) / \(\approx -0.245\) |
| \(\Delta_{\rm bias}\) | \(\approx 4.26\times 10^{-3}\) |
| Sabotage \(H_{\max}/H_0\) | \(\gg 1\) (trips) |

Driver: `src/scripts/vol_1_foundations/universe_stub_a2.py`
Tests: `src/tests/test_universe_stub_a2.py` (6 passed)

---

## Cascade

- A1 bin (i) remains the radiating-face gate; A2 adds projected IC without
  breaking it.
- Next thin charter (if Grant wants): **A3** only if needed — still no full
  outer mesh unless a concrete observable demands it.
- Hold siblings: #652 / #655 / #656 — do not merge with this branch.
