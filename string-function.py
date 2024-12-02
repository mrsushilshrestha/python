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

#remove the whiteSpace
firstString ="     this is  BIT Student    "
print(firstString.strip())

#splite the String
skill_shikshya = "skillshikshya@gmail.com"

splite_data = skill_shikshya.split('@')
print(splite_data)

#Conver the letter in UpperCase
father_name ="this is my father name"
print(father_name.upper()) #upper convert the all letter of the string
print(father_name.capitalize()) #It capitalize the first string of the string
print(father_name.title()) #It capitalize the all the string of first letter

#find the stiring position
strIndex ="sushil shrestha"
print(strIndex.index("h"))
 
 #islower() is use for check any lowercase
print(strIndex.islower())

#center
print("Center")
print(len(strIndex))
print(strIndex.center(30,"*"))



""""
String Handing Function In Python
str.endswith()
str.capitalize()
str.replace()
str.find()
str.count()
str.strip() #remove whiteSpace
str.split() #splite string 
str.title() 
"""

#WAP to find occurance of '$' in a string 
str1 ="the Dollor $ price in Nepal in current time is $1 per dollor is about Rs.136"

findValue= str1.count("$")
print("The Position Of string $ in the above string is:", findValue)






