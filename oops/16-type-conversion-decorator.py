# example-2
# WAP to calculate two string number to integer using decorator
def conversion(func):
    def inner(a,b):
        first= int(a)
        second=int(b)
        return func(first,second)
    return inner

def check_zero(fun):
    def inner(a,b):
        if b==0:
            print("Not Division By Zero!!!")
            return
        return fun(a,b)
    return inner
        

@conversion
def sum(a,b):
    print(a+b)


@conversion    
@check_zero
def division(a,b):
    print(a/b)
    

sum("4","95") #string input
division("4",10)
