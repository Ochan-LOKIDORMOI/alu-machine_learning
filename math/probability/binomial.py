#!/usr/bin/env python3
"""Initialize Binomial, normal distribution"""


class Binomial:
    """Class that represents a binomial distribution"""
    e = 2.7182818285
    π = 3.1415926536

    def __init__(self, data=None, n=1, p=0.5):
        """Class constructor

        data: is a list of the data to be used to estimate the distribution
        n: is the number of Bernoulli trials
        p: is the probability of a success
        """
        self.n = int(n)
        self.p = float(p)

        if data is None:
            if n < 1:
                raise ValueError('n must be a positive value')
            if p <= 0 or p >= 1:
                raise ValueError('p must be greater than 0 and less than 1')
        else:
            if type(data) is not list:
                raise TypeError('data must be a list')
            if len(data) < 2:
                raise ValueError('data must contain multiple values')
            mean = sum(data) / len(data)
            dev = sum(((x - mean) ** 2) for x in data) / len(data)
            self.p = 1 - (dev / mean)
            self.n = round(mean / self.p)
            self.p = mean / self.n
