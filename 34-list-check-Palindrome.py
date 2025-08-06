#WAP to check the palindrome In python

# number = int(input("Enter the number: "))
# list1 = []

# for i in range(1, number + 1):
#      list1.append(input(f"Enter the {i} number: "))


list1 = [1,2,1]

list_copy=list1.copy()
list_copy.reverse()

if(list_copy==list1):
     print(f"This is palindrome{list_copy}")
else:
     print(f"This is Not Palindrome{list1}")