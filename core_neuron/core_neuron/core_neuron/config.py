"""
core_neuron.config
==================
Global framework configuration.

All tuneable defaults live here so that nothing is hard-coded inside the
computational modules.  Application code may mutate these values before
importing other sub-packages, or pass overrides directly to individual APIs.

Example::

    from core_neuron import config
    config.DEFAULT_DTYPE = "float64"
    config.RANDOM_SEED = 42
"""

# ---------------------------------------------------------------------------
# Numeric precision
# ---------------------------------------------------------------------------

#: Default floating-point type used throughout the framework.
#: Accepted values: ``"float32"``, ``"float64"``.
DEFAULT_DTYPE: str = "float32"

#: Small epsilon value used to guard against division-by-zero.
EPSILON: float = 1e-8

# ---------------------------------------------------------------------------
# Randomness
# ---------------------------------------------------------------------------

#: Global random seed.  ``None`` means non-deterministic.
RANDOM_SEED: int | None = None

# ---------------------------------------------------------------------------
# Autograd
# ---------------------------------------------------------------------------

#: When ``True``, gradient computation is enabled globally.
GRAD_ENABLED: bool = True

# ---------------------------------------------------------------------------
# Logging / debugging
# ---------------------------------------------------------------------------

#: Verbosity level passed to the logging sub-system.
#: 0 = silent, 1 = warnings, 2 = info, 3 = debug.
VERBOSITY: int = 1

#: When ``True``, extra runtime assertions are enabled (slower but safer).
DEBUG_MODE: bool = False
