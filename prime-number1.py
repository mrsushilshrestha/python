number =int(input("Enter the Number to check prime:"))
count =0
start =1

while start<number:
    if number%start ==0:
        count=count+1
    start=start+1
        
        
if(count>2):
        print(f"This Number is Composite Number{number}")
else:
        print(f"The Number is Prime Number{number}")   