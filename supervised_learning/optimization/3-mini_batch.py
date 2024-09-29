#!/usr/bin/env python3
"""Mini-Batch"""

import tensorflow as tf

def train_mini_batch(X_train, Y_train, X_valid, Y_valid, batch_size=32,
                     epochs=5, load_path="/tmp/model.ckpt", save_path="/tmp/model.ckpt"):
    """
    Function that trains a loaded neural network
    model using mini-batch gradient descent
    """
    with tf.Session() as sess:
        saver = tf.train.import_meta_graph(load_path + ".meta")
        saver.restore(sess, load_path)
        x = tf.get_collection("x")[0]
        y = tf.get_collection("y")[0]
        loss = tf.get_collection("loss")[0]
        accuracy = tf.get_collection("accuracy")[0]
        train_op = tf.get_collection("train_op")[0]
        for epoch in range(epochs + 1):
            t_loss = sess.run(loss, feed_dict={x: X_train, y: Y_train})
            t_accuracy = sess.run(accuracy, feed_dict={x: X_train, y: Y_train})
            v_loss = sess.run(loss, feed_dict={x: X_valid, y: Y_valid})
            v_accuracy = sess.run(accuracy, feed_dict={x: X_valid, y: Y_valid})
            print("After {} epochs:".format(epoch))
            print("\tTraining Cost: {}".format(t_loss))
            print("\tTraining Accuracy: {}".format(t_accuracy))
            print("\tValidation Cost: {}".format(v_loss))
            print("\tValidation Accuracy: {}".format(v_accuracy))
            if epoch < epochs:
                for i in range(0, X_train.shape[0], batch_size):
                    X_batch = X_train[i:i + batch_size]
                    Y_batch = Y_train[i:i + batch_size]
                    sess.run(train_op, feed_dict={x: X_batch, y: Y_batch})
                    if i != 0 and (i / batch_size + 1) % 100 == 0:
                        b_loss = sess.run(loss, feed_dict={x: X_batch, y: Y_batch})
                        b_accuracy = sess.run(accuracy, feed_dict={x: X_batch, y: Y_batch})
                        print("\tStep {}:".format(i // batch_size + 1))
                        print("\t\tCost: {}".format(b_loss))
                        print("\t\tAccuracy: {}".format(b_accuracy))
        return saver.save(sess, save_path)
