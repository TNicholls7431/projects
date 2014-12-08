def getusername():
    check = False
    while check == False:
        name = input('what is your name: ')
        correct = input ('your name is {0}, is this correct: '.format(name))
        if correct.lower() == 'y':
            check = True
    
    
