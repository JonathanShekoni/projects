import cv2
import numpy as np
import mss
import pydirectinput
import pygetwindow as gw
import keyboard
import time

# Get Roblox window
window = gw.getWindowsWithTitle("Roblox")[0]

monitor = {
    "top": window.top,
    "left": window.left,
    "width": window.width,
    "height": window.height
}

sct = mss.mss()

print("Running... Press Q to stop.")

while True:
    screenshot = np.array(sct.grab(monitor))

    # Convert to HSV for better color detection
    hsv = cv2.cvtColor(screenshot, cv2.COLOR_BGR2HSV)

    #TARGET COLOR(Eg.Itadori red,Gojo blue,Hakari green e.t.c)
    lower = np.array([1, 200, 170])
    upper = np.array([6, 255, 255])  # Upper HSV bound
    # =====================================================

    mask = cv2.inRange(hsv, lower, upper)

    #Default to red as placeholder
    red_pixels = np.count_nonzero(mask)

    if red_pixels > 150:   # Adjust this number for accuracy
        print("Specific Red Detected!")
        pydirectinput.keyDown("f")
        time.sleep(0.5)
        pydirectinput.keyUp("f")

    time.sleep(0.2)   # Prevent spam

    # Proper global stop key
    if keyboard.is_pressed("z"):
        print("Stopped.")
        break