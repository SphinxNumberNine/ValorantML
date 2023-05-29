import cv2
import pafy
import urllib
import random
import os
import json
import threading
import numpy as np

# vodUrl = link to youtube VOD of valorant match
# startTime = game start time within the vod (in seconds)
# duration = length of the game within the vod (in seconds)


def processVOD(vodName, vodUrl, startTime, duration):
    # Getting video id from the url string
    url_data = urllib.parse.urlparse(vodUrl)
    print(url_data)
    query = urllib.parse.parse_qs(url_data.query)
    print(query)

    if "live" in url_data.path:
        id = url_data.path.split("/")[2]
    else: 
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
    print("Framerate: " + str(video_framerate))
    if video_framerate > 30:
        frame_skip = 8
    else:
        frame_skip = 4
    capture_counter = 1
    capture_names = []
    while True and cap.get(cv2.CAP_PROP_POS_MSEC) <= endTime*milliseconds:
        for i in range(0, frame_skip):
            cap.read()
        success, img = cap.read()
        cv2.imshow("Image", img)
        cv2.waitKey(1)

        if frame_count % 300 == 0:
            file_name = "assets\\test_screenshots\\" + vodName + \
                str(capture_counter) + ".png"
            capture_names.append(file_name)
            cv2.imwrite(file_name, img)
            capture_counter += 1

        frame_count += 1

    return capture_names


def processSingleImage(filePath, left_agents, right_agents):
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

    counter = 0
    for x, y in start_points:
        file_name = str(random.randint(0, 10000000))
        player1_left = cropped_image[y:y+y_offset, x:x+x_offset].copy()
        print("left processing " + left_agents[counter])
        crop_single_hud(player1_left)
        crop_ult(player1_left)
        hud_icon_left = player1_left[0:icon_y_offset, 0:icon_x_offset].copy()
        player1_right = cropped_image_2[y:y+y_offset, x:x+x_offset].copy()
        crop_single_hud(cv2.flip(player1_right, 1))
        crop_ult(cv2.flip(player1_right, 1))
        hud_icon_right = (cv2.flip(player1_right, 1))[
            0:icon_y_offset, 0:icon_x_offset].copy()
        # cv2.imwrite("test_crops\\left_" + file_name + ".png", player1_left)
        # cv2.imwrite("test_crops\\right_" + file_name + ".png", player1_right)
        # cv2.imwrite("test_dataset\\" + left_agents[counter] + "\\" +
                    # file_name + ".png", hud_icon_left)
        # cv2.imwrite("test_dataset\\" + right_agents[counter] + "\\" +
                    # file_name + ".png", hud_icon_right)
        counter += 1


def processImages():
    for file in os.listdir("test_screenshots\\"):
        try:
            processSingleImage("test_screenshots\\" + file)
        except:
            print("File not found")


def processSingleVod(vod):
    processed_files = processVOD(
        vod["name"], vod["url"], vod["start_time"], vod["duration"])
    for file in processed_files:
        processSingleImage(file, vod["left_agents"], vod["right_agents"])


def processAll():
    file = open("vod_data.json")
    vod_data = json.load(file)
    threads = []
    for vod in vod_data["vod_data"]:
        thread = threading.Thread(target=processSingleVod, args=(vod,))
        threads.append(threads)
        thread.start()

    for thread in threads:
        thread.join()

    file.close()


def recover():
    file = open("vod_data.json")
    vod_data = json.load(file)
    print(vod_data)
    directory = "screenshots"
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        for vod in vod_data["vod_data"]:
            if vod["name"] in f:
                print("Proccesing " + f)
                processSingleImage(f, vod["left_agents"], vod["right_agents"])


def count_dots(img):
    img = masked_image(img)
    # cv2.imshow("blobbed image", img)
    # cv2.waitKey(0)
    print(img.dtype)
    img = cv2.normalize(img, dst=None, alpha=0, beta=255,
                        norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)
    circles = cv2.HoughCircles(
        img, cv2.HOUGH_GRADIENT, 1, 3, param1=20, param2=9, minRadius=1, maxRadius=100)
    index = 0
    print(circles)
    if circles is not None:
        circles = circles[0]
        # convert the (x, y) coordinates and radius of the circles to integers
        circles = np.round(circles[:]).astype("int")

        # loop over the (x, y) coordinates and radius of the circles
        for (x, y, r) in circles:
            # draw the circle in the output image,
            #   then draw a rectangle corresponding to the center of the circle
            cv2.circle(img, (x, y), r, (255, 0, 255), 2)
            cv2.rectangle(img, (x - 5, y - 5),
                          (x + 5, y + 5), (255, 0, 255), -1)

            index = index + 1
            # print str(index) + " : " + str(r) + ", (x,y) = " + str(x) + ', ' + str(y)
        print('No. of circles detected = {}'.format(index))
        return index
    else:
        print("no circles")
        return 0


def count_blobs(img):
    img = masked_image(img)
    img = cv2.bitwise_not(img)
    img = cv2.resize(img, dsize=(0,0), fx=2, fy=2)
    # cv2.imshow("blobbed image", img)
    # cv2.waitKey(0)
    print(img.dtype)
    img = cv2.normalize(img, dst=None, alpha=0, beta=255,
                        norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)
    # Set up the detector with default parameters.
    detector = cv2.SimpleBlobDetector_create()

    # Detect blobs.
    keypoints = detector.detect(img)
    print("Found {} blobs".format(str(len(keypoints))))
    return len(keypoints)


def masked_image(img):
    # img = cv2.imread(path_to_img)
    img = cv2.GaussianBlur(img, (5, 5), 0)
    lower, upper = np.array([220, 220, 220]), np.array([255, 255, 255])
    mask = cv2.inRange(img, lower, upper)
    result = cv2.bitwise_and(img, img, mask=mask)
    result = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
    print(result.shape)
    cv2.imshow("masked image", result)
    cv2.waitKey(0)
    return result


def crop_single_hud(single_hud_img):  # non-astra usecase
    start_points = [(70, 32), (111, 32), (150, 32)]
    # start_points = [(70, 32)]
    x_offset, y_offset = 40, 17
    # x_offset, y_offset = 120, 20

    img = single_hud_img.copy()
    h, w, alpha = img.shape
    print(img.shape)
    cv2.imshow("original", img)

    counter = 0
    for x, y in start_points:
        crop = img[y: y + y_offset, x: x + x_offset]
        # cv2.imshow("crop" + str(counter), crop)
        # cv2.imwrite("ability_crops\\" + str(counter) + ".png", crop)
        count_blobs(crop)
        counter += 1

    cv2.waitKey(0)

def crop_ult(single_hud_img):
    start_point = (150, 60)
    x = start_point[0]
    y = start_point[1]
    x_offset, y_offset = 90, 30
    img = single_hud_img.copy()
    h, w, alpha = img.shape
    crop = img[y: y + y_offset, x: x + x_offset]
    print("ULT BLOBS")
    count_blobs(crop)

# processSingleImage("test_screenshots\\100TvsLEVLotus7.png", ["cypher", "skye", "omen", "phoenix", "chamber"], ["sova", "jett", "breach", "omen", "killjoy"])
processVOD("test_live", "https://www.youtube.com/live/WYbo5JKhTG8?feature=share&t=16353", 16353, 30)
