import numpy as np
from load_image import ft_load
import matplotlib.pyplot as plt


def main():
    """program that crops an image then rotates it"""
    image = ft_load('animal.jpeg')
    print(image)
    n_image = [image[:, i, 0] for i in range(401)]
    n_image = np.asarray(n_image)
    print('New shape after transpose:', n_image.shape[:2])
    print(n_image)
    plt.imshow(n_image, cmap='gray')
    plt.show()


if __name__ == '__main__':
    main()
