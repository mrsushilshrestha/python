number=[1,2,4,3]
number_first=[1,2,3]
number_second =[2,3,4]

#To find the square of the number using the map function with lambda
result= list(map(lambda a:a**2,number))
print(result)

#To find the cube of the number using the map function with lambda
result= list(map(lambda a:a**3,number))
print(result)

#Add the Two list using the map function
result= list(map(lambda x,y:x+y,number_first,number_second))
print(result)

