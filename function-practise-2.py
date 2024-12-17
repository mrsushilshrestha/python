#Making Calculator using functions

def add(number_first,number_second):
    print(number_first+number_second)

def sub(number_first,number_second):
    print(number_first-number_second)
    
def mul(number_first,number_second):
    print(number_first*number_second)

def div(number_first ,number_second):
    if number_second>0:
        print(number_first/number_second)
    else:
        print("Number NOT Divided By Zero")


first_number =int(input("Enter the first Number: "))
operator =input("Enter the Operator[+,-,*,/]: ")
second_number =int(input("Enter the Second Number: "))

if operator=='+':
    add(first_number,second_number)
elif operator=='-':
    sub(first_number,second_number)
elif operator=='*':
    mul(first_number,second_number)
elif operator=='/':
    div(first_number,second_number)
else:
    print("INVALID!!!")