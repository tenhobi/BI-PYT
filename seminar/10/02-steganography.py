from PIL import Image
import numpy as np

imgSource = Image.open('_source.jpg')
imgSecret = Image.open('_secret.png')
dataSource = np.array(imgSource)
dataSecret = np.array(imgSecret)

dataSource[...] = dataSource & 0xF8
dataSecret[...] = (dataSecret & 0xE0) >> 5
dataSource = dataSource + dataSecret

out = Image.fromarray(dataSource, "RGB")
out.save('final2.png')
