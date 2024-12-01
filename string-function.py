str ="i am studing python from apna COllege"

print(str.endswith("ege"))   #returns true of string ends with substr
print(str.endswith("apna"))

print(str.capitalize()) #capitalize first string

#replace old string to new string
print(str.replace("a" ,"O")) #str.replace("old-string, "new-replace-string)

#to find string position in first
print(str.find("o")) #return 1st index of 1st occurance

#count the string from specifice string
print(str.count("am")) #count the occurance of substr
print(str.count("a"))


""""
String Handing Function In Python
str.endswith()
str.capitalize()
str.replace()
str.find()
str.count()

"""

#WAP to find occurance of '$' in a string 

str1 ="the Dollor $ price in Nepal in current time is $1 per dollor is about Rs.136"

findValue= str1.count("$")
print("The Position Of string $ in the above string is:", findValue)






