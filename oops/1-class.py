# 1. What is a Class?
# A class is a blueprint or template for creating objects. 
# It defines the properties (attributes) and behaviors (methods) that the objects of the class will have.

# Class representing a person
class Person:
    country = "Nepal"
    gender = "Male"  # Fixed typo from "make" to "male"

# Class representing an animal
class Animal:
    family = "Dog"

# Creating instances of the classes
p1 = Person()
ani = Animal()

# Printing attributes of the Person instance
print("Person's country:", p1.country)
print("Person's gender:", p1.gender)

# Printing attributes of the Animal instance
print("Animal's family:", ani.family)
