from PIL import Image
import numpy as np

# img = Image.open('_source-s.png')
img = Image.open('final2.png')
data = np.array(img)

data[...] = (data & 0x07) << 5

out = Image.fromarray(data, "RGB")
out.save('final.png')
