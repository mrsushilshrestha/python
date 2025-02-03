students = ["Sushil", "Shiva", "Tekraj", "Dibisha"]
scores = [95, 88, 76, 89]

# Using zip() and dictionary comprehension
student_scores = {student: score for student, score in zip(students, scores)}

print(student_scores)



# output
# {'Sushil': 95, 'Shiva': 88, 'Tekraj': 76, 'Dibisha': 89}
