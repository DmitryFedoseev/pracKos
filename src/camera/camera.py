import cv2 as cv
import numpy as np

lower = np.array([15, 150, 20])
upper = np.array([35,255,255])

video = cv.VideoCapture(0)

while True:
    success, img = video.read()
    image = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    mask = cv.inRange(image, lower, upper)

    contours, hierarchy = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    if len(contours) != 0:
        for contour in contours:
            if cv.contourArea(contour) > 500:
                x, y, width, height = cv.boundingRect(contour)
                cv.rectangle(img, (x, y), (x + width, y + height), (0, 0, 255), 3)

    cv.imshow("mask", mask)
    cv.imshow("webcam", img)

    cv.waitKey(1)
