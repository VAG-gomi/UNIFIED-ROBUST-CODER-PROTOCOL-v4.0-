phase_0

(1)

"""
core_neuron
===========
A production-grade educational neural network framework built entirely from
scratch using only the Python standard library.  No third-party dependencies
are required or permitted.

Typical usage::

    import core_neuron

Sub-packages
------------
core          – Fundamental primitives and base classes.
math          – Pure-Python numerical / linear-algebra helpers.
tensor        – N-dimensional tensor abstraction.
nn            – Layer and model building blocks.
autograd      – Automatic differentiation engine.
optim         – Optimisation algorithms (SGD, Adam, …).
losses        – Loss / objective functions.
datasets      – Data loading and batching utilities.
serialization – Model save / load helpers.
utils         – Logging, seeding, timing, and other utilities.
"""

from core_neuron.version import __version__

__all__ = ["__version__"]


(2)

"""
core_neuron.core
================
Fundamental primitives and base classes used across the entire framework.

This sub-package provides the lowest-level abstractions:

* Base classes for all trainable objects (e.g. layers, models).
* Parameter containers.
* Protocol / interface definitions consumed by higher-level sub-packages.

Nothing in this sub-package should import from sibling sub-packages (``nn``,
``autograd``, etc.) to keep the dependency graph acyclic.
"""
