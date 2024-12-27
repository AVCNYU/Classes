#Classes!!!

"""
this is the template for how to make classes in python this is very basic 
just to show complete understanding of the concept 
"""



class Car:
    
    # CLASS VARIABLE 
    amount_cars = 0
    
    #  CONSTRUCTOR 
    def __init__(self, manufacturer, model, hp):
        # note: hp is horse power not health points 
        # note: "self.____" is a arbitrary value
        self.manufacturer = manufacturer
        self.model = model
        self.hp = hp
        Car.amount_cars += 1 
        # note: amount_cars does not belong to the individual object since its not addressed with self
    
    def print_info(self):
        # note: self is needed as a pramater 
        print("manufacturer: {}, model: {}, hp: {}".format(
            self.manufacturer,
            self.model,
            self.hp
        ))
        
    def print_car_amount(self):
        print( "Amount: {}".format(Car.amount_cars))
    
    # DESTRUCTOR 
    def __del__(self):
        Car.amount_cars -= 1

        
def main_test1():
    #Objects!!!
    myCar1 = Car("Tesla", "Model X", "525")
    myCar1.print_info()
    myCar1.print_car_amount()
    """
    print(myCar1.manufacturer)
    print(myCar1.model)
    print(myCar1.hp)

    """
        
def main_test2():
    myCar1 = Car("Tesla", "Model X", "525")
    myCar2 = Car("BMW", "X3", "200")
    myCar3 = Car("VW", "Golf", "100")
    myCar4 = Car("Porsche", "911", "520")
    
    del myCar3
    myCar1.print_car_amount()

#main_test1()

#main_test2()
    

# Hidden Attributes!!!
"""
two underlines before the attribute name, 
functionally makes that variable or method invisible outside the class
"""
class MyClass:
    def __init__(self):
        self.__hidden = "hello"
        print(self.__hidden) # works

m1 = MyClass()
print (m1.hidden) # doesnt work

    