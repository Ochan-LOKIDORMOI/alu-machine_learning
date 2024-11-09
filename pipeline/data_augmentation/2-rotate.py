#!/usr/bin/env python3

import tensorflow as tf
import tensorflow_datasets as tfds
import matplotlib.pyplot as plt

def rotate_image(image):
    """
    Rotates an image by 90 degrees counter-clockwise.
    - image: tf.Tensor, 3D tensor representing the image to rotate.
    - A tf.Tensor of the rotated image.
    """
    rotated_image = tf.image.rot90(image, k=1)
    return rotated_image

if __name__ == '__main__':
    doggies = tfds.load('stanford_dogs', split='train', as_supervised=True)
    for image, _ in doggies.shuffle(10).take(1):
        plt.imshow(rotate_image(image))
        plt.show()