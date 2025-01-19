# Write a program to generate the Fibonacci sequence up to the nth term using a recursive function. 
# Input n from the user and print the sequence.

a=0
b=1
number =int(input("Enter the number to find the fibonacci series... "))
for i in range(number):
    c=a+b
    a=b
    b=c
    print(c,end=" ")

print()
    
    