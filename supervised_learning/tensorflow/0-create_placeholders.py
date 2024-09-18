#!/usr/bin/env python3

"""Placeholders"""


import tensorflow as tf


def create_placeholders(nx, classes):
    """
    Returns two placeholders, x and y, for the neural network.

    Arguments:
    nx -- number of feature columns in the data
    classes -- number of classes in the classifier

    Returns:
    x -- placeholder for the input data (shape: [None, nx])
    y -- placeholder for the one-hot labels (shape: [None, classes])
    """
    x = tf.placeholder('float32', shape=[None, nx], name='x')
    y = tf.placeholder('float32', shape=[None, classes], name='y')
    return x, y
