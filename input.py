#a program to let users to choose when to quit
option =""
while option != 'q':
    option = input("please type something and i will print for you. input 'q' to quit\n")
    print(f"{option}")   
    ans =input('do you want to run me again? "y/n')
    if ans != 'y':
        break        
    else:
        continue