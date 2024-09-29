#!/usr/bin/env python3
"""Adam"""

import numpy as np


def update_variables_Adam(alpha, beta1, beta2, epsilon, var, grad, v, s, t):
    """updates a variable in place using the Adam optimization algorithm"""
    Vd = beta1 * v + (1 - beta1) * grad
    Sd = beta2 * s + (1 - beta2) * grad ** 2
    Vd_corrected = Vd / (1 - beta1 ** t)
    Sd_corrected = Sd / (1 - beta2 ** t)
    var -= alpha * Vd_corrected / (Sd_corrected ** 0.5 + epsilon)
    return var, Vd, Sd
