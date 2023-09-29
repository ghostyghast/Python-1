import numpy as np


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """function that returns list of bools
    True if element is bigger than given limit, false if not"""

    assert type(bmi) is list, "bmi is not a list"
    assert np.issubdtype(np.array(bmi).dtype, np.number), "bmi: non int/float"
    return [x > limit for x in bmi]


def give_bmi(height: list[int | float], weight: list[int | float]) -> list:
    """function that takes two lists, and respectively divides
    each element of the first list by the elements of the second"""

    assert type(height) is list, "height is not list"
    assert type(weight) is list, "weight is not list"

    np_height = np.array(height)
    np_weight = np.array(weight)

    assert np.issubdtype(np_height.dtype, np.number), "non int/float in array"
    assert np.issubdtype(np_weight.dtype, np.number), "non int/float in array"
    assert len(np_height) == len(np_weight), "array lengths not same"

    return list(np_weight / np.square(np_height))
