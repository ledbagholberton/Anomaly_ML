#!/usr/bin/env python3
from PIL import Image, ImageChops
import numpy as np
import matplotlib.pyplot as plt
import cv2
import os
import math
import seaborn as sb
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


def rmsdiff(im1, im2):
    """Calculates the root mean square error (RSME) between two images"""
    errors = np.asarray(ImageChops.difference(im1, im2)) / 255
    return np.mean(np.square(errors))


def Histogram_MSE(path_dir1, path_dir2):
    image_dir1 = []
    image_dir2 = []
    rmsdiff_list = []
    image_dir1 = [fn for fn in os.listdir(f'{path_dir1}') if fn.endswith('.jpg')]
    image_dir2 = [fn for fn in os.listdir(f'{path_dir2}') if fn.endswith('.jpg')]
    size = len(image_dir1)
    for img in range(size):
        path_img1 = path_dir1 + '/' + image_dir1[img]
        path_img2 = path_dir2 + '/' + image_dir2[img]
        img1 = Image.open(path_img1)
        img2 = Image.open(path_img2)
        rmsd = rmsdiff(img1, img2)
        rmsdiff_list.append(rmsd)
    # pass to array the list from the loop
    rmsdiff_arr = np.array(rmsdiff_list)
    bins = np.arange(start=0, stop=0.2, step=0.002)
    hist, bins = np.histogram(rmsdiff_arr, bins=bins)

    return hist, bins


if __name__ == '__main__':
    path_dir10 = "../Data/Images_Saved_cracks/Input_clean"
    path_dir20 = "../Data/Images_Saved_cracks/Output_clean"
    path_dir11 = "../Data/Images_Saved_cracks/Input_clean_for_real"
    path_dir21 = "../Data/Images_Saved_cracks/Output_clean_for_real"
    path_dir12 = "../Data/Images_Saved_cracks/Input_noisy_for_real"
    path_dir22 = "../Data/Images_Saved_cracks/Output_noisy_for_real"
    path_dir13 = "../Data/Images_Saved_cracks/Input_synthetic"
    path_dir23 = "../Data/Images_Saved_cracks/Output_synthetic"
    sb.set_style('darkgrid')
    hist10, bins10 = Histogram_MSE(path_dir10, path_dir20)
    hist11, bins11 = Histogram_MSE(path_dir11, path_dir21)
    hist12, bins12 = Histogram_MSE(path_dir12, path_dir22)
    hist13, bins13 = Histogram_MSE(path_dir13, path_dir23)
    x_multi = np.vstack((hist10, hist11))
    sb.histplot([hist13, hist12], stat='density', element='step')
    plt.legend(prop={'size': 12})
    plt.title('Histogram MSE Comparison Images')
    plt.xlabel('MSE')
    plt.ylabel('Count MSE')
    plt.show()
