#!/usr/bin/env python3
"""Shuffle Data"""

import numpy as np


def shuffle_data(X, Y):
    """Function that shuffles the data points in two matrices the same way"""
    shuffle = np.random.permutation(X.shape[0])
    return X[shuffle], Y[shuffle]
