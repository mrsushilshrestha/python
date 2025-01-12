#Hiding the implementation details of a class and only showing the essential features to the user.

class Car:
    def __init__(self):
        self.cluch=False
        self.bre =True
        self.accle =False
    
    def start(self):
        self.cluch=True
        self.bre=False
        self.accle=True
        print("Car is Running...")

        
obj = Car()
obj.start()