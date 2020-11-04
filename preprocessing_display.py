#!/usr/bin/env python3
"""
Function displays images one to one
"""
import os
import numpy
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import cv2
import tensorflow as tf


def display_images(origImage, altImages, title1="Original", title2="Edited"):
    """
    display images: original, edited
    """
    plt.subplot(121), plt.imshow(origImage), plt.title(title1)
    plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(altImages), plt.title(title2)
    plt.xticks([]), plt.yticks([])
    plt.show()
