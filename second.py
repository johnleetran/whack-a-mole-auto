import cv2
import pyautogui
import mss
import numpy as np
import os

threshold = 0.7
sct = mss.mss()
width, height = pyautogui.size()
print("screen width", width)
print("screen height", height)
monitor = {"top": 0, "left": 0, "width": 600, "height": 600}
mole_images = []
moles_directory = "./images/moles"
for mole_filename in os.listdir(moles_directory):
    if mole_filename.endswith(".jpg") or mole_filename.endswith(".png"):
        filename = moles_directory + '/' + mole_filename
        # print("checking for mole", filename)
        mole_images.append(cv2.imread(filename))

while True:
    print("Taking screenshot")
    #screenshot_filename = sct.shot()
    #screen = cv2.imread(screenshot_filename, cv2.IMREAD_GRAYSCALE)
    screen = np.array(sct.grab(monitor))
    screen_draw = screen[:, :, :3]
    for img in mole_images:
        result = cv2.matchTemplate(
            screen_draw, img, cv2.TM_CCOEFF_NORMED)
        yloc, xloc = np.where(result >= threshold)
        #x, y = pyautogui.position()
        #print("position", "x:", x, "y:", y)
        rectangles = []
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        if max_val >= threshold:
            #print("max_loc", max_loc, "max_val", max_val)
            pyautogui.click(x=max_loc[0]//2, y=max_loc[1]//2)

