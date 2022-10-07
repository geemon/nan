# create a class with an inheritance
class Human_head:
 
 #create init method
    def __init__(self,eye,nose,mouth) :
    #initialise method
        self.eye = eye
        self.nose = nose
        self.mouth = mouth 
    def define_me(self):
        my_self = f"{self.eye} eyes {self.nose} nose {self.mouth} mouth"
        return my_self
#create an object and assign to class
_appearance_ = Human_head('big', 'medium', 'small')
print(f'hello, am ben and below is how my face is to the human eye')
print(_appearance_.define_me())  

#now create an inheritance with an object
class Baby(Human_head):
    def __init__(self, eye, nose, mouth):
        super().__init__(eye, nose, mouth)
        """add new attributes to the inherit object"""
        self.months =6
    """create a new method to call"""
    def growth(self):
        print(f'then baby is only {self.months} months of age')
    
#creat an instance or object
new_born = Baby('small', 'tiny', 'cute')
print('The appearnce of baby head to the human eye')
print(new_born.define_me())
new_born.growth()