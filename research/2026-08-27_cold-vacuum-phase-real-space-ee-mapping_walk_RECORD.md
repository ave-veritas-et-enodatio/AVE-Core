# WALK RECORD — the cold-vacuum phase-space / real-space EE mapping: a floating polyphase mesh with an asymmetric reference (2026-08-27)

**Status: WALK-GRADE, UNAUDITED, MINTS NOTHING.** Nothing in this record is a
claim, a ruling, a promotion, or a design decision. It supersedes nothing. The
audit charter is §8, the kill conditions are §9, and the routing item is
[`_orchestration/open-items/2026-08-27-cold-vacuum-ee-mapping-audit.md`](../_orchestration/open-items/2026-08-27-cold-vacuum-ee-mapping-audit.md).
**Only Grant rules on any of it.**

**Provenance.** Grant, verbatim (2026-08-27): *"what is the ee circuit mapping
between phase space and real space with a 'cold' vacuum? isolated ground/ref?"*
The orchestrator answered walk-grade in seven items; three check lanes then ran
against item 7. This record carries the walk, the check result, the fences, and
what each item is graded at.

**Grade tags used throughout, applied per sentence, not per section:**
`[MEASURED]` — reproduced this session on the shipped operator, script named;
`[CANON]` — verified in-corpus with file:line and quoted;
`[WALK]` — the orchestrator's reading, un-audited;
`[OPEN]` — raised and not answered.

---

## §0 — ★ HEADLINE: the checked item is REFUTED

**Walk item 7 — the proposal that the common-mode open explains why $\mathcal{M}$
is continuous while $\mathcal{Q}$ and $\mathcal{J}$ are integers — DID NOT
SURVIVE. All three check lanes returned REFUTES, on independent grounds, and the
orchestrator's own flagged self-refutation is the one that lands hardest.** The
walk's own verdict on its own fork, carried as the lanes worded it: **category
error, not explanation.**

The refutation in one line: **$n$ is a local constitutive modulus, not a phasor,
so an argument about phasor reference cannot reach $\int_\Omega (n-1)\,dV$ at
all.** `[CANON]` — `manuscript/ave-kb/common/boundary-observables-m-q-j.md:110`
(clm-3bwhad), verified verbatim this session: *"The canonical
gravity-as-substrate-strain prediction $n(r) = 1 + 2GM/(rc^2)$ is **refractive
index** modulation (i.e., **impedance modulation** $\varepsilon_{\text{eff}},
\mu_{\text{eff}}$ via Axiom 4's kernel $S(A)$ at each cell), NOT geometric
bond-length compression."* A per-cell index is a real magnitude ratio set by the
local saturation state. It has no phase and no phasor reference to lose.

Three further kills, each sufficient on its own, each from a different lane:

1. **The minus sign IS a reference.** $\mathcal{M} = \int_\Omega (n(\mathbf{r})
   - 1)\,dV$ `[CANON]`, `boundary-observables-m-q-j.md:19`, verified verbatim.
   The $-1$ subtracts the asymptotic unstrained vacuum $n=1$, which
   $n(r)=1+2GM/(rc^2)$ makes explicit at $r\to\infty$. So $\mathcal{M}$ is not
   "an integral over the one mode that has no reference" — it is an integral of
   a quantity **defined by its reference**. Strip the reference and $\mathcal{M}$
   diverges with the integration volume. The premise is inverted on the face of
   the formula the walk cites.
2. **The explanans does not discriminate.** The L3 lane measured the
   $\Gamma=-1$ balanced subspace to be a continuous $(z-1)$-dimensional real
   vector space — a one-parameter family $t\mathbf{b}$ satisfies $S\mathbf{v} =
   -\mathbf{v}$ to $\le 3.5\times10^{-18}$ for $t$ from $0.1$ to $137$. **Both**
   eigenspaces are continuous. Having a virtual-neutral reference quantizes
   nothing, so reference-vs-no-reference cannot produce the integer/continuous
   split it was invoked to explain.
3. **The identification it rides on is a tautology by canon's own label.**
   `[CANON]` —
   `manuscript/ave-kb/vol9/ch3-pin-port-configuration/node-scattering-multiplicity.md:159`:
   *"| A1 longitudinal scalar $=$ $+1$ common mode | projector-algebra
   **sector-orthogonality FACT** (scramble-invariant) | **true by construction,
   NOT a test** |"*, enforced by a live regression named
   `verdict_is_projector_tautology`. An identity has no explanatory content to
   spend.

**And the explanandum was never open.** $\mathcal{Q} = \mathrm{Link}(\partial
\Omega, \mathbf{F}) \in \mathbb{Z}$ and $\mathcal{J} = \mathrm{Wind}(\partial
\Omega)$ `[CANON]`, `boundary-observables-m-q-j.md:20-21`, verified verbatim.
Link and Wind are homotopy invariants: they are integers because they **count**,
and a count cannot vary continuously. $\mathcal{M}$ is continuous because it
integrates a continuous field. That answer is canonical, referenceless, and
never touches the junction spectrum.

**Consequence for the rest of this record.** Item 7 is dead and is recorded as a
closed negative. **The walk stands or falls on items 1–6 alone**, which the
lanes did not test and which this record grades independently in §3–§7. Two of
those items gained MEASURED support this session (§3, §4); two collide with
canon (§7); the bundle noun in item 6 is fenced (§6).

## §1 — Sector, regime and phase-state declaration

Stated before any substrate word, per standing discipline. **The walk mixes four
objects that share vocabulary, and most of its trouble is here.**

| # | object | space it lives in | regime | what $\Gamma$ means there |
|---|---|---|---|---|
| **O1** | node scatter $S_{ij} = 2Y_j/\sum_k Y_k - \delta_{ij}$ | $z$-port **amplitude** space $(V_{inc},V_{ref})$ at ONE node | any $Y>0$; cold is $Y$ uniform | eigenvalue of the local scatter |
| **O2** | bond reflection at a terminating load | ONE bond's impedance | saturated, $S(A)\to0$ | $\Gamma = (Z-Z_0)/(Z+Z_0)$ at a wall |
| **O3** | $\varepsilon_{11}$ bias / clause-Q reference | real-space **bound** A1 sector | quasi-static, elliptic | not a $\Gamma$ at all |
| **O4** | $(2,3)$ phase-space winding | per-tank Clifford torus | — | not a $\Gamma$ at all |

**CHANNEL/SECTOR.** This walk is about **O1**, the cold node scatter: A1
common-mode $\oplus$ balanced/differential, longitudinal port-amplitude space.
It is **not** about the Cosserat $(2,3)$ carrier. `[CANON]` sector ownership:
mass $=$ A1 dilatation, charge/spin $=$ Cosserat $(2,3)$ winding, **never one
phasor** — `manuscript/ave-kb/common/boundary-observables-m-q-j.md:25`, verified
verbatim: *"**MASS (A1) $\perp$ CHARGE/spin (T2) — never one phasor**
(def-portmp)."*

**REGIME.** COLD: $A=0$, so $S(A)=1$, so every bond admittance $Y = Y_0/\sqrt{S}
= Y_0$ and the network is uniform and **linear**. Everything item 1–6 asserts is
scoped to this regime. §4 measures exactly where that scope ends.

**PHASE-STATE.** Unsaturated, sub-yield, lossless-reactive. No $\Gamma=-1$
saturation surface exists anywhere in a cold vacuum — which is the first
collision, because canon defines all three boundary observables *at* such a
surface (§7, C1).

**★ THE HOMONYM THAT DOES THE MOST DAMAGE.** O1 and O2 both produce the symbols
$\Gamma=+1$ and $\Gamma=-1$, and they mean **opposite things**:

- In **O1**, the $+1$ eigenvalue is the common mode and $-1$ is the differential
  sector — present in **empty cold vacuum**, at every node, always. `[MEASURED]`
  §3.
- In **O2**, `[CANON]` `src/ave/solvers/vacuum_varactor_scatter.py:44-49`,
  verified verbatim: *"As the core SATURATES (S -> 0): Z_bond -> 0 => Gamma ->
  -1 (the mass cage, the Z->0 SHORT) ... It is NOT the FORBIDDEN ε-load (Z_eff =
  Z0/sqrt(S) -> inf, **Gamma=+1**; the SCOPE ASSERTION / EPSILON-LOAD FORBID)."*

So in the O2 register the A1 mass wall is $\Gamma=-1$ (a **SHORT**) and
$\Gamma=+1$ is the **forbidden** $\varepsilon$-load. The walk says "the common
mode sees $\Gamma=+1$, an OPEN" — true in O1, and it must never be read across
into O2, where $+1$ names a load the engine explicitly forbids and where the
mass wall is the short. **Two different measurements, two different regimes.**
Any restatement of this walk must name which object it means. `[WALK]` — the
walk did not.

## §2 — The walk as asked and answered

## §3 — MEASURED: the cold specialisation, reproduced

## §4 — MEASURED: the reference asymmetry is real, and the gauge freedom is COLD-ONLY

## §5 — Where canon SUPPORTS the walk

## §6 — ★ MANDATORY FENCES (verified and quoted this session)

## §7 — Where canon CONTRADICTS the walk

## §8 — ★ AUDIT CHARTER

## §9 — ★ KILL CONDITIONS

## §10 — What this record does NOT do

## §11 — Method, and its known blind spots
