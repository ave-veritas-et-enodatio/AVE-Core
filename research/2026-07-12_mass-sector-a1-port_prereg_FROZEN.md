# Mass-sector two-body × A1 port — FROZEN prereg

**Freeze discipline.** Pushed BEFORE any mass-sector+A1 driver (ave-prereg v1.7
Step 3.11). **HOLD / no merge** until Grant.

**Authorization.** Grant 2026-07-12: proceed with (2) next physics use then (3)
genesis/X44 adjudication. After L5×A1 deconvolution (#659), wire A1 into
`mass_sector_two_body_scattering.py` — the driver already documents that once
field radiates into PML, fixed top-K centroids migrate and fake attraction; it
compensates with a tight pre-radiation window. A1 replaces that workaround with
certified leave-taking so the force window can be honest.

**Class.** Instrumentation application on a validate-on-known gravity readout —
**not** a new gravity chord, not outer mesh. Rule-14 parallel
`NativeCageIMEX` + A1 `port_sigma` arm. Does **not** silently rewrite the
2026-06-23 mass-sector result; reports deconvolution / extended-window comparison.

α-CLEAN (gravity / dilatation sector).

---

## Sector header

- **SECTOR** = two Mode-I dilatation breathers, head-on, force = phase-independent
  attraction (gravity-like) vs phase-dependent NLS.
- **Hurt today:** sponge/PML radiation contaminates centroids; driver shortens
  the force window to beat the pad.
- **A1 role:** passive matched leave-taking so radiated content exits without
  pad-kill centroid migration; compare O0 floor + O1 net_dsep in/out phase.
- **Refuse EMERGENCE / new G derivation.**

---

## Target (one sentence)

Run the mass-sector two-body O0/O1 protocol on `NativeCageIMEX` + A1 port and
gate whether phase-independent attraction (or NULL/BELOW-FLOOR) is readable
with certified passivity — vs the sponge arm’s radiation-floor workaround.

---

## Analytic expectations

### Arms

| Arm | Carrier | Boundary |
|---|---|---|
| **sponge** (reference) | reuse existing `_make_engine` path OR thin call into original helpers | PML=4 |
| **a1_port** | `NativeCageIMEX`, two sech breathers seeded into `V` | `port_sigma≈0.05` |

Primary: one separation \(d_0=7\) (mid of frozen SEPARATIONS), both phases.
Optional: full SEPARATIONS grid as flag.

### Observables

1. A1 passivity on two-body run: \(H_{\max}/H_0 \le 1+10^{-3}\).
2. O0 radiation floor (single blob) on both arms.
3. O1 `net_dsep` in-phase and out-of-phase; classify with existing
   `classify()` bins (GRAVITY-CONSISTENT / GENERIC-SOLITON / NULL / …).
4. **Discrimination:** either (a) A1 and sponge **disagree** on classify bin, or
   (b) same bin but A1 O0 floor is **lower** by \(>10\%\) relative (cleaner
   leave-taking), or (c) A1 can use a **longer** post-transient window without
   floor blow-up while sponge cannot — declare which in the result.

### Expectation (picture, not entailed)

A1 should keep passivity and either (i) recover the same gravity-consistency
bin with a lower radiation floor, or (ii) expose that the sponge “attraction”
was pad-contaminated (bin flip). NULL/BELOW-FLOOR on both is an honest WALL
outcome, not a fail of the wire-in if A1 passivity holds and floors are reported.

---

## Frozen bins (wire-in adjudicator)

| Bin | Label | Criterion |
|---|---|---|
| **(i)** | **FORCE-DECONVOLVED** | A1 passivity PASS; O0+O1 complete both phases; (a) bin flip vs sponge **or** (b) same classify + A1 floor ≤ 0.9× sponge floor **or** (c) declared longer-window advantage documented with numbers |
| **(ii)** | **FORCE-INDISTINGUISHABLE** | A1 green but no (a)/(b)/(c) |
| **(iii)** | **FORCE-PORT-FAIL** | A1 passivity fail or seeding/centroid protocol cannot run on IMEX |

Flags: full SEPARATIONS sweep; wall-window amplitudes.

---

## Out of scope

- Retiring 2026-06-23 mass-sector prereg bins as false by fiat
- Claiming Newton-G / Machian from this wire-in
- A2/A3 required for PASS
- Merging HOLD PRs

---

## Deliverables after freeze push

This prereg; then thin driver + tests + result; HOLD PR.
