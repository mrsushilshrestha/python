#create a class called Order which stores items & Its price.
#use Dunder function __gt__() to convert that:
# order1>order2 if price of order1>price of order2

class Order:
    def __init__(self,items,price):
        self.items=items
        self.price=price
    

    def __gt__(self,ord2):
        return self.price>ord2.price


oder1= Order("Apple",20)
oder2= Order("Banana",15)

print(oder1>oder2)
