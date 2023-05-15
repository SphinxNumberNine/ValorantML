import numpy as np
import cv2

# notes
# 64 pixels matches POV agent logo (bottom center of screen)


img = cv2.imread("assets\\round1_capture_5v5.PNG", 0)
template = cv2.resize(cv2.imread(
    "assets/icons/Jett_icon.png", 0), (0, 0), fx=0.25, fy=0.25)
h, w = template.shape

methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,
           cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

for method in methods:
    img2 = img.copy()

    result = cv2.matchTemplate(img2, template, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        location = min_loc
    else:
        location = max_loc

    bottom_right = (location[0] + w, location[1] + h)
    color = (255, 0, 0)
    cv2.rectangle(img2, location, bottom_right, color, 2)
    cv2.imshow('Match', img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
