#!/usr/bin/env python3
"""L2 Regularization Cost"""

import numpy as np


def l2_reg_cost(cost, lambtha, weights, L, m):
    """calculates the cost of a neural network with L2 regularization"""
    l2 = 0
    for i in range(1, L + 1):
        l2 += lambtha / (2 * m) * np.linalg.norm(weights['W' + str(i)])
    return cost + l2
