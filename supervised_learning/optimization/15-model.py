#!/usr/bin/env python3
"""Put it all together and what do you get"""

import tensorflow as tf


def model(Data_train, Data_valid, layers, activations,
          alpha=0.001, beta1=0.9, beta2=0.999, epsilon=1e-8,
          decay_rate=1, batch_size=32, epochs=5, save_path='/tmp/model.ckpt'):
    """
    Data_train is a tuple containing the training inputs
    and training labels, respectively
    Data_valid is a tuple containing the validation
    inputs and validation labels, respectively
    layers is a list containing the number of nodes
    in each layer of the network
    activations is a list containing the activation
    functions for each layer of the network
    alpha is the learning rate
    beta1 is the weight for the first
    moment of Adam Optimization
    beta2 is the weight for the second moment of Adam Optimization
    epsilon is a small number used to avoid division by zero
    decay_rate is the decay rate for inverse time
    decay of the learning rate
    batch_size is the number of data points
    that should be in a mini-batch
    epochs is the number of times the training
    should pass through the data set
    save_path is the path where the model should be saved to
    Returns: the path where the model was saved
    """
    x = tf.placeholder(tf.float32, shape=[None, Data_train[0].shape[1]], name='x')
    y = tf.placeholder(tf.float32, shape=[None, Data_train[1].shape[1]], name='y')
    tf.add_to_collection('x', x)
    tf.add_to_collection('y', y)
    for i in range(len(layers)):
        if i == 0:
            init = tf.contrib.layers.variance_scaling_initializer(mode="FAN_AVG")
            x = tf.layers.Dense(units=layers[i], kernel_initializer=init)(x)
        else:
            init = tf.contrib.layers.variance_scaling_initializer(mode="FAN_AVG")
            x = tf.layers.Dense(units=layers[i], kernel_initializer=init)(x)
        if i < len(layers) - 1:
            mean, variance = tf.nn.moments(x, axes=[0])
            beta = tf.Variable(tf.constant(0.0, shape=[layers[i]]), trainable=True)
            gamma = tf.Variable(tf.constant(1.0, shape=[layers[i]]), trainable=True)
            epsilon = 1e-8
            x = tf.nn.batch_normalization(x, mean, variance, beta, gamma, epsilon)
            x = activations[i](x)
    y_pred = x
    loss = tf.losses.softmax_cross_entropy(y, y_pred)
    global_step = tf.Variable(0, trainable=False)
    alpha = tf.train.inverse_time_decay(alpha, global_step, decay_rate, staircase=True)