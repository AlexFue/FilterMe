import time
import cv2
from flask import Flask, render_template, Response
from PIL import Image



class Filter:
	def find_filter(self, audio):
		dic = {'red' : cv2.COLOR_BGR2GRAY}
		default = 'did not find it here'
		for key, value in dic.items():
			if audio == key:
				return value
				break
		return default








