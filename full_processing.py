import cv2
import pafy
import urllib
import random
import os
import json
import threading
import numpy as np
from models.image_utils import PlayerCrops
from models.gamestate import *
from models.events import *
from models.frame import *
from processing.cropping import Cropping
from processing.text_detection import TextDetector
import time

def getVideoCapture(vodUrl):
    # Getting video id from the url string
    url_data = urllib.parse.urlparse(vodUrl)
    query = urllib.parse.parse_qs(url_data.query)
    id = query["v"][0]
    video = 'https://youtu.be/{}'.format(str(id))

    # Using the pafy library for youtube videos
    urlPafy = pafy.new(video)
    videoplay = urlPafy.getbestvideo(preftype="any")

    cap = cv2.VideoCapture(videoplay.url)
    return cap

def processVOD(vodName, vodUrl, startTime, duration):
    cap = getVideoCapture(vodUrl=vodUrl)

    milliseconds = 1000
    endTime = startTime + duration

    # Passing the start and end time for CV2
    cap.set(cv2.CAP_PROP_POS_MSEC, startTime*milliseconds)

    # Will execute till the duration specified by the user
    frame_count = 0
    video_framerate = cap.get(cv2.CAP_PROP_FPS)
    rounded_framerate = round(video_framerate)
    print("Framerate: " + str(video_framerate))
    if rounded_framerate > 55:
        frame_skip = 10
    else:
        frame_skip = 5
    while True and cap.get(cv2.CAP_PROP_POS_MSEC) <= endTime*milliseconds:
        for _ in range(0, frame_skip):
            cap.read()
            frame_count += 1
        success, img = cap.read()
        # process image
        frame_count += 1

def determineFrameType(frame, left_score, right_score):
    loadoutValueLabel = cropping_agent.getLoadoutValueLabel(frame)
    left_score = cv2.resize(left_score, (0,0), fx=3, fy=3)
    right_score = cv2.resize(right_score, (0,0), fx=3, fy=3)
    # loadoutValueLabel = cv2.resize(loadoutValueLabel, (0,0), fx=3, fy=3)
    # cv2.imshow("loadout value", loadoutValueLabel)
    # cv2.imshow("left score", left_score)
    # cv2.imshow("right score", right_score)
    # cv2.waitKey(0)
    leftScoreText = text_detection_agent.parseOutput(text_detection_agent.readNumbersFromImage(left_score))
    rightScoreTest = text_detection_agent.parseOutput(text_detection_agent.readNumbersFromImage(right_score))
    if leftScoreText is not None and rightScoreTest is not None:
        print("Game Frame")
        # TODO check game state, if in round then no need to check for preround frame
        loadoutValueText = text_detection_agent.parseOutput(text_detection_agent.readTextFromImage(loadoutValueLabel))
        if loadoutValueText is not None and "loadout value" in loadoutValueText.lower():
            print("PreRound Frame")
            return FrameType.PRE_ROUND_FRAME
        else:
            print("Round Frame")
            return FrameType.ROUND_FRAME
    else:
        print("Non Game Frame")
        return FrameType.NON_GAME_FRAME

# full processing of first screenshot seen
# calls agent classifier and easyocr to map player name to agent
# creates gamestate, teamstates, first roundstate
def initialProcessing(frame):
    frame = cv2.resize(frame, (1920, 1080), 0, 0)
    left_players, right_players, round_timer, left_score, right_score, round_number, killfeed = cropping_agent.cropFrame(frame)
    left_name, right_name = cropping_agent.getTeamNames(frame)
    left_name = cv2.resize(left_name, (0,0), fx=3, fy=3)
    right_name = cv2.resize(right_name, (0,0), fx=3, fy=3)
    text_detection_agent.parseOutput(text_detection_agent.readTextFromImage(left_name))
    text_detection_agent.parseOutput(text_detection_agent.readTextFromImage(right_name))
    for player in right_players:
        crops = cropping_agent.cropIndividualPlayer(player)
        crops = cropping_agent.reverseRightPlayer(crops)
        text_detection_agent.parseOutput(text_detection_agent.readTextFromImage(crops.playerName))
    gamestate = GameState()

    # for each player in left_players and right_players
        # call agent classifier
        # call easyocr to read player name


# processes every subsequent screenshot after first
# calls easyocr for killfeed analysis
# calls blob detection for ability change
# calls ult classifier for ult change -> calls blob detection if ult classifier returns non-ult
# calls easyocr for score / round number / round timer
def processFrame(frame):
    frame = cv2.resize(frame, (1920, 1080), 0, 0)
    left_players, right_players, round_timer, left_score, right_score, round_number, killfeed = cropping_agent.cropFrame(frame)
    # TODO: determine what type of frame it is
    determineFrameType(frame, left_score, right_score)
    initialProcessing(frame)
    
    counter = 0
    cv2.imshow("left score", left_score)
    cv2.imshow("right score", right_score)
    cv2.imshow("round timer", round_timer)
    cv2.imshow("round number", round_number)
    
    for player in right_players:
        crops = cropping_agent.cropIndividualPlayer(player)
        crops = cropping_agent.reverseRightPlayer(crops)
        # cropping_agent.showPlayerCrops(crops)
        # cv2.imwrite("assets\\players\\{}.png".format(counter), player)
        counter += 1
    for player in left_players:
        crops = cropping_agent.cropIndividualPlayer(player)
        # cropping_agent.showPlayerCrops(crops)
        # cv2.imwrite("assets\\players\\{}.png".format(counter), player)
        # counter += 1
    counter = 0
    for kill_event in killfeed:
        cv2.imwrite("assets\\killfeed_examples\\{}.png".format(counter), kill_event)
        counter += 1
    # return capture_names


path = "assets\\screenshots\\C9vsDRXHaven4.png"
# path = "test_screenshots\capture93619842.png"
img = cv2.imread(path)
cropping_agent = Cropping("config\\preround_hud_config.json")
text_detection_agent = TextDetector()
curr = round(time.time() * 1000)
processFrame(img)
curr = round(time.time() * 1000) - curr
print(str(curr))

