#!/usr/bin/env python3
"""Create Confusion"""

import numpy as np


def create_confusion_matrix(labels, logits, classes):
    """creates a confusion matrix"""
    confusion = np.zeros((classes, classes))
    for i in range(len(labels)):
        confusion[labels[i]][np.argmax(logits[i])] += 1
    return confusion

