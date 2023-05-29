import Levenshtein

import easyocr
import time
import pandas as pd
import math
import cv2
# this needs to run only once to load the model into memory
reader = easyocr.Reader(['en'], gpu=True)
img1 = cv2.imread('assets\\killfeed_examples\\1.png')
img2 = cv2.imread('assets\\killfeed_examples\\2.png')
img0 = cv2.imread('assets\\killfeed_examples\\0.png')

print(str(round(time.time() * 1000)))
result = reader.readtext(img1)
print(result)
print(str(round(time.time() * 1000)))

print(str(round(time.time() * 1000)))
result = reader.readtext(img2)
print(result)
print(str(round(time.time() * 1000)))

print(str(round(time.time() * 1000)))
result = reader.readtext(img0)
print(result)
print(str(round(time.time() * 1000)))


map_link = "https://www.vlr.gg/167358/drx-vs-cloud9-champions-tour-2023-lock-in-s-o-paulo-alpha-qf/?game=113071&tab=overview"
maps_cache = pd.read_pickle("config\\maps.pickle")
row = maps_cache[maps_cache["map_link"] == map_link].to_dict('records')[0]
comp = dict(row["comp_mappings"])
print(comp.keys())

def process_ocr_result(result):
    text = result[1]
    splitted = text.split(" ")
    if len(splitted) > 1:
        return splitted[-1]
    else:
        return splitted[0]

for res in result:
    inferred_name = process_ocr_result(res)
    curr_match = None
    curr_lowest_distance = math.inf
    for name in comp.keys():
        dist = Levenshtein.distance(inferred_name, name, weights=(4,4,1))
        if dist < curr_lowest_distance:
            curr_lowest_distance = dist
            curr_match = name

    print(curr_match)