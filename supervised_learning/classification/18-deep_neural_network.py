#!/usr/bin/env python3
""""DeepNeuralNetwork Forward Propagation"""


import numpy as np


class DeepNeuralNetwork:
    """Defines a deep neural network performing binary classification"""

    def __init__(self, nx, layers):
        """
        Initializes the deep neural network
        
        nx: number of input features
        layers: list representing the number of nodes in each layer
        """
        if not isinstance(nx, int) or nx < 1:
            raise ValueError("nx must be a positive integer")
        if not isinstance(layers, list) or len(layers) == 0 or not all(isinstance(i, int) and i > 0 for i in layers):
            raise TypeError("layers must be a list of positive integers")

        self.L = len(layers)
        self.cache = {}
        self.weights = {}
        for i in range(self.L):
            if i == 0:
                self.weights['W1'] = np.random.randn(layers[0], nx) * np.sqrt(2 / nx)
            else:
                self.weights['W{}'.format(i + 1)] = np.random.randn(layers[i], layers[i - 1]) * np.sqrt(2 / layers[i - 1])
            self.weights['b{}'.format(i + 1)] = np.zeros((layers[i], 1))

    def forward_prop(self, X):
        """
        Calculates the forward propagation of the deep neural network
        
        X: input data, numpy.ndarray of shape (nx, m)
        """
        self.cache['A0'] = X
        for i in range(1, self.L + 1):
            Z = np.dot(self.weights['W{}'.format(i)], self.cache['A{}'.format(i - 1)]) + self.weights['b{}'.format(i)]
            self.cache['A{}'.format(i)] = 1 / (1 + np.exp(-Z))
        return self.cache['A{}'.format(self.L)], self.cache

    def cost(self, Y, A):
        """
        Calculates the cost of the model using logistic regression
        
        Y: numpy.ndarray with shape (1, m) containing the correct labels
        A: numpy.ndarray with shape (1, m) containing the activated output
        """
        m = Y.shape[1]
        cost = -np.sum(Y * np.log(A) + (1 - Y) * np.log(1.0000001 - A)) / m
        return cost
