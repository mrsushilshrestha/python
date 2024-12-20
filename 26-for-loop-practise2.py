list_variable =[1,2,3,4,5,6,2,8,2]
number=int(input("Enter the Number for search: "))
idx=0
for i in list_variable:
    if(i==number):
        print(f"{i} Found index",idx,)
        continue
    else:
        print(f"{i} Seaching...")        
        idx+=1