class Person:
    def __init__(self,gender):
        self.gender=gender
    
    def get_gender(self):
        print(f"I am {self.name}, i am {self.gender}")
        

class Student(Person):    
    def __init__(self,name,gender):
        self.name =name
        
        Person.__init__(self,gender) #invoking the parent class
        
    def study(self):
        print(f"My name is {self.name} and i am studying ")
    

# p= Person("Sushil") #crete a object of Person class
# p.get_gender()  #to access the element of get_gender()

std =Student("sushil","male")  #crete a object of Student Class Which i child class
std.study()     #access study method
std.get_gender()
