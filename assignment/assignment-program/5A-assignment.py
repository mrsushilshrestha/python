# Write a program that takes a string as input and prints the string in reverse order.
# Example Input: "Python" Example Output: "nohtyP

string_input =input("Enter the String:-")
string_input_length=len(string_input)

for i in range(string_input_length-1,-1,-1): #reverse String 
  print(string_input[i],end=(""))

