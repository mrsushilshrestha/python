import math

class Calculator:
    def __init__(self,option, length=1, breadth=1, radius=1):
        self.option =option
        self.length = length
        self.breadth = breadth
        self.radius = radius
        
    def operations(self):
        if self.option ==1:
            return self.length * self.breadth

        elif self.option ==2:
            return math.pi * (self.radius ** 2)
        
        elif self.option ==3:
            return length**2
        
        else:
            print("Invalid Options")


message ="""
Select the Option[1,2,3] to perform Calculation:
1.Rectangle
2.Circle
3.Square
"""
# Taking input from the user
option =int(input(message))
length = int(input("Enter the length: "))
breadth = int(input("Enter the breadth: "))
radius = int(input("Enter the radius: "))

# Creating an object of the Calculator class
obj1 = Calculator(option,length, breadth, radius)

result=obj1.operations()
print("The Result is",result)
