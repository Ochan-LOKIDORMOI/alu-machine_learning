#!/usr/bin/env python3
""" Multiple Kernels"""


import numpy as np


def convolve(images, kernels, padding='same', stride=(1, 1)):
    """A convolution on images using multiple kernels:

    images is a numpy.ndarray with shape (m, h, w, c) containing multiple
    images
        m is the number of images
        h is the height in pixels of the images
        w is the width in pixels of the images
        c is the number of channels in the image
    kernels is a numpy.ndarray with shape (kh, kw, c, nc) containing the
    kernels for the convolution
        kh is the height of a kernel
        kw is the width of a kernel
        nc is the number of kernels
    padding is either a tuple of (ph, pw), ‘same’, or ‘valid’
        if ‘same’, performs a same convolution
        if ‘valid’, performs a valid convolution
        if a tuple:
            ph is the padding for the height of the image
            pw is the padding for the width of the image
    the image should be padded with 0’s
    stride is a tuple of (sh, sw)
        sh is the stride for the height of the image
        sw is the stride for the width of the image

    Returns: a numpy.ndarray containing the convolved images"""
m, h, w, c = images.shape
    kh, kw, _, nc = kernels.shape
    sh, sw = stride

    if padding == 'same':
        ph = ((h - 1) * sh + kh - h) // 2 + 1
        pw = ((w - 1) * sw + kw - w) // 2 + 1
    elif padding == 'valid':
        ph = pw = 0
    else:
        ph, pw = padding

    padded_h = h + 2 * ph
    padded_w = w + 2 * pw

    output_h = (padded_h - kh) // sh + 1
    output_w = (padded_w - kw) // sw + 1

    padding_values = ((0, 0), (ph, ph), (pw, pw), (0, 0))
    padded_images = np.pad(images, padding_values, mode='constant')

    output = np.zeros((m, output_h, output_w, nc))

    for i in range(output_h):
        for j in range(output_w):
            for k in range(nc):
                image_slice = padded_images[:, i*sh:i*sh+kh, j*sw:j*sw+kw, :]
                kernel = kernels[:, :, :, k]
                output[:, i, j, k] = np.sum(image_slice * kernel, axis=(1, 2, 3))

    return output
