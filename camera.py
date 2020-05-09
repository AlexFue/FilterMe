import time
import cv2
from flask import Flask, render_template, Response


def apply(applyfilter, frame):
    if applyfilter == 'apply negative':
        return cv2.bitwise_not(frame)
    if applyfilter == 'apply Gray':
        return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

class FilterCamera(object):
    def __init__(self, filter):
        self.video = cv2.VideoCapture(0)
        global filters
        filters = filter
        print(filters)
        global list_filters
        global non_filter
        list_filters = ['6', '52', '50', '44', '128', '2']
        non_filter = ['apply negative', 'apply Gray',]

    def __del__(self):
       self.video.release()

    def get_frame(self):
        ret, frame = self.video.read()

        # DO WHAT YOU WANT WITH TENSORFLOW / KERAS AND OPENCV
        if str(filters) in list_filters:
            frame = cv2.flip(frame,1)
            user_filter = filters
            color_cam = cv2.cvtColor(frame, user_filter)
            ret, jpeg = cv2.imencode('.jpg', color_cam)
            return jpeg.tobytes()
        elif filters in non_filter:
            print("Gray was found")
            frame = cv2.flip(frame,1)
            user_filter = apply(filters, frame)
            ret, jpeg = cv2.imencode('.jpg', user_filter)
            return jpeg.tobytes()
        elif filters == 'none':
            frame = cv2.flip(frame,1)
            ret, jpeg = cv2.imencode('.jpg', frame)
            return jpeg.tobytes()

# def get_frame(self):
#         # Default camera frame
#         ret, frame = self.video.read()
#         frame = cv2.flip(frame,1)
# ​
#         ret, frame_red = self.video.read()
#         frame_red = cv2.flip(frame_red,1)
# ​
#         ret, frame_blue = self.video.read()
#         frame_blue = cv2.flip(frame_blue,1)
# ​
#         ret, frame_green = self.video.read()
#         frame_green = cv2.flip(frame_green,1)
# ​
#         ret, frame_yellow = self.video.read()
#         frame_yellow = cv2.flip(frame_yellow,1)
# ​
#         ret, frame_orange = self.video.read()
#         frame_orange = cv2.flip(frame_orange,1)
# ​
#         ret, frame_purple = self.video.read()
#         frame_purple = cv2.flip(frame_purple,1)
# ​
#         filter_dict = {
#             'apply_negative' : ,
#             'apply_gray' : ,
#             'apply_red' : cv2.addWeighted((40,40,240,1), .25, frame_red, .89, 0, frame_red),
#             'apply_blue' : cv2.addWeighted((255,0,0,1), .25, frame_blue, .89, 0, frame_blue),
#             'apply_green' : cv2.addWeighted((0,255,60,1), .25, frame_green, .89, 0, frame_green),
#             'apply_yellow' : cv2.addWeighted((0,255,255,1), .25, frame_yellow, .89, 0, frame_yellow),
#             'apply_orange' : cv2.addWeighted((0,162,255,1), .25, frame_orange, .89, 0, frame_orange),
#             'apply_purple' : cv2.addWeighted((125,0,128,1), .25, frame_purple, .89, 0, frame_purple)
#         }
#         ret, jpeg = cv2.imencode('.jpg', filter_dict['apply_purple'])
#         return jpeg.tobytes()