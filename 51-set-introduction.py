# Set in Python
# Set: Mutable, Unordered

set_values1 = {"apple", "mango", "ball", "cat"}
set_values2 = {"dog", "rabbit", "apple", "mango", "graves"}

# Union: Combines all unique elements from both sets
set_result = set_values1.union(set_values2)
print("Union:", set_result)

# Intersection: Returns only the common elements between both sets
set_result = set_values1.intersection(set_values2)
print("Intersection:", set_result)

# Difference: Returns elements present in set_values1 but not in set_values2
set_result = set_values1.difference(set_values2)
print("Difference:", set_result)
