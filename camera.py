import time
import cv2
from flask import Flask, render_template, Response
import os

def apply(applyfilter, frame):
    # A list of filters that we wanted to experiment with
    if applyfilter == 'grayscale':
        return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    if applyfilter == 'negative':
        return cv2.bitwise_not(frame)
    if applyfilter == 'red':
        return cv2.addWeighted((40,40,240,1), .25, frame, .89, 0, frame)
    if applyfilter == 'blue':
        return cv2.addWeighted((255,0,0,1), .25, frame, .89, 0, frame)
    if applyfilter == 'green':
        return cv2.addWeighted((0,255,60,1), .25, frame, .89, 0, frame)
    if applyfilter == 'yellow':
        return cv2.addWeighted((0,255,255,1), .25, frame, .89, 0, frame)
    if applyfilter == 'orange':
        return cv2.addWeighted((0,162,255,1), .25, frame, .89, 0, frame)
    if applyfilter == 'purple':
        return cv2.addWeighted((125,0,128,1), .25, frame, .89, 0, frame)

class FilterCamera(object):
    def __init__(self, filter):
        global video
        self.video = cv2.VideoCapture(0)
        # Global variable for the users filters choice (referring to value, not key)
        global filters
        filters = filter
        # Making lists for the different types of filters used.
        global list_filters
        global non_filter
        global color_map
        list_filters = ['52', '50', '44', '128']
        non_filter = ['gray','negative', 'red', 'blue', 'green', 'yellow', 'orange', 'purple']
        color_map = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']

    def __del__(self):
       self.video.release()

    def get_frame(self):
        ret, frame = self.video.read()
        # DO WHAT YOU WANT WITH TENSORFLOW / KERAS AND OPENCV
        # Checks what list the user's filter choice goes into.
        if str(filters) in list_filters:
            frame = cv2.flip(frame,1)
            user_filter = filters
            color_cam = cv2.cvtColor(frame, user_filter)
            ret, jpeg = cv2.imencode('.jpg', color_cam)
            return jpeg.tobytes()
        elif filters in non_filter:
            frame = cv2.flip(frame,1)
            user_filter = apply(filters, frame)
            ret, jpeg = cv2.imencode('.jpg', user_filter)
            return jpeg.tobytes()
        elif filters == 'none':
            frame = cv2.flip(frame,1)
            ret, jpeg = cv2.imencode('.jpg', frame)
            return jpeg.tobytes()
        elif str(filters) in color_map:
            frame = cv2.flip(frame,1)
            ret, jpeg = cv2.imencode('.jpg', cv2.applyColorMap(frame, filters))
            return jpeg.tobytes()      
    def save_image_two(self):
        try:
        # creating a folder named data
            if not os.path.exists('images'):
                os.makedirs('images')
        # if not created then raise error
        except OSError:
            print('Error: Creating directory of data')
        # frame
        currentframe = 1
        ret, frame = self.video.read()

        if str(filters) in list_filters:
            frame = cv2.flip(frame,1)
            user_filter = filters
            color_cam = cv2.cvtColor(frame, user_filter)
            ret, jpeg = cv2.imencode('.jpg', color_cam)
            if ret:
        # if video is still left continue creating images
                name = './images/ColorSpace' + str(currentframe) + '.jpg'
                currentframe += 1
                cv2.imwrite(name, cv2.cvtColor(frame, user_filter))
        elif filters in non_filter:
            frame = cv2.flip(frame,1)
            user_filter = apply(filters, frame)
            ret, jpeg = cv2.imencode('.jpg', user_filter)
            if ret:
        # if video is still left continue creating images
                name = './images/Overlay' + str(currentframe) + '.jpg'
                currentframe += 1
                cv2.imwrite(name, apply(filters, frame))
        elif str(filters) in color_map:
            frame = cv2.flip(frame,1)
            ret, jpeg = cv2.imencode('.jpg', cv2.applyColorMap(frame, filters))
            if ret:
        # if video is still left continue creating images
                name = './images/ColorMap' + str(currentframe) + '.jpg'
                currentframe += 1
                cv2.imwrite(name, cv2.applyColorMap(frame, filters))
        else:
            if ret:
        # if video is still left continue creating images
                name = './images/None' + str(currentframe) + '.jpg'
                currentframe += 1
                # writing the extracted images
                cv2.imwrite(name, frame)



