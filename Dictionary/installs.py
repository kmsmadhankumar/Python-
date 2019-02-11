import numpy
import cv2

im_g = cv2.imread("smallgray.png",0)
im_c = cv2.imread("smallgray.png",1)

print(im_g[0:2,2:2])
