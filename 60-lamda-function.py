# The syntax for a lambda function (also called an anonymous function) in Python is:
#syntax:
#lambda arguments: expression

# -------Example------------------------------------------------------------
# Example 1: Single Argument
square = lambda x: x ** 2
print(square(5))  # Output: 25

# Example 2: Add Two numbers
add = lambda first_number,second_number:first_number+second_number
display=add(12,13)
print(display) # Output: 25

# Example 3: Multiple Arguments
add = lambda a, b: a + b
print(add(3, 7))  # Output: 10

# Example 4: Lambda in map()
nums = [1, 2, 3, 4]
squared_nums = list(map(lambda x: x ** 2, nums))
print(squared_nums)  # Output: [1, 4, 9, 16]

# Example 5: Lambda in filter()
nums = [1, 2, 3, 4, 5]
even_nums = list(filter(lambda x: x % 2 == 0, nums))
print(even_nums)  # Output: [2, 4]

# Example 6: Lambda in sorted()
points = [(2, 3), (1, 2), (4, 1)]
sorted_points = sorted(points, key=lambda x: x[1])
print(sorted_points)  # Output: [(4, 1), (1, 2), (2, 3)]