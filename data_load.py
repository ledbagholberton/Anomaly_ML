#!/usr/bin/env python3
import glob
import numpy as np
import cv2

def rescale(img, scale_percent):
    """ resize images """
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
    # resize image
    return cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

def load_images(images_path, noise_path, samples=None, scale=None):
    """
        - images_path is the path to a directory from which to load images without
	noise
	- noise_path is the path to a directory from which to load synthetic images
        - samples is the number of synthetic images to use
        - scale is the factor to scale the images, if it is None, it is ignored
        All images are loaded in RGB format
        Returns: x_data, x_noisy_data
            x_data are the clean images
            x_noisy_data are the synthetic images
    """
    print(noise_path)
    backgnd_paths = glob.glob(images_path + "/*.jpg")
    noisy_img_paths = glob.glob(noise_path + "/*.jpg")

    backgnd_paths.sort()
    noisy_img_paths.sort()

    print(backgnd_paths)
    print(noisy_img_paths)

    if samples != None:
        noisy_img_paths = noisy_img_paths[:samples]
    print("loading backgrounds - clean images")
    x_dict = {}
    for i, path in enumerate(backgnd_paths):
          img = cv2.imread(path)
          img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
          if scale != None:
              img = rescale(img, scale)
          x_dict[path.split('/')[-1].split('.')[0]] = img
    print("loading noisy images..", end='')
    x_data = []
    x_noisy_data = []
    for i, img_noisy in enumerate(noisy_img_paths):
        print(".", end='')
        name = img_noisy.split('/')[-1].split('_')[0]
        img_noisy = cv2.imread(img_noisy)
        img_noisy = cv2.cvtColor(img_noisy, cv2.COLOR_BGR2RGB)
        if scale != None:
            img_noisy = rescale(img_noisy, scale)
        x_noisy_data.append(img_noisy)
        x_data.append(x_dict[name])
    print("")

    x_data = np.stack(x_data, axis=0)
    x_noisy_data = np.stack(x_noisy_data, axis=0)

    return x_data, x_noisy_data
