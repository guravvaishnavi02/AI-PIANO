import cv2,os,urllib.request
import numpy as np
from django.conf import settings
from threading import Thread
import pyautogui
import math
import winsound

def Press(key):
	pyautogui.press(key)

class Webcam(object):
	def __init__(self):
		self.video = cv2.VideoCapture(0)

	def __del__(self):
		self.video.release()

	def get_frame(self):
		# musical notes (C, D, E, F, G, A, B)
		NOTES = [262, 294, 330, 350, 393, 441, 494, 524, 588, 660, 699, 784, 880, 989, 1047 ]
		readSucsess, sourceImage = self.video.read()
		sourceImage = cv2.flip(sourceImage, 1)
		sourceImage = cv2.resize(sourceImage, (640, 480), interpolation = cv2.INTER_LINEAR)
		crop = sourceImage[400:480, 5:635]
		color = (0,0,0)
		thickness = 2
		sourceImage = cv2.rectangle(sourceImage,(5,400),(635,480),(0,0,0),3)
		sourceImage = cv2.line(sourceImage, (50,400), (50,480), (0,0,0), thickness)
		sourceImage = cv2.line(sourceImage, (95,400), (95,480), color, thickness)
		sourceImage = cv2.line(sourceImage, (140,400), (140,480), color, thickness)
		sourceImage = cv2.line(sourceImage, (185,400), (185,480), color, thickness)
		sourceImage = cv2.line(sourceImage, (230,400), (230,480), color, thickness)
		sourceImage = cv2.line(sourceImage, (275,400), (275,480), color, thickness)
		sourceImage = cv2.line(sourceImage, (320,400), (320,480), color, thickness)
		sourceImage = cv2.line(sourceImage, (365,400), (365,480), color, thickness)
		sourceImage = cv2.line(sourceImage, (410,400), (410,480), color, thickness)
		sourceImage = cv2.line(sourceImage, (455,400), (455,480), color, thickness)
		sourceImage = cv2.line(sourceImage, (500,400), (500,480), color, thickness)
		sourceImage = cv2.line(sourceImage, (545,400), (545,480), color, thickness)
		sourceImage = cv2.line(sourceImage, (590,400), (590,480), color, thickness)

		min_YCrCb = np.array([0,133,77],np.uint8)
		max_YCrCb = np.array([255,173,127],np.uint8)
		# Convert image to YCrCb
		imageYCrCb = cv2.cvtColor(crop,cv2.COLOR_BGR2YCR_CB)
		# Find region with skin tone in YCrCb image
		skinRegion = cv2.inRange(imageYCrCb,min_YCrCb,max_YCrCb) 
		skin = cv2.bitwise_and(crop, crop, mask = skinRegion)

		# initialise switch
		switch = True
		# Do contour detection on skin region
		contours, hierarchy = cv2.findContours(skinRegion, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
		cnt = contours[0]
		area = cv2.contourArea(cnt)
		print(area)
		if area > 2:
			if len(contours) != 0:
				contour = max(contours, key = cv2.contourArea)
				M = cv2.moments(contour)
				if(M["m00"] != 0):
					cx = int(M["m10"]/M["m00"])
					cy = int(M["m01"]/M["m00"])
					area = M["m00"]
					sourceImage = cv2.circle(sourceImage, (cx, cy+400), 5 , (0, 0 , 225), -1)
					if cx < 45:
						if switch:
							winsound.Beep(NOTES[0], 1000)
						switch = not switch
					elif cx > 45 and cx < 90:
						if switch:
							winsound.Beep(NOTES[1], 1000)
						switch = not switch
					elif cx > 90 and cx < 135:
						if switch:
							winsound.Beep(NOTES[2], 1000)
						switch = not switch
					elif cx > 135 and cx < 180:
						if switch:
							winsound.Beep(NOTES[3], 1000)
						switch = not switch
					elif cx > 180 and cx < 225:
						if switch:
							winsound.Beep(NOTES[4], 1000)
						switch = not switch
					elif cx > 225 and cx < 270: 
						if switch:
							winsound.Beep(NOTES[5], 1000)
						switch = not switch
					elif cx > 270 and cx < 315:
						if switch:
							winsound.Beep(NOTES[6], 1000)
						switch = not switch
					elif cx > 315 and cx < 360:
						if switch:
							winsound.Beep(NOTES[7], 1000)
						switch = not switch
					elif cx > 360 and cx < 450:
						if switch:
							winsound.Beep(NOTES[8], 1000)
						switch = not switch
					elif cx > 405 and cx < 450:
						if switch:
							winsound.Beep(NOTES[9], 1000)
						switch = not switch
					elif cx > 450 and cx < 495:
						if switch:
							winsound.Beep(NOTES[10], 1000)
						switch = not switch
					elif cx > 495 and cx < 540:
						if switch:
							winsound.Beep(NOTES[11], 1000)
						switch = not switch
					elif cx > 540 and cx < 585:
						if switch:
							winsound.Beep(NOTES[12], 1000)
						switch = not switch
					elif cx > 585 and cx < 630:
						if switch:
							winsound.Beep(NOTES[13], 1000)
						switch = not switch
					elif cx > 630:
						if switch:
							winsound.Beep(NOTES[14], 1000)
						switch = not switch
		ret, jpeg = cv2.imencode('.jpg', sourceImage)
		return jpeg.tobytes()