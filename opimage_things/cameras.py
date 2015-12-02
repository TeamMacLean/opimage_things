'''simple methods for running a camera'''

import picamera

def take_picture(fname='pic.jpg', hflip=False, vflip=True)
    cam = picamera.PiCamera()
    cam.hflip=hflip
    cam.vflip=vflip
    cam.capture(fname)
