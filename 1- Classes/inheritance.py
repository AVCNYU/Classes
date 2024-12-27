#Inheritance!!!
class Person:
    def __init__(self, name, age ):
        self.name = name 
        self.age = age 
    
    def get_older(self, years):
        self.age += years
    
class Programmer(Person): 
        def __init__(self, name, age,lang):
            super(Programmer,self).__init__(name, age)
            self.language = lang 
        
        def print_language(self):
            return "Favorite Language: {}".format(self.language)


p1 = Programmer("Mike", 30, "Python")
print(p1.age)
print(p1.name)
print(p1.print_language())

p1.get_older(5)
print(p1.age)

