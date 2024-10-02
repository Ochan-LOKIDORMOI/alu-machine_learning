#!/usr/bin/env python3
"""F1 score calculation"""

import numpy as np
sensitivity = __import__('1-sensitivity').sensitivity
precision = __import__('2-precision').precision


def f1_score(confusion):
    """
    Calculates the F1 score for
    each class in a confusion matrix
    """
    sens = sensitivity(confusion)
    prec = precision(confusion)
    return 2 * sens * prec / (sens + prec)
