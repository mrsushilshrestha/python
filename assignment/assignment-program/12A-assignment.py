# Write a Python program that takes a list of students' names and their corresponding marks in a subject, stores them in a dictionary, and then calculates and prints the average mark.
# Example Input: ['Alice', 'Bob', 'Charlie'] and [85, 92, 78]
# Example Output: {'Alice': 85, 'Bob': 92, 'Charlie': 78} and Average = 85

student_name=[]
student_mark=[]

for i in range(3):
    name=input("Enter the name: ")
    mark =int(input("Enter the mark: "))

    student_name.append(name)
    student_mark.append(mark)

# student_length=len(student_name)
# print(student_length)

total_mark=sum(student_mark)
average_mark= total_mark/len(student_name)
print(f"The average Mark of {len(student_name)} is ",average_mark)