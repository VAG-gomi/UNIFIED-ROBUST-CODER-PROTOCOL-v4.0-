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
