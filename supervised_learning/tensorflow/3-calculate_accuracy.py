#!/usr/bin/env python3
"""Accuracy"""

import tensorflow as tf


def calculate_accuracy(y, y_pred):
    """Function that calculates the accuracy of a prediction

    y: is a placeholder for the labels of the input data
    y_pred: is a tensor containing the network's predictions

    Return: a tensor containing the decimal accuracy of the prediction"""
    accuracy = tf.equal(tf.argmax(y, axis=1), tf.argmax(y_pred, axis=1))
    return tf.reduce_mean(tf.cast(accuracy, tf.float32))
