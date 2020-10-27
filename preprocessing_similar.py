#!/usr/bin/env python3

"""
Functions: Preprocessing Similarity
"""
import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import cv2
import tensorflow as tf
from tensorflow.keras.layers import Input

"""
Function Preprocessing Similarity
Verifies the similarity of data images.
If different from original discard image.

Input: Data Images (path to data images)
       Original Image (path to original Image)
Output: Images same size as the original
"""
def sim_image(origImage, altImage):
    """
    origImage: original image
    altImage: image to be compared to original image

    Return: similar images in  array
    """
    simArray = []

