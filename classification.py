import cv2
import numpy as np
import os

best_matches_count = -1
orb = cv2.ORB_create()
bf = cv2.BFMatcher()
image = cv2.imread("assets\screencap_1_jett_hud.png", 0)
kp2, des2 = orb.detectAndCompute(image, None)
best_kp1, best_des1 = None, None
best_matches = None
best_template = None

for filename in os.listdir("assets\icons"):
    template = cv2.imread("assets\icons\\" + filename, 0)
    kp1, des1 = orb.detectAndCompute(template, None) 
    matches = bf.knnMatch(des1, des2, k=2)
    good = []
    for m, n in matches:
        if m.distance < 0.8 * n.distance:
            good.append([m])
    print(len(good))
    if len(good) > best_matches_count:
        best_matches_count = len(good)
        best_kp1 = kp1
        best_des1 = des1
        best_matches = good
        best_template = template


match_image = cv2.drawMatchesKnn(best_template, best_kp1, image, kp2, best_matches, None, flags=2)

cv2.imshow("best template", best_template)
cv2.imshow("image", image)
cv2.imshow("match_image", match_image)
cv2.waitKey(0)