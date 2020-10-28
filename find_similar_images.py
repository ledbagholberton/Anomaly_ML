#!/usr/bin/env python3
from __future__ import (absolute_import, division, print_function)
from PIL import Image
import os
import six
import imagehash
import random
import shutil
from os import path
"""
Demo of hashing
"""


def find_similar_images(userpaths, hashfunc):
    image_filenames = []
    new_list = []
    final_list = []
    image_filenames = [fn for fn in os.listdir(f'{userpaths}') if fn.endswith('.jpg')]
    """ print(image_filenames)"""
    count = 0
    for _ in range(20):
        new_list = []
        leng = len(final_list)
        x = random.randint(0, 2000)
        img_0 = image_filenames[x]
        first_hash = hashfunc(Image.open(userpaths + '/' + img_0))
        for img in sorted(image_filenames):
            try:
                hash = hashfunc(Image.open(userpaths + '/' + img))
                """print(type(hash))"""
            except Exception as e:
                print('Problem:', e, 'with', img)
                continue
            """print("Hash First: {} - Hash {} = {}".format(first_hash, hash, abs(hash - first_hash)))"""
            if abs(hash - first_hash) < 22:
                new_list.append(img)
                "print(new_list)"
            if len(new_list) > leng:
                """print(len(new_list))"""
                final_list = new_list.copy()
        count += 1
        print(count)
    print(len(new_list))
    print(final_list)
    src = userpaths
    dst = "../Data/Similar_phash/"
    for f in final_list:
        shutil.copy(path.join(src, f), dst)


if __name__ == '__main__':
    find_similar_images(userpaths="../Data/Negative", hashfunc=imagehash.phash)
