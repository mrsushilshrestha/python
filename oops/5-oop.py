class Dog:
    # Constructor to initialize dog's attributes
    def __init__(self, name, age, breed, weight):
        self.name = name       # Dog's name
        self.age = age         # Dog's age
        self.breed = breed     # Dog's breed
        self.weight = weight   # Dog's weight
        print(f"Dog Details: Name: {name}, Age: {age}, Breed: {breed}, Weight: {weight}kg")
    
    # Method to calculate food based on dog's weight
    def calculate_food(self):
        # Recommended food amounts based on weight
        if self.weight <= 5:
            print("Food is 100gm per meal")
        elif self.weight <= 10:
            print("Food is 200gm per meal")
        elif self.weight <= 20:
            print("Food is 400gm per meal")
        elif self.weight <= 30:
            print("Food is 600gm per meal")
        else:
            print("Food is 800gm per meal")  # For dogs heavier than 30kg
        
# Creating an object of the Dog class
dog = Dog("Buddy", 4, "Golden Retriever", 15)  # Example dog with 15kg weight
dog.calculate_food()  # Calling the method to calculate the food portion based on the dog's weight
