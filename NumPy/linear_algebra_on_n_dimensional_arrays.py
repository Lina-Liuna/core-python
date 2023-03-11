import scipy
from matplotlib import pyplot
from matplotlib import cbook
import os
import numpy
from numpy import linalg


def get_img(path):
    with cbook.get_sample_data(path) as img_file:
        return pyplot.imread(img_file)


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

def linalg_svd_apply_all_colors(path, output_img):
    img = get_img(path)
    print(img.shape)

    img_arr = img
    img_array_transposed = numpy.transpose(img_arr, (2, 0, 1))
    print(img_array_transposed.shape)
    U, s, Vt = linalg.svd(img_array_transposed)
    print(U.shape, s.shape, Vt.shape)
    Sigma = numpy.zeros((U.shape[1], Vt.shape[0]))
    numpy.fill_diagonal(Sigma, s)
    print(U.shape, s.shape, Vt.shape)
    Sigma = numpy.zeros((4, 1234, 1690))
    for j in range(4):
        numpy.fill_diagonal(Sigma[j, :, :], s[j, :])
    print(Sigma.shape)
    reconstructed = U @ Sigma @ Vt
    reconstructed = numpy.clip(reconstructed, 0, 1)
    pyplot.imshow(numpy.transpose(reconstructed, (1, 2, 0)))
    pyplot.show()
    k = 10
    approx_img = U @ Sigma[..., :k] @ Vt[..., :k, :]
    pyplot.imshow(numpy.transpose(approx_img, (1, 2, 0)))
    pyplot.show()
    # pyplot.imsave(output_img, approx_img,cmap='gray')








curdir = os.getcwd()
img_gray = turn_img_gray(curdir + '/data/unicorn.png', curdir + '/data/unicorn_gray.png')
use_linalg_svd(img_gray, curdir + '/data/unicorn_blur.png')

linalg_svd_apply_all_colors(curdir + '/data/unicorn.png', curdir + '/data/unicorn_blur_all_colors.png')




