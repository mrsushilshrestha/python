# Syntax:
class ClassName:
    def __init__(self, parameters):
        # Initialize attributes
        self.attribute = value

#Example:
class Person:
    def __init__(self, name, age):
        self.name = name  # Initializing the 'name' attribute
        self.age = age    # Initializing the 'age' attribute
    
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Creating an object
person1 = Person("Sushil", 20)

# Accessing attributes and methods
person1.display_info()  # Output: Name: Sushil, Age: 25

