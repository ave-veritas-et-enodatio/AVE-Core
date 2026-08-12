# K-IDENTITY — ADJUDICATION BRIEF FOR GRANT (R51 §3)

**From:** the boundary-response derivation lane (R51 §4) ·
[`research/2026-08-12_boundary-response_result.md`](../research/2026-08-12_boundary-response_result.md)
· prereg frozen `b05ec6bd`
**Question this brief answers:** **not** what `K`'s value is — **what kind of thing `K` is.**
**Posture:** options with evidence. **No recommendation**, because the math does not force one
(§4 states exactly what it *does* force).

---

## §1 — What the lane found, in one paragraph

The common-mode tank **exists**, and the chain that produces it contains **no `K` anywhere**:
`E(R) = a·R + b/R`, one minimum at finite `R*`, `E''(R*) > 0`. The collapsing term is the T2
winding's gradient energy (`a = c₁γ_c n²`, `γ_c = G_vac ℓ_c²`, receipted). The restoring term is the
defect's **own A1 self-field energy at fixed enclosed content** (`b = c₂𝒬²/𝒞_A1`, from Axiom 3's
kinetic term + the Gauss constraint + geometry). R51 item 2 **survives its kill-check** — but its
stated mechanism is wrong: the tank's `C` is **not** *"the medium's bulk compliance seen at the defect
boundary."* The medium's bulk compliance is **infinite** (zero stiffness) and contributes **nothing**.

---

## §2 — The plumber statement

The vacuum's A1 channel is **a pure inductor to ground with no shunt capacitor** — inertia, no
stiffness. Push a longitudinal wave into the cold bulk and nothing pushes back; that is #935's flat
band, re-derived here from Axiom 3's curl-only potential.

But a **defect** is not a wave. It is a fixed amount of stuff with a boundary. Its own self-field
energy goes as `1/R` and its own winding tension goes as `R`, so it has a size it wants to be, and it
rings about that size. **The medium never had to push back — the knot pushes back on itself.**

That is why the boundary response differs from the bond response, and it is the whole content of the
lane: **the flat direction is flat in the field, but the energy depends on the source geometry, and
the defect's size *is* the source geometry.**

---

## §3 — The three readings, with the evidence

### (i) CONSTITUTIVE — `K` is a property of the crystallized bond network, derivable in principle

**Against — now doubly unsupported:**
- #261 already ruled: **not crystalline, not constitutively forced** (both gates pass), GR-imported.
- This lane adds: on the receipted set the longitudinal stiffness is **exactly zero**, not merely
  unknown. Axiom 3's potential is curl-only, so `∇×A_L ≡ 0` contributes nothing; Axiom 5 explicitly
  *"adds no kinetic or potential term on the flat direction"* (`eq_axiom_5.tex:88`). A constitutive
  `K` read off the receipted axioms would have to be **`K = 0`**, contradicting `K = 2G ≠ 0`.
- And now: **the boundary response does not need it.** The one job `K` was doing in R51 item 2 —
  supplying the tank's compliance — is done by the defect's own self-field.

**⚠ But there is a live repair route, and it is the sharpest open question in this brief.** A discrete
central-force spring network with bond stiffness `k₀` generically **has** a nonzero bulk modulus set
by `k₀` + geometry. Axiom 3's *continuum* action says `K = 0`. **These two statements disagree.**
Either the continuum action is incomplete as a description of the discrete K4 network (⇒ `K` is
constitutive after all, recoverable from `k₀` + K4 geometry — reading (i) repaired), or the K4 network
is genuinely not central-force in the longitudinal sector and `K = 0` is correct (⇒ reading (iii)).
**This is a decidable fork and it is arguably the real content of #261's open item** — see §5.

### (ii) QUENCH INITIAL CONDITION — frozen in at genesis, measured-not-derived (your lean)

**For:**
- The lane's own result carries an IC dependence, and it is explicit: the tank's **scale** `R*` rides
  `𝒬`, and `𝒬` is **genesis-deposited boundary data** by Axiom 5 clause S's own wording
  (*"it states that the flux is written, not how"*). Existence is derived; scale is deposited.
- That is the **FORM-derived / VALUE-imported** signature landing again — consonant with the standing
  meta-finding and with the freeze-in thread (`trampoline-framework.md:95-125`, where `u₀` and
  therefore `G` are anchored to one cosmological parameter `Ω_freeze`).
- Pre-stress genuinely **can** manufacture effective stiffness on an otherwise-flat direction — a
  guitar string's restoring force is tension, not bending stiffness. So an IC reading is not
  mechanically absurd; frozen-in pre-tension is a real candidate source.

**Against / the sharp caveat:**
- **The IC the lane actually found is `𝒬`, not `K`.** `K` appears nowhere. So the evidence supports an
  IC reading of the **defect deposit**, and says nothing directly about `K`'s identity.
- For (ii) to be about `K`, the frozen-in state would have to add a longitudinal stiffness to the
  bond network. Pre-tension classically supplies **transverse** stiffness (that is already the
  `T_EM → G` route in canon); whether it supplies **longitudinal** stiffness is exactly the discrete
  central-force question in (i)'s repair route. **(ii) and (i)-repaired collapse onto the same test.**
- ⚠ **FLAG-4, load-bearing for this reading:** the freeze-in formula itself consumes a nonzero `K₀` —
  `u₀ = ρΩ²_freeze r²_node/(2K₀)` (`trampoline-framework.md`). If that `K₀` is the bulk modulus, the
  freeze-in derivation **consumes the very object #935 removed**, and reading (ii) is circular as
  currently written. If it is the bond stiffness `k₀` — which the same passage distinguishes
  (*"Bond stiffness k₀ is intrinsic to the LC tank … Not freeze-in dependent"*) — it is clean.
  **The source does not disambiguate the symbols.** This needs resolving before (ii) can be assessed
  on its merits.

### (iii) BOUNDARY-RESPONSE ECHO — the defect-boundary stiffness is the real object; `K = 2G` is its far-field shadow

**For — the most independently corroborated reading:**
- This lane **exhibits the real object**: a genuine, K-free, defect-boundary stiffness
  `E''(R*) = 2b/R*³`. Reading (iii) needs such an object to exist, and it now does.
- The cold vacuum has **zero** longitudinal stiffness (§3(i)). So any *measured* bulk stiffness must
  come from something present **only where matter is** — which is precisely **R51 item 3**: the cold
  vacuum is the empty band, the **defect population is the carrier gas**.
- `K = 2G` is **GR-imported** (#261) — i.e. it was read off the **far field** (trace-reversal /
  `ν = 2/7`). A quantity obtained by reading the far field is exactly what a far-field shadow looks
  like.

**Against / what is missing:**
- **This lane does not derive the factor 2, and does not attempt to.** ⚠ Any quick-looking route to
  the `2` should be treated as **suspect on arrival** — a `½`/`¼`-class over-determination is the
  known coincidence tell, and manufacturing the 2 is the single most likely way this reading gets
  wrongly banked.
- "Far-field shadow of the defect population" is a **mechanism sketch, not a derivation**. It predicts
  an effective `K_eff ∝ defect density`, which is checkable — and which the cold-vacuum reading
  requires to vanish in the empty limit.

---

## §4 — What the math DOES force (the only unhedged statements here)

1. **Whatever `K` is, it is not the compliance the common-mode tank runs on.** That specific reading —
   implicit in R51 item 2's wording — is **eliminated**. This is a real narrowing, and it is the one
   thing this lane settles about `K`.
2. **On the receipted continuum set, the cold vacuum's longitudinal stiffness is exactly zero.** Not
   underdetermined — zero. Any nonzero `K` must therefore come from outside that set: from the
   discrete network (i-repaired), from a frozen-in state (ii), or from the defect population (iii).
3. **The math does NOT choose among (i-repaired) / (ii) / (iii).** No recommendation is offered, per
   the brief's terms.

---

## §5 — The one test that would separate them (routed, not run)

**Compute the K4 network's longitudinal stiffness discretely, from bond stiffness `k₀` + K4 geometry,
with no continuum step and no `K` input.** The answer is one of:

- **`K_discrete ≠ 0`** ⇒ Axiom 3's continuum action is **incomplete** in the longitudinal sector, `K`
  is **constitutive** after all — reading **(i) repaired** — and #935's "the axioms underdetermine the
  bulk sector" sharpens to "the *written continuum action* underdetermines it while the discrete
  network does not." That is a significant and checkable claim about the axioms.
- **`K_discrete = 0`** ⇒ the K4 longitudinal sector is genuinely flat, the continuum action is
  faithful, and a measured `K ≠ 0` must be **matter-sourced** — reading **(iii)**, with the
  defect-density scaling as its forward test.

Either outcome also disposes of (ii): if `K_discrete = 0`, no frozen-in state can add a stiffness the
network does not have; if `K_discrete ≠ 0`, the freeze-in route becomes assessable — **once FLAG-4's
`K₀`-vs-`k₀` ambiguity is resolved**, which is a prerequisite, not a detail.

**This test is K-free by construction, needs no engine run, and is the natural successor lane.**

---

## §6 — Decisions this brief is asking for

- **The `K_discrete` test (§5)** — run it as the successor lane, or hold? It is cheap, it is the only
  clean separator identified, and it directly closes #261's open item.
- **FLAG-4, `K₀` vs `k₀` in `trampoline-framework.md:95-125`** — which symbol is that? Reading (ii)
  cannot be assessed until this is disambiguated, and only you can say what was meant.
- **FLAG-1, R51 item 2's mechanism wording** — item 2's *conclusion* survives; its stated mechanism
  (*"C is the medium's bulk compliance"*) does not. Correct the record, or leave it and let this
  result stand as the correction? *(Flagged, not fixed — no record edited by this lane.)*
- **FORK-W (result §3)** — the smooth `1/R` minimum vs the Axiom-4 saturation wall: which bounds the
  defect first is a value comparison this lane was scoped out of. Route it, or fold it into the
  successor lane?

**Not asked for and not implied:** any move on `K`'s value, any solidity change, any propagation. This
lane mints nothing and edits nothing.
