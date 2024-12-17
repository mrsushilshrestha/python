#WAP to take a input from the user and make different list for different user.
number=int(input("Enter the number of people: "))
i=1
list_third=[]

while i<=number:
    list_second=[] #Reset list_second for each user
    print(f"For user {i}")
    list_second.append(input(f"Enter the Name : "))
    list_second.append(input(f"Enter the Age: "))
    list_second.append(input(f"Enter the Address ")) 

    list_third.append(list_second)
    i+=1

print(list_third)