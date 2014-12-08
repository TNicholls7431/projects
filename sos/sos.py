#this part of the code tells python what packages to use and it configures the gpio pins
import RPi.GPIO as gp, time
gp.setmode(gp.BOARD)
gp.setup(11,gp.OUT)
#this part defines what dot is so that whenever you want to flash the led all you have to do is input dot()
def dot():
    gp.output(11,gp.HIGH)
    time.sleep(0.5)
    gp.output(11,gp.LOW)
    time.sleep(0.25)

#this area is the same as dot but the time inbetween turning of the led is longer
def dash():
    gp.output(11,gp.HIGH)
    time.sleep(0.75)
    gp.output(11,gp.LOW)
    time.sleep(0.25)

#this code tells python to determine whatletter has been inputed and the sequense of dots and dashes it needs to preform
def morseletter(letter):
    if letter == 'A':
        dot()
        dash()
    elif letter == 'B':
        dash()
        dot()
        dot()
        dot()
    elif letter == 'C':
        dash()
        dot()
        dash()
        dot()
    elif letter == 'D':
        dash()
        dot()
        dot()
    elif letter == 'E':
        dot()
    elif letter == 'F':
        dot()
        dot()
        dash()
        dot()
    elif letter == 'G':
        dash()
        dash()
        dot()
    elif letter == 'H':
        dot()
        dot()
        dot()
        dot()
    elif letter == 'I':
        dot()
        dot()
    elif letter == 'J':
        dot()
        dash()
        dash()
        dash()
    elif letter == 'K':
        dash()
        dot()
        dash()
    elif letter == 'L':
        dot()
        dash()
        dot()
        dot()
    elif letter == 'M':
        dash()
        dash()
    elif letter == 'N':
        dash()
        dot()
    elif letter == 'O':
        dash()
        dash()
        dash()
    elif letter == 'P':
        dot()
        dash()
        dash()
        dot()
    elif letter == 'Q':
        dash()
        dash()
        dot()
        dash()
    elif letter == 'R':
        dot()
        dash()
        dot()
    elif letter == 'S':
        dot()
        dot()
        dot()
    elif letter == 'T':
        dash()
    elif letter == 'U':
        dot()
        dot()
        dash()
    elif letter == 'V':
        dot()
        dot()
        dot()
        dash()
    elif letter == 'W':
        dot()
        dash()
        dash()
    elif letter == 'X':
        dash()
        dot()
        dot()
        dash()
    elif letter == 'Y':
        dash()
        dot()
        dash()
        dash()
    elif letter == 'Z':
        dash()
        dash()
        dot()
        dot()

#this piece of code asks the use what letter they want to translate
msg = input('what message do you want to translate? :')
for each in msg:
    morseletter(each)
        
    


 
