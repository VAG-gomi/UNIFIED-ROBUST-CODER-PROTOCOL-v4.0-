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
