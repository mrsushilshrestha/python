def square(num):
    print(f"{num} Square is",num*num)  
    
    if num<10:
        square(num+1)         
        return 
        
square(1)