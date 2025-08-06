#WAP to check the give input is multiple of 7 or Not

checkNumber = int(input("Enter the Number You Want To Check Multiple of 7:"))

if checkNumber%7==0:
    print(f"The Number {checkNumber} is Multiple of 7 with {int(checkNumber/7)} times" )
else:
    print(f"The Number {checkNumber} is Not Multiple Of Seven")
    
