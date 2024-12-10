#check the palindrome In python
list1=[1,2,3,1]



list_copy=list1.copy()
list_copy.reverse()

if(list_copy==list1):
     print(f"This is palindrome{list_copy}")
else:
     print(f"This is Not Palindrome{list1}")