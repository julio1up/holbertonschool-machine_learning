#!/usr/bin/env python3
"""Performs a convolution on grayscale images"""


import numpy as np


def convolve_grayscale(images, kernel, padding="same", stride=(1, 1)):
    """Performs a convolution on grayscale images"""

    m, height, width = images.shape
    kh, kw = kernel.shape
    sh, sw = stride

    if padding == "same":
        if kh % 2 == 0 and kw % 2 == 0:
            ph = (kh - 1) // 2
            pw = (kw - 1) // 2
        ph = kh // 2
        pw = kw // 2
    elif padding == "valid":
        ph = 0
        pw = 0
    else:
        ph, pw = padding

    p_images = np.pad(images, ((0, 0), (ph, ph), (pw, pw)))

    ch = ((height + 2 * ph - kh) // sh) + 1
    cw = ((width + 2 * pw - kw) // sw) + 1

    convoluted = np.zeros((m, ch, cw))

    i = 0
    for h in range(0, height + 2 * ph - kh + 1, sh):
        j = 0
        for w in range(0, width + 2 * pw - kw + 1, sw):
            output = p_images[:, h : h + kh, w : w + kw] * kernel
            sum_out = np.sum(output, axis=(1, 2))
            convoluted[:, i, j] = sum_out
            j += 1
        i += 1
    return convoluted

