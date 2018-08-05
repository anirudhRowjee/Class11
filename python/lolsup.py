print "Hello World"
while True:
    quit = 'q'
    answer = raw_input('press 1 or 2')
    if answer == 1:
        print "you pressed 1"
    if answer == 2:
        print "you pressed 2"
    if answer == quit:
        print "okay, bye"
        break
    else :
        print "please enter a proper value"
        
