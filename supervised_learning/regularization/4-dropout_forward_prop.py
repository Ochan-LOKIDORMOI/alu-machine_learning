#!/usr/bin/env python3
"""Forward Propagation with Dropout"""

import numpy as np


def dropout_forward_prop(X, weights, L, keep_prob):
    """conducts forward propagation using Dropout"""
    cache = {}
    cache['A0'] = X
    for i in range(1, L + 1):
        Z = np.matmul(weights['W' + str(i)],
                      cache['A' + str(i - 1)]) + weights['b' + str(i)]
        if i == L:
            cache['A' + str(i)] = np.exp(Z) / np.sum(np.exp(Z),
                                                     axis=0, keepdims=True)
        else:
            cache['A' + str(i)] = np.tanh(Z)
            cache['D' + str(i)] = np.random.rand(cache['A' + str(i)].shape[0],
                                                 cache['A' + str(i)].shape[1])
            cache['D' + str(i)] = np.where(cache['D' + str(i)]
                                           < keep_prob, 1, 0)
            cache['A' + str(i)] *= cache['D' + str(i)]
            cache['A' + str(i)] /= keep_prob
    return cache
