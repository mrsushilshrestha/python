# 1. Prime Numbers in a Range
# Write a program to input two numbers, start and end.
# Print all prime numbers between start and end (inclusive).
# Use a function is_prime(num) to check if a number is prime.

start = int(input("Enter the Start Number: "))
end = int(input("Enter the End Number: "))

# Function to check whether a number is prime or not
def is_prime(num):
    if num <= 1:
        return False
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1
    return count == 2  # prime numbers have exactly 2 divisors: 1 and the number itself

# Printing prime numbers between start and end
print(f"Prime Numbers between {start} and {end}:")
for num in range(start, end + 1):
    if is_prime(num):
        print(num, end=" ")
