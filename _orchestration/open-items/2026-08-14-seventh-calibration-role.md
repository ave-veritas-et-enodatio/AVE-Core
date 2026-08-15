---
id: seventh-calibration-role
title: A 7th `calibration_role` is authorized and unbuilt — the schema still lists six
status: ROUTED-TO-GRANT
owner: grant
opened: 2026-08-14
source: _orchestration/docket-entries/2026-08-13-forward-postdiction-manifest-split.md
anchor: "was the observable being predicted used to set any input?"
---

Grant authorized a **seventh** `calibration_role`, in its own PR, during the 2026-08-13 manifest
split: *"2. lets add the 7th in a new PR"*. It was never built, and until now it was tracked
**nowhere** — the authorization lived only in the split's docket entry, so a session reading
`BOARD.md` (which CLAUDE.md names as the first thing to read) could not see it existed.

Found 2026-08-14 by an independent review of PRs #966/#967/#968. Recorded here because the board is
generated from `open-items/`, so an untracked authorization is an invisible one.

**The class it names.** Form forced by the substrate + value computed from a declared calibration
input *measured in a different experiment* + output **never fit to the observable being predicted**.
That is a genuine forward value, and the six current roles have no slot for it: `echo` and `mixed`
collapse it together with the definitional case.

**The discriminator**, per the authorization: *"was the observable being predicted used to set any
input?"* — NOT *"does α appear?"*. Those come apart, and the current vocabulary keys on the wrong one.

**Current state**
- `manuscript/predictions.yaml` schema comment lists **six** roles: `chord`, `echo`, `mixed`,
  `fitted`, `consistency`, `forward-prediction`.
- `ALLOWED_CALIBRATION_ROLES` in `src/scripts/predictions_manifest_validator.py` carries the same six.
- `PROVENANCE_MARKERS` / `suggest_role()` reconcile against those six, and the reconciler GATES at
  `severity="critical"` — so adding a seventh is a change to a gating vocabulary and needs the
  frozen-snapshot test updated deliberately, with the census re-measured before it lands.

**What is needed from Grant**
1. The role's **name** — the thing that will appear in tracked YAML and in the public table's
   provenance column.
2. Whether any **existing rows** re-classify into it on landing, or whether it starts empty and is
   applied going forward only. If rows move, that is a second ruling, not a rider — the 2026-08-13
   split was already flagged once for extending an unasked-for relabel.
3. Whether it is a `calibration_role` value at all, or a separate axis. `def-fmv001` already carves
   FORM-vs-VALUE; this may be the VALUE axis's *provenance-of-the-input* dimension rather than a
   seventh peer of `chord`/`echo`.

**Not urgent.** Nothing is wrong in the corpus today; the gap is that a real class has no name, so
rows in it are currently labelled with a role that overstates their dependence on α.
