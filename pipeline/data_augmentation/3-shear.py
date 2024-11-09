#!/usr/bin/env python3

import tensorflow as tf
import tensorflow_datasets as tfds
import matplotlib.pyplot as plt

def shear_image(image, intensity):
    """
    Randomly shears an image
        - image: 3d tf.tensor
        - intensity of the shear
        - sheared image
    """
    return tf.keras.preprocessing.image.random_shear(image, intensity=intensity)
    doggies = tfds.load("stanford_dogs", split="train", as_supervised=True)
    for image, _ in doggies.shuffle(10).take(1):
        plt.imshow(shear_image(image, 50))
        plt.show()