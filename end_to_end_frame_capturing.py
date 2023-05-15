import cv2
import pafy
import urllib
import random

# vodUrl = link to youtube VOD of valorant match
# startTime = game start time within the vod (in seconds)
# duration = length of the game within the vod (in seconds)
def processVOD(vodUrl, startTime, duration):
    #Getting video id from the url string
    url_data = urllib.parse.urlparse(vodUrl)
    query = urllib.parse.parse_qs(url_data.query)
    id = query["v"][0]
    video = 'https://youtu.be/{}'.format(str(id))

    #Using the pafy library for youtube videos
    urlPafy = pafy.new(video)
    videoplay = urlPafy.getbestvideo(preftype="any")

    cap = cv2.VideoCapture(videoplay.url)

    milliseconds = 1000
    endTime = startTime + duration

    # Passing the start and end time for CV2
    cap.set(cv2.CAP_PROP_POS_MSEC, startTime*milliseconds)

    #Will execute till the duration specified by the user
    frame_count = 0
    video_framerate = cap.get(cv2.CAP_PROP_FPS)
    if video_framerate > 30:
        frame_skip = 8
    else:
        frame_skip = 4
    while True and cap.get(cv2.CAP_PROP_POS_MSEC)<=endTime*milliseconds:
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

processVOD("https://www.youtube.com/watch?v=CZMqTbFLYTY", 1293, 1996)