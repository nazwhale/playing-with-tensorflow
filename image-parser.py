import MNIST_softmax_regression
from MNIST_softmax_regression import Weights
import numpy as np
import PIL
from PIL import Image

I = np.asarray(PIL.Image.open('its-a-five.png'))

I = np.transpose(I.flatten())

bias = [-0.12531213, 0.34291193, -0.07756195, -0.15483579, 0.14375827,  0.38140905,
 0.04379947, 0.30139488, -0.70874661, -0.14681587]

w = Weights

fp = (np.dot(np.transpose(w), I))/2550 + bias

print(fp)
