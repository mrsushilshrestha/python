import re

pattern = r"^(?:\+977[-\s]?)?(9[78]\d{8}|0\d{1,2}[-\s]?\d{6,7})$"

# Test cases
numbers = input("Enter the Number: ")

if re.match(pattern, numbers):
    print(f"{numbers} ✅ Valid")
else:
    print(f"{numbers} ❌ Invalid")
