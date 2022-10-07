run = True
while run:
    mesg = input("input a test and it will be printed for you. input 'q' to quit the programm")
    if mesg == 'q':
        run = False
    else:
        print(mesg)