#!/usr/bin/env python3
"""F1 score calculation"""

import numpy as np


def f1_score(confusion):
    """
    Calculates the F1 score for
    each class in a confusion matrix
    """
    TP = np.diagonal(confusion)
    FP = np.sum(confusion, axis=0) - TP
    FN = np.sum(confusion, axis=1) - TP
    precision = TP / (TP + FP)
    recall = TP / (TP + FN)
    return 2 * (precision * recall) / (precision + recall)
