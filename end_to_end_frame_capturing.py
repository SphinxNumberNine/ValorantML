import cv2
import pafy
import urllib
import random
import os

# vodUrl = link to youtube VOD of valorant match
# startTime = game start time within the vod (in seconds)
# duration = length of the game within the vod (in seconds)


def processVOD(vodUrl, startTime, duration):
    # Getting video id from the url string
    url_data = urllib.parse.urlparse(vodUrl)
    query = urllib.parse.parse_qs(url_data.query)
    id = query["v"][0]
    video = 'https://youtu.be/{}'.format(str(id))

    # Using the pafy library for youtube videos
    urlPafy = pafy.new(video)
    videoplay = urlPafy.getbestvideo(preftype="any")

    cap = cv2.VideoCapture(videoplay.url)

    milliseconds = 1000
    endTime = startTime + duration

    # Passing the start and end time for CV2
    cap.set(cv2.CAP_PROP_POS_MSEC, startTime*milliseconds)

    # Will execute till the duration specified by the user
    frame_count = 0
    video_framerate = cap.get(cv2.CAP_PROP_FPS)
    if video_framerate > 30:
        frame_skip = 8
    else:
        frame_skip = 4
    while True and cap.get(cv2.CAP_PROP_POS_MSEC) <= endTime*milliseconds:
        for i in range(0, frame_skip):
            cap.read()
        success, img = cap.read()
        cv2.imshow("Image", img)
        cv2.waitKey(1)

        randomInt = str(random.randint(0, 100000000))
        if frame_count % 300 == 0:
            file_name = "test_screenshots\capture" + randomInt + ".png"
            cv2.imwrite(file_name, img)

        frame_count += 1


def processSingleImage(filePath):
    start_points = [(6, 10), (6, 116), (6, 222), (6, 328), (6, 434)]
    x_offset, y_offset = 312, 90

    icon_x_offset, icon_y_offset = 72, 54

    img = cv2.imread(filePath)
    h, w, alpha = img.shape
    print(img.shape)  # Print image shape
    cv2.imshow("original", img)

    # Cropping an image
    cropped_image = img[540:1065, 10:333].copy()
    cropped_image_2 = img[540:1065, w-333:w-10].copy()

    # Display cropped image
    cv2.imshow("cropped", cropped_image)
    cv2.imshow("cropped", cropped_image_2)

    for x, y in start_points:
        file_name = str(random.randint(0, 10000000))
        player1_left = cropped_image[y:y+y_offset, x:x+x_offset].copy()
        hud_icon_left = player1_left[0:icon_y_offset, 0:icon_x_offset].copy()
        player1_right = cropped_image_2[y:y+y_offset, x:x+x_offset].copy()
        hud_icon_right = (cv2.flip(player1_right, 1))[
            0:icon_y_offset, 0:icon_x_offset].copy()
        cv2.imwrite("test_crops\\left_" + file_name + ".png", player1_left)
        cv2.imwrite("test_crops\\right_" + file_name + ".png", player1_right)
        cv2.imwrite("icons_from_screenshots\\" +
                    file_name + ".png", hud_icon_left)
        cv2.imwrite("icons_from_screenshots\\" +
                    file_name + "_right.png", hud_icon_right)


def processImages():
    for file in os.listdir("test_screenshots\\"):
        processSingleImage("test_screenshots\\" + file)


# processVOD("https://www.youtube.com/watch?v=CZMqTbFLYTY", 1293, 1996)

processImages()
