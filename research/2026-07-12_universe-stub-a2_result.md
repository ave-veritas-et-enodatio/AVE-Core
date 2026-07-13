# A2 — Universe stub result

**Prereg (frozen by push):** [`2026-07-12_universe-stub-a2_prereg_FROZEN.md`](2026-07-12_universe-stub-a2_prereg_FROZEN.md) — commit `257c3141` (driver after freeze).
**Carrier:** `NativeCageIMEX` + A1 radiating face (Rule-14).
**Branch:** `analysis/universe-stub-a2` · **HOLD — no merge until Grant.**

---

## Verdict

**Frozen bin (ii) STUB-WEAK; post-freeze live-pump axis TRIPS (KEEP-BOTH)**

> **R4 correction (2026-07-12, post-adversarial-review).** The frozen prereg's
> sabotage is the ONE-SHOT wrong-sign \(10\theta_\star\) "applied once at \(t=0\)"
> (prereg lines 92–94, §Sabotage). On this carrier that one-shot plant is
> **SILENT** (it never injects — \(H_{\max}/H_0=1.0\) — and leave-takes cleanly
> through the A1 port on the same window the ON arm passes). The frozen bin table
> reads "sabotage silent → bin (ii) STUB-WEAK". The originally-shipped verdict
> "bin (i)" was selected against a **live-pump** sabotage substituted post-freeze.
> Per the KEEP-BOTH discriminator pattern (#612/x34): the FROZEN-AXIS verdict is
> re-reported as **bin (ii) STUB-WEAK**, and the live-pump TRIP is preserved as an
> explicitly-labeled **POST-FREEZE NEW AXIS**. See the Deviation ledger.

| Gate | Outcome (FROZEN axis) |
|---|---|
| Closed-box (frozen lossless-limit leg, reused from A1) | PASS (\(\text{rel\_drift}=-5.98\times10^{-10}<10^{-6}\)) |
| Bias ON: passivity | PASS (\(H_{\max}/H_0 = 1\)) |
| Bias ON: \(\mathcal{R}=H_{\rm end}/H_0\) | PASS (\(8.18\times 10^{-6} \ll 10^{-2}\)) |
| \(\Delta_{\rm bias}\) (primary: \(\|A_{\rm asym,on}-A_{\rm asym,off}\|\)) | PASS (\(4.26\times 10^{-3} > 10^{-6}\)) |
| **Sabotage (FROZEN one-shot \(10\theta_\star\), wrong sign, once at \(t=0\))** | **SILENT** — \(H_{\max}/H_0=1.0\), \(\mathcal{R}=8.74\times10^{-6}<10^{-2}\) → **bin (ii)** |

**POST-FREEZE NEW AXIS (KEEP-BOTH; non-frozen):**

| Axis | Outcome |
|---|---|
| Sabotage as a **live pump** (\(10\theta_\star\) wrong-sign re-applied each step) | **TRIPS** — \(H_{\max}/H_0=7.6\times10^{94}\) (injects loud) |

Physical argument for the frozen plant's toothlessness: a one-shot projected IC —
even oversized/wrong-sign — is **kinematically identical** to the legitimate bias
(both are ICs that radiate through the matched port and never inject). The
miswiring that IS dangerous is treating the cosmic projection as a **continuous
drive**; only that live-pump axis trips. That axis was minted after the freeze, so
it is reported alongside — it does **not** overturn the frozen bin (ii).

---

## Physical / EE picture

Cosmic freeze does not rebuild the horizon inside the local box. It leaves a
**projected preferred-axis tag** — here a slow \(z\)-hat velocity kick at
\(t=0\) with amplitude \(\sin\theta_\star\), \(\theta_\star\) an IC-scale
**engineering literal** near \(\sqrt{\alpha}\) (Decision-5 scale; frozen literal;
no `ALPHA` on the verdict path). **R5 label correction (2026-07-12):**
\(\theta_\star=0.08543648\ldots\) gives \(\theta_\star^2 = 1/136.998\); it is
**not** \(\sqrt{\alpha}\) (canonical \(\sqrt{\alpha}=0.08542454\Rightarrow
1/137.036\), \(\sqrt{\alpha_{\rm cold}}=0.08542445\) — off by \(1.4\times10^{-4}\)
relative). The "\(\sqrt{\alpha}\)" label at freeze time was erroneous; the value is
FROZEN, only the label is corrected (substrate-first-for-numbers: tagged
engineering-choice).

A1 is still the **matched port**: with the tag ON, the launched sech still
leave-takes (\(\mathcal{R}\) tiny, no energy injection). OFF vs ON is visible
as a mid-window asymmetry shift about \(\hat{e}_\Omega\) — the world is not
perfectly isotropic, but the port does not care enough to reflect.

The FROZEN sabotage is a one-shot oversized/wrong-sign IC (\(\theta=10\theta_\star\),
applied once at \(t=0\)). On this carrier it **radiates cleanly on the clearing
window and never injects** — it is kinematically identical to the legitimate bias
— so it is **SILENT**, which the frozen bin table reads as bin (ii) STUB-WEAK.
The miswiring that actually trips is treating the tag as a **continuous drive**
(a live pump), which explodes \(H\); that is a **post-freeze new axis** (KEEP-BOTH),
reported alongside, not the frozen plant.

**Does not claim:** live Machian integral, outer mesh, derived \(G\),
\(\Omega_{\rm freeze}\to\alpha/u_0^*\) forward chain, remanence, or emergence.

---

## Numbers (full suite, `fast=False`)

| Quantity | Value |
|---|---|
| \(\theta_\star\) (frozen engineering literal near \(\sqrt{\alpha}\); \(\theta_\star^2=1/136.998\), NOT \(\sqrt{\alpha}\)) | \(0.08543648040856954\) |
| \(\hat{\Omega}\) | \(+1\) |
| \(\mathcal{R}_{\rm off}\) / \(\mathcal{R}_{\rm on}\) | \(8.21\times 10^{-6}\) / \(8.18\times 10^{-6}\) |
| \(A_{\rm asym,off}\) / \(A_{\rm asym,on}\) (see R6 grid-artifact note) | \(-0.2496\) / \(-0.2454\) |
| \(\Delta_{\rm bias}\) | \(4.26\times 10^{-3}\) |
| Sabotage \(H_{\max}/H_0\) — FROZEN one-shot | \(1.0\) (**silent**, never injects) |
| Sabotage \(\mathcal{R}\) — FROZEN one-shot | \(8.74\times10^{-6}\) (\(<10^{-2}\), silent) |
| Sabotage \(H_{\max}/H_0\) — POST-FREEZE live-pump (new axis) | \(7.6\times10^{94}\) (trips) |

**R6 grid-artifact note (2026-07-12).** \(A_{\rm asym}\) rides an off-center
even-\(N\) mesh baseline (\(A_{\rm asym}\approx-0.25\) with bias OFF, \(\sim 59\times\)
the \(4.3\times10^{-3}\) signal): the mesh center is `N//2`, off the true
\((N-1)/2\) center for even \(N\). This baseline **common-modes out** of the
OFF−ON delta (identical grid on both arms), so \(\Delta_{\rm bias}\) stands; but the
observable's **absolute magnitude is artifact-dominated**. Future cross-carrier /
cross-\(N\) comparisons must center the mesh or use the OFF−ON delta only.

Driver: `src/scripts/vol_1_foundations/universe_stub_a2.py`
Tests: `src/tests/test_universe_stub_a2.py` (7 passed)

---

## Deviation ledger (dated; frozen prereg byte-untouched)

**2026-07-12 (post-adversarial-review) — sabotage swap / THE BIN CHANGE (R4).**
The frozen prereg's sabotage is the ONE-SHOT wrong-sign \(10\theta_\star\)
("applied once at \(t=0\)"; "Silent green sabotage = fail of the stub gate").
A **live-pump** plant (bias re-applied every step) was substituted post-freeze and
made the sabotage trip, which selected bin (i). The frozen one-shot plant is
**SILENT** on this carrier (\(H_{\max}/H_0=1.0\); \(\mathcal{R}=8.74\times10^{-6}\)
on the ON-arm clearing window). Under the frozen bin table (bin (ii): "sabotage
silent"), the FROZEN-AXIS verdict is **bin (ii) STUB-WEAK**. REPAIR (KEEP-BOTH,
#612/x34 precedent): re-report the frozen-axis bin as (ii); keep the live-pump
TRIP as an explicitly-labeled **POST-FREEZE NEW AXIS**. Frozen prereg
byte-untouched.

**2026-07-12 (post-adversarial-review) — \(\theta_\star\) label (R5).** The freeze
labeled \(\theta_\star=\sqrt{\alpha}\). It is not: \(\theta_\star=0.08543648\ldots\)
gives \(\theta_\star^2=1/136.998\), off by \(1.4\times10^{-4}\) relative from
\(\sqrt{\alpha}=0.08542454\) (and \(\sqrt{\alpha_{\rm cold}}=0.08542445\)). REPAIR
(value FROZEN, label corrected everywhere): \(\theta_\star\) is an IC-scale
**engineering literal** near \(\sqrt{\alpha}\); the "\(\sqrt{\alpha}\)" label was
erroneous (substrate-first-for-numbers ⇒ tagged engineering-choice). The 1e-12
test pin is kept (it pins the frozen literal, now honestly labeled).

**2026-07-12 (post-adversarial-review) — \(A_{\rm asym}\) grid artifact (R6).**
Disclosure only (no re-run): the \(\langle V\cdot\hat z\rangle\) asymmetry rides an
off-center even-\(N\) mesh baseline (\(\approx-0.25\), \(\sim59\times\) the signal).
It common-modes out of the OFF−ON delta, so \(\Delta_{\rm bias}\) stands; the
absolute magnitude is artifact-dominated. Future cross-carrier/cross-\(N\) work must
center the mesh or use the delta only.

**2026-07-12 — merge-forward reconciliation (A1 R1).** A1's `run_closed_box` was
split into a FROZEN lossless-limit leg + operating canary. A2 reuses the FROZEN
lossless-limit leg (`run_closed_box_lossless_limit`) as its closed-box control —
consistent with the prereg ("Closed-box control still PASS"; the tighter frozen
criterion still passes).

---

## Cascade

- A1 bin (i) remains the radiating-face gate; A2 adds projected IC without
  breaking it.
- Next thin charter (if Grant wants): **A3** only if needed — still no full
  outer mesh unless a concrete observable demands it.
- Hold siblings: #652 / #655 / #656 — do not merge with this branch.
