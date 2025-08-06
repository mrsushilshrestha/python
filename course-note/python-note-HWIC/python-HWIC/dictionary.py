# You are given a list of subjects for students. Assume one classroom is required for 1 subject. 
# How many classrooms are needed by all students.
# ”python”, “java”, “C++”, “python”, “javascript”,
# “java”, “python”, “java”, “C++”, “C”

total_subjects = ["python", "java", "C++", "python", "javascript","java", "python", "java", "C++", "C"]

subject = set(total_subjects)  # Using set to get unique subjects

print("Unique subjects:", subject)
print("Total number of classrooms needed:", len(subject))



