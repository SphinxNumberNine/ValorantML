import cv2
import pafy
import urllib

#Ask the user for url input
url = input("Enter Youtube Video URL: ")

#Getting video id from the url string
url_data = urllib.parse.urlparse(url)
query = urllib.parse.parse_qs(url_data.query)
id = query["v"][0]
video = 'https://youtu.be/{}'.format(str(id))

#Using the pafy library for youtube videos
urlPafy = pafy.new(video)
videoplay = urlPafy.getbestvideo(preftype="any")

cap = cv2.VideoCapture(videoplay.url)

#Asking the user for video start time and duration in seconds
milliseconds = 1000
start_time = int(input("Enter Start time: "))
end_time = int(input("Enter Length: "))
end_time = start_time + end_time

# Passing the start and end time for CV2
cap.set(cv2.CAP_PROP_POS_MSEC, start_time*milliseconds)

#Will execute till the duration specified by the user
frame_count = 0
while True and cap.get(cv2.CAP_PROP_POS_MSEC)<=end_time*milliseconds:
    for i in range(0, 8):
        cap.read()
    success, img = cap.read()
    cv2.imshow("Image", img)
    cv2.waitKey(1)
    
    if frame_count % 300 == 0:
        file_name = "test_screenshots\capture" + str(int(frame_count / 300)) + ".png"
        cv2.imwrite(file_name, img)

    frame_count += 1