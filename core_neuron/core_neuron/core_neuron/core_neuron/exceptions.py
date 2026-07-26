"""
core_neuron.exceptions
======================
Framework-wide exception hierarchy.

All public exceptions inherit from :class:`CoreNeuronError` so that callers
can catch the entire family with a single ``except CoreNeuronError`` clause
while still being able to handle specific sub-classes when needed.

Error taxonomy (aligned with the Unified Robust Coder Protocol v4.0):

* **User Error**        – :class:`ConfigurationError`, :class:`UsageError`
* **Validation Error**  – :class:`ShapeError`, :class:`DTypeError`,
                          :class:`ValidationError`
* **Internal Error**    – :class:`InternalError`, :class:`InvariantError`
* **Resource Error**    – :class:`ResourceError`
* **External Dependency Error** – (reserved; no external deps in this build)
* **Security Error**    – (reserved for future serialization hardening)
"""


# ---------------------------------------------------------------------------
# Base
# ---------------------------------------------------------------------------


class CoreNeuronError(Exception):
    """Root exception for the core_neuron framework.

    All framework exceptions inherit from this class.
    """


# ---------------------------------------------------------------------------
# User / configuration errors
# ---------------------------------------------------------------------------


class ConfigurationError(CoreNeuronError):
    """Raised when the framework is misconfigured by the caller."""


class UsageError(CoreNeuronError):
    """Raised when a public API is called in an unsupported way."""


# ---------------------------------------------------------------------------
# Validation / shape errors
# ---------------------------------------------------------------------------


class ValidationError(CoreNeuronError):
    """Raised when data fails a framework business rule."""


class ShapeError(ValidationError):
    """Raised when tensor shapes are incompatible for a requested operation."""


class DTypeError(ValidationError):
    """Raised when a dtype is not supported by the requested operation."""


class RankError(ValidationError):
    """Raised when a tensor has the wrong number of dimensions."""


# ---------------------------------------------------------------------------
# Autograd errors
# ---------------------------------------------------------------------------


class AutogradError(CoreNeuronError):
    """Base class for errors originating in the autograd engine."""


class GradientError(AutogradError):
    """Raised when gradient computation fails or produces an invalid result."""


class NoGradError(AutogradError):
    """Raised when a gradient is requested but has not been computed."""


# ---------------------------------------------------------------------------
# Serialization errors
# ---------------------------------------------------------------------------


class SerializationError(CoreNeuronError):
    """Raised when model save / load encounters an unrecoverable problem."""


class CheckpointCorruptedError(SerializationError):
    """Raised when a checkpoint file fails integrity verification."""


# ---------------------------------------------------------------------------
# Internal / invariant errors
# ---------------------------------------------------------------------------


class InternalError(CoreNeuronError):
    """Raised when an unexpected internal invariant is violated.

    These represent bugs in the framework, not user mistakes.
    """


class InvariantError(InternalError):
    """Raised when a module-level invariant is broken."""


# ---------------------------------------------------------------------------
# Resource errors
# ---------------------------------------------------------------------------


class ResourceError(CoreNeuronError):
    """Raised when a required resource (memory, file, …) is unavailable."""


class OutOfMemoryError(ResourceError):
    """Raised when an operation cannot be completed due to memory limits."""
