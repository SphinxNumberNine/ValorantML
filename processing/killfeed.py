from processing.text_detection import TextDetector
import math
class KillfeedProcessor:
    def __init__(self, player_names):
        self.text_detection_agent = TextDetector()
        self.player_names = player_names

    def process_ocr_result(self, result):
        text = result[1]
        splitted = text.split(" ")
        if len(splitted) > 1:
            return splitted[-1]
        else:
            return splitted[0]

    def findClosestMatch(inferred_name):
        curr_match = None
        curr_lowest_distance = math.inf
        for name in self.player_names():
            dist = Levenshtein.distance(inferred_name, name, weights=(4,4,1))
            if dist < curr_lowest_distance:
                curr_lowest_distance = dist
                curr_match = name

        return curr_match

    def detectKillEvent(self, img):
        ocr_output = self.text_detection_agent.readTextFromImage(img)
        readble_output = self.text_detection_agent.parseOutput(ocr_output)
        if len(readble_output) != 2:
            return None #some error happened

        player_1 = self.findClosestMatch(self.process_ocr_result(readable_output[0]))
        player_2 = self.findClosestMatch(self.process_ocr_result(readable_output[1]))

        

        
