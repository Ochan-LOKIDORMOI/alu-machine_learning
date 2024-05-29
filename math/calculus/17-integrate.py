#!/usr/bin/env python3
"""Integrate"""


def poly_integral(poly, C=0):
    """calculates the integral of a polynomial"""
    if (not isinstance(poly, list) or
       (not isinstance(C, (int, float))) or any
       (not isinstance(x, (int, float)) for x in poly)):
        return None
    integral = [C]
    if poly != [0]:
        integral = [float(C)] + [poly[i] / (i + 1) for i in range(len(poly))]
    return [float(x) if not x.is_integer() else int(x) for x in integral]
