#this file contains all of the functions required for guess who game

#gets a picture of the user
import picamera, time

def getuserimage(name):
    try:
        with picamera.PiCamera() as camera:
            check = False
            while check == False:
                 camera.start_preview()
                 time.sleep(1)
                 filename = '{0}.jpg'. format(name)
                 camera.capture(filename)
                 camera.stop_preview()
                 if input('are you happy y/n :').upper() =='Y':
                           check = True
    except picamera.exc.PiCameraMMALError:
         print('camera not detected, please connect your camera and restart the program')
         filename = ''

    return filename

def getcharprofile():
     name = input('what si your name? :')
     hair = ''
     while not(hair in['blonde','brown','ginger','black','grey']):
         hair = input('what is your hair color? :')

    



 
     
     
 
