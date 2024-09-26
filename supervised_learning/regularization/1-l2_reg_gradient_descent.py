#!/usr/bin/env python3
"""Gradient Descent with L2 Regularization"""

import numpy as np
def l2_reg_gradient_descent(Y, weights, cache, alpha, lambtha, L):
    """ updates the weights and biases of a neural network using gradient
        descent with L2 regularization
    """
    m = Y.shape[1]
    for i in range(L, 0, -1):
        A = cache['A' + str(i)]
        if i == L:
            dz = A - Y
        else:
            dz = da * (1 - A**2)
        da = dz
        dW = (1/m) * np.matmul(dz, cache['A' + str(i - 1)].T) + \
             (lambtha/m) * weights['W' + str(i)]
        db = (1/m) * np.sum(dz, axis=1, keepdims=True)
        weights['W' + str(i)] -= alpha * dW
        weights['b' + str(i)] -= alpha * db
