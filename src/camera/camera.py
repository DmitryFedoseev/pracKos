import cv2 as cv
import numpy as np
import os.path

def write_file(cent):    
    file = open(os.path.abspath(os.path.dirname(__file__))+"/coords.txt", "a")
    file.write(str(cent) + '\n')
    file.close()

def find_contours(lower, upper, img):
    image = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    mask = cv.inRange(image, lower, upper)
    contours, hierarchy = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    return contours 

def find_coordinate(contour):
    area = cv.contourArea(contour)
    rect = cv.minAreaRect(contour)
    center = (int(rect[0][0]), int(rect[0][1]))
    return area, center
      

def draw_coordinate(contour, img, center):
    x, y, w, h = cv.boundingRect(contour)
    cv.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
    cv.circle(img, center, 2, (0, 0, 255), 2)
    text = "(" + str(center[0]) + ", " + str(center[1]) + ")"
    cv.putText(img, text, (center[0] + 10, center[1] + 10), cv.FONT_HERSHEY_PLAIN, 1.5, (0, 0, 0), 1, 8, 0)
    return text

def find_color(contours, array, count, img):
    if len(contours) != 0:
        for contour in contours:
            area, center = find_coordinate(contour)
            if area > 500:
                draw_coordinate(contour, img, center)
                array[count] = "(" + str(center[0]) + ", " + str(center[1]) + ")"
                count += 1    

def run():
    video = cv.VideoCapture(0)
    while True:
        lower_yellow = np.array([15, 150, 20])
        upper_yellow = np.array([35, 255, 255])

        lower_green = np.array((10, 100, 100))
        upper_green = np.array((10, 255, 255))

        lower_red = np.array((0, 150, 130))
        upper_red = np.array((10, 255, 255))

        lower_blue = np.array((90, 130, 100))
        upper_blue = np.array((130, 255, 255))

        success, img = video.read()
        yellow_contours = find_contours(lower_yellow, upper_yellow, img)
        green_contours = find_contours(lower_green, upper_green, img)
        red_contours = find_contours(lower_red, upper_red, img)
        blue_contours = find_contours(lower_blue, upper_blue, img)

        # Массив для хранения координат
        array = [0] * (len(yellow_contours)+len(green_contours)+len(red_contours)+len(blue_contours))
        count = 0

        find_color(yellow_contours, array, count, img)
        find_color(green_contours, array, count, img)
        find_color(red_contours, array, count, img)
        find_color(blue_contours, array, count, img)

        # cv.imshow("mask", mask)
        cv.imshow("webcam", img)

        k = cv.waitKey(1)
        if k == 27:
            for coordinat in array:
                if coordinat != 0:
                    write_file(coordinat)
            break
    
    video.release()
    cv.destroyAllWindows()


if __name__ == '__main__':
    run()