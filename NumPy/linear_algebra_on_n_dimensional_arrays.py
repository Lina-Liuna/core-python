import scipy
from matplotlib import pyplot
from matplotlib import cbook
import os
import numpy
from numpy import linalg


def turn_img_gray(path, output_img):
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
        pyplot.imsave(output_img,img_gray, cmap='gray')
        return img_gray

def use_linalg_svd(img_array, output_img):
    U, s, Vt = linalg.svd(img_array)
    print(U.shape, s.shape, Vt.shape)
    Sigma = numpy.zeros((U.shape[1], Vt.shape[0]))
    numpy.fill_diagonal(Sigma, s)

    k = 10
    approx = U @ Sigma[:, :k] @ Vt[:k, :]
    pyplot.imshow(approx, cmap="gray")
    pyplot.show()
    pyplot.imsave(output_img,approx, cmap='gray')



curdir = os.getcwd()

img_gray = turn_img_gray(curdir + '/data/unicorn.png', curdir + '/data/unicorn_gray.png')
use_linalg_svd(img_gray, curdir + '/data/unicorn_blur.png')




