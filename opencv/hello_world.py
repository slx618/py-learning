import cv2 as cv

img = cv.imread('../img/0.jpg')

cv.namedWindow('my_image')
cv.imshow('my_image', img)
cv.waitKey(0)
cv.destroyAllWindows()