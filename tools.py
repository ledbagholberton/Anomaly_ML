#!/usr/bin/env python3
import numpy as np
import os
from skimage.metrics import structural_similarity as ssim
import matplotlib.pyplot as plt
import glob
import tensorflow.keras as K


def ssim_fun(im1, im2):
    ssim_ = 1-ssim(im1, im2, data_range=255, multichannel=True)
    return ssim_


def Histogram(imgs1, imgs2):
    hashdiff_list = []
    for i in range(imgs1.shape[0]):
        hashd = ssim_fun(imgs1[i], imgs2[i])
        hashdiff_list.append(hashd)
    hashdiff_arr = np.array(hashdiff_list)
    return hashdiff_arr


def histogram_intersection(h1, h2, bins):
    sm = 0
    for i in range(bins):
        sm += min(h1[i], h2[i])
    return sm


def load_images_real(images_path, noise_path, reference_path, as_array=True, samples=None, scale=None):
    """
        images_path is the path to a directory from which to load images withput noise
        noise_path is the path to a directory from wich to load noisy images.
        All images are loaded in RGB format
        Returns: x_data - images withput noise
                 x_noisy_data - noisy images
    """
    backgnd_paths = glob.glob(images_path + "/*.jpeg")
    noisy_img_paths = glob.glob(noise_path + "/*.jpeg")
    references = glob.glob(reference_path + "/*.jpeg")

    references = [path.split('/')[-1].split('.')[0] for path in references]
    backgnd_paths = [im for im in backgnd_paths if im.split('/')[-1].split('.')[0] not in references]
    backgnd_paths.sort(reverse=True)
    noisy_img_paths.sort(reverse=True)

    if samples != None:
        noisy_img_paths = noisy_img_paths[:samples]
        backgnd_paths = backgnd_paths[:samples]
    print("backgnd: ", backgnd_paths[0], " - ", backgnd_paths[-1])
    print("loading", end='')
    x_data = []
    x_noisy_data = []
    for n, img in enumerate(zip(backgnd_paths, noisy_img_paths)):
        if n % 100 == 0:
            print(".", end='')
        for i in range(2):
            img_data = cv2.imread(img[i])
            img_data = cv2.cvtColor(img_data, cv2.COLOR_BGR2RGB)
            if scale != None:
                img_data = rescale(img_data, scale)
            if i == 0:
                x_data.append(img_data)
            else:
                x_noisy_data.append(img_data)
    print("")

    if as_array:
        x_data = np.stack(x_data, axis=0)
        x_noisy_data = np.stack(x_noisy_data, axis=0)

    return x_data, x_noisy_data
