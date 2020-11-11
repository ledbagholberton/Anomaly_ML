#!/usr/bin/env python3
"""
Anomaly_detector.py
Output function in charge to label (Anomaly or Not Anomaly) the images from a directory. 
Input: 
	autoencoder.h5
	SSIM threshold
	path to directory with images
Output: 
	Label images & text file (already done look in Heimer Colab)
	visualize image with anomaly (already done in Heimer Colab)
"""
import numpy as np
import os
from skimage.metrics import structural_similarity as ssim
import matplotlib.pyplot as plt
import glob
import tensorflow.keras as K
ssim_fun = __import__('tools').ssim_fun
Histogram = __import__('tools').Histogram
histogram_intersection = __import__('tools').histogram_intersection


def anomaly_detector(model_path = "autoencoder_cylinders.h5", threshold, images_path)
    """
        anomaly detector function
    """    
    x_data = []
    backgnd_paths = glob.glob(images_path + "/*.jpeg")
    backgnd_paths.sort()
    for path in enumerate(backgnd_paths):
        img = cv2.imread(path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        x_data.append(img)
    x_data = np.stack(x_data, axis=0)
    auto = K.models.load_model(model_path, custom_objects={'ssim_loss': ssim_loss})
    x_reconstructed = auto.predict(x_data) * 255
    ssimdiff = Histogram(x_data, x_reconstructed)
    size = x_data.shape[0]
    for i in range(size):
        ax = fig.add_subplot(2, 10, i + 1)
        ax.axis('off')
        if i % 2 == 0:
            ax.set_title("Clean#{}".format(i))
            plt.imshow(x_data[i])
        else:
            ax.set_title("With Anomalies#{}".format(n))
            plt.imshow(x_test_noise[n])
        ax = fig.add_subplot(2, 10, i + 11)
        ax.axis('off')
        if i % 2 == 0:
            if np.abs(hashdiff[n]) < threshold:
                ax.set_title("No Anomalies\n diff:{:.4f}".format(hashdiff[n]))
            else:
                ax.set_title("Anomalies\n detected\n diff:{:.4f}".format(hashdiff[n]))
            plt.imshow(reconstructed[n])
        else:
            if np.abs(hashdiff_noisy[n]) < threshold:
                ax.set_title("No Anomalies\n diff:{:.4f}".format(hashdiff_noisy[n]))
            else:
                ax.set_title("Anomalies\n detected\n diff:{:.4f}".format(hashdiff_noisy[n]))
            plt.imshow(reconstructed_noise[n])
            plt.show()
    plt.close()
