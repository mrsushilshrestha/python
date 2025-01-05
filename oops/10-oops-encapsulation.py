# class Bankaccount:
#     def __init__(self):
#         self.__balance=100 #private modifier __balance
#         self._private_balance =200
#         self.public_balance =150
    
#     def get_amount(self):
#         return self.__balance
  
# obj = Bankaccount()
# print(obj.get_amount())
# print(obj._private_balance)
# print(obj.public_balance)

#-----------note----------

# public 
# public variable and class can be access outside of the classes functions


# protected
# protected variable or class can be access outside of the classes and function but
# more secure than public it indicate or declare by single underscore _protected
# eg:-
# _first_number =30
# _second_number =20
# sum = _first_number + _second_number

# private
# private variable or class can be access only in the same class or function not outside of the function so that it is more secure than other access modifier.
#It can be declare by using the double underscore __
#eg:-
# __first_number =20
# __ second_number =30
# sum=__first_number+__second_number


#make calculation using the Public protected and Private access modifier
class Calculation:
    def __init__(self):
        self.__first_number =20  #private variable
        self.__second_number =30 #private variable
        self.sum= self.__first_number+self.__second_number #add two number in public variable
        self.add =self.__first_number+self.__second_number
        
    def display(self):
        print(f"The sum of Two Number {self.__first_number} and {self.__second_number} is: {self.sum}")

calculation_obj =Calculation()
# print(calculation_obj.sum) #we can assess result directly
#print(calculation_obj.add) #we can assess result directly
calculation_obj.display()


