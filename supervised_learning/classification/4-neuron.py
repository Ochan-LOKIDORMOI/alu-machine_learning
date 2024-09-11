#!/usr/bin/env python3
"""Evaluate Neuron"""


from cmath import cos
import numpy as np


class Neuron:
    """This is a class that defines a single neuron performing
    binary classification"""

    def __init__(self, nx):
        """Class constructor

        nx: is the number of input features to the neuron"""
        if type(nx) is not int:
            raise TypeError('nx must be an integer')
        if nx < 1:
            raise ValueError('nx must be a positive integer')
        self.__W = np.random.normal(size=(1, nx))
        self.__b = 0
        self.__A = 0

    @property
    def W(self):
        """getter function of attribute W"""
        return self.__W

    @property
    def b(self):
        """getter function of attribute W"""
        return self.__b

    @property
    def A(self):
        """getter function of attribute W"""
        return self.__A

    def forward_prop(self, X):
        """Forward propagation of the neuron

        X: is a numpy.ndarray with shape (nx, m) that contains the input data

        Return: the private attribute A"""
        x = np.matmul(self.W, X) + self.b
        self.__A = 1 / (1 + np.e**(-x))
        return self.A

    def cost(self, Y, A):
        """The cost of the model in logistic
        regression

        Y: is a numpy.ndarray with shape (1, m) that contains the correct
        labels for the input data
        A: is a numpy.ndarray with shape (1, m) containing the activated
        output of the neuron for each example

        Return: the cost"""
        # To avoid division error I use 1.0000001 - A
        m = Y.shape[1]
        a = 1.0000001 - A
        x = - 1 / m * np.sum(Y * np.log(A) + (1 - Y) * np.log(a))
        return x

    def evaluate(self, X, Y):
        """The neuron predictions

        X: is a numpy.ndarray with shape (nx, m) that contains the input data
        Y: is a numpy.ndarray with shape (1, m) that contains the correct
        labels for the input data

        Return: The neuron prediction and the cost of the network respectively
        """
        A = self.forward_prop(X)
        evaluation = np.where(A >= 0.5, 1, 0)
        cost = self.cost(Y, self.A)
        return evaluation, cost