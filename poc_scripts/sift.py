import numpy as np
import cv2 as cv
ori = cv.imread("assets/Jett_icon.png", cv.IMREAD_UNCHANGED)
img = cv.imread("assets/Jett_icon.png", cv.IMREAD_UNCHANGED)
cv.imwrite("test.png", ori)
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
sift = cv.SIFT_create()
kp, des = sift.detectAndCompute(gray,None)
img=cv.drawKeypoints(gray,kp,img,flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv.imshow('Original',ori) 
cv.imshow('SIFT',img)
if cv.waitKey(0) & 0xff == 27:
    cv.destroyAllWindows()