import easyocr
import time

class TextDetector:
    def __init__(self):
        self.reader = easyocr.Reader(['en'], gpu=True)

    def readTextFromImage(self, image):
        result = self.reader.readtext(image)
        print(result)
        return result