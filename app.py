import cv2
import pyautogui
import mss
import numpy as np
import os

threshold = 0.68
sct = mss.mss()
width, height = pyautogui.size()
print("screen width", width)
print("screen height", height)
monitor = {"top": 200, "left": 195, "width": 400, "height": 400}
mole_images = []
moles_directory = "./images/moles"

w=10
h=10

for mole_filename in os.listdir(moles_directory):
    if mole_filename.endswith(".jpg") or mole_filename.endswith(".png"):
        filename = moles_directory + '/' + mole_filename
        # print("checking for mole", filename)
        mole_images.append(cv2.imread(filename))

while True:
    print("Taking screenshot")
    #screenshot_filename = sct.shot()
    #screen = cv2.imread(screenshot_filename, cv2.IMREAD_GRAYSCALE)
    sct_img = sct.grab(monitor)
    #mss.tools.to_png(sct_img.rgb, sct_img.size, output="test.png")
    screen = np.array(sct_img)
    screen_draw = screen[:, :, :3]
    for img in mole_images:
        result = cv2.matchTemplate(
            screen_draw, img, cv2.TM_CCOEFF_NORMED)
        yloc, xloc = np.where(result >= threshold)
        #x, y = pyautogui.position()
        #print("position", "x:", x, "y:", y)
        # min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        yloc, xloc = np.where(result >= threshold)
        rectangles = []
        for (x, y) in zip(xloc, yloc):
            rectangles.append([int(x), int(y), int(w), int(h)])
            rectangles.append([int(x), int(y), int(w), int(h)])
        #print("before", len(rectangles))
        rectangles, weights = cv2.groupRectangles(rectangles, 1, 2)
        #print("after", len(rectangles))

        for (x, y, w, h) in rectangles:
            pyautogui.click(x=x//2 + 200, y=y//2 + 195)
    #break
