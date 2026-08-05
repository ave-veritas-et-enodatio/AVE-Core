### ENTRY 2026-08-03-rulings-mr-batch (2026-08-03): implementer — Grant rulings 1 / 3 / 5 / 6 executed (K=2G register, PRODUCT declaration, incompressible repair, neon demote)

> **🔁 REPAIR PASS 2026-08-03 (review verdict CLEAR-WITH-REPAIRS, findings 1–9). Read this before the body — one headline claim is RETRACTED and one section now needs a Grant decision.**
>
> | # | finding | where the repair landed | class |
> |---|---|---|---|
> | **1** | *"the equation survives the premise strike"* is **wrong three independent ways** (parity / single-valuedness / magnitude) | §Ruling 3(b) — claim **RETRACTED** under Rule 12; **two variants staged, NEITHER FIRED** | **★ Grant decision required** |
> | 2 | neon print/mirror card mismatch + KB vocabulary in print | `12_neon.tex` — the "When subjected to an external electric field (as in a neon discharge tube)" sentence (cited `:65` here; moved to `:91` on 2026-08-05, so cite by ANCHOR TEXT) + `topological-area.md:18` sync note | canon fix |
> | 3 | repaired gauge chain covered $\mathbf{B}$ but not $\mathbf{E}$ | `05_electroweak_gauge_theory.tex` + `gauge-boson-masses.md` — `def-l0ngdu` promoted to **step 3′** | canon fix |
> | 4 | the *"mass flow"* follow-on is **premise-critical**, not wording | re-ranked to follow-on **#4**; severity corrected on the KB leaf | re-rank |
> | 5 | dual-ruler defect — EMF vs strain ruler | §Ruling 3(b) receipt corrected to $h/h_{yield}=1.2\times10^{-20}$; reconciliation routed as **#8** | receipt + route |
> | 6 | arm (b) available, but **not at $r_s$** — rupture is at $r_{sat}=3.5\,r_s$ | additive caveat on `black-holes-impedance-mismatch.md` | canon note |
> | 7 | transfer-cost candidate contradicted its own LC-tank example | §Ruling 3(c) — *within-channel* → **within-SYSTEM**; boundary-Joule named as open edge (iv) | wording + open edge |
> | 8 | `constants.py:589` stale (`XI_MACHIAN` is at `:650`) | §Ruling 1 — corrected in place; pattern routed as **#9** | cite fix |
> | 9 | branch count stale (11) | branch-overlap section — re-enumerated, **13 lanes, 0 overlap** | re-verify |
>
> **What did NOT change:** every Grant ruling as issued (1 / 3 / 5 / 6), the plasticity strike, the regime-broken-premise strike, the PRODUCT declaration on the BH-information FLAG, the K=2G register content, and the neon demote. **Zero ids minted; `.index/` and `src/` byte-untouched.**

- **Class: ruling execution, not adjudication.** Four Grant rulings fired 2026-08-03, **verbatim `[sic]`, as one message**:

  > ***"1. Agree, and I think we should at some point find it's a forced form … 3. follow your rec, there's always a cost when transferring energy between regimes/states/channels right? seems like a theorem or law territory … 5. repair 6. demote"***

  One commit per ruling (four), plus this fragment. **Mints ZERO ids** (INVARIANT-S11) — no `clm-`/`def-`/`exp-`/`sup-`/`ilk-` minted, retired or re-pointed. **No `confidence` / `quality` / `solidity` / `build_status` / `status` field moves anywhere.** `.index/` and `src/` **byte-untouched** (no file from either tree appears in the diff).
- **Two-method verification of every site BEFORE editing** (no line number trusted from the dispatch): each target was located by **content** (`grep -rn` on a quoted string from the sentence itself) and independently by **`git grep`**, and the two methods were required to return the same set. Two dispatch line-cites were off and are corrected in the receipts below.

---

## RULING 1 — `K = 2G` register (agree; plus the routed "forced form" aspiration)

**Ruling `[sic]`: *"1. Agree, and I think we should at some point find it's a forced form"*.** Commit **`7a6f4ba6`**. Two files: [`manuscript/ave-kb/common/interlock-register.md`](../../manuscript/ave-kb/common/interlock-register.md) (the machine home) and [`manuscript/ave-kb/common/form-deriving-value-importing.md`](../../manuscript/ave-kb/common/form-deriving-value-importing.md) (the prose home). Both carry the count; both were checked, and **neither needed a count edit** — see below.

### The tagging half (what the ruling settles)

- **`expected-independent-count:` STAYS 3, byte-untouched.** Verified before editing: `interlock-register.md:12` reads `expected-independent-count: 3` and `:11` reads `calibration-params: clm-0ktpcn clm-5xon03 clm-dsb560`. `form-deriving-value-importing.md:68-70` carries the same set in prose (*"a marked **calibration set of 3 dimensionful constants** `{m_e, α, G}`"*). **`K = 2G` was never in either set** — the ruling's job is to say *why it must not be added*, not to remove it.
- **The ruled sentence, landed at both sites:** `K = 2G` is **NOT an independent calibration input**; it is a **separately-tagged constitutive-FORM import edge** — the GR **trace-reversal lock**, GR-IMPORTED per PR [#261](https://github.com/ave-veritas-et-enodatio/AVE-Core/pull/261) (MERGED; both provenance gates pass — *not* crystalline-forced, *not* constitutively-forced) — **distinct from G's value import**.
- **Why the edge classes are genuinely different (the load-bearing distinction).** What `K = 2G` imports is a **relation between two moduli** — a constitutive **FORM**. What G imports is a **VALUE**: the dimensionless Machian termination `ξ ≈ 8.15×10⁴³`, back-solved `ξ = ℏc/(7 G m_e²)` from CODATA G (`ilk-gravmb` grounding; `src/ave/core/constants.py:650` `XI_MACHIAN`). Two different objects, two different edges. **Two distinct import edges; one count of 3.**

> **⚑ Cite correction 2026-08-03 (review finding 8) — and the sixth instance of a standing pattern.** This fragment first cited **`constants.py:589`** for `XI_MACHIAN`. Verified at this tip: the symbol is at **`:650`** (`XI_MACHIAN: float = HBAR * C_0 / (7.0 * G * M_E**2)`); `:589` sits inside the **topological-packing-fraction** comment block (`# P_C is the unique EMT operating point where K/G = 2 …`) — a *different* constant entirely, so the stale cite pointed at real-looking but wrong content. Corrected in place, and the path is now given in full (`src/ave/core/constants.py`) rather than by bare filename. **The pattern, not the typo, is the finding:** this is the **sixth** `src/` line-cite staleness caught in the corpus. KB and docket prose pins `src/` line numbers, refactors move them, and **nothing in `make verify` binds the two** — so these rot silently and are caught only by a reader who happens to open the file. Routed as follow-on **#9** (symbol-anchored cites, or a `src`-cite verifier); **not taken here.**
- **Mechanically why the count is untouched:** `K = 2G` mints no `ilk-` node, adds no `interlocks` edge, and moves no `real_or_fitted` tag. The count is computed **only** from the `ilk-` `real_or_fitted` tags (`compute_independent_parameter_count`, per `interlock-register.md:267`), so a note that mints nothing cannot move it. This is the same *mints-nothing / touches-nothing* shape the register already uses for the Calibration-Constant Criteria view (`:94-100`) and the yield consumer-map (`:102-117`) — the note was placed adjacent to those two, deliberately, so the pattern reads as one.
- **Two explicit prohibitions written into the register:** (i) do **not** book `K = 2G` as a fourth calibration parameter — it is not a dimensionful constant the substrate is fed; (ii) do **not** fold it into G's row — that would collapse a FORM import into a VALUE import and mis-state `ilk-gravmb`'s `mixed` grounding, which the leaf's own *"Accuracy is load-bearing"* banner (`form-deriving-value-importing.md:77-81`) already guards (*"**G is `mixed`, NEVER a pure echo**"*).

### The routed half — OPEN RESEARCH ITEM, recorded not attempted

- **Grant's aspiration, same sentence `[sic]`: *"I think we should at some point find it's a forced form"*.** Recorded as an **OPEN research item** at both sites. **Routed, NOT attempted** — no derivation is asserted, sketched, or graded anywhere in this branch.
- **Why it is the FORM-deriving pattern's completion for this row.** The meta-finding is *AVE forces FORMS, imports VALUES* — and `K = 2G` is **the one row where even the FORM is imported** (`form-deriving-value-importing.md:87`, the row's own "What is the chord (FORM)" cell claims only *"the substrate forces the form of the elastic response `K/G = f(ρ)`"*, i.e. the functional shape, while the **lock** `K = 2G` itself is the import). Forcing it would move the row from *import-of-a-form* to *derivation-of-a-form* — **a strictly different move from flipping a VALUE** (α `fitted→real`; G via Chain B′), and it is why this row is the pattern's completion rather than another instance of it.
- **The named attack point, cited rather than invented.** PR #261's record leaves **exactly one** open physics item. [`program-arc-map.md:118`](../../manuscript/ave-kb/common/program-arc-map.md), verified verbatim at that line: ***"*Closed:* K=2G-as-derived. *Opened:* eigenmode-existence as the only remaining open physics."*** The corresponding un-fired test is `clm-satnec`'s **static-existence test** ([`saturation-rim-inversion.md:55`](../../manuscript/ave-kb/common/saturation-rim-inversion.md): impose the `(2,3)` winding as a boundary condition, relax the lattice, ask whether the relaxed core rails `S → 0`), which the vocabulary register **already** names *"the K=2G eigenmode-existence open item"* ([`vocabulary-register.md:1119`](../../manuscript/ave-kb/common/vocabulary-register.md)). All three cites read and confirmed at this tip.
- **Scope guard, written into both leaves so the item cannot be over-read.** Forcing `K = 2G` **moves no calibration count by itself** — it flips no `real_or_fitted` tag. What it *would* do: (i) remove the GR-import that **Chain B′ currently routes through**, and (ii) lift the **Axiom-4 yield-anchor** row's inherited import (`arc* = 4ρ/(4ρ+1)·ℓ_node` with `ρ = 2 ⟺ K = 2G`, `form-deriving-value-importing.md:88`).
- **★ The one closed route is named so this is not read as re-opening a refutation.** The 2026-07-02 elastic-moduli arc (PRs [#459](https://github.com/ave-veritas-et-enodatio/AVE-Core/pull/459)/[#460](https://github.com/ave-veritas-et-enodatio/AVE-Core/pull/460)) tested exactly this and **could not** force it: `z=4` fixes only the form `K/G = f(ρ)`, `ρ` inherits from the imported value, and inextensibility (`ρ≫1`) is affirmatively `K=2G`-**forbidden** (`interlock-register.md:224`). That is a **standing negative on one named path**. Both leaves carry the corpus's own **closed ≠ exhausted** (Grant-ratified) qualifier from that same entry, so the aspiration is **live**, not a re-opened refutation.

## RULING 3 — GW-memory + BH-info, bundled PRODUCT declaration

**Ruling `[sic]`: *"3. follow your rec, there's always a cost when transferring energy between regimes/states/channels right? seems like a theorem or law territory"*.** Commit **`77d1c57e`** (KB half only). **KB-FIRST discipline: the `.tex` site rides the held ringdown wave, so the ruling is RECORDED now and the tex edit is STAGED, not fired.**

### (a) LANDED — the BH-information FLAG's declaration half

- **Site content-located, not line-trusted.** [`manuscript/ave-kb/vol3/cosmology/ch04-generative-cosmology/black-holes-impedance-mismatch.md`](../../manuscript/ave-kb/vol3/cosmology/ch04-generative-cosmology/black-holes-impedance-mismatch.md) — the 🔴 FLAG block is at **`:24-26`** at `origin/main` exactly as the dispatch stated (located by the string *"recorded + routed, NOT adjudicated"*; **dispatch cite VERIFIED, not corrected**).
- **THE DECLARATION: PRODUCT.** The retained quantity the FLAG names — the **linking-number invariant** of the knot / the **no-hair $M$–$Q$–$J$** exterior — is declared a **lossless latched residual**, under the discipline at `common/retention-transition-split.md:51` (read verbatim at that line: *"Any load-bearing use of **remanence / irreversible / plastic / latch / dissipates / frozen / erased** must declare WHICH moment it refers to: PRODUCT (product-persistence) or TRANSITION (transition-arrow)."*). **No maintenance resistor** — `:15` (*"Under canon this is **LOSSLESS** and needs **no maintenance resistor**"*) and the PRODUCT row of the regime table at `:57` (`requires_R` = **no**, licensed source *"topology (winding integer) or the `$\Gamma=-1$` reactive wall"*). Consistency-class read, never an emergence chord.
- **The consequence recorded for the body's two undeclared TRANSITION-register clauses** — `:17` *"permanently **erased**"* and `:20` *"enforcing **information loss**"*. Each must **either (a)** be re-scoped to the PRODUCT reading (a lossless latch is not an erasure), **or (b)** carry a **counting-sourced** TRANSITION arrow — mode-spread with reconvergence ≈ 0, or the energy-conserving click (`:33-34`) — and **never a valve**. Tier-1 canon quoted and independently verified at its own line: `research/2026-07-13_f6-tier1-two-reservoir-ledger_CHARTER.md:256` reads *"the arrow comes from mode-count or a click, never a valve"*.
- **★ Arm (b) is explicitly recorded as AVAILABLE, not foreclosed — this is the part a careless read would get backwards.** **Regime-IV rupture is one of the corpus's three RULED genuine loss channels** (`common/substrate-native-terminology.md:33`, verified verbatim: *"the corpus's genuine **loss/irreversibility channels reduce from four to THREE**: (1) radiative port, (2) boundary-Joule extraction, (3) Regime-IV rupture"*), and the BH interior **is** Regime IV (`vol3/claim-quality.md:121`). So the leaf is *permitted* to keep an arrow. What the ruling forbids is taking it **for free**: keep *"erased"* and you owe the **counting** source, not a friction.
- **⚑ RADIUS CAVEAT on arm (b) (added 2026-08-03, review finding 6) — the arm is available, but NOT at the radius the leaf names.** Both TRANSITION clauses locate the event at **the horizon** (`:17` *"**crossing the event horizon** destroys the structural canvas"*; `:20` *"violated **at the event horizon**"*). The **same line** cited above for *"the BH interior is Regime IV"* says the rupture is deeper — `vol3/claim-quality.md:121`, verified verbatim: *"The event horizon at $r_s = 2GM/c^2$ marks the **EM-transverse** saturation limit …; the **shear/bulk** rupture boundary is deeper, at $r_{sat} = 7GM/c^2 = 3.5\,r_s$ …; the interior beyond $r_{sat}$ is in **Regime IV** (ruptured topology)."* At $r_s$ only the **EM-transverse** channel saturates, and under Symmetric Gravity that channel is **matched** ($\Gamma_{EM}=0$, light transparent) — which is this leaf's own retired-title reading. **The topological canvas is intact at $r_s$ and ruptures at $r_{sat} = 3.5\,r_s$.** So a leaf taking arm (b) must **also move the radius**; *"erased at the event horizon"* would owe a counting source where the corpus says no rupture has occurred. **Landed on the leaf as an additive caveat; no body text edited, F5 routing unchanged.**
- **What the ruling does NOT do, stated on the leaf:** the **unitarity question itself stays OPEN**. The declaration **constrains the FORM** any answer may take; it picks no answer. Retention and destruction both stay live; what is foreclosed is a **third** option — sourcing the destruction from a valve / maintenance resistor. The FLAG's **F5 routing** to the generative-cosmology / BH-interior lane (`research/2026-07-17_regime-iv-dissipation-audit.md:127`) **STANDS**.
- **Rule 12:** both FLAG paragraphs are preserved **byte-unedited**; the resolution is a dated additive block beneath them. No body prose above the FLAG is touched. `clm-ir8h78` and `clm-c6k5om` untouched — no re-grade, no retraction.

### (b) STAGED, NOT FIRED — the GW-memory site (fires with the gated ch15 wave)

- **Site + status.** `manuscript/vol_3_macroscopic/chapters/15_black_hole_orbital_resonance.tex`, §*"Gravitational Wave Memory as Residual Strain"*. Content-located: the ruled sentence is at **`:322`** at `origin/main` — **dispatch cite VERIFIED**. **HELD.** Nothing in this branch touches that file (`git diff --name-only origin/main...HEAD` does not contain it — confirmed in the battery below).
- **The site's current text, verbatim at `:322` and `:328`:**

  > After a gravitational wave passes, the local metric retains a permanent offset---so-called ``memory'' or residual strain. In the AVE dielectric framework, this is the \textbf{permanent plastic deformation} of the LC lattice after being driven past its linear elastic limit by the passing wave. The residual memory strain scales as:
  >
  > […equation…]
  >
  > This is directly analogous to a metal permanently deforming after exceeding its yield stress $\sigma_Y$. The dimensionless yield strain of the vacuum lattice $h_{yield} = \sqrt{\alpha}$ emerges from the same Axiom 4 saturation physics that defines $V_{yield}$.

- **TWO INDEPENDENT DEFECTS, both ruled, both staged.**
  1. **The which-moment defect (PRODUCT).** *"permanent **plastic** deformation"* — `plastic` is on `retention-transition-split.md:11`'s own declaration-required word list, used here with **no declaration**, and in its dissipative sense (metal plasticity) it is an **Ax3 loss leak**. Ruled wording: **retained residual offset / latched strain; "plastic" struck.**
  2. **The regime-broken premise (independent of #1).** *"after being **driven past its linear elastic limit**"* is **false by ~28 decades**. Verified numerically against the corpus's own numbers: `vol3/gravity/ch08-gravitational-waves/ligo-gw-saturation-ratio.md:15` gives $V_{GW}/V_{\text{snap}} \approx \mathbf{1.4\times10^{-28}}$, and `vol3/claim-quality.md:76` reads *"All observed GW signals are **far in Regime I** (deeply linear)"* with the per-class table at `einstein-field-equation.md:92-95` (GW150914 $\sim10^{-28}$, GW170817 $\sim10^{-29}$, pulsar timing $\sim10^{-22}$; **all Regime I**). Nothing observed is anywhere near yield.

- 🔴 **RETRACTED 2026-08-03 (review finding 1) — "THE EQUATION SURVIVES THE PREMISE STRIKE" is WRONG. Body preserved per Rule 12; do not build on it.** The retracted claim read verbatim:

  > ***"★ THE EQUATION SURVIVES THE PREMISE STRIKE — and this is why the strike is a repair, not a deletion.** $\Delta h_{memory} = h_{peak}(h_{peak}/h_{yield})^2$ is exactly the shape of the **leading cubic nonlinear correction of the Axiom-4 kernel expanded about zero** ($\sqrt{1-x^2} \approx 1 - x^2/2$, first correction $O(x^2)$ on a linear response). That is a **Regime-I sub-yield** statement, fully consistent with $V_{GW}/V_{snap} \sim 10^{-28}$. It is **only the post-yield plasticity narrative** that dies, not the scaling law. The staged text keeps the equation byte-unchanged."*

  The review killed it **three independent ways**. Any one of the three is sufficient; all three are recorded so no single rescue re-opens it.

### The three strikes (review finding 1 — verbatim receipts)

**STRIKE (a) — PARITY. An even kernel cannot rectify.** $S(A) = \sqrt{1-A^2}$ is **even** in $A$. The modulated response $\sigma(h) = S(h/h_y)\,h$ is therefore **odd** in $h$. An odd nonlinearity driven by a symmetric wave generates only **odd harmonics** and **zero DC**:
$$\cos^3\omega t = \tfrac34\cos\omega t + \tfrac14\cos 3\omega t \;\Longrightarrow\; \langle\cos^3\omega t\rangle = 0 .$$
So the cubic term produces a **third harmonic**, not an offset. **No rectification ⇒ no residual.** Memory is by definition a **DC offset** surviving the drive; the cubic term is the one thing that provably cannot supply it. *(This is the plumber-physical statement: you cannot get a DC bias out of a symmetric device driven symmetrically — you need a diode, and Axiom 3 does not have one.)*

**STRIKE (b) — SINGLE-VALUEDNESS. The kernel is anhysteretic, so nothing is retained.** [`common/engine-capability-map.md`](../../manuscript/ave-kb/common/engine-capability-map.md)**`:67`**, read verbatim at that line at this tip (bullet 3, *"Anhysteretic ↮ loop"*):

  > *"The canonical kernel $S(A)=\sqrt{1-A^2}$ is anhysteretic — zero enclosed loop area ⇒ **no remanence** (`loop-gap-electron-resonator-closure-doctrine.md:18`). Every attempt to get retention imposes a latch by hand (the [#215] IMPOSED-LATCH). The loop is the deepest open gap (R10)."*

  $\sigma$ is a **single-valued function of the instantaneous $h$**. Therefore $h \to 0 \Rightarrow \sigma \to 0$, identically, for every history. **Nothing is retained when the wave passes** — not approximately, exactly. *(Byte-note: this fragment's earlier rendering of the same quote silently dropped the inline `loop-gap-…:18` cite and added bold to "anhysteretic" and "R10" that the source does not carry. The line above is the source's own bytes.)*

**STRIKE (c) — MAGNITUDE. ~39 orders below the effect it is supposed to model.** For GW150914 ($h_{peak} = 10^{-21}$, $h_{yield} = \sqrt{\alpha} = 0.085425$):
$$\frac{h_{peak}}{h_{yield}} = 1.171\times10^{-20}, \qquad \Delta h = h_{peak}\!\left(\frac{h_{peak}}{h_{yield}}\right)^{\!2} = 1.370\times10^{-61}.$$
The GR / Christodoulou memory for the same event is $\sim 10^{-22}$. The gap is $10^{38.86}$ — **~39 orders of magnitude**. With the correct $-\tfrac12$ prefactor (below) it is $6.85\times10^{-62}$, i.e. **~39.2 orders**. A formula that is 39 decades below the phenomenon it names is not "the scaling law surviving"; it is a different quantity wearing the same symbol.

### ★ The $-\tfrac12$ prefactor — the unhedged identity the review caught

The retracted bullet wrote *"exactly the shape of"* and then quoted $\sqrt{1-x^2} \approx 1 - x^2/2$ **without carrying the $-\tfrac12$ through**. Carried through:
$$\sigma(h) = S\!\left(\tfrac{h}{h_y}\right) h \;\approx\; h\left[1 - \tfrac12\!\left(\tfrac{h}{h_y}\right)^{\!2}\right] = h \;-\; \underbrace{\tfrac12\,h\!\left(\tfrac{h}{h_y}\right)^{\!2}}_{\text{leading nonlinear term}} .$$
So the kernel's leading nonlinear term is $-\tfrac12\,h(h/h_y)^2$: it differs from the printed $\Delta h_{memory} = +\,h(h/h_y)^2$ by a factor of $-2$, and — the load-bearing part — it is **negative**, a *softening of the instantaneous response*, not an *accumulated offset*. **"Exactly the shape of" was an unhedged identity claim and is withdrawn.**

### What actually survives

**Only this: the cubic $h(h/h_y)^2$ is the SCALE of the sub-yield nonlinearity.** Concretely, the fractional size of the leading nonlinear correction to the *instantaneous* strain response of a Regime-I gravitational wave is
$$\left|\frac{\delta\sigma}{\sigma}\right| = \tfrac12\!\left(\frac{h_{peak}}{h_{yield}}\right)^{\!2} = 6.85\times10^{-41} \quad\text{(GW150914)} .$$
That is a statement about **waveform distortion in-flight**, single-valued and drive-synchronous. It is **not** a memory law, **not** a residual, and **not** a DC quantity. The symbol $\Delta h_{memory}$ must not be attached to it.

### ⚑ The DUAL-RULER defect (review finding 5) — receipt corrected here, reconciliation ROUTED

- **What was wrong.** The retracted bullet said the cubic form *"is exactly what the deeply-linear regime supplies"* and cited $V_{GW}/V_{snap} \approx 1.4\times10^{-28}$ as its receipt. That silently asserts a **quantitative link between two different yield rulers** that the corpus has never reconciled:
  - the **EMF ruler** — $V_{GW}/V_{\text{snap}} \approx 1.4\times10^{-28}$ ([`vol3/gravity/ch08-gravitational-waves/ligo-gw-saturation-ratio.md`](../../manuscript/ave-kb/vol3/gravity/ch08-gravitational-waves/ligo-gw-saturation-ratio.md)`:15`);
  - the **strain ruler** — $h/h_{yield} = 10^{-21}/\sqrt{\alpha} = 1.171\times10^{-20}$.
- **The equation-native receipt is the strain one.** $\Delta h = h(h/h_{yield})^2$ contains $h/h_{yield}$ and nothing else. **$h/h_{yield} \approx 1.2\times10^{-20}$ is the number that belongs in that sentence**; $1.4\times10^{-28}$ belongs to a different quantity. *(The premise strike itself survives either way — both rulers put every observed signal far sub-yield — so this is a receipt correction, not a re-opening of Ruling 5's or Ruling 3's strike.)*
- **★ The two rulers are not related by any power, and they disagree about WHERE yield is by $\sim\!10^8$.** Recomputed here from the corpus's own regime table ([`vol3/gravity/ch02-general-relativity/einstein-field-equation.md`](../../manuscript/ave-kb/vol3/gravity/ch02-general-relativity/einstein-field-equation.md)`:92-95`): across **all four** of its rows the $V$ column is exactly $V_{GW}/V_{snap} = 10^{-7} h$ (checked: $10^{-21}\!\to\!10^{-28}$, $10^{-22}\!\to\!10^{-29}$, $10^{-15}\!\to\!10^{-22}$, $10^{-1}\!\to\!10^{-8}$ — a linear map, ratio $1.000$ each row). So the **EMF ruler places saturation at $h = 10^{7}$**, while the **strain ruler places yield at $h = \sqrt{\alpha} = 0.0854$** — the two rulers disagree about the location of the yield point by a factor of $\mathbf{1.17\times10^{8}}$.
- **The table contradicts itself in one row, and the corpus has been reading past it.** Its own **near-merger** row is $h = 10^{-1}$, $V_{GW}/V_{snap} \sim 10^{-8}$, labelled **"I–II boundary"**. On the strain ruler $h/h_{yield} = 1.171$, i.e. **past yield** — which is what earns the "I–II boundary" label. On the EMF ruler the same row is **$10^{-8}$ of saturation**, i.e. deeply Regime I. **One row, two columns, two incompatible regime verdicts.** The regime label follows the strain ruler; the number quoted in premise arguments (including this ruling's own strike) has been the EMF one.
- **Status: PRE-EXISTING DEBT, first surfaced here. Routed, not taken.** Nothing in this fragment attempts the reconciliation — it is corpus-wide (it touches every leaf that cites either ruler to place a regime), and it needs a physics answer (what maps lattice EMF to metric strain, and which of the two — if either — is the Axiom-4 argument $A$) rather than an editorial one. Booked as routed follow-on **#8** below. **Both rulers stay quoted as-is at their own leaves; neither is edited.**

- **The R10 flag is no longer a "flag" — after strikes (a)+(b) it is the whole finding.** The earlier staged text carried the remanence gap as a *caveat beneath a surviving equation*. With the equation retracted, the R10 gap **is** the state of this section: the canonical kernel is anhysteretic **and** even-parity, so it can neither *hold* a residual (b) nor *generate* one (a). **There is no engine behind $\Delta h_{memory}$ at all** — not a weak one, none. Recording that plainly is the whole content of the rewrite below.

- **What is unchanged from the first staging, because the review confirmed both:** the **plasticity strike** (rate-independent plastic loss is a dissipation channel Axiom 3 does not have; none of the three ruled loss channels is active) and the **regime-broken-premise strike** (observed GWs are nowhere near yield). Both stand exactly as ruled. Only the *"the equation survives"* half is rewritten.

---

### 🔴 REWRITTEN STAGED TEXT (2026-08-03, review finding 1) — TWO VARIANTS, **NEITHER FIRED**, Grant picks

**Routing, explicit.** The two variants below are **not** alternative wordings of one position — they are **two different epistemic postures**, and the choice is Grant's, not this lane's:

| | **VARIANT A — conservative retraction** | **VARIANT B — forward NULL prediction** |
|---|---|---|
| what the section ends up asserting | $\Delta h_{memory}$ is **UNDERIVED**; the memory law has no engine behind it until R10 closes | AVE-as-canonized **predicts GW memory ~39 orders below GR**; a GR-level detection falsifies this sector |
| class | Rule-12 retraction, no new claim | **forward-prediction class** — a real discriminator |
| risk if wrong | none (it claims nothing) | a genuine falsifier is on the table, and it can lose |
| what it costs | the section stops predicting anything | it commits the sector to a null that LISA/PTA can test |

**Neither is fired. Both are staged verbatim below. No `clm-` is minted by either.**

#### VARIANT A — conservative retraction (LaTeX, staged)

```latex
\subsection{Gravitational Wave Memory as Residual Strain}

After a gravitational wave passes, the local metric is observed to retain an
offset---so-called ``memory'' or residual strain. This section previously read that
offset as \textbf{permanent plastic deformation} of the LC lattice after being
driven past its linear elastic limit. \textbf{Both halves of that reading are
struck}, and the scaling law they carried is \textbf{marked UNDERIVED}.

\noindent\textbf{(i) The regime premise is false.} An observed gravitational wave
does not drive the lattice past any elastic limit. For GW150914,
$h_{peak}/h_{yield} = 10^{-21}/\sqrt{\alpha} = 1.2\times10^{-20}$---\textbf{twenty
decades} below yield---and every observed source is classified \textbf{Regime~I,
deeply linear} (\kbleaf{ave-kb/vol3/gravity/ch02-general-relativity/einstein-field-equation.md},
regime table).

\noindent\textbf{(ii) The plasticity analogy is struck.} Rate-independent plastic
loss is a dissipation channel the lossless substrate (Axiom~3) does not have, and
none of the three ruled loss channels---radiative port, boundary-Joule extraction,
Regime-IV rupture---is active in a Regime-I wave passing through cold vacuum.

\noindent\textbf{(iii) The scaling law is UNDERIVED, not merely re-scoped.} The
expression $\Delta h_{memory} = h_{peak}(h_{peak}/h_{yield})^2$ has \textbf{no
engine behind it}, for three independent reasons. \emph{Parity:} the Axiom~4 kernel
$S(A)=\sqrt{1-A^2}$ is \emph{even} in $A$, so the modulated response is \emph{odd}
in $h$; an odd nonlinearity driven by a symmetric wave yields a third harmonic and
\emph{zero} DC ($\langle\cos^3\omega t\rangle = 0$), and memory is by definition a
DC offset. \emph{Single-valuedness:} the same kernel is \textbf{anhysteretic}---zero
enclosed loop area, hence no remanence
(\kbleaf{ave-kb/common/engine-capability-map.md}, \S3.3)---so $h \to 0$ returns the
response identically to zero, retaining nothing. \emph{Magnitude:} evaluated for
GW150914 the expression gives $1.4\times10^{-61}$, roughly \textbf{39 orders of
magnitude} below the GR/Christodoulou memory of $\sim10^{-22}$ for the same event.

\noindent\textbf{What does survive} is a strictly weaker, non-memory statement: the
cubic form sets the \emph{scale of the sub-yield nonlinearity}. Expanding the
kernel, the leading nonlinear term in the instantaneous response is
$-\tfrac12\,h\,(h/h_{yield})^2$---note the $-\tfrac12$, and note that it is a
\emph{softening of the in-flight waveform}, not an accumulated offset. Its
fractional size for GW150914 is $\tfrac12 (h/h_{yield})^2 = 6.9\times10^{-41}$.
That is a statement about waveform distortion during propagation. It is not a
memory law and must not carry the symbol $\Delta h_{memory}$.

\noindent\textbf{Status.} Gravitational-wave memory is \textbf{an observable this
framework does not currently derive}. Supplying it requires a genuine, non-imposed
retention mechanism---the standing \textbf{R10 remanence gap}, the deepest open gap
in the engine map. Until R10 closes there is no AVE memory law, and none is claimed
here.
```

**Companion edits in VARIANT A:** the `resultbox` equation is **removed** (a boxed result is a claim; an UNDERIVED quantity does not get one), the `:328` metal-plasticity analogy sentence is **deleted**, and the figure caption at `:337` panel (5) — *"GW memory strain as residual lattice deformation **above** $h_{yield} = \sqrt{\alpha}$"* — becomes *"GW memory strain (panel retained for the observable; the AVE scaling law for it is marked UNDERIVED, see text)"*.

#### VARIANT B — forward NULL prediction (LaTeX, staged)

```latex
\subsection{Gravitational Wave Memory: A Null Prediction}

After a gravitational wave passes, the local metric is observed to retain an
offset---so-called ``memory'' or residual strain. General Relativity predicts this
(the Christodoulou memory, $\sim10^{-22}$ for a GW150914-class event) as a
second-order effect of the wave's own energy flux. \textbf{The AVE substrate, as
canonized, predicts no memory of its own}---and that is a testable statement.

\noindent\textbf{The substrate cannot rectify.} The Axiom~4 kernel
$S(A)=\sqrt{1-A^2}$ is \emph{even} in $A$, so the modulated strain response is
\emph{odd} in $h$. An odd nonlinearity driven by a symmetric wave produces odd
harmonics and \textbf{exactly zero DC}: $\cos^3\omega t = \tfrac34\cos\omega t +
\tfrac14\cos 3\omega t$, so $\langle\cos^3\omega t\rangle = 0$. Rectification
requires a diode; a lossless, even, single-valued substrate does not have one.

\noindent\textbf{The substrate cannot retain.} The same kernel is
\textbf{anhysteretic}---zero enclosed loop area, hence no remanence
(\kbleaf{ave-kb/common/engine-capability-map.md}, \S3.3). The response is a
single-valued function of the instantaneous strain, so $h \to 0$ returns it
identically to zero for \emph{every} drive history. Nothing is held.

\noindent\textbf{The bound, if one insists on a residual.} The most generous
estimate---taking the entire leading sub-yield nonlinearity and treating it as
though it accumulated---is $\tfrac12\,h_{peak}(h_{peak}/h_{yield})^2$, which for
GW150914 ($h_{peak}=10^{-21}$, $h_{yield}=\sqrt{\alpha}=0.0854$, so
$h_{peak}/h_{yield}=1.2\times10^{-20}$) is $6.9\times10^{-62}$: about
\textbf{39 orders of magnitude} below the GR value. So both the strict prediction
(zero) and the generous bound ($\sim10^{-61}$) sit far below anything observable.

\begin{resultbox}{Forward Null Prediction --- Substrate GW Memory}
The AVE substrate contributes \textbf{no} gravitational-wave memory:
\begin{equation}
    \Delta h_{\text{memory}}^{\text{substrate}} = 0
    \quad\text{(strictly)}, \qquad
    \left|\Delta h^{\text{substrate}}\right| \lesssim
    \tfrac12 h_{peak}\!\left(\frac{h_{peak}}{h_{yield}}\right)^{2}
    \sim 10^{-61} \quad\text{(generous bound)} .
\end{equation}
\end{resultbox}

\noindent\textbf{What would falsify this.} A LISA or pulsar-timing-array detection
of gravitational-wave memory \emph{in excess of} the GR/Christodoulou prediction,
scaling as $h^3$ with a $h_{yield}=\sqrt{\alpha}$ normalisation, would falsify the
lossless-anhysteretic substrate of this framework. Conversely, a memory detection
\emph{at} the GR level is consistent with this prediction only if the GR value is
sourced by the wave's own energy flux and not by the medium---see the scope
statement below, which is the load-bearing caveat on this test.

\noindent\textbf{Scope --- the caveat this prediction lives or dies on.} This is a
null on the \emph{medium} channel: the substrate's constitutive nonlinearity
contributes no memory. It is \emph{not} a prediction that no memory is observed.
Whether AVE also inherits the second-order GR/Christodoulou memory through its
Einstein-field-equation correspondence is \textbf{OPEN} and is stated here as
unresolved: if it does, this null is silent about the observed value and the test
above is not a discriminator; if it does not, AVE predicts \emph{no} memory at all
and the existing GR expectation is already the falsifier.
```

**Companion edits in VARIANT B:** the `:328` metal-plasticity analogy sentence is **deleted** (identically to Variant A — the plasticity strike is common to both), and the figure caption at `:337` panel (5) becomes *"GW memory: the AVE substrate's null contribution ($\lesssim 10^{-61}$) against the GR expectation ($\sim 10^{-22}$)"*, which requires the panel itself to be re-plotted or dropped — **flagged, not decided here.**

#### Adjudication notes for the pick (this lane's read, not a recommendation)

- **Variant A is the honest-closure shape** (Rule 11): a pre-registered claim failed decisively, a single mechanism (an even, single-valued, lossless kernel) explains all three failures, and the branch closes. It claims nothing and cannot be wrong.
- **Variant B is the only one that buys anything**, and per the corpus's own standing position — the chord lives in **forward predictions**, not in internal consistency — a clean sector-level null with a named falsifier is worth more than a silent retraction. **But** it is load-bearing on the OPEN scope question written into its own last paragraph, and if AVE inherits Christodoulou memory through the EFE correspondence, Variant B's discriminator is **not** a discriminator. **That question is not answered here and must not be assumed either way when picking.**
- **What is common to both and therefore not at issue:** the plasticity strike, the regime-premise strike, the $-\tfrac12$ prefactor, the $h/h_{yield}=1.2\times10^{-20}$ receipt, and the deletion of the `:328` analogy.

  Companion site in **both** staged variants, **flagged**: the figure caption at `15_black_hole_orbital_resonance.tex:337` panel (5) reads *"GW memory strain as residual lattice deformation **above** $h_{yield} = \sqrt{\alpha}$"* — carrying the same regime-broken premise, and now also the retracted law. **Disclosed as beyond the dispatch's letter** (which named `:322`): striking the premise at `:322` while leaving the identical premise in the caption and in the `:328` analogy would ship an internally inconsistent section. All three move together, and **none is fired here**.

### (c) CANONIZATION-CANDIDATE — Grant's theorem instinct (routed for a walk, NOT canonized)

- **Grant, verbatim `[sic]`: *"there's always a cost when transferring energy between regimes/states/channels right? seems like a theorem or law territory"*.**
- **The candidate statement, as this lane would put it for the walk** — *proposed wording only, nothing canonized, no `def-`/`clm-` minted:*
  > **Within-SYSTEM reactive exchange is free — however many CHANNELS it crosses** (Axiom 3: a lossless substrate moves energy between $L$- and $C$-storage at zero cost, indefinitely). **An ARROW appears iff the transfer crosses the SYSTEM boundary through a counting port** — a mode-spread with reconvergence ≈ 0, or a click. The cost is not paid to a resistor; it is paid in **countability**.

  > 🔴 **WORDING CORRECTED 2026-08-03 (review finding 7) — the prior form contradicted its own worked example. Preserved per Rule 12:** ***"**Within-channel reactive exchange is free** (Axiom 3: a lossless substrate moves energy between $L$- and $C$-storage at zero cost, indefinitely). **An ARROW appears iff the transfer crosses a COUNTING boundary** — a mode-spread with reconvergence ≈ 0, or a click. The cost is not paid to a resistor; it is paid in **countability**."*** **The defect:** the candidate said *within-channel* is free and then justified it with the ideal LC tank — but $E \leftrightarrow B$ **is** a channel crossing (electric storage ↔ magnetic storage, the corpus's own two EM channels), and it is **free**. So the very example offered as the licence for the clause is a **counterexample to it**. The scope word was wrong: the free/costed carve is **system**-level, not channel-level. **Corrected: within-SYSTEM is free however many channels are crossed; the boundary that costs is the SYSTEM boundary, and only through a counting port.**
- **Why this shape and not "there is always a cost".** The literal reading would be **false in AVE and would break Axiom 3**: an ideal LC tank transfers 100% of its energy between the electric and magnetic channels every quarter cycle at zero cost, forever — that is the electron's own persistence argument (`retention-transition-split.md:25`, $Q\to\infty$). **Note this example is *itself* a channel crossing**, which is exactly why the carve had to move from *channel* to *system*. So the theorem cannot be *"transfer costs"*, and it cannot be *"channel-crossing costs"* either; it must be *"**crossing the system boundary through a counting port** costs"*. This is the **retention-transition-split's own mechanism, generalized** from the yield crossing to any regime/state/channel crossing. It is also consistent with the corpus's own **MODE-loss** row (`retention-transition-split.md:59`): redistribution across modes/channels, `requires_R` = **no**, *"system conserves"* — a channel crossing with no arrow, by the register's own table.
- **The three ruled loss channels would be its instances** (`substrate-native-terminology.md:33`): **(1) radiative port** — energy leaves into a continuum of external modes with no return path (mode-spread); **(2) boundary-Joule extraction** — a real port at the boundary, a genuine $\mathrm{Re}(Z)$, i.e. counting done by the *detector*; **(3) Regime-IV rupture** — the lattice's mode inventory itself changes (the topological canvas is destroyed), which is the sharpest counting boundary in the corpus. **Op3 would be the negative control**: mode-loss without system-loss, RULED lossless transduction (RULING 21) — a channel crossing that does **not** cross a counting boundary and correspondingly has **no** arrow.
- **Status: CANONIZATION-CANDIDATE, routed for a Grant walk. NOT canonized here, NOT minted, NOT load-bearing for the (a) declaration.** Recorded because the ruling sentence carried it, and because a generalization at law/theorem level should get the walk-the-picture-first treatment rather than being landed inside a ruling-execution branch.
- **What the walk would need to settle (the open edges this lane will not decide):** (i) is *"crosses a counting boundary"* a **definition** of the arrow or a **claim** about when arrows occur — i.e. is it a tautology or a theorem; (ii) does the near-yield fork (still **OPEN**, `retention-transition-split.md:61-67`, Grant leans reversible) sit inside or outside its scope; (iii) whether it says anything the split leaf does not already say, or is a re-statement at a higher altitude — the honest null outcome; **(iv) ★ the boundary-Joule edge, which the candidate currently papers over** (added 2026-08-03, review finding 7). Channel (2) of the three ruled loss channels is **boundary-Joule extraction**, and the corpus's own register puts it at *"`$R_{rad}\equiv Z_0$` or `$Z_{det}$` (a real port)"* with `requires_R` = **port-only** (the **SYSTEM-loss** row, `retention-transition-split.md:60`) — i.e. the energy is **paid to a genuine $\mathrm{Re}(Z)$**. The candidate's gloss of it as *"counting done by the **detector**"* is a **reframe, not an instance**: it re-describes where the resistor sits (outside the system) rather than replacing the resistor with a count. Until that is settled the candidate cannot claim all three ruled channels as instances — **it has two clean instances (radiative mode-spread, Regime-IV rupture) and one contested one.** If boundary-Joule is genuinely resistor-sourced, then *"the cost is never paid to a resistor"* is **false as stated** and must weaken to *"the cost is never paid to a resistor **inside** the system"* — which may be true but is a materially smaller claim. **Named as an open edge for the walk; not decided here.**

## RULING 5 — the incompressible premise (repair)

**Ruling `[sic]`: *"5. repair"*.** Commit **`2d390e99`**. Two files, an exact print/KB mirror pair: `manuscript/vol_2_subatomic/chapters/05_electroweak_gauge_theory.tex` **`:35`** (dispatch cite **VERIFIED**) and its byte-identical KB mirror [`manuscript/ave-kb/vol2/particle-physics/ch05-electroweak-mechanics/gauge-boson-masses.md`](../../manuscript/ave-kb/vol2/particle-physics/ch05-electroweak-mechanics/gauge-boson-masses.md)**`:34`**.

### BEFORE (verbatim, both sites, modulo `\textbf{}` ↔ `**`)

> Because the vacuum substrate is incompressible ($K = 2G$), an irrotational flow field generates no localised compression ($-\partial_t \mathbf{A}$), no transverse vorticity ($\nabla \times \mathbf{A}$), and no topological defects. It is isomorphic to performing a **Galilean or Lorentz coordinate boost** of the observer's reference frame. Gauge invariance is not violated; it is revealed to be the classical network-dynamic freedom to shift the irrotational background coordinate velocity without altering the physical transverse observables.

### The premise is false — recomputed here, not restated from the corpus

- Isotropic relation $\nu = \dfrac{3K - 2G}{2(3K + G)}$. At $K = 2G$: $\nu = \dfrac{6G - 2G}{2(6G + G)} = \dfrac{4G}{14G} = \mathbf{2/7} = 0.2857\ldots$ — matching the corpus's $\nu_{\text{Hill}} = 2/7$ (the $\nu_{\text{Hill}} \equiv 2/7$ substitution later in the same section, `05_electroweak_gauge_theory.tex:75` at this tip; `common/appendix-derived-numerology.md:22`).
- $\nu \to 1/2$ requires $3K - 2G \to 3K + G$, i.e. $G \to 0$ at finite $K$, or $K \to \infty$ at finite $G$. **No finite $K$ with finite $G$ is incompressible.** So *"the vacuum substrate is incompressible ($K = 2G$)"* is not a rounding or a loose phrase — it is the **opposite** of what $K = 2G$ says. `K = 2G` is a *finite-modulus lock*, and the corpus knows it (`vol3/gravity/ch01-gravity-yield/trace-reversal-mechanism.md:21` puts $\nu = 1/2$ at the **rigidity threshold** $p_G = 0.117$, a **different** operating point from $p^* = 8\pi\alpha = 0.1834$ where $K/G = 2$).

### ★ The premise was LOAD-BEARING, not decorative — which is why this is a repair, not a word-swap

For general $\Lambda$, $\nabla\cdot(\nabla\Lambda) = \nabla^2\Lambda \neq 0$. So the clause *"generates no localised compression"* **does not follow from Helmholtz alone** — incompressibility was exactly the premise being asked to kill it. Removing the premise therefore **removes that leg of the conclusion**. The repair drops the compression leg rather than rescuing it, and keeps only what the gauge argument actually needs.

### AFTER (the ruled replacement, landed at both sites)

> The Helmholtz decomposition is exact at *any* compressibility, and that is all this argument needs: adding $\nabla\Lambda$ changes only the irrotational component, and **the irrotational component sources no transverse observable**. The curl identity $\nabla \times \nabla\Lambda \equiv 0$ leaves the transverse vorticity $\nabla \times \mathbf{A}$ pointwise unchanged, and the loop integral $\oint \nabla\Lambda \cdot d\boldsymbol{\ell} = 0$ around any closed contour (single-valued $\Lambda$) leaves every winding and linking integer unchanged — so no topological defect is created or destroyed. It is isomorphic to performing a **Galilean or Lorentz coordinate boost** … *(tail unchanged)*.

### Chain check — the repaired argument read end to end (the ruling asked for this explicitly)

1. **Critique:** a gauge shift on a *physical* $\mathbf{A}$ would spontaneously move macroscopic mass, violating Noether. *(unchanged, `:31`/`:30`)*
2. **Helmholtz:** $\nabla\Lambda$ is purely irrotational, so it enters only the longitudinal channel. **Exact at any $\nu$ — no premise spent.**
3. **Transverse observables:** built from the solenoidal channel ($\mathbf{B} = \nabla\times\mathbf{A}$); $\nabla\times\nabla\Lambda \equiv 0$ ⇒ **pointwise unchanged.**
3′. **The electric field** (added 2026-08-03, review finding 3): $\delta\mathbf{E} = -\partial_t\nabla\Lambda$ is **not** pointwise zero — but it **is** irrotational, so the whole of it sits in the EM longitudinal channel, which by `def-l0ngdu` has **no restoring force**. A channel with no restoring force **stores no energy and exerts no force** ⇒ **no observable of any kind**, $-\partial_t\nabla\Lambda$ included.
4. **Topological content:** loop/surface integrals of the solenoidal channel; $\oint\nabla\Lambda\cdot d\boldsymbol{\ell} = 0$ for single-valued $\Lambda$ ⇒ **no defect created or destroyed.**
5. **Conclusion:** the shift is a coordinate re-labelling of the irrotational background — the boost reading — so the critique is answered.
**No step uses compressibility**, and with (3′) in place **every** observable named in the critique ($\mathbf{B}$ *and* $\mathbf{E}$) is covered.

> **🔴 CORRECTION 2026-08-03 (review finding 3; the sentence above is the repaired form, the prior one is preserved here per Rule 12).** This chain check originally ended ***"No step uses compressibility. The chain reads soundly."*** with steps (1)–(5) and **no (3′)** — i.e. it **asserted soundness while covering $\mathbf{B}$ only**. That was wrong as written. **Why the gap existed:** the clause this ruling struck was the section's *only* $\mathbf{E}$ coverage, and it was **garbled** — it called $-\partial_t\mathbf{A}$ *"localised compression"* when $-\partial_t\mathbf{A}$ **is** the electric field. Striking it removed the $\mathbf{E}$ leg outright, and $\delta\mathbf{E} = -\partial_t\nabla\Lambda \neq 0$ **pointwise**. The textbook cancellation is **unavailable in this section's variables** — there is no scalar-potential companion here to absorb $\varphi \to \varphi - \partial_t\Lambda$. **The one-step fix, landed at both sites:** promote `def-l0ngdu`'s no-restoring-force clause (`vocabulary-register.md:870`, verified verbatim at that line: *"The **EM longitudinal** $\nabla\cdot\mathbf{A}$ is **GAUGE**: the curl-only EM Lagrangian gives it no restoring force."*) from **grounding-decoration to a step of the chain**. Landed in the print body + source comment (`05_electroweak_gauge_theory.tex`) and in the KB mirror body + chain check + premise note (`gauge-boson-masses.md`). **Disclosed second-order edit:** the body paragraph's closing clause moved from *"without altering the physical **transverse** observables"* to *"without altering the physical observables — transverse or longitudinal"*, because leaving *transverse* as the paragraph's concluding scope would rhetorically re-narrow the very leg (3′) just closed.

### Substrate-native grounding cited (not invented)

The corpus's **adjudicated longitudinal-sector split**, `common/vocabulary-register.md:867` (`def-l0ngdu`), verified verbatim: the mechanical dilatation $\nabla\cdot\mathbf{u}$ is **DYNAMICAL** — *"it carries a genuine bulk restoring force $\tfrac12 K(\nabla\cdot\mathbf{u})^2$ ($K = 2G$) and rides the **gapless lattice-computed P-branch**"* — while the EM longitudinal $\nabla\cdot\mathbf{A}$ is **GAUGE** — *"the curl-only EM Lagrangian gives it no restoring force"* — with the tag line *"**One word each way — $\nabla\cdot\mathbf{u}$ propagates; $\nabla\cdot\mathbf{A}$ is gauge.**"* That split is the substrate-native reason the shift is unobservable **and it needs no compressibility assumption**. Note the corpus's own `def-l0ngdu` text already carries `K = 2G` **alongside** a propagating P-branch — i.e. the corpus elsewhere treats $K = 2G$ as compressible, which is what made the `:35` premise an isolated defect rather than a corpus-wide belief.

### ⚑ FLAGGED, NOT FIXED (surfaced on the KB leaf, outside this ruling's scope)

The paragraph still says $\nabla\Lambda$ is added *"to the **mass flow**"*, reading $\mathbf{A}$ as the mechanical momentum field. The corpus's SOLID adjudication is that $\mathbf{u}$ and $\mathbf{A}$ are **COUNTERPART SECTOR VARIABLES — isomorphic structure, NOT one field** (`common/vocabulary-register.md:882`, `def-uatk1s`, SOLID 2026-07-21), differing precisely in constitutive stencil on the longitudinal channel. Whether that wording needs its own correction is a **separate question, routed** — surfaced rather than absorbed into this repair.

### Two-method mirror sweep — and two sites left deliberately unedited

Method 1 `grep -rn "incompressible\|Incompressible" manuscript/`; method 2 `git grep -in "incompress" -- manuscript/ src/`. **Both returned the same set.**
- **Exactly ONE exact mirror of the ruled sentence exists** — `gauge-boson-masses.md:34` — and it is repaired here.
- **TWO sites carry a DIFFERENT sentence with the same false premise, FLAGGED not edited** (outside the ruling's named scope): `manuscript/ave-kb/vol3/gravity/ch03-macroscopic-relativity/cauchy-implosion-resolution.md:15` and its print mirror `manuscript/vol_3_macroscopic/chapters/03_macroscopic_relativity.tex:164` — *"This positive bulk resistance guarantees that the spatial substrate is **incompressible** and thermodynamically stable against gravitational collapse."* Same defect (a finite $K$ is not incompressibility), different sentence, different chapter, and the *"stable against collapse"* conclusion may well survive on a finite-$K$ premise. **Routed as a follow-on; not silently swept in.**
- **NOT defects, checked and cleared so the flag is not over-broad:** the hollow-vortex *"incompressible melted-vacuum EOS floor"* sites (`vol2/claim-quality.md:1554,1557`, `hollow-vortex-binding.md:46,51-52`, `vol_2_subatomic/chapters/01_topological_matter.tex:152`) are **Regime-IV melted-state** statements about the *ruptured* medium's EOS, not cold-lattice $K = 2G$ statements. Different regime, different object, correct as written.

### Scope

**Premise-only.** Conclusion, boost reading, and every downstream result — $(m_W/m_Z)^2 = 1/(1+\nu) = 7/9$, $m_W/m_Z = \sqrt7/3$, $\sin^2\theta_W = 2/9$ — are **unchanged** (recomputed here: $1/(1+2/7) = 7/9$; $1 - 7/9 = 2/9$ ✓). `clm-5zuo7g` and `clm-q8un7j` untouched. **Rule-12 shape per Grant's standing register:** git carries the trail (struck sentence in the diff and in a source comment); the in-doc text is a compact current-status premise note, not a preservation banner — the `.tex` carries the condensed note, the KB leaf the explanation.

## RULING 6 — neon 585–703 nm (demote)

**Ruling `[sic]`: *"6. demote"*.** Commit **`1faee721`**. Two files, an exact print/KB mirror pair.

### ★ Receipt correction — the dispatch's line cite was RIGHT and the upstream fragment's was STALE

- The reconciliation fragment [`2026-08-02-mr-vol6-crosswires`](2026-08-02-mr-vol6-crosswires.md) item **(b)** and the board row it came from (`_orchestration/2026-08-02_manuscript-reconciliation-board.md:509`) both cite the print at **`12_neon.tex:48`**. At `origin/main` the sentence is at **`12_neon.tex:65`**. **The print moved `:48 → :65`; content unchanged.**
- **Two-method located** (`grep -rn "585" manuscript/` intersected with neon context; `git grep`): both methods returned **exactly the same two sites** — `manuscript/vol_6_periodic_table/chapters/12_neon.tex:65` and `manuscript/ave-kb/vol6/period-2/neon/topological-area.md:12`. **No third site anywhere in the corpus.** The correction is recorded on the KB leaf itself, not only here.

### BEFORE (verbatim, both sites)

> When subjected to an external electric field (as in a neon discharge tube), the high-$Q$ internal resonance stores the injected energy with extreme efficiency, then re-radiates it as narrow-band photon solitons at the characteristic $585$--$703$ nm wavelengths. The famous orange-red glow of neon signage is a direct emission signature of the Triangular Bipyramid's resonant frequency response: the photon energies correspond precisely to the standing-wave modes of the $81d$ inter-alpha cavity.

**Two register violations:** *"**characteristic** … wavelengths"* presents **observed** lines as an **output**; *"correspond **precisely**"* asserts a **computed quantitative match**. **Neither is computed** — there is no calculation anywhere in the corpus taking the $81d$ inter-alpha cavity to $585$–$703$ nm (checked: `git grep` for the band endpoints over `src/` and `research/` returns **no** driver, result-doc or JSON that computes a wavelength for this cavity — the only `585`/`703` hits in those trees are unrelated numerals).

### AFTER (demoted to the structural/interpretive register, both sites)

> When subjected to an external electric field (as in a neon discharge tube), the high-$Q$ internal resonance stores the injected energy efficiently and re-radiates it as narrow-band, rather than broadband, emission. Neon's *observed* discharge spectrum — the familiar orange-red signage glow — lies in the $585$--$703$ nm band; those wavelengths are quoted here as **measured values the picture is describing, not as an output of it**. What this leaf offers is a **structural mapping**: a closed, high-$Q$, zero-net-dipole Triangular Bipyramid is the kind of resonator whose response is narrow-band, and the discharge emission is read as that resonant response. **No line position is predicted** — the standing-wave modes of the $81d$ inter-alpha cavity are not computed against the observed lines anywhere in this framework. Read the correspondence as interpretive, not quantitative.

### The governing claim card, as ruled

`manuscript/ave-kb/vol6/claim-quality.md:662` (`clm-y7uvdc`), verified verbatim at that line: *"**Does NOT claim** a quantitative reproduction of multi-electron ionization energies, fine-structure splittings, or **spectroscopic line positions** from the soliton-packing picture alone."* A leaf may not assert what its governing register non-claims; the register wins and the print is demoted to match. **Nothing is retracted at the claim level** — the demote brings the prose *into* the band the card already declared.

### ★ CARD-SCOPE OBSERVATION — surfaced, not resolved (the dispatch's cite corrects the board's, and the gap is real)

- The board row and fragment (b) cite **`clm-f8k2um`** at `vol6/claim-quality.md:566`. That card **is** this leaf's governing claim by frontmatter (`topological-area.md` frontmatter: `claims: [clm-f8k2um]`), and its **solidity is 0.30** (*"do not build on, rework needed"*) — **dispatch cite VERIFIED**.
- **But its non-claim list at `:566` does not name spectra**: *"Does NOT claim quantitative predictions of **bond enthalpies, electronegativity scales** (Pauling / Mulliken), **reaction kinetics, or material constants** from the topology alone."* The **spectroscopic** non-claim lives on the **sibling** card `clm-y7uvdc` (the *Orbital Knot Topology* leaves), which is the card the ruling names — **correctly**, because it is the only one that actually non-claims line positions.
- **Both cards point the same way**, so the demote is not in doubt. **But the "Topological Area" card carrying no spectral non-claim is the actual gap the sweep exposed** — a per-element leaf under `clm-f8k2um` can currently assert spectra without contradicting its own card. **Flagged for the auditor lane. NO card is edited here** — no re-grade, no non-claim added, no solidity move, no `strengthen-by` touched.

> **🔴 CORRECTION 2026-08-03 (review finding 2) — the demote shipped a print/mirror MISMATCH, now fixed.** The demoted print sentence at `12_neon.tex:65` read ***"…and this leaf's governing claim entry explicitly non-claims spectroscopic line positions (`clm-y7uvdc`)"***. **Two defects.** (i) **Wrong card as governing.** This section's governing claim by frontmatter is **`clm-f8k2um`** (`topological-area.md` frontmatter `claims: [clm-f8k2um]`, verified); the spectroscopic non-claim is on the **sibling** card `clm-y7uvdc`. The KB mirror at `topological-area.md:18` **already said this correctly** — so the print contradicted its own mirror, which is precisely the failure the mirror pair exists to prevent. (ii) **Register leak:** *"leaf"* is **KB vocabulary appearing in print**; print says *section* / *card*. **Fix (one clause, `.tex` only):** the non-claim is attributed to the sibling card, this section's own card is named with the gap flagged, and *leaf* → *section*/*card*. **No claim card is edited** — the card-scope gap stays flagged for the claim register, unchanged. A print/mirror sync note is added to `topological-area.md:18` so the correction is visible from the KB side too.

### Scope

**Prose register only.** The $81d$ Triangular-Bipyramid geometry, the inertness account in the preceding paragraph, the $R = 81.181d$ figure caption, and every number elsewhere in either file are **unchanged**. Rule-12 shape as in Ruling 5: git carries the trail (struck text in the diff and in a source comment); the KB leaf carries the explanation, the `.tex` a condensed comment.

## Battery — REPAIR TIP (2026-08-03, review findings 1–9 in)

Re-run in full after the repair commits; **not** carried from the pre-repair run below.

- **`make verify` exit 0** — run after **each** repair commit (5 runs). Final: `[Verify] ALL PHYSICS PROTOCOLS PASSED.`
- **`make verify-md-links` gating 0** — `gating errors: 0  warn-only: 207  broken inter: 42` (inter-repo mode: warn). **The `origin/main` baseline was re-run directly in a clean worktree rather than inherited** and returns the **identical** `0 / 207 / 42`, so the repair introduces no new warn either. **`kbleaf` cites: `origin/main` 1211 → pre-repair tip 1213 → repair tip 1214; gating: 0, waived: 1 throughout** — the one cite the repair adds (`\kbleaf{ave-kb/common/vocabulary-register.md}` in the electroweak body, step 3′) **resolves**.
- **`make refresh-kb-metadata` idempotent** — two consecutive runs, `Wrote 0 file(s) … (6 unchanged)` both times, no working-tree delta from either. **`.index/` and `src/` byte-untouched at the repair tip** (`git diff --name-only origin/main...HEAD -- manuscript/ave-kb/.index src` returns **empty**).
- **`verify-docket-keys`** — **118 entries / 116 unique keys**, no new duplicate keys, grandfathered numeric dups `22`/`32` unchanged. Still exactly **one** minted key. Sibling-slug cross-check re-enumerated (see the branch-overlap section).
- **Pure-corpus scan, two methods, over the full branch diff *plus* the working tree** — **0 hits** on both (case-insensitive `grep -E` over the combined diff; independent Python substring scan over the same text across a wider pattern set). 
- **Byte-verification of every load-bearing quote, programmatic (12/12 PASS).** Each embedded quote was compared as an exact substring against the *source line it cites*, at this tip: `engine-capability-map.md:67`, `vocabulary-register.md:870`, `vol3/claim-quality.md:121`, `retention-transition-split.md:57` / `:59` / `:60`, `substrate-native-terminology.md:33`, `src/ave/core/constants.py:650`, `ligo-gw-saturation-ratio.md:15`, and the three staged ch15 sources `15_black_hole_orbital_resonance.tex:322` / `:328` / `:337`. **Two emphasis-drift disclosures** (quotes are otherwise byte-exact): this fragment renders the `:67` quote with the source's own bold, having previously added bold to *"anhysteretic"*/*"R10"* and dropped the inline `loop-gap-…:18` cite — **now corrected to the source's bytes**; and the `:337` panel-(5) caption is quoted with **`above`** bolded for emphasis, which the source does not bold — retained deliberately (it marks the offending word) and **disclosed here** rather than left silent.
- **Untouched-region check on all five edited canon files** — line-level `difflib` opcodes against the audited tip `bff36e15`: `05_electroweak_gauge_theory.tex` 175/177 lines untouched (2 hunks, both at the named targets `:35`, `:43`); `gauge-boson-masses.md` 71/75 (4 hunks, `:34`/`:42`/`:44`/`:46`); `12_neon.tex` 114/116 (2 hunks, `:65`, `:74`); `topological-area.md` 35/36 (1 hunk, `:18`); `black-holes-impedance-mismatch.md` **42/42 = 100%** (2 pure **inserts**, zero replacements — the leaf's body and its 🔴 FLAG are byte-untouched, Rule 12 intact).
- **Numeric receipts recomputed, not quoted** — $h_{yield}=\sqrt{\alpha}=0.08542454$; $h/h_{yield}=1.1706\times10^{-20}$; $h(h/h_y)^2 = 1.3704\times10^{-61}$; $\tfrac12 h(h/h_y)^2 = 6.8518\times10^{-62}$; $\tfrac12(h/h_y)^2 = 6.8518\times10^{-41}$; $\log_{10}(10^{-22}/1.37\times10^{-61}) = 38.86$; regime-table $V$ column $= 10^{-7}h$ exactly on all four rows; ruler disagreement $10^{7}/\sqrt{\alpha} = 1.1706\times10^{8}$.
- **Zero id churn at the repair tip** — no `clm-`/`def-`/`exp-`/`sup-`/`ilk-` minted, retired or re-pointed; no `confidence` / `derivation_solidity` / `solidity` / `build_status` / `status` / `real_or_fitted` field moves; `expected-independent-count: 3` byte-unchanged. **`clm-ir8h78`, `clm-c6k5om`, `clm-5zuo7g`, `clm-q8un7j`, `clm-f8k2um`, `clm-y7uvdc` all untouched** — no re-grade, no non-claim added, no `strengthen-by` touched.

## Battery (pre-repair run — at the four-rulings tip `bff36e15`)

- **`make verify` exit 0** — run after **each** ruling's edits, not once at the end (4 runs + a final tip run). Final: `[Verify] ALL PHYSICS PROTOCOLS PASSED.`
- **`make verify-md-links` gating 0** — `gating errors: 0  warn-only: 207  broken inter: 42` (inter-repo mode: warn; both numbers unchanged from `origin/main`, so this branch introduces no new warn either). **`kbleaf` cites: 1211 → 1213, gating 0** — the two new `\kbleaf{}`/leaf cites this branch adds (Ruling 5's `ave-kb/common/vocabulary-register.md`, Ruling 6's `ave-kb/vol6/claim-quality.md`) both **resolve**.
- **`make refresh-kb-metadata` idempotent** — two consecutive runs, 0 files written, clean tree after. **`.index/` byte-unchanged** (no `clm-`/`def-`/`ilk-` node body, frontmatter `claims:`/`no-claim:`, quality block or `strengthen-by` item was touched anywhere in the diff).
- **`verify-docket-keys`** — **118 entries / 116 unique keys** (117/115 before this fragment, so the one key this branch mints is unique), **no new duplicate keys**; grandfathered numeric dups `22`/`32` unchanged. This branch mints **one** key: `2026-08-03-rulings-mr-batch`. Cross-checked against the sibling branches that also write into `_orchestration/docket-entries/` — all different slugs. **Re-enumerated at the repair tip (2026-08-03, review finding 9), now SEVEN lanes / EIGHT slugs**: `2026-08-03-imax-mechanical` *(new)*, `2026-08-03-mr-handoff-mechanical`, `2026-08-03-mr-fragment-cite-repins-correction`, `2026-08-03-oort-walkback-propagation` *(new)*, `2026-08-03-petermann-amendments`, `2026-08-03-wall-taxonomy`, `2026-08-03-coldq-v2p2-root`, `2026-08-03-coldq-v2p4-root`. **No collision.** *(The prior receipt said "five sibling branches" and then listed six slugs — an internal miscount, corrected here along with the two new lanes.)*
- **Pure-corpus scan** over the full branch diff **plus** this fragment: **0 hits** (two methods: case-insensitive `grep -E` over `git diff origin/main...HEAD` piped with the fragment, and an independent Python scan of the same text).
- **Zero id churn** — no `clm-`/`def-`/`exp-`/`sup-`/`ilk-` minted, retired or re-pointed; **no `confidence` / `derivation_solidity` / `solidity` / `build_status` / `status` / `real_or_fitted` field moves anywhere**; `expected-independent-count: 3` byte-unchanged; **`src/` byte-untouched** (no `src/` path appears in `git diff --name-only`).

### Branch overlap — ZERO file overlap with every live sibling lane

Verified by intersecting `git diff --name-only origin/main...<branch>` per lane after a fresh `git fetch origin --prune`, **enumerated rather than taken from the dispatch** (the dispatch named one lane; a full enumeration found eleven branches ahead of `origin/main`).

> **⚑ RE-VERIFIED 2026-08-03 at the repair tip (review finding 9) — the count is now THIRTEEN; the zero-overlap conclusion is UNCHANGED and re-computed, not carried.** The 11-row table below was correct when written and is **stale by two lanes**: `docs/imax-mechanical-0803` (`99994c97`, 6 files) and `docs/oort-walkback-propagation` (`6623d051`, 11 files) have since appeared, and `kb/wall-taxonomy` has moved its tip `2a00df1a → b5b41fe5` (3 → 4 files). **All three are included in the re-run below.** Method: fresh `git fetch origin --prune`, then `comm -12` of the sorted `git diff --name-only origin/main...<branch>` file lists against this branch's — **not** a re-read of the prior table. **Result: 13 lanes, 0 overlapping files, every lane.** *(Recording the delta rather than silently overwriting the table: a branch-overlap receipt that gets edited in place loses the fact that it was ever wrong.)*

| lane | tip | files | common with this branch |
|---|---|---|---|
| `analysis/2026-06-06-open-short-relabel` | `cc63c420` | 2 | **0** |
| `analysis/moving-front-freezein` | `f647f58b` | 5 | **0** |
| `analysis/stage4-a1-eos-scope` | `205d6e6b` | 1 | **0** |
| **`docs/imax-mechanical-0803`** *(new)* | `99994c97` | 6 | **0** |
| `docs/mr-addenda-0803` | `6d5e0ddc` | 10 | **0** |
| `docs/mr-board-corrections-0803` | `eb914bd1` | 1 | **0** |
| `docs/mr-epic-closeout` | `745b5951` | 1 | **0** |
| `docs/mr-handoff-mechanical-0803` | `ae96ce22` | 20 | **0** |
| **`docs/oort-walkback-propagation`** *(new)* | `6623d051` | 11 | **0** |
| `kb/petermann-artifact-record` | `b8f757b9` | 7 | **0** |
| `kb/wall-taxonomy` | `b5b41fe5` *(was `2a00df1a`)* | 4 | **0** |
| `research/coldq-pole-v2p2` | `53144b5c` | 7 | **0** |
| `research/coldq-pole-v2p3` | `c65c3d7d` | 8 | **0** |

*(The 11-row form this table replaced named the same lanes minus the two new ones, with `kb/wall-taxonomy` at its older tip. Superseded, not deleted — the delta is stated above.)*

- **★ The named collision lane checked explicitly, file by file.** `docs/mr-handoff-mechanical-0803` owns the mechanical batch (k_HB, Li/B, ρ_bulk, Si-28 comment, varactor, boron, magnesium). Its **Vol-6 print** files are `02_chemistry.tex`, `07_boron.tex`, `14_magnesium.tex` — **not** `12_neon.tex`. Its **Vol-6 KB** file is `vol6/framework/chemistry-translation/quantum-vs-topological-shells.md` — **not** `vol6/period-2/neon/topological-area.md`. Its **Vol-2** file is `vol2/appendices/app-c-derivations/index.md` — **not** `vol2/particle-physics/ch05-electroweak-mechanics/gauge-boson-masses.md`, and it touches no `vol_2_subatomic/chapters/*.tex`. It writes **two** docket fragments, both under different slugs. **Confirmed disjoint at its live tip `ae96ce22`** (it was `0 commits ahead` with only working-tree modifications when this lane started and has since pushed 8 commits — **re-read at the new tip rather than carrying the stale receipt**).
- **★ What zero FILE overlap does not cover.** Ruling 5 flags `manuscript/vol_3_macroscopic/chapters/03_macroscopic_relativity.tex:164` + `cauchy-implosion-resolution.md:15` as carrying the same false premise in a different sentence; Ruling 3's GW-memory edit is staged against `manuscript/vol_3_macroscopic/chapters/15_black_hole_orbital_resonance.tex`. **None of those three files is edited by this branch**, but any lane that opens the Vol-3 print should read this fragment first.

### This branch's files (8)

`_orchestration/docket-entries/2026-08-03-rulings-mr-batch.md` · `manuscript/ave-kb/common/interlock-register.md` · `manuscript/ave-kb/common/form-deriving-value-importing.md` · `manuscript/ave-kb/vol3/cosmology/ch04-generative-cosmology/black-holes-impedance-mismatch.md` · `manuscript/ave-kb/vol2/particle-physics/ch05-electroweak-mechanics/gauge-boson-masses.md` · `manuscript/vol_2_subatomic/chapters/05_electroweak_gauge_theory.tex` · `manuscript/ave-kb/vol6/period-2/neon/topological-area.md` · `manuscript/vol_6_periodic_table/chapters/12_neon.tex`

### Routed follow-ons opened by this branch (none taken here)

1. **Derive `K = 2G` as substrate-forced** — Grant's routed aspiration; attack point = the eigenmode-existence open item (`program-arc-map.md:118` / `clm-satnec`). *(Ruling 1)*
2. **Canonization walk** — Grant's *"cost when transferring energy between regimes/states/channels"* theorem instinct; candidate wording, the three ruled loss channels as instances, and the three open edges are drafted in §Ruling 3(c). **Routed for a Grant walk, NOT canonized.** *(Ruling 3)*
3. **★ GRANT DECISION REQUIRED — pick VARIANT A or VARIANT B for the ch15 GW-memory section**, then fire with the gated ringdown wave. Both texts verbatim in §Ruling 3(b), together with the `:328` analogy deletion and the `:337` panel-(5) caption (which differ per variant). **This is a posture choice, not a wording choice** — A retracts, B stages a forward null with a named falsifier and a named open scope caveat. *(Ruling 3 / review finding 1)*
4. **★ PREMISE-CRITICAL — the `"mass flow"` reading at the repaired Vol-2 paragraph** vs `def-uatk1s`'s counterpart-sector-variables adjudication (`vocabulary-register.md:882`, SOLID 2026-07-21: $\mathbf{u}$ and $\mathbf{A}$ are **counterpart sector variables, NOT one field**). **Re-ranked from wording to premise-critical (review finding 4):** the repair rests on the added $\nabla\Lambda$ landing in the *EM* longitudinal channel, which has no restoring force. If it is genuinely added to the **mass flow** $\mathbf{u}$, the same `def-l0ngdu` makes that channel **dynamical** — bulk restoring force $\tfrac12 K(\nabla\cdot\mathbf{u})^2$, propagating P-branch — so the addition **is** observable and the repaired premise is **refuted**, not mis-worded. Resolution requires settling the $\mathbf{A}$-vs-$\mathbf{u}$ identification for this paragraph, not a synonym swap. *(Ruling 5 / review finding 4)*
5. **The `incompressible` premise at two Vol-3 sites** (`cauchy-implosion-resolution.md:15`, `03_macroscopic_relativity.tex:164`) — same false premise, different sentence, outside Ruling 5's named scope. *(Ruling 5)*
6. **`clm-f8k2um` carries no spectral non-claim** while governing leaves that describe spectra — auditor-lane card-scope question. *(Ruling 6)*
7. **Upstream receipt staleness** — the board row and fragment (b) cite `12_neon.tex:48`; the print sentence is the one beginning *"When subjected to an external electric field (as in a neon discharge tube)"*, which was at `:65` when this item was written and is at `:91` since 2026-08-05 — so **cite it by ANCHOR TEXT, not by `:NNN`**. Item still OPEN (the upstream board row and fragment (b) are unrepaired); owned by whichever lane next opens the board. *(Ruling 6)*
8. **★ CORPUS-WIDE — reconcile the two yield rulers.** The **EMF ruler** ($V_{GW}/V_{snap}$, saturation at $h = 10^{7}$) and the **strain ruler** ($h/h_{yield}$, yield at $h = \sqrt{\alpha} = 0.0854$) place the yield point $1.17\times10^{8}$ apart, and the regime table's own near-merger row ($h=10^{-1}$) is simultaneously *past yield* on one and $10^{-8}$ *of saturation* on the other. **Pre-existing debt, first surfaced here** (§Ruling 3(b), dual-ruler receipt); every leaf that cites either ruler to place a regime is downstream of it. **Needs a physics answer** — what maps lattice EMF to metric strain, and which (if either) is the Axiom-4 argument $A$ — not an editorial one. *(review finding 5)*
9. **Stale `src/` cite in this fragment, and the sixth instance of a standing pattern** — `constants.py:589` for `XI_MACHIAN` (§Ruling 1); the symbol is at **`:650`** at this tip (`:589` is inside the topological-packing-fraction comment block). Corrected in place. **This is the sixth `src/`-line-cite staleness caught in the corpus** — the underlying debt is that KB/docket prose pins `src/` line numbers that refactors move, with no check binding them. **Routed as its own infrastructure question** (symbol-anchored cites, or a `src`-cite verifier in `make verify`), not taken here. *(review finding 8)*
