#list compression

#using list compression add 100 to each data
data =[1,2,3,4,5,6]

my_add_data =[number+100 for number in data]  #list compression 
print(my_add_data)

#wap to find odd even using list_compression
data =[1,2,3,4,5,6]

even_data =[number for number in data if number%2==0]
print(even_data)