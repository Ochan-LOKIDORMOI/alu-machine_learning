#!/usr/bin/env python3
"""Specificity calculation"""

import numpy as np


def specificity(confusion):
    """
    Calculates the specificity for
    each class in a confusion matrix
    """
    TP = np.diagonal(confusion)
    FP = np.sum(confusion, axis=0) - TP
    FN = np.sum(confusion, axis=1) - TP
    TN = np.sum(confusion) - (TP + FP + FN)
    return TN / (TN + FP)
