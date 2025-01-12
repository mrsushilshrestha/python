# from calculator_decorator_pack import conversion, check_zero,negative ##for import

def conversion(fun):
    def inner(a,b):
        a=int(a)
        b=int(b)
        return fun(a,b)
    return inner


def check_zero(fun):
    def inner(a,b):
        if b==0:
            print(f"Divide By Zero{b} not allow !!!")
            return
        return fun(a,b)
    return inner


def negative(fun):
    def inner(a,b):
        if (a-b) <0:
            print("negative")
        return fun(a,b)
    return inner

class calculation:
    @conversion
    def sum(a,b):
        print(a+b)

    @conversion
    @negative 
    def sub(a,b):
        print(a-b)
        
    @conversion
    @check_zero
    def div(a,b):
        print(a/b)
        

    @conversion
    def mul(a,b):
        print(a*b)
    
        
def main():
    obj = calculation
    a= input("Enter the First Number: ")
    b= input("Enter the Second Number: ")
    operation=input("Enter the Operation: ")

    if operation=='+':
        obj.sum(a,b)
    elif operation=='-':
        obj.sub(a,b)
    elif operation=="*":
        obj.mul(a,b)
    elif operation=="/":
        obj.div(a,b)
    


                    
main()         
            