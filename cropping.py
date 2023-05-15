# Import packages
import cv2
import numpy as np
import random

start_points = [(6,10), (6,116), (6, 222), (6, 328), (6, 434)]
x_offset, y_offset = 312, 90

icon_x_offset, icon_y_offset = 72, 54
 
img = cv2.imread('test_screenshots\capture2.0.png')
h, w, alpha = img.shape
print(img.shape) # Print image shape
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
    hud_icon_right = (cv2.flip(player1_right, 1))[0:icon_y_offset, 0:icon_x_offset].copy()
    cv2.imwrite("test_crops\\left_" + file_name + ".png", player1_left)
    cv2.imwrite("test_crops\\right_" + file_name + ".png", player1_right)
    cv2.imwrite("icons_from_screenshots\\" + file_name + ".png", hud_icon_left)
    cv2.imwrite("icons_from_screenshots\\" + file_name + "_right.png", hud_icon_right)
 
cv2.waitKey(0)
cv2.destroyAllWindows()