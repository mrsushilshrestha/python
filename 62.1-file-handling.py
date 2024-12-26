#WAP to make a system for computer shop to store computer data like,computer name
#brand, price,id generation and core

name=input("Enter the Name: ")
brand=input("Enter the brand: ")
price=input("Enter the Price: ")
id=input("Enter the Id: ")
core=input("Enter the Core: ")


with open("computer-shop.txt","a") as computer_obj:
    computer_obj.write(name+" ,")
    computer_obj.write(brand+" ,")
    computer_obj.write(price+", ")
    computer_obj.write(id+ " ,")
    computer_obj.write(core+ " ")


with open("computer-shop.txt","r") as computer_obj:
    file_read=computer_obj.read()
    print(file_read)

