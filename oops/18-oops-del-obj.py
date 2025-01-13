class Student:
    def __init__(self,name):
        self.name=name
    


s1=Student("sushil")
print(s1.name)

# after using del
del s1  #delete object
print(s1.name)

