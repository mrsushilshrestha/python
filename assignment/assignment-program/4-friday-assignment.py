
# Write a Python program that takes a positive integer as input and calculates the sum of its digits.
# Example Input: 1234
# Example Output: Sum of digits = 10

number =int(input("Enter the Positive number: "))
total =0

while number>0:
    break_number = number%10
    total+=break_number
    # number=number/10 #it return the float value also like  332.3222
    number=number//10

print(total)