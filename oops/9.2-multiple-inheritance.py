#    multiple-Inheritance

    #   Vehicle      Machine
    #      |            |
    #      └───> HybridCar

#------------Example------------------------------------------------------------
class Vehicle:
    def has_wheels(self):
        return "This vehicle has wheels."

class Machine:
    def has_engine(self):
        return "This machine has an engine."

class HybridCar(Vehicle, Machine):
    def description(self):
        return "I am a hybrid car that combines the features of a vehicle and a machine."

# Creating an object of HybridCar
hybrid = HybridCar()

# Accessing methods from both parent classes
print(hybrid.has_wheels())  # From Vehicle
print(hybrid.has_engine())  # From Machine
print(hybrid.description()) # From HybridCar


#--------------example-2---------------------------------------------------
class Vehicle:
    def __init__(self, wheels):
        self.wheels = wheels

    def has_wheels(self):
        return f"This vehicle has {self.wheels} wheels."

class Machine:
    def __init__(self, engine_type):
        self.engine_type = engine_type

    def has_engine(self):
        return f"This machine has a {self.engine_type} engine."

class HybridCar(Vehicle, Machine):
    def __init__(self, wheels, engine_type, brand):
        # Initialize both parent classes
        Vehicle.__init__(self, wheels)
        Machine.__init__(self, engine_type)
        self.brand = brand

    def description(self):
        return (
            f"I am a {self.brand} hybrid car with {self.wheels} wheels and a {self.engine_type} engine."
        )

# Creating an object of HybridCar
hybrid = HybridCar(4, "electric", "Toyota")

# Access methods from both parent classes and child class
print(hybrid.has_wheels())  # From Vehicle
print(hybrid.has_engine())  # From Machine
print(hybrid.description()) # From HybridCar
