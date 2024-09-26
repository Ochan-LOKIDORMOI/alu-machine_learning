#!/usr/bin/env python3
"""Gradient descent with L2 regularization"""


import numpy as np


def l2_reg_gradient_descent(Y, weights, cache, alpha, lambtha, L):
    """ updates the weights and biases of a neural network using gradient
        descent with L2 regularization
        Y: (numpy.ndarray) one-hot encoded labels of the data
        weights: (dict) weights and biases of the network
        cache: (dict) output of each layer
        alpha: (float) learning rate
        lambtha: (float) regularization parameter
        L: (int) number of layers in the network
        Returns: None
    """
    m = Y.shape[1]
    dz = cache["A" + str(L)] - Y
    for i in range(L, 0, -1):
        A = cache["A" + str(i - 1)]
        W = weights["W" + str(i)]
        b = weights["b" + str(i)]
        dw = (1 / m) * np.matmul(dz, A.T) + (lambtha / m) * W
        db = (1 / m) * np.sum(dz, axis=1, keepdims=True)
        dz = np.matmul(W.T, dz) * (A * (1 - A))
        weights["W" + str(i)] = weights["W" + str(i)] - alpha * dw
        weights["b" + str(i)] = weights["b" + str(i)] - alpha * db
