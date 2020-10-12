#!/usr/bin/env python3
"""
Function Anomaly Detector
Based on the trained model anomaly_autoencoder.mh5
Inputs: path of directory with Batch of pictures.
Outputs: Dictionary with names of files and "Yes / No" for Anomaly
"""
from PIL import Image
import glob
import os


def anomaly_detector(path_source, path_target, path_model_anomaly):
    """Function Anomaly Detector"""
    source = path_source
    # All jpegs are in this folder
    imList = glob.glob(source + '*.jpg')
    # Reading all images with .jpg
    