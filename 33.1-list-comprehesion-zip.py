keys = ['name', 'age', 'location']
values = ['Sushil', 21, 'Nepal']

# Using zip() and list comprehension to create a dictionary
result = {key: value for key, value in zip(keys, values)}
print(result)

# output:
# {'name': 'Sushil', 'age': 21, 'location': 'Nepal'}
