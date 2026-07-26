phase_0

"""
core_neuron.version
===================
Single source of truth for the package version.

Follows `Semantic Versioning 2.0.0 <https://semver.org/>`_:
``MAJOR.MINOR.PATCH[-pre-release][+build]``.
"""

#: Current release version.
__version__: str = "0.1.0"

#: Minimum Python version required (major, minor).
MIN_PYTHON: tuple[int, int] = (3, 10)
