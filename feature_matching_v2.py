import cv2
import numpy as np

template = cv2.imread("assets\icons\jett_icon.png", 0)
image = cv2.imread("assets\jett_hud_example.png", 0)

orb = cv2.ORB_create()

kp1, des1 = orb.detectAndCompute(template, None)
kp2, des2 = orb.detectAndCompute(image, None)

bf = cv2.BFMatcher()
matches = bf.knnMatch(des1, des2, k=2)
print(matches)

good = []
for m, n in matches:
    if m.distance < 0.6 * n.distance:
        good.append([m])


print(len(good))
match_image = cv2.drawMatchesKnn(template, kp1, image, kp2, good, None, flags=2)

cv2.imshow("template", template)
cv2.imshow("image", image)
cv2.imshow("match_image", match_image)
cv2.waitKey(0)