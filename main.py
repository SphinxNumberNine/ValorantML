import numpy as np
import cv2

# notes
# 64 pixels matches POV agent logo (bottom center of screen)


# img = cv2.imread('test_crops\\left_8773598.png', 0)
img = cv2.flip(cv2.imread("test_crops\\right_761828.png", 0), 1)
template = cv2.imread("icons_from_screenshots\\viper.png", 0)
h, w = template.shape

methods = [cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF_NORMED]

for method in methods:
    img2 = img.copy()

    result = cv2.matchTemplate(img2, template, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        location = min_loc
    else:
        location = max_loc

    confidence = result[location[1], location[0]]
    print(confidence)
    bottom_right = (location[0] + w, location[1] + h)
    color = (255, 0, 0)
    cv2.rectangle(img2, location, bottom_right, color, 2)
    cv2.imshow('Match', img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
