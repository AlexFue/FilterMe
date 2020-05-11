import time
import cv2
import random
from flask import Flask, render_template, Response
from camera import FilterCamera
from speech import Speech
from filter import Filter
import os


app = Flask(__name__)
# Function that generates the camera on the webpage
def gen(camera):
	while True:
		global frame
		frame = camera.get_frame()
		yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

# Function that generates the filtered camera on the webpage
def filter_gen(camera, filter):
	while True:
		frame = camera.get_frame()
		yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

# This is the homepage route
@app.route('/')
def home():
	#renders the homepage template
    return render_template('homepage.html')

# This is the secondpage route
@app.route('/second')
def second():
	#renders the second page template
    return render_template('secondpage.html')

# This is the page with the filter route
@app.route('/filters_page')
def filters_page():
	# Render the filtered page template
	return render_template('filters.html')

# This is the video feed route that plays on the second page 
@app.route('/video_feed')
def video_feed():
    # Shows the video camera on the second page
    videostream = FilterCamera('none')
    return Response(gen(videostream), mimetype='multipart/x-mixed-replace; boundary=frame')

# This uses what the users choice in order to apply the filtered video
@app.route('/filter_feed')
def filter_feed():
	if choosenfilter != 'did not find it here':
		# Displays the camera with the new filter
		return Response(gen(filtervideostream), mimetype='multipart/x-mixed-replace; boundary=frame') 
	else:
		# If the user choice is not found then it returns a default camera
		videostream = FilterCamera('none')
		return Response(gen(videostream), mimetype='multipart/x-mixed-replace; boundary=frame')

# This is the audio route and plays when user clicks to record themselves saying the filter
@app.route('/audio')
def get_audio():
	# Stores what user said in var
	var = Speech().audio()
	# Var goes into find filter function and returns the found filter into choosenfilter
	global choosenfilter
	choosenfilter = Filter().find_filter(var)
	user_filter = Filter().get_name()
	global filtervideostream
	filtervideostream = FilterCamera(choosenfilter)
	curr_string = "You are currently using " + str(user_filter) + "!"
	return render_template('filters.html', message = curr_string)

@app.route('/random')
def get_random():
	list_of_keys = ['gray', 'negative', 'red', 'blue', 'green', 'yellow', 'orange', 'purple', 'hot', 'pink', 'hsv',
					'cool', 'spring', 'summer', 'ocean', 'rainbow', 'winter', 'jet', 'bone', 'autumn', 'alien',
					'beach', 'lime', 'black and white x 4']
	random_filter = list_of_keys[random.randint(0,22)]
	global choosenfilter
	choosenfilter = Filter().find_filter(random_filter)
	global filtervideostream
	filtervideostream = FilterCamera(choosenfilter)
	curr_string = "You are currently using " + str(random_filter) + "!"
	return render_template('filters.html', message=curr_string)

@app.route('/save_image')
def save_image():
	FilterCamera(choosenfilter).save_image_two()
	return render_template('filters.html', message = "Image saved!")
