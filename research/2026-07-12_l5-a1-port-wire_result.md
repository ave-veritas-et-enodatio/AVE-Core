# L5 × A1 port wire-in — RESULT

**Prereg (frozen by push):** [`2026-07-12_l5-a1-port-wire_prereg_FROZEN.md`](2026-07-12_l5-a1-port-wire_prereg_FROZEN.md) — `9cf436dc`.
**Driver:** `src/scripts/vol_1_foundations/l5_a1_port_wire.py`
**Branch:** `analysis/l5-a1-port-wire` · **HOLD — no merge until Grant.**

Preceded by HOLD-stack review (handoff): `.agents/handoffs/2026-07-12_hold-stack-review_a1-a3.md`.

---

## Verdict

**Bin (i) PORT-DECONVOLVED**

| Gate | Outcome |
|---|---|
| A1 passivity | PASS |
| \(\Delta\mathcal{R}\) (sponge \(\sum V^2\) vs A1 Newmark \(H\)) | PASS (\(\approx 0.10\)) |
| \(\Delta\mathcal{R}_{\sum V^2}\) same-proxy | PASS (\(\approx 0.41\)) |
| Retires 2026-06-07 L5 JSON? | **No** — parallel wire-in only |

---

## Physical / EE picture

L5 asks “how leaky is this localized seed?” On the original MasterEquation arm the
answer mixes **confinement** with **sponge pad kill** (`V *= damping` each step).

Same rest-scale sech (\(A=0.48\)) on the A1 `NativeCageIMEX` face:

- **Wave energy \(H\)** leave-takes cleanly: \(\mathcal{R}_H \approx 2.5\times 10^{-4}\),
  passive.
- **\(\sum V^2\)** still retains ~50% (DC residual — same honesty as A1).
- **Sponge** \(\sum V^2\) residual \(\approx 10\%\) — the pad **eats more of the
  field**, including content that A1 would leave as non-radiating offset.

So the sponge lane is **not** a passive matched universe port: it is a lossy
absorber that changes the Q/leak ledger. A1 deconvolves “radiated away” from
“pad swallowed.” This does **not** claim a new alpha / L5 emergence number.

---

## Numbers (full, `fast=False`, \(N=16\), 500 steps)

| Arm | \(\mathcal{R}\) | \(\mathcal{R}_{\sum V^2}\) | passive |
|---|---:|---:|---|
| sponge (ME FDTD) | \(0.100\) (\(\equiv\sum V^2\)) | \(0.100\) | yes |
| a1_port (IMEX) | \(2.53\times 10^{-4}\) (Newmark \(H\)) | \(0.507\) | yes |

---

## Cascade

- A1–A3 stack used on a **real** local question (L5 Q/leak confound).
- Next candidates if Grant wants: mass-sector two-body, apparatus-floor wall.
- Hold siblings unchanged; do not merge.
