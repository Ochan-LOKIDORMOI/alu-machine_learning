#!/usr/bin/env python3
"""Sensitivity of a confusion matrix"""

import numpy as np


def sensitivity(confusion):
    """
    Calculates the sensitivity for
    each class in a confusion matrix
    """
    return np.diag(confusion) / np.sum(confusion, axis=1)
