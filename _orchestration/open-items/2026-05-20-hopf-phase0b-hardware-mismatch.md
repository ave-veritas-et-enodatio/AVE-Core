---
id: hopf-phase0b-hardware-mismatch
title: A1-HOPF Phase 0b — ordering the board as drawn does NOT buy the surviving discriminator
status: ROUTED-TO-GRANT
owner: grant
opened: 2026-05-20
source: _orchestration/docket-entries/2026-08-01-bench-staleness-propagation.md
anchor: "Phase 0b physical fab order NOT placed"
---

★ **The framing this item carried was stale in a way that would waste the spend.** The index called
it *"your only low-friction high-signal exec item now"* — a ~$123 JLCPCB upload + mandrels.

**But the discriminator it was meant to buy is gone.** Grant retired the C3/C4 legs to
consistency-class on 2026-06-04. The surviving AVE-distinct leg is the **2-port S₂₁-vs-S₁₂
reciprocity sweep**, which per docket `2026-08-01-bench-staleness-propagation.md` needs *"**2-port
hardware the 1-port SMA edge-launch HOPF-02a board does not provide**."*

**So: ordering HOPF-02a as-drawn does not buy the surviving discriminator.** The decision owed is
not "upload the Gerbers" — it is whether to respin for 2-port, or shelve the bench.

State confirmed at 2026-08-01: *"Phase 0a fab-artifact generation complete … with the Phase 0b
physical fab order NOT placed … **No HOPF-02a board and no HOPF-02a measurement exist.**"* AVE-HOPF
has no Phase-0b commits since `29264b4` (2026-05-21). Verified 2026-08-13 by sweep.
