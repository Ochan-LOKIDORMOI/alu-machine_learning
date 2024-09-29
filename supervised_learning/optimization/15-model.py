#!/usr/bin/env python3
"""Put it all together and what do you get"""

import tensorflow as tf

def create_batch_norm_layer(prev, n, activation):
    """
    Creates a batch normalization
    layer for a neural network in tensorflow
    """
    init = tf.contrib.layers.variance_scaling_initializer(mode="FAN_AVG")
    layer = tf.layers.Dense(units=n, kernel_initializer=init)
    z = layer(prev)
    mean, variance = tf.nn.moments(z, axes=[0])
    beta = tf.Variable(tf.zeros([n]), trainable=True)
    gamma = tf.Variable(tf.ones([n]), trainable=True)
    epsilon = 1e-8
    batch_norm = tf.nn.batch_normalization(z, mean,
                                           variance, beta, gamma, epsilon)
    return activation(batch_norm)


def model(Data_train, Data_valid,
          layers, activations, alpha=0.001, beta1=0.9, beta2=0.999,
          epsilon=1e-8, decay_rate=1, batch_size=32, epochs=5,
          save_path='/tmp/model.ckpt'):
    """
    Function that builds, trains, and saves a
    neural network model in tensorflow using Adam optimization,
    mini-batch gradient descent, learning rate decay,
    and batch normalization
    """
    x, y = Data_train
    x_valid, y_valid = Data_valid
    tf.add_to_collection('x', x)
    tf.add_to_collection('y', y)
    tf.add_to_collection('x_valid', x_valid)
    tf.add_to_collection('y_valid', y_valid)
    tf.add_to_collection('alpha', alpha)
    tf.add_to_collection('beta1', beta1)
    tf.add_to_collection('beta2', beta2)
    tf.add_to_collection('epsilon', epsilon)
    tf.add_to_collection('decay_rate', decay_rate)
    tf.add_to_collection('batch_size', batch_size)
    tf.add_to_collection('epochs', epochs)
    tf.add_to_collection('save_path', save_path)
    with tf.Session() as sess:
        x = tf.placeholder(tf.float32, shape=(None, x.shape[1]), name='x')
        y = tf.placeholder(tf.float32, shape=(None, y.shape[1]), name='y')
        x_valid = tf.placeholder(tf.float32, shape=(None, x_valid.shape[1]), name='x_valid')
        y_valid = tf.placeholder(tf.float32, shape=(None, y_valid.shape[1]), name='y_valid')
        alpha = tf.placeholder(tf.float32, name='alpha')
        beta1 = tf.placeholder(tf.float32, name='beta1')
        beta2 = tf.placeholder(tf.float32, name='beta2')
        epsilon = tf.placeholder(tf.float32, name='epsilon')
        decay_rate = tf.placeholder(tf.float32, name='decay_rate')
        batch_size = tf.placeholder(tf.int32, name='batch_size')
        epochs = tf.placeholder(tf.int32, name='epochs')
        save_path = tf.placeholder(tf.string, name='save_path')
        y_pred = create_batch_norm_layer(x, layers[0], activations[0])
        for i in range(1, len(layers)):
            y_pred = create_batch_norm_layer(y_pred, layers[i],
                                             activations[i])
        loss = tf.losses.mean_squared_error(y, y_pred)
        accuracy = tf.reduce_mean(tf.cast(tf.equal(tf.argmax(y, 1),
                                                   tf.argmax(y_pred, 1)),
                                          tf.float32))
        global_step = tf.Variable(0, trainable=False)
        decayed_learning_rate = tf.train.inverse_time_decay(alpha,
                                                            global_step, decay_rate,
                                                            1, staircase=True)