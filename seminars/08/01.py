#!/usr/bin/env python3
from PIL import Image
import numpy as np

img = Image.open('image.png')

xsize, ysize = img.size

data = np.asarray(img)
print(data.shape)
print(data.dtype)

print(data[0, 0])
data_out = 255 - data
print(data_out[0, 0])

out = Image.fromarray(data_out, 'RGB')
out.save('negative.jpg')
