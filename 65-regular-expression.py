import re

pattern = r"^(?:\+977[-\s]?)?(9[78]\d{8}|0\d{1,2}[-\s]?\d{6,7})$"

# Test cases
numbers = [
    "+977-9841234567",  # Valid mobile number
    "9841234567",       # Valid mobile number
    "+977 9808765432",  # Valid mobile number
    "014411234",        # Valid landline number (Kathmandu)
    "021-512345",       # Valid landline number (other area)
    "987654321",        # Invalid number
    "12345678",         # Invalid number
]

for num in numbers:
    if re.match(pattern, num):
        print(f"{num} ✅ Valid")
    else:
        print(f"{num} ❌ Invalid")
