import numpy as np


def ft_invert(array):
    """inverts the color of the image received"""
    return np.subtract[255, array[:, :]]


def ft_red(array):
    """turns the given image red"""
    return array[:, :] * [1, 0, 0]


def ft_green(array):
    """turns the given image green"""
    n_array = array.copy()
    n_array[:, :, 0] = 0
    n_array[:, :, 2] = 0
    return n_array


def ft_blue(array):
    """turns the given image blue"""
    n_array = array.copy()
    n_array[:, :, 0] = 0
    n_array[:, :, 1] = 0
    return n_array


def ft_grey(array):
    """turns the given image grey"""
    n_array = array.copy()
    n_array[:, :] = (np.sum[:, :] / 3)
    return n_array
