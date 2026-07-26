"""
tests.test_exceptions
=====================
Placeholder tests for :mod:`core_neuron.exceptions`.

Tests to be implemented:
    - ``test_all_exceptions_inherit_base``  – every public exception is a
      subclass of :class:`~core_neuron.exceptions.CoreNeuronError`.
    - ``test_shape_error_is_validation``    – :class:`ShapeError` inherits
      from :class:`ValidationError`.
    - ``test_dtype_error_is_validation``    – :class:`DTypeError` inherits
      from :class:`ValidationError`.
    - ``test_gradient_error_is_autograd``   – :class:`GradientError` inherits
      from :class:`AutogradError`.
    - ``test_checkpoint_corrupted_is_serialization`` – subclass chain correct.
    - ``test_invariant_error_is_internal``  – :class:`InvariantError` inherits
      from :class:`InternalError`.
    - ``test_oom_is_resource``              – :class:`OutOfMemoryError` inherits
      from :class:`ResourceError`.
    - ``test_raise_and_catch_base``         – a raised subclass is caught by
      the base ``CoreNeuronError`` handler.
"""
