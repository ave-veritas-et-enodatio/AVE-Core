# Provenance-stamp gate fixture

A VALID stamp — carries an in-tree file path, so it resolves and PASSES:
The leading-order tension law is exact (sympy-verified, `driver_ok.py`).

A VALID stamp with a `path::symbol` reference (symbol must exist in the file):
Non-reciprocity holds (driver-confirmed, `driver_ok.py::verify_reciprocity`).

A VALID stamp with a `path:line` suffix:
Kernel integrates once (sympy-verified, `driver_ok.py:3`).

A BOGUS stamp — no artifact reference anywhere on the line, MUST FAIL:
The per-channel loading is consistent at second order (sympy-verified).

A BOGUS stamp naming a file that does not exist in-tree, MUST FAIL:
Curve values pinned (test-locked, `no_such_driver.py`).

A BOGUS stamp naming a real file but a symbol NOT in it, MUST FAIL:
Result confirmed (engine-confirmed, `driver_ok.py::function_that_is_absent`).

A stamp inside a code fence MUST be ignored (example text, not an assertion):

```
this is sympy-verified with no artifact and must not be flagged
```

A stamp inside an `inline sympy-verified code span` MUST be ignored too.

A stamp that will be GRANDFATHERED in the fixture baseline (a legacy bogus
stamp): the pre-existing law is engine-verified.
