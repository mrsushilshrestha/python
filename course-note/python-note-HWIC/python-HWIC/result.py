marks = input("Enter the marks obtained: ")

if marks.isdigit() and int(marks)<= 100 and int(marks) >= 0:
    marks = int(marks)
    if marks >= 90:
        print("Grade: A+")
    elif marks >= 80:
        print("Grade: A")
    elif marks >= 70:
        print("Grade: B+")
    elif marks >= 60:
        print("Grade: B")
    elif marks >= 50:
        print("Grade: C+")
    elif marks >= 40:
        print("Grade: C")
    elif marks >= 30:
        print("Grade: D")
    else:
        print("Grade: F")
else:
    print("Invalid input. Please enter a numeric value for marks.")