# L5 × A1 port wire-in — RESULT

**Prereg (frozen by push):** [`2026-07-12_l5-a1-port-wire_prereg_FROZEN.md`](2026-07-12_l5-a1-port-wire_prereg_FROZEN.md) — `9cf436dc`.
**Driver:** `src/scripts/vol_1_foundations/l5_a1_port_wire.py`
**Branch:** `analysis/l5-a1-port-wire` · **HOLD — no merge until Grant.**

Preceded by HOLD-stack review (handoff): `.agents/handoffs/2026-07-12_hold-stack-review_a1-a3.md`.

---

## Verdict

**Bin (i) PORT-DECONVOLVED** — via `AND(same-proxy ΣV², any-other)` (R9)

| Gate | Outcome |
|---|---|
| A1 passivity | PASS |
| **Same-proxy** \(\Delta\mathcal{R}_{\sum V^2}\) (both \(\sum V^2\)) — **required** | PASS (\(0.407 > 10^{-4}\)) |
| Any-other: cross-proxy \(\Delta\mathcal{R}\) (sponge \(\sum V^2\) vs A1 Newmark \(H\)) | PASS (\(0.100 > 10^{-4}\)) |
| Adjudicator | `same_proxy_ok AND any_other_ok` = **True** → bin (i) |
| Retires 2026-06-07 L5 JSON? | **No** — parallel wire-in only |

> **R9 note (2026-07-12).** The adjudicator now uses `AND(same-proxy ΣV², any-other)`
> as its own comment (`l5_a1_port_wire.py` adjudicate) already specified, not the
> shipped OR. The cross-proxy \(\Delta\mathcal{R}\) compares the sponge's \(\sum V^2\)
> energy against A1's Newmark \(H\) — a diff that can be non-zero from the
> energy-definition mismatch alone; requiring the same-proxy \(\Delta\mathcal{R}_{\sum V^2}\)
> ensures a PASS is not a pure definition mismatch. **This run passes either way**
> (same-proxy \(0.407\), cross-proxy \(0.100\), both \(\gg 10^{-4}\)).

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

## Deviation ledger (dated; frozen prereg byte-untouched)

**2026-07-12 (post-adversarial-review) — OR→AND adjudicator (R9).** The adjudicator's
`delta_ok` used OR across (`dR`, `dR_v2`, `dtau`) while its own comment required the
same-proxy comparison so the bin is not a pure definition mismatch. REPAIR:
implemented `AND(same-proxy ΣV², any-other)`. This run passes either way (same-proxy
\(0.407\), cross-proxy \(0.100\)); the test suite adds a discriminating case (cross-proxy
above floor, same-proxy below floor → correctly bin (ii)). FROZEN prereg byte-untouched.

**2026-07-12 — upstream propagation (A2 R4 / A3 R7-R8).** Parent A2 is now **frozen
bin (ii) STUB-WEAK** (post-freeze live-pump axis trips, KEEP-BOTH); A3 is bin (i)
via the FROZEN shell-only mask + null-differenced criterion. L5×A1 stacks on the A3
tip **code** (the working A1 face), independent of A2/A3 bin values.

---

## Cascade

- A1–A3 stack (A1 bin i · A2 frozen bin ii · A3 bin i) used on a **real** local
  question (L5 Q/leak confound).
- Next candidates if Grant wants: mass-sector two-body, apparatus-floor wall.
- Hold siblings unchanged; do not merge.
