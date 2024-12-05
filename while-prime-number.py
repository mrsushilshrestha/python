num=int(input())
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