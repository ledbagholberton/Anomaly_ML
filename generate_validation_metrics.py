#!/usr/bin/env python3
import numpy as np
import os
from skimage.metrics import structural_similarity as ssim
import matplotlib.pyplot as plt
import glob
import tensorflow.keras as K
ssim_fun = __import__('tools').ssim_fun
Histogram = __import__('tools').Histogram
histogram_intersection = __import__('tools').histogram_intersection
load_images_real = __import__('tools').load_images_real


def generate_validation_metrics(data_path_real, noise_path_real, reference_path, model_path):
    data_path_real = "../Data/casting_data/casting_data/train/ok_front"
    noise_path_real = "../Data/casting_data/casting_data/train/def_front"
    reference_path = "/Data/Original_Casting"
    model_path = "autoencoder_cylinders.h5"
    data_real, data_noise_real = load_images_real(data_path_real, noise_path_real, reference_path, scale=75.67, samples=1000)
    auto = K.models.load_model(model_path, custom_objects={'ssim_loss': ssim_loss})
    reconstructed_real = auto.predict(x_test_real) * 255
    reconstructed_noise_real = auto.predict(x_test_noise) * 255
    ssimdiff = Histogram(data_real, reconstructed_real)
    ssimdiff_noisy = Histogram(data_noise_real, reconstructed_noise_real)
    hist_ssimdiff, _ = np.histogram(ssimdiff, bins=200)
    hist_ssimdiff_noisy, _ = np.histogram(ssimdiff_noisy, bins=200)
    sm = histogram_intersection(hist_ssimdiff, hist_ssimdiff_noisy, bins)
    plt.figure(figsize=(30,15))
    sb.histplot([ssimdiff, ssimdiff_noisy], stat='density', element='step', bins=200)
    plt.legend(prop={'size': 12})
    plt.title('Histogram {}'.format(config.comparator))
    plt.xlabel('{}'.format(config.comparator))
    plt.ylabel('Count {}'.format(config.comparator))
    plt.xticks(np.arange(0, 0.1, step=0.001))
    plt.setp(plt.xticks()[1], rotation=30, ha='right')
    wandb.log({"Histogram new real data": wandb.Image(plt)})
    plt.show()
    plt.close()
    samples = data_real.shape[0]
    FP = np.count_nonzero(hashdiff > thld)
    TN = samples - FP
    TP = np.count_nonzero(hashdiff_noisy > thld)
    FN = samples - TP
    acc = (TP+TN)/(2 * samples)
    pre = TP / (TP + FP)
    rec = TP / (TP + FN)
    f1 = 2 * (pre * rec) / (pre + rec)
    print("Accuracy: ", acc)
    print("Precision: ", pre)
    print("Recall: ", rec)
    print("F1 Score: ", f1)
    print("Threshold:", sm)
