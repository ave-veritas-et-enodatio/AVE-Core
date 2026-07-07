"""Fixture artifact for the provenance-stamp gate self-test.

The gate resolves the basename, a path:line suffix, and a path::symbol against
this file. The self-test also references a symbol name that appears NOWHERE in
this file so the symbol-not-found failure path is exercised; that name is
deliberately NOT written here (writing it would satisfy the substring check).
"""


def verify_reciprocity():
    return True
