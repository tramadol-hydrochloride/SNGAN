import scipy
import scipy.misc
import random
from glob import glob
import os
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageOps
import chainer

class Video10000Dataset(chainer.dataset.DatasetMixin):
    def __init__(self, dataset_dirname):
        self.path = glob('./datasets/{}/*.jpg'.format(dataset_dirname))
        self.img_res = (256, 256)
        self.crop_ratio = 0.9

    def __len__(self):
        return len(self.path)
    
    def transform(self, img_path):
        image = Image.open(img_path)
        h, w = image.size
        crop_size = int(h * self.crop_ratio)
        # Randomly crop a region and flip the image
        top = random.randint(0, h - crop_size - 1)
        left = random.randint(0, w - crop_size - 1)
        if random.randint(0, 1):
            image = ImageOps.mirror(image)
        
        bottom = top + crop_size
        right = left + crop_size
        image = image.crop((left, top, right, bottom))
        image = image.resize(self.img_res)
        image = np.asarray(image).astype('float32')
        image = image / 128. - 1.
        image += np.random.uniform(size=image.shape, low=0., high=1. / 128)
        image = image.transpose(2, 0, 1)
        return image

    def get_example(self, i):
        image = self.transform(self.path[i])
        label = np.int32(0)
        return image, label