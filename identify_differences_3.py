#!/usr/bin/env python3
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import cv2
"""
Substract images and found the differences
"""


def img_to_array(path_img1, path_img2):
    img1 = cv2.imread(path_img1)
    img2 = cv2.imread(path_img2)
    """img1.show()
    img2.show()"""
    x = np.array(img1)
    y = np.array(img2)
    # print(x)
    # print(y)
    return x, y


def bound_differences(arr1, arr2):
    arr_dif = np.abs(np.subtract(arr1, arr2))
    arr_dif = cv2.cvtColor(arr_dif, cv2.COLOR_BGR2GRAY)
    threshed_img = cv2.adaptiveThreshold(arr_dif, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 199, 5)
    # _, threshed_img = cv2.threshold(arr_dif, 250, 255, cv2.THRESH_BINARY)
    _, contours, hier = cv2.findContours(threshed_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)
    return contours


if __name__ == '__main__':
    for file_number in range(15, 30, 1):
        file_1 = "{}.jpg".format(file_number)
        path_img2 = "../Data/Input_noisy_for_real/" + file_1
        path_img1 = "../Data/Output_noisy_for_real/" + file_1
        x, y = img_to_array(path_img1, path_img2)
        contours = bound_differences(x, y)
        # print(list_circle)
        img1 = cv2.imread(path_img1, 0)
        img2 = cv2.imread(path_img2, 0)
        img_diff = cv2.imread(path_img2, 0)
        try:
            img_diff = cv2.drawContours(img_diff, contours[0], -1, (0,255,255), thickness = 3)
            img_diff = cv2.drawContours(img_diff, contours[1], -1, (0,255,255), thickness = 3)
        except IndexError as e:
            print ("Similar Images")
        titles = ['Cleaned Image', "Original Image", "Differences"]
        images = [img1, img2, img_diff]
        for i in range(3):
            plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
            plt.title(titles[i])
            plt.xticks([]), plt.yticks([])
        plt.show()
        if cv2.waitKey(0) & 0xff == 27:  
            cv2.destroyAllWindows()
