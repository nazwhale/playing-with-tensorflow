import numpy as np
import PIL
from PIL import Image

I = np.asarray(PIL.Image.open('its-a-five.png'))

# I.flatten()

print(I.flatten())

bias = [-0.12531213  0.34291193 -0.07756195 -0.15483579  0.14375827  0.38140905
  0.04379947  0.30139488 -0.70874661 -0.14681587]
