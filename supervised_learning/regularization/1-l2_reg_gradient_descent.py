#!/usr/bin/env python3
"""Gradient Descent with L2 Regularization"""

import numpy as np

def l2_reg_gradient_descent(Y, weights, cache, alpha, lambtha, L):
    """ updates the weights and biases of a neural network using gradient
        descent with L2 regularization
    """
    m = Y.shape[1]
    la = L
    a = 'A' + str(la)
    W = 'W' + str(la)
    b = 'b' + str(la)
    dz = cache[a] - Y
    dw = (np.dot(cache['A' + str(la - 1)], dz.T) / m).T
    dw = dw + (lambtha / m) * weights[W]
    db = np.sum(dz, axis=1, keepdims=True) / m
    weights[W] = weights[W] - alpha * dw
    weights[b] = weights[b] - alpha * db

    for la in range(L - 1, 0, -1):
        a = 'A' + str(la)
        W = 'W' + str(la)
        b = 'b' + str(la)
        wNext = 'W' + str(la + 1)
        aNext = 'A' + str(la - 1)
        g = cache[a] * (1 - cache[a])
        dz = np.dot(weights[wNext].T, dz) * g
        dw = (np.dot(cache[aNext], dz.T) / m).T + ((lambtha / m) * weights[W])
        db = np.sum(dz, axis=1, keepdims=True) / m

        weights[W] = weights[W] - alpha * dw
        weights[b] = weights[b] - alpha * db
