'''simple methods for running a camera'''

import picamera

def take_picture(fname='pic.jpg', hflip=False, vflip=True, width=600, height=480, fmt="jpeg",shutter_speed=100000):
    with picamera.PiCamera() as cam:
        cam.hflip=hflip
        cam.vflip=vflip
        cam.resolution = (width,height)
        cam.shutter_speed = shutter_speed
        if fmt == 'rgb':
	    cam.capture(fname, 'rgb')
        else:
    	    cam.capture(fname, fmt)
