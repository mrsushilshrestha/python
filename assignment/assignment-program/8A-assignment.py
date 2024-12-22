#WAP to find the fibbonaci series from user input
a=0
b=1
number =int(input("Enter the number to find the fibonacci series... "))
for i in range(number):
    c=a+b
    a=b
    b=c
    print(c,end=" ")

print()

#WAP to find the factorial of the number which is enter by the users
fact=1
number = int(input("Enter the number to find the factorial..."))
for i in range(1,number+1):
    fact=fact*i  
    
print(fact)

#factorial using the recursion
def factorial(num):
    if num==0:
        return 1
    elif num==1:
        return 1
    else:
        return num*factorial(num-1)

print("factorialof the number using recursion",factorial(5))