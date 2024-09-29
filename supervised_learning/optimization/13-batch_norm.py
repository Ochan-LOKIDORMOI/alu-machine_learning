#!/usr/bin/env python3
""" Batch Normalization """

import numpy as np


def batch_norm(Z, gamma, beta, epsilon):
    """ 
    Normalizes an unactivated output of
    a neural network using batch norm
    """
    m = np.mean(Z, axis=0)
    s = np.var(Z, axis=0)
    Z_norm = (Z - m) / np.sqrt(s + epsilon)
    return gamma * Z_norm + beta
