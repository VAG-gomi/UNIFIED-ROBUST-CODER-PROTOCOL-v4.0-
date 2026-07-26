"""
tests.nn.test_linear
====================
Placeholder tests for core_neuron.nn.Linear (fully-connected layer).

Tests to be implemented:
    - ``test_output_shape``          – forward(x) shape is (batch, out_features).
    - ``test_bias_optional``         – layer with bias=False has no bias param.
    - ``test_weight_initialised``    – weights are non-zero after construction.
    - ``test_grad_flows_to_weight``  – backward pass populates weight.grad.
    - ``test_grad_flows_to_bias``    – backward pass populates bias.grad.
"""
