#!/usr/bin/env python3

"""Neuron"""

import numpy as np

class Neuron:
    def __init__(self, nx):
        """ Check if nx is an integer"""
        if not isinstance(nx, int):
            raise TypeError("nx must be an integer")
        """ Check if nx is greater than 0"""
        if nx < 1:
            raise ValueError("nx must be positive")
        
        """Initialize weights, bias, and activated output"""
        self.__W = np.random.randn(1, nx)
        self.__b = 0
        self.__A = 0

    @property
    def W(self):
        """Getter for the weights vector."""
        return self.__W

    @property
    def b(self):
        """Getter for the bias."""
        return self.__b

    @property
    def A(self):
        """Getter for the activated output (prediction)."""
        return self.__A

