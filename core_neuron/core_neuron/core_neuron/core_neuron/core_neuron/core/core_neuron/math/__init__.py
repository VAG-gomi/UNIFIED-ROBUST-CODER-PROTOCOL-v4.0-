"""
core_neuron.math
================
Pure-Python numerical and linear-algebra helpers.

This sub-package implements mathematical primitives required by the tensor
and autograd engines using **only the Python standard library**.  No NumPy,
SciPy, or any other third-party numerical library is used.

Planned modules (to be implemented in subsequent development phases):

* ``ops``       – Element-wise arithmetic: add, sub, mul, div, pow, …
* ``linalg``    – Matrix multiply, transpose, determinant, inverse, …
* ``activations`` – Sigmoid, ReLU, tanh, softmax, GELU, …
* ``random``    – Seeded pseudo-random number generators.
* ``stats``     – Mean, variance, standard deviation, normalisation.

All functions operate on nested Python lists (``list[list[float]]`` for
matrices, ``list[float]`` for vectors) and must handle edge-cases (empty
inputs, mismatched shapes) by raising the appropriate exception from
:mod:`core_neuron.exceptions`.
"""
