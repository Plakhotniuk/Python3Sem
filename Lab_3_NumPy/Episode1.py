import numpy as np
from PIL import Image

for i in range(3):
    img = Image.open(f'lunar0{i + 1}_raw.jpg')
    data = np.array(img)
    data *= int(255 / (data - data.min()).max())
    res_img = Image.fromarray(data)
    res_img.save(f'updated_lunar0{i + 1}_raw.jpg')
