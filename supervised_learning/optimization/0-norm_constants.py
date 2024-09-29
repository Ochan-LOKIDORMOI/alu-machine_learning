#!/usr/bin/env python3
"""Normalization Constants"""

import tensorflow as tf


def normalization_constants(X):
    """Calculates the normalization (standardization)
    constants of a matrix
    """
    return tf.math.reduce_mean(X, axis=0), tf.math.reduce_std(X, axis= 0)