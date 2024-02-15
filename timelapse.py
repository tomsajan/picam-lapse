from picamera2 import Picamera2
from libcamera import controls
from time import sleep


FOCUS = 0.2
PATH = '/var/www/html/images/script.jpg'

with Picamera2() as picam2:
    config = picam2.create_still_configuration(main={'size': picam2.sensor_resolution})
    picam2.configure(config)
    
    picam2.set_controls({"AfMode": controls.AfModeEnum.Manual, "LensPosition": FOCUS})
    picam2.start()
    picam2.capture_file(PATH)
    picam2.stop()
# picam2.close()