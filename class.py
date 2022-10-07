# a simple program to demonstrate program with class and a method
class Dog:
    #create a method within the dog class
    def __init__(self, name, age ):
    #initialise the method
     self.name = name
     self.age = age

    #create methods
    def sit(self):
        """function to be carried out by dog when given a command"""
        print(f'{self.name} is siting')
    
    def roll_over(self):
        """function to be carried out by dog when given a command"""
        print(f'{self.name} is rolling over')
#create an instance 
my_dog = Dog('denis',6)
print(f'the name of my dog is {my_dog.name}')
print(f'my dog age is {my_dog.age}')
my_dog.sit()
my_dog.roll_over()