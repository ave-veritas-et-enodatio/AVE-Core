# Major Topic Here

## Issues 
* [Issue Title](https://github.com/ave-veritas-et-enodatio/AVE-Core/issues/*number*)
* [Issue Title](https://github.com/ave-veritas-et-enodatio/AVE-Core/issues/*number*)

## Change Notes

### Primary Changes
* change 1
* change 2 

### Additional Changes
* change 1
* change 2

### AI code: [percentage-here]
If > 0 describe validation

## Requirements Checklist
[ ] Issue linked
[ ] AI coding usage declared
[ ] Changes have test coverage
[ ] No standard model smuggling (hard-coded or scipy constants, forbidden libraries or functions)
[ ] ```make test``` passes
[ ] ```make verify``` passes

### Axiom-Chain Discipline (A47 v11d)
*If this PR modifies any solver, operator, or physics-derivation function, complete the relevant items.*

[ ] Any axiom-chain-anchored docstring (Ax 1/2/3/4 + Op-N derivation chain) that was modified or removed is replaced with an equivalent or stronger explicit axiom chain — NOT a hand-wave like "organically incorporates" or "natively bypasses" without a derivation. See [research/L3_electron_soliton/100_a47_v9_reframing_line_687_retraction.md §10](../research/L3_electron_soliton/100_a47_v9_reframing_line_687_retraction.md) for the worked-example pattern.
[ ] If a numerical claim against a manuscript validation table is referenced, the manuscript file's commit-SHA pin (per A47 v11c) is unchanged OR has been deliberately advanced (in which case the table is regenerated against the new SHA).
[ ] If a public-API function's behavior changes, the corresponding test in `src/tests/` is updated to lock the new state at appropriate tolerance.
