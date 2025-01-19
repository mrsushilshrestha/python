# 5. Polymorphism with Shapes
# Create a parent class Shape with a method area(). Create two child classes Rectangle and Circle.
# In Rectangle, override the area() method to calculate and return the area of a rectangle (length × breadth).
# In Circle, override the area() method to calculate and return the area of a circle (π × radius²).
# Write a program to create objects of both Rectangle and Circle, and display their areas.

import math

# Parent
class Shape:
    def area(self):
        pass 

class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

# Create Rectangle object
length = int(input("Enter the length of the rectangle: "))
breadth = int(input("Enter the breadth of the rectangle: "))
rectangle = Rectangle(length, breadth)
print(f"The area of the rectangle is: {rectangle.area()}")

# Create Circle object
radius = int(input("\nEnter the radius of the circle: "))
circle = Circle(radius)
print(f"The area of the circle is: {circle.area():.2f}")
