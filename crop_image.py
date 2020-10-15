#!/usr/bin/env python3
"""
Function crop_image used to diminish the variability.
Explore the mean & standard deviation for each one of cropped
images and generate a Warning Message in case to have an 
outlier
Crop batch of images based on parameters
Inputs: path of directory with Batch of pictures to crop.
		path of directory where crop files be write
		coordinates (top, left, bottom, right)
		top left & bottom right coordinates (rectangle crop)
Outputs: Model anomaly_autoencoder.mh5
"""
import os
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
import imagehash
from PIL import Image
from tensorflow.keras.preprocessing import image
from sklearn.decomposition import PCA


def crop_image(dir_source, dir_target, coordinates):
	""" Crop Images in batch from a source directory"""
	# get the list of jpegs from dir_source
	normal_imgs = [fn for fn in os.listdir(f'{dir_source}') if fn.endswith('.jpg')]
	print (normal_imgs)
	mean_list = []
	std_list = []
	pca_list = []
	hash_list = []
	for file in normal_imgs:
		fp = dir_source + file
		current_image = image.load_img(fp, color_mode = 'grayscale')
		# img = Image.open(dir_source + file)
		# cropped_img = img.crop(coordinates)
		cropped_img = current_image.crop(coordinates)
		img_ts = image.img_to_array(cropped_img)
		img_ts = [img_ts.ravel()]
		try:
			full_mat = np.concatenate((full_mat, img_ts))
		except UnboundLocalError: 
			# if not assigned yet, assign one
			full_mat = img_ts
		hash = imagehash.average_hash(cropped_img)
		print(hash)
		mean_img = np.mean(full_mat, axis=1)
		std_img = np.std(full_mat, axis=1)
		pca = PCA(n_components = 0.7,  whiten = True)
		pca.fit(full_mat)
		mean_list.append(mean_img)
		std_list.append(std_img)
		pca_list.append(pca.n_components)
		hash_list.append(hash)
		final_filename = file.replace('.jpg', '_crop.jpg')
		cropped_img.save(os.path.join(dir_target, final_filename))
		# cropped_img.show()
	# for a in std_list:
	#	print(a)
	# print("Standard Deviation\n", std_list, sep="\n")
	# print("PCA", pca_list)
	# print(hash_list)
