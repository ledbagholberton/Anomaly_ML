#!/usr/bin/env python3
"""
Function displays images
"""
import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import cv2
import tensorflow as tf


origImage = "/Desktop/C8 Final Anomaly Detection/images"
altImages = "/Desktop/C8 Final Anomaly Detection/noisy_img"
"""
disply images original and edited
"""


def display_two(origImages, altImages, title1="Original", title2="Edited"):
    """
    display images: original, edited
    """
    plt.subplot(121), plt.imshow(origImage), plt.title(title1)
    plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(altImages), plt.title(title2)
    plt.xticks([]), plt.yticks([])
    plt.show()


# flag = 1
for orig in range(origImage):
    for alt in range(altImages):
        display_two(origImages[orig], altImages[alt], "Original", "Edited")
        alt += 3
        """
        flag = flag + 1
        if flag == 20:
             break
        """
print("Images Printed")
