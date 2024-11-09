#!/usr/bin/env python3

import tensorflow as tf
import tensorflow_datasets as tfds
import matplotlib.pyplot as plt

def crop_image(image, size):
    """
    Performs a random crop of an image.
    - image: tf.Tensor, 3D tensor representing the image to crop.
    - size: tuple, containing the desired crop size (height, width, channels).
    - A tf.Tensor of the cropped image.
    """
    cropped_image = tf.image.random_crop(image, size)
    return cropped_image

if __name__ == "__main__":
    doggies = tfds.load("stanford_dogs", split="train", as_supervised=True)
    for image, _ in doggies.shuffle(10).take(1):
        plt.imshow(crop_image(image, (200, 200, 3)))
        plt.show()