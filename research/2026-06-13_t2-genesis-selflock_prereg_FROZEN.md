# T2 — genesis self-lock (photon-at-a-field → autoresonant bulk breather) — pre-registration

> **STATUS: FROZEN (2026-06-14, Rule-11)** — frozen on cage-merged `main` (cage [PR #222](https://github.com/ave-veritas-et-enodatio/AVE-Core/pull/222) MERGED `c9b233cc`; the static-basin foundation is on `main`). **Auditor verifies this frozen prereg before any driver code** — the 5 §5 conditions + the four-way discriminator table (§6) + the g_front-engagement floor (§5 / §6 F6).
> **Platform:** `crystal_engine.py` — the **stiffening-cage firewall branch** (A1 dilatation). Advance a **rank**, NOT a new `genesis_v{N}` file (`ave-loop-gap-harness-discipline`).
> **Lane:** implementor (`analysis/2026-06-13-t2-genesis-selflock` off `main`).
> **Builds on:** the cage result (the static basin: sech self-focuses / generic Gaussian disperses → **profile-selective**; PR #222) + the auditor's §4 circuit + §5 spec (2026-06-13).

---

## 0. Derivation target (one sentence)

On `crystal_engine` (the A1-dilatation stiffening cage), does a **flowing transverse photon** (`seed_photon`) incident on a **generic sub-threshold bulk field** (the "nucleus") **dynamically autoresonant mode-convert** (via the front-gated gyrotropic converter) **and LOCK** into the persistent v14-Mode-I bulk breather — the carrier phase-locking to its **own dropping local resonance** $\omega_{\text{local}}(t)=\omega_0\sqrt{S(A(t))}$ as the core fills — vs **DISPERSE** (the sub-threshold field sheds it) or **DETONATE** (pump artifact)?

## 0.1 What is new (not a re-tread — verified by corpus inventory)

| Prior | Standing state | Why T2 is new |
|:---|:---|:---|
| autoresonance / self-lock at Γ=−1 | **underived ✗ GAP** (`photon-ee-mapping.md:98`) — *asserted, never tested* | T2 converts an asserted mechanism into a tested one |
| v14 Mode I breather | basin **planted** (stationary sech, A=0.85) + persists (`breathing-soliton-v14-mode-i.md:20`) | proves "the basin exists once you're in it"; never tested whether a **flowing sub-threshold carrier climbs in** |
| `AutoresonantCWSource` PLL | ⛔ INVALIDATED (60 kV vs V_yield=43.65 kV); 1.009 result **RETRACTED** (0/20) | different question (forced rupture-ring-up vs self-lock) on a different engine (discrete `VacuumEngine3D`). **NOT cited.** |

## 0.2 The collision that shaped this — *pair-production needs a field* (Grant + auditor confirmed)

`crystal_engine`'s converter is **front-gated**: $f_V=-\gamma\,g_{\text{front}}(A)\,\Omega_w$, with $g_{\text{front}}$ computed from $A=|V|/V_{\text{yield}}$ (**bulk-only**), so $g_{\text{front}}\approx0$ wherever $V\approx0$ ([`crystal_engine.py:238-240`](../src/ave/core/crystal_engine.py:238)). **A lone photon (no field) cannot bootstrap the bulk — it reproduces genesis-23's null by construction.** This is the engine **correctly** encoding that pair-production needs a field ($\gamma+Z\to e^+e^-$; lone-photon-in-vacuum is physically forbidden — no momentum sink). So the precursor is **photon-AT-A-FIELD**, not photon-from-vacuum.

> **(B) from-vacuum is OUT OF SCOPE** — physically forbidden + engine-nulled. **Not a build target**; no 4th / "substrate-complete" engine to host a non-physical process (anti-loophole; a new engine needs Grant sign-off).

## 1. Mechanism circuit (the spec the driver instruments against)

```
[photon: transverse AC source, helicity Ω_w]                 seed_photon(...)
        │
        ▼
[GATED gyrotropic converter:  M = γ·g_front(A)]   ← the gate IS the field-requirement
        │                                            (g_front≈0 at A=0 → no field, no coupling)
        ▼
[bulk varactor mass-tank (the cage):  ω_local = ω₀·√S(A)  ↓ as it fills]
        │                                            biased sub-threshold A₀<1 (the "nucleus")
        ▼
[autoresonant feedback: A detunes ω_local AND gates M]
        │
        ▼
   { LOCK  /  DISPERSE  /  DETONATE }
```

## 1.1 substrate-native-check (walked against `crystal_engine`)

| CP | Verdict |
|:---|:---|
| CP1 | Leapfrog wave propagation (no minimization; no CW pump). |
| CP2 | Cross-coupled — bulk $V$ (A1) ⊗ shear $w$ (transverse photon) via the front-gated converter. |
| CP4 / A46 | The autoresonance signature is a **phasor** claim → instrument in the $(V,\ \partial_tV/\omega_{\text{char}})$ reactance-pair (`phase_space_vinc_vref(ω_char)`), **NOT real-space**; feed `ω_char = ω_local(t)`. |
| 🔴 CP8 | Seed the **generative precursor** (flowing photon + **generic** sub-threshold field), **NOT the sech eigen-profile**. The generic field is the **site** pair-production happens at (the nucleus), not the electron-to-be. Planting the sech = the CP8 re-plant the cage exposed → **VOID**. |
| CP9 | The lock signature is the **dynamically-evolved** phasor phase-coherence + `max|A|` ring-up, NOT an algebraic $\omega_{\text{local}}$ read. |
| CP10 | The converter is the saturation-**FRONT** boundary coupling ($g_{\text{front}}$); confinement = Γ=−1 wall, not a bulk force. |

## 2. Platform + driver

- **Engine:** `crystal_engine.py` — `converter_on` toggle (:66); `seed_photon` (:305, flowing transverse); `seed_bulk(..., helical=False)` (:287, **generic Gaussian** — NOT a sech); `phase_space_vinc_vref(ω_char)` (:337); `saturation_kernel` (:191).
- **Rank discipline:** advance a rank on the cage lane; **do not** open `genesis_v{N}`. New driver `src/scripts/vol_1_foundations/t2_genesis_selflock.py` (driver-not-build).
- **canonical-source:** import `V_yield`, `ALPHA`, etc. from `ave.core.constants`; `verify_constants` cross-check before any output.

## 3. Instrumentation (🔴 corrected exponent — carry the flags)

- **$\omega_{\text{local}}(t) = \omega_0\cdot\sqrt{S_{\text{core}}}$**, with $S=$ `engine.saturation_kernel()` $=\sqrt{1-A^2}$ (correct), $S_{\text{core}}=\min$ over interior. The matter clock / LC resonance rides the shear speed $\sqrt{S}=(1-A^2)^{1/4}$.
  - 🔴 **NOT** $\omega_0\sqrt{1-A^2}$ — the **STALE** pre-split form (off by 2×) flagged at [`op14-local-clock-modulation.md:13`](../manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/op14-local-clock-modulation.md:13) (PR#149).
  - 🔴 **NOT** `engine.refractive_index()` — a **separate** carried defect (returns $S^{0.25}$, `crystal_engine.py:432`).
- **Autoresonance track (the self-lock signature):** the carrier phase vs $\omega_{\text{local}}(t)$ in the $(V,\partial_tV/\omega_{\text{local}})$ phasor (`phase_space_vinc_vref(ω_char=ω_local(t))`). **LOCK** = phase-coherence **sustained** as $\omega_{\text{local}}$ drops; its **absence** is the standing ✗.
- **Ring-up:** `max|A|`. **Boundedness:** `max|A| ≲ V_yield` (≪ genesis-24's ~1e4). **Persistence:** envelope trend (flat vs slow-decay, A2.4-style; long enough budget to resolve TRANSIENT).
- **Sign caveat:** $c_{\text{eff}}=c_0(1-A^2)^{-1/4}$ **diverges** (self-steepens) while $\omega_{\text{local}}$ **drops** — the lock tracks the **dropping resonance**, not the diverging phase velocity. Keep distinct.

## 4. Regime / phase-state declaration (`ave-regime-phase-state-check`)

- **MODE:** bulk A1 dilatation (the cage) + transverse shear (the photon), coupled via the front-gated converter.
- **REGIME:** **NEAR-YIELD FORMING** (the sub-threshold field $A_0<1$ climbing toward yield via the photon's energy) — **NOT** the post-rupture regime ($\max A^2\approx13$–$14$) that quarantined v9 Phase-2. **Exclude any arm that ruptures ($A^2>1$) from the lock verdict.**
- **PHASE-STATE:** forming / nucleating (the breather self-assembling), not steady-state.
- A null **is** meaningful here (the self-lock effect *can* exist in near-yield forming); a post-rupture artifact is excluded, not binned.

## 5. Arms

> **🔴 g_front-engagement window (pre-freeze gate — VERIFIED).** The converter is a pressure-gated valve: $f_V=-\gamma\,g_{\text{front}}(A)\,\Omega_w$, with $g_{\text{front}}$ a shell **centered at $A=$ `front_center` $=R_{II}=\sqrt3/2\approx0.866$**, width $0.18$ ([`crystal_engine.py:67,210`](../src/ave/core/crystal_engine.py:210)). The field's peak $A_0$ must reach the shell or the valve never cracks. The cage proved the **generic Gaussian disperses alone across frac 0.30–0.95, converter OFF (S1) AND ON (S2)** → a clean window exists:
> $$A_0\in[\,R_{II}-\text{front\_width}\approx0.69\ (\text{g\_front floor}),\ \ 0.95\ (\text{sub-rupture}, R_{III}=1)\,),\quad\text{centered on }R_{II}=0.866\ (\text{g\_front maximal}).$$
> **front_center $=0.866 < 0.95$ (generic disperse-ceiling) ⇒ the window exists** (the auditor's required check, PASSED — no arm-redesign). **"Sub-threshold" here = sub-LOCK-BASIN** (disperses alone), **NOT** sub-saturation — the field is *in* the saturated regime ($A_0\approx R_{II}$), which is **required** to open the valve.

| Arm | Config | Isolates |
|:---|:---|:---|
| **(C)** | photon + generic field ($A_0\in[0.69,0.95]$), converter **ON** | **PRIMARY** — the photon-at-a-field genesis |
| **(A′)** | generic field, converter **ON**, **NO photon** ($\Omega_w=0$) | **the photon-isolating discriminator** (converter ON in both; only the photon differs). *Pre-established: cage **S2 DISPERSES** at 0.70/0.85/0.95.* |
| **(A)** | generic field, converter **OFF**, no photon | the converter-isolating control. *Pre-established: cage **S1 DISPERSES**.* |
| **(PUMP)** | genesis-24 **fixed-ω** CW drive on $V$ | the **pump/detonate control** (`ave-conserved-vs-pumped`: lock must energize+LOCK a bounded invariant, not pump it) |

- **The single new variable is the photon.** Cage S1 (converter-OFF) and S2 (converter-ON, no photon — the converter is **inert without $\Omega_w$**) BOTH disperse across the window. (C) adds only the flowing photon ($\Omega_w\ne0$ → $f_V=-\gamma g_{\text{front}}\Omega_w\ne0$ where the valve is open) → **(C) LOCK ⟹ the photon did it** (vs (A′), the photon is the only difference).
- **$A_0$ swept across $[0.69, 0.95]$** (g_front-engaged AND generic-disperses-alone AND sub-rupture). **Ablations:** helicity ± · front-overlap (sweep below 0.69 only to *confirm* the valve-shut false-negative, §6 F6).

## 6. Falsifiers + the four-way discriminator table (LOAD-BEARING)

| (C) photon+field | (A/A′) field, no photon | Verdict |
|:---|:---|:---|
| **LOCK** (bounded+persist), $A_0\ge$ g_front floor | **DISPERSE** | ✅ **TARGET POSITIVE** — the photon makes the electron at the field |
| **LOCK** | **LOCK** | ⚠️ the **field self-genesises via Op14**; photon is a **PASSENGER** — bulk self-genesis, a *different* claim (NOT photon→mass). *Empirically pre-excluded: cage S2 (converter-ON, no photon) DISPERSES.* |
| **DISPERSE**, $A_0\ge$ g_front floor | — | ❌ no genesis on `crystal_engine` (valve **open**, photon still can't build it) |
| **DISPERSE**, $A_0<$ g_front floor | — | ⛔ **VALVE-NEVER-OPENED — apparatus artifact, EXCLUDED** (not binned; `ave-apparatus-floor-attribution`) |
| any → **DETONATE** | | 🔴 pump artifact, not genesis (conserved-vs-pumped guard) |

**TARGET POSITIVE = (C) LOCK ∧ (A/A′) DISPERSE, with $A_0\ge$ the g_front-engagement floor.** A (C)-disperse counts as ❌ "no electron" **only** where the valve was open ($A_0\ge0.69$); below it, the photon never coupled — not interpretable as a physics null.

- **F0 — KEEP-BOTH:** converter OFF ∧ photon OFF ∧ generic field sub-critical ⇒ disperses (cage-consistent baseline).
- **F1 — (C) lock:** `max|A|` grows + phasor phase-coherence tracks $\omega_{\text{local}}$ + bounded + persists.
- **F2 — discriminator:** (A′) (field + converter-ON, **no photon**) **DISPERSES** (else the field self-genesises via the converter and the photon is a passenger — the ⚠️ row).
- **F3 — autoresonance signature (CP9):** the phase-coherence is **dynamically sustained** as $\omega_{\text{local}}$ drops (not an algebraic read).
- **F4 — conserved-not-pumped:** bounded + persistent (the ratified **boundedness** criterion, **NOT energy-flat** — superseded in cage Amendment 3); the **PUMP** arm detonates/pumps (control).
- **F5 — regime:** the lock occurs in **near-yield forming** ($A^2\le1$); post-rupture excluded.
- **F6 — g_front-engagement floor (apparatus-floor-attribution):** a (C)-disperse is binned ❌ "no genesis" **only** if the field's peak $A_0\ge$ the g_front floor ($\approx R_{II}-\text{front\_width}=0.69$) so the converter valve was open. A (C)-disperse at $A_0<0.69$ = **valve-never-opened** (g_front$\approx0$ → $f_V\approx0$), an apparatus artifact → **EXCLUDED**, not a physics null. One arm at $A_0<0.5$ is run **only to confirm** this false-negative exists (the apparatus floor), never as evidence against photon→mass.

## 7. Success criterion

**Bounded + persistent breather** (the ratified FLAG-2 boundedness criterion — **not** energy-flat, the clause cage Amendment 3 just superseded), realized in the **(C) LOCK ∧ (A/A′) DISPERSE** cell, in the near-yield forming regime.

## 8. Hypotheses (`consistency-vs-emergence`)

| ID | Statement | Class |
|:---|:---|:---|
| H1 | (C) photon+field locks where (A) field-alone disperses | **emergence-test** (photon→mass at a field) |
| H2 | (A) generic sub-critical field alone disperses | consistency (cage-consistent) |
| H3 | the (C) lock is **autoresonant** (phase-coherence tracks $\omega_{\text{local}}$) | the autoresonance ✗ → **tested** |
| H4 | the fixed-ω PUMP arm detonates/pumps, not locks | consistency (conserved-vs-pumped control) |

## 9. Out of scope (flag, don't fold)

- **(B) from-vacuum photon→mass** — physically forbidden, engine-nulled; no 4th engine (anti-loophole).
- **The (2,3) winding / charge "3"** — T3 (the composite), separate; **never wire the winding into the bulk phasor** (`master-equation.md:20`, the genesis-24 double-count).
- **χ (chiral magnitude)** — the (c) lane (srs), independent.

## 10. Skills (mandatory)

`ave-prereg` (Rule-11 freeze; v1.2 referential-integrity) · `substrate-native-check` (CP8/9/10) · `consistency-vs-emergence` · `phase-space-coordinate-check` · `ave-regime-phase-state-check` · `ave-conserved-vs-pumped` · `ave-discrimination-check` · `ave-driver-script-honesty` · `ave-canonical-source` · `ave-loop-gap-harness-discipline`.

## 11. Corpus anchors

| Leaf / artifact | Role |
|:---|:---|
| cage result (PR #222) | the static basin (profile-selective: sech self-focuses / generic disperses) |
| `breathing-soliton-v14-mode-i.md:20` | the basin-exists precedent (planted, stationary) |
| `crystal_engine.py:238-240` | the front-gate = field-requirement (genesis-23 null by construction) |
| `crystal_engine.py:305` / `:337` | `seed_photon` (precursor) / `phase_space_vinc_vref` (phasor) |
| `op14-local-clock-modulation.md:13` | the $\omega_{\text{local}}$ exponent (corrected: $\sqrt S$, not $\sqrt{1-A^2}$) |
| `photon-ee-mapping.md:98` | autoresonance ✗ = underived GAP (the thing T2 tests) |
| genesis-24 result | the fixed-ω pump/detonate control |
| `master-equation.md:20` | the two-"3"s — winding OUT of scope (no double-count) |

---

> **Freeze gate (before driver):** cage PR #222 merged → rebase this prereg on cage-merged `main` (cross-links resolve) → freeze (`_FROZEN`, Rule-11, prereg-alone commit) → **auditor verifies** (referential integrity · CP8 generic-field guard · the $\omega_0\sqrt S$ exponent · the conserved-vs-pumped PUMP arm · the discriminator-table bins) → **then** dispatch the driver implementor.
