# create student class that take name & marks of 3 subject as arguments in constructor . 
# Then create a method to print the average

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def average_calculation(self):
        self.sum = 0
        for items in self.marks:
            self.sum += items
        self.average_marks = self.sum / 3  # This assumes exactly 3 subjects
    
    def data_store(self):  #to save the Executing data
        self.average_calculation()
        with open("oops/4.1-practice.txt","a+") as file:   
            file.write(f"Name is {self.name} and average marks are {self.average_marks:.2f}\n")
        
    def display(self):
        self.average_calculation()  # Call this method before displaying
        print(f"Name is {self.name} and average marks are {self.average_marks:.2f}")  # Format average to 2 decimal places

name = input("Enter the Name: ")
marks = []
for i in range(3):    
    number = int(input(f"Enter marks for subject {i + 1}: "))  # Clearer prompt
    marks.append(number)

std = Student(name, marks)
std.data_store() #to store the data in file
std.display()
