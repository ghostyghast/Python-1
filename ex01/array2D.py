import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """function that takes 2D array, prints its shape, and returns a
    truncated version of the array based on the
    provided start and end arguments."""
    assert type(family) is list, "family is not list"
    assert type(start) is int and type(end) is int, "start or end not int"
    np_family = np.asarray(family)
    assert np_family.ndim == 2, "family not 2D array"
    print("My shape:", np_family.shape)
    np_family = np_family[start:end]
    print("New shape is:", np_family.shape)
    return np_family.tolist()
