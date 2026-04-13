[↑ Ch.5 White Dwarf Predictions](../index.md)
<!-- leaf: verbatim -->

# Step 5: Numerical Engine Validation

All predictions use engine constants from `ave.core.constants`:

```
from ave.core.constants import G, C_0, NU_VAC, M_SUN, ALPHA
from ave.gravity import (principal_radial_strain, saturation_radius,
                         shear_modulus_factor, refractive_index)
# Canonical regime path (identical physics):
# from ave.regime_3_saturated.orbital_impedance import (
#     calculate_refractive_strain)
```

Scripts:
- `src/scripts/vol_4_engineering/white_dwarf_saturation_redshift.py`
- `src/scripts/vol_4_engineering/wd_shear_eigenfrequency.py`

---
