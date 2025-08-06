# Palindrome Check
# This code checks if the input string is a palindrome
# A palindrome reads the same backward as forward
#eg: "madam", "racecar","level","121", "12321" etc

values = input("Enter The Value To check the Palindrome: ")

if values== values[::-1]:
    print("The name is a palindrome.")
else:
    print("The name is not a palindrome.")