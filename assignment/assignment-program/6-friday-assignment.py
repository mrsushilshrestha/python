# Write a program that checks if a given word is a palindrome (reads the same forwards and backwards).
# Example Input: "madam"
# Example Output: "madam is a palindrome" Other words: racecar, level..

input_items =input("Enter the Items ")
length =len(input_items)
items_reverse=" "

for i in range(length-1,-1,-1):
    items_reverse +=input_items[i]

print(items_reverse)
if items_reverse == input_items:
    print("Palindrome")
else:
    print("Not palindrome")
