#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 16:50:14 2018

@author: minicoder
"""
import matplotlib.pyplot as plt
from skimage import io
import numpy as np

url = ('tata.jpg')
img = io.imread(url)
fig, ax = plt.subplots()
ax.imshow(img)
a=np.array([0,-1,0,-1,5,-1,0,-1,0])
a.resize(3,3)
kernel=a
def blur(a):
    arraylist = []
    for y in range(3):
        temparray = np.copy(a)
        temparray = np.roll(temparray, y - 1, axis=0)
        for x in range(3):
            temparray_X = np.copy(temparray)
            temparray_X = np.roll(temparray_X, x - 1, axis=1)*kernel[y,x]
            arraylist.append(temparray_X)

    arraylist = np.array(arraylist)
    arraylist_sum = np.sum(arraylist, axis=0)
    return arraylist_sum

img1=blur(img)
fig, ax = plt.subplots()
ax.imshow(img1)

from scipy.ndimage import convolve
import matplotlib.pyplot as plt
from skimage import io
import numpy as np

url = ('tata.jpg')
img = io.imread(url)
fig, ax = plt.subplots()
ax.imshow(img)

kernel=np.array([1.0,2.0,1.0,2.0,4.0,2.0,1.0,2.0,1.0,1.0,2.0,1.0,2.0,4.0,2.0,1.0,2.0,1.0,1.0,2.0,1.0,2.0,4.0,2.0,1.0,2.0,1.0])
kernel.resize(3,3,3)
kernel=kernel/np.sum()
fig, ax = plt.subplots()
ax.imshow(convolve(img,kernel))


    