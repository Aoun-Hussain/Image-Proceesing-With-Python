import cv2
import numpy as np
import sys
import os
import fnmatch

def sharpen(image):
    kernel = np.array([[0, -1, 0], [-1,5 ,-1], [0,-1,0]])
    sharpened_image = cv2.filter2D(image, -1, kernel)
    cv2.imshow("sharpened", sharpened_image)
    cv2.waitKey(0)
    return

def blur(image):
    kernels = [3,5,9,13]
    for idx, k in enumerate(kernels):
        image_blur = cv2.blur(image, ksize = (k,k))
        cv2.imshow(str(k), image_blur)
        cv2.waitKey(0)
    return

def resize(fname, width, height):
    image = cv2.imread(fname)
    cv2.imshow('Original image', image)
    cv2.waitKey(0)
    org_height, org_width = image.shape[0:2]
    print("Width: ", org_width)
    print("Height: ", org_height)

    if org_width >= org_height:
        new_image = cv2.resize(image, (width, height))
    else:
        new_image = cv2.resize(image,(height,width))
    return fname, new_image

listoffiles = os.listdir('.')
pattern = '*.jpg'
n = len(sys.argv)
if n==3:
    width = int[sys.argv(1)]
    height = int[sys.argv(2)]
else:
    width = 1280
    height = 960
if not os.path.exists("new_folder2"):
    os.makedirs("new_folder2")
for fn in listoffiles:
    if fnmatch.fnmatch(fn, pattern):
        filename, image = resize(fn,1280,960)
        cv2.imshow("resized image", image)
        cv2.waitKey(0)
        blur(image)
        sharpen(image)
        cv2.imwrite("new_folder2\\" + filename, image)


