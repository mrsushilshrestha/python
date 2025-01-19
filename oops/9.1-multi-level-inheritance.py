#multilevel-Inheritance

# Car
#  |
#  ├── ToyotaCar
#       |
#       └── Furtuner


# -----------------------Example------------------------------------------------------------------------------------

class Car:
    # def __init__(self):
    #     pass

    @staticmethod
    def start():
        print("car Run....")
    
    @staticmethod
    def stop():
        print("Car Stop.")
        
class ToyotaCar(Car):
    def __init__(self,brand):
        self.brand=brand

class Furtuner(ToyotaCar):
    def __init__(self, type,brand):
        super().__init__(brand)
        self.type=type


obj1= Furtuner("diseal","toyota")
obj1.start()



# ---------------------Advanced Version------------------------------------------------------------------------------

class Car:
    def __init__(self, brands):
        self.brands = brands  # Encapsulated attribute

    def brand(self):
        return self.brands

    @staticmethod
    def start():
        print("Car Run....")
    
    @staticmethod
    def stop():
        print("Car Stop.")

class ToyotaCar(Car):
    def __init__(self, brand, model):
        super().__init__(brand)  # Initialize parent class with brand
        self.model = model

    def display_info(self):
        return f"Brand: {self.brand}, Model: {self.model}"

class Furtuner(ToyotaCar):
    def __init__(self, brand, model, fuel_type):
        super().__init__(brand, model)  # Initialize ToyotaCar with brand and model
        self.fuel_type = fuel_type

    def display_info(self):
        # Extend the display info from parent class
        base_info = super().display_info()
        return f"{base_info}, Fuel Type: {self.fuel_type}"


# Create an object of Furtuner
obj1 = Furtuner("Toyota", "Furtuner", "Diesel")

# Access and display information
print(obj1.display_info())
obj1.start()
obj1.stop()


# -------------------------------------------------------------------------------------------------------------------------