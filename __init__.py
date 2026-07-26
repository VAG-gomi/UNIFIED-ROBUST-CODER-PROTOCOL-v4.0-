phase_0

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
