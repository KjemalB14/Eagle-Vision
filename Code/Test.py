from picamera2 import Picamer2, Preview
import cv2 as cv
import time

img = cv.imread("/home/ENKH/Downloads/2024-ferrari-sf90-xx-stradale-122-654a66978f827.jpg")
cv.imshow("display", img)
k = cv.waitKey(0)