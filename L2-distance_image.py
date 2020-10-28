#!/usr/bin/env python3
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import cv2
"""
Demo of hashing
"""


def mse(imageA, imageB):
    # the 'Mean Squared Error' between the two images is the
    # sum of the squared difference between the two images;
    # NOTE: the two images must have the same dimension
    err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
    err /= float(imageA.shape[0] * imageA.shape[1])
    # return the MSE, the lower the error, the more "similar"
    # the two images are
    return err


def L2_distance(path_img1, path_img2):
    img1 = Image.open(path_img1)
    img2 = Image.open(path_img2)
    # load the two input images
    imageA = cv2.imread(path_img1)
    imageB = cv2.imread(path_img2)
    # convert the images to grayscale
    imageA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
    imageB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)
    """img1.show()
    img2.show()"""
    img1 = img1.getdata()
    img2 = img2.getdata()
    mse_1 = mse(imageA, imageB)
    x = np.array(img1)
    y = np.array(img2)
    print(x)
    print(y)
    nx, p = x.shape
    x_ext = np.empty((nx, 3*p))
    for i in range(nx):
        dif = 0
        for j in range(p):
            dif += pow(x[i][j] - y[i][j], 2)
        res = pow(dif, 0.5)
        x_ext[i] = res
        suma = np.sum(x_ext)
    print(x_ext)
    print("SUMA", suma)
    y1, bins = np.histogram(x_ext, bins=np.arange(255), range=(0, 255))
    """print(y1)
    print(x1)"""
    width = 0.5 * (bins[1] - bins[0])
    center = (bins[:-1] + bins[1:]) / 2
    plt.bar(center, y1, align='center', width=width)
    plt.show()
    print("Este es el MSE", mse_1)
    return x_ext, mse


if __name__ == '__main__':
    L2_distance(path_img1="../Data/img3.jpg", path_img2="../Data/img2.jpg")
