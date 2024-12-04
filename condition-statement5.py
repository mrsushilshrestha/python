#WAP to check the give input is multiple of 7 or Not

print("Enter Number You Want To Check:")
checkNumber = int(input())

if(checkNumber%7==0):
    print(f"The Number {checkNumber} is Multiple of 7 with ", int(checkNumber/7), "times" )
else:
    print(f"The Number {checkNumber} is Not Multiple Of Seven")
    
