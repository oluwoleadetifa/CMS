import threading
from datetime import datetime, date

from django.http import HttpResponse, StreamingHttpResponse
from django.shortcuts import render
from django.views.decorators.clickjacking import xframe_options_exempt
import cv2

import CCTV.models
from .models import *
# Create your views here.
from django.views import View


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

    def get_shot(self):
        image = self.frame
        jpeg = cv2.imwrite(f'{datetime.now().strftime("%B %d, %Y, %H-%M-%S")}.png', image)
        return jpeg

    def update(self):
        while True:
            (self.grabbed, self.frame) = self.video.read()


@xframe_options_exempt
def video_feed(request, *args, **kwargs):
    id = kwargs.get('id')

    param = CCTV.models.Camera.objects.get(id=id)
    stream_url = f'rtsp://{param.username}:{param.password}@{param.host}:{param.port}/cam/realmonitor?channel=1&subtype=0'
    cam = IndexView(stream_url)
    return StreamingHttpResponse(gen_frames(cam), content_type='multipart/x-mixed-replace; boundary=frame')


def index(request):
    context = {
        'cameras': Camera.objects.all()
    }
    return render(request=request, template_name='CCTV/index.html', context=context)
