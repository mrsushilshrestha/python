from abc import ABC,abstractmethod

class Fuel(ABC):
    @abstractmethod
    def get_fuel(self):
        pass
    
    def refuel(self):
        print("I am Refueling")
        
class MissionTitan(Fuel):
    def get_fuel(self):
        print("50% remaining")
        
    def launch(self):
        print("Launching mission titan")
        

obj= MissionTitan()
obj.get_fuel()
obj.launch()
        