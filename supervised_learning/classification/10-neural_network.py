#!/usr/bin/env python3
"""
Module to create a neural network
"""
import numpy as np


class NeuralNetwork:
    """
    Class that defines a neural network with one hidden layer
    performing binary classification
    """

    def __init__(self, nx, nodes):
        """
        Class constructor
        """
        if type(nx) is not int:
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")
        if type(nodes) is not int:
            raise TypeError("nodes must be an integer")
        if nodes < 1:
            raise ValueError("nodes must be a positive integer")

        # nodes number of nodes and receives nx number of input feature
        self.W1 = np.random.randn(nodes, nx)
        # matches the shape of the hidden layer output
        self.b1 = np.zeros((nodes, 1))
        self.A1 = 0

        # only one node and receives the output from the hidden layer as input
        self.W2 = np.random.randn(1, nodes)
        # matching the shape of the output neuron's activation
        self.b2 = 0
        self.A2 = 0

    @property
    def W1(self):
        return (self.__W1)

    @property
    def b1(self):
        return (self.__b1)

    @property
    def A1(self):
        return (self.__A1)

    @property
    def W2(self):
        return (self.__W2)

    @property
    def b2(self):
        return (self.__b2)

    @property
    def A2(self):
        return (self.__A2)

    def forward_prop(self, X):
        """
        calculates the forward propagation of the neural network
        """

        z1 = np.matmul(self.W1, X) + self.b1
        self.__A1 = 1 / (1 + (np.exp(-z1)))

        z2 = np.matmul(self.W2, self.__A1) + self.b2
        self.__A2 = 1 / (1 + (np.exp(-z2)))

        return (self.A1, self.A2)