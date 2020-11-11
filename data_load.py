#!/usr/bin/env python3
import glob
import numpy as np
import cv2


def load_images(images_path, noise_path, samples=None,
                out_shape=None,
                train_percentage=0.95):
    """
        - images_path is the path to a directory from which to load images
                without noise
        - noise_path is the path to a directory from wich to load noisy images
        - samples: number of images to create dataset
        - out_shape: shape of images to rescale

        All images are loaded in RGB format

        Returns: x_data - images without noise
                 x_noisy_data - noisy images
    """
    backgnd_paths = glob.glob(images_path + "/*.jpeg")
    noisy_img_paths = glob.glob(noise_path + "/*.jpg")

    backgnd_paths.sort()
    noisy_img_paths.sort()

    if samples is not None:
        noisy_img_paths = noisy_img_paths[:samples]

    print("loading images without noise..", end='')
    x_dict = {}
    for i, path in enumerate(backgnd_paths):
        if i % 100 == 0:
            print(".", end='')
        img = cv2.imread(path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        if out_shape is not None:
            img = cv2.resize(img, out_shape, interpolation=cv2.INTER_AREA)
            # img = rescale(img, out_shape)
        x_dict[path.split('/')[-1].split('.')[0]] = img
    print("")
    print("loading noisy images..", end='')
    x_data = []
    x_noisy_data = []
    for i, img_noisy in enumerate(noisy_img_paths):
        if i % 100 == 0:
            print(".", end='')
        name = img_noisy.split('/')[-1].split('__')[0]
        img_noisy = cv2.imread(img_noisy)
        img_noisy = cv2.cvtColor(img_noisy, cv2.COLOR_BGR2RGB)
        if out_shape is not None:
            img_noisy = cv2.resize(
                img_noisy, out_shape, interpolation=cv2.INTER_AREA)
        x_noisy_data.append(img_noisy)
        x_data.append(x_dict[name])
    print("")
    x_data = np.stack(x_data, axis=0)
    x_noisy_data = np.stack(x_noisy_data, axis=0)

    train_samples = int(x_noisy_data.shape[0] * (train_percentage))

    x_train = x_noisy_data[:train_samples]
    y_train = x_data[:train_samples]
    x_valid = x_noisy_data[train_samples:]
    y_valid = x_data[train_samples:]

    return (x_train, y_train), (x_valid, y_valid)
