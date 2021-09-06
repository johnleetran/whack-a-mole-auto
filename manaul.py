import cv2 
import pyautogui
import mss
import numpy
import os

good_threshold = 0.7
# sct = mss.mss()
# width, height = pyautogui.size()
# monitor = {"top": 0, "left": 0, "width": width, "height": height}

screens_directory = "./images/screens"
for screen_filename in os.listdir(screens_directory):
    if screen_filename.endswith(".jpg") or screen_filename.endswith(".png"):
        #screen = numpy.array(sct.grab(monitor))
        sfilename = screens_directory + '/' + screen_filename
        screen = cv2.imread(sfilename, cv2.IMREAD_GRAYSCALE)
        screen_draw = screen
        w = 50 
        h = 50
        moles_directory = "./images/moles"
        for mole_filename in os.listdir(moles_directory):
            if mole_filename.endswith(".jpg") or mole_filename.endswith(".png"):
                filename = moles_directory + '/' + mole_filename
                mole_image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
                result = cv2.matchTemplate(screen_draw, mole_image, cv2.TM_CCOEFF_NORMED)
                _, max_val, _, max_loc = cv2.minMaxLoc(result)

                yloc, xloc = numpy.where(result >= good_threshold)
                rectangles = []
                for (x, y) in zip(xloc, yloc):
                    #rectangles.append([int(x), int(y), int(w), int(h)])
                    #rectangles.append([int(x), int(y), int(w), int(h)])
                    # cv2.rectangle(screen, (x + w + w//2, y + h + h//2), (x + w, y + h),(0, 255, 255), 2)
                    pyautogui.click(x=x, y=y)
        #rectangles, weights = cv2.groupRectangles(rectangles, 1, 0.2)
        # cv2.imshow('Screen Shot', screen)
        # cv2.waitKey(0)
