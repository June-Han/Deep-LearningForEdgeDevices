import time
import picamera

with picamera.PiCamera() as camera:
    camera.resolution = (1280, 720)
    camera.framerate = 90
    camera.start_preview()
    # Wait for the automatic gain control to settle
    time.sleep(2)
    # Now fix the values
    camera.shutter_speed = camera.exposure_speed
    camera.exposure_mode = 'off'
    g = camera.awb_gains
    camera.awb_mode = 'off'
    camera.awb_gains = g
    camera.vflip = False
    # Finally, take several photos with the fixed settings
    camera.capture_sequence(['wet_syringe_%02d.jpg' % i for i in range(50, 100)])