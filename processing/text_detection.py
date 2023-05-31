import easyocr
import time
import math
import cv2
from pytesseract import pytesseract


class TextDetector:
    def __init__(self):
        self.reader = easyocr.Reader(['en'], gpu=True)
        path_to_tesseract = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
        pytesseract.tesseract_cmd = path_to_tesseract

    def readTextFromImage(self, image):
        h, w, a = image.shape
        if h < 100 and w < 100:
            image = cv2.resize(image, (0, 0), fx=3, fy=3)
        result = self.reader.readtext(image)
        print(result)
        return result

    def readNumbersFromImage(self, image):
        result = self.reader.readtext(image, allowlist="0123456789:")
        print(result)
        return result

    def parseOutput(self, readerOutput):
        print(readerOutput)
        if readerOutput == []:
            return []
        output = []
        for result in readerOutput:
            boundingBox, text, confidence = result
            output.append(text)
        return output
    
    def readNumbersTesseract(self, image):
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        image = cv2.resize(image, (0,0), fx=4, fy=4)
        im_bw = cv2.threshold(image, 180, 255, cv2.THRESH_BINARY)[1]
        contours, hierarchy = cv2.findContours(im_bw, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        cv2.drawContours(im_bw, contours, -1, (255, 255, 255), 2)
        text = pytesseract.image_to_string(im_bw, config='--psm 13 --oem 3 digits -c tessedit_char_whitelist=0123456789:')
        return text
