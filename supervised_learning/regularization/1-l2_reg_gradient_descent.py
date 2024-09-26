#!/usr/bin/env python3
"""Gradient descent with L2 regularization"""


import numpy as np


def l2_reg_gradient_descent(Y, weights, cache, alpha, lambtha, L):
    """
    Updates the weights and biases of a neural network using gradient descent with L2 regularization.

    Parameters:
    - Y: numpy.ndarray of shape (classes, m) containing the correct labels for the data
    - weights: dictionary of the weights and biases of the neural network
    - cache: dictionary of the outputs of each layer of the neural network
    - alpha: learning rate
    - lambtha: L2 regularization parameter
    - L: number of layers of the network
    """
    m = Y.shape[1]
    dZ = cache["A" + str(L)] - Y  # dZ for the last layer (softmax)

    for i in range(L, 0, -1):
        A_prev = cache["A" + str(i - 1)] if i > 1 else cache["A0"]
        W = weights["W" + str(i)]
        b = weights["b" + str(i)]

        # Compute gradients for weights and biases
        dW = (np.dot(dZ, A_prev.T) / m) + (lambtha / m) * W
        db = np.sum(dZ, axis=1, keepdims=True) / m

        if i > 1:
            # Compute dZ for the previous layer (before softmax/tanh)
            dA_prev = np.dot(W.T, dZ)
            dZ = dA_prev * (1 - A_prev ** 2)
        weights["W" + str(i)] -= alpha * dW
        weights["b" + str(i)] -= alpha * db
