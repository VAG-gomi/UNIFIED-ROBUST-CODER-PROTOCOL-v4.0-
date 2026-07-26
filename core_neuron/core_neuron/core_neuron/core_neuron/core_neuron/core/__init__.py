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
