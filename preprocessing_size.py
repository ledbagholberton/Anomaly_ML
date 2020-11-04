#!/usr/bin/env python3

"""
Functions: Preprocessing Size, Grayscale, Display two images
"""

import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import cv2
import tensorflow as tf
from tensorflow.keras.layers import Input

"""
Function Preprocessing size
Verifies the size of data images.
If different from original, resize to match original
Input: Data Images (path to data images)
       Original Image (path to original Image)
Output: Images same size as the original
"""

# defining global variable path
# origImage_path =
# altImage_path =


def loadData(origpath, altpath, origfile_name, altfile_name):
    """
    Load data images from path
    """
    images = origfile_name
    altimages = altfile_name
    # Put files into lists and return them as one list of size 4
    origImage_files = sorted([os.origpath.join(path, 'images', file)
                              for file in os.listdir(path + "/images") if
                              file.endswith('*.jpg')])
    altImage_files = sorted([os.altpath.join(path, 'altImage', file)
                             for file in os.listdir(path + "/altIimages") if
                             file.endswith('*.jpg')])
    return origImage_files, altImage_files


def preprocessing_size(origData, altData):
    """
    load images
    set resize dimensions
    resize
    """
    original = []
    origImg = [cv2.imread(i, cv2.IMREAD_UNCHANGED) for i in origData[]]
    # print("Original", img[0].shape)
    original.append(origImg)
    try:
        print("Original".format(original[i]))
    except AttributeError:
        print("shape not found")

    # set dimensions
    height = int(origImg.shape[0])
    width = int(origImg.shape[1])
    dim = (width, height)
    reszd_img = []

    for j in range(len(altData)):
        reszd = cv2.resize(altData[j], dim, interpolation=cv2.INTER_LINEAR)
        reszd_img.append(reszd)

    # size check
    try:
        print("RESIZED {}".format(reszd_img[j]))
    except AttributeError:
        print("shape not found")

    return (original, reszd_img)
