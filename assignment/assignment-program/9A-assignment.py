# Write a program that takes a number n as input and prints the square of all numbers from 1 to n.
# Example Input: n = 4
# Example Output: 1^2 = 1, 2^2 = 4, 3^2 = 9, 4^2 = 16

number= int(input("Enter the number to find the Square : "))

for i in range(1,number+1):
    print(f"The sum of {i} is =",i**2)