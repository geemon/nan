#a pool with user najme and choice

users =[]
feedback = {}
session = True
while session:
   user_name = input('Provide your name : ')
   #gender =  input('provide your gender below. please use "m" for male and "f" for female: '
   country =  input('provide the country you would like to visit: ')

   #store user feedback into dictionary
   feedback[user_name]= country
   users.append(feedback)

   repeat = input('would you like to take the game again? '"y/n: ")
   if repeat != 'y':
    session = False 
#display result in dictionary
for user_choice in users:
    print(user_choice)
    #print(f"{user_name.title()} will like to travel to {country.title()}")  

