# list comprehension
# List comprehension offers a shorter syntax
#  when you want to create a new list based on the values of an existing list.

#syntax
# newlist = [expression for item in iterable if condition == True]

#using list comprehension add 100 to each data
data =[1,2,3,4,5,6]

my_add_data =[number+100 for number in data]  #list comprehension
print(my_add_data)

#wap to find odd even using list comprehension
data =[1,2,3,4,5,6]

even_data =[number for number in data if number%2==0]
print(even_data)