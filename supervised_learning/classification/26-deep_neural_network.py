#!/usr/bin/env python3
"""Persistence is Key"""

import numpy as np


class DeepNeuralNetwork:
    """ defines a deep neural network
    performing binary classification"""

    def __init__(self, nx, layers):
        """class constructor"""
        if not isinstance(nx, int):
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")
        if not isinstance(layers, list) or len(layers) == 0:
            raise TypeError('layers must be a list of positive integers')
        self.__L = len(layers)
        self.__cache = {}
        self.__weights = {}
        for i in range(self.L):
            if not isinstance(layers[i], int) or layers[i] < 1:
                raise TypeError('layers must be a list of positive integers')
            w = 'W' + str(i + 1)
            b = 'b' + str(i + 1)
            prev = layers[i - 1] if i else nx
            sqrt = np.sqrt(2 / prev)
            self.__weights[w] = np.random.randn(layers[i], prev) * sqrt
            self.__weights[b] = np.zeros(shape=(layers[i], 1))

    @property
    def L(self):
        """returns the number of layers in the neural network"""
        return self.__L

    @property
    def weights(self):
        """returns a dict with all intermediary values of the network"""
        return self.__weights

    @property
    def cache(self):
        """returns a dict with all weights and biased of the network"""
        return self.__cache

    def forward_prop(self, X):
        """calculates the forward propagation of the neural network"""

    def cost(self, Y, A):
        """calculates the cost of the model using logistic regression"""

    def gradient_descent(self, Y, cache, alpha=0.05):
        """calculates one pass of gradient descent on the neural network"""

    def train(self, X, Y, iterations=5000, alpha=0.05,
              verbose=True, graph=True, step=100):
        """trains the deep neural network by updating its private attributes"""

    def save(self, filename):
        """saves the instance object to a file in pickle format"""

    @staticmethod
    def load(filename):
        """loads a pickled DeepNeuralNetwork object"""
