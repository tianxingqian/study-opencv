import cv2 as cv
import numpy as np

src = cv.imread("D:/vcprojects/images/demo.png")
# cv.namedWindow("image", cv.WINDOW_AUTOSIZE)
cv.imshow("test", src)
cv.waitKey(0)
cv.destroyAllWindows()

