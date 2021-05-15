import cv2 as cv
from cv2 import VideoCapture as vc

cv.namedWindow('w1', cv.WINDOW_NORMAL)
cv.resizeWindow('w1', 600, 600)

img = cv.imread('./img/0.jpg')
size = img.shape

height = size[0]
width = size[1]


cv.Scharr(img)

cv.imshow('w1', img)


cv.waitKey(0)
# cv.cvtColor(img, gray_scale, cv.CV)



print(size)
