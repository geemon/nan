from mimetypes import init


class Family_members:
    def __init__(self, name, age , childred):
        self.name =name
        self.age = age  
        self.childred =childred

    def describe_fam(self):
        print(f'{self.name} is my name and I am {self.age} years of  age ')
    
    def family_position(self):
        print(f'I have {self.childred} number of children')


relative = Family_members('Madalyn', 65 , 4)
relative.describe_fam()
relative.family_position()

#inheritance

class Children(Family_members):
    def  __init__(self, name, age, childred):
        super().__init__(name, age, childred)
        self.position = "first"

    def describe_child(self):
        print(f'{self.name} is my name. I am {self.age} years of age ')

    def describe_position(self):
        print(f'I am the {self.position} child of {relative.name} ')

child = Children('kwesi',35, 'second ')
child.describe_child()
child.describe_position()    