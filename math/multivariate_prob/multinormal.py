#!/usr/bin/env python3
"""Initialize Multinormal"""

import numpy as np


class MultiNormal:
    """
    Multivariate Normal distribution
    """

    def __init__(self, data):

        if type(data) != np.ndarray:
            raise TypeError("data must be a 2D numpy.ndarray")
        if len(data.shape) != 2:
            raise TypeError("data must be a 2D numpy.ndarray")
        d, n = data.shape
        if n < 2:
            raise ValueError("data must contain multiple data points")
        self.mean = np.mean(data, axis=1, keepdims=True)
        X_mean = data - self.mean
        self.cov = (X_mean @ X_mean.T) / (n - 1)

    def pdf(self, x):
        """
        calculates the PDF at a data point
        """
        if type(x) is not np.ndarray:
            raise TypeError("x must be a numpy.ndarray")
        d = self.cov.shape[0]
        if len(x.shape) != 2 or x.shape[1] != 1 or x.shape[0] != d:
            raise ValueError("x must have the shape ({}, 1)".format(d))

        det = np.linalg.det(self.cov)
        inv = np.linalg.inv(self.cov)
        first = 1 / ((2 * np.pi) ** (d / 2) * np.sqrt(det))
        second = np.dot((x - self.mean).T, inv)
        third = np.dot(second, (x - self.mean) / -2)
        pdf = first * np.exp(third)

        return pdf[0][0]
