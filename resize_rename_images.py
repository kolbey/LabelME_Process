import os
import numpy as np
from PIL import Image
import torchvision.transforms as transforms


img_path = './imgs/'
out_path = './images/'

img_list = os.listdir(img_path)
i = 0
for img_file in img_list:
    imgpath = os.path.join(img_path, img_file)
    img = Image.open(imgpath)
    resize = transforms.Resize([1080, 1920])
    crooped_img = resize(img)
    new_name = img_file.split('.')[0] + '.png'
    savepath = os.path.join(out_path, new_name)
    crooped_img.save(savepath)
    i = i + 1
    print(i)