#!/usr/bin/env python3
"""Create Confusion"""

import numpy as np


def create_confusion_matrix(labels, logits, classes):
    """creates a confusion matrix"""
    m, classes = labels.shape
    confusion = np.zeros((classes, classes))
    for i in range(m):
        confusion[np.argmax(labels[i]), np.argmax(logits[i])] += 1
    return confusion
