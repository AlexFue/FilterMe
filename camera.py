import time
import cv2
from flask import Flask, render_template, Response

# class Camera:
    # def gen(self):
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


class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)
    def __del__(self):
        self.video.release()
    def get_frame(self):
        ret, frame = self.video.read()
        # DO WHAT YOU WANT WITH TENSORFLOW / KERAS AND OPENCV
        frame = cv2.flip(frame,1)
        # color_gray = cv2.COLOR_BGR2GRAY
        # gray = cv2.cvtColor(frame, color_gray)
        ret, jpeg = cv2.imencode('.jpg', frame)
        return jpeg.tobytes()


class FilterCamera(object):
    def __init__(self, filter):
        self.video = cv2.VideoCapture(0)
    def __del__(self):
        self.video.release()
    def get_frame(self, filter):
        ret, frame = self.video.read()
        # DO WHAT YOU WANT WITH TENSORFLOW / KERAS AND OPENCV
        frame = cv2.flip(frame,1)
        color_gray = filter
        gray = cv2.cvtColor(frame, color_gray)
        ret, jpeg = cv2.imencode('.jpg', gray)
        return jpeg.tobytes()



