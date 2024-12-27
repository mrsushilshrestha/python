# Define a dictionary representing a student with various attributes
student = {
    "name": "Sushil",  # Student's first name
    "class": "Bachelor",  # Student's class level
    "subject": {  # Subjects and their corresponding marks
        "english": 90, 
        "math": 70
    },
    "age": 20  # Student's age
}

# Print the entire student dictionary
print(student)

# Access and print the marks of the English subject from the nested dictionary
print(student["subject"]["english"])

# Add a new key-value pair to the dictionary to store the student's surname
student["surname_name"] = "Shrestha"

# Print the updated dictionary with the newly added key-value pair
print(student)
