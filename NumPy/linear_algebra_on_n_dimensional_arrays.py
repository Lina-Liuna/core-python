import scipy
from matplotlib import pyplot
from matplotlib import cbook
import os
from numpy import linalg


def get_img(path):
    with cbook.get_sample_data(path) as img_file:
        img = pyplot.imread(img_file)

        pyplot.title('Lina Liu image')
        pyplot.imshow(img)
        pyplot.show()
        print(img.shape)
        print(img.ndim)
        r,g,b= img[:,:,0],img[:,:,1], img[:,:,2]
        img_gray = r * 0.2126 + g * 0.7152 + b * 0.0722
        pyplot.imshow(img_gray, cmap="gray")
        pyplot.show()
        return img


img = get_img(os.getcwd() + '/data/unicorn.png')
print(img.shape)


