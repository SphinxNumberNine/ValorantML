from PIL import Image, ImageOps
from pytesseract import pytesseract
import cv2

# Defining paths to tesseract.exe
# and the image we would be using
path_to_tesseract = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
left_score_path = "top_of_hud\\left_score_number.png"
right_score_path = "top_of_hud\\right_score_number.png"
round_number_path = "top_of_hud\\round_ number.png"
round_timer_path = "top_of_hud\\round_timer.png"
killfeed_path = "test_killfeed.png"
kill_event_path = "killfeed\\1.png"

# Opening the image & storing it in an image object
image = cv2.imread(kill_event_path, cv2.IMREAD_GRAYSCALE)
image = cv2.resize(image, (0,0), fx=3, fy=3)
# cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
im_bw = cv2.threshold(image, 180, 255, cv2.THRESH_BINARY)[1]
contours, hierarchy = cv2.findContours(im_bw, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(im_bw, contours, -1, (255, 255, 255), 1)
# mask = cv2.inRange(image, (160, 160, 160), (255, 255, 255))
# mask = cv2.bitwise_not(image)
# thresh = cv2.threshold(
# mask, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
# thresh = cv2.resize(mask, (0, 0), fx=2, fy=2)
cv2.imshow("image", im_bw)
cv2.waitKey(0)

# Providing the tesseract executable
# location to pytesseract library
pytesseract.tesseract_cmd = path_to_tesseract

# Passing the image object to image_to_string() function
# This function will extract the text from the image
# text = pytesseract.image_to_string(
    # thresh, config='--psm 13 --oem 3 digits -c tessedit_char_whitelist=0123456789:')

text = pytesseract.image_to_string(
image, config='--psm 6 --oem 3')

# Displaying the extracted text
print(text)
