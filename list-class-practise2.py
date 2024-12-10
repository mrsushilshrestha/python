"""#WAP to take user input "first Name","mobile number , "address" and add it into list
list_first=[]
list_first.append(input("Enter the Name: "))
list_first.append(input("Phone Number: "))
list_first.append(input("Enter the address: "))

print(list_first)

"""
#WAP to take a input from the user and make different list for different user.
number=int(input("Enter the number of people: "))
i=1
list_third=[]

while i<=number:
    list_second=[]
    print(f"For user {i}")
    list_second.append(input(f"Enter the Name : "))
    list_second.append(input(f"Enter the Age: "))
    list_second.append(input(f"Enter the Address ")) 

    list_third.append(list_second)
    i+=1

print(list_third)





