#!/usr/bin/env python3
"""
Defines class NST that performs tasks for neural style transfer
"""

import numpy as np
import tensorflow as tf


class NST:
    """
    Performs tasks for Neural Style Transfer

    public class attributes:
        style_layers = ['block1_conv1', 'block2_conv1', 'block3_conv1',
                        'block4_conv1', 'block5_conv1']
        content_layer = 'block5_conv2'

    instance attributes:
        style_image: preprocessed style image
        content_image: preprocessed style image
        alpha: weight for content cost
        beta: weight for style cost

    class constructor:
        def __init__(self, style_image, content_image, alpha=1e4, beta=1)

    static methods:
        def scale_image(image):
            rescales an image so the pixel values are between 0 and 1
                and the largest side is 512 pixels
    """
    style_layers = ['block1_conv1', 'block2_conv1', 'block3_conv1',
                    'block4_conv1', 'block5_conv1']
    content_layer = 'block5_conv2'

    def __init__(self, style_image, content_image, alpha=1e4, beta=1):
        """
        Class constructor for Neural Style Transfer class

        parameters:
            style_image [numpy.ndarray with shape (h, w, 3)]:
                image used as style reference
            content_image [numpy.ndarray with shape (h, w, 3)]:
                image used as content reference
            alpha [float]: weight for content cost
            beta [float]: weight for style cost

        Raises TypeError if input are in incorrect format
        Sets TensorFlow to execute eagerly
        Sets instance attributes
        """
        if type(style_image) is not np.ndarray or len(style_image.shape) != 3:
            raise TypeError(
                "style_image must be a numpy.ndarray with shape (h, w, 3)")
        if type(content_image) is not np.ndarray or len(content_image.shape) != 3:
            raise TypeError(
                "content_image must be a numpy.ndarray with shape (h, w, 3)")

        style_h, style_w, style_c = style_image.shape
        content_h, content_w, content_c = content_image.shape

        if style_h <= 0 or style_w <= 0 or style_c != 3:
            raise TypeError(
                "style_image must be a numpy.ndarray with shape (h, w, 3)")
        if content_h <= 0 or content_w <= 0 or content_c != 3:
            raise TypeError(
                "content_image must be a numpy.ndarray with shape (h, w, 3)")
        if (type(alpha) is not float and type(alpha) is not int) or alpha < 0:
            raise TypeError("alpha must be a non-negative number")
        if (type(beta) is not float and type(beta) is not int) or beta < 0:
            raise TypeError("beta must be a non-negative number")

        self.style_image = self.scale_image(style_image)
        self.content_image = self.scale_image(content_image)
        self.alpha = alpha
        self.beta = beta

        self.load_model()
        self.generate_features()

    @staticmethod
    def scale_image(image):
        """
        Rescales an image such that its pixels values are between 0 and 1
            and its largest side is 512 pixels

        parameters:
            image [numpy.ndarray of shape (h, w, 3)]:
                 image to be rescaled

        Scaled image should be tf.tensor with shape (1, h_new, w_new, 3)
            where max(h_new, w_new) is 512 and
            min(h_new, w_new) is scaled proportionately
        Image should be resized using bicubic interpolation.
        Image's pixels should be rescaled from range [0, 255] to [0, 1].

        returns:
            the scaled image
        """
        if type(image) is not np.ndarray or len(image.shape) != 3:
            raise TypeError(
                "image must be a numpy.ndarray with shape (h, w, 3)")
        h, w, c = image.shape
        if h <= 0 or w <= 0 or c != 3:
            raise TypeError(
                "image must be a numpy.ndarray with shape (h, w, 3)")
        if h > w:
            h_new = 512
            w_new = int(w * (512 / h))
        else:
            w_new = 512
            h_new = int(h * (512 / w))

        resized = tf.image.resize(image, (h_new, w_new), method='bicubic')
        rescaled = resized / 255.0
        rescaled = tf.clip_by_value(rescaled, 0.0, 1.0)
        return tf.expand_dims(rescaled, axis=0)

    def load_model(self):
        """
        Creates the model used to calculate cost.

        The model uses the VGG19 Keras model as a base.
        The model's input is the same as the VGG19 input.
        The model's output is a list containing the outputs of the VGG19
        layers listed in style_layers followed by content_layer.

        Saves the model in the instance attribute model.
        """
        vgg = tf.keras.applications.VGG19(include_top=False, weights='imagenet')
        vgg.trainable = False

        style_outputs = [vgg.get_layer(name).output for name in self.style_layers]
        content_output = vgg.get_layer(self.content_layer).output

        model_outputs = style_outputs + [content_output]

        self.model = tf.keras.Model(inputs=vgg.input, outputs=model_outputs)

    @staticmethod
    def gram_matrix(input_layer):
        """
        Calculates the Gram matrix of an input layer.

        parameters:
            input_layer [tf.Tensor of shape (1, h, w, c)]: layer output

        returns:
            Gram matrix as a tf.Tensor of shape (1, c, c)
        """
        if not isinstance(input_layer, tf.Tensor) or len(input_layer.shape) != 4:
            raise TypeError("input_layer must be a tensor of rank 4")

        _, h, w, c = input_layer.shape
        features = tf.reshape(input_layer, (-1, c))
        gram = tf.matmul(features, features, transpose_a=True)
        gram = tf.expand_dims(gram, axis=0)
        return gram / tf.cast(h * w, tf.float32)

    def generate_features(self):
        """
        Extracts the features used to calculate neural style cost.

        Sets instance attributes:
            gram_style_features: list of Gram matrices for the style layers
            content_feature: tensor for the content layer
        """
        preprocessed_style = tf.keras.applications.vgg19.preprocess_input(
            self.style_image * 255.0
        )
        preprocessed_content = tf.keras.applications.vgg19.preprocess_input(
            self.content_image * 255.0
        )

        style_outputs = self.model(preprocessed_style)[:-1]
        content_output = self.model(preprocessed_content)[-1]

        self.gram_style_features = [self.gram_matrix(output) for output in style_outputs]
        self.content_feature = content_output

    def layer_style_cost(self, style_output, gram_target):
        """
        Calculates the style cost for a single layer.

        parameters:
            style_output [tf.Tensor of shape (1, h, w, c)]: layer output
            gram_target [tf.Tensor of shape (1, c, c)]: target Gram matrix

        returns:
            Style cost for the layer
        """
        if not isinstance(style_output, tf.Tensor) or len(style_output.shape) != 4:
            raise TypeError("style_output must be a tensor of rank 4")

        if not isinstance(gram_target, tf.Tensor) or len(gram_target.shape) != 3:
            raise TypeError("gram_target must be a tensor of shape (1, c, c)")

        gram_style = self.gram_matrix(style_output)
        return tf.reduce_mean(tf.square(gram_style - gram_target))

    def style_cost(self, style_outputs):
        """
        Calculates the style cost for the generated image.

        parameters:
            style_outputs: list containing the outputs of the style layers

        returns:
            Total style cost
        """
        if not isinstance(style_outputs, list) or len(style_outputs) != len(self.style_layers):
            raise TypeError(
                "style_outputs must be a list with a length of {}".format(len(self.style_layers))
            )

        weight = 1.0 / len(self.style_layers)
        total_style_cost = tf.add_n([
            weight * self.layer_style_cost(style_output, gram_target)
            for style_output, gram_target in zip(style_outputs, self.gram_style_features)
        ])
        return total_style_cost
