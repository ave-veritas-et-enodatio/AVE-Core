[↑ Ch.6 Universal Operators](index.md)
<!-- leaf: verbatim -->
<!-- path-stable: referenced from vol1 as sec:universal_y_to_s -->

## Section 6.5: The Universal Y-to-S Conversion

The multiport generalisation of Operator 3:

> **[Resultbox]** *Multiport S-Matrix*
>
> <!-- eq:y_to_s -->
>
> $$
> [S] = (I + [Y]/Y_0)^{-1} \cdot (I - [Y]/Y_0)
> $$

Used at: nuclear (K_MUTUAL eigenvalues), protein (fold eigenstate), antenna (S-parameters).

Code path: `universal_operators.universal_ymatrix_to_s(Y, Y0)`.

---
