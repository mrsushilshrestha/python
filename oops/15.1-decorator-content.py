# Day 41: Introduction to Decorators in Python
# Decorators are powerful tools in Python used to modify or enhance the behavior of functions or methods.

# Example 1: Returning Functions as Values

def outer(first_number):
    def inner(second_number):
        return first_number + second_number
    return inner

add_first = outer(4)
result = add_first(10)
print(result)

# Example 2: Passing Functions as Arguments

def sum(a, b):
    return a + b

def calculation(func, a, b):
    return func(a, b)

obj = calculation(sum, 5, 10)
print(obj)

# Day 42: Closures
# Closures are functions that retain access to variables from their containing scopes even after those scopes have finished execution.

# Example 1: Greeting with Closure

def greeting(name):
    def hello():
        return f"Hello {name}!"
    return hello

obj = greeting("Sushil")
print(obj())

# Example 2: Adding Behavior to a Function

def make_pretty(func):
    def sub_function():
        print("This is a Sub Function.")
        func()
    return sub_function

def ordinary():
    print("This is an Ordinary Function.")

obj = make_pretty(ordinary)
obj()

# Day 43: Introducing Decorator Syntax

# Example 1: Using Decorators

def make_pretty(func):
    def sub_function():
        print("This is a Sub Function.")
        func()
    return sub_function

@make_pretty
def ordinary():
    print("This is an Ordinary Function.")

ordinary()

# Example 2: Calculator with Decorators

def conversion(func):
    def inner(a, b):
        first = int(a)
        second = int(b)
        return func(first, second)
    return inner

def check_zero(func):
    def inner(a, b):
        if b == 0:
            print("Cannot Divide by Zero!")
            return
        return func(a, b)
    return inner

@conversion
def sum(a, b):
    print(a + b)

@conversion
@check_zero
def division(a, b):
    print(a / b)

sum("4", "95")
division("4", "0")

# Day 44: Stacking Multiple Decorators

# Example: Combining Multiple Functionalities

def conversion(func):
    def inner(a, b):
        a = int(a)
        b = int(b)
        return func(a, b)
    return inner

def check_zero(func):
    def inner(a, b):
        if b == 0:
            print("Cannot Divide by Zero!")
            return
        return func(a, b)
    return inner

def negative(func):
    def inner(a, b):
        if (a - b) < 0:
            print("Negative Result")
        return func(a, b)
    return inner

@conversion
@negative
def subtract(a, b):
    print(a - b)

subtract("4", "10")

# Day 45: Decorators with Classes

class Calculation:
    @conversion
    def sum(a, b):
        print(a + b)

    @conversion
    @negative
    def subtract(a, b):
        print(a - b)

    @conversion
    @check_zero
    def divide(a, b):
        print(a / b)

    @conversion
    def multiply(a, b):
        print(a * b)

def main():
    obj = Calculation
    a = input("Enter the First Number: ")
    b = input("Enter the Second Number: ")
    operation = input("Enter the Operation (+, -, *, /): ")

    if operation == '+':
        obj.sum(a, b)
    elif operation == '-':
        obj.subtract(a, b)
    elif operation == '*':
        obj.multiply(a, b)
    elif operation == '/':
        obj.divide(a, b)

main()

# Day 46: Real-World Use Cases of Decorators

# Example 1: Logging

def log(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with {args} and {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@log
def say_hello(name):
    print(f"Hello, {name}!")

say_hello("Shiva")

# Example 2: Timing

import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution Time: {end_time - start_time:.5f} seconds")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(2)
    print("Finished!")

slow_function()

# Day 47: Creating a Custom Decorator Library

# Example 1: Modular Decorators

def conversion(func):
    def inner(a, b):
        a = int(a)
        b = int(b)
        return func(a, b)
    return inner

def check_positive(func):
    def inner(a, b):
        if a < 0 or b < 0:
            print("Negative numbers are not allowed.")
            return
        return func(a, b)
    return inner

@conversion
@check_positive
def add(a, b):
    print(a + b)

add("5", "3")
add("-1", "3")

# Day 48: Advanced Features in Decorators

# Example: Preserving Function Metadata

from functools import wraps

def log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with {args} and {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@log
def multiply(a, b):
    """Multiplies two numbers."""
    return a * b

print(multiply(2, 3))
print(multiply.__name__)
print(multiply.__doc__)

# Day 49: Best Practices and Final Examples

# Example 1: Chaining Decorators

def upper_case(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

def exclaim(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result + "!"
    return wrapper

@upper_case
@exclaim
def greet(name):
    return f"hello, {name}"

print(greet("Dibisha"))

# Example 2: Debugging Decorators

def debug(func):
    def wrapper(*args, **kwargs):
        print(f"Function {func.__name__} called with arguments {args} and {kwargs}")
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} returned {result}")
        return result
    return wrapper

@debug
def power(base, exponent):
    return base ** exponent

print(power(2, 3))
