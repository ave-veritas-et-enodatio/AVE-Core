# Mass-sector × A1 port — RESULT

**Prereg (frozen by push):** [`2026-07-12_mass-sector-a1-port_prereg_FROZEN.md`](2026-07-12_mass-sector-a1-port_prereg_FROZEN.md) — `b0c0153b`.
**Driver:** `src/scripts/vol_1_foundations/mass_sector_a1_port.py`
**Branch:** `analysis/mass-sector-a1-port` · **HOLD — no merge until Grant.**

---

## Verdict

**Bin (iii) FORCE-PORT-FAIL** at the frozen primary \(d_0=7\), Mode-I amp \(0.85\).

| Gate | Outcome |
|---|---|
| A1 passivity at \(d_0=7\) | **FAIL** (\(H_{\max}/H_0 \gg 1\), energy blow-up) |
| Sponge classify (\(d_0=7\)) | NULL / BELOW-FLOOR (radiation floor ~2.3 cells) |
| Flag \(d_0=11\) A1 passivity | PASS (non-enforcing) |
| Flag \(d_0=11\) wire-in bin | (i) FORCE-DECONVOLVED via lower floor / bin flip — **flag only** |

Does **not** rewrite the 2026-06-23 mass-sector claim.

---

## Physical / EE picture

The mass-sector driver asks whether two dilatation breathers attract in a
**phase-independent** way (gravity-like) or a phase-dependent NLS way. On
sponge ME it already knows radiation into the pad contaminates centroids, so it
shortens the force window against an O0 jitter floor.

Drop-in A1 at the **same** Mode-I operating point (\(A=0.85\), \(d_0=7\)) fails
before that question can be re-asked: the two breathers **overlap** enough that
`NativeCageIMEX`’s nonlinear update **runs away** (even closed-box two-body at
\(d_0=7\) blows; single blob at \(0.85\) is fine; two-body becomes passive again
by \(d_0\ge 11\)).

So the honest wire-in result is not “A1 cleaned the force readout.” It is:

> **A1 is not yet a drop-in for the mass-sector close-pair Mode-I amp.** The
> sponge lane can sit in a regime the Newmark cage port cannot integrate
> stably when cores overlap. Wider separation restores passivity and starts to
> deconvolve floors — but that is a **different** kinematic point than the
> driver’s primary \(d_0=7\).

EE analogue: a matched port rated for one tone, then driven by two close high-amp
resonators whose beat / overlap saturates the nonlinear element — the amplifier
rails before you can measure coupling.

---

## Cascade

- L5×A1 = soft-seed leave-taking deconvolution (**worked**).
- Mass-sector×A1 = hard Mode-I close-pair (**port fail** at primary) — capacity
  gap, not a silent retune to make (i).
- Next: genesis #655 / X44 #652 adjudication (Grant step 3).
