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