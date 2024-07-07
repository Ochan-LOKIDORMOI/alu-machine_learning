#!/usr/bin/env python3
"""Pooling"""


import numpy as np


def pool(images, kernel_shape, stride, mode='max'):
    """Pooling on images:

    images is a numpy.ndarray with shape (m, h, w, c) containing multiple
    images
        m is the number of images
        h is the height in pixels of the images
        w is the width in pixels of the images
        c is the number of channels in the image
    kernel_shape is a tuple of (kh, kw) containing the kernel shape for the
    pooling
        kh is the height of the kernel
        kw is the width of the kernel
    stride is a tuple of (sh, sw)
        sh is the stride for the height of the image
        sw is the stride for the width of the image
    mode indicates the type of pooling
        max indicates max pooling
        avg indicates average pooling

    Returns: a numpy.ndarray containing the pooled images"""
    m, h, w, c = images.shape
    kh, kw = kernel_shape
    sh, sw = stride

    output_h = (h - kh) // sh + 1
    output_w = (w - kw) // sw + 1

    pooled = np.zeros((m, output_h, output_w, c))

    for i in range(output_h):
        for j in range(output_w):
            i_start = i * sh
            i_end = i_start + kh
            j_start = j * sw
            j_end = j_start + kw

            image_slice = images[:, i_start:i_end, j_start:j_end, :]

            if mode == 'max':
                pooled[:, i, j, :] = np.max(
                    image_slice, axis=(1, 2)
                )
            elif mode == 'avg':
                pooled[:, i, j, :] = np.mean(
                    image_slice, axis=(1, 2)
                )

    return pooled
