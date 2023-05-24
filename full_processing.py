import cv2
import pafy
import urllib
import random
import os
import json
import threading
import numpy as np

class PlayerCrops:
    agentImage = None
    playerName = None
    playerCredits = None
    ability1 = None
    ability2 = None
    ability3 = None
    ult = None
    playerArmor = None
    playerHealth = None

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

# given crop of 1 single player's hud: returns the agent icon image
def getAgentImageFromPlayerHud(player_hud):
    icon_x_offset, icon_y_offset = 72, 54 # constants
    hud_icon = player_hud[0:icon_y_offset, 0:icon_x_offset].copy()
    return hud_icon

# given crop of 1 single player's hud: returns the player's name crop
def getPlayerNameFromPlayerHud(player_hud):
    start_y, end_y = 62, 84
    start_x, end_x = 0, 160
    player_name = player_hud[start_y: end_y, start_x: end_x].copy()
    return player_name

# given crop of 1 single player's hud: returns the player's credits crop
def getPlayerCreditsFromPlayerHud(player_hud):
    start_y, end_y = 34, 50
    start_x, end_x = 266, 306
    credits = player_hud[start_y: end_y, start_x: end_x].copy()
    return credits

# non-astra usecases only
# given crop of 1 single player's hud: returns array of 3 images containing ability crops
def getAbilityCrops(player_hud):
    start_points = [(70, 32), (111, 32), (150, 32)]
    x_offset, y_offset = 40, 17
    img = player_hud.copy()

    ability_crops = []
    for x, y in start_points:
        crop = img[y: y + y_offset, x: x + x_offset]
        ability_crops.append(crop)

    return ability_crops

# given crop of 1 single player's hud: returns crop of ult (could be dots, could be ult icon)
def getUltCrop(player_hud):
    start_point = (150, 60)
    x = start_point[0]
    y = start_point[1]
    x_offset, y_offset = 90, 30
    img = player_hud.copy()
    h, w, alpha = img.shape
    ult_crop = img[y: y + y_offset, x: x + x_offset]
    return ult_crop

# given crop of 1 single player's hud: returns crop of armor number
def getArmorNumberCrop(player_hud):
    start_y, end_y = 63, 85
    start_x, end_x = 249, 266
    armor_number = player_hud[start_y: end_y, start_x: end_x].copy()
    return armor_number

def getHealthNumberCrop(player_hud):
    start_y, end_y = 66, 85
    start_x, end_x = 270, 305
    health_number = player_hud[start_y: end_y, start_x: end_x].copy()
    return health_number

# given crop of 1 single player's hud, returns object with 9 images:
# image 1: agent image
# image 2: player name
# image 3: player credits
# image 4: first ability dots
# image 5: second ability dots
# image 6: third ability dots
# image 7: ult ability dots / icon
# image 8: armor number image
# image 9: health number image
def cropIndividualPlayer(player_hud):
    crops = PlayerCrops()
    crops.agentImage = getAgentImageFromPlayerHud(player_hud)
    crops.playerName = getPlayerNameFromPlayerHud(player_hud)
    crops.playerCredits = getPlayerCreditsFromPlayerHud(player_hud)
    abilities = getAbilityCrops(player_hud)
    crops.ability1 = abilities[0]
    crops.ability2 = abilities[1]
    crops.ability3 = abilities[2]
    crops.ult = getUltCrop(player_hud)
    crops.playerArmor = getArmorNumberCrop(player_hud)
    crops.playerHealth = getHealthNumberCrop(player_hud)
    return crops
    
# returns 2 arrays of 5 images each - the left players crops and the right player crops
def cropPlayerHuds(frame):
    h, w, alpha = frame.shape
    left_player_hud = frame[540:1065, 10:333].copy()
    right_player_hud = frame[540:1065, w-333:w-10].copy()

    start_points = [(6, 10), (6, 116), (6, 222), (6, 328), (6, 434)] # constants
    x_offset, y_offset = 312, 90 # constants

    left_players = []
    right_players = []

    for x, y in start_points:
        player_left = left_player_hud[y:y+y_offset, x:x+x_offset].copy()
        player_right = cv2.flip(right_player_hud[y:y+y_offset, x:x+x_offset].copy(), 1)
        left_players.append(player_left)
        right_players.append(player_right)

    return left_players, right_players

def cropKillfeed(frame):
    kill_events = []
    for i in range(11):
        crop = frame[(i * 39) + 96: ((i + 1) * 39) + 96, 1330:1920]
        kill_events.append(crop)
    return kill_events
    

# returns images of all points of interest on the full frame
def cropFrame(frame):
    # datatypes: [img], [img], img, img, img, img, [img]
    left_players, right_players = cropPlayerHuds(frame)
    return left_players, right_players, round_timer, left_score, right_score, round_number, killfeed

def processFrame(frame):
    frame = cv2.resize(frame, (1920, 1080), 0, 0)


    return capture_names

path = "screenshots\\C9vsDRXHaven18.png"
img = cv2.imread(path)
killEvents = cropKillfeed(img)
counter = 0
for event in killEvents:
    cv2.imshow("test", event)
    cv2.imwrite("killfeed\\{}.png".format(counter), event)
    cv2.waitKey(0)
    counter += 1

