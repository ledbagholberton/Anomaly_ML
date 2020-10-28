#!/usr/bin/env python3
"""main file L2 distance
Inputs: path_img1 and path_img2
Output: Histogram Comparison & MSE
"""
L2_distance = __import__('L2-distance_image').L2_distance


if __name__ == '__main__':
    L2_distance(path_img1="../Data/img3.jpg", path_img2="../Data/img2.jpg")
