# WAP to count the number of students with the “A” grade in the following List.
# [”C”, “D”, “A”, “A”, “B”, “B”, “A”]
# Store the above values in a list & sort them from “A” to “D”.

# List of student grades
student_grade = ["C", "D", "A", "A", "B", "B", "A"]

#counting the number of students with "A" grade
print("The number of students with 'A' grade is:", student_grade.count("A"))

#sorting the list from "A" to "D"
student_grade.sort()
print(f"Sorted student grades: {student_grade}")
