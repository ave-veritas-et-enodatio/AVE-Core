# F6 tier-1 — global two-reservoir ODE ledger (ρ_latent ↔ T2) — CHARTER

**Date:** 2026-07-13
**Class:** charter (draft the discriminator BEFORE any driver) — modeled on the #662 remanence-charter pattern (`research/2026-07-12_remanence-r10-fixed-n_CHARTER.md`: charter doc + frozen bins + fireable-vs-entailed + fool-modes + Ax3 carve). **Charter first; PR DO-NOT-MERGE; driver only after charter review.**
**Grant GO (Q4):** 2026-07-13 — ρ_latent parameterization licensed as INPUT-ONLY at `clm-s4n33u` solidity 0.45.
**Frozen prereg:** downstream sibling file (`research/2026-07-13_f6-tier1-two-reservoir-ledger_prereg_FROZEN.md`) — **not created in this commit**; freeze-by-push BEFORE any driver, gated on this charter's review.

**Sector header (mandatory).** MODE: global bookkeeping **ODE ledger, NOT a field solve** — no `a(t)` evolver exists in the engine; `solve_backreaction` is static-elliptic; the engine has local first-law only, no global ΔE_cryst state object (`manuscript/ave-kb/common/engine-capability-map.md:155`). REGIME: the top-stage cascade port (Machian-horizon termination), at/near the cosmic operating point. PHASE-STATE: a held static store (ρ_latent) draining one-way into the T2 bath across the off-line↔on-line boundary. SECTOR: this is the **A-class (continuous drainage)** behavior of the **local top port** — a static-sector store transferring into a thermal reservoir; it is **NOT** the A1 dilatation-mass sector and **NOT** a Cosserat-winding claim.

**Register:** AVE substrate + EE (two-reservoir exchange, entropic sink, matched-termination absorption, Ax3-lossless interior). **Not** ΛCDM DE-as-fundamental-Λ, **not** QED zero-point energy, **not** a friction/dissipation loss.

---

## 0 · One-paragraph charter

F6 is the **irreversible ε→T2 depletion** primitive — the **DE-tracks-matter chord**, the one ΛCDM-distinct thing AVE could carry and the make-or-break the corpus has never built (`manuscript/ave-kb/vol3/cosmology/ch04-generative-cosmology/dark-energy-latent-heat-definition.md:139,144,146`: F6 = the one ΛCDM-distinct chord, UNBUILT; the `reading-i dQ/dt∝n_matter` chord is ABSENT-INVENTED at `:128`; the one attempt `photon_deplete=True` detonates). **Tier 1 is a GLOBAL TWO-RESERVOIR ODE LEDGER** (ρ_latent ↔ T2 bath): does a one-way, Ax3-legal, conservation-respecting transfer whose rate is **slaved to lower-stage occupancy** produce a DE component that **tracks matter in FORM** — and is that form distinguishable from a bare cosmological constant in the ledger's own observable? **No `a(t)` field solve** — tier 1 books reservoir exchange, nothing more. The scope is **existence + FORM only** (no magnitude matching; the naive ρ_latent value is ~120 OOM over ρ_Λ and that path is rejected canon). **TIER-2** (one X40-class discrete-click demo) is a **separate follow-on gated on this charter's review.**

---

## 1 · Physical picture (substrate)

### 1.1 What the medium is doing — the two reservoirs

The vacuum is a saturable Cosserat–LC lattice that is **continuously crystallizing** at the cosmic frontier. Crystallization has a **latent heat**: finishing a region of substrate into ordered matter releases a held store, ρ_latent — the static sector's fuel (`dark-energy-latent-heat-definition.md:64`: "DE free-store / latent heat | ε | the 'fuel'; consumed at the frontier"). Two reservoirs bracket the process:

- **ρ_latent** — the **source**: the static sector's held store (the latent heat of ongoing crystallization). Numerically SYMBOLIC-ONLY / ABSENT in the corpus; enters here as a Grant-GO'd **input parameter** at `clm-s4n33u` solidity 0.45, build_status "input-only, don't build deeper" (`dark-energy-latent-heat-definition.md:122,136`).
- **the T2 bath** — the **destination**: the huge thermal reservoir (the CMB photon gas is its entropic sink, `dark-energy-latent-heat-definition.md:67`). **Irreversibility comes from its mode-count, not from a nonlinearity** — the reconvergence probability into the source is effectively zero, so an energy-conserving transfer INTO T2 has `dS>0` and is Ax3-COMPLIANT (`dark-energy-latent-heat-definition.md:84-86`, verbatim: "an **energy-conserving one-way TRANSFER** into the huge T2 reservoir ($dS>0$), NOT a friction loss, so it is Ax3-COMPLIANT").

Tier-1 books **exactly this exchange and nothing else**. There is no `a(t)`, no field, no spatial solve: two scalars ρ_latent(t) and E_T2(t), a transfer rate Γ, and a conservation ledger `ρ_latent + E_T2 = const`.

### 1.2 What "DE-tracks-matter" means here

ΛCDM's Λ is a constant: the dark-energy density does not know how much matter exists. **AVE's F6 chord is that the drainage rate is slaved to how much matter has clicked in** — `reading-i`, `dQ/dt ∝ n_matter`, which the corpus tags **ABSENT-INVENTED** (`dark-energy-latent-heat-definition.md:128`). The *frontier* form (`reading-ii`, `Γ = 3H·ρ_latent`) is the corpus default and is FORCED-in-form / ASSERTED-in-rate (`:121,142`); it is **not** the chord. The chord is specifically the **inter-stage slaving**: lower-stage matter occupancy setting the top-port drainage rate, a coupling **no canon site derives** (the Machian integral is spatial, produces G, and moves no energy).

Tier-1's question is deliberately narrow: **does a matter-slaved, Ax3-legal, conservation-respecting drainage produce a DE component whose FORM tracks matter, and is that form distinguishable from a constant in the ledger's own observable?** Nothing about magnitude.

### 1.3 The walked architecture (ruling-grade inputs — Grant-walked 2026-07-13)

These four elements are recorded as **ruling-grade inputs** (the walked map), not canon derivations:

| Element | Identity |
|---|---|
| **Source** | **ρ_latent** — the static sector's held store (latent heat of ongoing crystallization). |
| **Destination** | **the T2 bath** — the huge thermal reservoir; irreversibility from its mode-count, not a nonlinearity. |
| **Transducer / locus** | **the mass envelope** — where the transfer is physically effected. |
| **Door** | **the off-line ↔ on-line boundary** — the gate the transfer passes through. |

### 1.4 Cascade address ★QUARANTINE — Grant-walked RULING-GRADE INPUT, not canon

> **★QUARANTINE TAG.** The following cascade address is a **Grant-walked ruling-grade INPUT (2026-07-13)**, NOT a canon-derived result. It is the physical picture the tier-1 ledger is built to test; it must not be cited elsewhere as established corpus physics. Treat every clause below as premise-under-test.

**F6 = the A-class (continuous drainage) behavior of the LOCAL top port** — the Machian-horizon termination. Canon already prices that port as a **distributed transmission-line input impedance at the Hubble-horizon termination** (`manuscript/ave-kb/common/translation-tables/translation-circuit.md:126`, Machian-G ↔ TL-input-impedance row; re-confirmed at `:335,:410`). **F6 is the claim that the Re(Z) at that termination is nonzero and one-way** — the port has a real, irreversible drainage channel, not a purely reactive/lossless one.

- **The FRW `3H·ρ_latent` rate reads as the matched termination's absorption rate** — the top-stage loaded Q ~ O(1) (matched), which is exactly where the cascade's far end already sits.
- **DE-TRACKS-MATTER = the top port's A-rate slaved to the lower stages' B-occupancy** — how much clicked-in matter loads the envelope sets the top port's drainage rate. **That inter-stage slaving IS the chord**, and it is **precisely what no canon site derives** (the Machian integral is spatial, produces G, and moves no energy; no inter-stage energy coupling exists in canon).

### 1.5 Channel tag (do not conflate)

| Channel | Role |
|---|---|
| Static-sector store ρ_latent → T2 (A-class drainage, LOCAL top port) | **THIS ledger's transfer axis** |
| A1 dilatation-mass tank | Owns rest-mass; **NOT** the F6 drainage source (SECTOR⊥). A finished electron is a LOSSLESS tank, paid latent heat ONCE (`dark-energy-latent-heat-definition.md:65`) — it must not appear as a drain in the ledger (see `electron-no-drain` detector, §4.2). |
| Cosserat-winding (2,3) charge | Owns charge/spin; **NOT** an energy source for the top port. |

This discriminator is **static-sector / top-port** tagged. The A1 and Cosserat sectors appear only as **constraints** (the three hard detectors, §4.2), never as the transfer source.

---

## Ax3 reconciliation (mandatory carve)

<!-- SECTION-AX3 -->

---

## 2 · Circuit picture (EE mapping)

<!-- SECTION-2 -->

---

## 3 · Map (where this sits in the program)

<!-- SECTION-3 -->

---

## 4 · Analysis (what would discriminate; what would fake)

<!-- SECTION-4 -->

---

## 5 · Deliverables and sequencing

<!-- SECTION-5 -->

---

## 6 · References (grep-verified anchors — 2026-07-13, at base d0037d8f)

<!-- SECTION-6 -->
