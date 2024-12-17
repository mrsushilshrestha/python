#WAP to find the Greatest of Three from the give user inputs
print("Enter the 3 Numbers:")
num1 = int(input()) #for first numbers
num2 = int(input())  #for second number
num3 = int(input())  #for third number


if(num1>num2 and num1>num3):
    print(f"Number first {num1} is greatest")
elif(num2>num3):
    print(f"Number second {num2} is greatest")
else:
    print(f"Number Third {num3} is greatest")