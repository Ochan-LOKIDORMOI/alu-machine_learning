#!/usr/bin/env python3
"""Neural Style Transfer Module"""

import numpy as np
import tensorflow as tf

class NST:
    style_layers = ['block1_conv1', 'block2_conv1', 'block3_conv1', 'block4_conv1', 'block5_conv1']
    content_layer = 'block5_conv2'

    def __init__(self, style_image, content_image, alpha=1e4, beta=1):
        # Validate style_image
        if not isinstance(style_image, np.ndarray) or style_image.ndim != 3 or style_image.shape[2] != 3:
            raise TypeError("style_image must be a numpy.ndarray with shape (h, w, 3)")
        
        # Validate content_image
        if not isinstance(content_image, np.ndarray) or content_image.ndim != 3 or content_image.shape[2] != 3:
            raise TypeError("content_image must be a numpy.ndarray with shape (h, w, 3)")
        
        # Validate alpha
        if not (isinstance(alpha, (int, float)) and alpha >= 0):
            raise TypeError("alpha must be a non-negative number")
        
        # Validate beta
        if not (isinstance(beta, (int, float)) and beta >= 0):
            raise TypeError("beta must be a non-negative number")

        # Set TensorFlow to execute eagerly
        tf.config.run_functions_eagerly(True)

        # Set instance attributes
        self.style_image = self.scale_image(style_image)
        self.content_image = self.scale_image(content_image)
        self.alpha = alpha
        self.beta = beta

    @staticmethod
    def scale_image(image):
        # Validate image
        if not isinstance(image, np.ndarray) or image.ndim != 3 or image.shape[2] != 3:
            raise TypeError("image must be a numpy.ndarray with shape (h, w, 3)")

        # Get original dimensions
        h, w, _ = image.shape

        # Determine new size maintaining aspect ratio
        if h > w:
            new_h = 512
            new_w = int(512 * w / h)
        else:
            new_w = 512
            new_h = int(512 * h / w)

        # Resize the image using bicubic interpolation
        image_resized = tf.image.resize(image, [new_h, new_w], method='bicubic')

        # Rescale pixel values from [0, 255] to [0, 1]
        image_scaled = image_resized / 255.0

        # Add batch dimension and return as tensor
        return tf.expand_dims(image_scaled, axis=0)