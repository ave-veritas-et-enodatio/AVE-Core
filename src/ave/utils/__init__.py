"""AVE reusable performance / instrumentation utilities.

Library-tier helpers shared across the vol_1 genesis drivers (crystal-graft,
electron-genesis). These are pure-numpy/stdlib modules with NO dependency on any
`src/scripts/**` driver (scripts depend on libs, never the reverse —
ave-module-library-discipline). Physics lives in `ave.core`; these modules only
make the EXISTING measurements run faster, never change what they measure.
"""
