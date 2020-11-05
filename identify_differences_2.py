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
    threshed_img = cv2.adaptiveThreshold(arr_dif, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 15, 2)
    # _, threshed_img = cv2.threshold(arr_dif, 250, 255, cv2.THRESH_BINARY)
    _, contours, hier = cv2.findContours(threshed_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    list_cont = []
    count = 0
    for c in contours:
        count += 1
        # get the bounding rect
        x, y, w, h = cv2.boundingRect(c)
        limit = 50
        if w > limit or h > limit:
            # print("x es {} ... y es {} ... w es {} .... h es {}".format(x, y, w, h))
            tuple_1 = (x, y, w, h, count)
            list_cont.append(tuple_1)
            print(list_cont)
    return list_cont, contours


if __name__ == '__main__':
    path_img1 = "../Data/00330.jpg"
    path_img2 = "../Data/00330_3.jpg"
    x, y = img_to_array(path_img1, path_img2)
    list_cont, contours = bound_differences(x, y)
    # print(list_circle)
    img1 = cv2.imread(path_img1, 0)
    img2 = cv2.imread(path_img2, 0)
    img_diff = cv2.imread(path_img2, 0)
    for x in range(len(list_cont)):
        iter = list_cont[x]
        x = iter[0]
        y = iter[1]
        w = iter[2]
        h = iter[3]
        count = iter[4]
        # draw a green rectangle to visualize the bounding rect
        img_diff = cv2.rectangle(img_diff, (x, y), (x+w, y+h), (7, 0, 0), 3)
    titles = ['Original Image', "Cleaned Image", "Differences"]
    images = [img1, img2, img_diff]
    for i in range(3):
        plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
        plt.title(titles[i])
        plt.xticks([]), plt.yticks([])
    plt.show()
