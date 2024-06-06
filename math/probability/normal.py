#!/usr/bin/env python3
"""Normal distribution"""


class Normal:
    """Normal class that represents a normal distribution"""
    e = 2.7182818285
    π = 3.1415926536

    def __init__(self, data=None, mean=0., stddev=1.):
        """Class constructor

        data: is a list of the data to be used to estimate the distribution
        mean: is the mean of the distribution
        stddev: is the standard deviation of the distribution
        """
        self.mean = float(mean)
        self.stddev = float(stddev)
        if data is None:
            if stddev <= 0:
                raise ValueError('stddev must be a positive value')
        else:
            if type(data) is not list:
                raise TypeError('data must be a list')
            if len(data) < 2:
                raise ValueError('data must contain multiple values')
            leng = len(data)
            self.mean = sum(data) / leng
            self.stddev = (sum((x - self.mean)**2 for x in data) / leng)**0.5

    def z_score(self, x):
        """Calculating the z-score of a given x-value"""
        return (x - self.mean) / self.stddev

    def x_value(self, z):
        """Calculating the x-value of a given z-score"""
        return (z * self.stddev) + self.mean
