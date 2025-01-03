# def square(num):
#     print(f"{num} Square is",num*num)  
    
#     if num<10:
#         square(num+1)         
#         return 
        
# square(1)



# Recursion Introduction
def display_squares(num):
    """
    Recursively prints the square of numbers starting from `num` 
    up to 8 (inclusive).
    """
    print(f"{num}^2 = {num*num}")  # Print the square of the number
    if num < 9:  # Recursive condition
        display_squares(num + 1)

# Call the function
print("Squares of numbers using recursion:")
display_squares(0)

# Recursion in Python

def countdown(n):
    """
    Recursively prints numbers from `n` down to 1.
    """
    if n == 0:  # Base case or control
        return 

    print(n)  # Print the current number
    countdown(n - 1)  # Recursive call

# Call the function
print("\nCountdown from 5 using recursion:")
countdown(5)

# Print numbers from 1 to 10 using recursion

def print_numbers(num):
    """
    Recursively prints numbers from `num` up to 10.
    """
    print(num, end=" ")  # Print the current number
    if num < 10:  # Recursive condition
        print_numbers(num + 1)

# Call the function
print("\n\nNumbers from 1 to 10 using recursion:")
print_numbers(1)
