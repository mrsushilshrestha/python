class Cat:
    def __init__(self,name,age,color,weight):
        self.name = name
        self.age = age
        self.color =color
        self.weight = weight
        print(name ,age ,color ,weight)
        
    def calculation(self):
        if self.weight==1:
            print("Food is 10gm")            
        elif self.weight==2:
            print("Food is 100gm")
        elif self.weight==5:
            print("Food is 1kg")
        else:
            print("Invalid Options")
     
     
     
    
obj = Cat("Pinky",10,"weight",1)
obj.calculation()

    