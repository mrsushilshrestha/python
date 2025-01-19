class Person:
    name="anonomouse"

    def changeName(self,name):
        self.name= name
    

obj =Person()
obj.changeName("sushil")
print(obj.name)
print(Person.name)

# -------------------------------------------------------------------
# how to change the class object
class Person:
    name="anonomouse"

    def changeName(self,name):
        Person.name= name    

obj =Person()
obj.changeName("sushil")
print(obj.name)
print(Person.name)

#-------------------------------------------------------------------------------------
#using the Class method

class Person:
    name="anonomouse"

    def changeName(self,name):
        self.__class__.name= name    

obj =Person()
obj.changeName("sushil")
print(obj.name)
print(Person.name)

#-----------------------------------------------------------------------
#using the class decorator

class Person:
    name="anonomouse"

    @classmethod  #decorator
    def changeName(cls,name):
        cls.name= name
    
obj =Person()
obj.changeName("sushil")
print(obj.name)
print(Person.name)




