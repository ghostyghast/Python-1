
import numpy as np
import matplotlib.pyplot as plt


def ft_invert(array):
    """inverts the color of the image received"""
    n_array = 255 - array[:, :]
    plt.imshow(n_array)
    plt.show()
    return n_array


def ft_red(array):
    """turns the given image red"""
    n_array = array[:, :] * [1, 0, 0]
    plt.imshow(n_array)
    plt.show()
    return n_array


def ft_green(array):
    """turns the given image green"""
    n_array = array.copy()
    n_array[:, :, 0] = 0
    n_array[:, :, 2] = 0
    plt.imshow(n_array)
    plt.show()
    return n_array


def ft_blue(array):
    """turns the given image blue"""
    n_array = array.copy()
    n_array[:, :, 0] = 0
    n_array[:, :, 1] = 0
    plt.imshow(n_array)
    plt.show()
    return n_array


def ft_grey(array):
    """turns the given image grey"""
    n_array = array.copy()
    n_array = np.sum(array[:, :], axis=2) / 3
    plt.imshow(n_array, cmap='gray')
    plt.show()
    return n_array
