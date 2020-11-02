#!/usr/bin/env python3
"""
Main Histogram
Clean images are original images through Autoencoder
Inputs:
    path_dir10 Path of directory with original images (similar) 
    path_dir11 Path of directory with clean images (similar)
    path_dir20 Path of directory with original images (non similar)
    path_dir21 Path of directory with clean images (non similar)

Outputs:
    Histogram

"""
import matplotlib.pyplot as plt
import seaborn as sb
Histogram_MSE = __import__('Histogram_MSE').Histogram_MSE


if __name__ == '__main__':
    path_dir10 = "../Data/Images_Saved_cracks/Input_noisy_for_real"
    path_dir20 = "../Data/Images_Saved_cracks/Output_noisy_for_real"
    path_dir11 = "../Data/Images_Saved_cracks/Input_synthetic"
    path_dir21 = "../Data/Images_Saved_cracks/Output_synthetic"
    sb.set_style('darkgrid')
    hist10, bins10 = Histogram_MSE(path_dir10, path_dir20)
    hist11, bins11 = Histogram_MSE(path_dir11, path_dir21)
    sb.histplot([hist10, hist11], stat='density', element='step')
    plt.legend(prop={'size': 12})
    plt.title('Histogram MSE Comparison Images')
    plt.xlabel('MSE')
    plt.ylabel('Count MSE')
    plt.show()
