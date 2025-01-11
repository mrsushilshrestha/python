# -----------------return function as value------------------------------------------
# def outer(first_number):
#     def inner(second_number):
#         return  first_number+second_number
#     return inner


# add_first= outer(4)
# result = add_first(10)

# # print(result)
# print(result)


##example-2
# def sum(a,b):
#     return a+b

# def calculation(funs,a,b):
#     return funs(a,b)

# obj=calculation(sum,5,10)
# print(obj)

##example-3
# def greeting(name):
#     def hello():
#         return (f"Hello {name} !")
#     return hello


# obj =greeting("sushil")
# print(obj())


# #example-4
# def make_preety(funcs):
#     def sub_function():
#         print("This is Sub Function.")
#         funcs()
        
#     return sub_function

# def ordinary():
#     print("This is Ordinary Function")


# # object
# obj =make_preety(ordinary)
# obj()


