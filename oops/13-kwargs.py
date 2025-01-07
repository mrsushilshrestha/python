def display_info(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")
        

display_info(name="alice",age=30,locaion="New York")


def display(*arg):
    print(arg)


display("sushil","kathmandu",20)