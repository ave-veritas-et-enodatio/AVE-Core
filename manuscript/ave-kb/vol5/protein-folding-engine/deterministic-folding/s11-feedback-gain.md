[↑ Protein Folding](../index.md)
<!-- leaf: verbatim -->

# Comparison with Statistical Approaches

The dominant paradigm in computational protein structure prediction is deep-learning pattern recognition. Google DeepMind's AlphaFold 2 (2020) achieved near-experimental accuracy on the CASP14 benchmark by training a neural network on $\sim$170,000 experimentally determined protein structures. While the engineering achievement is remarkable, it is a statistical interpolation: the network has no physical model of *why* certain sequences fold into certain shapes. It cannot extrapolate to novel fold topologies absent from its training set, and its predictions carry no mechanistic explanation.

The AVE approach is architecturally opposite. The folding engine contains *zero* trainable parameters and *zero* empirical structure data. The prediction flows entirely from the vacuum lattice axioms through the periodic table infrastructure:

$$\text{Axioms 1--2} \;\xrightarrow{\text{soliton solver}}\; d_{\text{eq}},\, r_{\text{Slater}} \;\xrightarrow{\text{Ramachandran}}\; Z_{topo} \;\xrightarrow{\text{5-force engine}}\; \text{Fold geometry}$$

The 20-sequence stress test demonstrates 95% accuracy across real protein architectures including helical bundles, $\beta$-hairpins, mixed $\alpha/\beta$ proteins, and collagen-like repeats. The current model cannot predict full tertiary structure (long-range disulfide bonds, hydrophobic core packing), but the secondary structure classification---derived entirely from axioms---matches the empirical consensus for 19 of 20 test sequences.

---
