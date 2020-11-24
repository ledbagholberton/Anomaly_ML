#!/usr/bin/env python3

import tensorflow as tf
import tensorflow.keras as K
import cv2
import numpy as np
from skimage.metrics import structural_similarity as ssim


def ssim_loss(y_true, y_pred):
    return tf.reduce_mean(1-tf.image.ssim(y_true, y_pred, 1.0))

def ssim_fun(im1, im2):
    ssim_ = 1-ssim(im1, im2, data_range=255, multichannel=True)
    return ssim_

def analyze_image(path_h5="cylinders.h5", path_image="/image.jpeg", name_img="image.jpeg", type_dataset="type_dataset"):
    "load the model with weights and biases"

    out_shape = (227, 227)

    if type_dataset == "cylinder_dataset":
        thld = 0.007
        path_h5 = "cylinders.h5"
    else:
        thld = 0.003
        path_h5 = "cracks.h5"

    label = "No anomaly detected"

    # load image to analyze
    img = cv2.imread(path_image)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # resize image
    original_img = cv2.resize(img, out_shape, interpolation = cv2.INTER_AREA)
    
    #cv2.imshow("Imagen", img)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()

    # add a dimension
    img = original_img.reshape(1, 227, 227, 3)

    # preprocessing
    img = img.astype("float32") / 255

    # load model
    auto = K.models.load_model(path_h5, custom_objects={'ssim_loss': ssim_loss})
    
    # prediction with loaded image and update formats
    predict = auto.predict(img) * 255
    predict = predict.astype("uint8")
    img = img * 255
    img = img.astype("uint8")

    # compare images (original and predict)
    ssim_val = ssim_fun(img[0], predict[0])
    # print(ssim_val)

    # It has anomalies?
    if ssim_val > thld:

        # keep differences
        diff = np.abs(img[0].astype(np.int16) - predict[0].astype(np.int16))

        # anomalies change color
        anomaly_img = np.where(diff < 50, img[0], [0,255,0])

        # update format
        predict[0] = anomaly_img.astype("uint8")

        label = "Detected anomaly"

    # cv2.imshow("reconstructed", img[0])
    # cv2.waitKey(0)
    
    # save image
    cv2.imwrite(f"static/images/output_{name_img}", predict[0])

    return label

# analyze_image(path_h5="cylinders.h5", path_image="image.jpeg")