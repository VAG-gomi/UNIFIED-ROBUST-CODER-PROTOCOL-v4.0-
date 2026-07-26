"""
tests.losses.test_classification
=================================
Placeholder tests for core_neuron.losses classification losses.

Tests to be implemented:
    - ``test_bce_perfect_prediction``    – BCE is ~0 when sigmoid(pred) ≈ target.
    - ``test_bce_clipped``               – BCE does not produce -inf / inf.
    - ``test_cross_entropy_argmax``      – loss is lower when correct class is highest logit.
    - ``test_cross_entropy_uniform``     – uniform logits produce maximum entropy loss.
    - ``test_nll_matches_cross_entropy`` – NLL(log_softmax(x)) == cross_entropy(x).
    - ``test_reduction_mean``            – mean reduction averages over batch.
"""
