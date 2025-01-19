#define a Circle Class to create a circle with radius r using the constructor.
#define an Area() method of class which calculates the area of circle
#define a perimeter() method of the class which allows you to calculate the perimeter of the circle
import math

class Circles:
    # Constructor to initialize the radius of the circle
    def __init__(self, r):
        self.r = r  # Set the radius
    
    # Method to calculate the area of the circle
    def area(self):
        return f"{math.pi * (self.r ** 2):.4f}"  # Area formula: πr²
    
    # Method to calculate the perimeter (circumference) of the circle
    def perimeter(self):
        return f"{(2 * math.pi * self.r):.4f}"  # Perimeter formula: 2πr

# Main function
def main():
    circleObj = Circles(2)  # Create a circle with radius 2
    print(f"The Area Of Circle is: {circleObj.area()}")  # Display area
    print(f"The Perimeter Of Circle is: {circleObj.perimeter()}")  # Display perimeter

main()  # Run the main function
