import cv2 as cv
import numpy as np

lower = np.array([15, 150, 20])
upper = np.array([35, 255, 255])

def find_object(video):
    while True:
        success, img = video.read()
        image = cv.cvtColor(img, cv.COLOR_BGR2HSV)
        mask = cv.inRange(image, lower, upper)

        contours, hierarchy = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

        if len(contours) != 0:
            for contour in contours:
                area = cv.contourArea(contour)
                if area > 500:
                    x, y, w, h = cv.boundingRect(contour)
                    cv.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    rect = cv.minAreaRect(contour)
                    box = cv.boxPoints(rect)
                    box = np.int0(box)
                    center = (int(rect[0][0]), int(rect[0][1]))
                    area = cv.contourArea(contour)
                    cv.circle(img, center, 2, (0, 0, 255), 2)
                    text = "(" + str(center[0]) + ", " + str(center[1]) + ")"
                    cv.putText(img, text, (center[0] + 10, center[1] + 10), cv.FONT_HERSHEY_PLAIN, 1.5, (0, 0, 0), 1, 8, 0)

        cv.imshow("mask", mask)
        cv.imshow("webcam", img)

        k = cv.waitKey(1)
        if k == 27:
            break


if __name__ == '__main__':
    video = cv.VideoCapture(0)
    find_object(video)

    video.release()
    cv.destroyAllWindows()
