import cv2 as cv
import numpy as np


def access_pixel(image):
    print(image.shape)
    height = image.shape[0]
    width = image.shape[1]
    channels = image.shape[2]

    print(height, width, channels)


src = cv.imread("D:/vcprojects/images/demo.png")
# cv.namedWindow("org", cv.WINDOW_AUTOSIZE)
cv.imshow("test", src)
access_pixel(src)

cv.waitKey(0)
cv.destroyAllWindows()

