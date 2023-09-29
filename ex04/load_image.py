import numpy as np
from PIL import Image


def ft_load(path: str):
    """function that takes the path of an image
    and prints the shape of the image, then it's
    pixel information"""
    assert type(path) is str, "path is not str"
    image = Image.open(path)
    image = np.asarray(image)
    image = image[:400, 400:801, :1]
    print("Shape of image is:", image.shape, 'or', end=' ')
    print(image.shape[:2])
    return image
