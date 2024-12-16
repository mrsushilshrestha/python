#swapping Element in python

a=5
b=9
print(f"Before Swapping a={a} ,b={b}")

#swapping using temp variable
temp =a
a=b
b=temp
print(f"After Swapping a={a} , b={b}")


#swapping Without using temp variable
a,b =b,a
print(a,b)