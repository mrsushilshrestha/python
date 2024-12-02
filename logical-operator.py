print("Enter the age:")
age=int(input())

print("\nEnter the Citizenship:")
citizenship = input()

#condition check
if(age>18 and citizenship=="nepali"):
    print("You can Vote")
else:
    print("sorry")