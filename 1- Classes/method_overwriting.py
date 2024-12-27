#Method Overwiting!!!

class Animal:
    def __init__(self, name):
        
        self.name = name 
    
    def make_sound(self):
        print( "some sound")

class Dog(Animal):
    
    def __init__(self, name):
        super(Dog,self).__init__(name)
    
    def make_sound(self):
        print( "bark!")
    
A1 = Dog("Zeus")
print(A1.name)
print(A1.make_sound())