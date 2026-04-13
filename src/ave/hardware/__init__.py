"""
AVE Hardware Module — Private Repository
=========================================

The hardware implementation layer (APU components, geometric diode,
geometric triode, soliton memory, etc.) is maintained in a separate
private repository pending patent review.

The physics engine (this repo) is fully functional without the
hardware module. All theoretical derivations, validations, and
predictions operate independently.

Repository: AVE-APU (private)
License: Proprietary — see AVE-APU/LICENSE

For licensing inquiries: [contact info]
"""


class _HardwareNotAvailable:
    """Stub that raises a clear error when hardware modules are accessed."""
    
    def __getattr__(self, name):
        raise ImportError(
            "The ave.hardware module is not included in the public release. "
            "Hardware components (APU, geometric diode, soliton memory, etc.) "
            "are maintained in a separate private repository. "
            "See README.md for details."
        )


# Allow `import ave.hardware` to succeed but access to fail gracefully
_stub = _HardwareNotAvailable()
