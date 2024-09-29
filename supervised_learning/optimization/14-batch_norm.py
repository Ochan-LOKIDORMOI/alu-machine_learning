#!/usr/bin/env python3
"""Batch Normalization"""

import tensorflow as tf


def create_batch_norm_layer(prev, n, activation):
    """creates a batch normalization layer for a neural network in tensorflow"""
    init = tf.contrib.layers.variance_scaling_initializer(mode="FAN_AVG")
    x = tf.layers.Dense(units=n, kernel_initializer=init)(prev)
    mean, variance = tf.nn.moments(x, axes=[0])
    beta = tf.Variable(tf.constant(0.0, shape=[n]), trainable=True)
    gamma = tf.Variable(tf.constant(1.0, shape=[n]), trainable=True)
    epsilon = 1e-8
    x = tf.nn.batch_normalization(x, mean, variance, beta, gamma, epsilon)
    return activation(x)
