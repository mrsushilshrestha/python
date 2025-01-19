#define a Employee class with attribute role,department &salary.
#this class also have a showDetails() method.

#create an Engineer Class That inbherits properties from Employee & has additional attributes:name,age.

class Employee:
    def __init__(self,role,department,salary):
        self.role=role
        self.department =department
        self.salary =salary
        
    # def showDetail(self):
    #     print(f"The Employee Role: {self.role} , Employee department: {self.department} , Employee Salary: {self.salary}")
    

class Engineer(Employee):
    def __init__(self, name,age=20,role="senior Developer", department='IT', salary=10000):
        super().__init__(role, department, salary)
        self.name=name
        self.age=age
    
    def showDetail(self):
        print(f"The Name is: {self.name} , Age is: {self.age} ,Employee Role: {self.role} , Employee department: {self.department} , Employee Salary: {self.salary}")


engineerObj =Engineer(name="sushil Shrestha")
engineerObj2 =Engineer("sushil Shrestha",20,"Senior",'IT',2000000)


engineerObj.showDetail()
engineerObj2.showDetail()

