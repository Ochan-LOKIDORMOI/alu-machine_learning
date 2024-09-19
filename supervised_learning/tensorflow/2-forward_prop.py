#!/usr/bin/env python3

""" Forward Propagation"""


def forward_prop(x, layer_sizes=[], activations=[]):
    """
    x is the placeholder for the input data
    layer_sizes is a list containing the number
    of nodes in each layer of the network
    activations is a list containing the activation
    functions for each layer of the network
    """
    create_layer = __import__('1-create_layer').create_layer
    for i in range(len(layer_sizes)):
        if i == 0:
            output = create_layer(x, layer_sizes[i], activations[i])
        else:
            output = create_layer(output, layer_sizes[i], activations[i])
            return output
