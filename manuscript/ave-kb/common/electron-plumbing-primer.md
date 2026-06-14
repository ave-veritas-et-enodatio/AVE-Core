[↑ Common Resources](index.md)

<!-- kb-frontmatter
kind: leaf
no-claim: self-scoped pedagogical primer — a picture-first re-exposition of the EE/plumber intuition for the substrate, building the picture from the reader's "a wire is a pipe for electrons" prior. Every physics beat is a re-exposition of an already-canonical leaf with a "→ Primary:" pointer; makes no new quantitative or structural claim of its own. Sister to trampoline-analogy-primer.md.
-->

# The Electron-Plumbing Primer: Wires, Shocks, and the Path of Least Resistance

**Sister primer.** [`trampoline-analogy-primer.md`](trampoline-analogy-primer.md) rewrites the reader's **GR-pop-sci** prior (bowling ball on a rubber sheet) into the substrate picture. **This** primer rewrites the reader's **EE / plumber** prior — *"a wire is a pipe electrons flow down"* — into the same substrate picture. Two different starting intuitions, one substrate. Use whichever door the reader walks in through.

This primer makes **no new claims**: each step is a re-exposition of an already-canonical leaf, with a `→ Primary:` pointer to where the load-bearing content actually lives. Where a beat is *standard* EE / bioelectricity (not AVE-specific), it is flagged as such. Where a beat is a forward research hypothesis (not yet canonical), it is flagged loudly.

---

## Step 0: The reader's prior — "a wire is a pipe for electrons"

The EE/plumber starting intuition: voltage is pressure, current is flow, a wire is a pipe, and current takes the path of least resistance like water flows downhill. **Most of this is right** — more right than the textbook reflex that tries to talk you out of it. The job of this primer is to keep what's right, fix the two places it's imprecise, and show that the corrected picture *is* the substrate.

---

## Step 1: E and B are the two real-space mechanical halves of the fabric

The first correction is the one that surprises EEs: **E and B are not abstract phase-space objects — they are real-space mechanical motions of the substrate.** Every micropolar node has two ways to move, and they *are* the two field sectors:

- **E-field = translational stretch** (strain $\varepsilon$) — you *push/stretch* the fabric. This is the capacitive (C) sector.
- **B-field = microrotation** ($\omega$) — you *spin* the fabric's micro-gyroscopes. This is the inductive (L) sector.

So "displacement exists in real space" is correct — and that displacement **is** the E-field. They are not two separate things. The translational displacement is the E-sector; the microrotation is the B-sector; both are real-space node DOFs.

> → Primary: [Trampoline/Spring Analogy Primer](trampoline-analogy-primer.md) Step 3.5 — the C/L (stretch/twist) split, "the trampoline only ever showed you the C; Step 3.5 is the L."
> → Primary: [AVE KB Cross-Cutting Invariants](../CLAUDE.md) INVARIANT-S2, Axiom 1 — "6 DOFs each: 3 translational → E, 3 microrotational → B."

**Rest-state caveat.** At rest the gyroscope-fabric is *wound but not spinning* ($\omega = 0$): cocked springs storing the chirality (parity), no net circulation, **no net B**. B turns on only when the fabric is excited or a soliton is trapped — spin-up to net $\omega$ is the magnetic moment.

---

## Step 2: The phase plane is the I/Q quadrature plane — and its axes are E and B

Now the reader's "phase space" intuition gets its home. Treat one substrate bond as an LC tank. Its instantaneous state is a point orbiting a **2D phasor plane**, and the two axes of that plane *are* the E-quadrature and the B-quadrature:

- $E \sim (V_{inc} + V_{ref})$ — in-phase, capacitive
- $B \sim (V_{inc} - V_{ref})/Z$ — quadrature, inductive
- locked together by the line impedance $Z$

Energy sloshing E↔B every quarter cycle = the phasor rotating in that plane. Over a carrier cycle the orbit is purely reactive and averages to zero net displacement; **what survives the time-average is the envelope** — the soliton's persistent real-space strain field, which is what you actually measure as "the field of the particle."

> → Primary: [Photon EE Mapping](../vol1/dynamics/ch4-continuum-electrodynamics/photon-ee-mapping.md) §4 — $E\sim(V_{inc}+V_{ref})$, $B\sim(V_{inc}-V_{ref})/Z$ as a LINEAR I/Q quadrature on the bond's forward/backward voltage waves; the $V \leftrightarrow \Phi_{link}$ linear LC slosh.

---

## Step 3: The flux-tube electron — a plain ring in real space, a (2,3) winding in the phase plane

The electron is a **closed flux-tube soliton**. Hold two facts apart:

- **In real space** it is the $0_1$ **unknot** — a plain closed loop, no knotting.
- **In the phase plane** its bond-pair LC tank winds **(2,3)** on the Clifford torus: 2 windings on the d-axis, 3 on the q-axis. The "(2,3) trefoil" is a *phase-space* winding pattern, **not** a real-space knot.

The **half-integer spin lives entirely in this phase plane**: the "2" means the trajectory only closes after a *double* traversal (720°), which is spin-½. In real space there is nothing to knot — it's just a ring.

> → Primary: [Vol 1 Ch 8 — α from the Golden Torus](../vol1/ch8-alpha-golden-torus.md) §"Topological identity of the electron" — "The trefoil lives in phase space; the soliton lives in real space."
> ↗ See also: [Spin-½ as Classical Gyroscopic Precession](../vol2/particle-physics/ch04-quantum-spin/spin-as-precession.md) — the $0_1$ unknot flux tube as a physical flywheel carrying the rotating (2,3) phase-space winding.

---

## Step 4: A wire carries two things at two speeds — and a plumber already knows this

"A wire is a pipe electrons flow down" is **literally true for charge**: electrons enter one end, exit the other, net transport. The drift is slow (~mm/s) but real. The only thing to add is the second quantity, and the plumber's own world already contains it:

| Plumbing | Wire |
|---|---|
| **Pressure wave** (water hammer) — races down the pipe near the speed of sound in water | **EM field / voltage signal** — travels at ~$c$, in the field. Carries the power. |
| **Water flow** — creeps along slowly | **Electron drift** — slow charge transport |

Both live in the same pipe at wildly different speeds. The "delivery of power" is the fast pressure wave (the I/Q quadrature E↔B slosh of Step 2 guided by the conductor); the slow flow is the literal electron pipe. Neither cancels the other.

*Status: standard EE (field-vs-drift). AVE-native only in that the "pressure wave" is the same substrate E↔B slosh as Steps 1–2.*

---

## Step 5: A shock is flow through you — but the push is your own muscles

A shock is the **flow** going through you: you become the load/resistor in the circuit, current in one contact and out another. Damage scales with **current** (flow-rate × path × duration), not voltage alone — which is why a 20 kV static zap merely stings while 0.1 A across the chest can stop the heart.

But the *push* you feel is **not** the electrons shoving your mass — their momentum is negligible. The current **commandeers your motor nerves and muscles** and they clamp down harder than you ever could voluntarily. **The shock doesn't push you; it makes you push you.** Flow-side tells:

- ~1 mA — felt (nerve threshold)
- ~10–16 mA — *can't-let-go*: grip muscles tetanize, hand won't open
- ~50–100 mA across the heart — fibrillation (external flow drowns out the heart's own pacing current)

**The seam where the pipe analogy breaks.** The pipe *wall* isn't copper the electron-fluid presses against — it's an **impedance boundary**. The electron-tubes don't fill the bore like water fills a hose; they are sparse solitons drifting in a screened sea, guided by impedance contrast, not by a physical wall. A pipe whose walls are made of impedance.

*Status: standard bioelectricity (nerve/muscle as ion-current control loops). The AVE-native layer — nerves/muscles as bioelectric flow loops — is Vol 5 / the AVE-Neurology incubator, not this primer.*

---

## Step 6: Path of least resistance = the delta = global minimum settlement

"Path of least resistance" is the headline, not the whole flow. Water down a hillside doesn't pick one gully and abandon the rest — it spreads into a **delta**, most down the easiest channel, every channel running. Current is identical: through parallel paths it splits by conductance, $I_{branch} \propto 1/R_{branch}$ — the lowest-R path hogs the most, none gets zero. Lightning **forks** for exactly this reason.

The deep point: **nothing chooses the path.** Each electron only feels its local downhill; the field arranges itself (surface charges) so the *global* steady flow is the one that **minimizes total dissipation** (Thomson's principle). Greedy locally → globally least-effort. The hillside doesn't plan the delta; it lets water everywhere go locally downhill, and the delta *is* the global answer.

**This is the substrate's own law — Axiom 3.** The vacuum settles its whole field into the globally least-reflected configuration, every node obeying its local impedance:

> → Primary: [AVE KB Cross-Cutting Invariants](../CLAUDE.md) INVARIANT-S2, Axiom 3 (Minimum Reflection Principle) — "minimizes the boundary reflection $|\Gamma|^2$ at every internal impedance boundary… least reflected action, lossless reactive cycling."

**The one honest difference — least heat vs least reflection.** A resistive wire minimizes *dissipation* (it burns heat to settle). The vacuum substrate is **lossless** — it has no heat to minimize, so it minimizes **reflection** instead. Same principle (a global extremum reached by local obedience), different currency, because one medium can lose and the other can't.

---

## Step 7 (forward pointer — RESEARCH HYPOTHESIS, NOT CANONICAL): the delta made solid

Run the Step-6 settling *forward in time* on a medium that can **freeze along the flow**, and you build a **dendrite**: a low-impedance finger plates into the high-impedance medium, concentrates the field at its tip (lightning-rod effect), grows faster, splits — the Mullins–Sekerka / Laplacian-growth tip-instability. Existing branches *screen* the field from interior valleys, so you get a sparse fractal tree, not a blob. A dendrite is, on this view, **the path of least resistance made solid** — the field's preferred flow, crystallized.

> ⚠ **This step is a forward research hypothesis, NOT a canonical AVE claim.** Corpus-grep (2026-06-08) found it **greenfield** — no leaf assembles "dendrite = minimum-reflection geometry crystallized into matter." Two cautions are load-bearing:
> 1. The corpus already commits to a **competing** morphogenesis mechanism — resonant **standing-wave / Turing** patterning ($\lambda = 2L/n$, $\Gamma \approx 0$). The Laplacian-growth picture here is an *alternative* to that, not a fresh field.
> 2. Standard Laplacian growth already explains dendrites without any AVE. The open crux is whether there is a **discriminator** — a prediction where substrate-minimum-reflection growth differs measurably from ordinary Laplacian growth / minimum-wiring-cost models. Without one, this is an *echo*, not a chord.
>
> Tracked as a prereg in the appropriate non-neural-biophysics locale (NOT this leaf, NOT canonical). This pointer exists only so the pedagogical arc is complete; do not cite it as established.

---

## Provisional status: what this primer IS vs IS NOT

### What this primer IS
- A **picture-first pedagogical anchor** for the substrate, built from the EE/plumber prior, each step adding one corrected intuition.
- A **routing aid** to the canonical EE-mapping leaves (photon-ee-mapping, Vol 1 Ch 8, Axiom 1, Axiom 3).
- **Sister to** [`trampoline-analogy-primer.md`](trampoline-analogy-primer.md) (the GR-pop-sci-prior door).

### What this primer is NOT
- A **source of claims.** Every physics beat re-exposes a canonical leaf; the leaf is authoritative, not this primer.
- A **derivation.** The pictures support analysis; they do not replace it.
- A **canonical statement of the dendrite hypothesis** (Step 7). That is an explicitly-flagged forward research hypothesis, greenfield as of 2026-06-08, with no established discriminator and a competing in-corpus mechanism.
- A claim that the **standard-EE / bioelectricity** beats (Steps 4–5) are AVE-distinct. They are standard physics, flagged as such; their only AVE-native content is that the "pressure wave" is the substrate E↔B slosh.

---

## Cross-references

- **Sister primer**: [`trampoline-analogy-primer.md`](trampoline-analogy-primer.md) — the GR-pop-sci-prior door into the same substrate picture
- **Canonical EE-mapping leaves**:
  - [Photon EE Mapping](../vol1/dynamics/ch4-continuum-electrodynamics/photon-ee-mapping.md) — Step 2 I/Q quadrature E↔B on $(V_{inc}, V_{ref})$
  - [Vol 1 Ch 8 — α from the Golden Torus](../vol1/ch8-alpha-golden-torus.md) — Step 3 $0_1$ unknot (real space) + (2,3) Clifford-torus winding (phase space)
  - [Spin-½ as Classical Gyroscopic Precession](../vol2/particle-physics/ch04-quantum-spin/spin-as-precession.md) — Step 3 flux-tube flywheel
- **Canonical axiom anchors**: [AVE KB Cross-Cutting Invariants](../CLAUDE.md) INVARIANT-S2 — Axiom 1 (translational→E / microrotational→B), Axiom 3 (Minimum Reflection)
- **Translation infrastructure**: [Circuit Translation Table](translation-tables/translation-circuit.md) — the EE↔AVE row-level mapping this primer narrates as a sequence
