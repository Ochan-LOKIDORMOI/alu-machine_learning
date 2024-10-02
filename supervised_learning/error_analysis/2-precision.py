#!/usr/bin/env python3
"""Precision of a confusion matrix"""


import numpy as np


def precision(confusion):
    """
    Calculates the precision for
    each class in a confusion matrix
    """
    return np.diag(confusion) / np.sum(confusion, axis=0)
