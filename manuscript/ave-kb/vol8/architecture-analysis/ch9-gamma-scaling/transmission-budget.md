[↑ Ch.9 Gamma Scaling](../index.md)
<!-- leaf: verbatim -->

# The Transmission Budget as a Training Metric

The parameter $B$ quantifies how much total signal attenuation the model tolerates before quality degrades. A poorly trained model (noisy weights, suboptimal convergence) will have a lower $B$. A well-trained model will have a higher $B$.

$B$ is therefore a single-number summary of *training quality*: the total cascade headroom available for impedance perturbation. It is an *emergent property* of the training process, analogous to the yield strength of a material---determined by the manufacturing process, not by fundamental constants.
