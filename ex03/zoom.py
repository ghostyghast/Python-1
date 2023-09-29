from load_image import ft_load
from matplotlib import pyplot as plt


def main():
    image = ft_load('animal.jpeg')
    print(image)
    image = image[:400, 400:800, :1]
    print('New shape after slicing:', image.shape, end=' ')
    print('or', image.shape[:2])
    print(image)
    plt.imshow(image, cmap='gray')
    plt.show()


if __name__ == '__main__':
    main()
