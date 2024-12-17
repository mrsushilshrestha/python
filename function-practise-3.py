# calculate profit and loss using with parameter and with return Types

cp=float(input("Enter Cp: "))
sp=float(input("Enter Sp: "))

def calculate(i):
    Amount=calc+(i/100*cp)
    return Amount
if cp<sp:
    calc=sp-cp
    Amount=calculate(5)
    print("Profit: ",Amount)

else:
    calc=cp-sp
    Amount=calculate(20)
    print("Loss: ",Amount)
