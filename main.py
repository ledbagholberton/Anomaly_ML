#!/usr/bin/env python3
import numpy as np
import os
import PIL
import PIL.Image
import tensorflow as tf
import tensorflow_datasets as tfds
crop_image = __import__('crop_image').crop_image


if __name__ == '__main__':
    dir_source = './Data/Source_train/back/'
    dir_target = './Data/Target_noise'
    coordinates = (0, 300, 500, 800)
    crop_image(dir_source, dir_target, coordinates)
