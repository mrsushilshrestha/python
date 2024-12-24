class calculators:
    
    def __init__(self,length=1,breath=1,height=1,radious=1):
        self.length = length
        self.breath = breath
        self.height = height
        self.radious=radious
        
    
    def rectangle_area(self):
        return self.length*self.breath*self.height
    
    def circle_area(self):
        return self.radious**2

length =int(input("Enter the length :- "))
breath =int(input("Enter the breath :- "))
height =int(input("Enter the height :- "))
radious =int(input("Enter the radious :-"))


obj1 = calculators(length,breath,height,radious)

area_rectnage =obj1.rectangle_area()
print("Are of rectange is:",area_rectnage)

area_circle =obj1.circle_area()
print("Are of Circle is:",area_circle)