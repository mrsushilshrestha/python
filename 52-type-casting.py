# Initial list with duplicate elements
list_with_duplicates = [1, 2, 3, 1, "sushil", "sushil", 1.22, 1.22]
print("All items in list",list_with_duplicates)

# Convert the list to a set to remove duplicates
unique_elements = set(list_with_duplicates)
print("Unique elements after conversion to set:", unique_elements)

# Convert the set back to a list
list_from_set = list(unique_elements)
print("List after conversion from set:", list_from_set)

# Print the type of the resulting list
print("Type of list_from_set:", type(list_from_set))