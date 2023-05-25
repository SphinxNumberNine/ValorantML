import cv2
import pafy
import urllib
import random
import os
import json
import threading
import numpy as np
from imutils.object_detection import non_max_suppression
from pytesseract import pytesseract
import time
import tesserocr
from tesserocr import PyTessBaseAPI
from PIL import Image

PyTessBaseAPI(path="E:\\tessdata-main\\tessdata-main")

curr_time = round(time.time()*1000)
print(str(curr_time))

path_to_tesseract = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

image = cv2.imread("killfeed\\8.png")
image = cv2.resize(image, (0, 0), fx=3, fy=3)

# image height and width should be multiple of 32
imgWidth = 1760
imgHeight = 96

orig = image.copy()
(H, W) = image.shape[:2]
(newW, newH) = (imgWidth, imgHeight)

rW = W / float(newW)
rH = H / float(newH)
image = cv2.resize(image, (newW, newH))

(H, W) = image.shape[:2]

grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
im_bw = cv2.threshold(grayscale, 180, 255, cv2.THRESH_BINARY)[1]
contours, hierarchy = cv2.findContours(
    im_bw, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(im_bw, contours, -1, (255, 0, 0), 2)
# cv2.imshow("test", im_bw)
# cv2.waitKey(0)

net = cv2.dnn.readNet("frozen_east_text_detection.pb")
blob = cv2.dnn.blobFromImage(image, 1.0, (W, H),
                             (123.68, 116.78, 103.94), swapRB=True, crop=False)


outputLayers = []
outputLayers.append("feature_fusion/Conv_7/Sigmoid")
outputLayers.append("feature_fusion/concat_3")

net.setInput(blob)
output = net.forward(outputLayers)
scores = output[0]
geometry = output[1]

(numRows, numCols) = scores.shape[2:4]
rects = []
confidences = []

for y in range(0, numRows):
    scoresData = scores[0, 0, y]
    xData0 = geometry[0, 0, y]
    xData1 = geometry[0, 1, y]
    xData2 = geometry[0, 2, y]
    xData3 = geometry[0, 3, y]
    anglesData = geometry[0, 4, y]

    for x in range(0, numCols):
        # if our score does not have sufficient probability, ignore it
        if scoresData[x] < 0.5:
            continue

        # compute the offset factor as our resulting feature maps will
        # be 4x smaller than the input image
        (offsetX, offsetY) = (x * 4.0, y * 4.0)

        # extract the rotation angle for the prediction and then
        # compute the sin and cosine
        angle = anglesData[x]
        cos = np.cos(angle)
        sin = np.sin(angle)

        # use the geometry volume to derive the width and height of
        # the bounding box
        h = xData0[x] + xData2[x]
        w = xData1[x] + xData3[x]

        # compute both the starting and ending (x, y)-coordinates for
        # the text prediction bounding box
        endX = int(offsetX + (cos * xData1[x]) + (sin * xData2[x]))
        endY = int(offsetY - (sin * xData1[x]) + (cos * xData2[x]))
        startX = int(endX - w)
        startY = int(endY - h)

        # add the bounding box coordinates and probability score to
        # our respective lists
        rects.append((startX, startY, endX, endY))
        confidences.append(scoresData[x])

boxes = non_max_suppression(
    np.array(rects), probs=confidences, overlapThresh=0.1)
print(boxes)

coords = []
# loop over the bounding boxes
for (startX, startY, endX, endY) in boxes:
    # scale the bounding box coordinates based on the respective
    # ratios
    startX = int(startX * rW)
    startY = int(startY * rH)
    endX = int(endX * rW)
    endY = int(endY * rH)
    coords.append((startX, startY, endX, endY))

    # draw the bounding box on the image
    cv2.rectangle(image, (startX, startY), (endX, endY), (0, 255, 0), 2)

# cv2.imshow("t", image)
# cv2.waitKey(0)


coords.sort(key=lambda x: x[0])
for (startX, startY, endX, endY) in coords:
    crop = image[startY-5:endY+15, startX-5:endX+5]
    pytesseract.tesseract_cmd = path_to_tesseract
    crop = Image.fromarray(crop)
    text = pytesseract.image_to_string(crop, config='--psm 6 --oem 3')
    print(text)
    # crop.show()

print(str(curr_time - round(time.time()*1000)))
