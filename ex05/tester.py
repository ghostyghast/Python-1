from load_image import ft_load
from pimp_image import ft_invert, ft_red, ft_grey, ft_blue, ft_green
import matplotlib.pyplot as plt
array = ft_load("landscape.jpg")
# plt.imshow(ft_invert(array))
# plt.show()
# plt.imshow(ft_red(array))
# plt.show()
# plt.imshow(ft_green(array))
# plt.show()
plt.imshow(ft_grey(array))
plt.show()
print(ft_invert.__doc__)