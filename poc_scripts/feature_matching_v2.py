import cv2
import numpy as np

template = cv2.imread("assets\\ability_icons\\Cloudburst.png", 0)
image = cv2.imread('assets\\cloudburst_crop.png', 0)

# orb = cv2.ORB_create()
sift = cv2.SIFT_create()

kp1, des1 = sift.detectAndCompute(template, None)
kp2, des2 = sift.detectAndCompute(image, None)

# bf = cv2.BFMatcher()
# matches = bf.knnMatch(des1, des2, k=2)
# print(matches)

FLANN_INDEX_KDTREE = 1
index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
search_params = dict(checks = 50)
flann = cv2.FlannBasedMatcher(index_params, search_params)
matches = flann.knnMatch(des1,des2,k=2)

good = []
for m, n in matches:
    if m.distance < 0.7 * n.distance:
        good.append([m])


print(len(good))
match_image = cv2.drawMatchesKnn(template, kp1, image, kp2, good, None, flags=2)

cv2.imshow("template", template)
cv2.imshow("image", image)
cv2.imshow("match_image", match_image)
cv2.waitKey(0)