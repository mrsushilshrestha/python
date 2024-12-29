#recursion Introduction
# def display(num):
#     print(num*num)
#     if num<9:
#         display(num+1)
    
# display(0)
    

# # Recursion in Python
# def display(n):
#     if n==0:   #base case or control
#         return 

#     print(n)
#     display(n-1)

# display(5)

# print number 1 2 3 4 5 6 7 8 9 10  using recursiom
def recursion_function(num):
    print(num,end=" ")
    
    if num<10:
        recursion_function(num+1)

recursion_function(1)


