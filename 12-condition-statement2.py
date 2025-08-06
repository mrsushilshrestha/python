#checking marks and assigning grades
#using if, elif, else statements
marks =input("Enter the marks of the student:")

if not marks.isdigit():
    print("INVALID! Please Enter Number Only")
    
else: 
    marks=int(marks) 
       
    if marks>=90 and marks<=100 :
        grade="A"
    elif marks<90 and marks>=80:
        grade="B"
    elif marks<80 and marks>=70:
        grade="C"
    elif marks<70 and marks>=32:
        grade="D"
    elif marks<32 and marks>=0:
        grade="F"
    else:
        grade="Invalid Marks"
    
    print("The Grade Obtain By Student is:", grade)
    
    # if grade=="Invalid Marks":
    #     print("Please Enter Marks Between 0 to 100")
    # else:
    #     print("The Grade Obtain By Student is:",grade)
    
    
# input()

