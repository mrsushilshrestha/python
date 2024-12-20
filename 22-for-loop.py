# Demonstration of for loops in Python
#for i in range(star, stop,step or increase/decrease)

# Basic for loop: Print numbers from 0 to 10
print("Numbers from 0 to 10:")
for i in range(0, 11): 
    print(i)
print("\n")

# For loop with a step: Print numbers from 0 to 10, increasing by 2
print("Numbers from 0 to 10 with a step of 2:")
for i in range(0, 11, 2): 
    print(i)
print("\n")

# For loop with a negative step: Print numbers from 10 to 1 in descending order
print("Numbers from 10 to 1 in descending order:")
for i in range(10, 0, -1): 
    print(i)