#!/usr/bin/env python3
"""
Module to perform forward propagation
"""
import tensorflow as tf
create_layer = __import__('1-create_layer').create_layer


def forward_prop(x, layer_sizes=[], activations=[]):
    """
    a function that creates the forward propagation graph
    """
    for i in range(len(layer_sizes)):
        if i == 0:
            output = create_layer(x, layer_sizes[0], activations[0])
        else:
            output = create_layer(prediction, layer_sizes[i],
                                      activations[i])
    return output
