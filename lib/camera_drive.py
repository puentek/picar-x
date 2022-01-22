'''The first thing to do is to isolate all the blue areas on the image. 
To do this, we first need to turn the color space used by the image, which is RGB (Red/Green/Blue) 
into the HSV (Hue/Saturation/Value) color space.'''
import numpy as np 
import cv2
from picamera.array import PiRGBArray
from picamera import PiCamera

frame = cv2.imread('/home/pi/DeepPiCar/driver/data/road1_240x320.png')
hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

