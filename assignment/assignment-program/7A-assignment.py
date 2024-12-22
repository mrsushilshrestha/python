# Write a program that counts the number of vowels (a, e, i, o, u) in a give string.	
# Example	Input:	"hello	world"		
# Example	Output:	Number	of vowels	=	3

strings =input("Enter the String:")
volvel="aeiouAEIOU"
count =0

for char in strings:
    if char in volvel:
        count+=1
print(count)