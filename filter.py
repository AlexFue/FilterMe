import time
import cv2
from flask import Flask, render_template, Response
from PIL import Image

class Filter:
	def find_filter(self, audio):
		global filter_name
		# A dictionary of the filters and there respective keys
		dic = {'alien' : cv2.COLOR_BGR2HLS,
			   'beach' : cv2.COLOR_BGR2LUV,
			   'lime' : cv2.COLOR_BGR2Lab,
			   'black and white x 4' : cv2.COLOR_BGR2YUV_I420,
			   'autumn': cv2.COLORMAP_AUTUMN,
			   'bone': cv2.COLORMAP_BONE,
			   'jet': cv2.COLORMAP_JET,
			   'winter': cv2.COLORMAP_WINTER,
			   'rainbow': cv2.COLORMAP_RAINBOW,
			   'ocean': cv2.COLORMAP_OCEAN,
			   'summer': cv2.COLORMAP_SUMMER,
			   'spring': cv2.COLORMAP_SPRING,
			   'cool': cv2.COLORMAP_COOL,
			   'hsv': cv2.COLORMAP_HSV,
			   'pink': cv2.COLORMAP_PINK,
			   'hot': cv2.COLORMAP_HOT,
			   'grayscale': 'grayscale',
			   'negative' : 'negative',
			   'red': 'red',
			   'blue': 'blue',
			   'green': 'green',
			   'yellow': 'yellow',
			   'orange': 'orange',
			   'purple': 'purple'}
		default = 'did not find it here'

		# Given the audio file this for loop finds which
		# key word the user selected (if on is selected)
		for key, value in dic.items():
			if audio == key:
				filter_name = key
				return value
				break
			if key in audio:
				filter_name = key
				return value
		filter_name = 'none'
		return default

	def get_name(self):
		if filter_name == 'none':
			return "no filter"
		else:
			return filter_name
