print("Enter the marks of the student:")
marks =input()

if not marks.isdigit():
    print("INVALID! Please Enter Number Only")
    
else: 
    marks=int(marks) 
       
    if(marks>=90):
        grade="A"
    elif(marks<90 and marks>=80 ):
        grade="B"
    elif(marks<80 and marks>=70):
        grade="C"
    elif(marks<70 and marks>=32):
        grade="D"
    else:
        grade="F"
    
    print("The Grade Obtain By Student is:",grade)
