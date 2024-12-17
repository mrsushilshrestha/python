#Convert the date BS to AD and AD to BS 

def AD_to_BS(year,month,day):
    year+=57
    month-=3
    day -=15
    BS =print(year,"/",month,"/",day)
    return BS

def BS_to_AD(year,month,day):
    year-=57
    month+=3
    day-=15
    AD =print(year,"/",month,"/",day)
    return AD


display ="""ENTER THE OPTION...
1> AD to BS
2> BS to AD
"""
print(display)
option=int(input())

year =int(input("ENTER THE YEAR "))
month =int(input("ENTER THE MONTH "))
day = int(input("ENTER THE DAY "))

if(not year and month and day.isdigit ):
    print("Please Enter Digit Only!!!")

if option==1:
    AD_to_BS(year,month,day)
elif option==2:
    BS_to_AD(year,month,day)

