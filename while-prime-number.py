#To find the Prime Number using While Loop 
num=int(input("Enter the Number to Know this number is Prime Or Composite Number"))
count=0
start=1
while start<=num:
    if num%start ==0:
        count=count+1 
    start=start+1  
  
if count <=2:
    print(f"{num} is prime number")
else:
    print(f"Composite Number {num}")