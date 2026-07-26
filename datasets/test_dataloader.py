"""
tests.datasets.test_dataloader
===============================
Placeholder tests for core_neuron.datasets.DataLoader.

Tests to be implemented:
    - ``test_batch_size_respected``    – each yielded batch has <= batch_size samples.
    - ``test_last_batch_drop``         – drop_last removes the incomplete final batch.
    - ``test_shuffle_reorders``        – shuffled epoch is not identical to original order.
    - ``test_epoch_length``            – number of batches matches ceil(N / batch_size).
    - ``test_deterministic_with_seed`` – same seed produces same iteration order.
"""
