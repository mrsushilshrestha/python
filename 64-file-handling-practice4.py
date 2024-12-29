#WAP to find the odd and even number from the file(store in the  file)
with open ("Calculation.txt","r") as f:
    data =f.read()
    
    num=data.split(",")
    count=0
    for i in num:
        if int(i)%2==0:
            # print("Even")
            count+=1
        else:
        #     print("odd Number")
            pass
        
    print(f"There are Total {count} Even Numbers in File")
        