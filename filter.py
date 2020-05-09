import time
import cv2
from flask import Flask, render_template, Response
from PIL import Image

class Filter:
	def find_filter(self, audio):
		dic = {'Gray' : cv2.COLOR_BGR2GRAY,
			   'alien' : cv2.COLOR_BGR2HLS,
			   'Beach' : cv2.COLOR_BGR2LUV,
			   'lime' : cv2.COLOR_BGR2Lab,
			   'black and white x 4' : cv2.COLOR_BGR2YUV_I420,
			   'smurf' : cv2.COLOR_RGB2BGRA, 
			   'apply negative' : 'apply negative',
               'apply Gray' : 'apply Gray'}
		default = 'did not find it here'
		for key, value in dic.items():
			if audio == key:
				return value
				break
		return default
