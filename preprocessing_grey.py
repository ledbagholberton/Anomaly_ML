#!/usr/bin/env python3
"""
Function converts images to grey scale
Function displays imagesß
"""
import os
import numpy
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import cv2
import tensorflow as tf
from tensorflow.keras.layers import Input


"""
makes images grey
"""


def make_grey(image):
    """
    Image color to grey scale
    """
    # for  i in range(len(image)):
    # segmentation and gray definition
    grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray, 0, 255,
                                cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    # display images
    display_two(image, thresh, "Original", "Grayed")
    return (image, grayImages)

    newAltImages = []
    for i in range(originalArr):
        newImage = make_grey(originalArr[i])
        newAltImages.append(newImage)
    return (newAltImages)
