#!/usr/bin/env python3
"""Mini-Batch"""

import tensorflow as tf

def shuffle_data(X, Y):
    """Shuffles the data points in two matrices the same way"""
    permutation = np.random.permutation(X.shape[0])
    return X[permutation], Y[permutation]


def train_mini_batch(X_train, Y_train, X_valid, Y_valid, batch_size=32,
                     epochs=5, load_path="/tmp/model.ckpt", save_path="/tmp/model.ckpt"):
    """
    Function that trains a loaded neural
    network model using mini-batch gradient descent
    """

    with tf.Session() as sess:
        saver = tf.train.import_meta_graph(load_path + ".meta")
        saver.restore(sess, load_path)

        x = tf.get_collection('x')[0]
        y = tf.get_collection('y')[0]
        loss = tf.get_collection('loss')[0]
        accuracy = tf.get_collection('accuracy')[0]
        train_op = tf.get_collection('train_op')[0]

        for epoch in range(epochs + 1):
            train_cost, train_accuracy = sess.run([loss, accuracy], feed_dict={x: X_train, y: Y_train})
            valid_cost, valid_accuracy = sess.run([loss, accuracy], feed_dict={x: X_valid, y: Y_valid})
            print("After {} epochs:".format(epoch))
            print("\tTraining Cost: {}".format(train_cost))
            print("\tTraining Accuracy: {}".format(train_accuracy))
            print("\tValidation Cost: {}".format(valid_cost))
            print("\tValidation Accuracy: {}".format(valid_accuracy))

            if epoch < epochs:
                X_shuffled, Y_shuffled = shuffle_data(X_train, Y_train)
                for i in range(0, X_train.shape[0], batch_size):
                    X_mini = X_shuffled[i:i + batch_size]
                    Y_mini = Y_shuffled[i:i + batch_size]
                    sess.run(train_op, feed_dict={x: X_mini, y: Y_mini})

        save_path = saver.save(sess, save_path)
    return save_path
