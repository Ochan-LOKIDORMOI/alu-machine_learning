#!/usr/bin/env python3

import tensorflow as tf
import tensorflow_datasets as tfds
import matplotlib.pyplot as plt

def change_hue(image, delta):
    """
    Changes the hue of an image.
    - image: tf.Tensor, 3D tensor representing the image to adjust.
    - delta: float, the amount to adjust the hue by (between -1 and 1).
    - A tf.Tensor of the altered image.
    """
    adjusted_image = tf.image.adjust_hue(image, delta)
    return adjusted_image

if __name__ == "__main__":
    doggies = tfds.load("stanford_dogs", split="train", as_supervised=True)
    for image, _ in doggies.shuffle(10).take(1):
        plt.imshow(change_hue(image, -0.5))
        plt.show()