import easyocr
import time

class TextDetector:
    def __init__(self):
        self.reader = easyocr.Reader(['en'], gpu=True)

    def readTextFromImage(self, image):
        result = self.reader.readtext(image)
        print(result)
        return result

    def readNumbersFromImage(self, image):
        result = self.reader.readtext(image, allowlist="0123456789")
        print(result)
        return result

    def parseOutput(self, readerOutput):
        if readerOutput == []:
            return None
        boundingBox, text, confidence = readerOutput[0]
        if confidence > 0.5:
            return text
        else:
            return None