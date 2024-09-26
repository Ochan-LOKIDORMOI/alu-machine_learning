#!/usr/bin/env python3
"""Gradient Descent with Dropout"""

import umpy as np

def dropout_gradient_descent(Y, weights, cache, alpha, keep_prob, L):
    """
    Updates the weights of a neural network with
    Dropout regularization using gradient descent
    """
    m = Y.shape[1]
    dZ = cache['A' + str(L)] - Y
    for i in range(L, 0, -1):
        A_prev = cache['A' + str(i - 1)]
        dW = np.matmul(dZ, A_prev.T) / m
        db = np.sum(dZ, axis=1, keepdims=True) / m
        dZ = np.matmul(weights['W' + str(i)].T, dZ) * (1 - (A_prev ** 2))
        if i > 1:
            dZ *= cache['D' + str(i - 1)]
            dZ /= keep_prob
        weights['W' + str(i)] -= alpha * dW
        weights['b' + str(i)] -= alpha * db
