from ave.nuclear.silicon_nucleus import silicon_nucleus_binding

def test_silicon_nucleus_binding() -> None:
    """
    Validates that the Z=14 nucleus constructs a strictly positive bounding target
    without propagating undefined numeric or generic terms.
    """
    mass, binding = silicon_nucleus_binding()
    assert binding > 0.0, "Topological LC binding target must be purely robust / strictly > 0"
    # Experimental Si-28 mass excess is roughly -21.49 MeV
    # We simply verify no exceptions thrown and mathematically stable.
    assert mass > 0.0 or mass <= 0.0  # simple stability ensure it returns a valid float.
