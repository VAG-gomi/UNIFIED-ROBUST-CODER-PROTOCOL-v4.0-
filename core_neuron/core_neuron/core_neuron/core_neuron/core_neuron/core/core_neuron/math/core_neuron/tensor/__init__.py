"""
core_neuron.tensor
==================
N-dimensional tensor abstraction.

The ``Tensor`` class is the primary data carrier throughout the framework.
It wraps a nested Python list and tracks:

* **shape**  – tuple of dimension sizes.
* **dtype**  – logical element type (``"float32"`` or ``"float64"``).
* **requires_grad** – whether the autograd engine should track this tensor.
* **grad**   – accumulated gradient, populated after a backward pass.

Planned modules (to be implemented in subsequent development phases):

* ``tensor``  – :class:`Tensor` class definition.
* ``ops``     – Functional tensor operations (reshape, slice, concat, …).
* ``init``    – Weight-initialisation strategies (Xavier, Kaiming, …).
* ``factory`` – Convenience constructors (zeros, ones, eye, arange, …).
"""
