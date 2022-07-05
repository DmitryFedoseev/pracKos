import cv2 as cv
import numpy as np

lower = np.array([15, 150, 20])
upper = np.array([35,255,255])

video = cv.VideoCapture(0)

while True:
    success, img = video.read()
    try:
        image = cv.cvtColor(img, cv.COLOR_BGR2HSV)
        mask = cv.inRange(image, lower, upper)

        moments = cv.moments(mask, 1)
        dM01 = moments['m01']
        dM10 = moments['m10']
        dArea = moments['m00']

        contours, hierarchy = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

        if len(contours) != 0:
            for contour in contours:
                if cv.contourArea(contour) > 500:
                    x, y, width, height = cv.boundingRect(contour)
                    cv.rectangle(img, (x, y), (x + width, y + height), (0, 0, 255), 3)

        if dArea > 150:
            x = int(dM10 / dArea)
            y = int(dM01 / dArea)
            cv.circle(img, (x, y), 4, (0, 0, 255), -1)

    except:
        video.release()
        raise

    cv.imshow("mask", mask)
    cv.imshow("webcam", img)

    k = cv.waitKey(1)
    if k == 27:
        break

cv.destroyAllWindows()