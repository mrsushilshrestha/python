# Write a program that takes a sentence as	input	and	counts	the	number	of	words in it.						
# Example	Input:	"Python	is	fun"		
# Example
# Skill Shikshya	Output:	Number	of	words	=	3

#count string
name =input("Enter the element ")
stringlen =len(name)
space_count = name.count( " ")
total_string =stringlen-space_count
print(total_string)
