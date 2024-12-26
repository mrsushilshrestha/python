import math

class Calculator:
    def __init__(self,option):
        self.option =option
        
    def operations(self):
        if self.option ==1: # or "Rectangle" or "rectangle": #For Rectangle
            self.option= "Rectangle" 
            length =int(input("Enter the Length: "))
            breadth =int(input("Enter the Breadth: "))
            return self.rectangle(length,breadth)

        elif self.option ==2: # or "Circle" or "circle": #For Circle
            self.option= "Circle"
            radius =int(input("Enter the Radius of Circle: "))
            return self.circle(radius)
        
        elif self.option ==3: # or "Square" or "square": #For Square
            self.option= "Square"
            length=int(input("Enter the lenght: "))
            return self.square(length)
        
        else:
            print("Invalid Options")
        
    def rectangle(self,length,breadth):  #Rectangle Area
        return length * breadth
    
    def circle(self,radius):    #Circle Area
        return math.pi * radius ** 2
    
    def square(self,length): #Square Area
        return length**2


message ="""
Select the Option[1,2,3] to perform Calculation:
1.Rectangle
2.Circle
3.Square
"""

option = int(input(message))

# Creating an object of the Calculator class
obj1 = Calculator(option)

result=obj1.operations()
print(f"The Area of {obj1.option} is",result)
