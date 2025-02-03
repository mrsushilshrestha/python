# Day 54: Understanding *args in Python

def display(*arg):
    print(arg)

display("Sushil", "Kathmandu", 20)

def add_numbers(*numbers):
    total = sum(numbers)
    print(f"Sum: {total}")

add_numbers(10, 20, 30)

# Day 55: Understanding **kwargs in Python

def display_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

display_info(name="Alice", age=30, location="New York")

def greet(**kwargs):
    print(f"Hello {kwargs.get('name', 'Guest')}, welcome from {kwargs.get('location', 'Unknown')}!")

greet(name="Sushil", location="Nepal")
greet(name="Shiva")
