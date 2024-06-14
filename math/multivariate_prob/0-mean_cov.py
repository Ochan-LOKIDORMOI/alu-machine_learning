#!/usr/bin/env python3
"""mean and covariance"""


import numpy as np


def mean_cov(X):
    """Calculating the covariance of dataset

    X is a numpy.ndarray of shape (n, d) containing the data set:
        n is the number of data points
        d is the number of dimensions in each data point
    If X is not a 2D numpy.ndarray, raise a TypeError with the message X
    must be a 2D numpy.ndarray
    """
    if len(X.shape) != 2 or type(X) is not np.ndarray:
        raise TypeError('X must be a 2D numpy.ndarray')
    data, dim = X.shape
    if data < 2:
        raise ValueError('X must contain multiple data points')
    mean = np.mean(X, axis=0).reshape(1, dim)
    x = X - mean
    cov = (x.T @ x) / (data - 1)
    return mean, cov
