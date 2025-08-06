#checking age for voting eligibility
#using if, elif, else statements

age=int(input("Enter Your age For Voting:"))

if age>18:
    print("You can Vote")
elif age==18:
    print("Become the Adult")
else:
    print("Sorry! You can Not Vote At The Time")