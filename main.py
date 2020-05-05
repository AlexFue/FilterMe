import time
import cv2
from flask import Flask, render_template, Response
from camera import Camera

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('homepage.html')



# def gen():
#     cap = cv2.VideoCapture(0)
#     while cap.isOpened():
#         ret, img = cap.read()
#         if ret == True:
#             img = cv2.resize(img, (0, 0), fx = 0.5, fy = 0.5)
#             frame = cv2.imencode('.jpg', img)[1].tobytes()
#             yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
#             time.sleep(0.1)
#         else:
#             break



#to apply filters: user says filter name, api turns speech to text and searches for the filter. then, it does a different app route that corresponds with the filter

@app.route('/second')
def second():
    Camera().gen()
    return render_template('secondpage.html')



@app.route('/video_feed')
def video_feed():
    # cam = Camera()
    return Response(Camera().gen(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')