#!/usr/bin/env python3
"""Layers"""


import tensorflow as tf


def create_layer(prev, n, activation):
    """The is the function that create a layer

    prev: is the tensor output of the previous layer
    n: is the number of nodes in the layer to create
    activation: is the activation function that the layer should be

    Return: the tensor output of the layer"""
    heetal = tf.contrib.layers.variance_scaling_initializer(mode="FAN_AVG")
    layer = tf.keras.layers.Dense(n, activation, kernel_initializer=heetal)
    return layer(prev)

