#!/usr/bin/env python3
"""Put it all together and what do you get"""

import numpy as np
import tensorflow as tf


def model(Data_train, Data_valid, layers,
          activations, alpha=0.001, beta1=0.9,
          beta2=0.999, epsilon=1e-8, decay_rate=1,
          batch_size=32, epochs=5, save_path='/tmp/model.ckpt'):
    """
    Function that builds, trains, and saves
    a neural network model in tensorflow using Adam
    optimization, mini-batch gradient descent, learning rate decay,
    and batch normalization
    """
    x_train, y_train = Data_train
    x_valid, y_valid = Data_valid

    x = tf.placeholder(tf.float32, shape=(None, x_train.shape[1]), name='x')
    y = tf.placeholder(tf.float32, shape=(None, y_train.shape[1]), name='y')

    for i in range(len(layers)):
        if i == 0:
            layer = tf.layers.Dense(layers[i],
                                    activation=activations[i],
                                    name='layer' + str(i))
            y_pred = layer(x)
        else:
            layer = tf.layers.Dense(layers[i],
                                    activation=activations[i],
                                    name='layer' + str(i))
            y_pred = layer(y_pred)

    loss = tf.losses.softmax_cross_entropy(y, y_pred)
    optimizer = tf.train.AdamOptimizer(alpha, beta1, beta2, epsilon)

    train_op = optimizer.minimize(loss)
    accuracy = tf.metrics.accuracy(y, y_pred)
    init = tf.global_variables_initializer()
    saver = tf.train.Saver()

    with tf.Session() as sess:
        sess.run(init)
        sess.run(tf.local_variables_initializer())

        for i in range(epochs + 1):
            loss_t = sess.run(loss, feed_dict={x: x_train, y: y_train})
            acc_t = sess.run(accuracy, feed_dict={x: x_train, y: y_train})
            loss_v = sess.run(loss, feed_dict={x: x_valid, y: y_valid})
            acc_v = sess.run(accuracy, feed_dict={x: x_valid, y: y_valid})

            print('After {} epochs:'.format(i))
            print('\tTraining Cost: {}'.format(loss_t))
            print('\tTraining Accuracy: {}'.format(acc_t))
            print('\tValidation Cost: {}'.format(loss_v))
            print('\tValidation Accuracy: {}'.format(acc_v))

            if i < epochs:
                x_t = x_train
                y_t = y_train
                for j in range(0, x_train.shape[0], batch_size):
                    x_t = x_train[j:j + batch_size]
                    y_t = y_train[j:j + batch_size]
                    sess.run(train_op, feed_dict={x: x_t, y: y_t})
