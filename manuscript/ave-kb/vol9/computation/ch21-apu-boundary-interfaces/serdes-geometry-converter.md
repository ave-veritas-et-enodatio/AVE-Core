[↑ Ch.21: APU Boundary Interfaces](./index.md)
<!-- leaf: verbatim -->

# SerDes Geometry Converter

The SerDes (Serializer/Deserializer) boundary module converts between the temporal bitstream format expected by external digital systems and the spatial harmonic wave-packet format native to the APU interior.

- **Serializer (APU → External):** The output Tensor Plate diffraction pattern is sampled at the boundary by an array of Axiomatic Transducers, each converting a spatial harmonic back to an electrical signal on a $50\,\Omega$ trace.
- **Deserializer (External → APU):** Incoming digital signals are Fourier-decomposed by the RF Topological Routing stage (Ch 12), and each spectral component is injected into the APU substrate as a distinct spatial harmonic via Klopfenstein tapers.

> **[Resultbox]** *Chapter 21 Summary*
>
> APU frameworks seamlessly decouple from internal $\Gamma = 0$ domains through discrete lambda matching stages and SerDes geometry converters, mapping vacuum impedance back into standard $50\,\Omega$ boundaries and translating between temporal bitstreams and spatial wave packets.
