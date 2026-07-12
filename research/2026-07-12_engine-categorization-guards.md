# Engine categorization guards — method note

**Date:** 2026-07-12 · **Branch:** `analysis/engine-categorization-guards`
**Class:** tooling / methodology (L0). **No chord. No new physics number.**

## Why

Agents repeatedly bank Gauss / install-tautology PASS as if it reconciled two
different functionals (X36 / #651 / X44), and occasionally put `c_shear` into α
or `c_EM` into Schwarzschild reduction (INVARIANT-S2 Pitfall #5). The taxonomy
already lived in skills + KB; the engine did not enforce it.

## What shipped

| piece | role |
|---|---|
| `src/ave/core/categorization.py` | enums + raisers: ledger pairing, claim class, wave-speed slots, SYM/ASYM, parity + 3-port keepers |
| `solve_backreaction` → `ledger_tags` | stamps ADD-convention entailment vs fireable ADM pairing on every solve |
| `_nordtvedt.py` | import-time `CERTIFICATION_PAIRING` / `MIXED_REGISTER_PAIRING` |
| pytest markers `claim_class` / `ledger_pairing` | discoverable tags in `pyproject.toml` |
| `src/tests/test_categorization_guards.py` | unit keepers |
| `src/scripts/verify/categorization_smoke.py` | zero-solve smoke fire |

## Non-goals

- Does not merge or retune X44 Komar source.
- Does not edit U6 / A7 / KB claim solidities.
- Does not replace existing X38 3-port or twotone drivers — adds the pure-identity keepers those arcs already proved.
