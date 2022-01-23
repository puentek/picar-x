'''The first thing to do is to isolate all the blue areas on the image. 
To do this, we first need to turn the color space used by the image, which is RGB (Red/Green/Blue) 
into the HSV (Hue/Saturation/Value) color space.'''
import numpy as np 
import cv2
from picamera.array import PiRGBArray
from picamera import PiCamera

def detect_edges(frame):
    # filter for blue lane lines
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    show_image("hsv", hsv)
    lower_blue = np.array([60, 40, 40])
    upper_blue = np.array([150, 255, 255])
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    show_image("blue mask", mask)

    # detect edges
    edges = cv2.Canny(mask, 200, 400)

    return edges
        
