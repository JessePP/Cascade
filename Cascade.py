import cv2 as cv

img = cv.imread('E:\projekty\cascade\Picure.jpg', 2)
draw = cv.Canny(img, 125, 140)
cv.imshow('Cats', draw)

cv.waitKey(0)




















