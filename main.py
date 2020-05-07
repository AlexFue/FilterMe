import time
import cv2
from flask import Flask, render_template, Response
from camera import FilterCamera
from speech import Speech
from filter import Filter

app = Flask(__name__)
#function that generates the camera on the webpage
def gen(camera):
	while True:
		frame = camera.get_frame()
		yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

def filter_gen(camera, filter):
	while True:
		frame = camera.get_frame()
		yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')




#this is the homepage route
@app.route('/')
def home():
	#renders the homepage template
    return render_template('homepage.html')


#this is the secondpage route
@app.route('/second')
def second():
	#renders the second page template
    return render_template('secondpage.html')


#this is the video feed route that plays on the second page 
@app.route('/video_feed')
def video_feed():
    # return Response(Camera().gen(),
    #                 mimetype='multipart/x-mixed-replace; boundary=frame')
    #shows the video camera on the second page
    videostream = FilterCamera('none')
    return Response(gen(videostream), mimetype='multipart/x-mixed-replace; boundary=frame')


#this is the audio route and plays when user clicks to record themselves saying the filter
@app.route('/audio')
def audio():
	#stores what user said in var
	var = Speech().audio()
	#var goes into find filter function and returns the found filter into choosenfilter
	choosenfilter = Filter().find_filter(var)
	filtervideostream = FilterCamera(choosenfilter)
	if choosenfilter != 'did not find it here':
		#shows the camera with the new filter
		return Response(gen(filtervideostream), mimetype='multipart/x-mixed-replace; boundary=frame')
	else:
		return choosenfilter









