#!/usr/bin/env python3
"""Train operation"""

import tensorflow as tf


def create_train_op(loss, alpha):
    """
    function that creates the training operation for the network
    loss is the loss of the networks prediction
    alpha is the learning rate
    Returns: an operation that trains the network using gradient descent
    """
    return tf.train.GradientDescentOptimizer(alpha).minimize(loss)
