#!/usr/bin/env python3
"""
This module defines a class for performing Neural Style Transfer (NST).
"""

import numpy as np
import tensorflow as tf


class NST:
    """
    A class to implement Neural Style Transfer (NST).

    Class-level attributes:
        style_layers (list of str): Names of layers used for style extraction.
        content_layer (str): Name of the layer used for content extraction.

    Instance attributes:
        style_image (numpy.ndarray): The processed image for style reference.
        content_image (numpy.ndarray): The processed image for content reference.
        alpha (float): The weight for the content loss term.
        beta (float): The weight for the style loss term.

    Methods:
        __init__(style_image, content_image, alpha, beta):
            Initializes the NST object with style and content images, and optional weights.
        scale_image(image):
            Scales an input image for style transfer by resizing and normalizing.
    """
    
    style_layers = ['block1_conv1', 'block2_conv1', 'block3_conv1',
                    'block4_conv1', 'block5_conv1']
    content_layer = 'block5_conv2'

    def __init__(self, style_image, content_image, alpha=1e4, beta=1):
        """
        Initializes the NST object for style transfer.

        Args:
            style_image (numpy.ndarray): The image representing the desired style.
            content_image (numpy.ndarray): The image to be used as content reference.
            alpha (float): The content loss weight factor (default is 1e4).
            beta (float): The style loss weight factor (default is 1).

        Raises:
            TypeError: If any input is of the wrong type or dimension.
        """
        if not isinstance(style_image, np.ndarray) or len(style_image.shape) != 3:
            raise TypeError("style_image should be a 3D numpy array with shape (h, w, 3)")
        if not isinstance(content_image, np.ndarray) or len(content_image.shape) != 3:
            raise TypeError("content_image should be a 3D numpy array with shape (h, w, 3)")

        # Check valid dimensions
        style_h, style_w, style_c = style_image.shape
        content_h, content_w, content_c = content_image.shape
        if style_h <= 0 or style_w <= 0 or style_c != 3:
            raise TypeError("style_image must have valid height, width, and 3 color channels")
        if content_h <= 0 or content_w <= 0 or content_c != 3:
            raise TypeError("content_image must have valid height, width, and 3 color channels")
        
        # Validate weights
        if not isinstance(alpha, (float, int)) or alpha < 0:
            raise TypeError("alpha must be a non-negative number")
        if not isinstance(beta, (float, int)) or beta < 0:
            raise TypeError("beta must be a non-negative number")

        tf.enable_eager_execution()

        self.style_image = self.scale_image(style_image)
        self.content_image = self.scale_image(content_image)
        self.alpha = alpha
        self.beta = beta

        self._initialize_model()

    @staticmethod
    def scale_image(image):
        """
        Resizes and normalizes an image to prepare it for the neural network.

        The resized image will have its largest side scaled to 512 pixels,
        and the pixel values will be normalized to the range [0, 1].

        Args:
            image (numpy.ndarray): The input image to be processed.

        Returns:
            tf.Tensor: The scaled and normalized image.
        """
        if not isinstance(image, np.ndarray) or len(image.shape) != 3:
            raise TypeError("image must be a 3D numpy array with shape (h, w, 3)")

        h, w, c = image.shape
        if h <= 0 or w <= 0 or c != 3:
            raise TypeError("image must have valid height, width, and 3 color channels")

        # Calculate new dimensions
        if h > w:
            new_h = 512
            new_w = int(w * (512 / h))
        else:
            new_w = 512
            new_h = int(h * (512 / w))

        # Resize image using bicubic interpolation
        resized_image = tf.image.resize_bicubic(np.expand_dims(image, axis=0), size=(new_h, new_w))
        # Normalize pixel values to [0, 1]
        normalized_image = resized_image / 255
        normalized_image = tf.clip_by_value(normalized_image, 0, 1)
        
        return normalized_image

    def _initialize_model(self):
        """
        Loads the pre-trained VGG19 model and configures it to extract features
        from the layers used for style and content.

        The VGG19 model is used as a feature extractor, and the outputs from the
        layers defined in `style_layers` and `content_layer` are stored in the
        instance attribute `model`.
        """
        # Load the VGG19 model with ImageNet weights
        vgg_model = tf.keras.applications.VGG19(include_top=False, weights='imagenet')
        vgg_model.save("VGG19_base_model")

        custom_objects = {'MaxPooling2D': tf.keras.layers.AveragePooling2D}

        # Reload the model with custom layers
        vgg = tf.keras.models.load_model("VGG19_base_model", custom_objects=custom_objects)

        style_outputs = []
        content_output = None

        # Extract outputs from the specified layers
        for layer in vgg.layers:
            if layer.name in self.style_layers:
                style_outputs.append(layer.output)
            if layer.name == self.content_layer:
                content_output = layer.output
            layer.trainable = False

        # Combine style and content layer outputs
        model_outputs = style_outputs + [content_output]

        # Create a new model with the desired outputs
        self.model = tf.keras.models.Model(vgg.input, model_outputs)
