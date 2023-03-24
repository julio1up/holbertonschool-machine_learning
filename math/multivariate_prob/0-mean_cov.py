#!/usr/bin/env python3
"""Calculates the mean and covariance of a data set"""


import numpy as np


def mean_cov(X):
    """Calculates the mean and covariance of a data set"""
    mean = np.mean(X, axis=0)
    cov = np.zeros((d, d))
    for i in range(n):
        cov += np.outer((X[i] - mean), (X[i] - mean))
    cov /= n - 1
    return mean.reshape(1, d), cov
