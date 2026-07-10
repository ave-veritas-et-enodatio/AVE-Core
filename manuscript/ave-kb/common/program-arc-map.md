[↑ Common Resources](index.md)

<!-- kb-frontmatter
kind: leaf
no-claim: "Navigational meta-leaf: the TEMPORAL/causal view of the corpus (which arc opened which question, what killed what, what each verdict unlocked). Originates no derivation and hosts no claim — it is a map over the existing claim graph, the release/tag history, and the orchestration record. The claim-quality register remains the source of truth for every verdict cited here; this leaf only routes to it. Maintained at era boundaries and release tags by orchestration sessions, via PR."
-->

# The Program Arc Map — the historical arc as navigational infrastructure

> ⛔ **This leaf is a MAP, not a diary.** It is the *temporal/causal* view of the AVE corpus: which arc opened which question, what verdict killed what, and what each closure unlocked. The [claim graph](claim-quality.md) is the *logical* view (what depends on what); this leaf is the *causal* view (what came from what). Every verdict quoted here is a pointer — the cited `clm-`/`exp-` entry, PR, audit tag, or research doc is the source of truth. Where this map and a leaf disagree, **the leaf wins and the drift is a bug in this map** (flag it, do not reframe the leaf).

Ratified 2026-07-10 (Grant): *"we need to start treating the historical arch as a map."*

---

## §1 — The Contract (how sessions use this map)

This leaf carries a **navigational contract**, parallel to and extending the `ave-prereg` corpus-grep discipline from the *claim* level up to the *arc* level:

1. **Check before opening an arc.** Before a session opens a new investigative arc, it greps §3 (the Arc Registry) and §5 (Standing Negatives) for a prior traversal of the same territory. `ave-prereg` asks "has this *claim* been made?"; this map asks "has this *question* already been opened, and with what verdict?" A pretty mechanism that a prior arc already killed does not get re-derived; it gets cited.

2. **The anti-repetition function.** §5 (Standing Negatives Index) is the arc-level analogue of the [Genesis / Chord Falsification Ledger](genesis-chord-falsification-ledger.md): a falsified mechanism, once banked, must not be silently re-walked. A new session proposing a mechanism in §5's table must either (a) cite a *new discriminator* the original arc lacked, or (b) not run it. This is Rule 11 (honest closure) enforced across sessions, not just within one.

3. **The open-forks function.** §6 (Standing Open Forks) shows every live question with its *assigned resolution route*. A session picking up a fork checks §6 first for the route already assigned, rather than minting a parallel plan (Rule 16 — corpus + Grant before a new methodology pivot).

4. **Maintenance rule.** This map is updated at **era boundaries** and **release tags** by orchestration sessions, via PR like everything else (no self-merge; `[REVIEW: pending-orchestrator]`). It is deliberately *not* updated per-PR — it is a coarse causal skeleton, not a commit log. When a release ships (`gh release`), the shipping session adds/closes the arcs that release summarizes. Between releases it is allowed to lag; the claim graph, not this map, is the live truth.

**What this map is NOT:** it is not a claim source (INVARIANT-S7 — leaves are canonical; this is a routing aid), not a substitute for reading the cited `clm-` entry, and not a place to litigate a verdict. A verdict changes in its home leaf first; this map follows.

---

## §2 — Era Timeline

The program's coarse phases. Each era's *character* is one line; the release/tag column is the receipt anchor. Windows before `2026-04-13` predate the AVE-Core git history (the repo's initial commit is `de9d2293`, 2026-04-13) and are anchored by the archived electron-soliton thread rather than by git dates.

| Era | Window | Character | Release / tag anchor |
|---|---|---|---|
| **E1 — the spark** | pre-repo → 2026-04-13 | Vacuum as an engineerable EE medium; the K4 / chiral-LC lattice picture; the α⁻¹ = 4π³+π²+π keystone posited as a zero-parameter closure. | initial commit `de9d2293` (2026-04-13); `v0.0` (2026-04-15) |
| **E2 — corpus building** | 2026-04-13 → ~2026-05-15 | Manuscript volumes + engine v1 + the L3 electron-soliton thread (137 `.md` docs, now archived). | `v0.5` "Remerged alpha" (2026-04-19); `research/_archive/L3_electron_soliton/` |
| **E3 — collaboration forms** | (pre-repo) → surfaces 2026-07 | The physics program acquires coauthors; the earliest git-receiptable coauthorship is the three-author Letter. | `v0.7` Letter authorship: G. Lindblom, K. Mertens, B. Herrera |
| **E4 — the honesty turn** | 2026-05-16 → ~2026-06-15 | α keystone resolved = Class-B ECHO; "real chord or echo?" becomes the north star; EE-as-substrate-native ratified; multi-lane adversarial orchestration built. | first audit tag `audit/2026-05-16_*`; `audit/2026-06-02_honest-alpha-relabel` |
| **E5 — the interior gauntlet** | ~2026-06-13 → 2026-06-29 | Sector-ownership canon; genesis energize-lock negative; K=2G = GR-imported; FORM/VALUE meta-finding named; mass sector closed ECHO-final; carrier sector closed-at-peer. Verdict: NO AVE-distinct chord *inside*. | PRs #220, #260–#264, #311, #313–#315, #433–#435 |
| **E6 — the testing pivot** | ~2026-06-22 → 2026-06-24 | Grant pivots to infrastructure-first testing; bench-model spine; birefringence flagship survives PVLAS via circulation-keyed μ (Route C); cleave-01 + impedance-probe primitives scoped. | PR #384; `audit/2026-06-22_*` handoffs; `audit/2026-07-03_birefringence-*` |
| **E7 — the Letter era** | ~2026-07-03 → 2026-07-09 | SVE Letter v1→v5 through 3 adversarial rounds; muonic-H self-kill → static-sector scoping; single-footing 3.75π/α²; NIST XCOM verify; OTS pre-reg chain Bitcoin-anchored; γγ/ATLAS → EFT-domain scoping. | `v0.6` / `v0.7` / `v0.8`; PRs #582–#600 |
| **E8 — the machine-fork nights** | 2026-07-09 / 2026-07-10 | srs band structure closed-form; the PARITY THEOREM; clock / tethered-pivot / node-shunt forks; operator-typing pass; breakthrough-patterns methods note. Three pretty mechanisms killed by pre-registered discriminators in one week. | PRs #603–#613 |

---

## §3 — Arc Registry

*(filled below — the heart of the map)*

---

## §4 — Epistemic State Transitions

*(filled below)*

---

## §5 — Standing Negatives Index

*(filled below)*

---

## §6 — Standing Open Forks

*(filled below)*

---

## §7 — Methods Evolution

*(filled below)*
