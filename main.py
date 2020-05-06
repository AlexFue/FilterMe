import time
import cv2
from flask import Flask, render_template, Response
from camera import VideoCamera
from speech import Speech
from filter import Filter

app = Flask(__name__)

videostream = VideoCamera()

def gen(camera):
	while True:
		frame = camera.get_frame()
		yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')



@app.route('/')
def home():
    return render_template('homepage.html')

#to apply filters: user says filter name, api turns speech to text and searches for the filter. then, it does a different app route that corresponds with the filter


@app.route('/second')
def second():
    return render_template('secondpage.html')


@app.route('/video_feed')
def video_feed():
    # return Response(Camera().gen(),
    #                 mimetype='multipart/x-mixed-replace; boundary=frame')
    return Response(gen(videostream), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/audio')
def audio():
	var = Speech().audio()
	choosenfilter = Filter().find_filter(var)
	if choosenfilter != 'did not find it here':
		# return FilteredCam().master(choosenfilter)
		return Response(FilteredCam().master(choosenfilter), mimetype='multipart/x-mixed-replace; boundary=frame')
	else:
		return choosenfilter









