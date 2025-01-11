# #example-1
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




#using decorator concept
# def make_preety(funcs):
#     def sub_function():
#         print("This is Sub Function.")
#         funcs()
        
#     return sub_function

# @make_preety
# def ordinary():
#     print("This is Ordinary Function")


# # object
# # obj =make_preety(ordinary)
# # obj()


# ordinary()




# example-2
# WAP to calculate two string number to integer using decorator
def modifier(func):
    def conversion(a,b):
        first= int(a)
        second=int(b)
        return func(first,second)
    
    return conversion


@modifier
def sum(a,b):
    print(a+b)
    

sum("4","95")
sum(4,10)
