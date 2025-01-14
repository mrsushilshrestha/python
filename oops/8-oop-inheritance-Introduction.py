# Day 35: Introduction to Inheritance in Python
"""
Inheritance is a way to enable a new class (called a derived class) to inherit the properties and methods of an existing class (called a base class).

Benefits of Inheritance:
1. Code Reusability
2. Readable and maintainable code
3. Extensibility
"""

# Example 1: Basic Inheritance Example
class BaseClass:
    def __init__(self):
        self.base_attribute = "I am from the BaseClass"
    
    def base_method(self):
        return "Base method called!"

class DerivedClass(BaseClass):
    def __init__(self):
        super().__init__()
        self.derived_attribute = "I am from DerivedClass"
    
    def derived_method(self):
        return "Derived method called!"

# Creating an object of DerivedClass
obj = DerivedClass()
print(obj.base_attribute)   # I am from the BaseClass
print(obj.base_method())    # Base method called!
print(obj.derived_attribute)  # I am from DerivedClass
print(obj.derived_method())  # Derived method called!

# Example 2: Inheritance with Overridden Method
class Animal:
    def __init__(self, name):
        self.name = name
    
    def sound(self):
        return "Animal sound"

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
    
    # Overriding the sound method
    def sound(self):
        return "Bark"

dog = Dog("Buddy")
print(dog.name)  # Buddy
print(dog.sound())  # Bark


# Day 36: Inheritance Types
"""
Inheritance types define the relationship between classes. The major types are:
1. Single Inheritance
2. Multiple Inheritance
3. Multilevel Inheritance
4. Hierarchical Inheritance
5. Hybrid Inheritance
"""

# Example 1: Single Inheritance
class Parent:
    def greet(self):
        return "Hello from Parent!"

class Child(Parent):
    pass

child = Child()
print(child.greet())  # Hello from Parent!

# Example 2: Multiple Inheritance
class Father:
    def father_method(self):
        return "Father's method"

class Mother:
    def mother_method(self):
        return "Mother's method"

class Child(Father, Mother):
    def child_method(self):
        return "Child's method"

child = Child()
print(child.father_method())  # Father's method
print(child.mother_method())  # Mother's method
print(child.child_method())   # Child's method


# Day 37: Method Overriding and Super
"""
Method overriding is the concept where a method in the child class has the same name as a method in the parent class.
The child class method overrides the parent class method.
"""

# Example 1: Method Overriding
class Animal:
    def speak(self):
        return "Animal speaks"

class Dog(Animal):
    def speak(self):
        return "Bark"

dog = Dog()
print(dog.speak())  # Bark

# Example 2: Using super() to call parent class method
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return f"{self.name} makes a sound"

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
    
    def speak(self):
        return f"{self.name} the {self.breed} barks"

dog = Dog("Buddy", "Golden Retriever")
print(dog.speak())  # Buddy the Golden Retriever barks


# Day 38: Polymorphism in Python
"""
Polymorphism allows objects of different classes to be treated as objects of a common super class.
It is usually achieved through method overriding or operator overloading.
"""

# Example 1: Polymorphism with Method Overriding
class Animal:
    def sound(self):
        return "Some animal sound"

class Dog(Animal):
    def sound(self):
        return "Bark"

class Cat(Animal):
    def sound(self):
        return "Meow"

# Function demonstrating polymorphism
def make_sound(animal):
    print(animal.sound())

dog = Dog()
cat = Cat()

make_sound(dog)  # Bark
make_sound(cat)  # Meow

# Example 2: Polymorphism with Same Method Name in Different Classes
class Car:
    def type_of_vehicle(self):
        return "This is a Car."

class Bike:
    def type_of_vehicle(self):
        return "This is a Bike."

# Function demonstrating polymorphism
def vehicle_info(vehicle):
    print(vehicle.type_of_vehicle())

car = Car()
bike = Bike()

vehicle_info(car)  # This is a Car.
vehicle_info(bike)  # This is a Bike.


# Day 39: Encapsulation in Python
"""
Encapsulation is the concept of restricting access to some of an object's components. It is often used to hide the internal state of an object.
"""

# Example 1: Using Encapsulation to Restrict Access
class Car:
    def __init__(self, brand, model):
        self.__brand = brand  # Private attribute
        self.__model = model  # Private attribute
    
    def get_brand(self):
        return self.__brand
    
    def set_brand(self, brand):
        self.__brand = brand

car = Car("Tesla", "Model X")
print(car.get_brand())  # Tesla
car.set_brand("BMW")
print(car.get_brand())  # BMW

# Example 2: Private Attribute in Encapsulation
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
    
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
    
    def get_balance(self):
        return self.__balance

account = BankAccount(1000)
account.deposit(500)
print(account.get_balance())  # 1500
account.withdraw(200)
print(account.get_balance())  # 1300


# Day 40: Access Modifiers in Python
"""
Access Modifiers control the visibility of class attributes and methods. The main types of access modifiers are:
1. Public: Can be accessed from anywhere.
2. Protected: Can be accessed within the class and its subclasses.
3. Private: Can only be accessed within the class.
"""

# Example 1: Public Access Modifier
class Person:
    def __init__(self, name):
        self.name = name  # Public attribute
    
    def greet(self):
        return f"Hello, {self.name}!"

person = Person("Alice")
print(person.name)  # Alice
print(person.greet())  # Hello, Alice!

# Example 2: Private Access Modifier
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
    
    def get_balance(self):
        return self.__balance

account = BankAccount(500)
# print(account.__balance)  # AttributeError: 'BankAccount' object has no attribute '__balance'
print(account.get_balance())  # 500
