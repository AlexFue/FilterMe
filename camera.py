import time
import cv2
from flask import Flask, render_template, Response

class Camera:
    def gen(self):
        cap = cv2.VideoCapture(0)
        while cap.isOpened():
            ret, img = cap.read()
            if ret == True:
                img = cv2.resize(img, (0, 0), fx = 0.5, fy = 0.5)
                frame = cv2.imencode('.jpg', img)[1].tobytes()
                yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
                time.sleep(0.1)
            else:
                break



