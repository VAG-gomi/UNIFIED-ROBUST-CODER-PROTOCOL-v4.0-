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
