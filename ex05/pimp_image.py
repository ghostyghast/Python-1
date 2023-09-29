import numpy as np


def ft_invert(array):
    """inverts the color of the image received"""
    return np.subtract(255, array[:, :])


def ft_red(array):
    """turns the given image red"""
    n_array = array
    n_array[:, :] = [255, 0, 0]
    return n_array

def ft_green(array):
    """turns the given image green"""


def ft_blue(array):
    """turns the given image blue"""


def ft_grey(array):
    """turns the given image grey"""
