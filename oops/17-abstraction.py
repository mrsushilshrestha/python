#abstraction
#Hiding the implementation details of a class and only showing the essential features to the user.

class Car:
    def __init__(self):
        self.cluch=False
        self.bre =True
        self.accle =False
    
    def start(self):
        self.cluch=True
        self.bre=False
        self.accle=True
        print("Car is Running...")

        
obj = Car()
obj.start()

#encapsulation
# Wapping data and function into a single unit(object)


#create Account class with 2 attribute -balcance & account no.
#create method for debit ,credit & print balance


class Account:
    def __init__(self,balance,account):
        self.balance=balance
        self.account =account

    
    def credit(self,amount):
        self.balance+=amount
        print(f"{amount} was credited successfully!!!")
    
    def debit(self,amount):
        self.balance-=amount
        print(f"{amount} was debited successfully!!!")
    
    def print(self):
        print(f"Current Amount in your {self.account} account is : {self.balance}")
    


obj= Account(10000,123456)
obj.debit(2000)
obj.credit(20000)
obj.print()