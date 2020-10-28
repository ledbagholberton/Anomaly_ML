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


def hamming(s1, s2):
    """Calculate the hamming distance between two hashes"""
    assert len(s1) == len(s2)
    return float(sum(c1 != c2 for c1, c2 in zip(s1, s2)) / float(len(s1)))


def find_similar_images(userpaths, hashfunc):
    image_filenames = []
    new_list = []
    final_list = []
    image_filenames = [fn for fn in os.listdir(f'{userpaths}') if fn.endswith('.jpeg')]
    print(image_filenames)
    count = 0
    for _ in range(20):
        new_list = []
        leng = len(final_list)
        x = random.randint(0, 518)
        img_0 = image_filenames[x]
        first_hash = hashfunc(Image.open(userpaths + '/' + img_0))
        for img in sorted(image_filenames):
            try:
                hash = hashfunc(Image.open(userpaths + '/' + img))
                """print(type(hash))"""
            except Exception as e:
                print('Problem:', e, 'with', img)
                continue
            if hamming(str(hash), str(first_hash)) < 0.7:
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
    dst = "../Data/Casting/Similar_phash"
    for f in final_list:
        shutil.copy(path.join(src, f), dst)


if __name__ == '__main__':
    find_similar_images(userpaths="../Data/Casting/casting_512x512/casting_512x512/ok_front", hashfunc=imagehash.phash)
