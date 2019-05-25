import cv2 as cv
import numpy as np


def image_info(image):
    print(type(image))
    print(image.shape)
    print(image.size)
    print(image.dtype)
    pixel = np.array(image)
    print(pixel)


def video_demo():
    capture = cv.VideoCapture(0)
    while True:
        ret, frame = capture.read()
        frame = cv.flip(frame, 1)   # 反转
        cv.imshow("video", frame)
        c = cv.waitKey(50)
        if c == 27:
            break


src = cv.imread("D:/vcprojects/images/demo.png")
# cv.namedWindow("org", cv.WINDOW_AUTOSIZE)
cv.imshow("test", src)
# cv.imwrite('d:/1.png',src)
image_info(src)
video_demo()
cv.waitKey(0)
cv.destroyAllWindows()

