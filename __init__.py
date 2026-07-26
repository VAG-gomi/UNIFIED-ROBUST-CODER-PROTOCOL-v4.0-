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

(3)

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

(4)

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

(5)

"""
core_neuron.nn
==============
Layer and model building blocks.

This sub-package contains the high-level API for constructing neural networks.
It depends on :mod:`core_neuron.tensor` for data and
:mod:`core_neuron.autograd` for gradient tracking, but is otherwise
self-contained.

Planned modules (to be implemented in subsequent development phases):

* ``module``   – :class:`Module` base class (forward, parameters, train/eval).
* ``linear``   – Fully-connected (dense) layer.
* ``conv``     – 1-D and 2-D convolution layers.
* ``recurrent``– RNN, LSTM, GRU cells and stacked variants.
* ``norm``     – Batch-norm, layer-norm, group-norm.
* ``dropout``  – Dropout and variational dropout.
* ``embedding``– Discrete token embedding table.
* ``container``– Sequential, Parallel, and ModuleList containers.
* ``attention``– Scaled dot-product and multi-head attention.
"""

(6)

"""
core_neuron.autograd
====================
Automatic differentiation engine.

Implements reverse-mode automatic differentiation (backpropagation) over the
:class:`~core_neuron.tensor.Tensor` graph.  The engine records operations
during the forward pass and replays them in reverse order during the backward
pass to accumulate gradients.

Planned modules (to be implemented in subsequent development phases):

* ``engine``   – :class:`Graph` / tape that records the computation DAG.
* ``function`` – :class:`Function` base class for differentiable operations.
* ``context``  – :class:`Context` for saving tensors needed in the backward pass.
* ``grad_fn``  – Concrete backward implementations for all primitive ops.
* ``no_grad``  – Context-manager and decorator to disable gradient tracking.
* ``checkpoint`` – Gradient checkpointing for memory-efficient training.
"""

(7)

"""
core_neuron.optim
=================
Optimisation algorithms.

All optimisers share a common interface: they accept a list of
:class:`~core_neuron.tensor.Tensor` parameters, a learning rate, and
optional hyper-parameters, then expose ``step()`` / ``zero_grad()`` methods.

Planned modules (to be implemented in subsequent development phases):

* ``base``      – :class:`Optimizer` abstract base class.
* ``sgd``       – Stochastic Gradient Descent with optional momentum.
* ``adam``      – Adam (Adaptive Moment Estimation).
* ``adamw``     – AdamW (Adam with decoupled weight decay).
* ``rmsprop``   – RMSProp.
* ``adagrad``   – Adagrad.
* ``scheduler`` – Learning-rate schedulers (step, cosine annealing, …).
"""

(8)

"""
core_neuron.losses
==================
Loss / objective functions.

Loss functions measure the discrepancy between model predictions and ground-
truth targets.  Each loss function returns a scalar
:class:`~core_neuron.tensor.Tensor` that can be differentiated via the
autograd engine.

Planned modules (to be implemented in subsequent development phases):

* ``base``       – :class:`Loss` abstract base class.
* ``regression`` – MSE (Mean Squared Error), MAE, Huber / smooth-L1.
* ``classification`` – Cross-entropy (binary and categorical), NLL.
* ``ranking``    – Contrastive loss, triplet margin loss.
* ``reduction``  – ``mean``, ``sum``, and ``none`` reduction modes.
"""

(9)

"""
core_neuron.datasets
====================
Data loading, preprocessing, and batching utilities.

This sub-package provides dataset abstractions and data-pipeline helpers
that feed mini-batches into the training loop.  Everything is implemented
using the Python standard library (``csv``, ``pathlib``, ``random``, etc.).

Planned modules (to be implemented in subsequent development phases):

* ``dataset``    – :class:`Dataset` abstract base class (``__len__``, ``__getitem__``).
* ``dataloader`` – :class:`DataLoader` – batching, shuffling, multi-sample collation.
* ``transforms`` – Composable preprocessing transforms (normalise, one-hot, …).
* ``samplers``   – :class:`SequentialSampler`, :class:`RandomSampler`.
* ``csv_dataset``– CSV-backed :class:`Dataset` using the ``csv`` stdlib module.
* ``splits``     – Train / validation / test splitting utilities.
"""

(10)

"""
core_neuron.serialization
=========================
Model save / load helpers.

Provides a stable, versioned serialization format for persisting trained
models, optimiser state, and arbitrary framework objects to disk.  Only the
Python standard library (``json``, ``struct``, ``hashlib``, ``pathlib``,
``zipfile``) is used; no external dependencies are required.

Planned modules (to be implemented in subsequent development phases):

* ``checkpoint``  – Save and load full training checkpoints (model + optimiser).
* ``format``      – Binary container format definition and version negotiation.
* ``registry``    – :class:`SerializableRegistry` for custom type dispatch.
* ``integrity``   – SHA-256 / HMAC verification of checkpoint files.
* ``migration``   – Forward-compatibility helpers when the schema evolves.
"""

(11)

"""
core_neuron.utils
=================
Logging, seeding, timing, and miscellaneous utilities.

This sub-package collects small, standalone helpers that do not belong to any
single computational module but are used throughout the framework.

Planned modules (to be implemented in subsequent development phases):

* ``logging``   – Structured logger wrapping :mod:`logging` from the stdlib.
* ``seed``      – Global random-seed management for reproducible runs.
* ``timer``     – :class:`Timer` context-manager for wall-clock profiling.
* ``progress``  – Lightweight ASCII progress bar (no curses dependency).
* ``registry``  – Generic key-value registry for plug-in lookup.
* ``inspect``   – Helpers for pretty-printing model summaries and shapes.
* ``typing``    – Framework-specific type aliases (``Shape``, ``DType``, …).
"""

(12)

"""
core_neuron.datasets
====================
Data loading, preprocessing, and batching utilities.

This sub-package provides dataset abstractions and data-pipeline helpers
that feed mini-batches into the training loop.  Everything is implemented
using the Python standard library (``csv``, ``pathlib``, ``random``, etc.).

Planned modules (to be implemented in subsequent development phases):

* ``dataset``    – :class:`Dataset` abstract base class (``__len__``, ``__getitem__``).
* ``dataloader`` – :class:`DataLoader` – batching, shuffling, multi-sample collation.
* ``transforms`` – Composable preprocessing transforms (normalise, one-hot, …).
* ``samplers``   – :class:`SequentialSampler`, :class:`RandomSampler`.
* ``csv_dataset``– CSV-backed :class:`Dataset` using the ``csv`` stdlib module.
* ``splits``     – Train / validation / test splitting utilities.
"""

(13)


"""
tests
=====
Test suite for core_neuron.

Directory layout::

    tests/
        __init__.py          ← this file
        test_version.py      ← placeholder: version checks
        test_config.py       ← placeholder: config defaults
        test_exceptions.py   ← placeholder: exception hierarchy
        core/
            __init__.py
            test_core.py
        math/
            __init__.py
            test_ops.py
            test_linalg.py
        tensor/
            __init__.py
            test_tensor.py
            test_init.py
        nn/
            __init__.py
            test_module.py
            test_linear.py
        autograd/
            __init__.py
            test_engine.py
        optim/
            __init__.py
            test_sgd.py
            test_adam.py
        losses/
            __init__.py
            test_regression.py
            test_classification.py
        datasets/
            __init__.py
            test_dataloader.py
        serialization/
            __init__.py
            test_checkpoint.py
        utils/
            __init__.py
            test_logging.py
            test_timer.py

All test modules are placeholder stubs; no test logic is generated in this
phase.  Tests will be implemented in Phase 4 of the development pipeline
(see the Unified Robust Coder Protocol v4.0).
"""


