#this file contains all of the functions required for guess who game

#gets a picture of the user
import picamera, time, json

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
    name = input('what is your name? :')
    getuserimage(name)
    hair =''
    while not(hair in['blonde','brown','ginger','black','grey']):
        hair = input('what is your hair color? :')
    eye =''
    while not(eye in['brown','blue','grey','green']):
        eye = input('what color are your eyes? :')
    facial =''
    while not(facial in['Y','N']):
        facial = input('do you have any facial hair? :').upper()
    glasses =''
    while not(glasses in['Y','N']):
        glasses = input('are you wearing glasses? :').upper()
    hat =''
    while not(hat in['Y','N']):
        hat = input('are you wearing a hat? :').upper()
    return [hair,name,eye,facial,glasses,hat]

def load():
    try:
        with open('chardata',mode='r')as file:
            people = json.load(file)

    except IOError:
        print('failed: no data found')
        people = []
    return people
people = load()

def store():
    person = getcharprofile()
    people.append(person)
    with open('chardata',mode='w') as file:
        json.dump(people, file)

              
        
    



 
     
     
 
