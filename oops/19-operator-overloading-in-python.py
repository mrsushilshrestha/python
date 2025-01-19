# # #valid operator additon
# # print("apna"+"college") #apnacollege
# # print(2+4)             #6
# # print([1,2,3,4]+[2,3,4,5,6]) #merge #[1, 2, 3, 4, 2, 3, 4, 5, 6]

# class Complex:

#     def __init__(self,real,imaginary):
#         self.real=real
#         self.imaginary=imaginary

    
#     def show(self):
#         print(self.real,"i +",self.imaginary,"j")

#     def add(self,num2):
#         newReal=self.real+num2.real
#         newImaginary=self.imaginary+num2.imaginary

#         return Complex(newReal,newImaginary)
    

# number1=Complex(1,2)
# number1.show()

# number2=Complex(3,2)
# number2.show()

# num3=number1.add(number2)
# num3.show()

#---------------using-dunder-function----------------------
# #valid operator additon
# print("apna"+"college") #apnacollege
# print(2+4)             #6
# print([1,2,3,4]+[2,3,4,5,6]) #merge #[1, 2, 3, 4, 2, 3, 4, 5, 6]

class Complex:

    def __init__(self,real,imaginary):
        self.real=real
        self.imaginary=imaginary

    
    def show(self):
        print(self.real,"i +",self.imaginary,"j")

    def __add__(self,num2):
        newReal=self.real+num2.real
        newImaginary=self.imaginary+num2.imaginary

        return Complex(newReal,newImaginary)
    

number1=Complex(1,2)
number1.show()

number2=Complex(3,2)
number2.show()

number3=number1+number2
number3.show()



# object.__add__(self, other)
# object.__sub__(self, other)
# object.__mul__(self, other)
# object.__matmul__(self, other)
# object.__truediv__(self, other)
# object.__floordiv__(self, other)
# object.__mod__(self, other)
# object.__divmod__(self, other)
# object.__pow__(self, other[, modulo])
# object.__lshift__(self, other)
# object.__rshift__(self, other)
# object.__and__(self, other)
# object.__xor__(self, other)
# object.__or__(self, other)¶