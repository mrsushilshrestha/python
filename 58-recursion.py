#Recursion in Python

def display(n):
    if n==0:   #base case or control
        return 

    print(n)
    display(n-1)

display(5)
