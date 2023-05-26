import cv2
import pafy
import urllib
import random
import os
import json
import threading
import numpy as np

# test_screenshot_path = "test_crops\\left_3620453.png"
# test_screenshot_path = "test_crops\\left_1185452.png"
test_screenshot_path = "test_crops\\left_4270239.png"


# test_screenshot_left_agents = ["cypher", "skye", "omen", "phoenix", "chamber"]
# test_screenshot_right_agents = ["sova", "jett", "breach", "omen", "killjoy"]
crop_test_path = "ability_crops\\2.png"


def crop_single_hud(path_to_crop):  # non-astra usecase
    start_points = [(70, 32), (111, 32), (150, 32)]
    # start_points = [(70, 32)]
    x_offset, y_offset = 40, 17
    # x_offset, y_offset = 120, 20

    img = cv2.imread(path_to_crop)
    h, w, alpha = img.shape
    print(img.shape)
    cv2.imshow("original", img)

    counter = 0
    for x, y in start_points:
        crop = img[y: y + y_offset, x: x + x_offset]
        cv2.imshow("crop" + str(counter), crop)
        cv2.imwrite("ability_crops\\" + str(counter) + ".png", crop)
        counter += 1

    cv2.waitKey(0)


def count_dots(path_to_img):
    img = masked_image(path_to_img)
    print(img.dtype)
    img = cv2.normalize(img, dst=None, alpha=0, beta=255,
                        norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)
    circles = cv2.HoughCircles(
        img, cv2.HOUGH_GRADIENT, 1, 1, param1=20, param2=8, minRadius=1, maxRadius=100)
    index = 0
    print(circles)
    if circles is not None:
        circles = circles[0]
        # convert the (x, y) coordinates and radius of the circles to integers
        circles = np.round(circles[:]).astype("int")

        # loop over the (x, y) coordinates and radius of the circles
        for (x, y, r) in circles:
            # draw the circle in the output image,
            #   then draw a rectangle corresponding to the center of the circle
            cv2.circle(img, (x, y), r, (255, 0, 255), 2)
            cv2.rectangle(img, (x - 5, y - 5),
                          (x + 5, y + 5), (255, 0, 255), -1)

            index = index + 1
            # print str(index) + " : " + str(r) + ", (x,y) = " + str(x) + ', ' + str(y)
        print('No. of circles detected = {}'.format(index))
        return index
    else:
        print("no circles")
        return 0


def count_dots_alt(path_to_img):
    gray = cv2.imread(path_to_img, 0)
    cv2.imshow("any", gray)
    cv2.waitKey(0)
    # threshold
    # th, threshed = cv2.threshold(gray, 100, 255,cv2.THRESH_BINARY_INV|cv2.THRESH_OTSU)
    # cv2.imshow("any", threshed)
    # cv2.waitKey(0)
    # findcontours
    cnts = cv2.findContours(gray, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[-2]

    # filter by area
    s1 = 3
    s2 = 20
    xcnts = []
    for cnt in cnts:
        if s1 < cv2.contourArea(cnt) < s2:
            xcnts.append(cnt)

    print("Dots number: {}".format(len(xcnts)))


def masked_image(path_to_img):
    img = cv2.imread(path_to_img)
    lower, upper = np.array([220, 220, 220]), np.array([255, 255, 255])
    mask = cv2.inRange(img, lower, upper)
    result = cv2.bitwise_and(img, img, mask=mask)
    result = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
    print(result.shape)
    cv2.imshow("masked image", result)
    cv2.waitKey(0)
    return result


crop_single_hud(test_screenshot_path)
count_dots(crop_test_path)
