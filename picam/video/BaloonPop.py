import picamera, RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
button = 14

GPIO.setup(button, GPIO.IN, GPIO.PUD_UP)
print('Ready...')
GPIO.wait_for_edge(button, GPIO.FALLING)
print('Pop!')

with picamera.PiCamera() as camera:
    camera.start_preview()
    camera.framerate = 90
    camera.resolution = (640, 480)
    camera.start_recording('my_video.h264')
    camera.wait_recording(60)
    camera.stop_recording()
