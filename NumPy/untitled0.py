from scipy.ndimage import convolve
import matplotlib.pyplot as plt
from skimage import io
import numpy as np

def blur(img):
    kernel=np.array([1.0,2.0,1.0,2.0,4.0,2.0,1.0,2.0,1.0,1.0,2.0,1.0,2.0,4.0,2.0,1.0,2.0,1.0,1.0,2.0,1.0,2.0,4.0,2.0,1.0,2.0,1.0])
    kernel.resize(3,3,3)
    kernel=kernel/np.sum(kernel)
    fig, ax = plt.subplots()
    img=img+105
    ax.imshow(img)
def contrast(img):
    kernel=np.array([0,-1,0,-1,5,-1,0,-1,0,0,-1,0,-1,5,-1,0,-1,0,0,-1,0,-1,5,-1,0,-1,0])
    kernel.resize(3,3,3)
    kernel=kernel/np.sum(kernel)
    fig, ax = plt.subplots()
    ax.imshow(convolve(img,kernel))
def blaknwhite():
    kernel=np.array([1.0,2.0,1.0,2.0,4.0,2.0,1.0,2.0,1.0,1.0,2.0,1.0,2.0,4.0,2.0,1.0,2.0,1.0,1.0,2.0,1.0,2.0,4.0,2.0,1.0,2.0,1.0])
    kernel.resize(3,3,3)
    kernel=kernel/np.sum(kernel)
    fig, ax = plt.subplots()
    ax.imshow(convolve(img,kernel))
url = ('2.jpg')
img = io.imread(url)
fig, ax = plt.subplots()
ax.imshow(img)

blur(img)
contrast(img)