import threading

import response as response
from django.http import HttpResponse, StreamingHttpResponse
from django.shortcuts import render
from django.views.decorators.clickjacking import xframe_options_exempt
import cv2
# Create your views here.
from django.views import View
from odf.draw import Object


def gen_frames(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


class IndexView(object):
    def __init__(self, stream_url):
        self.video = cv2.VideoCapture(stream_url)
        (self.grabbed, self.frame) = self.video.read()
        threading.Thread(target=self.update, args=()).start()

    def __del__(self):
        self.video.release()

    def get_frame(self):
        image = self.frame
        image = cv2.resize(image, (400, 300))
        _, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()

    def update(self):
        while True:
            (self.grabbed, self.frame) = self.video.read()


@xframe_options_exempt
def video_feed(request):
    username = request.GET.get('username', 'admin')
    password = request.GET.get('password', 'adminpass1')
    host = request.GET.get('host', '192.168.0.108')
    port = request.GET.get('port', '554')

    stream_url = f'rtsp://{username}:{password}@{host}:{port}/cam/realmonitor?channel=1&subtype=0'
    cam = IndexView(stream_url)
    return StreamingHttpResponse(gen_frames(cam), content_type='multipart/x-mixed-replace; boundary=frame')


def index(request):
    return render(request, 'index.html')

