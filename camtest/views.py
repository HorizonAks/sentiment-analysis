from django.shortcuts import render
from django.views.decorators import gzip
from django.template import loader
from django.http import StreamingHttpResponse
from django.http import HttpResponse
from . import backend
import cv2
import os
import threading

class VideoCamera(object):
    count = 0
    last = "No Face Found"
    def __init__(self):
        self.video = cv2.VideoCapture(0)
        (self.grabbed, self.frame) = self.video.read()
        threading.Thread(target=self.update, args=()).start()

    def __del__(self):
        self.video.release()

    def get_frame(self):
    	self.put_text(self.get_sentiment())
    	image = self.frame
    	t, jpeg = cv2.imencode('.jpg', image)
    	return jpeg.tobytes()

    def update(self):
        while True:
            (self.grabbed, self.frame) = self.video.read()

    def put_text(self,text):
    	font = cv2.FONT_HERSHEY_SIMPLEX
    	color = (0, 255, 255)
    	if text == "anger":
    		color = (255, 0, 0)
    	cv2.putText(self.frame,text,(50, 50),font, 1,color,2,cv2.LINE_4)

    def get_sentiment(self):
    	#print(os.getcwd())
        VideoCamera.count += 1
        if VideoCamera.count%5 != 0:
            if VideoCamera.count > 10000:
                VideoCamera.count = 0
            return VideoCamera.last
        cv2.imwrite("./camtest/buffer/frame"+".jpeg", self.frame)
        frame = open("./camtest/buffer/frame"+".jpeg","r+b")
        sentiment = backend.getsentiment(frame)
        if sentiment == None:
            return VideoCamera.last
        else:
            VideoCamera.last = sentiment
            return sentiment

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield(b'--frame\r\n'
              b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@gzip.gzip_page
def livefe(request):
    template = loader.get_template('underWork.html')
    return HttpResponse(template.render({},request))
    """
    try:
        cam = VideoCamera()
        return StreamingHttpResponse(gen(cam), content_type="multipart/x-mixed-replace;boundary=frame")
    except:  # This is bad! replace it with proper handling
        pass
    """