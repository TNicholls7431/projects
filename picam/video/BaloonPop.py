import picamera, RPi.GPIO as GPIO, time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
button = 14
balloon = 2

GPIO.setup(button, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(balloon, GPIO.OUT)
print('Ready...')
GPIO.wait_for_edge(button, GPIO.FALLING)
with picamera.PiCamera() as camera:
    camera.start_preview()
    camera.framerate = 90
    camera.resolution = (640, 480)
    camera.start_recording('my_video.h264')
    camera.wait_recording(60)
    camera.stop_recording()
GPIO.output(balloon, True)
time.sleep(5)
GPIO.output(balloon, False)
print('pop')
