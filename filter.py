import time
import cv2
from flask import Flask, render_template, Response
from PIL import Image



class Filter:
	def find_filter(self, audio):
		dic = {'red' : cv2.COLOR_BGR2GRAY,
			   'black and white' : cv2.COLOR_BGR2GRAY,
			   'alien' : cv2.COLOR_BGR2HLS,
			   'beach' : cv2.COLOR_BGR2LUV,
			   'lime' : cv2.COLOR_BGR2Lab,
			   'black and white times 4' : cv2.COLOR_BGR2YUV_I420,
			   'blueface' : cv2.COLOR_RGB2BGRA}
		default = 'did not find it here'
		for key, value in dic.items():
			if audio == key:
				return value
				break
		return default








