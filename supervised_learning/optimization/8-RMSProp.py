#!/usr/bin/env python3
"""RMSProp Upgraded"""

import tensorflow as tf


def create_RMSProp_op(loss, alpha, beta2, epsilon):
    """creates the training operation for a neural network in tensorflow
    using the RMSProp optimization algorithm"""
    optimizer = tf.train.RMSPropOptimizer(alpha, beta2, epsilon)
    train = optimizer.minimize(loss)
    return train

