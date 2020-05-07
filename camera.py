import time
import cv2
from flask import Flask, render_template, Response



# class VideoCamera(object):
#     def __init__(self):
#         self.video = cv2.VideoCapture(0)
#     def __del__(self):
#         self.video.release()
#     def get_frame(self):
#         ret, frame = self.video.read()
#         # DO WHAT YOU WANT WITH TENSORFLOW / KERAS AND OPENCV
#         frame = cv2.flip(frame,1)
#         # color_gray = cv2.COLOR_BGR2GRAY
#         # gray = cv2.cvtColor(frame, color_gray)
#         ret, jpeg = cv2.imencode('.jpg', frame)
#         return jpeg.tobytes()


class FilterCamera(object):
    def __init__(self, filter):
        self.video = cv2.VideoCapture(0)
        global filters
        filters = filter
    def __del__(self):
        self.video.release()
    def get_frame(self):
        ret, frame = self.video.read()
        # DO WHAT YOU WANT WITH TENSORFLOW / KERAS AND OPENCV
        if filters != 'none':
            frame = cv2.flip(frame,1)
            user_filter = filters
            color_cam = cv2.cvtColor(frame, user_filter)
            ret, jpeg = cv2.imencode('.jpg', color_cam)
            return jpeg.tobytes()
        else:
            frame = cv2.flip(frame,1)
            ret, jpeg = cv2.imencode('.jpg', frame)
            return jpeg.tobytes()

# class FilterCamera(object):
#     def __init__(self, filter):
#         self.video = cv2.VideoCapture(0)
#         global filters
#         filters = filter
#     def __del__(self):
#         self.video.release()
#     def get_frame(self):
#         ret, frame = self.video.read()
#         # DO WHAT YOU WANT WITH TENSORFLOW / KERAS AND OPENCV
#         frame = cv2.flip(frame,1)
#         user_filter = filters
#         color_cam = cv2.cvtColor(frame, user_filter)
#         ret, jpeg = cv2.imencode('.jpg', color_cam)
#         return jpeg.tobytes()


