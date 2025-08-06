# WAP to enter marks of 3 subjects from the user and store them in a dictionary.
# Start with an empty dictionary & add one by one. 
# Use subject name as key & marks as value.

# Start with an empty dictionary
marks = {}

# Take input for 3 subjects and store them
subject1 = input("Enter name of subject 1: ")
mark1 = float(input(f"Enter marks for {subject1}: "))
marks[subject1] = mark1

subject2 = input("Enter name of subject 2: ")
mark2 = float(input(f"Enter marks for {subject2}: "))
marks[subject2] = mark2

subject3 = input("Enter name of subject 3: ")
mark3 = float(input(f"Enter marks for {subject3}: "))
marks[subject3] = mark3

# Display the final dictionary
print("Marks Dictionary:", marks)
