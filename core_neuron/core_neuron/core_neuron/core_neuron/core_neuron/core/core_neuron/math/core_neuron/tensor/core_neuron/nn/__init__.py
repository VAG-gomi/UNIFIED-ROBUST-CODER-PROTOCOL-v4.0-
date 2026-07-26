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
