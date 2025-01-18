class BankAccount:
    def __init__(self, account_number, account_holder, balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} was successfully deposited into your account!!")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{amount} was successfully withdrawn from your account!")
        else:
            print("Insufficient funds.")

    def display_balance(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Account Number: {self.account_number}")
        print(f"Current Balance: {self.balance}")


account = BankAccount(123456, "Sushil Shrestha", 10000)

account.deposit(5000)

account.withdraw(6000)

account.withdraw(15000)

# account.display_balance()
