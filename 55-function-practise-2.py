#WAF for Calculator , Feature addition Subtraction, Multiplication, Division
def add(number_first,number_second): #addition function
    print(number_first+number_second)

def sub(number_first,number_second): #subtraction function
    print(number_first-number_second)
    
def mul(number_first,number_second):  #multiplication function
    print(number_first*number_second)

def div(number_first ,number_second): #division function
    if number_second>0:
        print(number_first/number_second)
    else:
        print("Number NOT Divided By Zero")


message ="""
Enter the Option What you want!!!!
1>ADDITION
2>SUBTRACTION
3>MULTIPLICATION
4>DIVISION
"""
print(message)
operator =input("Enter the Operator or Options[+,-,*,/]: ")
first_number =int(input("Enter the first Number: "))
second_number =int(input("Enter the Second Number: "))

if operator=='+' or 1:
    add(first_number,second_number)
elif operator=='-' or 2:
    sub(first_number,second_number)
elif operator=='*' or 3:
    mul(first_number,second_number)
elif operator=='/' or 4:
    div(first_number,second_number)
else:
    print("INVALID!!!")
    

