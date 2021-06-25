import os
from datetime import datetime, date
from email.mime.image import MIMEImage

import cv2
import googlemaps as googlemaps
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

from CMS.settings.settings import MAPS_GEOCODING_KEY


class EmailHandler:
    def __init__(self, to, subject, message=None, cc=None, bcc=None, reply_to=None, files=None):
        self.subject = subject
        self.to = to
        self.cc = cc
        self.bcc = bcc
        self.reply_to = reply_to
        self.message = message
        self.files = files

        self.email = EmailMessage()
        self.email.to = [x.strip() for x in self.to.split(',')]
        self.email.subject = self.subject

        if self.message:
            self.email.body = self.message

        if self.files:
            for file in self.files:
                self.email.attach(file['name'], file['bytes'])

    # html: This method format the email message to html format.
    def html(self, template, context, header_logo=None):
        self.email.content_subtype = "html"
        self.email.mixed_subtype = 'related'
        self.email.body = render_to_string(template, context)

        if header_logo and os.path.exists(header_logo):  # Attach logo to mail
            fp = open(header_logo, 'rb')
            msg_header = MIMEImage(fp.read())
            fp.close()
            msg_header.add_header('Content-ID', '<{}>'.format("header.png"))
            self.email.attach(msg_header)

        return self

    # send: This method actually send the email on after response.
    def send(self, images=[]):
        if self.cc:
            self.email.cc = [x.strip() for x in self.cc.split(',')]

        if self.bcc:
            self.email.bcc = [x.strip() for x in self.bcc.split(',')]

        if self.reply_to:
            self.email.reply_to = [x.strip() for x in self.reply_to.split(',')]

            # attach images
            for path in images:
                fp = open(path, 'rb')
                msg_header = MIMEImage(fp.read())
                fp.close()
                msg_header.add_header('Content-ID', '<{}>'.format(os.path.split(path)[1]))
                self.email.attach(msg_header)

        return self.email.send(fail_silently=True)


class Google:
    map = googlemaps.Client(key=MAPS_GEOCODING_KEY)

    # This method fetches the geocode property of a given address.
    def geocode(self, address):
        return self.map.geocode(address)


class WhatsappHandler:
    print('to be coded')


class SMSHandler:
    print('to handle sms')


class SnapShot:
    cam = cv2.VideoCapture('rtsp://admin:adminpass1@192.168.1.108:554/cam/realmonitor?channel=1&subtype=0')
    while True:
        time = datetime.now().time()
        the_date = date.today().strftime('%B-%d-%Y')
        ret, frame = cam.read()
        if not ret:
            print("failed to grab frame")
            break
        cv2.imshow("test", frame)

        k = cv2.waitKey(1)
        img_name = f'{datetime.now().strftime("%d-%m-%Y")}.png'

        file = cv2.imwrite(f'{datetime.now().strftime("%B %d, %Y, %H-%M-%S")}.png', frame)
        print("{} written!".format(img_name))
        break

    cam.release()

    cv2.destroyAllWindows()