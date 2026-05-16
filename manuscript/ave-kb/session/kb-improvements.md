# AVE-KB Improvements

Running list of improvements scoped specifically to the AVE-KB (canonical markdown tree at `AVE-Core/manuscript/ave-kb/`). Broader design questions about future agentic systems live elsewhere; items here are about making the existing KB better as it stands.

Completed items have been removed — git history holds them. What remains is what is still on the table.

---

## 1. KB-vs-LaTeX divergence as a staleness signal

The KB markdown tree is canonical; the LaTeX manuscript (`manuscript/vol_*/`) is a derived publication artifact. That inversion took effect 2026-05-07 and is documented in `kb-docent.md` ("Canonical Source") and INVARIANT-S7.

**Open:** decide whether to add a verifier step that flags KB-vs-LaTeX divergence as a *derivation-staleness* signal — "the LaTeX has not caught up to this leaf" — rather than letting it read as a KB error. There is currently no automated detection of LaTeX lag.
