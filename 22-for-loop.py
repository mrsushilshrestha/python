# Demonstration of for loops in Python
#for i in range(star, stop,step or increase/decrease)

# # Basic for loop: Print numbers from 1 to 100 using the range function
# print("Numbers from 1 to 100:")
# for i in range(0,100): 
#     print(i+1)
# print("\n")


# # Basic for loop: Print numbers from 100 to 1 using the range function
# print("Numbers from 100 to 1:")
# for i in range(100,0,-1): 
#     print(i)
# print("\n")


# Basic for loop: Print the multiplication table of a number n.
number = int(input("Enter the Number for multiplication: "))
for i in range(1,11): 
    print(f"{number} * {i} = {number * i}")
print("\n")

# # For loop with a step: Print numbers from 0 to 10, increasing by 2
# print("Numbers from 0 to 10 with a step of 2:")
# for i in range(0, 11, 2): 
#     print(i)
# print("\n")

# # For loop with a negative step: Print numbers from 10 to 1 in descending order
# print("Numbers from 10 to 1 in descending order:")
# for i in range(10, 0, -1): 
#     print(i)