import time
import cv2
from flask import Flask, render_template, Response

class Filter:
	def apply_invert(frame):
		return cv2.bitwise_not(frame)